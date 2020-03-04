# -*- coding: utf-8 -*-
"""
Microsoft-Windows-PortableWorkspaces-Creator-Tool
GUID : 42d5f8cb-0d2b-4522-8059-c35a37c94a77
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("42d5f8cb-0d2b-4522-8059-c35a37c94a77"), event_id=14, version=0)
class Microsoft_Windows_PortableWorkspaces_Creator_Tool_14_0(Etw):
    pattern = Struct(
        "ProvisionCharacteristics" / Int32ul,
        "DeviceCharacteristics" / Int32ul,
        "WindowsImageCharacteristics" / Int32ul,
        "WindowsImageSizeInMb" / Int32ul
    )


@declare(guid=guid("42d5f8cb-0d2b-4522-8059-c35a37c94a77"), event_id=1000, version=0)
class Microsoft_Windows_PortableWorkspaces_Creator_Tool_1000_0(Etw):
    pattern = Struct(
        "FriendlyName" / WString,
        "Name" / WString,
        "DriveLetters" / WString,
        "Size" / Int64ul,
        "MediaType" / Int32ul
    )


@declare(guid=guid("42d5f8cb-0d2b-4522-8059-c35a37c94a77"), event_id=1001, version=0)
class Microsoft_Windows_PortableWorkspaces_Creator_Tool_1001_0(Etw):
    pattern = Struct(
        "Path" / WString,
        "Architecture" / Int32ul,
        "IsEnterprise" / Int8ul
    )


@declare(guid=guid("42d5f8cb-0d2b-4522-8059-c35a37c94a77"), event_id=1003, version=0)
class Microsoft_Windows_PortableWorkspaces_Creator_Tool_1003_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32sl
    )


@declare(guid=guid("42d5f8cb-0d2b-4522-8059-c35a37c94a77"), event_id=1006, version=0)
class Microsoft_Windows_PortableWorkspaces_Creator_Tool_1006_0(Etw):
    pattern = Struct(
        "Path" / WString
    )


@declare(guid=guid("42d5f8cb-0d2b-4522-8059-c35a37c94a77"), event_id=1010, version=0)
class Microsoft_Windows_PortableWorkspaces_Creator_Tool_1010_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32sl
    )

