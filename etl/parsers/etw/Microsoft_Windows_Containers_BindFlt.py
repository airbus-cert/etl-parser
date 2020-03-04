# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Containers-BindFlt
GUID : fc4e8f51-7a04-4bab-8b91-6321416f72ab
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("fc4e8f51-7a04-4bab-8b91-6321416f72ab"), event_id=1, version=0)
class Microsoft_Windows_Containers_BindFlt_1_0(Etw):
    pattern = Struct(
        "NTStatus" / Int32ul
    )


@declare(guid=guid("fc4e8f51-7a04-4bab-8b91-6321416f72ab"), event_id=3, version=0)
class Microsoft_Windows_Containers_BindFlt_3_0(Etw):
    pattern = Struct(
        "NTStatus" / Int32ul,
        "VolumeNameLength" / Int16ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength)
    )

