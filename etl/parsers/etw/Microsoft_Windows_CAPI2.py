# -*- coding: utf-8 -*-
"""
Microsoft-Windows-CAPI2
GUID : 5bbca4a8-b209-48dc-a8c7-b23d3e5216fb
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=10, version=0)
class Microsoft_Windows_CAPI2_10_0(Etw):
    pattern = Struct(
        "EventWriteData" / WString
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=11, version=0)
class Microsoft_Windows_CAPI2_11_0(Etw):
    pattern = Struct(
        "EventWriteData" / WString
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=12, version=0)
class Microsoft_Windows_CAPI2_12_0(Etw):
    pattern = Struct(
        "EventWriteData" / WString
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=13, version=0)
class Microsoft_Windows_CAPI2_13_0(Etw):
    pattern = Struct(
        "EventWriteData" / WString
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=14, version=0)
class Microsoft_Windows_CAPI2_14_0(Etw):
    pattern = Struct(
        "EventWriteData" / WString
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=15, version=0)
class Microsoft_Windows_CAPI2_15_0(Etw):
    pattern = Struct(
        "EventWriteData" / WString
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=16, version=0)
class Microsoft_Windows_CAPI2_16_0(Etw):
    pattern = Struct(
        "EventWriteData" / WString
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=17, version=0)
class Microsoft_Windows_CAPI2_17_0(Etw):
    pattern = Struct(
        "EventWriteData" / WString
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=18, version=0)
class Microsoft_Windows_CAPI2_18_0(Etw):
    pattern = Struct(
        "EventWriteData" / WString
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=19, version=0)
class Microsoft_Windows_CAPI2_19_0(Etw):
    pattern = Struct(
        "EventWriteData" / WString
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=20, version=0)
class Microsoft_Windows_CAPI2_20_0(Etw):
    pattern = Struct(
        "EventWriteData" / WString
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=21, version=0)
class Microsoft_Windows_CAPI2_21_0(Etw):
    pattern = Struct(
        "EventWriteData" / WString
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=22, version=0)
class Microsoft_Windows_CAPI2_22_0(Etw):
    pattern = Struct(
        "EventWriteData" / WString
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=23, version=0)
class Microsoft_Windows_CAPI2_23_0(Etw):
    pattern = Struct(
        "EventWriteData" / WString
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=24, version=0)
class Microsoft_Windows_CAPI2_24_0(Etw):
    pattern = Struct(
        "EventWriteData" / WString
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=30, version=0)
class Microsoft_Windows_CAPI2_30_0(Etw):
    pattern = Struct(
        "EventWriteData" / WString
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=40, version=0)
class Microsoft_Windows_CAPI2_40_0(Etw):
    pattern = Struct(
        "EventWriteData" / WString
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=41, version=0)
class Microsoft_Windows_CAPI2_41_0(Etw):
    pattern = Struct(
        "EventWriteData" / WString
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=42, version=0)
class Microsoft_Windows_CAPI2_42_0(Etw):
    pattern = Struct(
        "EventWriteData" / WString
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=50, version=0)
class Microsoft_Windows_CAPI2_50_0(Etw):
    pattern = Struct(
        "EventWriteData" / WString
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=51, version=0)
class Microsoft_Windows_CAPI2_51_0(Etw):
    pattern = Struct(
        "EventWriteData" / WString
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=52, version=0)
class Microsoft_Windows_CAPI2_52_0(Etw):
    pattern = Struct(
        "EventWriteData" / WString
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=53, version=0)
class Microsoft_Windows_CAPI2_53_0(Etw):
    pattern = Struct(
        "EventWriteData" / WString
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=60, version=0)
class Microsoft_Windows_CAPI2_60_0(Etw):
    pattern = Struct(
        "EventWriteData" / WString
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=70, version=0)
class Microsoft_Windows_CAPI2_70_0(Etw):
    pattern = Struct(
        "EventWriteData" / WString
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=71, version=0)
class Microsoft_Windows_CAPI2_71_0(Etw):
    pattern = Struct(
        "EventWriteData" / WString
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=80, version=0)
class Microsoft_Windows_CAPI2_80_0(Etw):
    pattern = Struct(
        "EventWriteData" / WString
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=81, version=0)
class Microsoft_Windows_CAPI2_81_0(Etw):
    pattern = Struct(
        "EventWriteData" / WString
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=82, version=0)
class Microsoft_Windows_CAPI2_82_0(Etw):
    pattern = Struct(
        "EventWriteData" / WString
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=90, version=0)
class Microsoft_Windows_CAPI2_90_0(Etw):
    pattern = Struct(
        "EventWriteData" / WString
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=256, version=0)
class Microsoft_Windows_CAPI2_256_0(Etw):
    pattern = Struct(
        "1" / WString,
        "2" / WString
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=257, version=0)
class Microsoft_Windows_CAPI2_257_0(Etw):
    pattern = Struct(
        "1" / WString
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=512, version=0)
class Microsoft_Windows_CAPI2_512_0(Etw):
    pattern = Struct(
        "1" / WString
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=513, version=0)
class Microsoft_Windows_CAPI2_513_0(Etw):
    pattern = Struct(
        "1" / WString
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=4097, version=0)
class Microsoft_Windows_CAPI2_4097_0(Etw):
    pattern = Struct(
        "1" / WString,
        "2" / WString
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=4098, version=0)
class Microsoft_Windows_CAPI2_4098_0(Etw):
    pattern = Struct(
        "1" / WString
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=4099, version=0)
class Microsoft_Windows_CAPI2_4099_0(Etw):
    pattern = Struct(
        "1" / WString,
        "2" / WString
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=4100, version=0)
class Microsoft_Windows_CAPI2_4100_0(Etw):
    pattern = Struct(
        "1" / WString
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=4101, version=0)
class Microsoft_Windows_CAPI2_4101_0(Etw):
    pattern = Struct(
        "1" / WString,
        "2" / WString
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=4102, version=0)
class Microsoft_Windows_CAPI2_4102_0(Etw):
    pattern = Struct(
        "1" / WString,
        "2" / WString
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=4103, version=0)
class Microsoft_Windows_CAPI2_4103_0(Etw):
    pattern = Struct(
        "1" / WString
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=4104, version=0)
class Microsoft_Windows_CAPI2_4104_0(Etw):
    pattern = Struct(
        "1" / WString,
        "2" / WString
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=4105, version=0)
class Microsoft_Windows_CAPI2_4105_0(Etw):
    pattern = Struct(
        "1" / WString,
        "2" / WString
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=4106, version=0)
class Microsoft_Windows_CAPI2_4106_0(Etw):
    pattern = Struct(
        "1" / WString,
        "2" / WString
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=4107, version=0)
class Microsoft_Windows_CAPI2_4107_0(Etw):
    pattern = Struct(
        "1" / WString,
        "2" / WString
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=4108, version=0)
class Microsoft_Windows_CAPI2_4108_0(Etw):
    pattern = Struct(
        "1" / WString,
        "2" / WString
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=4109, version=0)
class Microsoft_Windows_CAPI2_4109_0(Etw):
    pattern = Struct(
        "1" / WString,
        "2" / WString
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=4110, version=0)
class Microsoft_Windows_CAPI2_4110_0(Etw):
    pattern = Struct(
        "1" / WString,
        "2" / WString
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=4111, version=0)
class Microsoft_Windows_CAPI2_4111_0(Etw):
    pattern = Struct(
        "1" / WString
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=4112, version=0)
class Microsoft_Windows_CAPI2_4112_0(Etw):
    pattern = Struct(
        "1" / WString
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=4113, version=0)
class Microsoft_Windows_CAPI2_4113_0(Etw):
    pattern = Struct(
        "1" / WString
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=4114, version=0)
class Microsoft_Windows_CAPI2_4114_0(Etw):
    pattern = Struct(
        "1" / WString,
        "2" / WString,
        "3" / WString,
        "4" / WString,
        "5" / WString,
        "6" / WString,
        "7" / WString
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=4115, version=0)
class Microsoft_Windows_CAPI2_4115_0(Etw):
    pattern = Struct(
        "1" / WString,
        "2" / WString,
        "3" / WString
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=4116, version=0)
class Microsoft_Windows_CAPI2_4116_0(Etw):
    pattern = Struct(
        "1" / WString,
        "2" / WString,
        "3" / WString,
        "4" / WString,
        "5" / WString,
        "6" / WString,
        "7" / WString
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=4117, version=0)
class Microsoft_Windows_CAPI2_4117_0(Etw):
    pattern = Struct(
        "1" / WString,
        "2" / WString,
        "3" / WString,
        "4" / WString,
        "5" / WString,
        "6" / WString,
        "7" / WString,
        "8" / WString,
        "9" / WString,
        "10" / WString
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=4128, version=0)
class Microsoft_Windows_CAPI2_4128_0(Etw):
    pattern = Struct(
        "1" / WString
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=4129, version=0)
class Microsoft_Windows_CAPI2_4129_0(Etw):
    pattern = Struct(
        "1" / WString,
        "2" / WString
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=4176, version=0)
class Microsoft_Windows_CAPI2_4176_0(Etw):
    pattern = Struct(
        "1" / WString,
        "2" / WString
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=4177, version=0)
class Microsoft_Windows_CAPI2_4177_0(Etw):
    pattern = Struct(
        "1" / WString,
        "2" / WString
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=4178, version=0)
class Microsoft_Windows_CAPI2_4178_0(Etw):
    pattern = Struct(
        "1" / WString,
        "2" / WString
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=8192, version=0)
class Microsoft_Windows_CAPI2_8192_0(Etw):
    pattern = Struct(
        "Subsystem" / WString,
        "FileName" / WString
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=8193, version=0)
class Microsoft_Windows_CAPI2_8193_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=8194, version=0)
class Microsoft_Windows_CAPI2_8194_0(Etw):
    pattern = Struct(
        "Subsystem" / WString,
        "FileName" / WString
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=8195, version=0)
class Microsoft_Windows_CAPI2_8195_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=8196, version=0)
class Microsoft_Windows_CAPI2_8196_0(Etw):
    pattern = Struct(
        "Subsystem" / WString,
        "FileName" / WString
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=8197, version=0)
class Microsoft_Windows_CAPI2_8197_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=8198, version=0)
class Microsoft_Windows_CAPI2_8198_0(Etw):
    pattern = Struct(
        "Subsystem" / WString
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=8199, version=0)
class Microsoft_Windows_CAPI2_8199_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=8200, version=0)
class Microsoft_Windows_CAPI2_8200_0(Etw):
    pattern = Struct(
        "Subsystem" / WString,
        "Algorithm" / WString,
        "Length" / Int16ul,
        "Value" / Bytes(lambda this: this.Length)
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=8201, version=0)
class Microsoft_Windows_CAPI2_8201_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "Count" / Int32ul
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=8202, version=0)
class Microsoft_Windows_CAPI2_8202_0(Etw):
    pattern = Struct(
        "Subsystem" / WString
    )


@declare(guid=guid("5bbca4a8-b209-48dc-a8c7-b23d3e5216fb"), event_id=8203, version=0)
class Microsoft_Windows_CAPI2_8203_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )

