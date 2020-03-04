# -*- coding: utf-8 -*-
"""
Microsoft-Windows-WMP-Setup_WM
GUID : 0d759f0f-cff9-4902-8867-eb9e29d7a98b
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("0d759f0f-cff9-4902-8867-eb9e29d7a98b"), event_id=801, version=0)
class Microsoft_Windows_WMP_Setup_WM_801_0(Etw):
    pattern = Struct(
        "WMPSetupID" / Int32ul
    )


@declare(guid=guid("0d759f0f-cff9-4902-8867-eb9e29d7a98b"), event_id=802, version=0)
class Microsoft_Windows_WMP_Setup_WM_802_0(Etw):
    pattern = Struct(
        "WMPSetupID" / Int32ul
    )


@declare(guid=guid("0d759f0f-cff9-4902-8867-eb9e29d7a98b"), event_id=803, version=0)
class Microsoft_Windows_WMP_Setup_WM_803_0(Etw):
    pattern = Struct(
        "WMPSetupID" / Int32ul
    )


@declare(guid=guid("0d759f0f-cff9-4902-8867-eb9e29d7a98b"), event_id=804, version=0)
class Microsoft_Windows_WMP_Setup_WM_804_0(Etw):
    pattern = Struct(
        "WMPSetupID" / Int32ul
    )


@declare(guid=guid("0d759f0f-cff9-4902-8867-eb9e29d7a98b"), event_id=805, version=0)
class Microsoft_Windows_WMP_Setup_WM_805_0(Etw):
    pattern = Struct(
        "WMPSetupID" / Int32ul
    )


@declare(guid=guid("0d759f0f-cff9-4902-8867-eb9e29d7a98b"), event_id=806, version=0)
class Microsoft_Windows_WMP_Setup_WM_806_0(Etw):
    pattern = Struct(
        "WMPSetupID" / Int32ul
    )

