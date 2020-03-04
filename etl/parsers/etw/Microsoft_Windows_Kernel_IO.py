# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Kernel-IO
GUID : abf1f586-2e50-4ba8-928d-49044e6f0db7
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("abf1f586-2e50-4ba8-928d-49044e6f0db7"), event_id=1, version=0)
class Microsoft_Windows_Kernel_IO_1_0(Etw):
    pattern = Struct(
        "VolumeGuid" / Guid,
        "VolumeNameLength" / Int16ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength)
    )


@declare(guid=guid("abf1f586-2e50-4ba8-928d-49044e6f0db7"), event_id=2, version=0)
class Microsoft_Windows_Kernel_IO_2_0(Etw):
    pattern = Struct(
        "VolumeGuid" / Guid,
        "VolumeNameLength" / Int16ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength)
    )


@declare(guid=guid("abf1f586-2e50-4ba8-928d-49044e6f0db7"), event_id=3, version=0)
class Microsoft_Windows_Kernel_IO_3_0(Etw):
    pattern = Struct(
        "VolumeGuid" / Guid,
        "VolumeNameLength" / Int16ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength),
        "Error" / Int32ul
    )


@declare(guid=guid("abf1f586-2e50-4ba8-928d-49044e6f0db7"), event_id=1205, version=0)
class Microsoft_Windows_Kernel_IO_1205_0(Etw):
    pattern = Struct(
        "FilterNameLength" / Int16ul,
        "FilterName" / Bytes(lambda this: this.FilterNameLength)
    )


@declare(guid=guid("abf1f586-2e50-4ba8-928d-49044e6f0db7"), event_id=1206, version=0)
class Microsoft_Windows_Kernel_IO_1206_0(Etw):
    pattern = Struct(
        "FilterNameLength" / Int16ul,
        "FilterName" / Bytes(lambda this: this.FilterNameLength),
        "VolumeNameLength" / Int16ul,
        "VolumeName" / Bytes(lambda this: this.VolumeNameLength)
    )


@declare(guid=guid("abf1f586-2e50-4ba8-928d-49044e6f0db7"), event_id=1207, version=0)
class Microsoft_Windows_Kernel_IO_1207_0(Etw):
    pattern = Struct(
        "DumpEncryptionFailureReason" / Int32ul
    )

