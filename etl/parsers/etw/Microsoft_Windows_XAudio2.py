# -*- coding: utf-8 -*-
"""
Microsoft-Windows-XAudio2
GUID : 1ee3abdb-c1fc-4b43-9e56-11064abba866
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("1ee3abdb-c1fc-4b43-9e56-11064abba866"), event_id=16, version=0)
class Microsoft_Windows_XAudio2_16_0(Etw):
    pattern = Struct(
        "Instance" / Int64ul,
        "Processors" / Int32ul
    )


@declare(guid=guid("1ee3abdb-c1fc-4b43-9e56-11064abba866"), event_id=32, version=0)
class Microsoft_Windows_XAudio2_32_0(Etw):
    pattern = Struct(
        "Pointer" / Int64ul
    )


@declare(guid=guid("1ee3abdb-c1fc-4b43-9e56-11064abba866"), event_id=33, version=0)
class Microsoft_Windows_XAudio2_33_0(Etw):
    pattern = Struct(
        "SourceVoiceCount" / Int32ul,
        "SubmixVoiceCount" / Int32ul,
        "MasteringVoiceCount" / Int32ul
    )


@declare(guid=guid("1ee3abdb-c1fc-4b43-9e56-11064abba866"), event_id=48, version=0)
class Microsoft_Windows_XAudio2_48_0(Etw):
    pattern = Struct(
        "Address" / Int64ul,
        "ProcessingStage" / Int32ul,
        "Channels" / Int32ul,
        "SampleRate" / Int32ul
    )


@declare(guid=guid("1ee3abdb-c1fc-4b43-9e56-11064abba866"), event_id=49, version=0)
class Microsoft_Windows_XAudio2_49_0(Etw):
    pattern = Struct(
        "OriginalHz" / Int32ul,
        "NewHz" / Int32ul,
        "Quantum" / Int32ul
    )


@declare(guid=guid("1ee3abdb-c1fc-4b43-9e56-11064abba866"), event_id=64, version=0)
class Microsoft_Windows_XAudio2_64_0(Etw):
    pattern = Struct(
        "Address" / Int64ul,
        "Channels" / Int32ul,
        "SampleRate" / Int32ul,
        "RendererId" / WString
    )


@declare(guid=guid("1ee3abdb-c1fc-4b43-9e56-11064abba866"), event_id=65, version=0)
class Microsoft_Windows_XAudio2_65_0(Etw):
    pattern = Struct(
        "OriginalHz" / Int32ul,
        "NewHz" / Int32ul,
        "Quantum" / Int32ul
    )


@declare(guid=guid("1ee3abdb-c1fc-4b43-9e56-11064abba866"), event_id=66, version=0)
class Microsoft_Windows_XAudio2_66_0(Etw):
    pattern = Struct(
        "Address" / Int64ul,
        "Channels" / Int32ul,
        "SampleRate" / Int32ul,
        "RendererId" / WString
    )


@declare(guid=guid("1ee3abdb-c1fc-4b43-9e56-11064abba866"), event_id=67, version=0)
class Microsoft_Windows_XAudio2_67_0(Etw):
    pattern = Struct(
        "DeviceId" / WString,
        "EndpointId" / WString
    )


@declare(guid=guid("1ee3abdb-c1fc-4b43-9e56-11064abba866"), event_id=80, version=0)
class Microsoft_Windows_XAudio2_80_0(Etw):
    pattern = Struct(
        "hr" / Int32sl
    )


@declare(guid=guid("1ee3abdb-c1fc-4b43-9e56-11064abba866"), event_id=96, version=0)
class Microsoft_Windows_XAudio2_96_0(Etw):
    pattern = Struct(
        "Time" / Float32l,
        "Callback" / Int32ul
    )


@declare(guid=guid("1ee3abdb-c1fc-4b43-9e56-11064abba866"), event_id=97, version=0)
class Microsoft_Windows_XAudio2_97_0(Etw):
    pattern = Struct(
        "Value" / Float32l
    )


@declare(guid=guid("1ee3abdb-c1fc-4b43-9e56-11064abba866"), event_id=98, version=0)
class Microsoft_Windows_XAudio2_98_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("1ee3abdb-c1fc-4b43-9e56-11064abba866"), event_id=99, version=0)
class Microsoft_Windows_XAudio2_99_0(Etw):
    pattern = Struct(
        "Pointer" / Int64ul
    )


@declare(guid=guid("1ee3abdb-c1fc-4b43-9e56-11064abba866"), event_id=256, version=0)
class Microsoft_Windows_XAudio2_256_0(Etw):
    pattern = Struct(
        "MinimumCyclesPerQuantum" / Int32ul,
        "MaximumCyclesPerQuantum" / Int32ul,
        "GlitchesSinceEngineStarted" / Int32ul,
        "CpuUsage" / Float32l,
        "LatencyInSamples" / Int32ul,
        "TotalMemoryUsage" / Int32ul,
        "ActiveSourceVoices" / Int32ul,
        "TotalSourceVoices" / Int32ul,
        "ActiveSubmixVoices" / Int32ul,
        "ActiveResamplers" / Int32ul,
        "ActiveMatrixMixers" / Int32ul
    )

