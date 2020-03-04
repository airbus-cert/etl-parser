# -*- coding: utf-8 -*-
"""
Microsoft-Windows-MF
GUID : a7364e1a-894f-4b3d-a930-2ed9c8c4c811
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1, version=0)
class Microsoft_Windows_MF_1_0(Etw):
    pattern = Struct(
        "StreamID" / Int32ul,
        "IsStreaming" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=2, version=0)
class Microsoft_Windows_MF_2_0(Etw):
    pattern = Struct(
        "AsyncTaskPointer" / Int64ul,
        "StreamID" / Int32ul,
        "BufferPointer" / Int64ul,
        "PinPointer" / Int64ul,
        "ParentPointer" / Int64ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=3, version=0)
class Microsoft_Windows_MF_3_0(Etw):
    pattern = Struct(
        "AsyncTaskPointer" / Int64ul,
        "StreamID" / Int32ul,
        "BufferPointer" / Int64ul,
        "PinPointer" / Int64ul,
        "ParentPointer" / Int64ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=4, version=0)
class Microsoft_Windows_MF_4_0(Etw):
    pattern = Struct(
        "StreamID" / Int32ul,
        "SamplePtr" / Int64ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=5, version=0)
class Microsoft_Windows_MF_5_0(Etw):
    pattern = Struct(
        "StreamID" / Int32ul,
        "ReadySampleCount" / Int32ul,
        "Sample" / Int64ul,
        "SampleTime" / Int64ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=6, version=0)
class Microsoft_Windows_MF_6_0(Etw):
    pattern = Struct(
        "OutputBufferCount" / Int32ul,
        "OutputSamplesPtr" / Int64ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=7, version=0)
class Microsoft_Windows_MF_7_0(Etw):
    pattern = Struct(
        "MediaType" / CString
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=8, version=0)
class Microsoft_Windows_MF_8_0(Etw):
    pattern = Struct(
        "MediaType" / CString
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=9, version=0)
class Microsoft_Windows_MF_9_0(Etw):
    pattern = Struct(
        "MediaType" / CString
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=10, version=0)
class Microsoft_Windows_MF_10_0(Etw):
    pattern = Struct(
        "MediaType" / CString
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=11, version=0)
class Microsoft_Windows_MF_11_0(Etw):
    pattern = Struct(
        "StreamingState" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=12, version=0)
class Microsoft_Windows_MF_12_0(Etw):
    pattern = Struct(
        "PinHandle" / Int64ul,
        "State" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=13, version=0)
class Microsoft_Windows_MF_13_0(Etw):
    pattern = Struct(
        "PinPtr" / Int64ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=14, version=0)
class Microsoft_Windows_MF_14_0(Etw):
    pattern = Struct(
        "PinPtr" / Int64ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=15, version=0)
class Microsoft_Windows_MF_15_0(Etw):
    pattern = Struct(
        "PinPtr" / Int64ul,
        "SamplePtr" / Int64ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=16, version=0)
class Microsoft_Windows_MF_16_0(Etw):
    pattern = Struct(
        "PinPtr" / Int64ul,
        "SamplePtr" / Int64ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=17, version=0)
class Microsoft_Windows_MF_17_0(Etw):
    pattern = Struct(
        "PinPtr" / Int64ul,
        "SamplePtr" / Int64ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=18, version=0)
class Microsoft_Windows_MF_18_0(Etw):
    pattern = Struct(
        "PinPtr" / Int64ul,
        "SamplePtr" / Int64ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=19, version=0)
class Microsoft_Windows_MF_19_0(Etw):
    pattern = Struct(
        "PinPtr" / Int64ul,
        "D3DManagerPtr" / Int64ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=20, version=0)
class Microsoft_Windows_MF_20_0(Etw):
    pattern = Struct(
        "PinPtr" / Int64ul,
        "D3DManagerPtr" / Int64ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=23, version=0)
class Microsoft_Windows_MF_23_0(Etw):
    pattern = Struct(
        "StreamID" / Int32ul,
        "IsStreaming" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=24, version=0)
class Microsoft_Windows_MF_24_0(Etw):
    pattern = Struct(
        "FormatInfoStruct" / WString
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=25, version=0)
class Microsoft_Windows_MF_25_0(Etw):
    pattern = Struct(
        "StreamID" / Int32ul,
        "IsStreaming" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=26, version=0)
class Microsoft_Windows_MF_26_0(Etw):
    pattern = Struct(
        "StreamID" / Int32ul,
        "IsStreaming" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=27, version=0)
class Microsoft_Windows_MF_27_0(Etw):
    pattern = Struct(
        "AsyncTaskPointer" / Int64ul,
        "StreamID" / Int32ul,
        "BufferPointer" / Int64ul,
        "PinPointer" / Int64ul,
        "ParentPointer" / Int64ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=28, version=0)
class Microsoft_Windows_MF_28_0(Etw):
    pattern = Struct(
        "DeviceStreamName" / WString,
        "DeviceStreamId" / Int32ul,
        "MFTStreamId" / Int32ul,
        "samplePointer" / Int64ul,
        "SampleTimestamp" / Int64ul,
        "ExpectedSampleCompletionNumber" / Int64ul,
        "ActualSampleCompletionNumber" / Int64ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=29, version=0)
class Microsoft_Windows_MF_29_0(Etw):
    pattern = Struct(
        "DeviceStreamName" / WString,
        "DeviceStreamId" / Int32ul,
        "MFTStreamId" / Int32ul,
        "DriverQueueDepth" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=30, version=0)
class Microsoft_Windows_MF_30_0(Etw):
    pattern = Struct(
        "DeviceStreamName" / WString,
        "DeviceStreamId" / Int32ul,
        "MFTStreamId" / Int32ul,
        "samplePointer" / Int64ul,
        "DriverTimeStamp" / Int64ul,
        "SystemTimeStamp" / Int64ul,
        "SampleCompletionNumber" / Int64ul,
        "FlagTimeStamp" / CString,
        "StreamName" / CString
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=31, version=0)
class Microsoft_Windows_MF_31_0(Etw):
    pattern = Struct(
        "SamplePtr" / Int64ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=32, version=0)
class Microsoft_Windows_MF_32_0(Etw):
    pattern = Struct(
        "SamplePtr" / Int64ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=33, version=0)
class Microsoft_Windows_MF_33_0(Etw):
    pattern = Struct(
        "SamplePtr" / Int64ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=34, version=0)
class Microsoft_Windows_MF_34_0(Etw):
    pattern = Struct(
        "SamplePtr" / Int64ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1001, version=0)
class Microsoft_Windows_MF_1001_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1002, version=0)
class Microsoft_Windows_MF_1002_0(Etw):
    pattern = Struct(
        "CLSID" / WString,
        "hr" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1003, version=0)
class Microsoft_Windows_MF_1003_0(Etw):
    pattern = Struct(
        "D3DFmt" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1004, version=0)
class Microsoft_Windows_MF_1004_0(Etw):
    pattern = Struct(
        "left" / Int32ul,
        "top" / Int32ul,
        "right" / Int32ul,
        "bottom" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1005, version=0)
class Microsoft_Windows_MF_1005_0(Etw):
    pattern = Struct(
        "left" / Int32ul,
        "top" / Int32ul,
        "right" / Int32ul,
        "bottom" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1006, version=0)
class Microsoft_Windows_MF_1006_0(Etw):
    pattern = Struct(
        "Bitpump" / Int64ul,
        "Count" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1007, version=0)
class Microsoft_Windows_MF_1007_0(Etw):
    pattern = Struct(
        "QueuePtr" / Int64ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1008, version=0)
class Microsoft_Windows_MF_1008_0(Etw):
    pattern = Struct(
        "Bitpump" / Int64ul,
        "Type" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1009, version=0)
class Microsoft_Windows_MF_1009_0(Etw):
    pattern = Struct(
        "Bitpump" / Int64ul,
        "Type" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1010, version=0)
class Microsoft_Windows_MF_1010_0(Etw):
    pattern = Struct(
        "MFT" / Int64ul,
        "Type" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1011, version=0)
class Microsoft_Windows_MF_1011_0(Etw):
    pattern = Struct(
        "MFT" / Int64ul,
        "Type" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1012, version=0)
class Microsoft_Windows_MF_1012_0(Etw):
    pattern = Struct(
        "MPStream" / Int64ul,
        "Node" / Int32ul,
        "SampleCount" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1013, version=0)
class Microsoft_Windows_MF_1013_0(Etw):
    pattern = Struct(
        "MPStream" / Int64ul,
        "Node" / Int32ul,
        "SampleCount" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1014, version=0)
class Microsoft_Windows_MF_1014_0(Etw):
    pattern = Struct(
        "Bitpump" / Int64ul,
        "Type" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1015, version=0)
class Microsoft_Windows_MF_1015_0(Etw):
    pattern = Struct(
        "Bitpump" / Int64ul,
        "Type" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1016, version=0)
class Microsoft_Windows_MF_1016_0(Etw):
    pattern = Struct(
        "PathLock" / Int64ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1017, version=0)
class Microsoft_Windows_MF_1017_0(Etw):
    pattern = Struct(
        "PathLock" / Int64ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1018, version=0)
class Microsoft_Windows_MF_1018_0(Etw):
    pattern = Struct(
        "Bitpump" / Int64ul,
        "TimeStamp" / Int64ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1019, version=0)
class Microsoft_Windows_MF_1019_0(Etw):
    pattern = Struct(
        "Bitpump" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1020, version=0)
class Microsoft_Windows_MF_1020_0(Etw):
    pattern = Struct(
        "Bitpump" / Int64ul,
        "pSample" / Int64ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1021, version=0)
class Microsoft_Windows_MF_1021_0(Etw):
    pattern = Struct(
        "Bitpump" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1022, version=0)
class Microsoft_Windows_MF_1022_0(Etw):
    pattern = Struct(
        "Node" / Int64ul,
        "EventType" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1023, version=0)
class Microsoft_Windows_MF_1023_0(Etw):
    pattern = Struct(
        "Node" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1024, version=0)
class Microsoft_Windows_MF_1024_0(Etw):
    pattern = Struct(
        "MP" / Int64ul,
        "Node" / Int64ul,
        "StreamIndex" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1025, version=0)
class Microsoft_Windows_MF_1025_0(Etw):
    pattern = Struct(
        "MP" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1026, version=0)
class Microsoft_Windows_MF_1026_0(Etw):
    pattern = Struct(
        "MPStream" / Int64ul,
        "Node" / Int32ul,
        "Index" / Int32ul,
        "SampleCount" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1027, version=0)
class Microsoft_Windows_MF_1027_0(Etw):
    pattern = Struct(
        "MPStream" / Int64ul,
        "Node" / Int32ul,
        "Index" / Int32ul,
        "SampleCount" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1028, version=0)
class Microsoft_Windows_MF_1028_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "node" / Int64ul,
        "OutputIndex" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1029, version=0)
class Microsoft_Windows_MF_1029_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "node" / Int64ul,
        "result" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1098, version=0)
class Microsoft_Windows_MF_1098_0(Etw):
    pattern = Struct(
        "fromtype" / Guid
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1099, version=0)
class Microsoft_Windows_MF_1099_0(Etw):
    pattern = Struct(
        "exitPolling" / Int8ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1100, version=0)
class Microsoft_Windows_MF_1100_0(Etw):
    pattern = Struct(
        "stream" / Int32ul,
        "action" / Int32ul,
        "enablerReturned" / Int8ul,
        "hr" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1101, version=0)
class Microsoft_Windows_MF_1101_0(Etw):
    pattern = Struct(
        "streamid" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1102, version=0)
class Microsoft_Windows_MF_1102_0(Etw):
    pattern = Struct(
        "streamid" / Int32ul,
        "Action" / Int32ul,
        "policyReturned" / Int8ul,
        "hr" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1103, version=0)
class Microsoft_Windows_MF_1103_0(Etw):
    pattern = Struct(
        "object" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1104, version=0)
class Microsoft_Windows_MF_1104_0(Etw):
    pattern = Struct(
        "object" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1105, version=0)
class Microsoft_Windows_MF_1105_0(Etw):
    pattern = Struct(
        "object" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1106, version=0)
class Microsoft_Windows_MF_1106_0(Etw):
    pattern = Struct(
        "streamId" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1107, version=0)
class Microsoft_Windows_MF_1107_0(Etw):
    pattern = Struct(
        "bytes" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1108, version=0)
class Microsoft_Windows_MF_1108_0(Etw):
    pattern = Struct(
        "value" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1109, version=0)
class Microsoft_Windows_MF_1109_0(Etw):
    pattern = Struct(
        "value" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1110, version=0)
class Microsoft_Windows_MF_1110_0(Etw):
    pattern = Struct(
        "value" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1111, version=0)
class Microsoft_Windows_MF_1111_0(Etw):
    pattern = Struct(
        "version" / Int32ul,
        "streamId" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1112, version=0)
class Microsoft_Windows_MF_1112_0(Etw):
    pattern = Struct(
        "version" / Int32ul,
        "streamId" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1113, version=0)
class Microsoft_Windows_MF_1113_0(Etw):
    pattern = Struct(
        "isProtected" / Int8ul,
        "hr" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1114, version=0)
class Microsoft_Windows_MF_1114_0(Etw):
    pattern = Struct(
        "type" / Guid,
        "hr" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1115, version=0)
class Microsoft_Windows_MF_1115_0(Etw):
    pattern = Struct(
        "CLSID" / Guid,
        "hr" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1116, version=0)
class Microsoft_Windows_MF_1116_0(Etw):
    pattern = Struct(
        "attributes" / Int32ul,
        "outputSubtype" / Guid,
        "cSchemas" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1117, version=0)
class Microsoft_Windows_MF_1117_0(Etw):
    pattern = Struct(
        "context" / Int32ul,
        "type" / Guid
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1118, version=0)
class Microsoft_Windows_MF_1118_0(Etw):
    pattern = Struct(
        "type" / Int32ul,
        "streamId" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1119, version=0)
class Microsoft_Windows_MF_1119_0(Etw):
    pattern = Struct(
        "classId" / WString,
        "hr" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1121, version=0)
class Microsoft_Windows_MF_1121_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1123, version=0)
class Microsoft_Windows_MF_1123_0(Etw):
    pattern = Struct(
        "type" / Guid,
        "level" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1124, version=0)
class Microsoft_Windows_MF_1124_0(Etw):
    pattern = Struct(
        "WrapperPtr" / Int64ul,
        "StreamID" / Int32ul,
        "InputRequestsCount" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1126, version=0)
class Microsoft_Windows_MF_1126_0(Etw):
    pattern = Struct(
        "WrapperPtr" / Int64ul,
        "StreamID" / Int32ul,
        "SamplePtr" / Int64ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1127, version=0)
class Microsoft_Windows_MF_1127_0(Etw):
    pattern = Struct(
        "WrapperPtr" / Int64ul,
        "StreamID" / Int32ul,
        "SamplePtr" / Int64ul,
        "SampleTimestamp" / Int64ul,
        "InputQueueLength" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1128, version=0)
class Microsoft_Windows_MF_1128_0(Etw):
    pattern = Struct(
        "WrapperPtr" / Int64ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1129, version=0)
class Microsoft_Windows_MF_1129_0(Etw):
    pattern = Struct(
        "WrapperPtr" / Int64ul,
        "SamplePtr" / Int64ul,
        "SampleTime" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1130, version=0)
class Microsoft_Windows_MF_1130_0(Etw):
    pattern = Struct(
        "WrapperPtr" / Int64ul,
        "OutputQueueLength" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1131, version=0)
class Microsoft_Windows_MF_1131_0(Etw):
    pattern = Struct(
        "WrapperPtr" / Int64ul,
        "SamplePtr" / Int64ul,
        "SampleTimestamp" / Int64ul,
        "OutputQueueLength" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1132, version=0)
class Microsoft_Windows_MF_1132_0(Etw):
    pattern = Struct(
        "WrapperPtr" / Int64ul,
        "WorkQueueID" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1133, version=0)
class Microsoft_Windows_MF_1133_0(Etw):
    pattern = Struct(
        "WrapperPtr" / Int64ul,
        "WorkQueueID" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1134, version=0)
class Microsoft_Windows_MF_1134_0(Etw):
    pattern = Struct(
        "WrapperPtr" / Int64ul,
        "WorkQueueID" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1135, version=0)
class Microsoft_Windows_MF_1135_0(Etw):
    pattern = Struct(
        "ObjectPtr" / Int64ul,
        "MFTPtr" / Int64ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1136, version=0)
class Microsoft_Windows_MF_1136_0(Etw):
    pattern = Struct(
        "ObjectPtr" / Int64ul,
        "MFTPtr" / Int64ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1137, version=0)
class Microsoft_Windows_MF_1137_0(Etw):
    pattern = Struct(
        "WrapperPtr" / Int64ul,
        "WorkQueueID" / Int32ul,
        "DeadlineHNS" / Int64ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1138, version=0)
class Microsoft_Windows_MF_1138_0(Etw):
    pattern = Struct(
        "WrapperPtr" / Int64ul,
        "WorkQueueID" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1139, version=0)
class Microsoft_Windows_MF_1139_0(Etw):
    pattern = Struct(
        "WrapperPtr" / Int64ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1140, version=0)
class Microsoft_Windows_MF_1140_0(Etw):
    pattern = Struct(
        "WrapperPtr" / Int64ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1141, version=0)
class Microsoft_Windows_MF_1141_0(Etw):
    pattern = Struct(
        "WrapperPtr" / Int64ul,
        "SampleTimestamp" / Int64ul,
        "Duration0" / Int64ul,
        "Duration1" / Int64ul,
        "DurationResult" / Int64ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1145, version=0)
class Microsoft_Windows_MF_1145_0(Etw):
    pattern = Struct(
        "WrapperPtr" / Int64ul,
        "StreamID" / Int32ul,
        "SamplePtr" / Int64ul,
        "SampleTimestamp" / Int64ul,
        "Duration" / Int64ul,
        "InputQueueLength" / Int32ul,
        "ShatterInputSamples" / Int32ul,
        "BufferCount" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1146, version=0)
class Microsoft_Windows_MF_1146_0(Etw):
    pattern = Struct(
        "WrapperPtr" / Int64ul,
        "StreamID" / Int32ul,
        "SamplePtr" / Int64ul,
        "InputQueueLength" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1147, version=0)
class Microsoft_Windows_MF_1147_0(Etw):
    pattern = Struct(
        "WrapperPtr" / Int64ul,
        "StreamID" / Int32ul,
        "BufferIndex" / Int32ul,
        "Timestamp" / Int64ul,
        "Duration" / Int64ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1150, version=0)
class Microsoft_Windows_MF_1150_0(Etw):
    pattern = Struct(
        "bandwidthInPixels" / Int64ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1151, version=0)
class Microsoft_Windows_MF_1151_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1160, version=0)
class Microsoft_Windows_MF_1160_0(Etw):
    pattern = Struct(
        "ProcessID" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1200, version=0)
class Microsoft_Windows_MF_1200_0(Etw):
    pattern = Struct(
        "ComponentType" / Int32ul,
        "SettingType" / Int32ul,
        "Result" / Int32sl
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1201, version=0)
class Microsoft_Windows_MF_1201_0(Etw):
    pattern = Struct(
        "ComponentType" / Int32ul,
        "SettingType" / Int32ul,
        "Result" / Int32sl
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1202, version=0)
class Microsoft_Windows_MF_1202_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "eMessage" / Int32ul,
        "ulParam" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1203, version=0)
class Microsoft_Windows_MF_1203_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1204, version=0)
class Microsoft_Windows_MF_1204_0(Etw):
    pattern = Struct(
        "DeviceStreamName" / WString,
        "DeviceStreamId" / Int32ul,
        "MFTStreamId" / Int32ul,
        "samplePointer" / Int64ul,
        "DriverTimeStamp" / Int64ul,
        "SystemTimeStamp" / Int64ul,
        "SampleCompletionNumber" / Int64ul,
        "FlagTimeStamp" / CString,
        "StreamName" / CString
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1205, version=0)
class Microsoft_Windows_MF_1205_0(Etw):
    pattern = Struct(
        "ObjectPtr" / Int64ul,
        "WorkQueueID" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1206, version=0)
class Microsoft_Windows_MF_1206_0(Etw):
    pattern = Struct(
        "ObjectPtr" / Int64ul,
        "WorkQueueID" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1207, version=0)
class Microsoft_Windows_MF_1207_0(Etw):
    pattern = Struct(
        "WrapperPtr" / Int64ul,
        "StreamID" / Int32ul,
        "SamplePtr" / Int64ul,
        "RemainingInputRequests" / Int32ul,
        "RemainingQueuedInputSamples" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1208, version=0)
class Microsoft_Windows_MF_1208_0(Etw):
    pattern = Struct(
        "WrapperPtr" / Int64ul,
        "StreamID" / Int32ul,
        "SamplePtr" / Int64ul,
        "SampleTimestamp" / Int64ul,
        "InputQueueLength" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1209, version=0)
class Microsoft_Windows_MF_1209_0(Etw):
    pattern = Struct(
        "WrapperPtr" / Int64ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1210, version=0)
class Microsoft_Windows_MF_1210_0(Etw):
    pattern = Struct(
        "WrapperPtr" / Int64ul,
        "SamplePtr" / Int64ul,
        "SampleTime" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1211, version=0)
class Microsoft_Windows_MF_1211_0(Etw):
    pattern = Struct(
        "WrapperPtr" / Int64ul,
        "StreamID" / Int32ul,
        "SamplePtr" / Int64ul,
        "RemainingInputRequests" / Int32ul,
        "RemainingQueuedInputSamples" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1212, version=0)
class Microsoft_Windows_MF_1212_0(Etw):
    pattern = Struct(
        "WrapperPtr" / Int64ul,
        "StreamID" / Int32ul,
        "SamplePtr" / Int64ul,
        "SampleTimestamp" / Int64ul,
        "InputQueueLength" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1213, version=0)
class Microsoft_Windows_MF_1213_0(Etw):
    pattern = Struct(
        "WrapperPtr" / Int64ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1214, version=0)
class Microsoft_Windows_MF_1214_0(Etw):
    pattern = Struct(
        "WrapperPtr" / Int64ul,
        "SamplePtr" / Int64ul,
        "SampleTime" / Int64ul,
        "hr" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1215, version=0)
class Microsoft_Windows_MF_1215_0(Etw):
    pattern = Struct(
        "ObjectPtr" / Int64ul,
        "WorkQueueID" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1300, version=0)
class Microsoft_Windows_MF_1300_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "SamplePtr" / Int64ul,
        "Timestamp" / Int64sl
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1301, version=0)
class Microsoft_Windows_MF_1301_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "StreamID" / Int32sl,
        "Sample" / Int64ul,
        "Timestamp" / Int64sl
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1302, version=0)
class Microsoft_Windows_MF_1302_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Sample" / Int64ul,
        "PendingCount" / Int32sl
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1303, version=0)
class Microsoft_Windows_MF_1303_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "StreamID" / Int32sl,
        "Sample" / Int64ul,
        "TimeStamp" / Int64sl,
        "QueueLen" / Int32sl
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1304, version=0)
class Microsoft_Windows_MF_1304_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "StreamID" / Int32sl,
        "Token" / Int64ul,
        "QueueLen" / Int32sl
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1305, version=0)
class Microsoft_Windows_MF_1305_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "StreamID" / Int32sl,
        "Sample" / Int64ul,
        "Token" / Int64ul,
        "SampleQueueLen" / Int32sl,
        "RequestQueueLen" / Int32sl
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1306, version=0)
class Microsoft_Windows_MF_1306_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "tsOrig" / Int64sl,
        "sysOrig" / Int64sl,
        "tsFixed" / Int64sl,
        "sysFixed" / Int64sl,
        "rtNow" / Int64sl,
        "tsOut" / Int64sl,
        "tsOut_ms" / Int64sl,
        "Diff_Now_LastSys_ms" / Int64sl,
        "Fixed" / Int32sl,
        "State" / Int32sl
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1307, version=0)
class Microsoft_Windows_MF_1307_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "State" / Int32sl
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1308, version=0)
class Microsoft_Windows_MF_1308_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "State" / Int32sl
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1310, version=0)
class Microsoft_Windows_MF_1310_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1311, version=0)
class Microsoft_Windows_MF_1311_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1312, version=0)
class Microsoft_Windows_MF_1312_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "StreamID" / Int32sl,
        "Oldstate" / Int32sl,
        "Newstate" / Int32sl
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1313, version=0)
class Microsoft_Windows_MF_1313_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "UseSampleBasedBuffering" / Int32sl,
        "Rate" / Float32l,
        "IsEOS" / Int32sl,
        "UnprocessedSamples" / Int32sl,
        "Prerolled" / Int32sl
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1314, version=0)
class Microsoft_Windows_MF_1314_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1315, version=0)
class Microsoft_Windows_MF_1315_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1316, version=0)
class Microsoft_Windows_MF_1316_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1317, version=0)
class Microsoft_Windows_MF_1317_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Token" / Int64ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1318, version=0)
class Microsoft_Windows_MF_1318_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Token" / Int64ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1350, version=0)
class Microsoft_Windows_MF_1350_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1351, version=0)
class Microsoft_Windows_MF_1351_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "hr" / Int32sl
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1352, version=0)
class Microsoft_Windows_MF_1352_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "StreamID" / Int32sl,
        "SampleCount" / Int32sl
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1353, version=0)
class Microsoft_Windows_MF_1353_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "StreamID" / Int32sl,
        "timestamps" / Int64sl,
        "prevDuration" / Int64sl,
        "newDuration" / Int64sl,
        "mergedDuration" / Int64sl
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1417, version=0)
class Microsoft_Windows_MF_1417_0(Etw):
    pattern = Struct(
        "SymLink" / WString
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1418, version=0)
class Microsoft_Windows_MF_1418_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1419, version=0)
class Microsoft_Windows_MF_1419_0(Etw):
    pattern = Struct(
        "PinId" / Int32ul,
        "MediaType" / CString,
        "PinState" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1420, version=0)
class Microsoft_Windows_MF_1420_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1421, version=0)
class Microsoft_Windows_MF_1421_0(Etw):
    pattern = Struct(
        "PinId" / Int32ul,
        "MediaType" / CString,
        "PinState" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1422, version=0)
class Microsoft_Windows_MF_1422_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1423, version=0)
class Microsoft_Windows_MF_1423_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "StreamID" / Int32sl,
        "Sample" / Int64ul,
        "Timestamp" / Int64sl
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1424, version=0)
class Microsoft_Windows_MF_1424_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1425, version=0)
class Microsoft_Windows_MF_1425_0(Etw):
    pattern = Struct(
        "PinId" / Int32ul,
        "MediaType" / CString,
        "PinState" / Int32ul
    )


@declare(guid=guid("a7364e1a-894f-4b3d-a930-2ed9c8c4c811"), event_id=1426, version=0)
class Microsoft_Windows_MF_1426_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )

