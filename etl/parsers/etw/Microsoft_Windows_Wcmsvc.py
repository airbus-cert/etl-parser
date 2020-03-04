# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Wcmsvc
GUID : 67d07935-283a-4791-8f8d-fa9117f3e6f2
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("67d07935-283a-4791-8f8d-fa9117f3e6f2"), event_id=1003, version=0)
class Microsoft_Windows_Wcmsvc_1003_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "Name" / Int32ul
    )


@declare(guid=guid("67d07935-283a-4791-8f8d-fa9117f3e6f2"), event_id=1005, version=0)
class Microsoft_Windows_Wcmsvc_1005_0(Etw):
    pattern = Struct(
        "Reason" / Int32ul
    )


@declare(guid=guid("67d07935-283a-4791-8f8d-fa9117f3e6f2"), event_id=1006, version=0)
class Microsoft_Windows_Wcmsvc_1006_0(Etw):
    pattern = Struct(
        "Reason" / Int32ul
    )


@declare(guid=guid("67d07935-283a-4791-8f8d-fa9117f3e6f2"), event_id=1007, version=0)
class Microsoft_Windows_Wcmsvc_1007_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("67d07935-283a-4791-8f8d-fa9117f3e6f2"), event_id=1008, version=0)
class Microsoft_Windows_Wcmsvc_1008_0(Etw):
    pattern = Struct(
        "InterfaceGUID" / Guid,
        "InternetConnectivityv4" / Int8ul,
        "InternetConnectivityv6" / Int8ul,
        "InternetProbeCompletev4" / Int8ul,
        "InternetProbeCompletev6" / Int8ul,
        "DomainConnectivity" / Int8ul,
        "DomainProbeComplete" / Int8ul
    )


@declare(guid=guid("67d07935-283a-4791-8f8d-fa9117f3e6f2"), event_id=1009, version=0)
class Microsoft_Windows_Wcmsvc_1009_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "MediaType" / Int32ul
    )


@declare(guid=guid("67d07935-283a-4791-8f8d-fa9117f3e6f2"), event_id=1010, version=0)
class Microsoft_Windows_Wcmsvc_1010_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "MediaType" / Int32ul
    )


@declare(guid=guid("67d07935-283a-4791-8f8d-fa9117f3e6f2"), event_id=1011, version=0)
class Microsoft_Windows_Wcmsvc_1011_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "MediaType" / Int32ul
    )


@declare(guid=guid("67d07935-283a-4791-8f8d-fa9117f3e6f2"), event_id=1012, version=0)
class Microsoft_Windows_Wcmsvc_1012_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "MediaType" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("67d07935-283a-4791-8f8d-fa9117f3e6f2"), event_id=1013, version=0)
class Microsoft_Windows_Wcmsvc_1013_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "MediaType" / Int32ul
    )


@declare(guid=guid("67d07935-283a-4791-8f8d-fa9117f3e6f2"), event_id=1014, version=0)
class Microsoft_Windows_Wcmsvc_1014_0(Etw):
    pattern = Struct(
        "InterfaceGUID" / Guid,
        "ProfileName" / WString,
        "WcmOpcode" / Int32ul,
        "Datalength" / Int32ul,
        "CallerProcessID" / Int32ul,
        "ReturnValue" / Int32ul
    )


@declare(guid=guid("67d07935-283a-4791-8f8d-fa9117f3e6f2"), event_id=1015, version=0)
class Microsoft_Windows_Wcmsvc_1015_0(Etw):
    pattern = Struct(
        "InterfaceGUID" / Guid,
        "Mediatype" / Int32ul,
        "ManualConnect" / Int8ul,
        "ManualFiltercontrol" / Int32ul,
        "NumManualprofiles" / Int32ul,
        "ManualProfileNames" / WString,
        "AutoConnect" / Int8ul,
        "AutoFiltercontrol" / Int32ul,
        "NumAutoprofiles" / Int32ul,
        "AutoProfileNames" / WString
    )


