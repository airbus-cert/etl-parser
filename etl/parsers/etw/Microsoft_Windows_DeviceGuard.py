# -*- coding: utf-8 -*-
"""
Microsoft-Windows-DeviceGuard
GUID : f717d024-f5b4-4f03-9ab9-331b2dc38ffb
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("f717d024-f5b4-4f03-9ab9-331b2dc38ffb"), event_id=6000, version=0)
class Microsoft_Windows_DeviceGuard_6000_0(Etw):
    pattern = Struct(
        "PolicyFilePath" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("f717d024-f5b4-4f03-9ab9-331b2dc38ffb"), event_id=7000, version=0)
class Microsoft_Windows_DeviceGuard_7000_0(Etw):
    pattern = Struct(
        "VirtualizationBasedSecurity" / WString,
        "SecureBoot" / WString,
        "DmaProtection" / WString,
        "HVCI" / WString,
        "LSA" / WString,
        "Reboot" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("f717d024-f5b4-4f03-9ab9-331b2dc38ffb"), event_id=7001, version=0)
class Microsoft_Windows_DeviceGuard_7001_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("f717d024-f5b4-4f03-9ab9-331b2dc38ffb"), event_id=7002, version=0)
class Microsoft_Windows_DeviceGuard_7002_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("f717d024-f5b4-4f03-9ab9-331b2dc38ffb"), event_id=7010, version=0)
class Microsoft_Windows_DeviceGuard_7010_0(Etw):
    pattern = Struct(
        "SiPolicy" / WString,
        "PolicyFilePath" / WString,
        "Reboot" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("f717d024-f5b4-4f03-9ab9-331b2dc38ffb"), event_id=7011, version=0)
class Microsoft_Windows_DeviceGuard_7011_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("f717d024-f5b4-4f03-9ab9-331b2dc38ffb"), event_id=7012, version=0)
class Microsoft_Windows_DeviceGuard_7012_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "ErrorMessage" / WString
    )

