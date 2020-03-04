# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Bluetooth-BthLEPrepairing
GUID : 4af188ac-e9c4-4c11-b07b-1fabc07dfeb2
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("4af188ac-e9c4-4c11-b07b-1fabc07dfeb2"), event_id=100, version=0)
class Microsoft_Windows_Bluetooth_BthLEPrepairing_100_0(Etw):
    pattern = Struct(

    )

