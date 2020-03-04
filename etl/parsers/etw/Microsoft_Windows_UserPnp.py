# -*- coding: utf-8 -*-
"""
Microsoft-Windows-UserPnp
GUID : 96f4a050-7e31-453c-88be-9634f4e02139
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("96f4a050-7e31-453c-88be-9634f4e02139"), event_id=7550, version=0)
class Microsoft_Windows_UserPnp_7550_0(Etw):
    pattern = Struct(
        "DeviceId" / WString
    )


@declare(guid=guid("96f4a050-7e31-453c-88be-9634f4e02139"), event_id=7551, version=0)
class Microsoft_Windows_UserPnp_7551_0(Etw):
    pattern = Struct(
        "ThreadId" / Int32ul
    )


@declare(guid=guid("96f4a050-7e31-453c-88be-9634f4e02139"), event_id=7552, version=0)
class Microsoft_Windows_UserPnp_7552_0(Etw):
    pattern = Struct(
        "ThreadId" / Int32ul
    )


@declare(guid=guid("96f4a050-7e31-453c-88be-9634f4e02139"), event_id=7553, version=0)
class Microsoft_Windows_UserPnp_7553_0(Etw):
    pattern = Struct(
        "ThreadId" / Int32ul,
        "DeviceId" / WString
    )


@declare(guid=guid("96f4a050-7e31-453c-88be-9634f4e02139"), event_id=7554, version=0)
class Microsoft_Windows_UserPnp_7554_0(Etw):
    pattern = Struct(
        "ThreadId" / Int32ul
    )


@declare(guid=guid("96f4a050-7e31-453c-88be-9634f4e02139"), event_id=7555, version=0)
class Microsoft_Windows_UserPnp_7555_0(Etw):
    pattern = Struct(
        "ChildDevice" / WString,
        "ParentDevice" / WString
    )


@declare(guid=guid("96f4a050-7e31-453c-88be-9634f4e02139"), event_id=7556, version=0)
class Microsoft_Windows_UserPnp_7556_0(Etw):
    pattern = Struct(
        "DeviceId" / WString
    )


@declare(guid=guid("96f4a050-7e31-453c-88be-9634f4e02139"), event_id=7700, version=0)
class Microsoft_Windows_UserPnp_7700_0(Etw):
    pattern = Struct(
        "DIF_CODE" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("96f4a050-7e31-453c-88be-9634f4e02139"), event_id=7701, version=0)
class Microsoft_Windows_UserPnp_7701_0(Etw):
    pattern = Struct(
        "DIF_CODE" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("96f4a050-7e31-453c-88be-9634f4e02139"), event_id=7900, version=0)
class Microsoft_Windows_UserPnp_7900_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "Package" / WString,
        "ErrorCode" / Int32ul,
        "Win32ErrorCode" / Int32ul
    )


@declare(guid=guid("96f4a050-7e31-453c-88be-9634f4e02139"), event_id=7901, version=0)
class Microsoft_Windows_UserPnp_7901_0(Etw):
    pattern = Struct(
        "PackagePath" / WString
    )


@declare(guid=guid("96f4a050-7e31-453c-88be-9634f4e02139"), event_id=7902, version=0)
class Microsoft_Windows_UserPnp_7902_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "Package" / WString,
        "ErrorCode" / Int32ul,
        "Win32ErrorCode" / Int32ul
    )


@declare(guid=guid("96f4a050-7e31-453c-88be-9634f4e02139"), event_id=7903, version=0)
class Microsoft_Windows_UserPnp_7903_0(Etw):
    pattern = Struct(
        "File" / WString,
        "Language" / WString
    )


@declare(guid=guid("96f4a050-7e31-453c-88be-9634f4e02139"), event_id=7950, version=0)
class Microsoft_Windows_UserPnp_7950_0(Etw):
    pattern = Struct(
        "PackageName" / WString,
        "PackagePath" / WString
    )


@declare(guid=guid("96f4a050-7e31-453c-88be-9634f4e02139"), event_id=7951, version=0)
class Microsoft_Windows_UserPnp_7951_0(Etw):
    pattern = Struct(
        "QueryType" / WString,
        "LookupKey" / WString
    )


@declare(guid=guid("96f4a050-7e31-453c-88be-9634f4e02139"), event_id=7952, version=0)
class Microsoft_Windows_UserPnp_7952_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "NetworkErrorCode" / Int32ul,
        "HttpStatusCode" / Int32ul
    )


@declare(guid=guid("96f4a050-7e31-453c-88be-9634f4e02139"), event_id=8000, version=0)
class Microsoft_Windows_UserPnp_8000_0(Etw):
    pattern = Struct(
        "DeviceId" / WString
    )


@declare(guid=guid("96f4a050-7e31-453c-88be-9634f4e02139"), event_id=8007, version=0)
class Microsoft_Windows_UserPnp_8007_0(Etw):
    pattern = Struct(
        "DeviceId" / WString
    )


@declare(guid=guid("96f4a050-7e31-453c-88be-9634f4e02139"), event_id=8010, version=0)
class Microsoft_Windows_UserPnp_8010_0(Etw):
    pattern = Struct(
        "hc_stateid" / Int32ul
    )


@declare(guid=guid("96f4a050-7e31-453c-88be-9634f4e02139"), event_id=20001, version=0)
class Microsoft_Windows_UserPnp_20001_0(Etw):
    pattern = Struct(
        "DriverName" / WString,
        "DriverVersion" / WString,
        "DriverProvider" / WString,
        "DeviceInstanceID" / WString,
        "SetupClass" / Guid,
        "RebootOption" / Int8ul,
        "UpgradeDevice" / Int8ul,
        "IsDriverOEM" / Int8ul,
        "InstallStatus" / Int32ul,
        "DriverDescription" / WString
    )


@declare(guid=guid("96f4a050-7e31-453c-88be-9634f4e02139"), event_id=20002, version=0)
class Microsoft_Windows_UserPnp_20002_0(Etw):
    pattern = Struct(
        "DriverName" / WString,
        "DriverVersion" / WString,
        "DriverProvider" / WString,
        "DeviceInstanceID" / WString,
        "SetupClass" / Guid,
        "RebootOption" / Int8ul,
        "UpgradeDevice" / Int8ul,
        "IsDriverOEM" / Int8ul,
        "InstallStatus" / Int32ul,
        "DriverDescription" / WString
    )


@declare(guid=guid("96f4a050-7e31-453c-88be-9634f4e02139"), event_id=20003, version=0)
class Microsoft_Windows_UserPnp_20003_0(Etw):
    pattern = Struct(
        "ServiceName" / WString,
        "DriverFileName" / WString,
        "DeviceInstanceID" / WString,
        "PrimaryService" / Int8ul,
        "UpdateService" / Int8ul,
        "AddServiceStatus" / Int32ul
    )


@declare(guid=guid("96f4a050-7e31-453c-88be-9634f4e02139"), event_id=20004, version=0)
class Microsoft_Windows_UserPnp_20004_0(Etw):
    pattern = Struct(
        "ServiceName" / WString,
        "DriverFileName" / WString,
        "DeviceInstanceID" / WString,
        "PrimaryService" / Int8ul,
        "UpdateService" / Int8ul,
        "AddServiceStatus" / Int32ul
    )


@declare(guid=guid("96f4a050-7e31-453c-88be-9634f4e02139"), event_id=20005, version=0)
class Microsoft_Windows_UserPnp_20005_0(Etw):
    pattern = Struct(
        "DeviceId" / WString
    )


@declare(guid=guid("96f4a050-7e31-453c-88be-9634f4e02139"), event_id=20006, version=0)
class Microsoft_Windows_UserPnp_20006_0(Etw):
    pattern = Struct(
        "DeviceId" / WString
    )


@declare(guid=guid("96f4a050-7e31-453c-88be-9634f4e02139"), event_id=20007, version=0)
class Microsoft_Windows_UserPnp_20007_0(Etw):
    pattern = Struct(
        "DeviceId" / WString
    )


@declare(guid=guid("96f4a050-7e31-453c-88be-9634f4e02139"), event_id=20008, version=0)
class Microsoft_Windows_UserPnp_20008_0(Etw):
    pattern = Struct(
        "DeviceId" / WString
    )


@declare(guid=guid("96f4a050-7e31-453c-88be-9634f4e02139"), event_id=20009, version=0)
class Microsoft_Windows_UserPnp_20009_0(Etw):
    pattern = Struct(
        "RebootTime" / Int32ul
    )

