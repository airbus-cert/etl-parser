# -*- coding: utf-8 -*-
"""
Microsoft-Windows-DHCPv6-Client
GUID : 6a1f2b00-6a90-4c38-95a5-5cab3b056778
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=1000, version=0)
class Microsoft_Windows_DHCPv6_Client_1000_0(Etw):
    pattern = Struct(
        "InterfaceGUID" / WString,
        "HWLength" / Int32ul,
        "HWAddress" / Bytes(lambda this: this.HWLength)
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=1003, version=0)
class Microsoft_Windows_DHCPv6_Client_1003_0(Etw):
    pattern = Struct(
        "HWLength" / Int32ul,
        "HWAddress" / Bytes(lambda this: this.HWLength),
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=1004, version=0)
class Microsoft_Windows_DHCPv6_Client_1004_0(Etw):
    pattern = Struct(
        "StatusCode" / Int32ul,
        "DwordVal" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=1005, version=0)
class Microsoft_Windows_DHCPv6_Client_1005_0(Etw):
    pattern = Struct(
        "InterfaceGUID" / WString,
        "HWLength" / Int32ul,
        "HWAddress" / Bytes(lambda this: this.HWLength)
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=1006, version=0)
class Microsoft_Windows_DHCPv6_Client_1006_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "Flag1" / Int8ul,
        "Flag2" / Int8ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=1008, version=0)
class Microsoft_Windows_DHCPv6_Client_1008_0(Etw):
    pattern = Struct(
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=1009, version=0)
class Microsoft_Windows_DHCPv6_Client_1009_0(Etw):
    pattern = Struct(
        "HWLength" / Int32ul,
        "HWAddress" / Bytes(lambda this: this.HWLength),
        "DUIDLength" / Int32ul,
        "DUID" / Bytes(lambda this: this.DUIDLength),
        "NewHWLength" / Int32ul,
        "NewHWAddress" / Bytes(lambda this: this.NewHWLength),
        "NewDUIDLength" / Int32ul,
        "NewDUID" / Bytes(lambda this: this.NewDUIDLength)
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=1010, version=0)
class Microsoft_Windows_DHCPv6_Client_1010_0(Etw):
    pattern = Struct(
        "NetworkHintString" / WString,
        "NetworkHint" / WString,
        "HWLength" / Int32ul,
        "HWAddress" / Bytes(lambda this: this.HWLength)
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=1011, version=0)
class Microsoft_Windows_DHCPv6_Client_1011_0(Etw):
    pattern = Struct(
        "NetworkHintString" / WString,
        "NetworkHint" / WString,
        "HWLength" / Int32ul,
        "HWAddress" / Bytes(lambda this: this.HWLength)
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=1012, version=0)
class Microsoft_Windows_DHCPv6_Client_1012_0(Etw):
    pattern = Struct(
        "NetworkHintString" / WString,
        "NetworkHint" / WString,
        "HWLength" / Int32ul,
        "HWAddress" / Bytes(lambda this: this.HWLength)
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=1013, version=0)
class Microsoft_Windows_DHCPv6_Client_1013_0(Etw):
    pattern = Struct(
        "NetworkHintString" / WString,
        "NetworkHint" / WString,
        "HWLength" / Int32ul,
        "HWAddress" / Bytes(lambda this: this.HWLength)
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=50057, version=0)
class Microsoft_Windows_DHCPv6_Client_50057_0(Etw):
    pattern = Struct(
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=50071, version=0)
class Microsoft_Windows_DHCPv6_Client_50071_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=50072, version=0)
class Microsoft_Windows_DHCPv6_Client_50072_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=51001, version=0)
class Microsoft_Windows_DHCPv6_Client_51001_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=51002, version=0)
class Microsoft_Windows_DHCPv6_Client_51002_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=51004, version=0)
class Microsoft_Windows_DHCPv6_Client_51004_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=51005, version=0)
class Microsoft_Windows_DHCPv6_Client_51005_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "DwordVal1" / Int32ul,
        "DwordVal2" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=51006, version=0)
class Microsoft_Windows_DHCPv6_Client_51006_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=51007, version=0)
class Microsoft_Windows_DHCPv6_Client_51007_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=51008, version=0)
class Microsoft_Windows_DHCPv6_Client_51008_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=51009, version=0)
class Microsoft_Windows_DHCPv6_Client_51009_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=51010, version=0)
class Microsoft_Windows_DHCPv6_Client_51010_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=51011, version=0)
class Microsoft_Windows_DHCPv6_Client_51011_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=51012, version=0)
class Microsoft_Windows_DHCPv6_Client_51012_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=51013, version=0)
class Microsoft_Windows_DHCPv6_Client_51013_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=51014, version=0)
class Microsoft_Windows_DHCPv6_Client_51014_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=51015, version=0)
class Microsoft_Windows_DHCPv6_Client_51015_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=51016, version=0)
class Microsoft_Windows_DHCPv6_Client_51016_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=51017, version=0)
class Microsoft_Windows_DHCPv6_Client_51017_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=51018, version=0)
class Microsoft_Windows_DHCPv6_Client_51018_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=51019, version=0)
class Microsoft_Windows_DHCPv6_Client_51019_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=51020, version=0)
class Microsoft_Windows_DHCPv6_Client_51020_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=51021, version=0)
class Microsoft_Windows_DHCPv6_Client_51021_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=51022, version=0)
class Microsoft_Windows_DHCPv6_Client_51022_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=51023, version=0)
class Microsoft_Windows_DHCPv6_Client_51023_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=51024, version=0)
class Microsoft_Windows_DHCPv6_Client_51024_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=51025, version=0)
class Microsoft_Windows_DHCPv6_Client_51025_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=51026, version=0)
class Microsoft_Windows_DHCPv6_Client_51026_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=51027, version=0)
class Microsoft_Windows_DHCPv6_Client_51027_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=51029, version=0)
class Microsoft_Windows_DHCPv6_Client_51029_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=51030, version=0)
class Microsoft_Windows_DHCPv6_Client_51030_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=51031, version=0)
class Microsoft_Windows_DHCPv6_Client_51031_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "StatusCode" / Int32ul,
        "Dword1" / Int32ul,
        "Dword2" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=51032, version=0)
class Microsoft_Windows_DHCPv6_Client_51032_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=51033, version=0)
class Microsoft_Windows_DHCPv6_Client_51033_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=51034, version=0)
class Microsoft_Windows_DHCPv6_Client_51034_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "StatusCode" / Int32ul,
        "Dword1" / Int32ul,
        "Dword2" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=51035, version=0)
class Microsoft_Windows_DHCPv6_Client_51035_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=51036, version=0)
class Microsoft_Windows_DHCPv6_Client_51036_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=51037, version=0)
class Microsoft_Windows_DHCPv6_Client_51037_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "RefreshTime" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=51038, version=0)
class Microsoft_Windows_DHCPv6_Client_51038_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=51039, version=0)
class Microsoft_Windows_DHCPv6_Client_51039_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=51040, version=0)
class Microsoft_Windows_DHCPv6_Client_51040_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=51043, version=0)
class Microsoft_Windows_DHCPv6_Client_51043_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=51044, version=0)
class Microsoft_Windows_DHCPv6_Client_51044_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=51045, version=0)
class Microsoft_Windows_DHCPv6_Client_51045_0(Etw):
    pattern = Struct(
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=51047, version=0)
class Microsoft_Windows_DHCPv6_Client_51047_0(Etw):
    pattern = Struct(
        "DwordVal" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=51048, version=0)
class Microsoft_Windows_DHCPv6_Client_51048_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=51049, version=0)
class Microsoft_Windows_DHCPv6_Client_51049_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=51050, version=0)
class Microsoft_Windows_DHCPv6_Client_51050_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "StatusCode" / Int32ul,
        "Dword" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=51051, version=0)
class Microsoft_Windows_DHCPv6_Client_51051_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=51057, version=0)
class Microsoft_Windows_DHCPv6_Client_51057_0(Etw):
    pattern = Struct(
        "DwordVal" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=51058, version=0)
class Microsoft_Windows_DHCPv6_Client_51058_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=51060, version=0)
class Microsoft_Windows_DHCPv6_Client_51060_0(Etw):
    pattern = Struct(
        "InterfaceGUID" / WString,
        "HWLength" / Int32ul,
        "HWAddress" / Bytes(lambda this: this.HWLength)
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=51061, version=0)
class Microsoft_Windows_DHCPv6_Client_51061_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=51062, version=0)
class Microsoft_Windows_DHCPv6_Client_51062_0(Etw):
    pattern = Struct(
        "HWLength" / Int32ul,
        "HWAddress" / Bytes(lambda this: this.HWLength),
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=51063, version=0)
class Microsoft_Windows_DHCPv6_Client_51063_0(Etw):
    pattern = Struct(
        "DwordVal" / Int32ul,
        "InterfaceId" / Int32ul,
        "DwordVal1" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=51064, version=0)
class Microsoft_Windows_DHCPv6_Client_51064_0(Etw):
    pattern = Struct(
        "DwordVal" / Int32ul,
        "InterfaceId" / Int32ul,
        "DwordVal1" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=51065, version=0)
class Microsoft_Windows_DHCPv6_Client_51065_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "NewMode" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=51066, version=0)
class Microsoft_Windows_DHCPv6_Client_51066_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=51067, version=0)
class Microsoft_Windows_DHCPv6_Client_51067_0(Etw):
    pattern = Struct(
        "DwordVal1" / Int32ul,
        "InterfaceId" / Int32ul,
        "Address1" / Int32ul,
        "DwordVal2" / Int32ul,
        "DwordVal3" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=51068, version=0)
class Microsoft_Windows_DHCPv6_Client_51068_0(Etw):
    pattern = Struct(
        "DwordVal1" / Int32ul,
        "InterfaceId" / Int32ul,
        "Address1" / Int32ul,
        "DwordVal2" / Int32ul,
        "DwordVal3" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=51069, version=0)
class Microsoft_Windows_DHCPv6_Client_51069_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "Address1" / Int32ul,
        "DwordVal1" / Int32ul,
        "DwordVal2" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=51070, version=0)
class Microsoft_Windows_DHCPv6_Client_51070_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "DwordVal1" / Int32ul,
        "DwordVal2" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=51073, version=0)
class Microsoft_Windows_DHCPv6_Client_51073_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "DwordVal1" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=51074, version=0)
class Microsoft_Windows_DHCPv6_Client_51074_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "DwordVal1" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=51077, version=0)
class Microsoft_Windows_DHCPv6_Client_51077_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "DwordVal1" / Int32ul,
        "DwordVal2" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=51078, version=0)
class Microsoft_Windows_DHCPv6_Client_51078_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "DwordVal1" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=51079, version=0)
class Microsoft_Windows_DHCPv6_Client_51079_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "DwordVal1" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=51080, version=0)
class Microsoft_Windows_DHCPv6_Client_51080_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=51081, version=0)
class Microsoft_Windows_DHCPv6_Client_51081_0(Etw):
    pattern = Struct(
        "DwordVal1" / Int32ul,
        "InterfaceId" / Int32ul,
        "DwordVal2" / Int32ul,
        "DwordVal3" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=51082, version=0)
class Microsoft_Windows_DHCPv6_Client_51082_0(Etw):
    pattern = Struct(
        "DwordVal1" / Int32ul,
        "InterfaceId" / Int32ul,
        "DwordVal2" / Int32ul,
        "DwordVal3" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=51083, version=0)
class Microsoft_Windows_DHCPv6_Client_51083_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=51084, version=0)
class Microsoft_Windows_DHCPv6_Client_51084_0(Etw):
    pattern = Struct(
        "InterfaceId" / Int32ul,
        "DwordVal1" / Int32ul,
        "DwordVal2" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=60000, version=0)
class Microsoft_Windows_DHCPv6_Client_60000_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceId" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=60001, version=0)
class Microsoft_Windows_DHCPv6_Client_60001_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceId" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=60002, version=0)
class Microsoft_Windows_DHCPv6_Client_60002_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceId" / Int32ul
    )


@declare(guid=guid("6a1f2b00-6a90-4c38-95a5-5cab3b056778"), event_id=60003, version=0)
class Microsoft_Windows_DHCPv6_Client_60003_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceId" / Int32ul
    )

