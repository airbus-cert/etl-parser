# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Sdbus
GUID : fe28004e-b08f-4407-92b3-bad3a2c51708
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("fe28004e-b08f-4407-92b3-bad3a2c51708"), event_id=100, version=0)
class Microsoft_Windows_Sdbus_100_0(Etw):
    pattern = Struct(
        "SDHostPhysicalAddress" / Int64ul,
        "EventMask" / Int32ul
    )


@declare(guid=guid("fe28004e-b08f-4407-92b3-bad3a2c51708"), event_id=101, version=0)
class Microsoft_Windows_Sdbus_101_0(Etw):
    pattern = Struct(
        "SDHostPhysicalAddress" / Int64ul
    )


@declare(guid=guid("fe28004e-b08f-4407-92b3-bad3a2c51708"), event_id=102, version=0)
class Microsoft_Windows_Sdbus_102_0(Etw):
    pattern = Struct(
        "SDHostPhysicalAddress" / Int64ul
    )


@declare(guid=guid("fe28004e-b08f-4407-92b3-bad3a2c51708"), event_id=103, version=0)
class Microsoft_Windows_Sdbus_103_0(Etw):
    pattern = Struct(
        "SDHostPhysicalAddress" / Int64ul,
        "RetuneCount" / Int64ul
    )


@declare(guid=guid("fe28004e-b08f-4407-92b3-bad3a2c51708"), event_id=104, version=0)
class Microsoft_Windows_Sdbus_104_0(Etw):
    pattern = Struct(
        "SDHostPhysicalAddress" / Int64ul,
        "ErrorCode" / Int32ul,
        "ErrorCount" / Int32ul
    )


@declare(guid=guid("fe28004e-b08f-4407-92b3-bad3a2c51708"), event_id=105, version=0)
class Microsoft_Windows_Sdbus_105_0(Etw):
    pattern = Struct(
        "SDHostPhysicalAddress" / Int64ul,
        "HpiIoCount" / Int64ul
    )


@declare(guid=guid("fe28004e-b08f-4407-92b3-bad3a2c51708"), event_id=106, version=0)
class Microsoft_Windows_Sdbus_106_0(Etw):
    pattern = Struct(
        "PoFxDeviceHandle" / Int64ul,
        "PStateRequested" / Int32ul,
        "PStateRequestCount" / Int64ul
    )


@declare(guid=guid("fe28004e-b08f-4407-92b3-bad3a2c51708"), event_id=107, version=0)
class Microsoft_Windows_Sdbus_107_0(Etw):
    pattern = Struct(
        "PoFxDeviceHandle" / Int64ul,
        "PStateCompleted" / Int32ul,
        "PStateCompletionCount" / Int64ul
    )


@declare(guid=guid("fe28004e-b08f-4407-92b3-bad3a2c51708"), event_id=108, version=0)
class Microsoft_Windows_Sdbus_108_0(Etw):
    pattern = Struct(
        "SDHostPhysicalAddress" / Int64ul,
        "Command" / Int8ul,
        "Argument" / Int64ul,
        "Size" / Int64ul
    )


@declare(guid=guid("fe28004e-b08f-4407-92b3-bad3a2c51708"), event_id=109, version=0)
class Microsoft_Windows_Sdbus_109_0(Etw):
    pattern = Struct(
        "SDHostPhysicalAddress" / Int64ul,
        "Command" / Int8ul,
        "Argument" / Int64ul,
        "Size" / Int64ul
    )


@declare(guid=guid("fe28004e-b08f-4407-92b3-bad3a2c51708"), event_id=110, version=0)
class Microsoft_Windows_Sdbus_110_0(Etw):
    pattern = Struct(
        "Irp" / Int64ul
    )


@declare(guid=guid("fe28004e-b08f-4407-92b3-bad3a2c51708"), event_id=111, version=0)
class Microsoft_Windows_Sdbus_111_0(Etw):
    pattern = Struct(
        "Irp" / Int64ul
    )


@declare(guid=guid("fe28004e-b08f-4407-92b3-bad3a2c51708"), event_id=112, version=0)
class Microsoft_Windows_Sdbus_112_0(Etw):
    pattern = Struct(
        "Irp" / Int64ul
    )


@declare(guid=guid("fe28004e-b08f-4407-92b3-bad3a2c51708"), event_id=113, version=0)
class Microsoft_Windows_Sdbus_113_0(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "HpiExitReason" / Int32ul
    )


@declare(guid=guid("fe28004e-b08f-4407-92b3-bad3a2c51708"), event_id=114, version=0)
class Microsoft_Windows_Sdbus_114_0(Etw):
    pattern = Struct(
        "PoFxDeviceHandle" / Int64ul,
        "PStateActivePercent" / Int32ul,
        "PStateActiveDuration" / Int32ul,
        "PStateSampleDuration" / Int32ul,
        "PStateCurrentFrequency" / Int32ul,
        "PStateRequestedFrequency" / Int32ul
    )


@declare(guid=guid("fe28004e-b08f-4407-92b3-bad3a2c51708"), event_id=115, version=0)
class Microsoft_Windows_Sdbus_115_0(Etw):
    pattern = Struct(
        "SDHostPhysicalAddress" / Int64ul,
        "Irp" / Int64ul,
        "WorkPacketWorkerProcFunction" / Int32ul,
        "WorkEngineCurrentState" / Int32ul,
        "WorkEngineFunctionPhase" / Int32ul
    )


@declare(guid=guid("fe28004e-b08f-4407-92b3-bad3a2c51708"), event_id=116, version=0)
class Microsoft_Windows_Sdbus_116_0(Etw):
    pattern = Struct(
        "SDHostPhysicalAddress" / Int64ul,
        "Irp" / Int64ul,
        "WorkPacketWorkerProcFunction" / Int32ul,
        "WorkEngineCurrentState" / Int32ul,
        "WorkEngineFunctionPhase" / Int32ul
    )


@declare(guid=guid("fe28004e-b08f-4407-92b3-bad3a2c51708"), event_id=117, version=0)
class Microsoft_Windows_Sdbus_117_0(Etw):
    pattern = Struct(
        "SDHostPhysicalAddress" / Int64ul,
        "Irp" / Int64ul,
        "WorkEngineCommand" / Int32ul,
        "WorkEngineArgument" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("fe28004e-b08f-4407-92b3-bad3a2c51708"), event_id=118, version=0)
class Microsoft_Windows_Sdbus_118_0(Etw):
    pattern = Struct(
        "SDHostPhysicalAddress" / Int64ul,
        "Irp" / Int64ul,
        "WorkEngineCommand" / Int32ul,
        "WorkEngineArgument" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("fe28004e-b08f-4407-92b3-bad3a2c51708"), event_id=119, version=0)
class Microsoft_Windows_Sdbus_119_0(Etw):
    pattern = Struct(
        "SDHostPhysicalAddress" / Int64ul
    )

