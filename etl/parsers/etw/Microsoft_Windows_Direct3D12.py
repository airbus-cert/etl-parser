# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Direct3D12
GUID : 5d8087dd-3a9b-4f56-90df-49196cdc4f11
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=1, version=0)
class Microsoft_Windows_Direct3D12_1_0(Etw):
    pattern = Struct(
        "pObject" / Int64ul,
        "CchOldDebugObjectName" / Int32ul,
        "OldDebugObjectName" / Bytes(lambda this: this.CchOldDebugObjectName),
        "CchNewDebugObjectName" / Int32ul,
        "NewDebugObjectName" / Bytes(lambda this: this.CchNewDebugObjectName)
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=2, version=0)
class Microsoft_Windows_Direct3D12_2_0(Etw):
    pattern = Struct(
        "pObject" / Int64ul,
        "CchDebugObjectName" / Int32ul,
        "DebugObjectName" / Bytes(lambda this: this.CchDebugObjectName)
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=3, version=0)
class Microsoft_Windows_Direct3D12_3_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "FeatureLevel" / Int32ul,
        "hKMAdapter" / Int32ul,
        "hUMAdapter" / Int64ul,
        "UMAdapterVersion" / Int64ul,
        "hKMDevice" / Int32ul,
        "UMDeviceVersion" / Int64ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=4, version=0)
class Microsoft_Windows_Direct3D12_4_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "FeatureLevel" / Int32ul,
        "hKMAdapter" / Int32ul,
        "hUMAdapter" / Int64ul,
        "UMAdapterVersion" / Int64ul,
        "hKMDevice" / Int32ul,
        "UMDeviceVersion" / Int64ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=5, version=0)
class Microsoft_Windows_Direct3D12_5_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "FeatureLevel" / Int32ul,
        "hKMAdapter" / Int32ul,
        "hUMAdapter" / Int64ul,
        "UMAdapterVersion" / Int64ul,
        "hKMDevice" / Int32ul,
        "UMDeviceVersion" / Int64ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=19, version=0)
class Microsoft_Windows_Direct3D12_19_0(Etw):
    pattern = Struct(
        "SemaphoreHandle" / Int64ul,
        "AdjustValue" / Int32ul,
        "PresentCount" / Int32ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=26, version=0)
class Microsoft_Windows_Direct3D12_26_0(Etw):
    pattern = Struct(
        "BufferSize" / Int32ul,
        "Buffer" / Bytes(lambda this: this.BufferSize)
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=35, version=0)
class Microsoft_Windows_Direct3D12_35_0(Etw):
    pattern = Struct(
        "pID3D12CommandQueue" / Int64ul,
        "Metadata" / Int32ul,
        "DataSize" / Int32ul,
        "Data" / Int8ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=36, version=0)
class Microsoft_Windows_Direct3D12_36_0(Etw):
    pattern = Struct(
        "pID3D12CommandQueue" / Int64ul,
        "Metadata" / Int32ul,
        "DataSize" / Int32ul,
        "Data" / Int8ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=37, version=0)
class Microsoft_Windows_Direct3D12_37_0(Etw):
    pattern = Struct(
        "pID3D12CommandQueue" / Int64ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=38, version=0)
class Microsoft_Windows_Direct3D12_38_0(Etw):
    pattern = Struct(
        "pID3D12CommandList" / Int64ul,
        "APISequenceNumber" / Int64ul,
        "Metadata" / Int32ul,
        "DataSize" / Int32ul,
        "Data" / Int8ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=39, version=0)
class Microsoft_Windows_Direct3D12_39_0(Etw):
    pattern = Struct(
        "CPUFrequency" / Int64ul,
        "FirstAPISequenceNumber" / Int64ul,
        "pID3D12CommandList" / Int64ul,
        "CPUTimeHigh" / Int32ul,
        "ThreadIDCount" / Int8ul,
        "ThreadIDs" / Int32ul,
        "DataSize" / Int32ul,
        "Data" / Int8ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=40, version=0)
class Microsoft_Windows_Direct3D12_40_0(Etw):
    pattern = Struct(
        "pID3D12DeviceContext" / Int64ul,
        "Type" / Int32ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=41, version=0)
