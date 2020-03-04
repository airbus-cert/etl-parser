# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Direct3D10
GUID : 9b7e4c0f-342c-4106-a19f-4f2704f689f0
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("9b7e4c0f-342c-4106-a19f-4f2704f689f0"), event_id=1, version=0)
class Microsoft_Windows_Direct3D10_1_0(Etw):
    pattern = Struct(
        "pObject" / Int64ul,
        "CchOldDebugObjectName" / Int32ul,
        "OldDebugObjectName" / Bytes(lambda this: this.CchOldDebugObjectName),
        "CchNewDebugObjectName" / Int32ul,
        "NewDebugObjectName" / Bytes(lambda this: this.CchNewDebugObjectName)
    )


@declare(guid=guid("9b7e4c0f-342c-4106-a19f-4f2704f689f0"), event_id=2, version=0)
class Microsoft_Windows_Direct3D10_2_0(Etw):
    pattern = Struct(
        "pObject" / Int64ul,
        "CchDebugObjectName" / Int32ul,
        "DebugObjectName" / Bytes(lambda this: this.CchDebugObjectName)
    )


@declare(guid=guid("9b7e4c0f-342c-4106-a19f-4f2704f689f0"), event_id=3, version=0)
class Microsoft_Windows_Direct3D10_3_0(Etw):
    pattern = Struct(
        "pID3D10Device" / Int64ul,
        "pIDXGIDevice" / Int64ul,
        "pIDXGIAdapter" / Int64ul,
        "CreationFlags" / Int32ul,
        "hKMAdapter" / Int32ul,
        "hUMAdapter" / Int64ul,
        "UMAdapterVersion" / Int64ul,
        "hKMDevice" / Int32ul,
        "hUMDevice" / Int64ul,
        "UMDeviceVersion" / Int64ul,
        "UMDeviceFlags" / Int32ul
    )


@declare(guid=guid("9b7e4c0f-342c-4106-a19f-4f2704f689f0"), event_id=4, version=0)
class Microsoft_Windows_Direct3D10_4_0(Etw):
    pattern = Struct(
        "pID3D10Device" / Int64ul,
        "pIDXGIDevice" / Int64ul,
        "pIDXGIAdapter" / Int64ul,
        "CreationFlags" / Int32ul,
        "hKMAdapter" / Int32ul,
        "hUMAdapter" / Int64ul,
        "UMAdapterVersion" / Int64ul,
        "hKMDevice" / Int32ul,
        "hUMDevice" / Int64ul,
        "UMDeviceVersion" / Int64ul,
        "UMDeviceFlags" / Int32ul
    )


@declare(guid=guid("9b7e4c0f-342c-4106-a19f-4f2704f689f0"), event_id=5, version=0)
class Microsoft_Windows_Direct3D10_5_0(Etw):
    pattern = Struct(
        "pID3D10Device" / Int64ul,
        "pIDXGIDevice" / Int64ul,
        "pIDXGIAdapter" / Int64ul,
        "CreationFlags" / Int32ul,
        "hKMAdapter" / Int32ul,
        "hUMAdapter" / Int64ul,
        "UMAdapterVersion" / Int64ul,
        "hKMDevice" / Int32ul,
        "hUMDevice" / Int64ul,
        "UMDeviceVersion" / Int64ul,
        "UMDeviceFlags" / Int32ul
    )


@declare(guid=guid("9b7e4c0f-342c-4106-a19f-4f2704f689f0"), event_id=6, version=0)
class Microsoft_Windows_Direct3D10_6_0(Etw):
    pattern = Struct(
        "pID3D10Resource" / Int64ul,
        "pIDXGISurface" / Int64ul,
        "pID3D10Device" / Int64ul,
        "Dimension" / Int32ul,
        "Usage" / Int32ul,
        "Width" / Int32ul,
        "Height" / Int32ul,
        "Depth" / Int32ul,
        "MipLevels" / Int32ul,
        "ArraySize" / Int32ul,
        "Format" / Int32ul,
        "SampleCount" / Int32ul,
        "SampleQuality" / Int32ul,
        "BindFlags" / Int32ul,
        "CPUAccessFlags" / Int32ul,
        "MiscFlags" / Int32ul,
        "hKMResource" / Int32ul,
        "hUMResource" / Int64ul,
        "UMResourceMiscFlags" / Int32ul
    )


