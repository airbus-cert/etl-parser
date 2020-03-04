# -*- coding: utf-8 -*-
"""
Microsoft-Windows-MCCS-InternetMail
GUID : 618473bc-8eef-4868-adff-a1b640b06411
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("618473bc-8eef-4868-adff-a1b640b06411"), event_id=1, version=0)
class Microsoft_Windows_MCCS_InternetMail_1_0(Etw):
    pattern = Struct(
        "P1_HResult" / Int32sl,
        "P2_String" / CString,
        "P3_UInt32" / Int32ul
    )


@declare(guid=guid("618473bc-8eef-4868-adff-a1b640b06411"), event_id=2, version=0)
class Microsoft_Windows_MCCS_InternetMail_2_0(Etw):
    pattern = Struct(
        "P1_HResult" / Int32sl,
        "P2_String" / CString,
        "P3_UInt32" / Int32ul
    )


@declare(guid=guid("618473bc-8eef-4868-adff-a1b640b06411"), event_id=101, version=0)
class Microsoft_Windows_MCCS_InternetMail_101_0(Etw):
    pattern = Struct(
        "Prop_String" / CString
    )


@declare(guid=guid("618473bc-8eef-4868-adff-a1b640b06411"), event_id=102, version=0)
class Microsoft_Windows_MCCS_InternetMail_102_0(Etw):
    pattern = Struct(
        "Prop_String" / CString,
        "Prop_String2" / CString
    )


@declare(guid=guid("618473bc-8eef-4868-adff-a1b640b06411"), event_id=103, version=0)
class Microsoft_Windows_MCCS_InternetMail_103_0(Etw):
    pattern = Struct(
        "Prop_String" / CString,
        "Prop_String2" / CString
    )


@declare(guid=guid("618473bc-8eef-4868-adff-a1b640b06411"), event_id=104, version=0)
class Microsoft_Windows_MCCS_InternetMail_104_0(Etw):
    pattern = Struct(
        "Prop_Hex" / Int32ul
    )


@declare(guid=guid("618473bc-8eef-4868-adff-a1b640b06411"), event_id=110, version=0)
class Microsoft_Windows_MCCS_InternetMail_110_0(Etw):
    pattern = Struct(
        "Prop_Hex" / Int32ul
    )


@declare(guid=guid("618473bc-8eef-4868-adff-a1b640b06411"), event_id=111, version=0)
class Microsoft_Windows_MCCS_InternetMail_111_0(Etw):
    pattern = Struct(
        "Prop_Hex" / Int32ul
    )


@declare(guid=guid("618473bc-8eef-4868-adff-a1b640b06411"), event_id=116, version=0)
class Microsoft_Windows_MCCS_InternetMail_116_0(Etw):
    pattern = Struct(
        "Prop_Hex" / Int32ul
    )


@declare(guid=guid("618473bc-8eef-4868-adff-a1b640b06411"), event_id=118, version=0)
class Microsoft_Windows_MCCS_InternetMail_118_0(Etw):
    pattern = Struct(
        "Prop_Uint" / Int32ul
    )


@declare(guid=guid("618473bc-8eef-4868-adff-a1b640b06411"), event_id=119, version=0)
class Microsoft_Windows_MCCS_InternetMail_119_0(Etw):
    pattern = Struct(
        "Prop_Uint" / Int32ul
    )


@declare(guid=guid("618473bc-8eef-4868-adff-a1b640b06411"), event_id=120, version=0)
class Microsoft_Windows_MCCS_InternetMail_120_0(Etw):
    pattern = Struct(
        "Prop_Uint" / Int32ul
    )


@declare(guid=guid("618473bc-8eef-4868-adff-a1b640b06411"), event_id=121, version=0)
class Microsoft_Windows_MCCS_InternetMail_121_0(Etw):
    pattern = Struct(
        "Prop_Uint1" / Int32ul,
        "Prop_Uint2" / Int32ul
    )


@declare(guid=guid("618473bc-8eef-4868-adff-a1b640b06411"), event_id=124, version=0)
class Microsoft_Windows_MCCS_InternetMail_124_0(Etw):
    pattern = Struct(
        "Prop_Uint" / Int32ul
    )


@declare(guid=guid("618473bc-8eef-4868-adff-a1b640b06411"), event_id=401, version=0)
class Microsoft_Windows_MCCS_InternetMail_401_0(Etw):
    pattern = Struct(
        "Prop_String" / WString,
        "Prop_Boolean" / Int8ul
    )


@declare(guid=guid("618473bc-8eef-4868-adff-a1b640b06411"), event_id=402, version=0)
class Microsoft_Windows_MCCS_InternetMail_402_0(Etw):
    pattern = Struct(
        "Prop_String" / WString,
        "Prop_Boolean" / Int8ul
    )


@declare(guid=guid("618473bc-8eef-4868-adff-a1b640b06411"), event_id=403, version=0)
class Microsoft_Windows_MCCS_InternetMail_403_0(Etw):
    pattern = Struct(
        "Prop_String" / WString,
        "Prop_Boolean" / Int8ul
    )


@declare(guid=guid("618473bc-8eef-4868-adff-a1b640b06411"), event_id=451, version=0)
class Microsoft_Windows_MCCS_InternetMail_451_0(Etw):
    pattern = Struct(
        "Prop_Uint" / Int32ul
    )


@declare(guid=guid("618473bc-8eef-4868-adff-a1b640b06411"), event_id=461, version=0)
class Microsoft_Windows_MCCS_InternetMail_461_0(Etw):
    pattern = Struct(
        "Prop_Uint" / Int32ul
    )


@declare(guid=guid("618473bc-8eef-4868-adff-a1b640b06411"), event_id=462, version=0)
class Microsoft_Windows_MCCS_InternetMail_462_0(Etw):
    pattern = Struct(
        "Prop_Uint" / Int32ul
    )


@declare(guid=guid("618473bc-8eef-4868-adff-a1b640b06411"), event_id=470, version=0)
class Microsoft_Windows_MCCS_InternetMail_470_0(Etw):
    pattern = Struct(
        "Prop_Guid" / Guid,
        "Prop_Dword_1" / Int32ul,
        "Prop_Dword_2" / Int32ul
    )


@declare(guid=guid("618473bc-8eef-4868-adff-a1b640b06411"), event_id=471, version=0)
class Microsoft_Windows_MCCS_InternetMail_471_0(Etw):
    pattern = Struct(
        "Prop_Guid" / Guid,
        "Prop_Dword_1" / Int32ul,
        "Prop_Dword_2" / Int32ul
    )


@declare(guid=guid("618473bc-8eef-4868-adff-a1b640b06411"), event_id=485, version=0)
class Microsoft_Windows_MCCS_InternetMail_485_0(Etw):
    pattern = Struct(
        "Prop_Hex" / Int32ul
    )


@declare(guid=guid("618473bc-8eef-4868-adff-a1b640b06411"), event_id=501, version=0)
class Microsoft_Windows_MCCS_InternetMail_501_0(Etw):
    pattern = Struct(
        "Prop_Guid" / Guid,
        "Prop_HexInt32" / Int32ul
    )