class Microsoft_Windows_Direct3D12_41_0(Etw):
    pattern = Struct(
        "pID3D12CommandQueue" / Int64ul,
        "ContextCount" / Int32ul,
        "Contexts" / Int32ul,
        "LoopIteration" / Int32ul,
        "SubmitCommandCBSequence" / Int32ul,
        "FirstAPISequenceNumberHigh" / Int32ul,
        "CompletedAPISequenceNumberSize" / Int32ul,
        "CompletedAPISequenceNumber" / Int32ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=45, version=0)
class Microsoft_Windows_Direct3D12_45_0(Etw):
    pattern = Struct(
        "InsertionAPISequenceNumber" / Int64ul,
        "pID3D12CommandList" / Int64ul,
        "Index" / Int32sl,
        "MarkerDescription" / WString
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=47, version=0)
class Microsoft_Windows_Direct3D12_47_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pCommandQueue" / Int64ul,
        "type" / Int32ul,
        "ContextCount" / Int32ul,
        "UMDContexts" / Int32ul,
        "Priority" / Int32sl,
        "Flags" / Int32ul,
        "NodeMask" / Int32ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=48, version=0)
class Microsoft_Windows_Direct3D12_48_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pCommandQueue" / Int64ul,
        "type" / Int32ul,
        "ContextCount" / Int32ul,
        "UMDContexts" / Int32ul,
        "Priority" / Int32sl,
        "Flags" / Int32ul,
        "NodeMask" / Int32ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=49, version=0)
class Microsoft_Windows_Direct3D12_49_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pCommandQueue" / Int64ul,
        "type" / Int32ul,
        "ContextCount" / Int32ul,
        "UMDContexts" / Int32ul,
        "Priority" / Int32sl,
        "Flags" / Int32ul,
        "NodeMask" / Int32ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=50, version=0)
class Microsoft_Windows_Direct3D12_50_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12CommandList" / Int64ul,
        "SequenceNumber" / Int64ul,
        "type" / Int32ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=51, version=0)
class Microsoft_Windows_Direct3D12_51_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12CommandList" / Int64ul,
        "SequenceNumber" / Int64ul,
        "type" / Int32ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=52, version=0)
class Microsoft_Windows_Direct3D12_52_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12CommandList" / Int64ul,
        "SequenceNumber" / Int64ul,
        "type" / Int32ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=53, version=0)
class Microsoft_Windows_Direct3D12_53_0(Etw):
    pattern = Struct(
        "pID3D12CommandQueue" / Int64ul,
        "pID3D12CommandList" / Int64ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=54, version=0)
class Microsoft_Windows_Direct3D12_54_0(Etw):
    pattern = Struct(
        "pID3D12CommandQueue" / Int64ul,
        "pID3D12CommandList" / Int64ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=55, version=0)
class Microsoft_Windows_Direct3D12_55_0(Etw):
    pattern = Struct(
        "pObject" / Int64ul,
        "CchOldDebugObjectName" / Int32ul,
        "OldDebugObjectName" / Bytes(lambda this: this.CchOldDebugObjectName),
        "CchNewDebugObjectName" / Int32ul,
        "NewDebugObjectName" / Bytes(lambda this: this.CchNewDebugObjectName)
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=56, version=0)
class Microsoft_Windows_Direct3D12_56_0(Etw):
    pattern = Struct(
        "pObject" / Int64ul,
        "CchDebugObjectName" / Int32ul,
        "DebugObjectName" / Bytes(lambda this: this.CchDebugObjectName)
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=57, version=0)
class Microsoft_Windows_Direct3D12_57_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12Fence" / Int64ul,
        "pDXGKFence" / Int64ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=58, version=0)
class Microsoft_Windows_Direct3D12_58_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12Fence" / Int64ul,
        "pDXGKFence" / Int64ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=59, version=0)
class Microsoft_Windows_Direct3D12_59_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12Fence" / Int64ul,
        "pDXGKFence" / Int64ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=60, version=0)
class Microsoft_Windows_Direct3D12_60_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12CommandAllocator" / Int64ul,
        "type" / Int32ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=61, version=0)
