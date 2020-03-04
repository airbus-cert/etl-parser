# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Directory-Services-SAM
GUID : 0d4fdc09-8c27-494a-bda0-505e4fd8adae
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=12288, version=0)
class Microsoft_Windows_Directory_Services_SAM_12288_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "ErrorCode" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=12289, version=0)
class Microsoft_Windows_Directory_Services_SAM_12289_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "ErrorCode" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=12291, version=0)
class Microsoft_Windows_Directory_Services_SAM_12291_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "LogStatus" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=12293, version=0)
class Microsoft_Windows_Directory_Services_SAM_12293_0(Etw):
    pattern = Struct(
        "AccountDistinguishedName" / WString
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=12294, version=0)
class Microsoft_Windows_Directory_Services_SAM_12294_0(Etw):
    pattern = Struct(
        "UserName" / WString,
        "__binLength" / Int32ul,
        "ErrorCode" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=12295, version=0)
class Microsoft_Windows_Directory_Services_SAM_12295_0(Etw):
    pattern = Struct(
        "FilePath" / WString,
        "__binLength" / Int32ul,
        "WinError" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=12296, version=0)
class Microsoft_Windows_Directory_Services_SAM_12296_0(Etw):
    pattern = Struct(
        "DirectoryPath" / WString,
        "__binLength" / Int32ul,
        "WinError" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=12297, version=0)
class Microsoft_Windows_Directory_Services_SAM_12297_0(Etw):
    pattern = Struct(
        "ComputerName" / WString
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=12298, version=0)
class Microsoft_Windows_Directory_Services_SAM_12298_0(Etw):
    pattern = Struct(
        "ComputerName" / WString
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=12299, version=0)
class Microsoft_Windows_Directory_Services_SAM_12299_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "ErrorCode" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=12302, version=0)
class Microsoft_Windows_Directory_Services_SAM_12302_0(Etw):
    pattern = Struct(
        "SecurityPackage" / WString,
        "UserName" / WString,
        "__binLength" / Int32ul,
        "ErrorCode" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=12303, version=0)
class Microsoft_Windows_Directory_Services_SAM_12303_0(Etw):
    pattern = Struct(
        "AccountDistinguishedName" / WString
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=12304, version=0)
class Microsoft_Windows_Directory_Services_SAM_12304_0(Etw):
    pattern = Struct(
        "AccountDistinguishedName" / WString,
        "SystemAssignedAccountName" / WString
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=12305, version=0)
class Microsoft_Windows_Directory_Services_SAM_12305_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "ErrorCode" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=16384, version=0)
class Microsoft_Windows_Directory_Services_SAM_16384_0(Etw):
    pattern = Struct(
        "AccountName" / WString,
        "__binLength" / Int32ul,
        "ErrorCode" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=16385, version=0)
class Microsoft_Windows_Directory_Services_SAM_16385_0(Etw):
    pattern = Struct(
        "UserName" / WString,
        "__binLength" / Int32ul,
        "ErrorCode" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=16386, version=0)
class Microsoft_Windows_Directory_Services_SAM_16386_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "ErrorCode" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=16387, version=0)
class Microsoft_Windows_Directory_Services_SAM_16387_0(Etw):
    pattern = Struct(
        "GroupName" / WString,
        "__binLength" / Int32ul,
        "ErrorCode" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=16388, version=0)
class Microsoft_Windows_Directory_Services_SAM_16388_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "ErrorCode" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=16389, version=0)
class Microsoft_Windows_Directory_Services_SAM_16389_0(Etw):
    pattern = Struct(
        "GroupName" / WString,
        "__binLength" / Int32ul,
        "ErrorCode" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=16390, version=0)
class Microsoft_Windows_Directory_Services_SAM_16390_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "ErrorCode" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=16391, version=0)
class Microsoft_Windows_Directory_Services_SAM_16391_0(Etw):
    pattern = Struct(
        "AccountDistinguishedName" / WString,
        "GroupName" / WString,
        "__binLength" / Int32ul,
        "ErrorCode" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=16392, version=0)
class Microsoft_Windows_Directory_Services_SAM_16392_0(Etw):
    pattern = Struct(
        "AccountSID" / WString,
        "AccountDistinguishedName" / WString,
        "__binLength" / Int32ul,
        "ErrorCode" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=16393, version=0)
class Microsoft_Windows_Directory_Services_SAM_16393_0(Etw):
    pattern = Struct(
        "AccountDistinguishedName" / WString,
        "GroupName" / WString,
        "__binLength" / Int32ul,
        "ErrorCode" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=16394, version=0)
