# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Bluetooth-Bthmini
GUID : db25b328-a6f6-444f-9d97-a50e20217d16
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("db25b328-a6f6-444f-9d97-a50e20217d16"), event_id=200, version=0)
class Microsoft_Windows_Bluetooth_Bthmini_200_0(Etw):
    pattern = Struct(
        "Major" / Int32ul,
        "Minor" / Int32ul,
        "Service" / Int32ul
    )


@declare(guid=guid("db25b328-a6f6-444f-9d97-a50e20217d16"), event_id=201, version=0)
class Microsoft_Windows_Bluetooth_Bthmini_201_0(Etw):
    pattern = Struct(
        "ExpectedLengthMin" / Int32ul,
        "ExpectedLengthMax" / Int32ul,
        "ActualLength" / Int32ul
    )


@declare(guid=guid("db25b328-a6f6-444f-9d97-a50e20217d16"), event_id=202, version=0)
class Microsoft_Windows_Bluetooth_Bthmini_202_0(Etw):
    pattern = Struct(
        "ExpectedLengthMin" / Int32ul,
        "ExpectedLengthMax" / Int32ul,
        "ActualLength" / Int32ul
    )

