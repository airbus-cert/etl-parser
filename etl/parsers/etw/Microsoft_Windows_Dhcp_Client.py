# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Dhcp-Client
GUID : 15a7a4f8-0072-4eab-abad-f98a4d666aed
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=1000, version=0)
class Microsoft_Windows_Dhcp_Client_1000_0(Etw):
    pattern = Struct(
        "Address" / Int32ul,
        "HWLength" / Int32ul,
        "HWAddress" / Bytes(lambda this: this.HWLength)
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=1001, version=0)
class Microsoft_Windows_Dhcp_Client_1001_0(Etw):
    pattern = Struct(
        "HWLength" / Int32ul,
        "HWAddress" / Bytes(lambda this: this.HWLength),
        "StatusCode" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=1002, version=0)
class Microsoft_Windows_Dhcp_Client_1002_0(Etw):
    pattern = Struct(
        "Address1" / Int32ul,
        "HWLength" / Int32ul,
        "HWAddress" / Bytes(lambda this: this.HWLength),
        "Address2" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=1003, version=0)
class Microsoft_Windows_Dhcp_Client_1003_0(Etw):
    pattern = Struct(
        "HWLength" / Int32ul,
        "HWAddress" / Bytes(lambda this: this.HWLength),
        "StatusCode" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=1004, version=0)
class Microsoft_Windows_Dhcp_Client_1004_0(Etw):
    pattern = Struct(
        "StatusCode" / Int32ul,
        "DwordVal" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=1005, version=0)
class Microsoft_Windows_Dhcp_Client_1005_0(Etw):
    pattern = Struct(
        "Address" / Int32ul,
        "HWLength" / Int32ul,
        "HWAddress" / Bytes(lambda this: this.HWLength)
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=1006, version=0)
class Microsoft_Windows_Dhcp_Client_1006_0(Etw):
    pattern = Struct(
        "HWLength" / Int32ul,
        "HWAddress" / Bytes(lambda this: this.HWLength),
        "StatusCode" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=1007, version=0)
class Microsoft_Windows_Dhcp_Client_1007_0(Etw):
    pattern = Struct(
        "HWLength" / Int32ul,
        "HWAddress" / Bytes(lambda this: this.HWLength),
        "Address" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=1008, version=0)
class Microsoft_Windows_Dhcp_Client_1008_0(Etw):
    pattern = Struct(
        "StatusCode" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=1018, version=0)
class Microsoft_Windows_Dhcp_Client_1018_0(Etw):
    pattern = Struct(
        "StatusCode" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50001, version=0)
class Microsoft_Windows_Dhcp_Client_50001_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50002, version=0)
class Microsoft_Windows_Dhcp_Client_50002_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50003, version=0)
class Microsoft_Windows_Dhcp_Client_50003_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50004, version=0)
class Microsoft_Windows_Dhcp_Client_50004_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50005, version=0)
class Microsoft_Windows_Dhcp_Client_50005_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50006, version=0)
class Microsoft_Windows_Dhcp_Client_50006_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50007, version=0)
class Microsoft_Windows_Dhcp_Client_50007_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50008, version=0)
class Microsoft_Windows_Dhcp_Client_50008_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50009, version=0)
class Microsoft_Windows_Dhcp_Client_50009_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50010, version=0)
class Microsoft_Windows_Dhcp_Client_50010_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "Address1" / Int32ul,
        "Address2" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50011, version=0)
class Microsoft_Windows_Dhcp_Client_50011_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50012, version=0)
class Microsoft_Windows_Dhcp_Client_50012_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50013, version=0)
class Microsoft_Windows_Dhcp_Client_50013_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "Address1" / Int32ul,
        "Address2" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50014, version=0)
class Microsoft_Windows_Dhcp_Client_50014_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50015, version=0)
class Microsoft_Windows_Dhcp_Client_50015_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50016, version=0)
class Microsoft_Windows_Dhcp_Client_50016_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50017, version=0)
class Microsoft_Windows_Dhcp_Client_50017_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50018, version=0)
class Microsoft_Windows_Dhcp_Client_50018_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50019, version=0)
class Microsoft_Windows_Dhcp_Client_50019_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50020, version=0)
class Microsoft_Windows_Dhcp_Client_50020_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "BoolFlag" / Int8ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50021, version=0)
class Microsoft_Windows_Dhcp_Client_50021_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50022, version=0)
class Microsoft_Windows_Dhcp_Client_50022_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "Address" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50023, version=0)
class Microsoft_Windows_Dhcp_Client_50023_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50024, version=0)
class Microsoft_Windows_Dhcp_Client_50024_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50025, version=0)
class Microsoft_Windows_Dhcp_Client_50025_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50028, version=0)
class Microsoft_Windows_Dhcp_Client_50028_0(Etw):
    pattern = Struct(
        "Address" / Int32ul,
        "InterfaceId" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50029, version=0)
