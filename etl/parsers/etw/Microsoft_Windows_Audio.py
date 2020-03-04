# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Audio
GUID : ae4bd3be-f36f-45b6-8d21-bdd6fb832853
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=0, version=0)
class Microsoft_Windows_Audio_0_0(Etw):
    pattern = Struct(
        "Event" / Int32ul,
        "EventName" / WString,
        "hr" / Int32ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=1, version=0)
class Microsoft_Windows_Audio_1_0(Etw):
    pattern = Struct(
        "DeviceEventType" / Int32ul,
        "DeviceEventTypeName" / WString,
        "hr" / Int32ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=2, version=0)
class Microsoft_Windows_Audio_2_0(Etw):
    pattern = Struct(
        "dwServiceType" / Int32ul,
        "dwCurrentState" / Int32ul,
        "dwControlsAccepted" / Int32ul,
        "dwWin32ExitCode" / Int32ul,
        "dwServiceSpecificExitCode" / Int32ul,
        "dwCheckPoint" / Int32ul,
        "dwWaitHint" / Int32ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=3, version=0)
class Microsoft_Windows_Audio_3_0(Etw):
    pattern = Struct(
        "szSubsystemName" / WString,
        "dwSubsystemFailureCode" / Int32ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=4, version=0)
class Microsoft_Windows_Audio_4_0(Etw):
    pattern = Struct(
        "dwAudioDgTerminationCode" / Int32ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=5, version=0)
class Microsoft_Windows_Audio_5_0(Etw):
    pattern = Struct(
        "dwAudioDgStartupFailureCode" / Int32ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=10, version=0)
class Microsoft_Windows_Audio_10_0(Etw):
    pattern = Struct(
        "dwRestartCount" / Int32ul,
        "szInputEndpointName" / WString,
        "szOutputEndpointName" / WString
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=11, version=0)
class Microsoft_Windows_Audio_11_0(Etw):
    pattern = Struct(
        "dwAudioSrvStreamFlags" / Int32ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=12, version=0)
class Microsoft_Windows_Audio_12_0(Etw):
    pattern = Struct(
        "Object" / Int32ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=13, version=0)
class Microsoft_Windows_Audio_13_0(Etw):
    pattern = Struct(
        "Object" / Int32ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=18, version=0)
class Microsoft_Windows_Audio_18_0(Etw):
    pattern = Struct(
        "dwAudioDgTerminationCode" / Int32ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=19, version=0)
class Microsoft_Windows_Audio_19_0(Etw):
    pattern = Struct(
        "dwGlitchCount" / Int32ul,
        "hnsTimeWindow" / Int64ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=20, version=0)
class Microsoft_Windows_Audio_20_0(Etw):
    pattern = Struct(
        "Format" / Int32ul,
        "SamplingRate" / Int32ul,
        "bAudioSrvStreamResourceType" / Int8ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=21, version=0)
class Microsoft_Windows_Audio_21_0(Etw):
    pattern = Struct(
        "AppId" / WString,
        "SoundLevel" / Int32ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=22, version=0)
class Microsoft_Windows_Audio_22_0(Etw):
    pattern = Struct(
        "bIsSuspended" / Int8ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=23, version=0)
class Microsoft_Windows_Audio_23_0(Etw):
    pattern = Struct(
        "bExclusiveModeStream" / Int8ul,
        "bOffloadStream" / Int8ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=24, version=0)
class Microsoft_Windows_Audio_24_0(Etw):
    pattern = Struct(
        "AppId" / WString,
        "PID" / Int32ul,
        "Category" / Int32ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=25, version=0)
class Microsoft_Windows_Audio_25_0(Etw):
    pattern = Struct(
        "AppId" / WString,
        "PID" / Int32ul,
        "Category" / Int32ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=26, version=0)
class Microsoft_Windows_Audio_26_0(Etw):
    pattern = Struct(
        "pCMonitor" / Int64ul,
        "DevicePosition" / Int64ul,
        "QPCPosition" / Int64ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=27, version=0)
class Microsoft_Windows_Audio_27_0(Etw):
    pattern = Struct(
        "pCMonitor" / Int64ul,
        "DevicePosition" / Int64ul,
        "QPCPosition" / Int64ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=28, version=0)
class Microsoft_Windows_Audio_28_0(Etw):
    pattern = Struct(
        "pCAudioFormatConvert" / Int64ul,
        "ConverstionType" / Int32ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=29, version=0)
class Microsoft_Windows_Audio_29_0(Etw):
    pattern = Struct(
        "pCCrossProcessClientInputEndpoint" / Int64ul,
        "Unused" / Int32ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=30, version=0)
