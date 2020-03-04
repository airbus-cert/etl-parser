# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Compat-Appraiser
GUID : 442c11c5-304b-45a4-ae73-dc2194c4e876
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("442c11c5-304b-45a4-ae73-dc2194c4e876"), event_id=1, version=0)
class Microsoft_Windows_Compat_Appraiser_1_0(Etw):
    pattern = Struct(
        "SourceLine" / Int32ul,
        "SourceFile" / CString,
        "FunctionName" / CString,
        "Message" / CString
    )


@declare(guid=guid("442c11c5-304b-45a4-ae73-dc2194c4e876"), event_id=2, version=0)
class Microsoft_Windows_Compat_Appraiser_2_0(Etw):
    pattern = Struct(
        "SourceLine" / Int32ul,
        "SourceFile" / CString,
        "FunctionName" / CString,
        "HResult" / Int32ul,
        "Message" / CString
    )


@declare(guid=guid("442c11c5-304b-45a4-ae73-dc2194c4e876"), event_id=3, version=0)
class Microsoft_Windows_Compat_Appraiser_3_0(Etw):
    pattern = Struct(
        "Message" / CString
    )

