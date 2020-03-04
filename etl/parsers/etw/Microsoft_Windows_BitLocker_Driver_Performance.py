# -*- coding: utf-8 -*-
"""
Microsoft-Windows-BitLocker-Driver-Performance
GUID : 1de130e1-c026-4cbf-ba0f-ab608e40aeea
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("1de130e1-c026-4cbf-ba0f-ab608e40aeea"), event_id=1, version=0)
class Microsoft_Windows_BitLocker_Driver_Performance_1_0(Etw):
    pattern = Struct(
        "DevObjPtr" / Int64ul,
        "IrpPtr" / Int64ul
    )


@declare(guid=guid("1de130e1-c026-4cbf-ba0f-ab608e40aeea"), event_id=2, version=0)
class Microsoft_Windows_BitLocker_Driver_Performance_2_0(Etw):
    pattern = Struct(
        "DevObjPtr" / Int64ul,
        "IrpPtr" / Int64ul
    )


@declare(guid=guid("1de130e1-c026-4cbf-ba0f-ab608e40aeea"), event_id=3, version=0)
class Microsoft_Windows_BitLocker_Driver_Performance_3_0(Etw):
    pattern = Struct(
        "DevObjPtr" / Int64ul,
        "IrpPtr" / Int64ul
    )


@declare(guid=guid("1de130e1-c026-4cbf-ba0f-ab608e40aeea"), event_id=4, version=0)
class Microsoft_Windows_BitLocker_Driver_Performance_4_0(Etw):
    pattern = Struct(
        "DevObjPtr" / Int64ul,
        "IrpPtr" / Int64ul
    )


@declare(guid=guid("1de130e1-c026-4cbf-ba0f-ab608e40aeea"), event_id=5, version=0)
class Microsoft_Windows_BitLocker_Driver_Performance_5_0(Etw):
    pattern = Struct(
        "DevObjPtr" / Int64ul,
        "IrpPtr" / Int64ul,
        "SubIrpPtr" / Int64ul
    )


@declare(guid=guid("1de130e1-c026-4cbf-ba0f-ab608e40aeea"), event_id=6, version=0)
class Microsoft_Windows_BitLocker_Driver_Performance_6_0(Etw):
    pattern = Struct(
        "DevObjPtr" / Int64ul,
        "IrpPtr" / Int64ul,
        "SubIrpPtr" / Int64ul
    )


@declare(guid=guid("1de130e1-c026-4cbf-ba0f-ab608e40aeea"), event_id=7, version=0)
class Microsoft_Windows_BitLocker_Driver_Performance_7_0(Etw):
    pattern = Struct(
        "DevObjPtr" / Int64ul,
        "IrpPtr" / Int64ul
    )


@declare(guid=guid("1de130e1-c026-4cbf-ba0f-ab608e40aeea"), event_id=8, version=0)
class Microsoft_Windows_BitLocker_Driver_Performance_8_0(Etw):
    pattern = Struct(
        "DevObjPtr" / Int64ul,
        "IrpPtr" / Int64ul
    )


@declare(guid=guid("1de130e1-c026-4cbf-ba0f-ab608e40aeea"), event_id=9, version=0)
class Microsoft_Windows_BitLocker_Driver_Performance_9_0(Etw):
    pattern = Struct(
        "DevObjPtr" / Int64ul,
        "IrpPtr" / Int64ul
    )


@declare(guid=guid("1de130e1-c026-4cbf-ba0f-ab608e40aeea"), event_id=10, version=0)
class Microsoft_Windows_BitLocker_Driver_Performance_10_0(Etw):
    pattern = Struct(
        "DevObjPtr" / Int64ul,
        "IrpPtr" / Int64ul
    )


@declare(guid=guid("1de130e1-c026-4cbf-ba0f-ab608e40aeea"), event_id=11, version=0)
class Microsoft_Windows_BitLocker_Driver_Performance_11_0(Etw):
    pattern = Struct(
        "DevObjPtr" / Int64ul,
        "PdoPtr" / Int64ul
    )


@declare(guid=guid("1de130e1-c026-4cbf-ba0f-ab608e40aeea"), event_id=12, version=0)
class Microsoft_Windows_BitLocker_Driver_Performance_12_0(Etw):
    pattern = Struct(
        "DevObjPtr" / Int64ul,
        "PdoPtr" / Int64ul
    )


@declare(guid=guid("1de130e1-c026-4cbf-ba0f-ab608e40aeea"), event_id=13, version=0)
class Microsoft_Windows_BitLocker_Driver_Performance_13_0(Etw):
    pattern = Struct(
        "DevObjPtr" / Int64ul
    )


@declare(guid=guid("1de130e1-c026-4cbf-ba0f-ab608e40aeea"), event_id=14, version=0)
class Microsoft_Windows_BitLocker_Driver_Performance_14_0(Etw):
    pattern = Struct(
        "DevObjPtr" / Int64ul
    )


@declare(guid=guid("1de130e1-c026-4cbf-ba0f-ab608e40aeea"), event_id=15, version=0)
class Microsoft_Windows_BitLocker_Driver_Performance_15_0(Etw):
    pattern = Struct(
        "DevObjPtr" / Int64ul,
        "Index" / Int32ul,
        "Offset" / Int64ul
    )


@declare(guid=guid("1de130e1-c026-4cbf-ba0f-ab608e40aeea"), event_id=16, version=0)
class Microsoft_Windows_BitLocker_Driver_Performance_16_0(Etw):
    pattern = Struct(
        "DevObjPtr" / Int64ul,
        "Index" / Int32ul,
        "Offset" / Int64ul
    )


@declare(guid=guid("1de130e1-c026-4cbf-ba0f-ab608e40aeea"), event_id=17, version=0)
class Microsoft_Windows_BitLocker_Driver_Performance_17_0(Etw):
    pattern = Struct(
        "DevObjPtr" / Int64ul,
        "Command" / Int32ul
    )


@declare(guid=guid("1de130e1-c026-4cbf-ba0f-ab608e40aeea"), event_id=18, version=0)
class Microsoft_Windows_BitLocker_Driver_Performance_18_0(Etw):
    pattern = Struct(
        "DevObjPtr" / Int64ul,
        "Command" / Int32ul
    )


@declare(guid=guid("1de130e1-c026-4cbf-ba0f-ab608e40aeea"), event_id=19, version=0)
class Microsoft_Windows_BitLocker_Driver_Performance_19_0(Etw):
    pattern = Struct(
        "DevObjPtr" / Int64ul,
        "Command" / Int32ul
    )


@declare(guid=guid("1de130e1-c026-4cbf-ba0f-ab608e40aeea"), event_id=20, version=0)
class Microsoft_Windows_BitLocker_Driver_Performance_20_0(Etw):
    pattern = Struct(
        "DevObjPtr" / Int64ul,
        "Command" / Int32ul
    )


@declare(guid=guid("1de130e1-c026-4cbf-ba0f-ab608e40aeea"), event_id=21, version=0)
class Microsoft_Windows_BitLocker_Driver_Performance_21_0(Etw):
    pattern = Struct(
        "DevObjPtr" / Int64ul,
        "Command" / Int32ul
    )


@declare(guid=guid("1de130e1-c026-4cbf-ba0f-ab608e40aeea"), event_id=22, version=0)
class Microsoft_Windows_BitLocker_Driver_Performance_22_0(Etw):
    pattern = Struct(
        "DevObjPtr" / Int64ul,
        "Command" / Int32ul
    )


@declare(guid=guid("1de130e1-c026-4cbf-ba0f-ab608e40aeea"), event_id=23, version=0)
class Microsoft_Windows_BitLocker_Driver_Performance_23_0(Etw):
    pattern = Struct(
        "DevObjPtr" / Int64ul,
        "Offset" / Int64ul,
        "Size" / Int32ul,
        "Command" / Int32ul
    )


@declare(guid=guid("1de130e1-c026-4cbf-ba0f-ab608e40aeea"), event_id=24, version=0)
class Microsoft_Windows_BitLocker_Driver_Performance_24_0(Etw):
    pattern = Struct(
        "DevObjPtr" / Int64ul,
        "Offset" / Int64ul,
        "Size" / Int32ul,
        "Command" / Int32ul
    )


@declare(guid=guid("1de130e1-c026-4cbf-ba0f-ab608e40aeea"), event_id=25, version=0)
class Microsoft_Windows_BitLocker_Driver_Performance_25_0(Etw):
    pattern = Struct(
        "DevObjPtr" / Int64ul,
        "PrevOffset" / Int64ul,
        "NextOffset" / Int64ul,
        "Size" / Int64ul
    )


@declare(guid=guid("1de130e1-c026-4cbf-ba0f-ab608e40aeea"), event_id=26, version=0)
class Microsoft_Windows_BitLocker_Driver_Performance_26_0(Etw):
    pattern = Struct(
        "DevObjPtr" / Int64ul,
        "PrevOffset" / Int64ul,
        "NextOffset" / Int64ul,
        "Size" / Int64ul
    )


@declare(guid=guid("1de130e1-c026-4cbf-ba0f-ab608e40aeea"), event_id=27, version=0)
class Microsoft_Windows_BitLocker_Driver_Performance_27_0(Etw):
    pattern = Struct(
        "DevObjPtr" / Int64ul,
        "SubIrpPtr" / Int64ul,
        "Offset" / Int64ul,
        "Size" / Int32ul
    )


@declare(guid=guid("1de130e1-c026-4cbf-ba0f-ab608e40aeea"), event_id=28, version=0)
class Microsoft_Windows_BitLocker_Driver_Performance_28_0(Etw):
    pattern = Struct(
        "DevObjPtr" / Int64ul,
        "SubIrpPtr" / Int64ul,
        "Offset" / Int64ul,
        "Size" / Int32ul
    )


@declare(guid=guid("1de130e1-c026-4cbf-ba0f-ab608e40aeea"), event_id=29, version=0)
class Microsoft_Windows_BitLocker_Driver_Performance_29_0(Etw):
    pattern = Struct(
        "DevObjPtr" / Int64ul,
        "SubIrpPtr" / Int64ul,
        "Offset" / Int64ul,
        "Size" / Int32ul
    )


@declare(guid=guid("1de130e1-c026-4cbf-ba0f-ab608e40aeea"), event_id=30, version=0)
class Microsoft_Windows_BitLocker_Driver_Performance_30_0(Etw):
    pattern = Struct(
        "DevObjPtr" / Int64ul,
        "SubIrpPtr" / Int64ul,
        "Offset" / Int64ul,
        "Size" / Int32ul
    )


@declare(guid=guid("1de130e1-c026-4cbf-ba0f-ab608e40aeea"), event_id=31, version=0)
class Microsoft_Windows_BitLocker_Driver_Performance_31_0(Etw):
    pattern = Struct(
        "BufferPtr" / Int64ul,
        "Size" / Int32ul
    )


@declare(guid=guid("1de130e1-c026-4cbf-ba0f-ab608e40aeea"), event_id=32, version=0)
class Microsoft_Windows_BitLocker_Driver_Performance_32_0(Etw):
    pattern = Struct(
        "BufferPtr" / Int64ul,
        "Size" / Int32ul
    )


@declare(guid=guid("1de130e1-c026-4cbf-ba0f-ab608e40aeea"), event_id=33, version=0)
class Microsoft_Windows_BitLocker_Driver_Performance_33_0(Etw):
    pattern = Struct(
        "BufferPtr" / Int64ul,
        "Size" / Int32ul
    )


@declare(guid=guid("1de130e1-c026-4cbf-ba0f-ab608e40aeea"), event_id=34, version=0)
class Microsoft_Windows_BitLocker_Driver_Performance_34_0(Etw):
    pattern = Struct(
        "BufferPtr" / Int64ul,
        "Size" / Int32ul
    )


@declare(guid=guid("1de130e1-c026-4cbf-ba0f-ab608e40aeea"), event_id=35, version=0)
class Microsoft_Windows_BitLocker_Driver_Performance_35_0(Etw):
    pattern = Struct(
        "BufferPtr" / Int64ul,
        "Size" / Int32ul
    )


@declare(guid=guid("1de130e1-c026-4cbf-ba0f-ab608e40aeea"), event_id=36, version=0)
class Microsoft_Windows_BitLocker_Driver_Performance_36_0(Etw):
    pattern = Struct(
        "BufferPtr" / Int64ul,
        "Size" / Int32ul
    )


@declare(guid=guid("1de130e1-c026-4cbf-ba0f-ab608e40aeea"), event_id=37, version=0)
class Microsoft_Windows_BitLocker_Driver_Performance_37_0(Etw):
    pattern = Struct(
        "BufferPtr" / Int64ul,
        "Size" / Int32ul
    )


@declare(guid=guid("1de130e1-c026-4cbf-ba0f-ab608e40aeea"), event_id=38, version=0)
class Microsoft_Windows_BitLocker_Driver_Performance_38_0(Etw):
    pattern = Struct(
        "BufferPtr" / Int64ul,
        "Size" / Int32ul
    )


@declare(guid=guid("1de130e1-c026-4cbf-ba0f-ab608e40aeea"), event_id=39, version=0)
class Microsoft_Windows_BitLocker_Driver_Performance_39_0(Etw):
    pattern = Struct(
        "BufferPtr" / Int64ul,
        "Size" / Int32ul
    )


@declare(guid=guid("1de130e1-c026-4cbf-ba0f-ab608e40aeea"), event_id=40, version=0)
class Microsoft_Windows_BitLocker_Driver_Performance_40_0(Etw):
    pattern = Struct(
        "BufferPtr" / Int64ul,
        "Size" / Int32ul
    )


@declare(guid=guid("1de130e1-c026-4cbf-ba0f-ab608e40aeea"), event_id=41, version=0)
class Microsoft_Windows_BitLocker_Driver_Performance_41_0(Etw):
    pattern = Struct(
        "BufferPtr" / Int64ul,
        "Size" / Int32ul
    )


@declare(guid=guid("1de130e1-c026-4cbf-ba0f-ab608e40aeea"), event_id=42, version=0)
class Microsoft_Windows_BitLocker_Driver_Performance_42_0(Etw):
    pattern = Struct(
        "BufferPtr" / Int64ul,
        "Size" / Int32ul
    )


@declare(guid=guid("1de130e1-c026-4cbf-ba0f-ab608e40aeea"), event_id=43, version=0)
class Microsoft_Windows_BitLocker_Driver_Performance_43_0(Etw):
    pattern = Struct(
        "BufferPtr" / Int64ul,
        "Size" / Int32ul
    )


@declare(guid=guid("1de130e1-c026-4cbf-ba0f-ab608e40aeea"), event_id=44, version=0)
class Microsoft_Windows_BitLocker_Driver_Performance_44_0(Etw):
    pattern = Struct(
        "BufferPtr" / Int64ul,
        "Size" / Int32ul
    )


@declare(guid=guid("1de130e1-c026-4cbf-ba0f-ab608e40aeea"), event_id=45, version=0)
class Microsoft_Windows_BitLocker_Driver_Performance_45_0(Etw):
    pattern = Struct(
        "BufferPtr" / Int64ul,
        "Size" / Int32ul
    )


@declare(guid=guid("1de130e1-c026-4cbf-ba0f-ab608e40aeea"), event_id=46, version=0)
class Microsoft_Windows_BitLocker_Driver_Performance_46_0(Etw):
    pattern = Struct(
        "BufferPtr" / Int64ul,
        "Size" / Int32ul
    )

