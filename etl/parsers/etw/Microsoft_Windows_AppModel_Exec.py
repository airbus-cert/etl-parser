# -*- coding: utf-8 -*-
"""
Microsoft-Windows-AppModel-Exec
GUID : eb65a492-86c0-406a-bace-9912d595bd69
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=100, version=0)
class Microsoft_Windows_AppModel_Exec_100_0(Etw):
    pattern = Struct(
        "PsmKey" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=101, version=0)
class Microsoft_Windows_AppModel_Exec_101_0(Etw):
    pattern = Struct(
        "PsmKey" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=102, version=0)
class Microsoft_Windows_AppModel_Exec_102_0(Etw):
    pattern = Struct(
        "PsmKey" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=103, version=0)
class Microsoft_Windows_AppModel_Exec_103_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "AppPsmKey" / WString,
        "State" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=104, version=0)
class Microsoft_Windows_AppModel_Exec_104_0(Etw):
    pattern = Struct(
        "Removal" / Int8ul,
        "SrcPsmKey" / WString,
        "TargetPsmKey" / WString,
        "Type" / Int32ul,
        "Error" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=105, version=0)
class Microsoft_Windows_AppModel_Exec_105_0(Etw):
    pattern = Struct(
        "ValueName" / WString,
        "Time" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=107, version=0)
class Microsoft_Windows_AppModel_Exec_107_0(Etw):
    pattern = Struct(
        "HwndPointer" / Int64ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=108, version=0)
class Microsoft_Windows_AppModel_Exec_108_0(Etw):
    pattern = Struct(
        "HwndPointer" / Int64ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=109, version=0)
class Microsoft_Windows_AppModel_Exec_109_0(Etw):
    pattern = Struct(
        "PsmKey" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=110, version=0)
class Microsoft_Windows_AppModel_Exec_110_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "Bool" / Int8ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=111, version=0)
class Microsoft_Windows_AppModel_Exec_111_0(Etw):
    pattern = Struct(
        "Hwnd" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=112, version=0)
class Microsoft_Windows_AppModel_Exec_112_0(Etw):
    pattern = Struct(
        "AUMID" / WString,
        "PID" / WString,
        "Count" / Int64ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=113, version=0)
class Microsoft_Windows_AppModel_Exec_113_0(Etw):
    pattern = Struct(
        "AUMID" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=114, version=0)
class Microsoft_Windows_AppModel_Exec_114_0(Etw):
    pattern = Struct(
        "PackageLevel" / Int8ul,
        "ErrorCode" / Int32ul,
        "Cookie" / Int64sl
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=115, version=0)
class Microsoft_Windows_AppModel_Exec_115_0(Etw):
    pattern = Struct(
        "AUMID" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=116, version=0)
class Microsoft_Windows_AppModel_Exec_116_0(Etw):
    pattern = Struct(
        "PsmKey" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=117, version=0)
class Microsoft_Windows_AppModel_Exec_117_0(Etw):
    pattern = Struct(
        "AUMID" / WString,
        "Bool1" / Int8ul,
        "Bool2" / Int8ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=118, version=0)
class Microsoft_Windows_AppModel_Exec_118_0(Etw):
    pattern = Struct(
        "AUMID" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=119, version=0)
class Microsoft_Windows_AppModel_Exec_119_0(Etw):
    pattern = Struct(
        "AUMID" / WString,
        "Flags" / Int32ul,
        "Reason" / Int64sl
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=120, version=0)
class Microsoft_Windows_AppModel_Exec_120_0(Etw):
    pattern = Struct(
        "MaxTterminate" / Int8ul,
        "AUMID" / WString,
        "ErrorCode" / Int32ul,
        "Reason" / Int64sl,
        "Misbehaving" / Int8ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=121, version=0)
class Microsoft_Windows_AppModel_Exec_121_0(Etw):
    pattern = Struct(
        "AUMID" / WString,
        "Flags" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=122, version=0)
class Microsoft_Windows_AppModel_Exec_122_0(Etw):
    pattern = Struct(
        "PlmFlags" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=123, version=0)
class Microsoft_Windows_AppModel_Exec_123_0(Etw):
    pattern = Struct(
        "AUMID" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=124, version=0)
class Microsoft_Windows_AppModel_Exec_124_0(Etw):
    pattern = Struct(
        "AUMID" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=125, version=0)
class Microsoft_Windows_AppModel_Exec_125_0(Etw):
    pattern = Struct(
        "ValueName" / WString,
        "Time" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=126, version=0)
class Microsoft_Windows_AppModel_Exec_126_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=127, version=0)
class Microsoft_Windows_AppModel_Exec_127_0(Etw):
    pattern = Struct(
        "AUMID" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=128, version=0)
class Microsoft_Windows_AppModel_Exec_128_0(Etw):
    pattern = Struct(
        "PID" / Int32ul,
        "ErrorCode" / Int32ul,
        "PackageState" / Int64sl
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=129, version=0)
class Microsoft_Windows_AppModel_Exec_129_0(Etw):
    pattern = Struct(
        "AUMID" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=130, version=0)
class Microsoft_Windows_AppModel_Exec_130_0(Etw):
    pattern = Struct(
        "SuspendExemptionReason" / Int32ul,
        "Priority" / Int32ul,
        "PsmKey" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=131, version=0)
class Microsoft_Windows_AppModel_Exec_131_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "Priority" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=132, version=0)
class Microsoft_Windows_AppModel_Exec_132_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "Priority" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=133, version=0)
class Microsoft_Windows_AppModel_Exec_133_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "Priority" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=134, version=0)
class Microsoft_Windows_AppModel_Exec_134_0(Etw):
    pattern = Struct(
        "PsmKey" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=135, version=0)
class Microsoft_Windows_AppModel_Exec_135_0(Etw):
    pattern = Struct(
        "PsmKey" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=136, version=0)
class Microsoft_Windows_AppModel_Exec_136_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "Exemption" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=137, version=0)
class Microsoft_Windows_AppModel_Exec_137_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "Bool" / Int8ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=138, version=0)
class Microsoft_Windows_AppModel_Exec_138_0(Etw):
    pattern = Struct(
        "PsmKey" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=140, version=0)
class Microsoft_Windows_AppModel_Exec_140_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "AUMID" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=142, version=0)
class Microsoft_Windows_AppModel_Exec_142_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "TimeOut" / Int64sl
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=143, version=0)
class Microsoft_Windows_AppModel_Exec_143_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=144, version=0)
class Microsoft_Windows_AppModel_Exec_144_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=145, version=0)
class Microsoft_Windows_AppModel_Exec_145_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString,
        "Time" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=146, version=0)
class Microsoft_Windows_AppModel_Exec_146_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=147, version=0)
class Microsoft_Windows_AppModel_Exec_147_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=148, version=0)
class Microsoft_Windows_AppModel_Exec_148_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=149, version=0)
class Microsoft_Windows_AppModel_Exec_149_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=150, version=0)
class Microsoft_Windows_AppModel_Exec_150_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "Trigger" / Int32ul,
        "Reason" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=151, version=0)
class Microsoft_Windows_AppModel_Exec_151_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "Trigger" / Int32ul,
        "Reason" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=152, version=0)
class Microsoft_Windows_AppModel_Exec_152_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "Trigger" / Int32ul,
        "Reason" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=153, version=0)
class Microsoft_Windows_AppModel_Exec_153_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "Trigger" / Int32ul,
        "Reason" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=154, version=0)
class Microsoft_Windows_AppModel_Exec_154_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "Trigger" / Int32ul,
        "Reason" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=155, version=0)
class Microsoft_Windows_AppModel_Exec_155_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "Trigger" / Int32ul,
        "Reason" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=156, version=0)
class Microsoft_Windows_AppModel_Exec_156_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "Type" / Int32ul,
        "Reason" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=157, version=0)
class Microsoft_Windows_AppModel_Exec_157_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "LogErrorCode" / Int32ul,
        "TerminationErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=158, version=0)
class Microsoft_Windows_AppModel_Exec_158_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString,
        "Type" / Int32ul,
        "Reason" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=159, version=0)
class Microsoft_Windows_AppModel_Exec_159_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString,
        "plmKnowsPackage" / Int8ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=161, version=0)
class Microsoft_Windows_AppModel_Exec_161_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=162, version=0)
class Microsoft_Windows_AppModel_Exec_162_0(Etw):
    pattern = Struct(
        "PsmKey" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=164, version=0)
class Microsoft_Windows_AppModel_Exec_164_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=165, version=0)
class Microsoft_Windows_AppModel_Exec_165_0(Etw):
    pattern = Struct(
        "PidCount" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=166, version=0)
class Microsoft_Windows_AppModel_Exec_166_0(Etw):
    pattern = Struct(
        "StateSource" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=167, version=0)
class Microsoft_Windows_AppModel_Exec_167_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=168, version=0)
class Microsoft_Windows_AppModel_Exec_168_0(Etw):
    pattern = Struct(
        "AUMID" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=169, version=0)
class Microsoft_Windows_AppModel_Exec_169_0(Etw):
    pattern = Struct(
        "AUMID" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=170, version=0)
class Microsoft_Windows_AppModel_Exec_170_0(Etw):
    pattern = Struct(
        "PsmKey" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=171, version=0)
class Microsoft_Windows_AppModel_Exec_171_0(Etw):
    pattern = Struct(
        "PsmKey" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=172, version=0)
class Microsoft_Windows_AppModel_Exec_172_0(Etw):
    pattern = Struct(
        "PsmKey" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=173, version=0)
class Microsoft_Windows_AppModel_Exec_173_0(Etw):
    pattern = Struct(
        "PsmKey" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=174, version=0)
class Microsoft_Windows_AppModel_Exec_174_0(Etw):
    pattern = Struct(
        "PsmKey" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=175, version=0)
class Microsoft_Windows_AppModel_Exec_175_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=176, version=0)
class Microsoft_Windows_AppModel_Exec_176_0(Etw):
    pattern = Struct(
        "PsmKey" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=177, version=0)
class Microsoft_Windows_AppModel_Exec_177_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=178, version=0)
class Microsoft_Windows_AppModel_Exec_178_0(Etw):
    pattern = Struct(
        "CommandLine" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=179, version=0)
class Microsoft_Windows_AppModel_Exec_179_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=180, version=0)
class Microsoft_Windows_AppModel_Exec_180_0(Etw):
    pattern = Struct(
        "PsmKey" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=181, version=0)
class Microsoft_Windows_AppModel_Exec_181_0(Etw):
    pattern = Struct(
        "PsmKey" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=182, version=0)
class Microsoft_Windows_AppModel_Exec_182_0(Etw):
    pattern = Struct(
        "AUMID" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=183, version=0)
class Microsoft_Windows_AppModel_Exec_183_0(Etw):
    pattern = Struct(
        "AUMID" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=184, version=0)
class Microsoft_Windows_AppModel_Exec_184_0(Etw):
    pattern = Struct(
        "AUMID" / WString,
        "Exemption" / Int64ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=185, version=0)
class Microsoft_Windows_AppModel_Exec_185_0(Etw):
    pattern = Struct(
        "AUMID" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=186, version=0)
class Microsoft_Windows_AppModel_Exec_186_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "State" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=187, version=0)
class Microsoft_Windows_AppModel_Exec_187_0(Etw):
    pattern = Struct(
        "PsmKey" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=188, version=0)
class Microsoft_Windows_AppModel_Exec_188_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=189, version=0)
class Microsoft_Windows_AppModel_Exec_189_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "State" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=190, version=0)
class Microsoft_Windows_AppModel_Exec_190_0(Etw):
    pattern = Struct(
        "PsmKey" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=191, version=0)
class Microsoft_Windows_AppModel_Exec_191_0(Etw):
    pattern = Struct(
        "PsmKey" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=192, version=0)
class Microsoft_Windows_AppModel_Exec_192_0(Etw):
    pattern = Struct(
        "PsmKey" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=193, version=0)
class Microsoft_Windows_AppModel_Exec_193_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=194, version=0)
class Microsoft_Windows_AppModel_Exec_194_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "State" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=195, version=0)
class Microsoft_Windows_AppModel_Exec_195_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "State" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=196, version=0)
class Microsoft_Windows_AppModel_Exec_196_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "Bool" / Int8ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=197, version=0)
class Microsoft_Windows_AppModel_Exec_197_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "State" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=198, version=0)
class Microsoft_Windows_AppModel_Exec_198_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=199, version=0)
class Microsoft_Windows_AppModel_Exec_199_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=200, version=0)
class Microsoft_Windows_AppModel_Exec_200_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=201, version=0)
class Microsoft_Windows_AppModel_Exec_201_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=202, version=0)
class Microsoft_Windows_AppModel_Exec_202_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=203, version=0)
class Microsoft_Windows_AppModel_Exec_203_0(Etw):
    pattern = Struct(
        "ValueName" / WString,
        "Timeout" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=204, version=0)
class Microsoft_Windows_AppModel_Exec_204_0(Etw):
    pattern = Struct(
        "AUMID" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=205, version=0)
class Microsoft_Windows_AppModel_Exec_205_0(Etw):
    pattern = Struct(
        "AUMID" / WString,
        "PID" / WString,
        "Count" / Int64ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=206, version=0)
class Microsoft_Windows_AppModel_Exec_206_0(Etw):
    pattern = Struct(
        "AUMID" / WString,
        "Canceled" / Int8ul,
        "Count" / Int64ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=207, version=0)
class Microsoft_Windows_AppModel_Exec_207_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "State" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=208, version=0)
class Microsoft_Windows_AppModel_Exec_208_0(Etw):
    pattern = Struct(
        "PsmKey" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=209, version=0)
class Microsoft_Windows_AppModel_Exec_209_0(Etw):
    pattern = Struct(
        "SwapState" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=213, version=0)
class Microsoft_Windows_AppModel_Exec_213_0(Etw):
    pattern = Struct(
        "MemorySize" / Int64ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=214, version=0)
class Microsoft_Windows_AppModel_Exec_214_0(Etw):
    pattern = Struct(
        "MemorySize" / Int64ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=215, version=0)
class Microsoft_Windows_AppModel_Exec_215_0(Etw):
    pattern = Struct(
        "MemorySize" / Int64ul,
        "AppCount" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=216, version=0)
class Microsoft_Windows_AppModel_Exec_216_0(Etw):
    pattern = Struct(
        "MemorySize" / Int64ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=217, version=0)
class Microsoft_Windows_AppModel_Exec_217_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "Exemption" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=218, version=0)
class Microsoft_Windows_AppModel_Exec_218_0(Etw):
    pattern = Struct(
        "PsmKey" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=219, version=0)
class Microsoft_Windows_AppModel_Exec_219_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "Time" / Int64sl
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=220, version=0)
class Microsoft_Windows_AppModel_Exec_220_0(Etw):
    pattern = Struct(
        "PsmKey" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=222, version=0)
class Microsoft_Windows_AppModel_Exec_222_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=223, version=0)
class Microsoft_Windows_AppModel_Exec_223_0(Etw):
    pattern = Struct(
        "MemorySize" / Int64ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=224, version=0)
class Microsoft_Windows_AppModel_Exec_224_0(Etw):
    pattern = Struct(
        "ApplicationCouunt" / Int64ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=225, version=0)
class Microsoft_Windows_AppModel_Exec_225_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "OldPsmKey" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=226, version=0)
class Microsoft_Windows_AppModel_Exec_226_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "MemorySize" / Int64ul,
        "Score" / Int64ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=228, version=0)
class Microsoft_Windows_AppModel_Exec_228_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=229, version=0)
class Microsoft_Windows_AppModel_Exec_229_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "Exemption" / Int32ul,
        "RegistrationRef" / Int32ul,
        "PendingRef" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=230, version=0)
class Microsoft_Windows_AppModel_Exec_230_0(Etw):
    pattern = Struct(
        "Added" / Int8ul,
        "Type" / Int32sl,
        "PsmKey" / WString,
        "Exemption" / Int32ul,
        "RegistrationRef" / Int32ul,
        "PendingRef" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=231, version=0)
class Microsoft_Windows_AppModel_Exec_231_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=232, version=0)
class Microsoft_Windows_AppModel_Exec_232_0(Etw):
    pattern = Struct(
        "PsmKey" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=233, version=0)
class Microsoft_Windows_AppModel_Exec_233_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "Priority" / Int64ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=234, version=0)
class Microsoft_Windows_AppModel_Exec_234_0(Etw):
    pattern = Struct(
        "PackageCount" / Int32ul,
        "Notify" / Int8ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=235, version=0)
class Microsoft_Windows_AppModel_Exec_235_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=236, version=0)
class Microsoft_Windows_AppModel_Exec_236_0(Etw):
    pattern = Struct(
        "PackageCount" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=237, version=0)
class Microsoft_Windows_AppModel_Exec_237_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=238, version=0)
class Microsoft_Windows_AppModel_Exec_238_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=239, version=0)
class Microsoft_Windows_AppModel_Exec_239_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=240, version=0)
class Microsoft_Windows_AppModel_Exec_240_0(Etw):
    pattern = Struct(
        "AUMID" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=241, version=0)
class Microsoft_Windows_AppModel_Exec_241_0(Etw):
    pattern = Struct(
        "ApplicationName" / WString,
        "Echange" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=242, version=0)
class Microsoft_Windows_AppModel_Exec_242_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "State" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=243, version=0)
class Microsoft_Windows_AppModel_Exec_243_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "State" / Int32ul,
        "TerminateAction" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=244, version=0)
class Microsoft_Windows_AppModel_Exec_244_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString,
        "State" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=245, version=0)
class Microsoft_Windows_AppModel_Exec_245_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "Trigger" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=246, version=0)
class Microsoft_Windows_AppModel_Exec_246_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "Trigger" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=247, version=0)
class Microsoft_Windows_AppModel_Exec_247_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "Reason" / Int64sl,
        "SuspendTrigger" / Int32sl
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=248, version=0)
class Microsoft_Windows_AppModel_Exec_248_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "SuspendTrigger" / Int32sl
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=249, version=0)
class Microsoft_Windows_AppModel_Exec_249_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "Timeout" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=250, version=0)
class Microsoft_Windows_AppModel_Exec_250_0(Etw):
    pattern = Struct(
        "PsmKey" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=251, version=0)
class Microsoft_Windows_AppModel_Exec_251_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "ResumeReason" / Int32sl
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=252, version=0)
class Microsoft_Windows_AppModel_Exec_252_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "ResumeReason" / Int32sl,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=253, version=0)
class Microsoft_Windows_AppModel_Exec_253_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "ResumeReason" / Int32sl
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=254, version=0)
class Microsoft_Windows_AppModel_Exec_254_0(Etw):
    pattern = Struct(
        "PsmKey" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=255, version=0)
class Microsoft_Windows_AppModel_Exec_255_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "KernelRequest" / Int32sl,
        "RunawayRpc" / Int8ul,
        "RpcDebounce" / Int8ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=256, version=0)
class Microsoft_Windows_AppModel_Exec_256_0(Etw):
    pattern = Struct(
        "PsmKey" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=257, version=0)
class Microsoft_Windows_AppModel_Exec_257_0(Etw):
    pattern = Struct(
        "AUMID" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=258, version=0)
class Microsoft_Windows_AppModel_Exec_258_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "PreserverProcessRequest" / Int32sl,
        "TaskCompletionCategory" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=259, version=0)
class Microsoft_Windows_AppModel_Exec_259_0(Etw):
    pattern = Struct(
        "fActivate" / Int8ul,
        "Result" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=260, version=0)
class Microsoft_Windows_AppModel_Exec_260_0(Etw):
    pattern = Struct(
        "NetworkAudioEntriesCount" / Int64sl,
        "NetworkingReferenced" / Int8ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=261, version=0)
class Microsoft_Windows_AppModel_Exec_261_0(Etw):
    pattern = Struct(
        "PsmKey" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=262, version=0)
class Microsoft_Windows_AppModel_Exec_262_0(Etw):
    pattern = Struct(
        "Guid" / WString,
        "PsmKey" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=263, version=0)
class Microsoft_Windows_AppModel_Exec_263_0(Etw):
    pattern = Struct(
        "Guid" / WString,
        "PsmKey" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=264, version=0)
class Microsoft_Windows_AppModel_Exec_264_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "Reason" / Int64sl
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=265, version=0)
class Microsoft_Windows_AppModel_Exec_265_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=266, version=0)
class Microsoft_Windows_AppModel_Exec_266_0(Etw):
    pattern = Struct(
        "AUMID" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=267, version=0)
class Microsoft_Windows_AppModel_Exec_267_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=268, version=0)
class Microsoft_Windows_AppModel_Exec_268_0(Etw):
    pattern = Struct(
        "AUMID" / WString,
        "Type" / Int32sl,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=269, version=0)
class Microsoft_Windows_AppModel_Exec_269_0(Etw):
    pattern = Struct(
        "AUMID" / WString,
        "Type" / Int32sl,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=270, version=0)
class Microsoft_Windows_AppModel_Exec_270_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "Type" / Int32sl,
        "NewRelativeExpirationTimer" / Int64ul,
        "ElapsedMs" / Int64ul,
        "CpuRunning" / Int64ul,
        "CpuReady" / Int64ul,
        "IoNormal" / Int64ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=271, version=0)
class Microsoft_Windows_AppModel_Exec_271_0(Etw):
    pattern = Struct(
        "Time" / Int64ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=272, version=0)
class Microsoft_Windows_AppModel_Exec_272_0(Etw):
    pattern = Struct(
        "PsmKey" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=273, version=0)
class Microsoft_Windows_AppModel_Exec_273_0(Etw):
    pattern = Struct(
        "PsmKey" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=274, version=0)
class Microsoft_Windows_AppModel_Exec_274_0(Etw):
    pattern = Struct(
        "PsmKey" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=275, version=0)
class Microsoft_Windows_AppModel_Exec_275_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=276, version=0)
class Microsoft_Windows_AppModel_Exec_276_0(Etw):
    pattern = Struct(
        "AUMID" / WString,
        "Hwnd" / Int64ul,
        "WindowChange" / Int32sl,
        "DeferredVisibility" / Int8ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=280, version=0)
class Microsoft_Windows_AppModel_Exec_280_0(Etw):
    pattern = Struct(
        "AUMID" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=282, version=0)
class Microsoft_Windows_AppModel_Exec_282_0(Etw):
    pattern = Struct(
        "ActivationType" / Int32ul,
        "ApplicationType" / Int32ul,
        "ErrorCode" / Int32ul,
        "Cookie" / Int32sl
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=283, version=0)
class Microsoft_Windows_AppModel_Exec_283_0(Etw):
    pattern = Struct(
        "Cookie" / Int32sl
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=284, version=0)
class Microsoft_Windows_AppModel_Exec_284_0(Etw):
    pattern = Struct(
        "AUMID" / WString,
        "Bool" / Int8ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=285, version=0)
class Microsoft_Windows_AppModel_Exec_285_0(Etw):
    pattern = Struct(
        "AUMID" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=286, version=0)
class Microsoft_Windows_AppModel_Exec_286_0(Etw):
    pattern = Struct(
        "AUMID" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=287, version=0)
class Microsoft_Windows_AppModel_Exec_287_0(Etw):
    pattern = Struct(
        "Aumid" / WString,
        "Reason" / Int64sl,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=289, version=0)
class Microsoft_Windows_AppModel_Exec_289_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=290, version=0)
class Microsoft_Windows_AppModel_Exec_290_0(Etw):
    pattern = Struct(
        "PsmKey" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=291, version=0)
class Microsoft_Windows_AppModel_Exec_291_0(Etw):
    pattern = Struct(
        "Category" / Int32ul,
        "PsmKey" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=292, version=0)
class Microsoft_Windows_AppModel_Exec_292_0(Etw):
    pattern = Struct(
        "Category" / Int32ul,
        "PsmKey" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=293, version=0)
class Microsoft_Windows_AppModel_Exec_293_0(Etw):
    pattern = Struct(
        "PsmKey" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=294, version=0)
class Microsoft_Windows_AppModel_Exec_294_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=295, version=0)
class Microsoft_Windows_AppModel_Exec_295_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=296, version=0)
class Microsoft_Windows_AppModel_Exec_296_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=297, version=0)
class Microsoft_Windows_AppModel_Exec_297_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=298, version=0)
class Microsoft_Windows_AppModel_Exec_298_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=299, version=0)
class Microsoft_Windows_AppModel_Exec_299_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=300, version=0)
class Microsoft_Windows_AppModel_Exec_300_0(Etw):
    pattern = Struct(
        "Hwnd" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=301, version=0)
class Microsoft_Windows_AppModel_Exec_301_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=302, version=0)
class Microsoft_Windows_AppModel_Exec_302_0(Etw):
    pattern = Struct(
        "PsmKey" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=303, version=0)
class Microsoft_Windows_AppModel_Exec_303_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=304, version=0)
class Microsoft_Windows_AppModel_Exec_304_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=305, version=0)
class Microsoft_Windows_AppModel_Exec_305_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=306, version=0)
class Microsoft_Windows_AppModel_Exec_306_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=307, version=0)
class Microsoft_Windows_AppModel_Exec_307_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=308, version=0)
class Microsoft_Windows_AppModel_Exec_308_0(Etw):
    pattern = Struct(
        "PsmKey" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=309, version=0)
class Microsoft_Windows_AppModel_Exec_309_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=310, version=0)
class Microsoft_Windows_AppModel_Exec_310_0(Etw):
    pattern = Struct(
        "PackageFamilyName" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=311, version=0)
class Microsoft_Windows_AppModel_Exec_311_0(Etw):
    pattern = Struct(
        "Priority" / Int32ul,
        "PsmKey" / WString,
        "Status" / Int32sl
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=312, version=0)
class Microsoft_Windows_AppModel_Exec_312_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString,
        "Type" / Int32sl,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=313, version=0)
class Microsoft_Windows_AppModel_Exec_313_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=314, version=0)
class Microsoft_Windows_AppModel_Exec_314_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=315, version=0)
class Microsoft_Windows_AppModel_Exec_315_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=316, version=0)
class Microsoft_Windows_AppModel_Exec_316_0(Etw):
    pattern = Struct(
        "PsmKey" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=317, version=0)
class Microsoft_Windows_AppModel_Exec_317_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=318, version=0)
class Microsoft_Windows_AppModel_Exec_318_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=319, version=0)
class Microsoft_Windows_AppModel_Exec_319_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=320, version=0)
class Microsoft_Windows_AppModel_Exec_320_0(Etw):
    pattern = Struct(
        "ProcessId" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=321, version=0)
class Microsoft_Windows_AppModel_Exec_321_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "SuspendTrigger" / Int32sl,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=322, version=0)
class Microsoft_Windows_AppModel_Exec_322_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "SuspendTrigger" / Int32sl,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=323, version=0)
class Microsoft_Windows_AppModel_Exec_323_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=324, version=0)
class Microsoft_Windows_AppModel_Exec_324_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "SuspendTrigger" / Int32sl
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=325, version=0)
class Microsoft_Windows_AppModel_Exec_325_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=326, version=0)
class Microsoft_Windows_AppModel_Exec_326_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=327, version=0)
class Microsoft_Windows_AppModel_Exec_327_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=328, version=0)
class Microsoft_Windows_AppModel_Exec_328_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=329, version=0)
class Microsoft_Windows_AppModel_Exec_329_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=330, version=0)
class Microsoft_Windows_AppModel_Exec_330_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=331, version=0)
class Microsoft_Windows_AppModel_Exec_331_0(Etw):
    pattern = Struct(
        "Template_PsmkeyCount" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=332, version=0)
class Microsoft_Windows_AppModel_Exec_332_0(Etw):
    pattern = Struct(
        "AUMID" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=333, version=0)
class Microsoft_Windows_AppModel_Exec_333_0(Etw):
    pattern = Struct(
        "AUMID" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=334, version=0)
class Microsoft_Windows_AppModel_Exec_334_0(Etw):
    pattern = Struct(
        "AUMID" / WString,
        "Hwnd" / Int64ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=335, version=0)
class Microsoft_Windows_AppModel_Exec_335_0(Etw):
    pattern = Struct(
        "AUMID" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=336, version=0)
class Microsoft_Windows_AppModel_Exec_336_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=337, version=0)
class Microsoft_Windows_AppModel_Exec_337_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=338, version=0)
class Microsoft_Windows_AppModel_Exec_338_0(Etw):
    pattern = Struct(
        "PsmKey" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=339, version=0)
class Microsoft_Windows_AppModel_Exec_339_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=340, version=0)
class Microsoft_Windows_AppModel_Exec_340_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "Status" / Int32ul,
        "Registered" / Int8ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=341, version=0)
class Microsoft_Windows_AppModel_Exec_341_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=342, version=0)
class Microsoft_Windows_AppModel_Exec_342_0(Etw):
    pattern = Struct(
        "PsmKey" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=343, version=0)
class Microsoft_Windows_AppModel_Exec_343_0(Etw):
    pattern = Struct(
        "Aumid" / WString,
        "State" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=344, version=0)
class Microsoft_Windows_AppModel_Exec_344_0(Etw):
    pattern = Struct(
        "PsmKey" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=345, version=0)
class Microsoft_Windows_AppModel_Exec_345_0(Etw):
    pattern = Struct(
        "Category" / Int32ul,
        "PsmKey" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=347, version=0)
class Microsoft_Windows_AppModel_Exec_347_0(Etw):
    pattern = Struct(
        "PID" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=348, version=0)
class Microsoft_Windows_AppModel_Exec_348_0(Etw):
    pattern = Struct(
        "AUMID" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=349, version=0)
class Microsoft_Windows_AppModel_Exec_349_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=350, version=0)
class Microsoft_Windows_AppModel_Exec_350_0(Etw):
    pattern = Struct(
        "AUMID" / WString,
        "Hwnd" / Int64ul,
        "WindowChange" / Int32sl,
        "DeferredVisibility" / Int8ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=351, version=0)
class Microsoft_Windows_AppModel_Exec_351_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=352, version=0)
class Microsoft_Windows_AppModel_Exec_352_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=353, version=0)
class Microsoft_Windows_AppModel_Exec_353_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=354, version=0)
class Microsoft_Windows_AppModel_Exec_354_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=355, version=0)
class Microsoft_Windows_AppModel_Exec_355_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=356, version=0)
class Microsoft_Windows_AppModel_Exec_356_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=357, version=0)
class Microsoft_Windows_AppModel_Exec_357_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=501, version=0)
class Microsoft_Windows_AppModel_Exec_501_0(Etw):
    pattern = Struct(
        "Message" / Int64ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=502, version=0)
class Microsoft_Windows_AppModel_Exec_502_0(Etw):
    pattern = Struct(
        "Message" / Int64ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=503, version=0)
class Microsoft_Windows_AppModel_Exec_503_0(Etw):
    pattern = Struct(
        "Message" / Int64ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=504, version=0)
class Microsoft_Windows_AppModel_Exec_504_0(Etw):
    pattern = Struct(
        "Message" / Int64ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=505, version=0)
class Microsoft_Windows_AppModel_Exec_505_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "HostJobType" / Int32ul,
        "WorkItemId" / Guid,
        "EntryPoint" / WString,
        "EventType" / Int32ul,
        "ActivationAction" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=506, version=0)
class Microsoft_Windows_AppModel_Exec_506_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "HostJobType" / Int32ul,
        "WorkItemId" / Guid,
        "EntryPoint" / WString,
        "EventType" / Int32ul,
        "ActivationAction" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=507, version=0)
class Microsoft_Windows_AppModel_Exec_507_0(Etw):
    pattern = Struct(
        "WorkItemId" / Guid,
        "TaskInstanceId" / Guid
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=508, version=0)
class Microsoft_Windows_AppModel_Exec_508_0(Etw):
    pattern = Struct(
        "WorkItemId" / Guid,
        "TaskInstanceId" / Guid
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=509, version=0)
class Microsoft_Windows_AppModel_Exec_509_0(Etw):
    pattern = Struct(
        "WorkItemId" / Guid,
        "TaskInstanceId" / Guid
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=510, version=0)
class Microsoft_Windows_AppModel_Exec_510_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "HostJobType" / Int32ul,
        "WorkItemId" / Guid,
        "EventType" / Int32ul,
        "ActivationAction" / Int32ul,
        "WallClockLimitMs" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=511, version=0)
class Microsoft_Windows_AppModel_Exec_511_0(Etw):
    pattern = Struct(
        "WorkItemId" / Guid,
        "TaskInstanceId" / Guid
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=512, version=0)
class Microsoft_Windows_AppModel_Exec_512_0(Etw):
    pattern = Struct(
        "String" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=513, version=0)
class Microsoft_Windows_AppModel_Exec_513_0(Etw):
    pattern = Struct(
        "String" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=514, version=0)
class Microsoft_Windows_AppModel_Exec_514_0(Etw):
    pattern = Struct(
        "WorkItemId" / Guid
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=515, version=0)
class Microsoft_Windows_AppModel_Exec_515_0(Etw):
    pattern = Struct(
        "WorkItemId" / Guid,
        "TaskInstanceId" / Guid
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=516, version=0)
class Microsoft_Windows_AppModel_Exec_516_0(Etw):
    pattern = Struct(
        "CallbackId" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=517, version=0)
class Microsoft_Windows_AppModel_Exec_517_0(Etw):
    pattern = Struct(
        "String" / WString,
        "WorkItemId" / Guid,
        "CallBackId" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=517, version=1)
class Microsoft_Windows_AppModel_Exec_517_1(Etw):
    pattern = Struct(
        "String" / WString,
        "WorkItemId" / Guid,
        "CallBackId" / Int32ul,
        "HRESULT" / Int32ul,
        "HostId" / Int64ul,
        "ResourceSetId" / Int64ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=518, version=0)
class Microsoft_Windows_AppModel_Exec_518_0(Etw):
    pattern = Struct(
        "String" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=518, version=1)
class Microsoft_Windows_AppModel_Exec_518_1(Etw):
    pattern = Struct(
        "String" / WString,
        "HRESULT" / Int32ul,
        "HostId" / Int64ul,
        "ResourceSetId" / Int64ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=519, version=0)
class Microsoft_Windows_AppModel_Exec_519_0(Etw):
    pattern = Struct(
        "ApplicationId" / WString,
        "AppState" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=520, version=0)
class Microsoft_Windows_AppModel_Exec_520_0(Etw):
    pattern = Struct(
        "CallbackId" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=521, version=0)
class Microsoft_Windows_AppModel_Exec_521_0(Etw):
    pattern = Struct(
        "CallbackId" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=522, version=0)
class Microsoft_Windows_AppModel_Exec_522_0(Etw):
    pattern = Struct(
        "WorkItemId" / Guid
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=523, version=0)
class Microsoft_Windows_AppModel_Exec_523_0(Etw):
    pattern = Struct(
        "WorkItemId" / Guid,
        "Status" / Int32sl
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=524, version=0)
class Microsoft_Windows_AppModel_Exec_524_0(Etw):
    pattern = Struct(
        "String" / WString,
        "WorkItemId" / Guid
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=525, version=0)
class Microsoft_Windows_AppModel_Exec_525_0(Etw):
    pattern = Struct(
        "String" / WString,
        "WorkItemId" / Guid,
        "TaskInstanceId" / Guid
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=526, version=0)
class Microsoft_Windows_AppModel_Exec_526_0(Etw):
    pattern = Struct(
        "String" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=527, version=0)
class Microsoft_Windows_AppModel_Exec_527_0(Etw):
    pattern = Struct(
        "String" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=528, version=0)
class Microsoft_Windows_AppModel_Exec_528_0(Etw):
    pattern = Struct(
        "String" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=529, version=0)
class Microsoft_Windows_AppModel_Exec_529_0(Etw):
    pattern = Struct(
        "PolicyCLSID" / Guid,
        "EventType" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=530, version=0)
class Microsoft_Windows_AppModel_Exec_530_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=531, version=0)
class Microsoft_Windows_AppModel_Exec_531_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "HostJobType" / Int32ul,
        "WorkItemId" / Guid,
        "EntryPoint" / WString,
        "EventType" / Int32ul,
        "WallClockLimitMs" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=532, version=0)
class Microsoft_Windows_AppModel_Exec_532_0(Etw):
    pattern = Struct(
        "WorkItemId" / Guid,
        "TaskInstanceId" / Guid
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=533, version=0)
class Microsoft_Windows_AppModel_Exec_533_0(Etw):
    pattern = Struct(
        "WorkItemId" / Guid,
        "TaskInstanceId" / Guid
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=534, version=0)
class Microsoft_Windows_AppModel_Exec_534_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "WorkItemId" / Guid,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=535, version=0)
class Microsoft_Windows_AppModel_Exec_535_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "WorkItemId" / Guid
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=536, version=0)
class Microsoft_Windows_AppModel_Exec_536_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "WorkItemId" / Guid
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=537, version=0)
class Microsoft_Windows_AppModel_Exec_537_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=538, version=0)
class Microsoft_Windows_AppModel_Exec_538_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=539, version=0)
class Microsoft_Windows_AppModel_Exec_539_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "PsmKey" / WString,
        "WorkItemId" / Guid
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=540, version=0)
class Microsoft_Windows_AppModel_Exec_540_0(Etw):
    pattern = Struct(
        "WorkItemId" / Guid,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=541, version=0)
class Microsoft_Windows_AppModel_Exec_541_0(Etw):
    pattern = Struct(
        "WorkItemId" / Guid
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=542, version=0)
class Microsoft_Windows_AppModel_Exec_542_0(Etw):
    pattern = Struct(
        "WorkItemId" / Guid,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=543, version=0)
class Microsoft_Windows_AppModel_Exec_543_0(Etw):
    pattern = Struct(
        "SqmId" / Int32ul,
        "PsmKey" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=544, version=0)
class Microsoft_Windows_AppModel_Exec_544_0(Etw):
    pattern = Struct(
        "SqmId" / Int32ul,
        "PsmKey" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=545, version=0)
class Microsoft_Windows_AppModel_Exec_545_0(Etw):
    pattern = Struct(
        "UserSid" / WString,
        "PsmKey" / WString,
        "WorkItemId" / Guid
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=546, version=0)
class Microsoft_Windows_AppModel_Exec_546_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "UserSid" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=547, version=0)
class Microsoft_Windows_AppModel_Exec_547_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "UserSid" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=548, version=0)
class Microsoft_Windows_AppModel_Exec_548_0(Etw):
    pattern = Struct(
        "WorkItemId" / Guid
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=549, version=0)
class Microsoft_Windows_AppModel_Exec_549_0(Etw):
    pattern = Struct(
        "EvaluationState" / Int32ul,
        "WorkItemId" / Guid
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=551, version=0)
class Microsoft_Windows_AppModel_Exec_551_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "HostJobType" / Int32ul,
        "WorkItemId" / Guid,
        "EventType" / Int32ul,
        "ActivationAction" / Int32ul,
        "WallClockLimitMs" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=552, version=0)
class Microsoft_Windows_AppModel_Exec_552_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=553, version=0)
class Microsoft_Windows_AppModel_Exec_553_0(Etw):
    pattern = Struct(
        "OldState" / Int32ul,
        "NewState" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=554, version=0)
class Microsoft_Windows_AppModel_Exec_554_0(Etw):
    pattern = Struct(
        "OldState" / Int8ul,
        "NewState" / Int8ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=555, version=0)
class Microsoft_Windows_AppModel_Exec_555_0(Etw):
    pattern = Struct(
        "WorkItemId" / Guid
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=556, version=0)
class Microsoft_Windows_AppModel_Exec_556_0(Etw):
    pattern = Struct(
        "WorkItemId" / Guid
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=557, version=0)
class Microsoft_Windows_AppModel_Exec_557_0(Etw):
    pattern = Struct(
        "WorkItemId" / Guid
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=558, version=0)
class Microsoft_Windows_AppModel_Exec_558_0(Etw):
    pattern = Struct(
        "WorkItemId" / Guid
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=559, version=0)
class Microsoft_Windows_AppModel_Exec_559_0(Etw):
    pattern = Struct(
        "WorkItemId" / Guid,
        "PsmKey" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=600, version=0)
class Microsoft_Windows_AppModel_Exec_600_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=601, version=0)
class Microsoft_Windows_AppModel_Exec_601_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul,
        "PluginClsid" / Guid
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=602, version=0)
class Microsoft_Windows_AppModel_Exec_602_0(Etw):
    pattern = Struct(
        "PluginClsid" / Guid
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=603, version=0)
class Microsoft_Windows_AppModel_Exec_603_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=604, version=0)
class Microsoft_Windows_AppModel_Exec_604_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=605, version=0)
class Microsoft_Windows_AppModel_Exec_605_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=700, version=0)
class Microsoft_Windows_AppModel_Exec_700_0(Etw):
    pattern = Struct(
        "Package" / WString,
        "UserSid" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=701, version=0)
class Microsoft_Windows_AppModel_Exec_701_0(Etw):
    pattern = Struct(
        "Package" / WString,
        "UserSid" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=702, version=0)
class Microsoft_Windows_AppModel_Exec_702_0(Etw):
    pattern = Struct(
        "AppUserModelId" / WString,
        "UserSid" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=703, version=0)
class Microsoft_Windows_AppModel_Exec_703_0(Etw):
    pattern = Struct(
        "AppUserModelId" / WString,
        "UserSid" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=704, version=0)
class Microsoft_Windows_AppModel_Exec_704_0(Etw):
    pattern = Struct(
        "Package" / WString,
        "Old_AccessState" / Int32ul,
        "New_AccessState" / Int32ul,
        "UserSid" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=705, version=0)
class Microsoft_Windows_AppModel_Exec_705_0(Etw):
    pattern = Struct(
        "AppUserModelId" / WString,
        "Returned_AccessState" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=706, version=0)
class Microsoft_Windows_AppModel_Exec_706_0(Etw):
    pattern = Struct(
        "AppUserModelId" / WString,
        "Returned_AccessState" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=707, version=0)
class Microsoft_Windows_AppModel_Exec_707_0(Etw):
    pattern = Struct(
        "AppUserModelId" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=708, version=0)
class Microsoft_Windows_AppModel_Exec_708_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=709, version=0)
class Microsoft_Windows_AppModel_Exec_709_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=710, version=0)
class Microsoft_Windows_AppModel_Exec_710_0(Etw):
    pattern = Struct(
        "PackageFullName" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=711, version=0)
class Microsoft_Windows_AppModel_Exec_711_0(Etw):
    pattern = Struct(
        "AppUserModelId" / WString,
        "Requested_AccessKind" / Int32ul,
        "Returned" / Int8ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=750, version=0)
class Microsoft_Windows_AppModel_Exec_750_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=751, version=0)
class Microsoft_Windows_AppModel_Exec_751_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=752, version=0)
class Microsoft_Windows_AppModel_Exec_752_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul,
        "p3_UInt32" / Int32ul,
        "p4_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=753, version=0)
class Microsoft_Windows_AppModel_Exec_753_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=754, version=0)
class Microsoft_Windows_AppModel_Exec_754_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=755, version=0)
class Microsoft_Windows_AppModel_Exec_755_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=756, version=0)
class Microsoft_Windows_AppModel_Exec_756_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=757, version=0)
class Microsoft_Windows_AppModel_Exec_757_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=758, version=0)
class Microsoft_Windows_AppModel_Exec_758_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=761, version=0)
class Microsoft_Windows_AppModel_Exec_761_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=762, version=0)
class Microsoft_Windows_AppModel_Exec_762_0(Etw):
    pattern = Struct(
        "p1_GUID" / Guid,
        "p2_UInt32" / Int32ul,
        "p3_UInt32" / Int32ul,
        "p4_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=763, version=0)
class Microsoft_Windows_AppModel_Exec_763_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=764, version=0)
class Microsoft_Windows_AppModel_Exec_764_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=765, version=0)
class Microsoft_Windows_AppModel_Exec_765_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul,
        "p3_UInt32" / Int32ul,
        "p4_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=766, version=0)
class Microsoft_Windows_AppModel_Exec_766_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=801, version=0)
class Microsoft_Windows_AppModel_Exec_801_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul,
        "p3_UInt32" / Int32ul,
        "p4_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=802, version=0)
class Microsoft_Windows_AppModel_Exec_802_0(Etw):
    pattern = Struct(
        "p1_GUID" / Guid,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=803, version=0)
class Microsoft_Windows_AppModel_Exec_803_0(Etw):
    pattern = Struct(
        "p1_GUID" / Guid
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=804, version=0)
class Microsoft_Windows_AppModel_Exec_804_0(Etw):
    pattern = Struct(
        "p1_GUID" / Guid
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=806, version=0)
class Microsoft_Windows_AppModel_Exec_806_0(Etw):
    pattern = Struct(
        "p1_GUID" / Guid,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=807, version=0)
class Microsoft_Windows_AppModel_Exec_807_0(Etw):
    pattern = Struct(
        "p1_GUID" / Guid
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=808, version=0)
class Microsoft_Windows_AppModel_Exec_808_0(Etw):
    pattern = Struct(
        "p1_GUID" / Guid
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=809, version=0)
class Microsoft_Windows_AppModel_Exec_809_0(Etw):
    pattern = Struct(
        "p1_GUID" / Guid
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=811, version=0)
class Microsoft_Windows_AppModel_Exec_811_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=812, version=0)
class Microsoft_Windows_AppModel_Exec_812_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=813, version=0)
class Microsoft_Windows_AppModel_Exec_813_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=814, version=0)
class Microsoft_Windows_AppModel_Exec_814_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=815, version=0)
class Microsoft_Windows_AppModel_Exec_815_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=816, version=0)
class Microsoft_Windows_AppModel_Exec_816_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=817, version=0)
class Microsoft_Windows_AppModel_Exec_817_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=819, version=0)
class Microsoft_Windows_AppModel_Exec_819_0(Etw):
    pattern = Struct(
        "p1_GUID" / Guid
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=820, version=0)
class Microsoft_Windows_AppModel_Exec_820_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=851, version=0)
class Microsoft_Windows_AppModel_Exec_851_0(Etw):
    pattern = Struct(
        "Message" / Int64ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=852, version=0)
class Microsoft_Windows_AppModel_Exec_852_0(Etw):
    pattern = Struct(
        "Message" / Int64ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=853, version=0)
class Microsoft_Windows_AppModel_Exec_853_0(Etw):
    pattern = Struct(
        "Message" / Int64ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=854, version=0)
class Microsoft_Windows_AppModel_Exec_854_0(Etw):
    pattern = Struct(
        "Message" / Int64ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=861, version=0)
class Microsoft_Windows_AppModel_Exec_861_0(Etw):
    pattern = Struct(
        "p1_UInt64" / Int64ul,
        "p2_String" / WString,
        "p3_String" / WString,
        "p4_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=862, version=0)
class Microsoft_Windows_AppModel_Exec_862_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_String" / WString,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=863, version=0)
class Microsoft_Windows_AppModel_Exec_863_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_String" / WString,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=864, version=0)
class Microsoft_Windows_AppModel_Exec_864_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_String" / WString,
        "p3_Boolean" / Int8ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=865, version=0)
class Microsoft_Windows_AppModel_Exec_865_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_String" / WString,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=866, version=0)
class Microsoft_Windows_AppModel_Exec_866_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_String" / WString,
        "p3_Boolean" / Int8ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=867, version=0)
class Microsoft_Windows_AppModel_Exec_867_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_String" / WString,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=868, version=0)
class Microsoft_Windows_AppModel_Exec_868_0(Etw):
    pattern = Struct(
        "p1_String" / WString,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=869, version=0)
class Microsoft_Windows_AppModel_Exec_869_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_String" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=870, version=0)
class Microsoft_Windows_AppModel_Exec_870_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_String" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=871, version=0)
class Microsoft_Windows_AppModel_Exec_871_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_String" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=872, version=0)
class Microsoft_Windows_AppModel_Exec_872_0(Etw):
    pattern = Struct(
        "user" / Int64ul,
        "ApplicationId" / WString,
        "AppState" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=873, version=0)
class Microsoft_Windows_AppModel_Exec_873_0(Etw):
    pattern = Struct(
        "ActivationId" / Int32ul,
        "ActState" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=874, version=0)
class Microsoft_Windows_AppModel_Exec_874_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt64" / Int64ul,
        "p3_String" / WString,
        "p4_String" / WString,
        "p5_UInt64" / Int64ul,
        "p6_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=875, version=0)
class Microsoft_Windows_AppModel_Exec_875_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=876, version=0)
class Microsoft_Windows_AppModel_Exec_876_0(Etw):
    pattern = Struct(
        "p1_AppLayer" / Int32ul,
        "p2_UInt32" / Int32ul,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=877, version=0)
class Microsoft_Windows_AppModel_Exec_877_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt64" / Int64ul,
        "p3_String" / WString,
        "p4_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=878, version=0)
class Microsoft_Windows_AppModel_Exec_878_0(Etw):
    pattern = Struct(
        "p1_UInt64" / Int64ul,
        "p2_String" / WString,
        "p3_Boolean" / Int8ul,
        "p4_Boolean" / Int8ul,
        "p5_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=879, version=0)
class Microsoft_Windows_AppModel_Exec_879_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt64" / Int64ul,
        "p3_String" / WString,
        "p4_Boolean" / Int8ul,
        "p5_Boolean" / Int8ul,
        "p6_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=880, version=0)
class Microsoft_Windows_AppModel_Exec_880_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_Boolean" / Int8ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=881, version=0)
class Microsoft_Windows_AppModel_Exec_881_0(Etw):
    pattern = Struct(
        "p1_UInt64" / Int64ul,
        "p2_String" / WString,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=882, version=0)
class Microsoft_Windows_AppModel_Exec_882_0(Etw):
    pattern = Struct(
        "p1_UInt64" / Int64ul,
        "p2_String" / WString,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=883, version=0)
class Microsoft_Windows_AppModel_Exec_883_0(Etw):
    pattern = Struct(
        "user" / Int64ul,
        "ApplicationId" / WString,
        "AppState" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=884, version=0)
class Microsoft_Windows_AppModel_Exec_884_0(Etw):
    pattern = Struct(
        "ActivationId" / Int32ul,
        "ActState" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=886, version=0)
class Microsoft_Windows_AppModel_Exec_886_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=887, version=0)
class Microsoft_Windows_AppModel_Exec_887_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=888, version=0)
class Microsoft_Windows_AppModel_Exec_888_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_String" / WString,
        "p3_Boolean" / Int8ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=889, version=0)
class Microsoft_Windows_AppModel_Exec_889_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_String" / WString,
        "p3_String" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=890, version=0)
class Microsoft_Windows_AppModel_Exec_890_0(Etw):
    pattern = Struct(
        "p1_String" / WString,
        "p2_UInt32" / Int32ul,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=891, version=0)
class Microsoft_Windows_AppModel_Exec_891_0(Etw):
    pattern = Struct(
        "ApplicationId" / WString,
        "AppState" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=892, version=0)
class Microsoft_Windows_AppModel_Exec_892_0(Etw):
    pattern = Struct(
        "p1_String" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=893, version=0)
class Microsoft_Windows_AppModel_Exec_893_0(Etw):
    pattern = Struct(
        "p1_String" / WString,
        "p2_String" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=894, version=0)
class Microsoft_Windows_AppModel_Exec_894_0(Etw):
    pattern = Struct(
        "p1_String" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=895, version=0)
class Microsoft_Windows_AppModel_Exec_895_0(Etw):
    pattern = Struct(
        "p1_String" / WString,
        "p2_String" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=896, version=0)
class Microsoft_Windows_AppModel_Exec_896_0(Etw):
    pattern = Struct(
        "p1_String" / WString,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=897, version=0)
class Microsoft_Windows_AppModel_Exec_897_0(Etw):
    pattern = Struct(
        "p1_String" / WString,
        "p2_UInt32" / Int32ul,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=898, version=0)
class Microsoft_Windows_AppModel_Exec_898_0(Etw):
    pattern = Struct(
        "p1_String" / WString,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=900, version=0)
class Microsoft_Windows_AppModel_Exec_900_0(Etw):
    pattern = Struct(
        "p1_UInt64" / Int64ul,
        "p2_String" / WString,
        "p3_String" / WString,
        "p4_Boolean" / Int8ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=901, version=0)
class Microsoft_Windows_AppModel_Exec_901_0(Etw):
    pattern = Struct(
        "p1_UInt64" / Int64ul,
        "p2_String" / WString,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=902, version=0)
class Microsoft_Windows_AppModel_Exec_902_0(Etw):
    pattern = Struct(
        "p1_UInt64" / Int64ul,
        "p2_String" / WString,
        "p3_String" / WString,
        "p4_String" / WString,
        "p5_UInt32" / Int32ul,
        "p6_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=903, version=0)
class Microsoft_Windows_AppModel_Exec_903_0(Etw):
    pattern = Struct(
        "p1_UInt64" / Int64ul,
        "p2_String" / WString,
        "p3_String" / WString,
        "p4_String" / WString,
        "p5_String" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=904, version=0)
class Microsoft_Windows_AppModel_Exec_904_0(Etw):
    pattern = Struct(
        "p1_UInt64" / Int64ul,
        "p2_String" / WString,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=905, version=0)
class Microsoft_Windows_AppModel_Exec_905_0(Etw):
    pattern = Struct(
        "p1_UInt64" / Int64ul,
        "p2_String" / WString,
        "p3_UInt32" / Int32ul,
        "p4_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=906, version=0)
class Microsoft_Windows_AppModel_Exec_906_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt64" / Int64ul,
        "p3_String" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=907, version=0)
class Microsoft_Windows_AppModel_Exec_907_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=908, version=0)
class Microsoft_Windows_AppModel_Exec_908_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt64" / Int64ul,
        "p3_String" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=909, version=0)
class Microsoft_Windows_AppModel_Exec_909_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt64" / Int64ul,
        "p3_String" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=910, version=0)
class Microsoft_Windows_AppModel_Exec_910_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_String" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=911, version=0)
class Microsoft_Windows_AppModel_Exec_911_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_Boolean" / Int8ul,
        "p3_UInt32" / Int32ul,
        "p4_Boolean" / Int8ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=912, version=0)
class Microsoft_Windows_AppModel_Exec_912_0(Etw):
    pattern = Struct(
        "p1_String" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=913, version=0)
class Microsoft_Windows_AppModel_Exec_913_0(Etw):
    pattern = Struct(
        "p1_String" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=914, version=0)
class Microsoft_Windows_AppModel_Exec_914_0(Etw):
    pattern = Struct(
        "p1_String" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=915, version=0)
class Microsoft_Windows_AppModel_Exec_915_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=916, version=0)
class Microsoft_Windows_AppModel_Exec_916_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=917, version=0)
class Microsoft_Windows_AppModel_Exec_917_0(Etw):
    pattern = Struct(
        "p1_String" / WString,
        "p2_Boolean" / Int8ul,
        "p3_UInt32" / Int32ul,
        "p4_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=918, version=0)
class Microsoft_Windows_AppModel_Exec_918_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=919, version=0)
class Microsoft_Windows_AppModel_Exec_919_0(Etw):
    pattern = Struct(
        "p1_UInt64" / Int64ul,
        "p2_String" / WString,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=920, version=0)
class Microsoft_Windows_AppModel_Exec_920_0(Etw):
    pattern = Struct(
        "p1_UInt64" / Int64ul,
        "p2_String" / WString,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=921, version=0)
class Microsoft_Windows_AppModel_Exec_921_0(Etw):
    pattern = Struct(
        "p1_UInt64" / Int64ul,
        "p2_String" / WString,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=922, version=0)
class Microsoft_Windows_AppModel_Exec_922_0(Etw):
    pattern = Struct(
        "p1_UInt64" / Int64ul,
        "p2_String" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=923, version=0)
class Microsoft_Windows_AppModel_Exec_923_0(Etw):
    pattern = Struct(
        "p1_String" / WString,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=925, version=0)
class Microsoft_Windows_AppModel_Exec_925_0(Etw):
    pattern = Struct(
        "p1_UInt64" / Int64ul,
        "p2_String" / WString,
        "p3_Boolean" / Int8ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1051, version=0)
class Microsoft_Windows_AppModel_Exec_1051_0(Etw):
    pattern = Struct(
        "p1_UInt64" / Int64ul,
        "p2_String" / WString,
        "p3_String" / WString,
        "p4_UInt32" / Int32ul,
        "p5_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1052, version=0)
class Microsoft_Windows_AppModel_Exec_1052_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1053, version=0)
class Microsoft_Windows_AppModel_Exec_1053_0(Etw):
    pattern = Struct(
        "p1_UInt64" / Int64ul,
        "p2_String" / WString,
        "p3_String" / WString,
        "p4_UInt32" / Int32ul,
        "p5_Boolean" / Int8ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1054, version=0)
class Microsoft_Windows_AppModel_Exec_1054_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1055, version=0)
class Microsoft_Windows_AppModel_Exec_1055_0(Etw):
    pattern = Struct(
        "p1_String" / WString,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1056, version=0)
class Microsoft_Windows_AppModel_Exec_1056_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int64ul,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1057, version=0)
class Microsoft_Windows_AppModel_Exec_1057_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1058, version=0)
class Microsoft_Windows_AppModel_Exec_1058_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1060, version=0)
class Microsoft_Windows_AppModel_Exec_1060_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1061, version=0)
class Microsoft_Windows_AppModel_Exec_1061_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1062, version=0)
class Microsoft_Windows_AppModel_Exec_1062_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1063, version=0)
class Microsoft_Windows_AppModel_Exec_1063_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1064, version=0)
class Microsoft_Windows_AppModel_Exec_1064_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1065, version=0)
class Microsoft_Windows_AppModel_Exec_1065_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1066, version=0)
class Microsoft_Windows_AppModel_Exec_1066_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1071, version=0)
class Microsoft_Windows_AppModel_Exec_1071_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1072, version=0)
class Microsoft_Windows_AppModel_Exec_1072_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1073, version=0)
class Microsoft_Windows_AppModel_Exec_1073_0(Etw):
    pattern = Struct(
        "p1_String" / WString,
        "p2_String" / WString,
        "p3_UInt32" / Int32ul,
        "p4_activationType" / Guid,
        "p5_UInt32" / Int32ul,
        "p6_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1074, version=0)
class Microsoft_Windows_AppModel_Exec_1074_0(Etw):
    pattern = Struct(
        "p1_String" / WString,
        "p2_UInt32" / Int32ul,
        "p3_UInt32" / Int32ul,
        "p4_UInt32" / Int32ul,
        "p5_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1075, version=0)
class Microsoft_Windows_AppModel_Exec_1075_0(Etw):
    pattern = Struct(
        "p1_String" / WString,
        "p2_UInt32" / Int32ul,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1076, version=0)
class Microsoft_Windows_AppModel_Exec_1076_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul,
        "p3_UInt32" / Int32ul,
        "p4_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1077, version=0)
class Microsoft_Windows_AppModel_Exec_1077_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul,
        "p3_UInt32" / Int32ul,
        "p4_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1078, version=0)
class Microsoft_Windows_AppModel_Exec_1078_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1080, version=0)
class Microsoft_Windows_AppModel_Exec_1080_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1081, version=0)
class Microsoft_Windows_AppModel_Exec_1081_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1082, version=0)
class Microsoft_Windows_AppModel_Exec_1082_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1083, version=0)
class Microsoft_Windows_AppModel_Exec_1083_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1084, version=0)
class Microsoft_Windows_AppModel_Exec_1084_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1085, version=0)
class Microsoft_Windows_AppModel_Exec_1085_0(Etw):
    pattern = Struct(
        "TaskId" / Int32ul,
        "State" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1086, version=0)
class Microsoft_Windows_AppModel_Exec_1086_0(Etw):
    pattern = Struct(
        "TaskId" / Int32ul,
        "State" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1087, version=0)
class Microsoft_Windows_AppModel_Exec_1087_0(Etw):
    pattern = Struct(
        "TaskId" / Int32ul,
        "TaskId_2" / Int32ul,
        "State" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1088, version=0)
class Microsoft_Windows_AppModel_Exec_1088_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1089, version=0)
class Microsoft_Windows_AppModel_Exec_1089_0(Etw):
    pattern = Struct(
        "p1_String" / WString,
        "p2_String" / WString,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1100, version=0)
class Microsoft_Windows_AppModel_Exec_1100_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt64" / Int64ul,
        "p3_String" / WString,
        "pResSet" / Int64ul,
        "p4_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1101, version=0)
class Microsoft_Windows_AppModel_Exec_1101_0(Etw):
    pattern = Struct(
        "UserContext" / Int64ul,
        "PsmKey" / WString,
        "pResSet" / Int64ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1102, version=0)
class Microsoft_Windows_AppModel_Exec_1102_0(Etw):
    pattern = Struct(
        "UserContext" / Int64ul,
        "PsmKey" / WString,
        "pResSet" / Int64ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1103, version=0)
class Microsoft_Windows_AppModel_Exec_1103_0(Etw):
    pattern = Struct(
        "UserContext" / Int64ul,
        "PsmKey" / WString,
        "pResSet" / Int64ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1104, version=0)
class Microsoft_Windows_AppModel_Exec_1104_0(Etw):
    pattern = Struct(
        "p1_UInt64" / Int64ul,
        "p2_String" / WString,
        "p3_UInt32" / Int32ul,
        "p4_Boolean" / Int8ul,
        "p5_Boolean" / Int8ul,
        "p6_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1105, version=0)
class Microsoft_Windows_AppModel_Exec_1105_0(Etw):
    pattern = Struct(
        "UserContext" / Int64ul,
        "PsmKey" / WString,
        "pResSet" / Int64ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1106, version=0)
class Microsoft_Windows_AppModel_Exec_1106_0(Etw):
    pattern = Struct(
        "UserContext" / Int64ul,
        "PsmKey" / WString,
        "pResSet" / Int64ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1107, version=0)
class Microsoft_Windows_AppModel_Exec_1107_0(Etw):
    pattern = Struct(
        "p1_UInt64" / Int64ul,
        "p2_String" / WString,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1108, version=0)
class Microsoft_Windows_AppModel_Exec_1108_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt64" / Int64ul,
        "p3_String" / WString,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1109, version=0)
class Microsoft_Windows_AppModel_Exec_1109_0(Etw):
    pattern = Struct(
        "p1_UInt64" / Int64ul,
        "p2_String" / WString,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1110, version=0)
class Microsoft_Windows_AppModel_Exec_1110_0(Etw):
    pattern = Struct(
        "p1_UInt64" / Int64ul,
        "p2_String" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1111, version=0)
class Microsoft_Windows_AppModel_Exec_1111_0(Etw):
    pattern = Struct(
        "p1_UInt64" / Int64ul,
        "p2_String" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1200, version=0)
class Microsoft_Windows_AppModel_Exec_1200_0(Etw):
    pattern = Struct(
        "UserContext" / Int64ul,
        "ApplicationId" / WString,
        "AppState" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1201, version=0)
class Microsoft_Windows_AppModel_Exec_1201_0(Etw):
    pattern = Struct(
        "p1_UInt64" / Int64ul,
        "p2_String" / WString,
        "p3_Boolean" / Int8ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1202, version=0)
class Microsoft_Windows_AppModel_Exec_1202_0(Etw):
    pattern = Struct(
        "p1_UInt64" / Int64ul,
        "p2_String" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1203, version=0)
class Microsoft_Windows_AppModel_Exec_1203_0(Etw):
    pattern = Struct(
        "p1_UInt64" / Int64ul,
        "p2_String" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1250, version=0)
class Microsoft_Windows_AppModel_Exec_1250_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1251, version=0)
class Microsoft_Windows_AppModel_Exec_1251_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_String" / WString,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1252, version=0)
class Microsoft_Windows_AppModel_Exec_1252_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul,
        "p3_Boolean" / Int8ul,
        "p4_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1253, version=0)
class Microsoft_Windows_AppModel_Exec_1253_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1254, version=0)
class Microsoft_Windows_AppModel_Exec_1254_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1255, version=0)
class Microsoft_Windows_AppModel_Exec_1255_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1256, version=0)
class Microsoft_Windows_AppModel_Exec_1256_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul,
        "p3_UInt32" / Int32ul,
        "p4_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1257, version=0)
class Microsoft_Windows_AppModel_Exec_1257_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul,
        "p3_UInt64" / Int64ul,
        "p4_UInt64" / Int64ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1258, version=0)
class Microsoft_Windows_AppModel_Exec_1258_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_Boolean" / Int8ul,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1259, version=0)
class Microsoft_Windows_AppModel_Exec_1259_0(Etw):
    pattern = Struct(
        "p1_UInt64" / Int64ul,
        "p2_String" / WString,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1260, version=0)
class Microsoft_Windows_AppModel_Exec_1260_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "pResSet" / Int64ul,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1261, version=0)
class Microsoft_Windows_AppModel_Exec_1261_0(Etw):
    pattern = Struct(
        "p0" / WString,
        "p1" / Int8ul,
        "p2" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1262, version=0)
class Microsoft_Windows_AppModel_Exec_1262_0(Etw):
    pattern = Struct(
        "p1_UInt64" / Int64ul,
        "p2_String" / WString,
        "p3_Boolean" / Int8ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1263, version=0)
class Microsoft_Windows_AppModel_Exec_1263_0(Etw):
    pattern = Struct(
        "p1_String" / WString,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1264, version=0)
class Microsoft_Windows_AppModel_Exec_1264_0(Etw):
    pattern = Struct(
        "p1_UInt64" / Int64ul,
        "p2_String" / WString,
        "p3_UInt32" / Int32ul,
        "p4_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1265, version=0)
class Microsoft_Windows_AppModel_Exec_1265_0(Etw):
    pattern = Struct(
        "p1_String" / WString,
        "p2_UInt32" / Int32ul,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1266, version=0)
class Microsoft_Windows_AppModel_Exec_1266_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1267, version=0)
class Microsoft_Windows_AppModel_Exec_1267_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1268, version=0)
class Microsoft_Windows_AppModel_Exec_1268_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1269, version=0)
class Microsoft_Windows_AppModel_Exec_1269_0(Etw):
    pattern = Struct(
        "p0" / WString,
        "p1" / Int32ul,
        "p2" / Int8ul,
        "p3" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1270, version=0)
class Microsoft_Windows_AppModel_Exec_1270_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1271, version=0)
class Microsoft_Windows_AppModel_Exec_1271_0(Etw):
    pattern = Struct(
        "p0" / WString,
        "p1" / Int8ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1400, version=0)
class Microsoft_Windows_AppModel_Exec_1400_0(Etw):
    pattern = Struct(
        "p1_String" / WString,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1401, version=0)
class Microsoft_Windows_AppModel_Exec_1401_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1402, version=0)
class Microsoft_Windows_AppModel_Exec_1402_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt64" / Int64ul,
        "p3_String" / WString,
        "p4_String" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1403, version=0)
class Microsoft_Windows_AppModel_Exec_1403_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_Boolean" / Int8ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1404, version=0)
class Microsoft_Windows_AppModel_Exec_1404_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1405, version=0)
class Microsoft_Windows_AppModel_Exec_1405_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1406, version=0)
class Microsoft_Windows_AppModel_Exec_1406_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_Boolean" / Int8ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1407, version=0)
class Microsoft_Windows_AppModel_Exec_1407_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1408, version=0)
class Microsoft_Windows_AppModel_Exec_1408_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1409, version=0)
class Microsoft_Windows_AppModel_Exec_1409_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1410, version=0)
class Microsoft_Windows_AppModel_Exec_1410_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1411, version=0)
class Microsoft_Windows_AppModel_Exec_1411_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_Boolean" / Int8ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1412, version=0)
class Microsoft_Windows_AppModel_Exec_1412_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1413, version=0)
class Microsoft_Windows_AppModel_Exec_1413_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1414, version=0)
class Microsoft_Windows_AppModel_Exec_1414_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_String" / WString,
        "p3_Boolean" / Int8ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1415, version=0)
class Microsoft_Windows_AppModel_Exec_1415_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1416, version=0)
class Microsoft_Windows_AppModel_Exec_1416_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1417, version=0)
class Microsoft_Windows_AppModel_Exec_1417_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1418, version=0)
class Microsoft_Windows_AppModel_Exec_1418_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_Boolean" / Int8ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1419, version=0)
class Microsoft_Windows_AppModel_Exec_1419_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1420, version=0)
class Microsoft_Windows_AppModel_Exec_1420_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1421, version=0)
class Microsoft_Windows_AppModel_Exec_1421_0(Etw):
    pattern = Struct(
        "ActivationId" / Int32ul,
        "ActState" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1422, version=0)
class Microsoft_Windows_AppModel_Exec_1422_0(Etw):
    pattern = Struct(
        "UserContext" / Int64ul,
        "ApplicationId" / WString,
        "AppState" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1423, version=0)
class Microsoft_Windows_AppModel_Exec_1423_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul,
        "p3_Boolean" / Int8ul,
        "p4_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1424, version=0)
class Microsoft_Windows_AppModel_Exec_1424_0(Etw):
    pattern = Struct(
        "p1_Boolean" / Int8ul,
        "p2_GUID" / Guid,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1425, version=0)
class Microsoft_Windows_AppModel_Exec_1425_0(Etw):
    pattern = Struct(
        "p1_GUID" / Guid,
        "p2_UInt32" / Int32ul,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1427, version=0)
class Microsoft_Windows_AppModel_Exec_1427_0(Etw):
    pattern = Struct(
        "p1_UInt64" / Int64ul,
        "p2_String" / WString,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1428, version=0)
class Microsoft_Windows_AppModel_Exec_1428_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1429, version=0)
class Microsoft_Windows_AppModel_Exec_1429_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_Boolean" / Int8ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1430, version=0)
class Microsoft_Windows_AppModel_Exec_1430_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_String" / WString,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1431, version=0)
class Microsoft_Windows_AppModel_Exec_1431_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1432, version=0)
class Microsoft_Windows_AppModel_Exec_1432_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1433, version=0)
class Microsoft_Windows_AppModel_Exec_1433_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1434, version=0)
class Microsoft_Windows_AppModel_Exec_1434_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1435, version=0)
class Microsoft_Windows_AppModel_Exec_1435_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_String" / WString,
        "p3_String" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1436, version=0)
class Microsoft_Windows_AppModel_Exec_1436_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1437, version=0)
class Microsoft_Windows_AppModel_Exec_1437_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1438, version=0)
class Microsoft_Windows_AppModel_Exec_1438_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1439, version=0)
class Microsoft_Windows_AppModel_Exec_1439_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1440, version=0)
class Microsoft_Windows_AppModel_Exec_1440_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1441, version=0)
class Microsoft_Windows_AppModel_Exec_1441_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1442, version=0)
class Microsoft_Windows_AppModel_Exec_1442_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1443, version=0)
class Microsoft_Windows_AppModel_Exec_1443_0(Etw):
    pattern = Struct(
        "p1_UInt64" / Int64ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1444, version=0)
class Microsoft_Windows_AppModel_Exec_1444_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1445, version=0)
class Microsoft_Windows_AppModel_Exec_1445_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1446, version=0)
class Microsoft_Windows_AppModel_Exec_1446_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1447, version=0)
class Microsoft_Windows_AppModel_Exec_1447_0(Etw):
    pattern = Struct(
        "p1_UInt64" / Int64ul,
        "p2_String" / WString,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1448, version=0)
class Microsoft_Windows_AppModel_Exec_1448_0(Etw):
    pattern = Struct(
        "p1_UInt64" / Int64ul,
        "p2_String" / WString,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=1449, version=0)
class Microsoft_Windows_AppModel_Exec_1449_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=2000, version=0)
class Microsoft_Windows_AppModel_Exec_2000_0(Etw):
    pattern = Struct(
        "WorkItemId" / Guid,
        "PsmKey" / WString,
        "ActivationAction" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=2001, version=0)
class Microsoft_Windows_AppModel_Exec_2001_0(Etw):
    pattern = Struct(
        "p0" / Guid,
        "p1" / WString,
        "p2" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=2002, version=0)
class Microsoft_Windows_AppModel_Exec_2002_0(Etw):
    pattern = Struct(
        "p0" / Guid,
        "p1" / WString,
        "p2" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=2003, version=0)
class Microsoft_Windows_AppModel_Exec_2003_0(Etw):
    pattern = Struct(
        "p0" / Guid,
        "p1" / WString,
        "p2" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=2004, version=0)
class Microsoft_Windows_AppModel_Exec_2004_0(Etw):
    pattern = Struct(
        "p0" / Guid,
        "p1" / WString,
        "p2" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=2005, version=0)
class Microsoft_Windows_AppModel_Exec_2005_0(Etw):
    pattern = Struct(
        "p0" / Guid,
        "p1" / WString,
        "p2" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=2006, version=0)
class Microsoft_Windows_AppModel_Exec_2006_0(Etw):
    pattern = Struct(
        "PID" / Int32ul,
        "PsmKey" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=2007, version=0)
class Microsoft_Windows_AppModel_Exec_2007_0(Etw):
    pattern = Struct(
        "PID" / Int32ul,
        "PsmKey" / WString,
        "TaskEntryPoint" / WString,
        "WnfStateName" / Int64ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=2008, version=0)
class Microsoft_Windows_AppModel_Exec_2008_0(Etw):
    pattern = Struct(
        "PID" / Int32ul,
        "PsmKey" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=2009, version=0)
class Microsoft_Windows_AppModel_Exec_2009_0(Etw):
    pattern = Struct(
        "PID" / Int32ul,
        "PsmKey" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=2010, version=0)
class Microsoft_Windows_AppModel_Exec_2010_0(Etw):
    pattern = Struct(
        "PID" / Int32ul,
        "PsmKey" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=2011, version=0)
class Microsoft_Windows_AppModel_Exec_2011_0(Etw):
    pattern = Struct(
        "PID" / Int32ul,
        "PsmKey" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=2012, version=0)
class Microsoft_Windows_AppModel_Exec_2012_0(Etw):
    pattern = Struct(
        "PID" / Int32ul,
        "PsmKey" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=2013, version=0)
class Microsoft_Windows_AppModel_Exec_2013_0(Etw):
    pattern = Struct(
        "WorkItemId" / Guid,
        "PsmKey" / WString,
        "HRESULT" / Int32ul,
        "InActiveCall" / Int8ul,
        "HasRTCTask" / Int8ul,
        "OnHold" / Int8ul,
        "TaskCompletionApplied" / Int8ul,
        "InForeground" / Int8ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=2014, version=0)
class Microsoft_Windows_AppModel_Exec_2014_0(Etw):
    pattern = Struct(
        "WorkItemId" / Guid,
        "PsmKey" / WString,
        "HRESULT" / Int32ul,
        "InActiveCall" / Int8ul,
        "HasRTCTask" / Int8ul,
        "OnHold" / Int8ul,
        "TaskCompletionApplied" / Int8ul,
        "InForeground" / Int8ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=2015, version=0)
class Microsoft_Windows_AppModel_Exec_2015_0(Etw):
    pattern = Struct(
        "WorkItemId" / Guid,
        "PsmKey" / WString,
        "HRESULT" / Int32ul,
        "InActiveCall" / Int8ul,
        "HasRTCTask" / Int8ul,
        "OnHold" / Int8ul,
        "TaskCompletionApplied" / Int8ul,
        "InForeground" / Int8ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=2016, version=0)
class Microsoft_Windows_AppModel_Exec_2016_0(Etw):
    pattern = Struct(
        "WorkItemId" / Guid,
        "PsmKey" / WString,
        "HRESULT" / Int32ul,
        "InActiveCall" / Int8ul,
        "HasRTCTask" / Int8ul,
        "OnHold" / Int8ul,
        "TaskCompletionApplied" / Int8ul,
        "InForeground" / Int8ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=2017, version=0)
class Microsoft_Windows_AppModel_Exec_2017_0(Etw):
    pattern = Struct(
        "WorkItemId" / Guid,
        "PsmKey" / WString,
        "HRESULT" / Int32ul,
        "InActiveCall" / Int8ul,
        "HasRTCTask" / Int8ul,
        "OnHold" / Int8ul,
        "TaskCompletionApplied" / Int8ul,
        "InForeground" / Int8ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=2018, version=0)
class Microsoft_Windows_AppModel_Exec_2018_0(Etw):
    pattern = Struct(
        "WorkItemId" / Guid,
        "PsmKey" / WString,
        "HRESULT" / Int32ul,
        "InActiveCall" / Int8ul,
        "HasRTCTask" / Int8ul,
        "OnHold" / Int8ul,
        "TaskCompletionApplied" / Int8ul,
        "InForeground" / Int8ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=2019, version=0)
class Microsoft_Windows_AppModel_Exec_2019_0(Etw):
    pattern = Struct(
        "WorkItemId" / Guid,
        "PsmKey" / WString,
        "HRESULT" / Int32ul,
        "InActiveCall" / Int8ul,
        "HasRTCTask" / Int8ul,
        "OnHold" / Int8ul,
        "TaskCompletionApplied" / Int8ul,
        "InForeground" / Int8ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=2020, version=0)
class Microsoft_Windows_AppModel_Exec_2020_0(Etw):
    pattern = Struct(
        "WorkItemId" / Guid,
        "PsmKey" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=2021, version=0)
class Microsoft_Windows_AppModel_Exec_2021_0(Etw):
    pattern = Struct(
        "WorkItemId" / Guid,
        "PsmKey" / WString,
        "ActivationAction" / Int8ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=2022, version=0)
class Microsoft_Windows_AppModel_Exec_2022_0(Etw):
    pattern = Struct(
        "WorkItemId" / Guid,
        "PsmKey" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=2023, version=0)
class Microsoft_Windows_AppModel_Exec_2023_0(Etw):
    pattern = Struct(
        "WorkItemId" / Guid,
        "PsmKey" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=2024, version=0)
class Microsoft_Windows_AppModel_Exec_2024_0(Etw):
    pattern = Struct(
        "WorkItemId" / Guid,
        "PsmKey" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=2025, version=0)
class Microsoft_Windows_AppModel_Exec_2025_0(Etw):
    pattern = Struct(
        "WorkItemId" / Guid,
        "PsmKey" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=2026, version=0)
class Microsoft_Windows_AppModel_Exec_2026_0(Etw):
    pattern = Struct(
        "WorkItemId" / Guid,
        "PsmKey" / WString,
        "HRESULT" / Int32ul,
        "InActiveCall" / Int8ul,
        "HasRTCTask" / Int8ul,
        "OnHold" / Int8ul,
        "TaskCompletionApplied" / Int8ul,
        "InForeground" / Int8ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=2027, version=0)
class Microsoft_Windows_AppModel_Exec_2027_0(Etw):
    pattern = Struct(
        "WorkItemId" / Guid,
        "PsmKey" / WString,
        "HRESULT" / Int32ul,
        "InActiveCall" / Int8ul,
        "HasRTCTask" / Int8ul,
        "OnHold" / Int8ul,
        "TaskCompletionApplied" / Int8ul,
        "InForeground" / Int8ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=2028, version=0)
class Microsoft_Windows_AppModel_Exec_2028_0(Etw):
    pattern = Struct(
        "WorkItemId" / Guid,
        "PsmKey" / WString,
        "HRESULT" / Int32ul,
        "InActiveCall" / Int8ul,
        "HasRTCTask" / Int8ul,
        "OnHold" / Int8ul,
        "TaskCompletionApplied" / Int8ul,
        "InForeground" / Int8ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=2029, version=0)
class Microsoft_Windows_AppModel_Exec_2029_0(Etw):
    pattern = Struct(
        "WorkItemId" / Guid,
        "PsmKey" / WString,
        "HRESULT" / Int32ul,
        "InActiveCall" / Int8ul,
        "HasRTCTask" / Int8ul,
        "OnHold" / Int8ul,
        "TaskCompletionApplied" / Int8ul,
        "InForeground" / Int8ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=2030, version=0)
class Microsoft_Windows_AppModel_Exec_2030_0(Etw):
    pattern = Struct(
        "PID" / Int32ul,
        "PsmKey" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3201, version=0)
class Microsoft_Windows_AppModel_Exec_3201_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3202, version=0)
class Microsoft_Windows_AppModel_Exec_3202_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3203, version=0)
class Microsoft_Windows_AppModel_Exec_3203_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3204, version=0)
class Microsoft_Windows_AppModel_Exec_3204_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3206, version=0)
class Microsoft_Windows_AppModel_Exec_3206_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3207, version=0)
class Microsoft_Windows_AppModel_Exec_3207_0(Etw):
    pattern = Struct(
        "p1_String" / WString,
        "p2_String" / WString,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3208, version=0)
class Microsoft_Windows_AppModel_Exec_3208_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3210, version=0)
class Microsoft_Windows_AppModel_Exec_3210_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3211, version=0)
class Microsoft_Windows_AppModel_Exec_3211_0(Etw):
    pattern = Struct(
        "skuId" / Guid,
        "productId" / Guid,
        "taskInstanceId" / Int32ul,
        "taskType" / Int32ul,
        "newState" / Int32ul,
        "reasonForStateChange" / Int32ul,
        "duration" / Int64ul,
        "peak" / Int64ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3215, version=0)
class Microsoft_Windows_AppModel_Exec_3215_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3216, version=0)
class Microsoft_Windows_AppModel_Exec_3216_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3217, version=0)
class Microsoft_Windows_AppModel_Exec_3217_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3218, version=0)
class Microsoft_Windows_AppModel_Exec_3218_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3219, version=0)
class Microsoft_Windows_AppModel_Exec_3219_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3220, version=0)
class Microsoft_Windows_AppModel_Exec_3220_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3221, version=0)
class Microsoft_Windows_AppModel_Exec_3221_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3222, version=0)
class Microsoft_Windows_AppModel_Exec_3222_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3223, version=0)
class Microsoft_Windows_AppModel_Exec_3223_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3224, version=0)
class Microsoft_Windows_AppModel_Exec_3224_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3225, version=0)
class Microsoft_Windows_AppModel_Exec_3225_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3226, version=0)
class Microsoft_Windows_AppModel_Exec_3226_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3230, version=0)
class Microsoft_Windows_AppModel_Exec_3230_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3240, version=0)
class Microsoft_Windows_AppModel_Exec_3240_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul,
        "p3_UInt32" / Int32ul,
        "p4_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3241, version=0)
class Microsoft_Windows_AppModel_Exec_3241_0(Etw):
    pattern = Struct(
        "p1_GUID" / Guid
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3242, version=0)
class Microsoft_Windows_AppModel_Exec_3242_0(Etw):
    pattern = Struct(
        "p1_GUID" / Guid
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3243, version=0)
class Microsoft_Windows_AppModel_Exec_3243_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3244, version=0)
class Microsoft_Windows_AppModel_Exec_3244_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3300, version=0)
class Microsoft_Windows_AppModel_Exec_3300_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3301, version=0)
class Microsoft_Windows_AppModel_Exec_3301_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3302, version=0)
class Microsoft_Windows_AppModel_Exec_3302_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3304, version=0)
class Microsoft_Windows_AppModel_Exec_3304_0(Etw):
    pattern = Struct(
        "p1_GUID" / Guid,
        "p2_UInt32" / Int32ul,
        "p3_UInt32" / Int32ul,
        "p4_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3305, version=0)
class Microsoft_Windows_AppModel_Exec_3305_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3306, version=0)
class Microsoft_Windows_AppModel_Exec_3306_0(Etw):
    pattern = Struct(
        "p1_Boolean" / Int8ul,
        "p2_GUID" / Guid,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3307, version=0)
class Microsoft_Windows_AppModel_Exec_3307_0(Etw):
    pattern = Struct(
        "p1_GUID" / Guid,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3308, version=0)
class Microsoft_Windows_AppModel_Exec_3308_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul,
        "p3_UInt32" / Int32ul,
        "p4_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3309, version=0)
class Microsoft_Windows_AppModel_Exec_3309_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3310, version=0)
class Microsoft_Windows_AppModel_Exec_3310_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3311, version=0)
class Microsoft_Windows_AppModel_Exec_3311_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3312, version=0)
class Microsoft_Windows_AppModel_Exec_3312_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3313, version=0)
class Microsoft_Windows_AppModel_Exec_3313_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3314, version=0)
class Microsoft_Windows_AppModel_Exec_3314_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3315, version=0)
class Microsoft_Windows_AppModel_Exec_3315_0(Etw):
    pattern = Struct(
        "p1_String" / WString,
        "p2_UInt32" / Int32ul,
        "p3_UInt32" / Int32ul,
        "p4_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3316, version=0)
class Microsoft_Windows_AppModel_Exec_3316_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3317, version=0)
class Microsoft_Windows_AppModel_Exec_3317_0(Etw):
    pattern = Struct(
        "p1_GUID" / Guid,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3318, version=0)
class Microsoft_Windows_AppModel_Exec_3318_0(Etw):
    pattern = Struct(
        "p1_GUID" / Guid,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3319, version=0)
class Microsoft_Windows_AppModel_Exec_3319_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3320, version=0)
class Microsoft_Windows_AppModel_Exec_3320_0(Etw):
    pattern = Struct(
        "p1_Boolean" / Int8ul,
        "p2_UInt32" / Int32ul,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3321, version=0)
class Microsoft_Windows_AppModel_Exec_3321_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul,
        "p3_UInt32" / Int32ul,
        "p4_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3322, version=0)
class Microsoft_Windows_AppModel_Exec_3322_0(Etw):
    pattern = Struct(
        "p1_Boolean" / Int8ul,
        "p2_UInt32" / Int32ul,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3323, version=0)
class Microsoft_Windows_AppModel_Exec_3323_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3324, version=0)
class Microsoft_Windows_AppModel_Exec_3324_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3325, version=0)
class Microsoft_Windows_AppModel_Exec_3325_0(Etw):
    pattern = Struct(
        "p1_GUID" / Guid,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3326, version=0)
class Microsoft_Windows_AppModel_Exec_3326_0(Etw):
    pattern = Struct(
        "p1_GUID" / Guid,
        "p2_UInt32" / Int32ul,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3327, version=0)
class Microsoft_Windows_AppModel_Exec_3327_0(Etw):
    pattern = Struct(
        "p1_GUID" / Guid,
        "p2_UInt32" / Int32ul,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3500, version=0)
class Microsoft_Windows_AppModel_Exec_3500_0(Etw):
    pattern = Struct(
        "p1_GUID" / Guid,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3501, version=0)
class Microsoft_Windows_AppModel_Exec_3501_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3502, version=0)
class Microsoft_Windows_AppModel_Exec_3502_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3503, version=0)
class Microsoft_Windows_AppModel_Exec_3503_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3504, version=0)
class Microsoft_Windows_AppModel_Exec_3504_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3505, version=0)
class Microsoft_Windows_AppModel_Exec_3505_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3506, version=0)
class Microsoft_Windows_AppModel_Exec_3506_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3507, version=0)
class Microsoft_Windows_AppModel_Exec_3507_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3508, version=0)
class Microsoft_Windows_AppModel_Exec_3508_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3509, version=0)
class Microsoft_Windows_AppModel_Exec_3509_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3511, version=0)
class Microsoft_Windows_AppModel_Exec_3511_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3512, version=0)
class Microsoft_Windows_AppModel_Exec_3512_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3513, version=0)
class Microsoft_Windows_AppModel_Exec_3513_0(Etw):
    pattern = Struct(
        "p1_String" / WString,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3514, version=0)
class Microsoft_Windows_AppModel_Exec_3514_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3515, version=0)
class Microsoft_Windows_AppModel_Exec_3515_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3516, version=0)
class Microsoft_Windows_AppModel_Exec_3516_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3517, version=0)
class Microsoft_Windows_AppModel_Exec_3517_0(Etw):
    pattern = Struct(
        "p1_String" / WString,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3518, version=0)
class Microsoft_Windows_AppModel_Exec_3518_0(Etw):
    pattern = Struct(
        "p1_String" / WString,
        "p2_UInt32" / Int32ul,
        "p3_UInt32" / Int32ul,
        "p4_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3519, version=0)
class Microsoft_Windows_AppModel_Exec_3519_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3520, version=0)
class Microsoft_Windows_AppModel_Exec_3520_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3521, version=0)
class Microsoft_Windows_AppModel_Exec_3521_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_Boolean" / Int8ul,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3522, version=0)
class Microsoft_Windows_AppModel_Exec_3522_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3523, version=0)
class Microsoft_Windows_AppModel_Exec_3523_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3524, version=0)
class Microsoft_Windows_AppModel_Exec_3524_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3525, version=0)
class Microsoft_Windows_AppModel_Exec_3525_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_String" / WString,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3526, version=0)
class Microsoft_Windows_AppModel_Exec_3526_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3527, version=0)
class Microsoft_Windows_AppModel_Exec_3527_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3528, version=0)
class Microsoft_Windows_AppModel_Exec_3528_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3529, version=0)
class Microsoft_Windows_AppModel_Exec_3529_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3530, version=0)
class Microsoft_Windows_AppModel_Exec_3530_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3531, version=0)
class Microsoft_Windows_AppModel_Exec_3531_0(Etw):
    pattern = Struct(
        "p1_GUID" / Guid
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3533, version=0)
class Microsoft_Windows_AppModel_Exec_3533_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3534, version=0)
class Microsoft_Windows_AppModel_Exec_3534_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3535, version=0)
class Microsoft_Windows_AppModel_Exec_3535_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3536, version=0)
class Microsoft_Windows_AppModel_Exec_3536_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3537, version=0)
class Microsoft_Windows_AppModel_Exec_3537_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3538, version=0)
class Microsoft_Windows_AppModel_Exec_3538_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3539, version=0)
class Microsoft_Windows_AppModel_Exec_3539_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3540, version=0)
class Microsoft_Windows_AppModel_Exec_3540_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3541, version=0)
class Microsoft_Windows_AppModel_Exec_3541_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul,
        "p3_UInt32" / Int32ul,
        "p4_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3542, version=0)
class Microsoft_Windows_AppModel_Exec_3542_0(Etw):
    pattern = Struct(
        "p1_GUID" / Guid,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3543, version=0)
class Microsoft_Windows_AppModel_Exec_3543_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul,
        "p3_Boolean" / Int8ul,
        "p4_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3544, version=0)
class Microsoft_Windows_AppModel_Exec_3544_0(Etw):
    pattern = Struct(
        "p1_GUID" / Guid,
        "p2_UInt32" / Int32ul,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3545, version=0)
class Microsoft_Windows_AppModel_Exec_3545_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3546, version=0)
class Microsoft_Windows_AppModel_Exec_3546_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3547, version=0)
class Microsoft_Windows_AppModel_Exec_3547_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3548, version=0)
class Microsoft_Windows_AppModel_Exec_3548_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3549, version=0)
class Microsoft_Windows_AppModel_Exec_3549_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3550, version=0)
class Microsoft_Windows_AppModel_Exec_3550_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3551, version=0)
class Microsoft_Windows_AppModel_Exec_3551_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3552, version=0)
class Microsoft_Windows_AppModel_Exec_3552_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3553, version=0)
class Microsoft_Windows_AppModel_Exec_3553_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3554, version=0)
class Microsoft_Windows_AppModel_Exec_3554_0(Etw):
    pattern = Struct(
        "p1_Boolean" / Int8ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3650, version=0)
class Microsoft_Windows_AppModel_Exec_3650_0(Etw):
    pattern = Struct(
        "p1_GUID" / Guid,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3651, version=0)
class Microsoft_Windows_AppModel_Exec_3651_0(Etw):
    pattern = Struct(
        "p1_GUID" / Guid
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3652, version=0)
class Microsoft_Windows_AppModel_Exec_3652_0(Etw):
    pattern = Struct(
        "p1_GUID" / Guid
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3653, version=0)
class Microsoft_Windows_AppModel_Exec_3653_0(Etw):
    pattern = Struct(
        "p1_GUID" / Guid
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3654, version=0)
class Microsoft_Windows_AppModel_Exec_3654_0(Etw):
    pattern = Struct(
        "p1_String" / WString,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3655, version=0)
class Microsoft_Windows_AppModel_Exec_3655_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3661, version=0)
class Microsoft_Windows_AppModel_Exec_3661_0(Etw):
    pattern = Struct(
        "p1_GUID" / Guid
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3662, version=0)
class Microsoft_Windows_AppModel_Exec_3662_0(Etw):
    pattern = Struct(
        "p1_GUID" / Guid
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3663, version=0)
class Microsoft_Windows_AppModel_Exec_3663_0(Etw):
    pattern = Struct(
        "p1_GUID" / Guid
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3664, version=0)
class Microsoft_Windows_AppModel_Exec_3664_0(Etw):
    pattern = Struct(
        "p1_GUID" / Guid
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3665, version=0)
class Microsoft_Windows_AppModel_Exec_3665_0(Etw):
    pattern = Struct(
        "p1_GUID" / Guid
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3666, version=0)
class Microsoft_Windows_AppModel_Exec_3666_0(Etw):
    pattern = Struct(
        "p1_GUID" / Guid
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3667, version=0)
class Microsoft_Windows_AppModel_Exec_3667_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_GUID" / Guid
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3668, version=0)
class Microsoft_Windows_AppModel_Exec_3668_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul,
        "p3_UInt32" / Int32ul,
        "p4_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3669, version=0)
class Microsoft_Windows_AppModel_Exec_3669_0(Etw):
    pattern = Struct(
        "p1_GUID" / Guid,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3670, version=0)
class Microsoft_Windows_AppModel_Exec_3670_0(Etw):
    pattern = Struct(
        "p1_GUID" / Guid,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3671, version=0)
class Microsoft_Windows_AppModel_Exec_3671_0(Etw):
    pattern = Struct(
        "p1_GUID" / Guid,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3672, version=0)
class Microsoft_Windows_AppModel_Exec_3672_0(Etw):
    pattern = Struct(
        "p1_GUID" / Guid
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3673, version=0)
class Microsoft_Windows_AppModel_Exec_3673_0(Etw):
    pattern = Struct(
        "p1_GUID" / Guid
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3674, version=0)
class Microsoft_Windows_AppModel_Exec_3674_0(Etw):
    pattern = Struct(
        "p1_GUID" / Guid
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3675, version=0)
class Microsoft_Windows_AppModel_Exec_3675_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3676, version=0)
class Microsoft_Windows_AppModel_Exec_3676_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3677, version=0)
class Microsoft_Windows_AppModel_Exec_3677_0(Etw):
    pattern = Struct(
        "p1_Boolean" / Int8ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3678, version=0)
class Microsoft_Windows_AppModel_Exec_3678_0(Etw):
    pattern = Struct(
        "p1_Boolean" / Int8ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3679, version=0)
class Microsoft_Windows_AppModel_Exec_3679_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3680, version=0)
class Microsoft_Windows_AppModel_Exec_3680_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3681, version=0)
class Microsoft_Windows_AppModel_Exec_3681_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3683, version=0)
class Microsoft_Windows_AppModel_Exec_3683_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3684, version=0)
class Microsoft_Windows_AppModel_Exec_3684_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3685, version=0)
class Microsoft_Windows_AppModel_Exec_3685_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3686, version=0)
class Microsoft_Windows_AppModel_Exec_3686_0(Etw):
    pattern = Struct(
        "p1_GUID" / Guid,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3687, version=0)
class Microsoft_Windows_AppModel_Exec_3687_0(Etw):
    pattern = Struct(
        "p1_GUID" / Guid
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3688, version=0)
class Microsoft_Windows_AppModel_Exec_3688_0(Etw):
    pattern = Struct(
        "p1_GUID" / Guid
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3689, version=0)
class Microsoft_Windows_AppModel_Exec_3689_0(Etw):
    pattern = Struct(
        "p1_GUID" / Guid
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3690, version=0)
class Microsoft_Windows_AppModel_Exec_3690_0(Etw):
    pattern = Struct(
        "p1_GUID" / Guid,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3691, version=0)
class Microsoft_Windows_AppModel_Exec_3691_0(Etw):
    pattern = Struct(
        "p1_GUID" / Guid,
        "p2_UInt32" / Int32ul,
        "p3_UInt32" / Int32ul,
        "p4_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3692, version=0)
class Microsoft_Windows_AppModel_Exec_3692_0(Etw):
    pattern = Struct(
        "p1_GUID" / Guid,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3693, version=0)
class Microsoft_Windows_AppModel_Exec_3693_0(Etw):
    pattern = Struct(
        "p1_GUID" / Guid,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3694, version=0)
class Microsoft_Windows_AppModel_Exec_3694_0(Etw):
    pattern = Struct(
        "p1_GUID" / Guid,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=3699, version=0)
class Microsoft_Windows_AppModel_Exec_3699_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6100, version=0)
class Microsoft_Windows_AppModel_Exec_6100_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / WString,
        "p2" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6101, version=0)
class Microsoft_Windows_AppModel_Exec_6101_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / WString,
        "p2" / Int32ul,
        "p3" / Int8ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6102, version=0)
class Microsoft_Windows_AppModel_Exec_6102_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6103, version=0)
class Microsoft_Windows_AppModel_Exec_6103_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / WString,
        "p2" / WString,
        "p3" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6104, version=0)
class Microsoft_Windows_AppModel_Exec_6104_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6105, version=0)
class Microsoft_Windows_AppModel_Exec_6105_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6106, version=0)
class Microsoft_Windows_AppModel_Exec_6106_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6107, version=0)
class Microsoft_Windows_AppModel_Exec_6107_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6108, version=0)
class Microsoft_Windows_AppModel_Exec_6108_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6109, version=0)
class Microsoft_Windows_AppModel_Exec_6109_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6110, version=0)
class Microsoft_Windows_AppModel_Exec_6110_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6111, version=0)
class Microsoft_Windows_AppModel_Exec_6111_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6112, version=0)
class Microsoft_Windows_AppModel_Exec_6112_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6113, version=0)
class Microsoft_Windows_AppModel_Exec_6113_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6114, version=0)
class Microsoft_Windows_AppModel_Exec_6114_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6115, version=0)
class Microsoft_Windows_AppModel_Exec_6115_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul,
        "p2" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6116, version=0)
class Microsoft_Windows_AppModel_Exec_6116_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6117, version=0)
class Microsoft_Windows_AppModel_Exec_6117_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6118, version=0)
class Microsoft_Windows_AppModel_Exec_6118_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6119, version=0)
class Microsoft_Windows_AppModel_Exec_6119_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int8ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6120, version=0)
class Microsoft_Windows_AppModel_Exec_6120_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6121, version=0)
class Microsoft_Windows_AppModel_Exec_6121_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6122, version=0)
class Microsoft_Windows_AppModel_Exec_6122_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6123, version=0)
class Microsoft_Windows_AppModel_Exec_6123_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6124, version=0)
class Microsoft_Windows_AppModel_Exec_6124_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6125, version=0)
class Microsoft_Windows_AppModel_Exec_6125_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6126, version=0)
class Microsoft_Windows_AppModel_Exec_6126_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6127, version=0)
class Microsoft_Windows_AppModel_Exec_6127_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6128, version=0)
class Microsoft_Windows_AppModel_Exec_6128_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6129, version=0)
class Microsoft_Windows_AppModel_Exec_6129_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6130, version=0)
class Microsoft_Windows_AppModel_Exec_6130_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6131, version=0)
class Microsoft_Windows_AppModel_Exec_6131_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul,
        "p2" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6132, version=0)
class Microsoft_Windows_AppModel_Exec_6132_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6133, version=0)
class Microsoft_Windows_AppModel_Exec_6133_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6134, version=0)
class Microsoft_Windows_AppModel_Exec_6134_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6135, version=0)
class Microsoft_Windows_AppModel_Exec_6135_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6136, version=0)
class Microsoft_Windows_AppModel_Exec_6136_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / WString,
        "p2" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6137, version=0)
class Microsoft_Windows_AppModel_Exec_6137_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6138, version=0)
class Microsoft_Windows_AppModel_Exec_6138_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / WString,
        "p2" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6139, version=0)
class Microsoft_Windows_AppModel_Exec_6139_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6140, version=0)
class Microsoft_Windows_AppModel_Exec_6140_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6141, version=0)
class Microsoft_Windows_AppModel_Exec_6141_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6142, version=0)
class Microsoft_Windows_AppModel_Exec_6142_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6143, version=0)
class Microsoft_Windows_AppModel_Exec_6143_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6144, version=0)
class Microsoft_Windows_AppModel_Exec_6144_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6145, version=0)
class Microsoft_Windows_AppModel_Exec_6145_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6146, version=0)
class Microsoft_Windows_AppModel_Exec_6146_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6147, version=0)
class Microsoft_Windows_AppModel_Exec_6147_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6148, version=0)
class Microsoft_Windows_AppModel_Exec_6148_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6149, version=0)
class Microsoft_Windows_AppModel_Exec_6149_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6150, version=0)
class Microsoft_Windows_AppModel_Exec_6150_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6151, version=0)
class Microsoft_Windows_AppModel_Exec_6151_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6152, version=0)
class Microsoft_Windows_AppModel_Exec_6152_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6153, version=0)
class Microsoft_Windows_AppModel_Exec_6153_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6154, version=0)
class Microsoft_Windows_AppModel_Exec_6154_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6155, version=0)
class Microsoft_Windows_AppModel_Exec_6155_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6156, version=0)
class Microsoft_Windows_AppModel_Exec_6156_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6157, version=0)
class Microsoft_Windows_AppModel_Exec_6157_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6158, version=0)
class Microsoft_Windows_AppModel_Exec_6158_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6159, version=0)
class Microsoft_Windows_AppModel_Exec_6159_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6160, version=0)
class Microsoft_Windows_AppModel_Exec_6160_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6161, version=0)
class Microsoft_Windows_AppModel_Exec_6161_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6162, version=0)
class Microsoft_Windows_AppModel_Exec_6162_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6163, version=0)
class Microsoft_Windows_AppModel_Exec_6163_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6164, version=0)
class Microsoft_Windows_AppModel_Exec_6164_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6165, version=0)
class Microsoft_Windows_AppModel_Exec_6165_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6166, version=0)
class Microsoft_Windows_AppModel_Exec_6166_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6167, version=0)
class Microsoft_Windows_AppModel_Exec_6167_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6168, version=0)
class Microsoft_Windows_AppModel_Exec_6168_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6169, version=0)
class Microsoft_Windows_AppModel_Exec_6169_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6170, version=0)
class Microsoft_Windows_AppModel_Exec_6170_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6171, version=0)
class Microsoft_Windows_AppModel_Exec_6171_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6172, version=0)
class Microsoft_Windows_AppModel_Exec_6172_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6173, version=0)
class Microsoft_Windows_AppModel_Exec_6173_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6174, version=0)
class Microsoft_Windows_AppModel_Exec_6174_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6175, version=0)
class Microsoft_Windows_AppModel_Exec_6175_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6176, version=0)
class Microsoft_Windows_AppModel_Exec_6176_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6177, version=0)
class Microsoft_Windows_AppModel_Exec_6177_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6178, version=0)
class Microsoft_Windows_AppModel_Exec_6178_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6179, version=0)
class Microsoft_Windows_AppModel_Exec_6179_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6180, version=0)
class Microsoft_Windows_AppModel_Exec_6180_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6181, version=0)
class Microsoft_Windows_AppModel_Exec_6181_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6182, version=0)
class Microsoft_Windows_AppModel_Exec_6182_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6183, version=0)
class Microsoft_Windows_AppModel_Exec_6183_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int8ul,
        "p2" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6184, version=0)
class Microsoft_Windows_AppModel_Exec_6184_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6185, version=0)
class Microsoft_Windows_AppModel_Exec_6185_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6186, version=0)
class Microsoft_Windows_AppModel_Exec_6186_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6187, version=0)
class Microsoft_Windows_AppModel_Exec_6187_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6188, version=0)
class Microsoft_Windows_AppModel_Exec_6188_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6189, version=0)
class Microsoft_Windows_AppModel_Exec_6189_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6190, version=0)
class Microsoft_Windows_AppModel_Exec_6190_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6191, version=0)
class Microsoft_Windows_AppModel_Exec_6191_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul,
        "p2" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6192, version=0)
class Microsoft_Windows_AppModel_Exec_6192_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6193, version=0)
class Microsoft_Windows_AppModel_Exec_6193_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul,
        "p2" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6194, version=0)
class Microsoft_Windows_AppModel_Exec_6194_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6195, version=0)
class Microsoft_Windows_AppModel_Exec_6195_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6196, version=0)
class Microsoft_Windows_AppModel_Exec_6196_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul,
        "p2" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6197, version=0)
class Microsoft_Windows_AppModel_Exec_6197_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul,
        "p2" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6198, version=0)
class Microsoft_Windows_AppModel_Exec_6198_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul,
        "p2" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6199, version=0)
class Microsoft_Windows_AppModel_Exec_6199_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6200, version=0)
class Microsoft_Windows_AppModel_Exec_6200_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6201, version=0)
class Microsoft_Windows_AppModel_Exec_6201_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul,
        "p2" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6202, version=0)
class Microsoft_Windows_AppModel_Exec_6202_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul,
        "p2" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6203, version=0)
class Microsoft_Windows_AppModel_Exec_6203_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul,
        "p2" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6204, version=0)
class Microsoft_Windows_AppModel_Exec_6204_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int8ul,
        "p2" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6205, version=0)
class Microsoft_Windows_AppModel_Exec_6205_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int8ul,
        "p2" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6206, version=0)
class Microsoft_Windows_AppModel_Exec_6206_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6207, version=0)
class Microsoft_Windows_AppModel_Exec_6207_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int8ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6208, version=0)
class Microsoft_Windows_AppModel_Exec_6208_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6209, version=0)
class Microsoft_Windows_AppModel_Exec_6209_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6210, version=0)
class Microsoft_Windows_AppModel_Exec_6210_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6211, version=0)
class Microsoft_Windows_AppModel_Exec_6211_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6212, version=0)
class Microsoft_Windows_AppModel_Exec_6212_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6213, version=0)
class Microsoft_Windows_AppModel_Exec_6213_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6214, version=0)
class Microsoft_Windows_AppModel_Exec_6214_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6215, version=0)
class Microsoft_Windows_AppModel_Exec_6215_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6216, version=0)
class Microsoft_Windows_AppModel_Exec_6216_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6217, version=0)
class Microsoft_Windows_AppModel_Exec_6217_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6218, version=0)
class Microsoft_Windows_AppModel_Exec_6218_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6219, version=0)
class Microsoft_Windows_AppModel_Exec_6219_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6220, version=0)
class Microsoft_Windows_AppModel_Exec_6220_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / WString,
        "p2" / WString,
        "p3" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6221, version=0)
class Microsoft_Windows_AppModel_Exec_6221_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6222, version=0)
class Microsoft_Windows_AppModel_Exec_6222_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6223, version=0)
class Microsoft_Windows_AppModel_Exec_6223_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6224, version=0)
class Microsoft_Windows_AppModel_Exec_6224_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6225, version=0)
class Microsoft_Windows_AppModel_Exec_6225_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6226, version=0)
class Microsoft_Windows_AppModel_Exec_6226_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6227, version=0)
class Microsoft_Windows_AppModel_Exec_6227_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6228, version=0)
class Microsoft_Windows_AppModel_Exec_6228_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6229, version=0)
class Microsoft_Windows_AppModel_Exec_6229_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / WString,
        "p2" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6230, version=0)
class Microsoft_Windows_AppModel_Exec_6230_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul,
        "p2" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6231, version=0)
class Microsoft_Windows_AppModel_Exec_6231_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6232, version=0)
class Microsoft_Windows_AppModel_Exec_6232_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6233, version=0)
class Microsoft_Windows_AppModel_Exec_6233_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6234, version=0)
class Microsoft_Windows_AppModel_Exec_6234_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / WString,
        "p2" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6235, version=0)
class Microsoft_Windows_AppModel_Exec_6235_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / WString,
        "p2" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6236, version=0)
class Microsoft_Windows_AppModel_Exec_6236_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6237, version=0)
class Microsoft_Windows_AppModel_Exec_6237_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6238, version=0)
class Microsoft_Windows_AppModel_Exec_6238_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6239, version=0)
class Microsoft_Windows_AppModel_Exec_6239_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6240, version=0)
class Microsoft_Windows_AppModel_Exec_6240_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / WString,
        "p2" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6241, version=0)
class Microsoft_Windows_AppModel_Exec_6241_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6242, version=0)
class Microsoft_Windows_AppModel_Exec_6242_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6243, version=0)
class Microsoft_Windows_AppModel_Exec_6243_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6244, version=0)
class Microsoft_Windows_AppModel_Exec_6244_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6245, version=0)
class Microsoft_Windows_AppModel_Exec_6245_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6246, version=0)
class Microsoft_Windows_AppModel_Exec_6246_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6247, version=0)
class Microsoft_Windows_AppModel_Exec_6247_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6248, version=0)
class Microsoft_Windows_AppModel_Exec_6248_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6249, version=0)
class Microsoft_Windows_AppModel_Exec_6249_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6250, version=0)
class Microsoft_Windows_AppModel_Exec_6250_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6251, version=0)
class Microsoft_Windows_AppModel_Exec_6251_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6252, version=0)
class Microsoft_Windows_AppModel_Exec_6252_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6253, version=0)
class Microsoft_Windows_AppModel_Exec_6253_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6254, version=0)
class Microsoft_Windows_AppModel_Exec_6254_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6255, version=0)
class Microsoft_Windows_AppModel_Exec_6255_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6256, version=0)
class Microsoft_Windows_AppModel_Exec_6256_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6257, version=0)
class Microsoft_Windows_AppModel_Exec_6257_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6258, version=0)
class Microsoft_Windows_AppModel_Exec_6258_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6259, version=0)
class Microsoft_Windows_AppModel_Exec_6259_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6260, version=0)
class Microsoft_Windows_AppModel_Exec_6260_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6261, version=0)
class Microsoft_Windows_AppModel_Exec_6261_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6262, version=0)
class Microsoft_Windows_AppModel_Exec_6262_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6263, version=0)
class Microsoft_Windows_AppModel_Exec_6263_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6264, version=0)
class Microsoft_Windows_AppModel_Exec_6264_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6265, version=0)
class Microsoft_Windows_AppModel_Exec_6265_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6266, version=0)
class Microsoft_Windows_AppModel_Exec_6266_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6267, version=0)
class Microsoft_Windows_AppModel_Exec_6267_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6268, version=0)
class Microsoft_Windows_AppModel_Exec_6268_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6269, version=0)
class Microsoft_Windows_AppModel_Exec_6269_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6270, version=0)
class Microsoft_Windows_AppModel_Exec_6270_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6271, version=0)
class Microsoft_Windows_AppModel_Exec_6271_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6272, version=0)
class Microsoft_Windows_AppModel_Exec_6272_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6273, version=0)
class Microsoft_Windows_AppModel_Exec_6273_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6274, version=0)
class Microsoft_Windows_AppModel_Exec_6274_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6275, version=0)
class Microsoft_Windows_AppModel_Exec_6275_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6276, version=0)
class Microsoft_Windows_AppModel_Exec_6276_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6277, version=0)
class Microsoft_Windows_AppModel_Exec_6277_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6278, version=0)
class Microsoft_Windows_AppModel_Exec_6278_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6279, version=0)
class Microsoft_Windows_AppModel_Exec_6279_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6280, version=0)
class Microsoft_Windows_AppModel_Exec_6280_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6281, version=0)
class Microsoft_Windows_AppModel_Exec_6281_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6282, version=0)
class Microsoft_Windows_AppModel_Exec_6282_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6283, version=0)
class Microsoft_Windows_AppModel_Exec_6283_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6284, version=0)
class Microsoft_Windows_AppModel_Exec_6284_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6285, version=0)
class Microsoft_Windows_AppModel_Exec_6285_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6286, version=0)
class Microsoft_Windows_AppModel_Exec_6286_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6287, version=0)
class Microsoft_Windows_AppModel_Exec_6287_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6288, version=0)
class Microsoft_Windows_AppModel_Exec_6288_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6289, version=0)
class Microsoft_Windows_AppModel_Exec_6289_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6290, version=0)
class Microsoft_Windows_AppModel_Exec_6290_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6291, version=0)
class Microsoft_Windows_AppModel_Exec_6291_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6292, version=0)
class Microsoft_Windows_AppModel_Exec_6292_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6293, version=0)
class Microsoft_Windows_AppModel_Exec_6293_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul,
        "p2" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6294, version=0)
class Microsoft_Windows_AppModel_Exec_6294_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / WString,
        "p2" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6295, version=0)
class Microsoft_Windows_AppModel_Exec_6295_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6296, version=0)
class Microsoft_Windows_AppModel_Exec_6296_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6297, version=0)
class Microsoft_Windows_AppModel_Exec_6297_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / WString,
        "p2" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6298, version=0)
class Microsoft_Windows_AppModel_Exec_6298_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6299, version=0)
class Microsoft_Windows_AppModel_Exec_6299_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6300, version=0)
class Microsoft_Windows_AppModel_Exec_6300_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int8ul,
        "p2" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6301, version=0)
class Microsoft_Windows_AppModel_Exec_6301_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6302, version=0)
class Microsoft_Windows_AppModel_Exec_6302_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6303, version=0)
class Microsoft_Windows_AppModel_Exec_6303_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / WString,
        "p2" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6304, version=0)
class Microsoft_Windows_AppModel_Exec_6304_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6305, version=0)
class Microsoft_Windows_AppModel_Exec_6305_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6306, version=0)
class Microsoft_Windows_AppModel_Exec_6306_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / WString,
        "p2" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6307, version=0)
class Microsoft_Windows_AppModel_Exec_6307_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / WString,
        "p2" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6308, version=0)
class Microsoft_Windows_AppModel_Exec_6308_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6309, version=0)
class Microsoft_Windows_AppModel_Exec_6309_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6310, version=0)
class Microsoft_Windows_AppModel_Exec_6310_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6311, version=0)
class Microsoft_Windows_AppModel_Exec_6311_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6312, version=0)
class Microsoft_Windows_AppModel_Exec_6312_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6313, version=0)
class Microsoft_Windows_AppModel_Exec_6313_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6314, version=0)
class Microsoft_Windows_AppModel_Exec_6314_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6315, version=0)
class Microsoft_Windows_AppModel_Exec_6315_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6316, version=0)
class Microsoft_Windows_AppModel_Exec_6316_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6317, version=0)
class Microsoft_Windows_AppModel_Exec_6317_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int8ul,
        "p2" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6318, version=0)
class Microsoft_Windows_AppModel_Exec_6318_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6319, version=0)
class Microsoft_Windows_AppModel_Exec_6319_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6320, version=0)
class Microsoft_Windows_AppModel_Exec_6320_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6321, version=0)
class Microsoft_Windows_AppModel_Exec_6321_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6322, version=0)
class Microsoft_Windows_AppModel_Exec_6322_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6323, version=0)
class Microsoft_Windows_AppModel_Exec_6323_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6324, version=0)
class Microsoft_Windows_AppModel_Exec_6324_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6325, version=0)
class Microsoft_Windows_AppModel_Exec_6325_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6326, version=0)
class Microsoft_Windows_AppModel_Exec_6326_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6327, version=0)
class Microsoft_Windows_AppModel_Exec_6327_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6328, version=0)
class Microsoft_Windows_AppModel_Exec_6328_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / WString,
        "p2" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6329, version=0)
class Microsoft_Windows_AppModel_Exec_6329_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6330, version=0)
class Microsoft_Windows_AppModel_Exec_6330_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6331, version=0)
class Microsoft_Windows_AppModel_Exec_6331_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int8ul,
        "p2" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6332, version=0)
class Microsoft_Windows_AppModel_Exec_6332_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6333, version=0)
class Microsoft_Windows_AppModel_Exec_6333_0(Etw):
    pattern = Struct(
        "p0" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6334, version=0)
class Microsoft_Windows_AppModel_Exec_6334_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6335, version=0)
class Microsoft_Windows_AppModel_Exec_6335_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6336, version=0)
class Microsoft_Windows_AppModel_Exec_6336_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / WString,
        "p2" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6337, version=0)
class Microsoft_Windows_AppModel_Exec_6337_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6338, version=0)
class Microsoft_Windows_AppModel_Exec_6338_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6339, version=0)
class Microsoft_Windows_AppModel_Exec_6339_0(Etw):
    pattern = Struct(
        "p0" / Int32ul,
        "p1" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6350, version=0)
class Microsoft_Windows_AppModel_Exec_6350_0(Etw):
    pattern = Struct(
        "CommitTotal" / Int64ul,
        "CommitLimit" / Int64ul,
        "CommitPeak" / Int64ul,
        "PhysicalTotal" / Int64ul,
        "PhysicalAvailable" / Int64ul,
        "SystemCache" / Int64ul,
        "KernelTotal" / Int64ul,
        "KernelPaged" / Int64ul,
        "KernelNonpaged" / Int64ul,
        "PageSize" / Int64ul,
        "HandleCount" / Int64ul,
        "ProcessCount" / Int64ul,
        "ThreadCount" / Int64ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=6351, version=0)
class Microsoft_Windows_AppModel_Exec_6351_0(Etw):
    pattern = Struct(
        "ProcessId" / Int32ul,
        "ProcessName" / WString,
        "ProductID" / Guid,
        "IsForeground" / Int8ul,
        "PageFaultCount" / Int64ul,
        "WorkingSetSize" / Int64ul,
        "PeakWorkingSetSize" / Int64ul,
        "QuotaPeakPagedPoolUsage" / Int64ul,
        "QuotaPagedPoolUsage" / Int64ul,
        "QuotaPeakNonPagedPoolUsage" / Int64ul,
        "QuotaNonPagedPoolUsage" / Int64ul,
        "PagefileUsage" / Int64ul,
        "PeakPagefileUsage" / Int64ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=8100, version=0)
class Microsoft_Windows_AppModel_Exec_8100_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=8101, version=0)
class Microsoft_Windows_AppModel_Exec_8101_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=8102, version=0)
class Microsoft_Windows_AppModel_Exec_8102_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=8103, version=0)
class Microsoft_Windows_AppModel_Exec_8103_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=8104, version=0)
class Microsoft_Windows_AppModel_Exec_8104_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=8105, version=0)
class Microsoft_Windows_AppModel_Exec_8105_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=8106, version=0)
class Microsoft_Windows_AppModel_Exec_8106_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=8107, version=0)
class Microsoft_Windows_AppModel_Exec_8107_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=8108, version=0)
class Microsoft_Windows_AppModel_Exec_8108_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=8110, version=0)
class Microsoft_Windows_AppModel_Exec_8110_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=8111, version=0)
class Microsoft_Windows_AppModel_Exec_8111_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=8112, version=0)
class Microsoft_Windows_AppModel_Exec_8112_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=8113, version=0)
class Microsoft_Windows_AppModel_Exec_8113_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=8114, version=0)
class Microsoft_Windows_AppModel_Exec_8114_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=8115, version=0)
class Microsoft_Windows_AppModel_Exec_8115_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_String" / WString,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=8116, version=0)
class Microsoft_Windows_AppModel_Exec_8116_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=8117, version=0)
class Microsoft_Windows_AppModel_Exec_8117_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_GUID" / Guid,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=8118, version=0)
class Microsoft_Windows_AppModel_Exec_8118_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_String" / WString,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=8119, version=0)
class Microsoft_Windows_AppModel_Exec_8119_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=8120, version=0)
class Microsoft_Windows_AppModel_Exec_8120_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=8121, version=0)
class Microsoft_Windows_AppModel_Exec_8121_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=8122, version=0)
class Microsoft_Windows_AppModel_Exec_8122_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=8123, version=0)
class Microsoft_Windows_AppModel_Exec_8123_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=8124, version=0)
class Microsoft_Windows_AppModel_Exec_8124_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=8125, version=0)
class Microsoft_Windows_AppModel_Exec_8125_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=8126, version=0)
class Microsoft_Windows_AppModel_Exec_8126_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=8200, version=0)
class Microsoft_Windows_AppModel_Exec_8200_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=8201, version=0)
class Microsoft_Windows_AppModel_Exec_8201_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=8202, version=0)
class Microsoft_Windows_AppModel_Exec_8202_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=8203, version=0)
class Microsoft_Windows_AppModel_Exec_8203_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul,
        "p3_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=8204, version=0)
class Microsoft_Windows_AppModel_Exec_8204_0(Etw):
    pattern = Struct(
        "p1_UInt32" / Int32ul,
        "p2_UInt32" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=8300, version=0)
class Microsoft_Windows_AppModel_Exec_8300_0(Etw):
    pattern = Struct(
        "UserSid" / Sid,
        "SessionId" / Int32ul,
        "PackageFullName" / WString,
        "EntryPoint" / WString,
        "WorkItemId" / Guid,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=8301, version=0)
class Microsoft_Windows_AppModel_Exec_8301_0(Etw):
    pattern = Struct(
        "UserSid" / Sid,
        "SessionId" / Int32ul,
        "WorkItemId" / Guid,
        "RudeTerminate" / Int8ul,
        "CancelationReason" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=8302, version=0)
class Microsoft_Windows_AppModel_Exec_8302_0(Etw):
    pattern = Struct(
        "WorkItemId" / Guid,
        "PsmKey" / WString,
        "HostJobType" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=8303, version=0)
class Microsoft_Windows_AppModel_Exec_8303_0(Etw):
    pattern = Struct(
        "WorkItemId" / Guid,
        "TaskInstanceId" / Guid,
        "PsmKey" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=8304, version=0)
class Microsoft_Windows_AppModel_Exec_8304_0(Etw):
    pattern = Struct(
        "WorkItemId" / Guid,
        "TaskInstanceId" / Guid,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=8305, version=0)
class Microsoft_Windows_AppModel_Exec_8305_0(Etw):
    pattern = Struct(
        "WorkItemId" / Guid,
        "TaskInstanceId" / Guid,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=8307, version=0)
class Microsoft_Windows_AppModel_Exec_8307_0(Etw):
    pattern = Struct(
        "p1_GUID" / Guid
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=10000, version=0)
class Microsoft_Windows_AppModel_Exec_10000_0(Etw):
    pattern = Struct(
        "p0" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=10001, version=0)
class Microsoft_Windows_AppModel_Exec_10001_0(Etw):
    pattern = Struct(
        "p1" / WString,
        "p2" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=10002, version=0)
class Microsoft_Windows_AppModel_Exec_10002_0(Etw):
    pattern = Struct(
        "p1_String" / WString
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=10010, version=0)
class Microsoft_Windows_AppModel_Exec_10010_0(Etw):
    pattern = Struct(
        "UserSid" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("eb65a492-86c0-406a-bace-9912d595bd69"), event_id=10011, version=0)
class Microsoft_Windows_AppModel_Exec_10011_0(Etw):
    pattern = Struct(
        "WorkItemId" / Guid,
        "UserSid" / WString,
        "PackageFullName" / WString,
        "EntryPoint" / WString,
        "HRESULT" / Int32ul
    )

