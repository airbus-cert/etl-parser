# -*- coding: utf-8 -*-
"""
Microsoft-Windows-CertPolEng
GUID : af9cc194-e9a8-42bd-b0d1-834e9cfab799
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("af9cc194-e9a8-42bd-b0d1-834e9cfab799"), event_id=0, version=0)
class Microsoft_Windows_CertPolEng_0_0(Etw):
    pattern = Struct(
        "FunctionName" / CString
    )


@declare(guid=guid("af9cc194-e9a8-42bd-b0d1-834e9cfab799"), event_id=1, version=0)
class Microsoft_Windows_CertPolEng_1_0(Etw):
    pattern = Struct(
        "FunctionName" / CString
    )


@declare(guid=guid("af9cc194-e9a8-42bd-b0d1-834e9cfab799"), event_id=2, version=0)
class Microsoft_Windows_CertPolEng_2_0(Etw):
    pattern = Struct(
        "FunctionName" / CString,
        "LastError" / Int32ul
    )


@declare(guid=guid("af9cc194-e9a8-42bd-b0d1-834e9cfab799"), event_id=3, version=0)
class Microsoft_Windows_CertPolEng_3_0(Etw):
    pattern = Struct(
        "FunctionName" / CString,
        "LastError" / Int32ul
    )


@declare(guid=guid("af9cc194-e9a8-42bd-b0d1-834e9cfab799"), event_id=9, version=0)
class Microsoft_Windows_CertPolEng_9_0(Etw):
    pattern = Struct(
        "Number" / Int32ul
    )


@declare(guid=guid("af9cc194-e9a8-42bd-b0d1-834e9cfab799"), event_id=10, version=0)
class Microsoft_Windows_CertPolEng_10_0(Etw):
    pattern = Struct(
        "TargetName" / WString,
        "HostName" / WString
    )


@declare(guid=guid("af9cc194-e9a8-42bd-b0d1-834e9cfab799"), event_id=11, version=0)
class Microsoft_Windows_CertPolEng_11_0(Etw):
    pattern = Struct(
        "NumOfCriteria" / Int32ul,
        "bClient" / Int8ul
    )


@declare(guid=guid("af9cc194-e9a8-42bd-b0d1-834e9cfab799"), event_id=12, version=0)
class Microsoft_Windows_CertPolEng_12_0(Etw):
    pattern = Struct(
        "Number" / Int32ul
    )


@declare(guid=guid("af9cc194-e9a8-42bd-b0d1-834e9cfab799"), event_id=14, version=0)
class Microsoft_Windows_CertPolEng_14_0(Etw):
    pattern = Struct(
        "LastError" / Int32ul
    )


@declare(guid=guid("af9cc194-e9a8-42bd-b0d1-834e9cfab799"), event_id=15, version=0)
class Microsoft_Windows_CertPolEng_15_0(Etw):
    pattern = Struct(
        "psz" / WString
    )


@declare(guid=guid("af9cc194-e9a8-42bd-b0d1-834e9cfab799"), event_id=19, version=0)
class Microsoft_Windows_CertPolEng_19_0(Etw):
    pattern = Struct(
        "Number" / Int32ul
    )


@declare(guid=guid("af9cc194-e9a8-42bd-b0d1-834e9cfab799"), event_id=24, version=0)
class Microsoft_Windows_CertPolEng_24_0(Etw):
    pattern = Struct(
        "psz" / WString
    )


@declare(guid=guid("af9cc194-e9a8-42bd-b0d1-834e9cfab799"), event_id=25, version=0)
class Microsoft_Windows_CertPolEng_25_0(Etw):
    pattern = Struct(
        "psz" / WString
    )


@declare(guid=guid("af9cc194-e9a8-42bd-b0d1-834e9cfab799"), event_id=26, version=0)
class Microsoft_Windows_CertPolEng_26_0(Etw):
    pattern = Struct(
        "psz" / WString
    )


@declare(guid=guid("af9cc194-e9a8-42bd-b0d1-834e9cfab799"), event_id=27, version=0)
class Microsoft_Windows_CertPolEng_27_0(Etw):
    pattern = Struct(
        "Provider" / Guid,
        "LastError" / Int32ul
    )


@declare(guid=guid("af9cc194-e9a8-42bd-b0d1-834e9cfab799"), event_id=28, version=0)
class Microsoft_Windows_CertPolEng_28_0(Etw):
    pattern = Struct(
        "Number" / Int32ul
    )


@declare(guid=guid("af9cc194-e9a8-42bd-b0d1-834e9cfab799"), event_id=29, version=0)
class Microsoft_Windows_CertPolEng_29_0(Etw):
    pattern = Struct(
        "Number" / Int32ul
    )


@declare(guid=guid("af9cc194-e9a8-42bd-b0d1-834e9cfab799"), event_id=30, version=0)
class Microsoft_Windows_CertPolEng_30_0(Etw):
    pattern = Struct(
        "SubKey" / Int32ul,
        "LastError" / Int32ul
    )


@declare(guid=guid("af9cc194-e9a8-42bd-b0d1-834e9cfab799"), event_id=31, version=0)
class Microsoft_Windows_CertPolEng_31_0(Etw):
    pattern = Struct(
        "SubKey" / WString,
        "LastError" / Int32ul
    )


@declare(guid=guid("af9cc194-e9a8-42bd-b0d1-834e9cfab799"), event_id=32, version=0)
class Microsoft_Windows_CertPolEng_32_0(Etw):
    pattern = Struct(
        "LastError" / Int32ul,
        "ChainIndex" / Int32ul,
        "lElementIndex" / Int32ul
    )


@declare(guid=guid("af9cc194-e9a8-42bd-b0d1-834e9cfab799"), event_id=33, version=0)
class Microsoft_Windows_CertPolEng_33_0(Etw):
    pattern = Struct(
        "Number" / Int32ul
    )


@declare(guid=guid("af9cc194-e9a8-42bd-b0d1-834e9cfab799"), event_id=35, version=0)
class Microsoft_Windows_CertPolEng_35_0(Etw):
    pattern = Struct(
        "StoreName" / WString,
        "LastError" / Int32ul
    )


@declare(guid=guid("af9cc194-e9a8-42bd-b0d1-834e9cfab799"), event_id=36, version=0)
class Microsoft_Windows_CertPolEng_36_0(Etw):
    pattern = Struct(
        "Source" / Int32ul,
        "Calculated" / Int32ul
    )


@declare(guid=guid("af9cc194-e9a8-42bd-b0d1-834e9cfab799"), event_id=39, version=0)
class Microsoft_Windows_CertPolEng_39_0(Etw):
    pattern = Struct(
        "UPN" / WString,
        "ClientName" / WString
    )


@declare(guid=guid("af9cc194-e9a8-42bd-b0d1-834e9cfab799"), event_id=40, version=0)
class Microsoft_Windows_CertPolEng_40_0(Etw):
    pattern = Struct(
        "psz" / WString
    )


@declare(guid=guid("af9cc194-e9a8-42bd-b0d1-834e9cfab799"), event_id=41, version=0)
class Microsoft_Windows_CertPolEng_41_0(Etw):
    pattern = Struct(
        "UPN" / WString,
        "ClientName" / WString
    )


@declare(guid=guid("af9cc194-e9a8-42bd-b0d1-834e9cfab799"), event_id=45, version=0)
class Microsoft_Windows_CertPolEng_45_0(Etw):
    pattern = Struct(
        "UserName" / WString
    )


@declare(guid=guid("af9cc194-e9a8-42bd-b0d1-834e9cfab799"), event_id=46, version=0)
class Microsoft_Windows_CertPolEng_46_0(Etw):
    pattern = Struct(
        "Provider" / Guid
    )

