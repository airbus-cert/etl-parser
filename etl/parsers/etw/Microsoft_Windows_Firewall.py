# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Firewall
GUID : e595f735-b42a-494b-afcd-b68666945cd3
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("e595f735-b42a-494b-afcd-b68666945cd3"), event_id=6400, version=0)
class Microsoft_Windows_Firewall_6400_0(Etw):
    pattern = Struct(
        "CallerProcessName" / WString,
        "ProcessId" / Int32ul,
        "Publisher" / WString
    )

