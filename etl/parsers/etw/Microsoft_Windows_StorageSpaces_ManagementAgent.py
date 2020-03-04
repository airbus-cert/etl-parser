# -*- coding: utf-8 -*-
"""
Microsoft-Windows-StorageSpaces-ManagementAgent
GUID : aa4c798d-d91b-4b07-a013-787f5803d6fc
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("aa4c798d-d91b-4b07-a013-787f5803d6fc"), event_id=100, version=0)
class Microsoft_Windows_StorageSpaces_ManagementAgent_100_0(Etw):
    pattern = Struct(
        "hc_stateid" / Int32ul
    )

