# -*- coding: utf-8 -*-
"""
Microsoft-Windows-IndirectDisplays-ClassExtension-Events
GUID : 966cd1c0-3f69-42ad-9877-517dce8462b4
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("966cd1c0-3f69-42ad-9877-517dce8462b4"), event_id=2, version=0)
class Microsoft_Windows_IndirectDisplays_ClassExtension_Events_2_0(Etw):
    pattern = Struct(
        "IddAdapterLuid" / Int64sl
    )


@declare(guid=guid("966cd1c0-3f69-42ad-9877-517dce8462b4"), event_id=3, version=0)
class Microsoft_Windows_IndirectDisplays_ClassExtension_Events_3_0(Etw):
    pattern = Struct(
        "IddAdapterLuid" / Int64sl
    )


@declare(guid=guid("966cd1c0-3f69-42ad-9877-517dce8462b4"), event_id=4, version=0)
class Microsoft_Windows_IndirectDisplays_ClassExtension_Events_4_0(Etw):
    pattern = Struct(
        "IddAdapterLuid" / Int64sl,
        "Bandwidth" / Int64ul
    )


@declare(guid=guid("966cd1c0-3f69-42ad-9877-517dce8462b4"), event_id=5, version=0)
class Microsoft_Windows_IndirectDisplays_ClassExtension_Events_5_0(Etw):
    pattern = Struct(
        "IddAdapterLuid" / Int64sl
    )


@declare(guid=guid("966cd1c0-3f69-42ad-9877-517dce8462b4"), event_id=6, version=0)
class Microsoft_Windows_IndirectDisplays_ClassExtension_Events_6_0(Etw):
    pattern = Struct(
        "IddAdapterLuid" / Int64sl,
        "ConnectorIndex" / Int32ul,
        "DescriptorType" / Int32ul
    )


@declare(guid=guid("966cd1c0-3f69-42ad-9877-517dce8462b4"), event_id=7, version=0)
class Microsoft_Windows_IndirectDisplays_ClassExtension_Events_7_0(Etw):
    pattern = Struct(
        "IddAdapterLuid" / Int64sl,
        "ConnectorIndex" / Int32ul
    )


@declare(guid=guid("966cd1c0-3f69-42ad-9877-517dce8462b4"), event_id=8, version=0)
class Microsoft_Windows_IndirectDisplays_ClassExtension_Events_8_0(Etw):
    pattern = Struct(
        "IddAdapterLuid" / Int64sl,
        "ConnectorIndex" / Int32ul
    )


@declare(guid=guid("966cd1c0-3f69-42ad-9877-517dce8462b4"), event_id=9, version=0)
class Microsoft_Windows_IndirectDisplays_ClassExtension_Events_9_0(Etw):
    pattern = Struct(
        "IddAdapterLuid" / Int64sl,
        "ConnectorIndex" / Int32ul,
        "InputModeCount" / Int32ul
    )


@declare(guid=guid("966cd1c0-3f69-42ad-9877-517dce8462b4"), event_id=10, version=0)
class Microsoft_Windows_IndirectDisplays_ClassExtension_Events_10_0(Etw):
    pattern = Struct(
        "IddAdapterLuid" / Int64sl,
        "ConnectorIndex" / Int32ul,
        "InputModeCount" / Int32ul
    )


@declare(guid=guid("966cd1c0-3f69-42ad-9877-517dce8462b4"), event_id=11, version=0)
class Microsoft_Windows_IndirectDisplays_ClassExtension_Events_11_0(Etw):
    pattern = Struct(
        "IddAdapterLuid" / Int64sl,
        "ConnectorIndex" / Int32ul,
        "Handle" / Int64ul
    )


@declare(guid=guid("966cd1c0-3f69-42ad-9877-517dce8462b4"), event_id=12, version=0)
class Microsoft_Windows_IndirectDisplays_ClassExtension_Events_12_0(Etw):
    pattern = Struct(
        "IddAdapterLuid" / Int64sl,
        "ConnectorIndex" / Int32ul
    )


@declare(guid=guid("966cd1c0-3f69-42ad-9877-517dce8462b4"), event_id=13, version=0)
class Microsoft_Windows_IndirectDisplays_ClassExtension_Events_13_0(Etw):
    pattern = Struct(
        "IddAdapterLuid" / Int64sl,
        "ConnectorIndex" / Int32ul,
        "SevenBitI2CAddress" / Int32ul,
        "DataSizeInBytes" / Int32ul
    )


@declare(guid=guid("966cd1c0-3f69-42ad-9877-517dce8462b4"), event_id=14, version=0)
class Microsoft_Windows_IndirectDisplays_ClassExtension_Events_14_0(Etw):
    pattern = Struct(
        "IddAdapterLuid" / Int64sl,
        "ConnectorIndex" / Int32ul,
        "SevenBitI2CAddress" / Int32ul,
        "DataSizeInBytes" / Int32ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("966cd1c0-3f69-42ad-9877-517dce8462b4"), event_id=15, version=0)
class Microsoft_Windows_IndirectDisplays_ClassExtension_Events_15_0(Etw):
    pattern = Struct(
        "IddAdapterLuid" / Int64sl,
        "ConnectorIndex" / Int32ul
    )


@declare(guid=guid("966cd1c0-3f69-42ad-9877-517dce8462b4"), event_id=16, version=0)
class Microsoft_Windows_IndirectDisplays_ClassExtension_Events_16_0(Etw):
    pattern = Struct(
        "IddAdapterLuid" / Int64sl,
        "ConnectorIndex" / Int32ul
    )


@declare(guid=guid("966cd1c0-3f69-42ad-9877-517dce8462b4"), event_id=17, version=0)
class Microsoft_Windows_IndirectDisplays_ClassExtension_Events_17_0(Etw):
    pattern = Struct(
        "IddAdapterLuid" / Int64sl,
        "ConnectorIndex" / Int32ul
    )


@declare(guid=guid("966cd1c0-3f69-42ad-9877-517dce8462b4"), event_id=18, version=0)
class Microsoft_Windows_IndirectDisplays_ClassExtension_Events_18_0(Etw):
    pattern = Struct(
        "IddAdapterLuid" / Int64sl,
        "ConnectorIndex" / Int32ul,
        "LastShapeId" / Int32ul
    )


@declare(guid=guid("966cd1c0-3f69-42ad-9877-517dce8462b4"), event_id=19, version=0)
class Microsoft_Windows_IndirectDisplays_ClassExtension_Events_19_0(Etw):
    pattern = Struct(
        "SwapChainPointer" / Int64ul
    )


@declare(guid=guid("966cd1c0-3f69-42ad-9877-517dce8462b4"), event_id=20, version=0)
class Microsoft_Windows_IndirectDisplays_ClassExtension_Events_20_0(Etw):
    pattern = Struct(
        "SwapChainPointer" / Int64ul
    )


@declare(guid=guid("966cd1c0-3f69-42ad-9877-517dce8462b4"), event_id=21, version=0)
class Microsoft_Windows_IndirectDisplays_ClassExtension_Events_21_0(Etw):
    pattern = Struct(
        "SwapChainPointer" / Int64ul
    )


@declare(guid=guid("966cd1c0-3f69-42ad-9877-517dce8462b4"), event_id=22, version=0)
class Microsoft_Windows_IndirectDisplays_ClassExtension_Events_22_0(Etw):
    pattern = Struct(
        "SwapChainPointer" / Int64ul
    )


@declare(guid=guid("966cd1c0-3f69-42ad-9877-517dce8462b4"), event_id=23, version=0)
class Microsoft_Windows_IndirectDisplays_ClassExtension_Events_23_0(Etw):
    pattern = Struct(
        "SwapChainPointer" / Int64ul
    )


@declare(guid=guid("966cd1c0-3f69-42ad-9877-517dce8462b4"), event_id=24, version=0)
class Microsoft_Windows_IndirectDisplays_ClassExtension_Events_24_0(Etw):
    pattern = Struct(
        "SwapChainPointer" / Int64ul
    )


@declare(guid=guid("966cd1c0-3f69-42ad-9877-517dce8462b4"), event_id=25, version=0)
class Microsoft_Windows_IndirectDisplays_ClassExtension_Events_25_0(Etw):
    pattern = Struct(
        "SwapChainPointer" / Int64ul
    )


@declare(guid=guid("966cd1c0-3f69-42ad-9877-517dce8462b4"), event_id=26, version=0)
class Microsoft_Windows_IndirectDisplays_ClassExtension_Events_26_0(Etw):
    pattern = Struct(
        "SwapChainPointer" / Int64ul,
        "PresentationFrameNumber" / Int32ul,
        "FrameStatus" / Int32ul,
        "ReencodeNumber" / Int32ul,
        "FrameSliceTotal" / Int32ul,
        "CurrentSlice" / Int32ul,
        "FrameAcquireQpcTime" / Int64ul,
        "FrameProcessingStepsCount" / Int32ul,
        "SendStartQpcTime" / Int64ul,
        "SendStopQpcTime" / Int64ul,
        "SendCompleteQpcTime" / Int64ul,
        "Flags" / Int32ul,
        "ProcessedPixelCount" / Int32ul,
        "FrameSizeInBytes" / Int32ul
    )


@declare(guid=guid("966cd1c0-3f69-42ad-9877-517dce8462b4"), event_id=36, version=0)
class Microsoft_Windows_IndirectDisplays_ClassExtension_Events_36_0(Etw):
    pattern = Struct(
        "Valid" / Int8ul,
        "IddAdapterLuid" / Int64sl,
        "ConnectorIndex" / Int32ul,
        "TargetModeIndex" / Int32ul,
        "PixelRate" / Int64ul,
        "VSync" / Float32l,
        "ActiveWidth" / Int32ul,
        "ActiveHeight" / Int32ul,
        "RequiredBandwidth" / Int64ul
    )


@declare(guid=guid("966cd1c0-3f69-42ad-9877-517dce8462b4"), event_id=37, version=0)
class Microsoft_Windows_IndirectDisplays_ClassExtension_Events_37_0(Etw):
    pattern = Struct(
        "Valid" / Int8ul,
        "IddAdapterLuid" / Int64sl,
        "ConnectorIndex" / Int32ul,
        "MonitorModeIndex" / Int32ul,
        "PixelRate" / Int64ul,
        "VSync" / Float32l,
        "ActiveWidth" / Int32ul,
        "ActiveHeight" / Int32ul,
        "VSyncDivider" / Int16ul,
        "RequiredBandwidth" / Int64ul
    )


@declare(guid=guid("966cd1c0-3f69-42ad-9877-517dce8462b4"), event_id=41, version=0)
class Microsoft_Windows_IndirectDisplays_ClassExtension_Events_41_0(Etw):
    pattern = Struct(
        "IddAdapterLuid" / Int64sl,
        "PathIndex" / Int32ul,
        "PathFlags" / Int32ul,
        "Width" / Int32ul,
        "Height" / Int32ul
    )


@declare(guid=guid("966cd1c0-3f69-42ad-9877-517dce8462b4"), event_id=42, version=0)
class Microsoft_Windows_IndirectDisplays_ClassExtension_Events_42_0(Etw):
    pattern = Struct(
        "SwapChainPointer" / Int64ul,
        "PresentationFrameNumber" / Int32ul,
        "ReencodeNumber" / Int32ul,
        "CurrentSlice" / Int32ul,
        "StepIndex" / Int32ul,
        "StepType" / Int32ul,
        "QpcTime" / Int64ul,
        "Data1" / Int32ul,
        "Data2" / Int32ul
    )


@declare(guid=guid("966cd1c0-3f69-42ad-9877-517dce8462b4"), event_id=43, version=0)
class Microsoft_Windows_IndirectDisplays_ClassExtension_Events_43_0(Etw):
    pattern = Struct(
        "IddAdapterLuid" / Int64sl,
        "ConnectorIndex" / Int32ul,
        "MftContext" / Int64sl
    )


@declare(guid=guid("966cd1c0-3f69-42ad-9877-517dce8462b4"), event_id=44, version=0)
class Microsoft_Windows_IndirectDisplays_ClassExtension_Events_44_0(Etw):
    pattern = Struct(
        "IddAdapterLuid" / Int64sl,
        "ConnectorIndex" / Int32ul,
        "PhysicalWidth" / Int32ul,
        "PhysicalHeight" / Int32ul
    )


@declare(guid=guid("966cd1c0-3f69-42ad-9877-517dce8462b4"), event_id=45, version=0)
class Microsoft_Windows_IndirectDisplays_ClassExtension_Events_45_0(Etw):
    pattern = Struct(
        "IddAdapterLuid" / Int64sl,
        "PathIdx" / Int32ul,
        "MonitorConnectorIndex" / Int32ul,
        "Positionx" / Int32ul,
        "Positiony" / Int32ul,
        "ResolutionWidth" / Int32ul,
        "ResolutionHeight" / Int32ul,
        "VSync" / Float32l,
        "VSyncDivider" / Int32ul,
        "Rotation" / Int32ul,
        "DPI" / Int32ul,
        "PhysicalSizeWidth" / Int32ul,
        "PhysicalSizeHeight" / Int32ul
    )

