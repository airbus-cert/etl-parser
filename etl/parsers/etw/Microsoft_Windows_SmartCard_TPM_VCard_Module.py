# -*- coding: utf-8 -*-
"""
Microsoft-Windows-SmartCard-TPM-VCard-Module
GUID : 125f2cf1-2768-4d33-976e-527137d080f8
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("125f2cf1-2768-4d33-976e-527137d080f8"), event_id=1101, version=0)
class Microsoft_Windows_SmartCard_TPM_VCard_Module_1101_0(Etw):
    pattern = Struct(
        "Path" / WString,
        "WinError" / Int32ul
    )


@declare(guid=guid("125f2cf1-2768-4d33-976e-527137d080f8"), event_id=1102, version=0)
class Microsoft_Windows_SmartCard_TPM_VCard_Module_1102_0(Etw):
    pattern = Struct(
        "Path" / WString
    )


@declare(guid=guid("125f2cf1-2768-4d33-976e-527137d080f8"), event_id=1103, version=0)
class Microsoft_Windows_SmartCard_TPM_VCard_Module_1103_0(Etw):
    pattern = Struct(
        "Path" / WString
    )


@declare(guid=guid("125f2cf1-2768-4d33-976e-527137d080f8"), event_id=1104, version=0)
class Microsoft_Windows_SmartCard_TPM_VCard_Module_1104_0(Etw):
    pattern = Struct(
        "WinError" / Int32ul
    )


@declare(guid=guid("125f2cf1-2768-4d33-976e-527137d080f8"), event_id=2101, version=0)
class Microsoft_Windows_SmartCard_TPM_VCard_Module_2101_0(Etw):
    pattern = Struct(
        "Context" / Int64ul
    )


@declare(guid=guid("125f2cf1-2768-4d33-976e-527137d080f8"), event_id=2102, version=0)
class Microsoft_Windows_SmartCard_TPM_VCard_Module_2102_0(Etw):
    pattern = Struct(
        "Context" / Int64ul
    )


@declare(guid=guid("125f2cf1-2768-4d33-976e-527137d080f8"), event_id=2103, version=0)
class Microsoft_Windows_SmartCard_TPM_VCard_Module_2103_0(Etw):
    pattern = Struct(
        "Context" / Int64ul,
        "WinError" / Int32ul
    )


@declare(guid=guid("125f2cf1-2768-4d33-976e-527137d080f8"), event_id=2104, version=0)
class Microsoft_Windows_SmartCard_TPM_VCard_Module_2104_0(Etw):
    pattern = Struct(
        "Context" / Int64ul
    )


@declare(guid=guid("125f2cf1-2768-4d33-976e-527137d080f8"), event_id=2105, version=0)
class Microsoft_Windows_SmartCard_TPM_VCard_Module_2105_0(Etw):
    pattern = Struct(
        "Context" / Int64ul
    )


@declare(guid=guid("125f2cf1-2768-4d33-976e-527137d080f8"), event_id=2106, version=0)
class Microsoft_Windows_SmartCard_TPM_VCard_Module_2106_0(Etw):
    pattern = Struct(
        "Context" / Int64ul
    )


@declare(guid=guid("125f2cf1-2768-4d33-976e-527137d080f8"), event_id=2107, version=0)
class Microsoft_Windows_SmartCard_TPM_VCard_Module_2107_0(Etw):
    pattern = Struct(
        "Context" / Int64ul
    )