class Microsoft_Windows_Directory_Services_SAM_16394_0(Etw):
    pattern = Struct(
        "AccountRID" / Int32ul,
        "GroupName" / WString,
        "__binLength" / Int32ul,
        "ErrorCode" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=16395, version=0)
class Microsoft_Windows_Directory_Services_SAM_16395_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "ErrorCode" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=16398, version=0)
class Microsoft_Windows_Directory_Services_SAM_16398_0(Etw):
    pattern = Struct(
        "SecurityPackage" / WString,
        "__binLength" / Int32ul,
        "ErrorCode" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=16399, version=0)
class Microsoft_Windows_Directory_Services_SAM_16399_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "ErrorCode" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=16400, version=0)
class Microsoft_Windows_Directory_Services_SAM_16400_0(Etw):
    pattern = Struct(
        "UserName" / WString,
        "__binLength" / Int32ul,
        "ErrorCode" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=16401, version=0)
class Microsoft_Windows_Directory_Services_SAM_16401_0(Etw):
    pattern = Struct(
        "AccountName" / WString,
        "GroupName" / WString,
        "ErrorMessage" / WString,
        "__binLength" / Int32ul,
        "ErrorCode" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=16402, version=0)
class Microsoft_Windows_Directory_Services_SAM_16402_0(Etw):
    pattern = Struct(
        "AccountName" / WString,
        "GroupName" / WString,
        "ErrorMessage" / WString,
        "__binLength" / Int32ul,
        "ErrorCode" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=16403, version=0)
class Microsoft_Windows_Directory_Services_SAM_16403_0(Etw):
    pattern = Struct(
        "AccountName" / WString,
        "ErrorMessage" / WString,
        "__binLength" / Int32ul,
        "ErrorCode" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=16405, version=0)
class Microsoft_Windows_Directory_Services_SAM_16405_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "ErrorCode" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=16406, version=0)
class Microsoft_Windows_Directory_Services_SAM_16406_0(Etw):
    pattern = Struct(
        "UserName" / WString,
        "__binLength" / Int32ul,
        "ErrorCode" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=16407, version=0)
class Microsoft_Windows_Directory_Services_SAM_16407_0(Etw):
    pattern = Struct(
        "GroupName" / WString,
        "__binLength" / Int32ul,
        "ErrorCode" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=16409, version=0)
class Microsoft_Windows_Directory_Services_SAM_16409_0(Etw):
    pattern = Struct(
        "AccountName" / WString,
        "__binLength" / Int32ul,
        "ErrorCode" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=16410, version=0)
class Microsoft_Windows_Directory_Services_SAM_16410_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "ErrorCode" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=16411, version=0)
class Microsoft_Windows_Directory_Services_SAM_16411_0(Etw):
    pattern = Struct(
        "AccountName" / WString,
        "__binLength" / Int32ul,
        "ErrorCode" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=16412, version=0)
class Microsoft_Windows_Directory_Services_SAM_16412_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "ErrorCode" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=16413, version=0)
class Microsoft_Windows_Directory_Services_SAM_16413_0(Etw):
    pattern = Struct(
        "AccountName" / WString,
        "GroupName" / WString,
        "ErrorString" / WString,
        "__binLength" / Int32ul,
        "BinaryData" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=16642, version=0)
class Microsoft_Windows_Directory_Services_SAM_16642_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "ErrorCode" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=16643, version=0)
class Microsoft_Windows_Directory_Services_SAM_16643_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "ErrorCode" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=16644, version=0)
class Microsoft_Windows_Directory_Services_SAM_16644_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "ErrorCode" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=16645, version=0)
class Microsoft_Windows_Directory_Services_SAM_16645_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "ErrorCode" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=16646, version=0)
class Microsoft_Windows_Directory_Services_SAM_16646_0(Etw):
    pattern = Struct(
        "ComputedRIDValue" / Int32ul,
        "__binLength" / Int32ul,
        "ErrorCode" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=16648, version=0)
class Microsoft_Windows_Directory_Services_SAM_16648_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "ErrorCode" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=16649, version=0)
class Microsoft_Windows_Directory_Services_SAM_16649_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "ErrorCode" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=16651, version=0)
class Microsoft_Windows_Directory_Services_SAM_16651_0(Etw):
    pattern = Struct(
        "ErrorMessage" / WString
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=16653, version=0)
class Microsoft_Windows_Directory_Services_SAM_16653_0(Etw):
    pattern = Struct(
        "Maximum" / Int32ul
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=16655, version=0)
class Microsoft_Windows_Directory_Services_SAM_16655_0(Etw):
    pattern = Struct(
        "NewValue" / Int32ul
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=16656, version=0)
class Microsoft_Windows_Directory_Services_SAM_16656_0(Etw):
    pattern = Struct(
        "CeilingTriggerRid" / Int32ul
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=16657, version=0)
class Microsoft_Windows_Directory_Services_SAM_16657_0(Etw):
    pattern = Struct(
        "CeilingTriggerRid" / Int32ul
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=16658, version=0)
class Microsoft_Windows_Directory_Services_SAM_16658_0(Etw):
    pattern = Struct(
        "RemainingRids" / Int32ul
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=16935, version=0)
class Microsoft_Windows_Directory_Services_SAM_16935_0(Etw):
    pattern = Struct(
        "ComputerName" / WString,
        "__binLength" / Int32ul,
        "ErrorCode" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=16936, version=0)