class Microsoft_Windows_Dhcp_Client_50029_0(Etw):
    pattern = Struct(
        "Address" / Int32ul,
        "InterfaceId" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50030, version=0)
class Microsoft_Windows_Dhcp_Client_50030_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50032, version=0)
class Microsoft_Windows_Dhcp_Client_50032_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "Address" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50033, version=0)
class Microsoft_Windows_Dhcp_Client_50033_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50034, version=0)
class Microsoft_Windows_Dhcp_Client_50034_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50035, version=0)
class Microsoft_Windows_Dhcp_Client_50035_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50037, version=0)
class Microsoft_Windows_Dhcp_Client_50037_0(Etw):
    pattern = Struct(
        "DwordVal" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50038, version=0)
class Microsoft_Windows_Dhcp_Client_50038_0(Etw):
    pattern = Struct(
        "StatusCode" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50039, version=0)
class Microsoft_Windows_Dhcp_Client_50039_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50040, version=0)
class Microsoft_Windows_Dhcp_Client_50040_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50042, version=0)
class Microsoft_Windows_Dhcp_Client_50042_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "StatusCode" / Int32ul,
        "Dword" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50043, version=0)
class Microsoft_Windows_Dhcp_Client_50043_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50044, version=0)
class Microsoft_Windows_Dhcp_Client_50044_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50053, version=0)
class Microsoft_Windows_Dhcp_Client_50053_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50055, version=0)
class Microsoft_Windows_Dhcp_Client_50055_0(Etw):
    pattern = Struct(
        "Address" / Int32ul,
        "InterfaceId" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50056, version=0)
class Microsoft_Windows_Dhcp_Client_50056_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50059, version=0)
class Microsoft_Windows_Dhcp_Client_50059_0(Etw):
    pattern = Struct(
        "Str1" / WString,
        "Str2" / WString,
        "Str3" / WString,
        "Str4" / WString
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50060, version=0)
class Microsoft_Windows_Dhcp_Client_50060_0(Etw):
    pattern = Struct(
        "Str1" / WString,
        "Str2" / WString,
        "Str3" / WString,
        "Str4" / WString
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50061, version=0)
class Microsoft_Windows_Dhcp_Client_50061_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50062, version=0)
class Microsoft_Windows_Dhcp_Client_50062_0(Etw):
    pattern = Struct(
        "Address" / Int32ul,
        "InterfaceId" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50063, version=0)
class Microsoft_Windows_Dhcp_Client_50063_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50064, version=0)
class Microsoft_Windows_Dhcp_Client_50064_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50065, version=0)
class Microsoft_Windows_Dhcp_Client_50065_0(Etw):
    pattern = Struct(
        "NetworkHintString" / WString,
        "NetworkHint" / WString,
        "HWLength" / Int32ul,
        "HWAddress" / Bytes(lambda this: this.HWLength)
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50066, version=0)
class Microsoft_Windows_Dhcp_Client_50066_0(Etw):
    pattern = Struct(
        "NetworkHintString" / WString,
        "NetworkHint" / WString,
        "HWLength" / Int32ul,
        "HWAddress" / Bytes(lambda this: this.HWLength)
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50067, version=0)
class Microsoft_Windows_Dhcp_Client_50067_0(Etw):
    pattern = Struct(
        "NetworkHintString" / WString,
        "NetworkHint" / WString,
        "HWLength" / Int32ul,
        "HWAddress" / Bytes(lambda this: this.HWLength)
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50068, version=0)
class Microsoft_Windows_Dhcp_Client_50068_0(Etw):
    pattern = Struct(
        "Address" / Int32ul,
        "InterfaceId" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50069, version=0)
class Microsoft_Windows_Dhcp_Client_50069_0(Etw):
    pattern = Struct(
        "BoolFlag" / Int8ul,
        "InterfaceId" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50070, version=0)