class Microsoft_Windows_Audio_30_0(Etw):
    pattern = Struct(
        "pCCrossProcessClientInputEndpoint" / Int64ul,
        "Unused" / Int32ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=31, version=0)
class Microsoft_Windows_Audio_31_0(Etw):
    pattern = Struct(
        "pCCrossProcessClientOutputEndpoint" / Int64ul,
        "WriteBytePos" / Int64ul,
        "ReadBytePos" / Int64ul,
        "BytesToWrite" / Int32ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=32, version=0)
class Microsoft_Windows_Audio_32_0(Etw):
    pattern = Struct(
        "pCCrossProcessClientOutputEndpoint" / Int64ul,
        "WriteOffset" / Int32ul,
        "ReadOffset" / Int32ul,
        "BytesToWrite" / Int32ul,
        "EndOfDataOffset" / Int32ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=33, version=0)
class Microsoft_Windows_Audio_33_0(Etw):
    pattern = Struct(
        "pCCrossProcessServerInputEndpoint" / Int64ul,
        "WriteOffset" / Int32ul,
        "ReadOffset" / Int32ul,
        "BufferSize" / Int32ul,
        "BytesAvailable" / Int32ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=34, version=0)
class Microsoft_Windows_Audio_34_0(Etw):
    pattern = Struct(
        "pCCrossProcessServerOutputEndpoint" / Int64ul,
        "WriteBytePos" / Int64ul,
        "DroppedBytes" / Int32ul,
        "ReadBytePos" / Int64ul,
        "BytesToWrite" / Int32ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=35, version=0)
class Microsoft_Windows_Audio_35_0(Etw):
    pattern = Struct(
        "pCCrossProcessServerOutputEndpoint" / Int64ul,
        "WriteOffset" / Int32ul,
        "ReadOffset" / Int32ul,
        "BytesToWrite" / Int32ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=36, version=0)
class Microsoft_Windows_Audio_36_0(Etw):
    pattern = Struct(
        "pOwner" / Int64ul,
        "NextStreamingPacketToComplete" / Int32ul,
        "MaxPacketCount" / Int32ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=37, version=0)
class Microsoft_Windows_Audio_37_0(Etw):
    pattern = Struct(
        "pOwner" / Int64ul,
        "IoctlTimeHNS" / Int64ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=38, version=0)
class Microsoft_Windows_Audio_38_0(Etw):
    pattern = Struct(
        "pCAudioBasePin" / Int64ul,
        "pLockedDataPointer" / Int64ul,
        "bLockedEqualsUnrolled" / Int8ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=39, version=0)
class Microsoft_Windows_Audio_39_0(Etw):
    pattern = Struct(
        "pCAudioBasePin" / Int64ul,
        "LockedDataPointer" / Int64ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=40, version=0)
class Microsoft_Windows_Audio_40_0(Etw):
    pattern = Struct(
        "pCAudioBasePin" / Int64ul,
        "LockedDataPointer" / Int64ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=41, version=0)
class Microsoft_Windows_Audio_41_0(Etw):
    pattern = Struct(
        "pCAudioBasePin" / Int64ul,
        "GlitchStreamPosition" / Int64ul,
        "GlitchDuration" / Int32ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=42, version=0)
class Microsoft_Windows_Audio_42_0(Etw):
    pattern = Struct(
        "pCAudioCapturePinRealtimeStreaming" / Int64ul,
        "WritePosition" / Int64ul,
        "PlayPosition" / Int64ul,
        "StreamPosition" / Int64ul,
        "StreamPosMinusReadPos" / Int64ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=43, version=0)
class Microsoft_Windows_Audio_43_0(Etw):
    pattern = Struct(
        "pCAudioCapturePinRealtimeStreaming" / Int64ul,
        "WritePosition" / Int64ul,
        "PlayPosition" / Int64ul,
        "StreamPosition" / Int64ul,
        "ReadPosMinusStreamPos" / Int64ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=44, version=0)
class Microsoft_Windows_Audio_44_0(Etw):
    pattern = Struct(
        "pCAudioRenderPinRealtimeStreaming" / Int64ul,
        "WritePosition" / Int64ul,
        "PlayPosition" / Int64ul,
        "TotalPosition" / Int64ul,
        "WritePosMinusTotalPos" / Int64ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=45, version=0)
class Microsoft_Windows_Audio_45_0(Etw):
    pattern = Struct(
        "pCAudioCapturePinStandardStreaming" / Int64ul,
        "ValidPositionEnd" / Int64ul,
        "ValidPositionStart" / Int64ul,
        "StreamPosition" / Int64ul,
        "StreamPosMinusValidPosEnd" / Int64ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=46, version=0)
