# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Containers-Wcifs
GUID : aec5c129-7c10-407d-be97-91a042c61aaa
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("aec5c129-7c10-407d-be97-91a042c61aaa"), event_id=1, version=0)
class Microsoft_Windows_Containers_Wcifs_1_0(Etw):
    pattern = Struct(
        "NTStatus" / Int32ul
    )


@declare(guid=guid("aec5c129-7c10-407d-be97-91a042c61aaa"), event_id=3, version=0)
class Microsoft_Windows_Containers_Wcifs_3_0(Etw):
    pattern = Struct(
        "NTStatus" / Int32ul,
        "VolumeNameLength" / Int16ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength)
    )

