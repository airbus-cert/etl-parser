# -*- coding: utf-8 -*-
"""
Microsoft-Windows-International-RegionalOptionsControlPanel
GUID : c6bf6832-f7bd-4151-ac21-753ce4707453
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("c6bf6832-f7bd-4151-ac21-753ce4707453"), event_id=15000, version=0)
class Microsoft_Windows_International_RegionalOptionsControlPanel_15000_0(Etw):
    pattern = Struct(
        "LocaleName" / WString
    )


@declare(guid=guid("c6bf6832-f7bd-4151-ac21-753ce4707453"), event_id=15001, version=0)
class Microsoft_Windows_International_RegionalOptionsControlPanel_15001_0(Etw):
    pattern = Struct(
        "LocaleName" / WString
    )


@declare(guid=guid("c6bf6832-f7bd-4151-ac21-753ce4707453"), event_id=15002, version=0)
class Microsoft_Windows_International_RegionalOptionsControlPanel_15002_0(Etw):
    pattern = Struct(
        "LCType" / WString,
        "Data" / WString
    )


@declare(guid=guid("c6bf6832-f7bd-4151-ac21-753ce4707453"), event_id=15003, version=0)
class Microsoft_Windows_International_RegionalOptionsControlPanel_15003_0(Etw):
    pattern = Struct(
        "LocaleName" / WString
    )


@declare(guid=guid("c6bf6832-f7bd-4151-ac21-753ce4707453"), event_id=15004, version=0)
class Microsoft_Windows_International_RegionalOptionsControlPanel_15004_0(Etw):
    pattern = Struct(
        "String" / WString
    )


@declare(guid=guid("c6bf6832-f7bd-4151-ac21-753ce4707453"), event_id=15005, version=0)
class Microsoft_Windows_International_RegionalOptionsControlPanel_15005_0(Etw):
    pattern = Struct(
        "String" / WString
    )


@declare(guid=guid("c6bf6832-f7bd-4151-ac21-753ce4707453"), event_id=15006, version=0)
class Microsoft_Windows_International_RegionalOptionsControlPanel_15006_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("c6bf6832-f7bd-4151-ac21-753ce4707453"), event_id=15007, version=0)
class Microsoft_Windows_International_RegionalOptionsControlPanel_15007_0(Etw):
    pattern = Struct(
        "LocaleName" / WString
    )


@declare(guid=guid("c6bf6832-f7bd-4151-ac21-753ce4707453"), event_id=15010, version=0)
class Microsoft_Windows_International_RegionalOptionsControlPanel_15010_0(Etw):
    pattern = Struct(
        "LocaleName" / WString
    )


@declare(guid=guid("c6bf6832-f7bd-4151-ac21-753ce4707453"), event_id=15011, version=0)
class Microsoft_Windows_International_RegionalOptionsControlPanel_15011_0(Etw):
    pattern = Struct(
        "LocaleName" / WString
    )


@declare(guid=guid("c6bf6832-f7bd-4151-ac21-753ce4707453"), event_id=16000, version=0)
class Microsoft_Windows_International_RegionalOptionsControlPanel_16000_0(Etw):
    pattern = Struct(
        "LocaleName" / WString,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("c6bf6832-f7bd-4151-ac21-753ce4707453"), event_id=16001, version=0)
class Microsoft_Windows_International_RegionalOptionsControlPanel_16001_0(Etw):
    pattern = Struct(
        "LocaleName" / WString,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("c6bf6832-f7bd-4151-ac21-753ce4707453"), event_id=16002, version=0)
class Microsoft_Windows_International_RegionalOptionsControlPanel_16002_0(Etw):
    pattern = Struct(
        "LocaleName" / WString
    )

