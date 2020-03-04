# -*- coding: utf-8 -*-
from construct import Struct, Int32ul, Int64ul

from etl.parsers.kernel.core import declare, Mof
from etl.wmi import EventTraceGroup


@declare(group=EventTraceGroup.EVENT_TRACE_GROUP_IO, version=3, event_types=[10, 11, 55, 56])
class DiskIo_TypeGroup1(Mof):
    """
    I/O Read/Write Event
    10: Read
    11: Write
    55: OpticalRead
    56: OpticalWrite
    """
    pattern = Struct(
        "DiskNumber" / Int32ul,
        "IrpFlags" / Int32ul,
        "TransferSize" / Int32ul,
        "Reserved" / Int32ul,
        "ByteOffset" / Int64ul,
        "FileObject" / Int64ul,
        "Irp" / Int64ul,
        "HighResponseTime" / Int64ul,
        "IssuingThreadId" / Int32ul
    )

    def get_disk_number(self) -> int:
        """
        :return: Get the disk number of the operation
        """
        return self.source.DiskNumber

    def get_issuing_thread_id(self) -> int:
        """
        :return: Id of issuing thread
        """
        return self.source.IssuingThreadId

    def get_transfer_size(self) -> int:
        """
        :return: Size of the transfer
        """
        return self.source.TransferSize


@declare(group=EventTraceGroup.EVENT_TRACE_GROUP_IO, version=3, event_types=[14, 57])
class DiskIo_TypeGroup3(Mof):
    """
    I/O Flush Buffers Event
    14: FlushBuffers
    57: OpticalFlushBuffers
    """
    pattern = Struct(
        "DiskNumber" / Int32ul,
        "IrpFlags" / Int32ul,
        "HighResResponseTime" / Int64ul,
        "Irp" / Int32ul,
        "IssuingThreadId" / Int32ul
    )

    def get_disk_number(self) -> int:
        """
        :return: Get the disk number of the operation
        """
        return self.source.DiskNumber

    def get_issuing_thread_id(self) -> int:
        """
        :return: Id of issuing thread
        """
        return self.source.IssuingThreadId
