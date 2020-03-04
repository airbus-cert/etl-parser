# -*- coding: utf-8 -*-
"""
Microsoft-Windows-DeviceManagement-Pushrouter
GUID : f1201b5a-e170-42b6-8d20-b57ac57e6416
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=100, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_100_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=101, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_101_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=102, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_102_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=103, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_103_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=104, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_104_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=105, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_105_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=106, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_106_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=107, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_107_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=108, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_108_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=109, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_109_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=110, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_110_0(Etw):
    pattern = Struct(
        "HexInt1" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=111, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_111_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=112, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_112_0(Etw):
    pattern = Struct(
        "HexInt1" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=113, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_113_0(Etw):
    pattern = Struct(
        "HexInt1" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=116, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_116_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=117, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_117_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=118, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_118_0(Etw):
    pattern = Struct(
        "HexInt1" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=119, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_119_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=120, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_120_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=121, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_121_0(Etw):
    pattern = Struct(
        "HexInt1" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=122, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_122_0(Etw):
    pattern = Struct(
        "HexInt1" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=123, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_123_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=124, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_124_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=125, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_125_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=126, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_126_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=127, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_127_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=128, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_128_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=129, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_129_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=130, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_130_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=132, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_132_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString,
        "Message4" / WString,
        "Message5" / WString,
        "HexInt1" / Int32ul,
        "HexInt3" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=133, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_133_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString,
        "Message4" / WString,
        "HexInt1" / Int32ul,
        "HexInt3" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=135, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_135_0(Etw):
    pattern = Struct(
        "Message1" / WString
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=136, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_136_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=137, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_137_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=138, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_138_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HexInt1" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=139, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_139_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "HexInt3" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=140, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_140_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "HexInt3" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=141, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_141_0(Etw):
    pattern = Struct(
        "Message1" / WString
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=142, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_142_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=143, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_143_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=144, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_144_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=146, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_146_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString,
        "Message4" / WString,
        "Message5" / WString,
        "HexInt1" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=147, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_147_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString,
        "Message4" / WString,
        "Message5" / WString,
        "HexInt1" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=149, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_149_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=150, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_150_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=151, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_151_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=152, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_152_0(Etw):
    pattern = Struct(
        "Message1" / WString
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=153, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_153_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=154, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_154_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=155, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_155_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString,
        "Message4" / WString,
        "HexInt1" / Int32ul,
        "HexInt3" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=156, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_156_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=157, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_157_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=158, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_158_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=159, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_159_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=160, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_160_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=162, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_162_0(Etw):
    pattern = Struct(
        "HexInt1" / Int32ul,
        "HexInt2" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=163, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_163_0(Etw):
    pattern = Struct(
        "HexInt1" / Int32ul,
        "HexInt2" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=164, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_164_0(Etw):
    pattern = Struct(
        "HexInt1" / Int32ul,
        "HexInt2" / Int32ul,
        "HexInt3" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=165, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_165_0(Etw):
    pattern = Struct(
        "HexInt1" / Int32ul,
        "HexInt2" / Int32ul,
        "HexInt3" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=166, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_166_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HexInt1" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=167, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_167_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HexInt1" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=168, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_168_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=169, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_169_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=170, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_170_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=171, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_171_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=172, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_172_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=173, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_173_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=176, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_176_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=177, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_177_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=300, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_300_0(Etw):
    pattern = Struct(
        "HexInt1" / Int32ul,
        "HexInt2" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=301, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_301_0(Etw):
    pattern = Struct(
        "HexInt1" / Int32ul,
        "HexInt2" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=500, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_500_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=501, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_501_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=502, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_502_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=503, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_503_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=504, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_504_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=505, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_505_0(Etw):
    pattern = Struct(
        "HexInt1" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=506, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_506_0(Etw):
    pattern = Struct(
        "HexInt1" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=507, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_507_0(Etw):
    pattern = Struct(
        "HexInt1" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=511, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_511_0(Etw):
    pattern = Struct(
        "HexInt1" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=512, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_512_0(Etw):
    pattern = Struct(
        "HexInt1" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=514, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_514_0(Etw):
    pattern = Struct(
        "HexInt1" / Int32ul,
        "HexInt2" / Int32ul,
        "HexInt3" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=515, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_515_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=516, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_516_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=517, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_517_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=518, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_518_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=519, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_519_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=520, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_520_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=521, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_521_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=522, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_522_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=523, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_523_0(Etw):
    pattern = Struct(
        "HexInt1" / Int32ul,
        "HexInt2" / Int32ul
    )


@declare(guid=guid("f1201b5a-e170-42b6-8d20-b57ac57e6416"), event_id=525, version=0)
class Microsoft_Windows_DeviceManagement_Pushrouter_525_0(Etw):
    pattern = Struct(
        "HexInt1" / Int32ul,
        "HRESULT" / Int32ul
    )

