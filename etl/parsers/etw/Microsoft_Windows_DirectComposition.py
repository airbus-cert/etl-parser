# -*- coding: utf-8 -*-
"""
Microsoft-Windows-DirectComposition
GUID : c44219d0-f344-11df-a5e2-b307dfd72085
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("c44219d0-f344-11df-a5e2-b307dfd72085"), event_id=1, version=0)
class Microsoft_Windows_DirectComposition_1_0(Etw):
    pattern = Struct(
        "channelHandle" / Int32ul,
        "resourceHandle" / Int32ul,
        "externalHandleAndChannel" / Int64ul,
        "resourceType" / Int32ul,
        "createShared" / Int8ul,
        "openShared" / Int8ul,
        "resourcePointer" / Int64ul
    )


@declare(guid=guid("c44219d0-f344-11df-a5e2-b307dfd72085"), event_id=2, version=0)
class Microsoft_Windows_DirectComposition_2_0(Etw):
    pattern = Struct(
        "channelHandle" / Int32ul,
        "resourceType" / Int32ul,
        "resourcePointer" / Int64ul,
        "left" / Int32sl,
        "top" / Int32sl,
        "right" / Int32sl,
        "bottom" / Int32sl
    )


@declare(guid=guid("c44219d0-f344-11df-a5e2-b307dfd72085"), event_id=4, version=0)
class Microsoft_Windows_DirectComposition_4_0(Etw):
    pattern = Struct(
        "channelHandle" / Int32ul,
        "resourceType" / Int32ul,
        "resourcePointer" / Int64ul
    )


@declare(guid=guid("c44219d0-f344-11df-a5e2-b307dfd72085"), event_id=6, version=0)
class Microsoft_Windows_DirectComposition_6_0(Etw):
    pattern = Struct(
        "channelHandle" / Int32ul,
        "resourceType" / Int32ul,
        "resourcePointer" / Int64ul
    )


@declare(guid=guid("c44219d0-f344-11df-a5e2-b307dfd72085"), event_id=8, version=0)
class Microsoft_Windows_DirectComposition_8_0(Etw):
    pattern = Struct(
        "channelHandle" / Int32ul,
        "resourceType" / Int32ul,
        "resourcePointer" / Int64ul
    )


@declare(guid=guid("c44219d0-f344-11df-a5e2-b307dfd72085"), event_id=10, version=0)
class Microsoft_Windows_DirectComposition_10_0(Etw):
    pattern = Struct(
        "channelHandle" / Int32ul,
        "resourceType" / Int32ul,
        "resourcePointer" / Int64ul
    )


@declare(guid=guid("c44219d0-f344-11df-a5e2-b307dfd72085"), event_id=12, version=0)
class Microsoft_Windows_DirectComposition_12_0(Etw):
    pattern = Struct(
        "channelHandle" / Int32ul,
        "resourceType" / Int32ul,
        "resourcePointer" / Int64ul
    )


@declare(guid=guid("c44219d0-f344-11df-a5e2-b307dfd72085"), event_id=14, version=0)
class Microsoft_Windows_DirectComposition_14_0(Etw):
    pattern = Struct(
        "channelHandle" / Int32ul,
        "resourceType" / Int32ul,
        "resourcePointer" / Int64ul
    )


@declare(guid=guid("c44219d0-f344-11df-a5e2-b307dfd72085"), event_id=16, version=0)
class Microsoft_Windows_DirectComposition_16_0(Etw):
    pattern = Struct(
        "Id" / Int64ul,
        "Width" / Int32ul,
        "Height" / Int32ul,
        "BitDepth" / Int32ul,
        "IsTexturingAtlas" / Int8ul,
        "ChannelHandle" / Int32ul,
        "PixelFormat" / Int32ul
    )


@declare(guid=guid("c44219d0-f344-11df-a5e2-b307dfd72085"), event_id=17, version=0)
class Microsoft_Windows_DirectComposition_17_0(Etw):
    pattern = Struct(
        "Id" / Int64ul
    )


@declare(guid=guid("c44219d0-f344-11df-a5e2-b307dfd72085"), event_id=18, version=0)
class Microsoft_Windows_DirectComposition_18_0(Etw):
    pattern = Struct(
        "AtlasId" / Int64ul,
        "X" / Int32ul,
        "Y" / Int32ul,
        "Width" / Int32ul,
        "Height" / Int32ul,
        "EntryId" / Int64ul
    )


@declare(guid=guid("c44219d0-f344-11df-a5e2-b307dfd72085"), event_id=19, version=0)
class Microsoft_Windows_DirectComposition_19_0(Etw):
    pattern = Struct(
        "AtlasId" / Int64ul,
        "X" / Int32ul,
        "Y" / Int32ul,
        "Width" / Int32ul,
        "Height" / Int32ul,
        "EntryId" / Int64ul
    )


@declare(guid=guid("c44219d0-f344-11df-a5e2-b307dfd72085"), event_id=20, version=0)
class Microsoft_Windows_DirectComposition_20_0(Etw):
    pattern = Struct(
        "Id" / Int64ul,
        "Width" / Int32ul,
        "Height" / Int32ul,
        "BitDepth" / Int32ul,
        "PercentUsed" / Float32l
    )


@declare(guid=guid("c44219d0-f344-11df-a5e2-b307dfd72085"), event_id=21, version=0)
class Microsoft_Windows_DirectComposition_21_0(Etw):
    pattern = Struct(
        "channelHandle" / Int32ul,
        "resourceType" / Int32ul,
        "resourcePointer" / Int64ul
    )


@declare(guid=guid("c44219d0-f344-11df-a5e2-b307dfd72085"), event_id=23, version=0)
class Microsoft_Windows_DirectComposition_23_0(Etw):
    pattern = Struct(
        "DeviceId" / Int64ul,
        "ChannelHandle" / Int32ul
    )


@declare(guid=guid("c44219d0-f344-11df-a5e2-b307dfd72085"), event_id=24, version=0)
class Microsoft_Windows_DirectComposition_24_0(Etw):
    pattern = Struct(
        "DeviceId" / Int64ul,
        "ChannelHandle" / Int32ul
    )


@declare(guid=guid("c44219d0-f344-11df-a5e2-b307dfd72085"), event_id=25, version=0)
class Microsoft_Windows_DirectComposition_25_0(Etw):
    pattern = Struct(
        "DeviceId" / Int64ul,
        "ChannelHandle" / Int32ul,
        "LastCommittedBatchId" / Int32ul,
        "LastConfirmedBatchId" / Int32ul
    )


@declare(guid=guid("c44219d0-f344-11df-a5e2-b307dfd72085"), event_id=26, version=0)
class Microsoft_Windows_DirectComposition_26_0(Etw):
    pattern = Struct(
        "Id" / Int64ul,
        "Owner" / Int64ul,
        "UseType" / Int32ul,
        "XData" / Int32sl,
        "YData" / Int32sl
    )


@declare(guid=guid("c44219d0-f344-11df-a5e2-b307dfd72085"), event_id=27, version=0)
class Microsoft_Windows_DirectComposition_27_0(Etw):
    pattern = Struct(
        "Id" / Int64ul
    )


@declare(guid=guid("c44219d0-f344-11df-a5e2-b307dfd72085"), event_id=28, version=0)
class Microsoft_Windows_DirectComposition_28_0(Etw):
    pattern = Struct(
        "Id" / Int64ul
    )


@declare(guid=guid("c44219d0-f344-11df-a5e2-b307dfd72085"), event_id=29, version=0)
class Microsoft_Windows_DirectComposition_29_0(Etw):
    pattern = Struct(
        "AtlasId" / Int64ul,
        "X" / Int32ul,
        "Y" / Int32ul,
        "Width" / Int32ul,
        "Height" / Int32ul,
        "EntryId" / Int64ul
    )


@declare(guid=guid("c44219d0-f344-11df-a5e2-b307dfd72085"), event_id=30, version=0)
class Microsoft_Windows_DirectComposition_30_0(Etw):
    pattern = Struct(
        "channelHandle" / Int32ul,
        "resourceHandle" / Int32ul,
        "resourcePointer" / Int64ul
    )


@declare(guid=guid("c44219d0-f344-11df-a5e2-b307dfd72085"), event_id=31, version=0)
class Microsoft_Windows_DirectComposition_31_0(Etw):
    pattern = Struct(
        "clumpPointer" / Int64ul,
        "virtualSurfacePointer" / Int64ul,
        "left" / Int32ul,
        "top" / Int32ul,
        "right" / Int32ul,
        "bottom" / Int32ul
    )


@declare(guid=guid("c44219d0-f344-11df-a5e2-b307dfd72085"), event_id=32, version=0)
class Microsoft_Windows_DirectComposition_32_0(Etw):
    pattern = Struct(
        "clumpPointer" / Int64ul
    )


@declare(guid=guid("c44219d0-f344-11df-a5e2-b307dfd72085"), event_id=33, version=0)
class Microsoft_Windows_DirectComposition_33_0(Etw):
    pattern = Struct(
        "surfacePointer" / Int64ul
    )


@declare(guid=guid("c44219d0-f344-11df-a5e2-b307dfd72085"), event_id=34, version=0)
class Microsoft_Windows_DirectComposition_34_0(Etw):
    pattern = Struct(
        "surfacePointer" / Int64ul
    )


@declare(guid=guid("c44219d0-f344-11df-a5e2-b307dfd72085"), event_id=35, version=0)
class Microsoft_Windows_DirectComposition_35_0(Etw):
    pattern = Struct(
        "surfacePointer" / Int64ul
    )


@declare(guid=guid("c44219d0-f344-11df-a5e2-b307dfd72085"), event_id=36, version=0)
class Microsoft_Windows_DirectComposition_36_0(Etw):
    pattern = Struct(
        "surfacePointer" / Int64ul
    )


@declare(guid=guid("c44219d0-f344-11df-a5e2-b307dfd72085"), event_id=37, version=0)
class Microsoft_Windows_DirectComposition_37_0(Etw):
    pattern = Struct(
        "percentValidTiles" / Int32ul,
        "pixelsPerClump" / Int32ul
    )


@declare(guid=guid("c44219d0-f344-11df-a5e2-b307dfd72085"), event_id=38, version=0)
class Microsoft_Windows_DirectComposition_38_0(Etw):
    pattern = Struct(
        "ChannelHandle" / Int32ul,
        "LastCommittedBatchId" / Int32ul,
        "largeSurfacesTotalAllocated" / Int64ul,
        "largeSurfacesInUseAllocated" / Int64ul,
        "largeSurfacesInUseActual" / Int64ul,
        "largeSurfacesPeakInUseActual" / Int64ul,
        "largeSurfacesAllowed" / Int64ul,
        "poolsTotalAllocated" / Int64ul,
        "poolsInUseAllocated" / Int64ul,
        "poolsInUseActual" / Int64ul,
        "poolsPeakInUseActual" / Int64ul,
        "poolsAllowed" / Int64ul,
        "largeSurfacesPendingRelease" / Int64ul,
        "poolsPendingRelease" / Int64ul,
        "largeSurfacesMaxStructuralWaste" / Int64ul,
        "poolsMaxStructuralWaste" / Int64ul
    )


@declare(guid=guid("c44219d0-f344-11df-a5e2-b307dfd72085"), event_id=39, version=0)
class Microsoft_Windows_DirectComposition_39_0(Etw):
    pattern = Struct(
        "Id" / Int64ul,
        "Width" / Int32ul,
        "Height" / Int32ul
    )


@declare(guid=guid("c44219d0-f344-11df-a5e2-b307dfd72085"), event_id=40, version=0)
class Microsoft_Windows_DirectComposition_40_0(Etw):
    pattern = Struct(
        "Id" / Int64ul
    )


@declare(guid=guid("c44219d0-f344-11df-a5e2-b307dfd72085"), event_id=41, version=0)
class Microsoft_Windows_DirectComposition_41_0(Etw):
    pattern = Struct(
        "Id" / Int64ul
    )


@declare(guid=guid("c44219d0-f344-11df-a5e2-b307dfd72085"), event_id=42, version=0)
class Microsoft_Windows_DirectComposition_42_0(Etw):
    pattern = Struct(
        "Id" / Int64ul,
        "Width" / Int32ul,
        "Height" / Int32ul
    )


@declare(guid=guid("c44219d0-f344-11df-a5e2-b307dfd72085"), event_id=43, version=0)
class Microsoft_Windows_DirectComposition_43_0(Etw):
    pattern = Struct(
        "Id" / Int64ul,
        "Width" / Int32ul,
        "Height" / Int32ul,
        "PixelsDiscarded" / Int8ul,
        "SurfaceInvalid" / Int8ul
    )


@declare(guid=guid("c44219d0-f344-11df-a5e2-b307dfd72085"), event_id=44, version=0)
class Microsoft_Windows_DirectComposition_44_0(Etw):
    pattern = Struct(
        "Id" / Int64ul
    )


@declare(guid=guid("c44219d0-f344-11df-a5e2-b307dfd72085"), event_id=45, version=0)
class Microsoft_Windows_DirectComposition_45_0(Etw):
    pattern = Struct(
        "Id" / Int64ul
    )


@declare(guid=guid("c44219d0-f344-11df-a5e2-b307dfd72085"), event_id=46, version=0)
class Microsoft_Windows_DirectComposition_46_0(Etw):
    pattern = Struct(
        "section" / Int64ul,
        "size" / Int32ul
    )


@declare(guid=guid("c44219d0-f344-11df-a5e2-b307dfd72085"), event_id=47, version=0)
class Microsoft_Windows_DirectComposition_47_0(Etw):
    pattern = Struct(
        "section" / Int64ul,
        "size" / Int32ul
    )


@declare(guid=guid("c44219d0-f344-11df-a5e2-b307dfd72085"), event_id=48, version=0)
class Microsoft_Windows_DirectComposition_48_0(Etw):
    pattern = Struct(
        "section" / Int64ul,
        "allocationSize" / Int32ul,
        "sectionSize" / Int32ul,
        "heap" / Int8ul
    )


@declare(guid=guid("c44219d0-f344-11df-a5e2-b307dfd72085"), event_id=50, version=0)
class Microsoft_Windows_DirectComposition_50_0(Etw):
    pattern = Struct(
        "deviceId" / Int64ul,
        "channelHandle" / Int32ul,
        "version" / Int16ul,
        "scenarioPriority" / Int16ul,
        "flags" / Int16ul,
        "qpcInitiate" / Int64ul,
        "qpcInput" / Int64ul,
        "msIntendedDuration" / Int32ul,
        "scenarioGuid" / Guid,
        "scenarioName" / WString,
        "scenarioDetails" / WString
    )


@declare(guid=guid("c44219d0-f344-11df-a5e2-b307dfd72085"), event_id=51, version=0)
class Microsoft_Windows_DirectComposition_51_0(Etw):
    pattern = Struct(
        "deviceId" / Int64ul,
        "channelHandle" / Int32ul,
        "scenarioGuid" / Guid,
        "uniqueKey" / Int64ul
    )


@declare(guid=guid("c44219d0-f344-11df-a5e2-b307dfd72085"), event_id=52, version=0)
class Microsoft_Windows_DirectComposition_52_0(Etw):
    pattern = Struct(
        "deviceId" / Int64ul,
        "channelHandle" / Int32ul,
        "scenarioGuid" / Guid,
        "uniqueKey" / Int64ul
    )


@declare(guid=guid("c44219d0-f344-11df-a5e2-b307dfd72085"), event_id=53, version=0)
class Microsoft_Windows_DirectComposition_53_0(Etw):
    pattern = Struct(
        "channelHandle" / Int32ul,
        "resourceHandle" / Int32ul,
        "flags" / Int32ul,
        "batchCount" / Int32ul,
        "totalPrimitiveCount" / Int32ul,
        "boundsLeft" / Float32l,
        "boundsTop" / Float32l,
        "boundsRight" / Float32l,
        "boundsBottom" / Float32l,
        "singlePrimitiveInfoLength" / Int16ul,
        "surfaceInfoLength" / Int16ul,
        "surfaceInfo" / Bytes(lambda this: this.surfaceInfoLength),
        "primitivesLength" / Int16ul,
        "primitives" / Bytes(lambda this: this.primitivesLength)
    )


@declare(guid=guid("c44219d0-f344-11df-a5e2-b307dfd72085"), event_id=54, version=0)
class Microsoft_Windows_DirectComposition_54_0(Etw):
    pattern = Struct(
        "TargetX" / Int32ul,
        "TargetY" / Int32ul,
        "MinX" / Int32ul,
        "MinY" / Int32ul,
        "MaxX" / Int32ul,
        "MaxY" / Int32ul,
        "RequestX" / Int32ul,
        "RequestY" / Int32ul,
        "ShrinkX" / Int32ul,
        "ShrinkY" / Int32ul,
        "GrowX" / Int32ul,
        "GrowY" / Int32ul,
        "AtlasX" / Int32ul,
        "AtlasY" / Int32ul
    )


@declare(guid=guid("c44219d0-f344-11df-a5e2-b307dfd72085"), event_id=55, version=0)
class Microsoft_Windows_DirectComposition_55_0(Etw):
    pattern = Struct(
        "Channel" / Int32ul,
        "visualHandle" / Int32ul,
        "interactionHandle" / Int32ul,
        "visualAndChannelHandle" / Int64ul,
        "interactionAndChannelHandle" / Int64ul
    )


@declare(guid=guid("c44219d0-f344-11df-a5e2-b307dfd72085"), event_id=56, version=0)
class Microsoft_Windows_DirectComposition_56_0(Etw):
    pattern = Struct(
        "visualAndChannelHandle" / Int64ul,
        "inputSinkHandle" / Int64ul
    )


@declare(guid=guid("c44219d0-f344-11df-a5e2-b307dfd72085"), event_id=57, version=0)
class Microsoft_Windows_DirectComposition_57_0(Etw):
    pattern = Struct(
        "Channel" / Int32ul,
        "visualHandle" / Int32ul,
        "visualAndChannelHandle" / Int64ul,
        "windowHandle" / Int64ul,
        "mouseConfigMask" / Int32ul,
        "mouseConfigValues" / Int32ul
    )


@declare(guid=guid("c44219d0-f344-11df-a5e2-b307dfd72085"), event_id=58, version=0)
class Microsoft_Windows_DirectComposition_58_0(Etw):
    pattern = Struct(
        "Channel" / Int32ul,
        "interactionHandle" / Int32ul,
        "interactionAndChannelHandle" / Int64ul,
        "propertyId" / Int32ul
    )


@declare(guid=guid("c44219d0-f344-11df-a5e2-b307dfd72085"), event_id=59, version=0)
class Microsoft_Windows_DirectComposition_59_0(Etw):
    pattern = Struct(
        "Channel" / Int32ul,
        "interactionHandle" / Int32ul,
        "interactionAndChannelHandle" / Int64ul,
        "captureType" / Int32ul,
        "pointerId" / Int32ul,
        "pointerTimeStamp" / Int64ul
    )


@declare(guid=guid("c44219d0-f344-11df-a5e2-b307dfd72085"), event_id=61, version=0)
class Microsoft_Windows_DirectComposition_61_0(Etw):
    pattern = Struct(
        "result" / Int32ul
    )


@declare(guid=guid("c44219d0-f344-11df-a5e2-b307dfd72085"), event_id=63, version=0)
class Microsoft_Windows_DirectComposition_63_0(Etw):
    pattern = Struct(
        "result" / Int32ul
    )


@declare(guid=guid("c44219d0-f344-11df-a5e2-b307dfd72085"), event_id=65, version=0)
class Microsoft_Windows_DirectComposition_65_0(Etw):
    pattern = Struct(
        "presentId" / Int64ul,
        "result" / Int32ul
    )

