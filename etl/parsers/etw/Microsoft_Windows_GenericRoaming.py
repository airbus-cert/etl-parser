# -*- coding: utf-8 -*-
"""
Microsoft-Windows-GenericRoaming
GUID : 4eacb4d0-263b-4b93-8cd6-778a278e5642
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("4eacb4d0-263b-4b93-8cd6-778a278e5642"), event_id=3, version=0)
class Microsoft_Windows_GenericRoaming_3_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "UnitId" / WString,
        "HResultFailure" / Int32sl
    )


@declare(guid=guid("4eacb4d0-263b-4b93-8cd6-778a278e5642"), event_id=4, version=0)
class Microsoft_Windows_GenericRoaming_4_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "UnitId" / WString,
        "HResultFailure" / Int32sl
    )


@declare(guid=guid("4eacb4d0-263b-4b93-8cd6-778a278e5642"), event_id=5, version=0)
class Microsoft_Windows_GenericRoaming_5_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "UnitId" / WString,
        "HResultFailure" / Int32sl
    )


@declare(guid=guid("4eacb4d0-263b-4b93-8cd6-778a278e5642"), event_id=6, version=0)
class Microsoft_Windows_GenericRoaming_6_0(Etw):
    pattern = Struct(
        "CollectionId" / WString,
        "HResultFailure" / Int32sl
    )


@declare(guid=guid("4eacb4d0-263b-4b93-8cd6-778a278e5642"), event_id=7, version=0)
class Microsoft_Windows_GenericRoaming_7_0(Etw):
    pattern = Struct(
        "Username" / WString,
        "HResultFailure" / Int32sl
    )

