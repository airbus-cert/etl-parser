# -*- coding: utf-8 -*-
"""
Microsoft-Windows-XAML
GUID : 531a35ab-63ce-4bcf-aa98-f88c7a89e455
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=1, version=0)
class Microsoft_Windows_XAML_1_0(Etw):
    pattern = Struct(
        "URI" / WString
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=2, version=0)
class Microsoft_Windows_XAML_2_0(Etw):
    pattern = Struct(
        "URI" / WString
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=4, version=0)
class Microsoft_Windows_XAML_4_0(Etw):
    pattern = Struct(
        "ClassName" / WString
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=5, version=0)
class Microsoft_Windows_XAML_5_0(Etw):
    pattern = Struct(
        "ElementId" / Int64ul,
        "ClassName" / WString
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=15, version=0)
class Microsoft_Windows_XAML_15_0(Etw):
    pattern = Struct(
        "CallbackName" / WString
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=20, version=0)
class Microsoft_Windows_XAML_20_0(Etw):
    pattern = Struct(
        "ComponentName" / WString
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=26, version=0)
class Microsoft_Windows_XAML_26_0(Etw):
    pattern = Struct(
        "IsHighPriority" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=38, version=0)
class Microsoft_Windows_XAML_38_0(Etw):
    pattern = Struct(
        "GraphicsDriverSupportType" / WString
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=39, version=0)
class Microsoft_Windows_XAML_39_0(Etw):
    pattern = Struct(
        "MediaElementID" / Int64ul,
        "InFullScreen" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=40, version=0)
class Microsoft_Windows_XAML_40_0(Etw):
    pattern = Struct(
        "MediaElementID" / Int64ul,
        "HasOverlap" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=47, version=0)
class Microsoft_Windows_XAML_47_0(Etw):
    pattern = Struct(
        "ElementId" / Int64ul,
        "Width" / Float32l,
        "Height" / Float32l
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=48, version=0)
class Microsoft_Windows_XAML_48_0(Etw):
    pattern = Struct(
        "ElementId" / Int64ul,
        "DesiredWidth" / Float32l,
        "DesiredHeight" / Float32l
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=49, version=0)
class Microsoft_Windows_XAML_49_0(Etw):
    pattern = Struct(
        "ElementId" / Int64ul,
        "Left" / Float32l,
        "Top" / Float32l,
        "Width" / Float32l,
        "Height" / Float32l
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=50, version=0)
class Microsoft_Windows_XAML_50_0(Etw):
    pattern = Struct(
        "ElementId" / Int64ul,
        "VisualOffsetX" / Float32l,
        "VisualOffsetY" / Float32l,
        "RenderWidth" / Float32l,
        "RenderHeight" / Float32l
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=61, version=0)
class Microsoft_Windows_XAML_61_0(Etw):
    pattern = Struct(
        "ElementId" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=62, version=0)
class Microsoft_Windows_XAML_62_0(Etw):
    pattern = Struct(
        "ElementId" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=64, version=0)
class Microsoft_Windows_XAML_64_0(Etw):
    pattern = Struct(
        "X" / Int32ul,
        "Y" / Int32ul,
        "Width" / Int32ul,
        "Height" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=84, version=0)
class Microsoft_Windows_XAML_84_0(Etw):
    pattern = Struct(
        "ElementId" / Int64ul,
        "TargetElementId" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=85, version=0)
class Microsoft_Windows_XAML_85_0(Etw):
    pattern = Struct(
        "ElementId" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=86, version=0)
class Microsoft_Windows_XAML_86_0(Etw):
    pattern = Struct(
        "ElementId" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=87, version=0)
class Microsoft_Windows_XAML_87_0(Etw):
    pattern = Struct(
        "ElementId" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=88, version=0)
class Microsoft_Windows_XAML_88_0(Etw):
    pattern = Struct(
        "ElementId" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=89, version=0)
class Microsoft_Windows_XAML_89_0(Etw):
    pattern = Struct(
        "ElementId" / Int64ul,
        "PropertyName" / WString
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=90, version=0)
class Microsoft_Windows_XAML_90_0(Etw):
    pattern = Struct(
        "CacheId" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=91, version=0)
class Microsoft_Windows_XAML_91_0(Etw):
    pattern = Struct(
        "CacheId" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=92, version=0)
class Microsoft_Windows_XAML_92_0(Etw):
    pattern = Struct(
        "CacheId" / Int64ul,
        "X" / Int32ul,
        "Y" / Int32ul,
        "UpdateWidth" / Int32ul,
        "UpdateHeight" / Int32ul,
        "SurfaceWidth" / Int32ul,
        "SurfaceHeight" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=94, version=1)
class Microsoft_Windows_XAML_94_1(Etw):
    pattern = Struct(
        "Visited" / Int32sl,
        "Rendered" / Int32sl
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=95, version=0)
class Microsoft_Windows_XAML_95_0(Etw):
    pattern = Struct(
        "ElementName" / WString
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=101, version=0)
class Microsoft_Windows_XAML_101_0(Etw):
    pattern = Struct(
        "FrameId" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=105, version=0)
class Microsoft_Windows_XAML_105_0(Etw):
    pattern = Struct(
        "FrameCount" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=109, version=0)
class Microsoft_Windows_XAML_109_0(Etw):
    pattern = Struct(
        "BatchCount" / Int32ul,
        "PrimitivesDrawn" / Int32ul,
        "GeometryGeneratedPrimitivesDrawn" / Int32ul,
        "GeometryGeneratedVerticesDrawn" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=113, version=0)
class Microsoft_Windows_XAML_113_0(Etw):
    pattern = Struct(
        "FrameId" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=134, version=0)
class Microsoft_Windows_XAML_134_0(Etw):
    pattern = Struct(
        "Transparent" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=135, version=0)
class Microsoft_Windows_XAML_135_0(Etw):
    pattern = Struct(
        "Transparent" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=136, version=0)
class Microsoft_Windows_XAML_136_0(Etw):
    pattern = Struct(
        "Transparent" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=137, version=0)
class Microsoft_Windows_XAML_137_0(Etw):
    pattern = Struct(
        "Transparent" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=138, version=0)
class Microsoft_Windows_XAML_138_0(Etw):
    pattern = Struct(
        "Id" / Int64ul,
        "Width" / Int32ul,
        "Height" / Int32ul,
        "BitDepth" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=139, version=0)
class Microsoft_Windows_XAML_139_0(Etw):
    pattern = Struct(
        "Id" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=140, version=0)
class Microsoft_Windows_XAML_140_0(Etw):
    pattern = Struct(
        "AtlasId" / Int64ul,
        "X" / Int32ul,
        "Y" / Int32ul,
        "Width" / Int32ul,
        "Height" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=141, version=0)
class Microsoft_Windows_XAML_141_0(Etw):
    pattern = Struct(
        "AtlasId" / Int64ul,
        "X" / Int32ul,
        "Y" / Int32ul,
        "Width" / Int32ul,
        "Height" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=142, version=0)
class Microsoft_Windows_XAML_142_0(Etw):
    pattern = Struct(
        "Id" / Int64ul,
        "Width" / Int32ul,
        "Height" / Int32ul,
        "BitDepth" / Int32ul,
        "PercentUsed" / Float32l
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=143, version=0)
class Microsoft_Windows_XAML_143_0(Etw):
    pattern = Struct(
        "URI" / WString
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=144, version=0)
class Microsoft_Windows_XAML_144_0(Etw):
    pattern = Struct(
        "URI" / WString
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=145, version=0)
class Microsoft_Windows_XAML_145_0(Etw):
    pattern = Struct(
        "URI" / WString
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=146, version=0)
class Microsoft_Windows_XAML_146_0(Etw):
    pattern = Struct(
        "URI" / WString
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=165, version=0)
class Microsoft_Windows_XAML_165_0(Etw):
    pattern = Struct(
        "PointerId" / Int32ul,
        "MsgId" / Int32ul,
        "X" / Float32l,
        "Y" / Float32l
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=167, version=0)
class Microsoft_Windows_XAML_167_0(Etw):
    pattern = Struct(
        "ViewportId" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=168, version=0)
class Microsoft_Windows_XAML_168_0(Etw):
    pattern = Struct(
        "ViewportId" / Int64ul,
        "OldStatus" / Int32ul,
        "NewStatus" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=169, version=0)
class Microsoft_Windows_XAML_169_0(Etw):
    pattern = Struct(
        "ViewportId" / Int64ul,
        "OldStatus" / Int32ul,
        "NewStatus" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=170, version=0)
class Microsoft_Windows_XAML_170_0(Etw):
    pattern = Struct(
        "ViewportId" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=171, version=0)
class Microsoft_Windows_XAML_171_0(Etw):
    pattern = Struct(
        "ViewportId" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=172, version=0)
class Microsoft_Windows_XAML_172_0(Etw):
    pattern = Struct(
        "ViewportId" / Int64ul,
        "TranslationX" / Float32l,
        "TranslationY" / Float32l,
        "ZoomFactor" / Float32l,
        "ZoomFactorX" / Float32l,
        "ZoomFactorY" / Float32l
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=173, version=0)
class Microsoft_Windows_XAML_173_0(Etw):
    pattern = Struct(
        "ViewportId" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=174, version=0)
class Microsoft_Windows_XAML_174_0(Etw):
    pattern = Struct(
        "ViewportId" / Int64ul,
        "TranslationX" / Float32l,
        "TranslationY" / Float32l,
        "ZoomFactor" / Float32l,
        "ZoomFactorX" / Float32l,
        "ZoomFactorY" / Float32l
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=175, version=0)
class Microsoft_Windows_XAML_175_0(Etw):
    pattern = Struct(
        "ViewportId" / Int64ul,
        "CompositorViewportId" / Int64ul,
        "ContainerId" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=176, version=0)
class Microsoft_Windows_XAML_176_0(Etw):
    pattern = Struct(
        "ViewportId" / Int64ul,
        "CompositorViewportId" / Int64ul,
        "ContainerId" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=188, version=0)
class Microsoft_Windows_XAML_188_0(Etw):
    pattern = Struct(
        "X" / Float32l,
        "Y" / Float32l,
        "Width" / Float32l,
        "Height" / Float32l
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=195, version=0)
class Microsoft_Windows_XAML_195_0(Etw):
    pattern = Struct(
        "PointerId" / Int32ul,
        "MsgId" / Int32ul,
        "X" / Float32l,
        "Y" / Float32l
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=213, version=0)
class Microsoft_Windows_XAML_213_0(Etw):
    pattern = Struct(
        "ElementId" / Int64ul,
        "Name" / WString
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=218, version=0)
class Microsoft_Windows_XAML_218_0(Etw):
    pattern = Struct(
        "ControllerId" / Int64ul,
        "PresentId" / Int32ul,
        "VBlankId" / Int32ul,
        "SyncRefreshCount" / Int32ul,
        "SyncQPCTime" / Int64ul,
        "QueuedPresentCount" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=219, version=0)
class Microsoft_Windows_XAML_219_0(Etw):
    pattern = Struct(
        "ControllerId" / Int64ul,
        "PresentId" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=220, version=0)
class Microsoft_Windows_XAML_220_0(Etw):
    pattern = Struct(
        "ControllerId" / Int64ul,
        "PresentId" / Int32ul,
        "StartQPCTicks" / Int64ul,
        "EndQPCTicks" / Int64ul,
        "LatencyInQPCTicks" / Int64ul,
        "QPCTicksPerVBlank" / Float32l,
        "LatencyInVBlanks" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=221, version=0)
class Microsoft_Windows_XAML_221_0(Etw):
    pattern = Struct(
        "ControllerId" / Int64ul,
        "PresentId" / Int32ul,
        "BeginPresentQPCTicks" / Int64ul,
        "QueuedPresentCount" / Int32ul,
        "FramesToQueue" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=222, version=0)
class Microsoft_Windows_XAML_222_0(Etw):
    pattern = Struct(
        "ControllerId" / Int64ul,
        "ShouldPresent" / Int32ul,
        "VBlanksToSkip" / Int32ul,
        "FramesToQueue" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=223, version=0)
class Microsoft_Windows_XAML_223_0(Etw):
    pattern = Struct(
        "ControllerId" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=224, version=0)
class Microsoft_Windows_XAML_224_0(Etw):
    pattern = Struct(
        "ControllerId" / Int64ul,
        "LatencyInVBlanks" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=225, version=0)
class Microsoft_Windows_XAML_225_0(Etw):
    pattern = Struct(
        "ControllerId" / Int64ul,
        "NewState" / Int32sl,
        "VBlanksToDrop" / Int32ul,
        "FramesToQueue" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=226, version=0)
class Microsoft_Windows_XAML_226_0(Etw):
    pattern = Struct(
        "ControllerId" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=227, version=0)
class Microsoft_Windows_XAML_227_0(Etw):
    pattern = Struct(
        "ControllerId" / Int64ul,
        "PresentId" / Int32ul,
        "PresentQPCTicks" / Int64ul,
        "PostPresentQPCTicks" / Int64ul,
        "PresentTimeInQPCTicks" / Int64ul,
        "QPCTicksPerVBlank" / Float32l,
        "PresentTimeInVBlanks" / Float32l
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=228, version=0)
class Microsoft_Windows_XAML_228_0(Etw):
    pattern = Struct(
        "ControllerId" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=229, version=0)
class Microsoft_Windows_XAML_229_0(Etw):
    pattern = Struct(
        "ControllerId" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=230, version=0)
class Microsoft_Windows_XAML_230_0(Etw):
    pattern = Struct(
        "Id" / Int64ul,
        "Width" / Int32ul,
        "Height" / Int32ul,
        "AlphaMode" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=231, version=0)
class Microsoft_Windows_XAML_231_0(Etw):
    pattern = Struct(
        "Id" / Int64ul,
        "Width" / Int32ul,
        "Height" / Int32ul,
        "AlphaMode" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=232, version=0)
class Microsoft_Windows_XAML_232_0(Etw):
    pattern = Struct(
        "Id" / Int64ul,
        "Width" / Int32ul,
        "Height" / Int32ul,
        "AlphaMode" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=233, version=0)
class Microsoft_Windows_XAML_233_0(Etw):
    pattern = Struct(
        "Id" / Int64ul,
        "Width" / Int32ul,
        "Height" / Int32ul,
        "AlphaMode" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=234, version=0)
class Microsoft_Windows_XAML_234_0(Etw):
    pattern = Struct(
        "SurfaceId" / Int64ul,
        "Width" / Int32ul,
        "Height" / Int32ul,
        "PixelSize" / Int32ul,
        "IsDriverVisible" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=235, version=0)
class Microsoft_Windows_XAML_235_0(Etw):
    pattern = Struct(
        "SurfaceId" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=236, version=0)
class Microsoft_Windows_XAML_236_0(Etw):
    pattern = Struct(
        "ControllerId" / Int64ul,
        "QPCTicks" / Int64ul,
        "VBlank0InQPCTicks" / Int64ul,
        "QPCTicksPerVBlank" / Float32l,
        "VBlankCount" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=237, version=0)
class Microsoft_Windows_XAML_237_0(Etw):
    pattern = Struct(
        "ControllerId" / Int64ul,
        "QPCTicks" / Int64ul,
        "PreviousRefreshVBlankCount" / Int32ul,
        "PreviousRefreshQPCTicks" / Int64ul,
        "QPCTicksPerVBlank" / Float32l,
        "VBlankOffset" / Int32ul,
        "VBlankCount" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=238, version=0)
class Microsoft_Windows_XAML_238_0(Etw):
    pattern = Struct(
        "Vsis" / Int64ul,
        "VisibleLeft" / Int32sl,
        "VisibleTop" / Int32sl,
        "VisibleRight" / Int32sl,
        "VisibleBottom" / Int32sl,
        "DesiredLeft" / Int32sl,
        "DesiredTop" / Int32sl,
        "DesiredRight" / Int32sl,
        "DesiredBottom" / Int32sl,
        "HighPriorityDesiredLeft" / Int32sl,
        "HighPriorityDesiredTop" / Int32sl,
        "HighPriorityDesiredRight" / Int32sl,
        "HighPriorityDesiredBottom" / Int32sl,
        "MotionFlags" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=239, version=0)
class Microsoft_Windows_XAML_239_0(Etw):
    pattern = Struct(
        "SurfaceImageSource" / Int64ul,
        "Left" / Int32sl,
        "Top" / Int32sl,
        "Right" / Int32sl,
        "Bottom" / Int32sl
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=240, version=0)
class Microsoft_Windows_XAML_240_0(Etw):
    pattern = Struct(
        "SurfaceImageSource" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=241, version=0)
class Microsoft_Windows_XAML_241_0(Etw):
    pattern = Struct(
        "CommandId" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=242, version=0)
class Microsoft_Windows_XAML_242_0(Etw):
    pattern = Struct(
        "CommandBatchId" / Int32ul,
        "CommandId" / Int32ul,
        "CommandVBlankNumber" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=243, version=0)
class Microsoft_Windows_XAML_243_0(Etw):
    pattern = Struct(
        "TimeToNextWorkInMilliseconds" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=244, version=0)
class Microsoft_Windows_XAML_244_0(Etw):
    pattern = Struct(
        "VisualId" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=244, version=1)
class Microsoft_Windows_XAML_244_1(Etw):
    pattern = Struct(
        "CompNode" / Int64ul,
        "VisualIndex" / Int32ul,
        "Visual" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=245, version=0)
class Microsoft_Windows_XAML_245_0(Etw):
    pattern = Struct(
        "VisualId" / Int64ul,
        "ZOrder" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=246, version=0)
class Microsoft_Windows_XAML_246_0(Etw):
    pattern = Struct(
        "VisualId" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=247, version=0)
class Microsoft_Windows_XAML_247_0(Etw):
    pattern = Struct(
        "VisualId" / Int64ul,
        "M11" / Float32l,
        "M12" / Float32l,
        "M21" / Float32l,
        "M22" / Float32l,
        "M31" / Float32l,
        "M32" / Float32l
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=247, version=1)
class Microsoft_Windows_XAML_247_1(Etw):
    pattern = Struct(
        "Visual" / Int64ul,
        "Transform" / Int64ul,
        "IsAnimated" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=248, version=0)
class Microsoft_Windows_XAML_248_0(Etw):
    pattern = Struct(
        "VisualId" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=249, version=0)
class Microsoft_Windows_XAML_249_0(Etw):
    pattern = Struct(
        "VisualId" / Int64ul,
        "Width" / Int32ul,
        "Height" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=250, version=0)
class Microsoft_Windows_XAML_250_0(Etw):
    pattern = Struct(
        "VisualId" / Int64ul,
        "Width" / Int32ul,
        "Height" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=251, version=0)
class Microsoft_Windows_XAML_251_0(Etw):
    pattern = Struct(
        "VisualId" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=252, version=0)
class Microsoft_Windows_XAML_252_0(Etw):
    pattern = Struct(
        "VisualId" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=253, version=0)
class Microsoft_Windows_XAML_253_0(Etw):
    pattern = Struct(
        "VisualId" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=253, version=1)
class Microsoft_Windows_XAML_253_1(Etw):
    pattern = Struct(
        "Visual" / Int64ul,
        "Left" / Float32l,
        "Top" / Float32l,
        "Right" / Float32l,
        "Bottom" / Float32l
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=254, version=0)
class Microsoft_Windows_XAML_254_0(Etw):
    pattern = Struct(
        "VisualId" / Int64ul,
        "Width" / Int32ul,
        "Height" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=255, version=0)
class Microsoft_Windows_XAML_255_0(Etw):
    pattern = Struct(
        "ControllerId" / Int64ul,
        "PreviousQPC" / Int64ul,
        "PreviousVBlank" / Int32ul,
        "ReportedQPC" / Int64ul,
        "QPCTicksPerVBlank" / Float32l,
        "CalculatedVBlank" / Int32ul,
        "ReportedVBlank" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=256, version=0)
class Microsoft_Windows_XAML_256_0(Etw):
    pattern = Struct(
        "State" / WString
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=257, version=0)
class Microsoft_Windows_XAML_257_0(Etw):
    pattern = Struct(
        "State" / WString
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=258, version=0)
class Microsoft_Windows_XAML_258_0(Etw):
    pattern = Struct(
        "HighPriority" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=259, version=0)
class Microsoft_Windows_XAML_259_0(Etw):
    pattern = Struct(
        "ApplicationViewState" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=260, version=0)
class Microsoft_Windows_XAML_260_0(Etw):
    pattern = Struct(
        "ApplicationViewState" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=261, version=0)
class Microsoft_Windows_XAML_261_0(Etw):
    pattern = Struct(
        "ApplicationViewState" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=261, version=1)
class Microsoft_Windows_XAML_261_1(Etw):
    pattern = Struct(
        "Window" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=262, version=0)
class Microsoft_Windows_XAML_262_0(Etw):
    pattern = Struct(
        "ApplicationViewState" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=262, version=1)
class Microsoft_Windows_XAML_262_1(Etw):
    pattern = Struct(
        "Window" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=266, version=0)
class Microsoft_Windows_XAML_266_0(Etw):
    pattern = Struct(
        "SourceSurface" / Int64ul,
        "DestinationSurface" / Int64ul,
        "UpdateType" / Int32ul,
        "SourceX" / Int32ul,
        "SourceY" / Int32ul,
        "SourceWidth" / Int32ul,
        "SourceHeight" / Int32ul,
        "TargetOffsetX" / Int32ul,
        "TargetOffsetY" / Int32ul,
        "Pixels" / Int64ul,
        "BitDepth" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=277, version=0)
class Microsoft_Windows_XAML_277_0(Etw):
    pattern = Struct(
        "SourceSurface" / Int64ul,
        "DestinationSurface" / Int64ul,
        "UpdateType" / Int32ul,
        "SourceX" / Int32ul,
        "SourceY" / Int32ul,
        "SourceWidth" / Int32ul,
        "SourceHeight" / Int32ul,
        "TargetOffsetX" / Int32ul,
        "TargetOffsetY" / Int32ul,
        "Pixels" / Int64ul,
        "BitDepth" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=278, version=0)
class Microsoft_Windows_XAML_278_0(Etw):
    pattern = Struct(
        "ParentDCompVisual" / Int64ul,
        "ChildDCompVisual" / Int64ul,
        "PreviousSiblingDCompVisual" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=279, version=0)
class Microsoft_Windows_XAML_279_0(Etw):
    pattern = Struct(
        "ParentDCompVisual" / Int64ul,
        "ChildDCompVisual" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=280, version=0)
class Microsoft_Windows_XAML_280_0(Etw):
    pattern = Struct(
        "DCompVisual" / Int64ul,
        "PrimitiveGroup" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=281, version=0)
class Microsoft_Windows_XAML_281_0(Etw):
    pattern = Struct(
        "Primitive" / Int64ul,
        "PrimitiveGroup" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=282, version=0)
class Microsoft_Windows_XAML_282_0(Etw):
    pattern = Struct(
        "Primitive" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=283, version=0)
class Microsoft_Windows_XAML_283_0(Etw):
    pattern = Struct(
        "SplitAfter" / Int64ul,
        "NewPrimitiveGroup" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=284, version=0)
class Microsoft_Windows_XAML_284_0(Etw):
    pattern = Struct(
        "From" / Int64ul,
        "To" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=285, version=0)
class Microsoft_Windows_XAML_285_0(Etw):
    pattern = Struct(
        "CompNode" / Int64ul,
        "IsEmulated" / Int32ul,
        "IsPlaceholder" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=286, version=0)
class Microsoft_Windows_XAML_286_0(Etw):
    pattern = Struct(
        "CompNode" / Int64ul,
        "PrimitiveGroup" / Int64ul,
        "IsEmulated" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=287, version=0)
class Microsoft_Windows_XAML_287_0(Etw):
    pattern = Struct(
        "CompNode" / Int64ul,
        "IsEmulated" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=288, version=0)
class Microsoft_Windows_XAML_288_0(Etw):
    pattern = Struct(
        "Parent" / Int64ul,
        "Child" / Int64ul,
        "ReferenceNode" / Int64ul,
        "InsertAtBeginning" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=289, version=0)
class Microsoft_Windows_XAML_289_0(Etw):
    pattern = Struct(
        "Parent" / Int64ul,
        "Child" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=290, version=0)
class Microsoft_Windows_XAML_290_0(Etw):
    pattern = Struct(
        "Parent" / Int64ul,
        "Child" / Int64ul,
        "RemoveForReparenting" / Int32ul,
        "MergePrimitiveGroups" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=291, version=0)
class Microsoft_Windows_XAML_291_0(Etw):
    pattern = Struct(
        "Parent" / Int64ul,
        "Child" / Int64ul,
        "RemoveForReparenting" / Int32ul,
        "MergePrimitiveGroups" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=292, version=0)
class Microsoft_Windows_XAML_292_0(Etw):
    pattern = Struct(
        "RedirectionNode" / Int64ul,
        "RedirectionTargetAncestor" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=293, version=0)
class Microsoft_Windows_XAML_293_0(Etw):
    pattern = Struct(
        "RenderDataNode" / Int64ul,
        "PrimitiveGroup" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=294, version=0)
class Microsoft_Windows_XAML_294_0(Etw):
    pattern = Struct(
        "Node" / Int64ul,
        "VisualIndex" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=295, version=0)
class Microsoft_Windows_XAML_295_0(Etw):
    pattern = Struct(
        "Element" / Int64ul,
        "CompNode" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=296, version=0)
class Microsoft_Windows_XAML_296_0(Etw):
    pattern = Struct(
        "Element" / Int64ul,
        "CompNode" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=297, version=0)
class Microsoft_Windows_XAML_297_0(Etw):
    pattern = Struct(
        "ResourceDictionaryId" / Int64ul,
        "ResourceId" / Int64ul,
        "Key" / WString,
        "KeyIsType" / Int8ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=298, version=0)
class Microsoft_Windows_XAML_298_0(Etw):
    pattern = Struct(
        "ResourceDictionaryId" / Int64ul,
        "Key" / WString,
        "KeyIsType" / Int8ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=299, version=0)
class Microsoft_Windows_XAML_299_0(Etw):
    pattern = Struct(
        "ResourceDictionaryId" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=300, version=0)
class Microsoft_Windows_XAML_300_0(Etw):
    pattern = Struct(
        "TemplateId" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=301, version=0)
class Microsoft_Windows_XAML_301_0(Etw):
    pattern = Struct(
        "TemplateId" / Int64ul,
        "ElementId" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=302, version=0)
class Microsoft_Windows_XAML_302_0(Etw):
    pattern = Struct(
        "TemplateId" / Int64ul,
        "OwnerId" / Int64ul,
        "OwnerIsStyle" / Int8ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=303, version=0)
class Microsoft_Windows_XAML_303_0(Etw):
    pattern = Struct(
        "ElementId" / Int64ul,
        "StyleId" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=304, version=0)
class Microsoft_Windows_XAML_304_0(Etw):
    pattern = Struct(
        "IsSelectionStartGripper" / Int32ul,
        "CenterX" / Int32ul,
        "CenterY" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=305, version=0)
class Microsoft_Windows_XAML_305_0(Etw):
    pattern = Struct(
        "IsSelectionStartGripper" / Int32ul,
        "CenterX" / Int32ul,
        "CenterY" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=306, version=0)
class Microsoft_Windows_XAML_306_0(Etw):
    pattern = Struct(
        "IsSelectionStartGripper" / Int32ul,
        "CenterX" / Int32ul,
        "CenterY" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=307, version=0)
class Microsoft_Windows_XAML_307_0(Etw):
    pattern = Struct(
        "IsSelectionStartGripper" / Int32ul,
        "CenterX" / Int32ul,
        "CenterY" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=310, version=0)
class Microsoft_Windows_XAML_310_0(Etw):
    pattern = Struct(
        "IsSelectionStartGripper" / Int32ul,
        "CenterX" / Int32ul,
        "CenterY" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=323, version=0)
class Microsoft_Windows_XAML_323_0(Etw):
    pattern = Struct(
        "ScrollViewerId" / Int64ul,
        "Left" / Float32l,
        "Top" / Float32l,
        "Width" / Float32l,
        "Height" / Float32l,
        "ViewportWidth" / Float32l,
        "ViewportHeight" / Float32l,
        "ExtentWidth" / Float32l,
        "ExtentHeight" / Float32l,
        "HasPlaceholders" / Int8ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=334, version=0)
class Microsoft_Windows_XAML_334_0(Etw):
    pattern = Struct(
        "IsSurfaceBeingRendered" / Int8ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=336, version=0)
class Microsoft_Windows_XAML_336_0(Etw):
    pattern = Struct(
        "WasDiscarded" / Int8ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=337, version=0)
class Microsoft_Windows_XAML_337_0(Etw):
    pattern = Struct(
        "DummyMetric" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=338, version=0)
class Microsoft_Windows_XAML_338_0(Etw):
    pattern = Struct(
        "Device" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=339, version=0)
class Microsoft_Windows_XAML_339_0(Etw):
    pattern = Struct(
        "Device" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=340, version=0)
class Microsoft_Windows_XAML_340_0(Etw):
    pattern = Struct(
        "Primitive" / Int64ul,
        "Left" / Float32l,
        "Top" / Float32l,
        "Right" / Float32l,
        "Bottom" / Float32l,
        "Color" / Int32ul,
        "Opacity" / Float32l
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=341, version=0)
class Microsoft_Windows_XAML_341_0(Etw):
    pattern = Struct(
        "Primitive" / Int64ul,
        "PCRenderDataList" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=342, version=0)
class Microsoft_Windows_XAML_342_0(Etw):
    pattern = Struct(
        "Primitive" / Int64ul,
        "InsertAfter" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=343, version=0)
class Microsoft_Windows_XAML_343_0(Etw):
    pattern = Struct(
        "CompNode" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=344, version=0)
class Microsoft_Windows_XAML_344_0(Etw):
    pattern = Struct(
        "CompNode" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=345, version=0)
class Microsoft_Windows_XAML_345_0(Etw):
    pattern = Struct(
        "Visual" / Int64ul,
        "Opacity" / Float32l,
        "IsAnimated" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=346, version=0)
class Microsoft_Windows_XAML_346_0(Etw):
    pattern = Struct(
        "TransformMainDevice" / Int64ul,
        "TransformSecondaryDevice" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=347, version=0)
class Microsoft_Windows_XAML_347_0(Etw):
    pattern = Struct(
        "TransformGroup" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=348, version=0)
class Microsoft_Windows_XAML_348_0(Etw):
    pattern = Struct(
        "Transform" / Int64ul,
        "M11" / Float32l,
        "M12" / Float32l,
        "M21" / Float32l,
        "M22" / Float32l,
        "M31" / Float32l,
        "M32" / Float32l
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=349, version=0)
class Microsoft_Windows_XAML_349_0(Etw):
    pattern = Struct(
        "TransformGroup" / Int64ul,
        "Transform" / Int64ul,
        "Index" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=352, version=0)
class Microsoft_Windows_XAML_352_0(Etw):
    pattern = Struct(
        "ScrollViewerId" / Int64ul,
        "Left" / Float32l,
        "Top" / Float32l,
        "Width" / Float32l,
        "Height" / Float32l
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=353, version=0)
class Microsoft_Windows_XAML_353_0(Etw):
    pattern = Struct(
        "ElementId" / Int64ul,
        "ScrollViewerId" / Int64ul,
        "ItemIndex" / Int32sl,
        "IsPlaceholder" / Int8ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=354, version=0)
class Microsoft_Windows_XAML_354_0(Etw):
    pattern = Struct(
        "ElementId" / Int64ul,
        "Phase" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=355, version=0)
class Microsoft_Windows_XAML_355_0(Etw):
    pattern = Struct(
        "ElementId" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=356, version=0)
class Microsoft_Windows_XAML_356_0(Etw):
    pattern = Struct(
        "ImageId" / Int64ul,
        "RenderWidth" / Int32ul,
        "RenderHeight" / Int32ul,
        "PreviousDecodeWidth" / Int32ul,
        "PreviousDecodeHeight" / Int32ul,
        "DecodeWidth" / Int32ul,
        "DecodeHeight" / Int32ul,
        "NativeWidth" / Int32ul,
        "NativeHeight" / Int32ul,
        "LayoutWidth" / Int32ul,
        "LayoutHeight" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=357, version=0)
class Microsoft_Windows_XAML_357_0(Etw):
    pattern = Struct(
        "ImageId" / Int64ul,
        "RenderWidth" / Int32ul,
        "RenderHeight" / Int32ul,
        "PreviousDecodeWidth" / Int32ul,
        "PreviousDecodeHeight" / Int32ul,
        "DecodeWidth" / Int32ul,
        "DecodeHeight" / Int32ul,
        "NativeWidth" / Int32ul,
        "NativeHeight" / Int32ul,
        "LayoutWidth" / Int32ul,
        "LayoutHeight" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=360, version=0)
class Microsoft_Windows_XAML_360_0(Etw):
    pattern = Struct(
        "ImageId" / Int64ul,
        "URI" / WString
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=360, version=1)
class Microsoft_Windows_XAML_360_1(Etw):
    pattern = Struct(
        "ImageId" / Int64ul,
        "RenderWidth" / Int32ul,
        "RenderHeight" / Int32ul,
        "PreviousDecodeWidth" / Int32ul,
        "PreviousDecodeHeight" / Int32ul,
        "DecodeWidth" / Int32ul,
        "DecodeHeight" / Int32ul,
        "NativeWidth" / Int32ul,
        "NativeHeight" / Int32ul,
        "LayoutWidth" / Int32ul,
        "LayoutHeight" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=361, version=0)
class Microsoft_Windows_XAML_361_0(Etw):
    pattern = Struct(
        "ImageId" / Int64ul,
        "URI" / WString
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=362, version=0)
class Microsoft_Windows_XAML_362_0(Etw):
    pattern = Struct(
        "ImageId" / Int64ul,
        "URI" / WString
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=363, version=0)
class Microsoft_Windows_XAML_363_0(Etw):
    pattern = Struct(
        "ImageId" / Int64ul,
        "URI" / WString
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=364, version=0)
class Microsoft_Windows_XAML_364_0(Etw):
    pattern = Struct(
        "ImageId" / Int64ul,
        "URI" / WString
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=365, version=0)
class Microsoft_Windows_XAML_365_0(Etw):
    pattern = Struct(
        "ImageId" / Int64ul,
        "URI" / WString
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=366, version=0)
class Microsoft_Windows_XAML_366_0(Etw):
    pattern = Struct(
        "Id" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=367, version=0)
class Microsoft_Windows_XAML_367_0(Etw):
    pattern = Struct(
        "Id" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=368, version=0)
class Microsoft_Windows_XAML_368_0(Etw):
    pattern = Struct(
        "ImageId" / Int64ul,
        "URI" / WString
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=369, version=0)
class Microsoft_Windows_XAML_369_0(Etw):
    pattern = Struct(
        "ImageId" / Int64ul,
        "URI" / WString
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=370, version=0)
class Microsoft_Windows_XAML_370_0(Etw):
    pattern = Struct(
        "Id" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=371, version=0)
class Microsoft_Windows_XAML_371_0(Etw):
    pattern = Struct(
        "Id" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=372, version=0)
class Microsoft_Windows_XAML_372_0(Etw):
    pattern = Struct(
        "ImageId" / Int64ul,
        "URI" / WString
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=373, version=0)
class Microsoft_Windows_XAML_373_0(Etw):
    pattern = Struct(
        "ImageId" / Int64ul,
        "URI" / WString
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=374, version=0)
class Microsoft_Windows_XAML_374_0(Etw):
    pattern = Struct(
        "ImageId" / Int64ul,
        "URI" / WString
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=375, version=0)
class Microsoft_Windows_XAML_375_0(Etw):
    pattern = Struct(
        "ImageId" / Int64ul,
        "URI" / WString
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=377, version=0)
class Microsoft_Windows_XAML_377_0(Etw):
    pattern = Struct(
        "IsEnabled" / Int8ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=377, version=1)
class Microsoft_Windows_XAML_377_1(Etw):
    pattern = Struct(
        "IsEnabled" / Int8ul,
        "ElementId" / Int64ul,
        "Name" / WString,
        "ClassType" / WString,
        "PropertyType" / WString
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=378, version=0)
class Microsoft_Windows_XAML_378_0(Etw):
    pattern = Struct(
        "IsEnabled" / Int8ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=378, version=1)
class Microsoft_Windows_XAML_378_1(Etw):
    pattern = Struct(
        "IsEnabled" / Int8ul,
        "ElementId" / Int64ul,
        "Name" / WString,
        "ClassType" / WString,
        "PropertyType" / WString
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=379, version=0)
class Microsoft_Windows_XAML_379_0(Etw):
    pattern = Struct(
        "CurrentSectionCount" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=382, version=0)
class Microsoft_Windows_XAML_382_0(Etw):
    pattern = Struct(
        "ImageId" / Int64ul,
        "Reason" / WString
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=382, version=1)
class Microsoft_Windows_XAML_382_1(Etw):
    pattern = Struct(
        "ImageId" / Int64ul,
        "Reason" / WString,
        "ReasonKey" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=383, version=0)
class Microsoft_Windows_XAML_383_0(Etw):
    pattern = Struct(
        "ViewportId" / Int64ul,
        "ContentId" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=384, version=0)
class Microsoft_Windows_XAML_384_0(Etw):
    pattern = Struct(
        "ViewportId" / Int64ul,
        "ContentId" / Int64ul,
        "ContentType" / Int32ul,
        "TranslationX" / Float32l,
        "TranslationY" / Float32l,
        "ZoomFactor" / Float32l,
        "ZoomFactorX" / Float32l,
        "ZoomFactorY" / Float32l
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=385, version=0)
class Microsoft_Windows_XAML_385_0(Etw):
    pattern = Struct(
        "ViewportId" / Int64ul,
        "ContentId" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=386, version=0)
class Microsoft_Windows_XAML_386_0(Etw):
    pattern = Struct(
        "ViewportId" / Int64ul,
        "ContentId" / Int64ul,
        "ContentType" / Int32ul,
        "TranslationX" / Float32l,
        "TranslationY" / Float32l,
        "ZoomFactor" / Float32l,
        "ZoomFactorX" / Float32l,
        "ZoomFactorY" / Float32l
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=387, version=0)
class Microsoft_Windows_XAML_387_0(Etw):
    pattern = Struct(
        "PageDescriptor" / WString,
        "NavigationMode" / Int8ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=388, version=0)
class Microsoft_Windows_XAML_388_0(Etw):
    pattern = Struct(
        "PageDescriptor" / WString,
        "NavigationMode" / Int8ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=389, version=0)
class Microsoft_Windows_XAML_389_0(Etw):
    pattern = Struct(
        "PageDescriptor" / WString,
        "InCache" / Int8ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=393, version=0)
class Microsoft_Windows_XAML_393_0(Etw):
    pattern = Struct(
        "Id" / Int64ul,
        "Width" / Int32ul,
        "Height" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=394, version=0)
class Microsoft_Windows_XAML_394_0(Etw):
    pattern = Struct(
        "Handle" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=395, version=0)
class Microsoft_Windows_XAML_395_0(Etw):
    pattern = Struct(
        "Id" / Int64ul,
        "Width" / Int32ul,
        "Height" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=396, version=0)
class Microsoft_Windows_XAML_396_0(Etw):
    pattern = Struct(
        "Id" / Int64ul,
        "EffectId" / WString,
        "EffectType" / Int32ul,
        "EffectOptional" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=397, version=0)
class Microsoft_Windows_XAML_397_0(Etw):
    pattern = Struct(
        "DeferredElementId" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=398, version=0)
class Microsoft_Windows_XAML_398_0(Etw):
    pattern = Struct(
        "DeferredElementId" / Int64ul,
        "RealizedElementId" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=399, version=0)
class Microsoft_Windows_XAML_399_0(Etw):
    pattern = Struct(
        "InputScopeValue" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=400, version=0)
class Microsoft_Windows_XAML_400_0(Etw):
    pattern = Struct(
        "IKSkinValue" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=401, version=0)
class Microsoft_Windows_XAML_401_0(Etw):
    pattern = Struct(
        "Id" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=402, version=0)
class Microsoft_Windows_XAML_402_0(Etw):
    pattern = Struct(
        "Id" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=403, version=0)
class Microsoft_Windows_XAML_403_0(Etw):
    pattern = Struct(
        "Axis" / Int32ul,
        "Curve" / Int32ul,
        "Segment" / Int32ul,
        "Offset" / Float32l,
        "Constant" / Float32l,
        "Linear" / Float32l
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=404, version=0)
class Microsoft_Windows_XAML_404_0(Etw):
    pattern = Struct(
        "ContentType" / Int32sl,
        "OffsetX" / Float32l,
        "OffseY" / Float32l
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=405, version=0)
class Microsoft_Windows_XAML_405_0(Etw):
    pattern = Struct(
        "address" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=406, version=0)
class Microsoft_Windows_XAML_406_0(Etw):
    pattern = Struct(
        "address" / Int64ul,
        "TranslateX" / Float32l,
        "TranslateY" / Float32l
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=407, version=0)
class Microsoft_Windows_XAML_407_0(Etw):
    pattern = Struct(
        "translateX" / Float32l,
        "translateY" / Float32l
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=408, version=0)
class Microsoft_Windows_XAML_408_0(Etw):
    pattern = Struct(
        "address" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=409, version=0)
class Microsoft_Windows_XAML_409_0(Etw):
    pattern = Struct(
        "FaultInType" / WString
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=411, version=0)
class Microsoft_Windows_XAML_411_0(Etw):
    pattern = Struct(
        "Id" / Int64ul,
        "IsFullScreen" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=413, version=0)
class Microsoft_Windows_XAML_413_0(Etw):
    pattern = Struct(
        "ContentNodeId" / Int64ul,
        "SwapchainHandle" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=414, version=0)
class Microsoft_Windows_XAML_414_0(Etw):
    pattern = Struct(
        "InvokeResult" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=415, version=0)
class Microsoft_Windows_XAML_415_0(Etw):
    pattern = Struct(
        "Result" / Int32ul,
        "SecondaryCheck" / Int8ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=416, version=0)
class Microsoft_Windows_XAML_416_0(Etw):
    pattern = Struct(
        "State" / WString
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=421, version=0)
class Microsoft_Windows_XAML_421_0(Etw):
    pattern = Struct(
        "ReleaseDcompDevice" / Int8ul,
        "IsDeviceLost" / Int8ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=428, version=0)
class Microsoft_Windows_XAML_428_0(Etw):
    pattern = Struct(
        "Parent" / Int64ul,
        "Visual" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=429, version=0)
class Microsoft_Windows_XAML_429_0(Etw):
    pattern = Struct(
        "setFocus" / Int8ul,
        "isProcessingTab" / Int8ul,
        "isShiftPressed" / Int8ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=430, version=0)
class Microsoft_Windows_XAML_430_0(Etw):
    pattern = Struct(
        "ElementId" / Int64ul,
        "Left" / Float32l,
        "Top" / Float32l,
        "Width" / Float32l,
        "Height" / Float32l
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=433, version=0)
class Microsoft_Windows_XAML_433_0(Etw):
    pattern = Struct(
        "Width" / Int32ul,
        "Height" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=434, version=0)
class Microsoft_Windows_XAML_434_0(Etw):
    pattern = Struct(
        "value" / CString,
        "CRC" / Int32ul,
        "chunk" / Int32ul,
        "numChunks" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=435, version=0)
class Microsoft_Windows_XAML_435_0(Etw):
    pattern = Struct(
        "ImageId" / Int64ul,
        "DecodeWidth" / Int32ul,
        "DecodeHeight" / Int32ul,
        "NaturalWidth" / Int32ul,
        "NaturalHeight" / Int32ul,
        "RetrievedFromCache" / Int8ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=436, version=0)
class Microsoft_Windows_XAML_436_0(Etw):
    pattern = Struct(
        "ImageId" / Int64ul,
        "URI" / WString,
        "ImageState" / WString,
        "ImageStateKey" / Int32ul,
        "Width" / Int32ul,
        "Height" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=437, version=0)
class Microsoft_Windows_XAML_437_0(Etw):
    pattern = Struct(
        "Size" / Int32sl
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=438, version=0)
class Microsoft_Windows_XAML_438_0(Etw):
    pattern = Struct(
        "Size" / Int32sl
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=439, version=0)
class Microsoft_Windows_XAML_439_0(Etw):
    pattern = Struct(
        "Size" / Int32sl
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=441, version=0)
class Microsoft_Windows_XAML_441_0(Etw):
    pattern = Struct(
        "Value" / Int8ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=444, version=0)
class Microsoft_Windows_XAML_444_0(Etw):
    pattern = Struct(
        "Value" / Int8ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=446, version=0)
class Microsoft_Windows_XAML_446_0(Etw):
    pattern = Struct(
        "RequestInMS" / Int32sl,
        "NextTickIntervalInMS" / Int32sl,
        "Reason" / Int32ul,
        "TotalReasons" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=447, version=0)
class Microsoft_Windows_XAML_447_0(Etw):
    pattern = Struct(
        "Id" / Int64ul,
        "Width" / Int32ul,
        "Height" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=448, version=0)
class Microsoft_Windows_XAML_448_0(Etw):
    pattern = Struct(
        "Id" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=450, version=0)
class Microsoft_Windows_XAML_450_0(Etw):
    pattern = Struct(
        "Id" / Int64ul,
        "HR" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=451, version=0)
class Microsoft_Windows_XAML_451_0(Etw):
    pattern = Struct(
        "ElementId" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=452, version=0)
class Microsoft_Windows_XAML_452_0(Etw):
    pattern = Struct(
        "Id" / Int64ul,
        "PropertyIndex" / Int16ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=453, version=0)
class Microsoft_Windows_XAML_453_0(Etw):
    pattern = Struct(
        "ElementId" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=454, version=0)
class Microsoft_Windows_XAML_454_0(Etw):
    pattern = Struct(
        "Id" / Int64ul,
        "PropertyIndex" / Int16ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=455, version=0)
class Microsoft_Windows_XAML_455_0(Etw):
    pattern = Struct(
        "Id" / Int64ul,
        "MethodIndex" / Int16ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=456, version=0)
class Microsoft_Windows_XAML_456_0(Etw):
    pattern = Struct(
        "Id" / Int64ul,
        "HR" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=465, version=0)
class Microsoft_Windows_XAML_465_0(Etw):
    pattern = Struct(
        "TargetId" / Int64ul,
        "TargetName" / WString,
        "TargetProperty" / WString
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=466, version=0)
class Microsoft_Windows_XAML_466_0(Etw):
    pattern = Struct(
        "ElementId" / Int64ul,
        "Name" / WString
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=467, version=0)
class Microsoft_Windows_XAML_467_0(Etw):
    pattern = Struct(
        "Id" / Int64ul,
        "Reason" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=468, version=0)
class Microsoft_Windows_XAML_468_0(Etw):
    pattern = Struct(
        "Objects" / Int32sl,
        "Sources" / Int32sl,
        "Targets" / Int32sl,
        "Unreachable" / Int32sl
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=469, version=0)
class Microsoft_Windows_XAML_469_0(Etw):
    pattern = Struct(
        "ID" / Int32sl
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=470, version=0)
class Microsoft_Windows_XAML_470_0(Etw):
    pattern = Struct(
        "Objects" / Int32sl,
        "Attempts" / Int32sl,
        "Completed" / Int32sl
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=471, version=0)
class Microsoft_Windows_XAML_471_0(Etw):
    pattern = Struct(
        "Id" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=472, version=0)
class Microsoft_Windows_XAML_472_0(Etw):
    pattern = Struct(
        "Id" / Int64ul,
        "HR" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=473, version=0)
class Microsoft_Windows_XAML_473_0(Etw):
    pattern = Struct(
        "ParentId" / Int64ul,
        "ChildId" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=474, version=0)
class Microsoft_Windows_XAML_474_0(Etw):
    pattern = Struct(
        "Id" / Int64ul,
        "Value" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=475, version=0)
class Microsoft_Windows_XAML_475_0(Etw):
    pattern = Struct(
        "Id" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=476, version=0)
class Microsoft_Windows_XAML_476_0(Etw):
    pattern = Struct(
        "Id" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=477, version=0)
class Microsoft_Windows_XAML_477_0(Etw):
    pattern = Struct(
        "Id" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=478, version=0)
class Microsoft_Windows_XAML_478_0(Etw):
    pattern = Struct(
        "ParentId" / Int64ul,
        "ChildId" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=479, version=0)
class Microsoft_Windows_XAML_479_0(Etw):
    pattern = Struct(
        "ParentId" / Int64ul,
        "ChildId" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=480, version=0)
class Microsoft_Windows_XAML_480_0(Etw):
    pattern = Struct(
        "Id" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=481, version=0)
class Microsoft_Windows_XAML_481_0(Etw):
    pattern = Struct(
        "Id" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=482, version=0)
class Microsoft_Windows_XAML_482_0(Etw):
    pattern = Struct(
        "Id" / Int64ul,
        "Value" / WString
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=483, version=0)
class Microsoft_Windows_XAML_483_0(Etw):
    pattern = Struct(
        "Id" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=484, version=0)
class Microsoft_Windows_XAML_484_0(Etw):
    pattern = Struct(
        "Id" / Int64ul,
        "HR" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=485, version=0)
class Microsoft_Windows_XAML_485_0(Etw):
    pattern = Struct(
        "Id" / Int64ul,
        "Size" / Int32sl
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=486, version=0)
class Microsoft_Windows_XAML_486_0(Etw):
    pattern = Struct(
        "Direction" / WString
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=488, version=0)
class Microsoft_Windows_XAML_488_0(Etw):
    pattern = Struct(
        "ElementId" / Int64ul,
        "Direction" / WString
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=489, version=0)
class Microsoft_Windows_XAML_489_0(Etw):
    pattern = Struct(
        "ItemIndex" / Int32sl
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=492, version=0)
class Microsoft_Windows_XAML_492_0(Etw):
    pattern = Struct(
        "ElementId" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=493, version=0)
class Microsoft_Windows_XAML_493_0(Etw):
    pattern = Struct(
        "ElementId" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=498, version=0)
class Microsoft_Windows_XAML_498_0(Etw):
    pattern = Struct(
        "ElementId" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=505, version=0)
class Microsoft_Windows_XAML_505_0(Etw):
    pattern = Struct(
        "ItemIndex" / Int32sl
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=507, version=0)
class Microsoft_Windows_XAML_507_0(Etw):
    pattern = Struct(
        "ItemIndex" / Int32sl
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=524, version=0)
class Microsoft_Windows_XAML_524_0(Etw):
    pattern = Struct(
        "RegisteredOn" / Int64ul,
        "KeyCode" / Int32ul,
        "OriginalSource" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=525, version=0)
class Microsoft_Windows_XAML_525_0(Etw):
    pattern = Struct(
        "Handled" / Int8ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=526, version=0)
class Microsoft_Windows_XAML_526_0(Etw):
    pattern = Struct(
        "RegisteredOn" / Int64ul,
        "KeyCode" / Int32ul,
        "OriginalSource" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=527, version=0)
class Microsoft_Windows_XAML_527_0(Etw):
    pattern = Struct(
        "Handled" / Int8ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=528, version=0)
class Microsoft_Windows_XAML_528_0(Etw):
    pattern = Struct(
        "KeyCode" / Int32ul,
        "RepeatCount" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=529, version=0)
class Microsoft_Windows_XAML_529_0(Etw):
    pattern = Struct(
        "KeyCode" / Int32ul,
        "RepeatCount" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=530, version=0)
class Microsoft_Windows_XAML_530_0(Etw):
    pattern = Struct(
        "KeyCode" / Int32ul,
        "RepeatCount" / Int32ul,
        "CountBeforeSubmitFrame" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=531, version=0)
class Microsoft_Windows_XAML_531_0(Etw):
    pattern = Struct(
        "KeyCode" / Int32ul,
        "RepeatCount" / Int32ul,
        "CountBeforeSubmitFrame" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=538, version=0)
class Microsoft_Windows_XAML_538_0(Etw):
    pattern = Struct(
        "ElementId" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=540, version=0)
class Microsoft_Windows_XAML_540_0(Etw):
    pattern = Struct(
        "ElementId" / Int64ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=542, version=0)
class Microsoft_Windows_XAML_542_0(Etw):
    pattern = Struct(
        "Direction" / WString
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=544, version=0)
class Microsoft_Windows_XAML_544_0(Etw):
    pattern = Struct(
        "Direction" / WString
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=556, version=0)
class Microsoft_Windows_XAML_556_0(Etw):
    pattern = Struct(
        "Type" / WString
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=558, version=0)
class Microsoft_Windows_XAML_558_0(Etw):
    pattern = Struct(
        "Type" / WString,
        "PropertyType" / WString
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=565, version=0)
class Microsoft_Windows_XAML_565_0(Etw):
    pattern = Struct(
        "Name" / WString
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=568, version=0)
class Microsoft_Windows_XAML_568_0(Etw):
    pattern = Struct(
        "Runtime" / Int64ul,
        "Type" / WString
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=575, version=0)
class Microsoft_Windows_XAML_575_0(Etw):
    pattern = Struct(
        "KeyCode" / Int32ul,
        "RepeatCount" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=576, version=0)
class Microsoft_Windows_XAML_576_0(Etw):
    pattern = Struct(
        "M4x4Multiplications" / Int32ul,
        "M3x2AsM4x4Multiplications" / Int32ul,
        "M4x4PointMultiplications" / Int32ul,
        "M4x4TransformBounds" / Int32ul,
        "Count3DBoundsMode" / Int32ul,
        "Projections" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=577, version=0)
class Microsoft_Windows_XAML_577_0(Etw):
    pattern = Struct(
        "RecalculatedCount" / Int32ul,
        "ReusedCount" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=578, version=0)
class Microsoft_Windows_XAML_578_0(Etw):
    pattern = Struct(
        "RecalculatedCount" / Int32ul,
        "ReusedCount" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=579, version=0)
class Microsoft_Windows_XAML_579_0(Etw):
    pattern = Struct(
        "RecalculatedCount" / Int32ul,
        "ReusedCount" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=580, version=0)
class Microsoft_Windows_XAML_580_0(Etw):
    pattern = Struct(
        "RecalculatedCount" / Int32ul,
        "ReusedCount" / Int32ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=581, version=0)
class Microsoft_Windows_XAML_581_0(Etw):
    pattern = Struct(
        "UIElement" / Int64ul,
        "OnRootVisual" / Int8ul
    )


@declare(guid=guid("531a35ab-63ce-4bcf-aa98-f88c7a89e455"), event_id=582, version=0)
class Microsoft_Windows_XAML_582_0(Etw):
    pattern = Struct(
        "UIElement" / Int64ul,
        "Interaction" / Int64ul
    )

