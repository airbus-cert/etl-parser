# -*- coding: utf-8 -*-
"""
Microsoft-Windows-FeatureConfiguration
GUID : c2f36562-a1e4-4bc3-a6f6-01a7adb643e8
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("c2f36562-a1e4-4bc3-a6f6-01a7adb643e8"), event_id=1001, version=0)
class Microsoft_Windows_FeatureConfiguration_1001_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("c2f36562-a1e4-4bc3-a6f6-01a7adb643e8"), event_id=1002, version=0)
class Microsoft_Windows_FeatureConfiguration_1002_0(Etw):
    pattern = Struct(
        "RegKeyName" / WString,
        "ValueName" / WString,
        "ValueType" / Int32ul,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("c2f36562-a1e4-4bc3-a6f6-01a7adb643e8"), event_id=1004, version=0)
class Microsoft_Windows_FeatureConfiguration_1004_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("c2f36562-a1e4-4bc3-a6f6-01a7adb643e8"), event_id=1005, version=0)
class Microsoft_Windows_FeatureConfiguration_1005_0(Etw):
    pattern = Struct(
        "FeatureId" / Int32ul,
        "FeatureState" / Int32ul
    )


@declare(guid=guid("c2f36562-a1e4-4bc3-a6f6-01a7adb643e8"), event_id=1006, version=0)
class Microsoft_Windows_FeatureConfiguration_1006_0(Etw):
    pattern = Struct(
        "FeatureId" / Int32ul
    )

