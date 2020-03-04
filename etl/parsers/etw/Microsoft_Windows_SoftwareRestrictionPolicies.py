# -*- coding: utf-8 -*-
"""
Microsoft-Windows-SoftwareRestrictionPolicies
GUID : 7d29d58a-931a-40ac-8743-48c733045548
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("7d29d58a-931a-40ac-8743-48c733045548"), event_id=50, version=0)
class Microsoft_Windows_SoftwareRestrictionPolicies_50_0(Etw):
    pattern = Struct(
        "AttemptedPath" / WString,
        "SrpRuleGuid" / Guid
    )


@declare(guid=guid("7d29d58a-931a-40ac-8743-48c733045548"), event_id=865, version=0)
class Microsoft_Windows_SoftwareRestrictionPolicies_865_0(Etw):
    pattern = Struct(
        "AttemptedPath" / WString
    )


@declare(guid=guid("7d29d58a-931a-40ac-8743-48c733045548"), event_id=866, version=0)
class Microsoft_Windows_SoftwareRestrictionPolicies_866_0(Etw):
    pattern = Struct(
        "AttemptedPath" / WString,
        "SrpRuleGuid" / Guid,
        "RulePath" / WString
    )


@declare(guid=guid("7d29d58a-931a-40ac-8743-48c733045548"), event_id=867, version=0)
class Microsoft_Windows_SoftwareRestrictionPolicies_867_0(Etw):
    pattern = Struct(
        "AttemptedPath" / WString
    )


@declare(guid=guid("7d29d58a-931a-40ac-8743-48c733045548"), event_id=868, version=0)
class Microsoft_Windows_SoftwareRestrictionPolicies_868_0(Etw):
    pattern = Struct(
        "AttemptedPath" / WString,
        "SrpRuleGuid" / Guid
    )


@declare(guid=guid("7d29d58a-931a-40ac-8743-48c733045548"), event_id=882, version=0)
class Microsoft_Windows_SoftwareRestrictionPolicies_882_0(Etw):
    pattern = Struct(
        "AttemptedPath" / WString,
        "SrpRuleGuid" / Guid
    )

