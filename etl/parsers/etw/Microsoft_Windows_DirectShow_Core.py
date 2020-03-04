# -*- coding: utf-8 -*-
"""
Microsoft-Windows-DirectShow-Core
GUID : 968f313b-097f-4e09-9cdd-bc62692d138b
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("968f313b-097f-4e09-9cdd-bc62692d138b"), event_id=1, version=0)
class Microsoft_Windows_DirectShow_Core_1_0(Etw):
    pattern = Struct(
        "ApplicationName" / WString,
        "FileName" / WString,
        "ContentType" / WString
    )


@declare(guid=guid("968f313b-097f-4e09-9cdd-bc62692d138b"), event_id=2, version=0)
class Microsoft_Windows_DirectShow_Core_2_0(Etw):
    pattern = Struct(
        "PreferredCount" / Int32ul,
        "DontUseCount" / Int32ul
    )


@declare(guid=guid("968f313b-097f-4e09-9cdd-bc62692d138b"), event_id=3, version=0)
class Microsoft_Windows_DirectShow_Core_3_0(Etw):
    pattern = Struct(
        "clsid" / Guid
    )


@declare(guid=guid("968f313b-097f-4e09-9cdd-bc62692d138b"), event_id=4, version=0)
class Microsoft_Windows_DirectShow_Core_4_0(Etw):
    pattern = Struct(
        "clsid" / Guid,
        "Disabled" / Int8ul
    )


@declare(guid=guid("968f313b-097f-4e09-9cdd-bc62692d138b"), event_id=5, version=0)
class Microsoft_Windows_DirectShow_Core_5_0(Etw):
    pattern = Struct(
        "clsid" / Guid,
        "Subtype" / Guid
    )


@declare(guid=guid("968f313b-097f-4e09-9cdd-bc62692d138b"), event_id=6, version=0)
class Microsoft_Windows_DirectShow_Core_6_0(Etw):
    pattern = Struct(
        "clsid" / Guid,
        "Subtype" / Guid
    )


@declare(guid=guid("968f313b-097f-4e09-9cdd-bc62692d138b"), event_id=7, version=0)
class Microsoft_Windows_DirectShow_Core_7_0(Etw):
    pattern = Struct(
        "FourCC" / WString,
        "dllName" / WString
    )


@declare(guid=guid("968f313b-097f-4e09-9cdd-bc62692d138b"), event_id=8, version=0)
class Microsoft_Windows_DirectShow_Core_8_0(Etw):
    pattern = Struct(
        "clsid" / Guid,
        "Subtype" / Guid
    )


@declare(guid=guid("968f313b-097f-4e09-9cdd-bc62692d138b"), event_id=9, version=0)
class Microsoft_Windows_DirectShow_Core_9_0(Etw):
    pattern = Struct(
        "Subtype" / Guid
    )


@declare(guid=guid("968f313b-097f-4e09-9cdd-bc62692d138b"), event_id=10, version=0)
class Microsoft_Windows_DirectShow_Core_10_0(Etw):
    pattern = Struct(
        "clsid" / Guid,
        "Disabled" / Int8ul
    )


@declare(guid=guid("968f313b-097f-4e09-9cdd-bc62692d138b"), event_id=100, version=0)
class Microsoft_Windows_DirectShow_Core_100_0(Etw):
    pattern = Struct(
        "context" / Int64ul,
        "url" / WString
    )


@declare(guid=guid("968f313b-097f-4e09-9cdd-bc62692d138b"), event_id=101, version=0)
class Microsoft_Windows_DirectShow_Core_101_0(Etw):
    pattern = Struct(
        "context" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("968f313b-097f-4e09-9cdd-bc62692d138b"), event_id=102, version=0)
class Microsoft_Windows_DirectShow_Core_102_0(Etw):
    pattern = Struct(
        "context" / Int64ul,
        "pinOutput" / Int64ul,
        "pinOutputName" / WString,
        "pinInput" / Int64ul,
        "pinInputName" / WString
    )


@declare(guid=guid("968f313b-097f-4e09-9cdd-bc62692d138b"), event_id=103, version=0)
class Microsoft_Windows_DirectShow_Core_103_0(Etw):
    pattern = Struct(
        "context" / Int64ul,
        "hr" / Int32ul,
        "type" / Guid,
        "subtype" / Guid
    )


@declare(guid=guid("968f313b-097f-4e09-9cdd-bc62692d138b"), event_id=104, version=0)
class Microsoft_Windows_DirectShow_Core_104_0(Etw):
    pattern = Struct(
        "context" / Int64ul,
        "pinOutput" / Int64ul,
        "pinOutputName" / WString
    )


@declare(guid=guid("968f313b-097f-4e09-9cdd-bc62692d138b"), event_id=105, version=0)
class Microsoft_Windows_DirectShow_Core_105_0(Etw):
    pattern = Struct(
        "context" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("968f313b-097f-4e09-9cdd-bc62692d138b"), event_id=106, version=0)
class Microsoft_Windows_DirectShow_Core_106_0(Etw):
    pattern = Struct(
        "context" / Int64ul,
        "filter" / Int64ul,
        "filterName" / WString,
        "name" / WString,
        "hr" / Int32ul
    )


@declare(guid=guid("968f313b-097f-4e09-9cdd-bc62692d138b"), event_id=107, version=0)
class Microsoft_Windows_DirectShow_Core_107_0(Etw):
    pattern = Struct(
        "context" / Int64ul,
        "url" / WString
    )


@declare(guid=guid("968f313b-097f-4e09-9cdd-bc62692d138b"), event_id=108, version=0)
class Microsoft_Windows_DirectShow_Core_108_0(Etw):
    pattern = Struct(
        "context" / Int64ul,
        "filter" / Int64ul,
        "filterName" / WString,
        "hr" / Int32ul
    )


@declare(guid=guid("968f313b-097f-4e09-9cdd-bc62692d138b"), event_id=109, version=0)
class Microsoft_Windows_DirectShow_Core_109_0(Etw):
    pattern = Struct(
        "context" / Int64ul,
        "eventCode" / Int32sl,
        "param1" / Int64ul,
        "param2" / Int64ul
    )


@declare(guid=guid("968f313b-097f-4e09-9cdd-bc62692d138b"), event_id=110, version=0)
class Microsoft_Windows_DirectShow_Core_110_0(Etw):
    pattern = Struct(
        "context" / Int64ul
    )


@declare(guid=guid("968f313b-097f-4e09-9cdd-bc62692d138b"), event_id=111, version=0)
class Microsoft_Windows_DirectShow_Core_111_0(Etw):
    pattern = Struct(
        "context" / Int64ul,
        "failingFilter" / Int64ul,
        "failingFilterName" / WString,
        "hr" / Int32ul
    )


@declare(guid=guid("968f313b-097f-4e09-9cdd-bc62692d138b"), event_id=112, version=0)
class Microsoft_Windows_DirectShow_Core_112_0(Etw):
    pattern = Struct(
        "context" / Int64ul
    )


@declare(guid=guid("968f313b-097f-4e09-9cdd-bc62692d138b"), event_id=113, version=0)
class Microsoft_Windows_DirectShow_Core_113_0(Etw):
    pattern = Struct(
        "context" / Int64ul,
        "failingFilter" / Int64ul,
        "failingFilterName" / WString,
        "hr" / Int32ul
    )


@declare(guid=guid("968f313b-097f-4e09-9cdd-bc62692d138b"), event_id=114, version=0)
class Microsoft_Windows_DirectShow_Core_114_0(Etw):
    pattern = Struct(
        "context" / Int64ul,
        "tStart" / Int64sl
    )


@declare(guid=guid("968f313b-097f-4e09-9cdd-bc62692d138b"), event_id=115, version=0)
class Microsoft_Windows_DirectShow_Core_115_0(Etw):
    pattern = Struct(
        "context" / Int64ul,
        "failingFilter" / Int64ul,
        "failingFilterName" / WString,
        "hr" / Int32ul
    )


@declare(guid=guid("968f313b-097f-4e09-9cdd-bc62692d138b"), event_id=116, version=0)
class Microsoft_Windows_DirectShow_Core_116_0(Etw):
    pattern = Struct(
        "context" / Int64ul,
        "pinOutput" / Int64ul,
        "pinOutputName" / WString,
        "pinInput" / Int64ul,
        "pinInputName" / WString
    )


@declare(guid=guid("968f313b-097f-4e09-9cdd-bc62692d138b"), event_id=117, version=0)
class Microsoft_Windows_DirectShow_Core_117_0(Etw):
    pattern = Struct(
        "context" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("968f313b-097f-4e09-9cdd-bc62692d138b"), event_id=118, version=0)
class Microsoft_Windows_DirectShow_Core_118_0(Etw):
    pattern = Struct(
        "context" / Int64ul,
        "pin" / Int64ul,
        "pinName" / WString,
        "hr" / Int32ul
    )


@declare(guid=guid("968f313b-097f-4e09-9cdd-bc62692d138b"), event_id=119, version=0)
class Microsoft_Windows_DirectShow_Core_119_0(Etw):
    pattern = Struct(
        "context" / Int64ul,
        "timeout" / Int32ul
    )


@declare(guid=guid("968f313b-097f-4e09-9cdd-bc62692d138b"), event_id=120, version=0)
class Microsoft_Windows_DirectShow_Core_120_0(Etw):
    pattern = Struct(
        "context" / Int64ul,
        "state" / Int32ul,
        "failingFilter" / Int64ul,
        "failingFilterName" / WString,
        "hr" / Int32ul
    )


@declare(guid=guid("968f313b-097f-4e09-9cdd-bc62692d138b"), event_id=121, version=0)
class Microsoft_Windows_DirectShow_Core_121_0(Etw):
    pattern = Struct(
        "context" / Int64ul,
        "filter" / Int64ul,
        "filterName" / WString,
        "hr" / Int32ul
    )

