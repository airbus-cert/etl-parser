# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Runtime-Media
GUID : 8f0db3a8-299b-4d64-a4ed-907b409d4584
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=200, version=0)
class Microsoft_Windows_Runtime_Media_200_0(Etw):
    pattern = Struct(
        "WinRTCaptureEngine" / Int64ul,
        "AsyncOp" / Int64ul,
        "OpStatus" / Int32ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=201, version=0)
class Microsoft_Windows_Runtime_Media_201_0(Etw):
    pattern = Struct(
        "WinRTCaptureEngine" / Int64ul,
        "AsyncOp" / Int64ul,
        "OpStatus" / Int32ul,
        "AudioDeviceId" / WString,
        "VideoDeviceId" / WString
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=202, version=0)
class Microsoft_Windows_Runtime_Media_202_0(Etw):
    pattern = Struct(
        "WinRTCaptureEngine" / Int64ul,
        "AsyncOp" / Int64ul,
        "OpStatus" / Int32ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=203, version=0)
class Microsoft_Windows_Runtime_Media_203_0(Etw):
    pattern = Struct(
        "WinRTCaptureEngine" / Int64ul,
        "AsyncOp" / Int64ul,
        "OpStatus" / Int32ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=204, version=0)
class Microsoft_Windows_Runtime_Media_204_0(Etw):
    pattern = Struct(
        "WinRTCaptureEngine" / Int64ul,
        "AsyncOp" / Int64ul,
        "OpStatus" / Int32ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=205, version=0)
class Microsoft_Windows_Runtime_Media_205_0(Etw):
    pattern = Struct(
        "WinRTCaptureEngine" / Int64ul,
        "AsyncOp" / Int64ul,
        "OpStatus" / Int32ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=206, version=0)
class Microsoft_Windows_Runtime_Media_206_0(Etw):
    pattern = Struct(
        "WinRTCaptureEngine" / Int64ul,
        "AsyncOp" / Int64ul,
        "OpStatus" / Int32ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=207, version=0)
class Microsoft_Windows_Runtime_Media_207_0(Etw):
    pattern = Struct(
        "WinRTCaptureEngine" / Int64ul,
        "AsyncOp" / Int64ul,
        "OpStatus" / Int32ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=208, version=0)
class Microsoft_Windows_Runtime_Media_208_0(Etw):
    pattern = Struct(
        "WinRTCaptureEngine" / Int64ul,
        "AsyncOp" / Int64ul,
        "OpStatus" / Int32ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=209, version=0)
class Microsoft_Windows_Runtime_Media_209_0(Etw):
    pattern = Struct(
        "WinRTCaptureEngine" / Int64ul,
        "AsyncOp" / Int64ul,
        "OpStatus" / Int32ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=210, version=0)
class Microsoft_Windows_Runtime_Media_210_0(Etw):
    pattern = Struct(
        "WinRTCaptureEngine" / Int64ul,
        "AsyncOp" / Int64ul,
        "OpStatus" / Int32ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=211, version=0)
class Microsoft_Windows_Runtime_Media_211_0(Etw):
    pattern = Struct(
        "WinRTCaptureEngine" / Int64ul,
        "AsyncOp" / Int64ul,
        "OpStatus" / Int32ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=212, version=0)
class Microsoft_Windows_Runtime_Media_212_0(Etw):
    pattern = Struct(
        "WinRTCaptureEngine" / Int64ul,
        "AsyncOp" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=213, version=0)
class Microsoft_Windows_Runtime_Media_213_0(Etw):
    pattern = Struct(
        "Source" / Int64ul,
        "Sample" / Int64ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=214, version=0)
class Microsoft_Windows_Runtime_Media_214_0(Etw):
    pattern = Struct(
        "WinRTCaptureEngine" / Int64ul,
        "AsyncOp" / Int64ul,
        "OpStatus" / Int32ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=215, version=0)
class Microsoft_Windows_Runtime_Media_215_0(Etw):
    pattern = Struct(
        "WinRTCaptureEngine" / Int64ul,
        "AsyncOp" / Int64ul,
        "OpStatus" / Int32ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=216, version=0)
class Microsoft_Windows_Runtime_Media_216_0(Etw):
    pattern = Struct(
        "WinRTCaptureEngine" / Int64ul,
        "AsyncOp" / Int64ul,
        "OpStatus" / Int32ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=217, version=0)
class Microsoft_Windows_Runtime_Media_217_0(Etw):
    pattern = Struct(
        "WinRTCaptureEngine" / Int64ul,
        "AsyncOp" / Int64ul,
        "OpStatus" / Int32ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=218, version=0)
class Microsoft_Windows_Runtime_Media_218_0(Etw):
    pattern = Struct(
        "WinRTCaptureEngine" / Int64ul,
        "AsyncOp" / Int64ul,
        "OpStatus" / Int32ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=219, version=0)
