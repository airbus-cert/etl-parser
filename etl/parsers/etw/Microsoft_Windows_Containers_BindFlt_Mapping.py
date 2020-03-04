# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Containers-BindFlt-Mapping
GUID : 8fe0dd83-1368-5786-3a82-f746c6f1dd62
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("8fe0dd83-1368-5786-3a82-f746c6f1dd62"), event_id=1, version=0)
class Microsoft_Windows_Containers_BindFlt_Mapping_1_0(Etw):
    pattern = Struct(
        "SourceLength" / Int16ul,
        "Source" / Bytes(lambda this: this.SourceLength),
        "TargetLength" / Int16ul,
        "Target" / Bytes(lambda this: this.TargetLength)
    )

