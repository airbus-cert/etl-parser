# -*- coding: utf-8 -*-
"""
Microsoft-Windows-DCLocator
GUID : cfaa5446-c6c4-4f5c-866f-31c9b55b962d
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("cfaa5446-c6c4-4f5c-866f-31c9b55b962d"), event_id=1, version=0)
class Microsoft_Windows_DCLocator_1_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("cfaa5446-c6c4-4f5c-866f-31c9b55b962d"), event_id=2, version=0)
class Microsoft_Windows_DCLocator_2_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("cfaa5446-c6c4-4f5c-866f-31c9b55b962d"), event_id=3, version=0)
class Microsoft_Windows_DCLocator_3_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("cfaa5446-c6c4-4f5c-866f-31c9b55b962d"), event_id=4, version=0)
class Microsoft_Windows_DCLocator_4_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("cfaa5446-c6c4-4f5c-866f-31c9b55b962d"), event_id=5, version=0)
class Microsoft_Windows_DCLocator_5_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("cfaa5446-c6c4-4f5c-866f-31c9b55b962d"), event_id=6, version=0)
class Microsoft_Windows_DCLocator_6_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("cfaa5446-c6c4-4f5c-866f-31c9b55b962d"), event_id=7, version=0)
class Microsoft_Windows_DCLocator_7_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("cfaa5446-c6c4-4f5c-866f-31c9b55b962d"), event_id=8, version=0)
class Microsoft_Windows_DCLocator_8_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("cfaa5446-c6c4-4f5c-866f-31c9b55b962d"), event_id=9, version=0)
class Microsoft_Windows_DCLocator_9_0(Etw):
    pattern = Struct(
        "Message" / WString
    )

