# -*- coding: utf-8 -*-
"""
Microsoft-Windows-DirectManipulation
GUID : 5786e035-ef2d-4178-84f2-5a6bbedbb947
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("5786e035-ef2d-4178-84f2-5a6bbedbb947"), event_id=26, version=0)
class Microsoft_Windows_DirectManipulation_26_0(Etw):
    pattern = Struct(
        "PointerId" / Int32ul,
        "ContactId" / Int32ul
    )


@declare(guid=guid("5786e035-ef2d-4178-84f2-5a6bbedbb947"), event_id=27, version=0)
class Microsoft_Windows_DirectManipulation_27_0(Etw):
    pattern = Struct(
        "PointerId" / Int32ul,
        "ContactId" / Int32ul
    )


@declare(guid=guid("5786e035-ef2d-4178-84f2-5a6bbedbb947"), event_id=28, version=0)
class Microsoft_Windows_DirectManipulation_28_0(Etw):
    pattern = Struct(
        "PointerId" / Int32ul,
        "RegionPointer" / Int64ul
    )


@declare(guid=guid("5786e035-ef2d-4178-84f2-5a6bbedbb947"), event_id=29, version=0)
class Microsoft_Windows_DirectManipulation_29_0(Etw):
    pattern = Struct(
        "PointerId" / Int32ul,
        "RegionPointer" / Int64ul
    )


@declare(guid=guid("5786e035-ef2d-4178-84f2-5a6bbedbb947"), event_id=30, version=0)
class Microsoft_Windows_DirectManipulation_30_0(Etw):
    pattern = Struct(
        "PointerId" / Int32ul,
        "ContactId" / Int32ul
    )


@declare(guid=guid("5786e035-ef2d-4178-84f2-5a6bbedbb947"), event_id=31, version=0)
class Microsoft_Windows_DirectManipulation_31_0(Etw):
    pattern = Struct(
        "PointerId" / Int32ul,
        "ContactId" / Int32ul
    )


@declare(guid=guid("5786e035-ef2d-4178-84f2-5a6bbedbb947"), event_id=32, version=0)
class Microsoft_Windows_DirectManipulation_32_0(Etw):
    pattern = Struct(
        "PointerId" / Int32ul,
        "RegionPointer" / Int64ul
    )


@declare(guid=guid("5786e035-ef2d-4178-84f2-5a6bbedbb947"), event_id=34, version=0)
class Microsoft_Windows_DirectManipulation_34_0(Etw):
    pattern = Struct(
        "MotionPointer" / Int64ul,
        "RegionPointer" / Int64ul,
        "LayerPointer" / Int64ul
    )


@declare(guid=guid("5786e035-ef2d-4178-84f2-5a6bbedbb947"), event_id=36, version=0)
class Microsoft_Windows_DirectManipulation_36_0(Etw):
    pattern = Struct(
        "PointerId" / Int32ul,
        "ContactId" / Int32ul
    )


@declare(guid=guid("5786e035-ef2d-4178-84f2-5a6bbedbb947"), event_id=38, version=0)
class Microsoft_Windows_DirectManipulation_38_0(Etw):
    pattern = Struct(
        "LayerPointer" / Int64ul
    )


@declare(guid=guid("5786e035-ef2d-4178-84f2-5a6bbedbb947"), event_id=39, version=0)
class Microsoft_Windows_DirectManipulation_39_0(Etw):
    pattern = Struct(
        "ViewportPointer" / Int64ul
    )


@declare(guid=guid("5786e035-ef2d-4178-84f2-5a6bbedbb947"), event_id=40, version=0)
class Microsoft_Windows_DirectManipulation_40_0(Etw):
    pattern = Struct(
        "ViewportPointer" / Int64ul
    )


@declare(guid=guid("5786e035-ef2d-4178-84f2-5a6bbedbb947"), event_id=41, version=0)
class Microsoft_Windows_DirectManipulation_41_0(Etw):
    pattern = Struct(
        "ViewportPointer" / Int64ul
    )


@declare(guid=guid("5786e035-ef2d-4178-84f2-5a6bbedbb947"), event_id=42, version=0)
class Microsoft_Windows_DirectManipulation_42_0(Etw):
    pattern = Struct(
        "ViewportPointer" / Int64ul
    )


@declare(guid=guid("5786e035-ef2d-4178-84f2-5a6bbedbb947"), event_id=43, version=0)
class Microsoft_Windows_DirectManipulation_43_0(Etw):
    pattern = Struct(
        "DManipLatency" / Int32ul,
        "ProcessName" / WString
    )


@declare(guid=guid("5786e035-ef2d-4178-84f2-5a6bbedbb947"), event_id=44, version=0)
class Microsoft_Windows_DirectManipulation_44_0(Etw):
    pattern = Struct(
        "ContentPointer" / Int64ul,
        "TransformType" / Int32sl,
        "xPosition" / Float32l,
        "yPosition" / Float32l,
        "zPosition" / Float32l,
        "PredictedTimeGap" / Int64ul
    )


@declare(guid=guid("5786e035-ef2d-4178-84f2-5a6bbedbb947"), event_id=45, version=0)
class Microsoft_Windows_DirectManipulation_45_0(Etw):
    pattern = Struct(
        "ViewportPointer" / Int64ul
    )


@declare(guid=guid("5786e035-ef2d-4178-84f2-5a6bbedbb947"), event_id=46, version=0)
class Microsoft_Windows_DirectManipulation_46_0(Etw):
    pattern = Struct(
        "ViewportPointer" / Int64ul
    )


@declare(guid=guid("5786e035-ef2d-4178-84f2-5a6bbedbb947"), event_id=47, version=0)
class Microsoft_Windows_DirectManipulation_47_0(Etw):
    pattern = Struct(
        "CompositorPointer" / Int64ul,
        "ViewportPointer" / Int64ul,
        "CurrentStatus" / Int32sl,
        "PreviousStatus" / Int32sl
    )


@declare(guid=guid("5786e035-ef2d-4178-84f2-5a6bbedbb947"), event_id=48, version=0)
class Microsoft_Windows_DirectManipulation_48_0(Etw):
    pattern = Struct(
        "CompositorPointer" / Int64ul,
        "ViewportPointer" / Int64ul,
        "CurrentStatus" / Int32sl,
        "PreviousStatus" / Int32sl
    )


@declare(guid=guid("5786e035-ef2d-4178-84f2-5a6bbedbb947"), event_id=49, version=0)
class Microsoft_Windows_DirectManipulation_49_0(Etw):
    pattern = Struct(
        "CompositorPointer" / Int64ul,
        "ViewportPointer" / Int64ul
    )


@declare(guid=guid("5786e035-ef2d-4178-84f2-5a6bbedbb947"), event_id=50, version=0)
class Microsoft_Windows_DirectManipulation_50_0(Etw):
    pattern = Struct(
        "CompositorPointer" / Int64ul,
        "ViewportPointer" / Int64ul
    )


@declare(guid=guid("5786e035-ef2d-4178-84f2-5a6bbedbb947"), event_id=51, version=0)
class Microsoft_Windows_DirectManipulation_51_0(Etw):
    pattern = Struct(
        "CompositorPointer" / Int64ul,
        "ContentPointer" / Int64ul
    )


@declare(guid=guid("5786e035-ef2d-4178-84f2-5a6bbedbb947"), event_id=52, version=0)
class Microsoft_Windows_DirectManipulation_52_0(Etw):
    pattern = Struct(
        "CompositorPointer" / Int64ul,
        "ContentPointer" / Int64ul
    )


@declare(guid=guid("5786e035-ef2d-4178-84f2-5a6bbedbb947"), event_id=53, version=0)
class Microsoft_Windows_DirectManipulation_53_0(Etw):
    pattern = Struct(
        "CompositorPointer" / Int64ul
    )


@declare(guid=guid("5786e035-ef2d-4178-84f2-5a6bbedbb947"), event_id=54, version=0)
class Microsoft_Windows_DirectManipulation_54_0(Etw):
    pattern = Struct(
        "CompositorPointer" / Int64ul
    )


@declare(guid=guid("5786e035-ef2d-4178-84f2-5a6bbedbb947"), event_id=55, version=0)
class Microsoft_Windows_DirectManipulation_55_0(Etw):
    pattern = Struct(
        "ManagerPointer" / Int64ul,
        "hWnd" / Int64ul
    )


@declare(guid=guid("5786e035-ef2d-4178-84f2-5a6bbedbb947"), event_id=56, version=0)
class Microsoft_Windows_DirectManipulation_56_0(Etw):
    pattern = Struct(
        "ManagerPointer" / Int64ul,
        "hWnd" / Int64ul
    )


@declare(guid=guid("5786e035-ef2d-4178-84f2-5a6bbedbb947"), event_id=57, version=0)
class Microsoft_Windows_DirectManipulation_57_0(Etw):
    pattern = Struct(
        "ManagerPointer" / Int64ul,
        "hWnd" / Int64ul
    )


@declare(guid=guid("5786e035-ef2d-4178-84f2-5a6bbedbb947"), event_id=58, version=0)
class Microsoft_Windows_DirectManipulation_58_0(Etw):
    pattern = Struct(
        "ManagerPointer" / Int64ul,
        "hWnd" / Int64ul
    )


@declare(guid=guid("5786e035-ef2d-4178-84f2-5a6bbedbb947"), event_id=59, version=0)
class Microsoft_Windows_DirectManipulation_59_0(Etw):
    pattern = Struct(
        "ManagerPointer" / Int64ul,
        "FrameInfo" / Int64ul,
        "hWnd" / Int64ul,
        "ViewportPointer" / Int64ul,
        "primaryContentPointer" / Int64ul
    )


@declare(guid=guid("5786e035-ef2d-4178-84f2-5a6bbedbb947"), event_id=60, version=0)
class Microsoft_Windows_DirectManipulation_60_0(Etw):
    pattern = Struct(
        "ManagerPointer" / Int64ul,
        "FrameInfo" / Int64ul,
        "hWnd" / Int64ul,
        "ViewportPointer" / Int64ul,
        "primaryContentPointer" / Int64ul
    )


@declare(guid=guid("5786e035-ef2d-4178-84f2-5a6bbedbb947"), event_id=61, version=0)
class Microsoft_Windows_DirectManipulation_61_0(Etw):
    pattern = Struct(
        "ContactId" / Int32ul
    )


@declare(guid=guid("5786e035-ef2d-4178-84f2-5a6bbedbb947"), event_id=62, version=0)
class Microsoft_Windows_DirectManipulation_62_0(Etw):
    pattern = Struct(
        "ContactId" / Int32ul
    )


@declare(guid=guid("5786e035-ef2d-4178-84f2-5a6bbedbb947"), event_id=63, version=0)
class Microsoft_Windows_DirectManipulation_63_0(Etw):
    pattern = Struct(
        "MessagesQueuedOrProcessed" / Int32sl
    )


@declare(guid=guid("5786e035-ef2d-4178-84f2-5a6bbedbb947"), event_id=64, version=0)
class Microsoft_Windows_DirectManipulation_64_0(Etw):
    pattern = Struct(
        "MessagesQueuedOrProcessed" / Int32sl
    )


@declare(guid=guid("5786e035-ef2d-4178-84f2-5a6bbedbb947"), event_id=65, version=0)
class Microsoft_Windows_DirectManipulation_65_0(Etw):
    pattern = Struct(
        "PointerId" / Int32ul,
        "FrameId" / Int32ul,
        "Message" / Int32ul
    )


@declare(guid=guid("5786e035-ef2d-4178-84f2-5a6bbedbb947"), event_id=66, version=0)
class Microsoft_Windows_DirectManipulation_66_0(Etw):
    pattern = Struct(
        "PointerId" / Int32ul,
        "FrameId" / Int32ul,
        "Message" / Int32ul
    )


@declare(guid=guid("5786e035-ef2d-4178-84f2-5a6bbedbb947"), event_id=67, version=0)
class Microsoft_Windows_DirectManipulation_67_0(Etw):
    pattern = Struct(
        "content" / Int64ul,
        "dimension" / Int32sl,
        "inertiaStartValue" / Float32l,
        "originalRestPoint" / Float32l,
        "outputRestPoint" / Float32l,
        "outputRestPointPriority" / Int32sl,
        "outputRestPointCurveId" / Int32sl
    )


@declare(guid=guid("5786e035-ef2d-4178-84f2-5a6bbedbb947"), event_id=68, version=0)
class Microsoft_Windows_DirectManipulation_68_0(Etw):
    pattern = Struct(
        "content" / Int64ul,
        "motionType" / Int32sl,
        "index" / Int32ul,
        "bIsNewSnapValues" / Int32sl,
        "newSnapPointValue" / Float32l
    )


@declare(guid=guid("5786e035-ef2d-4178-84f2-5a6bbedbb947"), event_id=69, version=0)
class Microsoft_Windows_DirectManipulation_69_0(Etw):
    pattern = Struct(
        "content" / Int64ul,
        "motionType" / Int32sl,
        "interval" / Float32l,
        "offset" / Float32l
    )


@declare(guid=guid("5786e035-ef2d-4178-84f2-5a6bbedbb947"), event_id=70, version=0)
class Microsoft_Windows_DirectManipulation_70_0(Etw):
    pattern = Struct(
        "content" / Int64ul,
        "restPointX" / Float32l,
        "restPointY" / Float32l,
        "restPointZ" / Float32l,
        "curveIdX" / Int32sl,
        "curveIdY" / Int32sl,
        "curveIdZ" / Int32sl
    )


@declare(guid=guid("5786e035-ef2d-4178-84f2-5a6bbedbb947"), event_id=71, version=0)
class Microsoft_Windows_DirectManipulation_71_0(Etw):
    pattern = Struct(
        "time" / Int64ul,
        "processTime" / Int64ul,
        "compositionTime" / Int64ul,
        "predictedTimeGap" / Int64ul,
        "predictionX" / Float32l,
        "predictionY" / Float32l
    )


@declare(guid=guid("5786e035-ef2d-4178-84f2-5a6bbedbb947"), event_id=72, version=0)
class Microsoft_Windows_DirectManipulation_72_0(Etw):
    pattern = Struct(
        "inertiaStartTime" / Int64ul,
        "time" / Int64ul,
        "processTime" / Int64ul,
        "compositionTime" / Int64ul,
        "timerElapsedTime" / Double,
        "timerOffset" / Double,
        "animationTime" / Double
    )


@declare(guid=guid("5786e035-ef2d-4178-84f2-5a6bbedbb947"), event_id=73, version=0)
class Microsoft_Windows_DirectManipulation_73_0(Etw):
    pattern = Struct(
        "content" / Int64ul,
        "targetMotionType" / Int32ul,
        "sourceMotionType" / Int32ul,
        "curveCount" / Int32ul
    )


@declare(guid=guid("5786e035-ef2d-4178-84f2-5a6bbedbb947"), event_id=74, version=0)
class Microsoft_Windows_DirectManipulation_74_0(Etw):
    pattern = Struct(
        "content" / Int64ul
    )


@declare(guid=guid("5786e035-ef2d-4178-84f2-5a6bbedbb947"), event_id=75, version=0)
class Microsoft_Windows_DirectManipulation_75_0(Etw):
    pattern = Struct(
        "content" / Int64ul,
        "inputScaleX" / Float32l,
        "inputScaleY" / Float32l,
        "inputTranslateX" / Float32l,
        "inputTranslateY" / Float32l
    )


@declare(guid=guid("5786e035-ef2d-4178-84f2-5a6bbedbb947"), event_id=76, version=0)
class Microsoft_Windows_DirectManipulation_76_0(Etw):
    pattern = Struct(
        "content" / Int64ul,
        "outputScaleX" / Float32l,
        "outputScaleY" / Float32l,
        "outputTranslateX" / Float32l,
        "outputTranslateY" / Float32l,
        "computedMotionTypes" / Int32ul
    )


@declare(guid=guid("5786e035-ef2d-4178-84f2-5a6bbedbb947"), event_id=77, version=0)
class Microsoft_Windows_DirectManipulation_77_0(Etw):
    pattern = Struct(
        "pNewValue" / Double,
        "pOldValue" / Double,
        "timeDeltaInMS" / Double
    )


@declare(guid=guid("5786e035-ef2d-4178-84f2-5a6bbedbb947"), event_id=78, version=0)
class Microsoft_Windows_DirectManipulation_78_0(Etw):
    pattern = Struct(
        "ViewportPointer" / Int64ul
    )


@declare(guid=guid("5786e035-ef2d-4178-84f2-5a6bbedbb947"), event_id=79, version=0)
class Microsoft_Windows_DirectManipulation_79_0(Etw):
    pattern = Struct(
        "ViewportPointer" / Int64ul
    )


@declare(guid=guid("5786e035-ef2d-4178-84f2-5a6bbedbb947"), event_id=80, version=0)
class Microsoft_Windows_DirectManipulation_80_0(Etw):
    pattern = Struct(
        "viewport" / Int64ul,
        "animate" / Int8ul
    )


@declare(guid=guid("5786e035-ef2d-4178-84f2-5a6bbedbb947"), event_id=81, version=0)
class Microsoft_Windows_DirectManipulation_81_0(Etw):
    pattern = Struct(
        "storyboard" / Int64ul,
        "content" / Int64ul,
        "status" / Int32ul
    )


@declare(guid=guid("5786e035-ef2d-4178-84f2-5a6bbedbb947"), event_id=82, version=0)
class Microsoft_Windows_DirectManipulation_82_0(Etw):
    pattern = Struct(
        "PointerId" / Int32ul,
        "ContactId" / Int32ul
    )


@declare(guid=guid("5786e035-ef2d-4178-84f2-5a6bbedbb947"), event_id=83, version=0)
class Microsoft_Windows_DirectManipulation_83_0(Etw):
    pattern = Struct(
        "PointerId" / Int32ul,
        "FrameId" / Int32ul,
        "Message" / Int32ul
    )


@declare(guid=guid("5786e035-ef2d-4178-84f2-5a6bbedbb947"), event_id=84, version=0)
class Microsoft_Windows_DirectManipulation_84_0(Etw):
    pattern = Struct(
        "UniqueKey" / Int64ul,
        "InertiaType" / Int32ul,
        "KernelInputReadTime" / Int64ul,
        "HostInputSendTime" / Int64ul,
        "ContainerInputReceiveTime" / Int64ul,
        "InteractionLibraryStartTime" / Int64ul,
        "CoalescedFrameCount" / Int32ul,
        "InputType" / Int32ul,
        "PointerCount" / Int16ul,
        "FrameId" / Int32ul,
        "ManipulationFrameId" / Int32ul,
        "ZoomToRectCount" / Int16ul,
        "Valid" / Int8ul,
        "InertiaZoom" / Int8ul
    )


@declare(guid=guid("5786e035-ef2d-4178-84f2-5a6bbedbb947"), event_id=85, version=0)
class Microsoft_Windows_DirectManipulation_85_0(Etw):
    pattern = Struct(
        "AppUserModeId" / WString,
        "AppType" / Int32ul,
        "InteractionLibraryType" / Int32ul,
        "UniqueKey" / Int64ul,
        "SurfaceWidth" / Int16ul,
        "SurfaceHeight" / Int16ul
    )


@declare(guid=guid("5786e035-ef2d-4178-84f2-5a6bbedbb947"), event_id=86, version=0)
class Microsoft_Windows_DirectManipulation_86_0(Etw):
    pattern = Struct(
        "UniqueKey" / Int64ul,
        "InputType" / Int32ul,
        "NumTouchPoints" / Int16ul,
        "ManipulationFrameId" / Int32ul,
        "FrameId" / Int32ul,
        "InteractionType" / Int32ul,
        "KernelInputStartTime" / Int64ul,
        "HostInputSendTime" / Int64ul,
        "ContainerInputReceiveTime" / Int64ul,
        "QpcInteractionLibraryStart" / Int64ul,
        "QpcInteractionLibraryStop" / Int64ul,
        "HostPerformanceFrequency" / Int64ul,
        "ZoomToRectCalls" / Int16ul,
        "CoalescedFrames" / Int32ul
    )


@declare(guid=guid("5786e035-ef2d-4178-84f2-5a6bbedbb947"), event_id=87, version=0)
class Microsoft_Windows_DirectManipulation_87_0(Etw):
    pattern = Struct(
        "UniqueKey" / Int64ul
    )


@declare(guid=guid("5786e035-ef2d-4178-84f2-5a6bbedbb947"), event_id=88, version=0)
class Microsoft_Windows_DirectManipulation_88_0(Etw):
    pattern = Struct(
        "InteractionLibraryStartTime" / Int64ul
    )


@declare(guid=guid("5786e035-ef2d-4178-84f2-5a6bbedbb947"), event_id=89, version=0)
class Microsoft_Windows_DirectManipulation_89_0(Etw):
    pattern = Struct(
        "Viewport" / Int64ul,
        "Interaction" / Int64ul
    )


@declare(guid=guid("5786e035-ef2d-4178-84f2-5a6bbedbb947"), event_id=90, version=0)
class Microsoft_Windows_DirectManipulation_90_0(Etw):
    pattern = Struct(
        "Viewport" / Int64ul,
        "Interaction" / Int64ul
    )

