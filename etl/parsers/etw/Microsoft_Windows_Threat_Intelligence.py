# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Threat-Intelligence
GUID : f4e1897c-bb5d-5668-f1d8-040f4d8dd344
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("f4e1897c-bb5d-5668-f1d8-040f4d8dd344"), event_id=1, version=0)
class Microsoft_Windows_Threat_Intelligence_1_0(Etw):
    pattern = Struct(
        "CallingProcessId" / Int32ul,
        "CallingProcessCreateTime" / Int64ul,
        "CallingProcessStartKey" / Int64ul,
        "CallingProcessSignatureLevel" / Int8ul,
        "CallingProcessSectionSignatureLevel" / Int8ul,
        "CallingProcessProtection" / Int8ul,
        "CallingThreadId" / Int32ul,
        "CallingThreadCreateTime" / Int64ul,
        "TargetProcessId" / Int32ul,
        "TargetProcessCreateTime" / Int64ul,
        "TargetProcessStartKey" / Int64ul,
        "TargetProcessSignatureLevel" / Int8ul,
        "TargetProcessSectionSignatureLevel" / Int8ul,
        "TargetProcessProtection" / Int8ul,
        "OriginalProcessId" / Int32ul,
        "OriginalProcessCreateTime" / Int64ul,
        "OriginalProcessStartKey" / Int64ul,
        "OriginalProcessSignatureLevel" / Int8ul,
        "OriginalProcessSectionSignatureLevel" / Int8ul,
        "OriginalProcessProtection" / Int8ul,
        "BaseAddress" / Int64ul,
        "RegionSize" / Int64ul,
        "AllocationType" / Int32ul,
        "ProtectionMask" / Int32ul
    )


@declare(guid=guid("f4e1897c-bb5d-5668-f1d8-040f4d8dd344"), event_id=2, version=0)
class Microsoft_Windows_Threat_Intelligence_2_0(Etw):
    pattern = Struct(
        "CallingProcessId" / Int32ul,
        "CallingProcessCreateTime" / Int64ul,
        "CallingProcessStartKey" / Int64ul,
        "CallingProcessSignatureLevel" / Int8ul,
        "CallingProcessSectionSignatureLevel" / Int8ul,
        "CallingProcessProtection" / Int8ul,
        "CallingThreadId" / Int32ul,
        "CallingThreadCreateTime" / Int64ul,
        "TargetProcessId" / Int32ul,
        "TargetProcessCreateTime" / Int64ul,
        "TargetProcessStartKey" / Int64ul,
        "TargetProcessSignatureLevel" / Int8ul,
        "TargetProcessSectionSignatureLevel" / Int8ul,
        "TargetProcessProtection" / Int8ul,
        "OriginalProcessId" / Int32ul,
        "OriginalProcessCreateTime" / Int64ul,
        "OriginalProcessStartKey" / Int64ul,
        "OriginalProcessSignatureLevel" / Int8ul,
        "OriginalProcessSectionSignatureLevel" / Int8ul,
        "OriginalProcessProtection" / Int8ul,
        "BaseAddress" / Int64ul,
        "RegionSize" / Int64ul,
        "ProtectionMask" / Int32ul,
        "LastProtectionMask" / Int32ul
    )


@declare(guid=guid("f4e1897c-bb5d-5668-f1d8-040f4d8dd344"), event_id=3, version=0)
class Microsoft_Windows_Threat_Intelligence_3_0(Etw):
    pattern = Struct(
        "CallingProcessId" / Int32ul,
        "CallingProcessCreateTime" / Int64ul,
        "CallingProcessStartKey" / Int64ul,
        "CallingProcessSignatureLevel" / Int8ul,
        "CallingProcessSectionSignatureLevel" / Int8ul,
        "CallingProcessProtection" / Int8ul,
        "CallingThreadId" / Int32ul,
        "CallingThreadCreateTime" / Int64ul,
        "TargetProcessId" / Int32ul,
        "TargetProcessCreateTime" / Int64ul,
        "TargetProcessStartKey" / Int64ul,
        "TargetProcessSignatureLevel" / Int8ul,
        "TargetProcessSectionSignatureLevel" / Int8ul,
        "TargetProcessProtection" / Int8ul,
        "BaseAddress" / Int64ul,
        "ViewSize" / Int64ul,
        "AllocationType" / Int32ul,
        "ProtectionMask" / Int32ul
    )


