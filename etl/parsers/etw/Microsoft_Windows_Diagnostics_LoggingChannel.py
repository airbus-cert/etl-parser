# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Diagnostics-LoggingChannel
GUID : 4bd2826e-54a1-4ba9-bf63-92b73ea1ac4a
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("4bd2826e-54a1-4ba9-bf63-92b73ea1ac4a"), event_id=1, version=0)
class Microsoft_Windows_Diagnostics_LoggingChannel_1_0(Etw):
    pattern = Struct(
        "LoggingChannelName" / WString,
        "StringMessage" / WString
    )


@declare(guid=guid("4bd2826e-54a1-4ba9-bf63-92b73ea1ac4a"), event_id=2, version=0)
class Microsoft_Windows_Diagnostics_LoggingChannel_2_0(Etw):
    pattern = Struct(
        "LoggingChannelName" / WString,
        "StringMessage" / WString
    )


@declare(guid=guid("4bd2826e-54a1-4ba9-bf63-92b73ea1ac4a"), event_id=3, version=0)
class Microsoft_Windows_Diagnostics_LoggingChannel_3_0(Etw):
    pattern = Struct(
        "LoggingChannelName" / WString,
        "StringMessage" / WString
    )


@declare(guid=guid("4bd2826e-54a1-4ba9-bf63-92b73ea1ac4a"), event_id=4, version=0)
class Microsoft_Windows_Diagnostics_LoggingChannel_4_0(Etw):
    pattern = Struct(
        "LoggingChannelName" / WString,
        "StringMessage" / WString
    )


@declare(guid=guid("4bd2826e-54a1-4ba9-bf63-92b73ea1ac4a"), event_id=5, version=0)
class Microsoft_Windows_Diagnostics_LoggingChannel_5_0(Etw):
    pattern = Struct(
        "LoggingChannelName" / WString,
        "StringMessage" / WString
    )


@declare(guid=guid("4bd2826e-54a1-4ba9-bf63-92b73ea1ac4a"), event_id=6, version=0)
class Microsoft_Windows_Diagnostics_LoggingChannel_6_0(Etw):
    pattern = Struct(
        "LoggingChannelName" / WString,
        "StringValue" / WString,
        "IntegerValue" / Int32sl
    )


@declare(guid=guid("4bd2826e-54a1-4ba9-bf63-92b73ea1ac4a"), event_id=7, version=0)
class Microsoft_Windows_Diagnostics_LoggingChannel_7_0(Etw):
    pattern = Struct(
        "LoggingChannelName" / WString,
        "StringValue" / WString,
        "IntegerValue" / Int32sl
    )


@declare(guid=guid("4bd2826e-54a1-4ba9-bf63-92b73ea1ac4a"), event_id=8, version=0)
class Microsoft_Windows_Diagnostics_LoggingChannel_8_0(Etw):
    pattern = Struct(
        "LoggingChannelName" / WString,
        "StringValue" / WString,
        "IntegerValue" / Int32sl
    )


@declare(guid=guid("4bd2826e-54a1-4ba9-bf63-92b73ea1ac4a"), event_id=9, version=0)
class Microsoft_Windows_Diagnostics_LoggingChannel_9_0(Etw):
    pattern = Struct(
        "LoggingChannelName" / WString,
        "StringValue" / WString,
        "IntegerValue" / Int32sl
    )


@declare(guid=guid("4bd2826e-54a1-4ba9-bf63-92b73ea1ac4a"), event_id=10, version=0)
class Microsoft_Windows_Diagnostics_LoggingChannel_10_0(Etw):
    pattern = Struct(
        "LoggingChannelName" / WString,
        "StringValue" / WString,
        "IntegerValue" / Int32sl
    )


@declare(guid=guid("4bd2826e-54a1-4ba9-bf63-92b73ea1ac4a"), event_id=11, version=0)
class Microsoft_Windows_Diagnostics_LoggingChannel_11_0(Etw):
    pattern = Struct(
        "LoggingChannelName" / WString,
        "ActivityName" / WString
    )


@declare(guid=guid("4bd2826e-54a1-4ba9-bf63-92b73ea1ac4a"), event_id=12, version=0)
class Microsoft_Windows_Diagnostics_LoggingChannel_12_0(Etw):
    pattern = Struct(
        "LoggingChannelName" / WString,
        "ActivityName" / WString
    )


@declare(guid=guid("4bd2826e-54a1-4ba9-bf63-92b73ea1ac4a"), event_id=13, version=0)
class Microsoft_Windows_Diagnostics_LoggingChannel_13_0(Etw):
    pattern = Struct(
        "LoggingChannelName" / WString,
        "ActivityName" / WString
    )


@declare(guid=guid("4bd2826e-54a1-4ba9-bf63-92b73ea1ac4a"), event_id=14, version=0)
class Microsoft_Windows_Diagnostics_LoggingChannel_14_0(Etw):
    pattern = Struct(
        "LoggingChannelName" / WString,
        "ActivityName" / WString
    )


@declare(guid=guid("4bd2826e-54a1-4ba9-bf63-92b73ea1ac4a"), event_id=15, version=0)
class Microsoft_Windows_Diagnostics_LoggingChannel_15_0(Etw):
    pattern = Struct(
        "LoggingChannelName" / WString,
        "ActivityName" / WString
    )


@declare(guid=guid("4bd2826e-54a1-4ba9-bf63-92b73ea1ac4a"), event_id=16, version=0)
class Microsoft_Windows_Diagnostics_LoggingChannel_16_0(Etw):
    pattern = Struct(
        "LoggingChannelName" / WString,
        "ActivityName" / WString
    )


@declare(guid=guid("4bd2826e-54a1-4ba9-bf63-92b73ea1ac4a"), event_id=17, version=0)
class Microsoft_Windows_Diagnostics_LoggingChannel_17_0(Etw):
    pattern = Struct(
        "LoggingChannelName" / WString,
        "ActivityName" / WString
    )


@declare(guid=guid("4bd2826e-54a1-4ba9-bf63-92b73ea1ac4a"), event_id=18, version=0)
class Microsoft_Windows_Diagnostics_LoggingChannel_18_0(Etw):
    pattern = Struct(
        "LoggingChannelName" / WString,
        "ActivityName" / WString
    )


@declare(guid=guid("4bd2826e-54a1-4ba9-bf63-92b73ea1ac4a"), event_id=19, version=0)
class Microsoft_Windows_Diagnostics_LoggingChannel_19_0(Etw):
    pattern = Struct(
        "LoggingChannelName" / WString,
        "ActivityName" / WString
    )


@declare(guid=guid("4bd2826e-54a1-4ba9-bf63-92b73ea1ac4a"), event_id=20, version=0)
class Microsoft_Windows_Diagnostics_LoggingChannel_20_0(Etw):
    pattern = Struct(
        "LoggingChannelName" / WString,
        "ActivityName" / WString
    )

