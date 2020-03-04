# -*- coding: utf-8 -*-
"""
Microsoft-Windows-ModernDeployment-Diagnostics-Provider
GUID : bab3ad92-fb96-5902-450b-b8421bdec7bd
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=100, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_100_0(Etw):
    pattern = Struct(
        "Message1" / WString
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=101, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_101_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Int1" / Int32sl
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=102, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_102_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul,
        "Message1" / WString
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=103, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_103_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=104, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_104_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul,
        "Message1" / WString
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=106, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_106_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=107, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_107_0(Etw):
    pattern = Struct(
        "Message1" / WString
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=108, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_108_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=109, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_109_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=110, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_110_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul,
        "Message1" / WString
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=112, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_112_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=113, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_113_0(Etw):
    pattern = Struct(
        "Int1" / Int32sl
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=115, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_115_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=117, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_117_0(Etw):
    pattern = Struct(
        "UInt1" / Int32ul
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=153, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_153_0(Etw):
    pattern = Struct(
        "InitialState" / Int32ul,
        "UpdateState" / Int32ul
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=154, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_154_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=155, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_155_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=157, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_157_0(Etw):
    pattern = Struct(
        "UInt1" / Int64ul
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=158, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_158_0(Etw):
    pattern = Struct(
        "UInt1" / Int32ul
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=171, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_171_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=172, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_172_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=173, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_173_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=174, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_174_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=175, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_175_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=176, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_176_0(Etw):
    pattern = Struct(
        "ServerState" / Int32ul,
        "ClientState" / Int32ul
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=177, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_177_0(Etw):
    pattern = Struct(
        "Uint1" / Int32ul,
        "Uint2" / Int32ul
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=178, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_178_0(Etw):
    pattern = Struct(
        "Int1" / Int32sl
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=179, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_179_0(Etw):
    pattern = Struct(
        "State" / Int32ul
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=180, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_180_0(Etw):
    pattern = Struct(
        "State" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=181, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_181_0(Etw):
    pattern = Struct(
        "State" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=182, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_182_0(Etw):
    pattern = Struct(
        "UInt1" / Int32ul
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=184, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_184_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=185, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_185_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=192, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_192_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul,
        "WaitMs" / Int32sl,
        "AttemptNumber" / Int32sl,
        "MaxAttempts" / Int32sl
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=193, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_193_0(Etw):
    pattern = Struct(
        "Uint1" / Int32ul,
        "Uint2" / Int32ul
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=194, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_194_0(Etw):
    pattern = Struct(
        "UInt1" / Int32ul
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=196, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_196_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=197, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_197_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=200, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_200_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=202, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_202_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=203, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_203_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=206, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_206_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=207, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_207_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=251, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_251_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul,
        "UInt1" / Int64ul,
        "Int1" / Int32sl
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=300, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_300_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=301, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_301_0(Etw):
    pattern = Struct(
        "State" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=302, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_302_0(Etw):
    pattern = Struct(
        "State" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=303, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_303_0(Etw):
    pattern = Struct(
        "State" / Int32ul
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=310, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_310_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=311, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_311_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=312, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_312_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=313, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_313_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul,
        "Message1" / WString
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=315, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_315_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=500, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_500_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul,
        "Message1" / WString
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=501, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_501_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul,
        "Message1" / WString,
        "Message2" / WString
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=502, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_502_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul,
        "Message1" / WString,
        "Message2" / WString
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=503, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_503_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul,
        "Message1" / WString,
        "Message2" / WString
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=504, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_504_0(Etw):
    pattern = Struct(
        "Message1" / WString
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=505, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_505_0(Etw):
    pattern = Struct(
        "Message1" / WString
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=506, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_506_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul,
        "Message1" / WString
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=509, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_509_0(Etw):
    pattern = Struct(
        "UInt1" / Int32ul
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=700, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_700_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul,
        "Message1" / WString
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=702, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_702_0(Etw):
    pattern = Struct(
        "Message1" / WString
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=703, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_703_0(Etw):
    pattern = Struct(
        "Message1" / WString
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=704, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_704_0(Etw):
    pattern = Struct(
        "Message1" / WString
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=705, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_705_0(Etw):
    pattern = Struct(
        "Message1" / WString
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=706, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_706_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul,
        "Message1" / WString,
        "Message2" / WString
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=707, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_707_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul,
        "Message1" / WString,
        "Message2" / WString
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=708, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_708_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul,
        "Message1" / WString
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=709, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_709_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul,
        "Message1" / WString
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=710, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_710_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul,
        "Message1" / WString
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=711, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_711_0(Etw):
    pattern = Struct(
        "Message1" / WString
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=712, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_712_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul,
        "Message1" / WString
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=1002, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_1002_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=1005, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_1005_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul,
        "File" / CString,
        "Line" / Int32sl,
        "Message" / WString
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=1006, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_1006_0(Etw):
    pattern = Struct(
        "Message1" / WString
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=1008, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_1008_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=1100, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_1100_0(Etw):
    pattern = Struct(
        "Message1" / WString
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=1101, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_1101_0(Etw):
    pattern = Struct(
        "Message1" / WString
    )


@declare(guid=guid("bab3ad92-fb96-5902-450b-b8421bdec7bd"), event_id=1102, version=0)
class Microsoft_Windows_ModernDeployment_Diagnostics_Provider_1102_0(Etw):
    pattern = Struct(
        "Message1" / WString
    )

