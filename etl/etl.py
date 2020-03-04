# -*- coding: utf-8 -*-
"""
This file parse ETL file
It's directly inspired from :
:see: https://www.geoffchappell.com/studies/windows/km/ntoskrnl/api/etw/tracelog/wmi_buffer_header.htm
"""
from abc import ABCMeta, abstractmethod
from typing import List

from construct import Struct, Bytes, CheckError, Aligned, Select, GreedyRange, Container, Computed, RepeatUntil

from etl.error import InvalidEtlFileHeader
from etl.wintrace import WinTrace, WinTraceRecord
from etl.event import EventRecord, Event
from etl.parsers.kernel.core import Mof
from etl.parsers.kernel.header import EventTraceHeader, EventTrace_V0_Header
from etl.perf import PerfInfoTraceRecord, PerfInfo
from etl.system import SystemTraceRecord, System
from etl.trace import Trace, TraceRecord
from etl.wmi import WmiBufferHeader

EtlChunk = Struct(
    "header" / WmiBufferHeader,
    "payload" / Bytes(lambda this: this.header.wnode.saved_offset - WmiBufferHeader.sizeof()),
    "padding" / Bytes(lambda this: this.header.wnode.buffer_size - this.header.wnode.saved_offset)
)


# An ETL file is structured by ETL chunks until the end
EtlLogFile = GreedyRange(EtlChunk)

# This is a common way to select any type of chunks
# We add name selecting as computed to handle typing during parsing
Chunk = Aligned(8,
    Select(
        Struct(
            "type" / Computed("PerfInfoTraceRecord"),
            "value" / PerfInfoTraceRecord
        ),
        Struct(
            "type" / Computed("EventRecord"),
            "value" / EventRecord
        ),
        Struct(
            "type" / Computed("TraceRecord"),
            "value" / TraceRecord
        ),
        Struct(
            "type" / Computed("SystemTraceRecord"),
            "value" / SystemTraceRecord
        ),
        Struct(
            "type" / Computed("WinTraceRecord"),
            "value" / WinTraceRecord
        )
    )
)

ChunkParser = RepeatUntil(lambda x, lst, ctx: len(x._io.getbuffer()) == x._io.tell(), Chunk)


class IEtlFileObserver(metaclass=ABCMeta):
    """
    This is etl file observer
    Parse sequentially an etl file and commit event when found a particular event
    """
    @abstractmethod
    def on_event_record(self, event: Event):
        """
        Raise when an event record is parsed
        Mostly use by ETW and tracelogging
        If you search classic provider you are at the correct place
        :param event: the event record
        """

    @abstractmethod
    def on_trace_record(self, event: Trace):
        """
        Raise when an event trace record is parsed (older than event trace)
        Never find some parser for this kind of event ...
        :param event: the event record
        """

    @abstractmethod
    def on_perfinfo_trace(self, obj: PerfInfo):
        """
        Raise when a wmi perfinfo trace is parsed
        Mostly use as mof container
        If you want to parse some kernel log you are at the correct place
        You can use system trace too
        """

    @abstractmethod
    def on_system_trace(self, obj: SystemTraceRecord):
        """
        Raise when an unknown system trace is parsed
        Mostly use as mof container
        If you want to parse some kernel log you are at the correct place
        You can use system trace too
        :return:
        """

    @abstractmethod
    def on_win_trace(self, obj: WinTrace):
        """
        Raise when an unknown ETW trace is parsed
        Mostly use as ETW container
        This is not for common ETW message, if you want to parse common ETW see on_event_record
        :return:
        """


class EtlFile:
    """
    This is the main class for reading an ETL file
    The parse function will traverse all ETL chunks
    and call appropriate function depends on node type
    """
    def __init__(self, header: Mof, chunks: List[Container]):
        """
        :param header System: This is the first chunk of ETL file, wich include some meta infos about file creation
        :param chunks: List of all chunk (not all event)
        """
        self.header = header
        self.chunks = chunks

    def parse(self, observer: IEtlFileObserver):
        """
        Parse the ETL file
        :param observer IEtlFileObserver: observer pattern
        """
        actions = {
            "EventRecord": lambda obj: observer.on_event_record(Event(obj)),
            "TraceRecord": lambda obj: observer.on_trace_record(Trace(obj)),
            "SystemTraceRecord": lambda obj: observer.on_system_trace(System(obj)),
            "PerfInfoTraceRecord": lambda obj: observer.on_perfinfo_trace(PerfInfo(obj)),
            "WinTraceRecord": lambda obj: observer.on_win_trace(WinTrace(obj))
        }
        for chunk in self.chunks:
            for event in ChunkParser.parse(chunk.payload):
                actions[event.type](event.value)

    def get_header(self) -> Mof:
        """
        :return: the event trace header
        """
        return self.header


def build_from_stream(stream: bytes) -> EtlFile:
    """
    Parse ETL file format stream
    :param stream: a bytes like object that encompass raw data
    :return: EtlFile object
    """
    chunks = EtlLogFile.parse(stream)
    # first chunk must be Wmi Log Type header
    try:
        event_header_chunk = ChunkParser.parse(chunks[0].payload)
        if event_header_chunk[0].type != "SystemTraceRecord":
            raise InvalidEtlFileHeader()
        mof = System(event_header_chunk[0].value).get_mof()
        if not (isinstance(mof, EventTraceHeader) or isinstance(mof, EventTrace_V0_Header)):
            raise InvalidEtlFileHeader()
    except CheckError as e:
        raise InvalidEtlFileHeader() from e

    return EtlFile(mof, chunks[1:])
