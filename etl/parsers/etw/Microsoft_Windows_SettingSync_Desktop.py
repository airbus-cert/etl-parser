# -*- coding: utf-8 -*-
"""
Microsoft-Windows-SettingSync-Desktop
GUID : 579402a2-883c-45d8-b70a-9bc856407751
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("579402a2-883c-45d8-b70a-9bc856407751"), event_id=5001, version=0)
class Microsoft_Windows_SettingSync_Desktop_5001_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "Operation" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("579402a2-883c-45d8-b70a-9bc856407751"), event_id=5002, version=0)
class Microsoft_Windows_SettingSync_Desktop_5002_0(Etw):
    pattern = Struct(
        "SettingUnitId" / WString,
        "CollectionId" / WString,
        "Operation" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("579402a2-883c-45d8-b70a-9bc856407751"), event_id=5003, version=0)
class Microsoft_Windows_SettingSync_Desktop_5003_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("579402a2-883c-45d8-b70a-9bc856407751"), event_id=5004, version=0)
class Microsoft_Windows_SettingSync_Desktop_5004_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("579402a2-883c-45d8-b70a-9bc856407751"), event_id=5005, version=0)
class Microsoft_Windows_SettingSync_Desktop_5005_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("579402a2-883c-45d8-b70a-9bc856407751"), event_id=5006, version=0)
class Microsoft_Windows_SettingSync_Desktop_5006_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("579402a2-883c-45d8-b70a-9bc856407751"), event_id=5007, version=0)
class Microsoft_Windows_SettingSync_Desktop_5007_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("579402a2-883c-45d8-b70a-9bc856407751"), event_id=5008, version=0)
class Microsoft_Windows_SettingSync_Desktop_5008_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("579402a2-883c-45d8-b70a-9bc856407751"), event_id=5009, version=0)
class Microsoft_Windows_SettingSync_Desktop_5009_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("579402a2-883c-45d8-b70a-9bc856407751"), event_id=6001, version=0)
class Microsoft_Windows_SettingSync_Desktop_6001_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("579402a2-883c-45d8-b70a-9bc856407751"), event_id=6002, version=0)
class Microsoft_Windows_SettingSync_Desktop_6002_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("579402a2-883c-45d8-b70a-9bc856407751"), event_id=6501, version=0)
class Microsoft_Windows_SettingSync_Desktop_6501_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("579402a2-883c-45d8-b70a-9bc856407751"), event_id=6502, version=0)
class Microsoft_Windows_SettingSync_Desktop_6502_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("579402a2-883c-45d8-b70a-9bc856407751"), event_id=6503, version=0)
class Microsoft_Windows_SettingSync_Desktop_6503_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("579402a2-883c-45d8-b70a-9bc856407751"), event_id=6509, version=0)
class Microsoft_Windows_SettingSync_Desktop_6509_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("579402a2-883c-45d8-b70a-9bc856407751"), event_id=6510, version=0)
class Microsoft_Windows_SettingSync_Desktop_6510_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("579402a2-883c-45d8-b70a-9bc856407751"), event_id=6511, version=0)
class Microsoft_Windows_SettingSync_Desktop_6511_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("579402a2-883c-45d8-b70a-9bc856407751"), event_id=7007, version=0)
class Microsoft_Windows_SettingSync_Desktop_7007_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )


@declare(guid=guid("579402a2-883c-45d8-b70a-9bc856407751"), event_id=7008, version=0)
class Microsoft_Windows_SettingSync_Desktop_7008_0(Etw):
    pattern = Struct(
        "Quality" / Int32ul
    )


@declare(guid=guid("579402a2-883c-45d8-b70a-9bc856407751"), event_id=7010, version=0)
class Microsoft_Windows_SettingSync_Desktop_7010_0(Etw):
    pattern = Struct(
        "OrigSizeX" / Int32ul,
        "OrigSizeY" / Int32ul
    )


@declare(guid=guid("579402a2-883c-45d8-b70a-9bc856407751"), event_id=7012, version=0)
class Microsoft_Windows_SettingSync_Desktop_7012_0(Etw):
    pattern = Struct(
        "CollectionId" / WString
    )

