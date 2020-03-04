# -*- coding: utf-8 -*-
"""
Microsoft-Windows-XWizards
GUID : 777ba8fe-2498-4875-933a-3067de883070
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("777ba8fe-2498-4875-933a-3067de883070"), event_id=81, version=0)
class Microsoft_Windows_XWizards_81_0(Etw):
    pattern = Struct(
        "Caption" / WString,
        "Text" / WString
    )


@declare(guid=guid("777ba8fe-2498-4875-933a-3067de883070"), event_id=82, version=0)
class Microsoft_Windows_XWizards_82_0(Etw):
    pattern = Struct(
        "Caption" / WString,
        "Text" / WString
    )


@declare(guid=guid("777ba8fe-2498-4875-933a-3067de883070"), event_id=83, version=0)
class Microsoft_Windows_XWizards_83_0(Etw):
    pattern = Struct(
        "Caption" / WString,
        "Text" / WString
    )

