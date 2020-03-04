# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Storsvc
GUID : a963a23c-0058-521d-71ec-a1cce6173f21
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("a963a23c-0058-521d-71ec-a1cce6173f21"), event_id=1001, version=0)
class Microsoft_Windows_Storsvc_1001_0(Etw):
    pattern = Struct(
        "Version" / Int32ul,
        "DiskNumber" / Int32ul,
        "VendorId" / CString,
        "ProductId" / CString,
        "ProductRevision" / CString,
        "SerialNumber" / CString,
        "ParentId" / WString,
        "FileSystem" / WString,
        "BusType" / Int32ul,
        "PartitionStyle" / Int32ul,
        "VolumeCount" / Int32ul,
        "ContainsRawVolumes" / Int8ul,
        "Size" / Int64ul
    )


@declare(guid=guid("a963a23c-0058-521d-71ec-a1cce6173f21"), event_id=1002, version=0)
class Microsoft_Windows_Storsvc_1002_0(Etw):
    pattern = Struct(
        "Version" / Int32ul,
        "Epoch" / Int32ul,
        "DiskIndex" / Int32ul,
        "TotalDisks" / Int32ul,
        "DiskNumber" / Int32ul,
        "VendorId" / CString,
        "ProductId" / CString,
        "ProductRevision" / CString,
        "SerialNumber" / CString,
        "ParentId" / WString,
        "FileSystem" / WString,
        "BusType" / Int32ul,
        "PartitionStyle" / Int32ul,
        "VolumeCount" / Int32ul,
        "ContainsRawVolumes" / Int8ul,
        "Size" / Int64ul
    )

