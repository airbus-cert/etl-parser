# -*- coding: utf-8 -*-
"""
Microsoft-Windows-SleepStudy
GUID : d37687e7-8bf0-4d11-b589-a7abe080756a
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("d37687e7-8bf0-4d11-b589-a7abe080756a"), event_id=1, version=0)
class Microsoft_Windows_SleepStudy_1_0(Etw):
    pattern = Struct(
        "ScenarioInstanceId" / Int8ul,
        "ParentGuid" / Guid,
        "BlockerNameLength" / Int32ul,
        "BlockerName" / Bytes(lambda this: this.BlockerNameLength),
        "BlockerGuid" / Guid,
        "ActiveTime" / Int64ul
    )


@declare(guid=guid("d37687e7-8bf0-4d11-b589-a7abe080756a"), event_id=2, version=0)
class Microsoft_Windows_SleepStudy_2_0(Etw):
    pattern = Struct(
        "ScenarioInstanceId" / Int8ul,
        "DataCount" / Int32ul,
        "Data" / Int8sl
    )


@declare(guid=guid("d37687e7-8bf0-4d11-b589-a7abe080756a"), event_id=3, version=0)
class Microsoft_Windows_SleepStudy_3_0(Etw):
    pattern = Struct(
        "ActiveTimeAndCommonData" / Int32ul,
        "TopLevelActiveTime" / Int32ul,
        "BlockerHierarchyLevel1" / WString,
        "BlockerHierarchyLevel2" / WString,
        "BlockerHierarchyLevel3" / WString
    )


@declare(guid=guid("d37687e7-8bf0-4d11-b589-a7abe080756a"), event_id=4, version=0)
class Microsoft_Windows_SleepStudy_4_0(Etw):
    pattern = Struct(
        "DataCount" / Int32ul,
        "Data" / CString
    )

