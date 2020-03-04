# -*- coding: utf-8 -*-
"""
Microsoft-Windows-ReFS-v1
GUID : 059f0f37-910e-4ff0-a7ee-ae8d49dd319b
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("059f0f37-910e-4ff0-a7ee-ae8d49dd319b"), event_id=130, version=0)
class Microsoft_Windows_ReFS_v1_130_0(Etw):
    pattern = Struct(
        "VolumeIdLength" / Int16ul,
        "VolumeId" / Bytes(lambda this: this.VolumeIdLength),
        "RepairDetail" / WString,
        "RepairDataLength" / Int16ul,
        "RepairData" / Bytes(lambda this: this.RepairDataLength)
    )


@declare(guid=guid("059f0f37-910e-4ff0-a7ee-ae8d49dd319b"), event_id=131, version=0)
class Microsoft_Windows_ReFS_v1_131_0(Etw):
    pattern = Struct(
        "VolumeIdLength" / Int16ul,
        "VolumeId" / Bytes(lambda this: this.VolumeIdLength),
        "RepairDetail" / WString,
        "RepairDataLength" / Int16ul,
        "RepairData" / Bytes(lambda this: this.RepairDataLength)
    )


@declare(guid=guid("059f0f37-910e-4ff0-a7ee-ae8d49dd319b"), event_id=132, version=0)
class Microsoft_Windows_ReFS_v1_132_0(Etw):
    pattern = Struct(
        "ObjectNameLength" / Int16ul,
        "ObjectName" / Bytes(lambda this: this.ObjectNameLength),
        "FailureReason" / Int32ul
    )


@declare(guid=guid("059f0f37-910e-4ff0-a7ee-ae8d49dd319b"), event_id=133, version=0)
class Microsoft_Windows_ReFS_v1_133_0(Etw):
    pattern = Struct(
        "ObjectNameLength" / Int16ul,
        "ObjectName" / Bytes(lambda this: this.ObjectNameLength),
        "FailureReason" / Int32ul
    )


@declare(guid=guid("059f0f37-910e-4ff0-a7ee-ae8d49dd319b"), event_id=134, version=0)
class Microsoft_Windows_ReFS_v1_134_0(Etw):
    pattern = Struct(
        "VolumeIdLength" / Int16ul,
        "VolumeId" / Bytes(lambda this: this.VolumeIdLength),
        "FailureReason" / Int32ul
    )


@declare(guid=guid("059f0f37-910e-4ff0-a7ee-ae8d49dd319b"), event_id=135, version=0)
class Microsoft_Windows_ReFS_v1_135_0(Etw):
    pattern = Struct(
        "VolumeIdLength" / Int16ul,
        "VolumeId" / Bytes(lambda this: this.VolumeIdLength),
        "FailureReason" / Int32ul
    )


@declare(guid=guid("059f0f37-910e-4ff0-a7ee-ae8d49dd319b"), event_id=136, version=0)
class Microsoft_Windows_ReFS_v1_136_0(Etw):
    pattern = Struct(
        "VolumeIdLength" / Int16ul,
        "VolumeId" / Bytes(lambda this: this.VolumeIdLength),
        "FailureReason" / Int32ul
    )


@declare(guid=guid("059f0f37-910e-4ff0-a7ee-ae8d49dd319b"), event_id=237, version=0)
class Microsoft_Windows_ReFS_v1_237_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("059f0f37-910e-4ff0-a7ee-ae8d49dd319b"), event_id=238, version=0)
class Microsoft_Windows_ReFS_v1_238_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmStringDatapointValue" / WString
    )


@declare(guid=guid("059f0f37-910e-4ff0-a7ee-ae8d49dd319b"), event_id=272, version=0)
class Microsoft_Windows_ReFS_v1_272_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmProcessHashValue" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamRow" / Int16ul
    )


@declare(guid=guid("059f0f37-910e-4ff0-a7ee-ae8d49dd319b"), event_id=273, version=0)
class Microsoft_Windows_ReFS_v1_273_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmProcessHashValue" / Int32ul,
        "SqmStreamRowLength" / Int32ul,
        "SqmStreamEntriesSize" / Int32ul,
        "SqmStreamEntries" / Bytes(lambda this: this.SqmStreamEntriesSize),
        "SqmStreamFlags" / Int32ul
    )


@declare(guid=guid("059f0f37-910e-4ff0-a7ee-ae8d49dd319b"), event_id=274, version=0)
class Microsoft_Windows_ReFS_v1_274_0(Etw):
    pattern = Struct(
        "SqmType" / Int32ul,
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmDWORD64DatapointValue" / Int64ul
    )


@declare(guid=guid("059f0f37-910e-4ff0-a7ee-ae8d49dd319b"), event_id=513, version=0)
class Microsoft_Windows_ReFS_v1_513_0(Etw):
    pattern = Struct(
        "ObjectNameLength" / Int16ul,
        "ObjectName" / Bytes(lambda this: this.ObjectNameLength),
        "FailureReason" / Int32ul
    )


@declare(guid=guid("059f0f37-910e-4ff0-a7ee-ae8d49dd319b"), event_id=514, version=0)
class Microsoft_Windows_ReFS_v1_514_0(Etw):
    pattern = Struct(
        "ObjectNameLength" / Int16ul,
        "ObjectName" / Bytes(lambda this: this.ObjectNameLength),
        "FailureReason" / Int32ul
    )


@declare(guid=guid("059f0f37-910e-4ff0-a7ee-ae8d49dd319b"), event_id=515, version=0)
class Microsoft_Windows_ReFS_v1_515_0(Etw):
    pattern = Struct(
        "ObjectNameLength" / Int16ul,
        "ObjectName" / Bytes(lambda this: this.ObjectNameLength),
        "FailureReason" / Int32ul
    )


@declare(guid=guid("059f0f37-910e-4ff0-a7ee-ae8d49dd319b"), event_id=516, version=0)
class Microsoft_Windows_ReFS_v1_516_0(Etw):
    pattern = Struct(
        "ObjectNameLength" / Int16ul,
        "ObjectName" / Bytes(lambda this: this.ObjectNameLength),
        "FailureReason" / Int32ul
    )


@declare(guid=guid("059f0f37-910e-4ff0-a7ee-ae8d49dd319b"), event_id=519, version=0)
class Microsoft_Windows_ReFS_v1_519_0(Etw):
    pattern = Struct(
        "ObjectNameLength" / Int16ul,
        "ObjectName" / Bytes(lambda this: this.ObjectNameLength),
        "FailureReason" / Int32ul
    )


@declare(guid=guid("059f0f37-910e-4ff0-a7ee-ae8d49dd319b"), event_id=520, version=0)
class Microsoft_Windows_ReFS_v1_520_0(Etw):
    pattern = Struct(
        "ObjectNameLength" / Int16ul,
        "ObjectName" / Bytes(lambda this: this.ObjectNameLength),
        "FailureReason" / Int32ul
    )


@declare(guid=guid("059f0f37-910e-4ff0-a7ee-ae8d49dd319b"), event_id=521, version=0)
class Microsoft_Windows_ReFS_v1_521_0(Etw):
    pattern = Struct(
        "ObjectNameLength" / Int16ul,
        "ObjectName" / Bytes(lambda this: this.ObjectNameLength),
        "FailureReason" / Int32ul
    )

