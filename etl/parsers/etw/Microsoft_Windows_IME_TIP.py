# -*- coding: utf-8 -*-
"""
Microsoft-Windows-IME-TIP
GUID : bdd4b92e-19ef-4497-9c4a-e10e7fd2e227
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("bdd4b92e-19ef-4497-9c4a-e10e7fd2e227"), event_id=142, version=0)
class Microsoft_Windows_IME_TIP_142_0(Etw):
    pattern = Struct(
        "Duration" / Int32ul,
        "PreviousKey" / Int32ul,
        "CurrentKey" / Int32ul
    )


@declare(guid=guid("bdd4b92e-19ef-4497-9c4a-e10e7fd2e227"), event_id=143, version=0)
class Microsoft_Windows_IME_TIP_143_0(Etw):
    pattern = Struct(
        "Duration" / Int32ul,
        "PreviousKey" / Int32ul,
        "CurrentKey" / Int32ul
    )


@declare(guid=guid("bdd4b92e-19ef-4497-9c4a-e10e7fd2e227"), event_id=144, version=0)
class Microsoft_Windows_IME_TIP_144_0(Etw):
    pattern = Struct(
        "Duration" / Int32ul,
        "PreviousKey" / Int32ul,
        "CurrentKey" / Int32ul
    )


@declare(guid=guid("bdd4b92e-19ef-4497-9c4a-e10e7fd2e227"), event_id=145, version=0)
class Microsoft_Windows_IME_TIP_145_0(Etw):
    pattern = Struct(
        "Duration" / Int32ul,
        "PreviousKey" / Int32ul,
        "CurrentKey" / Int32ul
    )

