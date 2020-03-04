# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Documents
GUID : c89b991e-3b48-49b2-80d3-ac000dfc9749
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1001, version=0)
class Microsoft_Windows_Documents_1001_0(Etw):
    pattern = Struct(
        "JobId" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1002, version=0)
class Microsoft_Windows_Documents_1002_0(Etw):
    pattern = Struct(
        "JobId" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1003, version=0)
class Microsoft_Windows_Documents_1003_0(Etw):
    pattern = Struct(
        "JobId" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1004, version=0)
class Microsoft_Windows_Documents_1004_0(Etw):
    pattern = Struct(
        "JobId" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1005, version=0)
class Microsoft_Windows_Documents_1005_0(Etw):
    pattern = Struct(
        "JobId" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1006, version=0)
class Microsoft_Windows_Documents_1006_0(Etw):
    pattern = Struct(
        "JobId" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1007, version=0)
class Microsoft_Windows_Documents_1007_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Level" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1008, version=0)
class Microsoft_Windows_Documents_1008_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Level" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1009, version=0)
class Microsoft_Windows_Documents_1009_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Level" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1010, version=0)
class Microsoft_Windows_Documents_1010_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Level" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1011, version=0)
class Microsoft_Windows_Documents_1011_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Level" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1012, version=0)
class Microsoft_Windows_Documents_1012_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Level" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1013, version=0)
class Microsoft_Windows_Documents_1013_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Level" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1014, version=0)
class Microsoft_Windows_Documents_1014_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Level" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1015, version=0)
class Microsoft_Windows_Documents_1015_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Level" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1016, version=0)
class Microsoft_Windows_Documents_1016_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Level" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1017, version=0)
class Microsoft_Windows_Documents_1017_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Level" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1018, version=0)
class Microsoft_Windows_Documents_1018_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Level" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1021, version=0)
class Microsoft_Windows_Documents_1021_0(Etw):
    pattern = Struct(
        "Name" / WString
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1022, version=0)
class Microsoft_Windows_Documents_1022_0(Etw):
    pattern = Struct(
        "Name" / WString
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1023, version=0)
class Microsoft_Windows_Documents_1023_0(Etw):
    pattern = Struct(
        "Name" / WString
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1024, version=0)
class Microsoft_Windows_Documents_1024_0(Etw):
    pattern = Struct(
        "Name" / WString
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1200, version=0)
class Microsoft_Windows_Documents_1200_0(Etw):
    pattern = Struct(
        "Module" / WString,
        "Printer" / WString,
        "Capability" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1201, version=0)
class Microsoft_Windows_Documents_1201_0(Etw):
    pattern = Struct(
        "Module" / WString,
        "Printer" / WString,
        "Capability" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1202, version=0)
