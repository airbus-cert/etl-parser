# -*- coding: utf-8 -*-
"""
Microsoft-Windows-WER-Diag
GUID : ad8aa069-a01b-40a0-ba40-948d1d8dedc5
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("ad8aa069-a01b-40a0-ba40-948d1d8dedc5"), event_id=1, version=0)
class Microsoft_Windows_WER_Diag_1_0(Etw):
    pattern = Struct(
        "CorruptedFilePath" / WString,
        "CrashedAppName" / WString,
        "ExceptionCode" / Int32ul,
        "ExceptionStatusCode" / Int32ul
    )


@declare(guid=guid("ad8aa069-a01b-40a0-ba40-948d1d8dedc5"), event_id=2, version=0)
class Microsoft_Windows_WER_Diag_2_0(Etw):
    pattern = Struct(
        "ExceptionCode" / Int32ul
    )


@declare(guid=guid("ad8aa069-a01b-40a0-ba40-948d1d8dedc5"), event_id=3, version=0)
class Microsoft_Windows_WER_Diag_3_0(Etw):
    pattern = Struct(
        "ProcessId" / Int32ul,
        "ModuleNameLength" / Int32ul,
        "ModuleName" / Bytes(lambda this: this.ModuleNameLength)
    )


@declare(guid=guid("ad8aa069-a01b-40a0-ba40-948d1d8dedc5"), event_id=4, version=0)
class Microsoft_Windows_WER_Diag_4_0(Etw):
    pattern = Struct(
        "ProcessId" / Int32ul,
        "ModuleName" / WString,
        "StartTime" / Int64ul,
        "CrashTimeFromStart" / Int64ul
    )


@declare(guid=guid("ad8aa069-a01b-40a0-ba40-948d1d8dedc5"), event_id=5, version=0)
class Microsoft_Windows_WER_Diag_5_0(Etw):
    pattern = Struct(
        "AppPath" / WString,
        "ProcessId" / Int32ul,
        "ProcessStartTime" / Int64ul,
        "Is64Bit" / Int8ul,
        "CallReturnAddress" / Int64ul,
        "CallReturnModName" / WString,
        "CallReturnModOffset" / Int32ul,
        "CallReturnInstructionBytesLength" / Int32ul,
        "CallReturnInstructionBytes" / Bytes(lambda this: this.CallReturnInstructionBytesLength),
        "CallReturnBaseAddress" / Int64ul,
        "CallReturnRegionSize" / Int64ul,
        "CallReturnState" / Int32ul,
        "CallReturnProtect" / Int32ul,
        "CallReturnType" / Int32ul,
        "TargetAddress" / Int64ul,
        "TargetModName" / WString,
        "TargetModOffset" / Int32ul,
        "TargetInstructionBytesLength" / Int32ul,
        "TargetInstructionBytes" / Bytes(lambda this: this.TargetInstructionBytesLength),
        "TargetBaseAddress" / Int64ul,
        "TargetRegionSize" / Int64ul,
        "TargetState" / Int32ul,
        "TargetProtect" / Int32ul,
        "TargetType" / Int32ul
    )

