# -*- coding: utf-8 -*-
"""
Microsoft-Windows-StorageManagement-WSP-Host
GUID : 595f33ea-d4af-4f4d-b4dd-9dacdd17fc6e
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("595f33ea-d4af-4f4d-b4dd-9dacdd17fc6e"), event_id=1000, version=0)
class Microsoft_Windows_StorageManagement_WSP_Host_1000_0(Etw):
    pattern = Struct(
        "ProviderName" / WString,
        "ProviderDLL" / WString,
        "ErrorCode" / Int32ul,
        "LoadPhase" / Int32ul
    )