class Microsoft_Windows_Documents_1202_0(Etw):
    pattern = Struct(
        "Module" / WString,
        "Printer" / WString
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1203, version=0)
class Microsoft_Windows_Documents_1203_0(Etw):
    pattern = Struct(
        "Module" / WString,
        "Printer" / WString
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1204, version=0)
class Microsoft_Windows_Documents_1204_0(Etw):
    pattern = Struct(
        "Module" / WString,
        "Printer" / WString
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1205, version=0)
class Microsoft_Windows_Documents_1205_0(Etw):
    pattern = Struct(
        "Module" / WString,
        "Printer" / WString
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1206, version=0)
class Microsoft_Windows_Documents_1206_0(Etw):
    pattern = Struct(
        "Module" / WString
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1207, version=0)
class Microsoft_Windows_Documents_1207_0(Etw):
    pattern = Struct(
        "Module" / WString
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1208, version=0)
class Microsoft_Windows_Documents_1208_0(Etw):
    pattern = Struct(
        "Module" / WString,
        "Document" / WString
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1209, version=0)
class Microsoft_Windows_Documents_1209_0(Etw):
    pattern = Struct(
        "Module" / WString,
        "Document" / WString
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1210, version=0)
class Microsoft_Windows_Documents_1210_0(Etw):
    pattern = Struct(
        "Module" / WString,
        "Document" / WString
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1211, version=0)
class Microsoft_Windows_Documents_1211_0(Etw):
    pattern = Struct(
        "Module" / WString,
        "Document" / WString
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1212, version=0)
class Microsoft_Windows_Documents_1212_0(Etw):
    pattern = Struct(
        "Module" / WString
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1213, version=0)
class Microsoft_Windows_Documents_1213_0(Etw):
    pattern = Struct(
        "Module" / WString
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1214, version=0)
class Microsoft_Windows_Documents_1214_0(Etw):
    pattern = Struct(
        "Module" / WString
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1215, version=0)
class Microsoft_Windows_Documents_1215_0(Etw):
    pattern = Struct(
        "Module" / WString
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1216, version=0)
class Microsoft_Windows_Documents_1216_0(Etw):
    pattern = Struct(
        "Module" / WString
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1217, version=0)
class Microsoft_Windows_Documents_1217_0(Etw):
    pattern = Struct(
        "Module" / WString
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1218, version=0)
class Microsoft_Windows_Documents_1218_0(Etw):
    pattern = Struct(
        "Module" / WString
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1219, version=0)
class Microsoft_Windows_Documents_1219_0(Etw):
    pattern = Struct(
        "Module" / WString
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1504, version=0)
class Microsoft_Windows_Documents_1504_0(Etw):
    pattern = Struct(
        "Name" / WString
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1505, version=0)
class Microsoft_Windows_Documents_1505_0(Etw):
    pattern = Struct(
        "Name" / WString
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1522, version=0)
class Microsoft_Windows_Documents_1522_0(Etw):
    pattern = Struct(
        "Event" / WString,
        "Description" / WString,
        "Device" / WString,
        "Type" / Int32ul,
        "Handler" / WString
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1523, version=0)
class Microsoft_Windows_Documents_1523_0(Etw):
    pattern = Struct(
        "Event" / WString,
        "Description" / WString,
        "Device" / WString,
        "Type" / Int32ul,
        "Handler" / WString
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1524, version=0)
class Microsoft_Windows_Documents_1524_0(Etw):
    pattern = Struct(
        "Event" / WString,
        "Description" / WString,
        "Device" / WString,
        "Type" / Int32ul,
        "Handler" / WString
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1525, version=0)
class Microsoft_Windows_Documents_1525_0(Etw):
    pattern = Struct(
        "Event" / WString,
        "Description" / WString,
        "Device" / WString,
        "Type" / Int32ul,
        "Handler" / WString
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1526, version=0)
class Microsoft_Windows_Documents_1526_0(Etw):
    pattern = Struct(
        "Id" / WString
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1527, version=0)
class Microsoft_Windows_Documents_1527_0(Etw):
    pattern = Struct(
        "Id" / WString
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1528, version=0)
class Microsoft_Windows_Documents_1528_0(Etw):
    pattern = Struct(
        "DeviceId" / WString,
        "ScanSource" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1529, version=0)
class Microsoft_Windows_Documents_1529_0(Etw):
    pattern = Struct(
        "DeviceId" / WString,
        "ScanSource" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1530, version=0)
class Microsoft_Windows_Documents_1530_0(Etw):
    pattern = Struct(
        "DeviceId" / WString,
        "ScanSource" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1531, version=0)
class Microsoft_Windows_Documents_1531_0(Etw):
    pattern = Struct(
        "DeviceId" / WString,
        "ScanSource" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1532, version=0)
class Microsoft_Windows_Documents_1532_0(Etw):
    pattern = Struct(
        "CountScannedFiles" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1533, version=0)
class Microsoft_Windows_Documents_1533_0(Etw):
    pattern = Struct(
        "CountScannedFiles" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1604, version=0)
class Microsoft_Windows_Documents_1604_0(Etw):
    pattern = Struct(
        "JobId" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1605, version=0)
class Microsoft_Windows_Documents_1605_0(Etw):
    pattern = Struct(
        "JobId" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1606, version=0)
class Microsoft_Windows_Documents_1606_0(Etw):
    pattern = Struct(
        "DocumentNumber" / Int32ul,
        "PageNumber" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1607, version=0)