class Microsoft_Windows_Audio_46_0(Etw):
    pattern = Struct(
        "pCAudioCapturePinStandardStreaming" / Int64ul,
        "ValidPositionEnd" / Int64ul,
        "ValidPositionStart" / Int64ul,
        "StreamPosition" / Int64ul,
        "ValidPosStartMinusStreamPos" / Int64ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=47, version=0)
class Microsoft_Windows_Audio_47_0(Etw):
    pattern = Struct(
        "pCAudioCapturePinStandardStreaming" / Int64ul,
        "StreamPosition" / Int64ul,
        "FrameCount" / Int32ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=48, version=0)
class Microsoft_Windows_Audio_48_0(Etw):
    pattern = Struct(
        "pCAudioRenderPinStandardStreaming" / Int64ul,
        "DevicePosition" / Int64ul,
        "StreamPosition" / Int64ul,
        "AvailableFrames" / Int32ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=49, version=0)
class Microsoft_Windows_Audio_49_0(Etw):
    pattern = Struct(
        "pCAudioRenderPinStandardStreaming" / Int64ul,
        "DevicePosition" / Int64ul,
        "StreamPosition" / Int64ul,
        "AvailableFrames" / Int32ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=50, version=0)
class Microsoft_Windows_Audio_50_0(Etw):
    pattern = Struct(
        "APOCLSID" / Guid,
        "AudioSignalProcessingMode" / Guid,
        "InitializeForDiscoveryOnly" / Int8ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=51, version=0)
class Microsoft_Windows_Audio_51_0(Etw):
    pattern = Struct(
        "objectpointer" / Int64ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=52, version=0)
class Microsoft_Windows_Audio_52_0(Etw):
    pattern = Struct(
        "objectpointer" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=53, version=0)
class Microsoft_Windows_Audio_53_0(Etw):
    pattern = Struct(
        "objectpointer" / Int64ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=58, version=0)
class Microsoft_Windows_Audio_58_0(Etw):
    pattern = Struct(
        "flow" / Int32ul,
        "role" / Int32ul,
        "TargetProcessId" / Int32ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=59, version=0)
class Microsoft_Windows_Audio_59_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=60, version=0)
class Microsoft_Windows_Audio_60_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=61, version=0)
class Microsoft_Windows_Audio_61_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "NewState" / Int32ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=62, version=0)
class Microsoft_Windows_Audio_62_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=63, version=0)
class Microsoft_Windows_Audio_63_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=64, version=0)
class Microsoft_Windows_Audio_64_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "flow" / Int32ul,
        "role" / Int32ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=65, version=0)
class Microsoft_Windows_Audio_65_0(Etw):
    pattern = Struct(
        "DeviceName" / WString,
        "DeviceId" / WString,
        "flow" / Int32ul,
        "NewState" / Int32ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=101, version=0)
class Microsoft_Windows_Audio_101_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=102, version=0)
class Microsoft_Windows_Audio_102_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=103, version=0)
class Microsoft_Windows_Audio_103_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=104, version=0)
class Microsoft_Windows_Audio_104_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=105, version=0)
class Microsoft_Windows_Audio_105_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=106, version=0)
class Microsoft_Windows_Audio_106_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=107, version=0)
class Microsoft_Windows_Audio_107_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=108, version=0)
class Microsoft_Windows_Audio_108_0(Etw):
    pattern = Struct(
        "DeviceId" / WString,
        "object" / Int64ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=109, version=0)
class Microsoft_Windows_Audio_109_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=110, version=0)
class Microsoft_Windows_Audio_110_0(Etw):
    pattern = Struct(
        "DeviceId" / WString,
        "object" / Int64ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=111, version=0)
class Microsoft_Windows_Audio_111_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "ioControlCode" / Int32ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=112, version=0)
class Microsoft_Windows_Audio_112_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=113, version=0)
class Microsoft_Windows_Audio_113_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "ioControlCode" / Int32ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=114, version=0)
class Microsoft_Windows_Audio_114_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=115, version=0)
class Microsoft_Windows_Audio_115_0(Etw):
    pattern = Struct(
        "CrossProcessInstance" / Int64ul,
        "ReadIndex" / Int32ul,
        "WriteIndexIndex" / Int32ul,
        "FramesInPacket" / Int32ul,
        "QPC" / Int64ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=116, version=0)