class Microsoft_Windows_Dhcp_Client_50070_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50071, version=0)
class Microsoft_Windows_Dhcp_Client_50071_0(Etw):
    pattern = Struct(
        "NetworkHintString" / WString,
        "NetworkHint" / WString,
        "InterfaceId" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50072, version=0)
class Microsoft_Windows_Dhcp_Client_50072_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50073, version=0)
class Microsoft_Windows_Dhcp_Client_50073_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50074, version=0)
class Microsoft_Windows_Dhcp_Client_50074_0(Etw):
    pattern = Struct(
        "DwordVal" / Int32ul,
        "InterfaceId" / Int32ul,
        "DwordVal1" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50075, version=0)
class Microsoft_Windows_Dhcp_Client_50075_0(Etw):
    pattern = Struct(
        "DwordVal" / Int32ul,
        "InterfaceId" / Int32ul,
        "DwordVal1" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50076, version=0)
class Microsoft_Windows_Dhcp_Client_50076_0(Etw):
    pattern = Struct(
        "NetworkHintString" / WString,
        "NetworkHint" / WString,
        "HWLength" / Int32ul,
        "HWAddress" / Bytes(lambda this: this.HWLength)
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50077, version=0)
class Microsoft_Windows_Dhcp_Client_50077_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50081, version=0)
class Microsoft_Windows_Dhcp_Client_50081_0(Etw):
    pattern = Struct(
        "DwordVal1" / Int32ul,
        "InterfaceId" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50083, version=0)
class Microsoft_Windows_Dhcp_Client_50083_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50084, version=0)
class Microsoft_Windows_Dhcp_Client_50084_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50085, version=0)
class Microsoft_Windows_Dhcp_Client_50085_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "Address" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50086, version=0)
class Microsoft_Windows_Dhcp_Client_50086_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "Address" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50087, version=0)
class Microsoft_Windows_Dhcp_Client_50087_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "Address" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50088, version=0)
class Microsoft_Windows_Dhcp_Client_50088_0(Etw):
    pattern = Struct(
        "ProcID" / Int32ul,
        "UniqueID" / Int32ul,
        "EventPath" / CString,
        "ClassIDSize" / Int32ul,
        "ClassID" / Bytes(lambda this: this.ClassIDSize),
        "OptListSize" / Int32ul,
        "OptList" / Bytes(lambda this: this.OptListSize),
        "IsVendor" / Int8ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50089, version=0)
class Microsoft_Windows_Dhcp_Client_50089_0(Etw):
    pattern = Struct(
        "ProcID" / Int32ul,
        "UniqueID" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50090, version=0)
class Microsoft_Windows_Dhcp_Client_50090_0(Etw):
    pattern = Struct(
        "ProcID" / Int32ul,
        "UniqueID" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50091, version=0)
class Microsoft_Windows_Dhcp_Client_50091_0(Etw):
    pattern = Struct(
        "InterfaceLUID" / Int64ul,
        "ClassIDSize" / Int32ul,
        "ClassID" / Bytes(lambda this: this.ClassIDSize),
        "StandardOptListSize" / Int32ul,
        "StandardOptList" / Bytes(lambda this: this.StandardOptListSize),
        "VendorOptListSize" / Int32ul,
        "VendorOptList" / Bytes(lambda this: this.VendorOptListSize)
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50092, version=0)
class Microsoft_Windows_Dhcp_Client_50092_0(Etw):
    pattern = Struct(
        "InterfaceLUID" / Int64ul,
        "InterfaceId" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50093, version=0)
class Microsoft_Windows_Dhcp_Client_50093_0(Etw):
    pattern = Struct(
        "InterfaceLUID" / Int64ul,
        "InterfaceId" / Int32ul,
        "StatusCode" / Int32ul,
        "OptDataSize" / Int32ul,
        "OptData" / Bytes(lambda this: this.OptDataSize)
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50094, version=0)
class Microsoft_Windows_Dhcp_Client_50094_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "DwordVal1" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50095, version=0)
class Microsoft_Windows_Dhcp_Client_50095_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "DwordVal1" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50096, version=0)
class Microsoft_Windows_Dhcp_Client_50096_0(Etw):
    pattern = Struct(
        "DwordVal1" / Int32ul,
        "InterfaceId" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50097, version=0)
