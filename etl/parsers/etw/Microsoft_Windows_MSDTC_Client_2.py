# -*- coding: utf-8 -*-
"""
Microsoft-Windows-MSDTC Client 2
GUID : 155cb334-3d7f-4ff1-b107-df8afc3c0363
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("155cb334-3d7f-4ff1-b107-df8afc3c0363"), event_id=4097, version=0)
class Microsoft_Windows_MSDTC_Client_2_4097_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("155cb334-3d7f-4ff1-b107-df8afc3c0363"), event_id=4098, version=0)
class Microsoft_Windows_MSDTC_Client_2_4098_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )


@declare(guid=guid("155cb334-3d7f-4ff1-b107-df8afc3c0363"), event_id=4099, version=0)
class Microsoft_Windows_MSDTC_Client_2_4099_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("155cb334-3d7f-4ff1-b107-df8afc3c0363"), event_id=4100, version=0)
class Microsoft_Windows_MSDTC_Client_2_4100_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("155cb334-3d7f-4ff1-b107-df8afc3c0363"), event_id=4101, version=0)
class Microsoft_Windows_MSDTC_Client_2_4101_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )


@declare(guid=guid("155cb334-3d7f-4ff1-b107-df8afc3c0363"), event_id=4102, version=0)
class Microsoft_Windows_MSDTC_Client_2_4102_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("155cb334-3d7f-4ff1-b107-df8afc3c0363"), event_id=4103, version=0)
class Microsoft_Windows_MSDTC_Client_2_4103_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("155cb334-3d7f-4ff1-b107-df8afc3c0363"), event_id=4104, version=0)
class Microsoft_Windows_MSDTC_Client_2_4104_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("155cb334-3d7f-4ff1-b107-df8afc3c0363"), event_id=4350, version=0)
class Microsoft_Windows_MSDTC_Client_2_4350_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )


@declare(guid=guid("155cb334-3d7f-4ff1-b107-df8afc3c0363"), event_id=4874, version=0)
class Microsoft_Windows_MSDTC_Client_2_4874_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("155cb334-3d7f-4ff1-b107-df8afc3c0363"), event_id=4875, version=0)
class Microsoft_Windows_MSDTC_Client_2_4875_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("155cb334-3d7f-4ff1-b107-df8afc3c0363"), event_id=4876, version=0)
class Microsoft_Windows_MSDTC_Client_2_4876_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("155cb334-3d7f-4ff1-b107-df8afc3c0363"), event_id=4878, version=0)
class Microsoft_Windows_MSDTC_Client_2_4878_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )


@declare(guid=guid("155cb334-3d7f-4ff1-b107-df8afc3c0363"), event_id=4879, version=0)
class Microsoft_Windows_MSDTC_Client_2_4879_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("155cb334-3d7f-4ff1-b107-df8afc3c0363"), event_id=4881, version=0)
class Microsoft_Windows_MSDTC_Client_2_4881_0(Etw):
    pattern = Struct(
        "param1" / WString
    )

