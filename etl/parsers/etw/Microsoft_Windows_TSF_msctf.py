# -*- coding: utf-8 -*-
"""
Microsoft-Windows-TSF-msctf
GUID : 4fba1227-f606-4e5f-b9e8-fab9ab5740f3
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("4fba1227-f606-4e5f-b9e8-fab9ab5740f3"), event_id=5, version=0)
class Microsoft_Windows_TSF_msctf_5_0(Etw):
    pattern = Struct(
        "thread_flags" / Int32ul,
        "activation_flags" / Int32ul
    )


@declare(guid=guid("4fba1227-f606-4e5f-b9e8-fab9ab5740f3"), event_id=7, version=0)
class Microsoft_Windows_TSF_msctf_7_0(Etw):
    pattern = Struct(
        "thread_flags" / Int32ul,
        "activation_flags" / Int32ul
    )


@declare(guid=guid("4fba1227-f606-4e5f-b9e8-fab9ab5740f3"), event_id=19, version=0)
class Microsoft_Windows_TSF_msctf_19_0(Etw):
    pattern = Struct(
        "guid" / Guid
    )


@declare(guid=guid("4fba1227-f606-4e5f-b9e8-fab9ab5740f3"), event_id=20, version=0)
class Microsoft_Windows_TSF_msctf_20_0(Etw):
    pattern = Struct(
        "guid" / Guid
    )


@declare(guid=guid("4fba1227-f606-4e5f-b9e8-fab9ab5740f3"), event_id=21, version=0)
class Microsoft_Windows_TSF_msctf_21_0(Etw):
    pattern = Struct(
        "guid" / Guid
    )


@declare(guid=guid("4fba1227-f606-4e5f-b9e8-fab9ab5740f3"), event_id=22, version=0)
class Microsoft_Windows_TSF_msctf_22_0(Etw):
    pattern = Struct(
        "guid" / Guid
    )


@declare(guid=guid("4fba1227-f606-4e5f-b9e8-fab9ab5740f3"), event_id=29, version=0)
class Microsoft_Windows_TSF_msctf_29_0(Etw):
    pattern = Struct(
        "LANGID" / Int32ul
    )


@declare(guid=guid("4fba1227-f606-4e5f-b9e8-fab9ab5740f3"), event_id=30, version=0)
class Microsoft_Windows_TSF_msctf_30_0(Etw):
    pattern = Struct(
        "LANGID" / Int32ul
    )


@declare(guid=guid("4fba1227-f606-4e5f-b9e8-fab9ab5740f3"), event_id=31, version=0)
class Microsoft_Windows_TSF_msctf_31_0(Etw):
    pattern = Struct(
        "event" / Int32ul,
        "hwnd" / Int64ul,
        "flags" / Int32ul,
        "event_order" / Int32ul
    )


@declare(guid=guid("4fba1227-f606-4e5f-b9e8-fab9ab5740f3"), event_id=32, version=0)
class Microsoft_Windows_TSF_msctf_32_0(Etw):
    pattern = Struct(
        "hwnd" / Int64ul
    )


@declare(guid=guid("4fba1227-f606-4e5f-b9e8-fab9ab5740f3"), event_id=33, version=0)
class Microsoft_Windows_TSF_msctf_33_0(Etw):
    pattern = Struct(
        "event" / Int32ul,
        "hwnd" / Int64ul,
        "flags" / Int32ul,
        "event_order" / Int32ul
    )


@declare(guid=guid("4fba1227-f606-4e5f-b9e8-fab9ab5740f3"), event_id=35, version=0)
class Microsoft_Windows_TSF_msctf_35_0(Etw):
    pattern = Struct(
        "message" / Int32ul,
        "target_tid" / Int32ul,
        "params" / Int32ul
    )


@declare(guid=guid("4fba1227-f606-4e5f-b9e8-fab9ab5740f3"), event_id=36, version=0)
class Microsoft_Windows_TSF_msctf_36_0(Etw):
    pattern = Struct(
        "message" / Int32ul,
        "target_tid" / Int32ul,
        "params" / Int32ul
    )


@declare(guid=guid("4fba1227-f606-4e5f-b9e8-fab9ab5740f3"), event_id=38, version=0)
class Microsoft_Windows_TSF_msctf_38_0(Etw):
    pattern = Struct(
        "message" / Int32ul,
        "target_tid" / Int32ul,
        "params" / Int32ul
    )


@declare(guid=guid("4fba1227-f606-4e5f-b9e8-fab9ab5740f3"), event_id=42, version=0)
class Microsoft_Windows_TSF_msctf_42_0(Etw):
    pattern = Struct(
        "message" / Int32ul,
        "target_tid" / Int32ul,
        "params" / Int32ul
    )


@declare(guid=guid("4fba1227-f606-4e5f-b9e8-fab9ab5740f3"), event_id=43, version=0)
class Microsoft_Windows_TSF_msctf_43_0(Etw):
    pattern = Struct(
        "param" / Int32ul
    )


@declare(guid=guid("4fba1227-f606-4e5f-b9e8-fab9ab5740f3"), event_id=45, version=0)
class Microsoft_Windows_TSF_msctf_45_0(Etw):
    pattern = Struct(
        "message" / Int32ul,
        "target_tid" / Int32ul,
        "params" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("4fba1227-f606-4e5f-b9e8-fab9ab5740f3"), event_id=52, version=0)
class Microsoft_Windows_TSF_msctf_52_0(Etw):
    pattern = Struct(
        "param" / Int32ul
    )


@declare(guid=guid("4fba1227-f606-4e5f-b9e8-fab9ab5740f3"), event_id=53, version=0)
class Microsoft_Windows_TSF_msctf_53_0(Etw):
    pattern = Struct(
        "param" / Int32ul
    )


@declare(guid=guid("4fba1227-f606-4e5f-b9e8-fab9ab5740f3"), event_id=54, version=0)
class Microsoft_Windows_TSF_msctf_54_0(Etw):
    pattern = Struct(
        "param" / Int32ul
    )


@declare(guid=guid("4fba1227-f606-4e5f-b9e8-fab9ab5740f3"), event_id=55, version=0)
class Microsoft_Windows_TSF_msctf_55_0(Etw):
    pattern = Struct(
        "param" / Int32ul
    )


@declare(guid=guid("4fba1227-f606-4e5f-b9e8-fab9ab5740f3"), event_id=56, version=0)
class Microsoft_Windows_TSF_msctf_56_0(Etw):
    pattern = Struct(
        "pdimNewFocus" / Int64ul,
        "pdimPrevFocus" / Int64ul
    )


@declare(guid=guid("4fba1227-f606-4e5f-b9e8-fab9ab5740f3"), event_id=57, version=0)
class Microsoft_Windows_TSF_msctf_57_0(Etw):
    pattern = Struct(
        "pdimNewFocus" / Int64ul,
        "pdimPrevFocus" / Int64ul
    )


@declare(guid=guid("4fba1227-f606-4e5f-b9e8-fab9ab5740f3"), event_id=58, version=0)
class Microsoft_Windows_TSF_msctf_58_0(Etw):
    pattern = Struct(
        "param" / Int32ul
    )


@declare(guid=guid("4fba1227-f606-4e5f-b9e8-fab9ab5740f3"), event_id=59, version=0)
class Microsoft_Windows_TSF_msctf_59_0(Etw):
    pattern = Struct(
        "param" / Int32ul
    )


@declare(guid=guid("4fba1227-f606-4e5f-b9e8-fab9ab5740f3"), event_id=64, version=0)
class Microsoft_Windows_TSF_msctf_64_0(Etw):
    pattern = Struct(
        "param" / Int32ul
    )


@declare(guid=guid("4fba1227-f606-4e5f-b9e8-fab9ab5740f3"), event_id=65, version=0)
class Microsoft_Windows_TSF_msctf_65_0(Etw):
    pattern = Struct(
        "guid" / Guid
    )


@declare(guid=guid("4fba1227-f606-4e5f-b9e8-fab9ab5740f3"), event_id=66, version=0)
class Microsoft_Windows_TSF_msctf_66_0(Etw):
    pattern = Struct(
        "guid" / Guid
    )


@declare(guid=guid("4fba1227-f606-4e5f-b9e8-fab9ab5740f3"), event_id=67, version=0)
class Microsoft_Windows_TSF_msctf_67_0(Etw):
    pattern = Struct(
        "guid" / Guid
    )


@declare(guid=guid("4fba1227-f606-4e5f-b9e8-fab9ab5740f3"), event_id=68, version=0)
class Microsoft_Windows_TSF_msctf_68_0(Etw):
    pattern = Struct(
        "guid" / Guid
    )


@declare(guid=guid("4fba1227-f606-4e5f-b9e8-fab9ab5740f3"), event_id=69, version=0)
class Microsoft_Windows_TSF_msctf_69_0(Etw):
    pattern = Struct(
        "guid" / Guid
    )


@declare(guid=guid("4fba1227-f606-4e5f-b9e8-fab9ab5740f3"), event_id=70, version=0)
class Microsoft_Windows_TSF_msctf_70_0(Etw):
    pattern = Struct(
        "guid" / Guid
    )


@declare(guid=guid("4fba1227-f606-4e5f-b9e8-fab9ab5740f3"), event_id=74, version=0)
class Microsoft_Windows_TSF_msctf_74_0(Etw):
    pattern = Struct(
        "param" / Int32ul
    )


@declare(guid=guid("4fba1227-f606-4e5f-b9e8-fab9ab5740f3"), event_id=75, version=0)
class Microsoft_Windows_TSF_msctf_75_0(Etw):
    pattern = Struct(
        "guid" / Guid,
        "langid" / Int16ul
    )


@declare(guid=guid("4fba1227-f606-4e5f-b9e8-fab9ab5740f3"), event_id=77, version=0)
class Microsoft_Windows_TSF_msctf_77_0(Etw):
    pattern = Struct(
        "param" / Int32ul
    )


@declare(guid=guid("4fba1227-f606-4e5f-b9e8-fab9ab5740f3"), event_id=79, version=0)
class Microsoft_Windows_TSF_msctf_79_0(Etw):
    pattern = Struct(
        "DocId" / Int32ul,
        "DocThread" / Int32ul,
        "GainFocus" / Int8ul
    )


@declare(guid=guid("4fba1227-f606-4e5f-b9e8-fab9ab5740f3"), event_id=80, version=0)
class Microsoft_Windows_TSF_msctf_80_0(Etw):
    pattern = Struct(
        "thread" / Int32ul,
        "document" / Int32ul
    )


@declare(guid=guid("4fba1227-f606-4e5f-b9e8-fab9ab5740f3"), event_id=81, version=0)
class Microsoft_Windows_TSF_msctf_81_0(Etw):
    pattern = Struct(
        "thread" / Int32ul,
        "document" / Int32ul
    )


@declare(guid=guid("4fba1227-f606-4e5f-b9e8-fab9ab5740f3"), event_id=82, version=0)
class Microsoft_Windows_TSF_msctf_82_0(Etw):
    pattern = Struct(
        "boolean" / Int8ul
    )


@declare(guid=guid("4fba1227-f606-4e5f-b9e8-fab9ab5740f3"), event_id=84, version=0)
class Microsoft_Windows_TSF_msctf_84_0(Etw):
    pattern = Struct(
        "param" / Int32ul
    )


@declare(guid=guid("4fba1227-f606-4e5f-b9e8-fab9ab5740f3"), event_id=85, version=0)
class Microsoft_Windows_TSF_msctf_85_0(Etw):
    pattern = Struct(
        "param" / Int32ul
    )


@declare(guid=guid("4fba1227-f606-4e5f-b9e8-fab9ab5740f3"), event_id=89, version=0)
class Microsoft_Windows_TSF_msctf_89_0(Etw):
    pattern = Struct(
        "boolean" / Int8ul
    )

