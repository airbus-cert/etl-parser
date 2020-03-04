# -*- coding: utf-8 -*-
"""
Microsoft-Windows-TabletPC-MathInput
GUID : 8443ccb7-feb0-4b8d-8e28-8d4c7cb814e8
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("8443ccb7-feb0-4b8d-8e28-8d4c7cb814e8"), event_id=3, version=0)
class Microsoft_Windows_TabletPC_MathInput_3_0(Etw):
    pattern = Struct(
        "intvalue" / Int32ul
    )


@declare(guid=guid("8443ccb7-feb0-4b8d-8e28-8d4c7cb814e8"), event_id=24, version=0)
class Microsoft_Windows_TabletPC_MathInput_24_0(Etw):
    pattern = Struct(
        "intvalue" / Int32ul
    )


@declare(guid=guid("8443ccb7-feb0-4b8d-8e28-8d4c7cb814e8"), event_id=25, version=0)
class Microsoft_Windows_TabletPC_MathInput_25_0(Etw):
    pattern = Struct(
        "intvalue" / Int32ul
    )


@declare(guid=guid("8443ccb7-feb0-4b8d-8e28-8d4c7cb814e8"), event_id=26, version=0)
class Microsoft_Windows_TabletPC_MathInput_26_0(Etw):
    pattern = Struct(
        "intvalue" / Int32ul
    )


@declare(guid=guid("8443ccb7-feb0-4b8d-8e28-8d4c7cb814e8"), event_id=29, version=0)
class Microsoft_Windows_TabletPC_MathInput_29_0(Etw):
    pattern = Struct(
        "intvalue" / Int32ul
    )


@declare(guid=guid("8443ccb7-feb0-4b8d-8e28-8d4c7cb814e8"), event_id=32, version=0)
class Microsoft_Windows_TabletPC_MathInput_32_0(Etw):
    pattern = Struct(
        "intvalue" / Int32ul
    )


@declare(guid=guid("8443ccb7-feb0-4b8d-8e28-8d4c7cb814e8"), event_id=33, version=0)
class Microsoft_Windows_TabletPC_MathInput_33_0(Etw):
    pattern = Struct(
        "intvalue" / Int32ul
    )

