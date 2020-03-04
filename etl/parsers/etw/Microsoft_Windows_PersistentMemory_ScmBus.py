# -*- coding: utf-8 -*-
"""
Microsoft-Windows-PersistentMemory-ScmBus
GUID : c03715ce-ea6f-5b67-4449-da1d1e1afeb8
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("c03715ce-ea6f-5b67-4449-da1d1e1afeb8"), event_id=1, version=1)
class Microsoft_Windows_PersistentMemory_ScmBus_1_1(Etw):
    pattern = Struct(
        "StartAddress" / Int64ul,
        "Size" / Int64ul
    )


@declare(guid=guid("c03715ce-ea6f-5b67-4449-da1d1e1afeb8"), event_id=2, version=1)
class Microsoft_Windows_PersistentMemory_ScmBus_2_1(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "MajorFunction" / Int32ul,
        "MinorFunction" / Int32ul,
        "Parameter" / Int32ul,
        "DeviceObject" / Int64ul
    )


@declare(guid=guid("c03715ce-ea6f-5b67-4449-da1d1e1afeb8"), event_id=3, version=1)
class Microsoft_Windows_PersistentMemory_ScmBus_3_1(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "Status" / Int32ul,
        "DeviceObject" / Int64ul
    )


@declare(guid=guid("c03715ce-ea6f-5b67-4449-da1d1e1afeb8"), event_id=4, version=1)
class Microsoft_Windows_PersistentMemory_ScmBus_4_1(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "MinorFunction" / Int32ul,
        "Type" / Int32ul,
        "DeviceObject" / Int64ul
    )


@declare(guid=guid("c03715ce-ea6f-5b67-4449-da1d1e1afeb8"), event_id=5, version=1)
class Microsoft_Windows_PersistentMemory_ScmBus_5_1(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "Status" / Int32ul,
        "DeviceObject" / Int64ul
    )


@declare(guid=guid("c03715ce-ea6f-5b67-4449-da1d1e1afeb8"), event_id=6, version=1)
class Microsoft_Windows_PersistentMemory_ScmBus_6_1(Etw):
    pattern = Struct(
        "CertificationArea" / CString,
        "FailureMessage" / CString
    )


@declare(guid=guid("c03715ce-ea6f-5b67-4449-da1d1e1afeb8"), event_id=7, version=1)
class Microsoft_Windows_PersistentMemory_ScmBus_7_1(Etw):
    pattern = Struct(
        "CertificationArea" / CString,
        "FailureMessage" / CString
    )


@declare(guid=guid("c03715ce-ea6f-5b67-4449-da1d1e1afeb8"), event_id=8, version=1)
class Microsoft_Windows_PersistentMemory_ScmBus_8_1(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "ExtendedStatus" / Int32ul,
        "Size" / Int32ul,
        "StartAddress" / Int64ul,
        "Length" / Int64ul,
        "RestartAddress" / Int64ul,
        "RestartLength" / Int64ul,
        "VolatileMemory" / Int8ul,
        "PersistentMemory" / Int8ul,
        "Overflow" / Int8ul,
        "NumErrorRecords" / Int32ul
    )


@declare(guid=guid("c03715ce-ea6f-5b67-4449-da1d1e1afeb8"), event_id=101, version=1)
class Microsoft_Windows_PersistentMemory_ScmBus_101_1(Etw):
    pattern = Struct(
        "NfitHandle" / Int32ul,
        "StartAddress" / Int64ul,
        "Length" / Int64ul
    )


@declare(guid=guid("c03715ce-ea6f-5b67-4449-da1d1e1afeb8"), event_id=215, version=0)
class Microsoft_Windows_PersistentMemory_ScmBus_215_0(Etw):
    pattern = Struct(
        "DeviceGuid" / Guid,
        "Message" / CString
    )


@declare(guid=guid("c03715ce-ea6f-5b67-4449-da1d1e1afeb8"), event_id=400, version=1)
class Microsoft_Windows_PersistentMemory_ScmBus_400_1(Etw):
    pattern = Struct(
        "NfitHandle" / Int32ul,
        "Location" / WString,
        "StartAddress" / Int64ul,
        "Length" / Int64ul
    )


@declare(guid=guid("c03715ce-ea6f-5b67-4449-da1d1e1afeb8"), event_id=900, version=0)
class Microsoft_Windows_PersistentMemory_ScmBus_900_0(Etw):
    pattern = Struct(
        "DeviceGuid" / Guid,
        "Message" / CString
    )

