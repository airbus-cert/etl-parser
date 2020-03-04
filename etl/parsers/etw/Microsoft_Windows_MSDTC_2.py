# -*- coding: utf-8 -*-
"""
Microsoft-Windows-MSDTC 2
GUID : 5d9e0020-3761-4f36-90c8-38ce6511bd12
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("5d9e0020-3761-4f36-90c8-38ce6511bd12"), event_id=4097, version=0)
class Microsoft_Windows_MSDTC_2_4097_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("5d9e0020-3761-4f36-90c8-38ce6511bd12"), event_id=4098, version=0)
class Microsoft_Windows_MSDTC_2_4098_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )


@declare(guid=guid("5d9e0020-3761-4f36-90c8-38ce6511bd12"), event_id=4099, version=0)
class Microsoft_Windows_MSDTC_2_4099_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("5d9e0020-3761-4f36-90c8-38ce6511bd12"), event_id=4100, version=0)
class Microsoft_Windows_MSDTC_2_4100_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("5d9e0020-3761-4f36-90c8-38ce6511bd12"), event_id=4101, version=0)
class Microsoft_Windows_MSDTC_2_4101_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )


@declare(guid=guid("5d9e0020-3761-4f36-90c8-38ce6511bd12"), event_id=4102, version=0)
class Microsoft_Windows_MSDTC_2_4102_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("5d9e0020-3761-4f36-90c8-38ce6511bd12"), event_id=4103, version=0)
class Microsoft_Windows_MSDTC_2_4103_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("5d9e0020-3761-4f36-90c8-38ce6511bd12"), event_id=4104, version=0)
class Microsoft_Windows_MSDTC_2_4104_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("5d9e0020-3761-4f36-90c8-38ce6511bd12"), event_id=4202, version=0)
class Microsoft_Windows_MSDTC_2_4202_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "param5" / WString,
        "param6" / WString,
        "param7" / WString,
        "param8" / WString,
        "param9" / WString,
        "param10" / WString,
        "param11" / WString,
        "param12" / WString
    )


@declare(guid=guid("5d9e0020-3761-4f36-90c8-38ce6511bd12"), event_id=4350, version=0)
class Microsoft_Windows_MSDTC_2_4350_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )


@declare(guid=guid("5d9e0020-3761-4f36-90c8-38ce6511bd12"), event_id=4875, version=0)
class Microsoft_Windows_MSDTC_2_4875_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("5d9e0020-3761-4f36-90c8-38ce6511bd12"), event_id=4876, version=0)
class Microsoft_Windows_MSDTC_2_4876_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("5d9e0020-3761-4f36-90c8-38ce6511bd12"), event_id=4878, version=0)
class Microsoft_Windows_MSDTC_2_4878_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )


@declare(guid=guid("5d9e0020-3761-4f36-90c8-38ce6511bd12"), event_id=4879, version=0)
class Microsoft_Windows_MSDTC_2_4879_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("5d9e0020-3761-4f36-90c8-38ce6511bd12"), event_id=4880, version=0)
class Microsoft_Windows_MSDTC_2_4880_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("5d9e0020-3761-4f36-90c8-38ce6511bd12"), event_id=53323, version=0)
class Microsoft_Windows_MSDTC_2_53323_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString
    )


@declare(guid=guid("5d9e0020-3761-4f36-90c8-38ce6511bd12"), event_id=53324, version=0)
class Microsoft_Windows_MSDTC_2_53324_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString
    )


@declare(guid=guid("5d9e0020-3761-4f36-90c8-38ce6511bd12"), event_id=53325, version=0)
class Microsoft_Windows_MSDTC_2_53325_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString
    )


@declare(guid=guid("5d9e0020-3761-4f36-90c8-38ce6511bd12"), event_id=53327, version=0)
class Microsoft_Windows_MSDTC_2_53327_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString
    )


@declare(guid=guid("5d9e0020-3761-4f36-90c8-38ce6511bd12"), event_id=53328, version=0)
class Microsoft_Windows_MSDTC_2_53328_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("5d9e0020-3761-4f36-90c8-38ce6511bd12"), event_id=53329, version=0)
class Microsoft_Windows_MSDTC_2_53329_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )


@declare(guid=guid("5d9e0020-3761-4f36-90c8-38ce6511bd12"), event_id=53330, version=0)
class Microsoft_Windows_MSDTC_2_53330_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )


@declare(guid=guid("5d9e0020-3761-4f36-90c8-38ce6511bd12"), event_id=53331, version=0)
class Microsoft_Windows_MSDTC_2_53331_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )


@declare(guid=guid("5d9e0020-3761-4f36-90c8-38ce6511bd12"), event_id=53332, version=0)
class Microsoft_Windows_MSDTC_2_53332_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )


@declare(guid=guid("5d9e0020-3761-4f36-90c8-38ce6511bd12"), event_id=53333, version=0)
class Microsoft_Windows_MSDTC_2_53333_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )


@declare(guid=guid("5d9e0020-3761-4f36-90c8-38ce6511bd12"), event_id=53334, version=0)
class Microsoft_Windows_MSDTC_2_53334_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )


@declare(guid=guid("5d9e0020-3761-4f36-90c8-38ce6511bd12"), event_id=53335, version=0)
class Microsoft_Windows_MSDTC_2_53335_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )


@declare(guid=guid("5d9e0020-3761-4f36-90c8-38ce6511bd12"), event_id=53336, version=0)
class Microsoft_Windows_MSDTC_2_53336_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString
    )


@declare(guid=guid("5d9e0020-3761-4f36-90c8-38ce6511bd12"), event_id=53337, version=0)
class Microsoft_Windows_MSDTC_2_53337_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString
    )


@declare(guid=guid("5d9e0020-3761-4f36-90c8-38ce6511bd12"), event_id=53338, version=0)
class Microsoft_Windows_MSDTC_2_53338_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString
    )


@declare(guid=guid("5d9e0020-3761-4f36-90c8-38ce6511bd12"), event_id=53339, version=0)
class Microsoft_Windows_MSDTC_2_53339_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString
    )

