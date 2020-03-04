# -*- coding: utf-8 -*-
"""
Microsoft-Windows-DXGIDebug
GUID : f1ff64ef-faf3-5699-8e51-f6ec2fbd97d1
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("f1ff64ef-faf3-5699-8e51-f6ec2fbd97d1"), event_id=1, version=0)
class Microsoft_Windows_DXGIDebug_1_0(Etw):
    pattern = Struct(
        "Producer" / Guid,
        "pProducer" / Int64ul,
        "Category" / Int32ul,
        "Severity" / Int32ul,
        "ID" / Int32ul,
        "DebugMessageByteLength" / Int32ul,
        "DebugMessage" / Bytes(lambda this: this.DebugMessageByteLength)
    )


@declare(guid=guid("f1ff64ef-faf3-5699-8e51-f6ec2fbd97d1"), event_id=2, version=0)
class Microsoft_Windows_DXGIDebug_2_0(Etw):
    pattern = Struct(
        "Producer" / Guid,
        "pProducer" / Int64ul,
        "Category" / Int32ul,
        "Severity" / Int32ul,
        "ID" / Int32ul,
        "DebugMessageByteLength" / Int32ul,
        "DebugMessage" / Bytes(lambda this: this.DebugMessageByteLength)
    )


@declare(guid=guid("f1ff64ef-faf3-5699-8e51-f6ec2fbd97d1"), event_id=3, version=0)
class Microsoft_Windows_DXGIDebug_3_0(Etw):
    pattern = Struct(
        "Producer" / Guid,
        "pProducer" / Int64ul,
        "Category" / Int32ul,
        "Severity" / Int32ul,
        "ID" / Int32ul,
        "DebugMessageByteLength" / Int32ul,
        "DebugMessage" / Bytes(lambda this: this.DebugMessageByteLength)
    )


@declare(guid=guid("f1ff64ef-faf3-5699-8e51-f6ec2fbd97d1"), event_id=4, version=0)
class Microsoft_Windows_DXGIDebug_4_0(Etw):
    pattern = Struct(
        "Producer" / Guid,
        "pProducer" / Int64ul,
        "Category" / Int32ul,
        "Severity" / Int32ul,
        "ID" / Int32ul,
        "DebugMessageByteLength" / Int32ul,
        "DebugMessage" / Bytes(lambda this: this.DebugMessageByteLength)
    )

