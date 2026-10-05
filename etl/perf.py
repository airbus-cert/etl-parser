# -*- coding: utf-8 -*-

"""
Use as MOF container
It use by kernel logger to send event but more concise than in system trace format
But add timestamp of the event
This an event driven log but without some of meta infos
"""
from datetime import datetime, timezone, timedelta

from construct import Struct, Enum, Int64ul, Bytes, Int8ul, Container

from etl.parsers.kernel.core import Mof, build_mof
from etl.wmi import WmiTracePacket, wmi_trace_marker

PerfInfoTraceMarker = Enum(
    Int8ul,
    PERFINFO_TRACE_MARKER_32=0x10,
    PERFINFO_TRACE_MARKER_64=0x11
)

PerfInfoTraceRecord = Struct(
    "marker" / wmi_trace_marker(PerfInfoTraceMarker),
    "header" / WmiTracePacket,
    "timestamp" / Int64ul,
    "mof_data" / Bytes(lambda this: this.header.size - 16)
)


class PerfInfo:
    """
    A PerfInfo log from Windows Kernel
    """
    def __init__(self, source: Container):
        self.source = source

    def get_timestamp(self, boot_time: int) -> str:
        """
        Return the ISO-formatted timestamp of the PerfInfo record. The integer value stored in the PerfInfo record
        structure is the number of 100-nanosecond intervals since the last boot. This is why the machine's boot time is
        needed to calculate the Event's actual timestamp.
        :param: boot_time: the machine's boot time in FILETIME integer format
        :return: ISO-formatted timestamp associated with this event.
        """
        return (
                datetime(1601, 1, 1, tzinfo=timezone.utc)
                + timedelta(microseconds=(boot_time + self.source.timestamp)/10)
        ).isoformat(timespec="microseconds")

    def get_mof(self) -> Mof:
        """
        This function try to build mof structure for PerfInfo
        MOF structure is a common way to send infos from kernel
        :return:
        """
        return build_mof(self.source.header.group, self.source.marker.version, self.source.header.type, self.source.mof_data)