class Microsoft_Windows_Runtime_Media_219_0(Etw):
    pattern = Struct(
        "WinRTCaptureEngine" / Int64ul,
        "AsyncOp" / Int64ul,
        "OpStatus" / Int32ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=220, version=0)
class Microsoft_Windows_Runtime_Media_220_0(Etw):
    pattern = Struct(
        "WinRTCaptureEngine" / Int64ul,
        "AsyncOp" / Int64ul,
        "OpStatus" / Int32ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=221, version=0)
class Microsoft_Windows_Runtime_Media_221_0(Etw):
    pattern = Struct(
        "WinRTCaptureEngine" / Int64ul,
        "AsyncOp" / Int64ul,
        "OpStatus" / Int32ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=222, version=0)
class Microsoft_Windows_Runtime_Media_222_0(Etw):
    pattern = Struct(
        "WinRTCaptureEngine" / Int64ul,
        "StartTime" / Int64sl,
        "CaptureTime" / Int64sl
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=223, version=0)
class Microsoft_Windows_Runtime_Media_223_0(Etw):
    pattern = Struct(
        "WinRTCaptureEngine" / Int64ul,
        "AsyncOp" / Int64ul,
        "OpStatus" / Int32ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=224, version=0)
class Microsoft_Windows_Runtime_Media_224_0(Etw):
    pattern = Struct(
        "WinRTCaptureEngine" / Int64ul,
        "AsyncOp" / Int64ul,
        "OpStatus" / Int32ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=225, version=0)
class Microsoft_Windows_Runtime_Media_225_0(Etw):
    pattern = Struct(
        "WinRTCaptureEngine" / Int64ul,
        "AsyncOp" / Int64ul,
        "OpStatus" / Int32ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=226, version=0)
class Microsoft_Windows_Runtime_Media_226_0(Etw):
    pattern = Struct(
        "WinRTCaptureEngine" / Int64ul,
        "AsyncOp" / Int64ul,
        "OpStatus" / Int32ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=227, version=0)
class Microsoft_Windows_Runtime_Media_227_0(Etw):
    pattern = Struct(
        "WinRTCaptureEngine" / Int64ul,
        "AsyncOp" / Int64ul,
        "OpStatus" / Int32ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=228, version=0)
class Microsoft_Windows_Runtime_Media_228_0(Etw):
    pattern = Struct(
        "WinRTCaptureEngine" / Int64ul,
        "AsyncOp" / Int64ul,
        "OpStatus" / Int32ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=229, version=0)
class Microsoft_Windows_Runtime_Media_229_0(Etw):
    pattern = Struct(
        "WinRTCaptureEngine" / Int64ul,
        "AsyncOp" / Int64ul,
        "OpStatus" / Int32ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=230, version=0)
class Microsoft_Windows_Runtime_Media_230_0(Etw):
    pattern = Struct(
        "WinRTCaptureEngine" / Int64ul,
        "AsyncOp" / Int64ul,
        "OpStatus" / Int32ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=231, version=0)
class Microsoft_Windows_Runtime_Media_231_0(Etw):
    pattern = Struct(
        "WinRTCaptureEngine" / Int64ul,
        "AsyncOp" / Int64ul,
        "OpStatus" / Int32ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=232, version=0)
class Microsoft_Windows_Runtime_Media_232_0(Etw):
    pattern = Struct(
        "WinRTCaptureEngine" / Int64ul,
        "AsyncOp" / Int64ul,
        "OpStatus" / Int32ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=233, version=0)
class Microsoft_Windows_Runtime_Media_233_0(Etw):
    pattern = Struct(
        "WinRTCaptureEngine" / Int64ul,
        "AsyncOp" / Int64ul,
        "OpStatus" / Int32ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=234, version=0)
class Microsoft_Windows_Runtime_Media_234_0(Etw):
    pattern = Struct(
        "WinRTCaptureEngine" / Int64ul,
        "AsyncOp" / Int64ul,
        "OpStatus" / Int32ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=235, version=0)
class Microsoft_Windows_Runtime_Media_235_0(Etw):
    pattern = Struct(
        "WinRTCaptureEngine" / Int64ul,
        "AsyncOp" / Int64ul,
        "OpStatus" / Int32ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=236, version=0)
class Microsoft_Windows_Runtime_Media_236_0(Etw):
    pattern = Struct(
        "WinRTCaptureEngine" / Int64ul,
        "AsyncOp" / Int64ul,
        "OpStatus" / Int32ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=237, version=0)
class Microsoft_Windows_Runtime_Media_237_0(Etw):
    pattern = Struct(
        "WinRTCaptureEngine" / Int64ul,
        "AsyncOp" / Int64ul,
        "OpStatus" / Int32ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=238, version=0)