class Microsoft_Windows_Audio_116_0(Etw):
    pattern = Struct(
        "PumpInstance" / Int64ul,
        "deadlineHns" / Int64sl
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=117, version=0)
class Microsoft_Windows_Audio_117_0(Etw):
    pattern = Struct(
        "PumpInstance" / Int64ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=118, version=0)
class Microsoft_Windows_Audio_118_0(Etw):
    pattern = Struct(
        "PumpInstance" / Int64ul,
        "deadlineHns" / Int64sl
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=119, version=0)
class Microsoft_Windows_Audio_119_0(Etw):
    pattern = Struct(
        "PumpInstance" / Int64ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=120, version=0)
class Microsoft_Windows_Audio_120_0(Etw):
    pattern = Struct(
        "PumpInstance" / Int64ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=121, version=0)
class Microsoft_Windows_Audio_121_0(Etw):
    pattern = Struct(
        "EndpointId" / WString
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=122, version=0)
class Microsoft_Windows_Audio_122_0(Etw):
    pattern = Struct(
        "EndpointId" / WString,
        "hr" / Int32ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=123, version=0)
class Microsoft_Windows_Audio_123_0(Etw):
    pattern = Struct(
        "EndpointId" / WString,
        "category" / Int32ul,
        "Raw" / Int8ul,
        "MatchFormat" / Int8ul,
        "ConnectorType" / Int32ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=125, version=0)
class Microsoft_Windows_Audio_125_0(Etw):
    pattern = Struct(
        "EndpointId" / WString,
        "category" / Int32ul,
        "Raw" / Int8ul,
        "MatchFormat" / Int8ul,
        "ConnectorType" / Int32ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=127, version=0)
class Microsoft_Windows_Audio_127_0(Etw):
    pattern = Struct(
        "EndpointId" / WString,
        "category" / Int32ul,
        "Raw" / Int8ul,
        "MatchFormat" / Int8ul,
        "ConnectorType" / Int32ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=133, version=0)
class Microsoft_Windows_Audio_133_0(Etw):
    pattern = Struct(
        "EndpointId" / WString,
        "ConnectorType" / Int32ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=135, version=0)
class Microsoft_Windows_Audio_135_0(Etw):
    pattern = Struct(
        "PumpInstance" / Int64ul,
        "SampleIndex" / Int64ul,
        "OrigProcessingStart" / Int64ul,
        "NewProcessingStart" / Int64ul,
        "StartCorrection" / Int64sl,
        "TimeDelta" / Int64ul,
        "SampleDelta" / Int32ul,
        "DevicePeriod" / Int64ul,
        "ActualDevicePeriod" / Int64ul,
        "WindowWidth_ms" / Int64ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=136, version=0)
class Microsoft_Windows_Audio_136_0(Etw):
    pattern = Struct(
        "PumpInstance" / Int64ul,
        "uEventMask" / Int32ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=137, version=0)
class Microsoft_Windows_Audio_137_0(Etw):
    pattern = Struct(
        "PumpInstance" / Int64ul,
        "WakeCategory" / Int32ul,
        "WakeValue" / Int32ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=138, version=0)
class Microsoft_Windows_Audio_138_0(Etw):
    pattern = Struct(
        "PumpInstance" / Int64ul,
        "Phase" / Int32ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=139, version=0)
class Microsoft_Windows_Audio_139_0(Etw):
    pattern = Struct(
        "PumpInstance" / Int64ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=140, version=0)
class Microsoft_Windows_Audio_140_0(Etw):
    pattern = Struct(
        "PumpInstance" / Int64ul,
        "WorkDuration" / Int64sl,
        "MaxWorkDuration" / Int64sl
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=141, version=0)
class Microsoft_Windows_Audio_141_0(Etw):
    pattern = Struct(
        "objInstance" / Int64ul,
        "ucType" / Int32ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=142, version=0)
class Microsoft_Windows_Audio_142_0(Etw):
    pattern = Struct(
        "objInstance" / Int64ul,
        "ucType" / Int32ul,
        "WritePosition" / Int64sl,
        "PlayPosition" / Int64ul,
        "StreamPosition" / Int64ul,
        "GlitchFrameCount" / Int64ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=143, version=0)
class Microsoft_Windows_Audio_143_0(Etw):
    pattern = Struct(
        "objInstance" / Int64ul,
        "SampleTime" / Int64ul,
        "u64ByteCount" / Int64ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=144, version=0)
class Microsoft_Windows_Audio_144_0(Etw):
    pattern = Struct(
        "objInstance" / Int64ul,
        "ucType" / Int32ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=145, version=0)
