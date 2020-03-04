# -*- coding: utf-8 -*-
"""
Microsoft-Windows-DeviceManagement-Enterprise-Diagnostics-Provider
GUID : 3da494e4-0fe2-415c-b895-fb5265c5c83b
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=3, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_3_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=5, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_5_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=7, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_7_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=9, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_9_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=11, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_11_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=15, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_15_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=17, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_17_0(Etw):
    pattern = Struct(
        "HexInt1" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=19, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_19_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=20, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_20_0(Etw):
    pattern = Struct(
        "Message1" / WString
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=21, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_21_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=23, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_23_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=25, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_25_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=26, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_26_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=27, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_27_0(Etw):
    pattern = Struct(
        "HexInt1" / Int32ul,
        "HexInt2" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=32, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_32_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=36, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_36_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString,
        "HexInt1" / Int32ul,
        "HexInt2" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=42, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_42_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=44, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_44_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=46, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_46_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=49, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_49_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=52, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_52_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=53, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_53_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=55, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_55_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=56, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_56_0(Etw):
    pattern = Struct(
        "Message1" / WString
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=57, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_57_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=59, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_59_0(Etw):
    pattern = Struct(
        "Message1" / WString
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=60, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_60_0(Etw):
    pattern = Struct(
        "Message1" / WString
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=61, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_61_0(Etw):
    pattern = Struct(
        "Message1" / WString
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=62, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_62_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=64, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_64_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=65, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_65_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=66, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_66_0(Etw):
    pattern = Struct(
        "Message1" / WString
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=67, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_67_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=68, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_68_0(Etw):
    pattern = Struct(
        "UInt1" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=70, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_70_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=71, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_71_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=75, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_75_0(Etw):
    pattern = Struct(
        "HexInt1" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=76, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_76_0(Etw):
    pattern = Struct(
        "HexInt1" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=77, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_77_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=78, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_78_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=79, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_79_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=80, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_80_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=81, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_81_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=82, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_82_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=83, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_83_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=84, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_84_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=100, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_100_0(Etw):
    pattern = Struct(
        "HexInt1" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=101, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_101_0(Etw):
    pattern = Struct(
        "HexInt1" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=102, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_102_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=103, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_103_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=104, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_104_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=105, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_105_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=106, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_106_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=107, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_107_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=108, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_108_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=109, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_109_0(Etw):
    pattern = Struct(
        "HexInt1" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=110, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_110_0(Etw):
    pattern = Struct(
        "HexInt1" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=111, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_111_0(Etw):
    pattern = Struct(
        "Boolean1" / Int8ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=201, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_201_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=203, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_203_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=204, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_204_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=206, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_206_0(Etw):
    pattern = Struct(
        "Message1" / WString
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=207, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_207_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=208, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_208_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString,
        "Message4" / WString,
        "HexInt1" / Int32ul,
        "HexInt2" / Int32ul,
        "HexInt3" / Int32ul,
        "UInt1" / Int32ul,
        "UInt2" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=209, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_209_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=210, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_210_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=211, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_211_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "HexInt1" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=212, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_212_0(Etw):
    pattern = Struct(
        "HRESULT1" / Int32ul,
        "HRESULT2" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=213, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_213_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HexInt1" / Int32ul,
        "HexInt2" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=214, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_214_0(Etw):
    pattern = Struct(
        "Message1" / CString,
        "HexInt1" / Int32ul,
        "HexInt2" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=215, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_215_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=216, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_216_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=217, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_217_0(Etw):
    pattern = Struct(
        "HexInt1" / Int32ul,
        "HexInt2" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=218, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_218_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HexInt1" / Int32ul,
        "HexInt2" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=219, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_219_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=220, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_220_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HexInt1" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=221, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_221_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=222, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_222_0(Etw):
    pattern = Struct(
        "HexInt1" / Int32ul,
        "HexInt2" / Int32ul,
        "HexInt3" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=223, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_223_0(Etw):
    pattern = Struct(
        "Message1" / WString
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=224, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_224_0(Etw):
    pattern = Struct(
        "HexInt1" / Int32ul,
        "HexInt2" / Int32ul,
        "HexInt3" / Int32ul,
        "HexInt4" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=225, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_225_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=226, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_226_0(Etw):
    pattern = Struct(
        "HexInt1" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=227, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_227_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=228, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_228_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / CString
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=229, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_229_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / CString,
        "HexInt1" / Int32ul,
        "HexInt2" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=230, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_230_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "HexInt1" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=231, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_231_0(Etw):
    pattern = Struct(
        "HexInt1" / Int32ul,
        "HexInt2" / Int32ul,
        "HRESULT" / Int32ul,
        "FileTime1" / Int64ul,
        "FileTime2" / Int64ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=232, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_232_0(Etw):
    pattern = Struct(
        "HexInt1" / Int32ul,
        "HexInt2" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=301, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_301_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=302, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_302_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=303, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_303_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=304, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_304_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=305, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_305_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=306, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_306_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString,
        "Message4" / WString,
        "HexInt1" / Int32ul,
        "HexInt3" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=307, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_307_0(Etw):
    pattern = Struct(
        "Message1" / CString
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=308, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_308_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=309, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_309_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString,
        "Message4" / WString,
        "HexInt1" / Int32ul,
        "HexInt2" / Int32ul,
        "HexInt3" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=310, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_310_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=400, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_400_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString,
        "Message4" / CString,
        "Message5" / WString,
        "HexInt1" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=401, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_401_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString,
        "Message4" / WString,
        "Message5" / WString,
        "Message6" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=402, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_402_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HexInt1" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=403, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_403_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HexInt1" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=404, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_404_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString,
        "InternalCmdType" / Int32ul,
        "Message5" / WString,
        "HexInt1" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=450, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_450_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString,
        "Message4" / CString,
        "Message5" / WString,
        "HexInt1" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=451, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_451_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString,
        "Message4" / WString,
        "Message5" / WString,
        "Message6" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=452, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_452_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HexInt1" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=453, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_453_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HexInt1" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=454, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_454_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString,
        "InternalCmdType" / Int32ul,
        "Message5" / WString,
        "HexInt1" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=600, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_600_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=601, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_601_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=700, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_700_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=800, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_800_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HexInt1" / Int32ul,
        "HexInt2" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=801, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_801_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HexInt1" / Int32ul,
        "HexInt2" / Int32ul,
        "HexInt3" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=802, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_802_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HexInt1" / Int32ul,
        "HexInt2" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=803, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_803_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HexInt1" / Int32ul,
        "HexInt2" / Int32ul,
        "HexInt3" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=805, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_805_0(Etw):
    pattern = Struct(
        "HexInt1" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=806, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_806_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString,
        "UInt1" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=807, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_807_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString,
        "UInt1" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=808, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_808_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString,
        "UInt1" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=809, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_809_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString,
        "Message4" / WString,
        "HexInt1" / Int32ul,
        "HexInt2" / Int32ul,
        "HexInt3" / Int32ul,
        "HexInt4" / Int32ul,
        "HexInt5" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=810, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_810_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString,
        "Message4" / WString,
        "Message5" / WString,
        "HexInt1" / Int32ul,
        "HexInt2" / Int32ul,
        "HexInt3" / Int32ul,
        "HexInt4" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=811, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_811_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString,
        "Message4" / WString,
        "HexInt1" / Int32ul,
        "HexInt2" / Int32ul,
        "HexInt3" / Int32ul,
        "HexInt4" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=812, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_812_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString,
        "Message4" / WString,
        "HexInt1" / Int32ul,
        "HexInt2" / Int32ul,
        "HexInt3" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=813, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_813_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString,
        "Message4" / WString,
        "HexInt1" / Int32ul,
        "HexInt2" / Int32ul,
        "HexInt3" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=814, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_814_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString,
        "Message4" / WString,
        "Message5" / WString,
        "HexInt1" / Int32ul,
        "HexInt2" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=815, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_815_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString,
        "Message4" / WString,
        "HexInt1" / Int32ul,
        "HexInt2" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=817, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_817_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "HexInt1" / Int32ul,
        "HexInt2" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=818, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_818_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString,
        "Message4" / WString,
        "HexInt1" / Int32ul,
        "HexInt2" / Int32ul,
        "HexInt3" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=819, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_819_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString,
        "Message4" / WString,
        "HexInt1" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=820, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_820_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "HexInt1" / Int32ul,
        "HexInt2" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=821, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_821_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "HexInt3" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=822, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_822_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "HexInt3" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=823, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_823_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "HexInt3" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=824, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_824_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "HexInt3" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=825, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_825_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "HexInt3" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=826, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_826_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "HexInt3" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=827, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_827_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "HexInt3" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=828, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_828_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "HexInt3" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=829, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_829_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "HexInt1" / Int32ul,
        "HexInt2" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=830, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_830_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "HexInt1" / Int32ul,
        "HexInt2" / Int32ul,
        "HexInt3" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=831, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_831_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "HexInt1" / Int32ul,
        "HexInt2" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=832, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_832_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "HexInt1" / Int32ul,
        "HexInt2" / Int32ul,
        "HexInt3" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=833, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_833_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HexInt1" / Int32ul,
        "HexInt2" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=834, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_834_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HexInt1" / Int32ul,
        "HexInt2" / Int32ul,
        "HexInt3" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=835, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_835_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=836, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_836_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString,
        "UInt1" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=837, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_837_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=838, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_838_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString,
        "UInt1" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=839, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_839_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=840, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_840_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "HexInt3" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=841, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_841_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=842, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_842_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString,
        "UInt1" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=843, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_843_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString,
        "UInt1" / Int32ul,
        "UInt2" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=844, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_844_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=845, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_845_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HexInt1" / Int32ul,
        "HexInt2" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=846, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_846_0(Etw):
    pattern = Struct(
        "HexInt1" / Int32ul,
        "HexInt2" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=848, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_848_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "HexInt3" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=849, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_849_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString,
        "UInt1" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=850, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_850_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=851, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_851_0(Etw):
    pattern = Struct(
        "Message1" / WString
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=852, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_852_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=853, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_853_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=854, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_854_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "HexInt1" / Int32ul,
        "HexInt2" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=855, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_855_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HexInt1" / Int32ul,
        "HexInt2" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=856, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_856_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HexInt1" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=857, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_857_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HexInt1" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=858, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_858_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HexInt1" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=859, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_859_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString,
        "UInt1" / Int32ul,
        "UInt2" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=860, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_860_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString,
        "UInt1" / Int32ul,
        "UInt2" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=861, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_861_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "HexInt1" / Int32ul,
        "HexInt2" / Int32ul,
        "HexInt3" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=862, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_862_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HexInt1" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=863, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_863_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "HexInt3" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=864, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_864_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "HexInt3" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=865, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_865_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString,
        "Message4" / WString,
        "HexInt1" / Int32ul,
        "HexInt3" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=866, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_866_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString,
        "Message4" / WString,
        "Message5" / WString
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=867, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_867_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString,
        "Message4" / WString,
        "HexInt1" / Int32ul,
        "HexInt3" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=868, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_868_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "HexInt3" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=869, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_869_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HexInt1" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=870, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_870_0(Etw):
    pattern = Struct(
        "HexInt1" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=871, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_871_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString,
        "Message4" / WString,
        "HexInt1" / Int32ul,
        "HexInt3" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=872, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_872_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString,
        "Message4" / WString,
        "HexInt1" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=873, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_873_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString,
        "Message4" / WString
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=880, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_880_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString,
        "UInt1" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=881, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_881_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=900, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_900_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=901, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_901_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=902, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_902_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=903, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_903_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=904, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_904_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=905, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_905_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=906, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_906_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=907, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_907_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=908, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_908_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=909, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_909_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=910, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_910_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=911, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_911_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=912, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_912_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=913, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_913_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=914, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_914_0(Etw):
    pattern = Struct(
        "Message1" / WString
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=915, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_915_0(Etw):
    pattern = Struct(
        "Message1" / WString
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=916, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_916_0(Etw):
    pattern = Struct(
        "Message1" / WString
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=917, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_917_0(Etw):
    pattern = Struct(
        "Message1" / WString
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=918, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_918_0(Etw):
    pattern = Struct(
        "Message1" / WString
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1100, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1100_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1102, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1102_0(Etw):
    pattern = Struct(
        "Message1" / WString
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1103, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1103_0(Etw):
    pattern = Struct(
        "HexInt1" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1104, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1104_0(Etw):
    pattern = Struct(
        "HexInt1" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1105, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1105_0(Etw):
    pattern = Struct(
        "HexInt1" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1106, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1106_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1107, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1107_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1108, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1108_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1109, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1109_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1110, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1110_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1111, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1111_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString,
        "UInt1" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1112, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1112_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString,
        "UInt1" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1113, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1113_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1114, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1114_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1115, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1115_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1116, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1116_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1117, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1117_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1118, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1118_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1119, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1119_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1120, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1120_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1121, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1121_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1122, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1122_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1123, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1123_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1124, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1124_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1125, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1125_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1126, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1126_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1127, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1127_0(Etw):
    pattern = Struct(
        "HexInt1" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1128, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1128_0(Etw):
    pattern = Struct(
        "UInt1" / Int32ul,
        "Message1" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1500, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1500_0(Etw):
    pattern = Struct(
        "UInt1" / Int32ul,
        "Message1" / WString
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1501, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1501_0(Etw):
    pattern = Struct(
        "UInt1" / Int32ul,
        "UInt2" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1502, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1502_0(Etw):
    pattern = Struct(
        "UInt1" / Int32ul,
        "Message1" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1503, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1503_0(Etw):
    pattern = Struct(
        "UInt1" / Int32ul,
        "Message1" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1504, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1504_0(Etw):
    pattern = Struct(
        "UInt1" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1505, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1505_0(Etw):
    pattern = Struct(
        "UInt1" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1506, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1506_0(Etw):
    pattern = Struct(
        "UInt1" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1507, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1507_0(Etw):
    pattern = Struct(
        "UInt1" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1508, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1508_0(Etw):
    pattern = Struct(
        "UInt1" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1509, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1509_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1510, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1510_0(Etw):
    pattern = Struct(
        "UInt1" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1511, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1511_0(Etw):
    pattern = Struct(
        "UInt1" / Int32ul,
        "Message1" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1534, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1534_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1535, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1535_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1536, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1536_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1537, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1537_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1538, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1538_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1539, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1539_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1600, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1600_0(Etw):
    pattern = Struct(
        "Message1" / WString
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1601, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1601_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1650, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1650_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1651, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1651_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "HexInt3" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1652, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1652_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1653, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1653_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString,
        "Message4" / WString,
        "HexInt1" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1701, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1701_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1702, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1702_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1703, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1703_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1705, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1705_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1706, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1706_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1707, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1707_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1708, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1708_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1901, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1901_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1902, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1902_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1903, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1903_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1905, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1905_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1906, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1906_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1907, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1907_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString,
        "Message4" / WString,
        "HexInt1" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1908, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1908_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1909, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1909_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1911, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1911_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1913, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1913_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1914, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1914_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1915, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1915_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1916, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1916_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1920, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1920_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1921, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1921_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1922, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1922_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1923, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1923_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1924, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1924_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString,
        "Message4" / WString,
        "HexInt1" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1925, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1925_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString,
        "Message4" / WString,
        "HexInt1" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1926, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1926_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1927, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1927_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1928, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1928_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HexInt1" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1930, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1930_0(Etw):
    pattern = Struct(
        "HexInt1" / Int32ul,
        "HexInt2" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1931, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1931_0(Etw):
    pattern = Struct(
        "Message1" / WString
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1932, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1932_0(Etw):
    pattern = Struct(
        "Message1" / WString
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=1933, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_1933_0(Etw):
    pattern = Struct(
        "Message1" / WString
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=2002, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_2002_0(Etw):
    pattern = Struct(
        "Message1" / WString
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=2003, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_2003_0(Etw):
    pattern = Struct(
        "Message1" / WString
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=2005, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_2005_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=2006, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_2006_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=2007, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_2007_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=2008, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_2008_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=2009, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_2009_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=2010, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_2010_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=2101, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_2101_0(Etw):
    pattern = Struct(
        "Message1" / WString
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=2102, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_2102_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=2103, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_2103_0(Etw):
    pattern = Struct(
        "Message1" / WString
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=2104, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_2104_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=2105, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_2105_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=2106, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_2106_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=2107, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_2107_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=2108, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_2108_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=2109, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_2109_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=2110, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_2110_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=2111, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_2111_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=2112, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_2112_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=2200, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_2200_0(Etw):
    pattern = Struct(
        "Message1" / WString
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=2201, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_2201_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=2202, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_2202_0(Etw):
    pattern = Struct(
        "Message1" / WString
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=2203, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_2203_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=2204, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_2204_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=2205, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_2205_0(Etw):
    pattern = Struct(
        "Message1" / WString
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=2206, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_2206_0(Etw):
    pattern = Struct(
        "Message1" / WString
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=2208, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_2208_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HexInt1" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=2209, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_2209_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=2210, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_2210_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=2211, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_2211_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=2212, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_2212_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=2213, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_2213_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=2214, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_2214_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=2215, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_2215_0(Etw):
    pattern = Struct(
        "HexInt1" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=2216, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_2216_0(Etw):
    pattern = Struct(
        "HexInt1" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=2219, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_2219_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=2220, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_2220_0(Etw):
    pattern = Struct(
        "HexInt1" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=2221, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_2221_0(Etw):
    pattern = Struct(
        "Message1" / WString
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=2223, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_2223_0(Etw):
    pattern = Struct(
        "Message1" / WString
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=2300, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_2300_0(Etw):
    pattern = Struct(
        "HexInt1" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=2400, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_2400_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString,
        "Message4" / WString,
        "Message5" / WString,
        "HexInt1" / Int32ul,
        "HexInt2" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=2401, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_2401_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString,
        "Message4" / WString,
        "Message5" / WString,
        "HexInt1" / Int32ul,
        "HexInt2" / Int32ul,
        "HexInt3" / Int32ul,
        "HexInt4" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=2402, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_2402_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString,
        "Message4" / WString,
        "Message5" / WString,
        "Message6" / WString,
        "Message7" / WString,
        "HexInt1" / Int32ul,
        "HexInt2" / Int32ul,
        "HexInt3" / Int32ul,
        "HexInt4" / Int32ul,
        "HexInt5" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=2403, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_2403_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString,
        "Message4" / WString,
        "Message5" / WString,
        "Message6" / WString,
        "Message7" / WString,
        "HexInt1" / Int32ul,
        "HexInt2" / Int32ul,
        "HexInt3" / Int32ul,
        "HexInt4" / Int32ul,
        "HexInt5" / Int32ul,
        "HexInt6" / Int32ul,
        "HexInt7" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=2404, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_2404_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString,
        "Message4" / WString,
        "Message5" / WString,
        "Message6" / WString,
        "Message7" / WString,
        "HexInt1" / Int32ul,
        "HexInt2" / Int32ul,
        "HexInt3" / Int32ul,
        "HexInt4" / Int32ul,
        "HexInt5" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=2405, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_2405_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString,
        "Message4" / WString,
        "Message5" / WString,
        "Message6" / WString,
        "Message7" / WString,
        "HexInt1" / Int32ul,
        "HexInt2" / Int32ul,
        "HexInt3" / Int32ul,
        "HexInt4" / Int32ul,
        "HexInt5" / Int32ul,
        "HexInt6" / Int32ul,
        "HexInt7" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=2406, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_2406_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=2407, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_2407_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString,
        "UInt1" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=2409, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_2409_0(Etw):
    pattern = Struct(
        "HexInt1" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=2410, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_2410_0(Etw):
    pattern = Struct(
        "HexInt1" / Int32ul,
        "HexInt2" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=2411, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_2411_0(Etw):
    pattern = Struct(
        "HexInt1" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=2412, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_2412_0(Etw):
    pattern = Struct(
        "HexInt1" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=2416, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_2416_0(Etw):
    pattern = Struct(
        "HexInt1" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=2420, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_2420_0(Etw):
    pattern = Struct(
        "HexInt1" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=2424, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_2424_0(Etw):
    pattern = Struct(
        "HexInt1" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=2428, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_2428_0(Etw):
    pattern = Struct(
        "HexInt1" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=2432, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_2432_0(Etw):
    pattern = Struct(
        "HexInt1" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=2436, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_2436_0(Etw):
    pattern = Struct(
        "HexInt1" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=2440, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_2440_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=2441, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_2441_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString
    )


@declare(guid=guid("3da494e4-0fe2-415c-b895-fb5265c5c83b"), event_id=2442, version=0)
class Microsoft_Windows_DeviceManagement_Enterprise_Diagnostics_Provider_2442_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString,
        "HexInt1" / Int32ul,
        "HexInt2" / Int32ul
    )

