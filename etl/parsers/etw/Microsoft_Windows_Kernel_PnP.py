# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Kernel-PnP
GUID : 9c205a39-1250-487d-abd7-e831c6290539
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=204, version=0)
class Microsoft_Windows_Kernel_PnP_204_0(Etw):
    pattern = Struct(
        "OSLoaderStart" / Int64ul,
        "OSLoaderEnd" / Int64ul
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=204, version=1)
class Microsoft_Windows_Kernel_PnP_204_1(Etw):
    pattern = Struct(
        "OSLoaderStart" / Int64ul,
        "OSLoaderEnd" / Int64ul,
        "PreloadEndTime" / Int64ul,
        "TcbLoaderStartTime" / Int64ul,
        "LoadHypervisorTime" / Int64ul,
        "LaunchHypervisorTime" / Int64ul,
        "LoadVsmTime" / Int64ul,
        "LaunchVsmTime" / Int64ul
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=204, version=2)
class Microsoft_Windows_Kernel_PnP_204_2(Etw):
    pattern = Struct(
        "OSLoaderStart" / Int64ul,
        "OSLoaderEnd" / Int64ul,
        "PreloadEndTime" / Int64ul,
        "TcbLoaderStartTime" / Int64ul,
        "LoadHypervisorTime" / Int64ul,
        "LaunchHypervisorTime" / Int64ul,
        "LoadVsmTime" / Int64ul,
        "LaunchVsmTime" / Int64ul,
        "ExecuteTransitionStartTime" / Int64ul,
        "ExecuteTransitionEndTime" / Int64ul
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=205, version=0)
class Microsoft_Windows_Kernel_PnP_205_0(Etw):
    pattern = Struct(
        "ElamDriverNameLength" / Int16ul,
        "ElamDriverName" / Bytes(lambda this: this.ElamDriverNameLength)
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=206, version=0)
class Microsoft_Windows_Kernel_PnP_206_0(Etw):
    pattern = Struct(
        "ElamDriverNameLength" / Int16ul,
        "ElamDriverName" / Bytes(lambda this: this.ElamDriverNameLength)
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=207, version=0)
class Microsoft_Windows_Kernel_PnP_207_0(Etw):
    pattern = Struct(
        "ElamStatus" / Int32ul
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=208, version=0)
class Microsoft_Windows_Kernel_PnP_208_0(Etw):
    pattern = Struct(
        "ElamStatus" / Int32ul
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=209, version=0)
class Microsoft_Windows_Kernel_PnP_209_0(Etw):
    pattern = Struct(
        "Classification" / Int32ul,
        "Policy" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=210, version=0)
