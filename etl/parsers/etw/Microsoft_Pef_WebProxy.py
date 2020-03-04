# -*- coding: utf-8 -*-
"""
Microsoft-Pef-WebProxy
GUID : 6ef4653a-71f9-4ad3-b093-61c38c9c299f
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("6ef4653a-71f9-4ad3-b093-61c38c9c299f"), event_id=1001, version=0)
class Microsoft_Pef_WebProxy_1001_0(Etw):
    pattern = Struct(
        "SessionID" / Int32ul,
        "AccurateTimeStamp" / Int64ul,
        "OneIfRequest" / Int32ul,
        "PayloadLength" / Int32ul,
        "Payload" / Bytes(lambda this: this.PayloadLength)
    )


@declare(guid=guid("6ef4653a-71f9-4ad3-b093-61c38c9c299f"), event_id=2000, version=0)
class Microsoft_Pef_WebProxy_2000_0(Etw):
    pattern = Struct(
        "ReassembledEventID" / Int16ul,
        "FragmentLength" / Int32ul,
        "Fragment" / Bytes(lambda this: this.FragmentLength)
    )

