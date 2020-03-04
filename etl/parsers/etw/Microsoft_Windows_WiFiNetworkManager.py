# -*- coding: utf-8 -*-
"""
Microsoft-Windows-WiFiNetworkManager
GUID : e5c16d49-2464-4382-bb20-97a4b5465db9
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=0, version=0)
class Microsoft_Windows_WiFiNetworkManager_0_0(Etw):
    pattern = Struct(
        "Message" / Int64ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1, version=0)
class Microsoft_Windows_WiFiNetworkManager_1_0(Etw):
    pattern = Struct(
        "Message" / Int64ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=2, version=0)
class Microsoft_Windows_WiFiNetworkManager_2_0(Etw):
    pattern = Struct(
        "Message" / Int64ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=100, version=0)
class Microsoft_Windows_WiFiNetworkManager_100_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=106, version=0)
class Microsoft_Windows_WiFiNetworkManager_106_0(Etw):
    pattern = Struct(
        "type" / Int32ul,
        "state" / Int32ul,
        "error" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=107, version=0)
class Microsoft_Windows_WiFiNetworkManager_107_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=200, version=0)
class Microsoft_Windows_WiFiNetworkManager_200_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=201, version=0)
class Microsoft_Windows_WiFiNetworkManager_201_0(Etw):
    pattern = Struct(
        "dwValue1" / Int32ul,
        "dwValue2" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=202, version=0)
class Microsoft_Windows_WiFiNetworkManager_202_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=203, version=0)
class Microsoft_Windows_WiFiNetworkManager_203_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=204, version=0)
class Microsoft_Windows_WiFiNetworkManager_204_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=206, version=0)
class Microsoft_Windows_WiFiNetworkManager_206_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=211, version=0)
class Microsoft_Windows_WiFiNetworkManager_211_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=212, version=0)
class Microsoft_Windows_WiFiNetworkManager_212_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=214, version=0)
class Microsoft_Windows_WiFiNetworkManager_214_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=215, version=0)
class Microsoft_Windows_WiFiNetworkManager_215_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=216, version=0)
class Microsoft_Windows_WiFiNetworkManager_216_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=217, version=0)
class Microsoft_Windows_WiFiNetworkManager_217_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=219, version=0)
class Microsoft_Windows_WiFiNetworkManager_219_0(Etw):
    pattern = Struct(
        "dwValue1" / Int32ul,
        "dwValue2" / Int32ul,
        "dwValue3" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=221, version=0)
class Microsoft_Windows_WiFiNetworkManager_221_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=222, version=0)
class Microsoft_Windows_WiFiNetworkManager_222_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=224, version=0)
class Microsoft_Windows_WiFiNetworkManager_224_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=300, version=0)
class Microsoft_Windows_WiFiNetworkManager_300_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=301, version=0)
class Microsoft_Windows_WiFiNetworkManager_301_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=305, version=0)
class Microsoft_Windows_WiFiNetworkManager_305_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=306, version=0)
class Microsoft_Windows_WiFiNetworkManager_306_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=307, version=0)
class Microsoft_Windows_WiFiNetworkManager_307_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=311, version=0)
class Microsoft_Windows_WiFiNetworkManager_311_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=314, version=0)
class Microsoft_Windows_WiFiNetworkManager_314_0(Etw):
    pattern = Struct(
        "ssidLen" / Int32ul,
        "ssid" / Bytes(lambda this: this.ssidLen)
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=316, version=0)
class Microsoft_Windows_WiFiNetworkManager_316_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=317, version=0)
class Microsoft_Windows_WiFiNetworkManager_317_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul,
        "ssidLen" / Int32ul,
        "ssid" / Bytes(lambda this: this.ssidLen)
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=319, version=0)
class Microsoft_Windows_WiFiNetworkManager_319_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=320, version=0)
class Microsoft_Windows_WiFiNetworkManager_320_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=322, version=0)
class Microsoft_Windows_WiFiNetworkManager_322_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=323, version=0)
class Microsoft_Windows_WiFiNetworkManager_323_0(Etw):
    pattern = Struct(
        "algo" / Int32ul,
        "cipher" / Int32ul,
        "secure" / Int32ul,
        "signal" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=324, version=0)
class Microsoft_Windows_WiFiNetworkManager_324_0(Etw):
    pattern = Struct(
        "szConnName" / WString
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=325, version=0)
class Microsoft_Windows_WiFiNetworkManager_325_0(Etw):
    pattern = Struct(
        "szConnName" / WString
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=326, version=0)
class Microsoft_Windows_WiFiNetworkManager_326_0(Etw):
    pattern = Struct(
        "ssidLen" / Int32ul,
        "ssid" / Bytes(lambda this: this.ssidLen)
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=327, version=0)
class Microsoft_Windows_WiFiNetworkManager_327_0(Etw):
    pattern = Struct(
        "szConnName" / WString
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=331, version=0)
class Microsoft_Windows_WiFiNetworkManager_331_0(Etw):
    pattern = Struct(
        "szConnName" / WString
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=333, version=0)
class Microsoft_Windows_WiFiNetworkManager_333_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=401, version=0)
class Microsoft_Windows_WiFiNetworkManager_401_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=403, version=0)
class Microsoft_Windows_WiFiNetworkManager_403_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=404, version=0)
class Microsoft_Windows_WiFiNetworkManager_404_0(Etw):
    pattern = Struct(
        "dwValue1" / Int32ul,
        "dwValue2" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=405, version=0)
class Microsoft_Windows_WiFiNetworkManager_405_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=406, version=0)
class Microsoft_Windows_WiFiNetworkManager_406_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=407, version=0)
class Microsoft_Windows_WiFiNetworkManager_407_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=408, version=0)
class Microsoft_Windows_WiFiNetworkManager_408_0(Etw):
    pattern = Struct(
        "szString" / WString,
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=600, version=0)
class Microsoft_Windows_WiFiNetworkManager_600_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=601, version=0)
class Microsoft_Windows_WiFiNetworkManager_601_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=602, version=0)
class Microsoft_Windows_WiFiNetworkManager_602_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=603, version=0)
class Microsoft_Windows_WiFiNetworkManager_603_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=604, version=0)
class Microsoft_Windows_WiFiNetworkManager_604_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=605, version=0)
class Microsoft_Windows_WiFiNetworkManager_605_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=606, version=0)
class Microsoft_Windows_WiFiNetworkManager_606_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=607, version=0)
class Microsoft_Windows_WiFiNetworkManager_607_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=608, version=0)
class Microsoft_Windows_WiFiNetworkManager_608_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=609, version=0)
class Microsoft_Windows_WiFiNetworkManager_609_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=610, version=0)
class Microsoft_Windows_WiFiNetworkManager_610_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1006, version=0)
class Microsoft_Windows_WiFiNetworkManager_1006_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1012, version=0)
class Microsoft_Windows_WiFiNetworkManager_1012_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1013, version=0)
class Microsoft_Windows_WiFiNetworkManager_1013_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1016, version=0)
class Microsoft_Windows_WiFiNetworkManager_1016_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1017, version=0)
class Microsoft_Windows_WiFiNetworkManager_1017_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1018, version=0)
class Microsoft_Windows_WiFiNetworkManager_1018_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1019, version=0)
class Microsoft_Windows_WiFiNetworkManager_1019_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1020, version=0)
class Microsoft_Windows_WiFiNetworkManager_1020_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1021, version=0)
class Microsoft_Windows_WiFiNetworkManager_1021_0(Etw):
    pattern = Struct(
        "dwValue1" / Int32ul,
        "dwValue2" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1022, version=0)
class Microsoft_Windows_WiFiNetworkManager_1022_0(Etw):
    pattern = Struct(
        "dwValue1" / Int32ul,
        "dwValue2" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1023, version=0)
class Microsoft_Windows_WiFiNetworkManager_1023_0(Etw):
    pattern = Struct(
        "dwValue1" / Int32ul,
        "dwValue2" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1024, version=0)
class Microsoft_Windows_WiFiNetworkManager_1024_0(Etw):
    pattern = Struct(
        "port" / Int32ul,
        "winerror" / Int32ul,
        "reasoncode" / Int32ul,
        "eaptype" / Int32ul,
        "string" / WString
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1025, version=0)
class Microsoft_Windows_WiFiNetworkManager_1025_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1026, version=0)
class Microsoft_Windows_WiFiNetworkManager_1026_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1027, version=0)
class Microsoft_Windows_WiFiNetworkManager_1027_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1028, version=0)
class Microsoft_Windows_WiFiNetworkManager_1028_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1029, version=0)
class Microsoft_Windows_WiFiNetworkManager_1029_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1030, version=0)
class Microsoft_Windows_WiFiNetworkManager_1030_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1031, version=0)
class Microsoft_Windows_WiFiNetworkManager_1031_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul,
        "ssidLen" / Int32ul,
        "ssid" / Bytes(lambda this: this.ssidLen)
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1032, version=0)
class Microsoft_Windows_WiFiNetworkManager_1032_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1033, version=0)
class Microsoft_Windows_WiFiNetworkManager_1033_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1034, version=0)
class Microsoft_Windows_WiFiNetworkManager_1034_0(Etw):
    pattern = Struct(
        "dwValue1" / Int32ul,
        "dwValue2" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1035, version=0)
class Microsoft_Windows_WiFiNetworkManager_1035_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1038, version=0)
class Microsoft_Windows_WiFiNetworkManager_1038_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1040, version=0)
class Microsoft_Windows_WiFiNetworkManager_1040_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1042, version=0)
class Microsoft_Windows_WiFiNetworkManager_1042_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1043, version=0)
class Microsoft_Windows_WiFiNetworkManager_1043_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1045, version=0)
class Microsoft_Windows_WiFiNetworkManager_1045_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1047, version=0)
class Microsoft_Windows_WiFiNetworkManager_1047_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1400, version=0)
class Microsoft_Windows_WiFiNetworkManager_1400_0(Etw):
    pattern = Struct(
        "dwValue1" / Int32ul,
        "dwValue2" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1401, version=0)
class Microsoft_Windows_WiFiNetworkManager_1401_0(Etw):
    pattern = Struct(
        "Error" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1402, version=0)
class Microsoft_Windows_WiFiNetworkManager_1402_0(Etw):
    pattern = Struct(
        "trigger" / Int32ul,
        "active" / Int32ul,
        "delayed" / Int32ul,
        "timer" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1403, version=0)
class Microsoft_Windows_WiFiNetworkManager_1403_0(Etw):
    pattern = Struct(
        "trigger" / Int32ul,
        "active" / Int32ul,
        "delayed" / Int32ul,
        "timer" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1404, version=0)
class Microsoft_Windows_WiFiNetworkManager_1404_0(Etw):
    pattern = Struct(
        "trigger" / Int32ul,
        "active" / Int32ul,
        "delayed" / Int32ul,
        "timer" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1405, version=0)
class Microsoft_Windows_WiFiNetworkManager_1405_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1406, version=0)
class Microsoft_Windows_WiFiNetworkManager_1406_0(Etw):
    pattern = Struct(
        "active" / Int32ul,
        "delayed" / Int32ul,
        "timer" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1407, version=0)
class Microsoft_Windows_WiFiNetworkManager_1407_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1408, version=0)
class Microsoft_Windows_WiFiNetworkManager_1408_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1500, version=0)
class Microsoft_Windows_WiFiNetworkManager_1500_0(Etw):
    pattern = Struct(
        "Error" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1503, version=0)
class Microsoft_Windows_WiFiNetworkManager_1503_0(Etw):
    pattern = Struct(
        "Error" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1508, version=0)
class Microsoft_Windows_WiFiNetworkManager_1508_0(Etw):
    pattern = Struct(
        "Error" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1509, version=0)
class Microsoft_Windows_WiFiNetworkManager_1509_0(Etw):
    pattern = Struct(
        "dwValue1" / Int32ul,
        "dwValue2" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1511, version=0)
class Microsoft_Windows_WiFiNetworkManager_1511_0(Etw):
    pattern = Struct(
        "dwValue1" / Int32ul,
        "dwValue2" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1512, version=0)
class Microsoft_Windows_WiFiNetworkManager_1512_0(Etw):
    pattern = Struct(
        "Error" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1600, version=0)
class Microsoft_Windows_WiFiNetworkManager_1600_0(Etw):
    pattern = Struct(
        "szString" / CString
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1601, version=0)
class Microsoft_Windows_WiFiNetworkManager_1601_0(Etw):
    pattern = Struct(
        "szString" / CString
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1602, version=0)
class Microsoft_Windows_WiFiNetworkManager_1602_0(Etw):
    pattern = Struct(
        "szString1" / WString,
        "dwValue1" / Int32ul,
        "dwValue2" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1603, version=0)
class Microsoft_Windows_WiFiNetworkManager_1603_0(Etw):
    pattern = Struct(
        "dwValue1" / Int32ul,
        "dwValue2" / Int32ul,
        "dwValue3" / Int32ul,
        "dwValue4" / Int32ul,
        "dwValue5" / Int32ul,
        "dwValue6" / Int32ul,
        "dwValue7" / Int32ul,
        "dwValue8" / Int32ul,
        "dwValue9" / Int32ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1604, version=0)
class Microsoft_Windows_WiFiNetworkManager_1604_0(Etw):
    pattern = Struct(
        "wsSource" / WString,
        "wsConnName" / WString,
        "szNotifType" / CString,
        "szNotifState" / CString,
        "dwType" / Int32ul,
        "dwState" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1605, version=0)
class Microsoft_Windows_WiFiNetworkManager_1605_0(Etw):
    pattern = Struct(
        "dwValue1" / Int32ul,
        "dwValue2" / Int32ul,
        "dwValue3" / Int32ul,
        "dwValue4" / Int32ul,
        "dwValue5" / Int32ul,
        "Ssid" / CString
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1606, version=0)
class Microsoft_Windows_WiFiNetworkManager_1606_0(Etw):
    pattern = Struct(
        "szString" / CString,
        "dwValue1" / Int32ul,
        "dwValue2" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1607, version=0)
class Microsoft_Windows_WiFiNetworkManager_1607_0(Etw):
    pattern = Struct(
        "szString" / CString,
        "dwValue1" / Int32ul,
        "dwValue2" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1608, version=0)
class Microsoft_Windows_WiFiNetworkManager_1608_0(Etw):
    pattern = Struct(
        "dwIndex" / Int32ul,
        "szNetwork" / CString,
        "dwAuth" / Int32ul,
        "dwCipher" / Int32ul,
        "dwQuality" / Int32ul,
        "dwFlags" / Int32ul,
        "Score" / Float32l,
        "dwCPSize" / Int32ul,
        "dwCPOffset" / Int32ul,
        "dwCredSize" / Int32ul,
        "dwCredOffset" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1609, version=0)
class Microsoft_Windows_WiFiNetworkManager_1609_0(Etw):
    pattern = Struct(
        "QueryType" / Int32ul,
        "QuerySources" / Int32ul,
        "dwNetworkOut" / Int32ul,
        "dwNetworksIn" / Int32ul,
        "dwFlags" / Int32ul,
        "dwACEnabled" / Int32ul,
        "ConfScanTO" / Int32ul,
        "MinLinkQ" / Int32ul,
        "MinScore" / Float32l,
        "dwScoreWt" / Int32ul,
        "dwSignalWt" / Int32ul,
        "OverlapP" / Int32ul,
        "dwRetries" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1610, version=0)
class Microsoft_Windows_WiFiNetworkManager_1610_0(Etw):
    pattern = Struct(
        "AllNetworks" / Int32ul,
        "ConnNetworks" / Int32ul,
        "dwGblFlags" / Int32ul,
        "dwMngFlags" / Int32ul,
        "dwUserFlags" / Int32ul,
        "dwWPSFlags" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1611, version=0)
class Microsoft_Windows_WiFiNetworkManager_1611_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1612, version=0)
class Microsoft_Windows_WiFiNetworkManager_1612_0(Etw):
    pattern = Struct(
        "dwIndex1" / Int32ul,
        "dwIndex2" / Int32ul,
        "szNetwork" / CString,
        "dwAuth" / Int32ul,
        "dwCipher" / Int32ul,
        "LinkQ" / Int32ul,
        "Score" / Float32l,
        "dwFlags" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1613, version=0)
class Microsoft_Windows_WiFiNetworkManager_1613_0(Etw):
    pattern = Struct(
        "dwIndex1" / Int32ul,
        "dwIndex2" / Int32ul,
        "szNetwork" / CString,
        "dwAuth" / Int32ul,
        "dwCipher" / Int32ul,
        "LinkQ" / Int32ul,
        "Score" / Float32l,
        "dwFlags" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1614, version=0)
class Microsoft_Windows_WiFiNetworkManager_1614_0(Etw):
    pattern = Struct(
        "dwIndex1" / Int32ul,
        "dwIndex2" / Int32ul,
        "szNetwork" / CString,
        "dwAuth" / Int32ul,
        "dwCipher" / Int32ul,
        "LinkQ" / Int32ul,
        "Score" / Float32l,
        "dwFlags" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1615, version=0)
class Microsoft_Windows_WiFiNetworkManager_1615_0(Etw):
    pattern = Struct(
        "dwIndex1" / Int32ul,
        "dwIndex2" / Int32ul,
        "szNetwork" / CString,
        "dwAuth" / Int32ul,
        "dwCipher" / Int32ul,
        "LinkQ" / Int32ul,
        "Score" / Float32l,
        "dwFlags" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1616, version=0)
class Microsoft_Windows_WiFiNetworkManager_1616_0(Etw):
    pattern = Struct(
        "dwIndex1" / Int32ul,
        "dwIndex2" / Int32ul,
        "szNetwork" / CString,
        "dwAuth" / Int32ul,
        "dwCipher" / Int32ul,
        "LinkQ" / Int32ul,
        "Score" / Float32l,
        "dwFlags" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1617, version=0)
class Microsoft_Windows_WiFiNetworkManager_1617_0(Etw):
    pattern = Struct(
        "szString" / CString
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1618, version=0)
class Microsoft_Windows_WiFiNetworkManager_1618_0(Etw):
    pattern = Struct(
        "dwIndex1" / Int32ul,
        "dwIndex2" / Int32ul,
        "szNetwork" / CString,
        "dwAuth" / Int32ul,
        "dwCipher" / Int32ul,
        "szType" / CString,
        "szState" / CString,
        "LinkQ" / Int32ul,
        "Score" / Float32l,
        "dwCfgWt" / Int32ul,
        "dwCalcWt" / Int32ul,
        "dwCfgFlags" / Int32ul,
        "dwProfFlags" / Int32ul,
        "dwCPLength" / Int32ul,
        "dwCredLength" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1620, version=0)
class Microsoft_Windows_WiFiNetworkManager_1620_0(Etw):
    pattern = Struct(
        "dwIndex" / Int32ul,
        "szNetwork" / CString,
        "wsConnection" / WString,
        "dwCfgWt" / Int32ul,
        "dwCalcWt" / Int32ul,
        "dwProfFlags" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1622, version=0)
class Microsoft_Windows_WiFiNetworkManager_1622_0(Etw):
    pattern = Struct(
        "szString1" / CString,
        "szString2" / CString,
        "wszString" / WString
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1624, version=0)
class Microsoft_Windows_WiFiNetworkManager_1624_0(Etw):
    pattern = Struct(
        "dwIndex" / Int32ul,
        "szNetwork" / CString,
        "wsConnection" / WString,
        "dwCfgWt" / Int32ul,
        "dwCalcWt" / Int32ul,
        "dwProfFlags" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1625, version=0)
class Microsoft_Windows_WiFiNetworkManager_1625_0(Etw):
    pattern = Struct(
        "dwIndex" / Int32ul,
        "szNetwork" / CString,
        "wsConnection" / WString,
        "dwCfgWt" / Int32ul,
        "dwCalcWt" / Int32ul,
        "dwProfFlags" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1626, version=0)
class Microsoft_Windows_WiFiNetworkManager_1626_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1627, version=0)
class Microsoft_Windows_WiFiNetworkManager_1627_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul,
        "szString" / WString
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1628, version=0)
class Microsoft_Windows_WiFiNetworkManager_1628_0(Etw):
    pattern = Struct(
        "wszStatus" / WString,
        "Ssid" / CString,
        "bUserNetwork" / Int8ul,
        "bACProfile" / Int8ul,
        "dwProfFlags" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1629, version=0)
class Microsoft_Windows_WiFiNetworkManager_1629_0(Etw):
    pattern = Struct(
        "szString1" / CString,
        "szString2" / WString
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1630, version=0)
class Microsoft_Windows_WiFiNetworkManager_1630_0(Etw):
    pattern = Struct(
        "szString" / CString,
        "dwValue1" / Int32ul,
        "dwValue2" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1631, version=0)
class Microsoft_Windows_WiFiNetworkManager_1631_0(Etw):
    pattern = Struct(
        "szNetwork" / CString,
        "szState" / CString,
        "dwRetries" / Int32ul,
        "dwBackoffMin" / Int32ul,
        "dwBackoffRng" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1632, version=0)
class Microsoft_Windows_WiFiNetworkManager_1632_0(Etw):
    pattern = Struct(
        "szString" / WString
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1633, version=0)
class Microsoft_Windows_WiFiNetworkManager_1633_0(Etw):
    pattern = Struct(
        "szString1" / CString,
        "szString2" / WString
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1634, version=0)
class Microsoft_Windows_WiFiNetworkManager_1634_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1635, version=0)
class Microsoft_Windows_WiFiNetworkManager_1635_0(Etw):
    pattern = Struct(
        "szString1" / CString,
        "szString2" / WString
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1636, version=0)
class Microsoft_Windows_WiFiNetworkManager_1636_0(Etw):
    pattern = Struct(
        "dwValue1" / Int32ul,
        "dwValue2" / Int32ul,
        "dwValue3" / Int32ul,
        "dwValue4" / Int32ul,
        "dwValue5" / Int32ul,
        "dwValue6" / Int32ul,
        "dwValue7" / Int32ul,
        "dwValue8" / Int32ul,
        "dwValue9" / Int32ul,
        "dwValue10" / Int32ul,
        "dwValue11" / Int32ul,
        "dwValue12" / Int32ul,
        "dwValue13" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1637, version=0)
class Microsoft_Windows_WiFiNetworkManager_1637_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1638, version=0)
class Microsoft_Windows_WiFiNetworkManager_1638_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1639, version=0)
class Microsoft_Windows_WiFiNetworkManager_1639_0(Etw):
    pattern = Struct(
        "dwValue1" / Int32ul,
        "dwValue2" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1641, version=0)
class Microsoft_Windows_WiFiNetworkManager_1641_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul,
        "szString" / WString
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1642, version=0)
class Microsoft_Windows_WiFiNetworkManager_1642_0(Etw):
    pattern = Struct(
        "dwValue1" / Int32ul,
        "dwValue2" / Int32ul,
        "dwValue3" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1643, version=0)
class Microsoft_Windows_WiFiNetworkManager_1643_0(Etw):
    pattern = Struct(
        "szString" / CString,
        "dwValue1" / Int32ul,
        "dwValue2" / Int32ul,
        "dwValue3" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1644, version=0)
class Microsoft_Windows_WiFiNetworkManager_1644_0(Etw):
    pattern = Struct(
        "dwIndex1" / Int32ul,
        "dwIndex2" / Int32ul,
        "szNetwork" / CString,
        "dwAuth" / Int32ul,
        "dwCipher" / Int32ul,
        "LinkQ" / Int32ul,
        "Score" / Float32l,
        "dwFlags" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1645, version=0)
class Microsoft_Windows_WiFiNetworkManager_1645_0(Etw):
    pattern = Struct(
        "dwIndex1" / Int32ul,
        "dwIndex2" / Int32ul,
        "szNetwork" / CString,
        "dwAuth" / Int32ul,
        "dwCipher" / Int32ul,
        "LinkQ" / Int32ul,
        "Score" / Float32l,
        "dwFlags" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1646, version=0)
class Microsoft_Windows_WiFiNetworkManager_1646_0(Etw):
    pattern = Struct(
        "dwIndex1" / Int32ul,
        "dwIndex2" / Int32ul,
        "szNetwork" / CString,
        "dwAuth" / Int32ul,
        "dwCipher" / Int32ul,
        "LinkQ" / Int32ul,
        "Score" / Float32l,
        "dwFlags" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1647, version=0)
class Microsoft_Windows_WiFiNetworkManager_1647_0(Etw):
    pattern = Struct(
        "dwIndex1" / Int32ul,
        "dwIndex2" / Int32ul,
        "szNetwork" / CString,
        "dwAuth" / Int32ul,
        "dwCipher" / Int32ul,
        "LinkQ" / Int32ul,
        "Score" / Float32l,
        "dwFlags" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1648, version=0)
class Microsoft_Windows_WiFiNetworkManager_1648_0(Etw):
    pattern = Struct(
        "dwIndex1" / Int32ul,
        "dwIndex2" / Int32ul,
        "szNetwork" / CString,
        "dwAuth" / Int32ul,
        "dwCipher" / Int32ul,
        "LinkQ" / Int32ul,
        "Score" / Float32l,
        "dwFlags" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1649, version=0)
class Microsoft_Windows_WiFiNetworkManager_1649_0(Etw):
    pattern = Struct(
        "szString" / CString,
        "dwValue1" / Int32ul,
        "dwValue2" / Int32ul,
        "dwValue3" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1650, version=0)
class Microsoft_Windows_WiFiNetworkManager_1650_0(Etw):
    pattern = Struct(
        "szString" / CString,
        "dwValue1" / Int32ul,
        "dwValue2" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1651, version=0)
class Microsoft_Windows_WiFiNetworkManager_1651_0(Etw):
    pattern = Struct(
        "szString" / CString,
        "dwValue1" / Int32ul,
        "dwValue2" / Int32ul,
        "dwValue3" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1652, version=0)
class Microsoft_Windows_WiFiNetworkManager_1652_0(Etw):
    pattern = Struct(
        "dwValue1" / Int32ul,
        "dwValue2" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1653, version=0)
class Microsoft_Windows_WiFiNetworkManager_1653_0(Etw):
    pattern = Struct(
        "szString" / CString,
        "dwValue1" / Int32ul,
        "dwValue2" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1654, version=0)
class Microsoft_Windows_WiFiNetworkManager_1654_0(Etw):
    pattern = Struct(
        "szString" / CString,
        "dwValue1" / Int32ul,
        "dwValue2" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1655, version=0)
class Microsoft_Windows_WiFiNetworkManager_1655_0(Etw):
    pattern = Struct(
        "dwIndex1" / Int32ul,
        "dwIndex2" / Int32ul,
        "szNetwork" / CString,
        "dwAuth" / Int32ul,
        "dwCipher" / Int32ul,
        "LinkQ" / Int32ul,
        "Score" / Float32l,
        "dwFlags" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1656, version=0)
class Microsoft_Windows_WiFiNetworkManager_1656_0(Etw):
    pattern = Struct(
        "dwValue1" / Int32ul,
        "dwValue2" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1657, version=0)
class Microsoft_Windows_WiFiNetworkManager_1657_0(Etw):
    pattern = Struct(
        "szString" / CString,
        "dwValue1" / Int32ul,
        "dwValue2" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1658, version=0)
class Microsoft_Windows_WiFiNetworkManager_1658_0(Etw):
    pattern = Struct(
        "Type" / Int32ul,
        "Context" / Int32ul,
        "szNetwork" / CString,
        "Score" / Float32l,
        "flightId" / Int64ul,
        "networkId" / Int64ul,
        "DataNeeded" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1659, version=0)
class Microsoft_Windows_WiFiNetworkManager_1659_0(Etw):
    pattern = Struct(
        "Context1" / Int32ul,
        "PCD" / Float32l,
        "Context2" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1660, version=0)
class Microsoft_Windows_WiFiNetworkManager_1660_0(Etw):
    pattern = Struct(
        "dwIndex1" / Int32ul,
        "dwIndex2" / Int32ul,
        "szNetwork" / CString,
        "dwAuth" / Int32ul,
        "dwCipher" / Int32ul,
        "LinkQ" / Int32ul,
        "Score" / Float32l,
        "dwFlags" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1661, version=0)
class Microsoft_Windows_WiFiNetworkManager_1661_0(Etw):
    pattern = Struct(
        "dwIndex1" / Int32ul,
        "dwIndex2" / Int32ul,
        "szNetwork" / CString,
        "dwAuth" / Int32ul,
        "dwCipher" / Int32ul,
        "LinkQ" / Int32ul,
        "Score" / Float32l,
        "dwFlags" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1662, version=0)
class Microsoft_Windows_WiFiNetworkManager_1662_0(Etw):
    pattern = Struct(
        "dwIndex1" / Int32ul,
        "dwIndex2" / Int32ul,
        "szNetwork" / CString,
        "dwAuth" / Int32ul,
        "dwCipher" / Int32ul,
        "LinkQ" / Int32ul,
        "Score" / Float32l,
        "dwFlags" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1663, version=0)
class Microsoft_Windows_WiFiNetworkManager_1663_0(Etw):
    pattern = Struct(
        "szString" / CString
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1664, version=0)
class Microsoft_Windows_WiFiNetworkManager_1664_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1666, version=0)
class Microsoft_Windows_WiFiNetworkManager_1666_0(Etw):
    pattern = Struct(
        "dwIndex1" / Int32ul,
        "dwIndex2" / Int32ul,
        "szReason" / CString,
        "szNetwork" / CString,
        "dwAuth" / Int32ul,
        "dwCipher" / Int32ul,
        "LinkQ" / Int32ul,
        "Score" / Float32l,
        "dwFlags" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1667, version=0)
class Microsoft_Windows_WiFiNetworkManager_1667_0(Etw):
    pattern = Struct(
        "szString" / CString,
        "dwValue1" / Int32ul,
        "dwValue2" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1668, version=0)
class Microsoft_Windows_WiFiNetworkManager_1668_0(Etw):
    pattern = Struct(
        "dwValue1" / Int32ul,
        "dwValue2" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1670, version=0)
class Microsoft_Windows_WiFiNetworkManager_1670_0(Etw):
    pattern = Struct(
        "szString" / CString,
        "dwValue1" / Int32ul,
        "dwValue2" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1671, version=0)
class Microsoft_Windows_WiFiNetworkManager_1671_0(Etw):
    pattern = Struct(
        "szString" / CString,
        "dwValue1" / Int32ul,
        "dwValue2" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1672, version=0)
class Microsoft_Windows_WiFiNetworkManager_1672_0(Etw):
    pattern = Struct(
        "szString" / CString,
        "dwValue1" / Int32ul,
        "dwValue2" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1673, version=0)
class Microsoft_Windows_WiFiNetworkManager_1673_0(Etw):
    pattern = Struct(
        "szString" / CString,
        "dwValue1" / Int32ul,
        "dwValue2" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1674, version=0)
class Microsoft_Windows_WiFiNetworkManager_1674_0(Etw):
    pattern = Struct(
        "szString" / CString,
        "dwValue1" / Int32ul,
        "dwValue2" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1675, version=0)
class Microsoft_Windows_WiFiNetworkManager_1675_0(Etw):
    pattern = Struct(
        "dwValue1" / Int32ul,
        "dwValue2" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1676, version=0)
class Microsoft_Windows_WiFiNetworkManager_1676_0(Etw):
    pattern = Struct(
        "szString" / CString,
        "dwValue1" / Int32ul,
        "dwValue2" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1677, version=0)
class Microsoft_Windows_WiFiNetworkManager_1677_0(Etw):
    pattern = Struct(
        "bQueryTM" / Int8ul,
        "bScmEnabled" / Int8ul,
        "bCredEnabled" / Int8ul,
        "bCPEnabled" / Int8ul,
        "dwTMFlags" / Int32ul,
        "bCloudEnabled" / Int8ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1700, version=0)
class Microsoft_Windows_WiFiNetworkManager_1700_0(Etw):
    pattern = Struct(
        "notif" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1701, version=0)
class Microsoft_Windows_WiFiNetworkManager_1701_0(Etw):
    pattern = Struct(
        "notif" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1702, version=0)
class Microsoft_Windows_WiFiNetworkManager_1702_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1703, version=0)
class Microsoft_Windows_WiFiNetworkManager_1703_0(Etw):
    pattern = Struct(
        "state" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1704, version=0)
class Microsoft_Windows_WiFiNetworkManager_1704_0(Etw):
    pattern = Struct(
        "level" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1705, version=0)
class Microsoft_Windows_WiFiNetworkManager_1705_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1706, version=0)
class Microsoft_Windows_WiFiNetworkManager_1706_0(Etw):
    pattern = Struct(
        "state" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1710, version=0)
class Microsoft_Windows_WiFiNetworkManager_1710_0(Etw):
    pattern = Struct(
        "state" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1713, version=0)
class Microsoft_Windows_WiFiNetworkManager_1713_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul,
        "szString" / WString
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1714, version=0)
class Microsoft_Windows_WiFiNetworkManager_1714_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1900, version=0)
class Microsoft_Windows_WiFiNetworkManager_1900_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=1901, version=0)
class Microsoft_Windows_WiFiNetworkManager_1901_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=2000, version=0)
class Microsoft_Windows_WiFiNetworkManager_2000_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=2001, version=0)
class Microsoft_Windows_WiFiNetworkManager_2001_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=2002, version=0)
class Microsoft_Windows_WiFiNetworkManager_2002_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=2004, version=0)
class Microsoft_Windows_WiFiNetworkManager_2004_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=2100, version=0)
class Microsoft_Windows_WiFiNetworkManager_2100_0(Etw):
    pattern = Struct(
        "dwValue1" / Int32ul,
        "dwValue2" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=2101, version=0)
class Microsoft_Windows_WiFiNetworkManager_2101_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=2106, version=0)
class Microsoft_Windows_WiFiNetworkManager_2106_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=2107, version=0)
class Microsoft_Windows_WiFiNetworkManager_2107_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=2111, version=0)
class Microsoft_Windows_WiFiNetworkManager_2111_0(Etw):
    pattern = Struct(
        "ssid" / WString,
        "bssid" / WString
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=2114, version=0)
class Microsoft_Windows_WiFiNetworkManager_2114_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=2115, version=0)
class Microsoft_Windows_WiFiNetworkManager_2115_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=2120, version=0)
class Microsoft_Windows_WiFiNetworkManager_2120_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=2200, version=0)
class Microsoft_Windows_WiFiNetworkManager_2200_0(Etw):
    pattern = Struct(
        "szConnName" / WString,
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=2202, version=0)
class Microsoft_Windows_WiFiNetworkManager_2202_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=2203, version=0)
class Microsoft_Windows_WiFiNetworkManager_2203_0(Etw):
    pattern = Struct(
        "szString" / WString
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=2204, version=0)
class Microsoft_Windows_WiFiNetworkManager_2204_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=2205, version=0)
class Microsoft_Windows_WiFiNetworkManager_2205_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=2207, version=0)
class Microsoft_Windows_WiFiNetworkManager_2207_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=2208, version=0)
class Microsoft_Windows_WiFiNetworkManager_2208_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=2209, version=0)
class Microsoft_Windows_WiFiNetworkManager_2209_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul,
        "szString" / WString
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=2301, version=0)
class Microsoft_Windows_WiFiNetworkManager_2301_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=2304, version=0)
class Microsoft_Windows_WiFiNetworkManager_2304_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=2305, version=0)
class Microsoft_Windows_WiFiNetworkManager_2305_0(Etw):
    pattern = Struct(
        "szConnName" / WString
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=2307, version=0)
class Microsoft_Windows_WiFiNetworkManager_2307_0(Etw):
    pattern = Struct(
        "dwValue1" / Int32ul,
        "dwValue2" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=2309, version=0)
class Microsoft_Windows_WiFiNetworkManager_2309_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=2311, version=0)
class Microsoft_Windows_WiFiNetworkManager_2311_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=2312, version=0)
class Microsoft_Windows_WiFiNetworkManager_2312_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=2314, version=0)
class Microsoft_Windows_WiFiNetworkManager_2314_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=2402, version=0)
class Microsoft_Windows_WiFiNetworkManager_2402_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=2403, version=0)
class Microsoft_Windows_WiFiNetworkManager_2403_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=2404, version=0)
class Microsoft_Windows_WiFiNetworkManager_2404_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=2405, version=0)
class Microsoft_Windows_WiFiNetworkManager_2405_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=2406, version=0)
class Microsoft_Windows_WiFiNetworkManager_2406_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=2407, version=0)
class Microsoft_Windows_WiFiNetworkManager_2407_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=2408, version=0)
class Microsoft_Windows_WiFiNetworkManager_2408_0(Etw):
    pattern = Struct(
        "dwValue1" / Int32ul,
        "dwValue2" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=2409, version=0)
class Microsoft_Windows_WiFiNetworkManager_2409_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )


@declare(guid=guid("e5c16d49-2464-4382-bb20-97a4b5465db9"), event_id=2410, version=0)
class Microsoft_Windows_WiFiNetworkManager_2410_0(Etw):
    pattern = Struct(
        "dwValue" / Int32ul
    )

