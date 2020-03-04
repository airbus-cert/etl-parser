# -*- coding: utf-8 -*-
"""
Microsoft-Windows-COMRuntime
GUID : bf406804-6afa-46e7-8a48-6c357e1d6d61
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("bf406804-6afa-46e7-8a48-6c357e1d6d61"), event_id=1, version=0)
class Microsoft_Windows_COMRuntime_1_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul,
        "BlockTimeMs" / Int32ul,
        "TotalTimeMs" / Int32ul
    )


@declare(guid=guid("bf406804-6afa-46e7-8a48-6c357e1d6d61"), event_id=2, version=0)
class Microsoft_Windows_COMRuntime_2_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul,
        "CallTimeMs" / Int32ul,
        "CallResult" / Int32ul,
        "TargetThreadId" / Int32ul,
        "TargetProcessId" / Int32ul,
        "TargetMethod" / Int32ul,
        "TargetInterface" / Guid
    )


@declare(guid=guid("bf406804-6afa-46e7-8a48-6c357e1d6d61"), event_id=3, version=0)
class Microsoft_Windows_COMRuntime_3_0(Etw):
    pattern = Struct(
        "ApartmentType" / Int32ul
    )


@declare(guid=guid("bf406804-6afa-46e7-8a48-6c357e1d6d61"), event_id=4, version=0)
class Microsoft_Windows_COMRuntime_4_0(Etw):
    pattern = Struct(
        "ApartmentType" / Int32ul
    )


@declare(guid=guid("bf406804-6afa-46e7-8a48-6c357e1d6d61"), event_id=5, version=0)
class Microsoft_Windows_COMRuntime_5_0(Etw):
    pattern = Struct(
        "ApartmentType" / Int32ul
    )


@declare(guid=guid("bf406804-6afa-46e7-8a48-6c357e1d6d61"), event_id=6, version=0)
class Microsoft_Windows_COMRuntime_6_0(Etw):
    pattern = Struct(
        "ApartmentType" / Int32ul,
        "Message" / Int32ul
    )


@declare(guid=guid("bf406804-6afa-46e7-8a48-6c357e1d6d61"), event_id=7, version=0)
class Microsoft_Windows_COMRuntime_7_0(Etw):
    pattern = Struct(
        "IID" / Guid,
        "Method" / Int32ul,
        "IPID" / Guid,
        "CallType" / Int32ul
    )


@declare(guid=guid("bf406804-6afa-46e7-8a48-6c357e1d6d61"), event_id=18205, version=0)
class Microsoft_Windows_COMRuntime_18205_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )


@declare(guid=guid("bf406804-6afa-46e7-8a48-6c357e1d6d61"), event_id=18207, version=0)
class Microsoft_Windows_COMRuntime_18207_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "param5" / WString,
        "param6" / WString,
        "param7" / WString,
        "param8" / WString,
        "param9" / WString,
        "param10" / WString
    )


@declare(guid=guid("bf406804-6afa-46e7-8a48-6c357e1d6d61"), event_id=18208, version=0)
class Microsoft_Windows_COMRuntime_18208_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "param5" / WString,
        "param6" / WString,
        "param7" / WString,
        "param8" / WString,
        "param9" / WString,
        "param10" / WString,
        "param11" / WString
    )


@declare(guid=guid("bf406804-6afa-46e7-8a48-6c357e1d6d61"), event_id=18209, version=0)
class Microsoft_Windows_COMRuntime_18209_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "param5" / WString,
        "param6" / WString,
        "param7" / WString,
        "param8" / WString,
        "param9" / WString,
        "param10" / WString
    )


@declare(guid=guid("bf406804-6afa-46e7-8a48-6c357e1d6d61"), event_id=18210, version=0)
class Microsoft_Windows_COMRuntime_18210_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "param5" / WString,
        "param6" / WString,
        "param7" / WString,
        "param8" / WString,
        "param9" / WString
    )


@declare(guid=guid("bf406804-6afa-46e7-8a48-6c357e1d6d61"), event_id=18211, version=0)
class Microsoft_Windows_COMRuntime_18211_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "param5" / WString,
        "param6" / WString,
        "param7" / WString,
        "param8" / WString,
        "param9" / WString
    )


@declare(guid=guid("bf406804-6afa-46e7-8a48-6c357e1d6d61"), event_id=18212, version=0)
class Microsoft_Windows_COMRuntime_18212_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("bf406804-6afa-46e7-8a48-6c357e1d6d61"), event_id=18213, version=0)
class Microsoft_Windows_COMRuntime_18213_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("bf406804-6afa-46e7-8a48-6c357e1d6d61"), event_id=18214, version=0)
class Microsoft_Windows_COMRuntime_18214_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )


@declare(guid=guid("bf406804-6afa-46e7-8a48-6c357e1d6d61"), event_id=18215, version=0)
class Microsoft_Windows_COMRuntime_18215_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("bf406804-6afa-46e7-8a48-6c357e1d6d61"), event_id=18216, version=0)
class Microsoft_Windows_COMRuntime_18216_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("bf406804-6afa-46e7-8a48-6c357e1d6d61"), event_id=18219, version=0)
class Microsoft_Windows_COMRuntime_18219_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "param5" / WString,
        "param6" / WString,
        "param7" / WString,
        "param8" / WString
    )


@declare(guid=guid("bf406804-6afa-46e7-8a48-6c357e1d6d61"), event_id=18220, version=0)
class Microsoft_Windows_COMRuntime_18220_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("bf406804-6afa-46e7-8a48-6c357e1d6d61"), event_id=18221, version=0)
class Microsoft_Windows_COMRuntime_18221_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "param5" / WString,
        "param6" / WString
    )


@declare(guid=guid("bf406804-6afa-46e7-8a48-6c357e1d6d61"), event_id=32769, version=0)
class Microsoft_Windows_COMRuntime_32769_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )

