# -*- coding: utf-8 -*-
"""
Microsoft-Windows-MCCS-SyncController
GUID : 7fcb9791-f481-46d1-846e-2eb6f003c4d3
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=1, version=0)
class Microsoft_Windows_MCCS_SyncController_1_0(Etw):
    pattern = Struct(
        "P1_HResult" / Int32sl,
        "P2_String" / CString,
        "P3_UInt32" / Int32ul
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=2, version=0)
class Microsoft_Windows_MCCS_SyncController_2_0(Etw):
    pattern = Struct(
        "P1_HResult" / Int32sl,
        "P2_String" / CString,
        "P3_UInt32" / Int32ul
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=102, version=0)
class Microsoft_Windows_MCCS_SyncController_102_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=103, version=0)
class Microsoft_Windows_MCCS_SyncController_103_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=104, version=0)
class Microsoft_Windows_MCCS_SyncController_104_0(Etw):
    pattern = Struct(
        "Prop_Dword_0" / Int32ul,
        "Prop_Dword_1" / Int32ul,
        "Prop_Dword_2" / Int32ul,
        "Prop_Dword_3" / Int32ul
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=105, version=0)
class Microsoft_Windows_MCCS_SyncController_105_0(Etw):
    pattern = Struct(
        "Prop_Dword_0" / Int32ul,
        "Prop_Dword_1" / Int32ul
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=106, version=0)
class Microsoft_Windows_MCCS_SyncController_106_0(Etw):
    pattern = Struct(
        "Prop_Dword_0" / Int32ul,
        "Prop_Dword_1" / Int32ul,
        "Prop_Dword_2" / Int32ul,
        "Prop_Dword_3" / Int32ul
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=191, version=0)
class Microsoft_Windows_MCCS_SyncController_191_0(Etw):
    pattern = Struct(
        "P2_UnicodeString" / WString
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=193, version=0)
class Microsoft_Windows_MCCS_SyncController_193_0(Etw):
    pattern = Struct(
        "P1_Guid" / Guid,
        "P2_UnicodeString" / WString
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=194, version=0)
class Microsoft_Windows_MCCS_SyncController_194_0(Etw):
    pattern = Struct(
        "P1_Guid" / Guid,
        "P2_UnicodeString" / WString
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=195, version=0)
class Microsoft_Windows_MCCS_SyncController_195_0(Etw):
    pattern = Struct(
        "P2_UnicodeString" / WString
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=196, version=0)
class Microsoft_Windows_MCCS_SyncController_196_0(Etw):
    pattern = Struct(
        "P1_Boolean" / Int8ul
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=201, version=0)
class Microsoft_Windows_MCCS_SyncController_201_0(Etw):
    pattern = Struct(
        "SyncMode" / Int32ul,
        "Prop_Dword_2" / Int32ul
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=500, version=0)
class Microsoft_Windows_MCCS_SyncController_500_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul,
        "EngineGuid" / Int32ul
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=501, version=0)
class Microsoft_Windows_MCCS_SyncController_501_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul,
        "EngineGuid" / Int32ul
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=502, version=0)
class Microsoft_Windows_MCCS_SyncController_502_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul,
        "EngineGuid" / Int32ul
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=503, version=0)
class Microsoft_Windows_MCCS_SyncController_503_0(Etw):
    pattern = Struct(
        "Prop_Dword_0" / Int32ul,
        "Prop_Dword_1" / Int32ul,
        "Prop_Dword_2" / Int32ul,
        "Prop_Dword_3" / Int32ul,
        "Prop_Dword_4" / Int32ul,
        "SaverMode" / Int32ul,
        "EngineGuid" / Int32ul
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=504, version=0)
class Microsoft_Windows_MCCS_SyncController_504_0(Etw):
    pattern = Struct(
        "Prop_Dword_0" / Int32ul,
        "Prop_Dword_1" / Int32ul,
        "Prop_Dword_2" / Int32ul,
        "Prop_Dword_3" / Int32ul,
        "SaverMode" / Int32ul,
        "EngineGuid" / Int32ul
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=505, version=0)
class Microsoft_Windows_MCCS_SyncController_505_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=506, version=0)
class Microsoft_Windows_MCCS_SyncController_506_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=507, version=0)
class Microsoft_Windows_MCCS_SyncController_507_0(Etw):
    pattern = Struct(
        "Prop_Dword_0" / Int32ul,
        "Prop_Dword_1" / Int32ul,
        "Prop_Dword_2" / Int32ul,
        "EngineGuid" / Int32ul
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=508, version=0)
class Microsoft_Windows_MCCS_SyncController_508_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul,
        "EngineGuid" / Int32ul
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=509, version=0)
class Microsoft_Windows_MCCS_SyncController_509_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=510, version=0)
class Microsoft_Windows_MCCS_SyncController_510_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=511, version=0)
class Microsoft_Windows_MCCS_SyncController_511_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=512, version=0)
class Microsoft_Windows_MCCS_SyncController_512_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=513, version=0)
class Microsoft_Windows_MCCS_SyncController_513_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul,
        "Prop_HResult_2" / Int32sl
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=516, version=0)
class Microsoft_Windows_MCCS_SyncController_516_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=517, version=0)
class Microsoft_Windows_MCCS_SyncController_517_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=518, version=0)
class Microsoft_Windows_MCCS_SyncController_518_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=519, version=0)
class Microsoft_Windows_MCCS_SyncController_519_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=522, version=0)
class Microsoft_Windows_MCCS_SyncController_522_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=523, version=0)
class Microsoft_Windows_MCCS_SyncController_523_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=524, version=0)
class Microsoft_Windows_MCCS_SyncController_524_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=525, version=0)
class Microsoft_Windows_MCCS_SyncController_525_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=526, version=0)
class Microsoft_Windows_MCCS_SyncController_526_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=527, version=0)
class Microsoft_Windows_MCCS_SyncController_527_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=530, version=0)
class Microsoft_Windows_MCCS_SyncController_530_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=531, version=0)
class Microsoft_Windows_MCCS_SyncController_531_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=534, version=0)
class Microsoft_Windows_MCCS_SyncController_534_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=535, version=0)
class Microsoft_Windows_MCCS_SyncController_535_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=536, version=0)
class Microsoft_Windows_MCCS_SyncController_536_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=537, version=0)
class Microsoft_Windows_MCCS_SyncController_537_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=538, version=0)
class Microsoft_Windows_MCCS_SyncController_538_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=539, version=0)
class Microsoft_Windows_MCCS_SyncController_539_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul,
        "Prop_HResult_2" / Int32sl
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=540, version=0)
class Microsoft_Windows_MCCS_SyncController_540_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=541, version=0)
class Microsoft_Windows_MCCS_SyncController_541_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=542, version=0)
class Microsoft_Windows_MCCS_SyncController_542_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=543, version=0)
class Microsoft_Windows_MCCS_SyncController_543_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=544, version=0)
class Microsoft_Windows_MCCS_SyncController_544_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul,
        "EngineGuid" / Int32ul
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=545, version=0)
class Microsoft_Windows_MCCS_SyncController_545_0(Etw):
    pattern = Struct(
        "P1_Guid" / Guid,
        "P2_UInt" / Int32ul
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=550, version=0)
class Microsoft_Windows_MCCS_SyncController_550_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul,
        "EngineGuid" / Int32ul
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=551, version=0)
class Microsoft_Windows_MCCS_SyncController_551_0(Etw):
    pattern = Struct(
        "Prop_Dword_0" / Int32ul,
        "Prop_Dword_1" / Int32ul,
        "Prop_Dword_2" / Int32ul
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=552, version=0)
class Microsoft_Windows_MCCS_SyncController_552_0(Etw):
    pattern = Struct(
        "Prop_Dword_0" / Int32ul,
        "Prop_Dword_1" / Int32ul,
        "Prop_Dword_2" / Int32ul
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=553, version=0)
class Microsoft_Windows_MCCS_SyncController_553_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=555, version=0)
class Microsoft_Windows_MCCS_SyncController_555_0(Etw):
    pattern = Struct(
        "Prop_Dword" / Int32ul,
        "Prop_ScheduleTriggerRequirementFlags" / Int32ul
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=556, version=0)
class Microsoft_Windows_MCCS_SyncController_556_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=561, version=0)
class Microsoft_Windows_MCCS_SyncController_561_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul,
        "Prop_HResult_2" / Int32sl
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=562, version=0)
class Microsoft_Windows_MCCS_SyncController_562_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul,
        "EngineGuid" / Int32ul
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=563, version=0)
class Microsoft_Windows_MCCS_SyncController_563_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul,
        "EngineGuid" / Int32ul
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=570, version=0)
class Microsoft_Windows_MCCS_SyncController_570_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul,
        "EngineGuid" / Int32ul,
        "WorkType" / Int32ul
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=701, version=0)
class Microsoft_Windows_MCCS_SyncController_701_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=702, version=0)
class Microsoft_Windows_MCCS_SyncController_702_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=801, version=0)
class Microsoft_Windows_MCCS_SyncController_801_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=802, version=0)
class Microsoft_Windows_MCCS_SyncController_802_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul,
        "Prop_Dword_2" / Int32ul
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=809, version=0)
class Microsoft_Windows_MCCS_SyncController_809_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=810, version=0)
class Microsoft_Windows_MCCS_SyncController_810_0(Etw):
    pattern = Struct(
        "Prop_Guid" / Guid,
        "Prop_Dword_1" / Int32ul,
        "Prop_Dword_2" / Int32ul,
        "Prop_Dword_3" / Int32ul,
        "Prop_Dword_4" / Int32ul,
        "Prop_ScheduleTriggerRequirementFlags" / Int32ul,
        "EngineGuid" / Int32ul
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=811, version=0)
class Microsoft_Windows_MCCS_SyncController_811_0(Etw):
    pattern = Struct(
        "Prop_Dword_0" / Int32ul,
        "Prop_Dword_1" / Int32ul
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=812, version=0)
class Microsoft_Windows_MCCS_SyncController_812_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=813, version=0)
class Microsoft_Windows_MCCS_SyncController_813_0(Etw):
    pattern = Struct(
        "Prop_Dword_1" / Int32ul
    )


@declare(guid=guid("7fcb9791-f481-46d1-846e-2eb6f003c4d3"), event_id=900, version=0)
class Microsoft_Windows_MCCS_SyncController_900_0(Etw):
    pattern = Struct(
        "P1_Boolean" / Int8ul
    )

