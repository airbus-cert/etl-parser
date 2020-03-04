# -*- coding: utf-8 -*-
"""
Microsoft-Windows-RemoteDesktopServices-RemoteFX-Synth3dvsc
GUID : 3903d5b9-988d-4c31-9ccd-4022f96703f0
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("3903d5b9-988d-4c31-9ccd-4022f96703f0"), event_id=4, version=0)
class Microsoft_Windows_RemoteDesktopServices_RemoteFX_Synth3dvsc_4_0(Etw):
    pattern = Struct(
        "MajorVersion" / Int8ul,
        "MinorVersion" / Int8ul
    )