@declare(guid=guid("f4e1897c-bb5d-5668-f1d8-040f4d8dd344"), event_id=4, version=0)
class Microsoft_Windows_Threat_Intelligence_4_0(Etw):
    pattern = Struct(
        "CallingProcessId" / Int32ul,
        "CallingProcessCreateTime" / Int64ul,
        "CallingProcessStartKey" / Int64ul,
        "CallingProcessSignatureLevel" / Int8ul,
        "CallingProcessSectionSignatureLevel" / Int8ul,
        "CallingProcessProtection" / Int8ul,
        "CallingThreadId" / Int32ul,
        "CallingThreadCreateTime" / Int64ul,
        "TargetProcessId" / Int32ul,
        "TargetProcessCreateTime" / Int64ul,
        "TargetProcessStartKey" / Int64ul,
        "TargetProcessSignatureLevel" / Int8ul,
        "TargetProcessSectionSignatureLevel" / Int8ul,
        "TargetProcessProtection" / Int8ul,
        "TargetThreadId" / Int32ul,
        "TargetThreadCreateTime" / Int64ul,
        "OriginalProcessId" / Int32ul,
        "OriginalProcessCreateTime" / Int64ul,
        "OriginalProcessStartKey" / Int64ul,
        "OriginalProcessSignatureLevel" / Int8ul,
        "OriginalProcessSectionSignatureLevel" / Int8ul,
        "OriginalProcessProtection" / Int8ul,
        "TargetThreadAlertable" / Int8ul,
        "ApcRoutine" / Int64ul,
        "ApcArgument1" / Int64ul,
        "ApcArgument2" / Int64ul,
        "ApcArgument3" / Int64ul,
        "RealEventTime" / Int64ul,
        "ApcRoutineVadQueryResult" / Int32ul,
        "ApcRoutineVadAllocationBase" / Int64ul,
        "ApcRoutineVadAllocationProtect" / Int32ul,
        "ApcRoutineVadRegionType" / Int32ul,
        "ApcRoutineVadRegionSize" / Int64ul,
        "ApcRoutineVadCommitSize" / Int64ul,
        "ApcRoutineVadMmfName" / WString,
        "ApcArgument1VadQueryResult" / Int32ul,
        "ApcArgument1VadAllocationBase" / Int64ul,
        "ApcArgument1VadAllocationProtect" / Int32ul,
        "ApcArgument1VadRegionType" / Int32ul,
        "ApcArgument1VadRegionSize" / Int64ul,
        "ApcArgument1VadCommitSize" / Int64ul,
        "ApcArgument1VadMmfName" / WString
    )


@declare(guid=guid("f4e1897c-bb5d-5668-f1d8-040f4d8dd344"), event_id=5, version=0)
class Microsoft_Windows_Threat_Intelligence_5_0(Etw):
    pattern = Struct(
        "CallingProcessId" / Int32ul,
        "CallingProcessCreateTime" / Int64ul,
        "CallingProcessStartKey" / Int64ul,
        "CallingProcessSignatureLevel" / Int8ul,
        "CallingProcessSectionSignatureLevel" / Int8ul,
        "CallingProcessProtection" / Int8ul,
        "CallingThreadId" / Int32ul,
        "CallingThreadCreateTime" / Int64ul,
        "TargetProcessId" / Int32ul,
        "TargetProcessCreateTime" / Int64ul,
        "TargetProcessStartKey" / Int64ul,
        "TargetProcessSignatureLevel" / Int8ul,
        "TargetProcessSectionSignatureLevel" / Int8ul,
        "TargetProcessProtection" / Int8ul,
        "TargetThreadId" / Int32ul,
        "TargetThreadCreateTime" / Int64ul,
        "ContextFlags" / Int32ul,
        "ContextMask" / Int16ul,
        "Pc" / Int64ul,
        "Sp" / Int64ul,
        "Lr" / Int64ul,
        "Fp" / Int64ul,
        "Reg0" / Int64ul,
        "Reg1" / Int64ul,
        "Reg2" / Int64ul,
        "Reg3" / Int64ul,
        "Reg4" / Int64ul,
        "Reg5" / Int64ul,
        "Reg6" / Int64ul,
        "Reg7" / Int64ul,
        "RealEventTime" / Int64ul,
        "PcVadQueryResult" / Int32ul,
        "PcVadAllocationBase" / Int64ul,
        "PcVadAllocationProtect" / Int32ul,
        "PcVadRegionType" / Int32ul,
        "PcVadRegionSize" / Int64ul,
        "PcVadCommitSize" / Int64ul,
        "PcVadMmfName" / WString
    )


