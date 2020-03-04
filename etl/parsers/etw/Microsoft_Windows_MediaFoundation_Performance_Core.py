# -*- coding: utf-8 -*-
"""
Microsoft-Windows-MediaFoundation-Performance-Core
GUID : b20e65ac-c905-4014-8f78-1b6a508142eb
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=1, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_1_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "WorkQueueId" / Int64ul,
        "IsMultithread" / Int8ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=2, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_2_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "m_u32StreamingPeriodMS" / Int32ul,
        "m_u32RenderBufferSizeInFrames" / Int32ul,
        "m_ui64ClockTicksPerSecond" / Int64ul,
        "m_u32AudioClientType" / Int32ul,
        "IsEventDriven" / Int8ul,
        "FillSilenceWhenStarving" / Int8ul,
        "FillCompressedSilenceWhenStarving" / Int8ul,
        "DropLateData" / Int8ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=3, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_3_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=4, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_4_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=5, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_5_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=6, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_6_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=7, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_7_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=8, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_8_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=9, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_9_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "SystemTime" / Int64sl,
        "mfsState" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=10, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_10_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=11, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_11_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=12, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_12_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32ul,
        "pullPlayPosition" / Int64sl,
        "pullRawPlayPosition" / Int64sl,
        "pullRawWritePosition" / Int64sl,
        "pullDevicePosition" / Int64sl,
        "phnsCorrelatedTime" / Int64sl
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=13, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_13_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "dwBytesWanted" / Int32ul,
        "u32FramesToRender" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=14, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_14_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=15, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_15_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "dwBytesWanted" / Int32ul,
        "m_bEOSReceived" / Int8ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=16, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_16_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "dwBytesWanted" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=17, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_17_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "ullEOSPosition" / Int64sl,
        "m_bIsEventDriven" / Int8ul,
        "IsOffloadedStream" / Int8ul,
        "IsOffloadedCompressedStream" / Int8ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=18, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_18_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=19, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_19_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=20, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_20_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=21, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_21_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=22, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_22_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=23, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_23_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "bFirstFill" / Int8ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=24, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_24_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "u32CurrentPadding" / Int32ul,
        "u32FramesToRender" / Int32ul,
        "u32TimeLeft" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=25, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_25_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "FrameCount" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=26, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_26_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "BytesInUse" / Int32ul,
        "dwBytesWanted" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=27, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_27_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "dwBytesStillWanted" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=28, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_28_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=29, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_29_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "bEOS" / Int8ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=30, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_30_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=31, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_31_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hr" / Int32sl,
        "fInserted" / Int8ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=32, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_32_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "fFlushed" / Int8ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=33, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_33_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "bEngineStarted" / Int8ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=34, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_34_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=35, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_35_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "bReset" / Int8ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=36, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_36_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=37, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_37_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=38, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_38_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=39, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_39_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "bEngineStarted" / Int8ul,
        "bIsEventDriven" / Int8ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=40, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_40_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=41, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_41_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=42, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_42_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=43, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_43_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=44, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_44_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=45, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_45_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=46, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_46_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=47, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_47_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=48, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_48_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "fFillBuffer" / Int8ul,
        "bIsEventDriven" / Int8ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=49, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_49_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=50, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_50_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=51, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_51_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=52, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_52_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "DisconnectReason" / Int32ul,
        "bReacquire" / Int8ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=53, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_53_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "dwFlags" / Int32ul,
        "ui32EndpointRole" / Int32ul,
        "eCategory" / Int32ul,
        "bIsLowLatency" / Int8ul,
        "bBufferDurationSpecified" / Int8ul,
        "hnsBufferDuration" / Int64sl,
        "bOnlyAudio" / Int8ul,
        "bDisableOffload" / Int8ul,
        "bNonSeekableStream" / Int8ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=54, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_54_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=55, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_55_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=56, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_56_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=57, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_57_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=58, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_58_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hnsSampleTime" / Int64sl,
        "hnsSampleDuration" / Int64sl
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=59, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_59_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=60, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_60_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "mfRenderTime" / Int64sl,
        "fDiscontinuity" / Int8ul,
        "mfAudioState" / Int32ul,
        "IsRateZero" / Int8ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=61, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_61_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hnsSampleTime" / Int64sl,
        "hnsSampleDuration" / Int64sl,
        "bPrerollSample" / Int8ul,
        "bDelayedSample" / Int8ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=62, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_62_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "scenario" / Int32ul,
        "fSignalPrerolled" / Int8ul,
        "m_cSamplesPrerolled" / Int32ul,
        "m_hnsPrerollDuration" / Int64sl,
        "m_u32CurrentPrerolledBytes" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=63, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_63_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hnsSampleDuration" / Int64sl,
        "m_hnsShortSampleTolerance" / Int64sl,
        "m_cMaxPendingRequestSample" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=64, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_64_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=65, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_65_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "MarkerType" / Int32sl
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=66, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_66_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "ControlPoint" / Int32sl,
        "Type" / Int32sl,
        "Value" / Int64sl
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=67, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_67_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=68, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_68_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "bFlushPreroll" / Int32sl
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=69, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_69_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32sl,
        "fDiscontinuity" / Int8ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=70, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_70_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=71, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_71_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=72, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_72_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=73, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_73_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=74, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_74_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=75, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_75_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=76, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_76_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=77, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_77_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=78, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_78_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=79, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_79_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "IsUninitialized" / Int8ul,
        "bInvalidatingStream" / Int8ul,
        "mfaOriginalState" / Int32sl
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=80, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_80_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=81, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_81_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=82, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_82_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32sl,
        "phnsTimeNow" / Int64sl,
        "phnsCorrelatedTime" / Int64sl
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=83, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_83_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=84, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_84_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "phnsTimeNow" / Int64sl,
        "m_mftMaxTimePriorToStreamSwitch" / Int64sl
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=85, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_85_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "phnsTimeNow" / Int64sl,
        "phnsCorrelatedTime" / Int64sl,
        "m_bInvalidatingStream" / Int8ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=86, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_86_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=87, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_87_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hnsSystemTime" / Int64sl,
        "llClockStartOffset" / Int64sl
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=88, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_88_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=89, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_89_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=90, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_90_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=91, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_91_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "StartOffset" / Int64sl,
        "mftStartOffset" / Int64sl,
        "bResetGapAndStallHandling" / Int8ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=92, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_92_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32sl,
        "StartOffset" / Int64sl
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=93, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_93_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=94, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_94_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=95, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_95_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hnsSystemTime" / Int64sl
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=96, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_96_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=97, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_97_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hnsSystemTime" / Int64sl
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=98, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_98_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=99, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_99_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hnsSystemTime" / Int64sl,
        "IsRateZero" / Int8ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=100, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_100_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=101, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_101_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=102, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_102_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=103, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_103_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "dwFlags" / Int32sl,
        "bUseResampler" / Int8ul,
        "bClockRateMatchEnabled" / Int8ul,
        "bUseLightWeightConverters" / Int8ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=104, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_104_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32sl,
        "m_bIsOffloadStream" / Int8ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=105, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_105_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=106, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_106_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32sl,
        "pullBytePosition" / Int64sl,
        "phnsCorrelatedTime" / Int64sl,
        "m_bIsCompressedStream" / Int8ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=107, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_107_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "dwSamples" / Int32sl
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=108, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_108_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=109, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_109_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "MarkerType" / Int32sl
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=110, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_110_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=111, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_111_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=112, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_112_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=113, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_113_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=114, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_114_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=115, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_115_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=116, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_116_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=117, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_117_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=118, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_118_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=119, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_119_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=120, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_120_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "mfRenderTime" / Int64sl
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=121, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_121_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32sl,
        "pfDiscontinuity" / Int8ul,
        "pullRenderBytePosition" / Int64sl,
        "pdwBytesToStall" / Int32sl
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=122, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_122_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "pfDiscontinuity" / Int8ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=123, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_123_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32sl,
        "pullRenderBytePosition" / Int64sl
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=124, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_124_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=125, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_125_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=126, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_126_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "bConvertToMFPos" / Int8ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=127, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_127_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32sl,
        "pullPlayPosition" / Int64sl,
        "pullWritePosition" / Int64sl,
        "pullDevicePlayPosition" / Int64sl,
        "phnsCorrelatedTime" / Int64sl
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=128, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_128_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "mftTrimAmount" / Int64sl,
        "mftCutoff" / Int64sl,
        "bTrimFromFront" / Int8ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=129, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_129_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=130, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_130_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "bEnable" / Int8ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=131, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_131_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "cPendingRequestSample" / Int32sl,
        "cMaxPendingRequestSample" / Int32sl
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=132, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_132_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "cPendingRequestSample" / Int32sl,
        "cMaxPendingRequestSample" / Int32sl
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=133, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_133_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "cPendingRequestSample" / Int32sl,
        "cMaxPendingRequestSample" / Int32sl
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=134, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_134_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "cPendingRequestSample" / Int32sl,
        "cMaxPendingRequestSample" / Int32sl
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=135, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_135_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "cMaxPendingRequestSample" / Int32sl,
        "NumContainers" / Int32sl,
        "BytesInUse" / Int32sl
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=136, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_136_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "MaxPendingRequestSample" / Int32sl,
        "NumContainers" / Int32sl,
        "DurationInUse" / Int64sl,
        "hnsMinAllocation" / Int64sl
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=137, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_137_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "cMaxPendingRequestSample" / Int32sl,
        "NumContainers" / Int32sl
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=138, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_138_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=139, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_139_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=140, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_140_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=141, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_141_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=142, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_142_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=143, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_143_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "TimeOutinMm" / Int32sl
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=144, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_144_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=145, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_145_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=146, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_146_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=147, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_147_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "bNeedFormatNegotiation" / Int8ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=148, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_148_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "mfaOriginalStreamState" / Int32sl
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=149, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_149_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=150, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_150_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=151, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_151_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hnsStreamInvalidationEventTime" / Int64sl,
        "hnsLastCorrelatedTime" / Int64sl,
        "hnsTimeElapsed" / Int64sl,
        "hnsLastTime" / Int64sl,
        "hnsNewLastTime" / Int64sl
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=152, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_152_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=153, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_153_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "bNeedFormatNegotiation" / Int8ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=154, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_154_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=155, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_155_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=156, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_156_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "bDeviceChange" / Int8ul,
        "hnsNewStreamStartTime" / Int64sl
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=157, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_157_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "bStopped" / Int8ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=158, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_158_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=159, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_159_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=160, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_160_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "eventType" / Int32sl,
        "bReacquireDevice" / Int8ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=161, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_161_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=162, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_162_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=163, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_163_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "eventType" / Int32sl
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=164, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_164_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=165, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_165_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=166, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_166_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=167, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_167_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=168, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_168_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=169, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_169_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "dwNewState" / Int32sl
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=170, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_170_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=171, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_171_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=172, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_172_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=173, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_173_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=174, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_174_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=175, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_175_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=176, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_176_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=177, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_177_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "MFTimeOfLastRenderSample" / Int64sl
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=178, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_178_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "u32FramesToRender" / Int32sl
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=179, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_179_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "ClockTime" / Int64sl,
        "CorrelatedTime" / Int64sl,
        "IsStreamInvalidating" / Int8ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=180, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_180_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=181, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_181_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "m_pCurrentMediaType" / Int64sl,
        "IsStreamInvalidating" / Int8ul,
        "hrAEFormatQuery" / Int32ul,
        "hFormatResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=182, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_182_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "wFormatTag" / Int32ul,
        "nChannels" / Int16ul,
        "nSamplesPerSec" / Int32ul,
        "nAvgBytesPerSec" / Int32ul,
        "nBlockAlign" / Int16ul,
        "wBitsPerSample" / Int16ul,
        "cbSize" / Int16ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=183, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_183_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=184, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_184_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "clientType" / Int32ul,
        "hFormatResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=185, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_185_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=186, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_186_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=187, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_187_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=188, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_188_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "clientType" / Int32ul,
        "hFormatResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=189, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_189_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=190, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_190_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "bufferDuration" / Int64sl,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=191, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_191_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=192, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_192_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=193, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_193_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=194, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_194_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=195, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_195_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=196, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_196_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=197, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_197_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "Key" / Int64ul,
        "Delay" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=198, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_198_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "Key" / Int64ul,
        "Delay" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=199, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_199_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=200, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_200_0(Etw):
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


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=500, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_500_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "u32FramesRead" / Int32ul,
        "m_u64LastSampleTime" / Int64ul,
        "u64Duration" / Int64ul,
        "dwFlagsForSample" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=501, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_501_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "m_pParent" / Int64ul,
        "eventType" / Int32sl
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=502, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_502_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "m_bAudioProcessingRaw" / Int8ul,
        "m_bIsEventDriven" / Int8ul,
        "m_bIsLowLatency" / Int8ul,
        "m_hnsBufferDuration" / Int64sl,
        "m_uiAudioCategory" / Int32ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=503, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_503_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "m_spAudioSessionControl" / Int64ul,
        "m_spAudioSessionEvents" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=504, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_504_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=505, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_505_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "wstrEndpointId" / WString,
        "role" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=506, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_506_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=507, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_507_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "wstrEndpointId" / WString,
        "role" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=508, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_508_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "uFailedLineNumber" / Int32ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=509, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_509_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=510, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_510_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "AudioClientProperties_bIsOffload" / Int8ul,
        "AudioClientProperties_eCategory" / Int32ul,
        "AudioClientProperties_Options" / Int32ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=511, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_511_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "m_spAudioClientForStreaming" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=512, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_512_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "m_u32BytesPerFrame" / Int32ul,
        "m_u32FramesPerSecond" / Int32ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=513, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_513_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "bFirstRead" / Int8ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=514, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_514_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=515, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_515_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=516, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_516_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=517, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_517_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "m_bEngineStarted" / Int8ul,
        "m_bIsEventDriven" / Int8ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=518, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_518_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "m_bEngineStarted" / Int8ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=519, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_519_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "bReset" / Int8ul,
        "m_bEngineStarted" / Int8ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=520, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_520_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=521, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_521_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=522, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_522_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=523, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_523_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=524, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_524_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=525, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_525_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "m_bEngineStarted" / Int8ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=526, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_526_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=527, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_527_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "DisconnectReason" / Int32sl
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=528, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_528_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "u32FramesRead" / Int32ul,
        "u32ActualFramesInCurrentPacket" / Int32ul,
        "dwFlags" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=529, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_529_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "fLevel" / Float32l
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=530, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_530_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "bMute" / Int8ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=531, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_531_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "pParentObj" / Int64ul,
        "dwWorkQueueId" / Int32ul,
        "lWorkQueuePriority" / Int32sl,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=532, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_532_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=533, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_533_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=534, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_534_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=535, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_535_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "m_u32BufferFrameCount" / Int32ul,
        "m_u32BytesPerFrame" / Int32ul,
        "m_u32FramesPerSecond" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=536, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_536_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=537, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_537_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "wFormatTag" / Int32ul,
        "nChannels" / Int16ul,
        "nSamplesPerSec" / Int32ul,
        "nAvgBytesPerSec" / Int32ul,
        "nBlockAlign" / Int16ul,
        "wBitsPerSample" / Int16ul,
        "cbSize" / Int16ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=538, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_538_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "wFormatTag" / Int32ul,
        "nChannels" / Int16ul,
        "nSamplesPerSec" / Int32ul,
        "nAvgBytesPerSec" / Int32ul,
        "nBlockAlign" / Int16ul,
        "wBitsPerSample" / Int16ul,
        "cbSize" / Int16ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=539, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_539_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=540, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_540_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=541, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_541_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "m_ReadySampleCount" / Int32ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=542, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_542_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "m_ReadySampleCount" / Int32ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=543, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_543_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "pMediaType" / Int64ul,
        "m_spCurrentMediaType" / Int64ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=544, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_544_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "m_spCurrentMediaType" / Int64ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=545, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_545_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "wFormatTag" / Int32ul,
        "nChannels" / Int16ul,
        "nSamplesPerSec" / Int32ul,
        "nAvgBytesPerSec" / Int32ul,
        "nBlockAlign" / Int16ul,
        "wBitsPerSample" / Int16ul,
        "cbSize" / Int16ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=546, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_546_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "guidService" / Guid,
        "riid" / Guid,
        "pvObject" / Int64ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=547, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_547_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "u32CurrentPadding" / Int32ul,
        "ulSamples" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=600, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_600_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "State" / Int32sl,
        "ClockOffset" / Int64sl,
        "QPC" / Int64sl
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=650, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_650_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "SrcObject" / Int64ul,
        "SamplesReceived" / Int32sl,
        "LateSamples" / Int64sl,
        "TotalLateTime_ms" / Int64sl,
        "SampleLatency_hns" / Int64sl,
        "SampleTime_hns" / Int64sl
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=651, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_651_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "Node" / Int64ul,
        "OutputIndex" / Int32sl,
        "WorkQueueID" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=652, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_652_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "Node" / Int64ul,
        "OutputIndex" / Int32sl,
        "WorkQueueID" / Int32ul
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=700, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_700_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "Stream" / Int32sl,
        "SamplePtr" / Int64ul,
        "TimeStamp" / Int64sl
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=701, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_701_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "Stream" / Int32sl,
        "ES_Stream" / Int32sl,
        "TimeStamp" / Int64sl,
        "PackSize" / Int32sl,
        "LastPCR" / Int64sl
    )


@declare(guid=guid("b20e65ac-c905-4014-8f78-1b6a508142eb"), event_id=702, version=0)
class Microsoft_Windows_MediaFoundation_Performance_Core_702_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "PCR" / Int64sl
    )

