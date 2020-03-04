# -*- coding: utf-8 -*-
"""
Microsoft-Windows-MediaEngine
GUID : 8f2048e0-f260-4f57-a8d1-932376291682
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=100, version=0)
class Microsoft_Windows_MediaEngine_100_0(Etw):
    pattern = Struct(
        "id" / Int32ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=101, version=0)
class Microsoft_Windows_MediaEngine_101_0(Etw):
    pattern = Struct(
        "id" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=102, version=0)
class Microsoft_Windows_MediaEngine_102_0(Etw):
    pattern = Struct(
        "id" / Int32ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=103, version=0)
class Microsoft_Windows_MediaEngine_103_0(Etw):
    pattern = Struct(
        "id" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=104, version=0)
class Microsoft_Windows_MediaEngine_104_0(Etw):
    pattern = Struct(
        "id" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=105, version=0)
class Microsoft_Windows_MediaEngine_105_0(Etw):
    pattern = Struct(
        "id" / Int32ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=106, version=0)
class Microsoft_Windows_MediaEngine_106_0(Etw):
    pattern = Struct(
        "id" / Int32ul,
        "rate" / Float32l
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=107, version=0)
class Microsoft_Windows_MediaEngine_107_0(Etw):
    pattern = Struct(
        "id" / Int32ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=108, version=0)
class Microsoft_Windows_MediaEngine_108_0(Etw):
    pattern = Struct(
        "id" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=109, version=0)
class Microsoft_Windows_MediaEngine_109_0(Etw):
    pattern = Struct(
        "id" / Int32ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=110, version=0)
class Microsoft_Windows_MediaEngine_110_0(Etw):
    pattern = Struct(
        "id" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=111, version=0)
class Microsoft_Windows_MediaEngine_111_0(Etw):
    pattern = Struct(
        "id" / Int32ul,
        "rate" / Float32l
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=112, version=0)
class Microsoft_Windows_MediaEngine_112_0(Etw):
    pattern = Struct(
        "id" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=113, version=0)
class Microsoft_Windows_MediaEngine_113_0(Etw):
    pattern = Struct(
        "id" / Int32ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=114, version=0)
class Microsoft_Windows_MediaEngine_114_0(Etw):
    pattern = Struct(
        "id" / Int32ul,
        "location" / Int32ul,
        "pts" / Int64sl,
        "clock" / Int64sl
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=115, version=0)
class Microsoft_Windows_MediaEngine_115_0(Etw):
    pattern = Struct(
        "id" / Int32ul,
        "pts" / Int64sl,
        "clock" / Int64sl
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=116, version=0)
class Microsoft_Windows_MediaEngine_116_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "sampleTime" / Int64sl,
        "QPC" / Int64sl,
        "Ahead" / Int64sl
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=117, version=0)
class Microsoft_Windows_MediaEngine_117_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "sampleTime" / Int64sl,
        "QPC" / Int64sl,
        "QPC_snapped" / Int64sl,
        "PresentFlags" / Int32ul,
        "SyncInterval" / Int32ul,
        "Repeat" / Int32ul,
        "Restart" / Int32ul,
        "Now" / Int64sl,
        "DeltaToTarget_MS" / Int32sl,
        "PresentCount" / Int32ul,
        "FrameCount" / Int32ul,
        "History_QueuedFrames" / Int32ul,
        "History_QueuedFramesWithRepeats" / Int32ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=118, version=0)
class Microsoft_Windows_MediaEngine_118_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "sampleTime" / Int64sl,
        "QPC_target" / Int64sl,
        "QPC_actual" / Int64sl,
        "QPC_actual_behind" / Int64sl,
        "FramePeriod" / Int64sl,
        "FrameAdjustment" / Int32sl,
        "PresentCount" / Int32sl,
        "FrameCount" / Int32sl,
        "RatioAverage" / Float32l
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=119, version=0)
class Microsoft_Windows_MediaEngine_119_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "sampleTime" / Int64sl,
        "FramesLate" / Int32sl
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=120, version=0)
class Microsoft_Windows_MediaEngine_120_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=121, version=0)
class Microsoft_Windows_MediaEngine_121_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "protected" / Int32ul,
        "width" / Int32ul,
        "height" / Int32ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=123, version=0)
class Microsoft_Windows_MediaEngine_123_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "protected" / Int32ul,
        "width" / Int32ul,
        "height" / Int32ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=125, version=0)
class Microsoft_Windows_MediaEngine_125_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "protected" / Int32ul,
        "width" / Int32ul,
        "height" / Int32ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=127, version=0)
class Microsoft_Windows_MediaEngine_127_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "Length" / Int32ul,
        "MaxPresentLatency" / Int32ul,
        "Queued" / Int32ul,
        "QueuedWithRepeats" / Int32ul,
        "EstimatedFramesNeeded" / Int32ul,
        "Free" / Int32ul,
        "DeltaToTarget" / Int64sl,
        "SubmittedAheadDelta" / Int64sl,
        "TimeInQueue" / Int64sl,
        "MinLatency" / Int64sl,
        "MaxLatency" / Int32sl,
        "FramePeriod" / Int64sl,
        "sampleTime" / Int64sl,
        "TargetQPC" / Int64sl,
        "HistoryPresents" / Int32sl,
        "TimeToDeadline" / Int64sl,
        "BufferIndex" / Int32ul,
        "StateFlags" / Int32ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=128, version=0)
class Microsoft_Windows_MediaEngine_128_0(Etw):
    pattern = Struct(
        "id" / Int32ul,
        "paused" / Int8ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=129, version=0)
class Microsoft_Windows_MediaEngine_129_0(Etw):
    pattern = Struct(
        "id" / Int32ul,
        "resumed" / Int8ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=130, version=0)
class Microsoft_Windows_MediaEngine_130_0(Etw):
    pattern = Struct(
        "id" / Int32ul,
        "thinning" / Int8ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=131, version=0)
class Microsoft_Windows_MediaEngine_131_0(Etw):
    pattern = Struct(
        "id" / Int32ul,
        "thinning" / Int8ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=132, version=0)
class Microsoft_Windows_MediaEngine_132_0(Etw):
    pattern = Struct(
        "id" / Int32ul,
        "resumed" / Int8ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=133, version=0)
class Microsoft_Windows_MediaEngine_133_0(Etw):
    pattern = Struct(
        "id" / Int32ul,
        "priority" / Int32sl
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=134, version=0)
class Microsoft_Windows_MediaEngine_134_0(Etw):
    pattern = Struct(
        "NumGlitches" / Int32ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=135, version=0)
class Microsoft_Windows_MediaEngine_135_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=136, version=0)
class Microsoft_Windows_MediaEngine_136_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "NativeWidth" / Int32ul,
        "NativeHeight" / Int32ul,
        "EncodedWidth" / Int32ul,
        "EncodedHeight" / Int32ul,
        "EncodedSize" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=137, version=0)
class Microsoft_Windows_MediaEngine_137_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=138, version=0)
class Microsoft_Windows_MediaEngine_138_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=139, version=0)
class Microsoft_Windows_MediaEngine_139_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "sampleTime" / Int64sl,
        "FramesEarly" / Int32sl
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=140, version=3)
class Microsoft_Windows_MediaEngine_140_3(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "QPC_Prev" / Int64sl,
        "Delta_us" / Int64sl,
        "Delta_Frames" / Int32sl,
        "DeltaPerFrame_us" / Int64sl,
        "RatioToPrimary" / Float32l,
        "InputFrameIndex" / Int32sl,
        "FrameIndex" / Int32sl,
        "PreviousFramerate" / Float32l,
        "Framerate" / Float32l,
        "MinFramerate" / Float32l,
        "MaxFramerate" / Float32l,
        "QPC_Actual" / Int64sl,
        "QPC_Smoothed" / Int64sl,
        "QPC_SmoothedNonQuant" / Int64sl,
        "Accepted" / Int8ul,
        "IsIFlip" / Int8ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=141, version=0)
class Microsoft_Windows_MediaEngine_141_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=142, version=0)
class Microsoft_Windows_MediaEngine_142_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "QPC" / Int64sl,
        "Delta" / Int64sl,
        "Frames" / Int32sl
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=143, version=0)
class Microsoft_Windows_MediaEngine_143_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "Requested" / Int8ul,
        "ReferenceCounter" / Int32ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=144, version=0)
class Microsoft_Windows_MediaEngine_144_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=145, version=0)
class Microsoft_Windows_MediaEngine_145_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=146, version=0)
class Microsoft_Windows_MediaEngine_146_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "Swapchain" / Int64ul,
        "TextureArray" / Int64ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=147, version=0)
class Microsoft_Windows_MediaEngine_147_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "Swapchain" / Int64ul,
        "SrcRect_Left" / Int32sl,
        "SrcRect_Top" / Int32sl,
        "SrcRect_Right" / Int32sl,
        "SrcRect_Bottom" / Int32sl,
        "DstRect_Left" / Int32sl,
        "DstRect_Top" / Int32sl,
        "DstRect_Right" / Int32sl,
        "DstRect_Bottom" / Int32sl,
        "DstSize_Width" / Int32sl,
        "DstRect_Height" / Int32sl
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=148, version=0)
class Microsoft_Windows_MediaEngine_148_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "Swapchain" / Int64ul,
        "SwapchainState" / Int32ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=149, version=0)
class Microsoft_Windows_MediaEngine_149_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "SwapchainState" / Int32ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=151, version=0)
class Microsoft_Windows_MediaEngine_151_0(Etw):
    pattern = Struct(
        "id" / Int32ul,
        "rate" / Float32l
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=152, version=0)
class Microsoft_Windows_MediaEngine_152_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "NumGlitches" / Int32ul,
        "SampleTime" / Int64sl,
        "GlitchDuration" / Int64sl
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=153, version=0)
class Microsoft_Windows_MediaEngine_153_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "FrameDuration" / Int64ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=154, version=0)
class Microsoft_Windows_MediaEngine_154_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "FrameDuration" / Int64ul,
        "RefreshDuration" / Int64ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=155, version=0)
class Microsoft_Windows_MediaEngine_155_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "RequestedRefreshDuration" / Int64ul,
        "ActualRefreshDuration" / Int64ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=156, version=0)
class Microsoft_Windows_MediaEngine_156_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "State" / Int32ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=157, version=0)
class Microsoft_Windows_MediaEngine_157_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "State" / Int32ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=158, version=0)
class Microsoft_Windows_MediaEngine_158_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "Dst_left" / Int32sl,
        "Dst_top" / Int32sl,
        "Dst_right" / Int32sl,
        "Dst_bottom" / Int32sl,
        "Src_left" / Float32l,
        "Src_top" / Float32l,
        "Src_right" / Float32l,
        "Src_bottom" / Float32l,
        "flags" / Int32sl
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=159, version=1)
class Microsoft_Windows_MediaEngine_159_1(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "Swapchain" / Int64ul,
        "Format" / Int32ul,
        "Width" / Int32ul,
        "Height" / Int32ul,
        "Backbuffers" / Int32ul,
        "Flags" / Int32ul,
        "ColorSpaceType" / Int32ul,
        "SwapChainType" / Int32ul,
        "SwapChainRotation" / Int32ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=160, version=0)
class Microsoft_Windows_MediaEngine_160_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "Sample" / Int64ul,
        "TimeStamp" / Int64sl,
        "Duration" / Int64sl,
        "FirstFrameReady" / Int32sl,
        "Dropped" / Int32sl
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=161, version=0)
class Microsoft_Windows_MediaEngine_161_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "Count" / Int32sl
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=162, version=0)
class Microsoft_Windows_MediaEngine_162_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "Count" / Int32sl
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=163, version=0)
class Microsoft_Windows_MediaEngine_163_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=164, version=0)
class Microsoft_Windows_MediaEngine_164_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=165, version=0)
class Microsoft_Windows_MediaEngine_165_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hr" / Int32ul,
        "PresentCount" / Int32sl,
        "PresentRefreshCount" / Int32sl,
        "SyncRefreshCount" / Int32sl,
        "SyncQPC_us" / Int64ul,
        "CompMode" / Int32sl,
        "Duration" / Int32sl
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=166, version=0)
class Microsoft_Windows_MediaEngine_166_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "PresentCount" / Int32sl
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=167, version=1)
class Microsoft_Windows_MediaEngine_167_1(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "FrameRate" / Float32l,
        "minFrameRate" / Float32l,
        "maxFrameRate" / Float32l,
        "Ratio" / Int32sl,
        "MaxRatio" / Int32sl,
        "Reason" / Int32sl
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=168, version=0)
class Microsoft_Windows_MediaEngine_168_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "ClockTime0_us" / Int64sl,
        "QPC0_us" / Int64sl,
        "SmoothedQPC0_us" / Int64sl,
        "QPCDelta_us" / Int64sl,
        "WindowCount" / Int32sl,
        "WindowWidth_us" / Int64sl,
        "Accepted" / Int8ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=169, version=1)
class Microsoft_Windows_MediaEngine_169_1(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "sampleTime_us" / Int64sl,
        "OrigTargetQPC_us" / Int64sl,
        "TargetQPC_us" / Int64sl,
        "DeltaQPC_us" / Int64sl,
        "framePeriod_us" / Int64sl
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=170, version=0)
class Microsoft_Windows_MediaEngine_170_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "newState" / Int32sl,
        "oldState" / Int32sl
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=171, version=0)
class Microsoft_Windows_MediaEngine_171_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "QPCnow_us" / Int64sl,
        "rate" / Float32l,
        "ClockTime0_us" / Int64sl,
        "QPC0_us" / Int64sl,
        "SampleTime_us" / Int64sl,
        "SampleQPC_us" / Int64sl,
        "SampleQPCAhead_us" / Int64sl,
        "Dejitter" / Int8ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=172, version=0)
class Microsoft_Windows_MediaEngine_172_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "QPCnow_us" / Int64sl,
        "ClockTime0_us" / Int64sl,
        "QPC0_us" / Int64sl,
        "ApproxClockJitter_us" / Int64sl
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=173, version=2)
class Microsoft_Windows_MediaEngine_173_2(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "SampleTime" / Int64sl,
        "LastQueuedStartQPC" / Int64sl,
        "TargetQPC" / Int64sl,
        "nowQPC" / Int64sl,
        "AheadQPC" / Int64sl,
        "RepeatCount_Rounded" / Int32sl,
        "RepeatCount_x1000" / Int32sl,
        "TimeUntilFrame_Orig" / Int64sl,
        "TimeUntilFrame_postRepeat" / Int64sl,
        "FramesBehindAdjustment" / Int32sl,
        "PresentCount" / Int32ul,
        "FrameCount" / Int32ul,
        "PrimaryFramePeriod" / Int64sl,
        "FramePeriod" / Int64sl
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=174, version=0)
class Microsoft_Windows_MediaEngine_174_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "QPCtarget_us" / Int64sl,
        "Delta_us" / Int64sl,
        "AverageLateness_us" / Int64sl
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=175, version=0)
class Microsoft_Windows_MediaEngine_175_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "TimeRemaining" / Int64sl
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=176, version=0)
class Microsoft_Windows_MediaEngine_176_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "old" / Int32sl,
        "new" / Int32sl,
        "hr" / Int32ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=177, version=0)
class Microsoft_Windows_MediaEngine_177_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "deadline" / Int64sl,
        "hnsDeltaFromNow" / Int64sl
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=178, version=0)
class Microsoft_Windows_MediaEngine_178_0(Etw):
    pattern = Struct(
        "id" / Int32ul,
        "Type" / Int32ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=179, version=0)
class Microsoft_Windows_MediaEngine_179_0(Etw):
    pattern = Struct(
        "id" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=180, version=0)
class Microsoft_Windows_MediaEngine_180_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "RequestsPending" / Int32ul,
        "FrameQueueCount" / Int32ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=181, version=0)
class Microsoft_Windows_MediaEngine_181_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "TimeToDeadline_us" / Int64sl
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=182, version=0)
class Microsoft_Windows_MediaEngine_182_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "pRecord" / Int64ul,
        "ListCount" / Int32sl,
        "DecodeYUV" / Int8ul,
        "FrameCount" / Int32sl,
        "PresentCount" / Int64sl,
        "Repeat" / Int8ul,
        "SampleTime" / Int64ul,
        "TargetQPC" / Int64ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=183, version=0)
class Microsoft_Windows_MediaEngine_183_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "pRecord" / Int64ul,
        "PresentCount" / Int64sl,
        "ListCount" / Int32sl
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=184, version=0)
class Microsoft_Windows_MediaEngine_184_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "ListCount" / Int32sl,
        "Location" / Int32sl
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=185, version=0)
class Microsoft_Windows_MediaEngine_185_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=186, version=0)
class Microsoft_Windows_MediaEngine_186_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "now" / Int64sl
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=187, version=0)
class Microsoft_Windows_MediaEngine_187_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "DXObject" / Int64ul,
        "DXType" / Int32ul,
        "deadline" / Int64sl,
        "hnsDeltaFromNow" / Int64sl
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=188, version=0)
class Microsoft_Windows_MediaEngine_188_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "Ratio" / Float32l,
        "Ratio_x100" / Float32l
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=189, version=0)
class Microsoft_Windows_MediaEngine_189_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "Ratio" / Float32l
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=200, version=0)
class Microsoft_Windows_MediaEngine_200_0(Etw):
    pattern = Struct(
        "length" / Int32ul,
        "data" / Bytes(lambda this: this.length)
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=201, version=0)
class Microsoft_Windows_MediaEngine_201_0(Etw):
    pattern = Struct(
        "keysystem" / WString,
        "defaultCdmStorePath" / WString,
        "inprivateCdmStorePath" / WString,
        "object" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=202, version=0)
class Microsoft_Windows_MediaEngine_202_0(Etw):
    pattern = Struct(
        "sessionId" / WString,
        "keySystem" / WString,
        "type" / WString,
        "length" / Int32ul,
        "data" / Bytes(lambda this: this.length),
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=203, version=0)
class Microsoft_Windows_MediaEngine_203_0(Etw):
    pattern = Struct(
        "sessionId" / WString
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=204, version=0)
class Microsoft_Windows_MediaEngine_204_0(Etw):
    pattern = Struct(
        "sessionId" / WString,
        "url" / WString,
        "length" / Int32ul,
        "data" / Bytes(lambda this: this.length)
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=205, version=0)
class Microsoft_Windows_MediaEngine_205_0(Etw):
    pattern = Struct(
        "sessionId" / WString,
        "code" / Int16ul,
        "systemError" / Int32ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=206, version=0)
class Microsoft_Windows_MediaEngine_206_0(Etw):
    pattern = Struct(
        "sessionId" / WString
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=207, version=0)
class Microsoft_Windows_MediaEngine_207_0(Etw):
    pattern = Struct(
        "sessionId" / WString,
        "length" / Int32ul,
        "data" / Bytes(lambda this: this.length),
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=208, version=0)
class Microsoft_Windows_MediaEngine_208_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=209, version=0)
class Microsoft_Windows_MediaEngine_209_0(Etw):
    pattern = Struct(
        "enabletype" / Guid,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=210, version=0)
class Microsoft_Windows_MediaEngine_210_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=212, version=1)
class Microsoft_Windows_MediaEngine_212_1(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "Ok" / Int8ul,
        "Bits" / Int32sl,
        "FullScreenPercent" / Int32sl,
        "FullScreenThreshold" / Int32sl,
        "Format" / Int32ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=213, version=0)
class Microsoft_Windows_MediaEngine_213_0(Etw):
    pattern = Struct(
        "buffer" / Int64ul,
        "sampleTime" / Int64sl,
        "sampleDuration" / Int64sl
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=214, version=0)
class Microsoft_Windows_MediaEngine_214_0(Etw):
    pattern = Struct(
        "id" / Int32ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=215, version=0)
class Microsoft_Windows_MediaEngine_215_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=216, version=0)
class Microsoft_Windows_MediaEngine_216_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Period" / Int32sl
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=217, version=0)
class Microsoft_Windows_MediaEngine_217_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Period" / Int32sl
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=218, version=0)
class Microsoft_Windows_MediaEngine_218_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "TimeDelta" / Int64sl
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=219, version=0)
class Microsoft_Windows_MediaEngine_219_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "TimeDelta" / Int64sl
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=220, version=0)
class Microsoft_Windows_MediaEngine_220_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "SampleStartTime" / Int64sl,
        "SampleEndTime" / Int64sl
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=221, version=0)
class Microsoft_Windows_MediaEngine_221_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "CueStartTime" / Int64sl,
        "CueEndTime" / Int64sl,
        "CueTicket" / Int64sl
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=222, version=0)
class Microsoft_Windows_MediaEngine_222_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "SampleStartTime" / Int64sl,
        "SampleEndTime" / Int64sl
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=223, version=0)
class Microsoft_Windows_MediaEngine_223_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "SampleStartTime" / Int64sl,
        "SampleEndTime" / Int64sl
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=236, version=0)
class Microsoft_Windows_MediaEngine_236_0(Etw):
    pattern = Struct(
        "Width" / Int32ul,
        "Height" / Int32ul,
        "Backbuffers" / Int32ul,
        "Format" / Int32ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=237, version=0)
class Microsoft_Windows_MediaEngine_237_0(Etw):
    pattern = Struct(
        "sessionId" / WString
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=238, version=0)
class Microsoft_Windows_MediaEngine_238_0(Etw):
    pattern = Struct(
        "sessionId" / WString,
        "keySystem" / WString,
        "length" / Int32ul,
        "data" / Bytes(lambda this: this.length)
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=239, version=0)
class Microsoft_Windows_MediaEngine_239_0(Etw):
    pattern = Struct(
        "sessionId" / WString
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=240, version=0)
class Microsoft_Windows_MediaEngine_240_0(Etw):
    pattern = Struct(
        "length" / Int32ul,
        "data" / Bytes(lambda this: this.length)
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=241, version=0)
class Microsoft_Windows_MediaEngine_241_0(Etw):
    pattern = Struct(
        "SessionType" / Int32ul,
        "keySystem" / WString,
        "UseDistinctiveIdentifier" / Int32ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=242, version=0)
class Microsoft_Windows_MediaEngine_242_0(Etw):
    pattern = Struct(
        "sessionId" / WString,
        "MessageType" / Int32ul,
        "url" / WString,
        "length" / Int32ul,
        "data" / Bytes(lambda this: this.length)
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=243, version=0)
class Microsoft_Windows_MediaEngine_243_0(Etw):
    pattern = Struct(
        "sessionId" / WString
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=244, version=0)
class Microsoft_Windows_MediaEngine_244_0(Etw):
    pattern = Struct(
        "length" / Int32ul,
        "data" / Bytes(lambda this: this.length)
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=245, version=0)
class Microsoft_Windows_MediaEngine_245_0(Etw):
    pattern = Struct(
        "keysystem" / WString,
        "CDMAccess" / Int64ul,
        "CDMCustomConfig" / Int64ul,
        "MediaKeysObject" / Int64ul,
        "SoftwareOverride" / Int32ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=246, version=0)
class Microsoft_Windows_MediaEngine_246_0(Etw):
    pattern = Struct(
        "keysystem" / WString,
        "configCount" / Int32ul,
        "selectedConfigCount" / Int32ul,
        "object" / Int64ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=247, version=0)
class Microsoft_Windows_MediaEngine_247_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "PresentCount" / Int32ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=248, version=0)
class Microsoft_Windows_MediaEngine_248_0(Etw):
    pattern = Struct(
        "Rotation" / Int32ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=249, version=0)
class Microsoft_Windows_MediaEngine_249_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "DecodeSwapchainState" / Int32ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=250, version=0)
class Microsoft_Windows_MediaEngine_250_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "IsDecode" / Int8ul,
        "DxgiFormat" / Int32ul,
        "Width" / Int32ul,
        "Height" / Int32ul,
        "ColorSpaceType" / Int32ul,
        "BufferCount" / Int32ul,
        "Flags" / Int32ul,
        "Dst_Left" / Int32sl,
        "Dst_Top" / Int32sl,
        "Dst_Right" / Int32sl,
        "Dst_Bottom" / Int32sl
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=251, version=0)
class Microsoft_Windows_MediaEngine_251_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=252, version=0)
class Microsoft_Windows_MediaEngine_252_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=253, version=0)
class Microsoft_Windows_MediaEngine_253_0(Etw):
    pattern = Struct(
        "ScrubbingState" / Int32ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=254, version=0)
class Microsoft_Windows_MediaEngine_254_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Index" / Int32ul,
        "Inverval" / Int32ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=255, version=0)
class Microsoft_Windows_MediaEngine_255_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Index" / Int32ul,
        "hrResult" / Int32ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=256, version=0)
class Microsoft_Windows_MediaEngine_256_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=257, version=0)
class Microsoft_Windows_MediaEngine_257_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=258, version=0)
class Microsoft_Windows_MediaEngine_258_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=259, version=0)
class Microsoft_Windows_MediaEngine_259_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=260, version=0)
class Microsoft_Windows_MediaEngine_260_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=261, version=0)
class Microsoft_Windows_MediaEngine_261_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=262, version=0)
class Microsoft_Windows_MediaEngine_262_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Sample" / Int64ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=263, version=0)
class Microsoft_Windows_MediaEngine_263_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Sample" / Int64ul,
        "hrResult" / Int32ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=264, version=0)
class Microsoft_Windows_MediaEngine_264_0(Etw):
    pattern = Struct(
        "IsEnabled" / Int8ul,
        "Format" / Int32ul,
        "ProjectionMode" / Int32ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=265, version=0)
class Microsoft_Windows_MediaEngine_265_0(Etw):
    pattern = Struct(
        "QuaternionW" / Float32l,
        "QuaternionX" / Float32l,
        "QuaternionY" / Float32l,
        "QuaternionZ" / Float32l,
        "FieldOfView" / Int32ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=266, version=0)
class Microsoft_Windows_MediaEngine_266_0(Etw):
    pattern = Struct(
        "Present" / Int8ul,
        "DcValue" / Int32ul,
        "Provisioned" / Int8ul,
        "Memory" / Int64sl
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=267, version=0)
class Microsoft_Windows_MediaEngine_267_0(Etw):
    pattern = Struct(
        "IsDisplayMetadata" / Int8ul,
        "MinLuminance" / Int32ul,
        "MaxLuminance" / Int32ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=268, version=0)
class Microsoft_Windows_MediaEngine_268_0(Etw):
    pattern = Struct(
        "Enabled" / Int8ul,
        "IsAC" / Int8ul,
        "IsMediaOptimizedForDisplayQuality" / Int8ul,
        "IsLowerScreenBrightnessActive" / Int8ul,
        "IsBrightnessPolicyActive" / Int8ul,
        "ContentMaxLuminance" / Int32ul,
        "DisplayMaxLuminance" / Int32ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=269, version=0)
class Microsoft_Windows_MediaEngine_269_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=270, version=0)
class Microsoft_Windows_MediaEngine_270_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=271, version=0)
class Microsoft_Windows_MediaEngine_271_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=272, version=0)
class Microsoft_Windows_MediaEngine_272_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=273, version=0)
class Microsoft_Windows_MediaEngine_273_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=274, version=0)
class Microsoft_Windows_MediaEngine_274_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=275, version=0)
class Microsoft_Windows_MediaEngine_275_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=276, version=0)
class Microsoft_Windows_MediaEngine_276_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=277, version=0)
class Microsoft_Windows_MediaEngine_277_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=278, version=0)
class Microsoft_Windows_MediaEngine_278_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "Delay" / Int32ul,
        "TimeToDeadline" / Int64sl,
        "Location" / Int32ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=279, version=0)
class Microsoft_Windows_MediaEngine_279_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=280, version=0)
class Microsoft_Windows_MediaEngine_280_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=281, version=0)
class Microsoft_Windows_MediaEngine_281_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "CallId" / Int32ul,
        "Id" / Int32ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=282, version=0)
class Microsoft_Windows_MediaEngine_282_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "CallId" / Int32ul,
        "Id" / Int32ul,
        "hrResult" / Int32ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=283, version=0)
class Microsoft_Windows_MediaEngine_283_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "CallId" / Int32ul,
        "Id" / Int32ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=284, version=0)
class Microsoft_Windows_MediaEngine_284_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "CallId" / Int32ul,
        "Id" / Int32ul,
        "hrResult" / Int32ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=285, version=0)
class Microsoft_Windows_MediaEngine_285_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "CallId" / Int32ul,
        "Id" / Int32ul,
        "Start" / Int64ul,
        "Now" / Int64ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=286, version=0)
class Microsoft_Windows_MediaEngine_286_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("8f2048e0-f260-4f57-a8d1-932376291682"), event_id=287, version=0)
class Microsoft_Windows_MediaEngine_287_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "Timestamp" / Int64sl
    )