class Microsoft_Windows_Direct3D12_61_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12CommandAllocator" / Int64ul,
        "type" / Int32ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=62, version=0)
class Microsoft_Windows_Direct3D12_62_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12CommandAllocator" / Int64ul,
        "type" / Int32ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=63, version=0)
class Microsoft_Windows_Direct3D12_63_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12GraphicsPipelineState" / Int64ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=64, version=0)
class Microsoft_Windows_Direct3D12_64_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12GraphicsPipelineState" / Int64ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=65, version=0)
class Microsoft_Windows_Direct3D12_65_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12GraphicsPipelineState" / Int64ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=66, version=0)
class Microsoft_Windows_Direct3D12_66_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12DescriptorHeap" / Int64ul,
        "Type" / Int32ul,
        "NumDescriptors" / Int32ul,
        "Flags" / Int32ul,
        "NodeMask" / Int32ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=67, version=0)
class Microsoft_Windows_Direct3D12_67_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12DescriptorHeap" / Int64ul,
        "Type" / Int32ul,
        "NumDescriptors" / Int32ul,
        "Flags" / Int32ul,
        "NodeMask" / Int32ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=68, version=0)
class Microsoft_Windows_Direct3D12_68_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12DescriptorHeap" / Int64ul,
        "Type" / Int32ul,
        "NumDescriptors" / Int32ul,
        "Flags" / Int32ul,
        "NodeMask" / Int32ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=69, version=0)
class Microsoft_Windows_Direct3D12_69_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12RootSignature" / Int64ul,
        "NodeMask" / Int32ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=70, version=0)
class Microsoft_Windows_Direct3D12_70_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12RootSignature" / Int64ul,
        "NodeMask" / Int32ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=71, version=0)
class Microsoft_Windows_Direct3D12_71_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12RootSignature" / Int64ul,
        "NodeMask" / Int32ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=72, version=0)
class Microsoft_Windows_Direct3D12_72_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12Heap" / Int64ul,
        "SizeInBytes" / Int64ul,
        "Alignment" / Int64ul,
        "Type" / Int32ul,
        "CPUPageProperty" / Int32ul,
        "MemoryPoolPreference" / Int32ul,
        "CreationNodeMask" / Int32ul,
        "VisibleNodeMask" / Int32ul,
        "Flags" / Int32ul,
        "pID3D12ConjoinedResource" / Int64ul,
        "hKMAllocation" / Int32ul,
        "hKMResource" / Int32ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=73, version=0)
class Microsoft_Windows_Direct3D12_73_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12Heap" / Int64ul,
        "SizeInBytes" / Int64ul,
        "Alignment" / Int64ul,
        "Type" / Int32ul,
        "CPUPageProperty" / Int32ul,
        "MemoryPoolPreference" / Int32ul,
        "CreationNodeMask" / Int32ul,
        "VisibleNodeMask" / Int32ul,
        "Flags" / Int32ul,
        "pID3D12ConjoinedResource" / Int64ul,
        "hKMAllocation" / Int32ul,
        "hKMResource" / Int32ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=74, version=0)
class Microsoft_Windows_Direct3D12_74_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12Heap" / Int64ul,
        "SizeInBytes" / Int64ul,
        "Alignment" / Int64ul,
        "Type" / Int32ul,
        "CPUPageProperty" / Int32ul,
        "MemoryPoolPreference" / Int32ul,
        "CreationNodeMask" / Int32ul,
        "VisibleNodeMask" / Int32ul,
        "Flags" / Int32ul,
        "pID3D12ConjoinedResource" / Int64ul,
        "hKMAllocation" / Int32ul,
        "hKMResource" / Int32ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=75, version=0)
class Microsoft_Windows_Direct3D12_75_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12QueryHeap" / Int64ul,
        "Type" / Int32ul,
        "Count" / Int32ul,
        "NodeMask" / Int32ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=76, version=0)
class Microsoft_Windows_Direct3D12_76_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12QueryHeap" / Int64ul,
        "Type" / Int32ul,
        "Count" / Int32ul,
        "NodeMask" / Int32ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=77, version=0)
