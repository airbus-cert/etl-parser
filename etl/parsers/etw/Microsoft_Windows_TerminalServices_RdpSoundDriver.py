# -*- coding: utf-8 -*-
"""
Microsoft-Windows-TerminalServices-RdpSoundDriver
GUID : 127e0dc5-e13b-4935-985e-78fd508b1d80
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("127e0dc5-e13b-4935-985e-78fd508b1d80"), event_id=1000, version=0)
class Microsoft_Windows_TerminalServices_RdpSoundDriver_1000_0(Etw):
    pattern = Struct(
        "UInt32_1" / Int32ul,
        "UInt32_2" / Int32ul,
        "SessionID" / Int32ul
    )


@declare(guid=guid("127e0dc5-e13b-4935-985e-78fd508b1d80"), event_id=1001, version=0)
class Microsoft_Windows_TerminalServices_RdpSoundDriver_1001_0(Etw):
    pattern = Struct(
        "UINT16_FORMAT_TAG" / Int16ul,
        "UINT16_NUM_CHANNELS" / Int16ul,
        "UINT32_SAMPLES_PER_SECOND" / Int32ul,
        "UINT32_AVERAGE_BYTES_PER_SECOND" / Int32ul,
        "UINT16_BLOCK_ALIGN" / Int16ul,
        "UINT16_BITS_PER_SAMPLE" / Int16ul,
        "UINT16_STRUCTURE_SIZE" / Int16ul,
        "SessionID" / Int32ul
    )


@declare(guid=guid("127e0dc5-e13b-4935-985e-78fd508b1d80"), event_id=1002, version=0)
class Microsoft_Windows_TerminalServices_RdpSoundDriver_1002_0(Etw):
    pattern = Struct(
        "UINT16_FORMAT_TAG" / Int16ul,
        "UINT16_NUM_CHANNELS" / Int16ul,
        "UINT32_SAMPLES_PER_SECOND" / Int32ul,
        "UINT32_AVERAGE_BYTES_PER_SECOND" / Int32ul,
        "UINT16_BLOCK_ALIGN" / Int16ul,
        "UINT16_BITS_PER_SAMPLE" / Int16ul,
        "UINT16_STRUCTURE_SIZE" / Int16ul,
        "SessionID" / Int32ul
    )


@declare(guid=guid("127e0dc5-e13b-4935-985e-78fd508b1d80"), event_id=1003, version=0)
class Microsoft_Windows_TerminalServices_RdpSoundDriver_1003_0(Etw):
    pattern = Struct(
        "StringParameter" / WString,
        "UInt32Parameter" / Int32ul,
        "SessionID" / Int32ul
    )


@declare(guid=guid("127e0dc5-e13b-4935-985e-78fd508b1d80"), event_id=1004, version=0)
class Microsoft_Windows_TerminalServices_RdpSoundDriver_1004_0(Etw):
    pattern = Struct(
        "StringParameter" / WString,
        "UInt32Parameter" / Int32ul,
        "SessionID" / Int32ul
    )


@declare(guid=guid("127e0dc5-e13b-4935-985e-78fd508b1d80"), event_id=1005, version=0)
class Microsoft_Windows_TerminalServices_RdpSoundDriver_1005_0(Etw):
    pattern = Struct(
        "StringParameter" / WString,
        "UInt32Parameter" / Int32ul,
        "SessionID" / Int32ul
    )


@declare(guid=guid("127e0dc5-e13b-4935-985e-78fd508b1d80"), event_id=1006, version=0)
class Microsoft_Windows_TerminalServices_RdpSoundDriver_1006_0(Etw):
    pattern = Struct(
        "StringParameter" / WString,
        "UInt32Parameter" / Int32ul,
        "SessionID" / Int32ul
    )


@declare(guid=guid("127e0dc5-e13b-4935-985e-78fd508b1d80"), event_id=1007, version=0)
class Microsoft_Windows_TerminalServices_RdpSoundDriver_1007_0(Etw):
    pattern = Struct(
        "StringParameter" / WString,
        "UInt32Parameter" / Int32ul,
        "SessionID" / Int32ul
    )


@declare(guid=guid("127e0dc5-e13b-4935-985e-78fd508b1d80"), event_id=1008, version=0)
class Microsoft_Windows_TerminalServices_RdpSoundDriver_1008_0(Etw):
    pattern = Struct(
        "StringParameter" / WString,
        "UInt32Parameter" / Int32ul,
        "SessionID" / Int32ul
    )


@declare(guid=guid("127e0dc5-e13b-4935-985e-78fd508b1d80"), event_id=1009, version=0)
class Microsoft_Windows_TerminalServices_RdpSoundDriver_1009_0(Etw):
    pattern = Struct(
        "StringParameter" / WString,
        "UInt32Parameter" / Int32ul,
        "SessionID" / Int32ul
    )


@declare(guid=guid("127e0dc5-e13b-4935-985e-78fd508b1d80"), event_id=2003, version=0)
class Microsoft_Windows_TerminalServices_RdpSoundDriver_2003_0(Etw):
    pattern = Struct(
        "StringParameter" / WString,
        "UInt32Parameter" / Int32ul,
        "SessionID" / Int32ul
    )


@declare(guid=guid("127e0dc5-e13b-4935-985e-78fd508b1d80"), event_id=2004, version=0)
class Microsoft_Windows_TerminalServices_RdpSoundDriver_2004_0(Etw):
    pattern = Struct(
        "StringParameter" / WString,
        "UInt32Parameter" / Int32ul,
        "SessionID" / Int32ul
    )


@declare(guid=guid("127e0dc5-e13b-4935-985e-78fd508b1d80"), event_id=2005, version=0)
class Microsoft_Windows_TerminalServices_RdpSoundDriver_2005_0(Etw):
    pattern = Struct(
        "StringParameter" / WString,
        "UInt32Parameter" / Int32ul,
        "SessionID" / Int32ul
    )


@declare(guid=guid("127e0dc5-e13b-4935-985e-78fd508b1d80"), event_id=2006, version=0)
class Microsoft_Windows_TerminalServices_RdpSoundDriver_2006_0(Etw):
    pattern = Struct(
        "StringParameter" / WString,
        "UInt32Parameter" / Int32ul,
        "SessionID" / Int32ul
    )


@declare(guid=guid("127e0dc5-e13b-4935-985e-78fd508b1d80"), event_id=2007, version=0)
class Microsoft_Windows_TerminalServices_RdpSoundDriver_2007_0(Etw):
    pattern = Struct(
        "StringParameter" / WString,
        "UInt32Parameter" / Int32ul,
        "SessionID" / Int32ul
    )


@declare(guid=guid("127e0dc5-e13b-4935-985e-78fd508b1d80"), event_id=2008, version=0)
class Microsoft_Windows_TerminalServices_RdpSoundDriver_2008_0(Etw):
    pattern = Struct(
        "StringParameter" / WString,
        "UInt32Parameter" / Int32ul,
        "SessionID" / Int32ul
    )


@declare(guid=guid("127e0dc5-e13b-4935-985e-78fd508b1d80"), event_id=2009, version=0)
class Microsoft_Windows_TerminalServices_RdpSoundDriver_2009_0(Etw):
    pattern = Struct(
        "StringParameter" / WString,
        "UInt32Parameter" / Int32ul,
        "SessionID" / Int32ul
    )

