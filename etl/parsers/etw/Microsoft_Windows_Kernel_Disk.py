# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Kernel-Disk
GUID : c7bde69a-e1e0-4177-b6ef-283ad1525271
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("c7bde69a-e1e0-4177-b6ef-283ad1525271"), event_id=10, version=0)
class Microsoft_Windows_Kernel_Disk_10_0(Etw):
    pattern = Struct(
        "DiskNumber" / Int32ul,
        "IrpFlags" / Int32ul,
        "TransferSize" / Int32ul,
        "Reserved" / Int32ul,
        "ByteOffset" / Int64ul,
        "FileObject" / Int64ul,
        "IORequestPacket" / Int64ul,
        "HighResResponseTime" / Int64ul
    )


@declare(guid=guid("c7bde69a-e1e0-4177-b6ef-283ad1525271"), event_id=11, version=0)
class Microsoft_Windows_Kernel_Disk_11_0(Etw):
    pattern = Struct(
        "DiskNumber" / Int32ul,
        "IrpFlags" / Int32ul,
        "TransferSize" / Int32ul,
        "Reserved" / Int32ul,
        "ByteOffset" / Int64ul,
        "FileObject" / Int64ul,
        "IORequestPacket" / Int64ul,
        "HighResResponseTime" / Int64ul
    )


@declare(guid=guid("c7bde69a-e1e0-4177-b6ef-283ad1525271"), event_id=14, version=0)
class Microsoft_Windows_Kernel_Disk_14_0(Etw):
    pattern = Struct(
        "DiskNumber" / Int32ul,
        "IrpFlags" / Int32ul,
        "HighResResponseTime" / Int64ul,
        "IORequestPacket" / Int64ul
    )

