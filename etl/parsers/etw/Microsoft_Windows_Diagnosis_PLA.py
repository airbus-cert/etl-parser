# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Diagnosis-PLA
GUID : e4d53f84-7de3-11d8-9435-505054503030
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("e4d53f84-7de3-11d8-9435-505054503030"), event_id=1000, version=0)
class Microsoft_Windows_Diagnosis_PLA_1000_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "User" / WString
    )


@declare(guid=guid("e4d53f84-7de3-11d8-9435-505054503030"), event_id=1001, version=0)
class Microsoft_Windows_Diagnosis_PLA_1001_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "User" / WString
    )


@declare(guid=guid("e4d53f84-7de3-11d8-9435-505054503030"), event_id=1002, version=0)
class Microsoft_Windows_Diagnosis_PLA_1002_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "User" / WString
    )


@declare(guid=guid("e4d53f84-7de3-11d8-9435-505054503030"), event_id=1003, version=0)
class Microsoft_Windows_Diagnosis_PLA_1003_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Key" / WString,
        "User" / WString
    )


@declare(guid=guid("e4d53f84-7de3-11d8-9435-505054503030"), event_id=1004, version=0)
class Microsoft_Windows_Diagnosis_PLA_1004_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Key" / WString,
        "User" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("e4d53f84-7de3-11d8-9435-505054503030"), event_id=1005, version=0)
class Microsoft_Windows_Diagnosis_PLA_1005_0(Etw):
    pattern = Struct(
        "Name" / WString
    )


@declare(guid=guid("e4d53f84-7de3-11d8-9435-505054503030"), event_id=1006, version=0)
class Microsoft_Windows_Diagnosis_PLA_1006_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("e4d53f84-7de3-11d8-9435-505054503030"), event_id=1007, version=0)
class Microsoft_Windows_Diagnosis_PLA_1007_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "TaskName" / WString
    )


@declare(guid=guid("e4d53f84-7de3-11d8-9435-505054503030"), event_id=1008, version=0)
class Microsoft_Windows_Diagnosis_PLA_1008_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "TaskName" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("e4d53f84-7de3-11d8-9435-505054503030"), event_id=1009, version=0)
class Microsoft_Windows_Diagnosis_PLA_1009_0(Etw):
    pattern = Struct(
        "Error" / Int32ul
    )


@declare(guid=guid("e4d53f84-7de3-11d8-9435-505054503030"), event_id=1010, version=0)
class Microsoft_Windows_Diagnosis_PLA_1010_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "CounterName" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("e4d53f84-7de3-11d8-9435-505054503030"), event_id=1011, version=0)
class Microsoft_Windows_Diagnosis_PLA_1011_0(Etw):
    pattern = Struct(
        "DataCollecotrSet" / WString,
        "Name" / WString
    )


@declare(guid=guid("e4d53f84-7de3-11d8-9435-505054503030"), event_id=1012, version=0)
class Microsoft_Windows_Diagnosis_PLA_1012_0(Etw):
    pattern = Struct(
        "Name" / WString
    )


@declare(guid=guid("e4d53f84-7de3-11d8-9435-505054503030"), event_id=1013, version=0)
class Microsoft_Windows_Diagnosis_PLA_1013_0(Etw):
    pattern = Struct(
        "Name" / WString
    )


@declare(guid=guid("e4d53f84-7de3-11d8-9435-505054503030"), event_id=1014, version=0)
class Microsoft_Windows_Diagnosis_PLA_1014_0(Etw):
    pattern = Struct(
        "DataCollecotrSet" / WString,
        "Name" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("e4d53f84-7de3-11d8-9435-505054503030"), event_id=1015, version=0)
class Microsoft_Windows_Diagnosis_PLA_1015_0(Etw):
    pattern = Struct(
        "DataCollecotrSet" / WString,
        "Name" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("e4d53f84-7de3-11d8-9435-505054503030"), event_id=1016, version=0)
class Microsoft_Windows_Diagnosis_PLA_1016_0(Etw):
    pattern = Struct(
        "DataCollecotrSet" / WString,
        "Name" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("e4d53f84-7de3-11d8-9435-505054503030"), event_id=1017, version=0)
