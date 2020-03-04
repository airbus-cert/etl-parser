# -*- coding: utf-8 -*-
"""
Microsoft-Windows-ApplicationExperience-SwitchBack
GUID : 17d6e590-f5fe-11dc-95ff-0800200c9a66
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("17d6e590-f5fe-11dc-95ff-0800200c9a66"), event_id=1, version=0)
class Microsoft_Windows_ApplicationExperience_SwitchBack_1_0(Etw):
    pattern = Struct(
        "SwitchBranchGuid" / Guid,
        "SwitchBranchNameLength" / Int16ul,
        "SwitchBranchName" / Bytes(lambda this: this.SwitchBranchNameLength),
        "SwitchBranchDescriptionLength" / Int16ul,
        "SwitchBranchDescription" / Bytes(lambda this: this.SwitchBranchDescriptionLength)
    )


@declare(guid=guid("17d6e590-f5fe-11dc-95ff-0800200c9a66"), event_id=2, version=0)
class Microsoft_Windows_ApplicationExperience_SwitchBack_2_0(Etw):
    pattern = Struct(
        "SwitchBranchImplGuid" / Guid,
        "SwitchBranchImplNameLength" / Int16ul,
        "SwitchBranchImplName" / Bytes(lambda this: this.SwitchBranchImplNameLength),
        "SwitchBranchImplDescriptionLength" / Int16ul,
        "SwitchBranchImplDescription" / Bytes(lambda this: this.SwitchBranchImplDescriptionLength)
    )


@declare(guid=guid("17d6e590-f5fe-11dc-95ff-0800200c9a66"), event_id=3, version=0)
class Microsoft_Windows_ApplicationExperience_SwitchBack_3_0(Etw):
    pattern = Struct(
        "TargetContextGuid" / Guid,
        "TargetContextType" / Int16ul,
        "ModuleNameLength" / Int16ul,
        "ModuleName" / Bytes(lambda this: this.ModuleNameLength)
    )


@declare(guid=guid("17d6e590-f5fe-11dc-95ff-0800200c9a66"), event_id=4, version=0)
class Microsoft_Windows_ApplicationExperience_SwitchBack_4_0(Etw):
    pattern = Struct(
        "ContextUpdateCounter" / Int64ul
    )