class Microsoft_Windows_Direct3D12_77_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12QueryHeap" / Int64ul,
        "Type" / Int32ul,
        "Count" / Int32ul,
        "NodeMask" / Int32ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=78, version=0)
class Microsoft_Windows_Direct3D12_78_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12CommandSignature" / Int64ul,
        "ByteStride" / Int32ul,
        "NumArgumentDescs" / Int32ul,
        "NodeMask" / Int32ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=79, version=0)
class Microsoft_Windows_Direct3D12_79_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12CommandSignature" / Int64ul,
        "ByteStride" / Int32ul,
        "NumArgumentDescs" / Int32ul,
        "NodeMask" / Int32ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=80, version=0)
class Microsoft_Windows_Direct3D12_80_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12CommandSignature" / Int64ul,
        "ByteStride" / Int32ul,
        "NumArgumentDescs" / Int32ul,
        "NodeMask" / Int32ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=81, version=0)
class Microsoft_Windows_Direct3D12_81_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12PipelineLibrary" / Int64ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=82, version=0)
class Microsoft_Windows_Direct3D12_82_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12PipelineLibrary" / Int64ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=83, version=0)
class Microsoft_Windows_Direct3D12_83_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12PipelineLibrary" / Int64ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=84, version=0)
class Microsoft_Windows_Direct3D12_84_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12VideoDecoder" / Int64ul,
        "NodeMask" / Int32ul,
        "DecodeProfile" / Guid,
        "BitstreamEncryption" / Int32ul,
        "InterlaceFormat" / Int32ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=85, version=0)
class Microsoft_Windows_Direct3D12_85_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12VideoDecoder" / Int64ul,
        "NodeMask" / Int32ul,
        "DecodeProfile" / Guid,
        "BitstreamEncryption" / Int32ul,
        "InterlaceFormat" / Int32ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=86, version=0)
class Microsoft_Windows_Direct3D12_86_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12VideoDecoder" / Int64ul,
        "NodeMask" / Int32ul,
        "DecodeProfile" / Guid,
        "BitstreamEncryption" / Int32ul,
        "InterlaceFormat" / Int32ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=87, version=0)
class Microsoft_Windows_Direct3D12_87_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12VideoProcessor" / Int64ul,
        "NodeMask" / Int32ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=88, version=0)
class Microsoft_Windows_Direct3D12_88_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12VideoProcessor" / Int64ul,
        "NodeMask" / Int32ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=89, version=0)
class Microsoft_Windows_Direct3D12_89_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12VideoProcessor" / Int64ul,
        "NodeMask" / Int32ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=90, version=0)
class Microsoft_Windows_Direct3D12_90_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12CommandList" / Int64ul,
        "SequenceNumber" / Int64ul,
        "type" / Int32ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=91, version=1)
class Microsoft_Windows_Direct3D12_91_1(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12Resource" / Int64ul,
        "hUMResource" / Int64ul,
        "Dimension" / Int32ul,
        "Width" / Int64ul,
        "Height" / Int32ul,
        "Depth" / Int32ul,
        "MipLevels" / Int32ul,
        "ArraySize" / Int32ul,
        "PlaneCount" / Int32ul,
        "Format" / Int32ul,
        "SampleCount" / Int32ul,
        "SampleQuality" / Int32ul,
        "Layout" / Int32ul,
        "Flags" / Int32ul,
        "HeapType" / Int32ul,
        "pHeap" / Int64ul,
        "ImmutableHeapOffset" / Int64ul,
        "PlacedAlignment" / Int64ul,
        "PlacedSize" / Int64ul,
        "NumTilesForResource" / Int32ul,
        "NumPackedMips" / Int32ul,
        "NumTilesForPackedMips" / Int32ul,
        "pImmutableBuffer" / Int64ul,
        "ImmutableBufferOffset" / Int64ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=92, version=1)
