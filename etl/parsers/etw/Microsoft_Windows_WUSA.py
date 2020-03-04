# -*- coding: utf-8 -*-
"""
Microsoft-Windows-WUSA
GUID : 09608c12-c1da-4104-a6fe-b959cf57560a
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("09608c12-c1da-4104-a6fe-b959cf57560a"), event_id=1, version=0)
class Microsoft_Windows_WUSA_1_0(Etw):
    pattern = Struct(
        "DebugMessage" / WString
    )


@declare(guid=guid("09608c12-c1da-4104-a6fe-b959cf57560a"), event_id=2, version=0)
class Microsoft_Windows_WUSA_2_0(Etw):
    pattern = Struct(
        "UpdateTitle" / WString,
        "CommandLine" / WString
    )


@declare(guid=guid("09608c12-c1da-4104-a6fe-b959cf57560a"), event_id=3, version=0)
class Microsoft_Windows_WUSA_3_0(Etw):
    pattern = Struct(
        "UpdateTitle" / WString,
        "ErrorCode" / Int32ul,
        "ErrorString" / WString,
        "CommandLine" / WString
    )


@declare(guid=guid("09608c12-c1da-4104-a6fe-b959cf57560a"), event_id=4, version=0)
class Microsoft_Windows_WUSA_4_0(Etw):
    pattern = Struct(
        "UpdateTitle" / WString,
        "CommandLine" / WString
    )


@declare(guid=guid("09608c12-c1da-4104-a6fe-b959cf57560a"), event_id=5, version=0)
class Microsoft_Windows_WUSA_5_0(Etw):
    pattern = Struct(
        "UpdateTitle" / WString,
        "CommandLine" / WString
    )


@declare(guid=guid("09608c12-c1da-4104-a6fe-b959cf57560a"), event_id=6, version=0)
class Microsoft_Windows_WUSA_6_0(Etw):
    pattern = Struct(
        "CommandLine" / WString
    )


@declare(guid=guid("09608c12-c1da-4104-a6fe-b959cf57560a"), event_id=7, version=0)
class Microsoft_Windows_WUSA_7_0(Etw):
    pattern = Struct(
        "UpdateTitle" / WString,
        "CommandLine" / WString
    )


@declare(guid=guid("09608c12-c1da-4104-a6fe-b959cf57560a"), event_id=8, version=0)
class Microsoft_Windows_WUSA_8_0(Etw):
    pattern = Struct(
        "UpdateTitle" / WString,
        "ErrorCode" / Int32ul,
        "ErrorString" / WString,
        "CommandLine" / WString
    )


@declare(guid=guid("09608c12-c1da-4104-a6fe-b959cf57560a"), event_id=9, version=0)
class Microsoft_Windows_WUSA_9_0(Etw):
    pattern = Struct(
        "UpdateTitle" / WString,
        "CommandLine" / WString
    )


@declare(guid=guid("09608c12-c1da-4104-a6fe-b959cf57560a"), event_id=10, version=0)
class Microsoft_Windows_WUSA_10_0(Etw):
    pattern = Struct(
        "UpdateTitle" / WString,
        "CommandLine" / WString
    )

