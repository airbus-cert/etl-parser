# -*- coding: utf-8 -*-
"""
Microsoft-Windows-AppModel-State
GUID : bff15e13-81bf-45ee-8b16-7cfead00da86
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("bff15e13-81bf-45ee-8b16-7cfead00da86"), event_id=1, version=0)
class Microsoft_Windows_AppModel_State_1_0(Etw):
    pattern = Struct(
        "ErrorString" / WString,
        "Error" / Int32sl
    )


@declare(guid=guid("bff15e13-81bf-45ee-8b16-7cfead00da86"), event_id=2, version=0)
class Microsoft_Windows_AppModel_State_2_0(Etw):
    pattern = Struct(
        "ErrorString" / WString,
        "Error" / Int32sl
    )


@declare(guid=guid("bff15e13-81bf-45ee-8b16-7cfead00da86"), event_id=4, version=0)
class Microsoft_Windows_AppModel_State_4_0(Etw):
    pattern = Struct(
        "ErrorString" / WString,
        "Error" / Int32sl
    )


@declare(guid=guid("bff15e13-81bf-45ee-8b16-7cfead00da86"), event_id=5, version=0)
class Microsoft_Windows_AppModel_State_5_0(Etw):
    pattern = Struct(
        "ErrorString" / WString,
        "Error" / Int32sl
    )


@declare(guid=guid("bff15e13-81bf-45ee-8b16-7cfead00da86"), event_id=8, version=0)
class Microsoft_Windows_AppModel_State_8_0(Etw):
    pattern = Struct(
        "ErrorString" / WString,
        "Error" / Int32sl
    )


@declare(guid=guid("bff15e13-81bf-45ee-8b16-7cfead00da86"), event_id=10, version=0)
class Microsoft_Windows_AppModel_State_10_0(Etw):
    pattern = Struct(
        "ErrorString" / WString,
        "Error" / Int32sl
    )


@declare(guid=guid("bff15e13-81bf-45ee-8b16-7cfead00da86"), event_id=11, version=0)
class Microsoft_Windows_AppModel_State_11_0(Etw):
    pattern = Struct(
        "ErrorString" / WString,
        "Error" / Int32sl
    )


@declare(guid=guid("bff15e13-81bf-45ee-8b16-7cfead00da86"), event_id=12, version=0)
class Microsoft_Windows_AppModel_State_12_0(Etw):
    pattern = Struct(
        "ErrorString" / WString,
        "Error" / Int32sl
    )


@declare(guid=guid("bff15e13-81bf-45ee-8b16-7cfead00da86"), event_id=13, version=0)
class Microsoft_Windows_AppModel_State_13_0(Etw):
    pattern = Struct(
        "FolderString" / WString,
        "PackageString" / WString,
        "Error" / Int32sl
    )


@declare(guid=guid("bff15e13-81bf-45ee-8b16-7cfead00da86"), event_id=14, version=0)
class Microsoft_Windows_AppModel_State_14_0(Etw):
    pattern = Struct(
        "PackageString" / WString,
        "UserSid" / WString,
        "Error" / Int32sl
    )


@declare(guid=guid("bff15e13-81bf-45ee-8b16-7cfead00da86"), event_id=15, version=0)
class Microsoft_Windows_AppModel_State_15_0(Etw):
    pattern = Struct(
        "PackageString" / WString,
        "UserSid" / WString,
        "Error" / Int32sl
    )


@declare(guid=guid("bff15e13-81bf-45ee-8b16-7cfead00da86"), event_id=16, version=0)
class Microsoft_Windows_AppModel_State_16_0(Etw):
    pattern = Struct(
        "PackageString" / WString,
        "UserSid" / WString,
        "Error" / Int32sl
    )


@declare(guid=guid("bff15e13-81bf-45ee-8b16-7cfead00da86"), event_id=17, version=0)
class Microsoft_Windows_AppModel_State_17_0(Etw):
    pattern = Struct(
        "PackageString" / WString,
        "UserSid" / WString,
        "Error" / Int32sl
    )


@declare(guid=guid("bff15e13-81bf-45ee-8b16-7cfead00da86"), event_id=18, version=0)
class Microsoft_Windows_AppModel_State_18_0(Etw):
    pattern = Struct(
        "InformationalString" / WString
    )


@declare(guid=guid("bff15e13-81bf-45ee-8b16-7cfead00da86"), event_id=19, version=0)
class Microsoft_Windows_AppModel_State_19_0(Etw):
    pattern = Struct(
        "ErrorString" / WString,
        "Error" / Int32sl
    )


@declare(guid=guid("bff15e13-81bf-45ee-8b16-7cfead00da86"), event_id=20, version=0)
class Microsoft_Windows_AppModel_State_20_0(Etw):
    pattern = Struct(
        "Operation" / WString,
        "PackageFamily" / WString,
        "OperationError" / Int32sl
    )


@declare(guid=guid("bff15e13-81bf-45ee-8b16-7cfead00da86"), event_id=21, version=0)
class Microsoft_Windows_AppModel_State_21_0(Etw):
    pattern = Struct(
        "Operation" / WString,
        "PackageFamily" / WString,
        "OperationError" / Int32sl,
        "RepairTriggerError" / Int32sl
    )


@declare(guid=guid("bff15e13-81bf-45ee-8b16-7cfead00da86"), event_id=22, version=0)
class Microsoft_Windows_AppModel_State_22_0(Etw):
    pattern = Struct(
        "FolderPath" / WString,
        "Error" / Int32sl
    )


@declare(guid=guid("bff15e13-81bf-45ee-8b16-7cfead00da86"), event_id=23, version=0)
class Microsoft_Windows_AppModel_State_23_0(Etw):
    pattern = Struct(
        "Operation" / WString,
        "PackageFamily" / WString,
        "OperationError" / Int32sl
    )


@declare(guid=guid("bff15e13-81bf-45ee-8b16-7cfead00da86"), event_id=24, version=0)
class Microsoft_Windows_AppModel_State_24_0(Etw):
    pattern = Struct(
        "Operation" / WString,
        "PackageFamily" / WString,
        "OperationError" / Int32sl,
        "RepairTriggerError" / Int32sl
    )