class Microsoft_Windows_Diagnosis_PLA_1017_0(Etw):
    pattern = Struct(
        "ServerName" / WString,
        "CabName" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("e4d53f84-7de3-11d8-9435-505054503030"), event_id=2031, version=0)
class Microsoft_Windows_Diagnosis_PLA_2031_0(Etw):
    pattern = Struct(
        "Counter" / WString,
        "Value" / WString,
        "Operator" / WString,
        "Threshold" / WString,
        "Message" / WString
    )


@declare(guid=guid("e4d53f84-7de3-11d8-9435-505054503030"), event_id=3000, version=0)
class Microsoft_Windows_Diagnosis_PLA_3000_0(Etw):
    pattern = Struct(
        "ReportFileName" / WString,
        "Description" / WString
    )


@declare(guid=guid("e4d53f84-7de3-11d8-9435-505054503030"), event_id=3001, version=0)
class Microsoft_Windows_Diagnosis_PLA_3001_0(Etw):
    pattern = Struct(
        "ReportFileName" / WString,
        "Description" / WString
    )


@declare(guid=guid("e4d53f84-7de3-11d8-9435-505054503030"), event_id=3002, version=0)
class Microsoft_Windows_Diagnosis_PLA_3002_0(Etw):
    pattern = Struct(
        "ReportFileName" / WString,
        "Description" / WString
    )


@declare(guid=guid("e4d53f84-7de3-11d8-9435-505054503030"), event_id=5001, version=0)
class Microsoft_Windows_Diagnosis_PLA_5001_0(Etw):
    pattern = Struct(
        "BuildNumber" / Int32ul,
        "BuildType" / CString
    )


@declare(guid=guid("e4d53f84-7de3-11d8-9435-505054503030"), event_id=5002, version=0)
class Microsoft_Windows_Diagnosis_PLA_5002_0(Etw):
    pattern = Struct(
        "BuildNumber" / Int32ul,
        "BuildType" / CString
    )


@declare(guid=guid("e4d53f84-7de3-11d8-9435-505054503030"), event_id=5003, version=0)
class Microsoft_Windows_Diagnosis_PLA_5003_0(Etw):
    pattern = Struct(
        "Reason" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("e4d53f84-7de3-11d8-9435-505054503030"), event_id=5004, version=0)
class Microsoft_Windows_Diagnosis_PLA_5004_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "FileName" / WString
    )


@declare(guid=guid("e4d53f84-7de3-11d8-9435-505054503030"), event_id=5005, version=0)
class Microsoft_Windows_Diagnosis_PLA_5005_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "SerialNumber" / Int32ul
    )


@declare(guid=guid("e4d53f84-7de3-11d8-9435-505054503030"), event_id=5006, version=0)
class Microsoft_Windows_Diagnosis_PLA_5006_0(Etw):
    pattern = Struct(
        "Name" / WString
    )


@declare(guid=guid("e4d53f84-7de3-11d8-9435-505054503030"), event_id=5007, version=0)
class Microsoft_Windows_Diagnosis_PLA_5007_0(Etw):
    pattern = Struct(
        "Name" / WString
    )


@declare(guid=guid("e4d53f84-7de3-11d8-9435-505054503030"), event_id=5008, version=0)
class Microsoft_Windows_Diagnosis_PLA_5008_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "SerialNumber" / Int32ul
    )


@declare(guid=guid("e4d53f84-7de3-11d8-9435-505054503030"), event_id=5009, version=0)
class Microsoft_Windows_Diagnosis_PLA_5009_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Index" / Int32ul
    )


@declare(guid=guid("e4d53f84-7de3-11d8-9435-505054503030"), event_id=5010, version=0)
class Microsoft_Windows_Diagnosis_PLA_5010_0(Etw):
    pattern = Struct(
        "Name" / WString
    )


@declare(guid=guid("e4d53f84-7de3-11d8-9435-505054503030"), event_id=5011, version=0)
class Microsoft_Windows_Diagnosis_PLA_5011_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "FileName" / WString
    )


@declare(guid=guid("e4d53f84-7de3-11d8-9435-505054503030"), event_id=5012, version=0)
class Microsoft_Windows_Diagnosis_PLA_5012_0(Etw):
    pattern = Struct(
        "Name" / WString
    )