@declare(guid=guid("67d07935-283a-4791-8f8d-fa9117f3e6f2"), event_id=1016, version=0)
class Microsoft_Windows_Wcmsvc_1016_0(Etw):
    pattern = Struct(
        "InterfaceGUID" / Guid,
        "Mediatype" / Int32ul,
        "ManualConnect" / Int8ul,
        "ManualFiltercontrol" / Int32ul,
        "NumManualprofiles" / Int32ul,
        "ManualProfileNames" / WString,
        "AutoConnect" / Int8ul,
        "AutoFiltercontrol" / Int32ul,
        "NumAutoprofiles" / Int32ul,
        "AutoProfileNames" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("67d07935-283a-4791-8f8d-fa9117f3e6f2"), event_id=1017, version=0)
class Microsoft_Windows_Wcmsvc_1017_0(Etw):
    pattern = Struct(
        "InterfaceGUID" / Guid,
        "AvgIn" / Int32ul,
        "AvgOut" / Int32ul,
        "SpikeIn" / Int32ul,
        "SpikeOut" / Int32ul,
        "ThresholdAvgIn" / Int32ul,
        "ThresholdAvgOut" / Int32ul,
        "ThresholdSpikeIn" / Int32ul,
        "ThresholdSpikeOut" / Int32ul
    )


@declare(guid=guid("67d07935-283a-4791-8f8d-fa9117f3e6f2"), event_id=1018, version=0)
class Microsoft_Windows_Wcmsvc_1018_0(Etw):
    pattern = Struct(
        "InterfaceGUID" / Guid,
        "AvgIn" / Int32ul,
        "AvgOut" / Int32ul,
        "SpikeIn" / Int32ul,
        "SpikeOut" / Int32ul,
        "ThresholdAvgIn" / Int32ul,
        "ThresholdAvgOut" / Int32ul,
        "ThresholdSpikeIn" / Int32ul,
        "ThresholdSpikeOut" / Int32ul
    )


@declare(guid=guid("67d07935-283a-4791-8f8d-fa9117f3e6f2"), event_id=1019, version=0)
class Microsoft_Windows_Wcmsvc_1019_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "MediaType" / Int32ul,
        "ProfileName" / WString
    )


@declare(guid=guid("67d07935-283a-4791-8f8d-fa9117f3e6f2"), event_id=1020, version=0)
class Microsoft_Windows_Wcmsvc_1020_0(Etw):
    pattern = Struct(
        "WCMPreferredOrderList" / WString
    )


@declare(guid=guid("67d07935-283a-4791-8f8d-fa9117f3e6f2"), event_id=1024, version=0)
class Microsoft_Windows_Wcmsvc_1024_0(Etw):
    pattern = Struct(
        "InterfaceGUID" / Guid
    )


@declare(guid=guid("67d07935-283a-4791-8f8d-fa9117f3e6f2"), event_id=1025, version=0)
class Microsoft_Windows_Wcmsvc_1025_0(Etw):
    pattern = Struct(
        "InterfaceGUID" / Guid
    )


@declare(guid=guid("67d07935-283a-4791-8f8d-fa9117f3e6f2"), event_id=1026, version=0)
class Microsoft_Windows_Wcmsvc_1026_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "MediaType" / Int32ul
    )


@declare(guid=guid("67d07935-283a-4791-8f8d-fa9117f3e6f2"), event_id=1027, version=0)
class Microsoft_Windows_Wcmsvc_1027_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "MediaType" / Int32ul
    )


@declare(guid=guid("67d07935-283a-4791-8f8d-fa9117f3e6f2"), event_id=1030, version=0)
class Microsoft_Windows_Wcmsvc_1030_0(Etw):
    pattern = Struct(
        "ProfileName" / WString,
        "InterfaceGuid" / Guid,
        "ProfileUpdatedorDeleted" / WString
    )


@declare(guid=guid("67d07935-283a-4791-8f8d-fa9117f3e6f2"), event_id=1031, version=0)
class Microsoft_Windows_Wcmsvc_1031_0(Etw):
    pattern = Struct(
        "ConfigtoSyncWithTimeServer" / Int8ul,
        "TimeServerName" / WString,
        "NumServerTimeRetries" / Int32ul,
        "ServerTimeRetrievalError" / Int32ul
    )


@declare(guid=guid("67d07935-283a-4791-8f8d-fa9117f3e6f2"), event_id=1032, version=0)
class Microsoft_Windows_Wcmsvc_1032_0(Etw):
    pattern = Struct(
        "InterfaceGUID" / Guid,
        "NdisRefError" / Int32ul
    )


