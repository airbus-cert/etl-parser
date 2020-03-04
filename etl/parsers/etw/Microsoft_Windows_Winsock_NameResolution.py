# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Winsock-NameResolution
GUID : 55404e71-4db9-4deb-a5f5-8f86e46dde56
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("55404e71-4db9-4deb-a5f5-8f86e46dde56"), event_id=1000, version=0)
class Microsoft_Windows_Winsock_NameResolution_1000_0(Etw):
    pattern = Struct(
        "NodeName" / WString,
        "ServiceName" / WString,
        "Location" / Int32ul,
        "Flags" / Int32ul,
        "Family" / Int32ul,
        "SocketType" / Int32ul,
        "Protocol" / Int32ul
    )


@declare(guid=guid("55404e71-4db9-4deb-a5f5-8f86e46dde56"), event_id=1001, version=0)
class Microsoft_Windows_Winsock_NameResolution_1001_0(Etw):
    pattern = Struct(
        "NodeName" / WString,
        "Status" / Int32ul,
        "Result" / WString
    )


@declare(guid=guid("55404e71-4db9-4deb-a5f5-8f86e46dde56"), event_id=1002, version=0)
class Microsoft_Windows_Winsock_NameResolution_1002_0(Etw):
    pattern = Struct(
        "NodeName" / WString,
        "ServiceName" / WString,
        "Location" / Int32ul,
        "NameSpace" / Int32ul,
        "NameSpaceGuid" / Guid,
        "Flags" / Int32ul,
        "Family" / Int32ul,
        "SocketType" / Int32ul,
        "protocol" / Int32ul,
        "InterfaceIndex" / Int32ul,
        "TimeOutInSec" / Int32ul,
        "AsyncWithCallback" / Int32ul,
        "AsyncWithOverlapped" / Int32ul
    )


@declare(guid=guid("55404e71-4db9-4deb-a5f5-8f86e46dde56"), event_id=1003, version=0)
class Microsoft_Windows_Winsock_NameResolution_1003_0(Etw):
    pattern = Struct(
        "NodeName" / WString,
        "CancelHandle" / Int64ul
    )


@declare(guid=guid("55404e71-4db9-4deb-a5f5-8f86e46dde56"), event_id=1004, version=0)
class Microsoft_Windows_Winsock_NameResolution_1004_0(Etw):
    pattern = Struct(
        "NodeName" / WString,
        "Status" / Int32ul,
        "Result" / WString
    )


@declare(guid=guid("55404e71-4db9-4deb-a5f5-8f86e46dde56"), event_id=1005, version=0)
class Microsoft_Windows_Winsock_NameResolution_1005_0(Etw):
    pattern = Struct(
        "CancelHandle" / Int64ul,
        "Location" / Int32ul
    )


@declare(guid=guid("55404e71-4db9-4deb-a5f5-8f86e46dde56"), event_id=1006, version=0)
class Microsoft_Windows_Winsock_NameResolution_1006_0(Etw):
    pattern = Struct(
        "ProviderGUID" / Guid,
        "QueryName" / WString,
        "ServiceGUID" / Guid,
        "InterfaceIndex" / Int32ul,
        "ControlFlags" / Int32ul
    )


@declare(guid=guid("55404e71-4db9-4deb-a5f5-8f86e46dde56"), event_id=1007, version=0)
class Microsoft_Windows_Winsock_NameResolution_1007_0(Etw):
    pattern = Struct(
        "ProviderGUID" / Guid,
        "QueryName" / WString,
        "ServiceGUID" / Guid,
        "InterfaceIndex" / Int32ul,
        "ControlFlags" / Int32ul,
        "LookupHandle" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("55404e71-4db9-4deb-a5f5-8f86e46dde56"), event_id=1008, version=0)
class Microsoft_Windows_Winsock_NameResolution_1008_0(Etw):
    pattern = Struct(
        "ProviderGUID" / Guid,
        "ControlFlags" / Int32ul,
        "LookupHandle" / Int64ul
    )


@declare(guid=guid("55404e71-4db9-4deb-a5f5-8f86e46dde56"), event_id=1009, version=0)
class Microsoft_Windows_Winsock_NameResolution_1009_0(Etw):
    pattern = Struct(
        "ProviderGUID" / Guid,
        "ControlFlags" / Int32ul,
        "LookupHandle" / Int64ul,
        "Status" / Int32ul,
        "Result" / WString
    )


@declare(guid=guid("55404e71-4db9-4deb-a5f5-8f86e46dde56"), event_id=1010, version=0)
class Microsoft_Windows_Winsock_NameResolution_1010_0(Etw):
    pattern = Struct(
        "ProviderGUID" / Guid,
        "LookupHandle" / Int64ul
    )


@declare(guid=guid("55404e71-4db9-4deb-a5f5-8f86e46dde56"), event_id=1011, version=0)
class Microsoft_Windows_Winsock_NameResolution_1011_0(Etw):
    pattern = Struct(
        "ProviderGUID" / Guid,
        "LookupHandle" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("55404e71-4db9-4deb-a5f5-8f86e46dde56"), event_id=1012, version=0)
class Microsoft_Windows_Winsock_NameResolution_1012_0(Etw):
    pattern = Struct(
        "NodeName" / WString,
        "ServiceName" / WString,
        "Location" / Int32ul,
        "NameSpace" / Int32ul,
        "NameSpaceGuid" / Guid,
        "Flags" / Int32ul,
        "Family" / Int32ul,
        "SocketType" / Int32ul,
        "protocol" / Int32ul,
        "InterfaceIndex" / Int32ul,
        "TimeOutInSec" / Int32ul,
        "AsyncWithCallback" / Int32ul,
        "AsyncWithOverlapped" / Int32ul,
        "Error" / Int32sl
    )


@declare(guid=guid("55404e71-4db9-4deb-a5f5-8f86e46dde56"), event_id=1013, version=0)
class Microsoft_Windows_Winsock_NameResolution_1013_0(Etw):
    pattern = Struct(
        "Location" / Int32ul
    )


@declare(guid=guid("55404e71-4db9-4deb-a5f5-8f86e46dde56"), event_id=1014, version=0)
class Microsoft_Windows_Winsock_NameResolution_1014_0(Etw):
    pattern = Struct(
        "Location" / Int32ul,
        "RefCount" / Int32ul
    )


@declare(guid=guid("55404e71-4db9-4deb-a5f5-8f86e46dde56"), event_id=1015, version=0)
class Microsoft_Windows_Winsock_NameResolution_1015_0(Etw):
    pattern = Struct(
        "Location" / Int32ul,
        "RefCount" / Int32ul
    )

