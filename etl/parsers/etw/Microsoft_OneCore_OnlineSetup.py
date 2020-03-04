# -*- coding: utf-8 -*-
"""
Microsoft-OneCore-OnlineSetup
GUID : 41862974-da3b-4f0b-97d5-bb29fbb9b71e
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("41862974-da3b-4f0b-97d5-bb29fbb9b71e"), event_id=1001, version=0)
class Microsoft_OneCore_OnlineSetup_1001_0(Etw):
    pattern = Struct(
        "CommandLine" / WString
    )


@declare(guid=guid("41862974-da3b-4f0b-97d5-bb29fbb9b71e"), event_id=1002, version=0)
class Microsoft_OneCore_OnlineSetup_1002_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("41862974-da3b-4f0b-97d5-bb29fbb9b71e"), event_id=2001, version=0)
class Microsoft_OneCore_OnlineSetup_2001_0(Etw):
    pattern = Struct(
        "Pass" / WString
    )


@declare(guid=guid("41862974-da3b-4f0b-97d5-bb29fbb9b71e"), event_id=2002, version=0)
class Microsoft_OneCore_OnlineSetup_2002_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("41862974-da3b-4f0b-97d5-bb29fbb9b71e"), event_id=2003, version=0)
class Microsoft_OneCore_OnlineSetup_2003_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("41862974-da3b-4f0b-97d5-bb29fbb9b71e"), event_id=2004, version=0)
class Microsoft_OneCore_OnlineSetup_2004_0(Etw):
    pattern = Struct(
        "Pass" / WString,
        "FilePath" / WString
    )

