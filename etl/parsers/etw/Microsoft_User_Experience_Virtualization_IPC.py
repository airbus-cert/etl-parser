# -*- coding: utf-8 -*-
"""
Microsoft-User Experience Virtualization-IPC
GUID : 21d79db0-8e03-41cd-9589-f3ef7001a92a
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("21d79db0-8e03-41cd-9589-f3ef7001a92a"), event_id=100, version=0)
class Microsoft_User_Experience_Virtualization_IPC_100_0(Etw):
    pattern = Struct(
        "_String1" / WString
    )