class Microsoft_Windows_Direct3D12_92_1(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12Resource" / Int64ul,
        "hUMResource" / Int64ul,
        "Dimension" / Int32ul,
        "Width" / Int64ul,
        "Height" / Int32ul,
        "Depth" / Int32ul,
        "MipLevels" / Int32ul,
        "ArraySize" / Int32ul,
        "PlaneCount" / Int32ul,
        "Format" / Int32ul,
        "SampleCount" / Int32ul,
        "SampleQuality" / Int32ul,
        "Layout" / Int32ul,
        "Flags" / Int32ul,
        "HeapType" / Int32ul,
        "pHeap" / Int64ul,
        "ImmutableHeapOffset" / Int64ul,
        "PlacedAlignment" / Int64ul,
        "PlacedSize" / Int64ul,
        "NumTilesForResource" / Int32ul,
        "NumPackedMips" / Int32ul,
        "NumTilesForPackedMips" / Int32ul,
        "pImmutableBuffer" / Int64ul,
        "ImmutableBufferOffset" / Int64ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=93, version=1)
class Microsoft_Windows_Direct3D12_93_1(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12Resource" / Int64ul,
        "hUMResource" / Int64ul,
        "Dimension" / Int32ul,
        "Width" / Int64ul,
        "Height" / Int32ul,
        "Depth" / Int32ul,
        "MipLevels" / Int32ul,
        "ArraySize" / Int32ul,
        "PlaneCount" / Int32ul,
        "Format" / Int32ul,
        "SampleCount" / Int32ul,
        "SampleQuality" / Int32ul,
        "Layout" / Int32ul,
        "Flags" / Int32ul,
        "HeapType" / Int32ul,
        "pHeap" / Int64ul,
        "ImmutableHeapOffset" / Int64ul,
        "PlacedAlignment" / Int64ul,
        "PlacedSize" / Int64ul,
        "NumTilesForResource" / Int32ul,
        "NumPackedMips" / Int32ul,
        "NumTilesForPackedMips" / Int32ul,
        "pImmutableBuffer" / Int64ul,
        "ImmutableBufferOffset" / Int64ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=94, version=1)
class Microsoft_Windows_Direct3D12_94_1(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pObject" / Int64ul,
        "NumVirtualAddressInfos" / Int32ul,
        "pVirtualAddressInfos" / Int16ul,
        "NumKMTInfos" / Int32ul,
        "pKMTInfos" / Int64sl
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=95, version=0)
class Microsoft_Windows_Direct3D12_95_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12CommandAllocator" / Int64ul,
        "pID3D12CommandList" / Int64ul,
        "m_hr" / Int32sl
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=96, version=0)
class Microsoft_Windows_Direct3D12_96_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12VideoDecoderHeap" / Int64ul,
        "NodeMask" / Int32ul,
        "DecodeProfile" / Guid,
        "BitstreamEncryption" / Int32ul,
        "InterlaceFormat" / Int32ul,
        "DecodeWidth" / Int32ul,
        "DecodeHeight" / Int32ul,
        "MaxDecodePictureBufferCount" / Int32ul,
        "FrameRate" / Float32l,
        "BitRate" / Int32ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=97, version=0)
class Microsoft_Windows_Direct3D12_97_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12VideoDecoderHeap" / Int64ul,
        "NodeMask" / Int32ul,
        "DecodeProfile" / Guid,
        "BitstreamEncryption" / Int32ul,
        "InterlaceFormat" / Int32ul,
        "DecodeWidth" / Int32ul,
        "DecodeHeight" / Int32ul,
        "MaxDecodePictureBufferCount" / Int32ul,
        "FrameRate" / Float32l,
        "BitRate" / Int32ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=98, version=0)
class Microsoft_Windows_Direct3D12_98_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12VideoDecoderHeap" / Int64ul,
        "NodeMask" / Int32ul,
        "DecodeProfile" / Guid,
        "BitstreamEncryption" / Int32ul,
        "InterlaceFormat" / Int32ul,
        "DecodeWidth" / Int32ul,
        "DecodeHeight" / Int32ul,
        "MaxDecodePictureBufferCount" / Int32ul,
        "FrameRate" / Float32l,
        "BitRate" / Int32ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=99, version=0)
