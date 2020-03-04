# -*- coding: utf-8 -*-
"""
Microsoft-Windows-SenseIR
GUID : b6d775ef-1436-4fe6-bad3-9e436319e218
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("b6d775ef-1436-4fe6-bad3-9e436319e218"), event_id=1, version=0)
class Microsoft_Windows_SenseIR_1_0(Etw):
    pattern = Struct(
        "ActionType" / WString,
        "ActionId" / WString
    )


@declare(guid=guid("b6d775ef-1436-4fe6-bad3-9e436319e218"), event_id=2, version=0)
class Microsoft_Windows_SenseIR_2_0(Etw):
    pattern = Struct(
        "ActionType" / WString,
        "ActionId" / WString,
        "HRESULT" / Int64ul
    )


@declare(guid=guid("b6d775ef-1436-4fe6-bad3-9e436319e218"), event_id=3, version=0)
class Microsoft_Windows_SenseIR_3_0(Etw):
    pattern = Struct(
        "ActionType" / WString,
        "ActionId" / WString
    )


@declare(guid=guid("b6d775ef-1436-4fe6-bad3-9e436319e218"), event_id=5, version=0)
class Microsoft_Windows_SenseIR_5_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("b6d775ef-1436-4fe6-bad3-9e436319e218"), event_id=7, version=0)
class Microsoft_Windows_SenseIR_7_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("b6d775ef-1436-4fe6-bad3-9e436319e218"), event_id=8, version=0)
class Microsoft_Windows_SenseIR_8_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("b6d775ef-1436-4fe6-bad3-9e436319e218"), event_id=9, version=0)
class Microsoft_Windows_SenseIR_9_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("b6d775ef-1436-4fe6-bad3-9e436319e218"), event_id=10, version=0)
class Microsoft_Windows_SenseIR_10_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("b6d775ef-1436-4fe6-bad3-9e436319e218"), event_id=11, version=0)
class Microsoft_Windows_SenseIR_11_0(Etw):
    pattern = Struct(
        "ActionType" / WString,
        "ActionId" / WString,
        "HRESULT" / Int64ul
    )


@declare(guid=guid("b6d775ef-1436-4fe6-bad3-9e436319e218"), event_id=12, version=0)
class Microsoft_Windows_SenseIR_12_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("b6d775ef-1436-4fe6-bad3-9e436319e218"), event_id=13, version=0)
class Microsoft_Windows_SenseIR_13_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("b6d775ef-1436-4fe6-bad3-9e436319e218"), event_id=14, version=0)
class Microsoft_Windows_SenseIR_14_0(Etw):
    pattern = Struct(
        "ActionType" / WString,
        "ActionId" / WString
    )


@declare(guid=guid("b6d775ef-1436-4fe6-bad3-9e436319e218"), event_id=15, version=0)
class Microsoft_Windows_SenseIR_15_0(Etw):
    pattern = Struct(
        "ActionType" / WString,
        "ActionId" / WString,
        "ActionPhase" / WString,
        "HRESULT" / Int64ul
    )