class Microsoft_Windows_Dhcp_Client_50097_0(Etw):
    pattern = Struct(
        "DwordVal1" / Int32ul,
        "InterfaceId" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50098, version=0)
class Microsoft_Windows_Dhcp_Client_50098_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50099, version=0)
class Microsoft_Windows_Dhcp_Client_50099_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=50100, version=0)
class Microsoft_Windows_Dhcp_Client_50100_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=60000, version=0)
class Microsoft_Windows_Dhcp_Client_60000_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceId" / Int32ul,
        "Address1" / Int32ul,
        "Address2" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=60001, version=0)
class Microsoft_Windows_Dhcp_Client_60001_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceId" / Int32ul,
        "Address1" / Int32ul,
        "Address2" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=60002, version=0)
class Microsoft_Windows_Dhcp_Client_60002_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceId" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=60003, version=0)
class Microsoft_Windows_Dhcp_Client_60003_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceId" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=60004, version=0)
class Microsoft_Windows_Dhcp_Client_60004_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceId" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=60005, version=0)
class Microsoft_Windows_Dhcp_Client_60005_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceId" / Int32ul,
        "Address1" / Int32ul,
        "Address2" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=60006, version=0)
class Microsoft_Windows_Dhcp_Client_60006_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceId" / Int32ul,
        "Address1" / Int32ul,
        "Address2" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=60007, version=0)
class Microsoft_Windows_Dhcp_Client_60007_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceId" / Int32ul,
        "Address1" / Int32ul,
        "Address2" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=60010, version=0)
class Microsoft_Windows_Dhcp_Client_60010_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceId" / Int32ul,
        "Address1" / Int32ul,
        "Address2" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=60011, version=0)
class Microsoft_Windows_Dhcp_Client_60011_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceId" / Int32ul,
        "Address1" / Int32ul,
        "Address2" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=60012, version=0)
class Microsoft_Windows_Dhcp_Client_60012_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceId" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=60013, version=0)
class Microsoft_Windows_Dhcp_Client_60013_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceId" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=60014, version=0)
class Microsoft_Windows_Dhcp_Client_60014_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceId" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=60015, version=0)
class Microsoft_Windows_Dhcp_Client_60015_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceId" / Int32ul,
        "Address1" / Int32ul,
        "Address2" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=60016, version=0)
class Microsoft_Windows_Dhcp_Client_60016_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceId" / Int32ul,
        "Address1" / Int32ul,
        "Address2" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=60017, version=0)
class Microsoft_Windows_Dhcp_Client_60017_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceId" / Int32ul,
        "Address1" / Int32ul,
        "Address2" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=60018, version=0)
class Microsoft_Windows_Dhcp_Client_60018_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceId" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=60019, version=0)
class Microsoft_Windows_Dhcp_Client_60019_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceId" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=60020, version=0)
class Microsoft_Windows_Dhcp_Client_60020_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceId" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=60021, version=0)
class Microsoft_Windows_Dhcp_Client_60021_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceId" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=60022, version=0)
class Microsoft_Windows_Dhcp_Client_60022_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceId" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=60023, version=0)
class Microsoft_Windows_Dhcp_Client_60023_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceId" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=60024, version=0)
class Microsoft_Windows_Dhcp_Client_60024_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceId" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=60025, version=0)
class Microsoft_Windows_Dhcp_Client_60025_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "Address" / Int32ul,
        "InterfaceId" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=60028, version=0)
class Microsoft_Windows_Dhcp_Client_60028_0(Etw):
    pattern = Struct(
        "StatusCode" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=60029, version=0)
class Microsoft_Windows_Dhcp_Client_60029_0(Etw):
    pattern = Struct(
        "StatusCode" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=60030, version=0)
class Microsoft_Windows_Dhcp_Client_60030_0(Etw):
    pattern = Struct(
        "StatusCode" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=60031, version=0)
class Microsoft_Windows_Dhcp_Client_60031_0(Etw):
    pattern = Struct(
        "StatusCode" / Int32ul
    )


@declare(guid=guid("15a7a4f8-0072-4eab-abad-f98a4d666aed"), event_id=60032, version=0)
class Microsoft_Windows_Dhcp_Client_60032_0(Etw):
    pattern = Struct(
        "StatusCode" / Int32ul
    )

