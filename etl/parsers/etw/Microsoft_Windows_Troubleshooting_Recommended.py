# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Troubleshooting-Recommended
GUID : 4969de67-439c-516f-f805-a82a4f905730
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("4969de67-439c-516f-f805-a82a4f905730"), event_id=1, version=0)
class Microsoft_Windows_Troubleshooting_Recommended_1_0(Etw):
    pattern = Struct(
        "Title" / WString,
        "LearnMoreURL" / WString,
        "Type" / WString
    )


@declare(guid=guid("4969de67-439c-516f-f805-a82a4f905730"), event_id=101, version=0)
class Microsoft_Windows_Troubleshooting_Recommended_101_0(Etw):
    pattern = Struct(
        "Title" / WString,
        "LearnMoreURL" / WString,
        "Type" / WString
    )


@declare(guid=guid("4969de67-439c-516f-f805-a82a4f905730"), event_id=102, version=0)
class Microsoft_Windows_Troubleshooting_Recommended_102_0(Etw):
    pattern = Struct(
        "Title" / WString,
        "ErrorCode" / Int32ul,
        "LearnMoreURL" / WString,
        "Type" / WString
    )

