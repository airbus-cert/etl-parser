# -*- coding: utf-8 -*-
"""
Microsoft-Windows-RemoteDesktopServices-SessionServices
GUID : f1394de0-32c7-4a76-a6de-b245e48f4615
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("f1394de0-32c7-4a76-a6de-b245e48f4615"), event_id=1, version=0)
class Microsoft_Windows_RemoteDesktopServices_SessionServices_1_0(Etw):
    pattern = Struct(
        "NumMonitors" / Int32ul
    )


@declare(guid=guid("f1394de0-32c7-4a76-a6de-b245e48f4615"), event_id=2, version=0)
class Microsoft_Windows_RemoteDesktopServices_SessionServices_2_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )

