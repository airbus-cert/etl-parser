# -*- coding: utf-8 -*-
"""
Microsoft-Windows-AxInstallService
GUID : dab3b18c-3c0f-43e8-80b1-e44bc0dad901
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("dab3b18c-3c0f-43e8-80b1-e44bc0dad901"), event_id=1, version=0)
class Microsoft_Windows_AxInstallService_1_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("dab3b18c-3c0f-43e8-80b1-e44bc0dad901"), event_id=2, version=0)
class Microsoft_Windows_AxInstallService_2_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("dab3b18c-3c0f-43e8-80b1-e44bc0dad901"), event_id=3, version=0)
class Microsoft_Windows_AxInstallService_3_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("dab3b18c-3c0f-43e8-80b1-e44bc0dad901"), event_id=4, version=0)
class Microsoft_Windows_AxInstallService_4_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("dab3b18c-3c0f-43e8-80b1-e44bc0dad901"), event_id=5, version=0)
class Microsoft_Windows_AxInstallService_5_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("dab3b18c-3c0f-43e8-80b1-e44bc0dad901"), event_id=6, version=0)
class Microsoft_Windows_AxInstallService_6_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("dab3b18c-3c0f-43e8-80b1-e44bc0dad901"), event_id=7, version=0)
class Microsoft_Windows_AxInstallService_7_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("dab3b18c-3c0f-43e8-80b1-e44bc0dad901"), event_id=8, version=0)
class Microsoft_Windows_AxInstallService_8_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("dab3b18c-3c0f-43e8-80b1-e44bc0dad901"), event_id=4097, version=0)
class Microsoft_Windows_AxInstallService_4097_0(Etw):
    pattern = Struct(
        "URL" / WString,
        "HostName" / WString
    )


@declare(guid=guid("dab3b18c-3c0f-43e8-80b1-e44bc0dad901"), event_id=4098, version=0)
class Microsoft_Windows_AxInstallService_4098_0(Etw):
    pattern = Struct(
        "URL" / WString,
        "HostName" / WString
    )


@declare(guid=guid("dab3b18c-3c0f-43e8-80b1-e44bc0dad901"), event_id=4099, version=0)
class Microsoft_Windows_AxInstallService_4099_0(Etw):
    pattern = Struct(
        "URL" / WString,
        "HostName" / WString
    )


@declare(guid=guid("dab3b18c-3c0f-43e8-80b1-e44bc0dad901"), event_id=4100, version=0)
class Microsoft_Windows_AxInstallService_4100_0(Etw):
    pattern = Struct(
        "URL" / WString,
        "HostName" / WString
    )

