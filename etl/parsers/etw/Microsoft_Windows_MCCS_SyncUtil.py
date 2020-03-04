# -*- coding: utf-8 -*-
"""
Microsoft-Windows-MCCS-SyncUtil
GUID : dca074ce-547c-4595-ae90-56229b8e3bd9
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("dca074ce-547c-4595-ae90-56229b8e3bd9"), event_id=1, version=0)
class Microsoft_Windows_MCCS_SyncUtil_1_0(Etw):
    pattern = Struct(
        "P1_HResult" / Int32sl,
        "P2_String" / CString,
        "P3_UInt32" / Int32ul
    )


@declare(guid=guid("dca074ce-547c-4595-ae90-56229b8e3bd9"), event_id=2, version=0)
class Microsoft_Windows_MCCS_SyncUtil_2_0(Etw):
    pattern = Struct(
        "P1_HResult" / Int32sl,
        "P2_String" / CString,
        "P3_UInt32" / Int32ul
    )


@declare(guid=guid("dca074ce-547c-4595-ae90-56229b8e3bd9"), event_id=101, version=0)
class Microsoft_Windows_MCCS_SyncUtil_101_0(Etw):
    pattern = Struct(
        "Prop_Dword" / Int32ul,
        "Prop_StringA_1" / CString,
        "Prop_StringA_2" / CString
    )


@declare(guid=guid("dca074ce-547c-4595-ae90-56229b8e3bd9"), event_id=104, version=0)
class Microsoft_Windows_MCCS_SyncUtil_104_0(Etw):
    pattern = Struct(
        "Prop_String1" / WString,
        "Prop_String2" / WString,
        "Prop_String3" / WString,
        "Prop_AnsiString" / CString
    )


@declare(guid=guid("dca074ce-547c-4595-ae90-56229b8e3bd9"), event_id=121, version=0)
class Microsoft_Windows_MCCS_SyncUtil_121_0(Etw):
    pattern = Struct(
        "P1_UnicodeString" / WString
    )


@declare(guid=guid("dca074ce-547c-4595-ae90-56229b8e3bd9"), event_id=122, version=0)
class Microsoft_Windows_MCCS_SyncUtil_122_0(Etw):
    pattern = Struct(
        "P1_UnicodeString" / WString
    )


@declare(guid=guid("dca074ce-547c-4595-ae90-56229b8e3bd9"), event_id=202, version=0)
class Microsoft_Windows_MCCS_SyncUtil_202_0(Etw):
    pattern = Struct(
        "P1_HexInt32" / Int32ul
    )


@declare(guid=guid("dca074ce-547c-4595-ae90-56229b8e3bd9"), event_id=203, version=0)
class Microsoft_Windows_MCCS_SyncUtil_203_0(Etw):
    pattern = Struct(
        "P1_UnicodeString" / WString
    )


@declare(guid=guid("dca074ce-547c-4595-ae90-56229b8e3bd9"), event_id=204, version=0)
class Microsoft_Windows_MCCS_SyncUtil_204_0(Etw):
    pattern = Struct(
        "P1_UnicodeString" / WString
    )


@declare(guid=guid("dca074ce-547c-4595-ae90-56229b8e3bd9"), event_id=205, version=0)
class Microsoft_Windows_MCCS_SyncUtil_205_0(Etw):
    pattern = Struct(
        "P1_UnicodeString" / WString
    )


@declare(guid=guid("dca074ce-547c-4595-ae90-56229b8e3bd9"), event_id=206, version=0)
class Microsoft_Windows_MCCS_SyncUtil_206_0(Etw):
    pattern = Struct(
        "P1_Int32" / Int32sl
    )


@declare(guid=guid("dca074ce-547c-4595-ae90-56229b8e3bd9"), event_id=800, version=0)
class Microsoft_Windows_MCCS_SyncUtil_800_0(Etw):
    pattern = Struct(
        "Prop_String1" / WString,
        "Prop_FileTime1" / Int64ul
    )


@declare(guid=guid("dca074ce-547c-4595-ae90-56229b8e3bd9"), event_id=802, version=0)
class Microsoft_Windows_MCCS_SyncUtil_802_0(Etw):
    pattern = Struct(
        "Prop_String1" / WString,
        "Prop_FileTime1" / Int64ul
    )


@declare(guid=guid("dca074ce-547c-4595-ae90-56229b8e3bd9"), event_id=803, version=0)
class Microsoft_Windows_MCCS_SyncUtil_803_0(Etw):
    pattern = Struct(
        "P1_Int32" / Int32sl
    )


@declare(guid=guid("dca074ce-547c-4595-ae90-56229b8e3bd9"), event_id=804, version=0)
class Microsoft_Windows_MCCS_SyncUtil_804_0(Etw):
    pattern = Struct(
        "Prop_HexInt32" / Int32ul,
        "Prop_String" / WString
    )


@declare(guid=guid("dca074ce-547c-4595-ae90-56229b8e3bd9"), event_id=810, version=0)
class Microsoft_Windows_MCCS_SyncUtil_810_0(Etw):
    pattern = Struct(
        "P1_HexInt32" / Int32ul
    )

