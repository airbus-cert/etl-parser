# -*- coding: utf-8 -*-
"""
Microsoft-Windows-AppSruProv
GUID : 0cc157b3-cf07-4fc2-91ee-31ac92e05fe1
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("0cc157b3-cf07-4fc2-91ee-31ac92e05fe1"), event_id=3000, version=0)
class Microsoft_Windows_AppSruProv_3000_0(Etw):
    pattern = Struct(
        "AppId" / WString,
        "UserSid" / Sid,
        "FgCycles" / Int64ul,
        "BgCycles" / Int64ul,
        "FgClockTime" / Int64ul,
        "FgCtxSwitches" / Int32ul,
        "BgCtxSwitches" / Int32ul,
        "FgBytesRead" / Int64ul,
        "FgBytesWritten" / Int64ul,
        "FgNumReadOps" / Int32ul,
        "FgNumWriteOps" / Int32ul,
        "FgNumFlushOps" / Int32ul,
        "BgBytesRead" / Int64ul,
        "BgBytesWritten" / Int64ul,
        "BgNumReadOps" / Int32ul,
        "BgNumWriteOps" / Int32ul,
        "BgNumFlushOps" / Int32ul
    )

