# -*- coding: utf-8 -*-
"""
Intel-Thunderbolt-App
GUID : 8ef15e41-05bf-5bcd-4aa8-4f0559564dc0
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("8ef15e41-05bf-5bcd-4aa8-4f0559564dc0"), event_id=0, version=0)
class Intel_Thunderbolt_App_0_0(Etw):
    pattern = Struct(
        "message" / WString
    )


@declare(guid=guid("8ef15e41-05bf-5bcd-4aa8-4f0559564dc0"), event_id=1, version=0)
class Intel_Thunderbolt_App_1_0(Etw):
    pattern = Struct(
        "message" / WString
    )


@declare(guid=guid("8ef15e41-05bf-5bcd-4aa8-4f0559564dc0"), event_id=2, version=0)
class Intel_Thunderbolt_App_2_0(Etw):
    pattern = Struct(
        "message" / WString,
        "stackTrace" / WString
    )


@declare(guid=guid("8ef15e41-05bf-5bcd-4aa8-4f0559564dc0"), event_id=3, version=0)
class Intel_Thunderbolt_App_3_0(Etw):
    pattern = Struct(
        "message" / WString
    )


@declare(guid=guid("8ef15e41-05bf-5bcd-4aa8-4f0559564dc0"), event_id=4, version=0)
class Intel_Thunderbolt_App_4_0(Etw):
    pattern = Struct(
        "message" / WString
    )


@declare(guid=guid("8ef15e41-05bf-5bcd-4aa8-4f0559564dc0"), event_id=5, version=0)
class Intel_Thunderbolt_App_5_0(Etw):
    pattern = Struct(
        "eventName" / WString
    )


@declare(guid=guid("8ef15e41-05bf-5bcd-4aa8-4f0559564dc0"), event_id=6, version=0)
class Intel_Thunderbolt_App_6_0(Etw):
    pattern = Struct(
        "obj" / WString,
        "method" / WString,
        "inparams" / WString,
        "stackFrame" / WString
    )


@declare(guid=guid("8ef15e41-05bf-5bcd-4aa8-4f0559564dc0"), event_id=7, version=0)
class Intel_Thunderbolt_App_7_0(Etw):
    pattern = Struct(
        "message" / WString
    )


@declare(guid=guid("8ef15e41-05bf-5bcd-4aa8-4f0559564dc0"), event_id=8, version=0)
class Intel_Thunderbolt_App_8_0(Etw):
    pattern = Struct(
        "info" / WString
    )


@declare(guid=guid("8ef15e41-05bf-5bcd-4aa8-4f0559564dc0"), event_id=9, version=0)
class Intel_Thunderbolt_App_9_0(Etw):
    pattern = Struct(
        "action" / WString,
        "message" / WString
    )

