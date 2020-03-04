# -*- coding: utf-8 -*-
"""
Microsoft-Windows-MediaFoundation-MFCaptureEngine
GUID : b8197c10-845f-40ca-82ab-9341e98cfc2b
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=200, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_200_0(Etw):
    pattern = Struct(
        "CaptureEnginePointer" / Int64ul,
        "hrStatus" / Int32ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=201, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_201_0(Etw):
    pattern = Struct(
        "CaptureEnginePointer" / Int64ul,
        "hrStatus" / Int32ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=202, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_202_0(Etw):
    pattern = Struct(
        "CaptureEnginePointer" / Int64ul,
        "hrStatus" / Int32ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=203, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_203_0(Etw):
    pattern = Struct(
        "CaptureEnginePointer" / Int64ul,
        "hrStatus" / Int32ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=204, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_204_0(Etw):
    pattern = Struct(
        "CaptureEnginePointer" / Int64ul,
        "hrStatus" / Int32ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=205, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_205_0(Etw):
    pattern = Struct(
        "CaptureEnginePointer" / Int64ul,
        "hrStatus" / Int32ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=206, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_206_0(Etw):
    pattern = Struct(
        "CaptureEnginePointer" / Int64ul,
        "hrStatus" / Int32ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=207, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_207_0(Etw):
    pattern = Struct(
        "CaptureEnginePointer" / Int64ul,
        "hrStatus" / Int32ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=208, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_208_0(Etw):
    pattern = Struct(
        "CaptureEnginePointer" / Int64ul,
        "hrStatus" / Int32ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=209, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_209_0(Etw):
    pattern = Struct(
        "CaptureEnginePointer" / Int64ul,
        "hrStatus" / Int32ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=210, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_210_0(Etw):
    pattern = Struct(
        "CaptureEnginePointer" / Int64ul,
        "hrStatus" / Int32ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=211, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_211_0(Etw):
    pattern = Struct(
        "CaptureEnginePointer" / Int64ul,
        "hrStatus" / Int32ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=212, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_212_0(Etw):
    pattern = Struct(
        "CaptureEnginePointer" / Int64ul,
        "hrStatus" / Int32ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=213, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_213_0(Etw):
    pattern = Struct(
        "CaptureEnginePointer" / Int64ul,
        "hrStatus" / Int32ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=214, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_214_0(Etw):
    pattern = Struct(
        "Source" / Int64ul,
        "StreamIndex" / Int32ul,
        "ControlFlags" / Int32ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=215, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_215_0(Etw):
    pattern = Struct(
        "Source" / Int64ul,
        "Sample" / Int64ul,
        "Timestamp" / Int64ul,
        "RefTimestamp" / Int64ul,
        "StreamIndex" / Int32ul,
        "StreamFlags" / Int32ul,
        "hrStatus" / Int32ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=216, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_216_0(Etw):
    pattern = Struct(
        "SourceOrSinkPointer" / Int64ul,
        "Sample" / Int64ul,
        "SourceStreamIndex" / Int32ul,
        "SinkStreamIndex" / Int32ul,
        "Timestamp" / Int64ul,
        "RefTimestamp" / Int64ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=217, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_217_0(Etw):
    pattern = Struct(
        "SourceOrSinkPointer" / Int64ul,
        "Sample" / Int64ul,
        "SourceStreamIndex" / Int32ul,
        "SinkStreamIndex" / Int32ul,
        "Timestamp" / Int64ul,
        "RefTimestamp" / Int64ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=218, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_218_0(Etw):
    pattern = Struct(
        "SourceOrSinkPointer" / Int64ul,
        "Sample" / Int64ul,
        "SourceStreamIndex" / Int32ul,
        "SinkStreamIndex" / Int32ul,
        "Timestamp" / Int64ul,
        "RefTimestamp" / Int64ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=219, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_219_0(Etw):
    pattern = Struct(
        "SinkPointer" / Int64ul,
        "SamplePointer" / Int64ul,
        "SinkStreamIndex" / Int32ul,
        "Timestamp" / Int64ul,
        "RefTimestamp" / Int64ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=220, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_220_0(Etw):
    pattern = Struct(
        "SinkPointer" / Int64ul,
        "SamplePointer" / Int64ul,
        "SinkStreamIndex" / Int32ul,
        "Timestamp" / Int64ul,
        "RefTimestamp" / Int64ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=221, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_221_0(Etw):
    pattern = Struct(
        "PhotoSink" / Int64ul,
        "Sample" / Int64ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=222, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_222_0(Etw):
    pattern = Struct(
        "PhotoSink" / Int64ul,
        "Sample" / Int64ul,
        "hrStatus" / Int32ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=223, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_223_0(Etw):
    pattern = Struct(
        "PhotoSink" / Int64ul,
        "hrStatus" / Int32ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=224, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_224_0(Etw):
    pattern = Struct(
        "PhotoSink" / Int64ul,
        "hrStatus" / Int32ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=225, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_225_0(Etw):
    pattern = Struct(
        "PhotoSink" / Int64ul,
        "hrStatus" / Int32ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=226, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_226_0(Etw):
    pattern = Struct(
        "PhotoSink" / Int64ul,
        "hrStatus" / Int32ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=227, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_227_0(Etw):
    pattern = Struct(
        "PhotoSink" / Int64ul,
        "hrStatus" / Int32ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=228, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_228_0(Etw):
    pattern = Struct(
        "PhotoSink" / Int64ul,
        "hrStatus" / Int32ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=229, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_229_0(Etw):
    pattern = Struct(
        "PhotoSink" / Int64ul,
        "hrStatus" / Int32ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=230, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_230_0(Etw):
    pattern = Struct(
        "PhotoSink" / Int64ul,
        "hrStatus" / Int32ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=231, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_231_0(Etw):
    pattern = Struct(
        "CaptureEnginePointer" / Int64ul,
        "Source" / Int64ul,
        "RecordSink" / Int64ul,
        "PreviewSink" / Int64ul,
        "PhotoSink" / Int64ul,
        "FrameReaderSink" / Int64ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=232, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_232_0(Etw):
    pattern = Struct(
        "Sample" / Int64ul,
        "SampleTimestamp" / Int64ul,
        "RefTimestamp" / Int64ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=233, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_233_0(Etw):
    pattern = Struct(
        "Sample" / Int64ul,
        "SampleTimestamp" / Int64ul,
        "RefTimestamp" / Int64ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=234, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_234_0(Etw):
    pattern = Struct(
        "Sample" / Int64ul,
        "SampleTimestamp" / Int64ul,
        "RefTimestamp" / Int64ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=235, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_235_0(Etw):
    pattern = Struct(
        "Sample" / Int64ul,
        "SampleTimestamp" / Int64ul,
        "RefTimestamp" / Int64ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=236, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_236_0(Etw):
    pattern = Struct(
        "RecordSinkWriter" / Int64ul,
        "SinkStreamIndex" / Int32ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=237, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_237_0(Etw):
    pattern = Struct(
        "PreviewSinkWriter" / Int64ul,
        "SinkStreamIndex" / Int32ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=238, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_238_0(Etw):
    pattern = Struct(
        "PhotoSink" / Int64ul,
        "XVP" / Int64ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=239, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_239_0(Etw):
    pattern = Struct(
        "SinkPointer" / Int64ul,
        "SamplePointer" / Int64ul,
        "SinkStreamIndex" / Int32ul,
        "Timestamp" / Int64ul,
        "RefTimestamp" / Int64ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=240, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_240_0(Etw):
    pattern = Struct(
        "Pointer" / Int64ul,
        "dwStreamIndex" / Int32ul,
        "hrStatus" / Int32ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=241, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_241_0(Etw):
    pattern = Struct(
        "Pointer" / Int64ul,
        "dwStreamIndex" / Int32ul,
        "hrStatus" / Int32ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=242, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_242_0(Etw):
    pattern = Struct(
        "Pointer" / Int64ul,
        "dwSourceStreamIndex" / Int32ul,
        "pMediaType" / CString,
        "HResult" / Int32ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=243, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_243_0(Etw):
    pattern = Struct(
        "Pointer" / Int64ul,
        "dwSourceStreamIndex" / Int32ul,
        "pMediaType" / CString,
        "HResult" / Int32ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=244, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_244_0(Etw):
    pattern = Struct(
        "Pointer" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=245, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_245_0(Etw):
    pattern = Struct(
        "Pointer" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=246, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_246_0(Etw):
    pattern = Struct(
        "Pointer" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=247, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_247_0(Etw):
    pattern = Struct(
        "Pointer" / Int64ul,
        "dwSourceStreamIndex" / Int32ul,
        "guidPropertySet" / Guid,
        "propertyID" / Int32ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=248, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_248_0(Etw):
    pattern = Struct(
        "Pointer" / Int64ul,
        "dwSourceStreamIndex" / Int32ul,
        "guidPropertySet" / Guid,
        "propertyID" / Int32ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=249, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_249_0(Etw):
    pattern = Struct(
        "Pointer" / Int64ul,
        "dwSourceStreamIndex" / Int32ul,
        "guidPropertySet" / Guid,
        "propertyID" / Int32ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=250, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_250_0(Etw):
    pattern = Struct(
        "Pointer" / Int64ul,
        "dwSourceStreamIndex" / Int32ul,
        "guidPropertySet" / Guid,
        "propertyID" / Int32ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=251, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_251_0(Etw):
    pattern = Struct(
        "CaptureEnginePointer" / Int64ul,
        "hrStatus" / Int32ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=252, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_252_0(Etw):
    pattern = Struct(
        "CaptureEnginePointer" / Int64ul,
        "hrStatus" / Int32ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=253, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_253_0(Etw):
    pattern = Struct(
        "Pointer" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=254, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_254_0(Etw):
    pattern = Struct(
        "Pointer" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=255, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_255_0(Etw):
    pattern = Struct(
        "CaptureEnginePointer" / Int64ul,
        "hrStatus" / Int32ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=256, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_256_0(Etw):
    pattern = Struct(
        "CaptureEnginePointer" / Int64ul,
        "hrStatus" / Int32ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=257, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_257_0(Etw):
    pattern = Struct(
        "Pointer" / Int64ul,
        "dwSourceStreamIndex" / Int32ul,
        "pMediaType" / CString,
        "dwSinkStreamIndex" / Int32ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=258, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_258_0(Etw):
    pattern = Struct(
        "guidExtendedType" / Guid,
        "HResult" / Int32sl,
        "StreamIndex" / Int32ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=259, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_259_0(Etw):
    pattern = Struct(
        "Pointer" / Int64ul,
        "dwSourceStreamIndex" / Int32ul,
        "dwMediaTypeIndex" / Int32ul,
        "pMediaType" / CString,
        "HResult" / Int32ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=260, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_260_0(Etw):
    pattern = Struct(
        "Pointer" / Int64ul,
        "dwSourceStreamIndex" / Int32ul,
        "dwMediaTypeIndex" / Int32ul,
        "pMediaType" / CString,
        "HResult" / Int32ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=261, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_261_0(Etw):
    pattern = Struct(
        "CaptureSource" / Int64ul,
        "SinkWrapper" / Int64ul,
        "bChangeStreamUsers" / Int8ul,
        "bPrepare" / Int8ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=262, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_262_0(Etw):
    pattern = Struct(
        "CaptureSource" / Int64ul,
        "SinkWrapper" / Int64ul,
        "bChangeStreamUsers" / Int8ul,
        "bPrepare" / Int8ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=263, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_263_0(Etw):
    pattern = Struct(
        "SourcePointer" / Int64ul,
        "SourceStreamIndex" / Int32ul,
        "StreamType" / Int32ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=264, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_264_0(Etw):
    pattern = Struct(
        "CameraSoundState" / CString,
        "CameraSoundLevel" / Int32ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=265, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_265_0(Etw):
    pattern = Struct(
        "CameraSoundObject" / Int64ul,
        "InitResult" / Int32ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=266, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_266_0(Etw):
    pattern = Struct(
        "CaptureEngineObject" / Int64ul,
        "QueuingResult" / Int32ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=267, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_267_0(Etw):
    pattern = Struct(
        "CaptureEngineObject" / Int64ul,
        "QueuingResult" / Int32ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=268, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_268_0(Etw):
    pattern = Struct(
        "CaptureEngineObject" / Int64ul,
        "PlaybackResult" / Int32ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=269, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_269_0(Etw):
    pattern = Struct(
        "CaptureEngineObject" / Int64ul,
        "PlaybackResult" / Int32ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=270, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_270_0(Etw):
    pattern = Struct(
        "SinkPointer" / Int64ul,
        "SamplePointer" / Int64ul,
        "SinkStreamIndex" / Int32ul,
        "Timestamp" / Int64ul,
        "RefTimestamp" / Int64ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=271, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_271_0(Etw):
    pattern = Struct(
        "SinkPointer" / Int64ul,
        "SamplePointer" / Int64ul,
        "SinkStreamIndex" / Int32ul,
        "Timestamp" / Int64ul,
        "RefTimestamp" / Int64ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=272, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_272_0(Etw):
    pattern = Struct(
        "RecordSink" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=273, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_273_0(Etw):
    pattern = Struct(
        "RecordSink" / Int64ul,
        "CaptureEngineObject" / Int64ul
    )


@declare(guid=guid("b8197c10-845f-40ca-82ab-9341e98cfc2b"), event_id=274, version=0)
class Microsoft_Windows_MediaFoundation_MFCaptureEngine_274_0(Etw):
    pattern = Struct(
        "SinkPointer" / Int64ul,
        "SamplePointer" / Int64ul,
        "SinkStreamIndex" / Int32ul,
        "Timestamp" / Int64ul,
        "RefTimestamp" / Int64ul
    )

