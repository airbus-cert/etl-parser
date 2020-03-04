# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Containers-Wcifs-Mapping
GUID : 0223f0a3-6383-5a7a-7bc7-04d4739e2e32
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("0223f0a3-6383-5a7a-7bc7-04d4739e2e32"), event_id=1, version=0)
class Microsoft_Windows_Containers_Wcifs_Mapping_1_0(Etw):
    pattern = Struct(
        "SourceLength" / Int16ul,
        "Source" / Bytes(lambda this: this.SourceLength),
        "TargetLength" / Int16ul,
        "Target" / Bytes(lambda this: this.TargetLength)
    )

