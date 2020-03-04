# -*- coding: utf-8 -*-
"""
Microsoft-Windows-USBVideo
GUID : da1d1dbd-3186-4fa2-bc2d-075efd9e43e2
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("da1d1dbd-3186-4fa2-bc2d-075efd9e43e2"), event_id=200, version=0)
class Microsoft_Windows_USBVideo_200_0(Etw):
    pattern = Struct(
        "DeviceObject" / Int64ul
    )


@declare(guid=guid("da1d1dbd-3186-4fa2-bc2d-075efd9e43e2"), event_id=201, version=0)
class Microsoft_Windows_USBVideo_201_0(Etw):
    pattern = Struct(
        "DeviceObject" / Int64ul
    )


@declare(guid=guid("da1d1dbd-3186-4fa2-bc2d-075efd9e43e2"), event_id=202, version=0)
class Microsoft_Windows_USBVideo_202_0(Etw):
    pattern = Struct(
        "DeviceObject" / Int64ul
    )


@declare(guid=guid("da1d1dbd-3186-4fa2-bc2d-075efd9e43e2"), event_id=203, version=0)
class Microsoft_Windows_USBVideo_203_0(Etw):
    pattern = Struct(
        "DeviceObject" / Int64ul
    )


@declare(guid=guid("da1d1dbd-3186-4fa2-bc2d-075efd9e43e2"), event_id=204, version=0)
class Microsoft_Windows_USBVideo_204_0(Etw):
    pattern = Struct(
        "DeviceObject" / Int64ul
    )


@declare(guid=guid("da1d1dbd-3186-4fa2-bc2d-075efd9e43e2"), event_id=205, version=0)
class Microsoft_Windows_USBVideo_205_0(Etw):
    pattern = Struct(
        "DeviceObject" / Int64ul
    )


@declare(guid=guid("da1d1dbd-3186-4fa2-bc2d-075efd9e43e2"), event_id=206, version=0)
class Microsoft_Windows_USBVideo_206_0(Etw):
    pattern = Struct(
        "DeviceObject" / Int64ul
    )


@declare(guid=guid("da1d1dbd-3186-4fa2-bc2d-075efd9e43e2"), event_id=207, version=0)
class Microsoft_Windows_USBVideo_207_0(Etw):
    pattern = Struct(
        "DeviceObject" / Int64ul
    )


@declare(guid=guid("da1d1dbd-3186-4fa2-bc2d-075efd9e43e2"), event_id=208, version=0)
class Microsoft_Windows_USBVideo_208_0(Etw):
    pattern = Struct(
        "pBuf" / Int64ul
    )


@declare(guid=guid("da1d1dbd-3186-4fa2-bc2d-075efd9e43e2"), event_id=209, version=0)
class Microsoft_Windows_USBVideo_209_0(Etw):
    pattern = Struct(
        "pBuf" / Int64ul,
        "ulBytesCopied" / Int32ul
    )


@declare(guid=guid("da1d1dbd-3186-4fa2-bc2d-075efd9e43e2"), event_id=213, version=0)
class Microsoft_Windows_USBVideo_213_0(Etw):
    pattern = Struct(
        "DeviceObject" / Int64ul,
        "FilterInstanceCount" / Int32sl,
        "ActiveStreamCount" / Int32ul,
        "ConnectedStandbyState" / Int32ul,
        "ntStatus" / Int32ul
    )


@declare(guid=guid("da1d1dbd-3186-4fa2-bc2d-075efd9e43e2"), event_id=214, version=0)
class Microsoft_Windows_USBVideo_214_0(Etw):
    pattern = Struct(
        "DeviceObject" / Int64ul,
        "FilterInstanceCount" / Int32sl,
        "ActiveStreamCount" / Int32ul,
        "ConnectedStandbyState" / Int32ul,
        "ntStatus" / Int32ul
    )


@declare(guid=guid("da1d1dbd-3186-4fa2-bc2d-075efd9e43e2"), event_id=215, version=0)
class Microsoft_Windows_USBVideo_215_0(Etw):
    pattern = Struct(
        "DeviceObject" / Int64ul,
        "SystemState" / Int32ul,
        "DeviceState" / Int32ul,
        "DevicePowerStage" / Int32ul,
        "ntStatus" / Int32ul
    )


@declare(guid=guid("da1d1dbd-3186-4fa2-bc2d-075efd9e43e2"), event_id=216, version=0)
class Microsoft_Windows_USBVideo_216_0(Etw):
    pattern = Struct(
        "DeviceObject" / Int64ul
    )


@declare(guid=guid("da1d1dbd-3186-4fa2-bc2d-075efd9e43e2"), event_id=217, version=0)
class Microsoft_Windows_USBVideo_217_0(Etw):
    pattern = Struct(
        "DeviceObject" / Int64ul,
        "Irp" / Int64ul
    )


@declare(guid=guid("da1d1dbd-3186-4fa2-bc2d-075efd9e43e2"), event_id=218, version=0)
class Microsoft_Windows_USBVideo_218_0(Etw):
    pattern = Struct(
        "DeviceObject" / Int64ul,
        "Irp" / Int64ul,
        "ntStatus" / Int32ul
    )


@declare(guid=guid("da1d1dbd-3186-4fa2-bc2d-075efd9e43e2"), event_id=219, version=0)
class Microsoft_Windows_USBVideo_219_0(Etw):
    pattern = Struct(
        "DeviceObject" / Int64ul
    )


@declare(guid=guid("da1d1dbd-3186-4fa2-bc2d-075efd9e43e2"), event_id=220, version=0)
class Microsoft_Windows_USBVideo_220_0(Etw):
    pattern = Struct(
        "DeviceObject" / Int64ul
    )


@declare(guid=guid("da1d1dbd-3186-4fa2-bc2d-075efd9e43e2"), event_id=221, version=0)
class Microsoft_Windows_USBVideo_221_0(Etw):
    pattern = Struct(
        "DeviceObject" / Int64ul
    )


@declare(guid=guid("da1d1dbd-3186-4fa2-bc2d-075efd9e43e2"), event_id=222, version=0)
class Microsoft_Windows_USBVideo_222_0(Etw):
    pattern = Struct(
        "DeviceObject" / Int64ul
    )


@declare(guid=guid("da1d1dbd-3186-4fa2-bc2d-075efd9e43e2"), event_id=223, version=0)
class Microsoft_Windows_USBVideo_223_0(Etw):
    pattern = Struct(
        "DeviceObject" / Int64ul
    )


@declare(guid=guid("da1d1dbd-3186-4fa2-bc2d-075efd9e43e2"), event_id=224, version=0)
class Microsoft_Windows_USBVideo_224_0(Etw):
    pattern = Struct(
        "Id" / Guid
    )


@declare(guid=guid("da1d1dbd-3186-4fa2-bc2d-075efd9e43e2"), event_id=225, version=0)
class Microsoft_Windows_USBVideo_225_0(Etw):
    pattern = Struct(
        "Id" / Guid,
        "ulBytesCopied" / Int32ul
    )