@declare(guid=guid("9b7e4c0f-342c-4106-a19f-4f2704f689f0"), event_id=7, version=0)
class Microsoft_Windows_Direct3D10_7_0(Etw):
    pattern = Struct(
        "pID3D10Resource" / Int64ul,
        "pIDXGISurface" / Int64ul,
        "pID3D10Device" / Int64ul,
        "Dimension" / Int32ul,
        "Usage" / Int32ul,
        "Width" / Int32ul,
        "Height" / Int32ul,
        "Depth" / Int32ul,
        "MipLevels" / Int32ul,
        "ArraySize" / Int32ul,
        "Format" / Int32ul,
        "SampleCount" / Int32ul,
        "SampleQuality" / Int32ul,
        "BindFlags" / Int32ul,
        "CPUAccessFlags" / Int32ul,
        "MiscFlags" / Int32ul,
        "hKMResource" / Int32ul,
        "hUMResource" / Int64ul,
        "UMResourceMiscFlags" / Int32ul
    )


@declare(guid=guid("9b7e4c0f-342c-4106-a19f-4f2704f689f0"), event_id=8, version=0)
class Microsoft_Windows_Direct3D10_8_0(Etw):
    pattern = Struct(
        "pID3D10Resource" / Int64ul,
        "pIDXGISurface" / Int64ul,
        "pID3D10Device" / Int64ul,
        "Dimension" / Int32ul,
        "Usage" / Int32ul,
        "Width" / Int32ul,
        "Height" / Int32ul,
        "Depth" / Int32ul,
        "MipLevels" / Int32ul,
        "ArraySize" / Int32ul,
        "Format" / Int32ul,
        "SampleCount" / Int32ul,
        "SampleQuality" / Int32ul,
        "BindFlags" / Int32ul,
        "CPUAccessFlags" / Int32ul,
        "MiscFlags" / Int32ul,
        "hKMResource" / Int32ul,
        "hUMResource" / Int64ul,
        "UMResourceMiscFlags" / Int32ul
    )


@declare(guid=guid("9b7e4c0f-342c-4106-a19f-4f2704f689f0"), event_id=9, version=0)
class Microsoft_Windows_Direct3D10_9_0(Etw):
    pattern = Struct(
        "pID3D10Resource" / Int64ul,
        "pIDXGISurface" / Int64ul,
        "pID3D10Device" / Int64ul,
        "Dimension" / Int32ul,
        "Usage" / Int32ul,
        "Width" / Int32ul,
        "Height" / Int32ul,
        "Depth" / Int32ul,
        "MipLevels" / Int32ul,
        "ArraySize" / Int32ul,
        "Format" / Int32ul,
        "SampleCount" / Int32ul,
        "SampleQuality" / Int32ul,
        "BindFlags" / Int32ul,
        "CPUAccessFlags" / Int32ul,
        "MiscFlags" / Int32ul,
        "hKMResource" / Int32ul,
        "hUMResource" / Int64ul,
        "UMResourceMiscFlags" / Int32ul
    )


@declare(guid=guid("9b7e4c0f-342c-4106-a19f-4f2704f689f0"), event_id=10, version=0)
class Microsoft_Windows_Direct3D10_10_0(Etw):
    pattern = Struct(
        "pID3D10Resource" / Int64ul,
        "pIDXGISurface" / Int64ul,
        "pID3D10Device" / Int64ul,
        "Dimension" / Int32ul,
        "Usage" / Int32ul,
        "Width" / Int32ul,
        "Height" / Int32ul,
        "Depth" / Int32ul,
        "MipLevels" / Int32ul,
        "ArraySize" / Int32ul,
        "Format" / Int32ul,
        "SampleCount" / Int32ul,
        "SampleQuality" / Int32ul,
        "BindFlags" / Int32ul,
        "CPUAccessFlags" / Int32ul,
        "MiscFlags" / Int32ul,
        "hKMResource" / Int32ul,
        "hUMResource" / Int64ul,
        "UMResourceMiscFlags" / Int32ul
    )


