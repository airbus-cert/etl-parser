# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Search-ProtocolHandlers
GUID : dab065a9-620f-45ba-b5d6-d6bb8efedee9
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("dab065a9-620f-45ba-b5d6-d6bb8efedee9"), event_id=58, version=0)
class Microsoft_Windows_Search_ProtocolHandlers_58_0(Etw):
    pattern = Struct(
        "Description" / WString
    )


@declare(guid=guid("dab065a9-620f-45ba-b5d6-d6bb8efedee9"), event_id=62, version=0)
class Microsoft_Windows_Search_ProtocolHandlers_62_0(Etw):
    pattern = Struct(
        "Description" / WString
    )