class Microsoft_Windows_Direct3D12_99_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "NumExtendedFeatures" / Int32ul,
        "pExtendedFeatures" / Int8sl
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=100, version=0)
class Microsoft_Windows_Direct3D12_100_0(Etw):
    pattern = Struct(
        "Index" / Int32ul,
        "Code" / Int32ul,
        "ThreadId" / Int32ul,
        "Message" / CString
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=101, version=0)
class Microsoft_Windows_Direct3D12_101_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12CommandPool" / Int64ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=102, version=0)
class Microsoft_Windows_Direct3D12_102_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12CommandPool" / Int64ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=103, version=0)
class Microsoft_Windows_Direct3D12_103_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12CommandPool" / Int64ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=104, version=0)
class Microsoft_Windows_Direct3D12_104_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12CommandRecorder" / Int64ul,
        "supportFlags" / Int32ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=105, version=0)
class Microsoft_Windows_Direct3D12_105_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12CommandRecorder" / Int64ul,
        "supportFlags" / Int32ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=106, version=0)
class Microsoft_Windows_Direct3D12_106_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12CommandRecorder" / Int64ul,
        "supportFlags" / Int32ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=107, version=0)
class Microsoft_Windows_Direct3D12_107_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12CommandRecorder" / Int64ul,
        "pID3D12CommandList" / Int64ul,
        "m_hr" / Int32sl
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=108, version=0)
class Microsoft_Windows_Direct3D12_108_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12CommandRecorder" / Int64ul,
        "pID3D12CommandList" / Int64ul,
        "m_hr" / Int32sl
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=109, version=0)
class Microsoft_Windows_Direct3D12_109_0(Etw):
    pattern = Struct(
        "hKMResource" / Int32ul,
        "hUMSharedResource" / Int64ul,
        "Name" / WString
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=110, version=0)
class Microsoft_Windows_Direct3D12_110_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12StateObject" / Int64ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=111, version=0)
class Microsoft_Windows_Direct3D12_111_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12StateObject" / Int64ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=112, version=0)
class Microsoft_Windows_Direct3D12_112_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12StateObject" / Int64ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=113, version=0)
class Microsoft_Windows_Direct3D12_113_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12MetaCommand" / Int64ul,
        "CommandId" / Guid
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=114, version=0)
class Microsoft_Windows_Direct3D12_114_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12MetaCommand" / Int64ul,
        "CommandId" / Guid
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=115, version=0)
class Microsoft_Windows_Direct3D12_115_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12MetaCommand" / Int64ul,
        "CommandId" / Guid
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=116, version=0)
class Microsoft_Windows_Direct3D12_116_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12ProtectedResourceSession" / Int64ul,
        "NodeMask" / Int32ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=117, version=0)
class Microsoft_Windows_Direct3D12_117_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12ProtectedResourceSession" / Int64ul,
        "NodeMask" / Int32ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=118, version=0)
class Microsoft_Windows_Direct3D12_118_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12ProtectedResourceSession" / Int64ul,
        "NodeMask" / Int32ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=119, version=0)
class Microsoft_Windows_Direct3D12_119_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12LifetimeTracker" / Int64ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=120, version=0)
class Microsoft_Windows_Direct3D12_120_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12LifetimeTracker" / Int64ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=121, version=0)
class Microsoft_Windows_Direct3D12_121_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12LifetimeTracker" / Int64ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=122, version=0)
class Microsoft_Windows_Direct3D12_122_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12SchedulingGroup" / Int64ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=123, version=0)
class Microsoft_Windows_Direct3D12_123_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12SchedulingGroup" / Int64ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=124, version=0)
class Microsoft_Windows_Direct3D12_124_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12SchedulingGroup" / Int64ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=125, version=0)
class Microsoft_Windows_Direct3D12_125_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12VideoMotionEstimator" / Int64ul,
        "NodeMask" / Int32ul,
        "InputFormat" / Int32ul,
        "BlockSize" / Int32ul,
        "Precision" / Int32ul,
        "MaxWidthInBlocks" / Int32ul,
        "MaxHeightInBlocks" / Int32ul,
        "MinWidthInBlocks" / Int32ul,
        "MinHeightInBlocks" / Int32ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=126, version=0)
