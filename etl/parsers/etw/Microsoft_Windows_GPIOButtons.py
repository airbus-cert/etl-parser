# -*- coding: utf-8 -*-
"""
Microsoft-Windows-GPIOButtons
GUID : e13ff11e-e989-4838-a9fa-38a4d13914cf
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("e13ff11e-e989-4838-a9fa-38a4d13914cf"), event_id=1, version=0)
class Microsoft_Windows_GPIOButtons_1_0(Etw):
    pattern = Struct(
        "ConvertibleState" / Int32ul
    )


@declare(guid=guid("e13ff11e-e989-4838-a9fa-38a4d13914cf"), event_id=2, version=0)
class Microsoft_Windows_GPIOButtons_2_0(Etw):
    pattern = Struct(
        "DockState" / Int32ul
    )

