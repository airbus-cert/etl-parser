# -*- coding: utf-8 -*-
"""
Microsoft-Windows-WLAN-AutoConfig
GUID : 9580d7dd-0379-4658-9870-d5be7d52d6de
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=4002, version=0)
class Microsoft_Windows_WLAN_AutoConfig_4002_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=4003, version=0)
class Microsoft_Windows_WLAN_AutoConfig_4003_0(Etw):
    pattern = Struct(
        "Event" / Int32ul,
        "ErrorCode" / Int32ul,
        "ChangeReason" / Int32ul,
        "IpFamily" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=8000, version=0)
class Microsoft_Windows_WLAN_AutoConfig_8000_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString,
        "ConnectionMode" / WString,
        "ProfileName" / WString,
        "SSID" / WString,
        "BSSType" / WString,
        "ConnectionId" / Int64ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=8001, version=0)
class Microsoft_Windows_WLAN_AutoConfig_8001_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString,
        "ConnectionMode" / WString,
        "ProfileName" / WString,
        "SSID" / WString,
        "BSSType" / WString,
        "PHYType" / WString,
        "AuthenticationAlgorithm" / WString,
        "CipherAlgorithm" / WString,
        "OnexEnabled" / Int32ul,
        "ConnectionId" / Int64ul,
        "NonBroadcast" / Int8ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=8002, version=0)
class Microsoft_Windows_WLAN_AutoConfig_8002_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString,
        "ConnectionMode" / WString,
        "ProfileName" / WString,
        "SSID" / WString,
        "BSSType" / WString,
        "FailureReason" / WString,
        "ReasonCode" / Int32ul,
        "ConnectionId" / Int64ul,
        "RSSI" / Int32sl
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=8003, version=0)
class Microsoft_Windows_WLAN_AutoConfig_8003_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString,
        "ConnectionMode" / WString,
        "ProfileName" / WString,
        "SSID" / WString,
        "BSSType" / WString,
        "Reason" / WString,
        "ConnectionId" / Int64ul,
        "ReasonCode" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=8004, version=0)
class Microsoft_Windows_WLAN_AutoConfig_8004_0(Etw):
    pattern = Struct(
        "InterfaceDescription" / WString,
        "InterfaceGuid" / Guid,
        "SSIDs" / WString,
        "ProfileName" / WString,
        "ConnectionMode" / WString,
        "BSSType" / WString,
        "FailureReason" / WString,
        "BlockTime" / Int32ul,
        "ReasonCode" / Int32ul,
        "ConnectionId" / Int64ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=8005, version=0)
class Microsoft_Windows_WLAN_AutoConfig_8005_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "SSID" / CString
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=8006, version=0)
class Microsoft_Windows_WLAN_AutoConfig_8006_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "SSID" / CString
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=8007, version=0)
class Microsoft_Windows_WLAN_AutoConfig_8007_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "ErrorCode" / Int32ul,
        "ErrorMsg" / WString,
        "SSID" / CString
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=8008, version=0)
class Microsoft_Windows_WLAN_AutoConfig_8008_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "SSID" / CString
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=8009, version=0)
class Microsoft_Windows_WLAN_AutoConfig_8009_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "SSID" / CString
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=8010, version=0)
class Microsoft_Windows_WLAN_AutoConfig_8010_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "ErrorCode" / Int32ul,
        "ErrorMsg" / WString,
        "SSID" / CString
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=8011, version=0)
class Microsoft_Windows_WLAN_AutoConfig_8011_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString,
        "ProfileName" / WString,
        "SSID" / WString,
        "BSSType" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=8012, version=0)
class Microsoft_Windows_WLAN_AutoConfig_8012_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=10000, version=0)
class Microsoft_Windows_WLAN_AutoConfig_10000_0(Etw):
    pattern = Struct(
        "ExtensibleModulePath" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=10001, version=0)
class Microsoft_Windows_WLAN_AutoConfig_10001_0(Etw):
    pattern = Struct(
        "ExtensibleModulePath" / WString
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=10002, version=0)
class Microsoft_Windows_WLAN_AutoConfig_10002_0(Etw):
    pattern = Struct(
        "ExtensibleModulePath" / WString
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=10003, version=0)
class Microsoft_Windows_WLAN_AutoConfig_10003_0(Etw):
    pattern = Struct(
        "ExtensibleModulePath" / WString
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=10004, version=0)
class Microsoft_Windows_WLAN_AutoConfig_10004_0(Etw):
    pattern = Struct(
        "ExtensibleModulePath" / WString
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=11000, version=0)
class Microsoft_Windows_WLAN_AutoConfig_11000_0(Etw):
    pattern = Struct(
        "Adapter" / WString,
        "DeviceGuid" / Guid,
        "LocalMac" / WString,
        "SSID" / WString,
        "BSSType" / WString,
        "Auth" / WString,
        "Cipher" / WString,
        "OnexEnabled" / Int32ul,
        "IhvConnectivitySetting" / WString,
        "ConnectionId" / Int64ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=11001, version=0)
class Microsoft_Windows_WLAN_AutoConfig_11001_0(Etw):
    pattern = Struct(
        "Adapter" / WString,
        "DeviceGuid" / Guid,
        "LocalMac" / WString,
        "SSID" / WString,
        "BSSType" / WString,
        "ConnectionId" / Int64ul,
        "MgmtFrameProtection" / Int8ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=11002, version=0)
class Microsoft_Windows_WLAN_AutoConfig_11002_0(Etw):
    pattern = Struct(
        "Adapter" / WString,
        "DeviceGuid" / Guid,
        "LocalMac" / WString,
        "SSID" / WString,
        "BSSType" / WString,
        "FailureReason" / WString,
        "ReasonCode" / Int32ul,
        "Dot11StatusCode" / Int32ul,
        "ConnectionId" / Int64ul,
        "RSSI" / Int32sl
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=11003, version=0)
class Microsoft_Windows_WLAN_AutoConfig_11003_0(Etw):
    pattern = Struct(
        "Adapter" / WString,
        "DeviceGuid" / Guid,
        "LocalMac" / WString,
        "SSID" / WString,
        "BSSType" / WString,
        "Auth" / WString,
        "AuthVal" / Int32ul,
        "Cipher" / WString,
        "CipherVal" / Int32ul,
        "FIPSMode" / Int32ul,
        "OnexEnabled" / Int32ul,
        "ConnectionId" / Int64ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=11004, version=0)
class Microsoft_Windows_WLAN_AutoConfig_11004_0(Etw):
    pattern = Struct(
        "Adapter" / WString,
        "DeviceGuid" / Guid,
        "LocalMac" / WString,
        "SSID" / WString,
        "BSSType" / WString,
        "SecurityHint" / WString,
        "SecurityHintCode" / Int32ul,
        "ConnectionId" / Int64ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=11005, version=0)
class Microsoft_Windows_WLAN_AutoConfig_11005_0(Etw):
    pattern = Struct(
        "Adapter" / WString,
        "DeviceGuid" / Guid,
        "LocalMac" / WString,
        "SSID" / WString,
        "BSSType" / WString,
        "ConnectionId" / Int64ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=11006, version=0)
class Microsoft_Windows_WLAN_AutoConfig_11006_0(Etw):
    pattern = Struct(
        "Adapter" / WString,
        "DeviceGuid" / Guid,
        "LocalMac" / WString,
        "SSID" / WString,
        "BSSType" / WString,
        "PeerMac" / WString,
        "ReasonText" / WString,
        "ReasonCode" / Int32ul,
        "ErrorCode" / Int32ul,
        "ConnectionId" / Int64ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=11007, version=0)
class Microsoft_Windows_WLAN_AutoConfig_11007_0(Etw):
    pattern = Struct(
        "Adapter" / WString,
        "DeviceGuid" / Guid,
        "LocalMac" / WString,
        "SSID" / WString,
        "BSSType" / WString,
        "IhvSecuritySetting" / WString,
        "ConnectionId" / Int64ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=11008, version=0)
class Microsoft_Windows_WLAN_AutoConfig_11008_0(Etw):
    pattern = Struct(
        "Adapter" / WString,
        "DeviceGuid" / Guid,
        "LocalMac" / WString,
        "SSID" / WString,
        "BSSType" / WString,
        "ConnectionId" / Int64ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=11009, version=0)
class Microsoft_Windows_WLAN_AutoConfig_11009_0(Etw):
    pattern = Struct(
        "Adapter" / WString,
        "DeviceGuid" / Guid,
        "LocalMac" / WString,
        "SSID" / WString,
        "BSSType" / WString,
        "PeerMac" / WString,
        "IhvReasonCode" / Int32ul,
        "IhvDataLength" / Int32ul,
        "ConnectionId" / Int64ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=11010, version=0)
class Microsoft_Windows_WLAN_AutoConfig_11010_0(Etw):
    pattern = Struct(
        "Adapter" / WString,
        "DeviceGuid" / Guid,
        "LocalMac" / WString,
        "SSID" / WString,
        "BSSType" / WString,
        "Auth" / WString,
        "AuthVal" / Int32ul,
        "Cipher" / WString,
        "CipherVal" / Int32ul,
        "FIPSMode" / Int32ul,
        "OnexEnabled" / Int32ul,
        "ConnectionId" / Int64ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=12011, version=0)
class Microsoft_Windows_WLAN_AutoConfig_12011_0(Etw):
    pattern = Struct(
        "Adapter" / WString,
        "DeviceGuid" / Guid,
        "LocalMac" / WString,
        "SSID" / WString,
        "BSSType" / WString,
        "EapType" / Int32ul,
        "VendorID" / Int32ul,
        "VendorType" / Int32ul,
        "AuthorID" / Int32ul,
        "ConnectionId" / Int64ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=12012, version=0)
class Microsoft_Windows_WLAN_AutoConfig_12012_0(Etw):
    pattern = Struct(
        "Adapter" / WString,
        "DeviceGuid" / Guid,
        "LocalMac" / WString,
        "SSID" / WString,
        "BSSType" / WString,
        "Identity" / WString,
        "User" / WString,
        "Domain" / WString,
        "ConnectionId" / Int64ul,
        "ExplicitCredentials" / Int8ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=12013, version=0)
class Microsoft_Windows_WLAN_AutoConfig_12013_0(Etw):
    pattern = Struct(
        "Adapter" / WString,
        "DeviceGuid" / Guid,
        "LocalMac" / WString,
        "SSID" / WString,
        "BSSType" / WString,
        "PeerMac" / WString,
        "Identity" / WString,
        "User" / WString,
        "Domain" / WString,
        "ReasonText" / WString,
        "ReasonCode" / Int32ul,
        "ErrorCode" / Int32ul,
        "EAPReasonCode" / Int32ul,
        "EAPRootCauseString" / WString,
        "EAPErrorCode" / Int32ul,
        "ConnectionId" / Int64ul,
        "ExplicitCredentials" / Int8ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=12014, version=0)
class Microsoft_Windows_WLAN_AutoConfig_12014_0(Etw):
    pattern = Struct(
        "Adapter" / WString,
        "DeviceGuid" / Guid,
        "LocalMac" / WString,
        "SSID" / WString,
        "BSSType" / WString,
        "EapType" / Int32ul,
        "VendorID" / Int32ul,
        "VendorType" / Int32ul,
        "AuthorID" / Int32ul,
        "RestartReason" / WString,
        "ConnectionId" / Int64ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=13001, version=0)
class Microsoft_Windows_WLAN_AutoConfig_13001_0(Etw):
    pattern = Struct(
        "Result" / Int32ul,
        "Reason" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=13002, version=0)
class Microsoft_Windows_WLAN_AutoConfig_13002_0(Etw):
    pattern = Struct(
        "Result" / Int32ul,
        "InterfaceGuid" / Guid,
        "ProfileName" / WString,
        "RequestedFields" / WString
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=13011, version=0)
class Microsoft_Windows_WLAN_AutoConfig_13011_0(Etw):
    pattern = Struct(
        "Result" / Int32ul,
        "Reason" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=13012, version=0)
class Microsoft_Windows_WLAN_AutoConfig_13012_0(Etw):
    pattern = Struct(
        "Result" / Int32ul,
        "InterfaceGuid" / Guid,
        "ProfileName" / WString
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=13013, version=0)
class Microsoft_Windows_WLAN_AutoConfig_13013_0(Etw):
    pattern = Struct(
        "Result" / Int32ul,
        "Reason" / Int32ul,
        "InterfaceGuid" / Guid,
        "ProfileName" / WString
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=13014, version=0)
class Microsoft_Windows_WLAN_AutoConfig_13014_0(Etw):
    pattern = Struct(
        "Result" / Int32ul,
        "InterfaceGuid" / Guid,
        "ProfileName" / WString
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=13100, version=0)
class Microsoft_Windows_WLAN_AutoConfig_13100_0(Etw):
    pattern = Struct(
        "CostSource" / Int32ul,
        "CostValue" / Int32ul,
        "InterfaceGuid" / Guid,
        "ProfileName" / WString
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=13101, version=0)
class Microsoft_Windows_WLAN_AutoConfig_13101_0(Etw):
    pattern = Struct(
        "CostValue" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=13102, version=0)
class Microsoft_Windows_WLAN_AutoConfig_13102_0(Etw):
    pattern = Struct(
        "CostSource" / Int32ul,
        "InterfaceGuid" / Guid,
        "ProfileName" / WString
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14000, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14000_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString,
        "Connected" / Int8ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14001, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14001_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString,
        "Joined" / Int8ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14002, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14002_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString,
        "Enabled" / Int8ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14003, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14003_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString,
        "Enabled" / Int8ul,
        "Result" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14004, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14004_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString,
        "BSSType" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14005, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14005_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString,
        "PHY" / Int32ul,
        "RadioState" / Int32ul,
        "Result" / Int32ul,
        "PHYCount" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14006, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14006_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14007, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14007_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14008, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14008_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString,
        "PowerSetting" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14009, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14009_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString,
        "ConnectionId" / Int64ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14010, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14010_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14011, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14011_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString,
        "PHY" / Int32ul,
        "SoftwareState" / Int32ul,
        "HardwareState" / Int32ul,
        "PHYCount" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14012, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14012_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14013, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14013_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString,
        "Profile" / WString
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14014, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14014_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString,
        "ConnectionResetReason" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14015, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14015_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString,
        "OpMode" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14016, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14016_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString,
        "ConnectionMode" / Int32ul,
        "Flags" / Int32ul,
        "Profile" / WString,
        "ConnectionId" / Int64ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14017, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14017_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14018, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14018_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul,
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14019, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14019_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14020, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14020_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14021, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14021_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString,
        "ConnectionId" / Int64ul,
        "Status" / Int32ul,
        "Adhoc" / Int8ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14022, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14022_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14023, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14023_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString,
        "Profile" / WString
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14024, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14024_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14025, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14025_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString,
        "State" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14026, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14026_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString,
        "Result" / Int8ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14027, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14027_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString,
        "Profile" / WString,
        "HealthCheckResult" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14028, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14028_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString,
        "OldProfileName" / WString,
        "NewProfileName" / WString
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14029, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14029_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14030, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14030_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString,
        "OpMode" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14031, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14031_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "Type" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14032, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14032_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul,
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14033, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14033_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14034, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14034_0(Etw):
    pattern = Struct(
        "DeviceGuid" / WString,
        "FriendlyName" / WString
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14035, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14035_0(Etw):
    pattern = Struct(
        "SSID" / WString
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14036, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14036_0(Etw):
    pattern = Struct(
        "Setting" / Int8ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14037, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14037_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString,
        "Profile" / WString,
        "Reason" / Int8ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14038, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14038_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14039, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14039_0(Etw):
    pattern = Struct(
        "Type" / Int32ul,
        "ConnectionId" / Int64ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14040, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14040_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString,
        "ScanType" / Int32ul,
        "FlushBSSList" / Int8ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14041, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14041_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14042, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14042_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14043, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14043_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14044, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14044_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString,
        "Profile" / WString
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14045, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14045_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString,
        "ProfileName" / WString,
        "Auto" / Int8ul,
        "SSID" / WString,
        "Multiple" / Int8ul,
        "SSIDListSize" / Int16ul,
        "SSIDList" / Bytes(lambda this: this.SSIDListSize)
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14046, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14046_0(Etw):
    pattern = Struct(
        "ConnectionId" / Int64ul,
        "Active" / Int8ul,
        "Console" / Int8ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14047, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14047_0(Etw):
    pattern = Struct(
        "ConnectionId" / Int64ul,
        "Active" / Int8ul,
        "Console" / Int8ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14048, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14048_0(Etw):
    pattern = Struct(
        "ActiveConsole" / Int8ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14049, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14049_0(Etw):
    pattern = Struct(
        "ConnectionId" / Int64ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14050, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14050_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14051, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14051_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14052, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14052_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul,
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14053, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14053_0(Etw):
    pattern = Struct(
        "ConnectionId" / Int64ul,
        "Network" / Guid,
        "Suppressed" / Int8ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14054, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14054_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString,
        "Enabled" / Int8ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14055, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14055_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14056, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14056_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14057, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14057_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14058, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14058_0(Etw):
    pattern = Struct(
        "ProfileName" / WString,
        "SSID" / WString
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14059, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14059_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString,
        "Enabled" / Int8ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14060, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14060_0(Etw):
    pattern = Struct(
        "Profile" / WString,
        "BlockTimeMs" / Int32ul,
        "SingleSSID" / Int8ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14061, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14061_0(Etw):
    pattern = Struct(
        "Profile" / WString,
        "Update" / Int8ul,
        "SingleSSID" / Int8ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14062, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14062_0(Etw):
    pattern = Struct(
        "WlanRpcCallType" / Int8ul,
        "ClientProcessId" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14063, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14063_0(Etw):
    pattern = Struct(
        "OpCode" / Int32ul,
        "ClientProcessId" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14064, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14064_0(Etw):
    pattern = Struct(
        "OpCode" / Int32ul,
        "ClientProcessId" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14065, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14065_0(Etw):
    pattern = Struct(
        "OpCode" / Int32ul,
        "ClientProcessId" / Int32ul,
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14066, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14066_0(Etw):
    pattern = Struct(
        "OpCode" / Int32ul,
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14067, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14067_0(Etw):
    pattern = Struct(
        "IsOn" / Int8ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14068, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14068_0(Etw):
    pattern = Struct(
        "IsEnabled" / Int8ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14069, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14069_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14070, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14070_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14071, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14071_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "ExpeditedScanTrigger" / Int8ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14072, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14072_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "DisconnectTrigger" / Int8ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14073, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14073_0(Etw):
    pattern = Struct(
        "RecoveryType" / Int8ul,
        "EventType" / Int8ul,
        "EventData" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14074, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14074_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "IsReachable" / Int8ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=14075, version=0)
class Microsoft_Windows_WLAN_AutoConfig_14075_0(Etw):
    pattern = Struct(
        "IsAutoConnectEnabled" / Int8ul,
        "AutoConnectProfileCount" / Int32ul,
        "AutoConnectFilterControl" / Int32ul,
        "IsManualConnectEnabled" / Int8ul,
        "ManualConnectProfileCount" / Int32ul,
        "ManualConnectFilterControl" / Int32ul,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=20000, version=0)
class Microsoft_Windows_WLAN_AutoConfig_20000_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString,
        "Session" / Int64ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=20001, version=0)
class Microsoft_Windows_WLAN_AutoConfig_20001_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=20002, version=0)
class Microsoft_Windows_WLAN_AutoConfig_20002_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=20003, version=0)
class Microsoft_Windows_WLAN_AutoConfig_20003_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=20004, version=0)
class Microsoft_Windows_WLAN_AutoConfig_20004_0(Etw):
    pattern = Struct(
        "Reason" / Int32ul,
        "Session" / Int64ul,
        "AdHocFormed" / Int8ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=20005, version=0)
class Microsoft_Windows_WLAN_AutoConfig_20005_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString,
        "Status" / Int32ul,
        "AssocStatus" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=20006, version=0)
class Microsoft_Windows_WLAN_AutoConfig_20006_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString,
        "CurrState" / Int32ul,
        "EventId" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=20007, version=0)
class Microsoft_Windows_WLAN_AutoConfig_20007_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString,
        "CurrState" / Int32ul,
        "NewState" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=20008, version=0)
class Microsoft_Windows_WLAN_AutoConfig_20008_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=20009, version=0)
class Microsoft_Windows_WLAN_AutoConfig_20009_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString,
        "Quality" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=20010, version=0)
class Microsoft_Windows_WLAN_AutoConfig_20010_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=20011, version=0)
class Microsoft_Windows_WLAN_AutoConfig_20011_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=20012, version=0)
class Microsoft_Windows_WLAN_AutoConfig_20012_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=20013, version=0)
class Microsoft_Windows_WLAN_AutoConfig_20013_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul,
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=20014, version=0)
class Microsoft_Windows_WLAN_AutoConfig_20014_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString,
        "PacketType" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=20015, version=0)
class Microsoft_Windows_WLAN_AutoConfig_20015_0(Etw):
    pattern = Struct(
        "Reason" / Int32ul,
        "Error" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=20016, version=0)
class Microsoft_Windows_WLAN_AutoConfig_20016_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString,
        "Length" / Int32ul,
        "Handle" / Int64ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=20017, version=0)
class Microsoft_Windows_WLAN_AutoConfig_20017_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString,
        "Length" / Int32ul,
        "Handle" / Int64ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=20018, version=0)
class Microsoft_Windows_WLAN_AutoConfig_20018_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString,
        "SSID" / WString,
        "BSSIDCount" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=20019, version=0)
class Microsoft_Windows_WLAN_AutoConfig_20019_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString,
        "SSID" / WString,
        "LocalMAC" / WString,
        "PeerMAC" / WString
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=20020, version=0)
class Microsoft_Windows_WLAN_AutoConfig_20020_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString,
        "SSID" / WString,
        "LocalMAC" / WString,
        "PeerMAC" / WString
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=20021, version=0)
class Microsoft_Windows_WLAN_AutoConfig_20021_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "ErrorCode" / Int32ul,
        "ErrorMsg" / WString,
        "InterfaceDescription" / WString,
        "SSID" / WString,
        "LocalMAC" / WString
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=20022, version=0)
class Microsoft_Windows_WLAN_AutoConfig_20022_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=20023, version=0)
class Microsoft_Windows_WLAN_AutoConfig_20023_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "Status" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=20024, version=0)
class Microsoft_Windows_WLAN_AutoConfig_20024_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "Count" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=20025, version=0)
class Microsoft_Windows_WLAN_AutoConfig_20025_0(Etw):
    pattern = Struct(
        "Ssid" / WString,
        "BssidCount" / Int32ul,
        "AuthAlgoId" / Int32ul,
        "CipherAlgoId" / Int32ul,
        "Rssi" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=21001, version=0)
class Microsoft_Windows_WLAN_AutoConfig_21001_0(Etw):
    pattern = Struct(
        "AdapterId" / Int32ul,
        "InterfaceGuid" / Guid,
        "FriendlyName" / WString,
        "PKMIDs" / Int32ul,
        "FourWayOffloadSupported" / Int8ul,
        "SafeModeSupported" / Int8ul,
        "SafeModeCertified" / Int8ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=21002, version=0)
class Microsoft_Windows_WLAN_AutoConfig_21002_0(Etw):
    pattern = Struct(
        "AdapterId" / Int32ul,
        "InterfaceGuid" / Guid,
        "OldState" / Int32ul,
        "NewState" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=21003, version=0)
class Microsoft_Windows_WLAN_AutoConfig_21003_0(Etw):
    pattern = Struct(
        "AdapterId" / Int32ul,
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=21004, version=0)
class Microsoft_Windows_WLAN_AutoConfig_21004_0(Etw):
    pattern = Struct(
        "AdapterId" / Int32ul,
        "InterfaceGuid" / Guid,
        "AuthAlgoId" / Int32ul,
        "CipherAlgoId" / Int32ul,
        "OneXEnabled" / Int8ul,
        "UICancelled" / Int8ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=21005, version=0)
class Microsoft_Windows_WLAN_AutoConfig_21005_0(Etw):
    pattern = Struct(
        "AdapterId" / Int32ul,
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=21006, version=0)
class Microsoft_Windows_WLAN_AutoConfig_21006_0(Etw):
    pattern = Struct(
        "AdapterId" / Int32ul,
        "InterfaceGuid" / Guid,
        "ResponseType" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=21007, version=0)
class Microsoft_Windows_WLAN_AutoConfig_21007_0(Etw):
    pattern = Struct(
        "AdapterId" / Int32ul,
        "InterfaceGuid" / Guid,
        "SessionId" / Int32ul,
        "PortId" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=21008, version=0)
class Microsoft_Windows_WLAN_AutoConfig_21008_0(Etw):
    pattern = Struct(
        "AdapterId" / Int32ul,
        "InterfaceGuid" / Guid,
        "SessionId" / Int32ul,
        "PortId" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=21009, version=0)
class Microsoft_Windows_WLAN_AutoConfig_21009_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=21010, version=0)
class Microsoft_Windows_WLAN_AutoConfig_21010_0(Etw):
    pattern = Struct(
        "AdapterId" / Int32ul,
        "InterfaceGuid" / Guid,
        "SessionId" / Int32ul,
        "PortId" / Int32ul,
        "OldState" / Int32ul,
        "NewState" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=21011, version=0)
class Microsoft_Windows_WLAN_AutoConfig_21011_0(Etw):
    pattern = Struct(
        "AdapterId" / Int32ul,
        "InterfaceGuid" / Guid,
        "SessionId" / Int32ul,
        "PortId" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=21012, version=0)
class Microsoft_Windows_WLAN_AutoConfig_21012_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "OldState" / Int32ul,
        "NewState" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=21013, version=0)
class Microsoft_Windows_WLAN_AutoConfig_21013_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "Reason" / Int32ul,
        "Error" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=21014, version=0)
class Microsoft_Windows_WLAN_AutoConfig_21014_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=21015, version=0)
class Microsoft_Windows_WLAN_AutoConfig_21015_0(Etw):
    pattern = Struct(
        "AdapterId" / Int32ul,
        "InterfaceGuid" / Guid,
        "SessionId" / Int32ul,
        "PortId" / Int32ul,
        "OldState" / Int32ul,
        "NewState" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=21016, version=0)
class Microsoft_Windows_WLAN_AutoConfig_21016_0(Etw):
    pattern = Struct(
        "AdapterId" / Int32ul,
        "InterfaceGuid" / Guid,
        "SessionId" / Int32ul,
        "PortId" / Int32ul,
        "Timeout" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=21017, version=0)
class Microsoft_Windows_WLAN_AutoConfig_21017_0(Etw):
    pattern = Struct(
        "AdapterId" / Int32ul,
        "InterfaceGuid" / Guid,
        "SessionId" / Int32ul,
        "PortId" / Int32ul,
        "Timeout" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=21018, version=0)
class Microsoft_Windows_WLAN_AutoConfig_21018_0(Etw):
    pattern = Struct(
        "AdapterId" / Int32ul,
        "InterfaceGuid" / Guid,
        "SessionId" / Int32ul,
        "PortId" / Int32ul,
        "Timeout" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=21019, version=0)
class Microsoft_Windows_WLAN_AutoConfig_21019_0(Etw):
    pattern = Struct(
        "AdapterId" / Int32ul,
        "InterfaceGuid" / Guid,
        "SessionId" / Int32ul,
        "PortId" / Int32ul,
        "OldState" / Int32ul,
        "NewState" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=21020, version=0)
class Microsoft_Windows_WLAN_AutoConfig_21020_0(Etw):
    pattern = Struct(
        "AdapterId" / Int32ul,
        "InterfaceGuid" / Guid,
        "SessionId" / Int32ul,
        "PortId" / Int32ul,
        "Timeout" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=21021, version=0)
class Microsoft_Windows_WLAN_AutoConfig_21021_0(Etw):
    pattern = Struct(
        "AdapterId" / Int32ul,
        "InterfaceGuid" / Guid,
        "SessionId" / Int32ul,
        "PortId" / Int32ul,
        "Authenticator" / Int8ul,
        "Reason" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=21022, version=0)
class Microsoft_Windows_WLAN_AutoConfig_21022_0(Etw):
    pattern = Struct(
        "Index" / Int32ul,
        "CipherAlgoId" / Int32ul,
        "Direction" / Int8ul,
        "Len" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=21023, version=0)
class Microsoft_Windows_WLAN_AutoConfig_21023_0(Etw):
    pattern = Struct(
        "CipherAlgoId" / Int32ul,
        "Direction" / Int8ul,
        "Len" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=21024, version=0)
class Microsoft_Windows_WLAN_AutoConfig_21024_0(Etw):
    pattern = Struct(
        "AdapterId" / Int32ul,
        "Reason" / Int32ul,
        "Error" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=21025, version=0)
class Microsoft_Windows_WLAN_AutoConfig_21025_0(Etw):
    pattern = Struct(
        "PortId" / Int32ul,
        "Reason" / Int32ul,
        "Error" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=21026, version=0)
class Microsoft_Windows_WLAN_AutoConfig_21026_0(Etw):
    pattern = Struct(
        "EtherType" / Int32ul,
        "Size" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=21027, version=0)
class Microsoft_Windows_WLAN_AutoConfig_21027_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "PageClsId" / Guid,
        "RequestType" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=21028, version=0)
class Microsoft_Windows_WLAN_AutoConfig_21028_0(Etw):
    pattern = Struct(
        "AdapterId" / Int32ul,
        "InterfaceGuid" / Guid,
        "SSID" / WString
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=21029, version=0)
class Microsoft_Windows_WLAN_AutoConfig_21029_0(Etw):
    pattern = Struct(
        "AdapterId" / Int32ul,
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=21030, version=0)
class Microsoft_Windows_WLAN_AutoConfig_21030_0(Etw):
    pattern = Struct(
        "AdapterId" / Int32ul,
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=21031, version=0)
class Microsoft_Windows_WLAN_AutoConfig_21031_0(Etw):
    pattern = Struct(
        "AdapterId" / Int32ul,
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=21032, version=0)
class Microsoft_Windows_WLAN_AutoConfig_21032_0(Etw):
    pattern = Struct(
        "AdapterId" / Int32ul,
        "InterfaceGuid" / Guid,
        "EtherType" / Int32ul,
        "Size" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=21033, version=0)
class Microsoft_Windows_WLAN_AutoConfig_21033_0(Etw):
    pattern = Struct(
        "AdapterId" / Int32ul,
        "InterfaceGuid" / Guid,
        "RequestType" / Int32ul,
        "ResponseType" / Int32ul,
        "Cancelled" / Int8ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=21034, version=0)
class Microsoft_Windows_WLAN_AutoConfig_21034_0(Etw):
    pattern = Struct(
        "AdapterID" / Int32ul,
        "InterfaceGuid" / Guid,
        "SSID" / CString,
        "BSSType" / Int32ul,
        "Secure" / Int8ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=21035, version=0)
class Microsoft_Windows_WLAN_AutoConfig_21035_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=21036, version=0)
class Microsoft_Windows_WLAN_AutoConfig_21036_0(Etw):
    pattern = Struct(
        "AdapterId" / Int32ul,
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=21037, version=0)
class Microsoft_Windows_WLAN_AutoConfig_21037_0(Etw):
    pattern = Struct(
        "AdapterId" / Int32ul,
        "InterfaceGuid" / Guid,
        "Healthy" / Int8ul,
        "HealthStatus" / Int32ul,
        "Hint" / Int8ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=21038, version=0)
class Microsoft_Windows_WLAN_AutoConfig_21038_0(Etw):
    pattern = Struct(

    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=21039, version=0)
class Microsoft_Windows_WLAN_AutoConfig_21039_0(Etw):
    pattern = Struct(
        "Valid" / Int8ul,
        "Cancelled" / Int8ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=21040, version=0)
class Microsoft_Windows_WLAN_AutoConfig_21040_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=21042, version=0)
class Microsoft_Windows_WLAN_AutoConfig_21042_0(Etw):
    pattern = Struct(
        "AdapterId" / Int32ul,
        "InterfaceGuid" / Guid,
        "SessionId" / Int32ul,
        "OldState" / Int32ul,
        "NewState" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=21043, version=0)
class Microsoft_Windows_WLAN_AutoConfig_21043_0(Etw):
    pattern = Struct(
        "AdapterId" / Int32ul,
        "InterfaceGuid" / Guid,
        "SessionId" / Int32ul,
        "PortId" / Int32ul,
        "Timeout" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=21044, version=0)
class Microsoft_Windows_WLAN_AutoConfig_21044_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "Reason" / Int32ul,
        "Error" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=21045, version=0)
class Microsoft_Windows_WLAN_AutoConfig_21045_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=21046, version=0)
class Microsoft_Windows_WLAN_AutoConfig_21046_0(Etw):
    pattern = Struct(
        "AdapterId" / Int32ul,
        "InterfaceGuid" / Guid,
        "SessionId" / Int32ul,
        "PortId" / Int32ul,
        "RapidRekey" / Int8ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=21047, version=0)
class Microsoft_Windows_WLAN_AutoConfig_21047_0(Etw):
    pattern = Struct(
        "AdapterId" / Int32ul,
        "InterfaceGuid" / Guid,
        "SessionId" / Int32ul,
        "PortId" / Int32ul,
        "Timeout" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=21048, version=0)
class Microsoft_Windows_WLAN_AutoConfig_21048_0(Etw):
    pattern = Struct(
        "AdapterId" / Int32ul,
        "InterfaceGuid" / Guid,
        "SessionId" / Int32ul,
        "PortId" / Int32ul,
        "Timeout" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=21049, version=0)
class Microsoft_Windows_WLAN_AutoConfig_21049_0(Etw):
    pattern = Struct(
        "AdapterId" / Int32ul,
        "InterfaceGuid" / Guid,
        "SessionId" / Int32ul,
        "PortId" / Int32ul,
        "Timeout" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=21050, version=0)
class Microsoft_Windows_WLAN_AutoConfig_21050_0(Etw):
    pattern = Struct(
        "AdapterId" / Int32ul,
        "InterfaceGuid" / Guid,
        "SessionId" / Int32ul,
        "PortId" / Int32ul,
        "Timeout" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=21051, version=0)
class Microsoft_Windows_WLAN_AutoConfig_21051_0(Etw):
    pattern = Struct(
        "AdapterId" / Int32ul,
        "InterfaceGuid" / Guid,
        "SessionId" / Int32ul,
        "PortId" / Int32ul,
        "Timeout" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=21052, version=0)
class Microsoft_Windows_WLAN_AutoConfig_21052_0(Etw):
    pattern = Struct(
        "AdapterId" / Int32ul,
        "InterfaceGuid" / Guid,
        "SessionId" / Int32ul,
        "PortId" / Int32ul,
        "Timeout" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=21053, version=0)
class Microsoft_Windows_WLAN_AutoConfig_21053_0(Etw):
    pattern = Struct(
        "AdapterId" / Int32ul,
        "InterfaceGuid" / Guid,
        "SessionId" / Int32ul,
        "PortId" / Int32ul,
        "Timeout" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=21054, version=0)
class Microsoft_Windows_WLAN_AutoConfig_21054_0(Etw):
    pattern = Struct(
        "AdapterId" / Int32ul,
        "InterfaceGuid" / Guid,
        "SessionId" / Int32ul,
        "PortId" / Int32ul,
        "Timeout" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=21055, version=0)
class Microsoft_Windows_WLAN_AutoConfig_21055_0(Etw):
    pattern = Struct(
        "AdapterId" / Int32ul,
        "InterfaceGuid" / Guid,
        "SessionId" / Int32ul,
        "PortId" / Int32ul,
        "FastRoam" / Int8ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=21056, version=0)
class Microsoft_Windows_WLAN_AutoConfig_21056_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=21057, version=0)
class Microsoft_Windows_WLAN_AutoConfig_21057_0(Etw):
    pattern = Struct(
        "AdapterId" / Int32ul,
        "InterfaceGuid" / Guid,
        "SessionId" / Int32ul,
        "PortId" / Int32ul,
        "OldState" / Int32ul,
        "NewState" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=21058, version=0)
class Microsoft_Windows_WLAN_AutoConfig_21058_0(Etw):
    pattern = Struct(
        "AdapterId" / Int32ul,
        "InterfaceGuid" / Guid,
        "SessionId" / Int32ul,
        "PortId" / Int32ul,
        "Timeout" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=21059, version=0)
class Microsoft_Windows_WLAN_AutoConfig_21059_0(Etw):
    pattern = Struct(
        "AdapterId" / Int32ul,
        "InterfaceGuid" / Guid,
        "SessionId" / Int32ul,
        "PortId" / Int32ul,
        "Timeout" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=21060, version=0)
class Microsoft_Windows_WLAN_AutoConfig_21060_0(Etw):
    pattern = Struct(
        "AdapterId" / Int32ul,
        "InterfaceGuid" / Guid,
        "SessionId" / Int32ul,
        "PortId" / Int32ul,
        "Timeout" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=21061, version=0)
class Microsoft_Windows_WLAN_AutoConfig_21061_0(Etw):
    pattern = Struct(
        "AdapterId" / Int32ul,
        "InterfaceGuid" / Guid,
        "SessionId" / Int32ul,
        "PortId" / Int32ul,
        "Timeout" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=21062, version=0)
class Microsoft_Windows_WLAN_AutoConfig_21062_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=21063, version=0)
class Microsoft_Windows_WLAN_AutoConfig_21063_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul,
        "Current" / Int32ul,
        "Max" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=21064, version=0)
class Microsoft_Windows_WLAN_AutoConfig_21064_0(Etw):
    pattern = Struct(
        "BSSType" / Int32ul,
        "AuthAlgoId" / Int32ul,
        "CipherAlgoId" / Int32ul,
        "OnexEnabled" / Int32ul,
        "EapType" / Int32ul,
        "VendorID" / Int32ul,
        "VendorType" / Int32ul,
        "AuthorID" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=21065, version=0)
class Microsoft_Windows_WLAN_AutoConfig_21065_0(Etw):
    pattern = Struct(
        "AdapterId" / Int32ul,
        "InterfaceGuid" / Guid,
        "SessionId" / Int32ul,
        "PortId" / Int32ul,
        "RapidRekey" / Int8ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=21066, version=0)
class Microsoft_Windows_WLAN_AutoConfig_21066_0(Etw):
    pattern = Struct(
        "Index" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=30000, version=0)
class Microsoft_Windows_WLAN_AutoConfig_30000_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=30001, version=0)
class Microsoft_Windows_WLAN_AutoConfig_30001_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=30002, version=0)
class Microsoft_Windows_WLAN_AutoConfig_30002_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=30003, version=0)
class Microsoft_Windows_WLAN_AutoConfig_30003_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=30004, version=0)
class Microsoft_Windows_WLAN_AutoConfig_30004_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=30005, version=0)
class Microsoft_Windows_WLAN_AutoConfig_30005_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=30006, version=0)
class Microsoft_Windows_WLAN_AutoConfig_30006_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=30007, version=0)
class Microsoft_Windows_WLAN_AutoConfig_30007_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=30008, version=0)
class Microsoft_Windows_WLAN_AutoConfig_30008_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=30009, version=0)
class Microsoft_Windows_WLAN_AutoConfig_30009_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=30010, version=0)
class Microsoft_Windows_WLAN_AutoConfig_30010_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=30011, version=0)
class Microsoft_Windows_WLAN_AutoConfig_30011_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=30012, version=0)
class Microsoft_Windows_WLAN_AutoConfig_30012_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=30013, version=0)
class Microsoft_Windows_WLAN_AutoConfig_30013_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=30014, version=0)
class Microsoft_Windows_WLAN_AutoConfig_30014_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=30015, version=0)
class Microsoft_Windows_WLAN_AutoConfig_30015_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=30016, version=0)
class Microsoft_Windows_WLAN_AutoConfig_30016_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=30017, version=0)
class Microsoft_Windows_WLAN_AutoConfig_30017_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=30018, version=0)
class Microsoft_Windows_WLAN_AutoConfig_30018_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=30019, version=0)
class Microsoft_Windows_WLAN_AutoConfig_30019_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=30020, version=0)
class Microsoft_Windows_WLAN_AutoConfig_30020_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=30021, version=0)
class Microsoft_Windows_WLAN_AutoConfig_30021_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "WLANStatusCode" / Int32ul,
        "DetailedStatusCode" / Int32ul,
        "ConnectionInformation" / Int32ul,
        "DeviceID" / WString
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=30022, version=0)
class Microsoft_Windows_WLAN_AutoConfig_30022_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=30100, version=0)
class Microsoft_Windows_WLAN_AutoConfig_30100_0(Etw):
    pattern = Struct(
        "RequestId" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=30101, version=0)
class Microsoft_Windows_WLAN_AutoConfig_30101_0(Etw):
    pattern = Struct(
        "RequestId" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=30102, version=0)
class Microsoft_Windows_WLAN_AutoConfig_30102_0(Etw):
    pattern = Struct(
        "RequestId" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=30103, version=0)
class Microsoft_Windows_WLAN_AutoConfig_30103_0(Etw):
    pattern = Struct(
        "RequestId" / Int32ul,
        "WFDPairReturnCode" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=30104, version=0)
class Microsoft_Windows_WLAN_AutoConfig_30104_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=30105, version=0)
class Microsoft_Windows_WLAN_AutoConfig_30105_0(Etw):
    pattern = Struct(
        "ReturnValue" / Int32ul,
        "ReasonCode" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=40001, version=0)
class Microsoft_Windows_WLAN_AutoConfig_40001_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString,
        "ConnectionMode" / Int32ul,
        "SSID" / WString,
        "BSSType" / Int32ul,
        "AuthAlgo" / Int32ul,
        "CipherAlgo" / Int32ul,
        "OnexEnabled" / Int32ul,
        "IHVBitmap" / Int32ul,
        "NonBroadcast" / Int8ul,
        "PeerMAC" / WString,
        "WLANStatusCode" / Int32ul,
        "DetailedStatusCode" / Int32ul,
        "AssocDuration" / Int32ul,
        "AssocRestartCount" / Int32ul,
        "AuthDuration" / Int32ul,
        "AuthRestartCount" / Int32ul,
        "DeviceID" / WString,
        "DriverVersion" / WString,
        "DriverService" / WString,
        "RSSI" / Int32sl,
        "SignalQualityPercentage" / Int32sl,
        "Channel" / Int32sl,
        "InterferingAPCount" / Int32sl,
        "TotalVisibleAPCount" / Int32sl,
        "APPhyType" / WString,
        "APMaxChannelWidth" / Int32sl,
        "APDescription" / CString,
        "APManufacturer" / CString,
        "APModelName" / CString,
        "APModelNum" / CString,
        "DetailedStatusCodeOnRoam" / Int32ul,
        "RxRate" / Int32sl,
        "TxRate" / Int32sl,
        "EAPType" / Int32sl,
        "OneXAuthMode" / WString,
        "HotSpot20IEPresent" / Int8ul,
        "DeviceMfg" / WString,
        "ProfileTypeUsed" / Int32sl,
        "SystemRandomizationStatus" / Int32ul,
        "ProfileRandomizationStatus" / Int32ul,
        "DriverDate" / SystemTime
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=40002, version=0)
class Microsoft_Windows_WLAN_AutoConfig_40002_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "DisconnectExtensions" / Int32ul,
        "RoamExtensions" / Int32ul,
        "SuspectDurationMs" / Int32ul,
        "BssidChanged" / Int8ul,
        "DetectionLinkQuality" / Int32ul,
        "CurrentLinkQuality" / Int32ul,
        "MacTxUnicastCount" / Int32sl,
        "MacRxUnicastCount" / Int32sl,
        "MacRxMulticastCount" / Int32sl,
        "MacRxUnicastDecryptSuccess" / Int32sl,
        "MacRxUnicastDecryptFailure" / Int32sl,
        "PhyTxFailedCount" / Int32sl,
        "PhyTxFrameCount" / Int32sl,
        "PhyTxRetryCount" / Int32sl,
        "PhyRxFrameCount" / Int32sl,
        "PhyRxFcsErrorCount" / Int32sl,
        "CurrentTxRate" / Int32ul,
        "CurrentRxRate" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=40003, version=0)
class Microsoft_Windows_WLAN_AutoConfig_40003_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "DiagnosticStatsDifferenceTrigger" / Int32ul,
        "MacTxUnicastCount" / Int32sl,
        "MacRxUnicastCount" / Int32sl,
        "MacRxMulticastCount" / Int32sl,
        "MacRxUnicastDecryptSuccess" / Int32sl,
        "MacRxUnicastDecryptFailure" / Int32sl,
        "PhyTxFailedCount" / Int32sl,
        "PhyTxFrameCount" / Int32sl,
        "PhyTxRetryCount" / Int32sl,
        "PhyRxFrameCount" / Int32sl,
        "PhyRxFcsErrorCount" / Int32sl,
        "TimeDiffMs" / Int64ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=60001, version=0)
class Microsoft_Windows_WLAN_AutoConfig_60001_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=60002, version=0)
class Microsoft_Windows_WLAN_AutoConfig_60002_0(Etw):
    pattern = Struct(
        "WarningCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=60003, version=0)
class Microsoft_Windows_WLAN_AutoConfig_60003_0(Etw):
    pattern = Struct(
        "NextState" / Int8ul,
        "Context" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=60004, version=0)
class Microsoft_Windows_WLAN_AutoConfig_60004_0(Etw):
    pattern = Struct(
        "Context" / Int32ul,
        "UpdateReasonCode" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=60101, version=0)
class Microsoft_Windows_WLAN_AutoConfig_60101_0(Etw):
    pattern = Struct(
        "SourceAddress" / Int32ul,
        "SourcePort" / Int32ul,
        "DestinationAddress" / Int32ul,
        "DestinationPort" / Int32ul,
        "Protocol" / Int32ul,
        "ReferenceContext" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=60102, version=0)
class Microsoft_Windows_WLAN_AutoConfig_60102_0(Etw):
    pattern = Struct(
        "SourcePort" / Int32ul,
        "DestinationPort" / Int32ul,
        "Protocol" / Int32ul,
        "ReferenceContext" / Int32ul
    )


@declare(guid=guid("9580d7dd-0379-4658-9870-d5be7d52d6de"), event_id=60103, version=0)
class Microsoft_Windows_WLAN_AutoConfig_60103_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "IfLuid" / Int64ul,
        "ReferenceContext" / Int32ul
    )