@declare(guid=guid("f4e1897c-bb5d-5668-f1d8-040f4d8dd344"), event_id=6, version=0)
class Microsoft_Windows_Threat_Intelligence_6_0(Etw):
    pattern = Struct(
        "CallingProcessId" / Int32ul,
        "CallingProcessCreateTime" / Int64ul,
        "CallingProcessStartKey" / Int64ul,
        "CallingProcessSignatureLevel" / Int8ul,
        "CallingProcessSectionSignatureLevel" / Int8ul,
        "CallingProcessProtection" / Int8ul,
        "CallingThreadId" / Int32ul,
        "CallingThreadCreateTime" / Int64ul,
        "TargetProcessId" / Int32ul,
        "TargetProcessCreateTime" / Int64ul,
        "TargetProcessStartKey" / Int64ul,
        "TargetProcessSignatureLevel" / Int8ul,
        "TargetProcessSectionSignatureLevel" / Int8ul,
        "TargetProcessProtection" / Int8ul,
        "OriginalProcessId" / Int32ul,
        "OriginalProcessCreateTime" / Int64ul,
        "OriginalProcessStartKey" / Int64ul,
        "OriginalProcessSignatureLevel" / Int8ul,
        "OriginalProcessSectionSignatureLevel" / Int8ul,
        "OriginalProcessProtection" / Int8ul,
        "BaseAddress" / Int64ul,
        "RegionSize" / Int64ul,
        "AllocationType" / Int32ul,
        "ProtectionMask" / Int32ul
    )


@declare(guid=guid("f4e1897c-bb5d-5668-f1d8-040f4d8dd344"), event_id=7, version=0)
class Microsoft_Windows_Threat_Intelligence_7_0(Etw):
    pattern = Struct(
        "CallingProcessId" / Int32ul,
        "CallingProcessCreateTime" / Int64ul,
        "CallingProcessStartKey" / Int64ul,
        "CallingProcessSignatureLevel" / Int8ul,
        "CallingProcessSectionSignatureLevel" / Int8ul,
        "CallingProcessProtection" / Int8ul,
        "CallingThreadId" / Int32ul,
        "CallingThreadCreateTime" / Int64ul,
        "TargetProcessId" / Int32ul,
        "TargetProcessCreateTime" / Int64ul,
        "TargetProcessStartKey" / Int64ul,
        "TargetProcessSignatureLevel" / Int8ul,
        "TargetProcessSectionSignatureLevel" / Int8ul,
        "TargetProcessProtection" / Int8ul,
        "OriginalProcessId" / Int32ul,
        "OriginalProcessCreateTime" / Int64ul,
        "OriginalProcessStartKey" / Int64ul,
        "OriginalProcessSignatureLevel" / Int8ul,
        "OriginalProcessSectionSignatureLevel" / Int8ul,
        "OriginalProcessProtection" / Int8ul,
        "BaseAddress" / Int64ul,
        "RegionSize" / Int64ul,
        "ProtectionMask" / Int32ul,
        "LastProtectionMask" / Int32ul
    )


@declare(guid=guid("f4e1897c-bb5d-5668-f1d8-040f4d8dd344"), event_id=8, version=0)
class Microsoft_Windows_Threat_Intelligence_8_0(Etw):
    pattern = Struct(
        "CallingProcessId" / Int32ul,
        "CallingProcessCreateTime" / Int64ul,
        "CallingProcessStartKey" / Int64ul,
        "CallingProcessSignatureLevel" / Int8ul,
        "CallingProcessSectionSignatureLevel" / Int8ul,
        "CallingProcessProtection" / Int8ul,
        "CallingThreadId" / Int32ul,
        "CallingThreadCreateTime" / Int64ul,
        "TargetProcessId" / Int32ul,
        "TargetProcessCreateTime" / Int64ul,
        "TargetProcessStartKey" / Int64ul,
        "TargetProcessSignatureLevel" / Int8ul,
        "TargetProcessSectionSignatureLevel" / Int8ul,
        "TargetProcessProtection" / Int8ul,
        "BaseAddress" / Int64ul,
        "ViewSize" / Int64ul,
        "AllocationType" / Int32ul,
        "ProtectionMask" / Int32ul
    )


@declare(guid=guid("f4e1897c-bb5d-5668-f1d8-040f4d8dd344"), event_id=11, version=0)
class Microsoft_Windows_Threat_Intelligence_11_0(Etw):
    pattern = Struct(
        "OperationStatus" / Int32ul,
        "CallingProcessId" / Int32ul,
        "CallingProcessCreateTime" / Int64ul,
        "CallingProcessStartKey" / Int64ul,
        "CallingProcessSignatureLevel" / Int8ul,
        "CallingProcessSectionSignatureLevel" / Int8ul,
        "CallingProcessProtection" / Int8ul,
        "CallingThreadId" / Int32ul,
        "CallingThreadCreateTime" / Int64ul,
        "TargetProcessId" / Int32ul,
        "TargetProcessCreateTime" / Int64ul,
        "TargetProcessStartKey" / Int64ul,
        "TargetProcessSignatureLevel" / Int8ul,
        "TargetProcessSectionSignatureLevel" / Int8ul,
        "TargetProcessProtection" / Int8ul,
        "BaseAddress" / Int64ul,
        "BytesCopied" / Int64ul
    )


