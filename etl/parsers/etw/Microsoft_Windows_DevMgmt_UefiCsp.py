# -*- coding: utf-8 -*-
"""
Microsoft-Windows-DevMgmt-UefiCsp
GUID : 739d66d8-76c4-4004-873f-169ae5c6eaca
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("739d66d8-76c4-4004-873f-169ae5c6eaca"), event_id=10, version=0)
class Microsoft_Windows_DevMgmt_UefiCsp_10_0(Etw):
    pattern = Struct(
        "FunctionName" / WString
    )


@declare(guid=guid("739d66d8-76c4-4004-873f-169ae5c6eaca"), event_id=11, version=0)
class Microsoft_Windows_DevMgmt_UefiCsp_11_0(Etw):
    pattern = Struct(
        "ErrorString" / WString,
        "ErrorCode" / Int32ul
    )

