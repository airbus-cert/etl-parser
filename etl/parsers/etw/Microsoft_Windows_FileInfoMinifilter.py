# -*- coding: utf-8 -*-
"""
Microsoft-Windows-FileInfoMinifilter
GUID : a319d300-015c-48be-acdb-47746e154751
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("a319d300-015c-48be-acdb-47746e154751"), event_id=1, version=0)
class Microsoft_Windows_FileInfoMinifilter_1_0(Etw):
    pattern = Struct(
        "FileObject" / Int64ul,
        "PathLength" / Int16ul,
        "Path" / Bytes(lambda this: this.PathLength)
    )


@declare(guid=guid("a319d300-015c-48be-acdb-47746e154751"), event_id=2, version=0)
class Microsoft_Windows_FileInfoMinifilter_2_0(Etw):
    pattern = Struct(
        "FileObject" / Int64ul,
        "PathLength" / Int16ul,
        "Path" / Bytes(lambda this: this.PathLength)
    )


@declare(guid=guid("a319d300-015c-48be-acdb-47746e154751"), event_id=3, version=0)
class Microsoft_Windows_FileInfoMinifilter_3_0(Etw):
    pattern = Struct(
        "FileObject" / Int64ul,
        "PathLength" / Int16ul,
        "Path" / Bytes(lambda this: this.PathLength)
    )

