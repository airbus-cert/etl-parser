# -*- coding: utf-8 -*-
"""
Microsoft-Windows-AppXDeployment
GUID : 8127f6d4-59f9-4abf-8952-3e3a02073d5f
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("8127f6d4-59f9-4abf-8952-3e3a02073d5f"), event_id=302, version=0)
class Microsoft_Windows_AppXDeployment_302_0(Etw):
    pattern = Struct(
        "ServiceName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("8127f6d4-59f9-4abf-8952-3e3a02073d5f"), event_id=303, version=0)
class Microsoft_Windows_AppXDeployment_303_0(Etw):
    pattern = Struct(
        "ServiceName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("8127f6d4-59f9-4abf-8952-3e3a02073d5f"), event_id=304, version=0)
class Microsoft_Windows_AppXDeployment_304_0(Etw):
    pattern = Struct(
        "RecoveryType" / Int32ul
    )


@declare(guid=guid("8127f6d4-59f9-4abf-8952-3e3a02073d5f"), event_id=305, version=0)
class Microsoft_Windows_AppXDeployment_305_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("8127f6d4-59f9-4abf-8952-3e3a02073d5f"), event_id=306, version=0)
class Microsoft_Windows_AppXDeployment_306_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString
    )


@declare(guid=guid("8127f6d4-59f9-4abf-8952-3e3a02073d5f"), event_id=307, version=0)
class Microsoft_Windows_AppXDeployment_307_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "PackageFullName" / WString
    )


@declare(guid=guid("8127f6d4-59f9-4abf-8952-3e3a02073d5f"), event_id=309, version=0)
class Microsoft_Windows_AppXDeployment_309_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("8127f6d4-59f9-4abf-8952-3e3a02073d5f"), event_id=310, version=0)
class Microsoft_Windows_AppXDeployment_310_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("8127f6d4-59f9-4abf-8952-3e3a02073d5f"), event_id=311, version=0)
class Microsoft_Windows_AppXDeployment_311_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("8127f6d4-59f9-4abf-8952-3e3a02073d5f"), event_id=312, version=0)
class Microsoft_Windows_AppXDeployment_312_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "ErrorCode" / Int32ul,
        "Size" / Int64ul,
        "Offset" / Int32ul,
        "HeaderAddr" / Int64ul,
        "Section" / WString,
        "ProcessId" / Int32ul
    )


@declare(guid=guid("8127f6d4-59f9-4abf-8952-3e3a02073d5f"), event_id=313, version=0)
class Microsoft_Windows_AppXDeployment_313_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "ErrorCode" / Int32ul,
        "Size" / Int64ul,
        "HeaderAddr" / Int64ul,
        "Section" / WString,
        "ProcessId" / Int32ul
    )


@declare(guid=guid("8127f6d4-59f9-4abf-8952-3e3a02073d5f"), event_id=314, version=0)
class Microsoft_Windows_AppXDeployment_314_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "ErrorCode" / Int32ul,
        "Size" / Int64ul,
        "Offset" / Int32ul,
        "HeaderAddr" / Int64ul,
        "Section" / WString,
        "ProcessId" / Int32ul
    )


@declare(guid=guid("8127f6d4-59f9-4abf-8952-3e3a02073d5f"), event_id=315, version=0)
class Microsoft_Windows_AppXDeployment_315_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "ErrorCode" / Int32ul,
        "Size" / Int64ul,
        "Offset" / Int32ul,
        "HeaderAddr" / Int64ul,
        "Section" / WString,
        "ProcessId" / Int32ul
    )


@declare(guid=guid("8127f6d4-59f9-4abf-8952-3e3a02073d5f"), event_id=316, version=0)
class Microsoft_Windows_AppXDeployment_316_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "ErrorCode" / Int32ul,
        "ProcessId" / Int32ul
    )


@declare(guid=guid("8127f6d4-59f9-4abf-8952-3e3a02073d5f"), event_id=317, version=0)
class Microsoft_Windows_AppXDeployment_317_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "ExceptionCode" / Int32sl
    )


@declare(guid=guid("8127f6d4-59f9-4abf-8952-3e3a02073d5f"), event_id=318, version=0)
class Microsoft_Windows_AppXDeployment_318_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "ErrorCode" / Int32sl,
        "Size" / Int64ul,
        "HeaderAddr" / Int64ul,
        "ApplicationUserModelId" / WString,
        "ProcessId" / Int32ul
    )


@declare(guid=guid("8127f6d4-59f9-4abf-8952-3e3a02073d5f"), event_id=319, version=0)
class Microsoft_Windows_AppXDeployment_319_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "ErrorCode" / Int32sl,
        "Size" / Int64ul,
        "HeaderAddr" / Int64ul,
        "ProcessId" / Int32ul
    )


@declare(guid=guid("8127f6d4-59f9-4abf-8952-3e3a02073d5f"), event_id=320, version=0)
class Microsoft_Windows_AppXDeployment_320_0(Etw):
    pattern = Struct(
        "PackageName" / WString,
        "UserSid" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("8127f6d4-59f9-4abf-8952-3e3a02073d5f"), event_id=321, version=0)
class Microsoft_Windows_AppXDeployment_321_0(Etw):
    pattern = Struct(
        "PackageName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("8127f6d4-59f9-4abf-8952-3e3a02073d5f"), event_id=322, version=0)
class Microsoft_Windows_AppXDeployment_322_0(Etw):
    pattern = Struct(
        "PackageName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("8127f6d4-59f9-4abf-8952-3e3a02073d5f"), event_id=324, version=0)
class Microsoft_Windows_AppXDeployment_324_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "ErrorCode" / Int32sl,
        "Type" / WString,
        "ProcessId" / Int32ul
    )


@declare(guid=guid("8127f6d4-59f9-4abf-8952-3e3a02073d5f"), event_id=325, version=0)
class Microsoft_Windows_AppXDeployment_325_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString
    )


@declare(guid=guid("8127f6d4-59f9-4abf-8952-3e3a02073d5f"), event_id=326, version=0)
class Microsoft_Windows_AppXDeployment_326_0(Etw):
    pattern = Struct(
        "UserSid" / WString,
        "IsSpecialUserProfile" / Int8ul
    )


@declare(guid=guid("8127f6d4-59f9-4abf-8952-3e3a02073d5f"), event_id=327, version=0)
class Microsoft_Windows_AppXDeployment_327_0(Etw):
    pattern = Struct(
        "InstallPackageList" / WString,
        "RemovePackageList" / WString
    )


@declare(guid=guid("8127f6d4-59f9-4abf-8952-3e3a02073d5f"), event_id=328, version=0)
class Microsoft_Windows_AppXDeployment_328_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("8127f6d4-59f9-4abf-8952-3e3a02073d5f"), event_id=1033, version=0)
class Microsoft_Windows_AppXDeployment_1033_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )

