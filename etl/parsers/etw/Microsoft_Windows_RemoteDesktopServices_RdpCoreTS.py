# -*- coding: utf-8 -*-
"""
Microsoft-Windows-RemoteDesktopServices-RdpCoreTS
GUID : 1139c61b-b549-4251-8ed3-27250a1edec8
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("1139c61b-b549-4251-8ed3-27250a1edec8"), event_id=1, version=0)
class Microsoft_Windows_RemoteDesktopServices_RdpCoreTS_1_0(Etw):
    pattern = Struct(
        "HresultCode" / Int32ul
    )


@declare(guid=guid("1139c61b-b549-4251-8ed3-27250a1edec8"), event_id=3, version=0)
class Microsoft_Windows_RemoteDesktopServices_RdpCoreTS_3_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("1139c61b-b549-4251-8ed3-27250a1edec8"), event_id=4, version=0)
class Microsoft_Windows_RemoteDesktopServices_RdpCoreTS_4_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("1139c61b-b549-4251-8ed3-27250a1edec8"), event_id=5, version=0)
class Microsoft_Windows_RemoteDesktopServices_RdpCoreTS_5_0(Etw):
    pattern = Struct(
        "StatusCode" / Int32ul
    )


@declare(guid=guid("1139c61b-b549-4251-8ed3-27250a1edec8"), event_id=6, version=0)
class Microsoft_Windows_RemoteDesktopServices_RdpCoreTS_6_0(Etw):
    pattern = Struct(
        "NumMonitors" / Int32ul,
        "RequestedMode" / WString,
        "AppliedMode" / WString
    )


@declare(guid=guid("1139c61b-b549-4251-8ed3-27250a1edec8"), event_id=35, version=0)
class Microsoft_Windows_RemoteDesktopServices_RdpCoreTS_35_0(Etw):
    pattern = Struct(
        "HresultCode" / Int32ul
    )


@declare(guid=guid("1139c61b-b549-4251-8ed3-27250a1edec8"), event_id=36, version=0)
class Microsoft_Windows_RemoteDesktopServices_RdpCoreTS_36_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("1139c61b-b549-4251-8ed3-27250a1edec8"), event_id=37, version=0)
class Microsoft_Windows_RemoteDesktopServices_RdpCoreTS_37_0(Etw):
    pattern = Struct(
        "NumMonitors" / Int32ul,
        "RequestedMode" / WString,
        "AppliedMode" / WString
    )


@declare(guid=guid("1139c61b-b549-4251-8ed3-27250a1edec8"), event_id=65, version=0)
class Microsoft_Windows_RemoteDesktopServices_RdpCoreTS_65_0(Etw):
    pattern = Struct(
        "ConnectionName" / WString
    )


@declare(guid=guid("1139c61b-b549-4251-8ed3-27250a1edec8"), event_id=66, version=0)
class Microsoft_Windows_RemoteDesktopServices_RdpCoreTS_66_0(Etw):
    pattern = Struct(
        "ConnectionName" / WString,
        "SessionID" / Int32ul
    )


@declare(guid=guid("1139c61b-b549-4251-8ed3-27250a1edec8"), event_id=67, version=0)
class Microsoft_Windows_RemoteDesktopServices_RdpCoreTS_67_0(Etw):
    pattern = Struct(
        "ConnectionName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("1139c61b-b549-4251-8ed3-27250a1edec8"), event_id=68, version=0)
class Microsoft_Windows_RemoteDesktopServices_RdpCoreTS_68_0(Etw):
    pattern = Struct(
        "ConnectionName" / WString,
        "PromptForCredentials" / Int32ul,
        "PromptForCredentialsDone" / Int32ul,
        "GfxChannelOpened" / Int32ul,
        "FirstGraphicsReceived" / Int32ul
    )


@declare(guid=guid("1139c61b-b549-4251-8ed3-27250a1edec8"), event_id=69, version=0)
class Microsoft_Windows_RemoteDesktopServices_RdpCoreTS_69_0(Etw):
    pattern = Struct(
        "ModuleName" / WString
    )


@declare(guid=guid("1139c61b-b549-4251-8ed3-27250a1edec8"), event_id=70, version=0)
class Microsoft_Windows_RemoteDesktopServices_RdpCoreTS_70_0(Etw):
    pattern = Struct(
        "DisplayDriverName" / WString
    )


@declare(guid=guid("1139c61b-b549-4251-8ed3-27250a1edec8"), event_id=71, version=0)
class Microsoft_Windows_RemoteDesktopServices_RdpCoreTS_71_0(Etw):
    pattern = Struct(
        "ConnectionName" / WString,
        "DisplayDriverName" / WString
    )


@declare(guid=guid("1139c61b-b549-4251-8ed3-27250a1edec8"), event_id=72, version=0)
class Microsoft_Windows_RemoteDesktopServices_RdpCoreTS_72_0(Etw):
    pattern = Struct(
        "MethodName" / WString
    )


@declare(guid=guid("1139c61b-b549-4251-8ed3-27250a1edec8"), event_id=73, version=0)
class Microsoft_Windows_RemoteDesktopServices_RdpCoreTS_73_0(Etw):
    pattern = Struct(
        "Disabled" / Int32ul
    )


@declare(guid=guid("1139c61b-b549-4251-8ed3-27250a1edec8"), event_id=97, version=0)
class Microsoft_Windows_RemoteDesktopServices_RdpCoreTS_97_0(Etw):
    pattern = Struct(
        "ComponentName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("1139c61b-b549-4251-8ed3-27250a1edec8"), event_id=99, version=0)
class Microsoft_Windows_RemoteDesktopServices_RdpCoreTS_99_0(Etw):
    pattern = Struct(
        "ResultCode" / Int32ul
    )


@declare(guid=guid("1139c61b-b549-4251-8ed3-27250a1edec8"), event_id=101, version=0)
class Microsoft_Windows_RemoteDesktopServices_RdpCoreTS_101_0(Etw):
    pattern = Struct(
        "ReasonString" / WString
    )


@declare(guid=guid("1139c61b-b549-4251-8ed3-27250a1edec8"), event_id=103, version=0)
class Microsoft_Windows_RemoteDesktopServices_RdpCoreTS_103_0(Etw):
    pattern = Struct(
        "ReasonCode" / Int32ul
    )


@declare(guid=guid("1139c61b-b549-4251-8ed3-27250a1edec8"), event_id=104, version=0)
class Microsoft_Windows_RemoteDesktopServices_RdpCoreTS_104_0(Etw):
    pattern = Struct(
        "TimezoneBiasHour" / WString
    )


@declare(guid=guid("1139c61b-b549-4251-8ed3-27250a1edec8"), event_id=129, version=0)
class Microsoft_Windows_RemoteDesktopServices_RdpCoreTS_129_0(Etw):
    pattern = Struct(
        "TransportProtocolName" / WString,
        "Port" / Int16ul
    )


@declare(guid=guid("1139c61b-b549-4251-8ed3-27250a1edec8"), event_id=130, version=0)
class Microsoft_Windows_RemoteDesktopServices_RdpCoreTS_130_0(Etw):
    pattern = Struct(
        "TunnelID" / Int32ul
    )


@declare(guid=guid("1139c61b-b549-4251-8ed3-27250a1edec8"), event_id=131, version=0)
class Microsoft_Windows_RemoteDesktopServices_RdpCoreTS_131_0(Etw):
    pattern = Struct(
        "ConnType" / WString,
        "ClientIP" / WString
    )


@declare(guid=guid("1139c61b-b549-4251-8ed3-27250a1edec8"), event_id=132, version=0)
class Microsoft_Windows_RemoteDesktopServices_RdpCoreTS_132_0(Etw):
    pattern = Struct(
        "ChannelName" / WString,
        "TunnelID" / Int32ul
    )


@declare(guid=guid("1139c61b-b549-4251-8ed3-27250a1edec8"), event_id=133, version=0)
class Microsoft_Windows_RemoteDesktopServices_RdpCoreTS_133_0(Etw):
    pattern = Struct(
        "TunnelID" / Int32ul,
        "RTT" / Int32ul,
        "Bandwidth" / Int32ul
    )


@declare(guid=guid("1139c61b-b549-4251-8ed3-27250a1edec8"), event_id=134, version=0)
class Microsoft_Windows_RemoteDesktopServices_RdpCoreTS_134_0(Etw):
    pattern = Struct(
        "ResultCode" / Int32ul,
        "TunnelID" / Int32ul,
        "RTT" / Int32ul,
        "Bandwidth" / Int32ul
    )


@declare(guid=guid("1139c61b-b549-4251-8ed3-27250a1edec8"), event_id=135, version=0)
class Microsoft_Windows_RemoteDesktopServices_RdpCoreTS_135_0(Etw):
    pattern = Struct(
        "TunnelID" / Int32ul,
        "TransportType" / WString
    )


@declare(guid=guid("1139c61b-b549-4251-8ed3-27250a1edec8"), event_id=137, version=0)
class Microsoft_Windows_RemoteDesktopServices_RdpCoreTS_137_0(Etw):
    pattern = Struct(
        "TunnelID" / Int32ul,
        "RTT" / Int32ul,
        "Bandwidth" / Int32ul
    )


@declare(guid=guid("1139c61b-b549-4251-8ed3-27250a1edec8"), event_id=138, version=0)
class Microsoft_Windows_RemoteDesktopServices_RdpCoreTS_138_0(Etw):
    pattern = Struct(
        "ResultCode" / Int32ul
    )


@declare(guid=guid("1139c61b-b549-4251-8ed3-27250a1edec8"), event_id=139, version=0)
class Microsoft_Windows_RemoteDesktopServices_RdpCoreTS_139_0(Etw):
    pattern = Struct(
        "ResultCode" / Int32ul,
        "IPString" / WString
    )


@declare(guid=guid("1139c61b-b549-4251-8ed3-27250a1edec8"), event_id=140, version=0)
class Microsoft_Windows_RemoteDesktopServices_RdpCoreTS_140_0(Etw):
    pattern = Struct(
        "IPString" / WString
    )


@declare(guid=guid("1139c61b-b549-4251-8ed3-27250a1edec8"), event_id=141, version=0)
class Microsoft_Windows_RemoteDesktopServices_RdpCoreTS_141_0(Etw):
    pattern = Struct(
        "InstanceID" / Int32ul
    )


@declare(guid=guid("1139c61b-b549-4251-8ed3-27250a1edec8"), event_id=142, version=0)
class Microsoft_Windows_RemoteDesktopServices_RdpCoreTS_142_0(Etw):
    pattern = Struct(
        "error" / Int32ul
    )


@declare(guid=guid("1139c61b-b549-4251-8ed3-27250a1edec8"), event_id=143, version=0)
class Microsoft_Windows_RemoteDesktopServices_RdpCoreTS_143_0(Etw):
    pattern = Struct(
        "error" / Int32ul
    )


@declare(guid=guid("1139c61b-b549-4251-8ed3-27250a1edec8"), event_id=145, version=0)
class Microsoft_Windows_RemoteDesktopServices_RdpCoreTS_145_0(Etw):
    pattern = Struct(
        "IdleSeconds" / Int32ul,
        "IdleSeconds1" / Int32ul,
        "IdleSeconds2" / Int32ul
    )


@declare(guid=guid("1139c61b-b549-4251-8ed3-27250a1edec8"), event_id=146, version=0)
class Microsoft_Windows_RemoteDesktopServices_RdpCoreTS_146_0(Etw):
    pattern = Struct(
        "Error" / WString
    )


@declare(guid=guid("1139c61b-b549-4251-8ed3-27250a1edec8"), event_id=147, version=0)
class Microsoft_Windows_RemoteDesktopServices_RdpCoreTS_147_0(Etw):
    pattern = Struct(
        "Error" / Int32ul
    )


@declare(guid=guid("1139c61b-b549-4251-8ed3-27250a1edec8"), event_id=148, version=0)
class Microsoft_Windows_RemoteDesktopServices_RdpCoreTS_148_0(Etw):
    pattern = Struct(
        "ChannelName" / WString,
        "TunnelID" / Int32ul
    )


@declare(guid=guid("1139c61b-b549-4251-8ed3-27250a1edec8"), event_id=149, version=0)
class Microsoft_Windows_RemoteDesktopServices_RdpCoreTS_149_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("1139c61b-b549-4251-8ed3-27250a1edec8"), event_id=150, version=0)
class Microsoft_Windows_RemoteDesktopServices_RdpCoreTS_150_0(Etw):
    pattern = Struct(
        "FlushTimeMs" / Int32ul,
        "FlushIntervalMs" / Int32ul
    )


@declare(guid=guid("1139c61b-b549-4251-8ed3-27250a1edec8"), event_id=151, version=0)
class Microsoft_Windows_RemoteDesktopServices_RdpCoreTS_151_0(Etw):
    pattern = Struct(
        "HistoryMs" / Int32ul,
        "NumHeartbeats" / Int32ul,
        "MaxRecentTimeNoPacketMs" / Int32ul,
        "MaxTotalTimeNoDataMs" / Int32ul,
        "MaxTotalTimeNoHeartbeatMs" / Int32ul,
        "MaxTotalTimeNoPacketMs" / Int32ul,
        "TimeNoLastPacketMs" / Int32ul
    )


@declare(guid=guid("1139c61b-b549-4251-8ed3-27250a1edec8"), event_id=152, version=0)
class Microsoft_Windows_RemoteDesktopServices_RdpCoreTS_152_0(Etw):
    pattern = Struct(
        "TimestampMs" / Int32ul,
        "NumHeartbeats" / Int32ul,
        "LastDataPacketMs" / Int32ul,
        "LastHeartbeatMs" / Int32ul
    )


@declare(guid=guid("1139c61b-b549-4251-8ed3-27250a1edec8"), event_id=153, version=0)
class Microsoft_Windows_RemoteDesktopServices_RdpCoreTS_153_0(Etw):
    pattern = Struct(
        "TLSVersion" / WString
    )


@declare(guid=guid("1139c61b-b549-4251-8ed3-27250a1edec8"), event_id=154, version=0)
class Microsoft_Windows_RemoteDesktopServices_RdpCoreTS_154_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("1139c61b-b549-4251-8ed3-27250a1edec8"), event_id=161, version=0)
class Microsoft_Windows_RemoteDesktopServices_RdpCoreTS_161_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "ServerName" / WString
    )


@declare(guid=guid("1139c61b-b549-4251-8ed3-27250a1edec8"), event_id=162, version=0)
class Microsoft_Windows_RemoteDesktopServices_RdpCoreTS_162_0(Etw):
    pattern = Struct(
        "Version" / Int32ul,
        "ClientMode" / Int32ul,
        "AvcEnabled" / Int32ul,
        "ProfileIdNum" / Int32ul,
        "ServerName" / WString
    )


@declare(guid=guid("1139c61b-b549-4251-8ed3-27250a1edec8"), event_id=163, version=0)
class Microsoft_Windows_RemoteDesktopServices_RdpCoreTS_163_0(Etw):
    pattern = Struct(
        "ServerName" / WString
    )


@declare(guid=guid("1139c61b-b549-4251-8ed3-27250a1edec8"), event_id=164, version=0)
class Microsoft_Windows_RemoteDesktopServices_RdpCoreTS_164_0(Etw):
    pattern = Struct(
        "ServerName" / WString
    )


@declare(guid=guid("1139c61b-b549-4251-8ed3-27250a1edec8"), event_id=165, version=0)
class Microsoft_Windows_RemoteDesktopServices_RdpCoreTS_165_0(Etw):
    pattern = Struct(
        "ServerName" / WString
    )


@declare(guid=guid("1139c61b-b549-4251-8ed3-27250a1edec8"), event_id=166, version=0)
class Microsoft_Windows_RemoteDesktopServices_RdpCoreTS_166_0(Etw):
    pattern = Struct(
        "ServerName" / WString
    )


@declare(guid=guid("1139c61b-b549-4251-8ed3-27250a1edec8"), event_id=167, version=0)
class Microsoft_Windows_RemoteDesktopServices_RdpCoreTS_167_0(Etw):
    pattern = Struct(
        "ServerName" / WString
    )


@declare(guid=guid("1139c61b-b549-4251-8ed3-27250a1edec8"), event_id=168, version=0)
class Microsoft_Windows_RemoteDesktopServices_RdpCoreTS_168_0(Etw):
    pattern = Struct(
        "MonitorNum" / Int32ul,
        "MonitorWidth" / Int32ul,
        "MonitorHeight" / Int32ul,
        "MonitorX" / Int32ul,
        "MonitorY" / Int32ul,
        "ServerName" / WString
    )


@declare(guid=guid("1139c61b-b549-4251-8ed3-27250a1edec8"), event_id=169, version=0)
class Microsoft_Windows_RemoteDesktopServices_RdpCoreTS_169_0(Etw):
    pattern = Struct(
        "MajorType" / Int32ul,
        "MinorType" / Int32ul,
        "ServerName" / WString
    )


@declare(guid=guid("1139c61b-b549-4251-8ed3-27250a1edec8"), event_id=170, version=0)
class Microsoft_Windows_RemoteDesktopServices_RdpCoreTS_170_0(Etw):
    pattern = Struct(
        "IsHardwareEncode" / Int32ul,
        "EncoderMFTName" / WString,
        "ServerName" / WString
    )


@declare(guid=guid("1139c61b-b549-4251-8ed3-27250a1edec8"), event_id=195, version=0)
class Microsoft_Windows_RemoteDesktopServices_RdpCoreTS_195_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("1139c61b-b549-4251-8ed3-27250a1edec8"), event_id=225, version=0)
class Microsoft_Windows_RemoteDesktopServices_RdpCoreTS_225_0(Etw):
    pattern = Struct(
        "StateTransition" / WString,
        "PreviousState" / Int32ul,
        "PreviousStateName" / WString,
        "NewState" / Int32ul,
        "NewStateName" / WString,
        "Event" / Int32ul,
        "EventName" / WString
    )


@declare(guid=guid("1139c61b-b549-4251-8ed3-27250a1edec8"), event_id=226, version=0)
class Microsoft_Windows_RemoteDesktopServices_RdpCoreTS_226_0(Etw):
    pattern = Struct(
        "StateTransition" / WString,
        "PreviousState" / Int32ul,
        "PreviousStateName" / WString,
        "NewState" / Int32ul,
        "NewStateName" / WString,
        "Event" / Int32ul,
        "EventName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("1139c61b-b549-4251-8ed3-27250a1edec8"), event_id=227, version=0)
class Microsoft_Windows_RemoteDesktopServices_RdpCoreTS_227_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Value" / Int32ul,
        "CustomLevel" / WString
    )


@declare(guid=guid("1139c61b-b549-4251-8ed3-27250a1edec8"), event_id=228, version=0)
class Microsoft_Windows_RemoteDesktopServices_RdpCoreTS_228_0(Etw):
    pattern = Struct(
        "ComponentName" / WString,
        "Message" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("1139c61b-b549-4251-8ed3-27250a1edec8"), event_id=229, version=0)
class Microsoft_Windows_RemoteDesktopServices_RdpCoreTS_229_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "CustomLevel" / WString
    )


@declare(guid=guid("1139c61b-b549-4251-8ed3-27250a1edec8"), event_id=289, version=0)
class Microsoft_Windows_RemoteDesktopServices_RdpCoreTS_289_0(Etw):
    pattern = Struct(
        "URL" / WString,
        "Port" / Int32ul,
        "ConnectionID" / WString
    )


@declare(guid=guid("1139c61b-b549-4251-8ed3-27250a1edec8"), event_id=291, version=0)
class Microsoft_Windows_RemoteDesktopServices_RdpCoreTS_291_0(Etw):
    pattern = Struct(
        "Error" / Int32ul
    )

