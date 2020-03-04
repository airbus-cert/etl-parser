# -*- coding: utf-8 -*-
"""
Microsoft-Windows-DeviceConfidence
GUID : 1d5990c1-ec62-49f0-9e37-1f4db12db41e
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("1d5990c1-ec62-49f0-9e37-1f4db12db41e"), event_id=2000, version=0)
class Microsoft_Windows_DeviceConfidence_2000_0(Etw):
    pattern = Struct(
        "packageSid" / WString,
        "capabilityName" / WString
    )


@declare(guid=guid("1d5990c1-ec62-49f0-9e37-1f4db12db41e"), event_id=2001, version=0)
class Microsoft_Windows_DeviceConfidence_2001_0(Etw):
    pattern = Struct(
        "packageSid" / WString,
        "error" / Int32ul
    )


@declare(guid=guid("1d5990c1-ec62-49f0-9e37-1f4db12db41e"), event_id=2002, version=0)
class Microsoft_Windows_DeviceConfidence_2002_0(Etw):
    pattern = Struct(
        "packageSid" / WString,
        "error" / Int32ul
    )