@declare(guid=guid("67d07935-283a-4791-8f8d-fa9117f3e6f2"), event_id=1033, version=0)
class Microsoft_Windows_Wcmsvc_1033_0(Etw):
    pattern = Struct(
        "InterfaceGUID" / Guid,
        "NdisRefError" / Int32ul
    )


@declare(guid=guid("67d07935-283a-4791-8f8d-fa9117f3e6f2"), event_id=1034, version=0)
class Microsoft_Windows_Wcmsvc_1034_0(Etw):
    pattern = Struct(
        "OnDemandType" / Int32ul,
        "InterfaceGUID" / Guid,
        "OnDemandInfo" / WString,
        "ProviderID" / WString,
        "NewState" / Int32ul,
        "Refcount" / Int32ul
    )


@declare(guid=guid("67d07935-283a-4791-8f8d-fa9117f3e6f2"), event_id=1035, version=0)
class Microsoft_Windows_Wcmsvc_1035_0(Etw):
    pattern = Struct(
        "APNname" / WString,
        "ProviderID" / WString,
        "SubscriberID" / WString,
        "Profilename" / WString
    )


@declare(guid=guid("67d07935-283a-4791-8f8d-fa9117f3e6f2"), event_id=1036, version=0)
class Microsoft_Windows_Wcmsvc_1036_0(Etw):
    pattern = Struct(
        "Profilename" / WString
    )


@declare(guid=guid("67d07935-283a-4791-8f8d-fa9117f3e6f2"), event_id=1037, version=0)
class Microsoft_Windows_Wcmsvc_1037_0(Etw):
    pattern = Struct(
        "AppID" / WString,
        "ProcessID" / Int32ul,
        "OnDemandType" / Int32ul,
        "OnDemandInfo" / WString,
        "ProviderID" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("67d07935-283a-4791-8f8d-fa9117f3e6f2"), event_id=1038, version=0)
class Microsoft_Windows_Wcmsvc_1038_0(Etw):
    pattern = Struct(
        "AppID" / WString,
        "ProcessID" / Int32ul,
        "OnDemandType" / Int32ul,
        "OnDemandInfo" / WString,
        "ProviderID" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("67d07935-283a-4791-8f8d-fa9117f3e6f2"), event_id=1039, version=0)
class Microsoft_Windows_Wcmsvc_1039_0(Etw):
    pattern = Struct(
        "AppID" / WString,
        "ProcessID" / Int32ul,
        "OnDemandType" / Int32ul,
        "OnDemandInfo" / WString,
        "ProviderID" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("67d07935-283a-4791-8f8d-fa9117f3e6f2"), event_id=1040, version=0)
class Microsoft_Windows_Wcmsvc_1040_0(Etw):
    pattern = Struct(
        "AppID" / WString,
        "ProcessID" / Int32ul,
        "OnDemandType" / Int32ul,
        "OnDemandInfo" / WString,
        "ProviderID" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("67d07935-283a-4791-8f8d-fa9117f3e6f2"), event_id=1050, version=0)
class Microsoft_Windows_Wcmsvc_1050_0(Etw):
    pattern = Struct(
        "InterfaceGUID" / Guid,
        "ActionType" / Int32ul
    )


@declare(guid=guid("67d07935-283a-4791-8f8d-fa9117f3e6f2"), event_id=1051, version=0)
class Microsoft_Windows_Wcmsvc_1051_0(Etw):
    pattern = Struct(
        "InterfaceGUID" / Guid,
        "ActionType" / Int32ul
    )


@declare(guid=guid("67d07935-283a-4791-8f8d-fa9117f3e6f2"), event_id=1054, version=0)
class Microsoft_Windows_Wcmsvc_1054_0(Etw):
    pattern = Struct(
        "PolicyValue" / Int32ul
    )


