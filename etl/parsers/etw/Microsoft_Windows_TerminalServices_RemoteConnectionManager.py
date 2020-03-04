# -*- coding: utf-8 -*-
"""
Microsoft-Windows-TerminalServices-RemoteConnectionManager
GUID : c76baa63-ae81-421c-b425-340b4b24157f
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=2, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_2_0(Etw):
    pattern = Struct(
        "message" / CString
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=3, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_3_0(Etw):
    pattern = Struct(
        "message" / CString
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=4, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_4_0(Etw):
    pattern = Struct(
        "message" / CString
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=5, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_5_0(Etw):
    pattern = Struct(
        "message" / CString
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=6, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_6_0(Etw):
    pattern = Struct(
        "message" / CString
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=7, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_7_0(Etw):
    pattern = Struct(
        "message" / CString
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=8, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_8_0(Etw):
    pattern = Struct(
        "message" / CString
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=9, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_9_0(Etw):
    pattern = Struct(
        "message" / CString
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=257, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_257_0(Etw):
    pattern = Struct(
        "isSuccess" / Int8ul
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=258, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_258_0(Etw):
    pattern = Struct(
        "listenerName" / WString
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=259, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_259_0(Etw):
    pattern = Struct(
        "listenerName" / WString
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=260, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_260_0(Etw):
    pattern = Struct(
        "listenerName" / WString,
        "errorCode" / Int64ul
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=261, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_261_0(Etw):
    pattern = Struct(
        "listenerName" / WString
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=262, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_262_0(Etw):
    pattern = Struct(
        "listenerName" / WString
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=272, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_272_0(Etw):
    pattern = Struct(
        "Param1" / WString
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=273, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_273_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / Int32sl,
        "Param3" / Int64sl,
        "Param4" / Int64sl
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=274, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_274_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / Int32sl,
        "Param3" / Int64sl
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=1003, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_1003_0(Etw):
    pattern = Struct(
        "Param1" / WString
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=1011, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_1011_0(Etw):
    pattern = Struct(
        "Param1" / WString
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=1137, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_1137_0(Etw):
    pattern = Struct(
        "Param1" / Int32ul
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=1138, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_1138_0(Etw):
    pattern = Struct(
        "Param1" / Int32ul
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=1139, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_1139_0(Etw):
    pattern = Struct(
        "Param1" / Int32ul
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=1140, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_1140_0(Etw):
    pattern = Struct(
        "Param1" / Int32ul
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=1141, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_1141_0(Etw):
    pattern = Struct(
        "Param1" / Int32ul
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=1144, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_1144_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / Int32ul,
        "Param3" / Int32ul
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=1145, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_1145_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / Int32ul
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=1146, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_1146_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Param3" / WString
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=1147, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_1147_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Param3" / WString
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=1148, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_1148_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Param3" / WString
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=1149, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_1149_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Param3" / WString
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=1150, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_1150_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Param3" / WString
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=1151, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_1151_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Param3" / WString
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=1152, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_1152_0(Etw):
    pattern = Struct(
        "Param1" / Int32ul
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=1153, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_1153_0(Etw):
    pattern = Struct(
        "Param1" / Int32ul
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=1157, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_1157_0(Etw):
    pattern = Struct(
        "listenerName" / WString
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=1158, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_1158_0(Etw):
    pattern = Struct(
        "Param1" / WString
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=1280, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_1280_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Param3" / Int32sl
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=1281, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_1281_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Param3" / Int32sl
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=1282, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_1282_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / Int32ul
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=1283, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_1283_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / Int32ul
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=1284, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_1284_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=1285, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_1285_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=1286, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_1286_0(Etw):
    pattern = Struct(
        "Param1" / WString
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=1287, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_1287_0(Etw):
    pattern = Struct(
        "Param1" / WString
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=1288, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_1288_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=1289, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_1289_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=2304, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_2304_0(Etw):
    pattern = Struct(
        "Param1" / Int32sl
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=2305, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_2305_0(Etw):
    pattern = Struct(
        "Param1" / Int32sl
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=2306, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_2306_0(Etw):
    pattern = Struct(
        "Param1" / Int32sl,
        "Param2" / WString
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=2307, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_2307_0(Etw):
    pattern = Struct(
        "Param1" / Int32sl,
        "Param2" / WString
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=20482, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_20482_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / Int32sl
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=20483, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_20483_0(Etw):
    pattern = Struct(
        "Param1" / Int32sl,
        "Param2" / Int32sl
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=20484, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_20484_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / Int32ul
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=20485, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_20485_0(Etw):
    pattern = Struct(
        "Param1" / Int32sl,
        "Param2" / Int32ul
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=20486, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_20486_0(Etw):
    pattern = Struct(
        "Param1" / Int32sl,
        "Param2" / Int32ul
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=20487, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_20487_0(Etw):
    pattern = Struct(
        "Param1" / WString
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=20488, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_20488_0(Etw):
    pattern = Struct(
        "Param1" / Int32sl
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=20489, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_20489_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / Int32ul
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=20490, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_20490_0(Etw):
    pattern = Struct(
        "Param1" / Int32sl,
        "Param2" / Int32ul
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=20491, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_20491_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / Int32ul,
        "Param3" / Int32sl
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=20492, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_20492_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / Int32ul,
        "Param3" / Int32sl
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=20493, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_20493_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / Int32ul,
        "Param3" / Int32sl
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=20494, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_20494_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / Int32ul,
        "Param3" / Int32sl
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=20495, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_20495_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / Int32ul,
        "Param3" / Int32sl
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=20496, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_20496_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / Int32ul,
        "Param3" / Int32sl
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=20499, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_20499_0(Etw):
    pattern = Struct(
        "UserName" / WString,
        "ServerName" / WString
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=20500, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_20500_0(Etw):
    pattern = Struct(
        "UserName" / WString,
        "ServerName" / WString,
        "time" / Int32sl
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=20502, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_20502_0(Etw):
    pattern = Struct(
        "Session" / Int32sl
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=20503, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_20503_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Param3" / WString,
        "Param4" / Int32sl
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=20504, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_20504_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Param3" / WString,
        "Param4" / Int32sl
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=20506, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_20506_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Param3" / WString,
        "Param4" / Int32sl
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=20507, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_20507_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Param3" / WString,
        "Param4" / Int32sl
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=20508, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_20508_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Param3" / Int32sl
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=20509, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_20509_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Param3" / Int32sl
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=20510, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_20510_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Param3" / Int32sl
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=20511, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_20511_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Param3" / Int32sl
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=20512, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_20512_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Param3" / Int32ul,
        "Param4" / Int32sl
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=20513, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_20513_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Param3" / Int32sl
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=20514, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_20514_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Param3" / Int32sl
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=20515, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_20515_0(Etw):
    pattern = Struct(
        "Session" / Int32sl
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=20516, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_20516_0(Etw):
    pattern = Struct(
        "Session" / Int32sl
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=20517, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_20517_0(Etw):
    pattern = Struct(
        "Session" / Int32sl
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=20518, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_20518_0(Etw):
    pattern = Struct(
        "Session" / Int32sl
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=20519, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_20519_0(Etw):
    pattern = Struct(
        "Session" / Int32sl
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=20520, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_20520_0(Etw):
    pattern = Struct(
        "Param1" / WString
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=20521, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_20521_0(Etw):
    pattern = Struct(
        "Param1" / WString
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=20522, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_20522_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString,
        "Param3" / WString,
        "Param4" / Int32sl,
        "Param5" / Int32sl
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=20523, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_20523_0(Etw):
    pattern = Struct(
        "ListenerName" / WString,
        "Class" / Guid
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=50180, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_50180_0(Etw):
    pattern = Struct(
        "Param1" / WString
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=50195, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_50195_0(Etw):
    pattern = Struct(
        "Param1" / WString
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=50213, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_50213_0(Etw):
    pattern = Struct(
        "errorCode" / WString
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=50214, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_50214_0(Etw):
    pattern = Struct(
        "errorCode" / WString
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=50215, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_50215_0(Etw):
    pattern = Struct(
        "errorCode" / WString
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=50281, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_50281_0(Etw):
    pattern = Struct(
        "Param1" / WString
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=50283, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_50283_0(Etw):
    pattern = Struct(
        "Param1" / WString
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=50284, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_50284_0(Etw):
    pattern = Struct(
        "Param1" / WString
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=50307, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_50307_0(Etw):
    pattern = Struct(
        "Param1" / WString
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=50309, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_50309_0(Etw):
    pattern = Struct(
        "Param1" / WString
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=50310, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_50310_0(Etw):
    pattern = Struct(
        "Param1" / WString
    )


@declare(guid=guid("c76baa63-ae81-421c-b425-340b4b24157f"), event_id=50312, version=0)
class Microsoft_Windows_TerminalServices_RemoteConnectionManager_50312_0(Etw):
    pattern = Struct(
        "Param1" / WString
    )