class Microsoft_Windows_Direct3D12_126_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12VideoMotionEstimator" / Int64ul,
        "NodeMask" / Int32ul,
        "InputFormat" / Int32ul,
        "BlockSize" / Int32ul,
        "Precision" / Int32ul,
        "MaxWidthInBlocks" / Int32ul,
        "MaxHeightInBlocks" / Int32ul,
        "MinWidthInBlocks" / Int32ul,
        "MinHeightInBlocks" / Int32ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=127, version=0)
class Microsoft_Windows_Direct3D12_127_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12VideoMotionEstimator" / Int64ul,
        "NodeMask" / Int32ul,
        "InputFormat" / Int32ul,
        "BlockSize" / Int32ul,
        "Precision" / Int32ul,
        "MaxWidthInBlocks" / Int32ul,
        "MaxHeightInBlocks" / Int32ul,
        "MinWidthInBlocks" / Int32ul,
        "MinHeightInBlocks" / Int32ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=128, version=0)
class Microsoft_Windows_Direct3D12_128_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12VideoMotionVectorHeap" / Int64ul,
        "NodeMask" / Int32ul,
        "InputFormat" / Int32ul,
        "BlockSize" / Int32ul,
        "Precision" / Int32ul,
        "MaxWidthInBlocks" / Int32ul,
        "MaxHeightInBlocks" / Int32ul,
        "MinWidthInBlocks" / Int32ul,
        "MinHeightInBlocks" / Int32ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=129, version=0)
class Microsoft_Windows_Direct3D12_129_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12VideoMotionVectorHeap" / Int64ul,
        "NodeMask" / Int32ul,
        "InputFormat" / Int32ul,
        "BlockSize" / Int32ul,
        "Precision" / Int32ul,
        "MaxWidthInBlocks" / Int32ul,
        "MaxHeightInBlocks" / Int32ul,
        "MinWidthInBlocks" / Int32ul,
        "MinHeightInBlocks" / Int32ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=130, version=0)
class Microsoft_Windows_Direct3D12_130_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12VideoMotionVectorHeap" / Int64ul,
        "NodeMask" / Int32ul,
        "InputFormat" / Int32ul,
        "BlockSize" / Int32ul,
        "Precision" / Int32ul,
        "MaxWidthInBlocks" / Int32ul,
        "MaxHeightInBlocks" / Int32ul,
        "MinWidthInBlocks" / Int32ul,
        "MinHeightInBlocks" / Int32ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=131, version=1)
class Microsoft_Windows_Direct3D12_131_1(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12Decoder" / Int64ul,
        "CurrPic" / Int8ul,
        "NumRefPicListEntries" / Int32ul,
        "RefPicList" / Int64ul,
        "pID3D12OutputTexture2D" / Int64ul,
        "OutputSubresource" / Int32ul,
        "pReferenceTexture2D" / Int64ul,
        "ReferenceSubresource" / Int32ul,
        "NumReferences" / Int32ul,
        "ReferenceTexture2Ds" / Sid,
        "SubresourceIndicies" / Int32ul,
        "ReferenceDecoderHeaps" / Int64ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=132, version=0)
class Microsoft_Windows_Direct3D12_132_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=133, version=0)
class Microsoft_Windows_Direct3D12_133_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=134, version=0)
class Microsoft_Windows_Direct3D12_134_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=135, version=0)
class Microsoft_Windows_Direct3D12_135_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12VideoExtensionCommand" / Int64ul,
        "NodeMask" / Int32ul,
        "CommandId" / Guid
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=136, version=0)
class Microsoft_Windows_Direct3D12_136_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12VideoExtensionCommand" / Int64ul,
        "NodeMask" / Int32ul,
        "CommandId" / Guid
    )


@declare(guid=guid("5d8087dd-3a9b-4f56-90df-49196cdc4f11"), event_id=137, version=0)
class Microsoft_Windows_Direct3D12_137_0(Etw):
    pattern = Struct(
        "pID3D12Device" / Int64ul,
        "pID3D12VideoExtensionCommand" / Int64ul,
        "NodeMask" / Int32ul,
        "CommandId" / Guid
    )

