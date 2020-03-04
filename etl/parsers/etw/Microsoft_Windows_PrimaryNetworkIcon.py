# -*- coding: utf-8 -*-
"""
Microsoft-Windows-PrimaryNetworkIcon
GUID : 8ce93926-bdae-4409-9155-2fe4799ef4d3
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("8ce93926-bdae-4409-9155-2fe4799ef4d3"), event_id=121, version=0)
class Microsoft_Windows_PrimaryNetworkIcon_121_0(Etw):
    pattern = Struct(
        "IconResID" / Int32ul
    )


@declare(guid=guid("8ce93926-bdae-4409-9155-2fe4799ef4d3"), event_id=123, version=0)
class Microsoft_Windows_PrimaryNetworkIcon_123_0(Etw):
    pattern = Struct(
        "IconResID" / Int32ul
    )


@declare(guid=guid("8ce93926-bdae-4409-9155-2fe4799ef4d3"), event_id=124, version=0)
class Microsoft_Windows_PrimaryNetworkIcon_124_0(Etw):
    pattern = Struct(
        "IconResID" / Int32ul
    )


@declare(guid=guid("8ce93926-bdae-4409-9155-2fe4799ef4d3"), event_id=125, version=0)
class Microsoft_Windows_PrimaryNetworkIcon_125_0(Etw):
    pattern = Struct(
        "IconResID" / Int32ul
    )


@declare(guid=guid("8ce93926-bdae-4409-9155-2fe4799ef4d3"), event_id=126, version=0)
class Microsoft_Windows_PrimaryNetworkIcon_126_0(Etw):
    pattern = Struct(
        "IconResID" / Int32ul
    )


@declare(guid=guid("8ce93926-bdae-4409-9155-2fe4799ef4d3"), event_id=127, version=0)
class Microsoft_Windows_PrimaryNetworkIcon_127_0(Etw):
    pattern = Struct(
        "IconResID" / Int32ul
    )


@declare(guid=guid("8ce93926-bdae-4409-9155-2fe4799ef4d3"), event_id=128, version=0)
class Microsoft_Windows_PrimaryNetworkIcon_128_0(Etw):
    pattern = Struct(
        "IconResID" / Int32ul
    )


@declare(guid=guid("8ce93926-bdae-4409-9155-2fe4799ef4d3"), event_id=129, version=0)
class Microsoft_Windows_PrimaryNetworkIcon_129_0(Etw):
    pattern = Struct(
        "IconResID" / Int32ul
    )


@declare(guid=guid("8ce93926-bdae-4409-9155-2fe4799ef4d3"), event_id=130, version=0)
class Microsoft_Windows_PrimaryNetworkIcon_130_0(Etw):
    pattern = Struct(
        "IconResID" / Int32ul
    )


@declare(guid=guid("8ce93926-bdae-4409-9155-2fe4799ef4d3"), event_id=132, version=0)
class Microsoft_Windows_PrimaryNetworkIcon_132_0(Etw):
    pattern = Struct(
        "IconResID" / Int32ul
    )


@declare(guid=guid("8ce93926-bdae-4409-9155-2fe4799ef4d3"), event_id=133, version=0)
class Microsoft_Windows_PrimaryNetworkIcon_133_0(Etw):
    pattern = Struct(
        "IconResID" / Int32ul
    )


@declare(guid=guid("8ce93926-bdae-4409-9155-2fe4799ef4d3"), event_id=134, version=0)
class Microsoft_Windows_PrimaryNetworkIcon_134_0(Etw):
    pattern = Struct(
        "IconResID" / Int32ul
    )


@declare(guid=guid("8ce93926-bdae-4409-9155-2fe4799ef4d3"), event_id=1005, version=0)
class Microsoft_Windows_PrimaryNetworkIcon_1005_0(Etw):
    pattern = Struct(
        "Error" / Int32ul
    )


@declare(guid=guid("8ce93926-bdae-4409-9155-2fe4799ef4d3"), event_id=1006, version=0)
class Microsoft_Windows_PrimaryNetworkIcon_1006_0(Etw):
    pattern = Struct(
        "Error" / Int32ul
    )


@declare(guid=guid("8ce93926-bdae-4409-9155-2fe4799ef4d3"), event_id=1007, version=0)
class Microsoft_Windows_PrimaryNetworkIcon_1007_0(Etw):
    pattern = Struct(
        "GUID" / Guid,
        "DWORD" / Int32ul
    )


@declare(guid=guid("8ce93926-bdae-4409-9155-2fe4799ef4d3"), event_id=1008, version=0)
class Microsoft_Windows_PrimaryNetworkIcon_1008_0(Etw):
    pattern = Struct(
        "DWORD" / Int32ul
    )


@declare(guid=guid("8ce93926-bdae-4409-9155-2fe4799ef4d3"), event_id=1010, version=0)
class Microsoft_Windows_PrimaryNetworkIcon_1010_0(Etw):
    pattern = Struct(
        "Error" / Int32ul
    )


@declare(guid=guid("8ce93926-bdae-4409-9155-2fe4799ef4d3"), event_id=2001, version=0)
class Microsoft_Windows_PrimaryNetworkIcon_2001_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )

