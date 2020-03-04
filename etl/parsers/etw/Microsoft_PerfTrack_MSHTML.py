# -*- coding: utf-8 -*-
"""
Microsoft-PerfTrack-MSHTML
GUID : ffdb9886-80f3-4540-aa8b-b85192217ddf
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("ffdb9886-80f3-4540-aa8b-b85192217ddf"), event_id=101, version=0)
class Microsoft_PerfTrack_MSHTML_101_0(Etw):
    pattern = Struct(
        "ObjectMSHTML" / Int64ul,
        "Counter" / Int32ul
    )


@declare(guid=guid("ffdb9886-80f3-4540-aa8b-b85192217ddf"), event_id=102, version=0)
class Microsoft_PerfTrack_MSHTML_102_0(Etw):
    pattern = Struct(
        "ObjectMSHTML" / Int64ul,
        "Counter" / Int32ul
    )


@declare(guid=guid("ffdb9886-80f3-4540-aa8b-b85192217ddf"), event_id=103, version=0)
class Microsoft_PerfTrack_MSHTML_103_0(Etw):
    pattern = Struct(
        "ObjectMSHTML" / Int64ul
    )


@declare(guid=guid("ffdb9886-80f3-4540-aa8b-b85192217ddf"), event_id=104, version=0)
class Microsoft_PerfTrack_MSHTML_104_0(Etw):
    pattern = Struct(
        "ObjectMSHTML" / Int64ul
    )


@declare(guid=guid("ffdb9886-80f3-4540-aa8b-b85192217ddf"), event_id=105, version=0)
class Microsoft_PerfTrack_MSHTML_105_0(Etw):
    pattern = Struct(
        "ObjectMSHTML" / Int64ul,
        "Counter" / Int32ul
    )


@declare(guid=guid("ffdb9886-80f3-4540-aa8b-b85192217ddf"), event_id=107, version=0)
class Microsoft_PerfTrack_MSHTML_107_0(Etw):
    pattern = Struct(
        "ObjectXSSFilter" / Int64ul,
        "Type" / WString
    )


@declare(guid=guid("ffdb9886-80f3-4540-aa8b-b85192217ddf"), event_id=108, version=0)
class Microsoft_PerfTrack_MSHTML_108_0(Etw):
    pattern = Struct(
        "ObjectXSSFilter" / Int64ul,
        "Type" / WString
    )


@declare(guid=guid("ffdb9886-80f3-4540-aa8b-b85192217ddf"), event_id=109, version=0)
class Microsoft_PerfTrack_MSHTML_109_0(Etw):
    pattern = Struct(
        "ObjectXSSFilter" / Int64ul
    )


@declare(guid=guid("ffdb9886-80f3-4540-aa8b-b85192217ddf"), event_id=110, version=0)
class Microsoft_PerfTrack_MSHTML_110_0(Etw):
    pattern = Struct(
        "ObjectXSSFilter" / Int64ul
    )