class Microsoft_Windows_Documents_1607_0(Etw):
    pattern = Struct(
        "DocumentNumber" / Int32ul,
        "PageNumber" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1608, version=0)
class Microsoft_Windows_Documents_1608_0(Etw):
    pattern = Struct(
        "DocumentNumber" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1609, version=0)
class Microsoft_Windows_Documents_1609_0(Etw):
    pattern = Struct(
        "DocumentNumber" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1620, version=0)
class Microsoft_Windows_Documents_1620_0(Etw):
    pattern = Struct(
        "DocumentNumber" / Int32ul,
        "PageNumber" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1621, version=0)
class Microsoft_Windows_Documents_1621_0(Etw):
    pattern = Struct(
        "DocumentNumber" / Int32ul,
        "PageNumber" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1640, version=0)
class Microsoft_Windows_Documents_1640_0(Etw):
    pattern = Struct(
        "JobId" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1641, version=0)
class Microsoft_Windows_Documents_1641_0(Etw):
    pattern = Struct(
        "JobId" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1642, version=0)
class Microsoft_Windows_Documents_1642_0(Etw):
    pattern = Struct(
        "JobId" / Int32ul,
        "IsOpenXPSDoc" / Int8ul,
        "IsOMInput" / Int8ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1643, version=0)
class Microsoft_Windows_Documents_1643_0(Etw):
    pattern = Struct(
        "JobId" / Int32ul,
        "IsOpenXPSDoc" / Int8ul,
        "IsOMInput" / Int8ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1644, version=0)
class Microsoft_Windows_Documents_1644_0(Etw):
    pattern = Struct(
        "JobId" / Int32ul,
        "IsOpenXPSDoc" / Int8ul,
        "IsOMInput" / Int8ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1645, version=0)
class Microsoft_Windows_Documents_1645_0(Etw):
    pattern = Struct(
        "JobId" / Int32ul,
        "IsOpenXPSDoc" / Int8ul,
        "IsOMInput" / Int8ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1646, version=0)
class Microsoft_Windows_Documents_1646_0(Etw):
    pattern = Struct(
        "JobId" / Int32ul,
        "IsOpenXPSDoc" / Int8ul,
        "IsOMInput" / Int8ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1647, version=0)
class Microsoft_Windows_Documents_1647_0(Etw):
    pattern = Struct(
        "JobId" / Int32ul,
        "IsOpenXPSDoc" / Int8ul,
        "IsOMInput" / Int8ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1648, version=0)
class Microsoft_Windows_Documents_1648_0(Etw):
    pattern = Struct(
        "FunctionName" / WString
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1649, version=0)
class Microsoft_Windows_Documents_1649_0(Etw):
    pattern = Struct(
        "FunctionName" / WString
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1800, version=0)
class Microsoft_Windows_Documents_1800_0(Etw):
    pattern = Struct(
        "OpNum" / Int32ul,
        "Handle" / Int64ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=1801, version=0)
class Microsoft_Windows_Documents_1801_0(Etw):
    pattern = Struct(
        "OpNum" / Int32ul,
        "Handle" / Int64ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=2033, version=0)
class Microsoft_Windows_Documents_2033_0(Etw):
    pattern = Struct(
        "JobId" / Int32ul,
        "FilterName" / WString
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=2034, version=0)
class Microsoft_Windows_Documents_2034_0(Etw):
    pattern = Struct(
        "JobId" / Int32ul,
        "FilterName" / WString
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=2041, version=0)
class Microsoft_Windows_Documents_2041_0(Etw):
    pattern = Struct(
        "IsEnabled" / Int8ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=2042, version=0)
class Microsoft_Windows_Documents_2042_0(Etw):
    pattern = Struct(
        "IsEnabled" / Int8ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=2043, version=0)
class Microsoft_Windows_Documents_2043_0(Etw):
    pattern = Struct(
        "FunctionName" / WString
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=2044, version=0)
class Microsoft_Windows_Documents_2044_0(Etw):
    pattern = Struct(
        "FunctionName" / WString
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=2101, version=0)
class Microsoft_Windows_Documents_2101_0(Etw):
    pattern = Struct(
        "JobId" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=2102, version=0)
