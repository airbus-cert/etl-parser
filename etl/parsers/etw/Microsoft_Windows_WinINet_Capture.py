# -*- coding: utf-8 -*-
"""
Microsoft-Windows-WinINet-Capture
GUID : a70ff94f-570b-4979-ba5c-e59c9feab61b
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("a70ff94f-570b-4979-ba5c-e59c9feab61b"), event_id=2001, version=0)
class Microsoft_Windows_WinINet_Capture_2001_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "SequenceNumber" / Int32ul,
        "Flags" / Int32ul,
        "PayloadByteLength" / Int32ul,
        "Payload" / Bytes(lambda this: this.PayloadByteLength)
    )


@declare(guid=guid("a70ff94f-570b-4979-ba5c-e59c9feab61b"), event_id=2002, version=0)
class Microsoft_Windows_WinINet_Capture_2002_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "SequenceNumber" / Int32ul,
        "Flags" / Int32ul,
        "PayloadByteLength" / Int32ul,
        "Payload" / Bytes(lambda this: this.PayloadByteLength)
    )


@declare(guid=guid("a70ff94f-570b-4979-ba5c-e59c9feab61b"), event_id=2003, version=0)
class Microsoft_Windows_WinINet_Capture_2003_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "SequenceNumber" / Int32ul,
        "Flags" / Int32ul,
        "PayloadByteLength" / Int32ul,
        "Payload" / Bytes(lambda this: this.PayloadByteLength)
    )


@declare(guid=guid("a70ff94f-570b-4979-ba5c-e59c9feab61b"), event_id=2004, version=0)
class Microsoft_Windows_WinINet_Capture_2004_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "SequenceNumber" / Int32ul,
        "Flags" / Int32ul,
        "PayloadByteLength" / Int32ul,
        "Payload" / Bytes(lambda this: this.PayloadByteLength)
    )