@declare(guid=guid("f4e1897c-bb5d-5668-f1d8-040f4d8dd344"), event_id=12, version=0)
class Microsoft_Windows_Threat_Intelligence_12_0(Etw):
    pattern = Struct(
        "OperationStatus" / Int32ul,
        "CallingProcessId" / Int32ul,
        "CallingProcessCreateTime" / Int64ul,
        "CallingProcessStartKey" / Int64ul,
        "CallingProcessSignatureLevel" / Int8ul,
        "CallingProcessSectionSignatureLevel" / Int8ul,
        "CallingProcessProtection" / Int8ul,
        "CallingThreadId" / Int32ul,
        "CallingThreadCreateTime" / Int64ul,
        "TargetProcessId" / Int32ul,
        "TargetProcessCreateTime" / Int64ul,
        "TargetProcessStartKey" / Int64ul,
        "TargetProcessSignatureLevel" / Int8ul,
        "TargetProcessSectionSignatureLevel" / Int8ul,
        "TargetProcessProtection" / Int8ul,
        "BaseAddress" / Int64ul,
        "BytesCopied" / Int64ul
    )


@declare(guid=guid("f4e1897c-bb5d-5668-f1d8-040f4d8dd344"), event_id=13, version=0)
class Microsoft_Windows_Threat_Intelligence_13_0(Etw):
    pattern = Struct(
        "OperationStatus" / Int32ul,
        "CallingProcessId" / Int32ul,
        "CallingProcessCreateTime" / Int64ul,
        "CallingProcessStartKey" / Int64ul,
        "CallingProcessSignatureLevel" / Int8ul,
        "CallingProcessSectionSignatureLevel" / Int8ul,
        "CallingProcessProtection" / Int8ul,
        "CallingThreadId" / Int32ul,
        "CallingThreadCreateTime" / Int64ul,
        "TargetProcessId" / Int32ul,
        "TargetProcessCreateTime" / Int64ul,
        "TargetProcessStartKey" / Int64ul,
        "TargetProcessSignatureLevel" / Int8ul,
        "TargetProcessSectionSignatureLevel" / Int8ul,
        "TargetProcessProtection" / Int8ul,
        "BaseAddress" / Int64ul,
        "BytesCopied" / Int64ul
    )


@declare(guid=guid("f4e1897c-bb5d-5668-f1d8-040f4d8dd344"), event_id=14, version=0)
class Microsoft_Windows_Threat_Intelligence_14_0(Etw):
    pattern = Struct(
        "OperationStatus" / Int32ul,
        "CallingProcessId" / Int32ul,
        "CallingProcessCreateTime" / Int64ul,
        "CallingProcessStartKey" / Int64ul,
        "CallingProcessSignatureLevel" / Int8ul,
        "CallingProcessSectionSignatureLevel" / Int8ul,
        "CallingProcessProtection" / Int8ul,
        "CallingThreadId" / Int32ul,
        "CallingThreadCreateTime" / Int64ul,
        "TargetProcessId" / Int32ul,
        "TargetProcessCreateTime" / Int64ul,
        "TargetProcessStartKey" / Int64ul,
        "TargetProcessSignatureLevel" / Int8ul,
        "TargetProcessSectionSignatureLevel" / Int8ul,
        "TargetProcessProtection" / Int8ul,
        "BaseAddress" / Int64ul,
        "BytesCopied" / Int64ul
    )


@declare(guid=guid("f4e1897c-bb5d-5668-f1d8-040f4d8dd344"), event_id=15, version=0)
class Microsoft_Windows_Threat_Intelligence_15_0(Etw):
    pattern = Struct(
        "OperationStatus" / Int32ul,
        "CallingProcessId" / Int32ul,
        "CallingProcessCreateTime" / Int64ul,
        "CallingProcessStartKey" / Int64ul,
        "CallingProcessSignatureLevel" / Int8ul,
        "CallingProcessSectionSignatureLevel" / Int8ul,
        "CallingProcessProtection" / Int8ul,
        "CallingThreadId" / Int32ul,
        "CallingThreadCreateTime" / Int64ul,
        "TargetProcessId" / Int32ul,
        "TargetProcessCreateTime" / Int64ul,
        "TargetProcessStartKey" / Int64ul,
        "TargetProcessSignatureLevel" / Int8ul,
        "TargetProcessSectionSignatureLevel" / Int8ul,
        "TargetProcessProtection" / Int8ul,
        "TargetThreadId" / Int32ul,
        "TargetThreadCreateTime" / Int64ul
    )


@declare(guid=guid("f4e1897c-bb5d-5668-f1d8-040f4d8dd344"), event_id=16, version=0)
class Microsoft_Windows_Threat_Intelligence_16_0(Etw):
    pattern = Struct(
        "OperationStatus" / Int32ul,
        "CallingProcessId" / Int32ul,
        "CallingProcessCreateTime" / Int64ul,
        "CallingProcessStartKey" / Int64ul,
        "CallingProcessSignatureLevel" / Int8ul,
        "CallingProcessSectionSignatureLevel" / Int8ul,
        "CallingProcessProtection" / Int8ul,
        "CallingThreadId" / Int32ul,
        "CallingThreadCreateTime" / Int64ul,
        "TargetProcessId" / Int32ul,
        "TargetProcessCreateTime" / Int64ul,
        "TargetProcessStartKey" / Int64ul,
        "TargetProcessSignatureLevel" / Int8ul,
        "TargetProcessSectionSignatureLevel" / Int8ul,
        "TargetProcessProtection" / Int8ul,
        "TargetThreadId" / Int32ul,
        "TargetThreadCreateTime" / Int64ul
    )