class Microsoft_Windows_Directory_Services_SAM_16936_0(Etw):
    pattern = Struct(
        "ComputerName" / WString,
        "__binLength" / Int32ul,
        "ErrorCode" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=16937, version=0)
class Microsoft_Windows_Directory_Services_SAM_16937_0(Etw):
    pattern = Struct(
        "ComputerName" / WString,
        "__binLength" / Int32ul,
        "ErrorCode" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=16944, version=0)
class Microsoft_Windows_Directory_Services_SAM_16944_0(Etw):
    pattern = Struct(
        "OID" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=16945, version=0)
class Microsoft_Windows_Directory_Services_SAM_16945_0(Etw):
    pattern = Struct(
        "OID" / WString,
        "OIDObjectDN" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=16946, version=0)
class Microsoft_Windows_Directory_Services_SAM_16946_0(Etw):
    pattern = Struct(
        "OID" / WString
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=16947, version=0)
class Microsoft_Windows_Directory_Services_SAM_16947_0(Etw):
    pattern = Struct(
        "OID" / WString,
        "OIDObjectDN" / WString,
        "GroupDN" / WString,
        "GroupGUID" / WString,
        "GroupSID" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=16948, version=0)
class Microsoft_Windows_Directory_Services_SAM_16948_0(Etw):
    pattern = Struct(
        "GroupDN" / WString,
        "GroupGUID" / WString,
        "GroupSID" / WString,
        "Operation" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=16949, version=0)
class Microsoft_Windows_Directory_Services_SAM_16949_0(Etw):
    pattern = Struct(
        "OIDName" / WString,
        "GroupName" / WString,
        "GroupGUID" / WString,
        "GroupSID" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=16950, version=0)
class Microsoft_Windows_Directory_Services_SAM_16950_0(Etw):
    pattern = Struct(
        "User" / WString,
        "DroppedClaims" / WString
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=16951, version=0)
class Microsoft_Windows_Directory_Services_SAM_16951_0(Etw):
    pattern = Struct(
        "User" / WString,
        "Errorcode" / Int32ul
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=16952, version=0)
class Microsoft_Windows_Directory_Services_SAM_16952_0(Etw):
    pattern = Struct(
        "User" / WString,
        "Errorcode" / Int32ul
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=16953, version=0)
class Microsoft_Windows_Directory_Services_SAM_16953_0(Etw):
    pattern = Struct(
        "NotificationPackage" / WString,
        "Registrykey" / WString,
        "Registryvalue" / WString,
        "Errorcode" / Int32ul
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=16962, version=0)
class Microsoft_Windows_Directory_Services_SAM_16962_0(Etw):
    pattern = Struct(
        "DefaultSDString" / WString
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=16963, version=0)
class Microsoft_Windows_Directory_Services_SAM_16963_0(Etw):
    pattern = Struct(
        "RegistrySDString" / WString
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=16964, version=0)
class Microsoft_Windows_Directory_Services_SAM_16964_0(Etw):
    pattern = Struct(
        "MalformedSDString" / WString,
        "DefaultSDString" / WString
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=16965, version=0)
class Microsoft_Windows_Directory_Services_SAM_16965_0(Etw):
    pattern = Struct(
        "ClientSID" / WString,
        "ClientNetworkAddress" / WString
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=16968, version=0)
class Microsoft_Windows_Directory_Services_SAM_16968_0(Etw):
    pattern = Struct(
        "ClientSID" / WString,
        "ClientNetworkAddress" / WString
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=16969, version=0)
class Microsoft_Windows_Directory_Services_SAM_16969_0(Etw):
    pattern = Struct(
        "Throttlewindow" / Int32ul,
        "SuppressedMessageCount" / Int32ul
    )


@declare(guid=guid("0d4fdc09-8c27-494a-bda0-505e4fd8adae"), event_id=16976, version=0)
class Microsoft_Windows_Directory_Services_SAM_16976_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )

