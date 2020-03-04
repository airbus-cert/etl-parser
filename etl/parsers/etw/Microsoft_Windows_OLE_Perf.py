# -*- coding: utf-8 -*-
"""
Microsoft-Windows-OLE-Perf
GUID : 84958368-7da7-49a0-b33d-07fabb879626
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("84958368-7da7-49a0-b33d-07fabb879626"), event_id=10, version=0)
class Microsoft_Windows_OLE_Perf_10_0(Etw):
    pattern = Struct(
        "HResult" / Int32sl
    )


@declare(guid=guid("84958368-7da7-49a0-b33d-07fabb879626"), event_id=12, version=0)
class Microsoft_Windows_OLE_Perf_12_0(Etw):
    pattern = Struct(
        "HResult" / Int32sl
    )


@declare(guid=guid("84958368-7da7-49a0-b33d-07fabb879626"), event_id=14, version=0)
class Microsoft_Windows_OLE_Perf_14_0(Etw):
    pattern = Struct(
        "HResult" / Int32sl
    )


@declare(guid=guid("84958368-7da7-49a0-b33d-07fabb879626"), event_id=16, version=0)
class Microsoft_Windows_OLE_Perf_16_0(Etw):
    pattern = Struct(
        "HResult" / Int32sl
    )


@declare(guid=guid("84958368-7da7-49a0-b33d-07fabb879626"), event_id=18, version=0)
class Microsoft_Windows_OLE_Perf_18_0(Etw):
    pattern = Struct(
        "HResult" / Int32sl
    )


@declare(guid=guid("84958368-7da7-49a0-b33d-07fabb879626"), event_id=20, version=0)
class Microsoft_Windows_OLE_Perf_20_0(Etw):
    pattern = Struct(
        "HResult" / Int32sl
    )


@declare(guid=guid("84958368-7da7-49a0-b33d-07fabb879626"), event_id=22, version=0)
class Microsoft_Windows_OLE_Perf_22_0(Etw):
    pattern = Struct(
        "HResult" / Int32sl
    )


@declare(guid=guid("84958368-7da7-49a0-b33d-07fabb879626"), event_id=24, version=0)
class Microsoft_Windows_OLE_Perf_24_0(Etw):
    pattern = Struct(
        "HResult" / Int32sl
    )


@declare(guid=guid("84958368-7da7-49a0-b33d-07fabb879626"), event_id=26, version=0)
class Microsoft_Windows_OLE_Perf_26_0(Etw):
    pattern = Struct(
        "HResult" / Int32sl
    )


@declare(guid=guid("84958368-7da7-49a0-b33d-07fabb879626"), event_id=28, version=0)
class Microsoft_Windows_OLE_Perf_28_0(Etw):
    pattern = Struct(
        "HResult" / Int32sl
    )

