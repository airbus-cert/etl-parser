# -*- coding: utf-8 -*-
"""
Microsoft-Windows-HomeGroup-ControlPanel
GUID : 134ea407-755d-4a93-b8a6-f290cd155023
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("134ea407-755d-4a93-b8a6-f290cd155023"), event_id=5001, version=0)
class Microsoft_Windows_HomeGroup_ControlPanel_5001_0(Etw):
    pattern = Struct(
        "Error" / WString
    )


@declare(guid=guid("134ea407-755d-4a93-b8a6-f290cd155023"), event_id=5002, version=0)
class Microsoft_Windows_HomeGroup_ControlPanel_5002_0(Etw):
    pattern = Struct(
        "Error" / WString,
        "Message" / WString
    )


@declare(guid=guid("134ea407-755d-4a93-b8a6-f290cd155023"), event_id=5003, version=0)
class Microsoft_Windows_HomeGroup_ControlPanel_5003_0(Etw):
    pattern = Struct(
        "Error" / WString
    )


@declare(guid=guid("134ea407-755d-4a93-b8a6-f290cd155023"), event_id=5004, version=0)
class Microsoft_Windows_HomeGroup_ControlPanel_5004_0(Etw):
    pattern = Struct(
        "Error" / WString
    )


@declare(guid=guid("134ea407-755d-4a93-b8a6-f290cd155023"), event_id=5005, version=0)
class Microsoft_Windows_HomeGroup_ControlPanel_5005_0(Etw):
    pattern = Struct(
        "Error" / WString
    )


@declare(guid=guid("134ea407-755d-4a93-b8a6-f290cd155023"), event_id=5006, version=0)
class Microsoft_Windows_HomeGroup_ControlPanel_5006_0(Etw):
    pattern = Struct(
        "Error" / WString
    )


@declare(guid=guid("134ea407-755d-4a93-b8a6-f290cd155023"), event_id=5007, version=0)
class Microsoft_Windows_HomeGroup_ControlPanel_5007_0(Etw):
    pattern = Struct(
        "Error" / WString
    )


@declare(guid=guid("134ea407-755d-4a93-b8a6-f290cd155023"), event_id=5008, version=0)
class Microsoft_Windows_HomeGroup_ControlPanel_5008_0(Etw):
    pattern = Struct(
        "Error" / WString
    )


@declare(guid=guid("134ea407-755d-4a93-b8a6-f290cd155023"), event_id=5009, version=0)
class Microsoft_Windows_HomeGroup_ControlPanel_5009_0(Etw):
    pattern = Struct(
        "Error" / WString
    )


@declare(guid=guid("134ea407-755d-4a93-b8a6-f290cd155023"), event_id=5010, version=0)
class Microsoft_Windows_HomeGroup_ControlPanel_5010_0(Etw):
    pattern = Struct(
        "Error" / WString
    )


@declare(guid=guid("134ea407-755d-4a93-b8a6-f290cd155023"), event_id=5011, version=0)
class Microsoft_Windows_HomeGroup_ControlPanel_5011_0(Etw):
    pattern = Struct(
        "Error" / WString,
        "DWORD" / Int32ul
    )


@declare(guid=guid("134ea407-755d-4a93-b8a6-f290cd155023"), event_id=5012, version=0)
class Microsoft_Windows_HomeGroup_ControlPanel_5012_0(Etw):
    pattern = Struct(
        "Error" / WString,
        "DWORD" / Int32ul
    )


@declare(guid=guid("134ea407-755d-4a93-b8a6-f290cd155023"), event_id=5013, version=0)
class Microsoft_Windows_HomeGroup_ControlPanel_5013_0(Etw):
    pattern = Struct(
        "Error" / WString,
        "DWORD" / Int32ul
    )


@declare(guid=guid("134ea407-755d-4a93-b8a6-f290cd155023"), event_id=5014, version=0)
class Microsoft_Windows_HomeGroup_ControlPanel_5014_0(Etw):
    pattern = Struct(
        "Error" / WString,
        "DWORD" / Int32ul
    )


@declare(guid=guid("134ea407-755d-4a93-b8a6-f290cd155023"), event_id=5015, version=0)
class Microsoft_Windows_HomeGroup_ControlPanel_5015_0(Etw):
    pattern = Struct(
        "Error" / WString,
        "DWORD" / Int32ul
    )


@declare(guid=guid("134ea407-755d-4a93-b8a6-f290cd155023"), event_id=5016, version=0)
class Microsoft_Windows_HomeGroup_ControlPanel_5016_0(Etw):
    pattern = Struct(
        "Error" / WString,
        "guid" / Guid,
        "DWORD" / Int32ul
    )


@declare(guid=guid("134ea407-755d-4a93-b8a6-f290cd155023"), event_id=5017, version=0)
class Microsoft_Windows_HomeGroup_ControlPanel_5017_0(Etw):
    pattern = Struct(
        "Error" / WString
    )


@declare(guid=guid("134ea407-755d-4a93-b8a6-f290cd155023"), event_id=5018, version=0)
class Microsoft_Windows_HomeGroup_ControlPanel_5018_0(Etw):
    pattern = Struct(
        "Error" / WString,
        "DWORD" / Int32ul
    )


@declare(guid=guid("134ea407-755d-4a93-b8a6-f290cd155023"), event_id=5020, version=0)
class Microsoft_Windows_HomeGroup_ControlPanel_5020_0(Etw):
    pattern = Struct(
        "Error" / WString,
        "DWORD" / Int32ul
    )


@declare(guid=guid("134ea407-755d-4a93-b8a6-f290cd155023"), event_id=5021, version=0)
class Microsoft_Windows_HomeGroup_ControlPanel_5021_0(Etw):
    pattern = Struct(
        "Error" / WString
    )


@declare(guid=guid("134ea407-755d-4a93-b8a6-f290cd155023"), event_id=5022, version=0)
class Microsoft_Windows_HomeGroup_ControlPanel_5022_0(Etw):
    pattern = Struct(
        "Error" / WString
    )


@declare(guid=guid("134ea407-755d-4a93-b8a6-f290cd155023"), event_id=5025, version=0)
class Microsoft_Windows_HomeGroup_ControlPanel_5025_0(Etw):
    pattern = Struct(
        "Error" / WString
    )


@declare(guid=guid("134ea407-755d-4a93-b8a6-f290cd155023"), event_id=8001, version=0)
class Microsoft_Windows_HomeGroup_ControlPanel_8001_0(Etw):
    pattern = Struct(
        "hc_stateid" / Int32ul,
        "OldState" / WString,
        "NewState" / WString
    )

