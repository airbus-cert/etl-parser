# -*- coding: utf-8 -*-
"""
Microsoft-Windows-OOBE-FirstLogonAnim
GUID : 2d4c0c5e-6704-493a-a44b-f5add4fc9283
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("2d4c0c5e-6704-493a-a44b-f5add4fc9283"), event_id=5005, version=0)
class Microsoft_Windows_OOBE_FirstLogonAnim_5005_0(Etw):
    pattern = Struct(
        "fZDP" / Int8ul
    )


@declare(guid=guid("2d4c0c5e-6704-493a-a44b-f5add4fc9283"), event_id=5041, version=0)
class Microsoft_Windows_OOBE_FirstLogonAnim_5041_0(Etw):
    pattern = Struct(
        "fOOBE" / Int8ul,
        "fExistingUser" / Int8ul,
        "fZDP" / Int8ul,
        "fExplorer" / Int8ul
    )


@declare(guid=guid("2d4c0c5e-6704-493a-a44b-f5add4fc9283"), event_id=5047, version=0)
class Microsoft_Windows_OOBE_FirstLogonAnim_5047_0(Etw):
    pattern = Struct(
        "fExistingUser" / Int8ul,
        "fPostZDP" / Int8ul
    )


@declare(guid=guid("2d4c0c5e-6704-493a-a44b-f5add4fc9283"), event_id=5048, version=0)
class Microsoft_Windows_OOBE_FirstLogonAnim_5048_0(Etw):
    pattern = Struct(
        "fExistingUserOrPostZDP" / Int8ul,
        "fZDP" / Int8ul,
        "fTouchDevice" / Int8ul,
        "fMouseDevice" / Int8ul
    )

