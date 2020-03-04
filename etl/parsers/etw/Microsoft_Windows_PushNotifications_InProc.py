# -*- coding: utf-8 -*-
"""
Microsoft-Windows-PushNotifications-InProc
GUID : 815a1f4a-3f8d-4b37-9b31-5142f9d724a5
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("815a1f4a-3f8d-4b37-9b31-5142f9d724a5"), event_id=1, version=0)
class Microsoft_Windows_PushNotifications_InProc_1_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "FunctionName" / WString,
        "LineNumber" / Int32sl,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("815a1f4a-3f8d-4b37-9b31-5142f9d724a5"), event_id=100, version=0)
class Microsoft_Windows_PushNotifications_InProc_100_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString
    )


@declare(guid=guid("815a1f4a-3f8d-4b37-9b31-5142f9d724a5"), event_id=101, version=0)
class Microsoft_Windows_PushNotifications_InProc_101_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "AppUserModelId" / WString,
        "SettingValue" / Int8ul
    )


@declare(guid=guid("815a1f4a-3f8d-4b37-9b31-5142f9d724a5"), event_id=102, version=0)
class Microsoft_Windows_PushNotifications_InProc_102_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "NumApps" / Int32ul
    )


@declare(guid=guid("815a1f4a-3f8d-4b37-9b31-5142f9d724a5"), event_id=103, version=0)
class Microsoft_Windows_PushNotifications_InProc_103_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "AppUserModelId" / WString,
        "SettingValue" / Int8ul
    )


@declare(guid=guid("815a1f4a-3f8d-4b37-9b31-5142f9d724a5"), event_id=104, version=0)
class Microsoft_Windows_PushNotifications_InProc_104_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "AppUserModelId" / WString
    )


@declare(guid=guid("815a1f4a-3f8d-4b37-9b31-5142f9d724a5"), event_id=105, version=0)
class Microsoft_Windows_PushNotifications_InProc_105_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "AppUserModelId" / WString
    )


@declare(guid=guid("815a1f4a-3f8d-4b37-9b31-5142f9d724a5"), event_id=106, version=0)
class Microsoft_Windows_PushNotifications_InProc_106_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "NumApps" / Int32ul
    )

