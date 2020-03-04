# -*- coding: utf-8 -*-
"""
Microsoft-Windows-EnhancedStorage-EhStorTcgDrv
GUID : aa3aa23b-bb6d-425a-b58c-1d7e37f5d02a
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("aa3aa23b-bb6d-425a-b58c-1d7e37f5d02a"), event_id=1, version=0)
class Microsoft_Windows_EnhancedStorage_EhStorTcgDrv_1_0(Etw):
    pattern = Struct(
        "Context" / CString,
        "hr" / Int32sl,
        "ErrorParam1" / Int32ul,
        "ErrorParam2" / Int32ul,
        "ErrorParam3" / Int32ul,
        "ErrorParam4" / Int32ul
    )


@declare(guid=guid("aa3aa23b-bb6d-425a-b58c-1d7e37f5d02a"), event_id=2, version=0)
class Microsoft_Windows_EnhancedStorage_EhStorTcgDrv_2_0(Etw):
    pattern = Struct(
        "Context" / CString,
        "Win32Err" / Int32ul,
        "ErrorParam1" / Int32ul,
        "ErrorParam2" / Int32ul,
        "ErrorParam3" / Int32ul,
        "ErrorParam4" / Int32ul
    )


@declare(guid=guid("aa3aa23b-bb6d-425a-b58c-1d7e37f5d02a"), event_id=3, version=0)
class Microsoft_Windows_EnhancedStorage_EhStorTcgDrv_3_0(Etw):
    pattern = Struct(
        "Context" / CString,
        "NTStatus" / Int32ul,
        "ErrorParam1" / Int32ul,
        "ErrorParam2" / Int32ul,
        "ErrorParam3" / Int32ul,
        "ErrorParam4" / Int32ul
    )


@declare(guid=guid("aa3aa23b-bb6d-425a-b58c-1d7e37f5d02a"), event_id=4, version=0)
class Microsoft_Windows_EnhancedStorage_EhStorTcgDrv_4_0(Etw):
    pattern = Struct(
        "ObjectName" / CString,
        "ObjectSize" / Int32ul
    )


@declare(guid=guid("aa3aa23b-bb6d-425a-b58c-1d7e37f5d02a"), event_id=5, version=0)
class Microsoft_Windows_EnhancedStorage_EhStorTcgDrv_5_0(Etw):
    pattern = Struct(
        "Context" / CString,
        "ExpectedSize" / Int32ul,
        "ActualSize" / Int32ul
    )


@declare(guid=guid("aa3aa23b-bb6d-425a-b58c-1d7e37f5d02a"), event_id=6, version=0)
class Microsoft_Windows_EnhancedStorage_EhStorTcgDrv_6_0(Etw):
    pattern = Struct(
        "Name" / CString,
        "Value" / Int32ul
    )


@declare(guid=guid("aa3aa23b-bb6d-425a-b58c-1d7e37f5d02a"), event_id=7, version=0)
class Microsoft_Windows_EnhancedStorage_EhStorTcgDrv_7_0(Etw):
    pattern = Struct(
        "Name" / CString,
        "Value" / Int32ul
    )


@declare(guid=guid("aa3aa23b-bb6d-425a-b58c-1d7e37f5d02a"), event_id=8, version=0)
class Microsoft_Windows_EnhancedStorage_EhStorTcgDrv_8_0(Etw):
    pattern = Struct(
        "Name" / CString,
        "String" / CString
    )


@declare(guid=guid("aa3aa23b-bb6d-425a-b58c-1d7e37f5d02a"), event_id=9, version=0)
class Microsoft_Windows_EnhancedStorage_EhStorTcgDrv_9_0(Etw):
    pattern = Struct(
        "Name" / CString,
        "String" / CString
    )


@declare(guid=guid("aa3aa23b-bb6d-425a-b58c-1d7e37f5d02a"), event_id=10, version=0)
class Microsoft_Windows_EnhancedStorage_EhStorTcgDrv_10_0(Etw):
    pattern = Struct(
        "Description" / CString,
        "Param1" / Int64ul,
        "Param2" / Int64ul,
        "Param3" / Int64ul,
        "Param4" / Int64ul,
        "CmdStatus" / Int32ul
    )


@declare(guid=guid("aa3aa23b-bb6d-425a-b58c-1d7e37f5d02a"), event_id=11, version=0)
class Microsoft_Windows_EnhancedStorage_EhStorTcgDrv_11_0(Etw):
    pattern = Struct(
        "Description" / CString,
        "SiloCommand" / Int32ul,
        "SiloStatus" / Int32ul,
        "TCGInvokingID" / Int64ul,
        "TCGMethodID" / Int64ul
    )


@declare(guid=guid("aa3aa23b-bb6d-425a-b58c-1d7e37f5d02a"), event_id=12, version=0)
class Microsoft_Windows_EnhancedStorage_EhStorTcgDrv_12_0(Etw):
    pattern = Struct(
        "Capabilities" / Int32ul,
        "KeyProtectionMechanism" / Int64ul,
        "MaxBandCount" / Int32ul,
        "BandMetadataSize" / Int32ul
    )


@declare(guid=guid("aa3aa23b-bb6d-425a-b58c-1d7e37f5d02a"), event_id=13, version=0)
class Microsoft_Windows_EnhancedStorage_EhStorTcgDrv_13_0(Etw):
    pattern = Struct(
        "BandID" / Int32ul,
        "Authorize" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("aa3aa23b-bb6d-425a-b58c-1d7e37f5d02a"), event_id=100, version=0)
class Microsoft_Windows_EnhancedStorage_EhStorTcgDrv_100_0(Etw):
    pattern = Struct(
        "Context" / CString,
        "Param1" / Int32ul,
        "Param2" / Int32ul,
        "Param3" / Int32ul,
        "Param4" / Int32ul
    )


@declare(guid=guid("aa3aa23b-bb6d-425a-b58c-1d7e37f5d02a"), event_id=101, version=0)
class Microsoft_Windows_EnhancedStorage_EhStorTcgDrv_101_0(Etw):
    pattern = Struct(
        "Context" / CString,
        "Param1" / Int32ul,
        "Param2" / Int32ul,
        "Param3" / Int32ul,
        "Param4" / Int32ul
    )


@declare(guid=guid("aa3aa23b-bb6d-425a-b58c-1d7e37f5d02a"), event_id=102, version=0)
class Microsoft_Windows_EnhancedStorage_EhStorTcgDrv_102_0(Etw):
    pattern = Struct(
        "Context" / CString,
        "Param1" / Int32ul,
        "Param2" / Int32ul,
        "Param3" / Int32ul,
        "Param4" / Int32ul
    )


@declare(guid=guid("aa3aa23b-bb6d-425a-b58c-1d7e37f5d02a"), event_id=200, version=0)
class Microsoft_Windows_EnhancedStorage_EhStorTcgDrv_200_0(Etw):
    pattern = Struct(
        "Context" / CString,
        "Param1" / Int64ul,
        "Param2" / Int64ul,
        "Param3" / Int64ul,
        "Param4" / Int64ul
    )


@declare(guid=guid("aa3aa23b-bb6d-425a-b58c-1d7e37f5d02a"), event_id=201, version=0)
class Microsoft_Windows_EnhancedStorage_EhStorTcgDrv_201_0(Etw):
    pattern = Struct(
        "Context" / CString,
        "Param1" / Int64ul,
        "Param2" / Int64ul,
        "Param3" / Int64ul,
        "Param4" / Int64ul
    )


@declare(guid=guid("aa3aa23b-bb6d-425a-b58c-1d7e37f5d02a"), event_id=202, version=0)
class Microsoft_Windows_EnhancedStorage_EhStorTcgDrv_202_0(Etw):
    pattern = Struct(
        "Context" / CString,
        "SiloCmd" / Int64ul,
        "TcgCmd" / CString,
        "Status" / Int64ul,
        "Param1" / Int64ul,
        "Param2" / Int64ul,
        "Param3" / Int64ul,
        "Param4" / Int64ul
    )


@declare(guid=guid("aa3aa23b-bb6d-425a-b58c-1d7e37f5d02a"), event_id=203, version=0)
class Microsoft_Windows_EnhancedStorage_EhStorTcgDrv_203_0(Etw):
    pattern = Struct(
        "Context" / CString,
        "SiloCmd" / Int64ul,
        "TcgCmd" / CString,
        "Status" / Int64ul,
        "Param1" / Int64ul,
        "Param2" / Int64ul,
        "Param3" / Int64ul,
        "Param4" / Int64ul
    )


@declare(guid=guid("aa3aa23b-bb6d-425a-b58c-1d7e37f5d02a"), event_id=204, version=0)
class Microsoft_Windows_EnhancedStorage_EhStorTcgDrv_204_0(Etw):
    pattern = Struct(
        "Context" / CString,
        "Param1" / Int64ul,
        "Param2" / Int64ul,
        "Param3" / Int64ul,
        "Param4" / Int64ul
    )


@declare(guid=guid("aa3aa23b-bb6d-425a-b58c-1d7e37f5d02a"), event_id=205, version=0)
class Microsoft_Windows_EnhancedStorage_EhStorTcgDrv_205_0(Etw):
    pattern = Struct(
        "Context" / CString,
        "Param1" / Int64ul,
        "Param2" / Int64ul,
        "Param3" / Int64ul,
        "Param4" / Int64ul
    )


@declare(guid=guid("aa3aa23b-bb6d-425a-b58c-1d7e37f5d02a"), event_id=206, version=0)
class Microsoft_Windows_EnhancedStorage_EhStorTcgDrv_206_0(Etw):
    pattern = Struct(
        "Context" / CString,
        "Param1" / Int64ul,
        "Param2" / Int64ul,
        "Param3" / Int64ul,
        "Param4" / Int64ul
    )


@declare(guid=guid("aa3aa23b-bb6d-425a-b58c-1d7e37f5d02a"), event_id=207, version=0)
class Microsoft_Windows_EnhancedStorage_EhStorTcgDrv_207_0(Etw):
    pattern = Struct(
        "Context" / CString,
        "Param1" / Int64ul,
        "Param2" / Int64ul,
        "Param3" / Int64ul,
        "Param4" / Int64ul
    )


@declare(guid=guid("aa3aa23b-bb6d-425a-b58c-1d7e37f5d02a"), event_id=208, version=0)
class Microsoft_Windows_EnhancedStorage_EhStorTcgDrv_208_0(Etw):
    pattern = Struct(
        "Context" / CString,
        "Param1" / Int64ul,
        "Param2" / Int64ul,
        "Param3" / Int64ul,
        "Param4" / Int64ul
    )


@declare(guid=guid("aa3aa23b-bb6d-425a-b58c-1d7e37f5d02a"), event_id=209, version=0)
class Microsoft_Windows_EnhancedStorage_EhStorTcgDrv_209_0(Etw):
    pattern = Struct(
        "Context" / CString,
        "Param1" / Int64ul,
        "Param2" / Int64ul,
        "Param3" / Int64ul,
        "Param4" / Int64ul
    )


@declare(guid=guid("aa3aa23b-bb6d-425a-b58c-1d7e37f5d02a"), event_id=210, version=0)
class Microsoft_Windows_EnhancedStorage_EhStorTcgDrv_210_0(Etw):
    pattern = Struct(
        "Context" / CString,
        "Param1" / Int64ul,
        "Param2" / Int64ul,
        "Param3" / Int64ul,
        "Param4" / Int64ul
    )


@declare(guid=guid("aa3aa23b-bb6d-425a-b58c-1d7e37f5d02a"), event_id=211, version=0)
class Microsoft_Windows_EnhancedStorage_EhStorTcgDrv_211_0(Etw):
    pattern = Struct(
        "Context" / CString,
        "Param1" / Int64ul,
        "Param2" / Int64ul,
        "Param3" / Int64ul,
        "Param4" / Int64ul
    )


@declare(guid=guid("aa3aa23b-bb6d-425a-b58c-1d7e37f5d02a"), event_id=212, version=0)
class Microsoft_Windows_EnhancedStorage_EhStorTcgDrv_212_0(Etw):
    pattern = Struct(
        "Context" / CString,
        "Param1" / Int64ul,
        "Param2" / Int64ul,
        "Param3" / Int64ul,
        "Param4" / Int64ul
    )


@declare(guid=guid("aa3aa23b-bb6d-425a-b58c-1d7e37f5d02a"), event_id=213, version=0)
class Microsoft_Windows_EnhancedStorage_EhStorTcgDrv_213_0(Etw):
    pattern = Struct(
        "Context" / CString,
        "Param1" / Int64ul,
        "Param2" / Int64ul,
        "Param3" / Int64ul,
        "Param4" / Int64ul
    )


@declare(guid=guid("aa3aa23b-bb6d-425a-b58c-1d7e37f5d02a"), event_id=214, version=0)
class Microsoft_Windows_EnhancedStorage_EhStorTcgDrv_214_0(Etw):
    pattern = Struct(
        "Context" / CString,
        "Param1" / Int64ul,
        "Param2" / Int64ul,
        "Param3" / Int64ul,
        "Param4" / Int64ul
    )


@declare(guid=guid("aa3aa23b-bb6d-425a-b58c-1d7e37f5d02a"), event_id=215, version=0)
class Microsoft_Windows_EnhancedStorage_EhStorTcgDrv_215_0(Etw):
    pattern = Struct(
        "Context" / CString,
        "Param1" / Int64ul,
        "Param2" / Int64ul,
        "Param3" / Int64ul,
        "Param4" / Int64ul
    )


@declare(guid=guid("aa3aa23b-bb6d-425a-b58c-1d7e37f5d02a"), event_id=216, version=0)
class Microsoft_Windows_EnhancedStorage_EhStorTcgDrv_216_0(Etw):
    pattern = Struct(
        "Context" / CString,
        "Param1" / Int64ul,
        "Param2" / Int64ul,
        "Param3" / Int64ul,
        "Param4" / Int64ul
    )


@declare(guid=guid("aa3aa23b-bb6d-425a-b58c-1d7e37f5d02a"), event_id=217, version=0)
class Microsoft_Windows_EnhancedStorage_EhStorTcgDrv_217_0(Etw):
    pattern = Struct(
        "Context" / CString,
        "Param1" / Int64ul,
        "Param2" / Int64ul,
        "Param3" / Int64ul,
        "Param4" / Int64ul
    )


@declare(guid=guid("aa3aa23b-bb6d-425a-b58c-1d7e37f5d02a"), event_id=218, version=0)
class Microsoft_Windows_EnhancedStorage_EhStorTcgDrv_218_0(Etw):
    pattern = Struct(
        "Context" / CString,
        "Param1" / Int64ul,
        "Param2" / Int64ul,
        "Param3" / Int64ul,
        "Param4" / Int64ul
    )


@declare(guid=guid("aa3aa23b-bb6d-425a-b58c-1d7e37f5d02a"), event_id=219, version=0)
class Microsoft_Windows_EnhancedStorage_EhStorTcgDrv_219_0(Etw):
    pattern = Struct(
        "Context" / CString,
        "Param1" / Int64ul,
        "Param2" / Int64ul,
        "Param3" / Int64ul,
        "Param4" / Int64ul
    )


@declare(guid=guid("aa3aa23b-bb6d-425a-b58c-1d7e37f5d02a"), event_id=220, version=0)
class Microsoft_Windows_EnhancedStorage_EhStorTcgDrv_220_0(Etw):
    pattern = Struct(
        "Context" / CString,
        "Param1" / Int64ul,
        "Param2" / Int64ul,
        "Param3" / Int64ul,
        "Param4" / Int64ul
    )


@declare(guid=guid("aa3aa23b-bb6d-425a-b58c-1d7e37f5d02a"), event_id=221, version=0)
class Microsoft_Windows_EnhancedStorage_EhStorTcgDrv_221_0(Etw):
    pattern = Struct(
        "Context" / CString,
        "Param1" / Int64ul,
        "Param2" / Int64ul,
        "Param3" / Int64ul,
        "Param4" / Int64ul
    )


@declare(guid=guid("aa3aa23b-bb6d-425a-b58c-1d7e37f5d02a"), event_id=222, version=0)
class Microsoft_Windows_EnhancedStorage_EhStorTcgDrv_222_0(Etw):
    pattern = Struct(
        "Context" / CString,
        "Param1" / Int64ul,
        "Param2" / Int64ul,
        "Param3" / Int64ul,
        "Param4" / Int64ul
    )


@declare(guid=guid("aa3aa23b-bb6d-425a-b58c-1d7e37f5d02a"), event_id=223, version=0)
class Microsoft_Windows_EnhancedStorage_EhStorTcgDrv_223_0(Etw):
    pattern = Struct(
        "Context" / CString,
        "Param1" / Int64ul,
        "Param2" / Int64ul,
        "Param3" / Int64ul,
        "Param4" / Int64ul
    )


@declare(guid=guid("aa3aa23b-bb6d-425a-b58c-1d7e37f5d02a"), event_id=224, version=0)
class Microsoft_Windows_EnhancedStorage_EhStorTcgDrv_224_0(Etw):
    pattern = Struct(
        "Context" / CString,
        "Param1" / Int64ul,
        "Param2" / Int64ul,
        "Param3" / Int64ul,
        "Param4" / Int64ul
    )


@declare(guid=guid("aa3aa23b-bb6d-425a-b58c-1d7e37f5d02a"), event_id=225, version=0)
class Microsoft_Windows_EnhancedStorage_EhStorTcgDrv_225_0(Etw):
    pattern = Struct(
        "Context" / CString,
        "Param1" / Int64ul,
        "Param2" / Int64ul,
        "Param3" / Int64ul,
        "Param4" / Int64ul
    )


@declare(guid=guid("aa3aa23b-bb6d-425a-b58c-1d7e37f5d02a"), event_id=226, version=0)
class Microsoft_Windows_EnhancedStorage_EhStorTcgDrv_226_0(Etw):
    pattern = Struct(
        "Context" / CString,
        "Param1" / Int64ul,
        "Param2" / Int64ul,
        "Param3" / Int64ul,
        "Param4" / Int64ul
    )


@declare(guid=guid("aa3aa23b-bb6d-425a-b58c-1d7e37f5d02a"), event_id=227, version=0)
class Microsoft_Windows_EnhancedStorage_EhStorTcgDrv_227_0(Etw):
    pattern = Struct(
        "Context" / CString,
        "Param1" / Int64ul,
        "Param2" / Int64ul,
        "Param3" / Int64ul,
        "Param4" / Int64ul
    )


@declare(guid=guid("aa3aa23b-bb6d-425a-b58c-1d7e37f5d02a"), event_id=228, version=0)
class Microsoft_Windows_EnhancedStorage_EhStorTcgDrv_228_0(Etw):
    pattern = Struct(
        "Context" / CString,
        "Param1" / Int64ul,
        "Param2" / Int64ul,
        "Param3" / Int64ul,
        "Param4" / Int64ul
    )


@declare(guid=guid("aa3aa23b-bb6d-425a-b58c-1d7e37f5d02a"), event_id=229, version=0)
class Microsoft_Windows_EnhancedStorage_EhStorTcgDrv_229_0(Etw):
    pattern = Struct(
        "Context" / CString,
        "Param1" / Int64ul,
        "Param2" / Int64ul,
        "Param3" / Int64ul,
        "Param4" / Int64ul
    )