class Microsoft_Windows_Kernel_PnP_210_0(Etw):
    pattern = Struct(
        "DriverNameLength" / Int16ul,
        "DriverName" / Bytes(lambda this: this.DriverNameLength)
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=211, version=0)
class Microsoft_Windows_Kernel_PnP_211_0(Etw):
    pattern = Struct(
        "DriverNameLength" / Int16ul,
        "DriverName" / Bytes(lambda this: this.DriverNameLength),
        "Status" / Int32ul
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=212, version=0)
class Microsoft_Windows_Kernel_PnP_212_0(Etw):
    pattern = Struct(
        "DriverNameLength" / Int16ul,
        "DriverName" / Bytes(lambda this: this.DriverNameLength)
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=213, version=0)
class Microsoft_Windows_Kernel_PnP_213_0(Etw):
    pattern = Struct(
        "ServiceNameLength" / Int16ul,
        "ServiceName" / Bytes(lambda this: this.ServiceNameLength),
        "Status" / Int32ul,
        "DriverNameLength" / Int16ul,
        "DriverName" / Bytes(lambda this: this.DriverNameLength),
        "Version" / Int32ul
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=214, version=0)
class Microsoft_Windows_Kernel_PnP_214_0(Etw):
    pattern = Struct(
        "DriverNameLength" / Int16ul,
        "DriverName" / Bytes(lambda this: this.DriverNameLength)
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=215, version=0)
class Microsoft_Windows_Kernel_PnP_215_0(Etw):
    pattern = Struct(
        "ServiceNameLength" / Int16ul,
        "ServiceName" / Bytes(lambda this: this.ServiceNameLength),
        "Status" / Int32ul,
        "DriverNameLength" / Int16ul,
        "DriverName" / Bytes(lambda this: this.DriverNameLength),
        "Version" / Int32ul
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=216, version=0)
class Microsoft_Windows_Kernel_PnP_216_0(Etw):
    pattern = Struct(
        "DriverNameLength" / Int16ul,
        "DriverName" / Bytes(lambda this: this.DriverNameLength)
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=217, version=0)
class Microsoft_Windows_Kernel_PnP_217_0(Etw):
    pattern = Struct(
        "DriverNameLength" / Int16ul,
        "DriverName" / Bytes(lambda this: this.DriverNameLength)
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=218, version=0)
class Microsoft_Windows_Kernel_PnP_218_0(Etw):
    pattern = Struct(
        "DriverNameLength" / Int16ul,
        "DriverName" / Bytes(lambda this: 2 * this.DriverNameLength),
        "Status" / Int32ul,
        "FailureNameLength" / Int16ul,
        "FailureName" / Bytes(lambda this: 2 * this.FailureNameLength),
        "Version" / Int32ul
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=219, version=0)
class Microsoft_Windows_Kernel_PnP_219_0(Etw):
    pattern = Struct(
        "DriverNameLength" / Int16ul,
        "DriverName" / Bytes(lambda this: this.DriverNameLength),
        "Status" / Int32ul,
        "FailureNameLength" / Int16ul,
        "FailureName" / Bytes(lambda this: this.FailureNameLength),
        "Version" / Int32ul
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=220, version=0)
class Microsoft_Windows_Kernel_PnP_220_0(Etw):
    pattern = Struct(
        "DriverNameLength" / Int16ul,
        "DriverName" / Bytes(lambda this: this.DriverNameLength)
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=221, version=0)
class Microsoft_Windows_Kernel_PnP_221_0(Etw):
    pattern = Struct(
        "DriverNameLength" / Int16ul,
        "DriverName" / Bytes(lambda this: this.DriverNameLength)
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=222, version=0)
class Microsoft_Windows_Kernel_PnP_222_0(Etw):
    pattern = Struct(
        "DriverNameLength" / Int16ul,
        "DriverName" / Bytes(lambda this: this.DriverNameLength)
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=223, version=0)
class Microsoft_Windows_Kernel_PnP_223_0(Etw):
    pattern = Struct(
        "DriverNameLength" / Int16ul,
        "DriverName" / Bytes(lambda this: this.DriverNameLength)
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=224, version=0)
class Microsoft_Windows_Kernel_PnP_224_0(Etw):
    pattern = Struct(
        "DriverNameLength" / Int16ul,
        "DriverName" / Bytes(lambda this: this.DriverNameLength),
        "Status" / Int32ul,
        "FailureNameLength" / Int16ul,
        "FailureName" / Bytes(lambda this: this.FailureNameLength),
        "Version" / Int32ul
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=225, version=0)
class Microsoft_Windows_Kernel_PnP_225_0(Etw):
    pattern = Struct(
        "ProcessId" / Int32ul,
        "ProcessNameLength" / Int16ul,
        "ProcessName" / Bytes(lambda this: this.ProcessNameLength),
        "DeviceInstanceLength" / Int16ul,
        "DeviceInstance" / Bytes(lambda this: this.DeviceInstanceLength)
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=226, version=0)
class Microsoft_Windows_Kernel_PnP_226_0(Etw):
    pattern = Struct(
        "DriverNameLength" / Int16ul,
        "DriverName" / Bytes(lambda this: this.DriverNameLength)
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=227, version=0)
class Microsoft_Windows_Kernel_PnP_227_0(Etw):
    pattern = Struct(
        "DriverNameLength" / Int16ul,
        "DriverName" / Bytes(lambda this: this.DriverNameLength),
        "Status" / Int32ul
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=228, version=0)
class Microsoft_Windows_Kernel_PnP_228_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid,
        "SqmSid" / Sid,
        "SqmWindowsSessionId" / Int32ul,
        "SqmSessionFlags" / Int32ul
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=229, version=0)
class Microsoft_Windows_Kernel_PnP_229_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=230, version=0)
class Microsoft_Windows_Kernel_PnP_230_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=231, version=0)
class Microsoft_Windows_Kernel_PnP_231_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=232, version=0)
class Microsoft_Windows_Kernel_PnP_232_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=233, version=0)
class Microsoft_Windows_Kernel_PnP_233_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=234, version=0)
class Microsoft_Windows_Kernel_PnP_234_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=235, version=0)
class Microsoft_Windows_Kernel_PnP_235_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmStringDatapointValue" / WString
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=236, version=0)
class Microsoft_Windows_Kernel_PnP_236_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16sl
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=240, version=0)
class Microsoft_Windows_Kernel_PnP_240_0(Etw):
    pattern = Struct(
        "TargetPath" / WString,
        "SparePath" / WString
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=241, version=0)
class Microsoft_Windows_Kernel_PnP_241_0(Etw):
    pattern = Struct(
        "TargetPath" / WString,
        "SparePath" / WString,
        "Status" / Int32ul,
        "Location" / Int32ul
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=241, version=1)
class Microsoft_Windows_Kernel_PnP_241_1(Etw):
    pattern = Struct(
        "TargetPath" / WString,
        "SparePath" / WString,
        "Status" / Int32ul,
        "Location" / Int32ul,
        "ExtendedStatus" / Int32ul
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=242, version=0)
class Microsoft_Windows_Kernel_PnP_242_0(Etw):
    pattern = Struct(
        "TargetPath" / WString,
        "TargetAffinity" / Int64ul,
        "TargetProcessorCount" / Int32ul,
        "TargetMemoryCount" / Int32ul,
        "TargetMemorySize" / Int64ul,
        "SparePath" / WString,
        "SpareProcessorCount" / Int32ul,
        "SpareMemoryCount" / Int32ul,
        "SpareMemorySize" / Int64ul,
        "TimeTotal" / Int32ul,
        "TimeToQuiesce" / Int32ul,
        "TimeQuiesced" / Int32ul,
        "TimeToWake" / Int32ul,
        "TargetProcessors" / Int64ul,
        "TargetMemoryRanges" / SystemTime,
        "SpareProcessors" / Int32ul,
        "SpareMemoryRanges" / Int64ul
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=250, version=0)
class Microsoft_Windows_Kernel_PnP_250_0(Etw):
    pattern = Struct(
        "DeviceInstanceLength" / Int16ul,
        "DeviceInstance" / Bytes(lambda this: this.DeviceInstanceLength)
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=251, version=0)
class Microsoft_Windows_Kernel_PnP_251_0(Etw):
    pattern = Struct(
        "DeviceInstanceLength" / Int16ul,
        "DeviceInstance" / Bytes(lambda this: this.DeviceInstanceLength)
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=252, version=0)
class Microsoft_Windows_Kernel_PnP_252_0(Etw):
    pattern = Struct(
        "DeviceInstanceLength" / Int16ul,
        "DeviceInstance" / Bytes(lambda this: this.DeviceInstanceLength),
        "Status" / Int32ul
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=270, version=0)
class Microsoft_Windows_Kernel_PnP_270_0(Etw):
    pattern = Struct(
        "DriverNameLength" / Int16ul,
        "DriverName" / Bytes(lambda this: this.DriverNameLength)
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=271, version=0)
class Microsoft_Windows_Kernel_PnP_271_0(Etw):
    pattern = Struct(
        "DriverNameLength" / Int16ul,
        "DriverName" / Bytes(lambda this: this.DriverNameLength)
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=272, version=0)
class Microsoft_Windows_Kernel_PnP_272_0(Etw):
    pattern = Struct(
        "DriverNameLength" / Int16ul,
        "DriverName" / Bytes(lambda this: this.DriverNameLength),
        "Status" / Int32ul
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=273, version=0)
class Microsoft_Windows_Kernel_PnP_273_0(Etw):
    pattern = Struct(
        "DriverNameLength" / Int16ul,
        "DriverName" / Bytes(lambda this: this.DriverNameLength)
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=274, version=0)
class Microsoft_Windows_Kernel_PnP_274_0(Etw):
    pattern = Struct(
        "DriverNameLength" / Int16ul,
        "DriverName" / Bytes(lambda this: this.DriverNameLength)
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=275, version=0)
class Microsoft_Windows_Kernel_PnP_275_0(Etw):
    pattern = Struct(
        "DriverNameLength" / Int16ul,
        "DriverName" / Bytes(lambda this: this.DriverNameLength),
        "Status" / Int32ul
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=276, version=0)
class Microsoft_Windows_Kernel_PnP_276_0(Etw):
    pattern = Struct(
        "DriverNameLength" / Int16ul,
        "DriverName" / Bytes(lambda this: this.DriverNameLength)
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=277, version=0)
class Microsoft_Windows_Kernel_PnP_277_0(Etw):
    pattern = Struct(
        "DriverNameLength" / Int16ul,
        "DriverName" / Bytes(lambda this: this.DriverNameLength),
        "Status" / Int32ul
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=278, version=0)
class Microsoft_Windows_Kernel_PnP_278_0(Etw):
    pattern = Struct(
        "BlockedDriverEntry" / Guid
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=400, version=0)
class Microsoft_Windows_Kernel_PnP_400_0(Etw):
    pattern = Struct(
        "DeviceInstanceId" / WString,
        "DriverName" / WString,
        "ClassGuid" / Guid,
        "DriverDate" / WString,
        "DriverVersion" / WString,
        "DriverProvider" / WString,
        "DriverInbox" / Int8ul,
        "DriverSection" / WString,
        "DriverRank" / Int32ul,
        "MatchingDeviceId" / WString,
        "OutrankedDrivers" / WString,
        "DeviceUpdated" / Int8ul,
        "Status" / Int32ul,
        "ParentDeviceInstanceId" / WString
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=401, version=0)
class Microsoft_Windows_Kernel_PnP_401_0(Etw):
    pattern = Struct(
        "DeviceInstanceId" / WString,
        "DriverName" / WString,
        "ClassGuid" / Guid,
        "DriverDate" / WString,
        "DriverVersion" / WString,
        "DriverProvider" / WString,
        "DriverInbox" / Int8ul,
        "DriverSection" / WString,
        "DriverRank" / Int32ul,
        "MatchingDeviceId" / WString,
        "OutrankedDrivers" / WString,
        "DeviceUpdated" / Int8ul,
        "Status" / Int32ul,
        "ParentDeviceInstanceId" / WString
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=402, version=0)
class Microsoft_Windows_Kernel_PnP_402_0(Etw):
    pattern = Struct(
        "DeviceInstanceId" / WString,
        "DriverName" / WString,
        "ClassGuid" / Guid,
        "DriverDate" / WString,
        "DriverVersion" / WString,
        "DriverProvider" / WString,
        "DriverInbox" / Int8ul,
        "DriverSection" / WString,
        "DriverRank" / Int32ul,
        "MatchingDeviceId" / WString,
        "OutrankedDrivers" / WString,
        "DeviceUpdated" / Int8ul,
        "Status" / Int32ul,
        "ParentDeviceInstanceId" / WString
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=403, version=0)
class Microsoft_Windows_Kernel_PnP_403_0(Etw):
    pattern = Struct(
        "DeviceInstanceId" / WString,
        "DriverName" / WString,
        "ClassGuid" / Guid,
        "DriverDate" / WString,
        "DriverVersion" / WString,
        "DriverProvider" / WString,
        "DriverInbox" / Int8ul,
        "DriverSection" / WString,
        "DriverRank" / Int32ul,
        "MatchingDeviceId" / WString,
        "OutrankedDrivers" / WString,
        "DeviceUpdated" / Int8ul,
        "Status" / Int32ul,
        "ParentDeviceInstanceId" / WString
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=410, version=0)
class Microsoft_Windows_Kernel_PnP_410_0(Etw):
    pattern = Struct(
        "DeviceInstanceId" / WString,
        "DriverName" / WString,
        "ClassGuid" / Guid,
        "ServiceName" / WString,
        "LowerFilters" / WString,
        "UpperFilters" / WString,
        "Problem" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=411, version=0)
