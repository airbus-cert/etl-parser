# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Kernel-PnP-Rundown
GUID : b3a0c2c8-83bb-4ddf-9f8d-4b22d3c38ad7
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("b3a0c2c8-83bb-4ddf-9f8d-4b22d3c38ad7"), event_id=1, version=0)
class Microsoft_Windows_Kernel_PnP_Rundown_1_0(Etw):
    pattern = Struct(
        "ResourceConsumerPdo" / Int64ul,
        "ConnectionId" / Int64ul,
        "ResourceConsumerInstancePathLength" / Int32ul,
        "ResourceConsumerInstancePath" / Bytes(lambda this: this.ResourceConsumerInstancePathLength)
    )


@declare(guid=guid("b3a0c2c8-83bb-4ddf-9f8d-4b22d3c38ad7"), event_id=2, version=0)
class Microsoft_Windows_Kernel_PnP_Rundown_2_0(Etw):
    pattern = Struct(
        "Pdo" / Int64ul,
        "ParentPdo" / Int64ul
    )


@declare(guid=guid("b3a0c2c8-83bb-4ddf-9f8d-4b22d3c38ad7"), event_id=3, version=0)
class Microsoft_Windows_Kernel_PnP_Rundown_3_0(Etw):
    pattern = Struct(
        "DevNode" / Int64ul,
        "ParentDevNode" / Int64ul
    )


@declare(guid=guid("b3a0c2c8-83bb-4ddf-9f8d-4b22d3c38ad7"), event_id=3, version=1)
class Microsoft_Windows_Kernel_PnP_Rundown_3_1(Etw):
    pattern = Struct(
        "DevNode" / Int64ul,
        "ParentDevNode" / Int64ul,
        "InstancePathLength" / Int32ul,
        "InstancePath" / Bytes(lambda this: this.InstancePathLength)
    )