@declare(guid=guid("67d07935-283a-4791-8f8d-fa9117f3e6f2"), event_id=4020, version=0)
class Microsoft_Windows_Wcmsvc_4020_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("67d07935-283a-4791-8f8d-fa9117f3e6f2"), event_id=4021, version=0)
class Microsoft_Windows_Wcmsvc_4021_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("67d07935-283a-4791-8f8d-fa9117f3e6f2"), event_id=4022, version=0)
class Microsoft_Windows_Wcmsvc_4022_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("67d07935-283a-4791-8f8d-fa9117f3e6f2"), event_id=4023, version=0)
class Microsoft_Windows_Wcmsvc_4023_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("67d07935-283a-4791-8f8d-fa9117f3e6f2"), event_id=4024, version=0)
class Microsoft_Windows_Wcmsvc_4024_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("67d07935-283a-4791-8f8d-fa9117f3e6f2"), event_id=4025, version=0)
class Microsoft_Windows_Wcmsvc_4025_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("67d07935-283a-4791-8f8d-fa9117f3e6f2"), event_id=4026, version=0)
class Microsoft_Windows_Wcmsvc_4026_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("67d07935-283a-4791-8f8d-fa9117f3e6f2"), event_id=4027, version=0)
class Microsoft_Windows_Wcmsvc_4027_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("67d07935-283a-4791-8f8d-fa9117f3e6f2"), event_id=4028, version=0)
class Microsoft_Windows_Wcmsvc_4028_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("67d07935-283a-4791-8f8d-fa9117f3e6f2"), event_id=4029, version=0)
class Microsoft_Windows_Wcmsvc_4029_0(Etw):
    pattern = Struct(
        "Activity" / Int8ul,
        "Status" / Int32ul
    )


@declare(guid=guid("67d07935-283a-4791-8f8d-fa9117f3e6f2"), event_id=4030, version=0)
class Microsoft_Windows_Wcmsvc_4030_0(Etw):
    pattern = Struct(
        "Activate" / Int8ul,
        "Result" / Int32ul,
        "TotalNetworkRefCount" / Int32ul,
        "ProcessId" / Int32ul,
        "ProcessNetworkRefCount" / Int32ul,
        "AppName" / WString
    )


@declare(guid=guid("67d07935-283a-4791-8f8d-fa9117f3e6f2"), event_id=4031, version=0)
class Microsoft_Windows_Wcmsvc_4031_0(Etw):
    pattern = Struct(
        "ProcessId" / Int32ul,
        "ProcessNetworkRefCount" / Int32ul,
        "TotalNetworkRefCount" / Int32ul
    )


@declare(guid=guid("67d07935-283a-4791-8f8d-fa9117f3e6f2"), event_id=4032, version=0)
class Microsoft_Windows_Wcmsvc_4032_0(Etw):
    pattern = Struct(
        "Result" / Int32ul,
        "TotalCmNdisRefCount" / Int32ul,
        "ProcessId" / Int32ul,
        "PerProcessCmNdisRefCount" / Int32ul,
        "AppName" / WString
    )


@declare(guid=guid("67d07935-283a-4791-8f8d-fa9117f3e6f2"), event_id=4033, version=0)
class Microsoft_Windows_Wcmsvc_4033_0(Etw):
    pattern = Struct(
        "Result" / Int32ul,
        "TotalCmNdisRefCount" / Int32ul,
        "ProcessId" / Int32ul,
        "PerProcessCmNdisRefCount" / Int32ul,
        "AppName" / WString
    )


@declare(guid=guid("67d07935-283a-4791-8f8d-fa9117f3e6f2"), event_id=4034, version=0)
class Microsoft_Windows_Wcmsvc_4034_0(Etw):
    pattern = Struct(
        "ProcessId" / Int32ul,
        "ProcessNetworkRefCount" / Int32ul,
        "TotalNetworkRefCount" / Int32ul
    )


@declare(guid=guid("67d07935-283a-4791-8f8d-fa9117f3e6f2"), event_id=4035, version=0)
class Microsoft_Windows_Wcmsvc_4035_0(Etw):
    pattern = Struct(
        "FunctionName" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("67d07935-283a-4791-8f8d-fa9117f3e6f2"), event_id=4036, version=0)
class Microsoft_Windows_Wcmsvc_4036_0(Etw):
    pattern = Struct(
        "AcquireRelease" / WString,
        "InterfaceLuid" / Int64ul,
        "Result" / Int32ul
    )

