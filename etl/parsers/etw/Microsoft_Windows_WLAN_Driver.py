# -*- coding: utf-8 -*-
"""
Microsoft-Windows-WLAN-Driver
GUID : daa6a96b-f3e7-4d4d-a0d6-31a350e6a445
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("daa6a96b-f3e7-4d4d-a0d6-31a350e6a445"), event_id=0, version=1)
class Microsoft_Windows_WLAN_Driver_0_1(Etw):
    pattern = Struct(
        "FrameUniqueID" / Int32ul,
        "PortNumber" / Int32ul,
        "TID" / Int8ul,
        "PeerID" / Int32ul,
        "PayloadLength" / Int16ul,
        "QueueLength" / Int16ul,
        "QueueState" / Int8ul,
        "CustomData1" / Int32ul,
        "CustomData2" / Int32ul,
        "CustomData3" / Int32ul
    )


@declare(guid=guid("daa6a96b-f3e7-4d4d-a0d6-31a350e6a445"), event_id=1, version=1)
class Microsoft_Windows_WLAN_Driver_1_1(Etw):
    pattern = Struct(
        "FrameUniqueID" / Int32ul,
        "QueueLength" / Int16ul,
        "QueueState" / Int8ul,
        "Status" / Int32ul,
        "CustomData1" / Int32ul,
        "CustomData2" / Int32ul,
        "CustomData3" / Int32ul
    )


@declare(guid=guid("daa6a96b-f3e7-4d4d-a0d6-31a350e6a445"), event_id=2, version=1)
class Microsoft_Windows_WLAN_Driver_2_1(Etw):
    pattern = Struct(
        "FrameUniqueID" / Int32ul,
        "SequenceNumber" / Int16ul,
        "Status" / Int32ul,
        "RetryCount" / Int16ul,
        "CustomData1" / Int32ul,
        "CustomData2" / Int32ul,
        "CustomData3" / Int32ul
    )


@declare(guid=guid("daa6a96b-f3e7-4d4d-a0d6-31a350e6a445"), event_id=3, version=1)
class Microsoft_Windows_WLAN_Driver_3_1(Etw):
    pattern = Struct(
        "FrameUniqueID" / Int32ul,
        "CustomData1" / Int32ul,
        "CustomData2" / Int32ul,
        "CustomData3" / Int32ul
    )


@declare(guid=guid("daa6a96b-f3e7-4d4d-a0d6-31a350e6a445"), event_id=4, version=1)
class Microsoft_Windows_WLAN_Driver_4_1(Etw):
    pattern = Struct(
        "FrameUniqueID" / Int32ul,
        "TID" / Int8ul,
        "PeerID" / Int32ul,
        "SequenceNumber" / Int16ul,
        "PayloadLength" / Int16ul,
        "QueueLength" / Int16ul,
        "Retransmit" / Int8ul,
        "Status" / Int32ul,
        "CustomData1" / Int32ul,
        "CustomData2" / Int32ul,
        "CustomData3" / Int32ul
    )


@declare(guid=guid("daa6a96b-f3e7-4d4d-a0d6-31a350e6a445"), event_id=5, version=1)
class Microsoft_Windows_WLAN_Driver_5_1(Etw):
    pattern = Struct(
        "FrameUniqueID" / Int32ul,
        "PortNumber" / Int32ul,
        "RxBacklog" / Int16ul,
        "CustomData1" / Int32ul,
        "CustomData2" / Int32ul,
        "CustomData3" / Int32ul
    )


@declare(guid=guid("daa6a96b-f3e7-4d4d-a0d6-31a350e6a445"), event_id=6, version=1)
class Microsoft_Windows_WLAN_Driver_6_1(Etw):
    pattern = Struct(
        "FrameUniqueID" / Int32ul,
        "QueueLength" / Int16ul,
        "RxBacklog" / Int16ul,
        "CustomData1" / Int32ul,
        "CustomData2" / Int32ul,
        "CustomData3" / Int32ul
    )