@declare(guid=guid("9b7e4c0f-342c-4106-a19f-4f2704f689f0"), event_id=11, version=0)
class Microsoft_Windows_Direct3D10_11_0(Etw):
    pattern = Struct(
        "pID3D10Resource" / Int64ul,
        "pIDXGISurface" / Int64ul,
        "pID3D10Device" / Int64ul,
        "Dimension" / Int32ul,
        "Usage" / Int32ul,
        "Width" / Int32ul,
        "Height" / Int32ul,
        "Depth" / Int32ul,
        "MipLevels" / Int32ul,
        "ArraySize" / Int32ul,
        "Format" / Int32ul,
        "SampleCount" / Int32ul,
        "SampleQuality" / Int32ul,
        "BindFlags" / Int32ul,
        "CPUAccessFlags" / Int32ul,
        "MiscFlags" / Int32ul,
        "hKMResource" / Int32ul,
        "hUMResource" / Int64ul,
        "UMResourceMiscFlags" / Int32ul
    )


@declare(guid=guid("9b7e4c0f-342c-4106-a19f-4f2704f689f0"), event_id=12, version=0)
class Microsoft_Windows_Direct3D10_12_0(Etw):
    pattern = Struct(
        "pID3D10Resource" / Int64ul,
        "pIDXGISurface" / Int64ul,
        "pID3D10Device" / Int64ul,
        "Dimension" / Int32ul,
        "Usage" / Int32ul,
        "Width" / Int32ul,
        "Height" / Int32ul,
        "Depth" / Int32ul,
        "MipLevels" / Int32ul,
        "ArraySize" / Int32ul,
        "Format" / Int32ul,
        "SampleCount" / Int32ul,
        "SampleQuality" / Int32ul,
        "BindFlags" / Int32ul,
        "CPUAccessFlags" / Int32ul,
        "MiscFlags" / Int32ul,
        "hKMResource" / Int32ul,
        "hUMResource" / Int64ul,
        "UMResourceMiscFlags" / Int32ul
    )


@declare(guid=guid("9b7e4c0f-342c-4106-a19f-4f2704f689f0"), event_id=13, version=0)
class Microsoft_Windows_Direct3D10_13_0(Etw):
    pattern = Struct(
        "pID3D10Resource" / Int64ul,
        "pIDXGISurface" / Int64ul,
        "pID3D10Device" / Int64ul,
        "Dimension" / Int32ul,
        "Usage" / Int32ul,
        "Width" / Int32ul,
        "Height" / Int32ul,
        "Depth" / Int32ul,
        "MipLevels" / Int32ul,
        "ArraySize" / Int32ul,
        "Format" / Int32ul,
        "SampleCount" / Int32ul,
        "SampleQuality" / Int32ul,
        "BindFlags" / Int32ul,
        "CPUAccessFlags" / Int32ul,
        "MiscFlags" / Int32ul,
        "hKMResource" / Int32ul,
        "hUMResource" / Int64ul,
        "UMResourceMiscFlags" / Int32ul
    )


