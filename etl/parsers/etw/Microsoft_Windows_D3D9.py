# -*- coding: utf-8 -*-
"""
Microsoft-Windows-D3D9
GUID : 783aca0a-790e-4d7f-8451-aa850511c6b9
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("783aca0a-790e-4d7f-8451-aa850511c6b9"), event_id=1, version=0)
class Microsoft_Windows_D3D9_1_0(Etw):
    pattern = Struct(
        "pSwapchain" / Int64ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("783aca0a-790e-4d7f-8451-aa850511c6b9"), event_id=2, version=0)
class Microsoft_Windows_D3D9_2_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("783aca0a-790e-4d7f-8451-aa850511c6b9"), event_id=3, version=0)
class Microsoft_Windows_D3D9_3_0(Etw):
    pattern = Struct(
        "pSwapchain" / Int64ul,
        "Width" / Int32ul,
        "Height" / Int32ul,
        "BackbufferFormat" / Int32ul,
        "BackbufferCount" / Int32ul,
        "SwapEffect" / Int32ul,
        "Windowed" / Int8ul,
        "PresentationInterval" / Int32ul,
        "AdditionalSwapchain" / Int8ul
    )


@declare(guid=guid("783aca0a-790e-4d7f-8451-aa850511c6b9"), event_id=4, version=0)
class Microsoft_Windows_D3D9_4_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("783aca0a-790e-4d7f-8451-aa850511c6b9"), event_id=5, version=0)
class Microsoft_Windows_D3D9_5_0(Etw):
    pattern = Struct(
        "LogicalSurfaceHandle" / Int64ul,
        "BackBufferCount" / Int16ul,
        "SharedHandles" / Int32ul
    )


@declare(guid=guid("783aca0a-790e-4d7f-8451-aa850511c6b9"), event_id=6, version=0)
class Microsoft_Windows_D3D9_6_0(Etw):
    pattern = Struct(
        "IsOn" / Int8ul
    )


@declare(guid=guid("783aca0a-790e-4d7f-8451-aa850511c6b9"), event_id=7, version=0)
class Microsoft_Windows_D3D9_7_0(Etw):
    pattern = Struct(
        "LogicalSurfaceHandle" / Int64ul,
        "BackBufferNumber" / Int32ul,
        "BackBufferHandle" / Int32ul
    )


@declare(guid=guid("783aca0a-790e-4d7f-8451-aa850511c6b9"), event_id=8, version=0)
class Microsoft_Windows_D3D9_8_0(Etw):
    pattern = Struct(
        "LogicalSurfaceHandle" / Int64ul,
        "AdjustValue" / Int32ul,
        "FenceValue" / Int64ul
    )


@declare(guid=guid("783aca0a-790e-4d7f-8451-aa850511c6b9"), event_id=9, version=0)
class Microsoft_Windows_D3D9_9_0(Etw):
    pattern = Struct(
        "ReturnValue" / Int32ul,
        "PresentCount" / Int32ul,
        "PresentRefreshCount" / Int32ul,
        "SyncRefreshCount" / Int32ul,
        "SyncQPCTime" / Int64ul
    )

