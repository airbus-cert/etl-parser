# -*- coding: utf-8 -*-

"""
System header for all WMI trace messages

see: https://www.geoffchappell.com/studies/windows/km/ntoskrnl/api/etw/tracelog/system_trace_header.htm?tx=25

Parse the system trace header
:see: https://www.geoffchappell.com/studies/windows/km/ntoskrnl/api/etw/tracelog/trace_logfile_header.htm

This message is always present in the first chunk of every ETL file

It often use as a mof data container for the kernel logger
It have a lot of metadata (ProcessID ThreadID etc...) in compare to Perf message
"""
from construct import Struct, Computed, Int32ul, Int64ul, If, LazyBound, Bytes, Enum, Int8ul, Container

from etl.parsers.kernel.core import Mof, build_mof
from etl.wmi import wmi_trace_marker, WmiTracePacket

"""
Marker use by the parser to determiner if current trace is a system trace
"""
SystemTraceMarker = Enum(
    Int8ul,
    SYSTEM_TRACE_MARKER_32=0x01,
    SYSTEM_TRACE_MARKER_64=0x02,
    COMPACT_TRACE_MARKER_32=0x03,
    COMPACT_TRACE_MARKER_64=0x04,
)

SystemTraceHeader = Struct(
    "start_mark" / Computed(lambda this: this._io.tell()),
    "marker" / wmi_trace_marker(SystemTraceMarker),
    "header" / WmiTracePacket,
    "thread_id" / Int32ul,
    "process_id" / Int32ul,
    "system_time" / Int64ul,
    "kernel_time" / If(lambda this: this.marker.type.enum in [SystemTraceMarker.SYSTEM_TRACE_MARKER_32, SystemTraceMarker.SYSTEM_TRACE_MARKER_64], LazyBound(lambda: Int32ul)),
    "user_time" / If(lambda this: this.marker.type.enum in [SystemTraceMarker.SYSTEM_TRACE_MARKER_32, SystemTraceMarker.SYSTEM_TRACE_MARKER_64], LazyBound(lambda: Int32ul)),
    "sizeof" / Computed(lambda this: this._io.tell() - this.start_mark)
)


SystemTraceRecord = Struct(
    "system_header" / SystemTraceHeader,
    "mof_data" / Bytes(lambda this: this.system_header.header.size - this.system_header.sizeof)
)


class System:
    """
    A System log from Windows Kernel
    """
    def __init__(self, source: Container):
        """
        :param source: SystemTrace
        """
        self.source = source

    def get_process_id(self) -> int:
        """
        :return: Source Process Id of the event
        """
        return self.source.system_header.process_id

    def get_thread_id(self) -> int:
        """
        :return: Source thread id of the event
        """
        return self.source.system_header.thread_id

    def get_mof(self) -> Mof:
        """
        This function try to build mof structure for SystemInfo container
        MOF structure is a common way to send infos from kernel
        :return: Mof structure
        """
        return build_mof(self.source.system_header.header.group, self.source.system_header.marker.version, self.source.system_header.header.type, self.source.mof_data)
