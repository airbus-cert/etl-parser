# -*- coding: utf-8 -*-
"""
Microsoft-Windows-ShellCommon-StartLayoutPopulation
GUID : 97ca8142-10b1-4baa-9fbb-70a7d11231c3
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=1, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_1_0(Etw):
    pattern = Struct(
        "collectionName" / WString,
        "initializationReason" / Int32ul
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=2, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_2_0(Etw):
    pattern = Struct(
        "value" / WString
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=3, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_3_0(Etw):
    pattern = Struct(
        "layoutSelectionSerializedString" / WString
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=5, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_5_0(Etw):
    pattern = Struct(
        "TaskHResultValue" / Int32ul
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=7, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_7_0(Etw):
    pattern = Struct(
        "layoutProviderName" / WString
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=8, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_8_0(Etw):
    pattern = Struct(
        "layoutProviderName" / WString
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=11, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_11_0(Etw):
    pattern = Struct(
        "layoutProviderName" / WString
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=12, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_12_0(Etw):
    pattern = Struct(
        "layoutProviderName" / WString,
        "HResultValue" / Int32ul
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=15, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_15_0(Etw):
    pattern = Struct(
        "value" / WString
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=16, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_16_0(Etw):
    pattern = Struct(
        "tileIdentifier" / WString
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=17, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_17_0(Etw):
    pattern = Struct(
        "tileIdentifier" / WString,
        "failureDetails" / CString
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=18, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_18_0(Etw):
    pattern = Struct(
        "TaskHResultValue" / Int32ul
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=19, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_19_0(Etw):
    pattern = Struct(
        "tileData" / WString
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=21, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_21_0(Etw):
    pattern = Struct(
        "failureDetails" / CString
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=22, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_22_0(Etw):
    pattern = Struct(
        "TaskHResultValue" / Int32ul
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=23, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_23_0(Etw):
    pattern = Struct(
        "tileIdentifier" / WString
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=28, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_28_0(Etw):
    pattern = Struct(
        "tileIdentifier" / WString
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=29, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_29_0(Etw):
    pattern = Struct(
        "tileAumid" / WString,
        "appSize" / Int64ul
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=30, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_30_0(Etw):
    pattern = Struct(
        "tileAumid" / WString,
        "appSize" / Int64ul
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=31, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_31_0(Etw):
    pattern = Struct(
        "appSize" / Int32ul
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=32, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_32_0(Etw):
    pattern = Struct(
        "tileIdentifier" / WString
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=33, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_33_0(Etw):
    pattern = Struct(
        "value" / WString
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=35, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_35_0(Etw):
    pattern = Struct(
        "TaskHResultValue" / Int32ul
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=38, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_38_0(Etw):
    pattern = Struct(
        "value" / WString
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=39, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_39_0(Etw):
    pattern = Struct(
        "value" / WString
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=41, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_41_0(Etw):
    pattern = Struct(
        "value" / WString
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=42, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_42_0(Etw):
    pattern = Struct(
        "value" / WString
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=45, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_45_0(Etw):
    pattern = Struct(
        "containerName" / WString,
        "containerXPosition" / Int32ul,
        "containerYPosition" / Int32ul
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=46, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_46_0(Etw):
    pattern = Struct(
        "containerName" / WString,
        "containerXPosition" / Int32ul,
        "containerYPosition" / Int32ul,
        "failureDetails" / CString
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=49, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_49_0(Etw):
    pattern = Struct(
        "value" / WString
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=52, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_52_0(Etw):
    pattern = Struct(
        "tileData" / WString
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=53, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_53_0(Etw):
    pattern = Struct(
        "tileIdentifier" / WString
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=54, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_54_0(Etw):
    pattern = Struct(
        "groupData" / WString
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=55, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_55_0(Etw):
    pattern = Struct(
        "groupData" / WString
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=56, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_56_0(Etw):
    pattern = Struct(
        "containerName" / WString,
        "containerXPosition" / Int32ul,
        "containerYPosition" / Int32ul
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=57, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_57_0(Etw):
    pattern = Struct(
        "containerName" / WString,
        "containerXPosition" / Int32ul,
        "containerYPosition" / Int32ul,
        "failureDetails" / CString
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=58, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_58_0(Etw):
    pattern = Struct(
        "TaskHResultValue" / Int32ul
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=60, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_60_0(Etw):
    pattern = Struct(
        "TaskHResultValue" / Int32ul
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=62, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_62_0(Etw):
    pattern = Struct(
        "TaskHResultValue" / Int32ul
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=63, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_63_0(Etw):
    pattern = Struct(
        "value" / WString
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=64, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_64_0(Etw):
    pattern = Struct(
        "value" / WString
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=65, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_65_0(Etw):
    pattern = Struct(
        "value1" / WString,
        "value2" / WString
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=1002, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_1002_0(Etw):
    pattern = Struct(
        "itemName" / WString,
        "itemId" / Guid
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=1004, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_1004_0(Etw):
    pattern = Struct(
        "itemId" / WString,
        "itemName" / WString,
        "groupCount" / Int32ul,
        "tileCount" / Int32ul
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=1005, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_1005_0(Etw):
    pattern = Struct(
        "itemId" / WString,
        "itemName" / WString,
        "groupCount" / Int32ul,
        "tileCount" / Int32ul
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=1100, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_1100_0(Etw):
    pattern = Struct(
        "itemId" / Guid,
        "containerId" / Guid,
        "collectionName" / WString
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=1101, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_1101_0(Etw):
    pattern = Struct(
        "itemName" / WString,
        "itemId" / Guid,
        "containerId" / Guid,
        "collectionName" / WString
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=1102, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_1102_0(Etw):
    pattern = Struct(
        "itemName" / WString,
        "itemId" / Guid,
        "containerId" / Guid,
        "collectionName" / WString
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=1103, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_1103_0(Etw):
    pattern = Struct(
        "itemName" / WString,
        "itemId" / Guid,
        "containerId" / Guid,
        "collectionName" / WString
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=1104, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_1104_0(Etw):
    pattern = Struct(
        "itemName" / WString,
        "itemId" / Guid,
        "containerId" / Guid,
        "collectionName" / WString
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=1105, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_1105_0(Etw):
    pattern = Struct(
        "itemName" / WString,
        "itemId" / Guid,
        "containerId" / Guid,
        "collectionName" / WString
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=1106, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_1106_0(Etw):
    pattern = Struct(
        "value" / WString
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=1107, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_1107_0(Etw):
    pattern = Struct(
        "value" / WString
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=1200, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_1200_0(Etw):
    pattern = Struct(
        "itemName" / WString,
        "itemId" / Guid
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=1202, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_1202_0(Etw):
    pattern = Struct(
        "itemName" / WString,
        "itemId" / Guid
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=1203, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_1203_0(Etw):
    pattern = Struct(
        "itemName" / WString,
        "itemId" / Guid
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=1204, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_1204_0(Etw):
    pattern = Struct(
        "itemId" / Guid,
        "containerId" / Guid,
        "collectionName" / WString
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=1205, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_1205_0(Etw):
    pattern = Struct(
        "itemId" / Guid,
        "containerId" / Guid,
        "collectionName" / WString
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=1206, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_1206_0(Etw):
    pattern = Struct(
        "itemId" / Guid
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=1207, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_1207_0(Etw):
    pattern = Struct(
        "itemId" / Guid,
        "containerId" / Guid,
        "collectionName" / WString
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=1208, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_1208_0(Etw):
    pattern = Struct(
        "itemId" / Guid,
        "containerId" / Guid,
        "collectionName" / WString
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=1209, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_1209_0(Etw):
    pattern = Struct(
        "itemId" / Guid
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=1250, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_1250_0(Etw):
    pattern = Struct(
        "savedVersion" / Int64ul,
        "itemId" / WString
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=1252, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_1252_0(Etw):
    pattern = Struct(
        "savedVersion" / Int64ul,
        "itemId" / WString
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=1253, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_1253_0(Etw):
    pattern = Struct(
        "savedVersion" / Int64ul,
        "itemId" / WString
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=1300, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_1300_0(Etw):
    pattern = Struct(
        "itemName" / WString,
        "itemId" / Guid
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=1301, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_1301_0(Etw):
    pattern = Struct(
        "itemName" / WString,
        "itemId" / Guid
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=1303, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_1303_0(Etw):
    pattern = Struct(
        "itemName" / WString,
        "itemId" / Guid
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=1400, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_1400_0(Etw):
    pattern = Struct(
        "tileIdentifier" / WString,
        "collectionName" / WString
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=1401, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_1401_0(Etw):
    pattern = Struct(
        "tileIdentifier" / WString,
        "collectionName" / WString
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=1404, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_1404_0(Etw):
    pattern = Struct(
        "value" / WString
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=1405, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_1405_0(Etw):
    pattern = Struct(
        "value" / WString
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=1900, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_1900_0(Etw):
    pattern = Struct(
        "itemName" / WString,
        "itemId" / Guid
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=1902, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_1902_0(Etw):
    pattern = Struct(
        "itemName" / WString,
        "itemId" / Guid
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=1903, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_1903_0(Etw):
    pattern = Struct(
        "itemName" / WString,
        "itemId" / Guid
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=1904, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_1904_0(Etw):
    pattern = Struct(
        "value" / WString
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=1905, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_1905_0(Etw):
    pattern = Struct(
        "value" / WString
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=1906, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_1906_0(Etw):
    pattern = Struct(
        "value" / WString
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=2101, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_2101_0(Etw):
    pattern = Struct(
        "itemName" / WString,
        "itemId" / Guid
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=2102, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_2102_0(Etw):
    pattern = Struct(
        "itemName" / WString,
        "itemId" / Guid,
        "savedVersion" / Int64ul
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=2103, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_2103_0(Etw):
    pattern = Struct(
        "itemName" / WString,
        "itemId" / Guid
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=2110, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_2110_0(Etw):
    pattern = Struct(
        "itemName" / WString,
        "size" / Int64ul
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=2111, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_2111_0(Etw):
    pattern = Struct(
        "itemName" / WString,
        "size" / Int64ul
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=2112, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_2112_0(Etw):
    pattern = Struct(
        "itemName" / WString,
        "size" / Int64ul,
        "savedVersion" / Int64ul
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=2150, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_2150_0(Etw):
    pattern = Struct(
        "itemName" / WString,
        "itemId" / Guid
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=2151, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_2151_0(Etw):
    pattern = Struct(
        "value" / WString
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=2152, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_2152_0(Etw):
    pattern = Struct(
        "packageFamilyName" / WString,
        "InstallState" / Int32ul
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=2153, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_2153_0(Etw):
    pattern = Struct(
        "packageFamilyName" / WString,
        "InstallState" / Int32ul
    )


@declare(guid=guid("97ca8142-10b1-4baa-9fbb-70a7d11231c3"), event_id=2154, version=0)
class Microsoft_Windows_ShellCommon_StartLayoutPopulation_2154_0(Etw):
    pattern = Struct(
        "value" / WString
    )

