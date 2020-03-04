# -*- coding: utf-8 -*-
"""
Application-Addon-Event-Provider
GUID : a83fa99f-c356-4ded-9fd6-5a5eb8546d68
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("a83fa99f-c356-4ded-9fd6-5a5eb8546d68"), event_id=1, version=1)
class Application_Addon_Event_Provider_1_1(Etw):
    pattern = Struct(
        "Application" / WString,
        "AddonName" / WString,
        "Publisher" / WString,
        "Version" / WString
    )


@declare(guid=guid("a83fa99f-c356-4ded-9fd6-5a5eb8546d68"), event_id=2, version=1)
class Application_Addon_Event_Provider_2_1(Etw):
    pattern = Struct(
        "Application" / WString,
        "AddonName" / WString,
        "Publisher" / WString,
        "Version" / WString
    )

