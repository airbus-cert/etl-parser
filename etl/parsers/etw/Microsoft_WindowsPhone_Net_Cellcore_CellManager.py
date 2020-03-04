# -*- coding: utf-8 -*-
"""
Microsoft-WindowsPhone-Net-Cellcore-CellManager
GUID : 9a6615a6-902a-4705-804b-57b8813089b8
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1_0(Etw):
    pattern = Struct(
        "wszString1" / WString,
        "wszString2" / WString
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=101, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_101_0(Etw):
    pattern = Struct(
        "hexCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=105, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_105_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=107, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_107_0(Etw):
    pattern = Struct(
        "AnsiStringName1" / CString,
        "HResultName" / Int32sl
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=108, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_108_0(Etw):
    pattern = Struct(
        "HResultName" / Int32sl
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=112, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_112_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=201, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_201_0(Etw):
    pattern = Struct(
        "hexCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=202, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_202_0(Etw):
    pattern = Struct(
        "hexCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=203, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_203_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "guidCode1" / Guid
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=206, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_206_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "guidCode1" / Guid
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=207, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_207_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "guidCode1" / Guid
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=208, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_208_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=210, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_210_0(Etw):
    pattern = Struct(
        "hexCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=212, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_212_0(Etw):
    pattern = Struct(
        "hexCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=215, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_215_0(Etw):
    pattern = Struct(
        "hexCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=216, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_216_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "wszString" / WString,
        "bCode1" / Int8ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=217, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_217_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=219, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_219_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=220, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_220_0(Etw):
    pattern = Struct(
        "DwordName" / Int32ul,
        "HResultName" / Int32sl,
        "IccIdLength" / Int32ul,
        "IccId" / Int8ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=221, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_221_0(Etw):
    pattern = Struct(
        "DwordName" / Int32ul,
        "HResultName" / Int32sl,
        "IccIdLength" / Int32ul,
        "IccId" / Int8ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=222, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_222_0(Etw):
    pattern = Struct(
        "DwordName" / Int32ul,
        "HResultName" / Int32sl,
        "IccIdLength" / Int32ul,
        "IccId" / Int8ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=223, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_223_0(Etw):
    pattern = Struct(
        "DwordName" / Int32ul,
        "HResultName" / Int32sl,
        "IccIdLength" / Int32ul,
        "IccId" / Int8ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=224, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_224_0(Etw):
    pattern = Struct(
        "DwordName" / Int32ul,
        "HResultName" / Int32sl,
        "IccIdLength" / Int32ul,
        "IccId" / Int8ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=225, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_225_0(Etw):
    pattern = Struct(
        "DwordName" / Int32ul,
        "HResultName" / Int32sl,
        "IccIdLength" / Int32ul,
        "IccId" / Int8ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=226, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_226_0(Etw):
    pattern = Struct(
        "DwordName" / Int32ul,
        "HResultName" / Int32sl,
        "IccIdLength" / Int32ul,
        "IccId" / Int8ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=227, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_227_0(Etw):
    pattern = Struct(
        "DwordName" / Int32ul,
        "HResultName" / Int32sl,
        "IccIdLength" / Int32ul,
        "IccId" / Int8ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=228, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_228_0(Etw):
    pattern = Struct(
        "DwordName" / Int32ul,
        "HResultName" / Int32sl,
        "IccIdLength" / Int32ul,
        "IccId" / Int8ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=229, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_229_0(Etw):
    pattern = Struct(
        "DwordName" / Int32ul,
        "HResultName" / Int32sl,
        "IccIdLength" / Int32ul,
        "IccId" / Int8ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=230, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_230_0(Etw):
    pattern = Struct(
        "DwordName" / Int32ul,
        "HResultName" / Int32sl,
        "IccIdLength" / Int32ul,
        "IccId" / Int8ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=231, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_231_0(Etw):
    pattern = Struct(
        "DwordName" / Int32ul,
        "HResultName" / Int32sl,
        "IccIdLength" / Int32ul,
        "IccId" / Int8ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=232, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_232_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=233, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_233_0(Etw):
    pattern = Struct(
        "AnsiStringName" / CString,
        "DwordName" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=236, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_236_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=237, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_237_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=238, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_238_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=239, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_239_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul,
        "dwCode3" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=240, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_240_0(Etw):
    pattern = Struct(
        "Dword1Name" / Int32ul,
        "HResultName" / Int32sl,
        "IccIdLength" / Int32ul,
        "IccId" / Int8ul,
        "Dword2Name" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=243, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_243_0(Etw):
    pattern = Struct(
        "IccIdLength" / Int32ul,
        "IccId" / Int8ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=244, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_244_0(Etw):
    pattern = Struct(
        "HResultName" / Int32sl
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=245, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_245_0(Etw):
    pattern = Struct(
        "IccIdLength" / Int32ul,
        "IccId" / Int8ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=246, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_246_0(Etw):
    pattern = Struct(
        "HResultName" / Int32sl
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=247, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_247_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=248, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_248_0(Etw):
    pattern = Struct(
        "bCode1" / Int8ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=250, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_250_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=251, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_251_0(Etw):
    pattern = Struct(
        "hexCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=253, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_253_0(Etw):
    pattern = Struct(
        "bCode1" / Int8ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=300, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_300_0(Etw):
    pattern = Struct(
        "hexCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=301, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_301_0(Etw):
    pattern = Struct(
        "hexCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=302, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_302_0(Etw):
    pattern = Struct(
        "apmState" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=303, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_303_0(Etw):
    pattern = Struct(
        "apmState1" / Int32ul,
        "apmState2" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=304, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_304_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=305, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_305_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=306, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_306_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=307, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_307_0(Etw):
    pattern = Struct(
        "apmStateDevices" / Int32ul,
        "apmPowerState" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=308, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_308_0(Etw):
    pattern = Struct(
        "apmPowerState" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=309, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_309_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul,
        "wszString" / WString
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=310, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_310_0(Etw):
    pattern = Struct(
        "apmPowerState" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=311, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_311_0(Etw):
    pattern = Struct(
        "apmPowerState" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=312, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_312_0(Etw):
    pattern = Struct(
        "apmStateDevices" / Int32ul,
        "bCode1" / Int8ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=313, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_313_0(Etw):
    pattern = Struct(
        "hexCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=314, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_314_0(Etw):
    pattern = Struct(
        "hexCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=315, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_315_0(Etw):
    pattern = Struct(
        "hexCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=316, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_316_0(Etw):
    pattern = Struct(
        "hexCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=317, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_317_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=318, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_318_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=319, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_319_0(Etw):
    pattern = Struct(
        "hexCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=320, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_320_0(Etw):
    pattern = Struct(
        "apmState" / Int32ul,
        "hexCode" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=321, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_321_0(Etw):
    pattern = Struct(
        "apmPowerState" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=322, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_322_0(Etw):
    pattern = Struct(
        "apmState" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=323, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_323_0(Etw):
    pattern = Struct(
        "apmState" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=324, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_324_0(Etw):
    pattern = Struct(
        "apmState" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=400, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_400_0(Etw):
    pattern = Struct(
        "hexCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=402, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_402_0(Etw):
    pattern = Struct(
        "bCode1" / Int8ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=403, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_403_0(Etw):
    pattern = Struct(
        "hexCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=802, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_802_0(Etw):
    pattern = Struct(
        "hexCode1" / Int32ul,
        "hexCode2" / Int32ul,
        "hexCode3" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=803, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_803_0(Etw):
    pattern = Struct(
        "hexCode1" / Int32ul,
        "hexCode2" / Int32ul,
        "hexCode3" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=900, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_900_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=901, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_901_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=902, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_902_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=903, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_903_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=904, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_904_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "guidCode1" / Guid
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=905, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_905_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "guidCode1" / Guid
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=906, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_906_0(Etw):
    pattern = Struct(
        "hexCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=907, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_907_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=908, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_908_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=910, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_910_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul,
        "rilUICCSlotState" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=911, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_911_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=912, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_912_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=913, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_913_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul,
        "hexCode3" / Int32ul,
        "hexCode4" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=914, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_914_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul,
        "hexCode3" / Int32ul,
        "hexCode4" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=916, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_916_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=917, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_917_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "guidCode1" / Guid
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=919, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_919_0(Etw):
    pattern = Struct(
        "hexCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=920, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_920_0(Etw):
    pattern = Struct(
        "hexCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=921, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_921_0(Etw):
    pattern = Struct(
        "hexCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=922, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_922_0(Etw):
    pattern = Struct(
        "hexCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=923, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_923_0(Etw):
    pattern = Struct(
        "hexCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=924, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_924_0(Etw):
    pattern = Struct(
        "hexCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=925, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_925_0(Etw):
    pattern = Struct(
        "hexCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=926, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_926_0(Etw):
    pattern = Struct(
        "tDword" / Int32ul,
        "modemPowerState" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=927, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_927_0(Etw):
    pattern = Struct(
        "rilRegStat" / Int32ul,
        "rilSystemType" / Int32ul,
        "szString" / WString
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=928, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_928_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=929, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_929_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=930, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_930_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=931, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_931_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=932, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_932_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=934, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_934_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul,
        "dwCode3" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=935, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_935_0(Etw):
    pattern = Struct(
        "hexCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=936, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_936_0(Etw):
    pattern = Struct(
        "hexCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=937, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_937_0(Etw):
    pattern = Struct(
        "hexCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=938, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_938_0(Etw):
    pattern = Struct(
        "hexCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=939, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_939_0(Etw):
    pattern = Struct(
        "hexCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=940, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_940_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=942, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_942_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul,
        "hexCode3" / Int32ul,
        "hexCode4" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=945, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_945_0(Etw):
    pattern = Struct(
        "hexCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=946, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_946_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=947, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_947_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=948, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_948_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=949, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_949_0(Etw):
    pattern = Struct(
        "DwordName1" / Int32ul,
        "DwordName2" / Int32ul,
        "cbBytes3" / Int32ul,
        "Bytes4" / Int8ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=950, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_950_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=951, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_951_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul,
        "dwCode3" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=952, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_952_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=953, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_953_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=955, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_955_0(Etw):
    pattern = Struct(
        "hexCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=957, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_957_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=958, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_958_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=959, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_959_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=962, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_962_0(Etw):
    pattern = Struct(
        "HResultName" / Int32sl
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=963, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_963_0(Etw):
    pattern = Struct(
        "HResultName" / Int32sl
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=965, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_965_0(Etw):
    pattern = Struct(
        "hexCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=966, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_966_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=967, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_967_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=968, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_968_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul,
        "dwCode3" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=969, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_969_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul,
        "dwCode3" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=971, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_971_0(Etw):
    pattern = Struct(
        "dwordName" / Int32ul,
        "booleanName" / Int8ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=972, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_972_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=973, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_973_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=974, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_974_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=975, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_975_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=976, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_976_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=977, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_977_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=978, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_978_0(Etw):
    pattern = Struct(
        "szString" / WString
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=981, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_981_0(Etw):
    pattern = Struct(
        "IccIdLength" / Int32ul,
        "IccId" / Int8ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=982, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_982_0(Etw):
    pattern = Struct(
        "IccIdLength" / Int32ul,
        "IccId" / Int8ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=983, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_983_0(Etw):
    pattern = Struct(
        "IccIdLength" / Int32ul,
        "IccId" / Int8ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=984, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_984_0(Etw):
    pattern = Struct(
        "IccIdLength" / Int32ul,
        "IccId" / Int8ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=985, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_985_0(Etw):
    pattern = Struct(
        "IccIdLength" / Int32ul,
        "IccId" / Int8ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=986, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_986_0(Etw):
    pattern = Struct(
        "IccIdLength" / Int32ul,
        "IccId" / Int8ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=987, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_987_0(Etw):
    pattern = Struct(
        "IccIdLength" / Int32ul,
        "IccId" / Int8ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=988, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_988_0(Etw):
    pattern = Struct(
        "IccIdLength" / Int32ul,
        "IccId" / Int8ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=990, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_990_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=992, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_992_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=993, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_993_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=994, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_994_0(Etw):
    pattern = Struct(
        "dwSlotIndex" / Int32ul,
        "ATRLength" / Int32ul,
        "ATR" / Int8ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=995, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_995_0(Etw):
    pattern = Struct(
        "bCode1" / Int8ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=997, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_997_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=998, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_998_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1000, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1000_0(Etw):
    pattern = Struct(
        "hexCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1001, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1001_0(Etw):
    pattern = Struct(
        "hexCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1002, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1002_0(Etw):
    pattern = Struct(
        "hexCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1003, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1003_0(Etw):
    pattern = Struct(
        "hexCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1004, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1004_0(Etw):
    pattern = Struct(
        "hexCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1005, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1005_0(Etw):
    pattern = Struct(
        "hexCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1006, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1006_0(Etw):
    pattern = Struct(
        "hexCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1007, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1007_0(Etw):
    pattern = Struct(
        "guidCode1" / Guid,
        "modemPowerState" / Int32ul,
        "powerStateChangeReason" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1008, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1008_0(Etw):
    pattern = Struct(
        "apmState" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1009, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1009_0(Etw):
    pattern = Struct(
        "guidCode1" / Guid,
        "guidCode2" / Guid,
        "rilSystemType" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1010, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1010_0(Etw):
    pattern = Struct(
        "guidCode1" / Guid,
        "guidCode2" / Guid,
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul,
        "dwCode3" / Int32ul,
        "rilSetSystemSelectionPrefsFlag" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1013, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1013_0(Etw):
    pattern = Struct(
        "hexCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1014, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1014_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1015, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1015_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1016, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1016_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1017, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1017_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1018, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1018_0(Etw):
    pattern = Struct(
        "CellularDataRoamingSettingName" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1020, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1020_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1022, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1022_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1023, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1023_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1024, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1024_0(Etw):
    pattern = Struct(
        "powerState" / Int8ul,
        "PowerStateChangeReason" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1025, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1025_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1026, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1026_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1027, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1027_0(Etw):
    pattern = Struct(
        "szString" / WString
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1028, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1028_0(Etw):
    pattern = Struct(
        "guidCode1" / Guid,
        "guidCode2" / Guid,
        "rilCDMAAvoidReqType" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1100, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1100_0(Etw):
    pattern = Struct(
        "hexCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1101, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1101_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul,
        "dwCode3" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1102, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1102_0(Etw):
    pattern = Struct(
        "Result" / Int32ul,
        "wnfName1" / Int32ul,
        "wnfName2" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1103, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1103_0(Etw):
    pattern = Struct(
        "hexCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1104, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1104_0(Etw):
    pattern = Struct(
        "hexCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1201, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1201_0(Etw):
    pattern = Struct(
        "hexCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1202, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1202_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1203, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1203_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1204, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1204_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1205, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1205_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul,
        "dwCode3" / Int32ul,
        "dwCode4" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1206, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1206_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1207, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1207_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul,
        "dwCode3" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1300, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1300_0(Etw):
    pattern = Struct(
        "hexCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1301, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1301_0(Etw):
    pattern = Struct(
        "bCode1" / Int8ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1302, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1302_0(Etw):
    pattern = Struct(
        "hexCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1400, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1400_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1401, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1401_0(Etw):
    pattern = Struct(
        "AnsiStringName1" / CString,
        "AnsiStringName2" / CString
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1410, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1410_0(Etw):
    pattern = Struct(
        "wszString1" / WString,
        "wszString2" / WString,
        "dwCode2" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1411, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1411_0(Etw):
    pattern = Struct(
        "wszString1" / WString,
        "wszString2" / WString
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1412, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1412_0(Etw):
    pattern = Struct(
        "wszString1" / WString,
        "wszString2" / WString,
        "dwCode2" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1413, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1413_0(Etw):
    pattern = Struct(
        "wszString1" / WString,
        "wszString2" / WString,
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1414, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1414_0(Etw):
    pattern = Struct(
        "wszString1" / WString,
        "wszString2" / WString,
        "dwCode2" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1415, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1415_0(Etw):
    pattern = Struct(
        "wszString1" / WString,
        "dwCode2" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1416, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1416_0(Etw):
    pattern = Struct(
        "wszString1" / WString,
        "wszString2" / WString,
        "dwCode2" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1417, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1417_0(Etw):
    pattern = Struct(
        "wszString1" / WString,
        "wszString2" / WString,
        "wszString3" / WString
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1418, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1418_0(Etw):
    pattern = Struct(
        "wszString1" / WString,
        "wszString2" / WString,
        "dwCode2" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1419, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1419_0(Etw):
    pattern = Struct(
        "wszString1" / WString
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1420, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1420_0(Etw):
    pattern = Struct(
        "wszString1" / WString,
        "dwCode2" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1421, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1421_0(Etw):
    pattern = Struct(
        "wszString1" / WString,
        "wszString2" / WString,
        "wszString3" / WString,
        "dwCode1" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1422, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1422_0(Etw):
    pattern = Struct(
        "wszString1" / WString,
        "wszString2" / WString,
        "wszString3" / WString
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1428, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1428_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1429, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1429_0(Etw):
    pattern = Struct(
        "wszString1" / WString
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1430, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1430_0(Etw):
    pattern = Struct(
        "wszString1" / WString,
        "wszString2" / WString,
        "dwCode2" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1431, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1431_0(Etw):
    pattern = Struct(
        "wszString1" / WString
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1500, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1500_0(Etw):
    pattern = Struct(
        "rilSystemTypeName" / Int32ul,
        "ardTypeName" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1501, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1501_0(Etw):
    pattern = Struct(
        "rilSystemTypeName" / Int32ul,
        "ardTypeName" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1502, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1502_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul,
        "ardTypeName" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1503, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1503_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul,
        "ardTypeName" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1509, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1509_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1510, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1510_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1513, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1513_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int64ul,
        "dwCode3" / Int64ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1515, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1515_0(Etw):
    pattern = Struct(
        "dwCode1" / Int64ul,
        "dwCode2" / Int8ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1517, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1517_0(Etw):
    pattern = Struct(
        "HResultName" / Int32sl
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1522, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1522_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1525, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1525_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1600, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1600_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1601, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1601_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1602, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1602_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1603, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1603_0(Etw):
    pattern = Struct(
        "bCode1" / Int8ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1604, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1604_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1605, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1605_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1606, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1606_0(Etw):
    pattern = Struct(
        "bCode1" / Int8ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1608, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1608_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1609, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1609_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1610, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1610_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1611, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1611_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1612, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1612_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul,
        "bCode1" / Int8ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1614, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1614_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1615, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1615_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1616, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1616_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1617, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1617_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1618, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1618_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1619, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1619_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1620, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1620_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul,
        "dwCode3" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1623, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1623_0(Etw):
    pattern = Struct(
        "wszString1" / WString
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1624, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1624_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "bCode1" / Int8ul,
        "bCode2" / Int8ul,
        "bCode3" / Int8ul,
        "bCode4" / Int8ul,
        "bCode5" / Int8ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1625, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1625_0(Etw):
    pattern = Struct(
        "dwordName" / Int32ul,
        "booleanName" / Int8ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1626, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1626_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1627, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1627_0(Etw):
    pattern = Struct(
        "dwordName" / Int32ul,
        "booleanName" / Int8ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1628, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1628_0(Etw):
    pattern = Struct(
        "SlotAffinity" / Int32ul,
        "DwordName" / Int32ul,
        "bCode" / Int8ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1629, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1629_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1630, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1630_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1631, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1631_0(Etw):
    pattern = Struct(
        "bCode1" / Int8ul,
        "bCode2" / Int8ul,
        "bCode3" / Int8ul,
        "bCode4" / Int8ul,
        "bCode5" / Int8ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1633, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1633_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1700, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1700_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul,
        "dwCode3" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1701, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1701_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul,
        "dwCode3" / Int32ul,
        "dwCode4" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1702, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1702_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul,
        "dwCode3" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1703, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1703_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul,
        "dwCode3" / Int32ul,
        "dwCode4" / Int32sl
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1704, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1704_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul,
        "dwCode3" / Int32ul,
        "dwCode4" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1705, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1705_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul,
        "dwCode3" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1706, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1706_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul,
        "dwCode3" / Int32ul,
        "dwCode4" / Int32ul,
        "CellularDataRoamingSettingName" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1707, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1707_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1708, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1708_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul,
        "wszString1" / WString,
        "wszString2" / WString
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1709, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1709_0(Etw):
    pattern = Struct(
        "hexCode1" / Int32ul,
        "hexCode2" / Int32ul,
        "hexCode3" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1710, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1710_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1711, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1711_0(Etw):
    pattern = Struct(
        "dwordName" / Int32ul,
        "booleanName" / Int8ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1712, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1712_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1713, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1713_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1714, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1714_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1715, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1715_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1716, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1716_0(Etw):
    pattern = Struct(
        "executorIndex" / Int32ul,
        "rilRegStat" / Int32ul,
        "rilSystemType" / Int32ul,
        "szString" / WString
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1717, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1717_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1718, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1718_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1719, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1719_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1720, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1720_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1721, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1721_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul,
        "dwCode3" / Int32ul,
        "dwCode4" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1722, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1722_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul,
        "dwCode3" / Int32ul,
        "dwCode4" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1723, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1723_0(Etw):
    pattern = Struct(
        "DwordName" / Int32ul,
        "ActualIccIdLength" / Int32ul,
        "ActualIccId" / Int8ul,
        "ExpectedIccIdLength" / Int32ul,
        "ExpectedIccId" / Int8ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1724, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1724_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1725, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1725_0(Etw):
    pattern = Struct(
        "hexCode1" / Int32ul,
        "hexCode2" / Int32ul,
        "hexCode3" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1726, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1726_0(Etw):
    pattern = Struct(
        "DwordName" / Int32ul,
        "hexCode1" / Int32ul,
        "dwCode2" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1727, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1727_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1728, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1728_0(Etw):
    pattern = Struct(
        "dwordName" / Int32ul,
        "booleanName" / Int8ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1729, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1729_0(Etw):
    pattern = Struct(
        "tDword" / Int32ul,
        "modemPowerState" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1730, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1730_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1731, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1731_0(Etw):
    pattern = Struct(
        "HResultName" / Int32sl,
        "DwordName" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1800, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1800_0(Etw):
    pattern = Struct(
        "AnsiStringName" / CString,
        "HResultName" / Int32sl,
        "IccIdLength" / Int32ul,
        "IccId" / Int8ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1801, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1801_0(Etw):
    pattern = Struct(
        "AnsiStringName" / CString,
        "IccIdLength" / Int32ul,
        "IccId" / Int8ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1802, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1802_0(Etw):
    pattern = Struct(
        "AnsiStringName" / CString,
        "IccIdLength" / Int32ul,
        "IccId" / Int8ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1900, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1900_0(Etw):
    pattern = Struct(
        "HResultName" / Int32sl,
        "DwordName" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1901, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1901_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1902, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1902_0(Etw):
    pattern = Struct(
        "AnsiStringName" / CString,
        "IccIdLength" / Int32ul,
        "IccId" / Int8ul,
        "CmResultName" / Int32ul,
        "DwordName" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1903, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1903_0(Etw):
    pattern = Struct(
        "AnsiStringName" / CString,
        "ActualIccIdLength" / Int32ul,
        "ActualIccId" / Int8ul,
        "ExpectedIccIdLength" / Int32ul,
        "ExpectedIccId" / Int8ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1904, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1904_0(Etw):
    pattern = Struct(
        "AnsiStringName" / CString,
        "IccIdLength" / Int32ul,
        "IccId" / Int8ul,
        "HResultName" / Int32sl,
        "DwordName" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1905, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1905_0(Etw):
    pattern = Struct(
        "HResultName" / Int32sl,
        "DwordName" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1906, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1906_0(Etw):
    pattern = Struct(
        "HResultName" / Int32sl,
        "DwordName" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1907, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1907_0(Etw):
    pattern = Struct(
        "AnsiStringName" / CString,
        "IccIdLength" / Int32ul,
        "IccId" / Int8ul,
        "HResultName" / Int32sl,
        "DwordName" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1908, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1908_0(Etw):
    pattern = Struct(
        "AnsiStringName" / CString,
        "CmResultName" / Int32ul,
        "DwordName" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1909, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1909_0(Etw):
    pattern = Struct(
        "AnsiStringName" / CString,
        "HResultName" / Int32sl,
        "DwordName" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1910, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1910_0(Etw):
    pattern = Struct(
        "AnsiStringName" / CString,
        "HResultName" / Int32sl,
        "DwordName" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1912, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1912_0(Etw):
    pattern = Struct(
        "dwordName" / Int32ul,
        "cmSelectionTypeName" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1913, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1913_0(Etw):
    pattern = Struct(
        "dwordName" / Int32ul,
        "cmSelectionTypeName" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1914, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1914_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1915, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1915_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1917, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1917_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1918, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1918_0(Etw):
    pattern = Struct(
        "dwCode" / Int32ul,
        "CmResultName" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1919, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1919_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1920, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1920_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "dwCode2" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1921, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1921_0(Etw):
    pattern = Struct(
        "CmApiName" / CString,
        "connectionName" / WString,
        "IccIdLength" / Int32ul,
        "IccId" / Int8ul,
        "CmResultName" / Int32ul,
        "DwordName" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1922, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1922_0(Etw):
    pattern = Struct(
        "AnsiStringName" / CString,
        "connectionName" / WString,
        "CmResultName" / Int32ul,
        "DwordName" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=1923, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_1923_0(Etw):
    pattern = Struct(
        "AnsiStringName" / CString,
        "connectionName" / WString,
        "DwordName1" / Int32ul,
        "DwordName2" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=2000, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_2000_0(Etw):
    pattern = Struct(
        "HResultName" / Int32sl
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=2001, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_2001_0(Etw):
    pattern = Struct(
        "HResultName" / Int32sl
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=2002, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_2002_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=2100, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_2100_0(Etw):
    pattern = Struct(
        "StringName1" / WString,
        "DwordName1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=2202, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_2202_0(Etw):
    pattern = Struct(
        "IccIdLength" / Int32ul,
        "IccId" / Int8ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=2203, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_2203_0(Etw):
    pattern = Struct(
        "HResultName" / Int32sl
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=2204, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_2204_0(Etw):
    pattern = Struct(
        "IccIdLength" / Int32ul,
        "IccId" / Int8ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=2205, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_2205_0(Etw):
    pattern = Struct(
        "HResultName" / Int32sl
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=2206, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_2206_0(Etw):
    pattern = Struct(
        "DwordName" / Int32ul,
        "HResultName" / Int32sl,
        "IccIdLength" / Int32ul,
        "IccId" / Int8ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=2207, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_2207_0(Etw):
    pattern = Struct(
        "DwordName" / Int32ul,
        "HResultName" / Int32sl,
        "IccIdLength" / Int32ul,
        "IccId" / Int8ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=2208, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_2208_0(Etw):
    pattern = Struct(
        "DwordName" / Int32ul,
        "HResultName" / Int32sl,
        "IccIdLength" / Int32ul,
        "IccId" / Int8ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=2209, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_2209_0(Etw):
    pattern = Struct(
        "DwordName" / Int32ul,
        "HResultName" / Int32sl,
        "IccIdLength" / Int32ul,
        "IccId" / Int8ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=2300, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_2300_0(Etw):
    pattern = Struct(
        "tDword" / Int32ul,
        "modemPowerState" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=2301, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_2301_0(Etw):
    pattern = Struct(
        "modemPowerState" / Int32ul,
        "HResultName" / Int32sl
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=2303, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_2303_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=2304, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_2304_0(Etw):
    pattern = Struct(
        "HResultName" / Int32sl,
        "DwordName" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=2306, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_2306_0(Etw):
    pattern = Struct(
        "DwordName" / Int32ul,
        "CellularDataRoamingSettingName" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=2308, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_2308_0(Etw):
    pattern = Struct(
        "HResultName" / Int32sl
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=2309, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_2309_0(Etw):
    pattern = Struct(
        "HResultName" / Int32sl
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=2310, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_2310_0(Etw):
    pattern = Struct(
        "HResultName" / Int32sl
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=2312, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_2312_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul,
        "rilSystemType" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=2313, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_2313_0(Etw):
    pattern = Struct(
        "bCode1" / Int8ul,
        "bCode2" / Int8ul,
        "bCode3" / Int8ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=2314, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_2314_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=2315, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_2315_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=2316, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_2316_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=2317, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_2317_0(Etw):
    pattern = Struct(
        "HResultName" / Int32sl,
        "DwordName" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=2318, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_2318_0(Etw):
    pattern = Struct(
        "HResultName" / Int32sl,
        "DwordName" / Int32ul,
        "CellularDataRoamingSettingName" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=2319, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_2319_0(Etw):
    pattern = Struct(
        "DwordName" / Int32ul,
        "CellularDataRoamingSettingName" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=2320, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_2320_0(Etw):
    pattern = Struct(
        "HResultName" / Int32sl,
        "DwordName" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=2321, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_2321_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=2322, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_2322_0(Etw):
    pattern = Struct(
        "DwordName" / Int32ul,
        "CellularDataRoamingSettingName" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=2323, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_2323_0(Etw):
    pattern = Struct(
        "dwCode1" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=2324, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_2324_0(Etw):
    pattern = Struct(
        "DwordName" / Int32ul,
        "CellularDataRoamingSettingName" / Int32ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=2325, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_2325_0(Etw):
    pattern = Struct(
        "bCode1" / Int8ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=2326, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_2326_0(Etw):
    pattern = Struct(
        "bCode1" / Int8ul
    )


@declare(guid=guid("9a6615a6-902a-4705-804b-57b8813089b8"), event_id=2327, version=0)
class Microsoft_WindowsPhone_Net_Cellcore_CellManager_2327_0(Etw):
    pattern = Struct(
        "HResultName" / Int32sl
    )