class Microsoft_Windows_Documents_2102_0(Etw):
    pattern = Struct(
        "JobId" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=2103, version=0)
class Microsoft_Windows_Documents_2103_0(Etw):
    pattern = Struct(
        "JobId" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=2104, version=0)
class Microsoft_Windows_Documents_2104_0(Etw):
    pattern = Struct(
        "JobId" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=2105, version=0)
class Microsoft_Windows_Documents_2105_0(Etw):
    pattern = Struct(
        "JobId" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=2106, version=0)
class Microsoft_Windows_Documents_2106_0(Etw):
    pattern = Struct(
        "JobId" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=2107, version=0)
class Microsoft_Windows_Documents_2107_0(Etw):
    pattern = Struct(
        "JobId" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=2108, version=0)
class Microsoft_Windows_Documents_2108_0(Etw):
    pattern = Struct(
        "JobId" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=2109, version=0)
class Microsoft_Windows_Documents_2109_0(Etw):
    pattern = Struct(
        "FunctionName" / WString,
        "FunctionId" / Int32ul,
        "FilterName" / WString
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=2110, version=0)
class Microsoft_Windows_Documents_2110_0(Etw):
    pattern = Struct(
        "FunctionName" / WString,
        "FunctionId" / Int32ul,
        "FilterName" / WString
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=3150, version=0)
class Microsoft_Windows_Documents_3150_0(Etw):
    pattern = Struct(
        "Notifier" / Int64ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=3151, version=0)
class Microsoft_Windows_Documents_3151_0(Etw):
    pattern = Struct(
        "Notifier" / Int64ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=3201, version=0)
class Microsoft_Windows_Documents_3201_0(Etw):
    pattern = Struct(
        "WindowHandle" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=3202, version=0)
class Microsoft_Windows_Documents_3202_0(Etw):
    pattern = Struct(
        "WindowHandle" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=3251, version=0)
class Microsoft_Windows_Documents_3251_0(Etw):
    pattern = Struct(
        "WindowHandle" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=3252, version=0)
class Microsoft_Windows_Documents_3252_0(Etw):
    pattern = Struct(
        "WindowHandle" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=6001, version=0)
class Microsoft_Windows_Documents_6001_0(Etw):
    pattern = Struct(
        "idGuid" / Guid
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=6002, version=0)
class Microsoft_Windows_Documents_6002_0(Etw):
    pattern = Struct(
        "idGuid" / Guid
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=6003, version=0)
class Microsoft_Windows_Documents_6003_0(Etw):
    pattern = Struct(
        "idGuid" / Guid
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=6004, version=0)
class Microsoft_Windows_Documents_6004_0(Etw):
    pattern = Struct(
        "idGuid" / Guid
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=6005, version=0)
class Microsoft_Windows_Documents_6005_0(Etw):
    pattern = Struct(
        "idGuid" / Guid
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=6006, version=0)
class Microsoft_Windows_Documents_6006_0(Etw):
    pattern = Struct(
        "idGuid" / Guid
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=6007, version=0)
class Microsoft_Windows_Documents_6007_0(Etw):
    pattern = Struct(
        "idGuid" / Guid
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=6008, version=0)
class Microsoft_Windows_Documents_6008_0(Etw):
    pattern = Struct(
        "idGuid" / Guid
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=6021, version=0)
class Microsoft_Windows_Documents_6021_0(Etw):
    pattern = Struct(
        "ScanRepository" / Int64ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=6022, version=0)
class Microsoft_Windows_Documents_6022_0(Etw):
    pattern = Struct(
        "ScanRepository" / Int64ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=6023, version=0)
class Microsoft_Windows_Documents_6023_0(Etw):
    pattern = Struct(
        "idGuid" / Guid
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=6024, version=0)
class Microsoft_Windows_Documents_6024_0(Etw):
    pattern = Struct(
        "idGuid" / Guid
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=6025, version=0)
class Microsoft_Windows_Documents_6025_0(Etw):
    pattern = Struct(
        "idGuid" / Guid
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=6026, version=0)
class Microsoft_Windows_Documents_6026_0(Etw):
    pattern = Struct(
        "idGuid" / Guid
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=6027, version=0)
class Microsoft_Windows_Documents_6027_0(Etw):
    pattern = Struct(
        "idGuid" / Guid,
        "FileIndex" / Int64ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=6028, version=0)
