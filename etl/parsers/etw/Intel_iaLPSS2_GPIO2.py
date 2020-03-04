# -*- coding: utf-8 -*-
"""
Intel-iaLPSS2-GPIO2
GUID : 63848cff-3ec7-4ddf-8072-5f95e8c8eb98
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("63848cff-3ec7-4ddf-8072-5f95e8c8eb98"), event_id=1001, version=0)
class Intel_iaLPSS2_GPIO2_1001_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("63848cff-3ec7-4ddf-8072-5f95e8c8eb98"), event_id=1002, version=0)
class Intel_iaLPSS2_GPIO2_1002_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("63848cff-3ec7-4ddf-8072-5f95e8c8eb98"), event_id=1003, version=0)
class Intel_iaLPSS2_GPIO2_1003_0(Etw):
    pattern = Struct(
        "Message" / CString
    )


@declare(guid=guid("63848cff-3ec7-4ddf-8072-5f95e8c8eb98"), event_id=1004, version=0)
class Intel_iaLPSS2_GPIO2_1004_0(Etw):
    pattern = Struct(
        "Message" / CString
    )


@declare(guid=guid("63848cff-3ec7-4ddf-8072-5f95e8c8eb98"), event_id=1005, version=0)
class Intel_iaLPSS2_GPIO2_1005_0(Etw):
    pattern = Struct(
        "Message" / CString,
        "Status" / Int32ul
    )


@declare(guid=guid("63848cff-3ec7-4ddf-8072-5f95e8c8eb98"), event_id=1013, version=0)
class Intel_iaLPSS2_GPIO2_1013_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("63848cff-3ec7-4ddf-8072-5f95e8c8eb98"), event_id=1014, version=0)
class Intel_iaLPSS2_GPIO2_1014_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("63848cff-3ec7-4ddf-8072-5f95e8c8eb98"), event_id=1017, version=0)
class Intel_iaLPSS2_GPIO2_1017_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("63848cff-3ec7-4ddf-8072-5f95e8c8eb98"), event_id=1018, version=0)
class Intel_iaLPSS2_GPIO2_1018_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("63848cff-3ec7-4ddf-8072-5f95e8c8eb98"), event_id=1023, version=0)
class Intel_iaLPSS2_GPIO2_1023_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("63848cff-3ec7-4ddf-8072-5f95e8c8eb98"), event_id=1024, version=0)
class Intel_iaLPSS2_GPIO2_1024_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("63848cff-3ec7-4ddf-8072-5f95e8c8eb98"), event_id=1025, version=0)
class Intel_iaLPSS2_GPIO2_1025_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("63848cff-3ec7-4ddf-8072-5f95e8c8eb98"), event_id=1026, version=0)
class Intel_iaLPSS2_GPIO2_1026_0(Etw):
    pattern = Struct(
        "Instance" / Int32ul,
        "Version" / Int32ul,
        "Revision" / Int32ul,
        "Mode" / Int32ul
    )


@declare(guid=guid("63848cff-3ec7-4ddf-8072-5f95e8c8eb98"), event_id=1027, version=0)
class Intel_iaLPSS2_GPIO2_1027_0(Etw):
    pattern = Struct(
        "Instance" / Int32ul,
        "Version" / Int32ul,
        "Revision" / Int32ul,
        "Mode" / Int32ul
    )


@declare(guid=guid("63848cff-3ec7-4ddf-8072-5f95e8c8eb98"), event_id=1031, version=0)
class Intel_iaLPSS2_GPIO2_1031_0(Etw):
    pattern = Struct(
        "Message" / CString
    )


@declare(guid=guid("63848cff-3ec7-4ddf-8072-5f95e8c8eb98"), event_id=1101, version=0)
class Intel_iaLPSS2_GPIO2_1101_0(Etw):
    pattern = Struct(
        "BankNo" / Int32ul
    )


@declare(guid=guid("63848cff-3ec7-4ddf-8072-5f95e8c8eb98"), event_id=1102, version=0)
class Intel_iaLPSS2_GPIO2_1102_0(Etw):
    pattern = Struct(
        "BankName" / CString,
        "PinNo" / Int32ul
    )


@declare(guid=guid("63848cff-3ec7-4ddf-8072-5f95e8c8eb98"), event_id=1103, version=0)
class Intel_iaLPSS2_GPIO2_1103_0(Etw):
    pattern = Struct(
        "BankName" / CString,
        "PinNo" / Int32ul,
        "PinOwnership" / Int32ul
    )


@declare(guid=guid("63848cff-3ec7-4ddf-8072-5f95e8c8eb98"), event_id=1104, version=0)
class Intel_iaLPSS2_GPIO2_1104_0(Etw):
    pattern = Struct(
        "BankName" / CString,
        "PinNo" / Int32ul,
        "PinMode" / Int32ul
    )


@declare(guid=guid("63848cff-3ec7-4ddf-8072-5f95e8c8eb98"), event_id=1110, version=0)
class Intel_iaLPSS2_GPIO2_1110_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("63848cff-3ec7-4ddf-8072-5f95e8c8eb98"), event_id=1111, version=0)
class Intel_iaLPSS2_GPIO2_1111_0(Etw):
    pattern = Struct(
        "MBAR" / Int32ul,
        "PA" / Int64ul,
        "LEN" / Int32ul,
        "VA" / Int64ul
    )


@declare(guid=guid("63848cff-3ec7-4ddf-8072-5f95e8c8eb98"), event_id=1112, version=0)
class Intel_iaLPSS2_GPIO2_1112_0(Etw):
    pattern = Struct(
        "MBAR" / Int32ul,
        "PA" / Int64ul,
        "LEN" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("63848cff-3ec7-4ddf-8072-5f95e8c8eb98"), event_id=1113, version=0)
class Intel_iaLPSS2_GPIO2_1113_0(Etw):
    pattern = Struct(
        "MBAR" / Int32ul,
        "PA" / Int64ul,
        "LEN" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("63848cff-3ec7-4ddf-8072-5f95e8c8eb98"), event_id=1114, version=0)
class Intel_iaLPSS2_GPIO2_1114_0(Etw):
    pattern = Struct(
        "Vector" / Int32ul
    )


@declare(guid=guid("63848cff-3ec7-4ddf-8072-5f95e8c8eb98"), event_id=1115, version=0)
class Intel_iaLPSS2_GPIO2_1115_0(Etw):
    pattern = Struct(
        "MBAR_current" / Int32ul,
        "MBAR_expected" / Int32ul,
        "INT_current" / Int32ul,
        "INT_expected" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("63848cff-3ec7-4ddf-8072-5f95e8c8eb98"), event_id=1121, version=0)
class Intel_iaLPSS2_GPIO2_1121_0(Etw):
    pattern = Struct(
        "BankName" / CString,
        "PinNo" / Int32ul,
        "IntMode" / Int32ul,
        "IntPolartity" / Int32ul
    )


@declare(guid=guid("63848cff-3ec7-4ddf-8072-5f95e8c8eb98"), event_id=1122, version=0)
class Intel_iaLPSS2_GPIO2_1122_0(Etw):
    pattern = Struct(
        "BankName" / CString,
        "PinNo" / Int32ul,
        "IntMode" / Int32ul,
        "IntPolartity" / Int32ul
    )


@declare(guid=guid("63848cff-3ec7-4ddf-8072-5f95e8c8eb98"), event_id=1123, version=0)
class Intel_iaLPSS2_GPIO2_1123_0(Etw):
    pattern = Struct(
        "BankName" / CString,
        "PinNo" / Int32ul,
        "PullMode" / Int32ul
    )


@declare(guid=guid("63848cff-3ec7-4ddf-8072-5f95e8c8eb98"), event_id=1124, version=0)
class Intel_iaLPSS2_GPIO2_1124_0(Etw):
    pattern = Struct(
        "BankName" / CString,
        "PinNo" / Int32ul,
        "PullMode" / Int32ul
    )


@declare(guid=guid("63848cff-3ec7-4ddf-8072-5f95e8c8eb98"), event_id=1125, version=0)
class Intel_iaLPSS2_GPIO2_1125_0(Etw):
    pattern = Struct(
        "BankName" / CString,
        "PinNo" / Int32ul
    )


@declare(guid=guid("63848cff-3ec7-4ddf-8072-5f95e8c8eb98"), event_id=1126, version=0)
class Intel_iaLPSS2_GPIO2_1126_0(Etw):
    pattern = Struct(
        "BankName" / CString,
        "PinNo" / Int32ul
    )


@declare(guid=guid("63848cff-3ec7-4ddf-8072-5f95e8c8eb98"), event_id=1127, version=0)
class Intel_iaLPSS2_GPIO2_1127_0(Etw):
    pattern = Struct(
        "BankName" / CString,
        "MaskSet" / Int32ul,
        "MaskRequested" / Int32ul,
        "MaskFailed" / Int32ul
    )


@declare(guid=guid("63848cff-3ec7-4ddf-8072-5f95e8c8eb98"), event_id=1128, version=0)
class Intel_iaLPSS2_GPIO2_1128_0(Etw):
    pattern = Struct(
        "BankName" / CString,
        "PinNo" / Int32ul
    )


@declare(guid=guid("63848cff-3ec7-4ddf-8072-5f95e8c8eb98"), event_id=1129, version=0)
class Intel_iaLPSS2_GPIO2_1129_0(Etw):
    pattern = Struct(
        "BankName" / CString,
        "Active" / Int32ul,
        "ActiveRaw" / Int32ul,
        "ActiveMask" / Int32ul
    )


@declare(guid=guid("63848cff-3ec7-4ddf-8072-5f95e8c8eb98"), event_id=1130, version=0)
class Intel_iaLPSS2_GPIO2_1130_0(Etw):
    pattern = Struct(
        "BankName" / CString,
        "Enabled" / Int32ul
    )


@declare(guid=guid("63848cff-3ec7-4ddf-8072-5f95e8c8eb98"), event_id=1131, version=0)
class Intel_iaLPSS2_GPIO2_1131_0(Etw):
    pattern = Struct(
        "BankName" / CString,
        "MaskSet" / Int32ul,
        "MaskRequested" / Int32ul,
        "MaskFailed" / Int32ul
    )


@declare(guid=guid("63848cff-3ec7-4ddf-8072-5f95e8c8eb98"), event_id=1132, version=0)
class Intel_iaLPSS2_GPIO2_1132_0(Etw):
    pattern = Struct(
        "BankName" / CString,
        "PinNo" / Int32ul,
        "PinIoMode" / Int32ul
    )


@declare(guid=guid("63848cff-3ec7-4ddf-8072-5f95e8c8eb98"), event_id=1133, version=0)
class Intel_iaLPSS2_GPIO2_1133_0(Etw):
    pattern = Struct(
        "BankName" / CString,
        "PinNo" / Int32ul
    )


@declare(guid=guid("63848cff-3ec7-4ddf-8072-5f95e8c8eb98"), event_id=1134, version=0)
class Intel_iaLPSS2_GPIO2_1134_0(Etw):
    pattern = Struct(
        "BankName" / CString,
        "PinNo" / Int32ul,
        "PinState" / Int32ul
    )


@declare(guid=guid("63848cff-3ec7-4ddf-8072-5f95e8c8eb98"), event_id=1135, version=0)
class Intel_iaLPSS2_GPIO2_1135_0(Etw):
    pattern = Struct(
        "BankName" / CString,
        "PinNo" / Int32ul,
        "PinState" / Int32ul
    )


@declare(guid=guid("63848cff-3ec7-4ddf-8072-5f95e8c8eb98"), event_id=1136, version=0)
class Intel_iaLPSS2_GPIO2_1136_0(Etw):
    pattern = Struct(
        "BankName" / CString,
        "PinNo" / Int32ul,
        "PinState" / Int32ul
    )


@declare(guid=guid("63848cff-3ec7-4ddf-8072-5f95e8c8eb98"), event_id=1137, version=0)
class Intel_iaLPSS2_GPIO2_1137_0(Etw):
    pattern = Struct(
        "BankName" / CString,
        "PinNo" / Int32ul,
        "PinIoMode" / Int32ul
    )


@declare(guid=guid("63848cff-3ec7-4ddf-8072-5f95e8c8eb98"), event_id=1138, version=0)
class Intel_iaLPSS2_GPIO2_1138_0(Etw):
    pattern = Struct(
        "BankName" / CString,
        "PinNo" / Int32ul,
        "PinIoMode" / Int32ul
    )


@declare(guid=guid("63848cff-3ec7-4ddf-8072-5f95e8c8eb98"), event_id=1139, version=0)
class Intel_iaLPSS2_GPIO2_1139_0(Etw):
    pattern = Struct(
        "BankName" / CString,
        "PinNo" / Int32ul,
        "PinIoModeCurrent" / Int32ul,
        "PinIoModeRequested" / Int32ul
    )


@declare(guid=guid("63848cff-3ec7-4ddf-8072-5f95e8c8eb98"), event_id=1140, version=0)
class Intel_iaLPSS2_GPIO2_1140_0(Etw):
    pattern = Struct(
        "BankName" / CString,
        "PinNo" / Int32ul
    )


@declare(guid=guid("63848cff-3ec7-4ddf-8072-5f95e8c8eb98"), event_id=1141, version=0)
class Intel_iaLPSS2_GPIO2_1141_0(Etw):
    pattern = Struct(
        "BankName" / CString,
        "PinNo" / Int32ul
    )


@declare(guid=guid("63848cff-3ec7-4ddf-8072-5f95e8c8eb98"), event_id=1142, version=0)
class Intel_iaLPSS2_GPIO2_1142_0(Etw):
    pattern = Struct(
        "BankName" / CString,
        "PinNo" / Int32ul
    )


@declare(guid=guid("63848cff-3ec7-4ddf-8072-5f95e8c8eb98"), event_id=1143, version=0)
class Intel_iaLPSS2_GPIO2_1143_0(Etw):
    pattern = Struct(
        "BankName" / CString,
        "PinNo" / Int32ul
    )


@declare(guid=guid("63848cff-3ec7-4ddf-8072-5f95e8c8eb98"), event_id=1144, version=0)
class Intel_iaLPSS2_GPIO2_1144_0(Etw):
    pattern = Struct(
        "BankName" / CString,
        "PinNo" / Int32ul,
        "PinIoMode" / Int32ul
    )


@declare(guid=guid("63848cff-3ec7-4ddf-8072-5f95e8c8eb98"), event_id=1150, version=0)
class Intel_iaLPSS2_GPIO2_1150_0(Etw):
    pattern = Struct(
        "BankName" / CString,
        "PinNo" / Int32ul
    )


@declare(guid=guid("63848cff-3ec7-4ddf-8072-5f95e8c8eb98"), event_id=1151, version=0)
class Intel_iaLPSS2_GPIO2_1151_0(Etw):
    pattern = Struct(
        "BankName" / CString
    )


@declare(guid=guid("63848cff-3ec7-4ddf-8072-5f95e8c8eb98"), event_id=1152, version=0)
class Intel_iaLPSS2_GPIO2_1152_0(Etw):
    pattern = Struct(
        "BankName" / CString,
        "PinNo" / Int32ul
    )


@declare(guid=guid("63848cff-3ec7-4ddf-8072-5f95e8c8eb98"), event_id=1153, version=0)
class Intel_iaLPSS2_GPIO2_1153_0(Etw):
    pattern = Struct(
        "BankName" / CString
    )


@declare(guid=guid("63848cff-3ec7-4ddf-8072-5f95e8c8eb98"), event_id=1201, version=0)
class Intel_iaLPSS2_GPIO2_1201_0(Etw):
    pattern = Struct(
        "BankName" / CString,
        "PinNo" / Int32ul
    )


@declare(guid=guid("63848cff-3ec7-4ddf-8072-5f95e8c8eb98"), event_id=1202, version=0)
class Intel_iaLPSS2_GPIO2_1202_0(Etw):
    pattern = Struct(
        "BankName" / CString,
        "PinNo" / Int32ul
    )


@declare(guid=guid("63848cff-3ec7-4ddf-8072-5f95e8c8eb98"), event_id=1203, version=0)
class Intel_iaLPSS2_GPIO2_1203_0(Etw):
    pattern = Struct(
        "BankName" / CString,
        "PinNo" / Int32ul
    )


@declare(guid=guid("63848cff-3ec7-4ddf-8072-5f95e8c8eb98"), event_id=1204, version=0)
class Intel_iaLPSS2_GPIO2_1204_0(Etw):
    pattern = Struct(
        "BankName" / CString,
        "PinNo" / Int32ul
    )

