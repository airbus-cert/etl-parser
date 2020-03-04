# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Services
GUID : 0063715b-eeda-4007-9429-ad526f62696e
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("0063715b-eeda-4007-9429-ad526f62696e"), event_id=103, version=0)
class Microsoft_Windows_Services_103_0(Etw):
    pattern = Struct(
        "GroupName" / WString
    )


@declare(guid=guid("0063715b-eeda-4007-9429-ad526f62696e"), event_id=104, version=0)
class Microsoft_Windows_Services_104_0(Etw):
    pattern = Struct(
        "GroupName" / WString
    )


@declare(guid=guid("0063715b-eeda-4007-9429-ad526f62696e"), event_id=105, version=0)
class Microsoft_Windows_Services_105_0(Etw):
    pattern = Struct(
        "ExecutionPhase" / Int32ul,
        "CurrentState" / Int32ul,
        "StartType" / Int32ul,
        "PID" / Int32ul,
        "ServiceName" / WString,
        "ImageName" / WString
    )