class Microsoft_Windows_Runtime_Media_238_0(Etw):
    pattern = Struct(
        "WinRTCaptureEngine" / Int64ul,
        "AsyncOp" / Int64ul,
        "OpStatus" / Int32ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=239, version=0)
class Microsoft_Windows_Runtime_Media_239_0(Etw):
    pattern = Struct(
        "WinRTCaptureEngine" / Int64ul,
        "AsyncOp" / Int64ul,
        "OpStatus" / Int32ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=240, version=0)
class Microsoft_Windows_Runtime_Media_240_0(Etw):
    pattern = Struct(
        "WinRTCaptureEngine" / Int64ul,
        "AsyncOp" / Int64ul,
        "OpStatus" / Int32ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=241, version=0)
class Microsoft_Windows_Runtime_Media_241_0(Etw):
    pattern = Struct(
        "WinRTCaptureEngine" / Int64ul,
        "AsyncOp" / Int64ul,
        "OpStatus" / Int32ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=242, version=0)
class Microsoft_Windows_Runtime_Media_242_0(Etw):
    pattern = Struct(
        "WinRTCaptureEngine" / Int64ul,
        "AsyncOp" / Int64ul,
        "OpStatus" / Int32ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=243, version=0)
class Microsoft_Windows_Runtime_Media_243_0(Etw):
    pattern = Struct(
        "WinRTCaptureEngine" / Int64ul,
        "ExecutablePath" / WString
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=244, version=0)
class Microsoft_Windows_Runtime_Media_244_0(Etw):
    pattern = Struct(
        "WinRTCaptureEngine" / Int64ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=245, version=0)
class Microsoft_Windows_Runtime_Media_245_0(Etw):
    pattern = Struct(
        "SamplePtr" / Int64ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=246, version=0)
class Microsoft_Windows_Runtime_Media_246_0(Etw):
    pattern = Struct(
        "FocusState" / Int32ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=300, version=0)
class Microsoft_Windows_Runtime_Media_300_0(Etw):
    pattern = Struct(
        "Transcode" / Int64ul,
        "EngineType" / Int32ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=301, version=0)
class Microsoft_Windows_Runtime_Media_301_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=302, version=0)
class Microsoft_Windows_Runtime_Media_302_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=303, version=0)
class Microsoft_Windows_Runtime_Media_303_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=304, version=0)
class Microsoft_Windows_Runtime_Media_304_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=305, version=0)
class Microsoft_Windows_Runtime_Media_305_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=306, version=0)
class Microsoft_Windows_Runtime_Media_306_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=307, version=0)
class Microsoft_Windows_Runtime_Media_307_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=308, version=0)
class Microsoft_Windows_Runtime_Media_308_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=309, version=0)
class Microsoft_Windows_Runtime_Media_309_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=310, version=0)
class Microsoft_Windows_Runtime_Media_310_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=311, version=0)
class Microsoft_Windows_Runtime_Media_311_0(Etw):
    pattern = Struct(
        "transcode" / Int64ul,
        "remuxing" / Int8ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=312, version=0)
class Microsoft_Windows_Runtime_Media_312_0(Etw):
    pattern = Struct(
        "WinRTCaptureEngine" / Int64ul,
        "AsyncOp" / Int64ul,
        "OpStatus" / Int32ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=313, version=0)
class Microsoft_Windows_Runtime_Media_313_0(Etw):
    pattern = Struct(
        "WinRTCaptureEngine" / Int64ul,
        "AsyncOp" / Int64ul,
        "OpStatus" / Int32ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=314, version=0)
class Microsoft_Windows_Runtime_Media_314_0(Etw):
    pattern = Struct(
        "MediaCapture" / Int64ul,
        "ThermalStatus" / Int32ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=315, version=0)
class Microsoft_Windows_Runtime_Media_315_0(Etw):
    pattern = Struct(
        "WinRTCaptureEngine" / Int64ul,
        "AsyncOp" / Int64ul,
        "OpStatus" / Int32ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=316, version=0)
class Microsoft_Windows_Runtime_Media_316_0(Etw):
    pattern = Struct(
        "WinRTCaptureEngine" / Int64ul,
        "AsyncOp" / Int64ul,
        "OpStatus" / Int32ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=317, version=0)
class Microsoft_Windows_Runtime_Media_317_0(Etw):
    pattern = Struct(
        "WinRTCaptureEngine" / Int64ul,
        "AsyncOp" / Int64ul,
        "OpStatus" / Int32ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=318, version=0)
class Microsoft_Windows_Runtime_Media_318_0(Etw):
    pattern = Struct(
        "WinRTCaptureEngine" / Int64ul,
        "AsyncOp" / Int64ul,
        "OpStatus" / Int32ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=319, version=0)
