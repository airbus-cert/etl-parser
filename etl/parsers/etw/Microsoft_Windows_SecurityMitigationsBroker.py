# -*- coding: utf-8 -*-
"""
Microsoft-Windows-SecurityMitigationsBroker
GUID : ea8cd8a5-78ff-4418-b292-aadc6a7181df
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("ea8cd8a5-78ff-4418-b292-aadc6a7181df"), event_id=1003, version=0)
class Microsoft_Windows_SecurityMitigationsBroker_1003_0(Etw):
    pattern = Struct(
        "DriverId" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("ea8cd8a5-78ff-4418-b292-aadc6a7181df"), event_id=1004, version=0)
class Microsoft_Windows_SecurityMitigationsBroker_1004_0(Etw):
    pattern = Struct(
        "DriverId" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("ea8cd8a5-78ff-4418-b292-aadc6a7181df"), event_id=1005, version=0)
class Microsoft_Windows_SecurityMitigationsBroker_1005_0(Etw):
    pattern = Struct(
        "DriverId" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("ea8cd8a5-78ff-4418-b292-aadc6a7181df"), event_id=1006, version=0)
class Microsoft_Windows_SecurityMitigationsBroker_1006_0(Etw):
    pattern = Struct(
        "DriverId" / Int64ul,
        "ACGState" / Int32ul
    )


@declare(guid=guid("ea8cd8a5-78ff-4418-b292-aadc6a7181df"), event_id=1007, version=0)
class Microsoft_Windows_SecurityMitigationsBroker_1007_0(Etw):
    pattern = Struct(
        "DriverId" / Int64ul,
        "ProcessId" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("ea8cd8a5-78ff-4418-b292-aadc6a7181df"), event_id=1008, version=0)
class Microsoft_Windows_SecurityMitigationsBroker_1008_0(Etw):
    pattern = Struct(
        "DriverId" / Int64ul,
        "ProcessId" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("ea8cd8a5-78ff-4418-b292-aadc6a7181df"), event_id=1009, version=0)
class Microsoft_Windows_SecurityMitigationsBroker_1009_0(Etw):
    pattern = Struct(
        "DriverId" / Int64ul,
        "ProcessId" / Int32ul,
        "ACGState" / Int32ul
    )


@declare(guid=guid("ea8cd8a5-78ff-4418-b292-aadc6a7181df"), event_id=1010, version=0)
class Microsoft_Windows_SecurityMitigationsBroker_1010_0(Etw):
    pattern = Struct(
        "DriverId" / Int64ul,
        "ProcessId" / Int32ul
    )


@declare(guid=guid("ea8cd8a5-78ff-4418-b292-aadc6a7181df"), event_id=1011, version=0)
class Microsoft_Windows_SecurityMitigationsBroker_1011_0(Etw):
    pattern = Struct(
        "DriverId" / Int64ul,
        "ProcessId" / Int32ul
    )


@declare(guid=guid("ea8cd8a5-78ff-4418-b292-aadc6a7181df"), event_id=1012, version=0)
class Microsoft_Windows_SecurityMitigationsBroker_1012_0(Etw):
    pattern = Struct(
        "DriverId" / Int64ul,
        "ProcessId" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("ea8cd8a5-78ff-4418-b292-aadc6a7181df"), event_id=1013, version=0)
class Microsoft_Windows_SecurityMitigationsBroker_1013_0(Etw):
    pattern = Struct(
        "DriverId" / Int64ul,
        "ProcessId" / Int32ul
    )


@declare(guid=guid("ea8cd8a5-78ff-4418-b292-aadc6a7181df"), event_id=1014, version=0)
class Microsoft_Windows_SecurityMitigationsBroker_1014_0(Etw):
    pattern = Struct(
        "DriverId" / Int64ul,
        "ProcessId" / Int32ul
    )


@declare(guid=guid("ea8cd8a5-78ff-4418-b292-aadc6a7181df"), event_id=1015, version=0)
class Microsoft_Windows_SecurityMitigationsBroker_1015_0(Etw):
    pattern = Struct(
        "DriverId" / Int64ul,
        "ProcessId" / Int32ul
    )


@declare(guid=guid("ea8cd8a5-78ff-4418-b292-aadc6a7181df"), event_id=1016, version=0)
class Microsoft_Windows_SecurityMitigationsBroker_1016_0(Etw):
    pattern = Struct(
        "DriverId" / Int64ul,
        "ProcessId" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("ea8cd8a5-78ff-4418-b292-aadc6a7181df"), event_id=1017, version=0)
class Microsoft_Windows_SecurityMitigationsBroker_1017_0(Etw):
    pattern = Struct(
        "DriverId" / Int64ul,
        "ProcessId" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("ea8cd8a5-78ff-4418-b292-aadc6a7181df"), event_id=1018, version=0)
class Microsoft_Windows_SecurityMitigationsBroker_1018_0(Etw):
    pattern = Struct(
        "DriverId" / Int64ul,
        "ProcessId" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("ea8cd8a5-78ff-4418-b292-aadc6a7181df"), event_id=1019, version=0)
class Microsoft_Windows_SecurityMitigationsBroker_1019_0(Etw):
    pattern = Struct(
        "DriverId1" / Int64ul,
        "DriverId2" / Int64ul,
        "ProcessId" / Int32ul
    )


@declare(guid=guid("ea8cd8a5-78ff-4418-b292-aadc6a7181df"), event_id=1020, version=0)
class Microsoft_Windows_SecurityMitigationsBroker_1020_0(Etw):
    pattern = Struct(
        "DriverId" / Int64ul,
        "ProcessId" / Int32ul
    )


@declare(guid=guid("ea8cd8a5-78ff-4418-b292-aadc6a7181df"), event_id=1021, version=0)
class Microsoft_Windows_SecurityMitigationsBroker_1021_0(Etw):
    pattern = Struct(
        "DriverId" / Int64ul,
        "ProcessId" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("ea8cd8a5-78ff-4418-b292-aadc6a7181df"), event_id=1022, version=0)
class Microsoft_Windows_SecurityMitigationsBroker_1022_0(Etw):
    pattern = Struct(
        "Description" / WString,
        "VendorId" / Int32ul,
        "DeviceId" / Int32ul,
        "DriverId" / Int64ul,
        "ProcessId" / Int32ul
    )


@declare(guid=guid("ea8cd8a5-78ff-4418-b292-aadc6a7181df"), event_id=1023, version=0)
class Microsoft_Windows_SecurityMitigationsBroker_1023_0(Etw):
    pattern = Struct(
        "Description" / WString,
        "VendorId" / Int32ul,
        "DeviceId" / Int32ul,
        "DriverId" / Int64ul,
        "ProcessId" / Int32ul
    )


@declare(guid=guid("ea8cd8a5-78ff-4418-b292-aadc6a7181df"), event_id=1024, version=0)
class Microsoft_Windows_SecurityMitigationsBroker_1024_0(Etw):
    pattern = Struct(
        "DriverId" / Int64ul,
        "ProcessId" / Int32ul
    )


@declare(guid=guid("ea8cd8a5-78ff-4418-b292-aadc6a7181df"), event_id=1025, version=0)
class Microsoft_Windows_SecurityMitigationsBroker_1025_0(Etw):
    pattern = Struct(
        "DriverId" / Int64ul,
        "ProcessId" / Int32ul
    )


@declare(guid=guid("ea8cd8a5-78ff-4418-b292-aadc6a7181df"), event_id=1026, version=0)
class Microsoft_Windows_SecurityMitigationsBroker_1026_0(Etw):
    pattern = Struct(
        "Description" / WString,
        "VendorId" / Int32ul,
        "DeviceId" / Int32ul,
        "DriverId" / Int64ul,
        "ProcessId" / Int32ul
    )


@declare(guid=guid("ea8cd8a5-78ff-4418-b292-aadc6a7181df"), event_id=1027, version=0)
class Microsoft_Windows_SecurityMitigationsBroker_1027_0(Etw):
    pattern = Struct(
        "DriverId" / Int64ul,
        "ProcessId" / Int32ul
    )


@declare(guid=guid("ea8cd8a5-78ff-4418-b292-aadc6a7181df"), event_id=1030, version=0)
class Microsoft_Windows_SecurityMitigationsBroker_1030_0(Etw):
    pattern = Struct(
        "ModuleName" / WString
    )

