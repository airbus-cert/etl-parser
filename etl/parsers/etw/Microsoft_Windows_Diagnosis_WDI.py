# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Diagnosis-WDI
GUID : e01b1a7c-c5c9-4e67-99a9-5e85acfb2e10
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("e01b1a7c-c5c9-4e67-99a9-5e85acfb2e10"), event_id=140, version=0)
class Microsoft_Windows_Diagnosis_WDI_140_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "FunctionName" / WString,
        "LineNumber" / Int32sl,
        "ErrorMessage" / WString
    )


@declare(guid=guid("e01b1a7c-c5c9-4e67-99a9-5e85acfb2e10"), event_id=5016, version=0)
class Microsoft_Windows_Diagnosis_WDI_5016_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "Line" / Int32ul,
        "Address" / Int64ul,
        "Size" / Int64ul
    )


@declare(guid=guid("e01b1a7c-c5c9-4e67-99a9-5e85acfb2e10"), event_id=5017, version=0)
class Microsoft_Windows_Diagnosis_WDI_5017_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "Line" / Int32ul,
        "Address" / Int64ul
    )