@declare(guid=guid("e4d53f84-7de3-11d8-9435-505054503030"), event_id=5013, version=0)
class Microsoft_Windows_Diagnosis_PLA_5013_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "FileName" / CString,
        "Line" / Int32ul
    )


@declare(guid=guid("e4d53f84-7de3-11d8-9435-505054503030"), event_id=5014, version=0)
class Microsoft_Windows_Diagnosis_PLA_5014_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "Line" / Int32ul,
        "Address" / Int64ul,
        "Size" / Int64ul
    )


@declare(guid=guid("e4d53f84-7de3-11d8-9435-505054503030"), event_id=5015, version=0)
class Microsoft_Windows_Diagnosis_PLA_5015_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "Line" / Int32ul,
        "Address" / Int64ul
    )


@declare(guid=guid("e4d53f84-7de3-11d8-9435-505054503030"), event_id=5016, version=0)
class Microsoft_Windows_Diagnosis_PLA_5016_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "Line" / Int32ul,
        "Address" / Int64ul,
        "Size" / Int64ul
    )


@declare(guid=guid("e4d53f84-7de3-11d8-9435-505054503030"), event_id=5017, version=0)
class Microsoft_Windows_Diagnosis_PLA_5017_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "Line" / Int32ul,
        "Address" / Int64ul
    )


@declare(guid=guid("e4d53f84-7de3-11d8-9435-505054503030"), event_id=5018, version=0)
class Microsoft_Windows_Diagnosis_PLA_5018_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "Line" / Int32ul,
        "Address" / Int64ul,
        "Size" / Int64ul,
        "OrigAddress" / Int64ul
    )


@declare(guid=guid("e4d53f84-7de3-11d8-9435-505054503030"), event_id=5019, version=0)
class Microsoft_Windows_Diagnosis_PLA_5019_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "Line" / Int32ul,
        "Address" / Int64ul,
        "Size" / Int64ul
    )


@declare(guid=guid("e4d53f84-7de3-11d8-9435-505054503030"), event_id=5020, version=0)
class Microsoft_Windows_Diagnosis_PLA_5020_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "Line" / Int32ul,
        "Address" / Int64ul
    )


@declare(guid=guid("e4d53f84-7de3-11d8-9435-505054503030"), event_id=5021, version=0)
class Microsoft_Windows_Diagnosis_PLA_5021_0(Etw):
    pattern = Struct(
        "Name" / CString,
        "Address" / Int64ul
    )


@declare(guid=guid("e4d53f84-7de3-11d8-9435-505054503030"), event_id=5022, version=0)
class Microsoft_Windows_Diagnosis_PLA_5022_0(Etw):
    pattern = Struct(
        "Name" / CString,
        "Address" / Int64ul
    )


@declare(guid=guid("e4d53f84-7de3-11d8-9435-505054503030"), event_id=5023, version=0)
class Microsoft_Windows_Diagnosis_PLA_5023_0(Etw):
    pattern = Struct(
        "Name" / CString,
        "Address" / Int64ul,
        "RefCount" / Int32ul
    )


@declare(guid=guid("e4d53f84-7de3-11d8-9435-505054503030"), event_id=5024, version=0)
class Microsoft_Windows_Diagnosis_PLA_5024_0(Etw):
    pattern = Struct(
        "Name" / CString,
        "Address" / Int64ul,
        "RefCount" / Int32ul
    )


@declare(guid=guid("e4d53f84-7de3-11d8-9435-505054503030"), event_id=5025, version=0)
class Microsoft_Windows_Diagnosis_PLA_5025_0(Etw):
    pattern = Struct(
        "Name" / CString,
        "Address" / Int64ul,
        "RefCount" / Int32ul
    )


@declare(guid=guid("e4d53f84-7de3-11d8-9435-505054503030"), event_id=5026, version=0)
class Microsoft_Windows_Diagnosis_PLA_5026_0(Etw):
    pattern = Struct(
        "Error" / Int32ul,
        "FileName" / CString,
        "Line" / Int32ul,
        "Function" / CString,
        "User" / WString
    )