class Microsoft_Windows_Documents_6028_0(Etw):
    pattern = Struct(
        "idGuid" / Guid,
        "FileIndex" / Int64ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=6029, version=0)
class Microsoft_Windows_Documents_6029_0(Etw):
    pattern = Struct(
        "idGuid" / Guid
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=6030, version=0)
class Microsoft_Windows_Documents_6030_0(Etw):
    pattern = Struct(
        "idGuid" / Guid
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=6031, version=0)
class Microsoft_Windows_Documents_6031_0(Etw):
    pattern = Struct(
        "idGuid" / Guid,
        "FileIndex" / Int64ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=6032, version=0)
class Microsoft_Windows_Documents_6032_0(Etw):
    pattern = Struct(
        "idGuid" / Guid,
        "FileIndex" / Int64ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=6101, version=0)
class Microsoft_Windows_Documents_6101_0(Etw):
    pattern = Struct(
        "InfNameOrPath" / WString,
        "ServerName" / WString,
        "ModelOrDriverName" / WString
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=6102, version=0)
class Microsoft_Windows_Documents_6102_0(Etw):
    pattern = Struct(
        "InfNameOrPath" / WString,
        "ServerName" / WString,
        "ModelOrDriverName" / WString
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=6103, version=0)
class Microsoft_Windows_Documents_6103_0(Etw):
    pattern = Struct(
        "InfNameOrPath" / WString,
        "ServerName" / WString,
        "ModelOrDriverName" / WString
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=6104, version=0)
class Microsoft_Windows_Documents_6104_0(Etw):
    pattern = Struct(
        "InfNameOrPath" / WString,
        "ServerName" / WString,
        "ModelOrDriverName" / WString
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=6105, version=0)
class Microsoft_Windows_Documents_6105_0(Etw):
    pattern = Struct(
        "InfNameOrPath" / WString,
        "ServerName" / WString,
        "ModelOrDriverName" / WString
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=6106, version=0)
class Microsoft_Windows_Documents_6106_0(Etw):
    pattern = Struct(
        "InfNameOrPath" / WString,
        "ServerName" / WString,
        "ModelOrDriverName" / WString
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=6107, version=0)
class Microsoft_Windows_Documents_6107_0(Etw):
    pattern = Struct(
        "DeviceInstanceId" / WString
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=6108, version=0)
class Microsoft_Windows_Documents_6108_0(Etw):
    pattern = Struct(
        "DeviceInstanceId" / WString
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=6109, version=0)
class Microsoft_Windows_Documents_6109_0(Etw):
    pattern = Struct(
        "InstanceId" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=6110, version=0)
class Microsoft_Windows_Documents_6110_0(Etw):
    pattern = Struct(
        "InstanceId" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=6111, version=0)
class Microsoft_Windows_Documents_6111_0(Etw):
    pattern = Struct(
        "InstanceId" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=6112, version=0)
class Microsoft_Windows_Documents_6112_0(Etw):
    pattern = Struct(
        "InstanceId" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=6113, version=0)
class Microsoft_Windows_Documents_6113_0(Etw):
    pattern = Struct(
        "PrinterName" / WString,
        "HardwareID" / WString
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=6114, version=0)
class Microsoft_Windows_Documents_6114_0(Etw):
    pattern = Struct(
        "PrinterName" / WString,
        "HardwareID" / WString
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=6117, version=0)
class Microsoft_Windows_Documents_6117_0(Etw):
    pattern = Struct(
        "Model" / WString,
        "Manufacturer" / WString,
        "Provider" / WString,
        "HardwareID" / WString,
        "DriverDate" / Int64ul,
        "DriverVersion" / Int64ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=6118, version=0)
