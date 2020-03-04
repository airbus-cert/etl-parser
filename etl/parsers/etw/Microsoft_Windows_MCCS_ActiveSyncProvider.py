# -*- coding: utf-8 -*-
"""
Microsoft-Windows-MCCS-ActiveSyncProvider
GUID : 4a155f10-25ad-47e6-aba8-2c4f5eee7846
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=1, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_1_0(Etw):
    pattern = Struct(
        "P1_HResult" / Int32sl,
        "P2_String" / CString,
        "P3_UInt32" / Int32ul
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=2, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_2_0(Etw):
    pattern = Struct(
        "P1_HResult" / Int32sl,
        "P2_String" / CString,
        "P3_UInt32" / Int32ul
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=101, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_101_0(Etw):
    pattern = Struct(
        "Prop_String" / WString,
        "Prop_HResult" / Int32sl
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=102, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_102_0(Etw):
    pattern = Struct(
        "Prop_String" / WString,
        "Prop_HResult" / Int32sl
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=103, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_103_0(Etw):
    pattern = Struct(
        "Prop_String" / WString,
        "Prop_HResult" / Int32sl
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=301, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_301_0(Etw):
    pattern = Struct(
        "Prop_Dword1" / Int32ul,
        "Prop_Dword2" / Int32ul,
        "Prop_Dword3" / Int32ul
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=302, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_302_0(Etw):
    pattern = Struct(
        "Prop_Dword" / Int32ul
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=303, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_303_0(Etw):
    pattern = Struct(
        "Prop_Dword" / Int32ul
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=304, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_304_0(Etw):
    pattern = Struct(
        "Prop_Dword1" / Int32ul,
        "Prop_String1" / CString,
        "Prop_String2" / WString,
        "Prop_Dword2" / Int32ul,
        "Prop_Dword3" / Int32ul,
        "Prop_Dword4" / Int32ul,
        "Prop_Status" / Int32ul
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=308, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_308_0(Etw):
    pattern = Struct(
        "Prop_String_1" / WString,
        "Prop_String_2" / WString,
        "Prop_String_3" / WString
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=309, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_309_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul,
        "Prop_String" / WString,
        "Prop_Dword_2" / Int32ul,
        "Prop_Dword_3" / Int32ul,
        "Prop_Bool" / Int8ul
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=310, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_310_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul,
        "Prop_String" / WString,
        "Prop_Dword_2" / Int32ul,
        "Prop_Dword_3" / Int32ul
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=312, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_312_0(Etw):
    pattern = Struct(
        "Prop_String1" / WString,
        "Prop_Dword_1" / Int32ul
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=313, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_313_0(Etw):
    pattern = Struct(
        "Prop_String1" / WString,
        "Prop_Dword_1" / Int32ul
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=314, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_314_0(Etw):
    pattern = Struct(
        "Prop_String1" / WString,
        "Prop_Dword_1" / Int32ul,
        "Prop_Dword_2" / Int32ul
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=315, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_315_0(Etw):
    pattern = Struct(
        "Prop_String1" / WString,
        "Prop_Dword_1" / Int32ul,
        "Prop_Dword_2" / Int32ul
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=316, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_316_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul,
        "Prop_String1" / WString,
        "Prop_String2" / WString
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=317, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_317_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul,
        "Prop_String1" / WString,
        "Prop_String2" / WString
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=318, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_318_0(Etw):
    pattern = Struct(
        "Prop_Dword" / Int32ul
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=319, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_319_0(Etw):
    pattern = Struct(
        "Prop_Dword1" / Int32ul,
        "Prop_Dword2" / Int32ul
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=320, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_320_0(Etw):
    pattern = Struct(
        "Prop_Dword" / Int32ul,
        "Prop_String" / WString
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=321, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_321_0(Etw):
    pattern = Struct(
        "Prop_Dword1" / Int32ul,
        "Prop_Dword2" / Int32ul,
        "Prop_String" / WString
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=322, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_322_0(Etw):
    pattern = Struct(
        "Prop_Dword1" / Int32ul,
        "Prop_Dword2" / Int32ul,
        "Prop_String" / WString
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=323, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_323_0(Etw):
    pattern = Struct(
        "Prop_Dword1" / Int32ul,
        "Prop_Dword2" / Int32ul,
        "Prop_String" / WString
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=324, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_324_0(Etw):
    pattern = Struct(
        "Prop_Dword" / Int32ul,
        "Prop_String" / WString
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=325, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_325_0(Etw):
    pattern = Struct(
        "Prop_Dword" / Int32ul
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=326, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_326_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul,
        "Prop_String1" / WString
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=327, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_327_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul,
        "Prop_String1" / WString
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=328, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_328_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul,
        "Prop_String1" / WString
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=329, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_329_0(Etw):
    pattern = Struct(
        "Prop_String" / WString
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=330, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_330_0(Etw):
    pattern = Struct(
        "Prop_String" / WString
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=331, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_331_0(Etw):
    pattern = Struct(
        "Prop_String1" / WString,
        "Prop_Dword_1" / Int32ul,
        "Prop_Dword_2" / Int32ul
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=332, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_332_0(Etw):
    pattern = Struct(
        "Prop_String" / WString
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=333, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_333_0(Etw):
    pattern = Struct(
        "Prop_String1" / WString,
        "Prop_Dword1" / Int32ul,
        "Prop_String2" / WString,
        "Prop_Dword2" / Int32ul,
        "Prop_String3" / WString,
        "Prop_Dword3" / Int32ul
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=334, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_334_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul,
        "Prop_String1" / WString,
        "Prop_String2" / WString
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=335, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_335_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul,
        "Prop_String1" / WString,
        "Prop_String2" / WString,
        "Prop_Dword_2" / Int32ul
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=336, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_336_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul,
        "Prop_String1" / WString,
        "Prop_String2" / WString,
        "Prop_Dword_2" / Int32ul
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=402, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_402_0(Etw):
    pattern = Struct(
        "Prop_ContentLengthBytes" / Int32sl,
        "Prop_ContentChars" / CString
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=421, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_421_0(Etw):
    pattern = Struct(
        "Prop_String" / WString,
        "Prop_HResult" / Int32sl
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=422, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_422_0(Etw):
    pattern = Struct(
        "Prop_String" / WString,
        "Prop_HResult" / Int32sl
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=423, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_423_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul,
        "Prop_String1" / WString,
        "Prop_Dword_2" / Int32ul,
        "Prop_HResult" / Int32sl
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=501, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_501_0(Etw):
    pattern = Struct(
        "Prop_Dword" / Int32ul
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=510, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_510_0(Etw):
    pattern = Struct(
        "Prop_Length" / Int32ul,
        "Prop_String" / Bytes(lambda this: this.Prop_Length)
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=511, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_511_0(Etw):
    pattern = Struct(
        "Prop_String" / WString
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=512, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_512_0(Etw):
    pattern = Struct(
        "Prop_String_1" / WString,
        "Prop_String_2" / WString
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=513, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_513_0(Etw):
    pattern = Struct(
        "Prop_String_1" / WString,
        "Prop_String_2" / WString
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=514, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_514_0(Etw):
    pattern = Struct(
        "Prop_String_1" / WString,
        "Prop_String_2" / WString,
        "Prop_String_3" / WString
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=515, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_515_0(Etw):
    pattern = Struct(
        "Prop_String1" / WString,
        "Prop_String2" / WString,
        "Prop_Length" / Int32ul,
        "Prop_Binary" / Bytes(lambda this: this.Prop_Length)
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=517, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_517_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul,
        "Prop_Dword_2" / Int32ul
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=518, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_518_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul,
        "Prop_Dword_2" / Int32ul
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=519, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_519_0(Etw):
    pattern = Struct(
        "Prop_String" / WString
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=520, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_520_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul,
        "Prop_Dword_2" / Int32ul
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=521, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_521_0(Etw):
    pattern = Struct(
        "Prop_Dword" / Int32ul
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=522, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_522_0(Etw):
    pattern = Struct(
        "Prop_Dword" / Int32ul
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=523, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_523_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul,
        "Prop_Dword_2" / Int32ul,
        "Prop_String1" / WString,
        "Prop_String2" / WString
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=524, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_524_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul,
        "Prop_String1" / WString,
        "Prop_String2" / WString
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=525, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_525_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul,
        "Prop_String1" / WString
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=526, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_526_0(Etw):
    pattern = Struct(
        "Prop_String" / WString
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=527, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_527_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul,
        "Prop_String1" / WString
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=528, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_528_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul,
        "Prop_String1" / WString
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=529, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_529_0(Etw):
    pattern = Struct(
        "Prop_String" / WString
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=530, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_530_0(Etw):
    pattern = Struct(
        "Prop_String" / WString
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=531, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_531_0(Etw):
    pattern = Struct(
        "Prop_Guid" / Guid
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=532, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_532_0(Etw):
    pattern = Struct(
        "Prop_Guid" / Guid,
        "Prop_String" / WString
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=533, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_533_0(Etw):
    pattern = Struct(
        "Prop_Guid" / Guid,
        "Prop_String1" / WString,
        "Prop_String2" / WString
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=534, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_534_0(Etw):
    pattern = Struct(
        "Prop_Guid" / Guid
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=535, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_535_0(Etw):
    pattern = Struct(
        "Prop_Guid" / Guid,
        "Prop_String1" / WString,
        "Prop_String2" / WString
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=536, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_536_0(Etw):
    pattern = Struct(
        "Prop_String_1" / WString,
        "Prop_String_2" / WString
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=537, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_537_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul,
        "Prop_Dword_2" / Int32ul,
        "Prop_Dword_3" / Int32ul
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=538, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_538_0(Etw):
    pattern = Struct(
        "Prop_String" / WString
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=551, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_551_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul,
        "Prop_Dword_2" / Int32ul
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=646, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_646_0(Etw):
    pattern = Struct(
        "Prop_Dword" / Int32ul
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=647, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_647_0(Etw):
    pattern = Struct(
        "Prop_Dword" / Int32ul
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=801, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_801_0(Etw):
    pattern = Struct(
        "Prop_Dword" / Int32ul
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=803, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_803_0(Etw):
    pattern = Struct(
        "Prop_Dword" / Int32ul,
        "Prop_HRESULT" / Int32ul
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=804, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_804_0(Etw):
    pattern = Struct(
        "Prop_Dword" / Int32ul
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=805, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_805_0(Etw):
    pattern = Struct(
        "Prop_Dword" / Int32ul
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=807, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_807_0(Etw):
    pattern = Struct(
        "Prop_Dword" / Int32ul
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=808, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_808_0(Etw):
    pattern = Struct(
        "Prop_Dword" / Int32ul
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=809, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_809_0(Etw):
    pattern = Struct(
        "Prop_Dword" / Int32ul
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=850, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_850_0(Etw):
    pattern = Struct(
        "Prop_Dword" / Int32ul,
        "Prop_HRESULT" / Int32ul
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=851, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_851_0(Etw):
    pattern = Struct(
        "Prop_Ulong" / Int64ul,
        "Prop_Hex" / Int32ul
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=852, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_852_0(Etw):
    pattern = Struct(
        "Prop_HRESULT" / Int32ul,
        "Prop_String1" / WString,
        "Prop_Dword" / Int32ul
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=901, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_901_0(Etw):
    pattern = Struct(
        "Prop_Dword" / Int32ul,
        "Prop_HRESULT" / Int32ul
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=1010, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_1010_0(Etw):
    pattern = Struct(
        "Prop_Guid" / Guid,
        "Prop_HexInt32" / Int32ul
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=1011, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_1011_0(Etw):
    pattern = Struct(
        "Prop_Guid" / Guid,
        "Prop_HexInt32" / Int32ul
    )


@declare(guid=guid("4a155f10-25ad-47e6-aba8-2c4f5eee7846"), event_id=1021, version=0)
class Microsoft_Windows_MCCS_ActiveSyncProvider_1021_0(Etw):
    pattern = Struct(
        "Prop_Dword" / Int32ul
    )