@declare(guid=guid("f4e1897c-bb5d-5668-f1d8-040f4d8dd344"), event_id=17, version=0)
class Microsoft_Windows_Threat_Intelligence_17_0(Etw):
    pattern = Struct(
        "OperationStatus" / Int32ul,
        "CallingProcessId" / Int32ul,
        "CallingProcessCreateTime" / Int64ul,
        "CallingProcessStartKey" / Int64ul,
        "CallingProcessSignatureLevel" / Int8ul,
        "CallingProcessSectionSignatureLevel" / Int8ul,
        "CallingProcessProtection" / Int8ul,
        "CallingThreadId" / Int32ul,
        "CallingThreadCreateTime" / Int64ul,
        "TargetProcessId" / Int32ul,
        "TargetProcessCreateTime" / Int64ul,
        "TargetProcessStartKey" / Int64ul,
        "TargetProcessSignatureLevel" / Int8ul,
        "TargetProcessSectionSignatureLevel" / Int8ul,
        "TargetProcessProtection" / Int8ul
    )


@declare(guid=guid("f4e1897c-bb5d-5668-f1d8-040f4d8dd344"), event_id=18, version=0)
class Microsoft_Windows_Threat_Intelligence_18_0(Etw):
    pattern = Struct(
        "OperationStatus" / Int32ul,
        "CallingProcessId" / Int32ul,
        "CallingProcessCreateTime" / Int64ul,
        "CallingProcessStartKey" / Int64ul,
        "CallingProcessSignatureLevel" / Int8ul,
        "CallingProcessSectionSignatureLevel" / Int8ul,
        "CallingProcessProtection" / Int8ul,
        "CallingThreadId" / Int32ul,
        "CallingThreadCreateTime" / Int64ul,
        "TargetProcessId" / Int32ul,
        "TargetProcessCreateTime" / Int64ul,
        "TargetProcessStartKey" / Int64ul,
        "TargetProcessSignatureLevel" / Int8ul,
        "TargetProcessSectionSignatureLevel" / Int8ul,
        "TargetProcessProtection" / Int8ul
    )


@declare(guid=guid("f4e1897c-bb5d-5668-f1d8-040f4d8dd344"), event_id=19, version=0)
class Microsoft_Windows_Threat_Intelligence_19_0(Etw):
    pattern = Struct(
        "OperationStatus" / Int32ul,
        "CallingProcessId" / Int32ul,
        "CallingProcessCreateTime" / Int64ul,
        "CallingProcessStartKey" / Int64ul,
        "CallingProcessSignatureLevel" / Int8ul,
        "CallingProcessSectionSignatureLevel" / Int8ul,
        "CallingProcessProtection" / Int8ul,
        "CallingThreadId" / Int32ul,
        "CallingThreadCreateTime" / Int64ul,
        "TargetProcessId" / Int32ul,
        "TargetProcessCreateTime" / Int64ul,
        "TargetProcessStartKey" / Int64ul,
        "TargetProcessSignatureLevel" / Int8ul,
        "TargetProcessSectionSignatureLevel" / Int8ul,
        "TargetProcessProtection" / Int8ul
    )


@declare(guid=guid("f4e1897c-bb5d-5668-f1d8-040f4d8dd344"), event_id=20, version=0)
class Microsoft_Windows_Threat_Intelligence_20_0(Etw):
    pattern = Struct(
        "OperationStatus" / Int32ul,
        "CallingProcessId" / Int32ul,
        "CallingProcessCreateTime" / Int64ul,
        "CallingProcessStartKey" / Int64ul,
        "CallingProcessSignatureLevel" / Int8ul,
        "CallingProcessSectionSignatureLevel" / Int8ul,
        "CallingProcessProtection" / Int8ul,
        "CallingThreadId" / Int32ul,
        "CallingThreadCreateTime" / Int64ul,
        "TargetProcessId" / Int32ul,
        "TargetProcessCreateTime" / Int64ul,
        "TargetProcessStartKey" / Int64ul,
        "TargetProcessSignatureLevel" / Int8ul,
        "TargetProcessSectionSignatureLevel" / Int8ul,
        "TargetProcessProtection" / Int8ul
    )


