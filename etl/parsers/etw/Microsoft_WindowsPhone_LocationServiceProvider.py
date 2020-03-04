# -*- coding: utf-8 -*-
"""
Microsoft-WindowsPhone-LocationServiceProvider
GUID : 4d13548f-c7b8-4174-bb7a-d7f64bf22d29
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=12, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_12_0(Etw):
    pattern = Struct(
        "Message" / Int64ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=13, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_13_0(Etw):
    pattern = Struct(
        "ExInfo0" / Int32ul,
        "ExInfo1" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=14, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_14_0(Etw):
    pattern = Struct(
        "Component" / Int32ul,
        "ComponentMsgId" / Int32ul,
        "szCustomString" / WString,
        "dwArg1" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=15, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_15_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "Filename" / CString,
        "Line" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=16, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_16_0(Etw):
    pattern = Struct(
        "HR" / Int32ul,
        "CustomMessage" / WString,
        "Function" / CString,
        "CallingCode" / CString,
        "Filename" / CString,
        "Line" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=17, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_17_0(Etw):
    pattern = Struct(
        "context" / Int64ul,
        "component" / Int32ul,
        "istakeref" / Int8ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=100, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_100_0(Etw):
    pattern = Struct(
        "Accuracy" / Int32ul,
        "Generate" / Int32ul,
        "dwHint" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=101, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_101_0(Etw):
    pattern = Struct(
        "Latitude" / Double,
        "Longitude" / Double,
        "Altitude" / Double,
        "HorizontalAccuracy" / Double,
        "VerticalAccuracy" / Double,
        "Heading" / Double,
        "Velocity" / Double,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=200, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_200_0(Etw):
    pattern = Struct(
        "Result" / Int32ul,
        "GnssEventType" / Int32ul,
        "NumberOfBytesTransferred" / Int64ul,
        "GnssEventSize" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=201, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_201_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "SessionType" / Int32ul,
        "RequestParameter" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=202, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_202_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=203, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_203_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "SessionType" / Int32ul,
        "RequestParameter" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=204, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_204_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=205, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_205_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "Status" / Int32ul,
        "Timestamp" / Int64ul,
        "IsIntermediate" / Int8ul,
        "Latitude" / Double,
        "Longitude" / Double,
        "Altitude" / Double,
        "Speed" / Double,
        "Heading" / Double,
        "hAccuracy" / Int32ul,
        "vAccuracy" / Int32ul,
        "SpeedAccuracy" / Int32ul,
        "hDilutionOfPrecision" / Float32l,
        "PositionDilutionOfPrecision" / Float32l
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=206, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_206_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "SessionType" / Int32ul,
        "RequestParameter" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=207, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_207_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "Ioctl" / Int32ul,
        "Result" / Int32ul,
        "Duration" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=208, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_208_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "SatelliteData" / WString
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=209, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_209_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "Result" / Int32ul,
        "NumberOfBytesTransferred" / Int64ul,
        "FixLevelOfDetails" / Int32ul,
        "ExpectedMinimumBytes" / Int32ul,
        "ExpectedMinimumSatelliteBytes" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=210, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_210_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "Pe" / Int32ul,
        "SessionType" / Int32ul,
        "AccuracyType" / Int32ul,
        "AccuracyValue" / Int32ul,
        "RequestParameter" / Int32ul,
        "AgeValue" / Int32ul,
        "IsVenueMandatory" / Int8ul,
        "IsClientSession" / Int8ul,
        "AttachedAcquireId" / Int32ul,
        "OwnerId" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=211, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_211_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "Pe" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=212, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_212_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "Pe" / Int32ul,
        "Status" / Int32ul,
        "SourcePe" / Int32ul,
        "Timestamp" / Int64ul,
        "IsIntermediate" / Int8ul,
        "Latitude" / Double,
        "Longitude" / Double,
        "HorizontalAccuracy" / Int32ul,
        "Speed" / Double,
        "Floor" / WString,
        "VenueId" / WString
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=213, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_213_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "Pe" / Int32ul,
        "ProductId" / Guid,
        "UserSid" / WString,
        "PackageId" / WString,
        "CallerName" / WString
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=220, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_220_0(Etw):
    pattern = Struct(
        "Result" / Int32ul,
        "ReportStatus" / Int32ul,
        "Timestamp" / Int64ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=221, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_221_0(Etw):
    pattern = Struct(
        "Result" / Int32ul,
        "ReportStatus" / Int32ul,
        "BlobSize" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=222, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_222_0(Etw):
    pattern = Struct(
        "WinHttpResult" / Int32ul,
        "OrionResult" / Int32ul,
        "Latitude" / Double,
        "Longitude" / Double,
        "Accuracy" / Double
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=230, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_230_0(Etw):
    pattern = Struct(
        "Hslp" / CString,
        "HslpSource" / Int32ul,
        "HslpFromImsi" / CString
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=231, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_231_0(Etw):
    pattern = Struct(
        "MPC" / CString,
        "PDE" / CString,
        "ApplicationType" / Int8ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=232, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_232_0(Etw):
    pattern = Struct(
        "Major" / Int32ul,
        "Minor" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=233, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_233_0(Etw):
    pattern = Struct(
        "Action" / Int32ul,
        "Name" / CString,
        "Size" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=234, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_234_0(Etw):
    pattern = Struct(
        "CommandType" / Int32ul,
        "Value" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=235, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_235_0(Etw):
    pattern = Struct(
        "InjectionType" / Int32ul,
        "InjectionStatus" / Int32ul,
        "InjectionDataSize" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=236, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_236_0(Etw):
    pattern = Struct(
        "RequestId" / Int32ul,
        "RequestType" / Int32ul,
        "RequestNotificationType" / Int32ul,
        "RequestPlaneType" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=237, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_237_0(Etw):
    pattern = Struct(
        "RequestId" / Int32ul,
        "UserResponse" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=238, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_238_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=239, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_239_0(Etw):
    pattern = Struct(
        "InjectionType" / Int32ul,
        "BlobFormat" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=240, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_240_0(Etw):
    pattern = Struct(
        "Trigger" / Int32ul,
        "RegStatus" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=241, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_241_0(Etw):
    pattern = Struct(
        "InjectionType" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=242, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_242_0(Etw):
    pattern = Struct(
        "InjectionStatus" / Int32ul,
        "Latitude" / Double,
        "Longitude" / Double,
        "Altitude" / Double,
        "Speed" / Double,
        "Heading" / Double,
        "hAccuracy" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=243, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_243_0(Etw):
    pattern = Struct(
        "InjectionStatus" / Int32ul,
        "UtcTime" / Int64ul,
        "Uncertainty" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=244, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_244_0(Etw):
    pattern = Struct(
        "InjectionStatus" / Int32ul,
        "BlobVersion" / Int32ul,
        "BlobFormat" / Int32ul,
        "BlobSize" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=245, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_245_0(Etw):
    pattern = Struct(
        "AppId" / Int32ul,
        "GeofenceId" / Int32ul,
        "ReturnId" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=246, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_246_0(Etw):
    pattern = Struct(
        "Id" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=247, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_247_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=248, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_248_0(Etw):
    pattern = Struct(
        "Id" / Int32ul,
        "State" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=249, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_249_0(Etw):
    pattern = Struct(
        "State" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=250, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_250_0(Etw):
    pattern = Struct(
        "ARFCN" / Int32ul,
        "BaseStationID" / Int32ul,
        "CellID" / Int32ul,
        "LocationAreaCode" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=251, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_251_0(Etw):
    pattern = Struct(
        "MobileCountryCode" / Int32ul,
        "MobileNetworkCode" / Int32ul,
        "CellID" / Int32ul,
        "LocationAreaCode" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=252, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_252_0(Etw):
    pattern = Struct(
        "BaseLat" / Int32ul,
        "BaseLong" / Int32ul,
        "BaseStationID" / Int32ul,
        "NID" / Int32ul,
        "SID" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=253, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_253_0(Etw):
    pattern = Struct(
        "MobileCountryCode" / Int32ul,
        "MobileNetworkCode" / Int32ul,
        "CellID" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=254, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_254_0(Etw):
    pattern = Struct(
        "Neighbors" / WString
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=255, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_255_0(Etw):
    pattern = Struct(
        "MobileCountryCode" / Int32ul,
        "MobileNetworkCode" / Int32ul,
        "LocationAreaCode" / Int32ul,
        "CellID" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=256, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_256_0(Etw):
    pattern = Struct(
        "Params" / Int32ul,
        "Executor" / Int32ul,
        "UiccApp" / Int32ul,
        "LocationAreaCode" / Int32ul,
        "TrackingAreaCode" / Int32ul,
        "CellID" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=257, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_257_0(Etw):
    pattern = Struct(
        "hrResult" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=258, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_258_0(Etw):
    pattern = Struct(
        "NeighborsBeaconHash" / WString
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=259, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_259_0(Etw):
    pattern = Struct(
        "IsMulticellUsed" / Int8ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=260, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_260_0(Etw):
    pattern = Struct(
        "MacAddress" / WString,
        "SignalStrength" / Int32sl
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=261, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_261_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "State" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=262, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_262_0(Etw):
    pattern = Struct(
        "MacAddresses" / WString
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=265, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_265_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "IsRecoverable" / Int8ul,
        "Description" / WString
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=266, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_266_0(Etw):
    pattern = Struct(
        "DeviceAvailable" / Int8ul,
        "SymbolicLink" / WString,
        "DeviceInUse" / Int8ul,
        "hr" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=267, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_267_0(Etw):
    pattern = Struct(
        "SymbolicLink" / WString,
        "IsExternal" / Int8ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=268, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_268_0(Etw):
    pattern = Struct(
        "SymbolicLink" / WString,
        "IsExternal" / Int8ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=269, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_269_0(Etw):
    pattern = Struct(
        "SymbolicLink" / WString
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=270, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_270_0(Etw):
    pattern = Struct(
        "Result" / Int32ul,
        "PE" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=271, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_271_0(Etw):
    pattern = Struct(
        "Result" / Int32ul,
        "PE" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=272, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_272_0(Etw):
    pattern = Struct(
        "AdapterName" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=273, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_273_0(Etw):
    pattern = Struct(
        "RequestId" / Int64ul,
        "CachedPositions" / WString
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=274, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_274_0(Etw):
    pattern = Struct(
        "IsInsideVenue" / Int8ul,
        "Lat" / Double,
        "Lon" / Double,
        "Acc" / Int32ul,
        "SourcePe" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=280, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_280_0(Etw):
    pattern = Struct(
        "DcpProfile" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=281, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_281_0(Etw):
    pattern = Struct(
        "SizeInBytes" / Int32ul,
        "DcpProfile" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=282, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_282_0(Etw):
    pattern = Struct(
        "SourcePE" / Int32ul,
        "IsReadyForData" / Int8ul,
        "IsValidData" / Int8ul,
        "Result" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=283, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_283_0(Etw):
    pattern = Struct(
        "rawDataListSize" / Int32ul,
        "IsCollectionStateActive" / Int8ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=284, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_284_0(Etw):
    pattern = Struct(
        "Level" / Int32ul,
        "CollectionType" / Int32ul,
        "IsBufferFull" / Int8ul,
        "IsBatterySavings" / Int8ul,
        "IsUserPresenceOn" / Int8ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=290, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_290_0(Etw):
    pattern = Struct(
        "PrimaryPE" / Int32ul,
        "AcquireId" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=291, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_291_0(Etw):
    pattern = Struct(
        "PeRole" / Int32ul,
        "RemainingTime" / Int32ul,
        "hr" / Int32ul,
        "AcquireId" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=292, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_292_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "SourcePe" / Int32ul,
        "Accuracy" / Int32ul,
        "AcquireId" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=294, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_294_0(Etw):
    pattern = Struct(
        "DistanceThreshold" / Int32ul,
        "Speed" / Double,
        "MDUsed" / Int8ul,
        "MovementPrecision" / Int32ul,
        "SpeedBasedWaitTimeSec" / Int32ul,
        "MDBasedWaitTimeSec" / Int32ul,
        "MinWaitTimeToMeetBudgetSec" / Int32ul,
        "SelectedWaitTimeSec" / Int32ul,
        "CumulativeRunningTimeSec" / Int64ul,
        "CumulativeAcquireTimeSec" / Int64ul,
        "RequestsCount" / Int32ul,
        "IsSpeedUnknown" / Int8ul,
        "RecentMovementTimeBoundApplied" / Int8ul,
        "AcquireId" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=295, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_295_0(Etw):
    pattern = Struct(
        "SpeedEstimate" / Double,
        "Bearing" / Double,
        "NumberOfPositions" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=296, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_296_0(Etw):
    pattern = Struct(
        "Timestamp" / Int64ul,
        "Latitude" / Double,
        "Longitude" / Double,
        "hAccuracy" / Double
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=298, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_298_0(Etw):
    pattern = Struct(
        "UnreliablePositionAccuracy" / Int32ul,
        "UnreliablePositionSourcePe" / Int32ul,
        "ReliablePositionAccuracy" / Int32ul,
        "ReliablePositionSourcePe" / Int32ul,
        "AcquireId" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=299, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_299_0(Etw):
    pattern = Struct(
        "PeCount" / Int32ul,
        "Pe1" / Int32ul,
        "Pe2" / Int32ul,
        "Pe3" / Int32ul,
        "Pe4" / Int32ul,
        "Pe5" / Int32ul,
        "Pe6" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=300, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_300_0(Etw):
    pattern = Struct(
        "RequestId" / Int32ul,
        "RequestType" / Int32ul,
        "EndpointLengthInChars" / Int32ul,
        "Endpoint" / Bytes(lambda this: this.EndpointLengthInChars),
        "TrackingIdLengthInChars" / Int32ul,
        "TrackingId" / Bytes(lambda this: this.TrackingIdLengthInChars)
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=301, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_301_0(Etw):
    pattern = Struct(
        "RequestId" / Int32ul,
        "RequestType" / Int32ul,
        "Latitude" / Double,
        "Longitude" / Double,
        "ServerStatus" / Int32ul,
        "MappedHResult" / Int32ul,
        "Accuracy" / Int32ul,
        "Floor" / WString,
        "VenueId" / WString,
        "StatusStringLengthInChars" / Int32ul,
        "StatusString" / Bytes(lambda this: this.StatusStringLengthInChars),
        "OrionSource" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=303, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_303_0(Etw):
    pattern = Struct(
        "RequestId" / Int32ul,
        "RequestType" / Int32ul,
        "ServerStatus" / Int32ul,
        "MappedHResult" / Int32ul,
        "StatusStringLengthInChars" / Int32ul,
        "StatusString" / Bytes(lambda this: this.StatusStringLengthInChars)
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=304, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_304_0(Etw):
    pattern = Struct(
        "RequestId" / Int32ul,
        "RequestType" / Int32ul,
        "ServerStatus" / Int32ul,
        "MappedHResult" / Int32ul,
        "StatusStringLengthInChars" / Int32ul,
        "StatusString" / Bytes(lambda this: this.StatusStringLengthInChars)
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=306, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_306_0(Etw):
    pattern = Struct(
        "RequestId" / Int32ul,
        "RequestType" / Int32ul,
        "Reason" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=307, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_307_0(Etw):
    pattern = Struct(
        "WebproxyRequestId" / Int32ul,
        "WebproxyRequestType" / Int32ul,
        "WinHttpHandle" / Int32ul,
        "WinHttpEventType" / Int32ul,
        "WinhttpCallbackStatus" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=308, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_308_0(Etw):
    pattern = Struct(
        "WebproxyRequestId" / Int32ul,
        "WebproxyRequestType" / Int32ul,
        "WinHttpHandle" / Int32ul,
        "WinHttpApiType" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=309, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_309_0(Etw):
    pattern = Struct(
        "PayloadLengthInChars" / Int32ul,
        "Payload" / Bytes(lambda this: this.PayloadLengthInChars)
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=310, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_310_0(Etw):
    pattern = Struct(
        "PayloadLengthInChars" / Int32ul,
        "Payload" / Bytes(lambda this: this.PayloadLengthInChars)
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=401, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_401_0(Etw):
    pattern = Struct(
        "hr" / Int32ul,
        "hrWifiRegistration" / Int32ul,
        "hrCellRegistration" / Int32ul,
        "WifiConnectionState" / Int32ul,
        "WifiThrottlingOn" / Int8ul,
        "WifiThrottlingOnElapsedTimeSec" / Int64ul,
        "CellThrottlingOn" / Int8ul,
        "CellThrottlingOnElapsedTimeSec" / Int64ul,
        "ActivityDetectionThrottlingOn" / Int8ul,
        "ActivityDetectionThrottlingOnElapsedTimeSec" / Int64ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=402, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_402_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=403, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_403_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=404, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_404_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=405, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_405_0(Etw):
    pattern = Struct(
        "hr" / Int32ul,
        "WifiConnectionState" / Int32ul,
        "WifiThrottlingOn" / Int8ul,
        "WifiThrottlingOnElapsedTimeSec" / Int64ul,
        "CellThrottlingOn" / Int8ul,
        "CellThrottlingOnElapsedTimeSec" / Int64ul,
        "ADThrottlingOn" / Int8ul,
        "ADThrottlingOnElapsedTimeSec" / Int64ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=406, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_406_0(Etw):
    pattern = Struct(
        "PeName" / Int32ul,
        "IsPrimaryNativeTracking" / Int8ul,
        "AcquireId" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=407, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_407_0(Etw):
    pattern = Struct(
        "SessionType" / Int32ul,
        "IsSupportsNativePT" / Int8ul,
        "IsSupportsNativeDT" / Int8ul,
        "IsSupportsRequest" / Int8ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=500, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_500_0(Etw):
    pattern = Struct(
        "GeolocationClass" / Int64ul,
        "SessionType" / Int32ul,
        "AgeValue" / Int32ul,
        "AccuracyValue" / Int32ul,
        "RequestParameter" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=501, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_501_0(Etw):
    pattern = Struct(
        "GeolocationClass" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=502, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_502_0(Etw):
    pattern = Struct(
        "GeolocationClass" / Int64ul,
        "PositionStatus" / Int32ul,
        "Latitude" / Double,
        "Longitude" / Double,
        "HorizontalAccuracy" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=503, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_503_0(Etw):
    pattern = Struct(
        "Geolocator" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=504, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_504_0(Etw):
    pattern = Struct(
        "State" / Int32sl
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=525, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_525_0(Etw):
    pattern = Struct(
        "Index" / Int32ul,
        "Latitude" / Double,
        "Longitude" / Double,
        "Radius" / Double,
        "StartTime" / Int64ul,
        "Duration" / Int64ul,
        "DwellTime" / Int64ul,
        "SingleUse" / Int8ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=526, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_526_0(Etw):
    pattern = Struct(
        "Index" / Int32ul,
        "Latitude" / Double,
        "Longitude" / Double,
        "Radius" / Double,
        "StartTime" / Int64ul,
        "Duration" / Int64ul,
        "DwellTime" / Int64ul,
        "SingleUse" / Int8ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=528, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_528_0(Etw):
    pattern = Struct(
        "TriggerType" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=529, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_529_0(Etw):
    pattern = Struct(
        "TriggerType" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=531, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_531_0(Etw):
    pattern = Struct(
        "TriggerType" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=534, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_534_0(Etw):
    pattern = Struct(
        "AppId" / Int32ul,
        "GeofenceId" / Int32ul,
        "Latitude" / Double,
        "Longitude" / Double,
        "Radius" / Double,
        "StartTime" / Int64ul,
        "Duration" / Int64ul,
        "DwellTime" / Int64ul,
        "SingleUse" / Int8ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=550, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_550_0(Etw):
    pattern = Struct(
        "Operation" / CString,
        "Status" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=551, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_551_0(Etw):
    pattern = Struct(
        "Operation" / CString,
        "ClientId" / Int32ul,
        "EventId" / Guid,
        "Status" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=552, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_552_0(Etw):
    pattern = Struct(
        "TriggerType" / Int32ul,
        "ForegroundEvent" / Int32ul,
        "RegistrationOperation" / Int32ul,
        "ProccessId" / Int32ul,
        "ApplicationId" / Int32ul,
        "EventId" / Guid,
        "Status" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=553, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_553_0(Etw):
    pattern = Struct(
        "AppId" / Int32ul,
        "GeofenceId" / Int32ul,
        "Latitude" / Double,
        "Longitude" / Double,
        "Radius" / Double,
        "StartTime" / Int64ul,
        "Duration" / Int64ul,
        "DwellTime" / Int64ul,
        "SingleUse" / Int8ul,
        "hr" / Int32ul,
        "CallerName" / WString
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=554, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_554_0(Etw):
    pattern = Struct(
        "AppId" / Int32ul,
        "GeofenceId" / Int32ul,
        "hr" / Int32ul,
        "CallerName" / WString
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=555, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_555_0(Etw):
    pattern = Struct(
        "AppId" / Int32ul,
        "hr" / Int32ul,
        "CallerName" / WString
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=556, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_556_0(Etw):
    pattern = Struct(
        "AppId" / Int32ul,
        "GeofencesCount" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=557, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_557_0(Etw):
    pattern = Struct(
        "AppId" / Int32ul,
        "GeofenceReportsCount" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=558, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_558_0(Etw):
    pattern = Struct(
        "GeofenceId" / Int32ul,
        "Trigger" / Int32ul,
        "RemovalReason" / Int32ul,
        "PositionStatus" / Int32ul,
        "Latitude" / Double,
        "Longitude" / Double,
        "Accuracy" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=559, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_559_0(Etw):
    pattern = Struct(
        "WnfForegroundEvent" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=560, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_560_0(Etw):
    pattern = Struct(
        "ClientId" / Int32ul,
        "EventId" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=600, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_600_0(Etw):
    pattern = Struct(
        "InstanceId" / Int32ul,
        "EventType" / Int32ul,
        "EventSource" / Int32ul,
        "TaskhostSource" / Int32ul,
        "CurrentState" / Int32ul,
        "Timeout" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=601, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_601_0(Etw):
    pattern = Struct(
        "InstanceId" / Int32ul,
        "GeoStatus" / Int32ul,
        "GeoPermission" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=700, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_700_0(Etw):
    pattern = Struct(
        "AppId" / Int32ul,
        "GeofenceId" / Int32ul,
        "Trigger" / Int32ul,
        "Latitude" / Double,
        "Longitude" / Double
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=701, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_701_0(Etw):
    pattern = Struct(
        "Tracker" / Int32ul,
        "AppId" / Int32ul,
        "GeofenceId" / Int32ul,
        "State" / Int32ul,
        "Latitude" / Double,
        "Longitude" / Double
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=703, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_703_0(Etw):
    pattern = Struct(
        "Latitude" / Double,
        "Longitude" / Double,
        "Radius" / Double,
        "NumberOfGeofences" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=704, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_704_0(Etw):
    pattern = Struct(
        "AppId" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=705, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_705_0(Etw):
    pattern = Struct(
        "AppId" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=706, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_706_0(Etw):
    pattern = Struct(
        "Tracker" / Int32ul,
        "AppId" / Int32ul,
        "GeofenceId" / Int32ul,
        "Latitude" / Double,
        "Longitude" / Double,
        "Radius" / Double,
        "DwellTime" / Int64ul,
        "StartTime" / Int64ul,
        "Duration" / Int64ul,
        "SingleUse" / Int8ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=707, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_707_0(Etw):
    pattern = Struct(
        "Tracker" / Int32ul,
        "AppId" / Int32ul,
        "GeofenceId" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=708, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_708_0(Etw):
    pattern = Struct(
        "Active" / Int8ul,
        "Distance" / Double,
        "Accuracy" / Double
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=709, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_709_0(Etw):
    pattern = Struct(
        "AppId" / Int32ul,
        "GeofenceId" / Int32ul,
        "Latitude" / Double,
        "Longitude" / Double,
        "Radius" / Double,
        "DwellTime" / Int64ul,
        "StartTime" / Int64ul,
        "Duration" / Int64ul,
        "SingleUse" / Int8ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=710, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_710_0(Etw):
    pattern = Struct(
        "Tracker" / Int32ul,
        "State" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=711, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_711_0(Etw):
    pattern = Struct(
        "Tracker" / Int32ul,
        "Enabled" / Int8ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=712, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_712_0(Etw):
    pattern = Struct(
        "AppId" / Int32ul,
        "GeofenceId" / Int32ul,
        "Latitude" / Double,
        "Longitude" / Double,
        "Radius" / Double,
        "DwellTime" / Int64ul,
        "StartTime" / Int64ul,
        "Duration" / Int64ul,
        "SingleUse" / Int8ul,
        "TrackedGeofencesCount" / Int32ul,
        "InternalTrackedGeofencesCount" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=713, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_713_0(Etw):
    pattern = Struct(
        "AppId" / Int32ul,
        "GeofenceId" / Int32ul,
        "TrackedGeofencesCount" / Int32ul,
        "InternalTrackedGeofencesCount" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=800, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_800_0(Etw):
    pattern = Struct(
        "Scenario" / WString,
        "TTFF" / Int32ul,
        "Accuracy" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=900, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_900_0(Etw):
    pattern = Struct(
        "AppId" / Int32ul,
        "GeofenceId" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=901, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_901_0(Etw):
    pattern = Struct(
        "AppId" / Int32ul,
        "GeofenceId" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=902, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_902_0(Etw):
    pattern = Struct(
        "AppId" / Int32ul,
        "GeofenceId" / Int32ul,
        "TriggerState" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=903, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_903_0(Etw):
    pattern = Struct(
        "AppId" / Int32ul,
        "GeofenceId" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=904, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_904_0(Etw):
    pattern = Struct(
        "AppId" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=905, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_905_0(Etw):
    pattern = Struct(
        "AppId" / Int32ul,
        "GeofenceCount" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=906, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_906_0(Etw):
    pattern = Struct(
        "Latitude" / Double,
        "Longitude" / Double,
        "AppCount" / Int32ul,
        "GeofenceCount" / Int32ul,
        "TransitionGeofenceCount" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=907, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_907_0(Etw):
    pattern = Struct(
        "AppId" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=908, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_908_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "hr" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=909, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_909_0(Etw):
    pattern = Struct(
        "AppContext" / WString,
        "AppId" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=1000, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_1000_0(Etw):
    pattern = Struct(
        "Scenario" / WString
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=1001, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_1001_0(Etw):
    pattern = Struct(
        "Scenario" / WString
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=1100, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_1100_0(Etw):
    pattern = Struct(
        "ClientID" / Int64ul,
        "UnconditionalPermissions" / Int32ul,
        "PolicyPermissions" / Int32ul,
        "WinLegacyPolicyPermission" / Int32ul,
        "MasterPermissions" / Int32ul,
        "UserPermissions" / Int32ul,
        "UserWinLegacyPolicyPermissions" / Int32ul,
        "AppPermissions" / Int32ul,
        "IsAppContainer" / Int8ul,
        "UserSid" / WString,
        "PackageFamilyName" / WString
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=1101, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_1101_0(Etw):
    pattern = Struct(
        "ClientID" / Int64ul,
        "UserSid" / WString,
        "PackageFamilyName" / WString
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=1250, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_1250_0(Etw):
    pattern = Struct(
        "PositionId" / Int32ul,
        "InferenceResult" / Int32ul,
        "PositionSource" / Int32ul,
        "PositionStatus" / Int32ul
    )


@declare(guid=guid("4d13548f-c7b8-4174-bb7a-d7f64bf22d29"), event_id=1251, version=0)
class Microsoft_WindowsPhone_LocationServiceProvider_1251_0(Etw):
    pattern = Struct(
        "Trigger" / Int32ul,
        "RegStatus" / Int32ul
    )

