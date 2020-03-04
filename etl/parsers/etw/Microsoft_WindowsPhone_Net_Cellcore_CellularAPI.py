# -*- coding: utf-8 -*-
"""
Microsoft-WindowsPhone-Net-Cellcore-CellularAPI
GUID : 6b7b5e3a-f4de-42d9-9545-bae12852d778
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=102, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_102_0(Etw):
    pattern = Struct(
        "AnsiStringName" / CString,
        "Int32Name" / Int32sl
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=103, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_103_0(Etw):
    pattern = Struct(
        "UInt16Name" / Int16ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=104, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_104_0(Etw):
    pattern = Struct(
        "UInt16Name" / Int16ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=105, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_105_0(Etw):
    pattern = Struct(
        "AnsiStringName1" / CString,
        "AnsiStringName2" / CString,
        "RilErrorName" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=106, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_106_0(Etw):
    pattern = Struct(
        "AnsiStringName" / CString
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=107, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_107_0(Etw):
    pattern = Struct(
        "AnsiStringName" / CString,
        "DwordName" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=108, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_108_0(Etw):
    pattern = Struct(
        "AnsiStringName1" / CString,
        "RilErrorName" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=110, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_110_0(Etw):
    pattern = Struct(
        "AnsiStringName" / CString
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=111, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_111_0(Etw):
    pattern = Struct(
        "FunctionName" / CString,
        "Pointer" / Int64ul,
        "RefCount" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=112, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_112_0(Etw):
    pattern = Struct(
        "FunctionName" / CString,
        "Pointer" / Int64ul,
        "RefCount" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=113, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_113_0(Etw):
    pattern = Struct(
        "FunctionName" / CString,
        "Tag" / Int32ul,
        "Pointer" / Int64ul,
        "RefCount" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=114, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_114_0(Etw):
    pattern = Struct(
        "FunctionName" / CString,
        "Pointer" / Int64ul,
        "RefCount" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=115, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_115_0(Etw):
    pattern = Struct(
        "FunctionName" / CString,
        "Pointer" / Int32ul,
        "Pointer2" / Int64ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=116, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_116_0(Etw):
    pattern = Struct(
        "DwordName" / Int32ul,
        "PointerName" / Int64ul,
        "GuidName" / Guid
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=117, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_117_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul,
        "HResultName" / Int32sl
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=190, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_190_0(Etw):
    pattern = Struct(
        "DwordName" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=191, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_191_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul,
        "DwordName2" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=192, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_192_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul,
        "DwordName2" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=200, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_200_0(Etw):
    pattern = Struct(
        "Pointer" / Int64ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=201, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_201_0(Etw):
    pattern = Struct(
        "Pointer" / Int64ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=202, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_202_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul,
        "DwordName2" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=203, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_203_0(Etw):
    pattern = Struct(
        "BooleanName" / Int8ul,
        "DwordName1" / Int32ul,
        "DwordName2" / Int32ul,
        "DwordName3" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=204, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_204_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul,
        "DwordName2" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=205, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_205_0(Etw):
    pattern = Struct(
        "DwordName" / Int32ul,
        "UiccSlotStateName" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=300, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_300_0(Etw):
    pattern = Struct(
        "Pointer" / Int64ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=301, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_301_0(Etw):
    pattern = Struct(
        "Pointer" / Int64ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=302, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_302_0(Etw):
    pattern = Struct(
        "DwordName" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=303, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_303_0(Etw):
    pattern = Struct(
        "DwordName" / Int32ul,
        "BooleanName" / Int8ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=400, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_400_0(Etw):
    pattern = Struct(
        "DwordName" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=401, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_401_0(Etw):
    pattern = Struct(
        "AnsiStringName" / CString,
        "DwordName" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=402, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_402_0(Etw):
    pattern = Struct(
        "DwordName" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=403, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_403_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul,
        "DwordName2" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=404, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_404_0(Etw):
    pattern = Struct(
        "DwordName" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=405, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_405_0(Etw):
    pattern = Struct(
        "Pointer" / Int64ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=406, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_406_0(Etw):
    pattern = Struct(
        "Pointer" / Int64ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=500, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_500_0(Etw):
    pattern = Struct(
        "Pointer" / Int64ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=501, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_501_0(Etw):
    pattern = Struct(
        "Pointer" / Int64ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=503, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_503_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul,
        "DwordName2" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=504, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_504_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul,
        "DwordName2" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=505, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_505_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul,
        "DwordName2" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=506, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_506_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=507, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_507_0(Etw):
    pattern = Struct(
        "ModemResetState" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=508, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_508_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul,
        "DwordName2" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=509, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_509_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul,
        "DwordName2" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=510, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_510_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=600, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_600_0(Etw):
    pattern = Struct(
        "DwordName" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=601, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_601_0(Etw):
    pattern = Struct(
        "Pointer" / Int64ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=602, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_602_0(Etw):
    pattern = Struct(
        "Pointer" / Int64ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=603, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_603_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul,
        "DwordName2" / Int32ul,
        "DwordName3" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=604, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_604_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=605, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_605_0(Etw):
    pattern = Struct(
        "DwordName" / Int32ul,
        "PointerName" / Int64ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=606, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_606_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul,
        "DwordName2" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=700, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_700_0(Etw):
    pattern = Struct(
        "DwordName" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=701, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_701_0(Etw):
    pattern = Struct(
        "DwordName" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=702, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_702_0(Etw):
    pattern = Struct(
        "DwordName" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=704, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_704_0(Etw):
    pattern = Struct(
        "DwordName" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=800, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_800_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul,
        "DwordName2" / Int32ul,
        "DwordName3" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=801, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_801_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul,
        "DwordName2" / Int32ul,
        "DwordName3" / Int32ul,
        "DwordName4" / Int32ul,
        "DwordName5" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=803, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_803_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "Path" / WString,
        "Key" / WString,
        "Value" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=804, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_804_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul,
        "DwordName2" / Int32ul,
        "DwordName3" / Int32ul,
        "DwordName4" / Int32ul,
        "DwordName5" / Int32ul,
        "DwordName6" / Int32ul,
        "DwordName7" / Int32ul,
        "DwordName8" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=805, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_805_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul,
        "DwordName2" / Int32ul,
        "DwordName3" / Int32ul,
        "DwordName4" / Int32ul,
        "DwordName5" / Int32ul,
        "DwordName6" / Int32ul,
        "DwordName7" / Int32ul,
        "DwordName8" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=806, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_806_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul,
        "DwordName2" / Int32ul,
        "DwordName3" / Int32ul,
        "DwordName4" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=807, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_807_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul,
        "DwordName2" / Int32ul,
        "BooleanName" / Int8ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=808, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_808_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul,
        "DwordName2" / Int32ul,
        "DwordName3" / Int32ul,
        "DwordName4" / Int32ul,
        "Pointer" / Int64ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=809, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_809_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul,
        "DwordName2" / Int32ul,
        "DwordName3" / Int32ul,
        "DwordName4" / Int32ul,
        "cbBytes5" / Int32ul,
        "Bytes5" / Int8ul,
        "DwordName6" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=810, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_810_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul,
        "DwordName2" / Int32ul,
        "DwordName3" / Int32ul,
        "DwordName4" / Int32ul,
        "DwordName5" / Int32ul,
        "DwordName6" / Int32ul,
        "DwordName7" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=811, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_811_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul,
        "DwordName2" / Int32ul,
        "DwordName3" / Int32ul,
        "DwordName4" / Int32ul,
        "DwordName5" / Int32ul,
        "Pointer" / Int64ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=812, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_812_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul,
        "DwordName2" / Int32ul,
        "DwordName3" / Int32ul,
        "DwordName4" / Int32ul,
        "DwordName5" / Int32ul,
        "cbBytes6" / Int32ul,
        "Bytes6" / Int8ul,
        "cbBytes7" / Int32ul,
        "Bytes7" / Int8ul,
        "StringName8" / WString,
        "DwordName6" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=813, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_813_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul,
        "DwordName2" / Int32ul,
        "DwordName3" / Int32ul,
        "DwordName4" / Int32ul,
        "cbBytes5" / Int32ul,
        "Bytes5" / Int8ul,
        "cbBytes6" / Int32ul,
        "Bytes6" / Int8ul,
        "Pointer" / Int64ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=814, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_814_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul,
        "DwordName2" / Int32ul,
        "DwordName3" / Int32ul,
        "DwordName4" / Int32ul,
        "cbBytes5" / Int32ul,
        "Bytes5" / Int8ul,
        "cbBytes6" / Int32ul,
        "Bytes6" / Int8ul,
        "Pointer" / Int64ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=815, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_815_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul,
        "DwordName2" / Int32ul,
        "cbBytes3" / Int32ul,
        "Bytes3" / Int8ul,
        "cbBytes4" / Int32ul,
        "Bytes4" / Int8ul,
        "Pointer" / Int64ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=816, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_816_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul,
        "DwordName2" / Int32ul,
        "cbBytes3" / Int32ul,
        "Bytes3" / Int8ul,
        "Pointer" / Int64ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=817, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_817_0(Etw):
    pattern = Struct(
        "DwordName" / Int32ul,
        "PointerName" / Int64ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=818, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_818_0(Etw):
    pattern = Struct(
        "cbBytes" / Int32ul,
        "Bytes" / Int8ul,
        "Pointer" / Int64ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=819, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_819_0(Etw):
    pattern = Struct(
        "DwordName" / Int32ul,
        "PointerName" / Int64ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=820, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_820_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul,
        "DwordName2" / Int32ul,
        "Pointer" / Int64ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=821, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_821_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul,
        "DwordName2" / Int32ul,
        "DwordName3" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=822, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_822_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul,
        "DwordName2" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=823, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_823_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul,
        "DwordName2" / Int32ul,
        "DwordName3" / Int32ul,
        "DwordName4" / Int32ul,
        "DwordName5" / Int32ul,
        "DwordName6" / Int32ul,
        "DwordName7" / Int32ul,
        "DwordName8" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=824, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_824_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "Path" / WString,
        "Key" / WString,
        "Value" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=825, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_825_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=826, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_826_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul,
        "DwordName2" / Int32ul,
        "DwordName3" / Int32ul,
        "DwordName4" / Int32ul,
        "DwordName5" / Int32ul,
        "DwordName6" / Int32ul,
        "DwordName7" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=827, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_827_0(Etw):
    pattern = Struct(
        "HResult" / Int32ul,
        "SmsType" / WString,
        "Pointer1" / Int64ul,
        "Pointer2" / Int64ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=828, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_828_0(Etw):
    pattern = Struct(
        "Pointer" / Int64ul,
        "String" / WString
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=829, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_829_0(Etw):
    pattern = Struct(
        "Pointer" / Int64ul,
        "DwordName1" / Int32ul,
        "DwordName2" / Int32ul,
        "String" / WString
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=830, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_830_0(Etw):
    pattern = Struct(
        "Pointer" / Int64ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=831, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_831_0(Etw):
    pattern = Struct(
        "Pointer" / Int64ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=832, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_832_0(Etw):
    pattern = Struct(
        "Pointer" / Int64ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=833, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_833_0(Etw):
    pattern = Struct(
        "AnsiStringName" / CString,
        "Dword1Name" / Int32ul,
        "HResultName" / Int32sl,
        "Pointer" / Int64ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=834, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_834_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul,
        "DwordName2" / Int32ul,
        "DwordName3" / Int32ul,
        "DwordName4" / Int32ul,
        "DwordName5" / Int32ul,
        "cbBytes6" / Int32ul,
        "Bytes6" / Int8ul,
        "cbBytes7" / Int32ul,
        "Bytes7" / Int8ul,
        "StringName8" / WString
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=835, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_835_0(Etw):
    pattern = Struct(
        "Pointer" / Int64ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=836, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_836_0(Etw):
    pattern = Struct(
        "StringName1" / WString,
        "DwordName1" / Int32ul,
        "Pointer1" / Int64ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=837, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_837_0(Etw):
    pattern = Struct(
        "Pointer" / Int64ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=838, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_838_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=839, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_839_0(Etw):
    pattern = Struct(
        "AnsiStringName" / CString,
        "DwordName" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=840, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_840_0(Etw):
    pattern = Struct(
        "AnsiStringName" / CString
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=841, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_841_0(Etw):
    pattern = Struct(
        "HResultName" / Int32sl,
        "Pointer" / Int64ul,
        "String" / WString
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=842, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_842_0(Etw):
    pattern = Struct(
        "HResultName" / Int32sl,
        "Pointer" / Int64ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=843, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_843_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul,
        "DwordName2" / Int32ul,
        "DwordName3" / Int32ul,
        "DwordName4" / Int32ul,
        "DwordName5" / Int32ul,
        "Pointer" / Int64ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=844, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_844_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul,
        "DwordName2" / Int32ul,
        "cbBytes3" / Int32ul,
        "Bytes3" / Int8ul,
        "Pointer" / Int64ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=845, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_845_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul,
        "DwordName2" / Int32ul,
        "cbBytes3" / Int32ul,
        "Bytes3" / Int8ul,
        "Pointer" / Int64ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=846, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_846_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul,
        "DwordName2" / Int32ul,
        "DwordName3" / Int32ul,
        "cbBytes3" / Int32ul,
        "Bytes3" / Int8ul,
        "Pointer" / Int64ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=847, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_847_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul,
        "Pointer1" / Int64ul,
        "Pointer2" / Int64ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=848, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_848_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul,
        "Pointer1" / Int64ul,
        "Pointer2" / Int64ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=855, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_855_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=856, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_856_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=857, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_857_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul,
        "DwordName2" / Int32ul,
        "DwordName3" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=858, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_858_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul,
        "DwordName2" / Int32ul,
        "DwordName3" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=859, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_859_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul,
        "DwordName2" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=860, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_860_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=861, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_861_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul,
        "DwordName2" / Int32ul,
        "DwordName3" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=862, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_862_0(Etw):
    pattern = Struct(
        "Result" / Int32ul,
        "String" / CString
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=863, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_863_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul,
        "DwordName2" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=864, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_864_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=865, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_865_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul,
        "Pointer1" / Int64ul,
        "Pointer2" / Int64ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=866, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_866_0(Etw):
    pattern = Struct(
        "FunctionName" / CString,
        "Pointer" / Int32ul,
        "Pointer2" / Int32ul,
        "Pointer3" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=867, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_867_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=868, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_868_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=869, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_869_0(Etw):
    pattern = Struct(
        "Dword1" / Int32ul,
        "Dword2" / Int32ul,
        "Dword3" / Int32ul,
        "cbDword" / Int32ul,
        "DwordArray" / Int32ul,
        "Pointer" / Int64ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=870, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_870_0(Etw):
    pattern = Struct(
        "Dword1" / Int32ul,
        "Dword2" / Int32ul,
        "Dword3" / Int32ul,
        "cbDword" / Int32ul,
        "DwordArray" / Int32ul,
        "Pointer" / Int64ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=871, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_871_0(Etw):
    pattern = Struct(
        "cbDword1" / Int32ul,
        "DwordArray1" / Int32ul,
        "cbDword2" / Int32ul,
        "DwordArray2" / Int32ul,
        "Pointer" / Int64ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=872, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_872_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=873, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_873_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul,
        "DwordName2" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=874, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_874_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul,
        "DwordName2" / Int32ul,
        "DwordName3" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=875, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_875_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul,
        "DwordName2" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=876, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_876_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=877, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_877_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=878, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_878_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=879, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_879_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul,
        "DwordName2" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=1000, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_1000_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul,
        "DwordName2" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=1001, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_1001_0(Etw):
    pattern = Struct(
        "Pointer" / Int64ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=1002, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_1002_0(Etw):
    pattern = Struct(
        "Pointer" / Int64ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=1003, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_1003_0(Etw):
    pattern = Struct(
        "Pointer" / Int64ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=1004, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_1004_0(Etw):
    pattern = Struct(
        "Pointer" / Int64ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=1005, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_1005_0(Etw):
    pattern = Struct(
        "Pointer" / Int64ul,
        "RefCount" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=1006, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_1006_0(Etw):
    pattern = Struct(
        "Pointer" / Int64ul,
        "RefCount" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=1007, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_1007_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=1008, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_1008_0(Etw):
    pattern = Struct(
        "Pointer" / Int64ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=1009, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_1009_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul,
        "DwordName2" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=1010, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_1010_0(Etw):
    pattern = Struct(
        "Pointer" / Int64ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=1100, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_1100_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul,
        "DwordName2" / Int32ul,
        "DwordName3" / Int32ul,
        "supSvcDataStatus" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=1102, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_1102_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul,
        "DwordName2" / Int32ul,
        "DwordName3" / Int32ul,
        "supSvcDataStatus" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=1105, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_1105_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul,
        "DwordName2" / Int32ul,
        "DwordName3" / Int32ul,
        "supSvcDataStatus" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=1106, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_1106_0(Etw):
    pattern = Struct(
        "Pointer" / Int64ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=1107, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_1107_0(Etw):
    pattern = Struct(
        "Pointer" / Int64ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=1108, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_1108_0(Etw):
    pattern = Struct(
        "Pointer" / Int64ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=1109, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_1109_0(Etw):
    pattern = Struct(
        "Pointer" / Int64ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=1110, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_1110_0(Etw):
    pattern = Struct(
        "Reason" / Int32ul,
        "ServiceStatus" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=1111, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_1111_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=1112, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_1112_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=1200, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_1200_0(Etw):
    pattern = Struct(
        "Pointer" / Int64ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=1201, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_1201_0(Etw):
    pattern = Struct(
        "Pointer" / Int64ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=1203, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_1203_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=1204, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_1204_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=1205, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_1205_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=1207, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_1207_0(Etw):
    pattern = Struct(
        "HResultName" / Int32sl
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=1300, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_1300_0(Etw):
    pattern = Struct(
        "DwordName" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=1301, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_1301_0(Etw):
    pattern = Struct(
        "FunctionName" / CString,
        "cbBytes" / Int32ul,
        "Bytes" / Int8ul,
        "Pointer1" / Int64ul,
        "Pointer2" / Int64ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=1400, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_1400_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=1600, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_1600_0(Etw):
    pattern = Struct(
        "Pointer" / Int64ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=1601, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_1601_0(Etw):
    pattern = Struct(
        "Pointer" / Int64ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=1603, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_1603_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul,
        "DwordName2" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=1604, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_1604_0(Etw):
    pattern = Struct(
        "BooleanName" / Int8ul,
        "DwordName1" / Int32ul,
        "DwordName2" / Int32ul,
        "DwordName3" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=1605, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_1605_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=1606, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_1606_0(Etw):
    pattern = Struct(
        "UiccSlotStateName1" / Int32ul,
        "UiccSlotStateName2" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=1607, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_1607_0(Etw):
    pattern = Struct(
        "UiccSlotStateName" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=1608, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_1608_0(Etw):
    pattern = Struct(
        "UiccSlotStateName" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=1610, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_1610_0(Etw):
    pattern = Struct(
        "UiccSlotStateName" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=1700, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_1700_0(Etw):
    pattern = Struct(
        "Pointer" / Int64ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=1701, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_1701_0(Etw):
    pattern = Struct(
        "Pointer" / Int64ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=1702, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_1702_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul,
        "DwordName2" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=1703, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_1703_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul
    )


@declare(guid=guid("6b7b5e3a-f4de-42d9-9545-bae12852d778"), event_id=1704, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellularAPI_1704_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul,
        "DwordName2" / Int32ul
    )