@declare(guid=guid("f4e1897c-bb5d-5668-f1d8-040f4d8dd344"), event_id=21, version=0)
class Microsoft_Windows_Threat_Intelligence_21_0(Etw):
    pattern = Struct(
        "CallingProcessId" / Int32ul,
        "CallingProcessCreateTime" / Int64ul,
        "CallingProcessStartKey" / Int64ul,
        "CallingProcessSignatureLevel" / Int8ul,
        "CallingProcessSectionSignatureLevel" / Int8ul,
        "CallingProcessProtection" / Int8ul,
        "CallingThreadId" / Int32ul,
        "CallingThreadCreateTime" / Int64ul,
        "TargetProcessId" / Int32ul,
        "TargetProcessCreateTime" / Int64ul,
        "TargetProcessStartKey" / Int64ul,
        "TargetProcessSignatureLevel" / Int8ul,
        "TargetProcessSectionSignatureLevel" / Int8ul,
        "TargetProcessProtection" / Int8ul,
        "OriginalProcessId" / Int32ul,
        "OriginalProcessCreateTime" / Int64ul,
        "OriginalProcessStartKey" / Int64ul,
        "OriginalProcessSignatureLevel" / Int8ul,
        "OriginalProcessSectionSignatureLevel" / Int8ul,
        "OriginalProcessProtection" / Int8ul,
        "BaseAddress" / Int64ul,
        "RegionSize" / Int64ul,
        "AllocationType" / Int32ul,
        "ProtectionMask" / Int32ul
    )


@declare(guid=guid("f4e1897c-bb5d-5668-f1d8-040f4d8dd344"), event_id=22, version=0)
class Microsoft_Windows_Threat_Intelligence_22_0(Etw):
    pattern = Struct(
        "CallingProcessId" / Int32ul,
        "CallingProcessCreateTime" / Int64ul,
        "CallingProcessStartKey" / Int64ul,
        "CallingProcessSignatureLevel" / Int8ul,
        "CallingProcessSectionSignatureLevel" / Int8ul,
        "CallingProcessProtection" / Int8ul,
        "CallingThreadId" / Int32ul,
        "CallingThreadCreateTime" / Int64ul,
        "TargetProcessId" / Int32ul,
        "TargetProcessCreateTime" / Int64ul,
        "TargetProcessStartKey" / Int64ul,
        "TargetProcessSignatureLevel" / Int8ul,
        "TargetProcessSectionSignatureLevel" / Int8ul,
        "TargetProcessProtection" / Int8ul,
        "OriginalProcessId" / Int32ul,
        "OriginalProcessCreateTime" / Int64ul,
        "OriginalProcessStartKey" / Int64ul,
        "OriginalProcessSignatureLevel" / Int8ul,
        "OriginalProcessSectionSignatureLevel" / Int8ul,
        "OriginalProcessProtection" / Int8ul,
        "BaseAddress" / Int64ul,
        "RegionSize" / Int64ul,
        "ProtectionMask" / Int32ul,
        "LastProtectionMask" / Int32ul
    )


@declare(guid=guid("f4e1897c-bb5d-5668-f1d8-040f4d8dd344"), event_id=23, version=0)
class Microsoft_Windows_Threat_Intelligence_23_0(Etw):
    pattern = Struct(
        "CallingProcessId" / Int32ul,
        "CallingProcessCreateTime" / Int64ul,
        "CallingProcessStartKey" / Int64ul,
        "CallingProcessSignatureLevel" / Int8ul,
        "CallingProcessSectionSignatureLevel" / Int8ul,
        "CallingProcessProtection" / Int8ul,
        "CallingThreadId" / Int32ul,
        "CallingThreadCreateTime" / Int64ul,
        "TargetProcessId" / Int32ul,
        "TargetProcessCreateTime" / Int64ul,
        "TargetProcessStartKey" / Int64ul,
        "TargetProcessSignatureLevel" / Int8ul,
        "TargetProcessSectionSignatureLevel" / Int8ul,
        "TargetProcessProtection" / Int8ul,
        "BaseAddress" / Int64ul,
        "ViewSize" / Int64ul,
        "AllocationType" / Int32ul,
        "ProtectionMask" / Int32ul
    )


