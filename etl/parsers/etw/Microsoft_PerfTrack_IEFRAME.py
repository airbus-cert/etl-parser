# -*- coding: utf-8 -*-
"""
Microsoft-PerfTrack-IEFRAME
GUID : b2a40f1f-a05a-4dfd-886a-4c4f18c4334c
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=101, version=0)
class Microsoft_PerfTrack_IEFRAME_101_0(Etw):
    pattern = Struct(
        "HWND" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=102, version=0)
class Microsoft_PerfTrack_IEFRAME_102_0(Etw):
    pattern = Struct(
        "HWND" / Int64ul,
        "NewTID" / Int32ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=103, version=0)
class Microsoft_PerfTrack_IEFRAME_103_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=104, version=0)
class Microsoft_PerfTrack_IEFRAME_104_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "NewTID" / Int32ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=105, version=0)
class Microsoft_PerfTrack_IEFRAME_105_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=106, version=0)
class Microsoft_PerfTrack_IEFRAME_106_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=107, version=0)
class Microsoft_PerfTrack_IEFRAME_107_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=108, version=0)
class Microsoft_PerfTrack_IEFRAME_108_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=109, version=0)
class Microsoft_PerfTrack_IEFRAME_109_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=110, version=0)
class Microsoft_PerfTrack_IEFRAME_110_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=111, version=0)
class Microsoft_PerfTrack_IEFRAME_111_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=116, version=0)
class Microsoft_PerfTrack_IEFRAME_116_0(Etw):
    pattern = Struct(
        "TimespanInMs" / Int32ul,
        "dwTabScenarioFlags" / Int32ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=119, version=0)
class Microsoft_PerfTrack_IEFRAME_119_0(Etw):
    pattern = Struct(
        "TimespanInMs" / Int32ul,
        "dwTabScenarioFlags" / Int32ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=120, version=0)
class Microsoft_PerfTrack_IEFRAME_120_0(Etw):
    pattern = Struct(
        "TimespanInMs" / Int32ul,
        "dwTabScenarioFlags" / Int32ul,
        "totalTabCount" / Int32ul,
        "halfTabCount" / Int32ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=122, version=0)
class Microsoft_PerfTrack_IEFRAME_122_0(Etw):
    pattern = Struct(
        "TimespanInMs" / Int32ul,
        "dwTabScenarioFlags" / Int32ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=124, version=0)
class Microsoft_PerfTrack_IEFRAME_124_0(Etw):
    pattern = Struct(
        "TimespanInMs" / Int32ul,
        "dwTabScenarioFlags" / Int32ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=201, version=0)
class Microsoft_PerfTrack_IEFRAME_201_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=202, version=0)
class Microsoft_PerfTrack_IEFRAME_202_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=203, version=0)
class Microsoft_PerfTrack_IEFRAME_203_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=204, version=0)
class Microsoft_PerfTrack_IEFRAME_204_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=205, version=0)
class Microsoft_PerfTrack_IEFRAME_205_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=206, version=0)
class Microsoft_PerfTrack_IEFRAME_206_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=207, version=0)
class Microsoft_PerfTrack_IEFRAME_207_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=208, version=0)
class Microsoft_PerfTrack_IEFRAME_208_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=209, version=0)
class Microsoft_PerfTrack_IEFRAME_209_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=210, version=0)
class Microsoft_PerfTrack_IEFRAME_210_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=211, version=0)
class Microsoft_PerfTrack_IEFRAME_211_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=212, version=0)
class Microsoft_PerfTrack_IEFRAME_212_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=213, version=0)
class Microsoft_PerfTrack_IEFRAME_213_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=214, version=0)
class Microsoft_PerfTrack_IEFRAME_214_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=301, version=0)
class Microsoft_PerfTrack_IEFRAME_301_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=302, version=0)
class Microsoft_PerfTrack_IEFRAME_302_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=303, version=0)
class Microsoft_PerfTrack_IEFRAME_303_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=304, version=0)
class Microsoft_PerfTrack_IEFRAME_304_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=305, version=0)
class Microsoft_PerfTrack_IEFRAME_305_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "ID" / Int32ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=306, version=0)
class Microsoft_PerfTrack_IEFRAME_306_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "ID" / Int32ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=601, version=0)
class Microsoft_PerfTrack_IEFRAME_601_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "TID" / Int32ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=602, version=0)
class Microsoft_PerfTrack_IEFRAME_602_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "TID" / Int32ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=603, version=0)
class Microsoft_PerfTrack_IEFRAME_603_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=604, version=0)
class Microsoft_PerfTrack_IEFRAME_604_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=607, version=0)
class Microsoft_PerfTrack_IEFRAME_607_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=608, version=0)
class Microsoft_PerfTrack_IEFRAME_608_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=609, version=0)
class Microsoft_PerfTrack_IEFRAME_609_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=610, version=0)
class Microsoft_PerfTrack_IEFRAME_610_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=611, version=0)
class Microsoft_PerfTrack_IEFRAME_611_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=612, version=0)
class Microsoft_PerfTrack_IEFRAME_612_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=613, version=0)
class Microsoft_PerfTrack_IEFRAME_613_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=614, version=0)
class Microsoft_PerfTrack_IEFRAME_614_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=615, version=0)
class Microsoft_PerfTrack_IEFRAME_615_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=616, version=0)
class Microsoft_PerfTrack_IEFRAME_616_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=617, version=0)
class Microsoft_PerfTrack_IEFRAME_617_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=618, version=0)
class Microsoft_PerfTrack_IEFRAME_618_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=619, version=0)
class Microsoft_PerfTrack_IEFRAME_619_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=620, version=0)
class Microsoft_PerfTrack_IEFRAME_620_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=621, version=0)
class Microsoft_PerfTrack_IEFRAME_621_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=622, version=0)
class Microsoft_PerfTrack_IEFRAME_622_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=623, version=0)
class Microsoft_PerfTrack_IEFRAME_623_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=625, version=0)
class Microsoft_PerfTrack_IEFRAME_625_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=627, version=0)
class Microsoft_PerfTrack_IEFRAME_627_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=629, version=0)
class Microsoft_PerfTrack_IEFRAME_629_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=631, version=0)
class Microsoft_PerfTrack_IEFRAME_631_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=633, version=0)
class Microsoft_PerfTrack_IEFRAME_633_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=634, version=0)
class Microsoft_PerfTrack_IEFRAME_634_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=635, version=0)
class Microsoft_PerfTrack_IEFRAME_635_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=636, version=0)
class Microsoft_PerfTrack_IEFRAME_636_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=637, version=0)
class Microsoft_PerfTrack_IEFRAME_637_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=638, version=0)
class Microsoft_PerfTrack_IEFRAME_638_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=639, version=0)
class Microsoft_PerfTrack_IEFRAME_639_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=640, version=0)
class Microsoft_PerfTrack_IEFRAME_640_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=641, version=0)
class Microsoft_PerfTrack_IEFRAME_641_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "TID" / Int32ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=642, version=0)
class Microsoft_PerfTrack_IEFRAME_642_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "TID" / Int32ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=643, version=0)
class Microsoft_PerfTrack_IEFRAME_643_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "TID" / Int32ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=644, version=0)
class Microsoft_PerfTrack_IEFRAME_644_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=645, version=0)
class Microsoft_PerfTrack_IEFRAME_645_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=646, version=0)
class Microsoft_PerfTrack_IEFRAME_646_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=647, version=0)
class Microsoft_PerfTrack_IEFRAME_647_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "TID" / Int32ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=650, version=0)
class Microsoft_PerfTrack_IEFRAME_650_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=651, version=0)
class Microsoft_PerfTrack_IEFRAME_651_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=652, version=0)
class Microsoft_PerfTrack_IEFRAME_652_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=653, version=0)
class Microsoft_PerfTrack_IEFRAME_653_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=700, version=0)
class Microsoft_PerfTrack_IEFRAME_700_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=701, version=0)
class Microsoft_PerfTrack_IEFRAME_701_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=702, version=0)
class Microsoft_PerfTrack_IEFRAME_702_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=703, version=0)
class Microsoft_PerfTrack_IEFRAME_703_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=704, version=0)
class Microsoft_PerfTrack_IEFRAME_704_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=705, version=0)
class Microsoft_PerfTrack_IEFRAME_705_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=706, version=0)
class Microsoft_PerfTrack_IEFRAME_706_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=707, version=0)
class Microsoft_PerfTrack_IEFRAME_707_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=708, version=0)
class Microsoft_PerfTrack_IEFRAME_708_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=709, version=0)
class Microsoft_PerfTrack_IEFRAME_709_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=710, version=0)
class Microsoft_PerfTrack_IEFRAME_710_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=711, version=0)
class Microsoft_PerfTrack_IEFRAME_711_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=712, version=0)
class Microsoft_PerfTrack_IEFRAME_712_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=713, version=0)
class Microsoft_PerfTrack_IEFRAME_713_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=714, version=0)
class Microsoft_PerfTrack_IEFRAME_714_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=715, version=0)
class Microsoft_PerfTrack_IEFRAME_715_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=716, version=0)
class Microsoft_PerfTrack_IEFRAME_716_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=717, version=0)
class Microsoft_PerfTrack_IEFRAME_717_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=800, version=0)
class Microsoft_PerfTrack_IEFRAME_800_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=801, version=0)
class Microsoft_PerfTrack_IEFRAME_801_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=806, version=0)
class Microsoft_PerfTrack_IEFRAME_806_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=807, version=0)
class Microsoft_PerfTrack_IEFRAME_807_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=808, version=0)
class Microsoft_PerfTrack_IEFRAME_808_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=809, version=0)
class Microsoft_PerfTrack_IEFRAME_809_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=810, version=0)
class Microsoft_PerfTrack_IEFRAME_810_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=811, version=0)
class Microsoft_PerfTrack_IEFRAME_811_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=812, version=0)
class Microsoft_PerfTrack_IEFRAME_812_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=813, version=0)
class Microsoft_PerfTrack_IEFRAME_813_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=816, version=0)
class Microsoft_PerfTrack_IEFRAME_816_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=817, version=0)
class Microsoft_PerfTrack_IEFRAME_817_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "ID" / Int32ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=818, version=0)
class Microsoft_PerfTrack_IEFRAME_818_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "ID" / Int32ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=819, version=0)
class Microsoft_PerfTrack_IEFRAME_819_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "ID" / Int32ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=828, version=0)
class Microsoft_PerfTrack_IEFRAME_828_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=829, version=0)
class Microsoft_PerfTrack_IEFRAME_829_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=830, version=0)
class Microsoft_PerfTrack_IEFRAME_830_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=831, version=0)
class Microsoft_PerfTrack_IEFRAME_831_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=832, version=0)
class Microsoft_PerfTrack_IEFRAME_832_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=833, version=0)
class Microsoft_PerfTrack_IEFRAME_833_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=836, version=0)
class Microsoft_PerfTrack_IEFRAME_836_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=837, version=0)
class Microsoft_PerfTrack_IEFRAME_837_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=838, version=0)
class Microsoft_PerfTrack_IEFRAME_838_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=839, version=0)
class Microsoft_PerfTrack_IEFRAME_839_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=840, version=0)
class Microsoft_PerfTrack_IEFRAME_840_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=841, version=0)
class Microsoft_PerfTrack_IEFRAME_841_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=842, version=0)
class Microsoft_PerfTrack_IEFRAME_842_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=843, version=0)
class Microsoft_PerfTrack_IEFRAME_843_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=844, version=0)
class Microsoft_PerfTrack_IEFRAME_844_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=845, version=0)
class Microsoft_PerfTrack_IEFRAME_845_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=846, version=0)
class Microsoft_PerfTrack_IEFRAME_846_0(Etw):
    pattern = Struct(
        "Cookie" / Int32ul,
        "AnimationType" / Int32ul,
        "RowCount" / Int32ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=847, version=0)
class Microsoft_PerfTrack_IEFRAME_847_0(Etw):
    pattern = Struct(
        "Cookie" / Int32ul,
        "AnimationType" / Int32ul,
        "RowCount" / Int32ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=900, version=0)
class Microsoft_PerfTrack_IEFRAME_900_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=901, version=0)
class Microsoft_PerfTrack_IEFRAME_901_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=902, version=0)
class Microsoft_PerfTrack_IEFRAME_902_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=903, version=0)
class Microsoft_PerfTrack_IEFRAME_903_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=908, version=0)
class Microsoft_PerfTrack_IEFRAME_908_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=909, version=0)
class Microsoft_PerfTrack_IEFRAME_909_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=910, version=0)
class Microsoft_PerfTrack_IEFRAME_910_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=911, version=0)
class Microsoft_PerfTrack_IEFRAME_911_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=912, version=0)
class Microsoft_PerfTrack_IEFRAME_912_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=914, version=0)
class Microsoft_PerfTrack_IEFRAME_914_0(Etw):
    pattern = Struct(
        "FileVersion" / Int32ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=915, version=0)
class Microsoft_PerfTrack_IEFRAME_915_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=916, version=0)
class Microsoft_PerfTrack_IEFRAME_916_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=917, version=0)
class Microsoft_PerfTrack_IEFRAME_917_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=918, version=0)
class Microsoft_PerfTrack_IEFRAME_918_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=919, version=0)
class Microsoft_PerfTrack_IEFRAME_919_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=920, version=0)
class Microsoft_PerfTrack_IEFRAME_920_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=921, version=0)
class Microsoft_PerfTrack_IEFRAME_921_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=922, version=0)
class Microsoft_PerfTrack_IEFRAME_922_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=923, version=0)
class Microsoft_PerfTrack_IEFRAME_923_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=924, version=0)
class Microsoft_PerfTrack_IEFRAME_924_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=925, version=0)
class Microsoft_PerfTrack_IEFRAME_925_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=926, version=0)
class Microsoft_PerfTrack_IEFRAME_926_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=930, version=0)
class Microsoft_PerfTrack_IEFRAME_930_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=931, version=0)
class Microsoft_PerfTrack_IEFRAME_931_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=933, version=0)
class Microsoft_PerfTrack_IEFRAME_933_0(Etw):
    pattern = Struct(
        "TriggerProtectionHResult" / Int32ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=934, version=0)
class Microsoft_PerfTrack_IEFRAME_934_0(Etw):
    pattern = Struct(
        "OpType" / Int32ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=935, version=0)
class Microsoft_PerfTrack_IEFRAME_935_0(Etw):
    pattern = Struct(
        "OpType" / Int32ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=936, version=0)
class Microsoft_PerfTrack_IEFRAME_936_0(Etw):
    pattern = Struct(
        "OpType" / Int32ul
    )


@declare(guid=guid("b2a40f1f-a05a-4dfd-886a-4c4f18c4334c"), event_id=937, version=0)
class Microsoft_PerfTrack_IEFRAME_937_0(Etw):
    pattern = Struct(
        "OpType" / Int32ul
    )

