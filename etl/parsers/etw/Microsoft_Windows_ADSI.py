# -*- coding: utf-8 -*-
"""
Microsoft-Windows-ADSI
GUID : 7288c9f8-d63c-4932-a345-89d6b060174d
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("7288c9f8-d63c-4932-a345-89d6b060174d"), event_id=1, version=0)
class Microsoft_Windows_ADSI_1_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("7288c9f8-d63c-4932-a345-89d6b060174d"), event_id=2, version=0)
class Microsoft_Windows_ADSI_2_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("7288c9f8-d63c-4932-a345-89d6b060174d"), event_id=3, version=0)
class Microsoft_Windows_ADSI_3_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("7288c9f8-d63c-4932-a345-89d6b060174d"), event_id=4, version=0)
class Microsoft_Windows_ADSI_4_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("7288c9f8-d63c-4932-a345-89d6b060174d"), event_id=5, version=0)
class Microsoft_Windows_ADSI_5_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("7288c9f8-d63c-4932-a345-89d6b060174d"), event_id=6, version=0)
class Microsoft_Windows_ADSI_6_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("7288c9f8-d63c-4932-a345-89d6b060174d"), event_id=7, version=0)
class Microsoft_Windows_ADSI_7_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("7288c9f8-d63c-4932-a345-89d6b060174d"), event_id=8, version=0)
class Microsoft_Windows_ADSI_8_0(Etw):
    pattern = Struct(
        "Message" / WString
    )