class Microsoft_Windows_Runtime_Media_319_0(Etw):
    pattern = Struct(
        "WinRTCaptureEngine" / Int64ul,
        "AsyncOp" / Int64ul,
        "OpStatus" / Int32ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=320, version=0)
class Microsoft_Windows_Runtime_Media_320_0(Etw):
    pattern = Struct(
        "WinRTCaptureEngine" / Int64ul,
        "AsyncOp" / Int64ul,
        "OpStatus" / Int32ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=500, version=0)
class Microsoft_Windows_Runtime_Media_500_0(Etw):
    pattern = Struct(
        "MediaStreamSource" / Int64ul,
        "EventObject" / Int64ul,
        "EventType" / Int32ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=501, version=0)
class Microsoft_Windows_Runtime_Media_501_0(Etw):
    pattern = Struct(
        "MediaStreamSource" / Int64ul,
        "EventObject" / Int64ul,
        "EventType" / Int32ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=502, version=0)
class Microsoft_Windows_Runtime_Media_502_0(Etw):
    pattern = Struct(
        "MediaStreamSource" / Int64ul,
        "EventObject" / Int64ul,
        "EventType" / Int32ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=503, version=0)
class Microsoft_Windows_Runtime_Media_503_0(Etw):
    pattern = Struct(
        "MediaStreamSource" / Int64ul,
        "EventObject" / Int64ul,
        "StreamId" / Int32ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=504, version=0)
class Microsoft_Windows_Runtime_Media_504_0(Etw):
    pattern = Struct(
        "MediaStreamSource" / Int64ul,
        "EventObject" / Int64ul,
        "StreamId" / Int32ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=505, version=0)
class Microsoft_Windows_Runtime_Media_505_0(Etw):
    pattern = Struct(
        "MediaStreamSource" / Int64ul,
        "EventObject" / Int64ul,
        "StreamId" / Int32ul,
        "MediaStreamSample" / Int64ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=600, version=0)
class Microsoft_Windows_Runtime_Media_600_0(Etw):
    pattern = Struct(
        "AdaptiveMediaSource" / Int64ul,
        "SourceBufferManager" / Int64ul,
        "BufferLevel" / Int64sl
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=601, version=0)
class Microsoft_Windows_Runtime_Media_601_0(Etw):
    pattern = Struct(
        "AdaptiveMediaSource" / Int64ul,
        "SourceBufferManager" / Int64ul,
        "BufferLevel" / Int64sl
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=602, version=0)
class Microsoft_Windows_Runtime_Media_602_0(Etw):
    pattern = Struct(
        "AdaptiveMediaSource" / Int64ul,
        "SourceBufferManager" / Int64ul,
        "BufferLevel" / Int64sl
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=603, version=0)
class Microsoft_Windows_Runtime_Media_603_0(Etw):
    pattern = Struct(
        "AdaptiveMediaSource" / Int64ul,
        "SourceBufferManager" / Int64ul,
        "BufferLevel" / Int64sl
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=604, version=0)
class Microsoft_Windows_Runtime_Media_604_0(Etw):
    pattern = Struct(
        "AdaptiveMediaSource" / Int64ul,
        "SourceBufferManager" / Int64ul,
        "BufferLevel" / Int64sl
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=605, version=0)
class Microsoft_Windows_Runtime_Media_605_0(Etw):
    pattern = Struct(
        "AdaptiveMediaSource" / Int64ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=606, version=0)
class Microsoft_Windows_Runtime_Media_606_0(Etw):
    pattern = Struct(
        "AdaptiveMediaSource" / Int64ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=607, version=0)
class Microsoft_Windows_Runtime_Media_607_0(Etw):
    pattern = Struct(
        "AdaptiveMediaSource" / Int64ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=608, version=0)
class Microsoft_Windows_Runtime_Media_608_0(Etw):
    pattern = Struct(
        "AdaptiveMediaSource" / Int64ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=609, version=0)
class Microsoft_Windows_Runtime_Media_609_0(Etw):
    pattern = Struct(
        "AdaptiveMediaSource" / Int64ul
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=610, version=0)
class Microsoft_Windows_Runtime_Media_610_0(Etw):
    pattern = Struct(
        "AdaptiveMediaSource" / Int64ul,
        "StopReason" / Int32sl
    )


@declare(guid=guid("8f0db3a8-299b-4d64-a4ed-907b409d4584"), event_id=611, version=0)
class Microsoft_Windows_Runtime_Media_611_0(Etw):
    pattern = Struct(
        "AdaptiveMediaSource" / Int64ul,
        "BytesTransferred" / Int64sl,
        "BytesTotal" / Int64sl
    )

