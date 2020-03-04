# -*- coding: utf-8 -*-
"""
Microsoft-Windows-VPN-Client
GUID : 3c088e51-65be-40d1-9b90-62bfec076737
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("3c088e51-65be-40d1-9b90-62bfec076737"), event_id=10001, version=0)
class Microsoft_Windows_VPN_Client_10001_0(Etw):
    pattern = Struct(
        "VpnConnectionName" / WString,
        "PropertiesString" / WString
    )


@declare(guid=guid("3c088e51-65be-40d1-9b90-62bfec076737"), event_id=10002, version=0)
class Microsoft_Windows_VPN_Client_10002_0(Etw):
    pattern = Struct(
        "VpnConnectionName" / WString,
        "ErrorCode" / Int32ul,
        "PropertiesString" / WString
    )


@declare(guid=guid("3c088e51-65be-40d1-9b90-62bfec076737"), event_id=10003, version=0)
class Microsoft_Windows_VPN_Client_10003_0(Etw):
    pattern = Struct(
        "VpnConnectionName" / WString
    )


@declare(guid=guid("3c088e51-65be-40d1-9b90-62bfec076737"), event_id=10004, version=0)
class Microsoft_Windows_VPN_Client_10004_0(Etw):
    pattern = Struct(
        "VpnConnectionName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("3c088e51-65be-40d1-9b90-62bfec076737"), event_id=10005, version=0)
class Microsoft_Windows_VPN_Client_10005_0(Etw):
    pattern = Struct(
        "VpnConnectionName" / WString,
        "PropertiesString" / WString
    )


@declare(guid=guid("3c088e51-65be-40d1-9b90-62bfec076737"), event_id=10006, version=0)
class Microsoft_Windows_VPN_Client_10006_0(Etw):
    pattern = Struct(
        "VpnConnectionName" / WString,
        "ErrorCode" / Int32ul,
        "PropertiesString" / WString
    )


@declare(guid=guid("3c088e51-65be-40d1-9b90-62bfec076737"), event_id=10007, version=0)
class Microsoft_Windows_VPN_Client_10007_0(Etw):
    pattern = Struct(
        "VpnConnectionName" / WString,
        "PropertiesString" / WString,
        "PropertiesNotUpdatedString" / WString
    )


@declare(guid=guid("3c088e51-65be-40d1-9b90-62bfec076737"), event_id=10008, version=0)
class Microsoft_Windows_VPN_Client_10008_0(Etw):
    pattern = Struct(
        "VpnConnectionName" / WString,
        "PropertiesString" / WString,
        "PropertiesNotUpdatedString" / WString
    )

