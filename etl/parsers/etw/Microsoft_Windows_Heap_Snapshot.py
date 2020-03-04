# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Heap-Snapshot
GUID : 901d2afa-4ff6-46d7-8d0e-53645e1a47f5
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("901d2afa-4ff6-46d7-8d0e-53645e1a47f5"), event_id=100, version=1)
class Microsoft_Windows_Heap_Snapshot_100_1(Etw):
    pattern = Struct(
        "HeapSnapshotInstance" / Int32ul,
        "HeapSnapshotSequence" / Int32ul,
        "HeapSnapshotBufferLen" / Int32ul,
        "HeapSnapshotBuffer" / Bytes(lambda this: this.HeapSnapshotBufferLen)
    )


@declare(guid=guid("901d2afa-4ff6-46d7-8d0e-53645e1a47f5"), event_id=200, version=1)
class Microsoft_Windows_Heap_Snapshot_200_1(Etw):
    pattern = Struct(
        "HeapSnapshotInstance" / Int32ul,
        "TotalData" / Int32ul
    )

