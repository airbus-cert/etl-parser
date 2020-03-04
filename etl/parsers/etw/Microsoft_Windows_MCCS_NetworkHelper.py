# -*- coding: utf-8 -*-
"""
Microsoft-Windows-MCCS-NetworkHelper
GUID : 25b99a4c-2f80-4fcd-982d-69cd1f77badf
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("25b99a4c-2f80-4fcd-982d-69cd1f77badf"), event_id=1, version=0)
class Microsoft_Windows_MCCS_NetworkHelper_1_0(Etw):
    pattern = Struct(
        "P1_HexInt32" / Int32sl,
        "P2_String" / CString,
        "P3_UInt32" / Int32ul
    )


@declare(guid=guid("25b99a4c-2f80-4fcd-982d-69cd1f77badf"), event_id=2, version=0)
class Microsoft_Windows_MCCS_NetworkHelper_2_0(Etw):
    pattern = Struct(
        "P1_HexInt32" / Int32sl,
        "P2_String" / CString,
        "P3_UInt32" / Int32ul
    )


@declare(guid=guid("25b99a4c-2f80-4fcd-982d-69cd1f77badf"), event_id=101, version=0)
class Microsoft_Windows_MCCS_NetworkHelper_101_0(Etw):
    pattern = Struct(
        "P1_UInt32" / Int32ul,
        "P2_UInt32" / Int32ul
    )


@declare(guid=guid("25b99a4c-2f80-4fcd-982d-69cd1f77badf"), event_id=102, version=0)
class Microsoft_Windows_MCCS_NetworkHelper_102_0(Etw):
    pattern = Struct(
        "P1_UInt32" / Int32ul,
        "P2_UInt32" / Int32ul
    )


@declare(guid=guid("25b99a4c-2f80-4fcd-982d-69cd1f77badf"), event_id=103, version=0)
class Microsoft_Windows_MCCS_NetworkHelper_103_0(Etw):
    pattern = Struct(
        "P1_UInt32" / Int32ul,
        "P2_UInt32" / Int32ul,
        "P3_UInt32" / Int32ul
    )


@declare(guid=guid("25b99a4c-2f80-4fcd-982d-69cd1f77badf"), event_id=104, version=0)
class Microsoft_Windows_MCCS_NetworkHelper_104_0(Etw):
    pattern = Struct(
        "P1_UInt32" / Int32ul,
        "P2_UInt32" / Int32ul
    )


@declare(guid=guid("25b99a4c-2f80-4fcd-982d-69cd1f77badf"), event_id=105, version=0)
class Microsoft_Windows_MCCS_NetworkHelper_105_0(Etw):
    pattern = Struct(
        "P1_UInt32" / Int32ul,
        "P2_UInt32" / Int32ul
    )


@declare(guid=guid("25b99a4c-2f80-4fcd-982d-69cd1f77badf"), event_id=106, version=0)
class Microsoft_Windows_MCCS_NetworkHelper_106_0(Etw):
    pattern = Struct(
        "P1_UInt32" / Int32ul,
        "P2_UInt32" / Int32ul
    )


@declare(guid=guid("25b99a4c-2f80-4fcd-982d-69cd1f77badf"), event_id=107, version=0)
class Microsoft_Windows_MCCS_NetworkHelper_107_0(Etw):
    pattern = Struct(
        "P1_UInt32" / Int32ul,
        "P2_UInt32" / Int32ul,
        "P3_UInt32" / Int32ul
    )


@declare(guid=guid("25b99a4c-2f80-4fcd-982d-69cd1f77badf"), event_id=109, version=0)
class Microsoft_Windows_MCCS_NetworkHelper_109_0(Etw):
    pattern = Struct(
        "P1_UInt32" / Int32ul,
        "P2_UInt32" / Int32ul
    )


@declare(guid=guid("25b99a4c-2f80-4fcd-982d-69cd1f77badf"), event_id=110, version=0)
class Microsoft_Windows_MCCS_NetworkHelper_110_0(Etw):
    pattern = Struct(
        "P1_String" / CString,
        "P2_UInt32" / Int32ul,
        "P3_UInt32" / Int32ul
    )


@declare(guid=guid("25b99a4c-2f80-4fcd-982d-69cd1f77badf"), event_id=111, version=0)
class Microsoft_Windows_MCCS_NetworkHelper_111_0(Etw):
    pattern = Struct(
        "P1_UInt32" / Int32sl,
        "P2_String" / WString
    )


@declare(guid=guid("25b99a4c-2f80-4fcd-982d-69cd1f77badf"), event_id=201, version=0)
class Microsoft_Windows_MCCS_NetworkHelper_201_0(Etw):
    pattern = Struct(
        "P1_Boolean" / Int8ul,
        "P2_Int32" / Int32sl
    )


@declare(guid=guid("25b99a4c-2f80-4fcd-982d-69cd1f77badf"), event_id=202, version=0)
class Microsoft_Windows_MCCS_NetworkHelper_202_0(Etw):
    pattern = Struct(
        "P1_String" / WString,
        "P2_Boolean" / Int8ul,
        "P3_String" / WString,
        "P4_Handle" / Int64ul
    )


@declare(guid=guid("25b99a4c-2f80-4fcd-982d-69cd1f77badf"), event_id=203, version=0)
class Microsoft_Windows_MCCS_NetworkHelper_203_0(Etw):
    pattern = Struct(
        "P1_String" / WString
    )


@declare(guid=guid("25b99a4c-2f80-4fcd-982d-69cd1f77badf"), event_id=206, version=0)
class Microsoft_Windows_MCCS_NetworkHelper_206_0(Etw):
    pattern = Struct(
        "P1_String" / WString,
        "P2_Boolean" / Int8ul
    )


@declare(guid=guid("25b99a4c-2f80-4fcd-982d-69cd1f77badf"), event_id=207, version=0)
class Microsoft_Windows_MCCS_NetworkHelper_207_0(Etw):
    pattern = Struct(
        "P1_Int32" / Int32sl
    )


@declare(guid=guid("25b99a4c-2f80-4fcd-982d-69cd1f77badf"), event_id=209, version=0)
class Microsoft_Windows_MCCS_NetworkHelper_209_0(Etw):
    pattern = Struct(
        "Message" / Int64ul
    )


@declare(guid=guid("25b99a4c-2f80-4fcd-982d-69cd1f77badf"), event_id=4005, version=0)
class Microsoft_Windows_MCCS_NetworkHelper_4005_0(Etw):
    pattern = Struct(
        "Prop_ptr" / Int64ul,
        "Prop_ansi" / CString
    )


@declare(guid=guid("25b99a4c-2f80-4fcd-982d-69cd1f77badf"), event_id=4006, version=0)
class Microsoft_Windows_MCCS_NetworkHelper_4006_0(Etw):
    pattern = Struct(
        "Prop_ptr" / Int64ul,
        "Prop_ansi" / CString,
        "Prop_int" / Int32sl
    )


@declare(guid=guid("25b99a4c-2f80-4fcd-982d-69cd1f77badf"), event_id=4007, version=0)
class Microsoft_Windows_MCCS_NetworkHelper_4007_0(Etw):
    pattern = Struct(
        "Prop_ptr" / Int64ul,
        "Prop_ansi" / CString,
        "Prop_hexint" / Int32ul
    )


@declare(guid=guid("25b99a4c-2f80-4fcd-982d-69cd1f77badf"), event_id=4008, version=0)
class Microsoft_Windows_MCCS_NetworkHelper_4008_0(Etw):
    pattern = Struct(
        "Prop_ptr" / Int64ul,
        "Prop_ansi" / CString,
        "Prop_uint" / Int32ul
    )


@declare(guid=guid("25b99a4c-2f80-4fcd-982d-69cd1f77badf"), event_id=4009, version=0)
class Microsoft_Windows_MCCS_NetworkHelper_4009_0(Etw):
    pattern = Struct(
        "Prop_ptr" / Int64ul,
        "Prop_ansi" / CString,
        "Prop_string" / WString
    )


@declare(guid=guid("25b99a4c-2f80-4fcd-982d-69cd1f77badf"), event_id=4010, version=0)
class Microsoft_Windows_MCCS_NetworkHelper_4010_0(Etw):
    pattern = Struct(
        "Prop_ptr" / Int64ul,
        "Prop_uint" / Int32ul
    )


@declare(guid=guid("25b99a4c-2f80-4fcd-982d-69cd1f77badf"), event_id=4020, version=0)
class Microsoft_Windows_MCCS_NetworkHelper_4020_0(Etw):
    pattern = Struct(
        "P1_Int32" / Int32sl
    )


@declare(guid=guid("25b99a4c-2f80-4fcd-982d-69cd1f77badf"), event_id=4021, version=0)
class Microsoft_Windows_MCCS_NetworkHelper_4021_0(Etw):
    pattern = Struct(
        "P1_String" / WString
    )


@declare(guid=guid("25b99a4c-2f80-4fcd-982d-69cd1f77badf"), event_id=4022, version=0)
class Microsoft_Windows_MCCS_NetworkHelper_4022_0(Etw):
    pattern = Struct(
        "Prop_hr" / Int32sl
    )


@declare(guid=guid("25b99a4c-2f80-4fcd-982d-69cd1f77badf"), event_id=4023, version=0)
class Microsoft_Windows_MCCS_NetworkHelper_4023_0(Etw):
    pattern = Struct(
        "Message" / Int64ul
    )


@declare(guid=guid("25b99a4c-2f80-4fcd-982d-69cd1f77badf"), event_id=4025, version=0)
class Microsoft_Windows_MCCS_NetworkHelper_4025_0(Etw):
    pattern = Struct(
        "Prop_string1" / WString,
        "Prop_string2" / WString
    )


@declare(guid=guid("25b99a4c-2f80-4fcd-982d-69cd1f77badf"), event_id=4030, version=0)
class Microsoft_Windows_MCCS_NetworkHelper_4030_0(Etw):
    pattern = Struct(
        "Message" / Int64ul
    )


@declare(guid=guid("25b99a4c-2f80-4fcd-982d-69cd1f77badf"), event_id=4032, version=0)
class Microsoft_Windows_MCCS_NetworkHelper_4032_0(Etw):
    pattern = Struct(
        "P1_Int32" / Int32sl
    )


@declare(guid=guid("25b99a4c-2f80-4fcd-982d-69cd1f77badf"), event_id=4033, version=0)
class Microsoft_Windows_MCCS_NetworkHelper_4033_0(Etw):
    pattern = Struct(
        "Prop_int1" / Int32sl,
        "Prop_int2" / Int32sl
    )


@declare(guid=guid("25b99a4c-2f80-4fcd-982d-69cd1f77badf"), event_id=4034, version=0)
class Microsoft_Windows_MCCS_NetworkHelper_4034_0(Etw):
    pattern = Struct(
        "Prop_int1" / Int32sl,
        "Prop_int2" / Int32sl
    )


@declare(guid=guid("25b99a4c-2f80-4fcd-982d-69cd1f77badf"), event_id=4040, version=0)
class Microsoft_Windows_MCCS_NetworkHelper_4040_0(Etw):
    pattern = Struct(
        "Prop_ptr" / Int64ul,
        "Prop_ansi" / CString,
        "Prop_int" / Int32sl
    )


@declare(guid=guid("25b99a4c-2f80-4fcd-982d-69cd1f77badf"), event_id=4041, version=0)
class Microsoft_Windows_MCCS_NetworkHelper_4041_0(Etw):
    pattern = Struct(
        "Message" / Int64ul
    )


@declare(guid=guid("25b99a4c-2f80-4fcd-982d-69cd1f77badf"), event_id=4043, version=0)
class Microsoft_Windows_MCCS_NetworkHelper_4043_0(Etw):
    pattern = Struct(
        "Prop_ptr" / Int64ul,
        "Prop_ansi" / CString,
        "Prop_int" / Int32sl
    )


@declare(guid=guid("25b99a4c-2f80-4fcd-982d-69cd1f77badf"), event_id=4044, version=0)
class Microsoft_Windows_MCCS_NetworkHelper_4044_0(Etw):
    pattern = Struct(
        "Prop_ptr" / Int64ul,
        "Prop_ansi" / CString,
        "Prop_uint" / Int32ul
    )


@declare(guid=guid("25b99a4c-2f80-4fcd-982d-69cd1f77badf"), event_id=4045, version=0)
class Microsoft_Windows_MCCS_NetworkHelper_4045_0(Etw):
    pattern = Struct(
        "Prop_ptr" / Int64ul,
        "Prop_int" / Int32sl
    )


@declare(guid=guid("25b99a4c-2f80-4fcd-982d-69cd1f77badf"), event_id=4051, version=0)
class Microsoft_Windows_MCCS_NetworkHelper_4051_0(Etw):
    pattern = Struct(
        "Prop_hexint" / Int32ul
    )


@declare(guid=guid("25b99a4c-2f80-4fcd-982d-69cd1f77badf"), event_id=4052, version=0)
class Microsoft_Windows_MCCS_NetworkHelper_4052_0(Etw):
    pattern = Struct(
        "P1_Int32" / Int32sl
    )

