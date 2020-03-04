# -*- coding: utf-8 -*-
"""
Microsoft-Windows-PrintService-USBMon
GUID : 7f812073-b28d-4afc-9ced-b8010f914ef6
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("7f812073-b28d-4afc-9ced-b8010f914ef6"), event_id=1, version=0)
class Microsoft_Windows_PrintService_USBMon_1_0(Etw):
    pattern = Struct(
        "PrinterName" / WString,
        "FilePath" / WString
    )


@declare(guid=guid("7f812073-b28d-4afc-9ced-b8010f914ef6"), event_id=2, version=0)
class Microsoft_Windows_PrintService_USBMon_2_0(Etw):
    pattern = Struct(
        "PrinterName" / WString,
        "FilePath" / WString
    )


@declare(guid=guid("7f812073-b28d-4afc-9ced-b8010f914ef6"), event_id=11, version=0)
class Microsoft_Windows_PrintService_USBMon_11_0(Etw):
    pattern = Struct(
        "HResult" / Int32ul,
        "ErrorText" / WString,
        "FailingLine" / Int32ul
    )


@declare(guid=guid("7f812073-b28d-4afc-9ced-b8010f914ef6"), event_id=12, version=0)
class Microsoft_Windows_PrintService_USBMon_12_0(Etw):
    pattern = Struct(
        "HResult" / Int32ul,
        "ErrorText" / WString
    )

