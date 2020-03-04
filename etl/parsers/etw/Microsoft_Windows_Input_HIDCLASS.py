# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Input-HIDCLASS
GUID : 6465da78-e7a0-4f39-b084-8f53c7c30dc6
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("6465da78-e7a0-4f39-b084-8f53c7c30dc6"), event_id=3, version=0)
class Microsoft_Windows_Input_HIDCLASS_3_0(Etw):
    pattern = Struct(
        "DeviceObject" / Int64ul,
        "VendorID" / Int16ul,
        "ProductID" / Int16ul,
        "VersionNumber" / Int16ul,
        "ReportDescriptorLength" / Int32ul,
        "ReportDescriptor" / Bytes(lambda this: this.ReportDescriptorLength)
    )

