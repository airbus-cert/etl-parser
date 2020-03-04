# -*- coding: utf-8 -*-
"""
Microsoft-Windows-WebIO
GUID : 50b3e73c-9370-461d-bb9f-26f32d68887d
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=1, version=0)
class Microsoft_Windows_WebIO_1_0(Etw):
    pattern = Struct(
        "ApiObject" / Int64ul,
        "ApiHandle" / Int64ul,
        "ApiVersion" / Int64ul,
        "Flags" / Int64ul,
        "Error" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=2, version=0)
class Microsoft_Windows_WebIO_2_0(Etw):
    pattern = Struct(
        "ApiObject" / Int64ul,
        "ApiHandle" / Int64ul,
        "ApiVersion" / Int64ul,
        "Flags" / Int64ul,
        "Error" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=3, version=0)
class Microsoft_Windows_WebIO_3_0(Etw):
    pattern = Struct(
        "ApiObject" / Int64ul,
        "ApiHandle" / Int64ul,
        "Flags" / Int64ul,
        "Error" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=4, version=0)
class Microsoft_Windows_WebIO_4_0(Etw):
    pattern = Struct(
        "ApiObject" / Int64ul,
        "ApiHandle" / Int64ul,
        "Flags" / Int64ul,
        "Error" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=5, version=0)
class Microsoft_Windows_WebIO_5_0(Etw):
    pattern = Struct(
        "ApiObject" / Int64ul,
        "ApiHandle" / Int64ul,
        "Session" / Int64ul,
        "SessionHandle" / Int64ul,
        "Flags" / Int64ul,
        "Error" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=6, version=0)
class Microsoft_Windows_WebIO_6_0(Etw):
    pattern = Struct(
        "ApiObject" / Int64ul,
        "ApiHandle" / Int64ul,
        "Session" / Int64ul,
        "SessionHandle" / Int64ul,
        "Flags" / Int64ul,
        "Error" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=7, version=0)
class Microsoft_Windows_WebIO_7_0(Etw):
    pattern = Struct(
        "ApiObject" / Int64ul,
        "ApiHandle" / Int64ul,
        "Flags" / Int64ul,
        "Error" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=8, version=0)
class Microsoft_Windows_WebIO_8_0(Etw):
    pattern = Struct(
        "ApiObject" / Int64ul,
        "ApiHandle" / Int64ul,
        "Flags" / Int64ul,
        "Error" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=9, version=0)
class Microsoft_Windows_WebIO_9_0(Etw):
    pattern = Struct(
        "ApiHandle" / Int64ul,
        "Api" / CString
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=10, version=0)
class Microsoft_Windows_WebIO_10_0(Etw):
    pattern = Struct(
        "ApiHandle" / Int64ul,
        "Api" / CString,
        "Result" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=11, version=0)
class Microsoft_Windows_WebIO_11_0(Etw):
    pattern = Struct(
        "ApiHandle" / Int64ul,
        "Api" / CString,
        "Result" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=12, version=0)
class Microsoft_Windows_WebIO_12_0(Etw):
    pattern = Struct(
        "ApiHandle" / Int64ul,
        "Api" / CString
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=13, version=0)
class Microsoft_Windows_WebIO_13_0(Etw):
    pattern = Struct(
        "ApiHandle" / Int64ul,
        "Api" / CString,
        "Result" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=14, version=0)
class Microsoft_Windows_WebIO_14_0(Etw):
    pattern = Struct(
        "ApiHandle" / Int64ul,
        "Api" / CString,
        "Result" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=15, version=0)
class Microsoft_Windows_WebIO_15_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "RequestHandle" / Int64ul,
        "Option" / Int32ul,
        "Length" / Int32ul,
        "Value" / Bytes(lambda this: this.Length),
        "Error" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=17, version=0)
class Microsoft_Windows_WebIO_17_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "RequestHandle" / Int64ul,
        "Session" / Int64ul,
        "SessionHandle" / Int64ul,
        "Method" / CString,
        "URI" / WString,
        "VersionMajor" / Int16ul,
        "VersionMinor" / Int16ul,
        "Error" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=18, version=0)
class Microsoft_Windows_WebIO_18_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "RequestHandle" / Int64ul,
        "Session" / Int64ul,
        "SessionHandle" / Int64ul,
        "Method" / CString,
        "URI" / WString,
        "VersionMajor" / Int16ul,
        "VersionMinor" / Int16ul,
        "Error" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=19, version=0)
class Microsoft_Windows_WebIO_19_0(Etw):
    pattern = Struct(
        "ApiObject" / Int64ul,
        "ApiHandle" / Int64ul,
        "Flags" / Int64ul,
        "Error" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=20, version=0)
class Microsoft_Windows_WebIO_20_0(Etw):
    pattern = Struct(
        "ApiObject" / Int64ul,
        "ApiHandle" / Int64ul,
        "Flags" / Int64ul,
        "Error" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=21, version=0)
class Microsoft_Windows_WebIO_21_0(Etw):
    pattern = Struct(
        "Handle" / Int64ul,
        "Event" / Int64ul,
        "Error" / Int32ul,
        "Information" / Int64ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=22, version=0)
class Microsoft_Windows_WebIO_22_0(Etw):
    pattern = Struct(
        "Handle" / Int64ul,
        "Event" / Int64ul,
        "Error" / Int32ul,
        "Information" / Int64ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=23, version=0)
class Microsoft_Windows_WebIO_23_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "RequestHandle" / Int64ul,
        "Flags" / Int32ul,
        "InformationRoutine" / Int64ul,
        "InformationContext" / Int64ul,
        "Error" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=24, version=0)
class Microsoft_Windows_WebIO_24_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "RequestHandle" / Int64ul,
        "Flags" / Int32ul,
        "InformationRoutine" / Int64ul,
        "InformationContext" / Int64ul,
        "Error" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=25, version=0)
class Microsoft_Windows_WebIO_25_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "RequestHandle" / Int64ul,
        "Flags" / Int32ul,
        "InformationRoutine" / Int64ul,
        "InformationContext" / Int64ul,
        "Error" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=26, version=0)
class Microsoft_Windows_WebIO_26_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "RequestHandle" / Int64ul,
        "Flags" / Int32ul,
        "InformationRoutine" / Int64ul,
        "InformationContext" / Int64ul,
        "Error" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=27, version=0)
class Microsoft_Windows_WebIO_27_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "PendingCount" / Int32ul,
        "InformationRoutine" / Int64ul,
        "InformationContext" / Int64ul,
        "Type" / Int32ul,
        "Information" / Int64ul,
        "InformationLength" / Int64ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=28, version=0)
class Microsoft_Windows_WebIO_28_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "PendingCount" / Int32ul,
        "InformationRoutine" / Int64ul,
        "InformationContext" / Int64ul,
        "Type" / Int32ul,
        "Information" / Int64ul,
        "InformationLength" / Int64ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=29, version=0)
class Microsoft_Windows_WebIO_29_0(Etw):
    pattern = Struct(
        "ApiObject" / Int64ul,
        "ApiHandle" / Int64ul,
        "Flags" / Int64ul,
        "Error" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=30, version=0)
class Microsoft_Windows_WebIO_30_0(Etw):
    pattern = Struct(
        "ApiObject" / Int64ul,
        "ApiHandle" / Int64ul,
        "Flags" / Int64ul,
        "Error" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=100, version=0)
class Microsoft_Windows_WebIO_100_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "Length" / Int16ul,
        "Headers" / Bytes(lambda this: this.Length)
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=101, version=0)
class Microsoft_Windows_WebIO_101_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "Length" / Int16ul,
        "Headers" / Bytes(lambda this: this.Length)
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=102, version=0)
class Microsoft_Windows_WebIO_102_0(Etw):
    pattern = Struct(
        "Context" / Int64ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=103, version=0)
class Microsoft_Windows_WebIO_103_0(Etw):
    pattern = Struct(
        "Context" / Int64ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=104, version=0)
class Microsoft_Windows_WebIO_104_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "ConnMgr" / Int64ul,
        "Connection" / Int64ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=105, version=0)
class Microsoft_Windows_WebIO_105_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "ServerEndpoint" / Int64ul,
        "ProxyEndpoint" / Int64ul,
        "ConnectionManager" / Int64ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=106, version=0)
class Microsoft_Windows_WebIO_106_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "DataChunks" / Int64ul,
        "Length" / Int64ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=107, version=0)
class Microsoft_Windows_WebIO_107_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "RequestHandle" / Int64ul,
        "Flags" / Int32ul,
        "DataChunks" / Int64ul,
        "DataChunkCount" / Int32ul,
        "CompletionContext" / Int64ul,
        "Error" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=108, version=0)
class Microsoft_Windows_WebIO_108_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "RequestHandle" / Int64ul,
        "Flags" / Int32ul,
        "DataChunks" / Int64ul,
        "DataChunkCount" / Int32ul,
        "CompletionContext" / Int64ul,
        "Error" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=109, version=0)
class Microsoft_Windows_WebIO_109_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "DataChunks" / Int64ul,
        "TotalChunkLength" / Int64ul,
        "IsEntity" / Int8ul,
        "RequestEntityComplete" / Int8ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=110, version=0)
class Microsoft_Windows_WebIO_110_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "Connection" / Int64ul,
        "DataChunks" / Int64ul,
        "PendingSendCount" / Int32ul,
        "LastSend" / Int8ul,
        "Error" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=111, version=0)
class Microsoft_Windows_WebIO_111_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "Connection" / Int64ul,
        "DataChunks" / Int64ul,
        "Index" / Int32ul,
        "Buffer" / Int64ul,
        "Length" / Int32ul,
        "Data" / Bytes(lambda this: this.Length)
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=112, version=0)
class Microsoft_Windows_WebIO_112_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "Connection" / Int64ul,
        "DataChunks" / Int64ul,
        "PendingSendCount" / Int32ul,
        "LastSend" / Int8ul,
        "Error" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=113, version=0)
class Microsoft_Windows_WebIO_113_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "DataChunks" / Int64ul,
        "Error" / Int32ul,
        "CompletionContext" / Int64ul,
        "CompletionInformation" / Int64ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=114, version=0)
class Microsoft_Windows_WebIO_114_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "DataChunks" / Int64ul,
        "Error" / Int32ul,
        "CompletionContext" / Int64ul,
        "CompletionInformation" / Int64ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=115, version=0)
class Microsoft_Windows_WebIO_115_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "RequestHandle" / Int64ul,
        "Flags" / Int32ul,
        "DataChunks" / Int64ul,
        "DataChunkCount" / Int32ul,
        "CompletionContext" / Int64ul,
        "Error" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=116, version=0)
class Microsoft_Windows_WebIO_116_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "RequestHandle" / Int64ul,
        "Flags" / Int32ul,
        "DataChunks" / Int64ul,
        "DataChunkCount" / Int32ul,
        "CompletionContext" / Int64ul,
        "Error" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=117, version=0)
class Microsoft_Windows_WebIO_117_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "DataChunks" / Int64ul,
        "Error" / Int32ul,
        "CompletionContext" / Int64ul,
        "CompletionInformation" / Int64ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=118, version=0)
class Microsoft_Windows_WebIO_118_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "DataChunks" / Int64ul,
        "Error" / Int32ul,
        "CompletionContext" / Int64ul,
        "CompletionInformation" / Int64ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=119, version=0)
class Microsoft_Windows_WebIO_119_0(Etw):
    pattern = Struct(
        "Connection" / Int64ul,
        "OldBuffer" / Int64ul,
        "OldBufferLength" / Int32ul,
        "BufferLengthData" / Int32ul,
        "NewBuffer" / Int64ul,
        "NewBufferLength" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=120, version=0)
class Microsoft_Windows_WebIO_120_0(Etw):
    pattern = Struct(
        "Connection" / Int64ul,
        "DataChunks" / Int64ul,
        "Buffer" / Int64ul,
        "BufferLengthConsumed" / Int32ul,
        "BufferLengthData" / Int32ul,
        "BufferLengthRemaining" / Int32ul,
        "Error" / Int32ul,
        "Information" / Int64ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=121, version=0)
class Microsoft_Windows_WebIO_121_0(Etw):
    pattern = Struct(
        "Connection" / Int64ul,
        "DataChunks" / Int64ul,
        "Buffer" / Int64ul,
        "BufferLengthConsumed" / Int32ul,
        "BufferLengthData" / Int32ul,
        "BufferLengthRemaining" / Int32ul,
        "Error" / Int32ul,
        "Information" / Int64ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=122, version=0)
class Microsoft_Windows_WebIO_122_0(Etw):
    pattern = Struct(
        "Connection" / Int64ul,
        "DataChunks" / Int64ul,
        "Length" / Int32ul,
        "Data" / Bytes(lambda this: this.Length)
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=123, version=0)
class Microsoft_Windows_WebIO_123_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "Connection" / Int64ul,
        "Buffer" / Int64ul,
        "BufferLengthConsumed" / Int32ul,
        "BufferLengthData" / Int32ul,
        "BufferLengthRemaining" / Int32ul,
        "ChunkData" / Int64ul,
        "ChunkDataLength" / Int32ul,
        "Error" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=124, version=0)
class Microsoft_Windows_WebIO_124_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "Connection" / Int64ul,
        "Buffer" / Int64ul,
        "BufferLengthConsumed" / Int32ul,
        "BufferLengthData" / Int32ul,
        "BufferLengthRemaining" / Int32ul,
        "ChunkData" / Int64ul,
        "ChunkDataLength" / Int32ul,
        "Error" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=125, version=0)
class Microsoft_Windows_WebIO_125_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "Buffer" / Int64ul,
        "HttpResponseCode" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=126, version=0)
class Microsoft_Windows_WebIO_126_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "DataChunks" / Int64ul,
        "ChunkData" / Int64ul,
        "ChunkDataLength" / Int32ul,
        "Error" / Int32ul,
        "CompletionContext" / Int64ul,
        "CompletionInformation" / Int64ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=127, version=0)
class Microsoft_Windows_WebIO_127_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "DataChunks" / Int64ul,
        "BytesToReceive" / Int32ul,
        "Error" / Int32ul,
        "CompletionContext" / Int64ul,
        "CompletionInformation" / Int64ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=128, version=0)
class Microsoft_Windows_WebIO_128_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "DataChunks" / Int64ul,
        "BytesToReceive" / Int32ul,
        "Error" / Int32ul,
        "CompletionContext" / Int64ul,
        "CompletionInformation" / Int64ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=129, version=0)
class Microsoft_Windows_WebIO_129_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "DataChunks" / Int64ul,
        "Index" / Int32ul,
        "Length" / Int32ul,
        "Data" / Bytes(lambda this: this.Length)
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=130, version=0)
class Microsoft_Windows_WebIO_130_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "RequestHandle" / Int64ul,
        "Flags" / Int32ul,
        "DataChunks" / Int64ul,
        "DataChunkCount" / Int32ul,
        "CompletionContext" / Int64ul,
        "Error" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=131, version=0)
class Microsoft_Windows_WebIO_131_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "RequestHandle" / Int64ul,
        "Flags" / Int32ul,
        "DataChunks" / Int64ul,
        "DataChunkCount" / Int32ul,
        "CompletionContext" / Int64ul,
        "Error" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=132, version=0)
class Microsoft_Windows_WebIO_132_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "RequestHandle" / Int64ul,
        "Flags" / Int32ul,
        "ResponseFlags" / Int32ul,
        "CompletionContext" / Int64ul,
        "Error" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=133, version=0)
class Microsoft_Windows_WebIO_133_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "RequestHandle" / Int64ul,
        "Flags" / Int32ul,
        "ResponseFlags" / Int32ul,
        "CompletionContext" / Int64ul,
        "Error" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=134, version=0)
class Microsoft_Windows_WebIO_134_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "ResponseFlags" / Int32ul,
        "Error" / Int32ul,
        "CompletionContext" / Int64ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=135, version=0)
class Microsoft_Windows_WebIO_135_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "ResponseFlags" / Int32ul,
        "Error" / Int32ul,
        "CompletionContext" / Int64ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=136, version=0)
class Microsoft_Windows_WebIO_136_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "RequestHandle" / Int64ul,
        "Flags" / Int32ul,
        "Error" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=137, version=0)
class Microsoft_Windows_WebIO_137_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "RequestHandle" / Int64ul,
        "Flags" / Int32ul,
        "Error" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=200, version=0)
class Microsoft_Windows_WebIO_200_0(Etw):
    pattern = Struct(
        "Connection" / Int64ul,
        "SocketHandle" / Int64ul,
        "AddressLength" / Int32ul,
        "Address" / Bytes(lambda this: this.AddressLength),
        "Context" / Int64ul,
        "RemainingAddressCount" / Int64ul,
        "Error" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=201, version=0)
class Microsoft_Windows_WebIO_201_0(Etw):
    pattern = Struct(
        "Connection" / Int64ul,
        "SocketHandle" / Int64ul,
        "AddressLength" / Int32ul,
        "Address" / Bytes(lambda this: this.AddressLength),
        "Context" / Int64ul,
        "RemainingAddressCount" / Int64ul,
        "Error" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=202, version=0)
class Microsoft_Windows_WebIO_202_0(Etw):
    pattern = Struct(
        "Connection" / Int64ul,
        "SocketHandle" / Int64ul,
        "AddressLength" / Int32ul,
        "Address" / Bytes(lambda this: this.AddressLength),
        "Context" / Int64ul,
        "RemainingAddressCount" / Int64ul,
        "Error" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=203, version=0)
class Microsoft_Windows_WebIO_203_0(Etw):
    pattern = Struct(
        "Connection" / Int64ul,
        "SocketHandle" / Int64ul,
        "Error" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=204, version=0)
class Microsoft_Windows_WebIO_204_0(Etw):
    pattern = Struct(
        "Endpoint" / Int64ul,
        "Socket" / Int64ul,
        "Reason" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=205, version=0)
class Microsoft_Windows_WebIO_205_0(Etw):
    pattern = Struct(
        "DnsQuery" / Int64ul,
        "HostName" / WString,
        "Timeout" / Int32ul,
        "CompletionContext" / Int64ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=206, version=0)
class Microsoft_Windows_WebIO_206_0(Etw):
    pattern = Struct(
        "DnsQuery" / Int64ul,
        "FQDN" / WString,
        "CanonicalName" / WString,
        "AddressCount" / Int32ul,
        "SockaddrLength" / Int32ul,
        "SockAddr" / Bytes(lambda this: this.SockaddrLength)
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=207, version=0)
class Microsoft_Windows_WebIO_207_0(Etw):
    pattern = Struct(
        "DnsQuery" / Int64ul,
        "Error" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=208, version=0)
class Microsoft_Windows_WebIO_208_0(Etw):
    pattern = Struct(
        "DnsQuery" / Int64ul,
        "CacheEntry" / Int64ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=209, version=0)
class Microsoft_Windows_WebIO_209_0(Etw):
    pattern = Struct(
        "ReferenceContext" / Int64ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=210, version=0)
class Microsoft_Windows_WebIO_210_0(Etw):
    pattern = Struct(
        "ReferenceContext" / Int64ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=211, version=0)
class Microsoft_Windows_WebIO_211_0(Etw):
    pattern = Struct(
        "CacheEntry" / Int64ul,
        "ResolveName" / WString,
        "Flags" / Int32ul,
        "Error" / Int32ul,
        "AddressCount" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=212, version=0)
class Microsoft_Windows_WebIO_212_0(Etw):
    pattern = Struct(
        "CacheEntry" / Int64ul,
        "ResolveName" / WString,
        "Flags" / Int32ul,
        "Error" / Int32ul,
        "AddressCount" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=213, version=0)
class Microsoft_Windows_WebIO_213_0(Etw):
    pattern = Struct(
        "Connection" / Int64ul,
        "DataChunks" / Int64ul,
        "SocketHandle" / Int64ul,
        "Buffer" / Int64ul,
        "Context" / Int64ul,
        "Error" / Int32ul,
        "Information" / Int64ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=214, version=0)
class Microsoft_Windows_WebIO_214_0(Etw):
    pattern = Struct(
        "Connection" / Int64ul,
        "DataChunks" / Int64ul,
        "SocketHandle" / Int64ul,
        "Buffer" / Int64ul,
        "Context" / Int64ul,
        "Error" / Int32ul,
        "Information" / Int64ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=215, version=0)
class Microsoft_Windows_WebIO_215_0(Etw):
    pattern = Struct(
        "Connection" / Int64ul,
        "DataChunks" / Int64ul,
        "SocketHandle" / Int64ul,
        "Buffer" / Int64ul,
        "Context" / Int64ul,
        "Error" / Int32ul,
        "Information" / Int64ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=216, version=0)
class Microsoft_Windows_WebIO_216_0(Etw):
    pattern = Struct(
        "Connection" / Int64ul,
        "DataChunks" / Int64ul,
        "SocketHandle" / Int64ul,
        "Buffer" / Int64ul,
        "Context" / Int64ul,
        "Error" / Int32ul,
        "Information" / Int64ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=700, version=0)
class Microsoft_Windows_WebIO_700_0(Etw):
    pattern = Struct(
        "Connection" / Int64ul,
        "SecurityHandleHigh" / Int64ul,
        "SecurityHandleLow" / Int64ul,
        "CredHandleHigh" / Int64ul,
        "CredHandleLow" / Int64ul,
        "HostName" / WString,
        "InputFlags" / Int32ul,
        "Buffer" / Int64ul,
        "BufferLengthData" / Int32ul,
        "BufferLengthRemaining" / Int32ul,
        "OutputFlags" / Int32ul,
        "DataChunks" / Int64ul,
        "DataChunkBufferLength" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=703, version=0)
class Microsoft_Windows_WebIO_703_0(Etw):
    pattern = Struct(
        "Connection" / Int64ul,
        "SecurityHandleHigh" / Int64ul,
        "SecurityHandleLow" / Int64ul,
        "CredHandleHigh" / Int64ul,
        "CredHandleLow" / Int64ul,
        "HostName" / WString,
        "InputFlags" / Int32ul,
        "Buffer" / Int64ul,
        "BufferLengthData" / Int32ul,
        "BufferLengthRemaining" / Int32ul,
        "OutputFlags" / Int32ul,
        "DataChunks" / Int64ul,
        "DataChunkBufferLength" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=704, version=0)
class Microsoft_Windows_WebIO_704_0(Etw):
    pattern = Struct(
        "Connection" / Int64ul,
        "SecurityHandleHigh" / Int64ul,
        "SecurityHandleLow" / Int64ul,
        "Buffer" / Int64ul,
        "BufferLengthData" / Int32ul,
        "BufferLengthRemaining" / Int32ul,
        "Data" / Bytes(lambda this: this.BufferLengthData)
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=705, version=0)
class Microsoft_Windows_WebIO_705_0(Etw):
    pattern = Struct(
        "Connection" / Int64ul,
        "SecurityHandleHigh" / Int64ul,
        "SecurityHandleLow" / Int64ul,
        "DataChunks" / Int64ul,
        "DataChunkBufferLength" / Int32ul,
        "Data" / Bytes(lambda this: this.DataChunkBufferLength)
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=706, version=0)
class Microsoft_Windows_WebIO_706_0(Etw):
    pattern = Struct(
        "Connection" / Int64ul,
        "SslIOContext" / Int64ul,
        "CredHandleHigh" / Int64ul,
        "CredHandleLow" / Int64ul,
        "DataChunks" / Int64ul,
        "Index" / Int32ul,
        "Buffer" / Int64ul,
        "Length" / Int64ul,
        "Flags" / Int32ul,
        "Error" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=707, version=0)
class Microsoft_Windows_WebIO_707_0(Etw):
    pattern = Struct(
        "Connection" / Int64ul,
        "SslIOContext" / Int64ul,
        "CredHandleHigh" / Int64ul,
        "CredHandleLow" / Int64ul,
        "DataChunks" / Int64ul,
        "Index" / Int32ul,
        "Buffer" / Int64ul,
        "Length" / Int64ul,
        "Flags" / Int32ul,
        "Error" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=708, version=0)
class Microsoft_Windows_WebIO_708_0(Etw):
    pattern = Struct(
        "Connection" / Int64ul,
        "SslIOContext" / Int64ul,
        "CredHandleHigh" / Int64ul,
        "CredHandleLow" / Int64ul,
        "DataChunks" / Int64ul,
        "Index" / Int32ul,
        "Buffer" / Int64ul,
        "Length" / Int64ul,
        "Flags" / Int32ul,
        "Error" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=709, version=0)
class Microsoft_Windows_WebIO_709_0(Etw):
    pattern = Struct(
        "Connection" / Int64ul,
        "SslIOContext" / Int64ul,
        "CredHandleHigh" / Int64ul,
        "CredHandleLow" / Int64ul,
        "DataChunks" / Int64ul,
        "Index" / Int32ul,
        "Buffer" / Int64ul,
        "Length" / Int32ul,
        "Flags" / Int32ul,
        "Data" / Bytes(lambda this: this.Length)
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=710, version=0)
class Microsoft_Windows_WebIO_710_0(Etw):
    pattern = Struct(
        "Connection" / Int64ul,
        "SslIOContext" / Int64ul,
        "DataChunks" / Int64ul,
        "RequestDisconnect" / Int8ul,
        "Error" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=711, version=0)
class Microsoft_Windows_WebIO_711_0(Etw):
    pattern = Struct(
        "Connection" / Int64ul,
        "SslIOContext" / Int64ul,
        "DataChunks" / Int64ul,
        "RequestDisconnect" / Int8ul,
        "Error" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=712, version=0)
class Microsoft_Windows_WebIO_712_0(Etw):
    pattern = Struct(
        "Connection" / Int64ul,
        "ContextHandleHigh" / Int64ul,
        "ContextHandleLow" / Int64ul,
        "IgnoredServerCertErrors" / Int32ul,
        "ServerCertErrors" / Int32ul,
        "Error" / Int32ul,
        "Reason" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=713, version=0)
class Microsoft_Windows_WebIO_713_0(Etw):
    pattern = Struct(
        "Connection" / Int64ul,
        "ContextHandleHigh" / Int64ul,
        "ContextHandleLow" / Int64ul,
        "IgnoredServerCertErrors" / Int32ul,
        "ServerCertErrors" / Int32ul,
        "Error" / Int32ul,
        "Reason" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=720, version=0)
class Microsoft_Windows_WebIO_720_0(Etw):
    pattern = Struct(
        "Connection" / Int64ul,
        "SslIOContext" / Int64ul,
        "DataChunks" / Int64ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=721, version=0)
class Microsoft_Windows_WebIO_721_0(Etw):
    pattern = Struct(
        "Connection" / Int64ul,
        "SslIOContext" / Int64ul,
        "DataChunks" / Int64ul,
        "PlainData" / Int64ul,
        "PlainDataLength" / Int32ul,
        "Information" / Int32ul,
        "Error" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=722, version=0)
class Microsoft_Windows_WebIO_722_0(Etw):
    pattern = Struct(
        "Connection" / Int64ul,
        "ContextHandleHigh" / Int64ul,
        "ContextHandleLow" / Int64ul,
        "Buffer" / Int64ul,
        "BufferLengthData" / Int32ul,
        "BufferLengthRemaining" / Int32ul,
        "PlainData" / Int64ul,
        "PlainDataLength" / Int32ul,
        "SecStatus" / Int32ul,
        "Error" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=723, version=0)
class Microsoft_Windows_WebIO_723_0(Etw):
    pattern = Struct(
        "Connection" / Int64ul,
        "ContextHandleHigh" / Int64ul,
        "ContextHandleLow" / Int64ul,
        "Buffer" / Int64ul,
        "BufferLengthData" / Int32ul,
        "BufferLengthRemaining" / Int32ul,
        "PlainData" / Int64ul,
        "PlainDataLength" / Int32ul,
        "SecStatus" / Int32ul,
        "Error" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=724, version=0)
class Microsoft_Windows_WebIO_724_0(Etw):
    pattern = Struct(
        "Connection" / Int64ul,
        "DataChunks" / Int64ul,
        "Buffer" / Int64ul,
        "Consumed" / Int32ul,
        "Available" / Int32ul,
        "Information" / Int32ul,
        "Error" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=725, version=0)
class Microsoft_Windows_WebIO_725_0(Etw):
    pattern = Struct(
        "Connection" / Int64ul,
        "DataChunks" / Int64ul,
        "Buffer" / Int64ul,
        "Consumed" / Int32ul,
        "Available" / Int32ul,
        "Information" / Int32ul,
        "Error" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=726, version=0)
class Microsoft_Windows_WebIO_726_0(Etw):
    pattern = Struct(
        "Connection" / Int64ul,
        "Buffer" / Int64ul,
        "BufferLengthData" / Int32ul,
        "BufferLengthRemaining" / Int32ul,
        "Data" / Bytes(lambda this: this.BufferLengthData),
        "DummyWorkaroundVal" / Int8ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=727, version=0)
class Microsoft_Windows_WebIO_727_0(Etw):
    pattern = Struct(
        "Connection" / Int64ul,
        "OldBuffer" / Int64ul,
        "NewBuffer" / Int64ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=728, version=0)
class Microsoft_Windows_WebIO_728_0(Etw):
    pattern = Struct(
        "Connection" / Int64ul,
        "EnabledProtocols" / Int32ul,
        "SSLClientCert" / Int64ul,
        "EnableRevertToSelfClientCertificate" / Int16ul,
        "CredHandleHigh" / Int64ul,
        "CredHandleLow" / Int64ul,
        "Result" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=728, version=1)
class Microsoft_Windows_WebIO_728_1(Etw):
    pattern = Struct(
        "Connection" / Int64ul,
        "EnabledProtocols" / Int32ul,
        "SSLClientCert" / Int64ul,
        "EnableRevertToSelfClientCertificate" / Int16ul,
        "CipherConfig" / Int32ul,
        "CredHandleHigh" / Int64ul,
        "CredHandleLow" / Int64ul,
        "Result" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=729, version=0)
class Microsoft_Windows_WebIO_729_0(Etw):
    pattern = Struct(
        "Connection" / Int64ul,
        "EnabledProtocols" / Int32ul,
        "SSLClientCert" / Int64ul,
        "EnableRevertToSelfClientCertificate" / Int16ul,
        "CredHandleHigh" / Int64ul,
        "CredHandleLow" / Int64ul,
        "Result" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=729, version=1)
class Microsoft_Windows_WebIO_729_1(Etw):
    pattern = Struct(
        "Connection" / Int64ul,
        "EnabledProtocols" / Int32ul,
        "SSLClientCert" / Int64ul,
        "EnableRevertToSelfClientCertificate" / Int16ul,
        "CipherConfig" / Int32ul,
        "CredHandleHigh" / Int64ul,
        "CredHandleLow" / Int64ul,
        "Result" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=730, version=0)
class Microsoft_Windows_WebIO_730_0(Etw):
    pattern = Struct(
        "Connection" / Int64ul,
        "EnabledProtocols" / Int32ul,
        "SSLClientCert" / Int64ul,
        "EnableRevertToSelfClientCertificate" / Int16ul,
        "CredHandleHigh" / Int64ul,
        "CredHandleLow" / Int64ul,
        "Result" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=730, version=1)
class Microsoft_Windows_WebIO_730_1(Etw):
    pattern = Struct(
        "Connection" / Int64ul,
        "EnabledProtocols" / Int32ul,
        "SSLClientCert" / Int64ul,
        "EnableRevertToSelfClientCertificate" / Int16ul,
        "CipherConfig" / Int32ul,
        "CredHandleHigh" / Int64ul,
        "CredHandleLow" / Int64ul,
        "Result" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=900, version=0)
class Microsoft_Windows_WebIO_900_0(Etw):
    pattern = Struct(
        "ProtocolObject" / Int64ul,
        "ProtocolHandle" / Int64ul,
        "Request" / Int64ul,
        "RequestHandle" / Int64ul,
        "Session" / Int64ul,
        "SessionHandle" / Int64ul,
        "Error" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=901, version=0)
class Microsoft_Windows_WebIO_901_0(Etw):
    pattern = Struct(
        "ProtocolObject" / Int64ul,
        "ProtocolHandle" / Int64ul,
        "Request" / Int64ul,
        "RequestHandle" / Int64ul,
        "Session" / Int64ul,
        "SessionHandle" / Int64ul,
        "Error" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=902, version=0)
class Microsoft_Windows_WebIO_902_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "RequestHandle" / Int64ul,
        "Flags" / Int32ul,
        "Error" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=903, version=0)
class Microsoft_Windows_WebIO_903_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "RequestHandle" / Int64ul,
        "Flags" / Int32ul,
        "Error" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=904, version=0)
class Microsoft_Windows_WebIO_904_0(Etw):
    pattern = Struct(
        "ApiObject" / Int64ul,
        "ApiHandle" / Int64ul,
        "Flags" / Int64ul,
        "Error" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=905, version=0)
class Microsoft_Windows_WebIO_905_0(Etw):
    pattern = Struct(
        "ApiObject" / Int64ul,
        "ApiHandle" / Int64ul,
        "Flags" / Int64ul,
        "Error" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=906, version=0)
class Microsoft_Windows_WebIO_906_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "RequestHandle" / Int64ul,
        "Option" / Int32ul,
        "Length" / Int32ul,
        "Value" / Bytes(lambda this: this.Length),
        "Error" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=907, version=0)
class Microsoft_Windows_WebIO_907_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "RequestHandle" / Int64ul,
        "Flags" / Int32ul,
        "DataChunks" / Int64ul,
        "DataChunkCount" / Int32ul,
        "CompletionContext" / Int64ul,
        "Error" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=908, version=0)
class Microsoft_Windows_WebIO_908_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "RequestHandle" / Int64ul,
        "Flags" / Int32ul,
        "DataChunks" / Int64ul,
        "DataChunkCount" / Int32ul,
        "CompletionContext" / Int64ul,
        "Error" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=909, version=0)
class Microsoft_Windows_WebIO_909_0(Etw):
    pattern = Struct(
        "ProtocolObject" / Int64ul,
        "Handle" / Int64ul,
        "Context" / Int64ul,
        "Error" / Int32ul,
        "Information" / Int64ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=910, version=0)
class Microsoft_Windows_WebIO_910_0(Etw):
    pattern = Struct(
        "ProtocolObject" / Int64ul,
        "Handle" / Int64ul,
        "Context" / Int64ul,
        "Error" / Int32ul,
        "Information" / Int64ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=911, version=0)
class Microsoft_Windows_WebIO_911_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "RequestHandle" / Int64ul,
        "Flags" / Int32ul,
        "DataChunks" / Int64ul,
        "DataChunkCount" / Int32ul,
        "CompletionContext" / Int64ul,
        "Error" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=912, version=0)
class Microsoft_Windows_WebIO_912_0(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "RequestHandle" / Int64ul,
        "Flags" / Int32ul,
        "DataChunks" / Int64ul,
        "DataChunkCount" / Int32ul,
        "CompletionContext" / Int64ul,
        "Error" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=913, version=0)
class Microsoft_Windows_WebIO_913_0(Etw):
    pattern = Struct(
        "ProtocolObject" / Int64ul,
        "Handle" / Int64ul,
        "Context" / Int64ul,
        "Error" / Int32ul,
        "Information" / Int64ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=914, version=0)
class Microsoft_Windows_WebIO_914_0(Etw):
    pattern = Struct(
        "ProtocolObject" / Int64ul,
        "Handle" / Int64ul,
        "Context" / Int64ul,
        "Error" / Int32ul,
        "Information" / Int64ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=2100, version=0)
class Microsoft_Windows_WebIO_2100_0(Etw):
    pattern = Struct(
        "Context" / Int64ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=2101, version=0)
class Microsoft_Windows_WebIO_2101_0(Etw):
    pattern = Struct(
        "Context" / Int64ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=2102, version=0)
class Microsoft_Windows_WebIO_2102_0(Etw):
    pattern = Struct(
        "Context" / Int64ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=2111, version=0)
class Microsoft_Windows_WebIO_2111_0(Etw):
    pattern = Struct(
        "Context" / Int64ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=2112, version=0)
class Microsoft_Windows_WebIO_2112_0(Etw):
    pattern = Struct(
        "Context" / Int64ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=2113, version=0)
class Microsoft_Windows_WebIO_2113_0(Etw):
    pattern = Struct(
        "Context" / Int64ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=2114, version=0)
class Microsoft_Windows_WebIO_2114_0(Etw):
    pattern = Struct(
        "Context" / Int64ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=2120, version=0)
class Microsoft_Windows_WebIO_2120_0(Etw):
    pattern = Struct(
        "Context" / Int64ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=2121, version=0)
class Microsoft_Windows_WebIO_2121_0(Etw):
    pattern = Struct(
        "Context" / Int64ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=2122, version=0)
class Microsoft_Windows_WebIO_2122_0(Etw):
    pattern = Struct(
        "Context" / Int64ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=2123, version=0)
class Microsoft_Windows_WebIO_2123_0(Etw):
    pattern = Struct(
        "Context" / Int64ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=2130, version=0)
class Microsoft_Windows_WebIO_2130_0(Etw):
    pattern = Struct(
        "Context" / Int64ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=2131, version=0)
class Microsoft_Windows_WebIO_2131_0(Etw):
    pattern = Struct(
        "Context" / Int64ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=2132, version=0)
class Microsoft_Windows_WebIO_2132_0(Etw):
    pattern = Struct(
        "Context" / Int64ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=2140, version=0)
class Microsoft_Windows_WebIO_2140_0(Etw):
    pattern = Struct(
        "Context" / Int64ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=2141, version=0)
class Microsoft_Windows_WebIO_2141_0(Etw):
    pattern = Struct(
        "Context" / Int64ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=59992, version=0)
class Microsoft_Windows_WebIO_59992_0(Etw):
    pattern = Struct(
        "Token" / Int64ul,
        "Error" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=59993, version=0)
class Microsoft_Windows_WebIO_59993_0(Etw):
    pattern = Struct(
        "Token" / Int64ul,
        "OldToken" / Int64ul,
        "Error" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=59994, version=0)
class Microsoft_Windows_WebIO_59994_0(Etw):
    pattern = Struct(
        "Token" / Int64ul,
        "SID" / Sid,
        "Error" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=59995, version=0)
class Microsoft_Windows_WebIO_59995_0(Etw):
    pattern = Struct(
        "Context" / Int64ul,
        "EtwQueueActionType" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=59996, version=0)
class Microsoft_Windows_WebIO_59996_0(Etw):
    pattern = Struct(
        "Context" / Int64ul,
        "EtwQueueActionType" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=59997, version=0)
class Microsoft_Windows_WebIO_59997_0(Etw):
    pattern = Struct(
        "Context" / Int64ul,
        "EtwQueueActionType" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=59998, version=0)
class Microsoft_Windows_WebIO_59998_0(Etw):
    pattern = Struct(
        "Context" / Int64ul,
        "EtwQueueActionType" / Int32ul
    )


@declare(guid=guid("50b3e73c-9370-461d-bb9f-26f32d68887d"), event_id=59999, version=0)
class Microsoft_Windows_WebIO_59999_0(Etw):
    pattern = Struct(
        "Length" / Int16ul,
        "Message" / Bytes(lambda this: this.Length)
    )

