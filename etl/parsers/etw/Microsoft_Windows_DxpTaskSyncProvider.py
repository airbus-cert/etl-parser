# -*- coding: utf-8 -*-
"""
Microsoft-Windows-DxpTaskSyncProvider
GUID : 271c5228-c3fe-4e47-831f-48c3652ce5ac
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("271c5228-c3fe-4e47-831f-48c3652ce5ac"), event_id=330, version=0)
class Microsoft_Windows_DxpTaskSyncProvider_330_0(Etw):
    pattern = Struct(
        "ContainerID" / Guid
    )


@declare(guid=guid("271c5228-c3fe-4e47-831f-48c3652ce5ac"), event_id=331, version=0)
class Microsoft_Windows_DxpTaskSyncProvider_331_0(Etw):
    pattern = Struct(
        "ContainerID" / Guid
    )


@declare(guid=guid("271c5228-c3fe-4e47-831f-48c3652ce5ac"), event_id=332, version=0)
class Microsoft_Windows_DxpTaskSyncProvider_332_0(Etw):
    pattern = Struct(
        "ContainerID" / Guid
    )


@declare(guid=guid("271c5228-c3fe-4e47-831f-48c3652ce5ac"), event_id=333, version=0)
class Microsoft_Windows_DxpTaskSyncProvider_333_0(Etw):
    pattern = Struct(
        "ContainerID" / Guid
    )

