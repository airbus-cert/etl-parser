# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Shell-OpenWith
GUID : 11bd2a68-77ff-4991-9658-f451f2eb6ce1
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("11bd2a68-77ff-4991-9658-f451f2eb6ce1"), event_id=103, version=0)
class Microsoft_Windows_Shell_OpenWith_103_0(Etw):
    pattern = Struct(
        "Target" / WString,
        "TargetIsURL" / Int8ul
    )


@declare(guid=guid("11bd2a68-77ff-4991-9658-f451f2eb6ce1"), event_id=104, version=0)
class Microsoft_Windows_Shell_OpenWith_104_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )

