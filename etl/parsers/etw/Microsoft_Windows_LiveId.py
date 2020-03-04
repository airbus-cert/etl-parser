# -*- coding: utf-8 -*-
"""
Microsoft-Windows-LiveId
GUID : 05f02597-fe85-4e67-8542-69567ab8fd4f
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=1006, version=0)
class Microsoft_Windows_LiveId_1006_0(Etw):
    pattern = Struct(
        "Result" / Int32sl
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=1008, version=0)
class Microsoft_Windows_LiveId_1008_0(Etw):
    pattern = Struct(
        "Result" / Int32sl
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=1014, version=0)
class Microsoft_Windows_LiveId_1014_0(Etw):
    pattern = Struct(
        "NoOfTargets" / Int32ul,
        "RequestType" / Int32ul
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=1016, version=0)
class Microsoft_Windows_LiveId_1016_0(Etw):
    pattern = Struct(
        "TicketsCached" / Int8ul,
        "Result" / Int32ul
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=1018, version=0)
class Microsoft_Windows_LiveId_1018_0(Etw):
    pattern = Struct(
        "TicketsCached" / Int8ul,
        "Result" / Int32ul
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=1020, version=0)
class Microsoft_Windows_LiveId_1020_0(Etw):
    pattern = Struct(
        "Result" / Int32sl
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=1021, version=0)
class Microsoft_Windows_LiveId_1021_0(Etw):
    pattern = Struct(
        "RegistryLocation" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=1022, version=0)
class Microsoft_Windows_LiveId_1022_0(Etw):
    pattern = Struct(
        "RegistryLocation" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=2016, version=0)
class Microsoft_Windows_LiveId_2016_0(Etw):
    pattern = Struct(
        "Result" / Int32sl
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=2018, version=0)
class Microsoft_Windows_LiveId_2018_0(Etw):
    pattern = Struct(
        "Result" / Int32sl
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=2020, version=0)
class Microsoft_Windows_LiveId_2020_0(Etw):
    pattern = Struct(
        "Result" / Int32sl
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=2022, version=0)
class Microsoft_Windows_LiveId_2022_0(Etw):
    pattern = Struct(
        "Result" / Int32sl
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=2023, version=0)
class Microsoft_Windows_LiveId_2023_0(Etw):
    pattern = Struct(
        "Operation" / WString,
        "Target" / WString,
        "Result" / Int32ul
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=2024, version=0)
class Microsoft_Windows_LiveId_2024_0(Etw):
    pattern = Struct(
        "Operation" / WString,
        "Details" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=2025, version=0)
class Microsoft_Windows_LiveId_2025_0(Etw):
    pattern = Struct(
        "Operation" / WString,
        "Reason" / WString,
        "Result" / Int32ul
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=2026, version=0)
class Microsoft_Windows_LiveId_2026_0(Etw):
    pattern = Struct(
        "PointType" / WString,
        "AppName" / WString,
        "ModuleName" / WString,
        "ModuleVersion" / WString,
        "FileName" / CString,
        "FunctionName" / CString,
        "LineNumber" / Int32ul,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=2027, version=0)
class Microsoft_Windows_LiveId_2027_0(Etw):
    pattern = Struct(
        "cid" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=2028, version=0)
class Microsoft_Windows_LiveId_2028_0(Etw):
    pattern = Struct(
        "FunctionName" / CString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=3000, version=0)
class Microsoft_Windows_LiveId_3000_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=3001, version=0)
class Microsoft_Windows_LiveId_3001_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=3002, version=0)
class Microsoft_Windows_LiveId_3002_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=3003, version=0)
class Microsoft_Windows_LiveId_3003_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=3004, version=0)
class Microsoft_Windows_LiveId_3004_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / CString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=3005, version=0)
class Microsoft_Windows_LiveId_3005_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / CString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=3006, version=0)
class Microsoft_Windows_LiveId_3006_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / CString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=3007, version=0)
class Microsoft_Windows_LiveId_3007_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / CString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=3008, version=0)
class Microsoft_Windows_LiveId_3008_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "FunctionName" / CString,
        "LineNumber" / Int32ul,
        "description" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=3009, version=0)
class Microsoft_Windows_LiveId_3009_0(Etw):
    pattern = Struct(
        "FunctionName" / CString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=3010, version=0)
class Microsoft_Windows_LiveId_3010_0(Etw):
    pattern = Struct(
        "FunctionName" / CString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=3011, version=0)
class Microsoft_Windows_LiveId_3011_0(Etw):
    pattern = Struct(
        "FunctionName" / CString,
        "Address" / Int64ul
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=3012, version=0)
class Microsoft_Windows_LiveId_3012_0(Etw):
    pattern = Struct(
        "ProcessName" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=3013, version=0)
class Microsoft_Windows_LiveId_3013_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "FunctionName" / CString,
        "LineNumber" / Int32ul,
        "Expression" / CString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=3014, version=0)
class Microsoft_Windows_LiveId_3014_0(Etw):
    pattern = Struct(
        "FunctionName" / CString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=3015, version=0)
class Microsoft_Windows_LiveId_3015_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=3016, version=0)
class Microsoft_Windows_LiveId_3016_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / CString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=4000, version=0)
class Microsoft_Windows_LiveId_4000_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=4001, version=0)
class Microsoft_Windows_LiveId_4001_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=4002, version=0)
class Microsoft_Windows_LiveId_4002_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=4003, version=0)
class Microsoft_Windows_LiveId_4003_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=4004, version=0)
class Microsoft_Windows_LiveId_4004_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / CString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=4005, version=0)
class Microsoft_Windows_LiveId_4005_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / CString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=4006, version=0)
class Microsoft_Windows_LiveId_4006_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / CString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=4007, version=0)
class Microsoft_Windows_LiveId_4007_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / CString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=4008, version=0)
class Microsoft_Windows_LiveId_4008_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "FunctionName" / CString,
        "LineNumber" / Int32ul,
        "description" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=4009, version=0)
class Microsoft_Windows_LiveId_4009_0(Etw):
    pattern = Struct(
        "FunctionName" / CString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=4010, version=0)
class Microsoft_Windows_LiveId_4010_0(Etw):
    pattern = Struct(
        "FunctionName" / CString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=4011, version=0)
class Microsoft_Windows_LiveId_4011_0(Etw):
    pattern = Struct(
        "FunctionName" / CString,
        "Address" / Int64ul
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=4012, version=0)
class Microsoft_Windows_LiveId_4012_0(Etw):
    pattern = Struct(
        "ProcessName" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=4013, version=0)
class Microsoft_Windows_LiveId_4013_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "FunctionName" / CString,
        "LineNumber" / Int32ul,
        "Expression" / CString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=4014, version=0)
class Microsoft_Windows_LiveId_4014_0(Etw):
    pattern = Struct(
        "FunctionName" / CString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=4015, version=0)
class Microsoft_Windows_LiveId_4015_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=4016, version=0)
class Microsoft_Windows_LiveId_4016_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / CString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=5000, version=0)
class Microsoft_Windows_LiveId_5000_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=5001, version=0)
class Microsoft_Windows_LiveId_5001_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=5002, version=0)
class Microsoft_Windows_LiveId_5002_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=5003, version=0)
class Microsoft_Windows_LiveId_5003_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=5004, version=0)
class Microsoft_Windows_LiveId_5004_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / CString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=5005, version=0)
class Microsoft_Windows_LiveId_5005_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / CString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=5006, version=0)
class Microsoft_Windows_LiveId_5006_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / CString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=5007, version=0)
class Microsoft_Windows_LiveId_5007_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / CString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=5008, version=0)
class Microsoft_Windows_LiveId_5008_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "FunctionName" / CString,
        "LineNumber" / Int32ul,
        "description" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=5009, version=0)
class Microsoft_Windows_LiveId_5009_0(Etw):
    pattern = Struct(
        "FunctionName" / CString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=5010, version=0)
class Microsoft_Windows_LiveId_5010_0(Etw):
    pattern = Struct(
        "FunctionName" / CString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=5011, version=0)
class Microsoft_Windows_LiveId_5011_0(Etw):
    pattern = Struct(
        "FunctionName" / CString,
        "Address" / Int64ul
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=5012, version=0)
class Microsoft_Windows_LiveId_5012_0(Etw):
    pattern = Struct(
        "ProcessName" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=5013, version=0)
class Microsoft_Windows_LiveId_5013_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "FunctionName" / CString,
        "LineNumber" / Int32ul,
        "Expression" / CString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=5014, version=0)
class Microsoft_Windows_LiveId_5014_0(Etw):
    pattern = Struct(
        "FunctionName" / CString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=5015, version=0)
class Microsoft_Windows_LiveId_5015_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=5016, version=0)
class Microsoft_Windows_LiveId_5016_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / CString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=6000, version=0)
class Microsoft_Windows_LiveId_6000_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=6001, version=0)
class Microsoft_Windows_LiveId_6001_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=6002, version=0)
class Microsoft_Windows_LiveId_6002_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=6003, version=0)
class Microsoft_Windows_LiveId_6003_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=6004, version=0)
class Microsoft_Windows_LiveId_6004_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / CString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=6005, version=0)
class Microsoft_Windows_LiveId_6005_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / CString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=6006, version=0)
class Microsoft_Windows_LiveId_6006_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / CString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=6007, version=0)
class Microsoft_Windows_LiveId_6007_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / CString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=6008, version=0)
class Microsoft_Windows_LiveId_6008_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "FunctionName" / CString,
        "LineNumber" / Int32ul,
        "description" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=6009, version=0)
class Microsoft_Windows_LiveId_6009_0(Etw):
    pattern = Struct(
        "FunctionName" / CString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=6010, version=0)
class Microsoft_Windows_LiveId_6010_0(Etw):
    pattern = Struct(
        "FunctionName" / CString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=6011, version=0)
class Microsoft_Windows_LiveId_6011_0(Etw):
    pattern = Struct(
        "FunctionName" / CString,
        "Address" / Int64ul
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=6012, version=0)
class Microsoft_Windows_LiveId_6012_0(Etw):
    pattern = Struct(
        "ProcessName" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=6013, version=0)
class Microsoft_Windows_LiveId_6013_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "FunctionName" / CString,
        "LineNumber" / Int32ul,
        "Expression" / CString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=6014, version=0)
class Microsoft_Windows_LiveId_6014_0(Etw):
    pattern = Struct(
        "FunctionName" / CString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=6015, version=0)
class Microsoft_Windows_LiveId_6015_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=6016, version=0)
class Microsoft_Windows_LiveId_6016_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / CString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=6100, version=0)
class Microsoft_Windows_LiveId_6100_0(Etw):
    pattern = Struct(
        "value" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=6101, version=0)
class Microsoft_Windows_LiveId_6101_0(Etw):
    pattern = Struct(
        "TargetName" / WString,
        "ExpiryTime" / Int64ul
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=6102, version=0)
class Microsoft_Windows_LiveId_6102_0(Etw):
    pattern = Struct(
        "value" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=6103, version=0)
class Microsoft_Windows_LiveId_6103_0(Etw):
    pattern = Struct(
        "value" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=6104, version=0)
class Microsoft_Windows_LiveId_6104_0(Etw):
    pattern = Struct(
        "value" / Int32sl
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=6105, version=0)
class Microsoft_Windows_LiveId_6105_0(Etw):
    pattern = Struct(
        "value" / Int32sl
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=6112, version=0)
class Microsoft_Windows_LiveId_6112_0(Etw):
    pattern = Struct(
        "value1" / WString,
        "value2" / CString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=6113, version=0)
class Microsoft_Windows_LiveId_6113_0(Etw):
    pattern = Struct(
        "FunctionName" / CString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=6114, version=0)
class Microsoft_Windows_LiveId_6114_0(Etw):
    pattern = Struct(
        "RequestType" / Int32ul,
        "cid" / CString,
        "ErrorCode" / Int32ul,
        "MachineEnvironment" / CString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=6115, version=0)
class Microsoft_Windows_LiveId_6115_0(Etw):
    pattern = Struct(
        "Value" / CString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=6116, version=0)
class Microsoft_Windows_LiveId_6116_0(Etw):
    pattern = Struct(
        "Value" / CString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=6117, version=0)
class Microsoft_Windows_LiveId_6117_0(Etw):
    pattern = Struct(
        "ResourceURI" / CString,
        "Created" / SystemTime,
        "Expires" / SystemTime,
        "TokenType" / CString,
        "AuthRequired" / Int32sl,
        "RequestStatus" / Int32sl,
        "HasFlowUrl" / Int8ul,
        "HasAuthUrl" / Int8ul,
        "HasEndAuthUrl" / Int8ul
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=7000, version=0)
class Microsoft_Windows_LiveId_7000_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=7001, version=0)
class Microsoft_Windows_LiveId_7001_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=7002, version=0)
class Microsoft_Windows_LiveId_7002_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=7003, version=0)
class Microsoft_Windows_LiveId_7003_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=7004, version=0)
class Microsoft_Windows_LiveId_7004_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / CString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=7005, version=0)
class Microsoft_Windows_LiveId_7005_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / CString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=7006, version=0)
class Microsoft_Windows_LiveId_7006_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / CString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=7007, version=0)
class Microsoft_Windows_LiveId_7007_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / CString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=7008, version=0)
class Microsoft_Windows_LiveId_7008_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "FunctionName" / CString,
        "LineNumber" / Int32ul,
        "description" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=7009, version=0)
class Microsoft_Windows_LiveId_7009_0(Etw):
    pattern = Struct(
        "FunctionName" / CString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=7010, version=0)
class Microsoft_Windows_LiveId_7010_0(Etw):
    pattern = Struct(
        "FunctionName" / CString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=7011, version=0)
class Microsoft_Windows_LiveId_7011_0(Etw):
    pattern = Struct(
        "FunctionName" / CString,
        "Address" / Int64ul
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=7012, version=0)
class Microsoft_Windows_LiveId_7012_0(Etw):
    pattern = Struct(
        "ProcessName" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=7013, version=0)
class Microsoft_Windows_LiveId_7013_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "FunctionName" / CString,
        "LineNumber" / Int32ul,
        "Expression" / CString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=7014, version=0)
class Microsoft_Windows_LiveId_7014_0(Etw):
    pattern = Struct(
        "FunctionName" / CString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=7015, version=0)
class Microsoft_Windows_LiveId_7015_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=7016, version=0)
class Microsoft_Windows_LiveId_7016_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / CString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=7100, version=0)
class Microsoft_Windows_LiveId_7100_0(Etw):
    pattern = Struct(
        "Uri" / WString,
        "Policy" / WString,
        "TimeToLive" / Int32ul
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=7101, version=0)
class Microsoft_Windows_LiveId_7101_0(Etw):
    pattern = Struct(
        "value1" / WString,
        "value2" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=7102, version=0)
class Microsoft_Windows_LiveId_7102_0(Etw):
    pattern = Struct(
        "value" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=7103, version=0)
class Microsoft_Windows_LiveId_7103_0(Etw):
    pattern = Struct(
        "value1" / WString,
        "value2" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=7104, version=0)
class Microsoft_Windows_LiveId_7104_0(Etw):
    pattern = Struct(
        "Attempts" / Int32ul,
        "latestIterationResult" / Int32ul,
        "continueRetry" / Int8ul,
        "isConnected" / Int8ul,
        "flowUrl" / WString,
        "defaultUser" / WString,
        "promptType" / Int32ul,
        "authUrl" / WString,
        "endAuthUrl" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=7105, version=0)
class Microsoft_Windows_LiveId_7105_0(Etw):
    pattern = Struct(
        "value" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=8000, version=0)
class Microsoft_Windows_LiveId_8000_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=8001, version=0)
class Microsoft_Windows_LiveId_8001_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=8002, version=0)
class Microsoft_Windows_LiveId_8002_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=8003, version=0)
class Microsoft_Windows_LiveId_8003_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=8004, version=0)
class Microsoft_Windows_LiveId_8004_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / CString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=8005, version=0)
class Microsoft_Windows_LiveId_8005_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / CString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=8006, version=0)
class Microsoft_Windows_LiveId_8006_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / CString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=8007, version=0)
class Microsoft_Windows_LiveId_8007_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / CString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=8008, version=0)
class Microsoft_Windows_LiveId_8008_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "FunctionName" / CString,
        "LineNumber" / Int32ul,
        "description" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=8009, version=0)
class Microsoft_Windows_LiveId_8009_0(Etw):
    pattern = Struct(
        "FunctionName" / CString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=8010, version=0)
class Microsoft_Windows_LiveId_8010_0(Etw):
    pattern = Struct(
        "FunctionName" / CString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=8011, version=0)
class Microsoft_Windows_LiveId_8011_0(Etw):
    pattern = Struct(
        "FunctionName" / CString,
        "Address" / Int64ul
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=8012, version=0)
class Microsoft_Windows_LiveId_8012_0(Etw):
    pattern = Struct(
        "ProcessName" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=8013, version=0)
class Microsoft_Windows_LiveId_8013_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "FunctionName" / CString,
        "LineNumber" / Int32ul,
        "Expression" / CString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=8014, version=0)
class Microsoft_Windows_LiveId_8014_0(Etw):
    pattern = Struct(
        "FunctionName" / CString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=8015, version=0)
class Microsoft_Windows_LiveId_8015_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=8016, version=0)
class Microsoft_Windows_LiveId_8016_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / CString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=9000, version=0)
class Microsoft_Windows_LiveId_9000_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=9001, version=0)
class Microsoft_Windows_LiveId_9001_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=9002, version=0)
class Microsoft_Windows_LiveId_9002_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=9003, version=0)
class Microsoft_Windows_LiveId_9003_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=9004, version=0)
class Microsoft_Windows_LiveId_9004_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / CString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=9005, version=0)
class Microsoft_Windows_LiveId_9005_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / CString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=9006, version=0)
class Microsoft_Windows_LiveId_9006_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / CString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=9007, version=0)
class Microsoft_Windows_LiveId_9007_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / CString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=9008, version=0)
class Microsoft_Windows_LiveId_9008_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "FunctionName" / CString,
        "LineNumber" / Int32ul,
        "description" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=9009, version=0)
class Microsoft_Windows_LiveId_9009_0(Etw):
    pattern = Struct(
        "FunctionName" / CString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=9010, version=0)
class Microsoft_Windows_LiveId_9010_0(Etw):
    pattern = Struct(
        "FunctionName" / CString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=9011, version=0)
class Microsoft_Windows_LiveId_9011_0(Etw):
    pattern = Struct(
        "FunctionName" / CString,
        "Address" / Int64ul
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=9012, version=0)
class Microsoft_Windows_LiveId_9012_0(Etw):
    pattern = Struct(
        "ProcessName" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=9013, version=0)
class Microsoft_Windows_LiveId_9013_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "FunctionName" / CString,
        "LineNumber" / Int32ul,
        "Expression" / CString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=9014, version=0)
class Microsoft_Windows_LiveId_9014_0(Etw):
    pattern = Struct(
        "FunctionName" / CString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=9015, version=0)
class Microsoft_Windows_LiveId_9015_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=9016, version=0)
class Microsoft_Windows_LiveId_9016_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / CString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=9100, version=0)
class Microsoft_Windows_LiveId_9100_0(Etw):
    pattern = Struct(
        "value" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=10000, version=0)
class Microsoft_Windows_LiveId_10000_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=10001, version=0)
class Microsoft_Windows_LiveId_10001_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=10002, version=0)
class Microsoft_Windows_LiveId_10002_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=10003, version=0)
class Microsoft_Windows_LiveId_10003_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=10004, version=0)
class Microsoft_Windows_LiveId_10004_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / CString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=10005, version=0)
class Microsoft_Windows_LiveId_10005_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / CString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=10006, version=0)
class Microsoft_Windows_LiveId_10006_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / CString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=10007, version=0)
class Microsoft_Windows_LiveId_10007_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / CString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=10008, version=0)
class Microsoft_Windows_LiveId_10008_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "FunctionName" / CString,
        "LineNumber" / Int32ul,
        "description" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=10009, version=0)
class Microsoft_Windows_LiveId_10009_0(Etw):
    pattern = Struct(
        "FunctionName" / CString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=10010, version=0)
class Microsoft_Windows_LiveId_10010_0(Etw):
    pattern = Struct(
        "FunctionName" / CString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=10011, version=0)
class Microsoft_Windows_LiveId_10011_0(Etw):
    pattern = Struct(
        "FunctionName" / CString,
        "Address" / Int64ul
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=10012, version=0)
class Microsoft_Windows_LiveId_10012_0(Etw):
    pattern = Struct(
        "ProcessName" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=10013, version=0)
class Microsoft_Windows_LiveId_10013_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "FunctionName" / CString,
        "LineNumber" / Int32ul,
        "Expression" / CString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=10014, version=0)
class Microsoft_Windows_LiveId_10014_0(Etw):
    pattern = Struct(
        "FunctionName" / CString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=10015, version=0)
class Microsoft_Windows_LiveId_10015_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=10016, version=0)
class Microsoft_Windows_LiveId_10016_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / CString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=11000, version=0)
class Microsoft_Windows_LiveId_11000_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=11001, version=0)
class Microsoft_Windows_LiveId_11001_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=11002, version=0)
class Microsoft_Windows_LiveId_11002_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=11003, version=0)
class Microsoft_Windows_LiveId_11003_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=11004, version=0)
class Microsoft_Windows_LiveId_11004_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / CString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=11005, version=0)
class Microsoft_Windows_LiveId_11005_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / CString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=11006, version=0)
class Microsoft_Windows_LiveId_11006_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / CString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=11007, version=0)
class Microsoft_Windows_LiveId_11007_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / CString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=11008, version=0)
class Microsoft_Windows_LiveId_11008_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "FunctionName" / CString,
        "LineNumber" / Int32ul,
        "description" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=11009, version=0)
class Microsoft_Windows_LiveId_11009_0(Etw):
    pattern = Struct(
        "FunctionName" / CString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=11010, version=0)
class Microsoft_Windows_LiveId_11010_0(Etw):
    pattern = Struct(
        "FunctionName" / CString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=11011, version=0)
class Microsoft_Windows_LiveId_11011_0(Etw):
    pattern = Struct(
        "FunctionName" / CString,
        "Address" / Int64ul
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=11012, version=0)
class Microsoft_Windows_LiveId_11012_0(Etw):
    pattern = Struct(
        "ProcessName" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=11013, version=0)
class Microsoft_Windows_LiveId_11013_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "FunctionName" / CString,
        "LineNumber" / Int32ul,
        "Expression" / CString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=11014, version=0)
class Microsoft_Windows_LiveId_11014_0(Etw):
    pattern = Struct(
        "FunctionName" / CString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=11015, version=0)
class Microsoft_Windows_LiveId_11015_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=11016, version=0)
class Microsoft_Windows_LiveId_11016_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / CString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=12000, version=0)
class Microsoft_Windows_LiveId_12000_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=12001, version=0)
class Microsoft_Windows_LiveId_12001_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=12002, version=0)
class Microsoft_Windows_LiveId_12002_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=12003, version=0)
class Microsoft_Windows_LiveId_12003_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=12004, version=0)
class Microsoft_Windows_LiveId_12004_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / CString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=12005, version=0)
class Microsoft_Windows_LiveId_12005_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / CString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=12006, version=0)
class Microsoft_Windows_LiveId_12006_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / CString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=12007, version=0)
class Microsoft_Windows_LiveId_12007_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / CString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=12008, version=0)
class Microsoft_Windows_LiveId_12008_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "FunctionName" / CString,
        "LineNumber" / Int32ul,
        "description" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=12009, version=0)
class Microsoft_Windows_LiveId_12009_0(Etw):
    pattern = Struct(
        "FunctionName" / CString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=12010, version=0)
class Microsoft_Windows_LiveId_12010_0(Etw):
    pattern = Struct(
        "FunctionName" / CString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=12011, version=0)
class Microsoft_Windows_LiveId_12011_0(Etw):
    pattern = Struct(
        "FunctionName" / CString,
        "Address" / Int64ul
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=12012, version=0)
class Microsoft_Windows_LiveId_12012_0(Etw):
    pattern = Struct(
        "ProcessName" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=12013, version=0)
class Microsoft_Windows_LiveId_12013_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "FunctionName" / CString,
        "LineNumber" / Int32ul,
        "Expression" / CString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=12014, version=0)
class Microsoft_Windows_LiveId_12014_0(Etw):
    pattern = Struct(
        "FunctionName" / CString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=12015, version=0)
class Microsoft_Windows_LiveId_12015_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / WString
    )


@declare(guid=guid("05f02597-fe85-4e67-8542-69567ab8fd4f"), event_id=12016, version=0)
class Microsoft_Windows_LiveId_12016_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "LineNumber" / Int32ul,
        "description" / CString
    )

