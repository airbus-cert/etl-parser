# -*- coding: utf-8 -*-
"""
Microsoft-Windows-UserDataAccess-PimIndexMaintenance
GUID : 99c66ba7-5a97-40d5-aa01-8a07fb3db292
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("99c66ba7-5a97-40d5-aa01-8a07fb3db292"), event_id=1, version=0)
class Microsoft_Windows_UserDataAccess_PimIndexMaintenance_1_0(Etw):
    pattern = Struct(
        "P1_HResult" / Int32sl,
        "P2_String" / CString,
        "P3_UInt32" / Int32ul
    )


@declare(guid=guid("99c66ba7-5a97-40d5-aa01-8a07fb3db292"), event_id=2, version=0)
class Microsoft_Windows_UserDataAccess_PimIndexMaintenance_2_0(Etw):
    pattern = Struct(
        "P1_HResult" / Int32sl,
        "P2_String" / CString,
        "P3_UInt32" / Int32ul
    )


@declare(guid=guid("99c66ba7-5a97-40d5-aa01-8a07fb3db292"), event_id=3, version=0)
class Microsoft_Windows_UserDataAccess_PimIndexMaintenance_3_0(Etw):
    pattern = Struct(
        "Message" / Int64ul
    )


@declare(guid=guid("99c66ba7-5a97-40d5-aa01-8a07fb3db292"), event_id=1000, version=0)
class Microsoft_Windows_UserDataAccess_PimIndexMaintenance_1000_0(Etw):
    pattern = Struct(
        "Prop_FUNC_AnsiString" / CString,
        "Prop_LINE_UInt32" / Int32ul,
        "Prop_Hr_Int32" / Int32sl
    )


@declare(guid=guid("99c66ba7-5a97-40d5-aa01-8a07fb3db292"), event_id=1009, version=0)
class Microsoft_Windows_UserDataAccess_PimIndexMaintenance_1009_0(Etw):
    pattern = Struct(
        "PROP_UInt32_1" / Int32ul,
        "PROP_UInt32_2" / Int32ul
    )


@declare(guid=guid("99c66ba7-5a97-40d5-aa01-8a07fb3db292"), event_id=1010, version=0)
class Microsoft_Windows_UserDataAccess_PimIndexMaintenance_1010_0(Etw):
    pattern = Struct(
        "Prop_Hr_UInt32" / Int32sl
    )


@declare(guid=guid("99c66ba7-5a97-40d5-aa01-8a07fb3db292"), event_id=1012, version=0)
class Microsoft_Windows_UserDataAccess_PimIndexMaintenance_1012_0(Etw):
    pattern = Struct(
        "PROP_UInt32" / Int32ul,
        "Prop_Hr_UInt32" / Int32sl
    )


@declare(guid=guid("99c66ba7-5a97-40d5-aa01-8a07fb3db292"), event_id=1013, version=0)
class Microsoft_Windows_UserDataAccess_PimIndexMaintenance_1013_0(Etw):
    pattern = Struct(
        "PROP_UInt32" / Int32ul,
        "Prop_Hr_UInt32" / Int32sl
    )


@declare(guid=guid("99c66ba7-5a97-40d5-aa01-8a07fb3db292"), event_id=1014, version=0)
class Microsoft_Windows_UserDataAccess_PimIndexMaintenance_1014_0(Etw):
    pattern = Struct(
        "Prop_Hr_UInt32" / Int32sl
    )


@declare(guid=guid("99c66ba7-5a97-40d5-aa01-8a07fb3db292"), event_id=1015, version=0)
class Microsoft_Windows_UserDataAccess_PimIndexMaintenance_1015_0(Etw):
    pattern = Struct(
        "PROP_FILE_uint" / Int32ul
    )


@declare(guid=guid("99c66ba7-5a97-40d5-aa01-8a07fb3db292"), event_id=1017, version=0)
class Microsoft_Windows_UserDataAccess_PimIndexMaintenance_1017_0(Etw):
    pattern = Struct(
        "PROP_UInt32_1" / Int32ul,
        "PROP_UInt32_2" / Int32ul
    )


@declare(guid=guid("99c66ba7-5a97-40d5-aa01-8a07fb3db292"), event_id=1018, version=0)
class Microsoft_Windows_UserDataAccess_PimIndexMaintenance_1018_0(Etw):
    pattern = Struct(
        "PROP_FILE_uint" / Int32ul
    )


@declare(guid=guid("99c66ba7-5a97-40d5-aa01-8a07fb3db292"), event_id=1023, version=0)
class Microsoft_Windows_UserDataAccess_PimIndexMaintenance_1023_0(Etw):
    pattern = Struct(
        "PROP_UInt32_1" / Int32ul,
        "PROP_UInt32_2" / Int32ul,
        "PROP_UInt32_3" / Int32ul,
        "PROP_UInt32_4" / Int32ul,
        "PROP_UInt32_5" / Int32ul
    )


@declare(guid=guid("99c66ba7-5a97-40d5-aa01-8a07fb3db292"), event_id=1024, version=0)
class Microsoft_Windows_UserDataAccess_PimIndexMaintenance_1024_0(Etw):
    pattern = Struct(
        "PROP_FILE_uint" / Int32ul
    )


@declare(guid=guid("99c66ba7-5a97-40d5-aa01-8a07fb3db292"), event_id=1028, version=0)
class Microsoft_Windows_UserDataAccess_PimIndexMaintenance_1028_0(Etw):
    pattern = Struct(
        "PROP_FILE_uint" / Int32ul
    )


@declare(guid=guid("99c66ba7-5a97-40d5-aa01-8a07fb3db292"), event_id=1029, version=0)
class Microsoft_Windows_UserDataAccess_PimIndexMaintenance_1029_0(Etw):
    pattern = Struct(
        "PROP_FILE_uint" / Int32ul
    )


@declare(guid=guid("99c66ba7-5a97-40d5-aa01-8a07fb3db292"), event_id=1030, version=0)
class Microsoft_Windows_UserDataAccess_PimIndexMaintenance_1030_0(Etw):
    pattern = Struct(
        "PROP_UInt32_1" / Int32ul,
        "PROP_UInt32_2" / Int32ul
    )


@declare(guid=guid("99c66ba7-5a97-40d5-aa01-8a07fb3db292"), event_id=1031, version=0)
class Microsoft_Windows_UserDataAccess_PimIndexMaintenance_1031_0(Etw):
    pattern = Struct(
        "PROP_UInt32" / Int32ul,
        "Prop_Hr_UInt32" / Int32sl
    )


@declare(guid=guid("99c66ba7-5a97-40d5-aa01-8a07fb3db292"), event_id=1032, version=0)
class Microsoft_Windows_UserDataAccess_PimIndexMaintenance_1032_0(Etw):
    pattern = Struct(
        "PROP_FILE_uint" / Int32ul
    )


@declare(guid=guid("99c66ba7-5a97-40d5-aa01-8a07fb3db292"), event_id=1033, version=0)
class Microsoft_Windows_UserDataAccess_PimIndexMaintenance_1033_0(Etw):
    pattern = Struct(
        "PROP_ByteCount" / Int32ul,
        "PROP_Bytes" / Bytes(lambda this: this.PROP_ByteCount)
    )


@declare(guid=guid("99c66ba7-5a97-40d5-aa01-8a07fb3db292"), event_id=1040, version=0)
class Microsoft_Windows_UserDataAccess_PimIndexMaintenance_1040_0(Etw):
    pattern = Struct(
        "App" / Guid,
        "Result" / Int32sl
    )


@declare(guid=guid("99c66ba7-5a97-40d5-aa01-8a07fb3db292"), event_id=1041, version=0)
class Microsoft_Windows_UserDataAccess_PimIndexMaintenance_1041_0(Etw):
    pattern = Struct(
        "Prop_Prop" / Int32ul
    )


@declare(guid=guid("99c66ba7-5a97-40d5-aa01-8a07fb3db292"), event_id=1042, version=0)
class Microsoft_Windows_UserDataAccess_PimIndexMaintenance_1042_0(Etw):
    pattern = Struct(
        "Prop_Prop" / Int32ul
    )


@declare(guid=guid("99c66ba7-5a97-40d5-aa01-8a07fb3db292"), event_id=1043, version=0)
class Microsoft_Windows_UserDataAccess_PimIndexMaintenance_1043_0(Etw):
    pattern = Struct(
        "P1_String" / CString
    )


@declare(guid=guid("99c66ba7-5a97-40d5-aa01-8a07fb3db292"), event_id=2018, version=0)
class Microsoft_Windows_UserDataAccess_PimIndexMaintenance_2018_0(Etw):
    pattern = Struct(
        "uint" / Int32ul
    )


@declare(guid=guid("99c66ba7-5a97-40d5-aa01-8a07fb3db292"), event_id=2019, version=0)
class Microsoft_Windows_UserDataAccess_PimIndexMaintenance_2019_0(Etw):
    pattern = Struct(
        "uint" / Int32ul
    )


@declare(guid=guid("99c66ba7-5a97-40d5-aa01-8a07fb3db292"), event_id=2022, version=0)
class Microsoft_Windows_UserDataAccess_PimIndexMaintenance_2022_0(Etw):
    pattern = Struct(
        "uint" / Int32ul
    )


@declare(guid=guid("99c66ba7-5a97-40d5-aa01-8a07fb3db292"), event_id=2023, version=0)
class Microsoft_Windows_UserDataAccess_PimIndexMaintenance_2023_0(Etw):
    pattern = Struct(
        "uint" / Int32ul
    )


@declare(guid=guid("99c66ba7-5a97-40d5-aa01-8a07fb3db292"), event_id=7003, version=0)
class Microsoft_Windows_UserDataAccess_PimIndexMaintenance_7003_0(Etw):
    pattern = Struct(
        "PROP_UInt32_1" / Int32ul,
        "PROP_UInt32_2" / Int32ul
    )

