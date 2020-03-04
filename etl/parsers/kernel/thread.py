# -*- coding: utf-8 -*-
from construct import Struct, Int32ul, Int64ul, Byte

from etl.parsers.kernel.core import declare, Mof
from etl.wmi import EventTraceGroup


@declare(group=EventTraceGroup.EVENT_TRACE_GROUP_THREAD, version=2, event_types=[1, 2, 3, 4])
class Thread_V2_TypeGroup1(Mof):
    """
    Thread Create/Exit Event
    1: Start
    2: End
    3: DCStart
    4: DCEnd
    """
    pattern = Struct(
        "ProcessId" / Int32ul,
        "ThreadId" / Int32ul,
        "StackBase" / Int64ul,
        "StackLimit" / Int64ul,
        "UserStackBase" / Int64ul,
        "UserStackLimit" / Int64ul,
        "StartAddr" / Int64ul,
        "Win32StartAddr" / Int64ul,
        "TebBase" / Int64ul,
        "SubProcessTag" / Int32ul
    )

    def get_process_id(self) -> int:
        """
        :return: Associate Process id
        """
        return self.source.ProcessId

    def get_thread_id(self) -> int:
        """
        :return: Thread id
        """
        return self.source.ThreadId

    def get_subprocess_tag(self) -> int:
        """
        :return: Use in service start
        """
        return self.source.SubProcessTag


@declare(group=EventTraceGroup.EVENT_TRACE_GROUP_THREAD, version=3, event_types=[1, 2, 3, 4])
class Thread_TypeGroup1(Mof):
    """
    Thread Create/Exit Event
    1: Start
    2: End
    3: DCStart
    4: DCEnd
    """
    pattern = Struct(
        "ProcessId" / Int32ul,
        "ThreadId" / Int32ul,
        "StackBase" / Int64ul,
        "StackLimit" / Int64ul,
        "UserStackBase" / Int64ul,
        "UserStackLimit" / Int64ul,
        "Affinity" / Int64ul,
        "Win32StartAddr" / Int64ul,
        "TebBase" / Int64ul,
        "SubProcessTag" / Int32ul,
        "BasePriority" / Byte,
        "PagePriority" / Byte,
        "IoPriority" / Byte,
        "ThreadFlags" / Byte
    )

    def get_process_id(self) -> int:
        """
        :return: Associate Process id
        """
        return self.source.ProcessId

    def get_thread_id(self) -> int:
        """
        :return: Thread id
        """
        return self.source.ThreadId

    def get_subprocess_tag(self) -> int:
        """
        :return: Use in service start
        """
        return self.source.SubProcessTag

    def get_thread_flags(self) -> int:
        """
        :return: Thread creation flags
        """
        return self.source.ThreadFlags


@declare(group=EventTraceGroup.EVENT_TRACE_GROUP_THREAD, version=2, event_types=[37])
class CompCS(Mof):
    """
    Empty log
    """
    pattern = Struct()
