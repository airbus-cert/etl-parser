# -*- coding: utf-8 -*-
"""
Microsoft-Windows-ShareMedia-ControlPanel
GUID : 02012a8a-adf5-4fab-92cb-ccb7bb3e689a
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("02012a8a-adf5-4fab-92cb-ccb7bb3e689a"), event_id=1001, version=0)
class Microsoft_Windows_ShareMedia_ControlPanel_1001_0(Etw):
    pattern = Struct(
        "ItemCount" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("02012a8a-adf5-4fab-92cb-ccb7bb3e689a"), event_id=1002, version=0)
class Microsoft_Windows_ShareMedia_ControlPanel_1002_0(Etw):
    pattern = Struct(
        "ItemCount" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("02012a8a-adf5-4fab-92cb-ccb7bb3e689a"), event_id=1003, version=0)
class Microsoft_Windows_ShareMedia_ControlPanel_1003_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("02012a8a-adf5-4fab-92cb-ccb7bb3e689a"), event_id=1004, version=0)
class Microsoft_Windows_ShareMedia_ControlPanel_1004_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("02012a8a-adf5-4fab-92cb-ccb7bb3e689a"), event_id=1005, version=0)
class Microsoft_Windows_ShareMedia_ControlPanel_1005_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("02012a8a-adf5-4fab-92cb-ccb7bb3e689a"), event_id=1006, version=0)
class Microsoft_Windows_ShareMedia_ControlPanel_1006_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("02012a8a-adf5-4fab-92cb-ccb7bb3e689a"), event_id=1007, version=0)
class Microsoft_Windows_ShareMedia_ControlPanel_1007_0(Etw):
    pattern = Struct(
        "ID" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("02012a8a-adf5-4fab-92cb-ccb7bb3e689a"), event_id=1008, version=0)
class Microsoft_Windows_ShareMedia_ControlPanel_1008_0(Etw):
    pattern = Struct(
        "ID" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("02012a8a-adf5-4fab-92cb-ccb7bb3e689a"), event_id=1009, version=0)
class Microsoft_Windows_ShareMedia_ControlPanel_1009_0(Etw):
    pattern = Struct(
        "ID" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("02012a8a-adf5-4fab-92cb-ccb7bb3e689a"), event_id=1010, version=0)
class Microsoft_Windows_ShareMedia_ControlPanel_1010_0(Etw):
    pattern = Struct(
        "ID" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("02012a8a-adf5-4fab-92cb-ccb7bb3e689a"), event_id=1011, version=0)
class Microsoft_Windows_ShareMedia_ControlPanel_1011_0(Etw):
    pattern = Struct(
        "ID" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("02012a8a-adf5-4fab-92cb-ccb7bb3e689a"), event_id=1012, version=0)
class Microsoft_Windows_ShareMedia_ControlPanel_1012_0(Etw):
    pattern = Struct(
        "ID" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("02012a8a-adf5-4fab-92cb-ccb7bb3e689a"), event_id=1013, version=0)
class Microsoft_Windows_ShareMedia_ControlPanel_1013_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("02012a8a-adf5-4fab-92cb-ccb7bb3e689a"), event_id=1014, version=0)
class Microsoft_Windows_ShareMedia_ControlPanel_1014_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("02012a8a-adf5-4fab-92cb-ccb7bb3e689a"), event_id=1015, version=0)
class Microsoft_Windows_ShareMedia_ControlPanel_1015_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("02012a8a-adf5-4fab-92cb-ccb7bb3e689a"), event_id=1016, version=0)
class Microsoft_Windows_ShareMedia_ControlPanel_1016_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("02012a8a-adf5-4fab-92cb-ccb7bb3e689a"), event_id=1017, version=0)
class Microsoft_Windows_ShareMedia_ControlPanel_1017_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("02012a8a-adf5-4fab-92cb-ccb7bb3e689a"), event_id=1018, version=0)
class Microsoft_Windows_ShareMedia_ControlPanel_1018_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("02012a8a-adf5-4fab-92cb-ccb7bb3e689a"), event_id=1019, version=0)
class Microsoft_Windows_ShareMedia_ControlPanel_1019_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("02012a8a-adf5-4fab-92cb-ccb7bb3e689a"), event_id=1020, version=0)
class Microsoft_Windows_ShareMedia_ControlPanel_1020_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("02012a8a-adf5-4fab-92cb-ccb7bb3e689a"), event_id=1021, version=0)
class Microsoft_Windows_ShareMedia_ControlPanel_1021_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("02012a8a-adf5-4fab-92cb-ccb7bb3e689a"), event_id=1022, version=0)
class Microsoft_Windows_ShareMedia_ControlPanel_1022_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("02012a8a-adf5-4fab-92cb-ccb7bb3e689a"), event_id=1023, version=0)
class Microsoft_Windows_ShareMedia_ControlPanel_1023_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("02012a8a-adf5-4fab-92cb-ccb7bb3e689a"), event_id=1024, version=0)
class Microsoft_Windows_ShareMedia_ControlPanel_1024_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("02012a8a-adf5-4fab-92cb-ccb7bb3e689a"), event_id=1025, version=0)
class Microsoft_Windows_ShareMedia_ControlPanel_1025_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("02012a8a-adf5-4fab-92cb-ccb7bb3e689a"), event_id=1026, version=0)
class Microsoft_Windows_ShareMedia_ControlPanel_1026_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("02012a8a-adf5-4fab-92cb-ccb7bb3e689a"), event_id=1027, version=0)
class Microsoft_Windows_ShareMedia_ControlPanel_1027_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("02012a8a-adf5-4fab-92cb-ccb7bb3e689a"), event_id=1028, version=0)
class Microsoft_Windows_ShareMedia_ControlPanel_1028_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("02012a8a-adf5-4fab-92cb-ccb7bb3e689a"), event_id=1029, version=0)
class Microsoft_Windows_ShareMedia_ControlPanel_1029_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("02012a8a-adf5-4fab-92cb-ccb7bb3e689a"), event_id=1030, version=0)
class Microsoft_Windows_ShareMedia_ControlPanel_1030_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("02012a8a-adf5-4fab-92cb-ccb7bb3e689a"), event_id=1031, version=0)
class Microsoft_Windows_ShareMedia_ControlPanel_1031_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul,
        "EnableSharingErrorDetails" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("02012a8a-adf5-4fab-92cb-ccb7bb3e689a"), event_id=1032, version=0)
class Microsoft_Windows_ShareMedia_ControlPanel_1032_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul,
        "EnableSharingErrorDetails" / Int32ul,
        "ErrorCode" / Int32ul
    )

