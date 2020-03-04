# -*- coding: utf-8 -*-
"""
Parse an event record
:see: https://docs.microsoft.com/fr-fr/windows/desktop/api/evntcons/ns-evntcons-_event_record
"""

from construct import Struct, Int16ul, Enum, Int32ul, Int64ul, FlagsEnum, Int8ul, Bytes, Aligned, RepeatUntil, Computed, \
    AlignedStruct, If

from etl.parsers.etw.core import Etw, build_etw, Guid as EtwGuid
from etl.parsers.tracelogging import build_tracelogging, TraceLogging
from etl.utils import Guid
from etl.wmi import wmi_trace_marker

EventHeaderType = Enum(
    Int8ul,
    EVENT_HEADER_EVENT32=0x12,
    EVENT_HEADER_EVENT64=0x13
)

EventHeaderFlag = FlagsEnum(
    Int16ul,
    EVENT_HEADER_FLAG_EXTENDED_INFO=0x0001,
    EVENT_HEADER_FLAG_PRIVATE_SESSION=0x0002,
    EVENT_HEADER_FLAG_STRING_ONLY=0x0004,
    EVENT_HEADER_FLAG_TRACE_MESSAGE=0x0008,
    EVENT_HEADER_FLAG_NO_CPUTIME=0x0010,
    EVENT_HEADER_FLAG_32_BIT_HEADER=0x0020,
    EVENT_HEADER_FLAG_64_BIT_HEADER=0x0040,
    EVENT_HEADER_FLAG_CLASSIC_HEADER=0x0100,
    EVENT_HEADER_FLAG_PROCESSOR_INDEX=0x0200
)

EventHeaderPropertyFlag = FlagsEnum(
    Int16ul,
    EVENT_HEADER_PROPERTY_XML=0x0001,
    EVENT_HEADER_PROPERTY_FORWARDED_XML=0x0002,
    EVENT_HEADER_PROPERTY_LEGACY_EVENTLOG=0x0004,
    EVENT_HEADER_PROPERTY_RELOGGABLE=0x0008
)

EventDescriptor = Struct(
    "Id" / Int16ul,
    "Version" / Int8ul,
    "Channel" / Int8ul,
    "Level" / Int8ul,
    "Opcode" / Int8ul,
    "Task" / Int16ul,
    "Keyword" / Int64ul
)

EventHeader = Struct(
    "marker" / wmi_trace_marker(EventHeaderType),
    "flags" / EventHeaderFlag,
    "event_property" / EventHeaderPropertyFlag,
    "thread_id" / Int32ul,
    "process_id" / Int32ul,
    "timestamp" / Int64ul,
    "provider_id" / Guid,
    "event_descriptor" / EventDescriptor,
    "processor_time" / Int64ul,
    "activity_id" / Guid
)

EventHeaderExtendedDataItem = Struct(
    "reserved1" / Int16ul,
    "ext_type" / Int16ul,
    "reserved2" / Int16ul,
    "data_size" / Int16ul,
    "data_item" / Bytes(lambda this: this.data_size)
)

EventRecord = AlignedStruct(8,
    "mark1" / Computed(lambda this: this._io.tell()),
    "event_header" / EventHeader,
    "extended_data" / If(lambda this: this.event_header.flags.EVENT_HEADER_FLAG_EXTENDED_INFO, RepeatUntil(
        lambda el, lst, this: not lst[-1].reserved2 & 0x1,
        Aligned(8, EventHeaderExtendedDataItem)
    )),
    "mark2" / Computed(lambda this: this._io.tell()),
    "user_data" / Bytes(lambda this: this.event_header.marker.version - (this.mark2 - this.mark1))
)


class Event:
    """
    This is a python wrapper around construct struct to access interesting fields
    """
    def __init__(self, source):
        self.source = source

    def get_process_id(self):
        """
        Return the process id of issuer
        :return: process id of issuer
        """
        return self.source.event_header.process_id

    def get_thread_id(self):
        """
        Return the thread id of issuer
        :return: thread id of issuer
        """
        return self.source.event_header.thread_id

    def get_timestamp(self) -> int:
        """
        :return: Timestamp associated with this event
        """
        return self.source.event_header.timestamp

    def parse_etw(self) -> Etw:
        """
        Try to parse user data with known etw format (if it's an ETW log)
        :return: If known build associate Etw class
        :raise: GuidNotFound, EventIdNotFound, EtwVersionNotFound
        """
        guid = EtwGuid(self.source.event_header.provider_id.data1, self.source.event_header.provider_id.data2,
                    self.source.event_header.provider_id.data3, self.source.event_header.provider_id.data4)
        event_id = self.source.event_header.event_descriptor.Id
        version = self.source.event_header.event_descriptor.Version
        user_data = self.source.user_data
        return build_etw(guid, event_id, version, user_data)

    def parse_tracelogging(self) -> TraceLogging:
        """
        Try to parse a tracelogging event
        """
        return build_tracelogging(self.source)