class Microsoft_Windows_Documents_6118_0(Etw):
    pattern = Struct(
        "Model" / WString,
        "Manufacturer" / WString,
        "Provider" / WString,
        "HardwareID" / WString,
        "DriverDate" / Int64ul,
        "DriverVersion" / Int64ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=6119, version=0)
class Microsoft_Windows_Documents_6119_0(Etw):
    pattern = Struct(
        "ModelName" / WString,
        "Manufacturer" / WString,
        "Provider" / WString,
        "HardwareID" / WString
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=6120, version=0)
class Microsoft_Windows_Documents_6120_0(Etw):
    pattern = Struct(
        "ModelName" / WString,
        "Manufacturer" / WString,
        "Provider" / WString,
        "HardwareID" / WString
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=6121, version=0)
class Microsoft_Windows_Documents_6121_0(Etw):
    pattern = Struct(
        "ModelName" / WString,
        "Manufacturer" / WString,
        "Provider" / WString,
        "HardwareID" / WString
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=6122, version=0)
class Microsoft_Windows_Documents_6122_0(Etw):
    pattern = Struct(
        "ModelName" / WString,
        "Manufacturer" / WString,
        "Provider" / WString,
        "HardwareID" / WString
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=6123, version=0)
class Microsoft_Windows_Documents_6123_0(Etw):
    pattern = Struct(
        "Model" / WString,
        "Manufacturer" / WString,
        "Provider" / WString,
        "HardwareID" / WString,
        "DriverDate" / Int64ul,
        "DriverVersion" / Int64ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=6124, version=0)
class Microsoft_Windows_Documents_6124_0(Etw):
    pattern = Struct(
        "Model" / WString,
        "Manufacturer" / WString,
        "Provider" / WString,
        "HardwareID" / WString,
        "DriverDate" / Int64ul,
        "DriverVersion" / Int64ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=6201, version=0)
class Microsoft_Windows_Documents_6201_0(Etw):
    pattern = Struct(
        "PortName" / WString,
        "Action" / WString
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=6202, version=0)
class Microsoft_Windows_Documents_6202_0(Etw):
    pattern = Struct(
        "PortName" / WString,
        "Action" / WString
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=6203, version=0)
class Microsoft_Windows_Documents_6203_0(Etw):
    pattern = Struct(
        "PortName" / WString,
        "PrinterName" / WString
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=6204, version=0)
class Microsoft_Windows_Documents_6204_0(Etw):
    pattern = Struct(
        "PortName" / WString,
        "PrinterName" / WString
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=6205, version=0)
class Microsoft_Windows_Documents_6205_0(Etw):
    pattern = Struct(
        "JobId" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=6206, version=0)
class Microsoft_Windows_Documents_6206_0(Etw):
    pattern = Struct(
        "JobId" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=6301, version=0)
class Microsoft_Windows_Documents_6301_0(Etw):
    pattern = Struct(
        "PortName" / WString
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=6302, version=0)
class Microsoft_Windows_Documents_6302_0(Etw):
    pattern = Struct(
        "PortName" / WString
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=6303, version=0)
class Microsoft_Windows_Documents_6303_0(Etw):
    pattern = Struct(
        "DeviceId" / WString,
        "ServiceId" / WString
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=6304, version=0)
class Microsoft_Windows_Documents_6304_0(Etw):
    pattern = Struct(
        "DeviceId" / WString,
        "ServiceId" / WString
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=6305, version=0)
class Microsoft_Windows_Documents_6305_0(Etw):
    pattern = Struct(
        "PortName" / WString
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=6306, version=0)
class Microsoft_Windows_Documents_6306_0(Etw):
    pattern = Struct(
        "PortName" / WString
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=6307, version=0)
class Microsoft_Windows_Documents_6307_0(Etw):
    pattern = Struct(
        "PortName" / WString
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=6308, version=0)
class Microsoft_Windows_Documents_6308_0(Etw):
    pattern = Struct(
        "PortName" / WString
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=6309, version=0)
class Microsoft_Windows_Documents_6309_0(Etw):
    pattern = Struct(
        "JobId" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=6310, version=0)
