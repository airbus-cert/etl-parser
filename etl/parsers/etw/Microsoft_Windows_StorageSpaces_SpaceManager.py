# -*- coding: utf-8 -*-
"""
Microsoft-Windows-StorageSpaces-SpaceManager
GUID : 69c8ca7e-1adf-472b-ba4c-a0485986b9f6
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("69c8ca7e-1adf-472b-ba4c-a0485986b9f6"), event_id=100, version=0)
class Microsoft_Windows_StorageSpaces_SpaceManager_100_0(Etw):
    pattern = Struct(
        "Type" / Int32ul,
        "Tag" / Int32ul
    )


@declare(guid=guid("69c8ca7e-1adf-472b-ba4c-a0485986b9f6"), event_id=101, version=0)
class Microsoft_Windows_StorageSpaces_SpaceManager_101_0(Etw):
    pattern = Struct(
        "Type" / Int32ul,
        "Tag" / Int32ul,
        "KernelModeStatus" / Int32ul,
        "UserModeStatus" / Int32ul
    )

