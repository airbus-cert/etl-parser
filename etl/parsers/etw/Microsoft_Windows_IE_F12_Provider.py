# -*- coding: utf-8 -*-
"""
Microsoft-Windows-IE-F12-Provider
GUID : d17fff2f-392d-478c-a41d-737a216eb2a4
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=101, version=0)
class Microsoft_Windows_IE_F12_Provider_101_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=102, version=0)
class Microsoft_Windows_IE_F12_Provider_102_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=103, version=0)
class Microsoft_Windows_IE_F12_Provider_103_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=104, version=0)
class Microsoft_Windows_IE_F12_Provider_104_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=105, version=0)
class Microsoft_Windows_IE_F12_Provider_105_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=106, version=0)
class Microsoft_Windows_IE_F12_Provider_106_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=107, version=0)
class Microsoft_Windows_IE_F12_Provider_107_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=108, version=0)
class Microsoft_Windows_IE_F12_Provider_108_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=109, version=0)
class Microsoft_Windows_IE_F12_Provider_109_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=110, version=0)
class Microsoft_Windows_IE_F12_Provider_110_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=111, version=0)
class Microsoft_Windows_IE_F12_Provider_111_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=112, version=0)
class Microsoft_Windows_IE_F12_Provider_112_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=113, version=0)
class Microsoft_Windows_IE_F12_Provider_113_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=114, version=0)
class Microsoft_Windows_IE_F12_Provider_114_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=115, version=0)
class Microsoft_Windows_IE_F12_Provider_115_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=116, version=0)
class Microsoft_Windows_IE_F12_Provider_116_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=117, version=0)
class Microsoft_Windows_IE_F12_Provider_117_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=118, version=0)
class Microsoft_Windows_IE_F12_Provider_118_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=119, version=0)
class Microsoft_Windows_IE_F12_Provider_119_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=120, version=0)
class Microsoft_Windows_IE_F12_Provider_120_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=201, version=0)
class Microsoft_Windows_IE_F12_Provider_201_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=202, version=0)
class Microsoft_Windows_IE_F12_Provider_202_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=203, version=1)
class Microsoft_Windows_IE_F12_Provider_203_1(Etw):
    pattern = Struct(
        "Key" / Int32ul,
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=204, version=1)
class Microsoft_Windows_IE_F12_Provider_204_1(Etw):
    pattern = Struct(
        "Key" / Int32ul,
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=205, version=1)
class Microsoft_Windows_IE_F12_Provider_205_1(Etw):
    pattern = Struct(
        "Key" / Int32ul,
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=206, version=1)
class Microsoft_Windows_IE_F12_Provider_206_1(Etw):
    pattern = Struct(
        "Key" / Int32ul,
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=207, version=0)
class Microsoft_Windows_IE_F12_Provider_207_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=208, version=0)
class Microsoft_Windows_IE_F12_Provider_208_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=209, version=0)
class Microsoft_Windows_IE_F12_Provider_209_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=210, version=0)
class Microsoft_Windows_IE_F12_Provider_210_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=211, version=0)
class Microsoft_Windows_IE_F12_Provider_211_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=212, version=0)
class Microsoft_Windows_IE_F12_Provider_212_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=213, version=0)
class Microsoft_Windows_IE_F12_Provider_213_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=214, version=0)
class Microsoft_Windows_IE_F12_Provider_214_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=215, version=0)
class Microsoft_Windows_IE_F12_Provider_215_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=216, version=0)
class Microsoft_Windows_IE_F12_Provider_216_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=217, version=0)
class Microsoft_Windows_IE_F12_Provider_217_0(Etw):
    pattern = Struct(
        "Key" / Int32ul,
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=218, version=0)
class Microsoft_Windows_IE_F12_Provider_218_0(Etw):
    pattern = Struct(
        "Key" / Int32ul,
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=219, version=0)
class Microsoft_Windows_IE_F12_Provider_219_0(Etw):
    pattern = Struct(
        "Key" / Int32ul,
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=220, version=0)
class Microsoft_Windows_IE_F12_Provider_220_0(Etw):
    pattern = Struct(
        "Key" / Int32ul,
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=301, version=0)
class Microsoft_Windows_IE_F12_Provider_301_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=302, version=0)
class Microsoft_Windows_IE_F12_Provider_302_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=303, version=0)
class Microsoft_Windows_IE_F12_Provider_303_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=304, version=0)
class Microsoft_Windows_IE_F12_Provider_304_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=305, version=0)
class Microsoft_Windows_IE_F12_Provider_305_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=306, version=0)
class Microsoft_Windows_IE_F12_Provider_306_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=307, version=0)
class Microsoft_Windows_IE_F12_Provider_307_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=308, version=0)
class Microsoft_Windows_IE_F12_Provider_308_0(Etw):
    pattern = Struct(
        "Key" / Int32ul,
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=309, version=0)
class Microsoft_Windows_IE_F12_Provider_309_0(Etw):
    pattern = Struct(
        "Key" / Int32ul,
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=310, version=0)
class Microsoft_Windows_IE_F12_Provider_310_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=311, version=0)
class Microsoft_Windows_IE_F12_Provider_311_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=312, version=0)
class Microsoft_Windows_IE_F12_Provider_312_0(Etw):
    pattern = Struct(
        "Key" / Int32ul,
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=313, version=0)
class Microsoft_Windows_IE_F12_Provider_313_0(Etw):
    pattern = Struct(
        "Key" / Int32ul,
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=314, version=0)
class Microsoft_Windows_IE_F12_Provider_314_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=315, version=0)
class Microsoft_Windows_IE_F12_Provider_315_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=316, version=0)
class Microsoft_Windows_IE_F12_Provider_316_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=317, version=0)
class Microsoft_Windows_IE_F12_Provider_317_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=318, version=0)
class Microsoft_Windows_IE_F12_Provider_318_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=319, version=0)
class Microsoft_Windows_IE_F12_Provider_319_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=320, version=0)
class Microsoft_Windows_IE_F12_Provider_320_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=321, version=0)
class Microsoft_Windows_IE_F12_Provider_321_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=322, version=0)
class Microsoft_Windows_IE_F12_Provider_322_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=323, version=0)
class Microsoft_Windows_IE_F12_Provider_323_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=324, version=0)
class Microsoft_Windows_IE_F12_Provider_324_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=325, version=0)
class Microsoft_Windows_IE_F12_Provider_325_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=326, version=0)
class Microsoft_Windows_IE_F12_Provider_326_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=327, version=0)
class Microsoft_Windows_IE_F12_Provider_327_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=328, version=0)
class Microsoft_Windows_IE_F12_Provider_328_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=329, version=0)
class Microsoft_Windows_IE_F12_Provider_329_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=330, version=0)
class Microsoft_Windows_IE_F12_Provider_330_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=331, version=0)
class Microsoft_Windows_IE_F12_Provider_331_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=332, version=0)
class Microsoft_Windows_IE_F12_Provider_332_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=333, version=0)
class Microsoft_Windows_IE_F12_Provider_333_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=334, version=0)
class Microsoft_Windows_IE_F12_Provider_334_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=335, version=0)
class Microsoft_Windows_IE_F12_Provider_335_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=336, version=0)
class Microsoft_Windows_IE_F12_Provider_336_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=337, version=0)
class Microsoft_Windows_IE_F12_Provider_337_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=338, version=0)
class Microsoft_Windows_IE_F12_Provider_338_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=339, version=0)
class Microsoft_Windows_IE_F12_Provider_339_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=340, version=0)
class Microsoft_Windows_IE_F12_Provider_340_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=341, version=0)
class Microsoft_Windows_IE_F12_Provider_341_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=342, version=0)
class Microsoft_Windows_IE_F12_Provider_342_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=343, version=0)
class Microsoft_Windows_IE_F12_Provider_343_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=344, version=0)
class Microsoft_Windows_IE_F12_Provider_344_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=345, version=0)
class Microsoft_Windows_IE_F12_Provider_345_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=346, version=0)
class Microsoft_Windows_IE_F12_Provider_346_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=347, version=0)
class Microsoft_Windows_IE_F12_Provider_347_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=348, version=0)
class Microsoft_Windows_IE_F12_Provider_348_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=349, version=0)
class Microsoft_Windows_IE_F12_Provider_349_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=350, version=0)
class Microsoft_Windows_IE_F12_Provider_350_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=351, version=0)
class Microsoft_Windows_IE_F12_Provider_351_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=352, version=0)
class Microsoft_Windows_IE_F12_Provider_352_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=353, version=0)
class Microsoft_Windows_IE_F12_Provider_353_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=354, version=0)
class Microsoft_Windows_IE_F12_Provider_354_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=355, version=0)
class Microsoft_Windows_IE_F12_Provider_355_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=356, version=0)
class Microsoft_Windows_IE_F12_Provider_356_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=357, version=0)
class Microsoft_Windows_IE_F12_Provider_357_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=358, version=0)
class Microsoft_Windows_IE_F12_Provider_358_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=359, version=0)
class Microsoft_Windows_IE_F12_Provider_359_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=360, version=0)
class Microsoft_Windows_IE_F12_Provider_360_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=361, version=0)
class Microsoft_Windows_IE_F12_Provider_361_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=362, version=0)
class Microsoft_Windows_IE_F12_Provider_362_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=363, version=0)
class Microsoft_Windows_IE_F12_Provider_363_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=364, version=0)
class Microsoft_Windows_IE_F12_Provider_364_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=365, version=0)
class Microsoft_Windows_IE_F12_Provider_365_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=366, version=0)
class Microsoft_Windows_IE_F12_Provider_366_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=367, version=0)
class Microsoft_Windows_IE_F12_Provider_367_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=368, version=0)
class Microsoft_Windows_IE_F12_Provider_368_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=369, version=0)
class Microsoft_Windows_IE_F12_Provider_369_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=370, version=0)
class Microsoft_Windows_IE_F12_Provider_370_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=371, version=0)
class Microsoft_Windows_IE_F12_Provider_371_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=372, version=1)
class Microsoft_Windows_IE_F12_Provider_372_1(Etw):
    pattern = Struct(
        "Key" / Int32ul,
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=373, version=1)
class Microsoft_Windows_IE_F12_Provider_373_1(Etw):
    pattern = Struct(
        "Key" / Int32ul,
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=374, version=1)
class Microsoft_Windows_IE_F12_Provider_374_1(Etw):
    pattern = Struct(
        "Key" / Int32ul,
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=375, version=1)
class Microsoft_Windows_IE_F12_Provider_375_1(Etw):
    pattern = Struct(
        "Key" / Int32ul,
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=376, version=1)
class Microsoft_Windows_IE_F12_Provider_376_1(Etw):
    pattern = Struct(
        "Key" / Int32ul,
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=377, version=1)
class Microsoft_Windows_IE_F12_Provider_377_1(Etw):
    pattern = Struct(
        "Key" / Int32ul,
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=378, version=1)
class Microsoft_Windows_IE_F12_Provider_378_1(Etw):
    pattern = Struct(
        "Key" / Int32ul,
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=379, version=1)
class Microsoft_Windows_IE_F12_Provider_379_1(Etw):
    pattern = Struct(
        "Key" / Int32ul,
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=380, version=1)
class Microsoft_Windows_IE_F12_Provider_380_1(Etw):
    pattern = Struct(
        "Key" / Int32ul,
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=381, version=1)
class Microsoft_Windows_IE_F12_Provider_381_1(Etw):
    pattern = Struct(
        "Key" / Int32ul,
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=382, version=0)
class Microsoft_Windows_IE_F12_Provider_382_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=383, version=0)
class Microsoft_Windows_IE_F12_Provider_383_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=384, version=0)
class Microsoft_Windows_IE_F12_Provider_384_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=385, version=0)
class Microsoft_Windows_IE_F12_Provider_385_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=386, version=0)
class Microsoft_Windows_IE_F12_Provider_386_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=387, version=0)
class Microsoft_Windows_IE_F12_Provider_387_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=388, version=0)
class Microsoft_Windows_IE_F12_Provider_388_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=401, version=0)
class Microsoft_Windows_IE_F12_Provider_401_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=402, version=0)
class Microsoft_Windows_IE_F12_Provider_402_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=403, version=0)
class Microsoft_Windows_IE_F12_Provider_403_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=404, version=0)
class Microsoft_Windows_IE_F12_Provider_404_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=405, version=0)
class Microsoft_Windows_IE_F12_Provider_405_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=406, version=0)
class Microsoft_Windows_IE_F12_Provider_406_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=407, version=0)
class Microsoft_Windows_IE_F12_Provider_407_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=408, version=0)
class Microsoft_Windows_IE_F12_Provider_408_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=409, version=0)
class Microsoft_Windows_IE_F12_Provider_409_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=410, version=0)
class Microsoft_Windows_IE_F12_Provider_410_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=411, version=0)
class Microsoft_Windows_IE_F12_Provider_411_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=412, version=0)
class Microsoft_Windows_IE_F12_Provider_412_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=413, version=0)
class Microsoft_Windows_IE_F12_Provider_413_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=414, version=0)
class Microsoft_Windows_IE_F12_Provider_414_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=415, version=0)
class Microsoft_Windows_IE_F12_Provider_415_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=416, version=0)
class Microsoft_Windows_IE_F12_Provider_416_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=417, version=0)
class Microsoft_Windows_IE_F12_Provider_417_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=418, version=0)
class Microsoft_Windows_IE_F12_Provider_418_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=419, version=0)
class Microsoft_Windows_IE_F12_Provider_419_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=420, version=0)
class Microsoft_Windows_IE_F12_Provider_420_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=421, version=1)
class Microsoft_Windows_IE_F12_Provider_421_1(Etw):
    pattern = Struct(
        "Key" / Int32ul,
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=422, version=1)
class Microsoft_Windows_IE_F12_Provider_422_1(Etw):
    pattern = Struct(
        "Key" / Int32ul,
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=423, version=1)
class Microsoft_Windows_IE_F12_Provider_423_1(Etw):
    pattern = Struct(
        "Key" / Int32ul,
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=424, version=1)
class Microsoft_Windows_IE_F12_Provider_424_1(Etw):
    pattern = Struct(
        "Key" / Int32ul,
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=425, version=1)
class Microsoft_Windows_IE_F12_Provider_425_1(Etw):
    pattern = Struct(
        "Key" / Int32ul,
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=426, version=1)
class Microsoft_Windows_IE_F12_Provider_426_1(Etw):
    pattern = Struct(
        "Key" / Int32ul,
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=427, version=1)
class Microsoft_Windows_IE_F12_Provider_427_1(Etw):
    pattern = Struct(
        "Key" / Int32ul,
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=428, version=1)
class Microsoft_Windows_IE_F12_Provider_428_1(Etw):
    pattern = Struct(
        "Key" / Int32ul,
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=429, version=1)
class Microsoft_Windows_IE_F12_Provider_429_1(Etw):
    pattern = Struct(
        "Key" / Int32ul,
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=430, version=1)
class Microsoft_Windows_IE_F12_Provider_430_1(Etw):
    pattern = Struct(
        "Key" / Int32ul,
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=431, version=0)
class Microsoft_Windows_IE_F12_Provider_431_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=432, version=0)
class Microsoft_Windows_IE_F12_Provider_432_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=433, version=0)
class Microsoft_Windows_IE_F12_Provider_433_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=434, version=0)
class Microsoft_Windows_IE_F12_Provider_434_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=501, version=0)
class Microsoft_Windows_IE_F12_Provider_501_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=502, version=0)
class Microsoft_Windows_IE_F12_Provider_502_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=503, version=0)
class Microsoft_Windows_IE_F12_Provider_503_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=504, version=0)
class Microsoft_Windows_IE_F12_Provider_504_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=505, version=0)
class Microsoft_Windows_IE_F12_Provider_505_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=506, version=0)
class Microsoft_Windows_IE_F12_Provider_506_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=507, version=0)
class Microsoft_Windows_IE_F12_Provider_507_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=508, version=0)
class Microsoft_Windows_IE_F12_Provider_508_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=509, version=0)
class Microsoft_Windows_IE_F12_Provider_509_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=510, version=0)
class Microsoft_Windows_IE_F12_Provider_510_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=511, version=0)
class Microsoft_Windows_IE_F12_Provider_511_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=512, version=0)
class Microsoft_Windows_IE_F12_Provider_512_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=513, version=0)
class Microsoft_Windows_IE_F12_Provider_513_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=514, version=0)
class Microsoft_Windows_IE_F12_Provider_514_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=515, version=0)
class Microsoft_Windows_IE_F12_Provider_515_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=516, version=0)
class Microsoft_Windows_IE_F12_Provider_516_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=517, version=0)
class Microsoft_Windows_IE_F12_Provider_517_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=518, version=0)
class Microsoft_Windows_IE_F12_Provider_518_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=519, version=0)
class Microsoft_Windows_IE_F12_Provider_519_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=520, version=0)
class Microsoft_Windows_IE_F12_Provider_520_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=521, version=0)
class Microsoft_Windows_IE_F12_Provider_521_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=522, version=0)
class Microsoft_Windows_IE_F12_Provider_522_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=523, version=0)
class Microsoft_Windows_IE_F12_Provider_523_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=524, version=0)
class Microsoft_Windows_IE_F12_Provider_524_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=525, version=0)
class Microsoft_Windows_IE_F12_Provider_525_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=526, version=0)
class Microsoft_Windows_IE_F12_Provider_526_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=527, version=0)
class Microsoft_Windows_IE_F12_Provider_527_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=528, version=0)
class Microsoft_Windows_IE_F12_Provider_528_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=529, version=0)
class Microsoft_Windows_IE_F12_Provider_529_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=530, version=0)
class Microsoft_Windows_IE_F12_Provider_530_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=531, version=0)
class Microsoft_Windows_IE_F12_Provider_531_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=532, version=0)
class Microsoft_Windows_IE_F12_Provider_532_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=533, version=0)
class Microsoft_Windows_IE_F12_Provider_533_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=534, version=0)
class Microsoft_Windows_IE_F12_Provider_534_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=535, version=0)
class Microsoft_Windows_IE_F12_Provider_535_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=536, version=0)
class Microsoft_Windows_IE_F12_Provider_536_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=537, version=0)
class Microsoft_Windows_IE_F12_Provider_537_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=538, version=0)
class Microsoft_Windows_IE_F12_Provider_538_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=539, version=0)
class Microsoft_Windows_IE_F12_Provider_539_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=540, version=0)
class Microsoft_Windows_IE_F12_Provider_540_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=541, version=0)
class Microsoft_Windows_IE_F12_Provider_541_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=542, version=0)
class Microsoft_Windows_IE_F12_Provider_542_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=543, version=0)
class Microsoft_Windows_IE_F12_Provider_543_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=544, version=0)
class Microsoft_Windows_IE_F12_Provider_544_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=545, version=0)
class Microsoft_Windows_IE_F12_Provider_545_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=546, version=0)
class Microsoft_Windows_IE_F12_Provider_546_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=547, version=0)
class Microsoft_Windows_IE_F12_Provider_547_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=548, version=0)
class Microsoft_Windows_IE_F12_Provider_548_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=549, version=0)
class Microsoft_Windows_IE_F12_Provider_549_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=550, version=0)
class Microsoft_Windows_IE_F12_Provider_550_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=551, version=0)
class Microsoft_Windows_IE_F12_Provider_551_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=552, version=0)
class Microsoft_Windows_IE_F12_Provider_552_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=601, version=0)
class Microsoft_Windows_IE_F12_Provider_601_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=602, version=0)
class Microsoft_Windows_IE_F12_Provider_602_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=701, version=0)
class Microsoft_Windows_IE_F12_Provider_701_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=702, version=0)
class Microsoft_Windows_IE_F12_Provider_702_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=703, version=0)
class Microsoft_Windows_IE_F12_Provider_703_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=704, version=0)
class Microsoft_Windows_IE_F12_Provider_704_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=705, version=0)
class Microsoft_Windows_IE_F12_Provider_705_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=706, version=0)
class Microsoft_Windows_IE_F12_Provider_706_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=707, version=0)
class Microsoft_Windows_IE_F12_Provider_707_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=708, version=0)
class Microsoft_Windows_IE_F12_Provider_708_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=709, version=0)
class Microsoft_Windows_IE_F12_Provider_709_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=710, version=0)
class Microsoft_Windows_IE_F12_Provider_710_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=711, version=0)
class Microsoft_Windows_IE_F12_Provider_711_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=712, version=0)
class Microsoft_Windows_IE_F12_Provider_712_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=713, version=0)
class Microsoft_Windows_IE_F12_Provider_713_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=714, version=0)
class Microsoft_Windows_IE_F12_Provider_714_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=715, version=0)
class Microsoft_Windows_IE_F12_Provider_715_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=716, version=0)
class Microsoft_Windows_IE_F12_Provider_716_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=717, version=0)
class Microsoft_Windows_IE_F12_Provider_717_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=718, version=0)
class Microsoft_Windows_IE_F12_Provider_718_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=801, version=0)
class Microsoft_Windows_IE_F12_Provider_801_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=802, version=0)
class Microsoft_Windows_IE_F12_Provider_802_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=901, version=0)
class Microsoft_Windows_IE_F12_Provider_901_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=902, version=0)
class Microsoft_Windows_IE_F12_Provider_902_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=903, version=0)
class Microsoft_Windows_IE_F12_Provider_903_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=904, version=0)
class Microsoft_Windows_IE_F12_Provider_904_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=905, version=0)
class Microsoft_Windows_IE_F12_Provider_905_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=906, version=0)
class Microsoft_Windows_IE_F12_Provider_906_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=907, version=0)
class Microsoft_Windows_IE_F12_Provider_907_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=908, version=0)
class Microsoft_Windows_IE_F12_Provider_908_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=909, version=0)
class Microsoft_Windows_IE_F12_Provider_909_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=910, version=0)
class Microsoft_Windows_IE_F12_Provider_910_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=911, version=0)
class Microsoft_Windows_IE_F12_Provider_911_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=912, version=0)
class Microsoft_Windows_IE_F12_Provider_912_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=913, version=0)
class Microsoft_Windows_IE_F12_Provider_913_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=914, version=0)
class Microsoft_Windows_IE_F12_Provider_914_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=915, version=0)
class Microsoft_Windows_IE_F12_Provider_915_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=916, version=0)
class Microsoft_Windows_IE_F12_Provider_916_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=917, version=0)
class Microsoft_Windows_IE_F12_Provider_917_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=918, version=0)
class Microsoft_Windows_IE_F12_Provider_918_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=921, version=0)
class Microsoft_Windows_IE_F12_Provider_921_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=922, version=0)
class Microsoft_Windows_IE_F12_Provider_922_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=923, version=0)
class Microsoft_Windows_IE_F12_Provider_923_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=924, version=0)
class Microsoft_Windows_IE_F12_Provider_924_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=925, version=0)
class Microsoft_Windows_IE_F12_Provider_925_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=926, version=0)
class Microsoft_Windows_IE_F12_Provider_926_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=927, version=0)
class Microsoft_Windows_IE_F12_Provider_927_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=928, version=0)
class Microsoft_Windows_IE_F12_Provider_928_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=929, version=0)
class Microsoft_Windows_IE_F12_Provider_929_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=930, version=0)
class Microsoft_Windows_IE_F12_Provider_930_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=931, version=0)
class Microsoft_Windows_IE_F12_Provider_931_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=932, version=0)
class Microsoft_Windows_IE_F12_Provider_932_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=933, version=0)
class Microsoft_Windows_IE_F12_Provider_933_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=934, version=0)
class Microsoft_Windows_IE_F12_Provider_934_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=935, version=0)
class Microsoft_Windows_IE_F12_Provider_935_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=936, version=0)
class Microsoft_Windows_IE_F12_Provider_936_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=937, version=0)
class Microsoft_Windows_IE_F12_Provider_937_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=938, version=0)
class Microsoft_Windows_IE_F12_Provider_938_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=939, version=0)
class Microsoft_Windows_IE_F12_Provider_939_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=940, version=0)
class Microsoft_Windows_IE_F12_Provider_940_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=941, version=0)
class Microsoft_Windows_IE_F12_Provider_941_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=942, version=0)
class Microsoft_Windows_IE_F12_Provider_942_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=943, version=0)
class Microsoft_Windows_IE_F12_Provider_943_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )


@declare(guid=guid("d17fff2f-392d-478c-a41d-737a216eb2a4"), event_id=944, version=0)
class Microsoft_Windows_IE_F12_Provider_944_0(Etw):
    pattern = Struct(
        "TraceDescription" / WString
    )