@declare(guid=guid("9b7e4c0f-342c-4106-a19f-4f2704f689f0"), event_id=14, version=0)
class Microsoft_Windows_Direct3D10_14_0(Etw):
    pattern = Struct(
        "pID3D10Resource" / Int64ul,
        "pIDXGISurface" / Int64ul,
        "pID3D10Device" / Int64ul,
        "Dimension" / Int32ul,
        "Usage" / Int32ul,
        "Width" / Int32ul,
        "Height" / Int32ul,
        "Depth" / Int32ul,
        "MipLevels" / Int32ul,
        "ArraySize" / Int32ul,
        "Format" / Int32ul,
        "SampleCount" / Int32ul,
        "SampleQuality" / Int32ul,
        "BindFlags" / Int32ul,
        "CPUAccessFlags" / Int32ul,
        "MiscFlags" / Int32ul,
        "hKMResource" / Int32ul,
        "hUMResource" / Int64ul,
        "UMResourceMiscFlags" / Int32ul
    )


@declare(guid=guid("9b7e4c0f-342c-4106-a19f-4f2704f689f0"), event_id=15, version=0)
class Microsoft_Windows_Direct3D10_15_0(Etw):
    pattern = Struct(
        "pID3D10Resource" / Int64ul,
        "pIDXGISurface" / Int64ul,
        "pID3D10Device" / Int64ul,
        "Dimension" / Int32ul,
        "Usage" / Int32ul,
        "Width" / Int32ul,
        "Height" / Int32ul,
        "Depth" / Int32ul,
        "MipLevels" / Int32ul,
        "ArraySize" / Int32ul,
        "Format" / Int32ul,
        "SampleCount" / Int32ul,
        "SampleQuality" / Int32ul,
        "BindFlags" / Int32ul,
        "CPUAccessFlags" / Int32ul,
        "MiscFlags" / Int32ul,
        "hKMResource" / Int32ul,
        "hUMResource" / Int64ul,
        "UMResourceMiscFlags" / Int32ul
    )


@declare(guid=guid("9b7e4c0f-342c-4106-a19f-4f2704f689f0"), event_id=16, version=0)
class Microsoft_Windows_Direct3D10_16_0(Etw):
    pattern = Struct(
        "pID3D10Resource" / Int64ul,
        "pIDXGISurface" / Int64ul,
        "pID3D10Device" / Int64ul,
        "Dimension" / Int32ul,
        "Usage" / Int32ul,
        "Width" / Int32ul,
        "Height" / Int32ul,
        "Depth" / Int32ul,
        "MipLevels" / Int32ul,
        "ArraySize" / Int32ul,
        "Format" / Int32ul,
        "SampleCount" / Int32ul,
        "SampleQuality" / Int32ul,
        "BindFlags" / Int32ul,
        "CPUAccessFlags" / Int32ul,
        "MiscFlags" / Int32ul,
        "hKMResource" / Int32ul,
        "hUMResource" / Int64ul,
        "UMResourceMiscFlags" / Int32ul
    )


@declare(guid=guid("9b7e4c0f-342c-4106-a19f-4f2704f689f0"), event_id=17, version=0)
class Microsoft_Windows_Direct3D10_17_0(Etw):
    pattern = Struct(
        "pID3D10Resource" / Int64ul,
        "pIDXGISurface" / Int64ul,
        "pID3D10Device" / Int64ul,
        "Dimension" / Int32ul,
        "Usage" / Int32ul,
        "Width" / Int32ul,
        "Height" / Int32ul,
        "Depth" / Int32ul,
        "MipLevels" / Int32ul,
        "ArraySize" / Int32ul,
        "Format" / Int32ul,
        "SampleCount" / Int32ul,
        "SampleQuality" / Int32ul,
        "BindFlags" / Int32ul,
        "CPUAccessFlags" / Int32ul,
        "MiscFlags" / Int32ul,
        "hKMResource" / Int32ul,
        "hUMResource" / Int64ul,
        "UMResourceMiscFlags" / Int32ul
    )


@declare(guid=guid("9b7e4c0f-342c-4106-a19f-4f2704f689f0"), event_id=18, version=0)
class Microsoft_Windows_Direct3D10_18_0(Etw):
    pattern = Struct(
        "Resources" / Int32ul,
        "pIDXGISurfaces" / Int64ul,
        "hNewKMResources" / Int32ul
    )