@declare(guid=guid("f4e1897c-bb5d-5668-f1d8-040f4d8dd344"), event_id=24, version=0)
class Microsoft_Windows_Threat_Intelligence_24_0(Etw):
    pattern = Struct(
        "CallingProcessId" / Int32ul,
        "CallingProcessCreateTime" / Int64ul,
        "CallingProcessStartKey" / Int64ul,
        "CallingProcessSignatureLevel" / Int8ul,
        "CallingProcessSectionSignatureLevel" / Int8ul,
        "CallingProcessProtection" / Int8ul,
        "CallingThreadId" / Int32ul,
        "CallingThreadCreateTime" / Int64ul,
        "TargetProcessId" / Int32ul,
        "TargetProcessCreateTime" / Int64ul,
        "TargetProcessStartKey" / Int64ul,
        "TargetProcessSignatureLevel" / Int8ul,
        "TargetProcessSectionSignatureLevel" / Int8ul,
        "TargetProcessProtection" / Int8ul,
        "TargetThreadId" / Int32ul,
        "TargetThreadCreateTime" / Int64ul,
        "OriginalProcessId" / Int32ul,
        "OriginalProcessCreateTime" / Int64ul,
        "OriginalProcessStartKey" / Int64ul,
        "OriginalProcessSignatureLevel" / Int8ul,
        "OriginalProcessSectionSignatureLevel" / Int8ul,
        "OriginalProcessProtection" / Int8ul,
        "TargetThreadAlertable" / Int8ul,
        "ApcRoutine" / Int64ul,
        "ApcArgument1" / Int64ul,
        "ApcArgument2" / Int64ul,
        "ApcArgument3" / Int64ul,
        "RealEventTime" / Int64ul,
        "ApcRoutineVadQueryResult" / Int32ul,
        "ApcRoutineVadAllocationBase" / Int64ul,
        "ApcRoutineVadAllocationProtect" / Int32ul,
        "ApcRoutineVadRegionType" / Int32ul,
        "ApcRoutineVadRegionSize" / Int64ul,
        "ApcRoutineVadCommitSize" / Int64ul,
        "ApcRoutineVadMmfName" / WString,
        "ApcArgument1VadQueryResult" / Int32ul,
        "ApcArgument1VadAllocationBase" / Int64ul,
        "ApcArgument1VadAllocationProtect" / Int32ul,
        "ApcArgument1VadRegionType" / Int32ul,
        "ApcArgument1VadRegionSize" / Int64ul,
        "ApcArgument1VadCommitSize" / Int64ul,
        "ApcArgument1VadMmfName" / WString
    )


@declare(guid=guid("f4e1897c-bb5d-5668-f1d8-040f4d8dd344"), event_id=25, version=0)
class Microsoft_Windows_Threat_Intelligence_25_0(Etw):
    pattern = Struct(
        "CallingProcessId" / Int32ul,
        "CallingProcessCreateTime" / Int64ul,
        "CallingProcessStartKey" / Int64ul,
        "CallingProcessSignatureLevel" / Int8ul,
        "CallingProcessSectionSignatureLevel" / Int8ul,
        "CallingProcessProtection" / Int8ul,
        "CallingThreadId" / Int32ul,
        "CallingThreadCreateTime" / Int64ul,
        "TargetProcessId" / Int32ul,
        "TargetProcessCreateTime" / Int64ul,
        "TargetProcessStartKey" / Int64ul,
        "TargetProcessSignatureLevel" / Int8ul,
        "TargetProcessSectionSignatureLevel" / Int8ul,
        "TargetProcessProtection" / Int8ul,
        "TargetThreadId" / Int32ul,
        "TargetThreadCreateTime" / Int64ul,
        "ContextFlags" / Int32ul,
        "ContextMask" / Int16ul,
        "Pc" / Int64ul,
        "Sp" / Int64ul,
        "Lr" / Int64ul,
        "Fp" / Int64ul,
        "Reg0" / Int64ul,
        "Reg1" / Int64ul,
        "Reg2" / Int64ul,
        "Reg3" / Int64ul,
        "Reg4" / Int64ul,
        "Reg5" / Int64ul,
        "Reg6" / Int64ul,
        "Reg7" / Int64ul,
        "RealEventTime" / Int64ul,
        "PcVadQueryResult" / Int32ul,
        "PcVadAllocationBase" / Int64ul,
        "PcVadAllocationProtect" / Int32ul,
        "PcVadRegionType" / Int32ul,
        "PcVadRegionSize" / Int64ul,
        "PcVadCommitSize" / Int64ul,
        "PcVadMmfName" / WString
    )


@declare(guid=guid("f4e1897c-bb5d-5668-f1d8-040f4d8dd344"), event_id=26, version=0)
class Microsoft_Windows_Threat_Intelligence_26_0(Etw):
    pattern = Struct(
        "CallingProcessId" / Int32ul,
        "CallingProcessCreateTime" / Int64ul,
        "CallingProcessStartKey" / Int64ul,
        "CallingProcessSignatureLevel" / Int8ul,
        "CallingProcessSectionSignatureLevel" / Int8ul,
        "CallingProcessProtection" / Int8ul,
        "CallingThreadId" / Int32ul,
        "CallingThreadCreateTime" / Int64ul,
        "TargetProcessId" / Int32ul,
        "TargetProcessCreateTime" / Int64ul,
        "TargetProcessStartKey" / Int64ul,
        "TargetProcessSignatureLevel" / Int8ul,
        "TargetProcessSectionSignatureLevel" / Int8ul,
        "TargetProcessProtection" / Int8ul,
        "OriginalProcessId" / Int32ul,
        "OriginalProcessCreateTime" / Int64ul,
        "OriginalProcessStartKey" / Int64ul,
        "OriginalProcessSignatureLevel" / Int8ul,
        "OriginalProcessSectionSignatureLevel" / Int8ul,
        "OriginalProcessProtection" / Int8ul,
        "BaseAddress" / Int64ul,
        "RegionSize" / Int64ul,
        "AllocationType" / Int32ul,
        "ProtectionMask" / Int32ul
    )


