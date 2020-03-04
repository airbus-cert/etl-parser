# -*- coding: utf-8 -*-
"""
Microsoft-Windows-SharedAccess_NAT
GUID : a6f32731-9a38-4159-a220-3d9b7fc5fe5d
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("a6f32731-9a38-4159-a220-3d9b7fc5fe5d"), event_id=30001, version=0)
class Microsoft_Windows_SharedAccess_NAT_30001_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("a6f32731-9a38-4159-a220-3d9b7fc5fe5d"), event_id=30002, version=0)
class Microsoft_Windows_SharedAccess_NAT_30002_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("a6f32731-9a38-4159-a220-3d9b7fc5fe5d"), event_id=30003, version=0)
class Microsoft_Windows_SharedAccess_NAT_30003_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("a6f32731-9a38-4159-a220-3d9b7fc5fe5d"), event_id=30004, version=0)
class Microsoft_Windows_SharedAccess_NAT_30004_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("a6f32731-9a38-4159-a220-3d9b7fc5fe5d"), event_id=30005, version=0)
class Microsoft_Windows_SharedAccess_NAT_30005_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("a6f32731-9a38-4159-a220-3d9b7fc5fe5d"), event_id=30006, version=0)
class Microsoft_Windows_SharedAccess_NAT_30006_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("a6f32731-9a38-4159-a220-3d9b7fc5fe5d"), event_id=30009, version=0)
class Microsoft_Windows_SharedAccess_NAT_30009_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("a6f32731-9a38-4159-a220-3d9b7fc5fe5d"), event_id=30010, version=0)
class Microsoft_Windows_SharedAccess_NAT_30010_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("a6f32731-9a38-4159-a220-3d9b7fc5fe5d"), event_id=30011, version=0)
class Microsoft_Windows_SharedAccess_NAT_30011_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("a6f32731-9a38-4159-a220-3d9b7fc5fe5d"), event_id=30012, version=0)
class Microsoft_Windows_SharedAccess_NAT_30012_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("a6f32731-9a38-4159-a220-3d9b7fc5fe5d"), event_id=30013, version=0)
class Microsoft_Windows_SharedAccess_NAT_30013_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )


@declare(guid=guid("a6f32731-9a38-4159-a220-3d9b7fc5fe5d"), event_id=31001, version=0)
class Microsoft_Windows_SharedAccess_NAT_31001_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("a6f32731-9a38-4159-a220-3d9b7fc5fe5d"), event_id=31002, version=0)
class Microsoft_Windows_SharedAccess_NAT_31002_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("a6f32731-9a38-4159-a220-3d9b7fc5fe5d"), event_id=31003, version=0)
class Microsoft_Windows_SharedAccess_NAT_31003_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("a6f32731-9a38-4159-a220-3d9b7fc5fe5d"), event_id=31004, version=0)
class Microsoft_Windows_SharedAccess_NAT_31004_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("a6f32731-9a38-4159-a220-3d9b7fc5fe5d"), event_id=31005, version=0)
class Microsoft_Windows_SharedAccess_NAT_31005_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("a6f32731-9a38-4159-a220-3d9b7fc5fe5d"), event_id=31006, version=0)
class Microsoft_Windows_SharedAccess_NAT_31006_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )


@declare(guid=guid("a6f32731-9a38-4159-a220-3d9b7fc5fe5d"), event_id=31009, version=0)
class Microsoft_Windows_SharedAccess_NAT_31009_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("a6f32731-9a38-4159-a220-3d9b7fc5fe5d"), event_id=31010, version=0)
class Microsoft_Windows_SharedAccess_NAT_31010_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("a6f32731-9a38-4159-a220-3d9b7fc5fe5d"), event_id=32001, version=0)
class Microsoft_Windows_SharedAccess_NAT_32001_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("a6f32731-9a38-4159-a220-3d9b7fc5fe5d"), event_id=32002, version=0)
class Microsoft_Windows_SharedAccess_NAT_32002_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("a6f32731-9a38-4159-a220-3d9b7fc5fe5d"), event_id=34002, version=0)
class Microsoft_Windows_SharedAccess_NAT_34002_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("a6f32731-9a38-4159-a220-3d9b7fc5fe5d"), event_id=34003, version=0)
class Microsoft_Windows_SharedAccess_NAT_34003_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("a6f32731-9a38-4159-a220-3d9b7fc5fe5d"), event_id=34004, version=0)
class Microsoft_Windows_SharedAccess_NAT_34004_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("a6f32731-9a38-4159-a220-3d9b7fc5fe5d"), event_id=34005, version=0)
class Microsoft_Windows_SharedAccess_NAT_34005_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("a6f32731-9a38-4159-a220-3d9b7fc5fe5d"), event_id=34006, version=0)
class Microsoft_Windows_SharedAccess_NAT_34006_0(Etw):
    pattern = Struct(
        "param1" / WString
    )

