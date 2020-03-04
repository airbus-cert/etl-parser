# -*- coding: utf-8 -*-
"""
Microsoft-Windows-UserDataAccess-UnifiedStore
GUID : 56f519ab-9df6-4345-8491-a4ba21ac825b
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=1, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_1_0(Etw):
    pattern = Struct(
        "P1_HResult" / Int32sl,
        "P2_String" / CString,
        "P3_UInt32" / Int32ul
    )


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=2, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_2_0(Etw):
    pattern = Struct(
        "P1_HResult" / Int32sl,
        "P2_String" / CString,
        "P3_UInt32" / Int32ul
    )


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=50, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_50_0(Etw):
    pattern = Struct(
        "P1_HResult" / Int32sl,
        "P2_String" / CString,
        "P3_UInt32" / Int32ul
    )


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=101, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_101_0(Etw):
    pattern = Struct(
        "P1_HResult" / Int32sl,
        "P2_String" / CString,
        "P3_UInt32" / Int32ul
    )


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=102, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_102_0(Etw):
    pattern = Struct(
        "P1_HResult" / Int32sl,
        "P2_String" / CString,
        "P3_UInt32" / Int32ul
    )


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=1000, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_1000_0(Etw):
    pattern = Struct(
        "Message" / Int64ul
    )


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=2000, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_2000_0(Etw):
    pattern = Struct(
        "Arg1" / Int32ul,
        "Arg2" / Int32ul,
        "Arg3" / Int32ul
    )


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=2001, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_2001_0(Etw):
    pattern = Struct(
        "Prop_Handle" / Int32ul,
        "Prop_INT" / Int32sl
    )


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=2002, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_2002_0(Etw):
    pattern = Struct(
        "Arg1" / WString,
        "Arg2" / Int64ul,
        "Arg3" / Int64ul
    )


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=3001, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_3001_0(Etw):
    pattern = Struct(
        "Prop_UInt64" / Int64ul,
        "Prop_Hex_UInt32" / Int32ul
    )


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=3002, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_3002_0(Etw):
    pattern = Struct(
        "Arg1" / Int32ul,
        "Arg2" / Int32ul,
        "Arg3" / Int32ul
    )


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=3003, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_3003_0(Etw):
    pattern = Struct(
        "Prop_Handle" / Int32ul,
        "Prop_HRESULT" / Int32ul,
        "Prop_UINT" / Int32ul
    )


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=3004, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_3004_0(Etw):
    pattern = Struct(
        "Prop_Handle" / Int32ul,
        "Prop_HRESULT" / Int32ul,
        "Prop_UINT" / Int32ul
    )


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=3005, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_3005_0(Etw):
    pattern = Struct(
        "Prop_Handle" / Int32ul,
        "Prop_HRESULT" / Int32ul,
        "Prop_UINT" / Int32ul
    )


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=3006, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_3006_0(Etw):
    pattern = Struct(
        "Prop_Handle" / Int32ul,
        "Prop_INT" / Int32sl
    )


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=3009, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_3009_0(Etw):
    pattern = Struct(
        "Prop_UInt32" / Int32ul,
        "Prop_Hex_UInt32" / Int32ul
    )


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=3010, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_3010_0(Etw):
    pattern = Struct(
        "Prop_ErrorCode" / Int32ul,
        "Prop_FullKnowledgeSize" / Int32ul,
        "Prop_LoggedKnowledgeSize" / Int32ul,
        "Prop_Knowledge" / Bytes(lambda this: this.Prop_LoggedKnowledgeSize)
    )


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=3011, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_3011_0(Etw):
    pattern = Struct(
        "Prop_UInt32" / Int32ul
    )


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=3012, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_3012_0(Etw):
    pattern = Struct(
        "Prop_UInt32" / Int32ul
    )


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=3013, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_3013_0(Etw):
    pattern = Struct(
        "Prop_Prop1" / Int32ul,
        "Prop_Prop2" / Int32ul
    )


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=3014, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_3014_0(Etw):
    pattern = Struct(
        "Prop_Prop1" / Int32ul,
        "Prop_Prop2" / Int32ul
    )


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=3015, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_3015_0(Etw):
    pattern = Struct(
        "Prop_UInt32" / Int32ul
    )


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=3016, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_3016_0(Etw):
    pattern = Struct(
        "Count" / Int32ul,
        "Array" / Int32ul
    )


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=3017, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_3017_0(Etw):
    pattern = Struct(
        "P1_HResult" / Int32sl
    )


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=3018, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_3018_0(Etw):
    pattern = Struct(
        "Prop_Handle" / Int32ul,
        "Prop_HRESULT" / Int32ul,
        "Prop_UINT" / Int32ul
    )


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=3019, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_3019_0(Etw):
    pattern = Struct(
        "Prop_Handle" / Int32ul,
        "Prop_HRESULT" / Int32ul,
        "Prop_UINT" / Int32ul
    )


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=3021, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_3021_0(Etw):
    pattern = Struct(
        "Prop_UInt32" / Int32ul
    )


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=3022, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_3022_0(Etw):
    pattern = Struct(
        "Prop_Handle" / Int32ul,
        "Prop_HRESULT" / Int32ul,
        "Prop_UINT" / Int32ul
    )


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=3023, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_3023_0(Etw):
    pattern = Struct(
        "Prop_Trace_UnicodeString" / WString
    )


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=3024, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_3024_0(Etw):
    pattern = Struct(
        "Prop_Prop1" / Int32ul,
        "Prop_Prop2" / Int32ul
    )


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=3025, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_3025_0(Etw):
    pattern = Struct(
        "Prop_Prop1" / Int32ul,
        "Prop_Prop2" / Int32ul
    )


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=3026, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_3026_0(Etw):
    pattern = Struct(
        "Prop_Prop1" / Int32ul,
        "Prop_Prop2" / Int32ul
    )


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=3028, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_3028_0(Etw):
    pattern = Struct(
        "Function" / Int64ul
    )


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=3029, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_3029_0(Etw):
    pattern = Struct(
        "Prop_Prop1" / Int32ul,
        "Prop_Prop2" / Int32ul
    )


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=3030, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_3030_0(Etw):
    pattern = Struct(
        "Prop_Prop1" / Int32ul,
        "Prop_Prop2" / Int32ul
    )


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=3031, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_3031_0(Etw):
    pattern = Struct(
        "Prop_Prop1" / Int32ul,
        "Prop_Prop2" / Int32ul
    )


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=3032, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_3032_0(Etw):
    pattern = Struct(
        "Prop_Prop1" / Int32ul,
        "Prop_Prop2" / Int32ul
    )


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=3033, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_3033_0(Etw):
    pattern = Struct(
        "Prop_Prop1" / Int32ul,
        "Prop_Prop2" / Int32ul
    )


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=3034, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_3034_0(Etw):
    pattern = Struct(
        "Prop_Prop" / Int32ul
    )


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=3035, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_3035_0(Etw):
    pattern = Struct(
        "Prop_Prop" / Int32ul
    )


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=3036, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_3036_0(Etw):
    pattern = Struct(
        "Prop_Prop1" / Int32ul,
        "Prop_Prop2" / Int32ul
    )


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=3037, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_3037_0(Etw):
    pattern = Struct(
        "Function" / Int64ul
    )


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=3039, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_3039_0(Etw):
    pattern = Struct(
        "P1_HResult" / Int32sl
    )


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=3040, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_3040_0(Etw):
    pattern = Struct(
        "Prop_Prop" / Int32ul
    )


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=3043, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_3043_0(Etw):
    pattern = Struct(
        "Prop_Prop" / Int32ul
    )


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=3044, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_3044_0(Etw):
    pattern = Struct(
        "Prop_Prop" / Int32ul
    )


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=3045, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_3045_0(Etw):
    pattern = Struct(
        "Prop_Prop1" / Int32ul,
        "Prop_Prop2" / Int32ul
    )


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=3046, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_3046_0(Etw):
    pattern = Struct(
        "Prop_Prop1" / Int32ul,
        "Prop_Prop2" / Int32ul
    )


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=3047, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_3047_0(Etw):
    pattern = Struct(
        "P1_HResult" / Int32sl
    )


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=3048, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_3048_0(Etw):
    pattern = Struct(
        "P1_HResult" / Int32sl
    )


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=3049, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_3049_0(Etw):
    pattern = Struct(
        "Prop_Handle" / Int32ul,
        "Prop_HRESULT" / Int32ul,
        "Prop_UINT" / Int32ul
    )


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=3050, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_3050_0(Etw):
    pattern = Struct(
        "Prop_Prop1" / Int32ul,
        "Prop_Prop2" / Int32ul
    )


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=3051, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_3051_0(Etw):
    pattern = Struct(
        "Prop_Prop1" / Int32ul,
        "Prop_Prop2" / Int32ul
    )


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=3070, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_3070_0(Etw):
    pattern = Struct(
        "Arg1" / Int32ul,
        "Arg2" / Int32ul,
        "Arg3" / Int32ul,
        "Arg4" / Int32ul,
        "Arg5" / Int32ul,
        "Arg6" / Int32ul,
        "Arg7" / Int64ul
    )


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=3071, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_3071_0(Etw):
    pattern = Struct(
        "Arg1" / Int32ul,
        "Arg2" / Int32ul,
        "Arg3" / Int32ul,
        "Arg4" / Int32ul,
        "Arg5" / Int32ul
    )


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=3072, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_3072_0(Etw):
    pattern = Struct(
        "Arg1" / Int32ul,
        "Arg2" / Int32ul,
        "Arg3" / Int8ul
    )


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=3073, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_3073_0(Etw):
    pattern = Struct(
        "Arg1" / Int32ul,
        "Arg2" / Int32ul,
        "Arg3" / Int32ul
    )


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=3074, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_3074_0(Etw):
    pattern = Struct(
        "Arg1" / Int32ul,
        "Arg2" / Int32ul,
        "Arg3" / Int64ul,
        "Arg4" / Int64ul,
        "Arg5" / Int32ul,
        "Arg6" / Int32ul
    )


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=3075, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_3075_0(Etw):
    pattern = Struct(
        "Arg1" / Int32ul,
        "Arg2" / Int32ul,
        "Arg3" / Int32ul
    )


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=3076, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_3076_0(Etw):
    pattern = Struct(
        "Arg1" / Int32ul,
        "Arg2" / Int32ul,
        "Arg3" / Int32ul
    )


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=3077, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_3077_0(Etw):
    pattern = Struct(
        "Arg1" / Int32ul,
        "Arg2" / Int8ul
    )


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=3078, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_3078_0(Etw):
    pattern = Struct(
        "Arg1" / Int32ul,
        "Arg2" / Int32ul,
        "Arg3" / Int32ul,
        "Arg4" / Int32ul
    )


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=3079, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_3079_0(Etw):
    pattern = Struct(
        "Arg1" / Int32ul,
        "Arg2" / Int32ul,
        "Arg3" / Int32ul,
        "Arg4" / Int32ul
    )


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=3080, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_3080_0(Etw):
    pattern = Struct(
        "Arg1" / Int32ul,
        "Arg2" / Int32ul,
        "Arg3" / Int32ul,
        "Arg4" / Int32ul
    )


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=3081, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_3081_0(Etw):
    pattern = Struct(
        "Arg1" / Int32ul,
        "Arg2" / Int32ul,
        "Arg3" / Int32ul
    )


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=3100, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_3100_0(Etw):
    pattern = Struct(
        "Rundown" / Int32ul,
        "Handle" / Int64ul
    )


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=3101, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_3101_0(Etw):
    pattern = Struct(
        "Rundown" / Int32ul,
        "Handle" / Int64ul
    )


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=3110, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_3110_0(Etw):
    pattern = Struct(
        "Prop_Prop" / Int32ul
    )


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=3112, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_3112_0(Etw):
    pattern = Struct(
        "TaskType" / Int32ul
    )


@declare(guid=guid("56f519ab-9df6-4345-8491-a4ba21ac825b"), event_id=3113, version=0)
class Microsoft_Windows_UserDataAccess_UnifiedStore_3113_0(Etw):
    pattern = Struct(
        "Prop_Prop" / Int32ul
    )

