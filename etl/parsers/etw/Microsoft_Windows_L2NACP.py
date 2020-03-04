# -*- coding: utf-8 -*-
"""
Microsoft-Windows-L2NACP
GUID : 85fe7609-ff4a-48e9-9d50-12918e43e1da
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("85fe7609-ff4a-48e9-9d50-12918e43e1da"), event_id=13003, version=0)
class Microsoft_Windows_L2NACP_13003_0(Etw):
    pattern = Struct(
        "Result" / Int32ul,
        "Reason" / Int32ul,
        "InterfaceGuid" / Guid,
        "ProfileName" / WString
    )


@declare(guid=guid("85fe7609-ff4a-48e9-9d50-12918e43e1da"), event_id=13004, version=0)
class Microsoft_Windows_L2NACP_13004_0(Etw):
    pattern = Struct(
        "Result" / Int32ul,
        "InterfaceGuid" / Guid,
        "ProfileName" / WString
    )


@declare(guid=guid("85fe7609-ff4a-48e9-9d50-12918e43e1da"), event_id=13023, version=0)
class Microsoft_Windows_L2NACP_13023_0(Etw):
    pattern = Struct(
        "Result" / Int32ul,
        "Reason" / Int32ul,
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("85fe7609-ff4a-48e9-9d50-12918e43e1da"), event_id=13024, version=0)
class Microsoft_Windows_L2NACP_13024_0(Etw):
    pattern = Struct(
        "Result" / Int32ul,
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("85fe7609-ff4a-48e9-9d50-12918e43e1da"), event_id=14000, version=0)
class Microsoft_Windows_L2NACP_14000_0(Etw):
    pattern = Struct(
        "Enabled" / Int8ul,
        "Remote" / Int8ul,
        "Dot3Allowed" / Int8ul,
        "WlanAllowed" / Int8ul,
        "CredentialsFound" / Int8ul
    )

