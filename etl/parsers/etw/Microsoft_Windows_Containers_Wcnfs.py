# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Containers-Wcnfs
GUID : b99317e5-89b7-4c0d-abd1-6e705f7912dc
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("b99317e5-89b7-4c0d-abd1-6e705f7912dc"), event_id=1, version=0)
class Microsoft_Windows_Containers_Wcnfs_1_0(Etw):
    pattern = Struct(
        "NTStatus" / Int32ul
    )


@declare(guid=guid("b99317e5-89b7-4c0d-abd1-6e705f7912dc"), event_id=3, version=0)
class Microsoft_Windows_Containers_Wcnfs_3_0(Etw):
    pattern = Struct(
        "NTStatus" / Int32ul,
        "VolumeNameLength" / Int16ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength)
    )

