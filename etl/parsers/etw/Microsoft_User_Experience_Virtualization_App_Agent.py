# -*- coding: utf-8 -*-
"""
Microsoft-User Experience Virtualization-App Agent
GUID : 1ed6976a-4171-4764-b415-7ea08bc46c51
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=1, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_1_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=2, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_2_0(Etw):
    pattern = Struct(
        "WString1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=3, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_3_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=4, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_4_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=5, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_5_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=6, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_6_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=7, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_7_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=8, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_8_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=9, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_9_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=10, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_10_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=11, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_11_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=12, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_12_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=13, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_13_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=14, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_14_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=15, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_15_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=16, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_16_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=17, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_17_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=18, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_18_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=19, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_19_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=507, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_507_0(Etw):
    pattern = Struct(
        "intValue1" / Int32sl
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=509, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_509_0(Etw):
    pattern = Struct(
        "Int1" / Int32sl,
        "String1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=690, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_690_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=691, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_691_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=692, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_692_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=693, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_693_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=694, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_694_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=695, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_695_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=701, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_701_0(Etw):
    pattern = Struct(
        "intValue1" / Int32sl
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=703, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_703_0(Etw):
    pattern = Struct(
        "Ulong1" / Int32ul
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=704, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_704_0(Etw):
    pattern = Struct(
        "Ulong1" / Int32ul
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=705, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_705_0(Etw):
    pattern = Struct(
        "Ulong1" / Int32ul
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=707, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_707_0(Etw):
    pattern = Struct(
        "intValue1" / Int32sl
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=1001, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_1001_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=1002, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_1002_0(Etw):
    pattern = Struct(
        "Ulong1" / Int32ul
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=1003, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_1003_0(Etw):
    pattern = Struct(
        "Ulong1" / Int32ul
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=1004, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_1004_0(Etw):
    pattern = Struct(
        "Ulong1" / Int32ul
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=1005, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_1005_0(Etw):
    pattern = Struct(
        "Ulong1" / Int32ul
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=1006, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_1006_0(Etw):
    pattern = Struct(
        "Ulong1" / Int32ul
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=1007, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_1007_0(Etw):
    pattern = Struct(
        "Ulong1" / Int32ul
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=1008, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_1008_0(Etw):
    pattern = Struct(
        "String1" / WString,
        "Ulong2" / Int32ul
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=1009, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_1009_0(Etw):
    pattern = Struct(
        "String1" / WString,
        "Ulong2" / Int32ul
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=1011, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_1011_0(Etw):
    pattern = Struct(
        "String1" / WString,
        "Ulong2" / Int32ul
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=1012, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_1012_0(Etw):
    pattern = Struct(
        "WString1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=1013, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_1013_0(Etw):
    pattern = Struct(
        "Ulong1" / Int32ul
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=1014, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_1014_0(Etw):
    pattern = Struct(
        "Int1" / Int32sl,
        "String1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=1501, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_1501_0(Etw):
    pattern = Struct(
        "WString1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=1503, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_1503_0(Etw):
    pattern = Struct(
        "String1" / CString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=1504, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_1504_0(Etw):
    pattern = Struct(
        "WString1" / WString,
        "AnsiString1" / CString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=1505, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_1505_0(Etw):
    pattern = Struct(
        "WString1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=1506, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_1506_0(Etw):
    pattern = Struct(
        "intValue1" / Int32sl
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=1507, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_1507_0(Etw):
    pattern = Struct(
        "intValue1" / Int32sl
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=1510, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_1510_0(Etw):
    pattern = Struct(
        "WString1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=1511, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_1511_0(Etw):
    pattern = Struct(
        "WString1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=1512, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_1512_0(Etw):
    pattern = Struct(
        "WString1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=1513, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_1513_0(Etw):
    pattern = Struct(
        "WString1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=1514, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_1514_0(Etw):
    pattern = Struct(
        "WString1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=2000, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_2000_0(Etw):
    pattern = Struct(
        "WString1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=2001, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_2001_0(Etw):
    pattern = Struct(
        "WString1" / WString,
        "AnsiString2" / CString,
        "HRESULT1" / Int32sl
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=2002, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_2002_0(Etw):
    pattern = Struct(
        "WString1" / WString,
        "WString2" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=2004, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_2004_0(Etw):
    pattern = Struct(
        "WString1" / WString,
        "HRESULT1" / Int32sl
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=2005, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_2005_0(Etw):
    pattern = Struct(
        "WString1" / WString,
        "AnsiString2" / CString,
        "HRESULT1" / Int32sl
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=2006, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_2006_0(Etw):
    pattern = Struct(
        "WString1" / WString,
        "AnsiString1" / CString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=2008, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_2008_0(Etw):
    pattern = Struct(
        "WString1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=2009, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_2009_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=2010, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_2010_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=2014, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_2014_0(Etw):
    pattern = Struct(
        "stringValue1" / WString,
        "intValue1" / Int32sl
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=2015, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_2015_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=2016, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_2016_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=2018, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_2018_0(Etw):
    pattern = Struct(
        "stringValue1" / WString,
        "intValue1" / Int32sl
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=2020, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_2020_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=2021, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_2021_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=2022, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_2022_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=2024, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_2024_0(Etw):
    pattern = Struct(
        "stringValue1" / WString,
        "intValue1" / Int32sl
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=2025, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_2025_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=2026, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_2026_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=2027, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_2027_0(Etw):
    pattern = Struct(
        "intValue1" / Int32sl
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=2033, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_2033_0(Etw):
    pattern = Struct(
        "Int1" / Int32sl,
        "String1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=2039, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_2039_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=2040, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_2040_0(Etw):
    pattern = Struct(
        "WString1" / WString,
        "WString2" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=2041, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_2041_0(Etw):
    pattern = Struct(
        "WString1" / WString,
        "WString2" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=2042, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_2042_0(Etw):
    pattern = Struct(
        "WString1" / WString,
        "WString2" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=2045, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_2045_0(Etw):
    pattern = Struct(
        "stringValue1" / WString,
        "intValue1" / Int32sl
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=2046, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_2046_0(Etw):
    pattern = Struct(
        "stringValue1" / WString,
        "intValue1" / Int32sl
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=2048, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_2048_0(Etw):
    pattern = Struct(
        "WString1" / WString,
        "WString2" / WString,
        "HRESULT1" / Int32sl
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=3000, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_3000_0(Etw):
    pattern = Struct(
        "String1" / WString,
        "Int1" / Int32ul,
        "Int2" / Int32ul
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=4000, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_4000_0(Etw):
    pattern = Struct(
        "repositoryPath" / WString,
        "settingsFilePathToAdd" / WString,
        "syncID" / Guid,
        "hresult" / Int32sl
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=4004, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_4004_0(Etw):
    pattern = Struct(
        "fileIdentifier" / WString,
        "packagePath" / WString,
        "serverRoot" / WString,
        "hresult" / Int32sl
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=4005, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_4005_0(Etw):
    pattern = Struct(
        "intValue1" / Int32sl
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=4009, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_4009_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=4010, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_4010_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=4017, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_4017_0(Etw):
    pattern = Struct(
        "stringValue1" / WString,
        "intValue1" / Int32sl
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=4018, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_4018_0(Etw):
    pattern = Struct(
        "stringValue1" / WString,
        "intValue1" / Int32sl
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=4020, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_4020_0(Etw):
    pattern = Struct(
        "stringValue1" / WString,
        "intValue1" / Int32sl
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=4025, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_4025_0(Etw):
    pattern = Struct(
        "stringValue1" / WString,
        "intValue1" / Int32sl
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=4026, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_4026_0(Etw):
    pattern = Struct(
        "stringValue1" / WString,
        "intValue1" / Int32sl
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=4027, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_4027_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=4028, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_4028_0(Etw):
    pattern = Struct(
        "repositoryPath" / WString,
        "recipeIDToSync" / WString,
        "SyncID" / Guid,
        "hresult" / Int32sl
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=4041, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_4041_0(Etw):
    pattern = Struct(
        "WString1" / WString,
        "WString2" / WString,
        "HRESULT1" / Int32sl
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=4042, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_4042_0(Etw):
    pattern = Struct(
        "WString1" / WString,
        "HRESULT1" / Int32sl
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=4044, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_4044_0(Etw):
    pattern = Struct(
        "intValue1" / Int32sl
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=4046, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_4046_0(Etw):
    pattern = Struct(
        "String1" / CString,
        "Int1" / Int32sl
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=4047, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_4047_0(Etw):
    pattern = Struct(
        "WString1" / WString,
        "AnsiString1" / CString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=4048, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_4048_0(Etw):
    pattern = Struct(
        "package" / WString,
        "actualSize" / Int32ul,
        "maxSize" / Int32ul
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=4051, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_4051_0(Etw):
    pattern = Struct(
        "WString1" / WString,
        "WString2" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=4059, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_4059_0(Etw):
    pattern = Struct(
        "Int1" / Int32sl,
        "String1" / WString,
        "Int2" / Int32ul
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=4060, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_4060_0(Etw):
    pattern = Struct(
        "stringValue1" / WString,
        "intValue1" / Int32sl
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=4061, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_4061_0(Etw):
    pattern = Struct(
        "stringValue1" / WString,
        "stringValue2" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=4063, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_4063_0(Etw):
    pattern = Struct(
        "WString1" / WString,
        "AnsiString1" / CString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=4064, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_4064_0(Etw):
    pattern = Struct(
        "WString1" / WString,
        "WString2" / WString,
        "HRESULT1" / Int32sl
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=4065, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_4065_0(Etw):
    pattern = Struct(
        "String1" / CString,
        "Int1" / Int32sl
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=4066, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_4066_0(Etw):
    pattern = Struct(
        "stringValue1" / WString,
        "intValue1" / Int32sl
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=4070, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_4070_0(Etw):
    pattern = Struct(
        "fileIdentifier" / WString,
        "packagePath" / WString,
        "serverRoot" / WString,
        "hresult" / Int32sl
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=4071, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_4071_0(Etw):
    pattern = Struct(
        "WString1" / WString,
        "HRESULT1" / Int32sl
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=4073, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_4073_0(Etw):
    pattern = Struct(
        "stringValue1" / WString,
        "stringValue2" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=4074, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_4074_0(Etw):
    pattern = Struct(
        "String1" / WString,
        "String2" / WString,
        "Int" / Int32sl
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=4075, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_4075_0(Etw):
    pattern = Struct(
        "String1" / WString,
        "String2" / WString,
        "String3" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=5000, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_5000_0(Etw):
    pattern = Struct(
        "RecipeID" / WString,
        "ErrorCode" / Int32sl,
        "AdditionalInformation" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=5001, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_5001_0(Etw):
    pattern = Struct(
        "RecipeID" / WString,
        "ErrorCode" / Int32sl,
        "AdditionalInformation" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=5002, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_5002_0(Etw):
    pattern = Struct(
        "RecipeID" / WString,
        "ErrorCode" / Int32sl,
        "AdditionalInformation" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=5003, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_5003_0(Etw):
    pattern = Struct(
        "RecipeID" / WString,
        "ErrorCode" / Int32sl,
        "AdditionalInformation" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=5312, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_5312_0(Etw):
    pattern = Struct(
        "RecipeID" / WString,
        "ErrorCode" / Int32sl,
        "AdditionalInformation" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=5313, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_5313_0(Etw):
    pattern = Struct(
        "stringValue1" / WString,
        "intValue1" / Int32sl
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=5314, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_5314_0(Etw):
    pattern = Struct(
        "stringValue1" / WString,
        "stringValue2" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=8000, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_8000_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=8010, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_8010_0(Etw):
    pattern = Struct(
        "intValue1" / Int32sl
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=8020, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_8020_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=8030, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_8030_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=8100, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_8100_0(Etw):
    pattern = Struct(
        "intValue1" / Int32sl
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=8110, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_8110_0(Etw):
    pattern = Struct(
        "intValue1" / Int32sl
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=8200, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_8200_0(Etw):
    pattern = Struct(
        "stringValue1" / WString,
        "intValue1" / Int32sl
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=8210, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_8210_0(Etw):
    pattern = Struct(
        "String1" / WString,
        "String2" / WString,
        "Int" / Int32sl
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=8220, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_8220_0(Etw):
    pattern = Struct(
        "String1" / WString,
        "String2" / WString,
        "Int" / Int32sl
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=8230, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_8230_0(Etw):
    pattern = Struct(
        "String1" / WString,
        "String2" / WString,
        "Int" / Int32sl
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=8240, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_8240_0(Etw):
    pattern = Struct(
        "stringValue1" / WString,
        "intValue1" / Int32sl
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=8300, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_8300_0(Etw):
    pattern = Struct(
        "intValue1" / Int32sl
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=8310, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_8310_0(Etw):
    pattern = Struct(
        "stringValue1" / WString,
        "intValue1" / Int32sl
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=8320, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_8320_0(Etw):
    pattern = Struct(
        "stringValue1" / WString,
        "intValue1" / Int32sl
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=8330, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_8330_0(Etw):
    pattern = Struct(
        "intValue1" / Int32sl
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=8340, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_8340_0(Etw):
    pattern = Struct(
        "UIntValue1" / Int32ul,
        "UIntValue2" / Int32ul,
        "intValue" / Int32sl
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=8350, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_8350_0(Etw):
    pattern = Struct(
        "stringValue1" / WString,
        "intValue1" / Int32sl
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=8360, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_8360_0(Etw):
    pattern = Struct(
        "String1" / WString,
        "String2" / WString,
        "Int" / Int32sl
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=8370, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_8370_0(Etw):
    pattern = Struct(
        "stringValue1" / WString,
        "intValue1" / Int32sl
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=8400, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_8400_0(Etw):
    pattern = Struct(
        "stringValue1" / WString,
        "intValue1" / Int32sl
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=9001, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_9001_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=9002, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_9002_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=9003, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_9003_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=9004, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_9004_0(Etw):
    pattern = Struct(
        "String1" / CString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=9005, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_9005_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=9006, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_9006_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=9007, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_9007_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=9008, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_9008_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=9009, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_9009_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=9010, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_9010_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=9011, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_9011_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=9012, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_9012_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=9013, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_9013_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=9014, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_9014_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=9015, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_9015_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=9016, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_9016_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=9017, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_9017_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=9018, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_9018_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=9019, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_9019_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=9020, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_9020_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=9021, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_9021_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=9022, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_9022_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=9023, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_9023_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=9024, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_9024_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=9025, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_9025_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=9026, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_9026_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=9027, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_9027_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=9028, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_9028_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=9029, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_9029_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=9030, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_9030_0(Etw):
    pattern = Struct(
        "String1" / WString,
        "String2" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=9031, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_9031_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=9032, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_9032_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=9033, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_9033_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=9034, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_9034_0(Etw):
    pattern = Struct(
        "String1" / WString,
        "Int1" / Int32ul,
        "Int2" / Int32ul
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=12003, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_12003_0(Etw):
    pattern = Struct(
        "Starttime" / SystemTime,
        "Endtime" / SystemTime
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=13000, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_13000_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=13001, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_13001_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=13002, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_13002_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=13006, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_13006_0(Etw):
    pattern = Struct(
        "intValue1" / Int32sl
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=13007, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_13007_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=13008, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_13008_0(Etw):
    pattern = Struct(
        "Int1" / Int32sl,
        "String1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=13009, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_13009_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=14000, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_14000_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=15000, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_15000_0(Etw):
    pattern = Struct(
        "intValue1" / Int32sl
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=15003, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_15003_0(Etw):
    pattern = Struct(
        "stringValue1" / WString,
        "stringValue2" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=16001, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_16001_0(Etw):
    pattern = Struct(
        "stringValue1" / WString
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=17000, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_17000_0(Etw):
    pattern = Struct(
        "hresultValue" / Int32sl
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=17001, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_17001_0(Etw):
    pattern = Struct(
        "hresultValue" / Int32sl
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=17002, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_17002_0(Etw):
    pattern = Struct(
        "hresultValue" / Int32sl
    )


@declare(guid=guid("1ed6976a-4171-4764-b415-7ea08bc46c51"), event_id=17003, version=0)
class Microsoft_User_Experience_Virtualization_App_Agent_17003_0(Etw):
    pattern = Struct(
        "WString1" / WString,
        "HRESULT1" / Int32sl
    )

