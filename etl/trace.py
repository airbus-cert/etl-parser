# -*- coding: utf-8 -*-
"""
Parse an event trace record
:see: https://www.geoffchappell.com/studies/windows/km/ntoskrnl/api/etw/tracelog/event_trace_header.htm

Actually there is no infos about this logs. It seems to come from kernel.
"""

from construct import Struct, Int16ul, Enum, Int32ul, Int64ul, Int8ul, Bytes, Computed, AlignedStruct, Container
from etl.utils import Guid
from etl.wmi import wmi_trace_marker

"""
Marker use to determine if it's an event trace
"""
TraceHeaderType = Enum(
    Int8ul,
    TRACE_HEADER_TYPE_FULL_HEADER32=0x0A,
    TRACE_HEADER_TYPE_FULL_HEADER64=0x14
)

"""
Basic level trace meta infos
"""
TraceClass = Struct(
    "type" / Int8ul,
    "level" / Int8ul,
    "version" / Int16ul
)

"""
Header of the event trace
Contain interesting sender infos like process id thread id and the GUID
It's the base of ETW trace
"""
TraceHeader = Struct(
    "marker" / wmi_trace_marker(TraceHeaderType),
    "class" / TraceClass,
    "thread_id" / Int32ul,
    "process_id" / Int32ul,
    "timestamp" / Int64ul,
    "guid" / Guid,
    "processor_time" / Int64ul
)

"""
A Trace record with header and body
Actually version field of header is used to record trace size
"""
TraceRecord = AlignedStruct(8,
    "mark1" / Computed(lambda this: this._io.tell()),
    "event_header" / TraceHeader,
    "mark2" / Computed(lambda this: this._io.tell()),
    "user_data" / Bytes(lambda this: this.event_header.marker.version - (this.mark2 - this.mark1))
                            )


class Trace:
    """
    This is a python wrapper around construct struct to access interesting fields
    """
    def __init__(self, source: Container):
        """
        :param source Container: The EventTraceRecord Container once it's parsed
        """
        self.source = source

    def get_process_id(self) -> int:
        """
        Return the process id of issuer
        :return: process id of issuer
        """
        return self.source.event_header.process_id

    def get_thread_id(self) -> int:
        """
        Return the thread id of issuer
        :return: thread id of issuer
        """
        return self.source.event_header.thread_id

