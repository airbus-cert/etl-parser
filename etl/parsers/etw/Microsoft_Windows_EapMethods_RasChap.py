# -*- coding: utf-8 -*-
"""
Microsoft-Windows-EapMethods-RasChap
GUID : 58980f4b-bd39-4a3e-b344-492ed2254a4e
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("58980f4b-bd39-4a3e-b344-492ed2254a4e"), event_id=100, version=0)
class Microsoft_Windows_EapMethods_RasChap_100_0(Etw):
    pattern = Struct(
        "Domain" / CString,
        "Username" / CString
    )


@declare(guid=guid("58980f4b-bd39-4a3e-b344-492ed2254a4e"), event_id=101, version=0)
class Microsoft_Windows_EapMethods_RasChap_101_0(Etw):
    pattern = Struct(
        "Domain" / CString,
        "Username" / CString,
        "int1" / Int32ul
    )


@declare(guid=guid("58980f4b-bd39-4a3e-b344-492ed2254a4e"), event_id=102, version=0)
class Microsoft_Windows_EapMethods_RasChap_102_0(Etw):
    pattern = Struct(
        "Domain" / CString,
        "Username" / CString
    )


@declare(guid=guid("58980f4b-bd39-4a3e-b344-492ed2254a4e"), event_id=103, version=0)
class Microsoft_Windows_EapMethods_RasChap_103_0(Etw):
    pattern = Struct(
        "Domain" / CString,
        "Username" / CString
    )


@declare(guid=guid("58980f4b-bd39-4a3e-b344-492ed2254a4e"), event_id=104, version=0)
class Microsoft_Windows_EapMethods_RasChap_104_0(Etw):
    pattern = Struct(
        "Domain" / CString,
        "Username" / CString
    )


@declare(guid=guid("58980f4b-bd39-4a3e-b344-492ed2254a4e"), event_id=105, version=0)
class Microsoft_Windows_EapMethods_RasChap_105_0(Etw):
    pattern = Struct(
        "Domain" / CString,
        "Username" / CString
    )


@declare(guid=guid("58980f4b-bd39-4a3e-b344-492ed2254a4e"), event_id=106, version=0)
class Microsoft_Windows_EapMethods_RasChap_106_0(Etw):
    pattern = Struct(
        "Domain" / CString,
        "Username" / CString
    )


@declare(guid=guid("58980f4b-bd39-4a3e-b344-492ed2254a4e"), event_id=107, version=0)
class Microsoft_Windows_EapMethods_RasChap_107_0(Etw):
    pattern = Struct(
        "Domain" / CString,
        "Username" / CString
    )