@declare(guid=guid("f4e1897c-bb5d-5668-f1d8-040f4d8dd344"), event_id=27, version=0)
class Microsoft_Windows_Threat_Intelligence_27_0(Etw):
    pattern = Struct(
        "CallingProcessId" / Int32ul,
        "CallingProcessCreateTime" / Int64ul,
        "CallingProcessStartKey" / Int64ul,
        "CallingProcessSignatureLevel" / Int8ul,
        "CallingProcessSectionSignatureLevel" / Int8ul,
        "CallingProcessProtection" / Int8ul,
        "CallingThreadId" / Int32ul,
        "CallingThreadCreateTime" / Int64ul,
        "TargetProcessId" / Int32ul,
        "TargetProcessCreateTime" / Int64ul,
        "TargetProcessStartKey" / Int64ul,
        "TargetProcessSignatureLevel" / Int8ul,
        "TargetProcessSectionSignatureLevel" / Int8ul,
        "TargetProcessProtection" / Int8ul,
        "OriginalProcessId" / Int32ul,
        "OriginalProcessCreateTime" / Int64ul,
        "OriginalProcessStartKey" / Int64ul,
        "OriginalProcessSignatureLevel" / Int8ul,
        "OriginalProcessSectionSignatureLevel" / Int8ul,
        "OriginalProcessProtection" / Int8ul,
        "BaseAddress" / Int64ul,
        "RegionSize" / Int64ul,
        "ProtectionMask" / Int32ul,
        "LastProtectionMask" / Int32ul
    )


@declare(guid=guid("f4e1897c-bb5d-5668-f1d8-040f4d8dd344"), event_id=28, version=0)
class Microsoft_Windows_Threat_Intelligence_28_0(Etw):
    pattern = Struct(
        "CallingProcessId" / Int32ul,
        "CallingProcessCreateTime" / Int64ul,
        "CallingProcessStartKey" / Int64ul,
        "CallingProcessSignatureLevel" / Int8ul,
        "CallingProcessSectionSignatureLevel" / Int8ul,
        "CallingProcessProtection" / Int8ul,
        "CallingThreadId" / Int32ul,
        "CallingThreadCreateTime" / Int64ul,
        "TargetProcessId" / Int32ul,
        "TargetProcessCreateTime" / Int64ul,
        "TargetProcessStartKey" / Int64ul,
        "TargetProcessSignatureLevel" / Int8ul,
        "TargetProcessSectionSignatureLevel" / Int8ul,
        "TargetProcessProtection" / Int8ul,
        "BaseAddress" / Int64ul,
        "ViewSize" / Int64ul,
        "AllocationType" / Int32ul,
        "ProtectionMask" / Int32ul
    )


@declare(guid=guid("f4e1897c-bb5d-5668-f1d8-040f4d8dd344"), event_id=29, version=0)
class Microsoft_Windows_Threat_Intelligence_29_0(Etw):
    pattern = Struct(
        "DriverNameLength" / Int16ul,
        "DriverName" / Bytes(lambda this: this.DriverNameLength),
        "CodeIntegrityOption" / Int32ul
    )


@declare(guid=guid("f4e1897c-bb5d-5668-f1d8-040f4d8dd344"), event_id=30, version=0)
class Microsoft_Windows_Threat_Intelligence_30_0(Etw):
    pattern = Struct(
        "DriverNameLength" / Int16ul,
        "DriverName" / Bytes(lambda this: this.DriverNameLength)
    )


@declare(guid=guid("f4e1897c-bb5d-5668-f1d8-040f4d8dd344"), event_id=31, version=0)
class Microsoft_Windows_Threat_Intelligence_31_0(Etw):
    pattern = Struct(
        "DriverNameLength" / Int16ul,
        "DriverName" / Bytes(lambda this: this.DriverNameLength),
        "DeviceNameLength" / Int16ul,
        "DeviceName" / Bytes(lambda this: this.DeviceNameLength)
    )


@declare(guid=guid("f4e1897c-bb5d-5668-f1d8-040f4d8dd344"), event_id=32, version=0)
class Microsoft_Windows_Threat_Intelligence_32_0(Etw):
    pattern = Struct(
        "DriverNameLength" / Int16ul,
        "DriverName" / Bytes(lambda this: this.DriverNameLength),
        "DeviceNameLength" / Int16ul,
        "DeviceName" / Bytes(lambda this: this.DeviceNameLength)
    )

