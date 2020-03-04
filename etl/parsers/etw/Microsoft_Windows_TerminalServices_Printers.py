# -*- coding: utf-8 -*-
"""
Microsoft-Windows-TerminalServices-Printers
GUID : 952773bf-c2b7-49bc-88f4-920744b82c43
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("952773bf-c2b7-49bc-88f4-920744b82c43"), event_id=1100, version=0)
class Microsoft_Windows_TerminalServices_Printers_1100_0(Etw):
    pattern = Struct(
        "Param1" / WString
    )


@declare(guid=guid("952773bf-c2b7-49bc-88f4-920744b82c43"), event_id=1102, version=0)
class Microsoft_Windows_TerminalServices_Printers_1102_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString
    )


@declare(guid=guid("952773bf-c2b7-49bc-88f4-920744b82c43"), event_id=1105, version=0)
class Microsoft_Windows_TerminalServices_Printers_1105_0(Etw):
    pattern = Struct(
        "Param1" / WString
    )


@declare(guid=guid("952773bf-c2b7-49bc-88f4-920744b82c43"), event_id=1107, version=0)
class Microsoft_Windows_TerminalServices_Printers_1107_0(Etw):
    pattern = Struct(
        "Param1" / WString
    )


@declare(guid=guid("952773bf-c2b7-49bc-88f4-920744b82c43"), event_id=1108, version=0)
class Microsoft_Windows_TerminalServices_Printers_1108_0(Etw):
    pattern = Struct(
        "Param1" / WString
    )


@declare(guid=guid("952773bf-c2b7-49bc-88f4-920744b82c43"), event_id=1109, version=0)
class Microsoft_Windows_TerminalServices_Printers_1109_0(Etw):
    pattern = Struct(
        "Param1" / WString
    )


@declare(guid=guid("952773bf-c2b7-49bc-88f4-920744b82c43"), event_id=1110, version=0)
class Microsoft_Windows_TerminalServices_Printers_1110_0(Etw):
    pattern = Struct(
        "Param1" / WString
    )


@declare(guid=guid("952773bf-c2b7-49bc-88f4-920744b82c43"), event_id=1111, version=0)
class Microsoft_Windows_TerminalServices_Printers_1111_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString
    )


@declare(guid=guid("952773bf-c2b7-49bc-88f4-920744b82c43"), event_id=1116, version=0)
class Microsoft_Windows_TerminalServices_Printers_1116_0(Etw):
    pattern = Struct(
        "Param1" / WString
    )


@declare(guid=guid("952773bf-c2b7-49bc-88f4-920744b82c43"), event_id=1123, version=0)
class Microsoft_Windows_TerminalServices_Printers_1123_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString
    )


@declare(guid=guid("952773bf-c2b7-49bc-88f4-920744b82c43"), event_id=1124, version=0)
class Microsoft_Windows_TerminalServices_Printers_1124_0(Etw):
    pattern = Struct(
        "Param1" / WString,
        "Param2" / WString
    )

