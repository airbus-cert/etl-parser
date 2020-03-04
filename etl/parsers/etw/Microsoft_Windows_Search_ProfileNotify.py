# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Search-ProfileNotify
GUID : fc6f77dd-769a-470e-bcf9-1b6555a118be
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("fc6f77dd-769a-470e-bcf9-1b6555a118be"), event_id=1, version=0)
class Microsoft_Windows_Search_ProfileNotify_1_0(Etw):
    pattern = Struct(
        "User" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("fc6f77dd-769a-470e-bcf9-1b6555a118be"), event_id=2, version=0)
class Microsoft_Windows_Search_ProfileNotify_2_0(Etw):
    pattern = Struct(
        "UserAccount" / WString,
        "ErrorCode" / WString,
        "ErrorMessage" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("fc6f77dd-769a-470e-bcf9-1b6555a118be"), event_id=3, version=0)
class Microsoft_Windows_Search_ProfileNotify_3_0(Etw):
    pattern = Struct(
        "OldUserAccount" / WString,
        "NewUserAccount" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("fc6f77dd-769a-470e-bcf9-1b6555a118be"), event_id=4, version=0)
class Microsoft_Windows_Search_ProfileNotify_4_0(Etw):
    pattern = Struct(
        "OldUserAccount" / WString,
        "NewUserAccount" / WString,
        "ErrorCode" / WString,
        "ErrorMessage" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("fc6f77dd-769a-470e-bcf9-1b6555a118be"), event_id=5, version=0)
class Microsoft_Windows_Search_ProfileNotify_5_0(Etw):
    pattern = Struct(
        "User" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("fc6f77dd-769a-470e-bcf9-1b6555a118be"), event_id=6, version=0)
class Microsoft_Windows_Search_ProfileNotify_6_0(Etw):
    pattern = Struct(
        "UserAccount" / WString,
        "ErrorCode" / WString,
        "ErrorMessage" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )

