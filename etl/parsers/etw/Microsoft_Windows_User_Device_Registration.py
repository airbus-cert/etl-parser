# -*- coding: utf-8 -*-
"""
Microsoft-Windows-User Device Registration
GUID : 23b8d46b-67dd-40a3-b636-d43e50552c6d
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=101, version=0)
class Microsoft_Windows_User_Device_Registration_101_0(Etw):
    pattern = Struct(
        "ServerMessage" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=102, version=0)
class Microsoft_Windows_User_Device_Registration_102_0(Etw):
    pattern = Struct(
        "JoinRequestType" / Int32sl,
        "JoinRequestTypeSymbolicName" / WString,
        "Domain" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=103, version=0)
class Microsoft_Windows_User_Device_Registration_103_0(Etw):
    pattern = Struct(
        "AuthToken" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=104, version=0)
class Microsoft_Windows_User_Device_Registration_104_0(Etw):
    pattern = Struct(
        "ServerResponse" / WString,
        "ActivityId" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=107, version=0)
class Microsoft_Windows_User_Device_Registration_107_0(Etw):
    pattern = Struct(
        "KeyName" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=108, version=0)
class Microsoft_Windows_User_Device_Registration_108_0(Etw):
    pattern = Struct(
        "UserSid" / WString,
        "IdpDomain" / WString,
        "TenantDomain" / WString,
        "Flags" / Int32ul
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=109, version=0)
class Microsoft_Windows_User_Device_Registration_109_0(Etw):
    pattern = Struct(
        "UserSid" / WString,
        "IdpDomain" / WString,
        "TenantDomain" / WString,
        "UserId" / WString,
        "Flags" / Int32ul
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=110, version=0)
class Microsoft_Windows_User_Device_Registration_110_0(Etw):
    pattern = Struct(
        "JoinType" / Int32sl,
        "JoinTypeSymbolicName" / WString,
        "TenantId" / WString,
        "UPN" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=111, version=0)
class Microsoft_Windows_User_Device_Registration_111_0(Etw):
    pattern = Struct(
        "JoinRequestType" / Int32sl,
        "JoinRequestTypeSymbolicName" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=200, version=0)
class Microsoft_Windows_User_Device_Registration_200_0(Etw):
    pattern = Struct(
        "ExitCode" / Int32sl,
        "Domain" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=201, version=0)
class Microsoft_Windows_User_Device_Registration_201_0(Etw):
    pattern = Struct(
        "ExitCode" / Int32sl,
        "HttpStatus" / Int32ul,
        "ServerMessage" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=202, version=0)
class Microsoft_Windows_User_Device_Registration_202_0(Etw):
    pattern = Struct(
        "ExitCode" / Int32sl,
        "JoinRequestType" / Int32sl,
        "JoinRequestTypeSymbolicName" / WString,
        "Domain" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=203, version=0)
class Microsoft_Windows_User_Device_Registration_203_0(Etw):
    pattern = Struct(
        "ExitCode" / Int32sl,
        "ActivityId" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=204, version=0)
class Microsoft_Windows_User_Device_Registration_204_0(Etw):
    pattern = Struct(
        "ExitCode" / Int32sl,
        "ActivityId" / WString,
        "HttpStatus" / Int32ul,
        "ServerResponse" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=205, version=0)
class Microsoft_Windows_User_Device_Registration_205_0(Etw):
    pattern = Struct(
        "ExitCode" / Int32sl
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=206, version=0)
class Microsoft_Windows_User_Device_Registration_206_0(Etw):
    pattern = Struct(
        "ExitCode" / Int32sl
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=207, version=0)
class Microsoft_Windows_User_Device_Registration_207_0(Etw):
    pattern = Struct(
        "FunctionName" / WString,
        "ParameterName" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=208, version=0)
class Microsoft_Windows_User_Device_Registration_208_0(Etw):
    pattern = Struct(
        "Group" / WString,
        "UserSID" / Sid,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=209, version=0)
class Microsoft_Windows_User_Device_Registration_209_0(Etw):
    pattern = Struct(
        "SID" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=210, version=0)
class Microsoft_Windows_User_Device_Registration_210_0(Etw):
    pattern = Struct(
        "SID" / Sid,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=211, version=0)
class Microsoft_Windows_User_Device_Registration_211_0(Etw):
    pattern = Struct(
        "Group" / WString,
        "UserSID" / Sid,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=212, version=0)
class Microsoft_Windows_User_Device_Registration_212_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Operation" / WString,
        "Path" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=213, version=0)
class Microsoft_Windows_User_Device_Registration_213_0(Etw):
    pattern = Struct(
        "NtStatus" / Int32ul
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=214, version=0)
class Microsoft_Windows_User_Device_Registration_214_0(Etw):
    pattern = Struct(
        "PackageName" / CString,
        "NtStatus" / Int32ul
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=215, version=0)
class Microsoft_Windows_User_Device_Registration_215_0(Etw):
    pattern = Struct(
        "PackageId" / Int32ul,
        "PackageName" / CString,
        "NtStatus" / Int32ul
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=216, version=0)
class Microsoft_Windows_User_Device_Registration_216_0(Etw):
    pattern = Struct(
        "FunctionName" / WString,
        "ParameterName" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=217, version=0)
class Microsoft_Windows_User_Device_Registration_217_0(Etw):
    pattern = Struct(
        "SID" / Sid,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=218, version=0)
class Microsoft_Windows_User_Device_Registration_218_0(Etw):
    pattern = Struct(
        "Email" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=219, version=0)
class Microsoft_Windows_User_Device_Registration_219_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=220, version=0)
class Microsoft_Windows_User_Device_Registration_220_0(Etw):
    pattern = Struct(
        "Format" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=221, version=0)
class Microsoft_Windows_User_Device_Registration_221_0(Etw):
    pattern = Struct(
        "Server" / WString,
        "Port" / Int32ul,
        "AuthMethod" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=222, version=0)
class Microsoft_Windows_User_Device_Registration_222_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=223, version=0)
class Microsoft_Windows_User_Device_Registration_223_0(Etw):
    pattern = Struct(
        "Option" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=224, version=0)
class Microsoft_Windows_User_Device_Registration_224_0(Etw):
    pattern = Struct(
        "Option" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=225, version=0)
class Microsoft_Windows_User_Device_Registration_225_0(Etw):
    pattern = Struct(
        "UserAgent" / WString,
        "AccessType" / Int32ul,
        "ProxyName" / WString,
        "ProxyBypassList" / WString,
        "Flags" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=226, version=0)
class Microsoft_Windows_User_Device_Registration_226_0(Etw):
    pattern = Struct(
        "Server" / WString,
        "Port" / Int16ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=227, version=0)
class Microsoft_Windows_User_Device_Registration_227_0(Etw):
    pattern = Struct(
        "Verb" / WString,
        "Flags" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=228, version=0)
class Microsoft_Windows_User_Device_Registration_228_0(Etw):
    pattern = Struct(
        "NotificationFlags" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=229, version=0)
class Microsoft_Windows_User_Device_Registration_229_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul,
        "HeaderName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=230, version=0)
class Microsoft_Windows_User_Device_Registration_230_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=231, version=0)
class Microsoft_Windows_User_Device_Registration_231_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "WinHttpStatus" / Int32ul,
        "WinHttpStatusFlag" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=232, version=0)
class Microsoft_Windows_User_Device_Registration_232_0(Etw):
    pattern = Struct(
        "StatusCode" / Int32ul,
        "StatusName" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=233, version=0)
class Microsoft_Windows_User_Device_Registration_233_0(Etw):
    pattern = Struct(
        "StatusCode" / Int32ul,
        "ErrorCode" / Int32sl,
        "StatusName" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=234, version=0)
class Microsoft_Windows_User_Device_Registration_234_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=235, version=0)
class Microsoft_Windows_User_Device_Registration_235_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=236, version=0)
class Microsoft_Windows_User_Device_Registration_236_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=237, version=0)
class Microsoft_Windows_User_Device_Registration_237_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=238, version=0)
class Microsoft_Windows_User_Device_Registration_238_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=239, version=0)
class Microsoft_Windows_User_Device_Registration_239_0(Etw):
    pattern = Struct(
        "ExitCode" / Int32sl,
        "JoinType" / Int32sl,
        "JoinTypeSymbolicName" / WString,
        "TenantId" / WString,
        "UPN" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=240, version=0)
class Microsoft_Windows_User_Device_Registration_240_0(Etw):
    pattern = Struct(
        "ExitCode" / Int32sl,
        "JoinRequestType" / Int32sl,
        "JoinRequestTypeSymbolicName" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=241, version=0)
class Microsoft_Windows_User_Device_Registration_241_0(Etw):
    pattern = Struct(
        "KspSessionID" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=242, version=0)
class Microsoft_Windows_User_Device_Registration_242_0(Etw):
    pattern = Struct(
        "Group" / WString,
        "UserSID" / Sid
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=243, version=0)
class Microsoft_Windows_User_Device_Registration_243_0(Etw):
    pattern = Struct(
        "Group" / WString,
        "UserSID" / Sid
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=244, version=0)
class Microsoft_Windows_User_Device_Registration_244_0(Etw):
    pattern = Struct(
        "ExitCode" / Int32sl
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=245, version=0)
class Microsoft_Windows_User_Device_Registration_245_0(Etw):
    pattern = Struct(
        "ExitCode" / Int32sl
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=246, version=0)
class Microsoft_Windows_User_Device_Registration_246_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "SourceId" / WString,
        "DefaultPath" / WString,
        "LocationType" / Int32sl,
        "LocationTypeName" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=247, version=0)
class Microsoft_Windows_User_Device_Registration_247_0(Etw):
    pattern = Struct(
        "ExitCode" / Int32sl
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=248, version=0)
class Microsoft_Windows_User_Device_Registration_248_0(Etw):
    pattern = Struct(
        "ExitCode" / Int32sl,
        "Attribute" / WString,
        "TenantId" / WString,
        "DeviceId" / WString,
        "JoinType" / Int32sl,
        "JoinTypeName" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=249, version=0)
class Microsoft_Windows_User_Device_Registration_249_0(Etw):
    pattern = Struct(
        "ExitCode" / Int32sl,
        "Attribute" / WString,
        "TenantId" / WString,
        "DeviceId" / WString,
        "JoinType" / Int32sl,
        "JoinTypeName" / WString,
        "RequestId" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=250, version=0)
class Microsoft_Windows_User_Device_Registration_250_0(Etw):
    pattern = Struct(
        "Attribute" / WString,
        "TenantId" / WString,
        "DeviceId" / WString,
        "JoinType" / Int32sl,
        "JoinTypeName" / WString,
        "RequestId" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=251, version=0)
class Microsoft_Windows_User_Device_Registration_251_0(Etw):
    pattern = Struct(
        "Attribute" / WString,
        "TenantId" / WString,
        "DeviceId" / WString,
        "JoinType" / Int32sl,
        "JoinTypeName" / WString,
        "RequestId" / WString,
        "HttpStatus" / Int32sl,
        "ServerTime" / WString,
        "ServerMessage" / WString,
        "ResponseBody" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=252, version=0)
class Microsoft_Windows_User_Device_Registration_252_0(Etw):
    pattern = Struct(
        "ExitCode" / Int32sl,
        "Attribute" / WString,
        "TenantId" / WString,
        "DeviceId" / WString,
        "JoinType" / Int32sl,
        "JoinTypeName" / WString,
        "RequestId" / WString,
        "HttpStatus" / Int32sl,
        "ServerTime" / WString,
        "ServerMessage" / WString,
        "ResponseBody" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=253, version=0)
class Microsoft_Windows_User_Device_Registration_253_0(Etw):
    pattern = Struct(
        "HttpStatus" / Int32ul,
        "ResponseBody" / WString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=254, version=0)
class Microsoft_Windows_User_Device_Registration_254_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=255, version=0)
class Microsoft_Windows_User_Device_Registration_255_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32sl,
        "JoinType" / Int32sl,
        "JoinTypeName" / WString,
        "TenantId" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=256, version=0)
class Microsoft_Windows_User_Device_Registration_256_0(Etw):
    pattern = Struct(
        "JoinType" / Int32sl,
        "JoinTypeName" / WString,
        "TenantId" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=257, version=0)
class Microsoft_Windows_User_Device_Registration_257_0(Etw):
    pattern = Struct(
        "Folder" / WString,
        "TaskName" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=258, version=0)
class Microsoft_Windows_User_Device_Registration_258_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32sl,
        "Folder" / WString,
        "TaskName" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=259, version=0)
class Microsoft_Windows_User_Device_Registration_259_0(Etw):
    pattern = Struct(
        "Folder" / WString,
        "TaskName" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=260, version=0)
class Microsoft_Windows_User_Device_Registration_260_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32sl,
        "Folder" / WString,
        "TaskName" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=300, version=0)
class Microsoft_Windows_User_Device_Registration_300_0(Etw):
    pattern = Struct(
        "KeyId" / Guid,
        "UPN" / WString,
        "Attestation" / WString,
        "ClientRequestId" / WString,
        "ServerRequestId" / WString,
        "ServerResponse" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=301, version=0)
class Microsoft_Windows_User_Device_Registration_301_0(Etw):
    pattern = Struct(
        "ExitCode" / Int32sl,
        "ClientRequestId" / WString,
        "ServerRequestId" / WString,
        "ErrorCode" / WString,
        "ServerErrorMessage" / WString,
        "RecommendedClientResponse" / WString,
        "ServerResponse" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=302, version=0)
class Microsoft_Windows_User_Device_Registration_302_0(Etw):
    pattern = Struct(
        "Email" / WString,
        "AuthToken" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=303, version=0)
class Microsoft_Windows_User_Device_Registration_303_0(Etw):
    pattern = Struct(
        "ExitCode" / Int32sl,
        "Email" / WString,
        "AuthToken" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=304, version=0)
class Microsoft_Windows_User_Device_Registration_304_0(Etw):
    pattern = Struct(
        "ExitCode" / Int32sl,
        "ServerErrorMessage" / WString,
        "TenantType" / WString,
        "JoinType" / WString,
        "DebugOutput" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=305, version=0)
class Microsoft_Windows_User_Device_Registration_305_0(Etw):
    pattern = Struct(
        "ExitCode" / Int32sl,
        "ServerErrorMessage" / WString,
        "TenantType" / WString,
        "TenantName" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=307, version=0)
class Microsoft_Windows_User_Device_Registration_307_0(Etw):
    pattern = Struct(
        "ExitCode" / Int32sl
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=308, version=0)
class Microsoft_Windows_User_Device_Registration_308_0(Etw):
    pattern = Struct(
        "UserSID" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=309, version=0)
class Microsoft_Windows_User_Device_Registration_309_0(Etw):
    pattern = Struct(
        "ExitCode" / Int32sl
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=310, version=0)
class Microsoft_Windows_User_Device_Registration_310_0(Etw):
    pattern = Struct(
        "KeyName" / WString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=311, version=0)
class Microsoft_Windows_User_Device_Registration_311_0(Etw):
    pattern = Struct(
        "UserSid" / WString,
        "IdpDomain" / WString,
        "TenantDomain" / WString,
        "Flags" / Int32ul,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=312, version=0)
class Microsoft_Windows_User_Device_Registration_312_0(Etw):
    pattern = Struct(
        "UserSid" / WString,
        "IdpDomain" / WString,
        "TenantDomain" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=314, version=0)
class Microsoft_Windows_User_Device_Registration_314_0(Etw):
    pattern = Struct(
        "UserSid" / WString,
        "IdpDomain" / WString,
        "TenantDomain" / WString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=315, version=0)
class Microsoft_Windows_User_Device_Registration_315_0(Etw):
    pattern = Struct(
        "UserSid" / WString,
        "IdpDomain" / WString,
        "TenantDomain" / WString,
        "UserId" / WString,
        "Flags" / Int32ul,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=316, version=0)
class Microsoft_Windows_User_Device_Registration_316_0(Etw):
    pattern = Struct(
        "UserSid" / WString,
        "IdpDomain" / WString,
        "TenantDomain" / WString,
        "UserId" / WString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=317, version=0)
class Microsoft_Windows_User_Device_Registration_317_0(Etw):
    pattern = Struct(
        "KeyName" / WString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=318, version=0)
class Microsoft_Windows_User_Device_Registration_318_0(Etw):
    pattern = Struct(
        "UserSid" / WString,
        "IdpDomain" / WString,
        "TenantDomain" / WString,
        "UserId" / WString,
        "KeyType" / Int32sl,
        "Flags" / Int32ul,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=319, version=0)
class Microsoft_Windows_User_Device_Registration_319_0(Etw):
    pattern = Struct(
        "UserSid" / WString,
        "IdpDomain" / WString,
        "TenantDomain" / WString,
        "UserId" / WString,
        "ErrorCode" / Int32sl,
        "Flags" / Int32ul
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=320, version=0)
class Microsoft_Windows_User_Device_Registration_320_0(Etw):
    pattern = Struct(
        "HttpStatus" / Int32ul,
        "ResponseBody" / WString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=321, version=0)
class Microsoft_Windows_User_Device_Registration_321_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=322, version=0)
class Microsoft_Windows_User_Device_Registration_322_0(Etw):
    pattern = Struct(
        "AppSid" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=323, version=0)
class Microsoft_Windows_User_Device_Registration_323_0(Etw):
    pattern = Struct(
        "AccountProvider" / WString,
        "Scope" / WString,
        "Client" / WString,
        "Authority" / WString,
        "Resource" / WString,
        "CorrelationId" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=324, version=0)
class Microsoft_Windows_User_Device_Registration_324_0(Etw):
    pattern = Struct(
        "RequestStatus" / Int32sl,
        "RequestStatusSymbolicName" / WString,
        "ProviderErrorCode" / Int32ul,
        "ProviderErrorMessage" / WString,
        "ErrorCode" / Int32sl,
        "CorrelationId" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=325, version=0)
class Microsoft_Windows_User_Device_Registration_325_0(Etw):
    pattern = Struct(
        "CorrelationId" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=326, version=0)
class Microsoft_Windows_User_Device_Registration_326_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=327, version=0)
class Microsoft_Windows_User_Device_Registration_327_0(Etw):
    pattern = Struct(
        "UserSid" / WString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=328, version=0)
class Microsoft_Windows_User_Device_Registration_328_0(Etw):
    pattern = Struct(
        "UserSid" / WString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=329, version=0)
class Microsoft_Windows_User_Device_Registration_329_0(Etw):
    pattern = Struct(
        "AccountProvider" / WString,
        "Scope" / WString,
        "Client" / WString,
        "Authority" / WString,
        "Resource" / WString,
        "CorrelationId" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=330, version=0)
class Microsoft_Windows_User_Device_Registration_330_0(Etw):
    pattern = Struct(
        "AzureADTenantName" / WString,
        "EnterpriseDrsName" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=331, version=0)
class Microsoft_Windows_User_Device_Registration_331_0(Etw):
    pattern = Struct(
        "DebugOutput" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=336, version=0)
class Microsoft_Windows_User_Device_Registration_336_0(Etw):
    pattern = Struct(
        "dwInternetStatus" / Int32ul,
        "dwResult" / Int64ul,
        "dwError" / Int32ul,
        "InternetStatus" / WString,
        "Result" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=337, version=0)
class Microsoft_Windows_User_Device_Registration_337_0(Etw):
    pattern = Struct(
        "dwInternetStatus" / Int32ul,
        "dwResult" / Int64ul,
        "dwError" / Int32ul,
        "InternetStatus" / WString,
        "Result" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=338, version=0)
class Microsoft_Windows_User_Device_Registration_338_0(Etw):
    pattern = Struct(
        "ProxyCount" / Int32ul
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=339, version=0)
class Microsoft_Windows_User_Device_Registration_339_0(Etw):
    pattern = Struct(
        "fProxy" / WString,
        "fBypass" / WString,
        "INTERNET_SCHEME" / Int32ul,
        "pwszProxy" / WString,
        "ProxyPort" / Int32ul
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=340, version=0)
class Microsoft_Windows_User_Device_Registration_340_0(Etw):
    pattern = Struct(
        "dwInternetStatus" / Int32ul,
        "dwResult" / Int64ul,
        "dwError" / Int32ul,
        "InternetStatus" / WString,
        "Result" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=341, version=0)
class Microsoft_Windows_User_Device_Registration_341_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=342, version=0)
class Microsoft_Windows_User_Device_Registration_342_0(Etw):
    pattern = Struct(
        "UserSid" / WString,
        "IdpDomain" / WString,
        "TenantDomain" / WString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=343, version=0)
class Microsoft_Windows_User_Device_Registration_343_0(Etw):
    pattern = Struct(
        "UserSid" / WString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=344, version=0)
class Microsoft_Windows_User_Device_Registration_344_0(Etw):
    pattern = Struct(
        "ExitCode" / Int32sl
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=345, version=0)
class Microsoft_Windows_User_Device_Registration_345_0(Etw):
    pattern = Struct(
        "ExitCode" / Int32sl
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=346, version=0)
class Microsoft_Windows_User_Device_Registration_346_0(Etw):
    pattern = Struct(
        "KeyHash" / WString,
        "UPN" / WString,
        "ClientRequestId" / WString,
        "ServerRequestId" / WString,
        "ServerResponse" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=347, version=0)
class Microsoft_Windows_User_Device_Registration_347_0(Etw):
    pattern = Struct(
        "KeyHash" / WString,
        "ErrorCode" / Int32sl,
        "ClientRequestId" / WString,
        "ServerRequestId" / WString,
        "ServerErrorCode" / WString,
        "ServerErrorMessage" / WString,
        "RecommendedClientResponse" / WString,
        "ServerResponse" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=348, version=0)
class Microsoft_Windows_User_Device_Registration_348_0(Etw):
    pattern = Struct(
        "Email" / WString,
        "TenantId" / WString,
        "AuthToken" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=349, version=0)
class Microsoft_Windows_User_Device_Registration_349_0(Etw):
    pattern = Struct(
        "ExitCode" / Int32sl,
        "Email" / WString,
        "TenantId" / WString,
        "AuthToken" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=350, version=0)
class Microsoft_Windows_User_Device_Registration_350_0(Etw):
    pattern = Struct(
        "KeyId" / WString,
        "AttLevel" / Int64ul,
        "AikStatus" / Int64ul,
        "KeyType" / Int64ul,
        "KeyName" / WString,
        "IdpDomain" / WString,
        "TenantId" / WString,
        "UserEmail" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=351, version=0)
class Microsoft_Windows_User_Device_Registration_351_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32sl,
        "KeyId" / WString,
        "AttLevel" / Int64ul,
        "AikStatus" / Int64ul,
        "KeyType" / Int64ul,
        "KeyName" / WString,
        "IdpDomain" / WString,
        "TenantId" / WString,
        "UserEmail" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=352, version=0)
class Microsoft_Windows_User_Device_Registration_352_0(Etw):
    pattern = Struct(
        "KeyId" / WString,
        "UserSid" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=353, version=0)
class Microsoft_Windows_User_Device_Registration_353_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32sl,
        "KeyId" / WString,
        "UserSid" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=354, version=0)
class Microsoft_Windows_User_Device_Registration_354_0(Etw):
    pattern = Struct(
        "ExitCode" / Int32sl,
        "HttpStatus" / Int32ul,
        "ServerMessage" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=355, version=0)
class Microsoft_Windows_User_Device_Registration_355_0(Etw):
    pattern = Struct(
        "Upn" / WString,
        "TenantId" / WString,
        "Authority" / WString,
        "Resource" / WString,
        "ExitCode" / Int32sl
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=356, version=0)
class Microsoft_Windows_User_Device_Registration_356_0(Etw):
    pattern = Struct(
        "UPN" / WString,
        "TenantId" / WString,
        "ExitCode" / Int32sl
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=357, version=0)
class Microsoft_Windows_User_Device_Registration_357_0(Etw):
    pattern = Struct(
        "Sid" / WString,
        "TenantId" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=358, version=0)
class Microsoft_Windows_User_Device_Registration_358_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "DeviceIsJoined" / WString,
        "AADPrt" / WString,
        "NgcPolicyEnabled" / WString,
        "NgcPostLogonProvisioningEnabled" / WString,
        "NgcHardwarePolicyMet" / WString,
        "UserIsRemote" / WString,
        "LogonCertRequired" / WString,
        "MachinePolicySource" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=359, version=0)
class Microsoft_Windows_User_Device_Registration_359_0(Etw):
    pattern = Struct(
        "ExitCode" / Int32sl,
        "Method" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=360, version=0)
class Microsoft_Windows_User_Device_Registration_360_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "DeviceIsJoined" / WString,
        "AADPrt" / WString,
        "NgcPolicyEnabled" / WString,
        "NgcPostLogonProvisioningEnabled" / WString,
        "NgcHardwarePolicyMet" / WString,
        "UserIsRemote" / WString,
        "LogonCertRequired" / WString,
        "MachinePolicySource" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=361, version=0)
class Microsoft_Windows_User_Device_Registration_361_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "DeviceIsJoined" / WString,
        "AADPrt" / WString,
        "NgcPolicyEnabled" / WString,
        "NgcPostLogonProvisioningEnabled" / WString,
        "NgcHardwarePolicyMet" / WString,
        "UserIsRemote" / WString,
        "LogonCertRequired" / WString,
        "MDMCertEnrollmentReady" / WString,
        "MachinePolicySource" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=362, version=0)
class Microsoft_Windows_User_Device_Registration_362_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "DeviceIsJoined" / WString,
        "AADPrt" / WString,
        "NgcPolicyEnabled" / WString,
        "NgcPostLogonProvisioningEnabled" / WString,
        "NgcHardwarePolicyMet" / WString,
        "UserIsRemote" / WString,
        "LogonCertRequired" / WString,
        "ADFSRaReady" / WString,
        "RATemplateReady" / WString,
        "ADFSPrtPresent" / WString,
        "MachinePolicySource" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=363, version=0)
class Microsoft_Windows_User_Device_Registration_363_0(Etw):
    pattern = Struct(
        "KeyId" / Guid,
        "AttLevel" / Int64ul,
        "AikStatus" / Int64ul,
        "KeyType" / Int64ul,
        "KeyName" / WString,
        "IdpDomain" / WString,
        "TenantId" / WString,
        "UserEmail" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=364, version=0)
class Microsoft_Windows_User_Device_Registration_364_0(Etw):
    pattern = Struct(
        "SavedKeyId" / Guid,
        "SavedKeyName" / WString,
        "SavedIdpDomain" / WString,
        "SavedTenantId" / WString,
        "SavedUserEmail" / WString,
        "KeyName" / WString,
        "IdpDomain" / WString,
        "TenantId" / WString,
        "UserEmail" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=365, version=0)
class Microsoft_Windows_User_Device_Registration_365_0(Etw):
    pattern = Struct(
        "UPN" / WString,
        "TenantId" / WString,
        "ExitCode" / Int32sl
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=366, version=0)
class Microsoft_Windows_User_Device_Registration_366_0(Etw):
    pattern = Struct(
        "Resource" / WString,
        "ExitCode" / Int32sl
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=367, version=0)
class Microsoft_Windows_User_Device_Registration_367_0(Etw):
    pattern = Struct(
        "Properties" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=368, version=0)
class Microsoft_Windows_User_Device_Registration_368_0(Etw):
    pattern = Struct(
        "Properties" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=369, version=0)
class Microsoft_Windows_User_Device_Registration_369_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=370, version=0)
class Microsoft_Windows_User_Device_Registration_370_0(Etw):
    pattern = Struct(
        "ExitCode" / Int32sl,
        "ServerErrorMessage" / WString,
        "TenantType" / WString,
        "JoinType" / WString,
        "DebugOutput" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=372, version=0)
class Microsoft_Windows_User_Device_Registration_372_0(Etw):
    pattern = Struct(
        "KeyId" / WString,
        "UPN" / WString,
        "RequestId" / WString,
        "Time" / WString,
        "ServerResponse" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=373, version=0)
class Microsoft_Windows_User_Device_Registration_373_0(Etw):
    pattern = Struct(
        "ExitCode" / Int32sl,
        "RequestId" / WString,
        "Time" / WString,
        "HttpStatus" / Int32ul,
        "ErrorCode" / WString,
        "ErrorSubCode" / WString,
        "ServerErrorMessage" / WString,
        "ServerResponse" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=374, version=0)
class Microsoft_Windows_User_Device_Registration_374_0(Etw):
    pattern = Struct(
        "RPID" / WString,
        "UPN" / WString,
        "KeyDisplayName" / WString,
        "UserDisplayName" / WString,
        "UserImageUrl" / WString,
        "KeyAlgorithm" / WString,
        "AuthToken" / WString,
        "RequestId" / WString,
        "Flags" / Int32ul
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=375, version=0)
class Microsoft_Windows_User_Device_Registration_375_0(Etw):
    pattern = Struct(
        "ExitCode" / Int32sl,
        "RPID" / WString,
        "UPN" / WString,
        "KeyDisplayName" / WString,
        "UserDisplayName" / WString,
        "UserImageUrl" / WString,
        "KeyAlgorithm" / WString,
        "AuthToken" / WString,
        "RequestId" / WString,
        "Flags" / Int32ul
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=376, version=0)
class Microsoft_Windows_User_Device_Registration_376_0(Etw):
    pattern = Struct(
        "UPN" / WString,
        "KeyDisplayName" / WString,
        "UserDisplayName" / WString,
        "UserImageUrl" / WString,
        "KeyAlgorithm" / WString,
        "AuthToken" / WString,
        "RequestId" / WString,
        "Flags" / Int32ul,
        "PinStatus" / Int32ul,
        "PinRetries" / Int32ul
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=377, version=0)
class Microsoft_Windows_User_Device_Registration_377_0(Etw):
    pattern = Struct(
        "ExitCode" / Int32sl,
        "UPN" / WString,
        "KeyDisplayName" / WString,
        "UserDisplayName" / WString,
        "UserImageUrl" / WString,
        "KeyAlgorithm" / WString,
        "AuthToken" / WString,
        "RequestId" / WString,
        "Flags" / Int32ul,
        "PinStatus" / Int32ul,
        "PinRetries" / Int32ul
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=378, version=0)
class Microsoft_Windows_User_Device_Registration_378_0(Etw):
    pattern = Struct(
        "NumOfKeyIds" / Int32ul,
        "KeyId" / WString,
        "UPN" / WString,
        "RequestId" / WString,
        "Time" / WString,
        "ServerResponse" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=379, version=0)
class Microsoft_Windows_User_Device_Registration_379_0(Etw):
    pattern = Struct(
        "ExitCode" / Int32sl,
        "RequestId" / WString,
        "Time" / WString,
        "HttpStatus" / Int32ul,
        "ErrorCode" / WString,
        "ErrorSubCode" / WString,
        "ServerErrorMessage" / WString,
        "ServerResponse" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=380, version=0)
class Microsoft_Windows_User_Device_Registration_380_0(Etw):
    pattern = Struct(
        "UPN" / WString,
        "KeyId" / WString,
        "AuthToken" / WString,
        "RequestId" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=381, version=0)
class Microsoft_Windows_User_Device_Registration_381_0(Etw):
    pattern = Struct(
        "ExitCode" / Int32sl,
        "UPN" / WString,
        "KeyId" / WString,
        "AuthToken" / WString,
        "RequestId" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=382, version=0)
class Microsoft_Windows_User_Device_Registration_382_0(Etw):
    pattern = Struct(
        "HttpStatus" / Int32ul,
        "ResponseBody" / WString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=383, version=0)
class Microsoft_Windows_User_Device_Registration_383_0(Etw):
    pattern = Struct(
        "hWnd" / Int64ul
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=384, version=0)
class Microsoft_Windows_User_Device_Registration_384_0(Etw):
    pattern = Struct(
        "ExitCode" / Int32sl,
        "hWnd" / Int64ul
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=385, version=0)
class Microsoft_Windows_User_Device_Registration_385_0(Etw):
    pattern = Struct(
        "KeyName" / WString,
        "KeyStatus" / Int32sl,
        "KeyStatusSymbolicName" / WString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=386, version=0)
class Microsoft_Windows_User_Device_Registration_386_0(Etw):
    pattern = Struct(
        "KeyName" / WString,
        "KeyStatus" / Int32sl,
        "KeyStatusSymbolicName" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=387, version=0)
class Microsoft_Windows_User_Device_Registration_387_0(Etw):
    pattern = Struct(
        "ExitCode" / Int32sl
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=388, version=0)
class Microsoft_Windows_User_Device_Registration_388_0(Etw):
    pattern = Struct(
        "APIName" / WString,
        "ExitCode" / Int32sl
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=390, version=0)
class Microsoft_Windows_User_Device_Registration_390_0(Etw):
    pattern = Struct(
        "IdType" / WString,
        "RACertificateId" / WString,
        "DeviceCeritifcateId" / WString,
        "ServerRequestId" / WString,
        "ServerTime" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=391, version=0)
class Microsoft_Windows_User_Device_Registration_391_0(Etw):
    pattern = Struct(
        "UserSid" / WString,
        "UserKeyName" / WString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=392, version=0)
class Microsoft_Windows_User_Device_Registration_392_0(Etw):
    pattern = Struct(
        "UserSid" / WString,
        "UserKeyName" / WString,
        "ContainerStatus" / Int32ul
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=394, version=0)
class Microsoft_Windows_User_Device_Registration_394_0(Etw):
    pattern = Struct(
        "ExitCode" / Int32sl
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=395, version=0)
class Microsoft_Windows_User_Device_Registration_395_0(Etw):
    pattern = Struct(
        "ExitCode" / Int32sl
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=396, version=0)
class Microsoft_Windows_User_Device_Registration_396_0(Etw):
    pattern = Struct(
        "PolicyValue" / Int32sl
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=500, version=0)
class Microsoft_Windows_User_Device_Registration_500_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=501, version=0)
class Microsoft_Windows_User_Device_Registration_501_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=502, version=0)
class Microsoft_Windows_User_Device_Registration_502_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=503, version=0)
class Microsoft_Windows_User_Device_Registration_503_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("23b8d46b-67dd-40a3-b636-d43e50552c6d"), event_id=504, version=0)
class Microsoft_Windows_User_Device_Registration_504_0(Etw):
    pattern = Struct(
        "Message" / WString
    )

