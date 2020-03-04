# -*- coding: utf-8 -*-
"""
Microsoft-Windows-WindowsToGo-StartupOptions
GUID : 2e6cb42e-161d-413b-a6c1-84ca4c1e5890
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("2e6cb42e-161d-413b-a6c1-84ca4c1e5890"), event_id=8193, version=0)
class Microsoft_Windows_WindowsToGo_StartupOptions_8193_0(Etw):
    pattern = Struct(
        "State" / Int32ul
    )


@declare(guid=guid("2e6cb42e-161d-413b-a6c1-84ca4c1e5890"), event_id=8194, version=0)
class Microsoft_Windows_WindowsToGo_StartupOptions_8194_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )

