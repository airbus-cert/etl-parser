# -*- coding: utf-8 -*-
"""
Microsoft-Windows-OneX
GUID : ab0d8ef9-866d-4d39-b83f-453f3b8f6325
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=1, version=0)
class Microsoft_Windows_OneX_1_0(Etw):
    pattern = Struct(
        "PortId" / Int32ul
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=2, version=0)
class Microsoft_Windows_OneX_2_0(Etw):
    pattern = Struct(
        "PortId" / Int32ul
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=3, version=0)
class Microsoft_Windows_OneX_3_0(Etw):
    pattern = Struct(
        "PortId" / Int32ul
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=4, version=0)
class Microsoft_Windows_OneX_4_0(Etw):
    pattern = Struct(
        "PortId" / Int32ul,
        "WinError" / Int32ul,
        "ReasonCode" / Int32ul,
        "EAPMethodType" / Int8ul,
        "RootCauseString" / WString
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=5, version=0)
class Microsoft_Windows_OneX_5_0(Etw):
    pattern = Struct(
        "PortId" / Int32ul
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=6, version=0)
class Microsoft_Windows_OneX_6_0(Etw):
    pattern = Struct(
        "PortId" / Int32ul,
        "WinError" / Int32ul,
        "ReasonCode" / Int32ul
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=7, version=0)
class Microsoft_Windows_OneX_7_0(Etw):
    pattern = Struct(
        "PortId" / Int32ul,
        "UserDataSize" / Int32ul
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=8, version=0)
class Microsoft_Windows_OneX_8_0(Etw):
    pattern = Struct(
        "PortId" / Int32ul,
        "UserDataSize" / Int32ul
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=9, version=0)
class Microsoft_Windows_OneX_9_0(Etw):
    pattern = Struct(
        "PortId" / Int32ul
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=10, version=0)
class Microsoft_Windows_OneX_10_0(Etw):
    pattern = Struct(
        "PortId" / Int32ul,
        "Response" / Int32ul
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=11, version=0)
class Microsoft_Windows_OneX_11_0(Etw):
    pattern = Struct(
        "PortId" / Int32ul
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=12, version=0)
class Microsoft_Windows_OneX_12_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=13, version=0)
class Microsoft_Windows_OneX_13_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=14, version=0)
class Microsoft_Windows_OneX_14_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=15, version=0)
class Microsoft_Windows_OneX_15_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=16, version=0)
class Microsoft_Windows_OneX_16_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=17, version=0)
class Microsoft_Windows_OneX_17_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=18, version=0)
class Microsoft_Windows_OneX_18_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=19, version=0)
class Microsoft_Windows_OneX_19_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=20, version=0)
class Microsoft_Windows_OneX_20_0(Etw):
    pattern = Struct(
        "PortId" / Int32ul,
        "UIRequestCode" / Int32ul
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=21, version=0)
class Microsoft_Windows_OneX_21_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=22, version=0)
class Microsoft_Windows_OneX_22_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=23, version=0)
class Microsoft_Windows_OneX_23_0(Etw):
    pattern = Struct(
        "PortId" / Int32ul
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=24, version=0)
class Microsoft_Windows_OneX_24_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=25, version=0)
class Microsoft_Windows_OneX_25_0(Etw):
    pattern = Struct(
        "WarningCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=26, version=0)
class Microsoft_Windows_OneX_26_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=27, version=0)
class Microsoft_Windows_OneX_27_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=28, version=0)
class Microsoft_Windows_OneX_28_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=29, version=0)
class Microsoft_Windows_OneX_29_0(Etw):
    pattern = Struct(
        "EAPMethodType" / Int8ul
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=30, version=0)
class Microsoft_Windows_OneX_30_0(Etw):
    pattern = Struct(
        "EAPMethodType" / Int8ul
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=31, version=0)
class Microsoft_Windows_OneX_31_0(Etw):
    pattern = Struct(
        "ProfilesCount" / Int32ul
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=32, version=0)
class Microsoft_Windows_OneX_32_0(Etw):
    pattern = Struct(
        "EAPMethodType" / Int8ul,
        "AuthMode" / WString
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=33, version=0)
class Microsoft_Windows_OneX_33_0(Etw):
    pattern = Struct(
        "EAPMethodType" / Int8ul,
        "MediaType" / Int32ul
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=34, version=0)
class Microsoft_Windows_OneX_34_0(Etw):
    pattern = Struct(
        "PortId" / Int32ul,
        "UIRequestCode" / Int32ul
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=35, version=0)
class Microsoft_Windows_OneX_35_0(Etw):
    pattern = Struct(
        "ChangeType" / Int32ul
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=36, version=0)
class Microsoft_Windows_OneX_36_0(Etw):
    pattern = Struct(
        "PortId" / Int32ul,
        "FriendlyName" / WString
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=37, version=0)
class Microsoft_Windows_OneX_37_0(Etw):
    pattern = Struct(
        "PortId" / Int32ul
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=38, version=0)
class Microsoft_Windows_OneX_38_0(Etw):
    pattern = Struct(
        "PortId" / Int32ul,
        "UIRequestCode" / Int32ul
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=39, version=0)
class Microsoft_Windows_OneX_39_0(Etw):
    pattern = Struct(
        "PortId" / Int32ul
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=40, version=0)
class Microsoft_Windows_OneX_40_0(Etw):
    pattern = Struct(
        "PortId" / Int32ul,
        "PacketLength" / Int16ul,
        "PacketType" / Int32ul,
        "Identifier" / Int8ul,
        "EapMethodType" / Int32ul
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=41, version=0)
class Microsoft_Windows_OneX_41_0(Etw):
    pattern = Struct(
        "PortId" / Int32ul
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=42, version=0)
class Microsoft_Windows_OneX_42_0(Etw):
    pattern = Struct(
        "PortId" / Int32ul
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=43, version=0)
class Microsoft_Windows_OneX_43_0(Etw):
    pattern = Struct(
        "PortId" / Int32ul,
        "Reason" / Int32ul
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=44, version=0)
class Microsoft_Windows_OneX_44_0(Etw):
    pattern = Struct(
        "PortId" / Int32ul
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=45, version=0)
class Microsoft_Windows_OneX_45_0(Etw):
    pattern = Struct(
        "PortId" / Int32ul
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=46, version=0)
class Microsoft_Windows_OneX_46_0(Etw):
    pattern = Struct(
        "PortId" / Int32ul,
        "TimeTaken" / Int32ul
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=47, version=0)
class Microsoft_Windows_OneX_47_0(Etw):
    pattern = Struct(
        "PortId" / Int32ul,
        "AuthIdentity" / WString,
        "SessionId" / Int32ul,
        "Username" / WString,
        "Domain" / WString
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=48, version=0)
class Microsoft_Windows_OneX_48_0(Etw):
    pattern = Struct(
        "PortId" / Int32ul
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=49, version=0)
class Microsoft_Windows_OneX_49_0(Etw):
    pattern = Struct(
        "PortId" / Int32ul,
        "Reason" / Int32ul
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=50, version=0)
class Microsoft_Windows_OneX_50_0(Etw):
    pattern = Struct(
        "PortId" / Int32ul
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=51, version=0)
class Microsoft_Windows_OneX_51_0(Etw):
    pattern = Struct(
        "PortId" / Int32ul
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=52, version=0)
class Microsoft_Windows_OneX_52_0(Etw):
    pattern = Struct(
        "PortId" / Int32ul
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=53, version=0)
class Microsoft_Windows_OneX_53_0(Etw):
    pattern = Struct(
        "PortId" / Int32ul
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=54, version=0)
class Microsoft_Windows_OneX_54_0(Etw):
    pattern = Struct(
        "PortId" / Int32ul
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=55, version=0)
class Microsoft_Windows_OneX_55_0(Etw):
    pattern = Struct(
        "PortId" / Int32ul,
        "SessionId" / Int32ul,
        "UIRequestSessionId" / Int32ul
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=56, version=0)
class Microsoft_Windows_OneX_56_0(Etw):
    pattern = Struct(
        "PortId" / Int32ul,
        "Size" / Int32ul,
        "SessionId" / Int32ul
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=57, version=0)
class Microsoft_Windows_OneX_57_0(Etw):
    pattern = Struct(
        "PortId" / Int32ul,
        "Reason" / Int32ul,
        "SessionId" / Int32ul
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=58, version=0)
class Microsoft_Windows_OneX_58_0(Etw):
    pattern = Struct(
        "PortId" / Int32ul
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=59, version=0)
class Microsoft_Windows_OneX_59_0(Etw):
    pattern = Struct(
        "PortId" / Int32ul,
        "WinError" / Int32ul,
        "ReasonCode" / Int32ul
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=60, version=0)
class Microsoft_Windows_OneX_60_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=61, version=0)
class Microsoft_Windows_OneX_61_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=62, version=0)
class Microsoft_Windows_OneX_62_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=63, version=0)
class Microsoft_Windows_OneX_63_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=64, version=0)
class Microsoft_Windows_OneX_64_0(Etw):
    pattern = Struct(
        "PortId" / Int32ul,
        "PacketLength" / Int16ul,
        "PacketType" / Int32ul,
        "Identifier" / Int8ul,
        "EapMethodType" / Int32ul
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=65, version=0)
class Microsoft_Windows_OneX_65_0(Etw):
    pattern = Struct(
        "PortId" / Int32ul,
        "Identity" / CString
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=66, version=0)
class Microsoft_Windows_OneX_66_0(Etw):
    pattern = Struct(
        "PortId" / Int32ul,
        "ExplicitCredentials" / Int8ul
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=68, version=0)
class Microsoft_Windows_OneX_68_0(Etw):
    pattern = Struct(
        "PortId" / Int32ul,
        "ExplicitCredentials" / Int8ul
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=70, version=0)
class Microsoft_Windows_OneX_70_0(Etw):
    pattern = Struct(
        "PortId" / Int32ul
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=60001, version=0)
class Microsoft_Windows_OneX_60001_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=60002, version=0)
class Microsoft_Windows_OneX_60002_0(Etw):
    pattern = Struct(
        "WarningCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=60003, version=0)
class Microsoft_Windows_OneX_60003_0(Etw):
    pattern = Struct(
        "NextState" / Int8ul,
        "Context" / Int32ul
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=60004, version=0)
class Microsoft_Windows_OneX_60004_0(Etw):
    pattern = Struct(
        "Context" / Int32ul,
        "UpdateReasonCode" / Int32ul
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=60101, version=0)
class Microsoft_Windows_OneX_60101_0(Etw):
    pattern = Struct(
        "SourceAddress" / Int32ul,
        "SourcePort" / Int32ul,
        "DestinationAddress" / Int32ul,
        "DestinationPort" / Int32ul,
        "Protocol" / Int32ul,
        "ReferenceContext" / Int32ul
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=60102, version=0)
class Microsoft_Windows_OneX_60102_0(Etw):
    pattern = Struct(
        "SourcePort" / Int32ul,
        "DestinationPort" / Int32ul,
        "Protocol" / Int32ul,
        "ReferenceContext" / Int32ul
    )


@declare(guid=guid("ab0d8ef9-866d-4d39-b83f-453f3b8f6325"), event_id=60103, version=0)
class Microsoft_Windows_OneX_60103_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "IfLuid" / Int64ul,
        "ReferenceContext" / Int32ul
    )

