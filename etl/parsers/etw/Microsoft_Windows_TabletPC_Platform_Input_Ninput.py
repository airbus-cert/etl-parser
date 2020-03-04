# -*- coding: utf-8 -*-
"""
Microsoft-Windows-TabletPC-Platform-Input-Ninput
GUID : 2c3e6d9f-8298-450f-8e5d-49b724f1216f
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("2c3e6d9f-8298-450f-8e5d-49b724f1216f"), event_id=1, version=0)
class Microsoft_Windows_TabletPC_Platform_Input_Ninput_1_0(Etw):
    pattern = Struct(
        "frameId" / Int32ul
    )


@declare(guid=guid("2c3e6d9f-8298-450f-8e5d-49b724f1216f"), event_id=2, version=0)
class Microsoft_Windows_TabletPC_Platform_Input_Ninput_2_0(Etw):
    pattern = Struct(
        "frameId" / Int32ul
    )


@declare(guid=guid("2c3e6d9f-8298-450f-8e5d-49b724f1216f"), event_id=11, version=0)
class Microsoft_Windows_TabletPC_Platform_Input_Ninput_11_0(Etw):
    pattern = Struct(
        "ContactsDownCount" / Int32ul,
        "PacketsInContactCount" / Int32ul,
        "HistoryPacketsInContactCount" / Int32ul
    )


@declare(guid=guid("2c3e6d9f-8298-450f-8e5d-49b724f1216f"), event_id=13, version=0)
class Microsoft_Windows_TabletPC_Platform_Input_Ninput_13_0(Etw):
    pattern = Struct(
        "GestureId" / Int32ul
    )


@declare(guid=guid("2c3e6d9f-8298-450f-8e5d-49b724f1216f"), event_id=14, version=0)
class Microsoft_Windows_TabletPC_Platform_Input_Ninput_14_0(Etw):
    pattern = Struct(
        "GestureId" / Int32ul
    )


@declare(guid=guid("2c3e6d9f-8298-450f-8e5d-49b724f1216f"), event_id=15, version=0)
class Microsoft_Windows_TabletPC_Platform_Input_Ninput_15_0(Etw):
    pattern = Struct(
        "promotionFlags" / Int32ul
    )


@declare(guid=guid("2c3e6d9f-8298-450f-8e5d-49b724f1216f"), event_id=16, version=0)
class Microsoft_Windows_TabletPC_Platform_Input_Ninput_16_0(Etw):
    pattern = Struct(
        "promotionFlags" / Int32ul
    )


@declare(guid=guid("2c3e6d9f-8298-450f-8e5d-49b724f1216f"), event_id=33, version=0)
class Microsoft_Windows_TabletPC_Platform_Input_Ninput_33_0(Etw):
    pattern = Struct(
        "frameId" / Int32ul
    )


@declare(guid=guid("2c3e6d9f-8298-450f-8e5d-49b724f1216f"), event_id=34, version=0)
class Microsoft_Windows_TabletPC_Platform_Input_Ninput_34_0(Etw):
    pattern = Struct(
        "InteractionId" / Int32ul
    )


@declare(guid=guid("2c3e6d9f-8298-450f-8e5d-49b724f1216f"), event_id=35, version=0)
class Microsoft_Windows_TabletPC_Platform_Input_Ninput_35_0(Etw):
    pattern = Struct(
        "InteractionId" / Int32ul
    )


@declare(guid=guid("2c3e6d9f-8298-450f-8e5d-49b724f1216f"), event_id=43, version=0)
class Microsoft_Windows_TabletPC_Platform_Input_Ninput_43_0(Etw):
    pattern = Struct(
        "GestureId" / Int32ul
    )


@declare(guid=guid("2c3e6d9f-8298-450f-8e5d-49b724f1216f"), event_id=51, version=0)
class Microsoft_Windows_TabletPC_Platform_Input_Ninput_51_0(Etw):
    pattern = Struct(
        "delta" / Int32sl
    )


@declare(guid=guid("2c3e6d9f-8298-450f-8e5d-49b724f1216f"), event_id=52, version=0)
class Microsoft_Windows_TabletPC_Platform_Input_Ninput_52_0(Etw):
    pattern = Struct(
        "delta" / Int32sl
    )


@declare(guid=guid("2c3e6d9f-8298-450f-8e5d-49b724f1216f"), event_id=53, version=0)
class Microsoft_Windows_TabletPC_Platform_Input_Ninput_53_0(Etw):
    pattern = Struct(
        "scrollMode" / Int32ul
    )


@declare(guid=guid("2c3e6d9f-8298-450f-8e5d-49b724f1216f"), event_id=54, version=0)
class Microsoft_Windows_TabletPC_Platform_Input_Ninput_54_0(Etw):
    pattern = Struct(
        "scrollMode" / Int32ul
    )


@declare(guid=guid("2c3e6d9f-8298-450f-8e5d-49b724f1216f"), event_id=55, version=0)
class Microsoft_Windows_TabletPC_Platform_Input_Ninput_55_0(Etw):
    pattern = Struct(
        "scrollMode" / Int32ul
    )