class Microsoft_Windows_Audio_145_0(Etw):
    pattern = Struct(
        "objInstance" / Int64ul,
        "ucType" / Int32ul,
        "ProcessTime" / Int64ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=146, version=0)
class Microsoft_Windows_Audio_146_0(Etw):
    pattern = Struct(
        "objInstance" / Int64ul,
        "ucType" / Int32ul,
        "WritePosition" / Int64ul,
        "PlayPosition" / Int64ul,
        "StreamPosition" / Int64ul,
        "LoopPosition" / Int64ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=147, version=0)
class Microsoft_Windows_Audio_147_0(Etw):
    pattern = Struct(
        "objInstance" / Int64ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=148, version=0)
class Microsoft_Windows_Audio_148_0(Etw):
    pattern = Struct(
        "objInstance" / Int64ul,
        "ucType" / Int32ul,
        "Data1" / Int64ul,
        "Data2" / Int64ul,
        "Data3" / Int64ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=149, version=0)
class Microsoft_Windows_Audio_149_0(Etw):
    pattern = Struct(
        "objInstance" / Int64ul,
        "ucType" / Int32ul,
        "Index" / Int32ul,
        "OutStandingCount" / Int32ul,
        "FrameExtent" / Int64ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=150, version=0)
class Microsoft_Windows_Audio_150_0(Etw):
    pattern = Struct(
        "objInstance" / Int64ul,
        "ucType" / Int32ul,
        "PinHandle" / Int64ul,
        "FormatTag" / Int32ul,
        "SampleRate" / Int32ul,
        "BitsPerSample" / Int32ul,
        "Channels" / Int32ul,
        "Period" / Int32ul,
        "Latency" / Int32ul,
        "BufferSize" / Int32ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=151, version=0)
class Microsoft_Windows_Audio_151_0(Etw):
    pattern = Struct(
        "objInstance" / Int64ul,
        "ucType" / Int32ul,
        "InterpolatedPlayPosition" / Int64ul,
        "InterpolatedWritePosition" / Int64ul,
        "RealPlayPosition" / Int64ul,
        "RealWritePosition" / Int64ul,
        "SampleRate" / Float32l,
        "FilteredError" / Float32l
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=152, version=0)
class Microsoft_Windows_Audio_152_0(Etw):
    pattern = Struct(
        "objInstance" / Int64ul,
        "ucType" / Int32ul,
        "Flag" / Int64ul,
        "Padding" / Int64ul,
        "QPCPos" / Int64ul,
        "DevPos" / Int64ul,
        "StrmPos" / Int64ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=153, version=0)
class Microsoft_Windows_Audio_153_0(Etw):
    pattern = Struct(
        "objInstance" / Int64ul,
        "ucType" / Int32ul,
        "Custom1" / Int64ul,
        "Custom2" / Int64ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=154, version=0)
class Microsoft_Windows_Audio_154_0(Etw):
    pattern = Struct(
        "objInstance" / Int64ul,
        "ucType" / Int32ul,
        "u64Param1" / Int64ul,
        "u64Param2" / Int64ul,
        "u64Param3" / Int64ul,
        "u64Param4" / Int64ul,
        "f64Param1" / Float32l,
        "f64Param2" / Float32l,
        "f64Param3" / Float32l,
        "f64Param4" / Float32l
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=155, version=0)
class Microsoft_Windows_Audio_155_0(Etw):
    pattern = Struct(
        "objInstance" / Int64ul,
        "ucType" / Int32ul,
        "hHeap" / Int64ul,
        "ulInitial" / Int32ul,
        "ulMin" / Int32ul,
        "ulMax" / Int32ul,
        "ulAllocCount" / Int32ul,
        "ulExtendCount" / Int32ul,
        "ulTotalAlloc" / Int32ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=156, version=0)
class Microsoft_Windows_Audio_156_0(Etw):
    pattern = Struct(
        "objInstance" / Int64ul,
        "ucType" / Int32ul,
        "u64Param1" / Int64ul,
        "u64Param2" / Int64ul,
        "u64Param3" / Int64ul,
        "u64Param4" / Int64ul
    )


@declare(guid=guid("ae4bd3be-f36f-45b6-8d21-bdd6fb832853"), event_id=157, version=0)
class Microsoft_Windows_Audio_157_0(Etw):
    pattern = Struct(
        "objInstance" / Int64ul,
        "ucType" / Int32ul,
        "u64Param1" / Int64ul,
        "u64Param2" / Int64ul,
        "u64Param3" / Int64ul,
        "u64Param4" / Int64ul
    )

