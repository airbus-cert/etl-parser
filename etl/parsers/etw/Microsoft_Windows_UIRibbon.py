# -*- coding: utf-8 -*-
"""
Microsoft-Windows-UIRibbon
GUID : 87d476fe-1a0f-4370-b785-60b028019693
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("87d476fe-1a0f-4370-b785-60b028019693"), event_id=25, version=0)
class Microsoft_Windows_UIRibbon_25_0(Etw):
    pattern = Struct(
        "tcid" / Int32sl,
        "tcidParent" / Int32sl,
        "extraInfo" / Int32sl,
        "actionType" / Int32sl,
        "wasPressed" / Int8ul,
        "gallerySelect" / Int8ul,
        "gallery" / Int32sl
    )

