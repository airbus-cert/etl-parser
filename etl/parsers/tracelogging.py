# -*- coding: utf-8 -*-

"""
Trace logging API is a DEV API offer by microsoft to exploit ETW without
all stuff around manifest, and include the message scheme directly into event.

It's a beautiful C Macro based API
"""

import struct
from enum import Enum
from io import BytesIO

from construct import Int16ul, Int8ul, CString, If, GreedyRange, LazyBound, Struct
from etl.error import TlMetaDataNotFound, TlUnhandledTag
from etl.utils import Guid, SystemTime


class TagIn(Enum):
    NULL = 0
    UNICODESTRING = 1
    ANSISTRING = 2
    INT8 = 3
    UINT8 = 4
    INT16 = 5
    UINT16 = 6
    INT32 = 7
    UINT32 = 8
    INT64 = 9
    UINT64 = 10
    FLOAT = 11
    DOUBLE = 12
    BOOL32 = 13
    BINARY = 14
    GUID = 15
    POINTER_unsupported = 16
    FILETIME = 17
    SYSTEMTIME = 18
    SID = 19
    HEXINT32 = 20
    HEXINT64 = 21
    COUNTEDSTRING = 22
    COUNTEDANSISTRING = 23
    STRUCT = 24
    COUNTEDBINARY = 25

    CCOUNT = 32
    VCCOUNT = 64
    CHAIN = 128


TlMetaDataField = Struct(
    "name" / CString("ascii"),
    "tag_in" / Int8ul,
    "tag_out" / If(lambda this: this.tag_in & TagIn.CHAIN.value, LazyBound(lambda: Int8ul))
)

TlMetaData = Struct(
    "size" / Int16ul,
    "tag" / Int8ul,
    "name" / CString("ascii"),
    "fields" / GreedyRange(TlMetaDataField)
)


def build_tracelogging(event):
    """
    Build tracelogging based on the source event
    Check if event have an extended
    :param event: event that encompass Tracelogging data
    """
    if event.extended_data is not None:
        for extended_data in event.extended_data:
            if extended_data.ext_type == 11:
                return TraceLogging().load(extended_data.data_item, event.user_data)

    raise TlMetaDataNotFound()


def read_field(stream, tag):
    """
    Read a trace logging field in accordance to the tag present into scheme
    :param stream: current stream
    :param tag: tag present into extended data of the event
    """
    if tag & 0x1f == TagIn.UNICODESTRING.value:
        current = []
        while len(current) == 0 or current[-1] != b"\x00\x00":
            current.append(stream.read_exact(2))
        # Encode in utf16 and ignore last null byte
        return b"".join(current).decode("utf-16le")[:-1]
    elif tag & 0x1f == TagIn.ANSISTRING.value:
        current = []
        while len(current) == 0 or current[-1] != b"\x00":
            current.append(stream.read_exact(1))
        # Encode in ascii and ignore last null byte
        return b"".join(current).decode("ascii")[:-1]

    elif tag & 0x1f == TagIn.INT8.value:
        return struct.unpack("b", stream.read_exact(1))[0]
    elif tag & 0x1f == TagIn.UINT8.value:
        return struct.unpack("B", stream.read_exact(1))[0]
    elif tag & 0x1f == TagIn.INT16.value:
        return struct.unpack("h", stream.read_exact(2))[0]
    elif tag & 0x1f == TagIn.UINT16.value:
        return struct.unpack("H", stream.read_exact(2))[0]
    elif tag & 0x1f == TagIn.INT32.value:
        return struct.unpack("i", stream.read_exact(4))[0]
    elif tag & 0x1f == TagIn.UINT32.value:
        return struct.unpack("I", stream.read_exact(4))[0]
    elif tag & 0x1f == TagIn.HEXINT32.value:
        return struct.unpack("I", stream.read_exact(4))[0]
    elif tag & 0x1f == TagIn.INT64.value:
        return struct.unpack("q", stream.read_exact(8))[0]
    elif tag & 0x1f == TagIn.UINT64.value:
        return struct.unpack("Q", stream.read_exact(8))[0]
    elif tag & 0x1f == TagIn.HEXINT32.value:
        return struct.unpack("Q", stream.read_exact(8))[0]
    elif tag & 0x1f == TagIn.FLOAT.value:
        return struct.unpack("f", stream.read_exact(4))[0]
    elif tag & 0x1f == TagIn.DOUBLE.value:
        return struct.unpack("d", stream.read_exact(8))[0]
    elif tag & 0x1f == TagIn.BOOL32.value:
        return bool(struct.unpack("i", stream.read_exact(4))[0])
    elif tag & 0x1f == TagIn.BINARY.value:
        return read_array_field(stream, TagIn.UINT8.value)
    elif tag & 0x1f == TagIn.GUID.value:
        return Guid.parse(stream.read_exact(16))
    elif tag & 0x1f == TagIn.SYSTEMTIME.value:
        return SystemTime.parse(stream.read_exact(16))
    else:
        raise TlUnhandledTag(tag)


def read_array_field(stream, tag):
    """
    Read array field that use the first 2 bytes for size
    :param stream: current stream
    :param tag: tag present into extended data of the event
    """
    nb_element = struct.unpack("H", stream.read(2))[0]
    result = []
    for _ in range(0, nb_element):
        result.append(read_field(stream, tag))

    return result


class BytesIORaise(BytesIO):
    def read_exact(self, size):
        buffer = self.read(size)
        if size != 0 and len(buffer) == 0:
            raise EOFError("no more data in stream")
        return buffer


class TraceLogging(dict):
    """
    This class is a TraceLogging parser
    It may be partial because TraceLogging format
    is not documented
    It's work like a dict
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.scheme = None

    def load(self, scheme, user_data):
        """
        Load this dict struct from the event
        :param scheme: data present into extended data
        :param user_data: data present into the event
        """
        self.scheme = TlMetaData.parse(scheme)

        stream = BytesIORaise(user_data)
        for field in self.scheme.fields:
            if field.tag_in & TagIn.CCOUNT.value or field.tag_in & TagIn.VCCOUNT.value:
                self[field.name] = read_array_field(stream, field.tag_in)
            else:
                self[field.name] = read_field(stream, field.tag_in)
        return self

    def get_name(self):
        """
        Name of the tracelogging provider
        :return: name of the tracelogging provider
        """
        return self.scheme.name
