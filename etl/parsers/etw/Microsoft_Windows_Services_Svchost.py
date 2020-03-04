# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Services-Svchost
GUID : 06184c97-5201-480e-92af-3a3626c5b140
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("06184c97-5201-480e-92af-3a3626c5b140"), event_id=101, version=0)
class Microsoft_Windows_Services_Svchost_101_0(Etw):
    pattern = Struct(
        "ServiceName" / WString
    )


@declare(guid=guid("06184c97-5201-480e-92af-3a3626c5b140"), event_id=102, version=0)
class Microsoft_Windows_Services_Svchost_102_0(Etw):
    pattern = Struct(
        "ServiceName" / WString
    )