class Microsoft_Windows_Kernel_PnP_411_0(Etw):
    pattern = Struct(
        "DeviceInstanceId" / WString,
        "DriverName" / WString,
        "ClassGuid" / Guid,
        "ServiceName" / WString,
        "LowerFilters" / WString,
        "UpperFilters" / WString,
        "Problem" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=412, version=0)
class Microsoft_Windows_Kernel_PnP_412_0(Etw):
    pattern = Struct(
        "DeviceInstanceId" / WString,
        "DriverName" / WString,
        "ClassGuid" / Guid,
        "ServiceName" / WString,
        "LowerFilters" / WString,
        "UpperFilters" / WString,
        "Problem" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=420, version=0)
class Microsoft_Windows_Kernel_PnP_420_0(Etw):
    pattern = Struct(
        "DeviceInstanceId" / WString,
        "ClassGuid" / Guid,
        "Problem" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=421, version=0)
class Microsoft_Windows_Kernel_PnP_421_0(Etw):
    pattern = Struct(
        "DeviceInstanceId" / WString,
        "ClassGuid" / Guid,
        "Problem" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=430, version=0)
class Microsoft_Windows_Kernel_PnP_430_0(Etw):
    pattern = Struct(
        "DeviceInstanceId" / WString
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=440, version=0)
class Microsoft_Windows_Kernel_PnP_440_0(Etw):
    pattern = Struct(
        "DeviceInstanceId" / WString,
        "LastDeviceInstanceId" / WString,
        "ClassGuid" / Guid,
        "LocationPath" / WString,
        "MigrationRank" / Int64ul,
        "Present" / Int8ul,
        "Status" / Int32ul
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=441, version=0)
class Microsoft_Windows_Kernel_PnP_441_0(Etw):
    pattern = Struct(
        "DeviceInstanceId" / WString,
        "LastDeviceInstanceId" / WString,
        "ClassGuid" / Guid,
        "LocationPath" / WString,
        "MigrationRank" / Int64ul,
        "Present" / Int8ul,
        "Status" / Int32ul
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=442, version=0)
class Microsoft_Windows_Kernel_PnP_442_0(Etw):
    pattern = Struct(
        "DeviceInstanceId" / WString,
        "LastDeviceInstanceId" / WString,
        "ClassGuid" / Guid,
        "LocationPath" / WString,
        "MigrationRank" / Int64ul,
        "Present" / Int8ul,
        "Status" / Int32ul
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=500, version=0)
class Microsoft_Windows_Kernel_PnP_500_0(Etw):
    pattern = Struct(
        "QueryAddress" / Int64ul,
        "ProcessId" / Int32ul,
        "ObjectType" / WString,
        "QueryType" / WString,
        "ObjectId" / WString,
        "QueryFlags" / WString,
        "PreferredLanguages" / WString,
        "RequestedProperties" / WString,
        "FilterExpression" / WString
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=501, version=0)
class Microsoft_Windows_Kernel_PnP_501_0(Etw):
    pattern = Struct(
        "QueryAddress" / Int64ul
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=502, version=0)
class Microsoft_Windows_Kernel_PnP_502_0(Etw):
    pattern = Struct(
        "QueryAddress" / Int64ul
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=503, version=0)
class Microsoft_Windows_Kernel_PnP_503_0(Etw):
    pattern = Struct(
        "QueryAddress" / Int64ul
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=600, version=0)
class Microsoft_Windows_Kernel_PnP_600_0(Etw):
    pattern = Struct(
        "HardwareConfigurationId" / Int32ul,
        "Driver" / WString,
        "StartType" / Int32ul
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=700, version=0)
class Microsoft_Windows_Kernel_PnP_700_0(Etw):
    pattern = Struct(
        "Filter" / WString,
        "FilterBy" / WString,
        "OnlyPresent" / Int8ul
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=701, version=0)
class Microsoft_Windows_Kernel_PnP_701_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=702, version=0)
class Microsoft_Windows_Kernel_PnP_702_0(Etw):
    pattern = Struct(
        "Class" / Guid,
        "Device" / WString,
        "OnlyPresent" / Int8ul
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=703, version=0)
class Microsoft_Windows_Kernel_PnP_703_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=704, version=0)
class Microsoft_Windows_Kernel_PnP_704_0(Etw):
    pattern = Struct(
        "QueryRemoveType" / Int32ul,
        "Device" / WString
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=705, version=0)
class Microsoft_Windows_Kernel_PnP_705_0(Etw):
    pattern = Struct(
        "Device" / WString
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=800, version=0)
class Microsoft_Windows_Kernel_PnP_800_0(Etw):
    pattern = Struct(
        "DeviceNode" / Int64ul
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=801, version=0)
class Microsoft_Windows_Kernel_PnP_801_0(Etw):
    pattern = Struct(
        "DeviceNode" / Int64ul,
        "DeviceInstancePath" / WString
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=802, version=0)
class Microsoft_Windows_Kernel_PnP_802_0(Etw):
    pattern = Struct(
        "DeviceNode" / Int64ul
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=803, version=0)
class Microsoft_Windows_Kernel_PnP_803_0(Etw):
    pattern = Struct(
        "Phase" / Int32ul,
        "Device" / WString
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=804, version=0)
class Microsoft_Windows_Kernel_PnP_804_0(Etw):
    pattern = Struct(
        "Phase" / Int32ul,
        "Device" / WString
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=805, version=0)
class Microsoft_Windows_Kernel_PnP_805_0(Etw):
    pattern = Struct(
        "Phase" / Int32ul,
        "Device" / WString
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=806, version=0)
class Microsoft_Windows_Kernel_PnP_806_0(Etw):
    pattern = Struct(
        "Phase" / Int32ul,
        "Device" / WString
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=807, version=0)
class Microsoft_Windows_Kernel_PnP_807_0(Etw):
    pattern = Struct(
        "ServiceType" / Int32ul,
        "DriverNameLength" / Int16ul,
        "DriverName" / Bytes(lambda this: this.DriverNameLength),
        "DeviceInstancePath" / WString
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=808, version=0)
class Microsoft_Windows_Kernel_PnP_808_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=810, version=0)
class Microsoft_Windows_Kernel_PnP_810_0(Etw):
    pattern = Struct(
        "Device" / WString,
        "ReenumerateType" / Int32ul
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=811, version=0)
class Microsoft_Windows_Kernel_PnP_811_0(Etw):
    pattern = Struct(
        "Device" / WString,
        "ReenumerateType" / Int32ul
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=812, version=0)
class Microsoft_Windows_Kernel_PnP_812_0(Etw):
    pattern = Struct(
        "Device" / WString,
        "ReenumerateType" / Int32ul
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=813, version=0)
class Microsoft_Windows_Kernel_PnP_813_0(Etw):
    pattern = Struct(
        "Device" / WString
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=814, version=0)
class Microsoft_Windows_Kernel_PnP_814_0(Etw):
    pattern = Struct(
        "Device" / WString
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=815, version=0)
class Microsoft_Windows_Kernel_PnP_815_0(Etw):
    pattern = Struct(
        "Device" / WString
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=816, version=0)
class Microsoft_Windows_Kernel_PnP_816_0(Etw):
    pattern = Struct(
        "Device" / WString,
        "RequestType" / Int32ul
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=817, version=0)
class Microsoft_Windows_Kernel_PnP_817_0(Etw):
    pattern = Struct(
        "Device" / WString,
        "RequestType" / Int32ul
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=818, version=0)
class Microsoft_Windows_Kernel_PnP_818_0(Etw):
    pattern = Struct(
        "Device" / WString,
        "RequestType" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=819, version=0)
