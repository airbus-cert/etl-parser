# -*- coding: utf-8 -*-
"""
Microsoft-Windows-WWAN-CFE
GUID : 71c993b8-1e28-4543-9886-fb219b63fdb3
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("71c993b8-1e28-4543-9886-fb219b63fdb3"), event_id=12, version=0)
class Microsoft_Windows_WWAN_CFE_12_0(Etw):
    pattern = Struct(
        "Manufacture" / WString,
        "Model" / WString,
        "FirmwareVersion" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("71c993b8-1e28-4543-9886-fb219b63fdb3"), event_id=15, version=0)
class Microsoft_Windows_WWAN_CFE_15_0(Etw):
    pattern = Struct(
        "ProviderName" / WString
    )


@declare(guid=guid("71c993b8-1e28-4543-9886-fb219b63fdb3"), event_id=16, version=0)
class Microsoft_Windows_WWAN_CFE_16_0(Etw):
    pattern = Struct(
        "Manufacture" / WString,
        "Model" / WString,
        "FirmwareVersion" / WString,
        "ErrorCode" / Int32ul
    )

