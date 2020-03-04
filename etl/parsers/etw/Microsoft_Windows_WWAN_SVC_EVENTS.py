# -*- coding: utf-8 -*-
"""
Microsoft-Windows-WWAN-SVC-EVENTS
GUID : 3cb40aaa-1145-4fb8-b27b-7e30f0454316
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=1001, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_1001_0(Etw):
    pattern = Struct(
        "FunctionCall" / CString,
        "Message" / WString
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=1002, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_1002_0(Etw):
    pattern = Struct(
        "FunctionCall" / CString,
        "Message" / WString
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=1003, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_1003_0(Etw):
    pattern = Struct(
        "FunctionCall" / WString,
        "Method" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=1004, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_1004_0(Etw):
    pattern = Struct(
        "FunctionCall" / CString,
        "Message" / WString
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=1005, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_1005_0(Etw):
    pattern = Struct(
        "FunctionCall" / CString,
        "Message" / WString
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=1006, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_1006_0(Etw):
    pattern = Struct(
        "FunctionCall" / CString,
        "InterfaceGuid" / Guid,
        "Message" / WString
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=1007, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_1007_0(Etw):
    pattern = Struct(
        "FunctionCall" / CString,
        "InterfaceGuid" / Guid,
        "Message" / WString
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=1008, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_1008_0(Etw):
    pattern = Struct(
        "FunctionCall" / CString,
        "InterfaceGuid" / Guid,
        "Message" / WString
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=1009, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_1009_0(Etw):
    pattern = Struct(
        "FunctionCall" / CString,
        "InterfaceGuid" / Guid,
        "Message" / WString
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=1010, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_1010_0(Etw):
    pattern = Struct(
        "hresult" / Int32sl,
        "wilFailureType" / Int32ul,
        "moduleName" / CString,
        "fileName" / CString,
        "lineNumber" / Int32ul,
        "message" / WString
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=2003, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_2003_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString,
        "ModemCreationCount" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=2004, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_2004_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=2005, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_2005_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=2006, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_2006_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "dwMajorVersion" / Int32ul,
        "dwMinorVersion" / Int32ul,
        "dwDriverCaps" / Int32ul,
        "WwanCellularClass" / Int32ul,
        "WwanDataClass" / Int32ul,
        "WwanGSMBandClass" / Int32ul,
        "WwanCDMABandClass" / Int32ul,
        "ReadyState" / Int32ul,
        "HwRadioState" / Int32ul,
        "SwRadioState" / Int32ul,
        "InformationAvailability" / Int8ul,
        "NoOfProviders" / Int32ul,
        "RegisterState" / Int32ul,
        "RegisterMode" / Int32ul,
        "PacketAttachState" / Int32ul,
        "CurrentNetworkCaps" / Int32ul,
        "NwError" / Int32ul,
        "ConnectionId" / Int32ul,
        "ActivationState" / Int32ul,
        "VoiceCallState" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=2007, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_2007_0(Etw):
    pattern = Struct(
        "APIName" / Int32ul,
        "InterfaceGuid" / Guid,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=2008, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_2008_0(Etw):
    pattern = Struct(
        "WwanApiName" / Int32ul,
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=2101, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_2101_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "ModemCreationCount" / Int32ul,
        "Method" / CString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=2102, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_2102_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "InterfaceDescription" / WString,
        "ModemCreationCount" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=2103, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_2103_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "ModemIndex" / Int32sl,
        "ExecutorIndex" / Int32sl,
        "ModemType" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=2104, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_2104_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "ModemIndex" / Int32sl,
        "ExecutorIndex" / Int32sl,
        "ModemType" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=2105, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_2105_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "ModemIndex" / Int32sl,
        "ExecutorIndex" / Int32sl,
        "ModemGuid" / Guid
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=2106, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_2106_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "ModemIndex" / Int32sl,
        "ExecutorIndex" / Int32sl,
        "ModemGuid" / Guid
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=2107, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_2107_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "ModemIndex" / Int32sl,
        "ExecutorIndex" / Int32sl,
        "IsSysCapsSupport" / Int8ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=2108, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_2108_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "ModemIndex" / Int32sl,
        "ExecutorIndex" / Int32sl,
        "CapsType" / WString
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=3001, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_3001_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "EventCode" / Int32ul,
        "RequestID" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=3002, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_3002_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "EventCode" / Int32ul,
        "ErrorCode" / Int32ul,
        "NetworkErrorCode" / Int32ul,
        "RequestID" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=3003, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_3003_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "EventCode" / Int32ul,
        "RequestID" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=3004, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_3004_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "EventCode" / Int32ul,
        "RequestID" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=3006, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_3006_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "EventCode" / Int32ul,
        "RequestID" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=3008, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_3008_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "EventCode" / Int32ul,
        "RequestID" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=3010, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_3010_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "EventCode" / Int32ul,
        "RequestID" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=3012, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_3012_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "EventCode" / Int32ul,
        "RequestID" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=3013, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_3013_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "EventCode" / Int32ul,
        "ErrorCode" / Int32ul,
        "NetworkErrorCode" / Int32ul,
        "RequestID" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=3014, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_3014_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "EventCode" / Int32ul,
        "RequestID" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=3015, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_3015_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "EventCode" / Int32ul,
        "ErrorCode" / Int32ul,
        "NetworkErrorCode" / Int32ul,
        "RequestID" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=3016, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_3016_0(Etw):
    pattern = Struct(
        "IpType" / WString,
        "IpAddress" / WString
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=4001, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_4001_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "Rssi" / Int32ul,
        "ErrorRate" / Int32ul,
        "RssiInterval" / Int32ul,
        "RssiThreshold" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=4002, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_4002_0(Etw):
    pattern = Struct(
        "HWRadio" / Int32ul,
        "SWRadio" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=4003, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_4003_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "ModemIndex" / Int32sl,
        "ExecutorIndex" / Int32sl,
        "ProfileUpdateType" / Int32ul,
        "ProfileName" / WString,
        "oldProfileName" / WString
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=4004, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_4004_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=4005, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_4005_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "RegisteredType" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=5001, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_5001_0(Etw):
    pattern = Struct(
        "PinType" / Int32ul,
        "PinState" / Int32ul,
        "AttemptsRemaining" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=5003, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_5003_0(Etw):
    pattern = Struct(
        "PinType" / Int32ul,
        "PinOperation" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=6001, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_6001_0(Etw):
    pattern = Struct(
        "CostSource" / Int32ul,
        "CostValue" / Int32ul,
        "InterfaceGuid" / Guid,
        "ProfileName" / WString
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=6002, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_6002_0(Etw):
    pattern = Struct(
        "CostSource" / Int32ul,
        "InterfaceGuid" / Guid,
        "ProfileName" / WString
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=6003, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_6003_0(Etw):
    pattern = Struct(
        "CostValue" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=6100, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_6100_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=6101, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_6101_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=6102, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_6102_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=6103, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_6103_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "ConnectInformationFlags" / Int32ul,
        "APIErrorCode" / Int32ul,
        "NetworkErrorCode" / Int32ul,
        "HardwareId" / WString
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=6104, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_6104_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=7000, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_7000_0(Etw):
    pattern = Struct(
        "error" / Int32ul,
        "hresult" / Int32sl
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=7001, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_7001_0(Etw):
    pattern = Struct(
        "mbnInterface" / WString,
        "propname" / WString,
        "error" / Int32ul,
        "hresult" / Int32sl
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=7002, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_7002_0(Etw):
    pattern = Struct(
        "mbnInterface" / WString,
        "cellularClass" / Int32sl
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=7006, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_7006_0(Etw):
    pattern = Struct(
        "error" / Int32ul,
        "hresult" / Int32sl
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=7007, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_7007_0(Etw):
    pattern = Struct(
        "error" / Int32ul,
        "hresult" / Int32sl
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=7008, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_7008_0(Etw):
    pattern = Struct(
        "error" / Int32ul,
        "hresult" / Int32sl
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=7009, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_7009_0(Etw):
    pattern = Struct(
        "mbnInterface" / WString,
        "info" / WString
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=7010, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_7010_0(Etw):
    pattern = Struct(
        "mbnInterface" / WString,
        "info" / WString
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=7011, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_7011_0(Etw):
    pattern = Struct(
        "mbnInterface" / WString,
        "info" / WString
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=7012, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_7012_0(Etw):
    pattern = Struct(
        "mbnInterface" / WString,
        "info" / WString
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=7013, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_7013_0(Etw):
    pattern = Struct(
        "mbnInterface" / WString
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=7014, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_7014_0(Etw):
    pattern = Struct(
        "mbnInterface" / WString
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=7015, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_7015_0(Etw):
    pattern = Struct(
        "mbnInterface" / WString
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=7016, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_7016_0(Etw):
    pattern = Struct(
        "mbnInterface" / WString
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=7017, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_7017_0(Etw):
    pattern = Struct(
        "mbnInterface" / WString
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=7018, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_7018_0(Etw):
    pattern = Struct(
        "mbnInterface" / WString,
        "error" / Int32ul,
        "hresult" / Int32sl
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=7900, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_7900_0(Etw):
    pattern = Struct(
        "interfaceGuid" / Guid
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=7901, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_7901_0(Etw):
    pattern = Struct(
        "interfaceGuid" / Guid
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=8001, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_8001_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "RequestType" / Int32ul,
        "DataCodingScheme" / Int8ul,
        "StringLength" / Int8ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=8002, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_8002_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "EventType" / Int32ul,
        "SessionState" / Int32ul,
        "DataCodingScheme" / Int8ul,
        "StringLength" / Int8ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=8003, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_8003_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "EventCode" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=10021, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_10021_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=10022, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_10022_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=11001, version=1)
class Microsoft_Windows_WWAN_SVC_EVENTS_11001_1(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "RequestId" / Int32ul,
        "WwanStatus" / Int32ul,
        "DeviceType" / Int32ul,
        "CellularClass" / Int32ul,
        "VoiceClass" / Int32ul,
        "SimClass" / Int32ul,
        "DataClass" / Int32ul,
        "CustomDataClass" / WString,
        "BandClass" / Int32ul,
        "CustomBandClass" / WString,
        "SmsCaps" / Int32ul,
        "ControlCaps" / Int32ul,
        "DeviceId" / WString,
        "Manufacturer" / WString,
        "Model" / WString,
        "FirmwareInfo" / WString,
        "MaxActivatedContexts" / Int32ul,
        "AuthAlgoCaps" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=11002, version=1)
class Microsoft_Windows_WWAN_SVC_EVENTS_11002_1(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "RequestId" / Int32ul,
        "ReadyState" / Int32ul,
        "EmergencyMode" / Int32ul,
        "SubscriberId" / WString,
        "SimIccId" / WString
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=11003, version=1)
class Microsoft_Windows_WWAN_SVC_EVENTS_11003_1(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "RequestId" / Int32ul,
        "WwanStatus" / Int32ul,
        "HwRadioState" / Int32ul,
        "SwRadioState" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=11004, version=2)
class Microsoft_Windows_WWAN_SVC_EVENTS_11004_2(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "RequestId" / Int32ul,
        "SwRadioAction" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=11005, version=1)
class Microsoft_Windows_WWAN_SVC_EVENTS_11005_1(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "RequestId" / Int32ul,
        "WwanStatus" / Int32ul,
        "NetworkErrorCode" / Int32ul,
        "RegisterState" / Int32ul,
        "RegisterMode" / Int32ul,
        "ProviderId" / WString,
        "ProviderName" / WString,
        "RoamingText" / WString,
        "RegistrationFlags" / Int32ul,
        "PreferredDataClasses" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=11006, version=2)
class Microsoft_Windows_WWAN_SVC_EVENTS_11006_2(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "RequestId" / Int32ul,
        "ProviderId" / WString,
        "RegisterAction" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=11007, version=1)
class Microsoft_Windows_WWAN_SVC_EVENTS_11007_1(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "RequestId" / Int32ul,
        "WwanStatus" / Int32ul,
        "NetworkErrorCode" / Int32ul,
        "PacketServiceState" / Int32ul,
        "Wwan5GFrequencyRange" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=11008, version=2)
class Microsoft_Windows_WWAN_SVC_EVENTS_11008_2(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "RequestId" / Int32ul,
        "PacketServiceAction" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=11009, version=1)
class Microsoft_Windows_WWAN_SVC_EVENTS_11009_1(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "RequestId" / Int32ul,
        "WwanStatus" / Int32ul,
        "NetworkErrorCode" / Int32ul,
        "ConnectionId" / Int32ul,
        "ActivationState" / Int32ul,
        "VoiceCallState" / Int32ul,
        "IPType" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=11010, version=2)
class Microsoft_Windows_WWAN_SVC_EVENTS_11010_2(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "RequestId" / Int32ul,
        "ConnectionId" / Int32ul,
        "ActivationCommand" / Int32ul,
        "AccessString" / WString,
        "Compression" / Int32ul,
        "AuthProtocol" / Int32ul,
        "IPType" / Int32ul,
        "MediaPreference" / Int32ul,
        "ConnectionMediaSource" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=11011, version=1)
class Microsoft_Windows_WWAN_SVC_EVENTS_11011_1(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "RequestId" / Int32ul,
        "WwanStatus" / Int32ul,
        "PinType" / Int32ul,
        "PinState" / Int32ul,
        "AttemptsRemaining" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=11012, version=2)
class Microsoft_Windows_WWAN_SVC_EVENTS_11012_2(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "RequestId" / Int32ul,
        "PinType" / Int32ul,
        "PinOperation" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=11013, version=1)
class Microsoft_Windows_WWAN_SVC_EVENTS_11013_1(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "RequestId" / Int32ul,
        "WwanStatus" / Int32ul,
        "ProviderId" / WString,
        "ProviderState" / Int32ul,
        "ProviderName" / WString
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=11014, version=2)
class Microsoft_Windows_WWAN_SVC_EVENTS_11014_2(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "RequestId" / Int32ul,
        "ProviderId" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=11015, version=1)
class Microsoft_Windows_WWAN_SVC_EVENTS_11015_1(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "RequestId" / Int32ul,
        "DeviceServiceGuid" / Guid,
        "WwanDeviceServiceCommands" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=11016, version=1)
class Microsoft_Windows_WWAN_SVC_EVENTS_11016_1(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "RequestId" / Int32ul,
        "DeviceServiceGuid" / Guid,
        "WwanDeviceServiceEvents" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=11017, version=1)
class Microsoft_Windows_WWAN_SVC_EVENTS_11017_1(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "RequestId" / Int32ul,
        "DeviceServiceGuid" / Guid,
        "WwanDeviceServiceResponse" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=11018, version=1)
class Microsoft_Windows_WWAN_SVC_EVENTS_11018_1(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "RequestId" / Int32ul,
        "DeviceServiceGuid" / Guid,
        "WwanDeviceServiceResponse" / Int32ul,
        "ModemNumber" / Int32ul,
        "ExecutorID" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=11019, version=1)
class Microsoft_Windows_WWAN_SVC_EVENTS_11019_1(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "RequestId" / Int32ul,
        "DeviceServiceGuid" / Guid,
        "WwanDeviceServiceResponse" / Int32ul,
        "MaxContextCount" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=11020, version=1)
class Microsoft_Windows_WWAN_SVC_EVENTS_11020_1(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "RequestId" / Int32ul,
        "DeviceServiceGuid" / Guid,
        "WwanDeviceServiceResponse" / Int32ul,
        "Executors" / Int32ul,
        "ActiveExecutors" / Int32ul,
        "ActiveDataExecutors" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=11021, version=1)
class Microsoft_Windows_WWAN_SVC_EVENTS_11021_1(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "RequestId" / Int32ul,
        "WwanStatus" / Int32ul,
        "ModemConfigMode" / Int32ul,
        "ModemConfigState" / Int32ul,
        "ModemConfigReason" / Int32ul,
        "PreviousConfigIDLen" / Int32ul,
        "PreviousConfigID" / CString,
        "CurrentConfigIDLen" / Int32ul,
        "CurrentConfigID" / CString,
        "IsCurrentConfigDefault" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=11022, version=1)
class Microsoft_Windows_WWAN_SVC_EVENTS_11022_1(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "RequestId" / Int32ul,
        "WwanStatus" / Int32ul,
        "DeviceType" / Int32ul,
        "CellularClass" / Int32ul,
        "VoiceClass" / Int32ul,
        "SimClass" / Int32ul,
        "DataClass" / Int32ul,
        "CustomDataClass" / WString,
        "BandClass" / Int32ul,
        "CustomBandClass" / WString,
        "SmsCaps" / Int32ul,
        "ControlCaps" / Int32ul,
        "DeviceId" / WString,
        "Manufacturer" / WString,
        "Model" / WString,
        "FirmwareInfo" / WString,
        "MaxActivatedContexts" / Int32ul,
        "AuthAlgoCaps" / Int32ul,
        "ExecutorID" / Int32ul,
        "OptServiceCaps" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=11023, version=1)
class Microsoft_Windows_WWAN_SVC_EVENTS_11023_1(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "RequestId" / Int32ul,
        "WwanStatus" / Int32ul,
        "ModemID" / Int64ul,
        "NumberOfExecutors" / Int32ul,
        "NumberOfSlots" / Int32ul,
        "Concurrency" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=11024, version=1)
class Microsoft_Windows_WWAN_SVC_EVENTS_11024_1(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "RequestId" / Int32ul,
        "WwanStatus" / Int32ul,
        "UtcTime" / WString,
        "TimeZoneOffsetMinutes" / Int32sl,
        "DaylightSavingTimeOffsetMinutes" / Int32sl,
        "DataClasses" / Int32sl
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=11025, version=1)
class Microsoft_Windows_WWAN_SVC_EVENTS_11025_1(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "RequestId" / Int32ul,
        "WwanStatus" / Int32ul,
        "Version" / Int32sl,
        "AppCount" / Int32sl,
        "ActiveAppIndex" / Int32sl,
        "AppListSize" / Int32sl
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=11026, version=1)
class Microsoft_Windows_WWAN_SVC_EVENTS_11026_1(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "RequestId" / Int32ul,
        "WwanStatus" / Int32ul,
        "Version" / Int32sl,
        "StatusWord1" / Int32sl,
        "StatusWord2" / Int32sl,
        "FileAccessibility" / CString,
        "FileType" / CString,
        "FileStructure" / CString,
        "ItemCount" / Int32sl,
        "ItemSize" / Int32sl
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=11027, version=1)
class Microsoft_Windows_WWAN_SVC_EVENTS_11027_1(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "RequestId" / Int32ul,
        "WwanStatus" / Int32ul,
        "Version" / Int32sl,
        "StatusWord1" / Int32sl,
        "StatusWord2" / Int32sl,
        "ResponseDataSize" / Int32sl
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=11028, version=1)
class Microsoft_Windows_WWAN_SVC_EVENTS_11028_1(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "RequestId" / Int32ul,
        "WwanStatus" / Int32ul,
        "Version" / Int32ul,
        "SegmentSize" / Int32ul,
        "MaxFlushTime" / Int32ul,
        "LevelConfig" / WString
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=11101, version=1)
class Microsoft_Windows_WWAN_SVC_EVENTS_11101_1(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "RequestId" / Int32ul,
        "OID" / Int32ul,
        "cbPayload" / Int32ul,
        "Payload" / Bytes(lambda this: this.cbPayload),
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=11102, version=1)
class Microsoft_Windows_WWAN_SVC_EVENTS_11102_1(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "RequestId" / Int32ul,
        "OID" / Int32ul,
        "cbPayload" / Int32ul,
        "Payload" / Bytes(lambda this: this.cbPayload),
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=11103, version=1)
class Microsoft_Windows_WWAN_SVC_EVENTS_11103_1(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "RequestId" / Int32ul,
        "NdisStatusId" / Int32ul,
        "cbPayload" / Int32ul,
        "Payload" / Bytes(lambda this: this.cbPayload)
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=12000, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_12000_0(Etw):
    pattern = Struct(
        "ObjectGUID" / Guid,
        "ObjectType" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=12001, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_12001_0(Etw):
    pattern = Struct(
        "ObjectGUID" / Guid,
        "ObjectType" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=12100, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_12100_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "RegisteredType" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=12101, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_12101_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=12102, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_12102_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "PacketServiceState" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=12103, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_12103_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "IWLANAvailabilityState" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=12200, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_12200_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "State" / WString
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=12201, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_12201_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "PolicyType" / WString,
        "PolicyState" / WString
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=12202, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_12202_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "IsExecutorAvailable" / Int8ul,
        "IsAutoConnectEnabled" / Int8ul,
        "IsGPolicyDisableAc" / Int8ul,
        "IsClientDisableAc" / Int8ul,
        "IsAutoProfileWithAllowedPri" / Int8ul,
        "IsPowerStatesAllowingAc" / Int8ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=12211, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_12211_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "ModemIdx" / Int32sl,
        "execIdx" / Int32ul,
        "profileName" / WString
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=12212, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_12212_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "ModemIdx" / Int32sl,
        "execIdx" / Int32ul,
        "profileName" / WString
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=12213, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_12213_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "ModemIdx" / Int32sl,
        "execIdx" / Int32ul,
        "profileName" / WString,
        "IccID" / WString
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=12214, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_12214_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "ModemIdx" / Int32sl,
        "execIdx" / Int32ul,
        "profileName" / WString,
        "IccID" / WString,
        "connMode" / Int32ul,
        "isAdditionalPdpContextProfile" / Int8ul,
        "profileSource" / Int32ul,
        "purposeGuids" / Int32ul,
        "apnName" / WString,
        "ipType" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=12215, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_12215_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "ModemIdx" / Int32sl,
        "execIdx" / Int32ul,
        "profileName" / WString,
        "IccID" / WString,
        "connMode" / Int32ul,
        "isAdditionalPdpContextProfile" / Int8ul,
        "profileSource" / Int32ul,
        "purposeGuids" / Int32ul,
        "apnName" / WString,
        "ipType" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=12216, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_12216_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "ModemIdx" / Int32sl,
        "execIdx" / Int32ul,
        "IccID" / WString,
        "TotalNumberOfProfiles" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=12217, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_12217_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "ModemIdx" / Int32sl,
        "execIdx" / Int32ul,
        "profileName" / WString,
        "IccID" / WString,
        "connMode" / Int32ul,
        "isAdditionalPdpContextProfile" / Int8ul,
        "profileSource" / Int32ul,
        "purposeGuids" / Int32ul,
        "apnName" / WString,
        "ipType" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=12231, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_12231_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "authMethod" / Int32ul,
        "size" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=12232, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_12232_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "EnablementPolicy" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=12233, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_12233_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "PolicyType" / Int32ul,
        "RoamingPolicy" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=12240, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_12240_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "error" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=12241, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_12241_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "error" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=12242, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_12242_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "error" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=12243, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_12243_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "error" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=12250, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_12250_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "ModemIndex" / Int32sl,
        "ExecutorIndex" / Int32sl,
        "ProfileName" / WString,
        "ProfileSource" / Int32ul,
        "connMode" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=12251, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_12251_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "ModemIndex" / Int32sl,
        "ExecutorIndex" / Int32sl,
        "ProfileName" / WString,
        "connMode" / Int32ul,
        "Method" / CString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=12252, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_12252_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "ModemIndex" / Int32sl,
        "ExecutorIndex" / Int32sl,
        "ProfileName" / WString,
        "ProfileSource" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=12253, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_12253_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "ModemIndex" / Int32sl,
        "ExecutorIndex" / Int32sl,
        "ProfileName" / WString,
        "Method" / CString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=12300, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_12300_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "ModemIndex" / Int32sl,
        "ExecutorIndex" / Int32sl,
        "RequestId" / Int32ul,
        "ModemType" / Int32ul,
        "Operation" / CString
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=12301, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_12301_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "ModemIndex" / Int32sl,
        "ExecutorIndex" / Int32sl,
        "RequestId" / Int32sl,
        "ModemType" / Int32ul,
        "FailedOperation" / CString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=12302, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_12302_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "ModemIndex" / Int32sl,
        "ExecutorIndex" / Int32sl,
        "RequestId" / Int32sl,
        "CommandType" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=12303, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_12303_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "ModemIndex" / Int32sl,
        "ExecutorIndex" / Int32sl,
        "RequestId" / Int32sl,
        "CommandType" / Int32ul
    )


@declare(guid=guid("3cb40aaa-1145-4fb8-b27b-7e30f0454316"), event_id=12400, version=0)
class Microsoft_Windows_WWAN_SVC_EVENTS_12400_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "ModemIndex" / Int32sl,
        "ExecutorIndex" / Int32sl,
        "RequestId" / Int32sl,
        "CommandType" / Int32ul
    )