class Microsoft_Windows_Kernel_PnP_819_0(Etw):
    pattern = Struct(
        "Device" / WString,
        "RequestType" / Int32ul
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=820, version=0)
class Microsoft_Windows_Kernel_PnP_820_0(Etw):
    pattern = Struct(
        "Device" / WString,
        "RequestType" / Int32ul
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=821, version=0)
class Microsoft_Windows_Kernel_PnP_821_0(Etw):
    pattern = Struct(
        "Device" / WString,
        "RequestType" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=830, version=0)
class Microsoft_Windows_Kernel_PnP_830_0(Etw):
    pattern = Struct(
        "Device" / WString
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=831, version=0)
class Microsoft_Windows_Kernel_PnP_831_0(Etw):
    pattern = Struct(
        "Device" / WString
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=832, version=0)
class Microsoft_Windows_Kernel_PnP_832_0(Etw):
    pattern = Struct(
        "Device" / WString
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=840, version=0)
class Microsoft_Windows_Kernel_PnP_840_0(Etw):
    pattern = Struct(
        "DeviceInstanceLength" / Int16ul,
        "DeviceInstance" / Bytes(lambda this: this.DeviceInstanceLength)
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=841, version=0)
class Microsoft_Windows_Kernel_PnP_841_0(Etw):
    pattern = Struct(
        "DeviceInstanceLength" / Int16ul,
        "DeviceInstance" / Bytes(lambda this: this.DeviceInstanceLength),
        "Status" / Int32ul,
        "VetoType" / Int32ul,
        "VetoNameLength" / Int16ul,
        "VetoName" / Bytes(lambda this: this.VetoNameLength)
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=850, version=0)
class Microsoft_Windows_Kernel_PnP_850_0(Etw):
    pattern = Struct(
        "Device" / WString
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=851, version=0)
class Microsoft_Windows_Kernel_PnP_851_0(Etw):
    pattern = Struct(
        "Device" / WString
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=852, version=0)
class Microsoft_Windows_Kernel_PnP_852_0(Etw):
    pattern = Struct(
        "DeviceInstanceLength" / Int16ul,
        "DeviceInstance" / Bytes(lambda this: this.DeviceInstanceLength)
    )


@declare(guid=guid("9c205a39-1250-487d-abd7-e831c6290539"), event_id=853, version=0)
class Microsoft_Windows_Kernel_PnP_853_0(Etw):
    pattern = Struct(
        "DeviceInstanceLength" / Int16ul,
        "DeviceInstance" / Bytes(lambda this: this.DeviceInstanceLength),
        "Status" / Int32ul
    )

