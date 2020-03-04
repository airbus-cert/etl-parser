# -*- coding: utf-8 -*-
"""
OfficeAirSpace
GUID : f562bb8e-422d-4b5c-b20e-90d710f7d11c
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=3, version=2)
class OfficeAirSpace_3_2(Etw):
    pattern = Struct(
        "automationId" / CString,
        "handle" / Int32sl
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=4, version=2)
class OfficeAirSpace_4_2(Etw):
    pattern = Struct(
        "isHardware" / Int8ul,
        "isShared" / Int8ul,
        "featureLevel" / Int32ul,
        "adapterLuidLowPart" / Int32ul,
        "adapterLuidHighPart" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=11, version=2)
class OfficeAirSpace_11_2(Etw):
    pattern = Struct(
        "width" / Int32ul,
        "height" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=16, version=2)
class OfficeAirSpace_16_2(Etw):
    pattern = Struct(
        "command" / Int32ul,
        "hresult" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=30, version=2)
class OfficeAirSpace_30_2(Etw):
    pattern = Struct(
        "handle" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=31, version=2)
class OfficeAirSpace_31_2(Etw):
    pattern = Struct(
        "layerHandle" / Int32sl,
        "animationClass" / CString,
        "animation" / CString,
        "storyboardHandle" / Int32sl,
        "triggerProperty" / Int32ul,
        "triggerValue" / Double,
        "eventType" / Int32ul,
        "customEvent" / Int32ul,
        "looping" / Int8ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=32, version=2)
class OfficeAirSpace_32_2(Etw):
    pattern = Struct(
        "storyboardHandle" / Int32sl,
        "layerHandle" / Int32sl,
        "seconds" / Double,
        "animationProperty" / Int32ul,
        "value" / Double,
        "instant" / Int8ul,
        "implied" / Int8ul,
        "inherited" / Int8ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=33, version=2)
class OfficeAirSpace_33_2(Etw):
    pattern = Struct(
        "layerHandle" / Int32sl,
        "storyboardHandle" / Int32sl,
        "animationProperty" / Int32ul,
        "value" / Double,
        "animationTick" / Int8ul,
        "animationSeconds" / Double
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=34, version=2)
class OfficeAirSpace_34_2(Etw):
    pattern = Struct(
        "storyboardHandle" / Int32sl,
        "started" / Int8ul,
        "finished" / Int8ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=35, version=2)
class OfficeAirSpace_35_2(Etw):
    pattern = Struct(
        "layerHostCount" / Int32ul,
        "layerCount" / Int32ul,
        "textureCount" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=37, version=2)
class OfficeAirSpace_37_2(Etw):
    pattern = Struct(
        "width" / Int32ul,
        "height" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=38, version=2)
class OfficeAirSpace_38_2(Etw):
    pattern = Struct(
        "layerHandle" / Int32sl,
        "animationProperty" / Int32ul,
        "finalValue" / Double,
        "deleted" / Int8ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=39, version=2)
class OfficeAirSpace_39_2(Etw):
    pattern = Struct(
        "frameId" / Int32sl,
        "frameTimestamp" / Double,
        "totalTime" / Double,
        "channelTime" / Double,
        "animationUpdateTime" / Double,
        "layoutTime" / Double,
        "repairDamageTime" / Double,
        "storyboardsScheduled" / Int32ul,
        "storyboardScheduleTime" / Double
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=40, version=1)
class OfficeAirSpace_40_1(Etw):
    pattern = Struct(
        "frameId" / Int32ul,
        "frameTimestamp" / Double,
        "totalTime" / Double,
        "channelTime" / Double,
        "updateTime" / Double,
        "drawingTime" / Double,
        "compositorBatches" / Int32ul,
        "canvasesPresented" / Int32ul,
        "totalCompNodeCount" / Int32ul,
        "dirtyCompNodeCount" / Int32ul,
        "canvasesPainted" / Int32ul,
        "pixelsPainted" / Int32ul,
        "paintTime" / Double,
        "pixelsPresented" / Int32ul,
        "pixelsScrolled" / Int32ul,
        "presentTime" / Double
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=41, version=2)
class OfficeAirSpace_41_2(Etw):
    pattern = Struct(
        "frameId" / Int32ul,
        "frameTimestamp" / Double,
        "handle" / Int32ul,
        "width" / Int32ul,
        "height" / Int32ul,
        "totalCompNodeCount" / Int32ul,
        "dirtyCompNodeCount" / Int32ul,
        "pixelsPainted" / Int32ul,
        "paintTime" / Double,
        "pixelsPresented" / Int32ul,
        "pixelsScrolled" / Int32ul,
        "presentTime" / Double
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=42, version=2)
class OfficeAirSpace_42_2(Etw):
    pattern = Struct(
        "hardwareMode" / Int8ul,
        "sharedDevice" / Int8ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=43, version=2)
class OfficeAirSpace_43_2(Etw):
    pattern = Struct(
        "enabled" / Int8ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=46, version=2)
class OfficeAirSpace_46_2(Etw):
    pattern = Struct(
        "hwnd" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=47, version=2)
class OfficeAirSpace_47_2(Etw):
    pattern = Struct(
        "hwnd" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=48, version=2)
class OfficeAirSpace_48_2(Etw):
    pattern = Struct(
        "handle" / Int32ul,
        "hwnd" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=49, version=2)
class OfficeAirSpace_49_2(Etw):
    pattern = Struct(
        "handle" / Int32ul,
        "hwnd" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=50, version=2)
class OfficeAirSpace_50_2(Etw):
    pattern = Struct(
        "pixelsScrolled" / Int32ul,
        "pixelsPresented" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=51, version=1)
class OfficeAirSpace_51_1(Etw):
    pattern = Struct(
        "batched" / Int8ul,
        "channelCommandId" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=52, version=1)
class OfficeAirSpace_52_1(Etw):
    pattern = Struct(
        "start" / Int8ul,
        "batchId" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=53, version=2)
class OfficeAirSpace_53_2(Etw):
    pattern = Struct(
        "frameTimestamp" / Double,
        "FramesPerSecond" / Double,
        "PresentsPerSecond" / Double
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=55, version=1)
class OfficeAirSpace_55_1(Etw):
    pattern = Struct(
        "method" / Int32ul,
        "numBytesUpdated" / Int32ul,
        "textureHandle" / Int32ul,
        "x" / Int32ul,
        "y" / Int32ul,
        "width" / Int32ul,
        "height" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=56, version=1)
class OfficeAirSpace_56_1(Etw):
    pattern = Struct(
        "batchId" / Int32ul,
        "frameId" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=59, version=2)
class OfficeAirSpace_59_2(Etw):
    pattern = Struct(
        "droppedForLowResourceMode" / Int8ul,
        "deviceLostNotificationPending" / Int8ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=60, version=2)
class OfficeAirSpace_60_2(Etw):
    pattern = Struct(
        "handle" / Int32ul,
        "hwnd" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=61, version=2)
class OfficeAirSpace_61_2(Etw):
    pattern = Struct(
        "isFrontEndDevice" / Int8ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=62, version=2)
class OfficeAirSpace_62_2(Etw):
    pattern = Struct(
        "handle" / Int32ul,
        "hwnd" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=63, version=2)
class OfficeAirSpace_63_2(Etw):
    pattern = Struct(
        "isHardware" / Int8ul,
        "featureLevel" / Int32ul,
        "adapterLuidLowPart" / Int32ul,
        "adapterLuidHighPart" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=67, version=2)
class OfficeAirSpace_67_2(Etw):
    pattern = Struct(
        "handle" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=68, version=2)
class OfficeAirSpace_68_2(Etw):
    pattern = Struct(
        "handle" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=69, version=2)
class OfficeAirSpace_69_2(Etw):
    pattern = Struct(
        "ControlCount" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=70, version=2)
class OfficeAirSpace_70_2(Etw):
    pattern = Struct(
        "handle" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=71, version=2)
class OfficeAirSpace_71_2(Etw):
    pattern = Struct(
        "handle" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=72, version=2)
class OfficeAirSpace_72_2(Etw):
    pattern = Struct(
        "ControlCount" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=73, version=2)
class OfficeAirSpace_73_2(Etw):
    pattern = Struct(
        "handle" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=74, version=2)
class OfficeAirSpace_74_2(Etw):
    pattern = Struct(
        "handle" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=75, version=2)
class OfficeAirSpace_75_2(Etw):
    pattern = Struct(
        "level" / Int32sl,
        "category" / Int32sl,
        "message" / WString
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=78, version=2)
class OfficeAirSpace_78_2(Etw):
    pattern = Struct(
        "XamlDrawableSurface" / Int64ul,
        "XamlDrawResult" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=79, version=2)
class OfficeAirSpace_79_2(Etw):
    pattern = Struct(
        "XamlVirtualSurface" / Int64ul,
        "X" / Int32ul,
        "Y" / Int32ul,
        "Width" / Int32ul,
        "Height" / Int32ul,
        "IsDrawOutstanding" / Int8ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=80, version=2)
class OfficeAirSpace_80_2(Etw):
    pattern = Struct(
        "ObjectHandle" / Int32ul,
        "Mode" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=81, version=2)
class OfficeAirSpace_81_2(Etw):
    pattern = Struct(
        "CommandListComposite" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=82, version=2)
class OfficeAirSpace_82_2(Etw):
    pattern = Struct(
        "XamlVirtualizedSurface" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=83, version=2)
class OfficeAirSpace_83_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "RectX" / Int32ul,
        "RectY" / Int32ul,
        "RectWidth" / Int32ul,
        "RectHeight" / Int32ul,
        "Fidelity" / Float32l
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=84, version=2)
class OfficeAirSpace_84_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=85, version=2)
class OfficeAirSpace_85_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "ID2D1RenderTarget" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=86, version=2)
class OfficeAirSpace_86_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=87, version=2)
class OfficeAirSpace_87_2(Etw):
    pattern = Struct(
        "CommandListComposite" / Int64ul,
        "RectX" / Int32ul,
        "RectY" / Int32ul,
        "RectWidth" / Int32ul,
        "RectHeight" / Int32ul,
        "OutstandingDraw" / Int8ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=88, version=2)
class OfficeAirSpace_88_2(Etw):
    pattern = Struct(
        "Width" / Double,
        "Height" / Double
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=89, version=2)
class OfficeAirSpace_89_2(Etw):
    pattern = Struct(
        "XamlVirtualizedSurface" / Int64ul,
        "IVirtualSurfaceImageSourceNative" / Int64ul,
        "NumberOfRects" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=90, version=2)
class OfficeAirSpace_90_2(Etw):
    pattern = Struct(
        "CommandListComposite" / Int64ul,
        "RectX" / Int32ul,
        "RectY" / Int32ul,
        "RectWidth" / Int32ul,
        "RectHeight" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=91, version=2)
class OfficeAirSpace_91_2(Etw):
    pattern = Struct(
        "XamlDrawableSurface" / Int64ul,
        "ISurfaceImageSourceNativeWithD2D" / Int64ul,
        "ID2D1DeviceContext" / Int64ul,
        "IDXGISurface" / Int64ul,
        "OffsetX" / Int32sl,
        "OffsetY" / Int32sl
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=92, version=2)
class OfficeAirSpace_92_2(Etw):
    pattern = Struct(
        "CommandListComposite" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=93, version=2)
class OfficeAirSpace_93_2(Etw):
    pattern = Struct(
        "PrefetchScope" / Int64ul,
        "NumberOfRootEvents" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=94, version=2)
class OfficeAirSpace_94_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "ID2D1RenderTarget" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=95, version=2)
class OfficeAirSpace_95_2(Etw):
    pattern = Struct(
        "XamlVirtualizedSurface" / Int64ul,
        "IVirtualSurfaceImageSourceNative" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=96, version=2)
class OfficeAirSpace_96_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=97, version=2)
class OfficeAirSpace_97_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "RectX" / Int32ul,
        "RectY" / Int32ul,
        "RectWidth" / Int32ul,
        "RectHeight" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=98, version=2)
class OfficeAirSpace_98_2(Etw):
    pattern = Struct(
        "CommandListComposite" / Int64ul,
        "OldWidth" / Int32ul,
        "OldHeight" / Int32ul,
        "NewWidth" / Int32ul,
        "NewHeight" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=99, version=2)
class OfficeAirSpace_99_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=100, version=2)
class OfficeAirSpace_100_2(Etw):
    pattern = Struct(
        "XamlDrawableSurface" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=101, version=2)
class OfficeAirSpace_101_2(Etw):
    pattern = Struct(
        "CommandListComposite" / Int64ul,
        "RectX" / Int32ul,
        "RectY" / Int32ul,
        "RectWidth" / Int32ul,
        "RectHeight" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=102, version=2)
class OfficeAirSpace_102_2(Etw):
    pattern = Struct(
        "XamlVirtualizedSurface" / Int64ul,
        "RectX" / Int32ul,
        "RectY" / Int32ul,
        "RectWidth" / Int32ul,
        "RectHeight" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=103, version=2)
class OfficeAirSpace_103_2(Etw):
    pattern = Struct(
        "PrefetchScope" / Int64ul,
        "PointX" / Int32ul,
        "PointY" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=104, version=2)
class OfficeAirSpace_104_2(Etw):
    pattern = Struct(
        "XamlDrawableSurface" / Int64ul,
        "ISurfaceImageSourceNativeWithD2D" / Int64ul,
        "RectX" / Int32ul,
        "RectY" / Int32ul,
        "RectWidth" / Int32ul,
        "RectHeight" / Int32ul,
        "DpiX" / Float32l,
        "DpiY" / Float32l
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=105, version=2)
class OfficeAirSpace_105_2(Etw):
    pattern = Struct(
        "XamlVirtualSurface" / Int64ul,
        "NewWidth" / Int32ul,
        "NewHeight" / Int32ul,
        "IsDrawOutstanding" / Int8ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=106, version=2)
class OfficeAirSpace_106_2(Etw):
    pattern = Struct(
        "CommandList" / Int64ul,
        "ID2D1DeviceContext" / Int64ul,
        "RectX" / Int32ul,
        "RectY" / Int32ul,
        "RectWidth" / Int32ul,
        "RectHeight" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=107, version=2)
class OfficeAirSpace_107_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "ID2D1DeviceContext" / Int64ul,
        "ID2D1CommandList" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=108, version=2)
class OfficeAirSpace_108_2(Etw):
    pattern = Struct(
        "CommandListComposite" / Int64ul,
        "NumberTrimmed" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=109, version=2)
class OfficeAirSpace_109_2(Etw):
    pattern = Struct(
        "CanvasOffsetX" / Double,
        "CanvasOffsetY" / Double,
        "AdjustedOffsetX" / Double,
        "AdjustedOffsetY" / Double
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=110, version=2)
class OfficeAirSpace_110_2(Etw):
    pattern = Struct(
        "CommandListComposite" / Int64ul,
        "Success" / Int8ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=111, version=2)
class OfficeAirSpace_111_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "Zoom" / Double
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=112, version=2)
class OfficeAirSpace_112_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "Width" / Int32ul,
        "Height" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=113, version=2)
class OfficeAirSpace_113_2(Etw):
    pattern = Struct(
        "CommandListComposite" / Int64ul,
        "RectX" / Int32ul,
        "RectY" / Int32ul,
        "RectWidth" / Int32ul,
        "RectHeight" / Int32ul,
        "NumberOfCommandLists" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=114, version=2)
class OfficeAirSpace_114_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "ISurfaceImageSourceNativeWithD2D" / Int64ul,
        "IDXGISurface" / Int64ul,
        "OffsetX" / Int32sl,
        "OffsetY" / Int32sl,
        "ID2D1DeviceContext" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=115, version=2)
class OfficeAirSpace_115_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=116, version=2)
class OfficeAirSpace_116_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "IVirtualSurfaceImageSource" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=117, version=2)
class OfficeAirSpace_117_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "Width" / Int32ul,
        "Height" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=118, version=2)
class OfficeAirSpace_118_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "CommandListRasterizerSource" / Int64ul,
        "CommandListComposite" / Int64ul,
        "VSISTiler" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=119, version=2)
class OfficeAirSpace_119_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "ISurfaceImageSource" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=120, version=2)
class OfficeAirSpace_120_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "IVirtualSurfaceImageSource" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=121, version=2)
class OfficeAirSpace_121_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "ID2D1RenderTarget" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=122, version=2)
class OfficeAirSpace_122_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "RectX" / Int32ul,
        "RectY" / Int32ul,
        "RectWidth" / Int32ul,
        "RectHeight" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=123, version=2)
class OfficeAirSpace_123_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "XamlMultithreadNativeSurfaceUI" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=124, version=2)
class OfficeAirSpace_124_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=125, version=2)
class OfficeAirSpace_125_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "TextureType" / Int32ul,
        "XamlVirtualizedSurface" / Int64ul,
        "XamlDrawableSurface" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=126, version=2)
class OfficeAirSpace_126_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "RectX" / Int32ul,
        "RectY" / Int32ul,
        "RectWidth" / Int32ul,
        "RectHeight" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=127, version=2)
class OfficeAirSpace_127_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "RectX" / Int32ul,
        "RectY" / Int32ul,
        "RectWidth" / Int32ul,
        "RectHeight" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=128, version=2)
class OfficeAirSpace_128_2(Etw):
    pattern = Struct(
        "Width" / Int32ul,
        "Height" / Int32ul,
        "MaxTextureDimension" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=129, version=2)
class OfficeAirSpace_129_2(Etw):
    pattern = Struct(
        "Width" / Int32ul,
        "Height" / Int32ul,
        "MaxTextureDimension" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=130, version=2)
class OfficeAirSpace_130_2(Etw):
    pattern = Struct(
        "Width" / Int32ul,
        "Height" / Int32ul,
        "MaxTextureDimension" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=131, version=2)
class OfficeAirSpace_131_2(Etw):
    pattern = Struct(
        "Width" / Int32ul,
        "Height" / Int32ul,
        "MaxTextureDimension" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=132, version=2)
class OfficeAirSpace_132_2(Etw):
    pattern = Struct(
        "Width" / Int32ul,
        "Height" / Int32ul,
        "MaxTextureDimension" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=133, version=2)
class OfficeAirSpace_133_2(Etw):
    pattern = Struct(
        "Width" / Int32ul,
        "Height" / Int32ul,
        "MaxTextureDimension" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=134, version=2)
class OfficeAirSpace_134_2(Etw):
    pattern = Struct(
        "Width" / Int32ul,
        "Height" / Int32ul,
        "MaxTextureDimension" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=135, version=2)
class OfficeAirSpace_135_2(Etw):
    pattern = Struct(
        "Width" / Int32ul,
        "Height" / Int32ul,
        "MaxTextureDimension" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=136, version=2)
class OfficeAirSpace_136_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "NullRenderTargetReason" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=137, version=2)
class OfficeAirSpace_137_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "NullRenderTargetReason" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=138, version=2)
class OfficeAirSpace_138_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "OffsetX" / Double,
        "OffsetY" / Double,
        "VirtualOffsetX" / Double,
        "VirtualOffsetY" / Double,
        "ZoomFactor" / Float32l,
        "CanvasWidth" / Double,
        "CanvasHeight" / Double,
        "VirtualCanvasWidth" / Double,
        "VirtualCanvasHeight" / Double,
        "ViewportWidth" / Double,
        "ViewportHeight" / Double,
        "IsRTL" / Int8ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=139, version=2)
class OfficeAirSpace_139_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "VirtualZoomedX" / Double,
        "VirtualZoomedY" / Double,
        "RealUnzoomedX" / Double,
        "RealUnzoomedY" / Double,
        "VirtualZoomedX_Rtl" / Double,
        "VirtualZoomedY_Rtl" / Double,
        "RealUnzoomedX_Rtl" / Double,
        "RealUnzoomedY_Rtl" / Double,
        "currentZoom" / Float32l,
        "IsIntermediate" / Int8ul,
        "Width" / Double,
        "Height" / Double
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=140, version=2)
class OfficeAirSpace_140_2(Etw):
    pattern = Struct(
        "InkInputMode" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=141, version=2)
class OfficeAirSpace_141_2(Etw):
    pattern = Struct(
        "PenStroke" / Int8ul,
        "PresentCount" / Int32ul,
        "SyncQPCTime" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=142, version=2)
class OfficeAirSpace_142_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "Directionality" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=143, version=2)
class OfficeAirSpace_143_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "Directionality" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=144, version=2)
class OfficeAirSpace_144_2(Etw):
    pattern = Struct(
        "Tag1" / Int32ul,
        "QpcTime" / Int64ul,
        "DeltaTime" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=145, version=2)
class OfficeAirSpace_145_2(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=146, version=2)
class OfficeAirSpace_146_2(Etw):
    pattern = Struct(
        "Bitmap" / Int8ul,
        "Thread" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=147, version=2)
class OfficeAirSpace_147_2(Etw):
    pattern = Struct(
        "Resize" / Int8ul,
        "Width" / Int32ul,
        "Height" / Int32ul,
        "Thread" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=148, version=2)
class OfficeAirSpace_148_2(Etw):
    pattern = Struct(
        "Bitmap" / Int8ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=149, version=2)
class OfficeAirSpace_149_2(Etw):
    pattern = Struct(
        "Resize" / Int8ul,
        "Width" / Int32ul,
        "Height" / Int32ul,
        "Thread" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=150, version=2)
class OfficeAirSpace_150_2(Etw):
    pattern = Struct(
        "Thread" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=151, version=2)
class OfficeAirSpace_151_2(Etw):
    pattern = Struct(
        "TAG" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=152, version=2)
class OfficeAirSpace_152_2(Etw):
    pattern = Struct(
        "Context" / Int8ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=153, version=2)
class OfficeAirSpace_153_2(Etw):
    pattern = Struct(
        "xDpi" / Float32l,
        "yDpi" / Float32l
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=154, version=2)
class OfficeAirSpace_154_2(Etw):
    pattern = Struct(
        "xDpi" / Float32l,
        "yDpi" / Float32l
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=155, version=2)
class OfficeAirSpace_155_2(Etw):
    pattern = Struct(
        "newDpi" / Float32l
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=156, version=2)
class OfficeAirSpace_156_2(Etw):
    pattern = Struct(
        "layerHandle" / Int32sl,
        "animationClass" / CString,
        "animation" / CString,
        "storyboardHandle" / Int32sl,
        "triggerProperty" / Int32ul,
        "triggerValue" / Double,
        "eventType" / Int32ul,
        "customEvent" / Int32ul,
        "looping" / Int8ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=159, version=2)
class OfficeAirSpace_159_2(Etw):
    pattern = Struct(
        "xPoint" / Int32sl,
        "yPoint" / Int32sl
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=160, version=2)
class OfficeAirSpace_160_2(Etw):
    pattern = Struct(
        "xPoint" / Int32sl,
        "yPoint" / Int32sl,
        "Succeeded" / Int8ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=161, version=2)
class OfficeAirSpace_161_2(Etw):
    pattern = Struct(
        "xPoint" / Int32sl,
        "yPoint" / Int32sl
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=162, version=2)
class OfficeAirSpace_162_2(Etw):
    pattern = Struct(
        "xPoint" / Int32sl,
        "yPoint" / Int32sl,
        "HitLayerHandle" / Int32ul,
        "xLayer" / Double,
        "yLayer" / Double
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=163, version=2)
class OfficeAirSpace_163_2(Etw):
    pattern = Struct(
        "XamlNativeSurface" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=164, version=2)
class OfficeAirSpace_164_2(Etw):
    pattern = Struct(
        "XamlNativeSurface" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=165, version=2)
class OfficeAirSpace_165_2(Etw):
    pattern = Struct(
        "ReadyToPresent" / Int8ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=166, version=2)
class OfficeAirSpace_166_2(Etw):
    pattern = Struct(
        "PointerId" / Int32ul,
        "PointCount" / Int32ul,
        "RectX" / Int32ul,
        "RectY" / Int32ul,
        "RectWidth" / Int32ul,
        "RectHeight" / Int32ul,
        "PresentCount" / Int32ul,
        "SyncQPCTime" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=167, version=2)
class OfficeAirSpace_167_2(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul,
        "Tag1" / Int32ul,
        "Tag2" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=168, version=2)
class OfficeAirSpace_168_2(Etw):
    pattern = Struct(
        "SyncQPCTime" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=169, version=2)
class OfficeAirSpace_169_2(Etw):
    pattern = Struct(
        "StartTime" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=170, version=2)
class OfficeAirSpace_170_2(Etw):
    pattern = Struct(
        "PointerId" / Int32ul,
        "PointCount" / Int32ul,
        "SyncQPCTime" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=171, version=2)
class OfficeAirSpace_171_2(Etw):
    pattern = Struct(
        "PresentSyncRefreshCountDelta" / Int32ul,
        "LastPresentSyncRefreshCountDelta" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=172, version=2)
class OfficeAirSpace_172_2(Etw):
    pattern = Struct(
        "PointerId" / Int32ul,
        "PointCount" / Int32ul,
        "SyncQPCTime" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=173, version=2)
class OfficeAirSpace_173_2(Etw):
    pattern = Struct(
        "TAG" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=174, version=2)
class OfficeAirSpace_174_2(Etw):
    pattern = Struct(
        "SyncQPCTime" / Int64ul,
        "PresentCount" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=175, version=2)
class OfficeAirSpace_175_2(Etw):
    pattern = Struct(
        "PointerId" / Int32ul,
        "NewPointCount" / Int32ul,
        "PointCount" / Int32ul,
        "SyncQPCTime" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=176, version=2)
class OfficeAirSpace_176_2(Etw):
    pattern = Struct(
        "PresentCount" / Int32ul,
        "RefreshCount" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=177, version=2)
class OfficeAirSpace_177_2(Etw):
    pattern = Struct(
        "StopTime" / Int64ul,
        "DeltaTime" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=178, version=2)
class OfficeAirSpace_178_2(Etw):
    pattern = Struct(
        "PointerId" / Int32ul,
        "NewPointCount" / Int32ul,
        "PointCount" / Int32ul,
        "SyncQPCTime" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=179, version=2)
class OfficeAirSpace_179_2(Etw):
    pattern = Struct(
        "PresentCount" / Int32ul,
        "PresentRefreshCount" / Int32ul,
        "SyncRefreshCount" / Int32ul,
        "TotalPointCount" / Int32ul,
        "SyncQPCTime" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=180, version=2)
class OfficeAirSpace_180_2(Etw):
    pattern = Struct(
        "GetLastPresentCount" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=181, version=2)
class OfficeAirSpace_181_2(Etw):
    pattern = Struct(
        "PointerId" / Int32ul,
        "TotalPointCount" / Int32ul,
        "PresentCount" / Int32ul,
        "SyncQPCTime" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=182, version=2)
class OfficeAirSpace_182_2(Etw):
    pattern = Struct(
        "Tag" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=183, version=2)
class OfficeAirSpace_183_2(Etw):
    pattern = Struct(
        "ForceToPresent" / Int8ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=184, version=2)
class OfficeAirSpace_184_2(Etw):
    pattern = Struct(
        "XamlDrawableSurface" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=185, version=2)
class OfficeAirSpace_185_2(Etw):
    pattern = Struct(
        "XamlMultithreadDrawableSurfaceOffThread" / Int64ul,
        "XamlMultithreadNativeSurface" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=186, version=2)
class OfficeAirSpace_186_2(Etw):
    pattern = Struct(
        "XamlDrawableSurface" / Int64ul,
        "State" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=187, version=2)
class OfficeAirSpace_187_2(Etw):
    pattern = Struct(
        "XamlMultithreadDrawableSurfaceOffThread" / Int64ul,
        "Result" / Int8ul,
        "InBatch" / Int8ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=188, version=2)
class OfficeAirSpace_188_2(Etw):
    pattern = Struct(
        "XamlDrawableSurface" / Int64ul,
        "ID2D1DeviceContext" / Int64ul,
        "EndDrawDirect2dResult" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=189, version=2)
class OfficeAirSpace_189_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "XamlMultithreadNativeSurfaceOffThread" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=190, version=2)
class OfficeAirSpace_190_2(Etw):
    pattern = Struct(
        "IDXGIDevice" / Int64ul,
        "HResult" / Int32sl
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=191, version=2)
class OfficeAirSpace_191_2(Etw):
    pattern = Struct(
        "XamlMultithreadNativeSurfaceUI" / Int64ul,
        "X" / Int32ul,
        "Y" / Int32ul,
        "Width" / Int32ul,
        "Height" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=192, version=2)
class OfficeAirSpace_192_2(Etw):
    pattern = Struct(
        "XamlDrawableSurface" / Int64ul,
        "XamlDrawResult" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=193, version=2)
class OfficeAirSpace_193_2(Etw):
    pattern = Struct(
        "XamlDrawableSurface" / Int64ul,
        "State" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=194, version=2)
class OfficeAirSpace_194_2(Etw):
    pattern = Struct(
        "XamlMultithreadDrawableSurface" / Int64ul,
        "IXamlMultithreadDrawableSurfaceUser" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=195, version=2)
class OfficeAirSpace_195_2(Etw):
    pattern = Struct(
        "XamlDrawableSurface" / Int64ul,
        "IDXGIDevice" / Int64ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=196, version=2)
class OfficeAirSpace_196_2(Etw):
    pattern = Struct(
        "XamlDrawableSurface" / Int64ul,
        "IDXGISurface" / Int64ul,
        "ID2D1Bitmap1" / Int64ul,
        "offsetX" / Int32sl,
        "offsetY" / Int32sl,
        "State" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=197, version=2)
class OfficeAirSpace_197_2(Etw):
    pattern = Struct(
        "XamlDrawableSurface" / Int64ul,
        "ISurfaceImageSourceNativeWithD2D" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=198, version=2)
class OfficeAirSpace_198_2(Etw):
    pattern = Struct(
        "XamlMultithreadNativeSurfaceUI" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=199, version=2)
class OfficeAirSpace_199_2(Etw):
    pattern = Struct(
        "XamlDrawableSurface" / Int64ul,
        "State" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=200, version=2)
class OfficeAirSpace_200_2(Etw):
    pattern = Struct(
        "XamlDrawableSurface" / Int64ul,
        "State" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=201, version=2)
class OfficeAirSpace_201_2(Etw):
    pattern = Struct(
        "XamlMultithreadNativeSurfaceUI" / Int64ul,
        "SetDeviceCount" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=202, version=2)
class OfficeAirSpace_202_2(Etw):
    pattern = Struct(
        "XamlDrawableSurface" / Int64ul,
        "RectX" / Int32ul,
        "RectY" / Int32ul,
        "RectWidth" / Int32ul,
        "RectHeight" / Int32ul,
        "DpiX" / Float32l,
        "DpiY" / Float32l,
        "IncludeInverseTransform" / Int8ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=203, version=2)
class OfficeAirSpace_203_2(Etw):
    pattern = Struct(
        "XamlMultithreadNativeSurfaceUI" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=204, version=2)
class OfficeAirSpace_204_2(Etw):
    pattern = Struct(
        "XamlDrawableSurface" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=205, version=2)
class OfficeAirSpace_205_2(Etw):
    pattern = Struct(
        "XamlDrawableSurface" / Int64ul,
        "State" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=206, version=2)
class OfficeAirSpace_206_2(Etw):
    pattern = Struct(
        "XamlMultithreadDrawableSurfaceOffThread" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=208, version=2)
class OfficeAirSpace_208_2(Etw):
    pattern = Struct(
        "XamlDrawableSurface" / Int64ul,
        "Drawable" / Int8ul,
        "DeviceMismatch" / Int8ul,
        "XamlDrawResult" / Int32ul,
        "ID2D1DeviceContext" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=209, version=2)
class OfficeAirSpace_209_2(Etw):
    pattern = Struct(
        "UpdateInstanceStopTime" / Int64ul,
        "DeltaTime" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=210, version=2)
class OfficeAirSpace_210_2(Etw):
    pattern = Struct(
        "X" / Double,
        "Y" / Double,
        "pointerId" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=211, version=2)
class OfficeAirSpace_211_2(Etw):
    pattern = Struct(
        "X" / Double,
        "Y" / Double,
        "pointerId" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=212, version=2)
class OfficeAirSpace_212_2(Etw):
    pattern = Struct(
        "UpdateInstanceCalcTime" / Int64ul,
        "DeltaTime" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=213, version=2)
class OfficeAirSpace_213_2(Etw):
    pattern = Struct(
        "horizontal" / Float32l,
        "vertical" / Float32l,
        "left" / Double,
        "top" / Double,
        "width" / Double,
        "height" / Double
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=214, version=2)
class OfficeAirSpace_214_2(Etw):
    pattern = Struct(
        "layerCount" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=215, version=2)
class OfficeAirSpace_215_2(Etw):
    pattern = Struct(
        "eventType" / Int32ul,
        "UpdateInstanceStartTime" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=216, version=2)
class OfficeAirSpace_216_2(Etw):
    pattern = Struct(
        "CommandListRasterizeWork" / Int64ul,
        "NumberOfCommandLists" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=217, version=2)
class OfficeAirSpace_217_2(Etw):
    pattern = Struct(
        "CommandListRasterizeWork" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=218, version=2)
class OfficeAirSpace_218_2(Etw):
    pattern = Struct(
        "CommandListRasterizeWork" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=219, version=2)
class OfficeAirSpace_219_2(Etw):
    pattern = Struct(
        "CommandListRasterizer" / Int64ul,
        "CommandListRasterizeWork" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=221, version=2)
class OfficeAirSpace_221_2(Etw):
    pattern = Struct(
        "Width" / Int32ul,
        "Height" / Int32ul,
        "MaxTextureDimension" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=222, version=2)
class OfficeAirSpace_222_2(Etw):
    pattern = Struct(
        "AreAnimationsDisabled" / Int8ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=223, version=2)
class OfficeAirSpace_223_2(Etw):
    pattern = Struct(
        "Width" / Int32ul,
        "Height" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=224, version=2)
class OfficeAirSpace_224_2(Etw):
    pattern = Struct(
        "X" / Int32ul,
        "Y" / Int32ul,
        "Width" / Int32ul,
        "Height" / Int32ul,
        "TileId" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=225, version=2)
class OfficeAirSpace_225_2(Etw):
    pattern = Struct(
        "X" / Int32ul,
        "Y" / Int32ul,
        "Width" / Int32ul,
        "Height" / Int32ul,
        "TileId" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=226, version=2)
class OfficeAirSpace_226_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "tileId" / Int32ul,
        "RectX" / Int32ul,
        "RectY" / Int32ul,
        "RectWidth" / Int32ul,
        "RectHeight" / Int32ul,
        "RasterizeOnUI" / Int8ul,
        "XamlMultithreadVirtualSurfaceUI" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=227, version=2)
class OfficeAirSpace_227_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "tileId" / Int8ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=228, version=2)
class OfficeAirSpace_228_2(Etw):
    pattern = Struct(
        "Width" / Int32ul,
        "Height" / Int32ul,
        "Number" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=229, version=2)
class OfficeAirSpace_229_2(Etw):
    pattern = Struct(
        "XamlMultithreadNativeSurfaceUI" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=230, version=2)
class OfficeAirSpace_230_2(Etw):
    pattern = Struct(
        "XamlVirtualizedSurface" / Int64ul,
        "RectX" / Int32ul,
        "RectY" / Int32ul,
        "RectWidth" / Int32ul,
        "RectHeight" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=231, version=2)
class OfficeAirSpace_231_2(Etw):
    pattern = Struct(
        "XamlNativeSurface" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=232, version=2)
class OfficeAirSpace_232_2(Etw):
    pattern = Struct(
        "XamlVirtualizedSurface" / Int64ul,
        "IVirtualSurfaceImageSourceNative" / Int64ul,
        "NumberOfRects" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=233, version=2)
class OfficeAirSpace_233_2(Etw):
    pattern = Struct(
        "XamlVirtualizedSurface" / Int64ul,
        "IVirtualSurfaceImageSourceNative" / Int64ul,
        "RectX" / Int32ul,
        "RectY" / Int32ul,
        "RectWidth" / Int32ul,
        "RectHeight" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=234, version=2)
class OfficeAirSpace_234_2(Etw):
    pattern = Struct(
        "XamlVirtualizedSurface" / Int64ul,
        "IVirtualSurfaceImageSourceNative" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=235, version=2)
class OfficeAirSpace_235_2(Etw):
    pattern = Struct(
        "XamlVirtualizedSurface" / Int64ul,
        "IVirtualSurfaceImageSourceNative" / Int64ul,
        "Width" / Int32ul,
        "Height" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=236, version=2)
class OfficeAirSpace_236_2(Etw):
    pattern = Struct(
        "XamlNativeSurface" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=237, version=2)
class OfficeAirSpace_237_2(Etw):
    pattern = Struct(
        "XamlVirtualizedSurface" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=238, version=2)
class OfficeAirSpace_238_2(Etw):
    pattern = Struct(
        "XamlVirtualSurface" / Int64ul,
        "IXamlDrawableSurface" / Int64ul,
        "Width" / Int32ul,
        "Height" / Int32ul,
        "Opaque" / Int8ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=239, version=2)
class OfficeAirSpace_239_2(Etw):
    pattern = Struct(
        "XamlMultithreadNativeSurface" / Int64ul,
        "IXamlMultithreadDrawableSurfaceUser" / Int64ul,
        "IXamlDrawableSurface" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=240, version=2)
class OfficeAirSpace_240_2(Etw):
    pattern = Struct(
        "XamlSurface" / Int64ul,
        "IXamlDrawableSurface" / Int64ul,
        "Width" / Int32ul,
        "Height" / Int32ul,
        "Opaque" / Int8ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=241, version=2)
class OfficeAirSpace_241_2(Etw):
    pattern = Struct(
        "VirtualTexture" / Int64ul,
        "VirtualTextureEvents" / Int64ul,
        "Handle" / Int32ul,
        "Width" / Int32ul,
        "Height" / Int32ul,
        "Opaque" / Int8ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=242, version=2)
class OfficeAirSpace_242_2(Etw):
    pattern = Struct(
        "VirtualTextureEvents" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=243, version=2)
class OfficeAirSpace_243_2(Etw):
    pattern = Struct(
        "XamlMultithreadNativeSurface" / Int64ul,
        "IXamlMultithreadDrawableSurfaceUser" / Int64ul,
        "IXamlDrawableSurface" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=244, version=2)
class OfficeAirSpace_244_2(Etw):
    pattern = Struct(
        "XamlVirtualizedSurface" / Int64ul,
        "Width" / Int32ul,
        "Height" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=245, version=2)
class OfficeAirSpace_245_2(Etw):
    pattern = Struct(
        "XamlVirtualSurface" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=246, version=2)
class OfficeAirSpace_246_2(Etw):
    pattern = Struct(
        "XamlVirtualSurface" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=247, version=2)
class OfficeAirSpace_247_2(Etw):
    pattern = Struct(
        "XamlVirtualSurface" / Int64ul,
        "Width" / Int32ul,
        "Height" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=248, version=2)
class OfficeAirSpace_248_2(Etw):
    pattern = Struct(
        "OfficeDeviceLost" / Int8ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=249, version=2)
class OfficeAirSpace_249_2(Etw):
    pattern = Struct(
        "InputType" / Int32sl,
        "LayerWidth" / Double,
        "LayerHeight" / Double,
        "SlopAmount" / Int32ul,
        "SlopUsedX" / Double,
        "SlopUsedY" / Double,
        "IsHighDPI" / Int8ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=250, version=2)
class OfficeAirSpace_250_2(Etw):
    pattern = Struct(
        "CanvasOffsetX" / Double,
        "CanvasOffsetY" / Double,
        "AdjustedOffsetX" / Double,
        "AdjustedOffsetY" / Double
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=251, version=2)
class OfficeAirSpace_251_2(Etw):
    pattern = Struct(
        "CanvasOffsetX" / Double,
        "CanvasOffsetY" / Double,
        "AdjustedOffsetX" / Double,
        "AdjustedOffsetY" / Double
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=252, version=2)
class OfficeAirSpace_252_2(Etw):
    pattern = Struct(
        "MaxLimit" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=253, version=2)
class OfficeAirSpace_253_2(Etw):
    pattern = Struct(
        "MemoryUsage" / Int32ul,
        "IsInLowResourceMode" / Int8ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=254, version=2)
class OfficeAirSpace_254_2(Etw):
    pattern = Struct(
        "value1" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=257, version=2)
class OfficeAirSpace_257_2(Etw):
    pattern = Struct(
        "PendingScrollTo" / Int8ul,
        "PendingZoomTo" / Int8ul,
        "PendingSetCanvasSize" / Int8ul,
        "IsFIrstScroll" / Int8ul,
        "OffsetX" / Double,
        "OffsetY" / Double,
        "ZoomFactor" / Double
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=258, version=2)
class OfficeAirSpace_258_2(Etw):
    pattern = Struct(
        "ResetPendingScrollTo" / Int8ul,
        "PendingScrollTo" / Int8ul,
        "OffsetX" / Double,
        "OffSetY" / Double
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=259, version=2)
class OfficeAirSpace_259_2(Etw):
    pattern = Struct(
        "ResetPendingZoomTo" / Int8ul,
        "PendingZoomTo" / Int8ul,
        "ZoomFactor" / Double
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=260, version=2)
class OfficeAirSpace_260_2(Etw):
    pattern = Struct(
        "Layer" / Int64ul,
        "Handle" / Int32ul,
        "Property" / Int32ul,
        "Value" / Double
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=261, version=2)
class OfficeAirSpace_261_2(Etw):
    pattern = Struct(
        "Layer" / Int64ul,
        "Handle" / Int32ul,
        "Offset" / Double,
        "ParentAnchor" / Float32l
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=262, version=2)
class OfficeAirSpace_262_2(Etw):
    pattern = Struct(
        "Layer" / Int64ul,
        "Handle" / Int32ul,
        "Offset" / Double,
        "ParentAnchor" / Float32l
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=263, version=2)
class OfficeAirSpace_263_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "ViewportOffsetRealX" / Double,
        "ViewportOffsetRealY" / Double,
        "OldVirtualOffsetX" / Double,
        "OldVirtualOffsetY" / Double,
        "NewVirtualOffsetX" / Double,
        "NewVirtualOffsetY" / Double,
        "OldCanvasSizeVirtualX" / Double,
        "OldCanvasSizeVirtualY" / Double,
        "NewCanvasSizeVirtualX" / Double,
        "NewCanvasSizeVirtualY" / Double,
        "OldPlatformViewportOffsetX" / Double,
        "OldPlatformViewportOffsetY" / Double,
        "NewPlatformViewportOffsetX" / Double,
        "NewPlatformViewportOffsetY" / Double
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=264, version=2)
class OfficeAirSpace_264_2(Etw):
    pattern = Struct(
        "Layer" / Int64ul,
        "Handle" / Int32ul,
        "Width" / Double,
        "AdjustRightEdge" / Int8ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=265, version=2)
class OfficeAirSpace_265_2(Etw):
    pattern = Struct(
        "Layer" / Int64ul,
        "Handle" / Int32ul,
        "Height" / Double
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=266, version=2)
class OfficeAirSpace_266_2(Etw):
    pattern = Struct(
        "Layer" / Int64ul,
        "Handle" / Int32ul,
        "Offset" / Double,
        "ParentAnchor" / Float32l
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=268, version=2)
class OfficeAirSpace_268_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "VirtualZoomedX" / Double,
        "VirtualZoomedY" / Double,
        "RealUnzoomedX" / Double,
        "RealUnzoomedY" / Double,
        "VirtualZoomedX_Rtl" / Double,
        "VirtualZoomedY_Rtl" / Double,
        "RealUnzoomedX_Rtl" / Double,
        "RealUnzoomedY_Rtl" / Double,
        "finalZoom" / Float32l,
        "Width" / Double,
        "Height" / Double,
        "IsAnimated" / Int8ul,
        "VirtualPerimeterChanged" / Int8ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=269, version=2)
class OfficeAirSpace_269_2(Etw):
    pattern = Struct(
        "Layer" / Int64ul,
        "Handle" / Int32ul,
        "TileId" / Int32ul,
        "TileRectX" / Int32ul,
        "TileRectY" / Int32ul,
        "TileRectWidth" / Int32ul,
        "TileRectHeight" / Int32ul,
        "VirtualOffsetX" / Double,
        "VirtualOffsetY" / Double
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=270, version=2)
class OfficeAirSpace_270_2(Etw):
    pattern = Struct(
        "Layer" / Int64ul,
        "Handle" / Int32ul,
        "Height" / Double,
        "AdjustRightEdge" / Int8ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=271, version=2)
class OfficeAirSpace_271_2(Etw):
    pattern = Struct(
        "Layer" / Int64ul,
        "Handle" / Int32ul,
        "TileId" / Int32ul,
        "IsRecyclingTile" / Int8ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=272, version=2)
class OfficeAirSpace_272_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "VirtualOffsetNextX" / Double,
        "VirtualOffsetNextY" / Double,
        "ZoomFactorNext" / Double,
        "VirtualOffsetFinalX" / Double,
        "VirtualOffsetFinalY" / Double,
        "ZoomFactorFinal" / Double
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=273, version=2)
class OfficeAirSpace_273_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "X" / Double,
        "Y" / Double,
        "IsRTL" / Int8ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=274, version=2)
class OfficeAirSpace_274_2(Etw):
    pattern = Struct(
        "Layer" / Int64ul,
        "Handle" / Int32ul,
        "TileId" / Int32ul,
        "HiddenTileCount" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=275, version=2)
class OfficeAirSpace_275_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "ViewportX" / Double,
        "ViewportY" / Double,
        "ViewportWidth" / Double,
        "ViewportHeight" / Double,
        "Zoom" / Float32l,
        "IsMoving" / Int8ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=277, version=2)
class OfficeAirSpace_277_2(Etw):
    pattern = Struct(
        "Layer" / Int64ul,
        "Handle" / Int32ul,
        "Offset" / Double,
        "ParentAnchor" / Float32l
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=278, version=2)
class OfficeAirSpace_278_2(Etw):
    pattern = Struct(
        "Layer" / Int64ul,
        "Handle" / Int32ul,
        "OldNumberOfVsisTilesX" / Int32ul,
        "OldNumberOfVsisTilesY" / Int32ul,
        "NewNumberOfVsisTilesX" / Int32ul,
        "NewNumberOfVsisTilesY" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=280, version=2)
class OfficeAirSpace_280_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "virtualPerimeterX" / Double,
        "virtualPerimeterY" / Double,
        "virtualPerimeterWidth" / Double,
        "virtualPerimeterHeight" / Double,
        "CalculatedvirtualPerimeterX" / Double,
        "CalculatedvirtualPerimeterY" / Double,
        "CalculatedvirtualPerimeterWidth" / Double,
        "CalculatedvirtualPerimeterHeight" / Double
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=281, version=2)
class OfficeAirSpace_281_2(Etw):
    pattern = Struct(
        "Layer" / Int64ul,
        "Handle" / Int32ul,
        "virtualPerimeterX" / Double,
        "virtualPerimeterY" / Double,
        "virtualPerimeterWidth" / Double,
        "virtualPerimeterHeight" / Double
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=282, version=2)
class OfficeAirSpace_282_2(Etw):
    pattern = Struct(
        "Layer" / Int64ul,
        "Handle" / Int32ul,
        "Width" / Double
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=283, version=2)
class OfficeAirSpace_283_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "VirtualZoomedX" / Double,
        "VirtualZoomedY" / Double,
        "RealUnzoomedX" / Double,
        "RealUnzoomedY" / Double,
        "VirtualZoomedX_Rtl" / Double,
        "VirtualZoomedY_Rtl" / Double,
        "RealUnzoomedX_Rtl" / Double,
        "RealUnzoomedY_Rtl" / Double,
        "finalZoom" / Float32l,
        "Width" / Double,
        "Height" / Double
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=284, version=2)
class OfficeAirSpace_284_2(Etw):
    pattern = Struct(
        "Layer" / Int64ul,
        "Handle" / Int32ul,
        "virtualPerimeterX" / Double,
        "virtualPerimeterY" / Double,
        "virtualPerimeterWidth" / Double,
        "virtualPerimeterHeight" / Double,
        "parentVirtualOffsetX" / Double,
        "parentVirtualOffsetY" / Double
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=285, version=2)
class OfficeAirSpace_285_2(Etw):
    pattern = Struct(
        "Layer" / Int64ul,
        "Handle" / Int32ul,
        "VirtualizedRectX" / Double,
        "VirtualizedRectY" / Double,
        "VirtualizedRectWidth" / Double,
        "VirtualizedRectHeight" / Double
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=286, version=2)
class OfficeAirSpace_286_2(Etw):
    pattern = Struct(
        "Layer" / Int64ul,
        "Handle" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=287, version=2)
class OfficeAirSpace_287_2(Etw):
    pattern = Struct(
        "Layer" / Int64ul,
        "Handle" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=288, version=2)
class OfficeAirSpace_288_2(Etw):
    pattern = Struct(
        "Layer" / Int64ul,
        "Handle" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=289, version=2)
class OfficeAirSpace_289_2(Etw):
    pattern = Struct(
        "Layer" / Int64ul,
        "Handle" / Int32ul,
        "Width" / Double,
        "Height" / Double
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=290, version=2)
class OfficeAirSpace_290_2(Etw):
    pattern = Struct(
        "Layer" / Int64ul,
        "Handle" / Int32ul,
        "LayerBoundingBoxX" / Float32l,
        "LayerBoundingBoxY" / Float32l,
        "LayerBoundingBoxWidth" / Float32l,
        "LayerBoundingBoxHeight" / Float32l,
        "LayerOffsetFromViewportX" / Float32l,
        "LayerOffsetFromViewportY" / Float32l,
        "Zoom" / Float32l
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=291, version=2)
class OfficeAirSpace_291_2(Etw):
    pattern = Struct(
        "Layer" / Int64ul,
        "Handle" / Int32ul,
        "PointTestX" / Float32l,
        "PointTestY" / Float32l,
        "HitTestOptions" / Int32ul,
        "Zoom" / Float32l,
        "ViewportOffsetX" / Float32l,
        "ViewportOffsetY" / Float32l,
        "HeaderType" / Int32ul,
        "ParentScrollingLayer" / Int32ul,
        "SearchForHitTestData" / Int8ul,
        "InputSourceType" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=292, version=2)
class OfficeAirSpace_292_2(Etw):
    pattern = Struct(
        "Layer" / Int64ul,
        "Handle" / Int32ul,
        "PointX" / Float32l,
        "PointY" / Float32l,
        "PointTestX" / Float32l,
        "PointTestY" / Float32l,
        "HitTestOptions" / Int32ul,
        "Zoom" / Float32l,
        "ViewportOffsetX" / Float32l,
        "ViewportOffsetY" / Float32l,
        "HeaderType" / Int32ul,
        "ParentScrollingLayer" / Int32ul,
        "SearchForHitTestData" / Int8ul,
        "InputSourceType" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=293, version=2)
class OfficeAirSpace_293_2(Etw):
    pattern = Struct(
        "ScrollingLayerCanvas" / Int64ul,
        "ZoomFactor" / Double,
        "IsAnimated" / Int8ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=294, version=2)
class OfficeAirSpace_294_2(Etw):
    pattern = Struct(
        "ScrollingLayerCanvas" / Int64ul,
        "Width" / Double,
        "Height" / Double
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=295, version=2)
class OfficeAirSpace_295_2(Etw):
    pattern = Struct(
        "ScrollingLayerCanvas" / Int64ul,
        "PendingScrollTo" / Int8ul,
        "PendingZoomTo" / Int8ul,
        "PendingSetCanvasSize" / Int8ul,
        "IsFirstScroll" / Int8ul,
        "ScrollToX" / Double,
        "ScrollToY" / Double,
        "ScrollToAnimate" / Int8ul,
        "Zoom" / Double,
        "ZoomAnimate" / Int8ul,
        "Width" / Double,
        "Height" / Double
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=296, version=2)
class OfficeAirSpace_296_2(Etw):
    pattern = Struct(
        "ScrollingLayerCanvas" / Int64ul,
        "OffsetX" / Double,
        "OffsetY" / Double,
        "IsAnimated" / Int8ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=297, version=2)
class OfficeAirSpace_297_2(Etw):
    pattern = Struct(
        "ScrollingLayerCanvas" / Int64ul,
        "CanvasOffsetX" / Double,
        "CanvasOffsetY" / Double,
        "AdjustedOffsetX" / Double,
        "AdjustedOffsetY" / Double
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=298, version=2)
class OfficeAirSpace_298_2(Etw):
    pattern = Struct(
        "ScrollingLayerCanvas" / Int64ul,
        "Zoom" / Double
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=299, version=2)
class OfficeAirSpace_299_2(Etw):
    pattern = Struct(
        "ScrollingLayerCanvas" / Int64ul,
        "Width" / Double,
        "Height" / Double
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=300, version=2)
class OfficeAirSpace_300_2(Etw):
    pattern = Struct(
        "command" / Int32ul,
        "hresult" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=301, version=2)
class OfficeAirSpace_301_2(Etw):
    pattern = Struct(
        "DeviceMode" / Int32ul,
        "ShareDevice" / Int8ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=302, version=2)
class OfficeAirSpace_302_2(Etw):
    pattern = Struct(
        "Scene" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=303, version=2)
class OfficeAirSpace_303_2(Etw):
    pattern = Struct(
        "ReacquireDevice" / Int8ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=304, version=2)
class OfficeAirSpace_304_2(Etw):
    pattern = Struct(
        "DeviceMode" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=305, version=2)
class OfficeAirSpace_305_2(Etw):
    pattern = Struct(
        "DirectXDeviceResources" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=306, version=2)
class OfficeAirSpace_306_2(Etw):
    pattern = Struct(
        "Direct2dDeviceResources" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=307, version=2)
class OfficeAirSpace_307_2(Etw):
    pattern = Struct(
        "DeviceLossType" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=308, version=2)
class OfficeAirSpace_308_2(Etw):
    pattern = Struct(
        "DirectXDeviceResources" / Int64ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=309, version=2)
class OfficeAirSpace_309_2(Etw):
    pattern = Struct(
        "Scene" / Int64ul,
        "LockDevice" / Int8ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=310, version=2)
class OfficeAirSpace_310_2(Etw):
    pattern = Struct(
        "DirectXDeviceResources" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=311, version=2)
class OfficeAirSpace_311_2(Etw):
    pattern = Struct(
        "Scene" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=312, version=2)
class OfficeAirSpace_312_2(Etw):
    pattern = Struct(
        "Direct2dDeviceResources" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=313, version=2)
class OfficeAirSpace_313_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "VirtualZoomedX" / Double,
        "VirtualZoomedY" / Double,
        "RealUnzoomedX" / Double,
        "RealUnzoomedY" / Double,
        "VirtualZoomedX_Rtl" / Double,
        "VirtualZoomedY_Rtl" / Double,
        "RealUnzoomedX_Rtl" / Double,
        "RealUnzoomedY_Rtl" / Double,
        "currentZoom" / Float32l,
        "Width" / Double,
        "Height" / Double
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=314, version=2)
class OfficeAirSpace_314_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "CanvasSizeWidth" / Double,
        "CanvasSizeHeight" / Double
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=315, version=2)
class OfficeAirSpace_315_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "VirtualZoomedX" / Double,
        "VirtualZoomedY" / Double,
        "RealUnzoomedX" / Double,
        "RealUnzoomedY" / Double,
        "VirtualZoomedX_Rtl" / Double,
        "VirtualZoomedY_Rtl" / Double,
        "RealUnzoomedX_Rtl" / Double,
        "RealUnzoomedY_Rtl" / Double,
        "finalZoom" / Float32l,
        "VirtualPerimeterX" / Double,
        "VirtualPerimeterY" / Double,
        "VirtualPerimeterWidth" / Double,
        "VirtualPerimeterHeight" / Double
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=316, version=2)
class OfficeAirSpace_316_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "MaxViewportDestinationX" / Double,
        "MaxViewportDestinationY" / Double
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=317, version=2)
class OfficeAirSpace_317_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "VirtualZoomedX" / Double,
        "VirtualZoomedY" / Double,
        "RealUnzoomedX" / Double,
        "RealUnzoomedY" / Double,
        "VirtualZoomedX_Rtl" / Double,
        "VirtualZoomedY_Rtl" / Double,
        "RealUnzoomedX_Rtl" / Double,
        "RealUnzoomedY_Rtl" / Double,
        "nextZoom" / Float32l,
        "Width" / Double,
        "Height" / Double
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=318, version=2)
class OfficeAirSpace_318_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=319, version=2)
class OfficeAirSpace_319_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "VirtualZoomedX" / Double,
        "VirtualZoomedY" / Double,
        "RealUnzoomedX" / Double,
        "RealUnzoomedY" / Double,
        "VirtualZoomedX_Rtl" / Double,
        "VirtualZoomedY_Rtl" / Double,
        "RealUnzoomedX_Rtl" / Double,
        "RealUnzoomedY_Rtl" / Double,
        "finalZoom" / Float32l,
        "Width" / Double,
        "Height" / Double
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=320, version=2)
class OfficeAirSpace_320_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "IsIntermediate" / Int8ul,
        "LastSteadyZoom" / Float32l,
        "Zoom" / Float32l,
        "IntermediateCount" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=321, version=2)
class OfficeAirSpace_321_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "VirtualZoomedX" / Double,
        "VirtualZoomedY" / Double,
        "RealUnzoomedX" / Double,
        "RealUnzoomedY" / Double,
        "VirtualZoomedX_Rtl" / Double,
        "VirtualZoomedY_Rtl" / Double,
        "RealUnzoomedX_Rtl" / Double,
        "RealUnzoomedY_Rtl" / Double,
        "currentZoom" / Float32l,
        "VirtualPerimeterX" / Double,
        "VirtualPerimeterY" / Double,
        "VirtualPerimeterWidth" / Double,
        "VirtualPerimeterHeight" / Double
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=322, version=2)
class OfficeAirSpace_322_2(Etw):
    pattern = Struct(
        "ScrollingLayerCanvas" / Int64ul,
        "IsScroll" / Int8ul,
        "IsZoom" / Int8ul,
        "X" / Double,
        "Y" / Double,
        "Zoom" / Float32l
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=323, version=2)
class OfficeAirSpace_323_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "ViewportX" / Double,
        "ViewportY" / Double,
        "ViewportWidth" / Double,
        "ViewportHeight" / Double,
        "Zoom" / Double,
        "IsMoving" / Int8ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=324, version=2)
class OfficeAirSpace_324_2(Etw):
    pattern = Struct(
        "AllAppsBlocked" / Int8ul,
        "BlockedDeviceId" / WString,
        "BlockedDriverVersion" / WString,
        "CrashHistory" / WString,
        "SecsBetweenCrashes" / Double
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=325, version=2)
class OfficeAirSpace_325_2(Etw):
    pattern = Struct(
        "DeviceId" / WString,
        "BlockedDriverVersion" / WString,
        "UpdatedDriverVersion" / WString
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=326, version=2)
class OfficeAirSpace_326_2(Etw):
    pattern = Struct(
        "eventType" / Int32ul,
        "animationProperty" / Int32ul,
        "newValue" / Double
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=327, version=2)
class OfficeAirSpace_327_2(Etw):
    pattern = Struct(
        "animationClass" / CString,
        "animation" / CString,
        "animationInstanceId" / Int32sl,
        "animationEvent" / Int32ul,
        "customEvent" / Int32ul,
        "looping" / Int8ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=328, version=2)
class OfficeAirSpace_328_2(Etw):
    pattern = Struct(
        "animationInstanceId" / Int32sl,
        "animationClass" / CString,
        "animation" / CString
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=329, version=2)
class OfficeAirSpace_329_2(Etw):
    pattern = Struct(
        "animationInstanceId" / Int32sl,
        "animationClass" / CString,
        "animation" / CString
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=330, version=2)
class OfficeAirSpace_330_2(Etw):
    pattern = Struct(
        "animationInstanceId" / Int32sl,
        "animationClass" / CString,
        "animation" / CString
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=331, version=2)
class OfficeAirSpace_331_2(Etw):
    pattern = Struct(
        "animationInstanceHandle" / Int32sl,
        "animationClass" / CString,
        "animation" / CString,
        "seconds" / Double,
        "animationProperty" / Int32ul,
        "value" / Double
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=332, version=2)
class OfficeAirSpace_332_2(Etw):
    pattern = Struct(
        "airSpaceLayerHandle" / Int32sl,
        "classCookie" / Int32sl,
        "animationClassId" / Int32sl
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=333, version=2)
class OfficeAirSpace_333_2(Etw):
    pattern = Struct(
        "airSpaceLayerHandle" / Int32sl,
        "classCookie" / Int32sl,
        "animationClassId" / Int32sl
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=334, version=2)
class OfficeAirSpace_334_2(Etw):
    pattern = Struct(
        "airSpaceLayerHandle" / Int32sl
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=335, version=2)
class OfficeAirSpace_335_2(Etw):
    pattern = Struct(
        "animationInstanceHandle" / Int32sl,
        "contextVariableId" / Int32ul,
        "contextableValue" / Double
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=336, version=2)
class OfficeAirSpace_336_2(Etw):
    pattern = Struct(
        "AppCrashingInHw" / WString
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=337, version=2)
class OfficeAirSpace_337_2(Etw):
    pattern = Struct(
        "SafeMode" / Int8ul,
        "TerminalServer" / Int8ul,
        "Registry" / Int8ul,
        "AdminPolicy" / Int8ul,
        "AnimationDisabled" / Int8ul,
        "EaseOfAccess" / Int8ul,
        "WARP" / Int8ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=338, version=2)
class OfficeAirSpace_338_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "OldZoomFactor" / Float32l,
        "NewZoomFactor" / Float32l
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=339, version=2)
class OfficeAirSpace_339_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "OldZoomFactor" / Float32l,
        "NewZoomFactor" / Float32l
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=340, version=2)
class OfficeAirSpace_340_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "oldVirtualPerimeterX" / Double,
        "oldVirtualPerimeterY" / Double,
        "oldVirtualPerimeterWidth" / Double,
        "oldVirtualPerimeterHeight" / Double,
        "newVirtualPerimeterX" / Double,
        "newVirtualPerimeterY" / Double,
        "newVirtualPerimeterWidth" / Double,
        "newVirtualPerimeterHeight" / Double
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=341, version=2)
class OfficeAirSpace_341_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "VirtualZoomedX" / Double,
        "VirtualZoomedY" / Double,
        "RealUnzoomedX" / Double,
        "RealUnzoomedY" / Double,
        "VirtualZoomedX_Rtl" / Double,
        "VirtualZoomedY_Rtl" / Double,
        "RealUnzoomedX_Rtl" / Double,
        "RealUnzoomedY_Rtl" / Double,
        "finalZoom" / Float32l,
        "IsPendingScroll" / Int8ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=342, version=2)
class OfficeAirSpace_342_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=343, version=2)
class OfficeAirSpace_343_2(Etw):
    pattern = Struct(
        "value1" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=345, version=2)
class OfficeAirSpace_345_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=346, version=2)
class OfficeAirSpace_346_2(Etw):
    pattern = Struct(
        "LayerTileManager" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=348, version=2)
class OfficeAirSpace_348_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=350, version=2)
class OfficeAirSpace_350_2(Etw):
    pattern = Struct(
        "LCLVT" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=352, version=2)
class OfficeAirSpace_352_2(Etw):
    pattern = Struct(
        "LayerTexture" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=355, version=2)
class OfficeAirSpace_355_2(Etw):
    pattern = Struct(
        "LCLVT" / Int64ul,
        "LTM" / Int64ul,
        "LayerHandle" / Int32ul,
        "TextureHandle" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=356, version=2)
class OfficeAirSpace_356_2(Etw):
    pattern = Struct(
        "LCLVT" / Int64ul,
        "ContentZoom" / Float32l,
        "HighDpiScaleFactor" / Float32l,
        "BoundsLeft" / Int32ul,
        "BoundsTop" / Int32ul,
        "BoundsWidth" / Int32ul,
        "BoundsHeight" / Int32ul,
        "PrefetchDistanceX" / Int32ul,
        "PrefetchDistanceY" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=359, version=2)
class OfficeAirSpace_359_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=362, version=2)
class OfficeAirSpace_362_2(Etw):
    pattern = Struct(
        "LCLVT" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=365, version=2)
class OfficeAirSpace_365_2(Etw):
    pattern = Struct(
        "LayerTexture" / Int64ul,
        "Surface" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=366, version=2)
class OfficeAirSpace_366_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "Width" / Int32ul,
        "Height" / Int32ul,
        "Playback" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=371, version=2)
class OfficeAirSpace_371_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "OldStretchMode" / Int32ul,
        "NewStretchMode" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=375, version=2)
class OfficeAirSpace_375_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "Width" / Int32ul,
        "Height" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=377, version=2)
class OfficeAirSpace_377_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "OldWidth" / Int32ul,
        "OldHeight" / Int32ul,
        "NewWidth" / Int32ul,
        "NewHeight" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=379, version=2)
class OfficeAirSpace_379_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "Width" / Int32ul,
        "Height" / Int32ul,
        "IsArc" / Int8ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=381, version=2)
class OfficeAirSpace_381_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=382, version=2)
class OfficeAirSpace_382_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "ScrollingIndicatorMode" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=384, version=2)
class OfficeAirSpace_384_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "X" / Int32ul,
        "Y" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=385, version=2)
class OfficeAirSpace_385_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=386, version=2)
class OfficeAirSpace_386_2(Etw):
    pattern = Struct(
        "LayerVirtualTexture" / Int64ul,
        "LTM" / Int64ul,
        "LayerHandle" / Int32ul,
        "TextureHandle" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=390, version=2)
class OfficeAirSpace_390_2(Etw):
    pattern = Struct(
        "LayerTexture" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=394, version=2)
class OfficeAirSpace_394_2(Etw):
    pattern = Struct(
        "LayerTexture" / Int64ul,
        "StretchMode" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=397, version=2)
class OfficeAirSpace_397_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=398, version=2)
class OfficeAirSpace_398_2(Etw):
    pattern = Struct(
        "LayerVirtualTexture" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=399, version=2)
class OfficeAirSpace_399_2(Etw):
    pattern = Struct(
        "LCLVT" / Int64ul,
        "ContentZoom" / Float32l,
        "HighDpiScaleFactor" / Float32l,
        "BoundsLeft" / Int32ul,
        "BoundsTop" / Int32ul,
        "BoundsWidth" / Int32ul,
        "BoundsHeight" / Int32ul,
        "PrefetchDistanceX" / Int32ul,
        "PrefetchDistanceY" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=400, version=2)
class OfficeAirSpace_400_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=401, version=2)
class OfficeAirSpace_401_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=402, version=2)
class OfficeAirSpace_402_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=404, version=2)
class OfficeAirSpace_404_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=405, version=2)
class OfficeAirSpace_405_2(Etw):
    pattern = Struct(
        "LayerTexture" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=407, version=2)
class OfficeAirSpace_407_2(Etw):
    pattern = Struct(
        "LayerTexture" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=409, version=2)
class OfficeAirSpace_409_2(Etw):
    pattern = Struct(
        "LayerTexture" / Int64ul,
        "LayerHandle" / Int32ul,
        "TextureHandle" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=410, version=2)
class OfficeAirSpace_410_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=411, version=2)
class OfficeAirSpace_411_2(Etw):
    pattern = Struct(
        "LayerTileManager" / Int64ul,
        "BoundsLeft" / Int32ul,
        "BoundsTop" / Int32ul,
        "BoundsWidth" / Int32ul,
        "BoundsHeight" / Int32ul,
        "PrefetchDistanceX" / Int32ul,
        "PrefetchDistanceY" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=412, version=2)
class OfficeAirSpace_412_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "X" / Int32ul,
        "Y" / Int32ul,
        "Width" / Int32ul,
        "Height" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=413, version=2)
class OfficeAirSpace_413_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "RectX" / Int32ul,
        "RectY" / Int32ul,
        "RectWidth" / Int32ul,
        "RectHeight" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=414, version=2)
class OfficeAirSpace_414_2(Etw):
    pattern = Struct(
        "LayerTexture" / Int64ul,
        "LayerHandle" / Int32ul,
        "TextureHandle" / Int32ul,
        "Surface" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=415, version=2)
class OfficeAirSpace_415_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=416, version=2)
class OfficeAirSpace_416_2(Etw):
    pattern = Struct(
        "WindowCompositor" / Int64ul,
        "WindowCompositionGraphicsDevice" / Int64ul,
        "DxgiDevice" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=418, version=2)
class OfficeAirSpace_418_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=419, version=2)
class OfficeAirSpace_419_2(Etw):
    pattern = Struct(
        "WindowCompositor" / Int64ul,
        "Compositor" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=420, version=2)
class OfficeAirSpace_420_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=422, version=2)
class OfficeAirSpace_422_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=425, version=2)
class OfficeAirSpace_425_2(Etw):
    pattern = Struct(
        "WindowCompositor" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=426, version=2)
class OfficeAirSpace_426_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=427, version=2)
class OfficeAirSpace_427_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "StretchMode" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=432, version=2)
class OfficeAirSpace_432_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "Width" / Int32ul,
        "Height" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=433, version=2)
class OfficeAirSpace_433_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=434, version=2)
class OfficeAirSpace_434_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=436, version=2)
class OfficeAirSpace_436_2(Etw):
    pattern = Struct(
        "LayerTexture" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=437, version=2)
class OfficeAirSpace_437_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=440, version=2)
class OfficeAirSpace_440_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "Width" / Int32ul,
        "Height" / Int32ul,
        "IgnoreAlpha" / Int8ul,
        "IsCommandListBacked" / Int8ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=441, version=2)
class OfficeAirSpace_441_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "Width" / Int32ul,
        "Height" / Int32ul,
        "Opaque" / Int8ul,
        "Depth" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=443, version=2)
class OfficeAirSpace_443_2(Etw):
    pattern = Struct(
        "WindowCompositor" / Int64ul,
        "DxgiDevice" / Int64ul,
        "WindowCompositionGraphicsDevice" / Int64ul,
        "GraphicsDevice" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=444, version=2)
class OfficeAirSpace_444_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=445, version=2)
class OfficeAirSpace_445_2(Etw):
    pattern = Struct(
        "WindowCompositionGraphicsDevice" / Int64ul,
        "GraphicsDevice" / Int64ul,
        "DxgiDevice" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=448, version=2)
class OfficeAirSpace_448_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=456, version=2)
class OfficeAirSpace_456_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=457, version=2)
class OfficeAirSpace_457_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=458, version=2)
class OfficeAirSpace_458_2(Etw):
    pattern = Struct(
        "LayerTexture" / Int64ul,
        "Surface" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=459, version=2)
class OfficeAirSpace_459_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "OldWidth" / Int32ul,
        "OldHeight" / Int32ul,
        "NewWidth" / Int32ul,
        "NewHeight" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=460, version=2)
class OfficeAirSpace_460_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=461, version=2)
class OfficeAirSpace_461_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=464, version=2)
class OfficeAirSpace_464_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=466, version=2)
class OfficeAirSpace_466_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=469, version=2)
class OfficeAirSpace_469_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=470, version=2)
class OfficeAirSpace_470_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=472, version=2)
class OfficeAirSpace_472_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=473, version=2)
class OfficeAirSpace_473_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "NullRenderTargetReason" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=474, version=2)
class OfficeAirSpace_474_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "Width" / Int32ul,
        "Height" / Int32ul,
        "Depth" / Int32ul,
        "Opaque" / Int8ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=475, version=2)
class OfficeAirSpace_475_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "isMouseWheelSupportEnabled" / Int8ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=476, version=2)
class OfficeAirSpace_476_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=477, version=2)
class OfficeAirSpace_477_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "BorderPosition" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=478, version=2)
class OfficeAirSpace_478_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=479, version=2)
class OfficeAirSpace_479_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=480, version=2)
class OfficeAirSpace_480_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "Type" / Int32ul,
        "isHorizontal" / Int8ul,
        "Distance" / Float32l,
        "Offset" / Float32l
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=481, version=2)
class OfficeAirSpace_481_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "Type" / Int32ul,
        "isHorizontal" / Int8ul,
        "isZoom" / Int8ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=482, version=2)
class OfficeAirSpace_482_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "Type" / Int32ul,
        "isHorizontal" / Int8ul,
        "Size" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=483, version=2)
class OfficeAirSpace_483_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "zoomFactor" / Float32l
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=484, version=2)
class OfficeAirSpace_484_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=485, version=2)
class OfficeAirSpace_485_2(Etw):
    pattern = Struct(
        "HResult" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=486, version=2)
class OfficeAirSpace_486_2(Etw):
    pattern = Struct(
        "WinCompEnabled" / Int8ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=487, version=2)
class OfficeAirSpace_487_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "Type" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=488, version=2)
class OfficeAirSpace_488_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "HResult" / Int32ul,
        "Type" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=489, version=2)
class OfficeAirSpace_489_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "Type" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=490, version=2)
class OfficeAirSpace_490_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "Type" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=491, version=2)
class OfficeAirSpace_491_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "Type" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=492, version=2)
class OfficeAirSpace_492_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=493, version=2)
class OfficeAirSpace_493_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=494, version=2)
class OfficeAirSpace_494_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "X" / Int32ul,
        "Y" / Int32ul,
        "Width" / Int32ul,
        "Height" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=495, version=2)
class OfficeAirSpace_495_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "OldWidth" / Int32ul,
        "OldHeight" / Int32ul,
        "NewWidth" / Int32ul,
        "NewHeight" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=496, version=2)
class OfficeAirSpace_496_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "X" / Int32ul,
        "Y" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=497, version=2)
class OfficeAirSpace_497_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "isXChainingSupportEnabled" / Int8ul,
        "isYChainingSupportEnabled" / Int8ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=498, version=2)
class OfficeAirSpace_498_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=499, version=2)
class OfficeAirSpace_499_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=500, version=2)
class OfficeAirSpace_500_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "IsViewportMoving" / Int8ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=501, version=2)
class OfficeAirSpace_501_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "VirtualZoomedX" / Double,
        "VirtualZoomedY" / Double,
        "RealUnzoomedX" / Double,
        "RealUnzoomedY" / Double,
        "VirtualZoomedX_Rtl" / Double,
        "VirtualZoomedY_Rtl" / Double,
        "RealUnzoomedX_Rtl" / Double,
        "RealUnzoomedY_Rtl" / Double,
        "finalZoom" / Float32l,
        "Width" / Double,
        "Height" / Double,
        "IsViewportMoving" / Int8ul,
        "IsClientScroll" / Int8ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=502, version=2)
class OfficeAirSpace_502_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=503, version=2)
class OfficeAirSpace_503_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=504, version=2)
class OfficeAirSpace_504_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "VirtualZoomedX" / Double,
        "VirtualZoomedY" / Double,
        "RealUnzoomedX" / Double,
        "RealUnzoomedY" / Double,
        "VirtualZoomedX_Rtl" / Double,
        "VirtualZoomedY_Rtl" / Double,
        "RealUnzoomedX_Rtl" / Double,
        "RealUnzoomedY_Rtl" / Double,
        "finalZoom" / Float32l,
        "VirtualPerimeterX" / Double,
        "VirtualPerimeterY" / Double,
        "VirtualPerimeterWidth" / Double,
        "VirtualPerimeterHeight" / Double
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=505, version=2)
class OfficeAirSpace_505_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=506, version=2)
class OfficeAirSpace_506_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=507, version=2)
class OfficeAirSpace_507_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "VirtualZoomedX" / Double,
        "VirtualZoomedY" / Double,
        "RealUnzoomedX" / Double,
        "RealUnzoomedY" / Double,
        "VirtualZoomedX_Rtl" / Double,
        "VirtualZoomedY_Rtl" / Double,
        "RealUnzoomedX_Rtl" / Double,
        "RealUnzoomedY_Rtl" / Double,
        "currentZoom" / Float32l,
        "Width" / Double,
        "Height" / Double,
        "IsViewportMoving" / Int8ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=508, version=2)
class OfficeAirSpace_508_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=509, version=2)
class OfficeAirSpace_509_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "IsViewportMoving" / Int8ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=510, version=2)
class OfficeAirSpace_510_2(Etw):
    pattern = Struct(
        "ObjectHandle" / Int32ul,
        "MinPositionX" / Double,
        "MinPositionY" / Double,
        "MaxPositionX" / Double,
        "MaxPositionY" / Double,
        "MinMaxOrder" / Int8ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=511, version=2)
class OfficeAirSpace_511_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "RectX" / Int32ul,
        "RectY" / Int32ul,
        "RectWidth" / Int32ul,
        "RectHeight" / Int32ul,
        "Width" / Int32ul,
        "Height" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=512, version=2)
class OfficeAirSpace_512_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "NullRenderTargetReason" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=513, version=2)
class OfficeAirSpace_513_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "NullRenderTargetReason" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=514, version=2)
class OfficeAirSpace_514_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "NullRenderTargetReason" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=515, version=2)
class OfficeAirSpace_515_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "NullRenderTargetReason" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=516, version=2)
class OfficeAirSpace_516_2(Etw):
    pattern = Struct(
        "animationProperty" / Int32ul,
        "value" / Double,
        "hasAnimation" / Int8ul,
        "animating" / Int8ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=517, version=2)
class OfficeAirSpace_517_2(Etw):
    pattern = Struct(
        "animationTracker" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=518, version=2)
class OfficeAirSpace_518_2(Etw):
    pattern = Struct(
        "animationTracker" / Int64ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=519, version=2)
class OfficeAirSpace_519_2(Etw):
    pattern = Struct(
        "animationTracker" / Int64ul,
        "handle" / Int32ul,
        "duration" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=520, version=2)
class OfficeAirSpace_520_2(Etw):
    pattern = Struct(
        "HResult" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=521, version=2)
class OfficeAirSpace_521_2(Etw):
    pattern = Struct(
        "HResult" / Int32ul,
        "IsActivating" / Int8ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=522, version=2)
class OfficeAirSpace_522_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "RequestId" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=523, version=2)
class OfficeAirSpace_523_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "virtualPerimeterX" / Double,
        "virtualPerimeterY" / Double,
        "virtualPerimeterWidth" / Double,
        "virtualPerimeterHeight" / Double,
        "CalculatedvirtualPerimeterX" / Double,
        "CalculatedvirtualPerimeterY" / Double,
        "CalculatedvirtualPerimeterWidth" / Double,
        "CalculatedvirtualPerimeterHeight" / Double
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=524, version=2)
class OfficeAirSpace_524_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "virtualPerimeterX" / Double,
        "virtualPerimeterY" / Double,
        "virtualPerimeterWidth" / Double,
        "virtualPerimeterHeight" / Double,
        "CalculatedvirtualPerimeterX" / Double,
        "CalculatedvirtualPerimeterY" / Double,
        "CalculatedvirtualPerimeterWidth" / Double,
        "CalculatedvirtualPerimeterHeight" / Double
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=526, version=2)
class OfficeAirSpace_526_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "RequestId" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=528, version=2)
class OfficeAirSpace_528_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "ZoomCenterPointX" / Float32l,
        "ZoomCenterPointY" / Float32l,
        "RequestId" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=529, version=2)
class OfficeAirSpace_529_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "RequestId" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=531, version=2)
class OfficeAirSpace_531_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "ZoomCenterPointX" / Float32l,
        "ZoomCenterPointY" / Float32l,
        "RequestId" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=533, version=2)
class OfficeAirSpace_533_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "canvasSizeX" / Float32l,
        "canvasSizeY" / Float32l
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=534, version=2)
class OfficeAirSpace_534_2(Etw):
    pattern = Struct(
        "Width" / Int32ul,
        "Height" / Int32ul,
        "MaxTextureDimension" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=535, version=2)
class OfficeAirSpace_535_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "Width" / Int32ul,
        "Height" / Int32ul,
        "MaxTextureDimension" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=536, version=2)
class OfficeAirSpace_536_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "NullRenderTargetReason" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=537, version=2)
class OfficeAirSpace_537_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "VirtualZoomedX" / Double,
        "VirtualZoomedY" / Double,
        "finalZoom" / Float32l
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=538, version=2)
class OfficeAirSpace_538_2(Etw):
    pattern = Struct(
        "SurfaceWidth" / Int32ul,
        "SurfaceHeight" / Int32ul,
        "UpdateWidth" / Int32ul,
        "UpdateHeight" / Int32ul,
        "TextureHandle" / Int64sl
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=539, version=2)
class OfficeAirSpace_539_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "StretchMode" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=540, version=2)
class OfficeAirSpace_540_2(Etw):
    pattern = Struct(
        "Handle" / Int32ul,
        "hasCalledBeginDraw" / Int8ul,
        "IsDrawing" / Int8ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=541, version=2)
class OfficeAirSpace_541_2(Etw):
    pattern = Struct(
        "Command" / WString,
        "BatchDesc" / WString,
        "V1Name" / WString,
        "V1Val" / WString,
        "V2Name" / WString,
        "V2Val" / WString,
        "V3Name" / WString,
        "V3Val" / WString,
        "V4Name" / WString,
        "V4Val" / WString,
        "V5Name" / WString,
        "V5Val" / WString,
        "V6Name" / WString,
        "V6Val" / WString,
        "V7Name" / WString,
        "V7Val" / WString
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=542, version=2)
class OfficeAirSpace_542_2(Etw):
    pattern = Struct(
        "LayerHandle" / Int32ul,
        "TextureHandle" / Int32ul,
        "IncomingVirtualTextureAction" / Int32ul
    )


@declare(guid=guid("f562bb8e-422d-4b5c-b20e-90d710f7d11c"), event_id=543, version=2)
class OfficeAirSpace_543_2(Etw):
    pattern = Struct(
        "Command" / WString,
        "BatchDesc" / WString,
        "V1Name" / WString,
        "V1Val" / WString,
        "V2Name" / WString,
        "V2Val" / WString,
        "V3Name" / WString,
        "V3Val" / WString,
        "V4Name" / WString,
        "V4Val" / WString,
        "V5Name" / WString,
        "V5Val" / WString,
        "V6Name" / WString,
        "V6Val" / WString,
        "V7Name" / WString,
        "V7Val" / WString
    )

