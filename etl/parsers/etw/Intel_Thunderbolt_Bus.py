# -*- coding: utf-8 -*-
"""
Intel-Thunderbolt-Bus
GUID : 88ef8329-295d-4d79-ac09-38f9610a40c9
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("88ef8329-295d-4d79-ac09-38f9610a40c9"), event_id=1, version=1)
class Intel_Thunderbolt_Bus_1_1(Etw):
    pattern = Struct(
        "Version" / WString
    )


@declare(guid=guid("88ef8329-295d-4d79-ac09-38f9610a40c9"), event_id=2, version=1)
class Intel_Thunderbolt_Bus_2_1(Etw):
    pattern = Struct(
        "Date" / WString,
        "Time" / WString
    )


@declare(guid=guid("88ef8329-295d-4d79-ac09-38f9610a40c9"), event_id=3, version=1)
class Intel_Thunderbolt_Bus_3_1(Etw):
    pattern = Struct(
        "FunctionName" / WString
    )


@declare(guid=guid("88ef8329-295d-4d79-ac09-38f9610a40c9"), event_id=4, version=1)
class Intel_Thunderbolt_Bus_4_1(Etw):
    pattern = Struct(
        "FunctionName" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("88ef8329-295d-4d79-ac09-38f9610a40c9"), event_id=5, version=1)
class Intel_Thunderbolt_Bus_5_1(Etw):
    pattern = Struct(
        "FunctionName" / WString
    )


@declare(guid=guid("88ef8329-295d-4d79-ac09-38f9610a40c9"), event_id=6, version=1)
class Intel_Thunderbolt_Bus_6_1(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("88ef8329-295d-4d79-ac09-38f9610a40c9"), event_id=7, version=1)
class Intel_Thunderbolt_Bus_7_1(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("88ef8329-295d-4d79-ac09-38f9610a40c9"), event_id=101, version=1)
class Intel_Thunderbolt_Bus_101_1(Etw):
    pattern = Struct(
        "Version" / WString
    )


@declare(guid=guid("88ef8329-295d-4d79-ac09-38f9610a40c9"), event_id=102, version=1)
class Intel_Thunderbolt_Bus_102_1(Etw):
    pattern = Struct(
        "Message" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("88ef8329-295d-4d79-ac09-38f9610a40c9"), event_id=201, version=1)
class Intel_Thunderbolt_Bus_201_1(Etw):
    pattern = Struct(
        "DeviceId" / Int16ul,
        "RevisionId" / Int16ul,
        "SubVendorId" / Int16ul,
        "SubSystemId" / Int16ul
    )


@declare(guid=guid("88ef8329-295d-4d79-ac09-38f9610a40c9"), event_id=203, version=1)
class Intel_Thunderbolt_Bus_203_1(Etw):
    pattern = Struct(
        "Size" / Int32ul,
        "Virtual" / Int64ul,
        "Physical" / Int64ul
    )


@declare(guid=guid("88ef8329-295d-4d79-ac09-38f9610a40c9"), event_id=204, version=1)
class Intel_Thunderbolt_Bus_204_1(Etw):
    pattern = Struct(
        "Message" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("88ef8329-295d-4d79-ac09-38f9610a40c9"), event_id=205, version=1)
class Intel_Thunderbolt_Bus_205_1(Etw):
    pattern = Struct(
        "Message" / WString,
        "Id" / Int16ul,
        "Status" / Int32ul
    )


@declare(guid=guid("88ef8329-295d-4d79-ac09-38f9610a40c9"), event_id=206, version=1)
class Intel_Thunderbolt_Bus_206_1(Etw):
    pattern = Struct(
        "AllocatedBytes" / Int32ul,
        "NeededBytes" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("88ef8329-295d-4d79-ac09-38f9610a40c9"), event_id=301, version=1)
class Intel_Thunderbolt_Bus_301_1(Etw):
    pattern = Struct(
        "Message" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("88ef8329-295d-4d79-ac09-38f9610a40c9"), event_id=302, version=1)
class Intel_Thunderbolt_Bus_302_1(Etw):
    pattern = Struct(
        "Message" / Int32ul
    )


@declare(guid=guid("88ef8329-295d-4d79-ac09-38f9610a40c9"), event_id=303, version=1)
class Intel_Thunderbolt_Bus_303_1(Etw):
    pattern = Struct(
        "Queue" / Int64ul,
        "Request" / Int64ul,
        "OutputBufferLength" / Int32ul,
        "InputBufferLength" / Int32ul,
        "IoControlCode" / Int32ul
    )


@declare(guid=guid("88ef8329-295d-4d79-ac09-38f9610a40c9"), event_id=401, version=1)
class Intel_Thunderbolt_Bus_401_1(Etw):
    pattern = Struct(
        "Message" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("88ef8329-295d-4d79-ac09-38f9610a40c9"), event_id=402, version=1)
class Intel_Thunderbolt_Bus_402_1(Etw):
    pattern = Struct(
        "ProducerIndex" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("88ef8329-295d-4d79-ac09-38f9610a40c9"), event_id=403, version=1)
class Intel_Thunderbolt_Bus_403_1(Etw):
    pattern = Struct(
        "Message" / WString,
        "Size" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("88ef8329-295d-4d79-ac09-38f9610a40c9"), event_id=404, version=1)
class Intel_Thunderbolt_Bus_404_1(Etw):
    pattern = Struct(
        "MediumStatus" / WString
    )


@declare(guid=guid("88ef8329-295d-4d79-ac09-38f9610a40c9"), event_id=405, version=1)
class Intel_Thunderbolt_Bus_405_1(Etw):
    pattern = Struct(
        "FailureTime" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("88ef8329-295d-4d79-ac09-38f9610a40c9"), event_id=406, version=1)
class Intel_Thunderbolt_Bus_406_1(Etw):
    pattern = Struct(
        "FailureTime" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("88ef8329-295d-4d79-ac09-38f9610a40c9"), event_id=407, version=1)
class Intel_Thunderbolt_Bus_407_1(Etw):
    pattern = Struct(
        "Pdf" / WString,
        "Sw2fwcmd" / WString
    )


@declare(guid=guid("88ef8329-295d-4d79-ac09-38f9610a40c9"), event_id=408, version=1)
class Intel_Thunderbolt_Bus_408_1(Etw):
    pattern = Struct(
        "Sw2fwmail" / WString
    )


@declare(guid=guid("88ef8329-295d-4d79-ac09-38f9610a40c9"), event_id=409, version=1)
class Intel_Thunderbolt_Bus_409_1(Etw):
    pattern = Struct(
        "Message" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("88ef8329-295d-4d79-ac09-38f9610a40c9"), event_id=410, version=1)
class Intel_Thunderbolt_Bus_410_1(Etw):
    pattern = Struct(
        "Port" / Int32ul
    )


@declare(guid=guid("88ef8329-295d-4d79-ac09-38f9610a40c9"), event_id=501, version=1)
class Intel_Thunderbolt_Bus_501_1(Etw):
    pattern = Struct(
        "Message" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("88ef8329-295d-4d79-ac09-38f9610a40c9"), event_id=502, version=1)
class Intel_Thunderbolt_Bus_502_1(Etw):
    pattern = Struct(
        "Length" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("88ef8329-295d-4d79-ac09-38f9610a40c9"), event_id=503, version=1)
class Intel_Thunderbolt_Bus_503_1(Etw):
    pattern = Struct(
        "Interrupt" / Int8ul,
        "Memory" / Int8ul,
        "Status" / Int32ul
    )


@declare(guid=guid("88ef8329-295d-4d79-ac09-38f9610a40c9"), event_id=504, version=1)
class Intel_Thunderbolt_Bus_504_1(Etw):
    pattern = Struct(
        "MboxDelayError" / Int32ul
    )


@declare(guid=guid("88ef8329-295d-4d79-ac09-38f9610a40c9"), event_id=505, version=1)
class Intel_Thunderbolt_Bus_505_1(Etw):
    pattern = Struct(
        "MboxDelayError" / Int32ul
    )


@declare(guid=guid("88ef8329-295d-4d79-ac09-38f9610a40c9"), event_id=506, version=1)
class Intel_Thunderbolt_Bus_506_1(Etw):
    pattern = Struct(
        "DescriptorCount" / Int32ul,
        "MessageCount" / Int32ul,
        "NumInterruptVectors" / Int32ul,
        "Level" / Int32ul,
        "Vector" / Int32ul,
        "NumBARs" / Int32ul
    )


@declare(guid=guid("88ef8329-295d-4d79-ac09-38f9610a40c9"), event_id=507, version=1)
class Intel_Thunderbolt_Bus_507_1(Etw):
    pattern = Struct(
        "DescriptorCount" / Int32ul,
        "Level" / Int32ul,
        "Vector" / Int32ul,
        "NumBARs" / Int32ul
    )


@declare(guid=guid("88ef8329-295d-4d79-ac09-38f9610a40c9"), event_id=508, version=1)
class Intel_Thunderbolt_Bus_508_1(Etw):
    pattern = Struct(
        "DescriptorCount" / Int32ul,
        "LowPart" / Int32ul,
        "HighPart" / Int32ul,
        "Length" / Int32ul,
        "NumBARs" / Int32ul
    )


@declare(guid=guid("88ef8329-295d-4d79-ac09-38f9610a40c9"), event_id=509, version=1)
class Intel_Thunderbolt_Bus_509_1(Etw):
    pattern = Struct(
        "DescriptorCount" / Int32ul,
        "LowPart" / Int32ul,
        "HighPart" / Int32ul,
        "Length" / Int32ul,
        "NumBARs" / Int32ul
    )


@declare(guid=guid("88ef8329-295d-4d79-ac09-38f9610a40c9"), event_id=510, version=1)
class Intel_Thunderbolt_Bus_510_1(Etw):
    pattern = Struct(
        "Virtual" / Int64ul,
        "Physical" / Int64ul
    )


@declare(guid=guid("88ef8329-295d-4d79-ac09-38f9610a40c9"), event_id=511, version=1)
class Intel_Thunderbolt_Bus_511_1(Etw):
    pattern = Struct(
        "DescriptorCount" / Int32ul,
        "Data0" / Int32ul,
        "Data1" / Int32ul,
        "Data2" / Int32ul
    )


@declare(guid=guid("88ef8329-295d-4d79-ac09-38f9610a40c9"), event_id=512, version=1)
class Intel_Thunderbolt_Bus_512_1(Etw):
    pattern = Struct(
        "DescriptorCount" / Int32ul,
        "DescriptorType" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("88ef8329-295d-4d79-ac09-38f9610a40c9"), event_id=601, version=1)
class Intel_Thunderbolt_Bus_601_1(Etw):
    pattern = Struct(
        "Message" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("88ef8329-295d-4d79-ac09-38f9610a40c9"), event_id=602, version=1)
class Intel_Thunderbolt_Bus_602_1(Etw):
    pattern = Struct(
        "Type" / WString,
        "Index" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("88ef8329-295d-4d79-ac09-38f9610a40c9"), event_id=603, version=1)
class Intel_Thunderbolt_Bus_603_1(Etw):
    pattern = Struct(
        "Message" / Int32ul
    )


@declare(guid=guid("88ef8329-295d-4d79-ac09-38f9610a40c9"), event_id=604, version=1)
class Intel_Thunderbolt_Bus_604_1(Etw):
    pattern = Struct(
        "Version" / WString
    )


@declare(guid=guid("88ef8329-295d-4d79-ac09-38f9610a40c9"), event_id=605, version=1)
class Intel_Thunderbolt_Bus_605_1(Etw):
    pattern = Struct(
        "Pdf" / WString,
        "Description" / WString
    )


@declare(guid=guid("88ef8329-295d-4d79-ac09-38f9610a40c9"), event_id=606, version=1)
class Intel_Thunderbolt_Bus_606_1(Etw):
    pattern = Struct(
        "Pdf" / WString,
        "Fw2swnotify" / WString
    )


@declare(guid=guid("88ef8329-295d-4d79-ac09-38f9610a40c9"), event_id=607, version=1)
class Intel_Thunderbolt_Bus_607_1(Etw):
    pattern = Struct(
        "Pdf" / WString,
        "Fw2swres" / WString
    )


@declare(guid=guid("88ef8329-295d-4d79-ac09-38f9610a40c9"), event_id=608, version=1)
class Intel_Thunderbolt_Bus_608_1(Etw):
    pattern = Struct(
        "Pdf" / WString,
        "Cioerr" / WString
    )


@declare(guid=guid("88ef8329-295d-4d79-ac09-38f9610a40c9"), event_id=609, version=1)
class Intel_Thunderbolt_Bus_609_1(Etw):
    pattern = Struct(
        "Pdf" / WString,
        "Message" / Int32ul
    )


@declare(guid=guid("88ef8329-295d-4d79-ac09-38f9610a40c9"), event_id=610, version=1)
class Intel_Thunderbolt_Bus_610_1(Etw):
    pattern = Struct(
        "Description" / WString,
        "MessageIdOrInterruptRecognized" / Int32ul,
        "InterruptQueued" / Int8ul
    )


@declare(guid=guid("88ef8329-295d-4d79-ac09-38f9610a40c9"), event_id=611, version=1)
class Intel_Thunderbolt_Bus_611_1(Etw):
    pattern = Struct(
        "Message" / WString,
        "PortNum" / Int8ul
    )


@declare(guid=guid("88ef8329-295d-4d79-ac09-38f9610a40c9"), event_id=701, version=1)
class Intel_Thunderbolt_Bus_701_1(Etw):
    pattern = Struct(
        "Message" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("88ef8329-295d-4d79-ac09-38f9610a40c9"), event_id=702, version=1)
class Intel_Thunderbolt_Bus_702_1(Etw):
    pattern = Struct(
        "Version" / WString
    )


@declare(guid=guid("88ef8329-295d-4d79-ac09-38f9610a40c9"), event_id=703, version=1)
class Intel_Thunderbolt_Bus_703_1(Etw):
    pattern = Struct(
        "Type" / WString,
        "Index" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("88ef8329-295d-4d79-ac09-38f9610a40c9"), event_id=704, version=1)
class Intel_Thunderbolt_Bus_704_1(Etw):
    pattern = Struct(
        "Type" / WString,
        "Index" / Int32ul,
        "NumDescriptors" / Int32ul
    )


@declare(guid=guid("88ef8329-295d-4d79-ac09-38f9610a40c9"), event_id=705, version=1)
class Intel_Thunderbolt_Bus_705_1(Etw):
    pattern = Struct(
        "Description" / WString,
        "Sw2fwmail" / WString,
        "Delay" / Int32ul
    )


@declare(guid=guid("88ef8329-295d-4d79-ac09-38f9610a40c9"), event_id=706, version=1)
class Intel_Thunderbolt_Bus_706_1(Etw):
    pattern = Struct(
        "FrameSize" / Int32ul
    )


@declare(guid=guid("88ef8329-295d-4d79-ac09-38f9610a40c9"), event_id=707, version=1)
class Intel_Thunderbolt_Bus_707_1(Etw):
    pattern = Struct(
        "Description" / WString,
        "Status" / Int32ul,
        "AllocatedBuffers" / Int32ul
    )


@declare(guid=guid("88ef8329-295d-4d79-ac09-38f9610a40c9"), event_id=708, version=1)
class Intel_Thunderbolt_Bus_708_1(Etw):
    pattern = Struct(
        "Description" / WString,
        "Status" / Int32ul,
        "AllocatedBuffers" / Int32ul
    )


@declare(guid=guid("88ef8329-295d-4d79-ac09-38f9610a40c9"), event_id=709, version=1)
class Intel_Thunderbolt_Bus_709_1(Etw):
    pattern = Struct(
        "Message" / WString,
        "Status" / Int32ul
    )

