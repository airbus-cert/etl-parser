# -*- coding: utf-8 -*-
"""
Microsoft-Windows-GPIO-ClassExtension
GUID : 55ab77f6-fa04-43ef-af45-688fbf500482
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("55ab77f6-fa04-43ef-af45-688fbf500482"), event_id=1000, version=1)
class Microsoft_Windows_GPIO_ClassExtension_1000_1(Etw):
    pattern = Struct(
        "ControllerBiosName" / WString,
        "BankId" / Int16ul,
        "PinNumber" / Int16ul
    )


@declare(guid=guid("55ab77f6-fa04-43ef-af45-688fbf500482"), event_id=1001, version=1)
class Microsoft_Windows_GPIO_ClassExtension_1001_1(Etw):
    pattern = Struct(
        "PinNumber" / Int16ul
    )


@declare(guid=guid("55ab77f6-fa04-43ef-af45-688fbf500482"), event_id=1002, version=1)
class Microsoft_Windows_GPIO_ClassExtension_1002_1(Etw):
    pattern = Struct(
        "ControllerBiosName" / WString,
        "BankId" / Int16ul,
        "PinMask" / Int64ul
    )


@declare(guid=guid("55ab77f6-fa04-43ef-af45-688fbf500482"), event_id=1003, version=1)
class Microsoft_Windows_GPIO_ClassExtension_1003_1(Etw):
    pattern = Struct(
        "PinMask" / Int64ul
    )


@declare(guid=guid("55ab77f6-fa04-43ef-af45-688fbf500482"), event_id=1004, version=1)
class Microsoft_Windows_GPIO_ClassExtension_1004_1(Etw):
    pattern = Struct(
        "ControllerBiosName" / WString,
        "BankId" / Int16ul,
        "PinNumber" / Int16ul,
        "Timeout" / Int16ul
    )


@declare(guid=guid("55ab77f6-fa04-43ef-af45-688fbf500482"), event_id=1005, version=1)
class Microsoft_Windows_GPIO_ClassExtension_1005_1(Etw):
    pattern = Struct(
        "PinNumber" / Int16ul
    )


@declare(guid=guid("55ab77f6-fa04-43ef-af45-688fbf500482"), event_id=1006, version=1)
class Microsoft_Windows_GPIO_ClassExtension_1006_1(Etw):
    pattern = Struct(
        "ControllerBiosName" / WString,
        "BankId" / Int16ul
    )


@declare(guid=guid("55ab77f6-fa04-43ef-af45-688fbf500482"), event_id=1008, version=1)
class Microsoft_Windows_GPIO_ClassExtension_1008_1(Etw):
    pattern = Struct(
        "ControllerBiosName" / WString,
        "BankId" / Int16ul,
        "PinNumber" / Int16ul
    )


@declare(guid=guid("55ab77f6-fa04-43ef-af45-688fbf500482"), event_id=1009, version=1)
class Microsoft_Windows_GPIO_ClassExtension_1009_1(Etw):
    pattern = Struct(
        "PinNumber" / Int16ul
    )


@declare(guid=guid("55ab77f6-fa04-43ef-af45-688fbf500482"), event_id=1010, version=1)
class Microsoft_Windows_GPIO_ClassExtension_1010_1(Etw):
    pattern = Struct(
        "ControllerBiosName" / WString,
        "BankId" / Int16ul,
        "PinNumber" / Int16ul
    )


@declare(guid=guid("55ab77f6-fa04-43ef-af45-688fbf500482"), event_id=1011, version=1)
class Microsoft_Windows_GPIO_ClassExtension_1011_1(Etw):
    pattern = Struct(
        "PinNumber" / Int16ul
    )


@declare(guid=guid("55ab77f6-fa04-43ef-af45-688fbf500482"), event_id=1012, version=1)
class Microsoft_Windows_GPIO_ClassExtension_1012_1(Etw):
    pattern = Struct(
        "PinNumber" / Int16ul,
        "Gsiv" / Int32ul
    )


@declare(guid=guid("55ab77f6-fa04-43ef-af45-688fbf500482"), event_id=1014, version=1)
class Microsoft_Windows_GPIO_ClassExtension_1014_1(Etw):
    pattern = Struct(
        "EnableRegister" / Int64ul,
        "MaskRegister" / Int64ul,
        "StatusRegister" / Int64ul,
        "NonEnabledActiveInterrupts" / Int64ul,
        "ReplayRegister" / Int64ul
    )


@declare(guid=guid("55ab77f6-fa04-43ef-af45-688fbf500482"), event_id=1015, version=1)
class Microsoft_Windows_GPIO_ClassExtension_1015_1(Etw):
    pattern = Struct(
        "ControllerBiosName" / WString,
        "BankId" / Int16ul,
        "Gsiv" / Int32ul
    )


@declare(guid=guid("55ab77f6-fa04-43ef-af45-688fbf500482"), event_id=1017, version=1)
class Microsoft_Windows_GPIO_ClassExtension_1017_1(Etw):
    pattern = Struct(
        "ControllerBiosName" / WString,
        "BankId" / Int16ul,
        "PinMask" / Int64ul
    )


@declare(guid=guid("55ab77f6-fa04-43ef-af45-688fbf500482"), event_id=1018, version=1)
class Microsoft_Windows_GPIO_ClassExtension_1018_1(Etw):
    pattern = Struct(
        "PinMask" / Int64ul
    )


@declare(guid=guid("55ab77f6-fa04-43ef-af45-688fbf500482"), event_id=1019, version=1)
class Microsoft_Windows_GPIO_ClassExtension_1019_1(Etw):
    pattern = Struct(
        "ControllerBiosName" / WString,
        "BankId" / Int16ul
    )


@declare(guid=guid("55ab77f6-fa04-43ef-af45-688fbf500482"), event_id=1021, version=1)
class Microsoft_Windows_GPIO_ClassExtension_1021_1(Etw):
    pattern = Struct(
        "ControllerBiosName" / WString,
        "BankId" / Int16ul
    )


@declare(guid=guid("55ab77f6-fa04-43ef-af45-688fbf500482"), event_id=1023, version=1)
class Microsoft_Windows_GPIO_ClassExtension_1023_1(Etw):
    pattern = Struct(
        "ControllerBiosName" / WString,
        "BankId" / Int16ul,
        "PinNumber" / Int16ul
    )


@declare(guid=guid("55ab77f6-fa04-43ef-af45-688fbf500482"), event_id=1024, version=1)
class Microsoft_Windows_GPIO_ClassExtension_1024_1(Etw):
    pattern = Struct(
        "PinNumber" / Int16ul
    )


@declare(guid=guid("55ab77f6-fa04-43ef-af45-688fbf500482"), event_id=1025, version=1)
class Microsoft_Windows_GPIO_ClassExtension_1025_1(Etw):
    pattern = Struct(
        "ControllerBiosName" / WString,
        "BankId" / Int16ul,
        "PinNumber" / Int16ul
    )


@declare(guid=guid("55ab77f6-fa04-43ef-af45-688fbf500482"), event_id=1026, version=1)
class Microsoft_Windows_GPIO_ClassExtension_1026_1(Etw):
    pattern = Struct(
        "PinNumber" / Int16ul
    )


@declare(guid=guid("55ab77f6-fa04-43ef-af45-688fbf500482"), event_id=1027, version=1)
class Microsoft_Windows_GPIO_ClassExtension_1027_1(Etw):
    pattern = Struct(
        "PinNumber" / Int16ul,
        "Gsiv" / Int32ul
    )