class Microsoft_Windows_Documents_6310_0(Etw):
    pattern = Struct(
        "JobId" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=7021, version=0)
class Microsoft_Windows_Documents_7021_0(Etw):
    pattern = Struct(
        "PageIndex" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=7022, version=0)
class Microsoft_Windows_Documents_7022_0(Etw):
    pattern = Struct(
        "PageIndex" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=7023, version=0)
class Microsoft_Windows_Documents_7023_0(Etw):
    pattern = Struct(
        "PageIndex" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=7024, version=0)
class Microsoft_Windows_Documents_7024_0(Etw):
    pattern = Struct(
        "PageIndex" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=7025, version=0)
class Microsoft_Windows_Documents_7025_0(Etw):
    pattern = Struct(
        "PageIndex" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=7026, version=0)
class Microsoft_Windows_Documents_7026_0(Etw):
    pattern = Struct(
        "PageIndex" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=7033, version=0)
class Microsoft_Windows_Documents_7033_0(Etw):
    pattern = Struct(
        "PageIndex" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=7034, version=0)
class Microsoft_Windows_Documents_7034_0(Etw):
    pattern = Struct(
        "PageIndex" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=7062, version=0)
class Microsoft_Windows_Documents_7062_0(Etw):
    pattern = Struct(
        "ID" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=7063, version=0)
class Microsoft_Windows_Documents_7063_0(Etw):
    pattern = Struct(
        "ID" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=7066, version=0)
class Microsoft_Windows_Documents_7066_0(Etw):
    pattern = Struct(
        "PageIndex" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=7067, version=0)
class Microsoft_Windows_Documents_7067_0(Etw):
    pattern = Struct(
        "PageIndex" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=7068, version=0)
class Microsoft_Windows_Documents_7068_0(Etw):
    pattern = Struct(
        "Type" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=7069, version=0)
class Microsoft_Windows_Documents_7069_0(Etw):
    pattern = Struct(
        "Type" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=8000, version=0)
class Microsoft_Windows_Documents_8000_0(Etw):
    pattern = Struct(
        "PrinterName" / WString,
        "IsCached" / Int8ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=8001, version=0)
class Microsoft_Windows_Documents_8001_0(Etw):
    pattern = Struct(
        "PrinterName" / WString,
        "IsCached" / Int8ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=8002, version=0)
class Microsoft_Windows_Documents_8002_0(Etw):
    pattern = Struct(
        "PrinterName" / WString,
        "IsFirstCall" / Int8ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=8003, version=0)
class Microsoft_Windows_Documents_8003_0(Etw):
    pattern = Struct(
        "PrinterName" / WString,
        "IsFirstCall" / Int8ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=8004, version=0)
class Microsoft_Windows_Documents_8004_0(Etw):
    pattern = Struct(
        "PrinterName" / WString
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=8005, version=0)
class Microsoft_Windows_Documents_8005_0(Etw):
    pattern = Struct(
        "PrinterName" / WString
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=8006, version=0)
class Microsoft_Windows_Documents_8006_0(Etw):
    pattern = Struct(
        "PrinterName" / WString,
        "FeatureName" / WString,
        "IsFirstCall" / Int8ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=8007, version=0)
class Microsoft_Windows_Documents_8007_0(Etw):
    pattern = Struct(
        "PrinterName" / WString,
        "FeatureName" / WString,
        "IsFirstCall" / Int8ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=8008, version=0)
class Microsoft_Windows_Documents_8008_0(Etw):
    pattern = Struct(
        "JobId" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=8009, version=0)
class Microsoft_Windows_Documents_8009_0(Etw):
    pattern = Struct(
        "JobId" / Int32ul
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=8100, version=0)
class Microsoft_Windows_Documents_8100_0(Etw):
    pattern = Struct(
        "FunctionName" / WString,
        "PrinterName" / WString
    )


@declare(guid=guid("c89b991e-3b48-49b2-80d3-ac000dfc9749"), event_id=8101, version=0)
class Microsoft_Windows_Documents_8101_0(Etw):
    pattern = Struct(
        "FunctionName" / WString,
        "PrinterName" / WString
    )

