# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Kernel-LicensingSqm
GUID : a0af438f-4431-41cb-a675-a265050ee947
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("a0af438f-4431-41cb-a675-a265050ee947"), event_id=6, version=0)
class Microsoft_Windows_Kernel_LicensingSqm_6_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )

