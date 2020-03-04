# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Sdstor
GUID : afe654eb-0a83-4eb4-948f-d4510ec39c30
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("afe654eb-0a83-4eb4-948f-d4510ec39c30"), event_id=100, version=0)
class Microsoft_Windows_Sdstor_100_0(Etw):
    pattern = Struct(
        "Port" / Int8ul,
        "Bus" / Int8ul,
        "Target" / Int8ul,
        "LUN" / Int8ul,
        "RequestDuration" / Int64ul,
        "CDBLength" / Int32ul,
        "CDB" / Bytes(lambda this: this.CDBLength),
        "SrbStatus" / Int8ul,
        "Irp" / Int64ul,
        "OriginalIrp" / Int64ul
    )


@declare(guid=guid("afe654eb-0a83-4eb4-948f-d4510ec39c30"), event_id=101, version=0)
class Microsoft_Windows_Sdstor_101_0(Etw):
    pattern = Struct(
        "PackedCommandCount" / Int32ul,
        "NumIrpsPacked" / Int32ul
    )


@declare(guid=guid("afe654eb-0a83-4eb4-948f-d4510ec39c30"), event_id=102, version=0)
class Microsoft_Windows_Sdstor_102_0(Etw):
    pattern = Struct(
        "PackedCommandCount" / Int32ul,
        "NumIrpsPacked" / Int32ul
    )


@declare(guid=guid("afe654eb-0a83-4eb4-948f-d4510ec39c30"), event_id=105, version=0)
class Microsoft_Windows_Sdstor_105_0(Etw):
    pattern = Struct(
        "ResultCode" / Int32ul
    )


@declare(guid=guid("afe654eb-0a83-4eb4-948f-d4510ec39c30"), event_id=107, version=0)
class Microsoft_Windows_Sdstor_107_0(Etw):
    pattern = Struct(
        "LBA" / Int64ul,
        "Length" / Int32ul
    )

