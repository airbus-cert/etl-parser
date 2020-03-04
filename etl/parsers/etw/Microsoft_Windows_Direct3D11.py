# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Direct3D11
GUID : db6f6ddb-ac77-4e88-8253-819df9bbf140
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=1, version=0)
class Microsoft_Windows_Direct3D11_1_0(Etw):
    pattern = Struct(
        "pObject" / Int64ul,
        "CchOldDebugObjectName" / Int32ul,
        "OldDebugObjectName" / Bytes(lambda this: this.CchOldDebugObjectName),
        "CchNewDebugObjectName" / Int32ul,
        "NewDebugObjectName" / Bytes(lambda this: this.CchNewDebugObjectName)
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=2, version=0)
class Microsoft_Windows_Direct3D11_2_0(Etw):
    pattern = Struct(
        "pObject" / Int64ul,
        "CchDebugObjectName" / Int32ul,
        "DebugObjectName" / Bytes(lambda this: this.CchDebugObjectName)
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=3, version=0)
class Microsoft_Windows_Direct3D11_3_0(Etw):
    pattern = Struct(
        "pID3D11Device" / Int64ul,
        "pIDXGIDevice" / Int64ul,
        "pIDXGIAdapter" / Int64ul,
        "CreationFlags" / Int32ul,
        "FeatureLevel" / Int32ul,
        "FeatureSupport" / Int32ul,
        "hKMAdapter" / Int32ul,
        "hUMAdapter" / Int64ul,
        "UMAdapterVersion" / Int64ul,
        "hKMDevice" / Int32ul,
        "hUMDevice" / Int64ul,
        "UMDeviceVersion" / Int64ul,
        "UMDeviceFlags" / Int32ul
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=4, version=0)
class Microsoft_Windows_Direct3D11_4_0(Etw):
    pattern = Struct(
        "pID3D11Device" / Int64ul,
        "pIDXGIDevice" / Int64ul,
        "pIDXGIAdapter" / Int64ul,
        "CreationFlags" / Int32ul,
        "FeatureLevel" / Int32ul,
        "FeatureSupport" / Int32ul,
        "hKMAdapter" / Int32ul,
        "hUMAdapter" / Int64ul,
        "UMAdapterVersion" / Int64ul,
        "hKMDevice" / Int32ul,
        "hUMDevice" / Int64ul,
        "UMDeviceVersion" / Int64ul,
        "UMDeviceFlags" / Int32ul
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=5, version=0)
class Microsoft_Windows_Direct3D11_5_0(Etw):
    pattern = Struct(
        "pID3D11Device" / Int64ul,
        "pIDXGIDevice" / Int64ul,
        "pIDXGIAdapter" / Int64ul,
        "CreationFlags" / Int32ul,
        "FeatureLevel" / Int32ul,
        "FeatureSupport" / Int32ul,
        "hKMAdapter" / Int32ul,
        "hUMAdapter" / Int64ul,
        "UMAdapterVersion" / Int64ul,
        "hKMDevice" / Int32ul,
        "hUMDevice" / Int64ul,
        "UMDeviceVersion" / Int64ul,
        "UMDeviceFlags" / Int32ul
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=6, version=0)
class Microsoft_Windows_Direct3D11_6_0(Etw):
    pattern = Struct(
        "pID3D11Resource" / Int64ul,
        "pIDXGISurface" / Int64ul,
        "pID3D11Device" / Int64ul,
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
        "StructureByteStride" / Int32ul,
        "hKMResource" / Int32ul,
        "hUMResource" / Int64ul,
        "UMResourceMiscFlags" / Int32ul
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=7, version=0)
class Microsoft_Windows_Direct3D11_7_0(Etw):
    pattern = Struct(
        "pID3D11Resource" / Int64ul,
        "pIDXGISurface" / Int64ul,
        "pID3D11Device" / Int64ul,
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
        "StructureByteStride" / Int32ul,
        "hKMResource" / Int32ul,
        "hUMResource" / Int64ul,
        "UMResourceMiscFlags" / Int32ul
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=8, version=0)
class Microsoft_Windows_Direct3D11_8_0(Etw):
    pattern = Struct(
        "pID3D11Resource" / Int64ul,
        "pIDXGISurface" / Int64ul,
        "pID3D11Device" / Int64ul,
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
        "StructureByteStride" / Int32ul,
        "hKMResource" / Int32ul,
        "hUMResource" / Int64ul,
        "UMResourceMiscFlags" / Int32ul
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=9, version=0)
class Microsoft_Windows_Direct3D11_9_0(Etw):
    pattern = Struct(
        "pID3D11Resource" / Int64ul,
        "pIDXGISurface" / Int64ul,
        "pID3D11Device" / Int64ul,
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
        "StructureByteStride" / Int32ul,
        "hKMResource" / Int32ul,
        "hUMResource" / Int64ul,
        "UMResourceMiscFlags" / Int32ul
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=10, version=0)
class Microsoft_Windows_Direct3D11_10_0(Etw):
    pattern = Struct(
        "pID3D11Resource" / Int64ul,
        "pIDXGISurface" / Int64ul,
        "pID3D11Device" / Int64ul,
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
        "StructureByteStride" / Int32ul,
        "hKMResource" / Int32ul,
        "hUMResource" / Int64ul,
        "UMResourceMiscFlags" / Int32ul
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=11, version=0)
class Microsoft_Windows_Direct3D11_11_0(Etw):
    pattern = Struct(
        "pID3D11Resource" / Int64ul,
        "pIDXGISurface" / Int64ul,
        "pID3D11Device" / Int64ul,
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
        "StructureByteStride" / Int32ul,
        "hKMResource" / Int32ul,
        "hUMResource" / Int64ul,
        "UMResourceMiscFlags" / Int32ul
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=12, version=0)
class Microsoft_Windows_Direct3D11_12_0(Etw):
    pattern = Struct(
        "pID3D11Resource" / Int64ul,
        "pIDXGISurface" / Int64ul,
        "pID3D11Device" / Int64ul,
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
        "StructureByteStride" / Int32ul,
        "hKMResource" / Int32ul,
        "hUMResource" / Int64ul,
        "UMResourceMiscFlags" / Int32ul
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=13, version=0)
class Microsoft_Windows_Direct3D11_13_0(Etw):
    pattern = Struct(
        "pID3D11Resource" / Int64ul,
        "pIDXGISurface" / Int64ul,
        "pID3D11Device" / Int64ul,
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
        "StructureByteStride" / Int32ul,
        "hKMResource" / Int32ul,
        "hUMResource" / Int64ul,
        "UMResourceMiscFlags" / Int32ul
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=14, version=0)
class Microsoft_Windows_Direct3D11_14_0(Etw):
    pattern = Struct(
        "pID3D11Resource" / Int64ul,
        "pIDXGISurface" / Int64ul,
        "pID3D11Device" / Int64ul,
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
        "StructureByteStride" / Int32ul,
        "hKMResource" / Int32ul,
        "hUMResource" / Int64ul,
        "UMResourceMiscFlags" / Int32ul
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=15, version=0)
class Microsoft_Windows_Direct3D11_15_0(Etw):
    pattern = Struct(
        "pID3D11Resource" / Int64ul,
        "pIDXGISurface" / Int64ul,
        "pID3D11Device" / Int64ul,
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
        "StructureByteStride" / Int32ul,
        "hKMResource" / Int32ul,
        "hUMResource" / Int64ul,
        "UMResourceMiscFlags" / Int32ul
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=16, version=0)
class Microsoft_Windows_Direct3D11_16_0(Etw):
    pattern = Struct(
        "pID3D11Resource" / Int64ul,
        "pIDXGISurface" / Int64ul,
        "pID3D11Device" / Int64ul,
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
        "StructureByteStride" / Int32ul,
        "hKMResource" / Int32ul,
        "hUMResource" / Int64ul,
        "UMResourceMiscFlags" / Int32ul
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=17, version=0)
class Microsoft_Windows_Direct3D11_17_0(Etw):
    pattern = Struct(
        "pID3D11Resource" / Int64ul,
        "pIDXGISurface" / Int64ul,
        "pID3D11Device" / Int64ul,
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
        "StructureByteStride" / Int32ul,
        "hKMResource" / Int32ul,
        "hUMResource" / Int64ul,
        "UMResourceMiscFlags" / Int32ul
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=18, version=0)
class Microsoft_Windows_Direct3D11_18_0(Etw):
    pattern = Struct(
        "Resources" / Int32ul,
        "pIDXGISurfaces" / Int64ul,
        "hNewKMResources" / Int32ul
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=19, version=0)
class Microsoft_Windows_Direct3D11_19_0(Etw):
    pattern = Struct(
        "SemaphoreHandle" / Int64ul,
        "AdjustValue" / Int32ul,
        "PresentCount" / Int32ul
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=26, version=0)
class Microsoft_Windows_Direct3D11_26_0(Etw):
    pattern = Struct(
        "BufferSize" / Int32ul,
        "Buffer" / Bytes(lambda this: this.BufferSize)
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=27, version=0)
class Microsoft_Windows_Direct3D11_27_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "riid" / Guid,
        "m_Ret" / Int32ul,
        "ppvObject" / Int64ul
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=28, version=0)
class Microsoft_Windows_Direct3D11_28_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "ReturnValue" / Int32ul
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=29, version=0)
class Microsoft_Windows_Direct3D11_29_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "ReturnValue" / Int32ul
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=30, version=0)
class Microsoft_Windows_Direct3D11_30_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=35, version=0)
class Microsoft_Windows_Direct3D11_35_0(Etw):
    pattern = Struct(
        "pID3D11Device" / Int64ul,
        "pID3D11DeviceContext" / Int64ul,
        "ContextType" / Int32ul,
        "ContextFlags" / Int32ul
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=36, version=0)
class Microsoft_Windows_Direct3D11_36_0(Etw):
    pattern = Struct(
        "pID3D11Device" / Int64ul,
        "pID3D11DeviceContext" / Int64ul,
        "ContextType" / Int32ul,
        "ContextFlags" / Int32ul
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=37, version=0)
class Microsoft_Windows_Direct3D11_37_0(Etw):
    pattern = Struct(
        "pID3D11Device" / Int64ul,
        "pID3D11DeviceContext" / Int64ul,
        "ContextType" / Int32ul,
        "ContextFlags" / Int32ul
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=38, version=0)
class Microsoft_Windows_Direct3D11_38_0(Etw):
    pattern = Struct(
        "pID3D11DeviceContext" / Int64ul,
        "APISequenceNumber" / Int64ul,
        "Label" / WString,
        "Data" / Int32sl
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=39, version=0)
class Microsoft_Windows_Direct3D11_39_0(Etw):
    pattern = Struct(
        "CPUFrequency" / Int64ul,
        "FirstAPISequenceNumber" / Int64ul,
        "pID3D11DeviceContext" / Int64ul,
        "CPUTimeHigh" / Int32ul,
        "ThreadIDs" / Int8ul,
        "ThreadID" / Int32ul,
        "DataSize" / Int32ul,
        "Data" / Int8ul
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=40, version=0)
class Microsoft_Windows_Direct3D11_40_0(Etw):
    pattern = Struct(
        "pID3D11DeviceContext" / Int64ul,
        "Type" / Int32ul
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=41, version=0)
class Microsoft_Windows_Direct3D11_41_0(Etw):
    pattern = Struct(
        "pIDXGIDevice" / Int64ul,
        "hContext" / Int32ul,
        "BroadcastContexts" / Int8ul,
        "hBroadcastContexts" / Int32ul,
        "MarkerLogType" / Int32ul,
        "RenderCBSequenceNumber" / Int32ul,
        "FirstAPISequenceNumberHigh" / Int32ul,
        "CompletedAPISequenceNumberLow0Size" / Int32ul,
        "CompletedAPISequenceNumberLow1Size" / Int32ul,
        "BegunAPISequenceNumberLow0Size" / Int32ul,
        "BegunAPISequenceNumberLow1Size" / Int32ul,
        "CompletedAPISequenceNumberLow0" / Int32ul,
        "CompletedAPISequenceNumberLow1" / Int32ul,
        "BegunAPISequenceNumberLow0" / Int32ul,
        "BegunAPISequenceNumberLow1" / Int32ul
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=42, version=0)
class Microsoft_Windows_Direct3D11_42_0(Etw):
    pattern = Struct(
        "pID3D11DeviceContext" / Int64ul,
        "pID3D11CommandList" / Int64ul
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=43, version=0)
class Microsoft_Windows_Direct3D11_43_0(Etw):
    pattern = Struct(
        "pID3D11DeviceContext" / Int64ul,
        "pID3D11CommandList" / Int64ul
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=44, version=0)
class Microsoft_Windows_Direct3D11_44_0(Etw):
    pattern = Struct(
        "pID3D11DeviceContext" / Int64ul,
        "pID3D11CommandList" / Int64ul
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=45, version=0)
class Microsoft_Windows_Direct3D11_45_0(Etw):
    pattern = Struct(
        "InsertionAPISequenceNumber" / Int64ul,
        "pID3D11DeviceContext" / Int64ul,
        "hContext" / Int32ul,
        "Index" / Int32sl,
        "StringIndex" / Int32sl,
        "MarkerDescription" / WString
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=46, version=0)
class Microsoft_Windows_Direct3D11_46_0(Etw):
    pattern = Struct(
        "pID3D11Device" / Int64ul,
        "StringIndex" / Int32sl,
        "Description" / WString
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=1714, version=0)
class Microsoft_Windows_Direct3D11_1714_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "NumResources" / Int32ul,
        "ppResources" / Int64ul,
        "Priority" / Int32ul
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=1715, version=0)
class Microsoft_Windows_Direct3D11_1715_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=1716, version=0)
class Microsoft_Windows_Direct3D11_1716_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "NumResources" / Int32ul,
        "ppResources" / Int64ul,
        "NumDiscardedResources" / Int32ul,
        "pDiscarded" / Int32ul
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=1717, version=0)
class Microsoft_Windows_Direct3D11_1717_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul,
        "pDiscarded" / Int32ul
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=1720, version=0)
class Microsoft_Windows_Direct3D11_1720_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "pEnum" / Int64ul,
        "RateConversionIndex" / Int32ul,
        "ppVideoProcessor" / Int64ul
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=1721, version=0)
class Microsoft_Windows_Direct3D11_1721_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul,
        "ppVideoProcessor" / Int64ul
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=1722, version=0)
class Microsoft_Windows_Direct3D11_1722_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "pVideoDescTID_D3D11_VIDEO_DECODER_DESC" / Int8ul,
        "pConfigTID_D3D11_VIDEO_DECODER_CONFIG" / Int32ul,
        "ppDecoder" / Int64ul
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=1723, version=0)
class Microsoft_Windows_Direct3D11_1723_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul,
        "ppDecoder" / Int64ul
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=1728, version=0)
class Microsoft_Windows_Direct3D11_1728_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=1729, version=0)
class Microsoft_Windows_Direct3D11_1729_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=1734, version=0)
class Microsoft_Windows_Direct3D11_1734_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=1735, version=0)
class Microsoft_Windows_Direct3D11_1735_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=1778, version=0)
class Microsoft_Windows_Direct3D11_1778_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "pVideoProcessor" / Int64ul,
        "pView" / Int64ul,
        "OutputFrame" / Int32ul,
        "StreamCount" / Int32ul,
        "pStreamsTID_D3D11_VIDEO_PROCESSOR_STREAM" / Int16ul
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=1779, version=0)
class Microsoft_Windows_Direct3D11_1779_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=1780, version=0)
class Microsoft_Windows_Direct3D11_1780_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "pDecoder" / Int64ul,
        "Type" / Int32ul,
        "pBufferSize" / Int32ul,
        "ppBuffer" / Int64ul
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=1781, version=0)
class Microsoft_Windows_Direct3D11_1781_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul,
        "pBufferSize" / Int32ul,
        "ppBuffer" / Int64ul
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=1784, version=0)
class Microsoft_Windows_Direct3D11_1784_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "pDecoder" / Int64ul,
        "View" / Int64ul,
        "ContentKeySize" / Int32ul,
        "pContentKey" / Int64ul
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=1785, version=0)
class Microsoft_Windows_Direct3D11_1785_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=1786, version=0)
class Microsoft_Windows_Direct3D11_1786_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "pDecoder" / Int64ul
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=1787, version=0)
class Microsoft_Windows_Direct3D11_1787_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=1788, version=0)
class Microsoft_Windows_Direct3D11_1788_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "pDecoder" / Int64ul,
        "NumBuffers" / Int32ul,
        "pBufferDescTID_D3D11_VIDEO_DECODER_BUFFER_DESC" / Int8ul
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=1789, version=0)
class Microsoft_Windows_Direct3D11_1789_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=1804, version=0)
class Microsoft_Windows_Direct3D11_1804_0(Etw):
    pattern = Struct(
        "pDXGIDevice" / Int64ul
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=1806, version=0)
class Microsoft_Windows_Direct3D11_1806_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "CryptoType" / Guid,
        "KeyExhangeType" / Guid,
        "ppCryptoSession" / Int64ul
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=1807, version=0)
class Microsoft_Windows_Direct3D11_1807_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul,
        "ppCryptoSession" / Int64ul
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=1808, version=0)
class Microsoft_Windows_Direct3D11_1808_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "pCryptoSession" / Int64ul
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=1809, version=0)
class Microsoft_Windows_Direct3D11_1809_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=1810, version=0)
class Microsoft_Windows_Direct3D11_1810_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "pVideoProcessor" / Int64ul,
        "OutputWidth" / Int32ul,
        "OutputHeight" / Int32ul,
        "OutputFormat" / Int32ul,
        "StreamCount" / Int32ul
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=1811, version=0)
class Microsoft_Windows_Direct3D11_1811_0(Etw):
    pattern = Struct(
        "BehaviorHints" / Int32ul,
        "m_Ret" / Int32ul
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=1812, version=0)
class Microsoft_Windows_Direct3D11_1812_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "pCryptoSession" / Int64ul,
        "TeardownCount" / Int32ul
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=1813, version=0)
class Microsoft_Windows_Direct3D11_1813_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "TeardownCount" / Int32ul,
        "Recover" / Int32ul
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=1814, version=0)
class Microsoft_Windows_Direct3D11_1814_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "SourceWidth" / Int32ul,
        "SourceHeight" / Int32ul,
        "SourceFormat" / Int32ul,
        "SourceColorspace" / Int32ul,
        "DestWidth" / Int32ul,
        "DestHeight" / Int32ul,
        "DestFormat" / Int32ul,
        "DestColorspace" / Int32ul,
        "Rotation" / Int32ul
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=1815, version=0)
class Microsoft_Windows_Direct3D11_1815_0(Etw):
    pattern = Struct(
        "pCryptoSession" / Int64ul
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=1816, version=0)
class Microsoft_Windows_Direct3D11_1816_0(Etw):
    pattern = Struct(
        "pCryptoSession" / Int64ul
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=1817, version=0)
class Microsoft_Windows_Direct3D11_1817_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "TeardownCount" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=1818, version=0)
class Microsoft_Windows_Direct3D11_1818_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "pDecoder" / Int64ul,
        "NumBuffers" / Int32ul,
        "pBufferDescTID_D3D11_VIDEO_DECODER_BUFFER_DESC1" / Int8ul
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=1819, version=0)
class Microsoft_Windows_Direct3D11_1819_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=1820, version=0)
class Microsoft_Windows_Direct3D11_1820_0(Etw):
    pattern = Struct(
        "Index" / Int32ul,
        "Code" / Int32ul,
        "ThreadId" / Int32ul,
        "Message" / CString
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=1821, version=0)
class Microsoft_Windows_Direct3D11_1821_0(Etw):
    pattern = Struct(
        "hKMResource" / Int32ul,
        "hUMSharedResource" / Int64ul,
        "Name" / WString
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=1822, version=0)
class Microsoft_Windows_Direct3D11_1822_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "pCryptoSession" / Int64ul
    )


@declare(guid=guid("db6f6ddb-ac77-4e88-8253-819df9bbf140"), event_id=1823, version=0)
class Microsoft_Windows_Direct3D11_1823_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )

