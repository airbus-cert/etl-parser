# -*- coding: utf-8 -*-
"""
Microsoft-Windows-EapMethods-Sim
GUID : 3d42a67d-9ce8-4284-b755-2550672b0ce0
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("3d42a67d-9ce8-4284-b755-2550672b0ce0"), event_id=100, version=0)
class Microsoft_Windows_EapMethods_Sim_100_0(Etw):
    pattern = Struct(
        "MethodName" / WString,
        "ErrorCause" / WString
    )


@declare(guid=guid("3d42a67d-9ce8-4284-b755-2550672b0ce0"), event_id=101, version=0)
class Microsoft_Windows_EapMethods_Sim_101_0(Etw):
    pattern = Struct(
        "MethodName" / WString,
        "ErrorCause" / WString
    )


@declare(guid=guid("3d42a67d-9ce8-4284-b755-2550672b0ce0"), event_id=102, version=0)
class Microsoft_Windows_EapMethods_Sim_102_0(Etw):
    pattern = Struct(
        "MethodName" / WString,
        "ErrorCause" / WString
    )


@declare(guid=guid("3d42a67d-9ce8-4284-b755-2550672b0ce0"), event_id=103, version=0)
class Microsoft_Windows_EapMethods_Sim_103_0(Etw):
    pattern = Struct(
        "MethodName" / WString
    )


@declare(guid=guid("3d42a67d-9ce8-4284-b755-2550672b0ce0"), event_id=104, version=0)
class Microsoft_Windows_EapMethods_Sim_104_0(Etw):
    pattern = Struct(
        "MethodName" / WString
    )

