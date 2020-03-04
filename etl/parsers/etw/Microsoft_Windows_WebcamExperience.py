# -*- coding: utf-8 -*-
"""
Microsoft-Windows-WebcamExperience
GUID : 9e12ceb1-e3ff-46ad-a0aa-11738b122d20
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("9e12ceb1-e3ff-46ad-a0aa-11738b122d20"), event_id=111, version=0)
class Microsoft_Windows_WebcamExperience_111_0(Etw):
    pattern = Struct(
        "HR" / Int32ul
    )


@declare(guid=guid("9e12ceb1-e3ff-46ad-a0aa-11738b122d20"), event_id=112, version=0)
class Microsoft_Windows_WebcamExperience_112_0(Etw):
    pattern = Struct(
        "PageMode" / Int32ul
    )


@declare(guid=guid("9e12ceb1-e3ff-46ad-a0aa-11738b122d20"), event_id=113, version=0)
class Microsoft_Windows_WebcamExperience_113_0(Etw):
    pattern = Struct(
        "PageMode" / Int32ul
    )

