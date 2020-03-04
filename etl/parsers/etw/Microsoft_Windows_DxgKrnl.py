# -*- coding: utf-8 -*-
"""
Microsoft-Windows-DxgKrnl
GUID : 802ec45a-1e99-4b83-9920-87c98277ba9d
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1, version=0)
class Microsoft_Windows_DxgKrnl_1_0(Etw):
    pattern = Struct(
        "ProcessHandle" / Int64ul,
        "PagingLevel" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=17, version=0)
class Microsoft_Windows_DxgKrnl_17_0(Etw):
    pattern = Struct(
        "pDxgAdapter" / Int64ul,
        "VidPnTargetId" / Int32ul,
        "ScannedPhysicalAddress" / Int64ul,
        "VidPnSourceId" / Int32ul,
        "FrameNumber" / Int32ul,
        "FrameQPCTime" / Int64sl,
        "hFlipDevice" / Int64ul,
        "FlipType" / Int32ul,
        "FlipFenceId" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=18, version=0)
class Microsoft_Windows_DxgKrnl_18_0(Etw):
    pattern = Struct(
        "pDxgAdapter" / Int64ul,
        "EventId" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=19, version=0)
class Microsoft_Windows_DxgKrnl_19_0(Etw):
    pattern = Struct(
        "pDxgAdapter" / Int64ul,
        "EventId" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=20, version=0)
class Microsoft_Windows_DxgKrnl_20_0(Etw):
    pattern = Struct(
        "hContext" / Int64ul,
        "Status" / Int32ul,
        "Line" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=21, version=0)
class Microsoft_Windows_DxgKrnl_21_0(Etw):
    pattern = Struct(
        "hContext" / Int64ul,
        "PublicPriority" / Int32ul,
        "SchedulingPriority" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=22, version=0)
class Microsoft_Windows_DxgKrnl_22_0(Etw):
    pattern = Struct(
        "hContext" / Int64ul,
        "AttemptResult" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=23, version=0)
class Microsoft_Windows_DxgKrnl_23_0(Etw):
    pattern = Struct(
        "pDxgAdapter" / Int64ul,
        "hContext" / Int64ul,
        "NodeOrdinal" / Int32ul,
        "ReadyContextPriorityMapBits" / Int32ul,
        "ReadyNodeSwMapBits" / Int64ul,
        "ReadyNodeHwMapBits" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=24, version=0)
class Microsoft_Windows_DxgKrnl_24_0(Etw):
    pattern = Struct(
        "pDeviceObject" / Int64ul,
        "pDxgAdapter" / Int64ul,
        "NbVidPnSources" / Int32ul,
        "HighestAcceptableAddress" / Int64ul,
        "MaxSlotId" / Int32ul,
        "ApertureSegmentCommitLimit" / Int64ul,
        "MaxPointerWidth" / Int32ul,
        "MaxPointerHeight" / Int32ul,
        "InterruptMessageNumber" / Int32ul,
        "NumberOfSwizzlingRanges" / Int32ul,
        "MaxOverlays" / Int32ul,
        "MaxQueuedFlipOnVSync" / Int32ul,
        "PointerCaps" / Int32ul,
        "GammaRampCaps" / Int32ul,
        "PresentationCaps" / Int32ul,
        "AlignmentShift" / Int8ul,
        "MaxTextureWidthShift" / Int8ul,
        "MaxTextureHeightShift" / Int8ul,
        "Reserved" / Int8ul,
        "FlipCaps" / Int32ul,
        "SchedulingCaps" / Int32ul,
        "ReservedMemoryManagementCaps" / Int32ul,
        "PagingNode" / Int32ul,
        "NbAsymetricProcessingNodes" / Int32ul,
        "ReservedTopology" / Int32ul,
        "NumPowerComponents" / Int32ul,
        "AdapterType" / Int32ul,
        "pMiniportContext" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=25, version=0)
class Microsoft_Windows_DxgKrnl_25_0(Etw):
    pattern = Struct(
        "pDeviceObject" / Int64ul,
        "pDxgAdapter" / Int64ul,
        "NbVidPnSources" / Int32ul,
        "HighestAcceptableAddress" / Int64ul,
        "MaxSlotId" / Int32ul,
        "ApertureSegmentCommitLimit" / Int64ul,
        "MaxPointerWidth" / Int32ul,
        "MaxPointerHeight" / Int32ul,
        "InterruptMessageNumber" / Int32ul,
        "NumberOfSwizzlingRanges" / Int32ul,
        "MaxOverlays" / Int32ul,
        "MaxQueuedFlipOnVSync" / Int32ul,
        "PointerCaps" / Int32ul,
        "GammaRampCaps" / Int32ul,
        "PresentationCaps" / Int32ul,
        "AlignmentShift" / Int8ul,
        "MaxTextureWidthShift" / Int8ul,
        "MaxTextureHeightShift" / Int8ul,
        "Reserved" / Int8ul,
        "FlipCaps" / Int32ul,
        "SchedulingCaps" / Int32ul,
        "ReservedMemoryManagementCaps" / Int32ul,
        "PagingNode" / Int32ul,
        "NbAsymetricProcessingNodes" / Int32ul,
        "ReservedTopology" / Int32ul,
        "NumPowerComponents" / Int32ul,
        "AdapterType" / Int32ul,
        "pMiniportContext" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=26, version=0)
class Microsoft_Windows_DxgKrnl_26_0(Etw):
    pattern = Struct(
        "pDeviceObject" / Int64ul,
        "pDxgAdapter" / Int64ul,
        "NbVidPnSources" / Int32ul,
        "HighestAcceptableAddress" / Int64ul,
        "MaxSlotId" / Int32ul,
        "ApertureSegmentCommitLimit" / Int64ul,
        "MaxPointerWidth" / Int32ul,
        "MaxPointerHeight" / Int32ul,
        "InterruptMessageNumber" / Int32ul,
        "NumberOfSwizzlingRanges" / Int32ul,
        "MaxOverlays" / Int32ul,
        "MaxQueuedFlipOnVSync" / Int32ul,
        "PointerCaps" / Int32ul,
        "GammaRampCaps" / Int32ul,
        "PresentationCaps" / Int32ul,
        "AlignmentShift" / Int8ul,
        "MaxTextureWidthShift" / Int8ul,
        "MaxTextureHeightShift" / Int8ul,
        "Reserved" / Int8ul,
        "FlipCaps" / Int32ul,
        "SchedulingCaps" / Int32ul,
        "ReservedMemoryManagementCaps" / Int32ul,
        "PagingNode" / Int32ul,
        "NbAsymetricProcessingNodes" / Int32ul,
        "ReservedTopology" / Int32ul,
        "NumPowerComponents" / Int32ul,
        "AdapterType" / Int32ul,
        "pMiniportContext" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=27, version=1)
class Microsoft_Windows_DxgKrnl_27_1(Etw):
    pattern = Struct(
        "hProcessId" / Int64ul,
        "pDxgAdapter" / Int64ul,
        "ClientType" / Int32ul,
        "hDevice" / Int64ul,
        "RequestVSync" / Int8ul,
        "DisableGpuTimeout" / Int8ul,
        "hThunkHandle" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=28, version=1)
class Microsoft_Windows_DxgKrnl_28_1(Etw):
    pattern = Struct(
        "hProcessId" / Int64ul,
        "pDxgAdapter" / Int64ul,
        "ClientType" / Int32ul,
        "hDevice" / Int64ul,
        "RequestVSync" / Int8ul,
        "DisableGpuTimeout" / Int8ul,
        "hThunkHandle" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=29, version=1)
class Microsoft_Windows_DxgKrnl_29_1(Etw):
    pattern = Struct(
        "hProcessId" / Int64ul,
        "pDxgAdapter" / Int64ul,
        "ClientType" / Int32ul,
        "hDevice" / Int64ul,
        "RequestVSync" / Int8ul,
        "DisableGpuTimeout" / Int8ul,
        "hThunkHandle" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=30, version=0)
class Microsoft_Windows_DxgKrnl_30_0(Etw):
    pattern = Struct(
        "hDevice" / Int64ul,
        "NodeOrdinal" / Int32ul,
        "EngineAffinity" / Int32ul,
        "DmaBufferSize" / Int32ul,
        "DmaBufferSegmentSet" / Int32ul,
        "DmaBufferPrivateDataSize" / Int32ul,
        "AllocationListSize" / Int32ul,
        "PatchLocationListSize" / Int32ul,
        "Flags" / Int32ul,
        "hContext" / Int64ul,
        "ContextHandle" / Int64ul,
        "ParentDxgContext" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=31, version=0)
class Microsoft_Windows_DxgKrnl_31_0(Etw):
    pattern = Struct(
        "hDevice" / Int64ul,
        "NodeOrdinal" / Int32ul,
        "EngineAffinity" / Int32ul,
        "DmaBufferSize" / Int32ul,
        "DmaBufferSegmentSet" / Int32ul,
        "DmaBufferPrivateDataSize" / Int32ul,
        "AllocationListSize" / Int32ul,
        "PatchLocationListSize" / Int32ul,
        "Flags" / Int32ul,
        "hContext" / Int64ul,
        "ContextHandle" / Int64ul,
        "ParentDxgContext" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=32, version=0)
class Microsoft_Windows_DxgKrnl_32_0(Etw):
    pattern = Struct(
        "hDevice" / Int64ul,
        "NodeOrdinal" / Int32ul,
        "EngineAffinity" / Int32ul,
        "DmaBufferSize" / Int32ul,
        "DmaBufferSegmentSet" / Int32ul,
        "DmaBufferPrivateDataSize" / Int32ul,
        "AllocationListSize" / Int32ul,
        "PatchLocationListSize" / Int32ul,
        "Flags" / Int32ul,
        "hContext" / Int64ul,
        "ContextHandle" / Int64ul,
        "ParentDxgContext" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=33, version=3)
class Microsoft_Windows_DxgKrnl_33_3(Etw):
    pattern = Struct(
        "hProcessId" / Int64ul,
        "hDevice" / Int64ul,
        "pDxgAdapter" / Int64ul,
        "Flags" / Int32ul,
        "allocSize" / Int64ul,
        "ulAlignment" / Int32ul,
        "dwReadSegment" / Int32ul,
        "dwWriteSegment" / Int32ul,
        "PreferredSegment" / Int32ul,
        "HintedBank" / Int32ul,
        "dwEvictionSegment" / Int32ul,
        "Priority" / Int32ul,
        "hVidMmGlobalAlloc" / Int64ul,
        "hDxgGlobalAlloc" / Int64ul,
        "hDxgSharedResource" / Int64ul,
        "UsageVersion" / Int32ul,
        "UsageFlags" / Int32ul,
        "Format" / Int32ul,
        "SwizzledFormat" / Int32ul,
        "ByteOffset" / Int32ul,
        "Width" / Int32ul,
        "Height" / Int32ul,
        "Pitch" / Int32ul,
        "Depth" / Int32ul,
        "SlicePitch" / Int32ul,
        "BackingStoreWasPinned" / Int8ul,
        "pSectionObject" / Int64ul,
        "PhysicalAdapterIndex" / Int16ul,
        "PageTableOrDirectory" / Int8ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=34, version=3)
class Microsoft_Windows_DxgKrnl_34_3(Etw):
    pattern = Struct(
        "hProcessId" / Int64ul,
        "hDevice" / Int64ul,
        "pDxgAdapter" / Int64ul,
        "Flags" / Int32ul,
        "allocSize" / Int64ul,
        "ulAlignment" / Int32ul,
        "dwReadSegment" / Int32ul,
        "dwWriteSegment" / Int32ul,
        "PreferredSegment" / Int32ul,
        "HintedBank" / Int32ul,
        "dwEvictionSegment" / Int32ul,
        "Priority" / Int32ul,
        "hVidMmGlobalAlloc" / Int64ul,
        "hDxgGlobalAlloc" / Int64ul,
        "hDxgSharedResource" / Int64ul,
        "UsageVersion" / Int32ul,
        "UsageFlags" / Int32ul,
        "Format" / Int32ul,
        "SwizzledFormat" / Int32ul,
        "ByteOffset" / Int32ul,
        "Width" / Int32ul,
        "Height" / Int32ul,
        "Pitch" / Int32ul,
        "Depth" / Int32ul,
        "SlicePitch" / Int32ul,
        "BackingStoreWasPinned" / Int8ul,
        "pSectionObject" / Int64ul,
        "PhysicalAdapterIndex" / Int16ul,
        "PageTableOrDirectory" / Int8ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=35, version=3)
class Microsoft_Windows_DxgKrnl_35_3(Etw):
    pattern = Struct(
        "hProcessId" / Int64ul,
        "hDevice" / Int64ul,
        "pDxgAdapter" / Int64ul,
        "Flags" / Int32ul,
        "allocSize" / Int64ul,
        "ulAlignment" / Int32ul,
        "dwReadSegment" / Int32ul,
        "dwWriteSegment" / Int32ul,
        "PreferredSegment" / Int32ul,
        "HintedBank" / Int32ul,
        "dwEvictionSegment" / Int32ul,
        "Priority" / Int32ul,
        "hVidMmGlobalAlloc" / Int64ul,
        "hDxgGlobalAlloc" / Int64ul,
        "hDxgSharedResource" / Int64ul,
        "UsageVersion" / Int32ul,
        "UsageFlags" / Int32ul,
        "Format" / Int32ul,
        "SwizzledFormat" / Int32ul,
        "ByteOffset" / Int32ul,
        "Width" / Int32ul,
        "Height" / Int32ul,
        "Pitch" / Int32ul,
        "Depth" / Int32ul,
        "SlicePitch" / Int32ul,
        "BackingStoreWasPinned" / Int8ul,
        "pSectionObject" / Int64ul,
        "PhysicalAdapterIndex" / Int16ul,
        "PageTableOrDirectory" / Int8ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=36, version=1)
class Microsoft_Windows_DxgKrnl_36_1(Etw):
    pattern = Struct(
        "hProcessId" / Int64ul,
        "hDevice" / Int64ul,
        "pDxgAdapter" / Int64ul,
        "hVidMmAlloc" / Int64ul,
        "hVidMmGlobalAlloc" / Int64ul,
        "hDxgResource" / Int64ul,
        "hDxgSharedResource" / Int64ul,
        "hThunkAllocation" / Int64ul,
        "hThunkResource" / Int64ul,
        "PrivateRuntimeResourceHandle" / Int64ul,
        "pVirtualAddress" / Int64ul,
        "hProcessAllocDetails" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=37, version=1)
class Microsoft_Windows_DxgKrnl_37_1(Etw):
    pattern = Struct(
        "hProcessId" / Int64ul,
        "hDevice" / Int64ul,
        "pDxgAdapter" / Int64ul,
        "hVidMmAlloc" / Int64ul,
        "hVidMmGlobalAlloc" / Int64ul,
        "hDxgResource" / Int64ul,
        "hDxgSharedResource" / Int64ul,
        "hThunkAllocation" / Int64ul,
        "hThunkResource" / Int64ul,
        "PrivateRuntimeResourceHandle" / Int64ul,
        "pVirtualAddress" / Int64ul,
        "hProcessAllocDetails" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=38, version=1)
class Microsoft_Windows_DxgKrnl_38_1(Etw):
    pattern = Struct(
        "hProcessId" / Int64ul,
        "hDevice" / Int64ul,
        "pDxgAdapter" / Int64ul,
        "hVidMmAlloc" / Int64ul,
        "hVidMmGlobalAlloc" / Int64ul,
        "hDxgResource" / Int64ul,
        "hDxgSharedResource" / Int64ul,
        "hThunkAllocation" / Int64ul,
        "hThunkResource" / Int64ul,
        "PrivateRuntimeResourceHandle" / Int64ul,
        "pVirtualAddress" / Int64ul,
        "hProcessAllocDetails" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=39, version=0)
class Microsoft_Windows_DxgKrnl_39_0(Etw):
    pattern = Struct(
        "hVidMmAlloc" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=40, version=0)
class Microsoft_Windows_DxgKrnl_40_0(Etw):
    pattern = Struct(
        "hVidMmAlloc" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=41, version=0)
class Microsoft_Windows_DxgKrnl_41_0(Etw):
    pattern = Struct(
        "hDevice" / Int64ul,
        "hAllocationHandle" / Int64ul,
        "dwFlags" / Int32ul,
        "uiLockStatus" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=42, version=0)
class Microsoft_Windows_DxgKrnl_42_0(Etw):
    pattern = Struct(
        "hDevice" / Int64ul,
        "hAllocationHandle" / Int64ul,
        "dwFlags" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=43, version=0)
class Microsoft_Windows_DxgKrnl_43_0(Etw):
    pattern = Struct(
        "hContext" / Int64ul,
        "pDmaBuffer" / Int64ul,
        "uiNbAllocations" / Int32ul,
        "Allocations" / Int64ul,
        "Write" / Int8ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=45, version=0)
class Microsoft_Windows_DxgKrnl_45_0(Etw):
    pattern = Struct(
        "hContext" / Int64ul,
        "pDmaBuffer" / Int64ul,
        "PatchLocationCount" / Int32ul,
        "PatchLocationAllocationIndex" / Int32ul,
        "PatchLocationSlotId" / Int32ul,
        "PatchLocationReserved" / Int32ul,
        "PatchLocationDriverId" / Int32ul,
        "PatchLocationAllocationOffset" / Int32ul,
        "PatchLocationPatchOffset" / Int32ul,
        "PatchLocationSplitOffset" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=46, version=0)
class Microsoft_Windows_DxgKrnl_46_0(Etw):
    pattern = Struct(
        "hAllocationHandle" / Int64ul,
        "Priority" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=47, version=0)
class Microsoft_Windows_DxgKrnl_47_0(Etw):
    pattern = Struct(
        "hAllocationGlobalHandle" / Int64ul,
        "Priority" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=48, version=0)
class Microsoft_Windows_DxgKrnl_48_0(Etw):
    pattern = Struct(
        "hAllocationGlobalHandle" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=49, version=0)
class Microsoft_Windows_DxgKrnl_49_0(Etw):
    pattern = Struct(
        "hAllocationGlobalHandle" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=50, version=0)
class Microsoft_Windows_DxgKrnl_50_0(Etw):
    pattern = Struct(
        "hProcessId" / Int64ul,
        "hAllocationGlobalHandle" / Int64ul,
        "pDmaBuffer" / Int64ul,
        "offset" / Int64ul,
        "size" / Int64ul,
        "uiType" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=51, version=0)
class Microsoft_Windows_DxgKrnl_51_0(Etw):
    pattern = Struct(
        "hDevice" / Int64ul,
        "hAllocationGlobalHandle" / Int64ul,
        "size" / Int64ul,
        "bTemporary" / Int8ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=52, version=0)
class Microsoft_Windows_DxgKrnl_52_0(Etw):
    pattern = Struct(
        "hDevice" / Int64ul,
        "hAllocationGlobalHandle" / Int64ul,
        "size" / Int64ul,
        "bTemporary" / Int8ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=53, version=0)
class Microsoft_Windows_DxgKrnl_53_0(Etw):
    pattern = Struct(
        "pDxgAdapter" / Int64ul,
        "hDmaBuffer" / Int64ul,
        "ContinueNextBuffer" / Int8ul,
        "hAllocationGlobalHandle" / Int64ul,
        "TransferOffset" / Int32ul,
        "TransferSize" / Int64ul,
        "SourceSegmentId" / Int32ul,
        "SourceSegmentOffset" / Int64ul,
        "DestinationSegmentId" / Int32ul,
        "DestinationSegmentOffset" / Int64ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=54, version=0)
class Microsoft_Windows_DxgKrnl_54_0(Etw):
    pattern = Struct(
        "pDxgAdapter" / Int64ul,
        "hDmaBuffer" / Int64ul,
        "ContinueNextBuffer" / Int8ul,
        "hAllocationGlobalHandle" / Int64ul,
        "FillSize" / Int64ul,
        "FillPattern" / Int32ul,
        "SegmentId" / Int32ul,
        "SegmentOffset" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=55, version=0)
class Microsoft_Windows_DxgKrnl_55_0(Etw):
    pattern = Struct(
        "pDxgAdapter" / Int64ul,
        "hDmaBuffer" / Int64ul,
        "ContinueNextBuffer" / Int8ul,
        "hAllocationGlobalHandle" / Int64ul,
        "Flags" / Int32ul,
        "SegmentId" / Int32ul,
        "SegmentOffset" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=56, version=0)
class Microsoft_Windows_DxgKrnl_56_0(Etw):
    pattern = Struct(
        "pDxgAdapter" / Int64ul,
        "hDmaBuffer" / Int64ul,
        "ContinueNextBuffer" / Int8ul,
        "SegmentId" / Int32ul,
        "SegmentOffset" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=57, version=0)
class Microsoft_Windows_DxgKrnl_57_0(Etw):
    pattern = Struct(
        "pDxgAdapter" / Int64ul,
        "hDmaBuffer" / Int64ul,
        "ContinueNextBuffer" / Int8ul,
        "SegmentId" / Int32ul,
        "SegmentOffset" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=58, version=0)
class Microsoft_Windows_DxgKrnl_58_0(Etw):
    pattern = Struct(
        "pDxgAdapter" / Int64ul,
        "hDmaBuffer" / Int64ul,
        "ContinueNextBuffer" / Int8ul,
        "hAllocationGlobalHandle" / Int64ul,
        "SegmentId" / Int32ul,
        "OffsetInPages" / Int64ul,
        "NumberOfPages" / Int64ul,
        "Flags" / Int32ul,
        "EvictionResource" / Int8ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=59, version=0)
class Microsoft_Windows_DxgKrnl_59_0(Etw):
    pattern = Struct(
        "pDxgAdapter" / Int64ul,
        "hDmaBuffer" / Int64ul,
        "ContinueNextBuffer" / Int8ul,
        "hAllocationGlobalHandle" / Int64ul,
        "SegmentId" / Int32ul,
        "OffsetInPages" / Int64ul,
        "NumberOfPages" / Int64ul,
        "EvictionResource" / Int8ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=60, version=0)
class Microsoft_Windows_DxgKrnl_60_0(Etw):
    pattern = Struct(
        "pDxgAdapter" / Int64ul,
        "hDmaBuffer" / Int64ul,
        "ContinueNextBuffer" / Int8ul,
        "hAllocationGlobalHandle" / Int64ul,
        "TransferOffset" / Int32ul,
        "TransferSize" / Int64ul,
        "SourceSegmentId" / Int32ul,
        "SourceSegmentOffset" / Int64ul,
        "DestinationSegmentId" / Int32ul,
        "DestinationSegmentOffset" / Int64ul,
        "Flags" / Int32ul,
        "SwizzlingRangeId" / Int32ul,
        "SwizzlingRangeData" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=61, version=0)
class Microsoft_Windows_DxgKrnl_61_0(Etw):
    pattern = Struct(
        "hContext" / Int64ul,
        "pDmaBuffer" / Int64ul,
        "uiAllocationListLength" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=62, version=0)
class Microsoft_Windows_DxgKrnl_62_0(Etw):
    pattern = Struct(
        "uiPass" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=63, version=0)
class Microsoft_Windows_DxgKrnl_63_0(Etw):
    pattern = Struct(
        "uiStatus" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=64, version=0)
class Microsoft_Windows_DxgKrnl_64_0(Etw):
    pattern = Struct(
        "hAllocationGlobalHandle" / Int64ul,
        "hAllocationHandle" / Int64ul,
        "Count" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=65, version=0)
class Microsoft_Windows_DxgKrnl_65_0(Etw):
    pattern = Struct(
        "hAllocationGlobalHandle" / Int64ul,
        "hAllocationHandle" / Int64ul,
        "Count" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=66, version=0)
class Microsoft_Windows_DxgKrnl_66_0(Etw):
    pattern = Struct(
        "SegmentId" / Int32ul,
        "hAllocationGlobalHandle" / Int64ul,
        "ProcessCommittedState" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=67, version=0)
class Microsoft_Windows_DxgKrnl_67_0(Etw):
    pattern = Struct(
        "SegmentId" / Int32ul,
        "hAllocationGlobalHandle" / Int64ul,
        "MinAddress" / Int64ul,
        "MaxAddress" / Int64ul,
        "NoEvict" / Int8ul,
        "TrimmingPriorityLimit" / Int32ul,
        "Restriction" / Int32ul,
        "ProcessCommittedState" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=68, version=0)
class Microsoft_Windows_DxgKrnl_68_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=69, version=0)
class Microsoft_Windows_DxgKrnl_69_0(Etw):
    pattern = Struct(
        "hAllocationGlobalHandle" / Int64ul,
        "PlacementRestriction" / Int32ul,
        "SegmentGroup" / Int32ul,
        "StartIndex" / Int32ul,
        "EndIndex" / Int32ul,
        "TrimmingPriorityLimit" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=70, version=0)
class Microsoft_Windows_DxgKrnl_70_0(Etw):
    pattern = Struct(
        "hAllocationGlobalHandle" / Int64ul,
        "Status" / Int32ul,
        "SegmentId" / Int32ul,
        "SegmentOffset" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=71, version=0)
class Microsoft_Windows_DxgKrnl_71_0(Etw):
    pattern = Struct(
        "hAllocationHandle" / Int64ul,
        "Reason" / Int32ul,
        "Write" / Int8ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=72, version=0)
class Microsoft_Windows_DxgKrnl_72_0(Etw):
    pattern = Struct(
        "hAllocationHandle" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=73, version=0)
class Microsoft_Windows_DxgKrnl_73_0(Etw):
    pattern = Struct(
        "hAllocationHandle" / Int64ul,
        "uiSegmentId" / Int32ul,
        "uliOffset" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=74, version=0)
class Microsoft_Windows_DxgKrnl_74_0(Etw):
    pattern = Struct(
        "hGlobalAllocationHandle" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=75, version=0)
class Microsoft_Windows_DxgKrnl_75_0(Etw):
    pattern = Struct(
        "hGlobalAllocationHandle" / Int64ul,
        "cReads" / Int32ul,
        "cPages" / Int32ul,
        "Succeeded" / Int8ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=76, version=0)
class Microsoft_Windows_DxgKrnl_76_0(Etw):
    pattern = Struct(
        "hContext" / Int64ul,
        "pDxgAdapter" / Int64ul,
        "pDmaBuffer" / Int64ul,
        "DmaSize" / Int64ul,
        "AllocationListSize" / Int64ul,
        "PatchLocationListSize" / Int64ul,
        "hAllocationGlobalHandle" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=77, version=0)
class Microsoft_Windows_DxgKrnl_77_0(Etw):
    pattern = Struct(
        "hContext" / Int64ul,
        "pDxgAdapter" / Int64ul,
        "pDmaBuffer" / Int64ul,
        "DmaSize" / Int64ul,
        "AllocationListSize" / Int64ul,
        "PatchLocationListSize" / Int64ul,
        "hAllocationGlobalHandle" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=78, version=1)
class Microsoft_Windows_DxgKrnl_78_1(Etw):
    pattern = Struct(
        "ulSegmentId" / Int32ul,
        "pDxgAdapter" / Int64ul,
        "BaseAddress" / Int64ul,
        "CpuTranslatedAddress" / Int64ul,
        "Size" / Int64ul,
        "NbOfBanks" / Int32ul,
        "Flags" / Int32ul,
        "CommitLimit" / Int64ul,
        "SystemMemoryEndAddress" / Int64ul,
        "MemorySegmentGroup" / Int8ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=80, version=0)
class Microsoft_Windows_DxgKrnl_80_0(Etw):
    pattern = Struct(
        "hProcessId" / Int64ul,
        "hDevice" / Int64ul,
        "hAllocationHandle" / Int64ul,
        "Pinned" / Int8ul,
        "EvictionResource" / Int8ul,
        "Size" / Int64ul,
        "ulSegmentId" / Int32ul,
        "SegmentOffset" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=81, version=0)
class Microsoft_Windows_DxgKrnl_81_0(Etw):
    pattern = Struct(
        "hProcessId" / Int64ul,
        "pDxgAdapter" / Int64ul,
        "AllocationPriorityClass" / Int32ul,
        "Policy" / Int32ul,
        "Value" / Int64ul,
        "ulHysteresisCount" / Int32ul,
        "ulHysteresisNext" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=82, version=0)
class Microsoft_Windows_DxgKrnl_82_0(Etw):
    pattern = Struct(
        "Device" / Int64ul,
        "Policy" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=83, version=0)
class Microsoft_Windows_DxgKrnl_83_0(Etw):
    pattern = Struct(
        "UseDefault" / Int8ul,
        "MinimumWorkingSetPercentile" / Int32ul,
        "MaximumWorkingSetPercentile" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=84, version=0)
class Microsoft_Windows_DxgKrnl_84_0(Etw):
    pattern = Struct(
        "hAdapter" / Int64ul,
        "hSyncObject" / Int64ul,
        "Reason" / Int32ul,
        "Flags" / Int32ul,
        "SharedHandle" / Int64ul,
        "InitialState" / Int8ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=85, version=0)
class Microsoft_Windows_DxgKrnl_85_0(Etw):
    pattern = Struct(
        "hAdapter" / Int64ul,
        "hSyncObject" / Int64ul,
        "Reason" / Int32ul,
        "Flags" / Int32ul,
        "SharedHandle" / Int64ul,
        "InitialState" / Int8ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=86, version=0)
class Microsoft_Windows_DxgKrnl_86_0(Etw):
    pattern = Struct(
        "hAdapter" / Int64ul,
        "hSyncObject" / Int64ul,
        "Reason" / Int32ul,
        "Flags" / Int32ul,
        "SharedHandle" / Int64ul,
        "InitialState" / Int8ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=87, version=0)
class Microsoft_Windows_DxgKrnl_87_0(Etw):
    pattern = Struct(
        "hAdapter" / Int64ul,
        "hSyncObject" / Int64ul,
        "Reason" / Int32ul,
        "Flags" / Int32ul,
        "SharedHandle" / Int64ul,
        "InitialState" / Int8ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=88, version=0)
class Microsoft_Windows_DxgKrnl_88_0(Etw):
    pattern = Struct(
        "hAdapter" / Int64ul,
        "hSyncObject" / Int64ul,
        "Reason" / Int32ul,
        "Flags" / Int32ul,
        "SharedHandle" / Int64ul,
        "MaxCount" / Int32ul,
        "InitialCount" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=89, version=0)
class Microsoft_Windows_DxgKrnl_89_0(Etw):
    pattern = Struct(
        "hAdapter" / Int64ul,
        "hSyncObject" / Int64ul,
        "Reason" / Int32ul,
        "Flags" / Int32ul,
        "SharedHandle" / Int64ul,
        "MaxCount" / Int32ul,
        "InitialCount" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=90, version=0)
class Microsoft_Windows_DxgKrnl_90_0(Etw):
    pattern = Struct(
        "hAdapter" / Int64ul,
        "hSyncObject" / Int64ul,
        "Reason" / Int32ul,
        "Flags" / Int32ul,
        "SharedHandle" / Int64ul,
        "MaxCount" / Int32ul,
        "InitialCount" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=91, version=0)
class Microsoft_Windows_DxgKrnl_91_0(Etw):
    pattern = Struct(
        "hAdapter" / Int64ul,
        "hSyncObject" / Int64ul,
        "Reason" / Int32ul,
        "Flags" / Int32ul,
        "SharedHandle" / Int64ul,
        "MaxCount" / Int32ul,
        "InitialCount" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=92, version=0)
class Microsoft_Windows_DxgKrnl_92_0(Etw):
    pattern = Struct(
        "hAdapter" / Int64ul,
        "hSyncObject" / Int64ul,
        "Reason" / Int32ul,
        "Flags" / Int32ul,
        "SharedHandle" / Int64ul,
        "InitialValue" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=93, version=0)
class Microsoft_Windows_DxgKrnl_93_0(Etw):
    pattern = Struct(
        "hAdapter" / Int64ul,
        "hSyncObject" / Int64ul,
        "Reason" / Int32ul,
        "Flags" / Int32ul,
        "SharedHandle" / Int64ul,
        "InitialValue" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=94, version=0)
class Microsoft_Windows_DxgKrnl_94_0(Etw):
    pattern = Struct(
        "hAdapter" / Int64ul,
        "hSyncObject" / Int64ul,
        "Reason" / Int32ul,
        "Flags" / Int32ul,
        "SharedHandle" / Int64ul,
        "InitialValue" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=95, version=0)
class Microsoft_Windows_DxgKrnl_95_0(Etw):
    pattern = Struct(
        "hAdapter" / Int64ul,
        "hSyncObject" / Int64ul,
        "Reason" / Int32ul,
        "Flags" / Int32ul,
        "SharedHandle" / Int64ul,
        "InitialValue" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=96, version=0)
class Microsoft_Windows_DxgKrnl_96_0(Etw):
    pattern = Struct(
        "hAdapter" / Int64ul,
        "hSyncObject" / Int64ul,
        "Reason" / Int32ul,
        "Flags" / Int32ul,
        "SharedHandle" / Int64ul,
        "Event" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=97, version=0)
class Microsoft_Windows_DxgKrnl_97_0(Etw):
    pattern = Struct(
        "hAdapter" / Int64ul,
        "hSyncObject" / Int64ul,
        "Reason" / Int32ul,
        "Flags" / Int32ul,
        "SharedHandle" / Int64ul,
        "Event" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=98, version=0)
class Microsoft_Windows_DxgKrnl_98_0(Etw):
    pattern = Struct(
        "hAdapter" / Int64ul,
        "hSyncObject" / Int64ul,
        "Reason" / Int32ul,
        "Flags" / Int32ul,
        "SharedHandle" / Int64ul,
        "Event" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=99, version=0)
class Microsoft_Windows_DxgKrnl_99_0(Etw):
    pattern = Struct(
        "hAdapter" / Int64ul,
        "hSyncObject" / Int64ul,
        "Reason" / Int32ul,
        "Flags" / Int32ul,
        "SharedHandle" / Int64ul,
        "Event" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=100, version=0)
class Microsoft_Windows_DxgKrnl_100_0(Etw):
    pattern = Struct(
        "hContext" / Int64ul,
        "ObjectCount" / Int32ul,
        "ObjectArray" / Int64ul,
        "FenceValue" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=101, version=0)
class Microsoft_Windows_DxgKrnl_101_0(Etw):
    pattern = Struct(
        "hContext" / Int64ul,
        "ObjectCount" / Int32ul,
        "ObjectArray" / Int64ul,
        "Flags" / Int32ul,
        "FenceValue" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=102, version=0)
class Microsoft_Windows_DxgKrnl_102_0(Etw):
    pattern = Struct(
        "pDxgAdapter" / Int64ul,
        "VidPnSourceId" / Int32ul,
        "Width" / Int32ul,
        "Height" / Int32ul,
        "Format" / Int32ul,
        "RefreshRateNumerator" / Int32ul,
        "RefreshRateDenominator" / Int32ul,
        "ScanLineOrdering" / Int32ul,
        "Orientation" / Int32ul,
        "DisplayFixedOutput" / Int32ul,
        "Flags" / Int32ul,
        "NumSamples" / Int32ul,
        "NumQualityLevels" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=103, version=0)
class Microsoft_Windows_DxgKrnl_103_0(Etw):
    pattern = Struct(
        "Reason" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=104, version=0)
class Microsoft_Windows_DxgKrnl_104_0(Etw):
    pattern = Struct(
        "Event" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=105, version=0)
class Microsoft_Windows_DxgKrnl_105_0(Etw):
    pattern = Struct(
        "Function" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=106, version=0)
class Microsoft_Windows_DxgKrnl_106_0(Etw):
    pattern = Struct(
        "Function" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=107, version=0)
class Microsoft_Windows_DxgKrnl_107_0(Etw):
    pattern = Struct(
        "Function" / Int32ul,
        "Src" / Int32ul,
        "Dst" / Int32ul,
        "SrcWidth" / Int32ul,
        "SrcHeight" / Int32ul,
        "DstWidth" / Int32ul,
        "DstHeight" / Int32ul,
        "Accelerated" / Int8ul,
        "SolidColor" / Int8ul,
        "Reserved" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=108, version=0)
class Microsoft_Windows_DxgKrnl_108_0(Etw):
    pattern = Struct(
        "Function" / Int32ul,
        "Src" / Int32ul,
        "Dst" / Int32ul,
        "SrcWidth" / Int32ul,
        "SrcHeight" / Int32ul,
        "DstWidth" / Int32ul,
        "DstHeight" / Int32ul,
        "Accelerated" / Int8ul,
        "SolidColor" / Int8ul,
        "Reserved" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=109, version=0)
class Microsoft_Windows_DxgKrnl_109_0(Etw):
    pattern = Struct(
        "DxgAdapter" / Int64ul,
        "VidPnSourceId" / Int32ul,
        "X" / Int32ul,
        "Y" / Int32ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=110, version=1)
class Microsoft_Windows_DxgKrnl_110_1(Etw):
    pattern = Struct(
        "pDxgAdapter" / Int64ul,
        "ConfigSpaceSize" / Int32ul,
        "ConfigSpace" / Int8ul,
        "ChainUid" / Int32ul,
        "NumberOfLinksInChain" / Int32ul,
        "LeadLink" / Int8ul,
        "BusType" / Int32ul,
        "VendorID" / Int32ul,
        "DeviceID" / Int32ul,
        "SubVendorID" / Int32ul,
        "SubSystemID" / Int32ul,
        "RevisionID" / Int32ul,
        "AdapterLuid" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=111, version=0)
class Microsoft_Windows_DxgKrnl_111_0(Etw):
    pattern = Struct(
        "pDxgAdapter" / Int64ul,
        "VidPnSourceIdNotToInvalidate" / Int32ul,
        "ClientType" / Int8ul,
        "VidPnChange" / Int8ul,
        "ReclaimClonedTarget" / Int8ul,
        "CleanupAfterFailedCommitVidPn" / Int8ul,
        "ForceAllActiveVidPnModeListInvalidation" / Int8ul,
        "ModeChangeRequestId" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=112, version=0)
class Microsoft_Windows_DxgKrnl_112_0(Etw):
    pattern = Struct(
        "pDxgAdapter" / Int64ul,
        "VidPnSourceId" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=113, version=0)
class Microsoft_Windows_DxgKrnl_113_0(Etw):
    pattern = Struct(
        "hContext" / Int64ul,
        "RunningTime" / Int64sl,
        "RemainingQuantum" / Int64sl,
        "RemainingYieldBudget" / Int64ul,
        "QuantumStatus" / Int32ul,
        "Reason" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=115, version=0)
class Microsoft_Windows_DxgKrnl_115_0(Etw):
    pattern = Struct(
        "pDxgAdapter" / Int64ul,
        "VidPnSourceId" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=116, version=0)
class Microsoft_Windows_DxgKrnl_116_0(Etw):
    pattern = Struct(
        "pDxgAdapter" / Int64ul,
        "VidPnSourceId" / Int32ul,
        "FlipSubmitSequence" / Int32ul,
        "FlipToDriverAllocation" / Int64ul,
        "FlipToPhysicalAddress" / Int64ul,
        "FlipToSegmentId" / Int32ul,
        "FlipPresentId" / Int32ul,
        "FlipPhysicalAdapterMask" / Int32ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=117, version=0)
class Microsoft_Windows_DxgKrnl_117_0(Etw):
    pattern = Struct(
        "hProcessId" / Int64ul,
        "pDxgAdapter" / Int64ul,
        "ulSegmentId" / Int32ul,
        "Policy" / Int32ul,
        "ullValue" / Int64ul,
        "ulHysteresisCount" / Int32ul,
        "ulHysteresisNext" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=118, version=0)
class Microsoft_Windows_DxgKrnl_118_0(Etw):
    pattern = Struct(
        "DriverObject" / Int64ul,
        "PhysicalDeviceObject" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=119, version=0)
class Microsoft_Windows_DxgKrnl_119_0(Etw):
    pattern = Struct(
        "DriverObject" / Int64ul,
        "PhysicalDeviceObject" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=120, version=0)
class Microsoft_Windows_DxgKrnl_120_0(Etw):
    pattern = Struct(
        "DriverObject" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=121, version=0)
class Microsoft_Windows_DxgKrnl_121_0(Etw):
    pattern = Struct(
        "DriverObject" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=122, version=0)
class Microsoft_Windows_DxgKrnl_122_0(Etw):
    pattern = Struct(
        "DeviceObject" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=123, version=0)
class Microsoft_Windows_DxgKrnl_123_0(Etw):
    pattern = Struct(
        "DeviceObject" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=124, version=0)
class Microsoft_Windows_DxgKrnl_124_0(Etw):
    pattern = Struct(
        "DeviceObject" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=125, version=0)
class Microsoft_Windows_DxgKrnl_125_0(Etw):
    pattern = Struct(
        "DeviceObject" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=126, version=0)
class Microsoft_Windows_DxgKrnl_126_0(Etw):
    pattern = Struct(
        "DeviceObject" / Int64ul,
        "StackLocationSize" / Int16ul,
        "StackLocation" / Bytes(lambda this: this.StackLocationSize),
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=127, version=0)
class Microsoft_Windows_DxgKrnl_127_0(Etw):
    pattern = Struct(
        "DeviceObject" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=128, version=0)
class Microsoft_Windows_DxgKrnl_128_0(Etw):
    pattern = Struct(
        "DeviceObject" / Int64ul,
        "StackLocationSize" / Int16ul,
        "StackLocation" / Bytes(lambda this: this.StackLocationSize),
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=129, version=0)
class Microsoft_Windows_DxgKrnl_129_0(Etw):
    pattern = Struct(
        "DeviceObject" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=130, version=0)
class Microsoft_Windows_DxgKrnl_130_0(Etw):
    pattern = Struct(
        "DeviceObject" / Int64ul,
        "StackLocationSize" / Int16ul,
        "StackLocation" / Bytes(lambda this: this.StackLocationSize),
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=131, version=0)
class Microsoft_Windows_DxgKrnl_131_0(Etw):
    pattern = Struct(
        "DeviceObject" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=132, version=0)
class Microsoft_Windows_DxgKrnl_132_0(Etw):
    pattern = Struct(
        "DeviceObject" / Int64ul,
        "StackLocationSize" / Int16ul,
        "StackLocation" / Bytes(lambda this: this.StackLocationSize),
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=133, version=0)
class Microsoft_Windows_DxgKrnl_133_0(Etw):
    pattern = Struct(
        "DeviceObject" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=134, version=0)
class Microsoft_Windows_DxgKrnl_134_0(Etw):
    pattern = Struct(
        "DeviceObject" / Int64ul,
        "StackLocationSize" / Int16ul,
        "StackLocation" / Bytes(lambda this: this.StackLocationSize),
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=135, version=0)
class Microsoft_Windows_DxgKrnl_135_0(Etw):
    pattern = Struct(
        "DeviceObject" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=136, version=0)
class Microsoft_Windows_DxgKrnl_136_0(Etw):
    pattern = Struct(
        "DeviceObject" / Int64ul,
        "MiniportContext" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=137, version=0)
class Microsoft_Windows_DxgKrnl_137_0(Etw):
    pattern = Struct(
        "DeviceObject" / Int64ul,
        "MiniportContext" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=138, version=0)
class Microsoft_Windows_DxgKrnl_138_0(Etw):
    pattern = Struct(
        "MiniportContext" / Int64ul,
        "NumVidPnSources" / Int32ul,
        "ChildCount" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=139, version=0)
class Microsoft_Windows_DxgKrnl_139_0(Etw):
    pattern = Struct(
        "MiniportContext" / Int64ul,
        "NumVidPnSources" / Int32ul,
        "ChildCount" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=140, version=0)
class Microsoft_Windows_DxgKrnl_140_0(Etw):
    pattern = Struct(
        "MiniportContext" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=141, version=0)
class Microsoft_Windows_DxgKrnl_141_0(Etw):
    pattern = Struct(
        "MiniportContext" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=142, version=0)
class Microsoft_Windows_DxgKrnl_142_0(Etw):
    pattern = Struct(
        "MiniportContext" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=143, version=0)
class Microsoft_Windows_DxgKrnl_143_0(Etw):
    pattern = Struct(
        "MiniportContext" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=144, version=0)
class Microsoft_Windows_DxgKrnl_144_0(Etw):
    pattern = Struct(
        "MiniportContext" / Int64ul,
        "VidPnSourceId" / Int32ul,
        "IoControlCode" / Int32ul,
        "StatusBlock" / Int64ul,
        "InputBufferLength" / Int32ul,
        "OutputBufferLength" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=145, version=0)
class Microsoft_Windows_DxgKrnl_145_0(Etw):
    pattern = Struct(
        "MiniportContext" / Int64ul,
        "VidPnSourceId" / Int32ul,
        "IoControlCode" / Int32ul,
        "StatusBlock" / Int64ul,
        "InputBufferLength" / Int32ul,
        "OutputBufferLength" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=146, version=0)
class Microsoft_Windows_DxgKrnl_146_0(Etw):
    pattern = Struct(
        "MiniportContext" / Int64ul,
        "ProtectedCallbackContext" / Int64ul,
        "ProtectionStatus" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=147, version=0)
class Microsoft_Windows_DxgKrnl_147_0(Etw):
    pattern = Struct(
        "MiniportContext" / Int64ul,
        "ProtectedCallbackContext" / Int64ul,
        "ProtectionStatus" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=148, version=0)
class Microsoft_Windows_DxgKrnl_148_0(Etw):
    pattern = Struct(
        "ChildRelationSize" / Int16ul,
        "ChildDescriptors" / Bytes(lambda this: this.ChildRelationSize),
        "MiniportContext" / Int64ul,
        "Status" / Int32ul,
        "ChildCount" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=149, version=0)
class Microsoft_Windows_DxgKrnl_149_0(Etw):
    pattern = Struct(
        "ChildRelationSize" / Int16ul,
        "ChildDescriptors" / Bytes(lambda this: this.ChildRelationSize),
        "MiniportContext" / Int64ul,
        "Status" / Int32ul,
        "ChildCount" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=150, version=0)
class Microsoft_Windows_DxgKrnl_150_0(Etw):
    pattern = Struct(
        "MiniportContext" / Int64ul,
        "Type" / Int32sl,
        "ChildUid" / Int32ul,
        "Connected" / Int8ul,
        "NonDestructiveOnly" / Int8ul,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=151, version=0)
class Microsoft_Windows_DxgKrnl_151_0(Etw):
    pattern = Struct(
        "MiniportContext" / Int64ul,
        "Type" / Int32sl,
        "ChildUid" / Int32ul,
        "Connected" / Int8ul,
        "NonDestructiveOnly" / Int8ul,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=152, version=0)
class Microsoft_Windows_DxgKrnl_152_0(Etw):
    pattern = Struct(
        "DeviceDescriptorOffset" / Int32ul,
        "DeviceDescriptorLength" / Int32ul,
        "DeviceDescriptor" / Bytes(lambda this: this.DeviceDescriptorLength),
        "MiniportContext" / Int64ul,
        "ChildUid" / Int32ul,
        "Status" / Int32ul,
        "DeviceDescriptorBuffer" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=153, version=0)
class Microsoft_Windows_DxgKrnl_153_0(Etw):
    pattern = Struct(
        "DeviceDescriptorOffset" / Int32ul,
        "DeviceDescriptorLength" / Int32ul,
        "DeviceDescriptor" / Bytes(lambda this: this.DeviceDescriptorLength),
        "MiniportContext" / Int64ul,
        "ChildUid" / Int32ul,
        "Status" / Int32ul,
        "DeviceDescriptorBuffer" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=154, version=0)
class Microsoft_Windows_DxgKrnl_154_0(Etw):
    pattern = Struct(
        "MiniportContext" / Int64ul,
        "DeviceUid" / Int32ul,
        "DevicePowerState" / Int32sl,
        "ActionType" / Int32sl,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=155, version=0)
class Microsoft_Windows_DxgKrnl_155_0(Etw):
    pattern = Struct(
        "MiniportContext" / Int64ul,
        "DeviceUid" / Int32ul,
        "DevicePowerState" / Int32sl,
        "ActionType" / Int32sl,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=156, version=0)
class Microsoft_Windows_DxgKrnl_156_0(Etw):
    pattern = Struct(
        "MiniportContext" / Int64ul,
        "EventType" / Int32sl,
        "Event" / Int32ul,
        "AcpiFlags" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=157, version=0)
class Microsoft_Windows_DxgKrnl_157_0(Etw):
    pattern = Struct(
        "MiniportContext" / Int64ul,
        "EventType" / Int32sl,
        "Event" / Int32ul,
        "AcpiFlags" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=160, version=0)
class Microsoft_Windows_DxgKrnl_160_0(Etw):
    pattern = Struct(
        "MiniportContext" / Int64ul,
        "InterfaceType" / Guid,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=161, version=0)
class Microsoft_Windows_DxgKrnl_161_0(Etw):
    pattern = Struct(
        "MiniportContext" / Int64ul,
        "InterfaceType" / Guid,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=162, version=0)
class Microsoft_Windows_DxgKrnl_162_0(Etw):
    pattern = Struct(
        "PhysicalDeviceObject" / Int64ul,
        "MiniportDeviceContext" / Int64ul,
        "ChainUid" / Int32ul,
        "NumberOfLinksInChain" / Int32ul,
        "LeadLink" / Int8ul,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=163, version=0)
class Microsoft_Windows_DxgKrnl_163_0(Etw):
    pattern = Struct(
        "PhysicalDeviceObject" / Int64ul,
        "MiniportDeviceContext" / Int64ul,
        "ChainUid" / Int32ul,
        "NumberOfLinksInChain" / Int32ul,
        "LeadLink" / Int8ul,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=164, version=0)
class Microsoft_Windows_DxgKrnl_164_0(Etw):
    pattern = Struct(
        "Version" / Int32ul,
        "Flags" / Int64ul,
        "Level" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=165, version=0)
class Microsoft_Windows_DxgKrnl_165_0(Etw):
    pattern = Struct(
        "EventGuid" / Guid,
        "EventType" / Int8ul,
        "BufferSize" / Int16ul,
        "Buffer" / Bytes(lambda this: this.BufferSize)
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=166, version=0)
class Microsoft_Windows_DxgKrnl_166_0(Etw):
    pattern = Struct(
        "hwnd" / Int64ul,
        "pDmaBuffer" / Int64ul,
        "PresentHistoryToken" / Int64ul,
        "hSourceAllocation" / Int64ul,
        "hDestAllocation" / Int64ul,
        "bSubmit" / Int8ul,
        "bRedirectedPresent" / Int8ul,
        "Flags" / Int32ul,
        "SourceLeft" / Int32sl,
        "SourceRight" / Int32sl,
        "SourceTop" / Int32sl,
        "SourceBottom" / Int32sl,
        "DestLeft" / Int32sl,
        "DestRight" / Int32sl,
        "DestTop" / Int32sl,
        "DestBottom" / Int32sl,
        "SubRectCount" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=167, version=0)
class Microsoft_Windows_DxgKrnl_167_0(Etw):
    pattern = Struct(
        "pDmaBuffer" / Int64ul,
        "FinalEvent" / Int8ul,
        "RectCount" / Int32ul,
        "Left" / Int32sl,
        "Right" / Int32sl,
        "Top" / Int32sl,
        "Bottom" / Int32sl
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=168, version=0)
class Microsoft_Windows_DxgKrnl_168_0(Etw):
    pattern = Struct(
        "pDmaBuffer" / Int64ul,
        "VidPnSourceId" / Int32ul,
        "FlipToAllocation" / Int64ul,
        "FlipInterval" / Int32ul,
        "FlipWithNoWait" / Int8ul,
        "MMIOFlip" / Int8ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=169, version=0)
class Microsoft_Windows_DxgKrnl_169_0(Etw):
    pattern = Struct(
        "pDmaBuffer" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=170, version=0)
class Microsoft_Windows_DxgKrnl_170_0(Etw):
    pattern = Struct(
        "pDmaBuffer" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=171, version=0)
class Microsoft_Windows_DxgKrnl_171_0(Etw):
    pattern = Struct(
        "hAdapter" / Int64ul,
        "Token" / Int64ul,
        "Model" / Int32ul,
        "TokenSize" / Int32ul,
        "TokenData" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=172, version=0)
class Microsoft_Windows_DxgKrnl_172_0(Etw):
    pattern = Struct(
        "hAdapter" / Int64ul,
        "Token" / Int64ul,
        "Model" / Int32ul,
        "TokenSize" / Int32ul,
        "TokenData" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=173, version=0)
class Microsoft_Windows_DxgKrnl_173_0(Etw):
    pattern = Struct(
        "hAdapter" / Int64ul,
        "Token" / Int64ul,
        "Model" / Int32ul,
        "TokenSize" / Int32ul,
        "TokenData" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=174, version=0)
class Microsoft_Windows_DxgKrnl_174_0(Etw):
    pattern = Struct(
        "Id" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=175, version=1)
class Microsoft_Windows_DxgKrnl_175_1(Etw):
    pattern = Struct(
        "hContext" / Int64ul,
        "hQueuePacketContext" / Int64ul,
        "PacketType" / Int32ul,
        "uliSubmissionId" / Int64ul,
        "ulQueueSubmitSequence" / Int32ul,
        "pDmaBuffer" / Int64ul,
        "QuantumStatus" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=176, version=0)
class Microsoft_Windows_DxgKrnl_176_0(Etw):
    pattern = Struct(
        "hContext" / Int64ul,
        "PacketType" / Int32ul,
        "uliCompletionId" / Int64ul,
        "ulQueueSubmitSequence" / Int32ul,
        "bPreempted" / Int8ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=177, version=1)
class Microsoft_Windows_DxgKrnl_177_1(Etw):
    pattern = Struct(
        "hContext" / Int64ul,
        "PacketType" / Int32ul,
        "uliCompletionId" / Int64ul,
        "ulQueueSubmitSequence" / Int32ul,
        "InterruptType" / Int32ul,
        "QuantumStatus" / Int32ul,
        "FaultedVirtualAddress" / Int64ul,
        "PageFaultFlags" / Int32ul,
        "FaultedProcessHandle" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=178, version=1)
class Microsoft_Windows_DxgKrnl_178_1(Etw):
    pattern = Struct(
        "hContext" / Int64ul,
        "PacketType" / Int32ul,
        "SubmitSequence" / Int32ul,
        "DmaBufferSize" / Int64ul,
        "AllocationListSize" / Int32ul,
        "PatchLocationListSize" / Int32ul,
        "bPresent" / Int8ul,
        "hDmaBuffer" / Int64ul,
        "pQueuePacket" / Int64ul,
        "ProgressFenceValue" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=179, version=0)
class Microsoft_Windows_DxgKrnl_179_0(Etw):
    pattern = Struct(
        "hContext" / Int64ul,
        "PacketType" / Int32ul,
        "SubmitSequence" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=180, version=1)
class Microsoft_Windows_DxgKrnl_180_1(Etw):
    pattern = Struct(
        "hContext" / Int64ul,
        "PacketType" / Int32ul,
        "SubmitSequence" / Int32ul,
        "bPreempted" / Int8ul,
        "bTimeouted" / Int8ul,
        "pQueuePacket" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=181, version=0)
class Microsoft_Windows_DxgKrnl_181_0(Etw):
    pattern = Struct(
        "pDxgAdapter" / Int64ul,
        "VidPnTargetId" / Int32ul,
        "ScannedPhysicalAddress" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=182, version=0)
class Microsoft_Windows_DxgKrnl_182_0(Etw):
    pattern = Struct(
        "hDevice" / Int64ul,
        "DeviceState" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=183, version=0)
class Microsoft_Windows_DxgKrnl_183_0(Etw):
    pattern = Struct(
        "hDevice" / Int64ul,
        "VidPnSourceId" / Int32ul,
        "PresentCount" / Int32ul,
        "PresentRefreshCount" / Int32ul,
        "SyncRefreshCount" / Int32ul,
        "SyncQPCTime" / Int64ul,
        "SyncGPUTime" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=184, version=1)
class Microsoft_Windows_DxgKrnl_184_1(Etw):
    pattern = Struct(
        "hContext" / Int32ul,
        "hWindow" / Int64ul,
        "VidPnSourceId" / Int32ul,
        "FlipInterval" / Int32ul,
        "Flags" / Int32ul,
        "ReturnStatus" / Int32ul,
        "hSrcAllocHandle" / Int64ul,
        "hDstAllocHandle" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=185, version=0)
class Microsoft_Windows_DxgKrnl_185_0(Etw):
    pattern = Struct(
        "hContext" / Int64ul,
        "FenceId" / Int64ul,
        "ProcessorFrequencyInMHz" / Int32ul,
        "NumberOfTimestamps" / Int32ul,
        "Timestamps" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=186, version=0)
class Microsoft_Windows_DxgKrnl_186_0(Etw):
    pattern = Struct(
        "hAllocationHandle" / Int64ul,
        "Priority" / Int8ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=187, version=0)
class Microsoft_Windows_DxgKrnl_187_0(Etw):
    pattern = Struct(
        "hAllocationHandle" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=188, version=0)
class Microsoft_Windows_DxgKrnl_188_0(Etw):
    pattern = Struct(
        "hGlobalAllocationHandle" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=189, version=0)
class Microsoft_Windows_DxgKrnl_189_0(Etw):
    pattern = Struct(
        "hGlobalAllocationHandle" / Int64ul,
        "State" / Int8ul,
        "Priority" / Int8ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=190, version=0)
class Microsoft_Windows_DxgKrnl_190_0(Etw):
    pattern = Struct(
        "hAllocationHandle" / Int64ul,
        "Priority" / Int8ul,
        "State" / Int8ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=191, version=0)
class Microsoft_Windows_DxgKrnl_191_0(Etw):
    pattern = Struct(
        "hGlobalAllocationHandle" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=192, version=0)
class Microsoft_Windows_DxgKrnl_192_0(Etw):
    pattern = Struct(
        "PacketIndex" / Int32ul,
        "WdLogIndex" / Int32ul,
        "VidPnSourceId" / Int32ul,
        "ContextIndex" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=193, version=0)
class Microsoft_Windows_DxgKrnl_193_0(Etw):
    pattern = Struct(
        "PacketIndex" / Int32ul,
        "WdLogIndex" / Int32ul,
        "VidPnSourceId" / Int32ul,
        "ContextIndex" / Int32ul,
        "DestroyReason" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=194, version=0)
class Microsoft_Windows_DxgKrnl_194_0(Etw):
    pattern = Struct(
        "PacketIndex" / Int32ul,
        "WdLogIndex" / Int32ul,
        "VidPnSourceId" / Int32ul,
        "PresentFlags" / Int32ul,
        "PresentRgnDirtyRectCount" / Int32ul,
        "PresentRgnMoveRectCount" / Int32ul,
        "DirtyRectIntCount" / Int32ul,
        "DirtyRects" / Int32sl,
        "MoveRectIntCount" / Int32ul,
        "MoveRects" / Int32sl
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=195, version=0)
class Microsoft_Windows_DxgKrnl_195_0(Etw):
    pattern = Struct(
        "PacketIndex" / Int32ul,
        "WdLogIndex" / Int32ul,
        "VidPnSourceId" / Int32ul,
        "Type" / Int32ul,
        "Width" / Int32ul,
        "Height" / Int32ul,
        "Pitch" / Int32ul,
        "HotSpotx" / Int32sl,
        "HotSpoty" / Int32sl
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=196, version=0)
class Microsoft_Windows_DxgKrnl_196_0(Etw):
    pattern = Struct(
        "PacketIndex" / Int32ul,
        "WdLogIndex" / Int32ul,
        "VidPnSourceId" / Int32ul,
        "Positionx" / Int32sl,
        "Positiony" / Int32sl,
        "Visible" / Int8ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=197, version=0)
class Microsoft_Windows_DxgKrnl_197_0(Etw):
    pattern = Struct(
        "PacketIndex" / Int32ul,
        "WdLogIndex" / Int32ul,
        "VidPnSourceId" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=198, version=0)
class Microsoft_Windows_DxgKrnl_198_0(Etw):
    pattern = Struct(
        "PacketIndex" / Int32ul,
        "WdLogIndex" / Int32ul,
        "VidPnSourceId" / Int32ul,
        "ContextIndex" / Int32ul,
        "Status" / Int32ul,
        "AcquiredMutex" / Int8ul,
        "AccumulatedFrames" / Int32ul,
        "AccumulatedFrameUpdated" / Int8ul,
        "StatusBits" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=199, version=0)
class Microsoft_Windows_DxgKrnl_199_0(Etw):
    pattern = Struct(
        "PacketIndex" / Int32ul,
        "WdLogIndex" / Int32ul,
        "VidPnSourceId" / Int32ul,
        "LastPresentTime" / Int64sl,
        "LastMouseUpdateTime" / Int64sl,
        "AccumulatedFrames" / Int32ul,
        "RectsCoalesced" / Int8ul,
        "ProtectedContentMaskedOut" / Int8ul,
        "PointerPositionPositionx" / Int32sl,
        "PointerPositionPositiony" / Int32sl,
        "PointerPositionVisible" / Int8ul,
        "TotalMetadataBufferSize" / Int32ul,
        "PointerShapeBufferSize" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=200, version=0)
class Microsoft_Windows_DxgKrnl_200_0(Etw):
    pattern = Struct(
        "PacketIndex" / Int32ul,
        "WdLogIndex" / Int32ul,
        "VidPnSourceId" / Int32ul,
        "MetaDataType" / Int32ul,
        "BufferSizeSupplied" / Int32ul,
        "BufferSizeRequired" / Int32ul,
        "Status" / Int32ul,
        "DirtyCount" / Int32ul,
        "DirtyRectIntCount" / Int32ul,
        "DirtyRects" / Int32sl
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=201, version=0)
class Microsoft_Windows_DxgKrnl_201_0(Etw):
    pattern = Struct(
        "PacketIndex" / Int32ul,
        "WdLogIndex" / Int32ul,
        "VidPnSourceId" / Int32ul,
        "MetaDataType" / Int32ul,
        "BufferSizeSupplied" / Int32ul,
        "BufferSizeRequired" / Int32ul,
        "Status" / Int32ul,
        "MoveCount" / Int32ul,
        "MoveRectIntCount" / Int32ul,
        "MoveRects" / Int32sl
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=202, version=0)
class Microsoft_Windows_DxgKrnl_202_0(Etw):
    pattern = Struct(
        "PacketIndex" / Int32ul,
        "WdLogIndex" / Int32ul,
        "VidPnSourceId" / Int32ul,
        "Type" / Int32ul,
        "Width" / Int32ul,
        "Height" / Int32ul,
        "Pitch" / Int32ul,
        "HotSpotx" / Int32sl,
        "HotSpoty" / Int32sl,
        "BufferSizeSupplied" / Int32ul,
        "BufferSizeRequired" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=203, version=0)
class Microsoft_Windows_DxgKrnl_203_0(Etw):
    pattern = Struct(
        "AdapterHandle" / Int64ul,
        "ComponentIndex" / Int32ul,
        "State" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=204, version=0)
class Microsoft_Windows_DxgKrnl_204_0(Etw):
    pattern = Struct(
        "AdapterHandle" / Int64ul,
        "ComponentIndex" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=205, version=0)
class Microsoft_Windows_DxgKrnl_205_0(Etw):
    pattern = Struct(
        "AdapterHandle" / Int64ul,
        "ComponentIndex" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=206, version=0)
class Microsoft_Windows_DxgKrnl_206_0(Etw):
    pattern = Struct(
        "AdapterHandle" / Int64ul,
        "ComponentIndex" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=207, version=0)
class Microsoft_Windows_DxgKrnl_207_0(Etw):
    pattern = Struct(
        "AdapterHandle" / Int64ul,
        "ComponentIndex" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=208, version=0)
class Microsoft_Windows_DxgKrnl_208_0(Etw):
    pattern = Struct(
        "AdapterHandle" / Int64ul,
        "ComponentIndex" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=209, version=0)
class Microsoft_Windows_DxgKrnl_209_0(Etw):
    pattern = Struct(
        "AdapterHandle" / Int64ul,
        "ComponentIndex" / Int32ul,
        "State" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=210, version=0)
class Microsoft_Windows_DxgKrnl_210_0(Etw):
    pattern = Struct(
        "MiniportDeviceContext" / Int64ul,
        "TargetId" / Int32ul,
        "Width" / Int32ul,
        "Height" / Int32ul,
        "Pitch" / Int32ul,
        "ColorFormat" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=211, version=0)
class Microsoft_Windows_DxgKrnl_211_0(Etw):
    pattern = Struct(
        "MiniportDeviceContext" / Int64ul,
        "TargetId" / Int32ul,
        "Width" / Int32ul,
        "Height" / Int32ul,
        "Pitch" / Int32ul,
        "ColorFormat" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=212, version=0)
class Microsoft_Windows_DxgKrnl_212_0(Etw):
    pattern = Struct(
        "PacketIndex" / Int32ul,
        "WdLogIndex" / Int32ul,
        "VidPnSourceId" / Int32ul,
        "StatusBits" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=214, version=1)
class Microsoft_Windows_DxgKrnl_214_1(Etw):
    pattern = Struct(
        "AdapterHandle" / Int64ul,
        "ComponentIndex" / Int32ul,
        "State" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=215, version=0)
class Microsoft_Windows_DxgKrnl_215_0(Etw):
    pattern = Struct(
        "hAdapter" / Int64ul,
        "Token" / Int64ul,
        "Model" / Int32ul,
        "TokenSize" / Int32ul,
        "TokenData" / Int64ul,
        "ScrollRectleft" / Int32ul,
        "ScrollRectright" / Int32ul,
        "ScrollRecttop" / Int32ul,
        "ScrollRectbottom" / Int32ul,
        "ScrollOffsetX" / Int32ul,
        "ScrollOffsetY" / Int32ul,
        "DirtyRectCount" / Int32ul,
        "Left" / Int32sl,
        "Right" / Int32sl,
        "Top" / Int32sl,
        "Bottom" / Int32sl,
        "SourceRectleft" / Int32ul,
        "SourceRectright" / Int32ul,
        "SourceRecttop" / Int32ul,
        "SourceRectbottom" / Int32ul,
        "DestWidth" / Int32ul,
        "DestHeight" / Int32ul,
        "TargetRectleft" / Int32ul,
        "TargetRectright" / Int32ul,
        "TargetRecttop" / Int32ul,
        "TargetRectbottom" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=216, version=0)
class Microsoft_Windows_DxgKrnl_216_0(Etw):
    pattern = Struct(
        "AdapterOrdinal" / Int32sl,
        "hProcessId" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=217, version=0)
class Microsoft_Windows_DxgKrnl_217_0(Etw):
    pattern = Struct(
        "hContext" / Int64ul,
        "hProcessId" / Int64ul,
        "PreemptionTime" / Int64ul,
        "SchedulingDelay" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=218, version=0)
class Microsoft_Windows_DxgKrnl_218_0(Etw):
    pattern = Struct(
        "MiniportDeviceContext" / Int64ul,
        "ChildUid" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=219, version=0)
class Microsoft_Windows_DxgKrnl_219_0(Etw):
    pattern = Struct(
        "MiniportDeviceContext" / Int64ul,
        "ChildUid" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=220, version=0)
class Microsoft_Windows_DxgKrnl_220_0(Etw):
    pattern = Struct(
        "AdapterHandle" / Int64ul,
        "ControlGuid" / Guid
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=221, version=0)
class Microsoft_Windows_DxgKrnl_221_0(Etw):
    pattern = Struct(
        "AdapterHandle" / Int64ul,
        "ControlGuid" / Guid
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=222, version=0)
class Microsoft_Windows_DxgKrnl_222_0(Etw):
    pattern = Struct(
        "AdapterHandle" / Int64ul,
        "ComponentIndex" / Int32ul,
        "ComponentType" / Int32ul,
        "ComponentTypeId" / Int32ul,
        "NumberOfIdleStates" / Int32ul,
        "ControlGuid" / Guid,
        "Name" / WString,
        "Flags" / Int32ul,
        "CurrentFState" / Int32ul,
        "CurrentLatencyTolerance" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=223, version=0)
class Microsoft_Windows_DxgKrnl_223_0(Etw):
    pattern = Struct(
        "AdapterHandle" / Int64ul,
        "ComponentIndex" / Int32ul,
        "FState" / Int32ul,
        "NominalPower" / Int32ul,
        "TransitionLatency" / Int64ul,
        "ResidencyRequirement" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=225, version=1)
class Microsoft_Windows_DxgKrnl_225_1(Etw):
    pattern = Struct(
        "Handle" / Int64ul,
        "Size" / Int64ul,
        "Mapping" / Int32ul,
        "ProcessId" / Int32ul,
        "IsHeapBlock" / Int8ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=226, version=1)
class Microsoft_Windows_DxgKrnl_226_1(Etw):
    pattern = Struct(
        "Handle" / Int64ul,
        "Size" / Int64ul,
        "Mapping" / Int32ul,
        "ProcessId" / Int32ul,
        "IsHeapBlock" / Int8ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=227, version=0)
class Microsoft_Windows_DxgKrnl_227_0(Etw):
    pattern = Struct(
        "hGlobalAllocationHandle" / Int64ul,
        "ulSegmentId" / Int32ul,
        "SegmentOffset" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=228, version=0)
class Microsoft_Windows_DxgKrnl_228_0(Etw):
    pattern = Struct(
        "AdapterHandle" / Int64ul,
        "ComponentIndex" / Int32ul,
        "Latency" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=229, version=0)
class Microsoft_Windows_DxgKrnl_229_0(Etw):
    pattern = Struct(
        "AdapterHandle" / Int64ul,
        "ComponentIndex" / Int32ul,
        "Residency" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=230, version=0)
class Microsoft_Windows_DxgKrnl_230_0(Etw):
    pattern = Struct(
        "ContextCount" / Int32ul,
        "hContext" / Int64ul,
        "ObjectCount" / Int32ul,
        "ObjectArray" / Int64ul,
        "Flags" / Int32ul,
        "FenceValue" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=231, version=0)
class Microsoft_Windows_DxgKrnl_231_0(Etw):
    pattern = Struct(
        "hContext" / Int64ul,
        "ObjectCount" / Int32ul,
        "ObjectArray" / Int64ul,
        "FenceValue" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=236, version=0)
class Microsoft_Windows_DxgKrnl_236_0(Etw):
    pattern = Struct(
        "AdapterHandle" / Int64ul,
        "DevicePowerState" / Int32ul,
        "Reason" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=237, version=0)
class Microsoft_Windows_DxgKrnl_237_0(Etw):
    pattern = Struct(
        "AdapterHandle" / Int64ul,
        "DevicePowerState" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=238, version=0)
class Microsoft_Windows_DxgKrnl_238_0(Etw):
    pattern = Struct(
        "QueuePacket" / Int64ul,
        "hContext" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=239, version=0)
class Microsoft_Windows_DxgKrnl_239_0(Etw):
    pattern = Struct(
        "hContext" / Int64ul,
        "OldPriority" / Int32sl,
        "NewPriority" / Int32sl
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=240, version=0)
class Microsoft_Windows_DxgKrnl_240_0(Etw):
    pattern = Struct(
        "MiniportDeviceContext" / Int64ul,
        "RemovalType" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=241, version=0)
class Microsoft_Windows_DxgKrnl_241_0(Etw):
    pattern = Struct(
        "MiniportDeviceContext" / Int64ul,
        "RemovalType" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=242, version=0)
class Microsoft_Windows_DxgKrnl_242_0(Etw):
    pattern = Struct(
        "hGlobalAllocationHandle" / Int64ul,
        "cPages" / Int32ul,
        "RemoveFromWorkingSet" / Int8ul,
        "Succeeded" / Int8ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=243, version=0)
class Microsoft_Windows_DxgKrnl_243_0(Etw):
    pattern = Struct(
        "AdapterHandle" / Int64ul,
        "ComponentIndex" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=244, version=1)
class Microsoft_Windows_DxgKrnl_244_1(Etw):
    pattern = Struct(
        "hContext" / Int64ul,
        "SubmitSequence" / Int32ul,
        "Flags" / Int32ul,
        "hSyncObject" / Int64ul,
        "FenceValue" / Int64ul,
        "pQueuePacket" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=245, version=2)
class Microsoft_Windows_DxgKrnl_245_2(Etw):
    pattern = Struct(
        "hContext" / Int64ul,
        "SubmitSequence" / Int32ul,
        "Flags" / Int32ul,
        "ObjectCount" / Int32ul,
        "ObjectArray" / Int64ul,
        "FenceValue" / Int64ul,
        "pQueuePacket" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=246, version=0)
class Microsoft_Windows_DxgKrnl_246_0(Etw):
    pattern = Struct(
        "hContext" / Int64ul,
        "RecordCount" / Int32ul,
        "RecordTime" / Int64sl
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=247, version=0)
class Microsoft_Windows_DxgKrnl_247_0(Etw):
    pattern = Struct(
        "hAdapter" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=248, version=0)
class Microsoft_Windows_DxgKrnl_248_0(Etw):
    pattern = Struct(
        "hAdapter" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=250, version=0)
class Microsoft_Windows_DxgKrnl_250_0(Etw):
    pattern = Struct(
        "pDxgAdapter" / Int64ul,
        "NodeOrdinal" / Int32ul,
        "EngineType" / Int32ul,
        "FriendlyName" / WString
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=251, version=0)
class Microsoft_Windows_DxgKrnl_251_0(Etw):
    pattern = Struct(
        "hContext" / Int32ul,
        "VidPnSourceId" / Int32ul,
        "PresentCount" / Int32ul,
        "FlipInterval" / Int32ul,
        "Flags" / Int32ul,
        "PresentPlaneCount" / Int32ul,
        "ReturnStatus" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=252, version=0)
class Microsoft_Windows_DxgKrnl_252_0(Etw):
    pattern = Struct(
        "VidPnSourceId" / Int32ul,
        "LayerIndex" / Int32ul,
        "Enabled" / Int32ul,
        "hAllocation" / Int64ul,
        "Flags" / Int32ul,
        "SrcRectleft" / Int32sl,
        "SrcRectright" / Int32sl,
        "SrcRecttop" / Int32sl,
        "SrcRectbottom" / Int32sl,
        "DstRectleft" / Int32sl,
        "DstRectright" / Int32sl,
        "DstRecttop" / Int32sl,
        "DstRectbottom" / Int32sl,
        "ClipRectleft" / Int32sl,
        "ClipRectright" / Int32sl,
        "ClipRecttop" / Int32sl,
        "ClipRectbottom" / Int32sl,
        "Rotation" / Int32ul,
        "Blend" / Int32ul,
        "NumFilters" / Int32ul,
        "ColorSpace" / Int32ul,
        "HDRMetaDataType" / Int32ul,
        "SDRWhiteLevel" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=253, version=0)
class Microsoft_Windows_DxgKrnl_253_0(Etw):
    pattern = Struct(
        "AdapterHandle" / Int64ul,
        "ComponentIndex" / Int32ul,
        "NodeIndex" / Int32ul,
        "NumberOfPStates" / Int32ul,
        "CurrentPState" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=254, version=0)
class Microsoft_Windows_DxgKrnl_254_0(Etw):
    pattern = Struct(
        "AdapterHandle" / Int64ul,
        "NodeIndex" / Int32ul,
        "PState" / Int32ul,
        "OperatingFrequency" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=255, version=0)
class Microsoft_Windows_DxgKrnl_255_0(Etw):
    pattern = Struct(
        "AdapterHandle" / Int64ul,
        "ComponentIndex" / Int32ul,
        "PreviousState" / Int32ul,
        "State" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=256, version=0)
class Microsoft_Windows_DxgKrnl_256_0(Etw):
    pattern = Struct(
        "AdapterHandle" / Int64ul,
        "ComponentIndex" / Int32ul,
        "PreviousState" / Int32ul,
        "State" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=257, version=0)
class Microsoft_Windows_DxgKrnl_257_0(Etw):
    pattern = Struct(
        "AdapterHandle" / Int64ul,
        "ComponentIndex" / Int32ul,
        "State" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=259, version=3)
class Microsoft_Windows_DxgKrnl_259_3(Etw):
    pattern = Struct(
        "pDxgAdapter" / Int64ul,
        "VidPnSourceId" / Int32ul,
        "LayerIndex" / Int32ul,
        "FlipSubmitSequence" / Int64ul,
        "FlipToDriverAllocation" / Int64ul,
        "FlipToPhysicalAddress" / Int64ul,
        "FlipToSegmentId" / Int32ul,
        "FlipPresentId" / Int32ul,
        "FlipPhysicalAdapterMask" / Int32ul,
        "SrcRectleft" / Int32sl,
        "SrcRectright" / Int32sl,
        "SrcRecttop" / Int32sl,
        "SrcRectbottom" / Int32sl,
        "DstRectleft" / Int32sl,
        "DstRectright" / Int32sl,
        "DstRecttop" / Int32sl,
        "DstRectbottom" / Int32sl,
        "ClipRectleft" / Int32sl,
        "ClipRectright" / Int32sl,
        "ClipRecttop" / Int32sl,
        "ClipRectbottom" / Int32sl,
        "ColorSpace" / Int32ul,
        "FlipEntryStatusAfterFlip" / Int32ul,
        "Enabled" / Int8ul,
        "SDRWhiteLevel" / Int32ul,
        "DirtyRectCount" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=260, version=0)
class Microsoft_Windows_DxgKrnl_260_0(Etw):
    pattern = Struct(
        "FunctionalDeviceObject" / Int64ul,
        "Engaged" / Int8ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=261, version=0)
class Microsoft_Windows_DxgKrnl_261_0(Etw):
    pattern = Struct(
        "FunctionalDeviceObject" / Int64ul,
        "Percentage" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=262, version=0)
class Microsoft_Windows_DxgKrnl_262_0(Etw):
    pattern = Struct(
        "hAdapter" / Int64ul,
        "NodeOrdinal" / Int32ul,
        "EngineOrdinal" / Int32ul,
        "GpuFrequency" / Int64ul,
        "GpuClock" / Int64ul,
        "CpuClock" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=263, version=0)
class Microsoft_Windows_DxgKrnl_263_0(Etw):
    pattern = Struct(
        "hContext" / Int64ul,
        "RenderCbSequence" / Int32ul,
        "DmaSubmissionSequence" / Int32ul,
        "Precision" / Int32ul,
        "HistoryBufferSize" / Int32ul,
        "HistoryBuffer" / Int8ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=264, version=0)
class Microsoft_Windows_DxgKrnl_264_0(Etw):
    pattern = Struct(
        "HighestPriorityLevelOfThresholdExceeded" / Int64ul,
        "HighestPriorityLevel" / Int64ul,
        "RemainingYieldBudget" / Int64ul,
        "ThresholdExceededPriorityMapBits" / Int32ul,
        "TickFrequency" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=265, version=0)
class Microsoft_Windows_DxgKrnl_265_0(Etw):
    pattern = Struct(
        "PriorityLevelToSchedule" / Int64ul,
        "ReadyContextMapBits" / Int64ul,
        "ThresholdExceededPriorityMapBits" / Int32ul,
        "bInYieldState" / Int8ul,
        "bYieldStateStartTimeInitialized" / Int8ul,
        "bYieldingDone" / Int8ul,
        "YieldStartTime" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=266, version=1)
class Microsoft_Windows_DxgKrnl_266_1(Etw):
    pattern = Struct(
        "hContext" / Int64ul,
        "SubmitSequence" / Int32ul,
        "VidPnSourceId" / Int32ul,
        "FlipToAllocation" / Int64ul,
        "FlipInterval" / Int32ul,
        "PlaneIndex" / Int32ul,
        "SwapChainIndex" / Int32ul,
        "CompositionSurfaceLuid" / Int64ul,
        "BindId" / Int64ul,
        "PresentCount" / Int32ul,
        "FlipTrueImmediate" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=267, version=1)
class Microsoft_Windows_DxgKrnl_267_1(Etw):
    pattern = Struct(
        "Entering" / Int8ul,
        "compositionSurfaceLuid" / Int64ul,
        "VidPnSourceId" / Int32ul,
        "Plane" / Int32ul,
        "ApprovedPresentDuration" / Int32ul,
        "PendingIndependentFlip" / Int8ul,
        "bindId" / Int64ul,
        "RequestedByDwm" / Int8ul,
        "confirmationCookie" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=268, version=0)
class Microsoft_Windows_DxgKrnl_268_0(Etw):
    pattern = Struct(
        "pDxgAdapter" / Int64ul,
        "ScannedPhysicalAddress" / Int64ul,
        "VidPnSourceId" / Int32ul,
        "PresentId" / Int32ul,
        "hFlipDevice" / Int64ul,
        "FlipType" / Int32ul,
        "FlipFenceId" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=269, version=0)
class Microsoft_Windows_DxgKrnl_269_0(Etw):
    pattern = Struct(
        "AdapterHandle" / Int64ul,
        "State" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=270, version=0)
class Microsoft_Windows_DxgKrnl_270_0(Etw):
    pattern = Struct(
        "AdapterHandle" / Int64ul,
        "State" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=271, version=0)
class Microsoft_Windows_DxgKrnl_271_0(Etw):
    pattern = Struct(
        "NewValue" / Int8ul,
        "Optimized" / Int8ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=272, version=0)
class Microsoft_Windows_DxgKrnl_272_0(Etw):
    pattern = Struct(
        "FunctionalDeviceObject" / Int64ul,
        "ChildUid" / Int32ul,
        "Type" / Int32ul,
        "Connected" / Int8ul,
        "MiracastMonitorType" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=273, version=1)
class Microsoft_Windows_DxgKrnl_273_1(Etw):
    pattern = Struct(
        "pDxgAdapter" / Int64ul,
        "PlaneCount" / Int32ul,
        "PresentIdOrPhysicalAddress" / Int64ul,
        "VidPnSourceId" / Int32ul,
        "FrameNumber" / Int32ul,
        "FlipEntryCount" / Int32ul,
        "FlipSubmitSequence" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=274, version=0)
class Microsoft_Windows_DxgKrnl_274_0(Etw):
    pattern = Struct(
        "DxgAdapter" / Int64ul,
        "SegmentId" / Int32ul,
        "TotalBytesResident" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=275, version=0)
class Microsoft_Windows_DxgKrnl_275_0(Etw):
    pattern = Struct(
        "DeviceObject" / Int64ul,
        "OldBrightness" / Int32ul,
        "NewBrightness" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=276, version=0)
class Microsoft_Windows_DxgKrnl_276_0(Etw):
    pattern = Struct(
        "DeviceObject" / Int64ul,
        "OldOptimizationLevel" / Int32ul,
        "NewOptimizationLevel" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=277, version=0)
class Microsoft_Windows_DxgKrnl_277_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=278, version=0)
class Microsoft_Windows_DxgKrnl_278_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=279, version=0)
class Microsoft_Windows_DxgKrnl_279_0(Etw):
    pattern = Struct(
        "EProcess" / Int64ul,
        "Section" / Int64ul,
        "VirtualAddress" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=280, version=0)
class Microsoft_Windows_DxgKrnl_280_0(Etw):
    pattern = Struct(
        "EProcess" / Int64ul,
        "Section" / Int64ul,
        "VirtualAddress" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=281, version=0)
class Microsoft_Windows_DxgKrnl_281_0(Etw):
    pattern = Struct(
        "pDmaBuffer" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=282, version=0)
class Microsoft_Windows_DxgKrnl_282_0(Etw):
    pattern = Struct(
        "pDmaBuffer" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=283, version=0)
class Microsoft_Windows_DxgKrnl_283_0(Etw):
    pattern = Struct(
        "AdapterHandle" / Int64ul,
        "State" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=284, version=0)
class Microsoft_Windows_DxgKrnl_284_0(Etw):
    pattern = Struct(
        "pDxgAdapterAllocation" / Int64ul,
        "Flags" / Int32ul,
        "Width" / Int32ul,
        "Height" / Int32ul,
        "Format" / Int32ul,
        "RefreshRateNumerator" / Int32ul,
        "RefreshRateDenominator" / Int32ul,
        "VidPnSourceId" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=285, version=0)
class Microsoft_Windows_DxgKrnl_285_0(Etw):
    pattern = Struct(
        "pDxgAdapterAllocation" / Int64ul,
        "Flags" / Int32ul,
        "Width" / Int32ul,
        "Height" / Int32ul,
        "Format" / Int32ul,
        "Pitch" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=286, version=0)
class Microsoft_Windows_DxgKrnl_286_0(Etw):
    pattern = Struct(
        "pDxgAdapterAllocation" / Int64ul,
        "Flags" / Int32ul,
        "Width" / Int32ul,
        "Height" / Int32ul,
        "Pitch" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=287, version=0)
class Microsoft_Windows_DxgKrnl_287_0(Etw):
    pattern = Struct(
        "pDxgAdapterAllocation" / Int64ul,
        "Flags" / Int32ul,
        "Width" / Int32ul,
        "Height" / Int32ul,
        "Format" / Int32ul,
        "GdiSurfaceType" / Int32ul,
        "GdiSurfaceFlags" / Int32ul,
        "Pitch" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=288, version=0)
class Microsoft_Windows_DxgKrnl_288_0(Etw):
    pattern = Struct(
        "ProcessId" / Int32ul,
        "Handle" / Int64ul,
        "Size" / Int64ul,
        "hProcessAlloc" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=289, version=0)
class Microsoft_Windows_DxgKrnl_289_0(Etw):
    pattern = Struct(
        "ProcessId" / Int32ul,
        "Handle" / Int64ul,
        "Size" / Int64ul,
        "hProcessAlloc" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=290, version=0)
class Microsoft_Windows_DxgKrnl_290_0(Etw):
    pattern = Struct(
        "hAdapter" / Int64ul,
        "hSyncObject" / Int64ul,
        "Reason" / Int32ul,
        "Flags" / Int32ul,
        "SharedHandle" / Int64ul,
        "InitialValue" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=291, version=0)
class Microsoft_Windows_DxgKrnl_291_0(Etw):
    pattern = Struct(
        "hAdapter" / Int64ul,
        "hSyncObject" / Int64ul,
        "Reason" / Int32ul,
        "Flags" / Int32ul,
        "SharedHandle" / Int64ul,
        "InitialValue" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=292, version=0)
class Microsoft_Windows_DxgKrnl_292_0(Etw):
    pattern = Struct(
        "hAdapter" / Int64ul,
        "hSyncObject" / Int64ul,
        "Reason" / Int32ul,
        "Flags" / Int32ul,
        "SharedHandle" / Int64ul,
        "InitialValue" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=293, version=0)
class Microsoft_Windows_DxgKrnl_293_0(Etw):
    pattern = Struct(
        "hAdapter" / Int64ul,
        "hSyncObject" / Int64ul,
        "Reason" / Int32ul,
        "Flags" / Int32ul,
        "SharedHandle" / Int64ul,
        "InitialValue" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=294, version=0)
class Microsoft_Windows_DxgKrnl_294_0(Etw):
    pattern = Struct(
        "ContextCount" / Int32ul,
        "hContext" / Int64ul,
        "Flags" / Int32ul,
        "ObjectCount" / Int32ul,
        "ObjectArray" / Int64ul,
        "MonitoredFenceValue" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=295, version=0)
class Microsoft_Windows_DxgKrnl_295_0(Etw):
    pattern = Struct(
        "hContext" / Int64ul,
        "ObjectCount" / Int32ul,
        "ObjectArray" / Int64ul,
        "MonitoredFenceValue" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=296, version=0)
class Microsoft_Windows_DxgKrnl_296_0(Etw):
    pattern = Struct(
        "hDevice" / Int64ul,
        "ObjectCount" / Int32ul,
        "ObjectArray" / Int64ul,
        "MonitoredFenceValue" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=297, version=0)
class Microsoft_Windows_DxgKrnl_297_0(Etw):
    pattern = Struct(
        "hDevice" / Int64ul,
        "ObjectCount" / Int32ul,
        "ObjectArray" / Int64ul,
        "MonitoredFenceValue" / Int64ul,
        "hAsyncEvent" / Int64ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=298, version=0)
class Microsoft_Windows_DxgKrnl_298_0(Etw):
    pattern = Struct(
        "hDevice" / Int64ul,
        "SyncPointId" / Int64ul,
        "ContextCount" / Int32ul,
        "ContextArray" / Int64ul,
        "SubmissionIdArray" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=299, version=0)
class Microsoft_Windows_DxgKrnl_299_0(Etw):
    pattern = Struct(
        "hDevice" / Int64ul,
        "SyncPointId" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=300, version=0)
class Microsoft_Windows_DxgKrnl_300_0(Etw):
    pattern = Struct(
        "Event" / Int64ul,
        "WaitConditionCount" / Int32ul,
        "FenceValues" / Int64ul,
        "SyncObjects" / Int64ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=301, version=0)
class Microsoft_Windows_DxgKrnl_301_0(Etw):
    pattern = Struct(
        "EProcess" / Int64ul,
        "Range" / Int64ul,
        "Block" / Int64ul,
        "Section" / Int64ul,
        "Heap" / Int64ul,
        "StartAddress" / Int64ul,
        "EndAddress" / Int64ul,
        "HeapType" / Int32ul,
        "CreationState" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=302, version=0)
class Microsoft_Windows_DxgKrnl_302_0(Etw):
    pattern = Struct(
        "Range" / Int64ul,
        "PreviousState" / Int32ul,
        "NewState" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=303, version=0)
class Microsoft_Windows_DxgKrnl_303_0(Etw):
    pattern = Struct(
        "Range" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=304, version=1)
class Microsoft_Windows_DxgKrnl_304_1(Etw):
    pattern = Struct(
        "PhysicalAdapterIndex" / Int32ul,
        "DriverSegmentIndex" / Int32ul,
        "VprIndex" / Int32ul,
        "NewStartOffset" / Int64ul,
        "NewSize" / Int64ul,
        "pDxgAdapter" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=305, version=1)
class Microsoft_Windows_DxgKrnl_305_1(Etw):
    pattern = Struct(
        "hContext" / Int64ul,
        "SubmitSequence" / Int32ul,
        "uiNbWrittenPrimaries" / Int32ul,
        "WrittenPrimaries" / Int64ul,
        "pQueuePacket" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=306, version=1)
class Microsoft_Windows_DxgKrnl_306_1(Etw):
    pattern = Struct(
        "pDxgAdapter" / Int64ul,
        "hDmaBuffer" / Int64ul,
        "ContinueNextBuffer" / Int8ul,
        "hAllocationGlobalHandle" / Int64ul,
        "AllocationOffset" / Int64ul,
        "TransferSize" / Int64ul,
        "SourceSegmentId" / Int32ul,
        "DestinationSegmentId" / Int32ul,
        "SourceVirtualAddress" / Int64ul,
        "DestinationVirtualAddress" / Int64ul,
        "SourcePageTable" / Int64ul,
        "TransferDirection" / Int32ul,
        "TransferFlags" / Int32ul,
        "DestinationPageTable" / Int64ul,
        "SourceSegmentOffset" / Int64ul,
        "DestinationSegmentOffset" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=307, version=1)
class Microsoft_Windows_DxgKrnl_307_1(Etw):
    pattern = Struct(
        "pDxgAdapter" / Int64ul,
        "hDmaBuffer" / Int64ul,
        "ContinueNextBuffer" / Int8ul,
        "hAllocationGlobalHandle" / Int64ul,
        "AllocationOffset" / Int64ul,
        "FillSize" / Int64ul,
        "FillPattern" / Int32ul,
        "SegmentId" / Int32ul,
        "DestinationVirtualAddress" / Int64ul,
        "SegmentOffset" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=308, version=0)
class Microsoft_Windows_DxgKrnl_308_0(Etw):
    pattern = Struct(
        "pDxgAdapter" / Int64ul,
        "hDmaBuffer" / Int64ul,
        "ContinueNextBuffer" / Int8ul,
        "hAllocationGlobalHandle" / Int64ul,
        "SegmentId" / Int32ul,
        "SegmentAddress" / Int64ul,
        "VirtualAddress" / Int64ul,
        "GpuVirtualAddress" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=309, version=0)
class Microsoft_Windows_DxgKrnl_309_0(Etw):
    pattern = Struct(
        "pDxgAdapter" / Int64ul,
        "hDmaBuffer" / Int64ul,
        "ContinueNextBuffer" / Int8ul,
        "hAllocationGlobalHandle" / Int64ul,
        "PageTableLevel" / Int32ul,
        "PageTableAddress" / Int64ul,
        "SegmentId" / Int32ul,
        "NumPageTableUpdateEntries" / Int32ul,
        "PageTableEntries" / Int64ul,
        "PageTableEntries64KB" / Int64ul,
        "StartIndex" / Int32ul,
        "Flags" / Int32ul,
        "DriverProtection" / Int64ul,
        "AllocationOffsetInBytes" / Int64ul,
        "hProcess" / Int64ul,
        "UpdateMode" / Int32ul,
        "FirstPteVirtualAddress" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=310, version=0)
class Microsoft_Windows_DxgKrnl_310_0(Etw):
    pattern = Struct(
        "pDxgAdapter" / Int64ul,
        "hDmaBuffer" / Int64ul,
        "ContinueNextBuffer" / Int8ul,
        "hAllocationGlobalHandle" / Int64ul,
        "RootPageTableSegmentId" / Int32ul,
        "RootPageTableSegmentOffset" / Int64ul,
        "hProcess" / Int64ul,
        "StartVirtualAddress" / Int64ul,
        "EndVirtualAddress" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=311, version=0)
class Microsoft_Windows_DxgKrnl_311_0(Etw):
    pattern = Struct(
        "pDxgAdapter" / Int64ul,
        "hDmaBuffer" / Int64ul,
        "ContinueNextBuffer" / Int8ul,
        "hAllocationGlobalHandle" / Int64ul,
        "ContextAllocation" / Int64ul,
        "ContextAllocationSize" / Int64ul,
        "pDriverPrivateData" / Int64ul,
        "DriverPrivateDataSize" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=312, version=0)
class Microsoft_Windows_DxgKrnl_312_0(Etw):
    pattern = Struct(
        "pDxgAdapter" / Int64ul,
        "hDmaBuffer" / Int64ul,
        "ContinueNextBuffer" / Int8ul,
        "hAllocationGlobalHandle" / Int64ul,
        "SegmentId" / Int32ul,
        "SegmentOffset" / Int64ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=313, version=0)
class Microsoft_Windows_DxgKrnl_313_0(Etw):
    pattern = Struct(
        "pDxgAdapter" / Int64ul,
        "hAllocationGlobalHandle" / Int64ul,
        "SegmentId" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=314, version=0)
class Microsoft_Windows_DxgKrnl_314_0(Etw):
    pattern = Struct(
        "pDxgAdapter" / Int64ul,
        "hAllocationGlobalHandle" / Int64ul,
        "SegmentId" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=315, version=0)
class Microsoft_Windows_DxgKrnl_315_0(Etw):
    pattern = Struct(
        "VidPnSourceId" / Int32ul,
        "PlaneCount" / Int32ul,
        "Scenario" / Int32ul,
        "SourceDimension" / Int32ul,
        "DestDimension" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=316, version=0)
class Microsoft_Windows_DxgKrnl_316_0(Etw):
    pattern = Struct(
        "VidPnSourceId" / Int32ul,
        "PlaneCount" / Int32ul,
        "Scenario" / Int32ul,
        "SourceDimension" / Int32ul,
        "DestDimension" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=317, version=0)
class Microsoft_Windows_DxgKrnl_317_0(Etw):
    pattern = Struct(
        "VidPnSourceId" / Int32ul,
        "YUV" / Int32ul,
        "Flags" / Int32ul,
        "SrcRectleft" / Int32sl,
        "SrcRectright" / Int32sl,
        "SrcRecttop" / Int32sl,
        "SrcRectbottom" / Int32sl,
        "DstRectleft" / Int32sl,
        "DstRectright" / Int32sl,
        "DstRecttop" / Int32sl,
        "DstRectbottom" / Int32sl,
        "ClipRectleft" / Int32sl,
        "ClipRectright" / Int32sl,
        "ClipRecttop" / Int32sl,
        "ClipRectbottom" / Int32sl,
        "Rotation" / Int32ul,
        "Blend" / Int32ul,
        "ColorSpaces" / Int32ul,
        "StretchQuality" / Int32ul,
        "PlaneIndex" / Int32ul,
        "SDRWhiteLevel" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=318, version=0)
class Microsoft_Windows_DxgKrnl_318_0(Etw):
    pattern = Struct(
        "DWMCount" / Int32ul,
        "VsyncCount" / Int32ul,
        "VsyncFlag" / Int32ul,
        "VsyncWaiters" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=319, version=0)
class Microsoft_Windows_DxgKrnl_319_0(Etw):
    pattern = Struct(
        "DWMCount" / Int32ul,
        "VsyncCount" / Int32ul,
        "VsyncFlag" / Int32ul,
        "VsyncWaiters" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=320, version=0)
class Microsoft_Windows_DxgKrnl_320_0(Etw):
    pattern = Struct(
        "pVidMmAlloc" / Int64ul,
        "ResidencyCount" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=321, version=0)
class Microsoft_Windows_DxgKrnl_321_0(Etw):
    pattern = Struct(
        "pVidMmAlloc" / Int64ul,
        "ResidencyCount" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=322, version=1)
class Microsoft_Windows_DxgKrnl_322_1(Etw):
    pattern = Struct(
        "DxgDevice" / Int64ul,
        "PagingQueue" / Int64ul,
        "PagingQueuePacket" / Int64ul,
        "SequenceId" / Int64ul,
        "VidMmOpType" / Int32ul,
        "Alloc" / Int64ul,
        "PagingQueueType" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=323, version=1)
class Microsoft_Windows_DxgKrnl_323_1(Etw):
    pattern = Struct(
        "DxgAdapter" / Int64ul,
        "PagingQueue" / Int64ul,
        "PagingQueuePacket" / Int64ul,
        "SequenceId" / Int64ul,
        "VidMmOpType" / Int32ul,
        "PagingQueueType" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=324, version=0)
class Microsoft_Windows_DxgKrnl_324_0(Etw):
    pattern = Struct(
        "PagingQueue" / Int64ul,
        "PagingQueuePacket" / Int64ul,
        "SequenceId" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=325, version=0)
class Microsoft_Windows_DxgKrnl_325_0(Etw):
    pattern = Struct(
        "PagingQueue" / Int64ul,
        "PagingQueuePacket" / Int64ul,
        "SequenceId" / Int64ul,
        "ExecutionTime100ns" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=326, version=0)
class Microsoft_Windows_DxgKrnl_326_0(Etw):
    pattern = Struct(
        "hDevice" / Int64ul,
        "VidPnSourceId" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=327, version=0)
class Microsoft_Windows_DxgKrnl_327_0(Etw):
    pattern = Struct(
        "Owner" / Int64ul,
        "OwnerType" / Int32ul,
        "VaRangeStart" / Int64ul,
        "VaRangeSize" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=328, version=0)
class Microsoft_Windows_DxgKrnl_328_0(Etw):
    pattern = Struct(
        "VidMmAlloc" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=329, version=0)
class Microsoft_Windows_DxgKrnl_329_0(Etw):
    pattern = Struct(
        "EProcess" / Int64ul,
        "ProcessStatus" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=330, version=1)
class Microsoft_Windows_DxgKrnl_330_1(Etw):
    pattern = Struct(
        "pVaAllocator" / Int64ul,
        "Flags" / Int32ul,
        "StartAddress" / Int64ul,
        "EndAddress" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=331, version=1)
class Microsoft_Windows_DxgKrnl_331_1(Etw):
    pattern = Struct(
        "pVaAllocator" / Int64ul,
        "Flags" / Int32ul,
        "StartAddress" / Int64ul,
        "EndAddress" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=332, version=1)
class Microsoft_Windows_DxgKrnl_332_1(Etw):
    pattern = Struct(
        "pVaAllocator" / Int64ul,
        "Flags" / Int32ul,
        "StartAddress" / Int64ul,
        "EndAddress" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=333, version=1)
class Microsoft_Windows_DxgKrnl_333_1(Etw):
    pattern = Struct(
        "pVaAllocator" / Int64ul,
        "pOwner" / Int64ul,
        "OwnerOffset" / Int64ul,
        "StartAddress" / Int64ul,
        "EndAddress" / Int64ul,
        "Protection" / Int64ul,
        "DriverProtection" / Int64ul,
        "Flags" / Int32ul,
        "MappedAllocationBase" / Int64ul,
        "MappedAllocationSize" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=334, version=1)
class Microsoft_Windows_DxgKrnl_334_1(Etw):
    pattern = Struct(
        "pVaAllocator" / Int64ul,
        "pOwner" / Int64ul,
        "OwnerOffset" / Int64ul,
        "StartAddress" / Int64ul,
        "EndAddress" / Int64ul,
        "Protection" / Int64ul,
        "DriverProtection" / Int64ul,
        "Flags" / Int32ul,
        "MappedAllocationBase" / Int64ul,
        "MappedAllocationSize" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=335, version=0)
class Microsoft_Windows_DxgKrnl_335_0(Etw):
    pattern = Struct(
        "pVaAllocator" / Int64ul,
        "hProcessId" / Int64ul,
        "pDxgAdapter" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=336, version=0)
class Microsoft_Windows_DxgKrnl_336_0(Etw):
    pattern = Struct(
        "pVaAllocator" / Int64ul,
        "hProcessId" / Int64ul,
        "pDxgAdapter" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=337, version=0)
class Microsoft_Windows_DxgKrnl_337_0(Etw):
    pattern = Struct(
        "pVaAllocator" / Int64ul,
        "hProcessId" / Int64ul,
        "pDxgAdapter" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=338, version=0)
class Microsoft_Windows_DxgKrnl_338_0(Etw):
    pattern = Struct(
        "pPagingQueue" / Int64ul,
        "pSyncObject" / Int64ul,
        "NumAllocations" / Int32ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=339, version=0)
class Microsoft_Windows_DxgKrnl_339_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "NumBytesToTrim" / Int64ul,
        "PagingFenceValue" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=340, version=0)
class Microsoft_Windows_DxgKrnl_340_0(Etw):
    pattern = Struct(
        "pAlloc" / Int64ul,
        "Flags" / Int32ul,
        "Location" / Int32ul,
        "bFallbackToSystemMemory" / Int8ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=341, version=0)
class Microsoft_Windows_DxgKrnl_341_0(Etw):
    pattern = Struct(
        "pAlloc" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=342, version=0)
class Microsoft_Windows_DxgKrnl_342_0(Etw):
    pattern = Struct(
        "pDxgAdapter" / Int64ul,
        "Flags" / Int32ul,
        "SessionId" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=343, version=0)
class Microsoft_Windows_DxgKrnl_343_0(Etw):
    pattern = Struct(
        "Function" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=344, version=0)
class Microsoft_Windows_DxgKrnl_344_0(Etw):
    pattern = Struct(
        "Function" / Int32ul,
        "Src" / Int32ul,
        "Dst" / Int32ul,
        "SrcWidth" / Int32ul,
        "SrcHeight" / Int32ul,
        "DstWidth" / Int32ul,
        "DstHeight" / Int32ul,
        "Accelerated" / Int8ul,
        "SolidColor" / Int8ul,
        "Reserved" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=346, version=0)
class Microsoft_Windows_DxgKrnl_346_0(Etw):
    pattern = Struct(
        "VidMmDevice" / Int64ul,
        "PagingQueue" / Int64ul,
        "PagingQueuePacket" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=347, version=0)
class Microsoft_Windows_DxgKrnl_347_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "PageInPass" / Int32ul,
        "OverBudget" / Int8ul,
        "PriorityBandRestriction" / Int32ul,
        "PageInPreferredOnly" / Int8ul,
        "Recoverable" / Int8ul,
        "FailedVidMmAlloc" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=348, version=0)
class Microsoft_Windows_DxgKrnl_348_0(Etw):
    pattern = Struct(
        "Function" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=349, version=0)
class Microsoft_Windows_DxgKrnl_349_0(Etw):
    pattern = Struct(
        "Function" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=350, version=0)
class Microsoft_Windows_DxgKrnl_350_0(Etw):
    pattern = Struct(
        "pDxgDevice" / Int64ul,
        "TargetBand" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=351, version=0)
class Microsoft_Windows_DxgKrnl_351_0(Etw):
    pattern = Struct(
        "pDxgDevice" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=352, version=0)
class Microsoft_Windows_DxgKrnl_352_0(Etw):
    pattern = Struct(
        "pDxgDevice" / Int64ul,
        "pYieldedTo" / Int64ul,
        "Delta" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=353, version=0)
class Microsoft_Windows_DxgKrnl_353_0(Etw):
    pattern = Struct(
        "pDxgDevice" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=354, version=0)
class Microsoft_Windows_DxgKrnl_354_0(Etw):
    pattern = Struct(
        "pDxgAdapter" / Int64ul,
        "YieldingPriority" / Int32ul,
        "YieldBudget" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=355, version=0)
class Microsoft_Windows_DxgKrnl_355_0(Etw):
    pattern = Struct(
        "pDxgAdapter" / Int64ul,
        "NodeOrdinal" / Int32ul,
        "YieldExpirationInterval" / Int64ul,
        "YieldTimerExpirationInterval" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=356, version=0)
class Microsoft_Windows_DxgKrnl_356_0(Etw):
    pattern = Struct(
        "pDxgAdapter" / Int64ul,
        "NodeOrdinal" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=357, version=0)
class Microsoft_Windows_DxgKrnl_357_0(Etw):
    pattern = Struct(
        "pDxgAdapter" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=358, version=0)
class Microsoft_Windows_DxgKrnl_358_0(Etw):
    pattern = Struct(
        "pDxgAdapter" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=359, version=0)
class Microsoft_Windows_DxgKrnl_359_0(Etw):
    pattern = Struct(
        "pDxgAdapter" / Int64ul,
        "YieldCondition" / Int32ul,
        "Parameter0" / Int64ul,
        "Parameter1" / Int64ul,
        "Parameter2" / Int64ul,
        "Parameter3" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=360, version=0)
class Microsoft_Windows_DxgKrnl_360_0(Etw):
    pattern = Struct(
        "pDxgAdapter" / Int64ul,
        "FlushSchedulerReason" / Int32ul,
        "VidPnSourceId" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=361, version=0)
class Microsoft_Windows_DxgKrnl_361_0(Etw):
    pattern = Struct(
        "QueuePacket" / Int64ul,
        "hContext" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=362, version=0)
class Microsoft_Windows_DxgKrnl_362_0(Etw):
    pattern = Struct(
        "Timeout" / Int64sl,
        "WakeReason" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=363, version=0)
class Microsoft_Windows_DxgKrnl_363_0(Etw):
    pattern = Struct(
        "pDxgAdapter" / Int64ul,
        "YieldPriorityBand" / Int32ul,
        "RunningTime" / Int64ul,
        "NodeOrdinal" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=364, version=0)
class Microsoft_Windows_DxgKrnl_364_0(Etw):
    pattern = Struct(
        "hProcessId" / Int64ul,
        "hVidMmGlobalAlloc" / Int64ul,
        "PageCount" / Int32ul,
        "Pages" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=365, version=0)
class Microsoft_Windows_DxgKrnl_365_0(Etw):
    pattern = Struct(
        "hVidMmGlobalAlloc" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=366, version=0)
class Microsoft_Windows_DxgKrnl_366_0(Etw):
    pattern = Struct(
        "NewBudget" / Int64ul,
        "OldBudget" / Int64ul,
        "pDxgAdapter" / Int64ul,
        "ProcessId" / Int32ul,
        "PhysicalAdapterIndex" / Int16ul,
        "NewPriorityBand" / Int8ul,
        "OldPriorityBand" / Int8ul,
        "NewVisibilityState" / Int8ul,
        "OldVisibilityState" / Int8ul,
        "MemorySegmentGroup" / Int8ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=367, version=0)
class Microsoft_Windows_DxgKrnl_367_0(Etw):
    pattern = Struct(
        "NewUsage" / Int64ul,
        "OldUsage" / Int64ul,
        "pDxgAdapter" / Int64ul,
        "ProcessId" / Int32ul,
        "PhysicalAdapterIndex" / Int16ul,
        "MemorySegmentGroup" / Int8ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=368, version=0)
class Microsoft_Windows_DxgKrnl_368_0(Etw):
    pattern = Struct(
        "AdapterFdoContext" / Int64ul,
        "DevicePowerState" / Int32ul,
        "Reason" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=369, version=0)
class Microsoft_Windows_DxgKrnl_369_0(Etw):
    pattern = Struct(
        "DxgAdapter" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=370, version=0)
class Microsoft_Windows_DxgKrnl_370_0(Etw):
    pattern = Struct(
        "Commitment" / Int64ul,
        "OldCommitment" / Int64ul,
        "pDxgAdapter" / Int64ul,
        "ProcessId" / Int32ul,
        "PhysicalAdapterIndex" / Int16ul,
        "PriorityClass" / Int8ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=371, version=0)
class Microsoft_Windows_DxgKrnl_371_0(Etw):
    pattern = Struct(
        "Commitment" / Int64ul,
        "OldCommitment" / Int64ul,
        "pDxgAdapter" / Int64ul,
        "ProcessId" / Int32ul,
        "PhysicalAdapterIndex" / Int16ul,
        "MemorySegmentGroup" / Int8ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=372, version=0)
class Microsoft_Windows_DxgKrnl_372_0(Etw):
    pattern = Struct(
        "VidPnSourceId" / Int32ul,
        "Flags" / Int32ul,
        "SrcRectleft" / Int32sl,
        "SrcRectright" / Int32sl,
        "SrcRecttop" / Int32sl,
        "SrcRectbottom" / Int32sl,
        "DstRectleft" / Int32sl,
        "DstRectright" / Int32sl,
        "DstRecttop" / Int32sl,
        "DstRectbottom" / Int32sl,
        "Rotation" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=373, version=0)
class Microsoft_Windows_DxgKrnl_373_0(Etw):
    pattern = Struct(
        "hVidmmGlobalAlloc" / Int64ul,
        "OldOwnerPid" / Int32ul,
        "NewOwnerPid" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=374, version=0)
class Microsoft_Windows_DxgKrnl_374_0(Etw):
    pattern = Struct(
        "pVidMmAlloc" / Int64ul,
        "ResidencyCount" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=375, version=0)
class Microsoft_Windows_DxgKrnl_375_0(Etw):
    pattern = Struct(
        "hAdapter" / Int64ul,
        "hSyncObject" / Int64ul,
        "Reason" / Int32ul,
        "Flags" / Int32ul,
        "SharedHandle" / Int64ul,
        "hNotificationAdapter" / Int64ul,
        "VidPnTargetId" / Int32ul,
        "TimeOffset" / Int64sl
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=376, version=0)
class Microsoft_Windows_DxgKrnl_376_0(Etw):
    pattern = Struct(
        "hAdapter" / Int64ul,
        "hSyncObject" / Int64ul,
        "Reason" / Int32ul,
        "Flags" / Int32ul,
        "SharedHandle" / Int64ul,
        "hNotificationAdapter" / Int64ul,
        "VidPnTargetId" / Int32ul,
        "TimeOffset" / Int64sl
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=377, version=0)
class Microsoft_Windows_DxgKrnl_377_0(Etw):
    pattern = Struct(
        "hAdapter" / Int64ul,
        "hSyncObject" / Int64ul,
        "Reason" / Int32ul,
        "Flags" / Int32ul,
        "SharedHandle" / Int64ul,
        "hNotificationAdapter" / Int64ul,
        "VidPnTargetId" / Int32ul,
        "TimeOffset" / Int64sl
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=378, version=0)
class Microsoft_Windows_DxgKrnl_378_0(Etw):
    pattern = Struct(
        "hAdapter" / Int64ul,
        "hSyncObject" / Int64ul,
        "Reason" / Int32ul,
        "Flags" / Int32ul,
        "SharedHandle" / Int64ul,
        "hNotificationAdapter" / Int64ul,
        "VidPnTargetId" / Int32ul,
        "TimeOffset" / Int64sl
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=379, version=0)
class Microsoft_Windows_DxgKrnl_379_0(Etw):
    pattern = Struct(
        "pVidSchSyncObject" / Int64ul,
        "VidPnSourceID" / Int32ul,
        "TimeOffset" / Int64ul,
        "RefreshPeriod" / Int64ul,
        "NotificationID" / Int32ul,
        "hNotification" / Int64ul,
        "pHighResolutionTimer" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=380, version=0)
class Microsoft_Windows_DxgKrnl_380_0(Etw):
    pattern = Struct(
        "pVidSchSyncObject" / Int64ul,
        "VidPnSourceID" / Int32ul,
        "NotificationID" / Int32ul,
        "IsrFrameTimeValue" / Int64sl,
        "DueValue" / Int64sl,
        "FrameNumber" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=381, version=0)
class Microsoft_Windows_DxgKrnl_381_0(Etw):
    pattern = Struct(
        "pDxgAdapter" / Int64ul,
        "VidPnTargetId" / Int32ul,
        "ScannedPhysicalAddress" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=382, version=0)
class Microsoft_Windows_DxgKrnl_382_0(Etw):
    pattern = Struct(
        "pDxgAdapter" / Int64ul,
        "PlaneCount" / Int32ul,
        "ScannedPhysicalAddress" / Int64ul,
        "VidPnSourceId" / Int32ul,
        "FrameNumber" / Int32ul,
        "FlipEntryCount" / Int32ul,
        "FlipSubmitSequence" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=383, version=0)
class Microsoft_Windows_DxgKrnl_383_0(Etw):
    pattern = Struct(
        "pDxgAdapter" / Int64ul,
        "VidPnSourceId" / Int32ul,
        "SessionId" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=384, version=0)
class Microsoft_Windows_DxgKrnl_384_0(Etw):
    pattern = Struct(
        "NodeOrdinal" / Int32ul,
        "hContext" / Int64ul,
        "DefaultQuantum" / Int64sl,
        "RemainingQuantum" / Int64sl,
        "LastRunningTimeCalculatedAt" / Int64ul,
        "LastRunningTime" / Int64sl
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=385, version=0)
class Microsoft_Windows_DxgKrnl_385_0(Etw):
    pattern = Struct(
        "NodeOrdinal" / Int32ul,
        "YieldPriorityLevel" / Int8ul,
        "hContext" / Int64ul,
        "DefaultQuantum" / Int64sl,
        "RemainingQuantum" / Int64sl,
        "LastRunningTimeCalculatedAt" / Int64ul,
        "LastRunningTime" / Int64sl
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=386, version=3)
class Microsoft_Windows_DxgKrnl_386_3(Etw):
    pattern = Struct(
        "pDxgAdapter" / Int64ul,
        "VidPnSourceId" / Int32ul,
        "PlaneCount" / Int32ul,
        "PresentId" / Int64ul,
        "InputFlags" / Int32ul,
        "OutputFlags" / Int32ul,
        "PostCompositionSrcRectleft" / Int32sl,
        "PostCompositionSrcRectright" / Int32sl,
        "PostCompositionSrcRecttop" / Int32sl,
        "PostCompositionSrcRectbottom" / Int32sl,
        "PostCompositionDstRectleft" / Int32sl,
        "PostCompositionDstRectright" / Int32sl,
        "PostCompositionDstRecttop" / Int32sl,
        "PostCompositionDstRectbottom" / Int32sl,
        "HDRMetaDataSpecified" / Int8ul,
        "HDRMetaDataType" / Int32ul,
        "FlipDoNotFlip" / Int8ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=387, version=0)
class Microsoft_Windows_DxgKrnl_387_0(Etw):
    pattern = Struct(
        "pVidSchSyncObject" / Int64ul,
        "VidPnSourceID" / Int32ul,
        "TimeOffset" / Int64ul,
        "RefreshPeriod" / Int64ul,
        "NotificationID" / Int32ul,
        "hNotification" / Int64ul,
        "pHighResolutionTimer" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=389, version=0)
class Microsoft_Windows_DxgKrnl_389_0(Etw):
    pattern = Struct(
        "SessionGuid" / Guid
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=390, version=0)
class Microsoft_Windows_DxgKrnl_390_0(Etw):
    pattern = Struct(
        "SessionGuid" / Guid
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=391, version=0)
class Microsoft_Windows_DxgKrnl_391_0(Etw):
    pattern = Struct(
        "hGlobalAllocationHandle" / Int64ul,
        "ulSegmentId" / Int32ul,
        "SegmentOffset" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=392, version=0)
class Microsoft_Windows_DxgKrnl_392_0(Etw):
    pattern = Struct(
        "VmBusChannel" / Int64ul,
        "CommandId" / Int64ul,
        "CommandType" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=393, version=0)
class Microsoft_Windows_DxgKrnl_393_0(Etw):
    pattern = Struct(
        "VmBusChannel" / Int64ul,
        "CommandId" / Int64ul,
        "CommandType" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=394, version=0)
class Microsoft_Windows_DxgKrnl_394_0(Etw):
    pattern = Struct(
        "VmBusChannel" / Int64ul,
        "CommandId" / Int64ul,
        "CommandType" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=395, version=0)
class Microsoft_Windows_DxgKrnl_395_0(Etw):
    pattern = Struct(
        "VmBusChannel" / Int64ul,
        "CommandId" / Int64ul,
        "CommandType" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=396, version=0)
class Microsoft_Windows_DxgKrnl_396_0(Etw):
    pattern = Struct(
        "VmBusChannel" / Int64ul,
        "CommandId" / Int64ul,
        "CommandType" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=397, version=0)
class Microsoft_Windows_DxgKrnl_397_0(Etw):
    pattern = Struct(
        "VmBusChannel" / Int64ul,
        "CommandId" / Int64ul,
        "CommandType" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=398, version=0)
class Microsoft_Windows_DxgKrnl_398_0(Etw):
    pattern = Struct(
        "VmBusChannel" / Int64ul,
        "CommandId" / Int64ul,
        "CommandType" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=399, version=0)
class Microsoft_Windows_DxgKrnl_399_0(Etw):
    pattern = Struct(
        "AdapterHandle" / Int64ul,
        "Function" / WString,
        "Parameters" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=400, version=0)
class Microsoft_Windows_DxgKrnl_400_0(Etw):
    pattern = Struct(
        "AdapterHandle" / Int64ul,
        "Function" / WString,
        "Parameters" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=401, version=0)
class Microsoft_Windows_DxgKrnl_401_0(Etw):
    pattern = Struct(
        "pDxgAdapter" / Int64ul,
        "Allocation" / Int64ul,
        "VidPnSourceId" / Int32ul,
        "PlaneIndex" / Int32ul,
        "VidPnSourceVisibilty" / Int8ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=402, version=0)
class Microsoft_Windows_DxgKrnl_402_0(Etw):
    pattern = Struct(
        "VmBusChannel" / Int64ul,
        "CommandId" / Int64ul,
        "CommandType" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=403, version=0)
class Microsoft_Windows_DxgKrnl_403_0(Etw):
    pattern = Struct(
        "VmBusChannel" / Int64ul,
        "CommandId" / Int64ul,
        "CommandType" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=404, version=0)
class Microsoft_Windows_DxgKrnl_404_0(Etw):
    pattern = Struct(
        "VmBusChannel" / Int64ul,
        "CommandId" / Int64ul,
        "CommandType" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=405, version=0)
class Microsoft_Windows_DxgKrnl_405_0(Etw):
    pattern = Struct(
        "VmBusChannel" / Int64ul,
        "CommandId" / Int64ul,
        "CommandType" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=406, version=0)
class Microsoft_Windows_DxgKrnl_406_0(Etw):
    pattern = Struct(
        "VmBusChannel" / Int64ul,
        "CommandId" / Int64ul,
        "CommandType" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=407, version=0)
class Microsoft_Windows_DxgKrnl_407_0(Etw):
    pattern = Struct(
        "VmBusChannel" / Int64ul,
        "CommandId" / Int64ul,
        "CommandType" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=408, version=0)
class Microsoft_Windows_DxgKrnl_408_0(Etw):
    pattern = Struct(
        "VmBusChannel" / Int64ul,
        "CommandId" / Int64ul,
        "CommandType" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=409, version=0)
class Microsoft_Windows_DxgKrnl_409_0(Etw):
    pattern = Struct(
        "VmBusChannel" / Int64ul,
        "CommandId" / Int64ul,
        "CommandType" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=410, version=0)
class Microsoft_Windows_DxgKrnl_410_0(Etw):
    pattern = Struct(
        "VmBusChannel" / Int64ul,
        "CommandId" / Int64ul,
        "CommandType" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=411, version=0)
class Microsoft_Windows_DxgKrnl_411_0(Etw):
    pattern = Struct(
        "VmBusChannel" / Int64ul,
        "CommandId" / Int64ul,
        "CommandType" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=412, version=0)
class Microsoft_Windows_DxgKrnl_412_0(Etw):
    pattern = Struct(
        "VmBusChannel" / Int64ul,
        "CommandId" / Int64ul,
        "CommandType" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=413, version=0)
class Microsoft_Windows_DxgKrnl_413_0(Etw):
    pattern = Struct(
        "VmBusChannel" / Int64ul,
        "CommandId" / Int64ul,
        "CommandType" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=414, version=0)
class Microsoft_Windows_DxgKrnl_414_0(Etw):
    pattern = Struct(
        "VmBusChannel" / Int64ul,
        "CommandId" / Int64ul,
        "CommandType" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=415, version=0)
class Microsoft_Windows_DxgKrnl_415_0(Etw):
    pattern = Struct(
        "VmBusChannel" / Int64ul,
        "CommandId" / Int64ul,
        "CommandType" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=416, version=0)
class Microsoft_Windows_DxgKrnl_416_0(Etw):
    pattern = Struct(
        "pDxgAdapter" / Int64ul,
        "VidPnSourceId" / Int32ul,
        "PlaneIndex" / Int32ul,
        "Enabled" / Int8ul,
        "Flags" / Int32ul,
        "SrcRectleft" / Int32ul,
        "SrcRecttop" / Int32ul,
        "SrcRectright" / Int32ul,
        "SrcRectbottom" / Int32ul,
        "DstRectleft" / Int32ul,
        "DstRecttop" / Int32ul,
        "DstRectright" / Int32ul,
        "DstRectbottom" / Int32ul,
        "ClipRectleft" / Int32ul,
        "ClipRecttop" / Int32ul,
        "ClipRectright" / Int32ul,
        "ClipRectbottom" / Int32ul,
        "Blend" / Int32ul,
        "ColorSpace" / Int32ul,
        "SDRWhiteLevel" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=417, version=0)
class Microsoft_Windows_DxgKrnl_417_0(Etw):
    pattern = Struct(
        "pDxgAdapter" / Int64ul,
        "VidPnSourceId" / Int32ul,
        "Enabled" / Int8ul,
        "SrcRectleft" / Int32ul,
        "SrcRecttop" / Int32ul,
        "SrcRectright" / Int32ul,
        "SrcRectbottom" / Int32ul,
        "DstRectleft" / Int32ul,
        "DstRecttop" / Int32ul,
        "DstRectright" / Int32ul,
        "DstRectbottom" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=418, version=0)
class Microsoft_Windows_DxgKrnl_418_0(Etw):
    pattern = Struct(
        "pDxgAdapter" / Int64ul,
        "PhysicalAdapterIndex" / Int16ul,
        "DriverSegmentIndex" / Int16ul,
        "VprIndex" / Int16ul,
        "Commit" / Int64ul,
        "Size" / Int64ul,
        "GrowRatio" / Int32ul,
        "CurrentRatio" / Int32ul,
        "Capacity" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=419, version=0)
class Microsoft_Windows_DxgKrnl_419_0(Etw):
    pattern = Struct(
        "pDxgAdapter" / Int64ul,
        "PhysicalAdapterIndex" / Int16ul,
        "DriverSegmentIndex" / Int16ul,
        "VprIndex" / Int16ul,
        "CapacityRatio" / Int32ul,
        "CurrentRatio" / Int32ul,
        "Capacity" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=420, version=0)
class Microsoft_Windows_DxgKrnl_420_0(Etw):
    pattern = Struct(
        "VidPnSourceID" / Int32ul,
        "NotificationID" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=421, version=0)
class Microsoft_Windows_DxgKrnl_421_0(Etw):
    pattern = Struct(
        "VidPnSourceID" / Int32ul,
        "NotificationID" / Int32ul,
        "DpcFrameTimeValue" / Int64sl,
        "DpcFrameNumber" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=422, version=0)
class Microsoft_Windows_DxgKrnl_422_0(Etw):
    pattern = Struct(
        "hContext" / Int64ul,
        "hHwQueue" / Int64ul,
        "ParentDxgHwQueue" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=423, version=0)
class Microsoft_Windows_DxgKrnl_423_0(Etw):
    pattern = Struct(
        "hContext" / Int64ul,
        "hHwQueue" / Int64ul,
        "ParentDxgHwQueue" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=424, version=0)
class Microsoft_Windows_DxgKrnl_424_0(Etw):
    pattern = Struct(
        "hContext" / Int64ul,
        "hHwQueue" / Int64ul,
        "ParentDxgHwQueue" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=425, version=0)
class Microsoft_Windows_DxgKrnl_425_0(Etw):
    pattern = Struct(
        "pDxgAdapter" / Int64ul,
        "QueriedSize" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=426, version=0)
class Microsoft_Windows_DxgKrnl_426_0(Etw):
    pattern = Struct(
        "pDxgAdapter" / Int64ul,
        "Offset" / Int32ul,
        "Size" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=427, version=0)
class Microsoft_Windows_DxgKrnl_427_0(Etw):
    pattern = Struct(
        "pDxgAdapter" / Int64ul,
        "Offset" / Int32ul,
        "Size" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=428, version=0)
class Microsoft_Windows_DxgKrnl_428_0(Etw):
    pattern = Struct(
        "pDxgAdapter" / Int64ul,
        "SourceMaskFlushHwAndAbortSwQueue" / Int32ul,
        "SourceMaskFlushHwAndKeepSwQueue" / Int32ul,
        "SourceMaskDisableAllPlanes" / Int32ul,
        "SourceMaskSuspendScheduler" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=429, version=0)
class Microsoft_Windows_DxgKrnl_429_0(Etw):
    pattern = Struct(
        "pDxgAdapter" / Int64ul,
        "SourceMaskResumeScheduler" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=430, version=0)
class Microsoft_Windows_DxgKrnl_430_0(Etw):
    pattern = Struct(
        "pDxgAdapter" / Int64ul,
        "CurrentUsingSource" / Int32ul,
        "NewUsingSource" / Int32ul,
        "ChangedSource" / Int32ul,
        "RemovedSource" / Int32ul,
        "NeedToActivateSource" / Int32ul,
        "ActivityChangedSource" / Int32ul,
        "TopologyChangeSource" / Int32ul,
        "UpdatedSource" / Int32ul,
        "RotatedSource" / Int32ul,
        "PriorityChangeSource" / Int32ul,
        "ReclaimSource" / Int32ul,
        "RenewModeListSource" / Int32ul,
        "MonitorChangedSource" / Int32ul,
        "PowerOffSource" / Int32ul,
        "HMDUsingSource" / Int32ul,
        "HiddenSource" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=431, version=0)
class Microsoft_Windows_DxgKrnl_431_0(Etw):
    pattern = Struct(
        "hAdapter" / Int64ul,
        "NodeOrdinal" / Int32ul,
        "EngineOrdinal" / Int32ul,
        "GpuFrequency" / Int64ul,
        "GpuClock" / Int64ul,
        "CpuClock" / Int64ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=432, version=0)
class Microsoft_Windows_DxgKrnl_432_0(Etw):
    pattern = Struct(
        "hAdapter" / Int64ul,
        "NodeOrdinal" / Int32ul,
        "EngineOrdinal" / Int32ul,
        "CpuTimestamp0" / Int64ul,
        "GpuTimestamp0" / Int64ul,
        "CpuTimestamp1" / Int64ul,
        "GpuTimestamp1" / Int64ul,
        "SchedulingLogSize" / Int32ul,
        "SchedulingLogData" / Bytes(lambda this: this.SchedulingLogSize)
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=433, version=1)
class Microsoft_Windows_DxgKrnl_433_1(Etw):
    pattern = Struct(
        "pDxgObject" / Int64ul,
        "pSchObject" / Int64ul,
        "hKmdHandle" / Int64ul,
        "hOsHandle" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=434, version=0)
class Microsoft_Windows_DxgKrnl_434_0(Etw):
    pattern = Struct(
        "pDxgAdapter" / Int64ul,
        "hDmaBuffer" / Int64ul,
        "ContinueNextBuffer" / Int8ul,
        "hAllocationGlobalHandle" / Int64ul,
        "MonitoredFenceGpuVa" / Int64ul,
        "MonitoredFenceValue" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=435, version=1)
class Microsoft_Windows_DxgKrnl_435_1(Etw):
    pattern = Struct(
        "pVaAllocator" / Int64ul,
        "pOwner" / Int64ul,
        "OwnerOffset" / Int64ul,
        "StartAddress" / Int64ul,
        "EndAddress" / Int64ul,
        "Protection" / Int64ul,
        "DriverProtection" / Int64ul,
        "Flags" / Int32ul,
        "MappedAllocationBase" / Int64ul,
        "MappedAllocationSize" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=436, version=0)
class Microsoft_Windows_DxgKrnl_436_0(Etw):
    pattern = Struct(
        "pDxgAdapter" / Int64ul,
        "hContext" / Int64ul,
        "NodeOrdinal" / Int32ul,
        "ReadyContextPriorityMapBits" / Int32ul,
        "NumberOfULongPtrsInNodeMask" / Int32ul,
        "ReadyNodeSwMapBits" / Int64ul,
        "ReadyNodeHwMapBits" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=437, version=0)
class Microsoft_Windows_DxgKrnl_437_0(Etw):
    pattern = Struct(
        "FinalEvent" / Int8ul,
        "RectCount" / Int32ul,
        "Left" / Int32sl,
        "Right" / Int32sl,
        "Top" / Int32sl,
        "Bottom" / Int32sl
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=438, version=0)
class Microsoft_Windows_DxgKrnl_438_0(Etw):
    pattern = Struct(
        "MiniportContext" / Int64ul,
        "Flags" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=439, version=0)
class Microsoft_Windows_DxgKrnl_439_0(Etw):
    pattern = Struct(
        "MiniportContext" / Int64ul,
        "Flags" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=440, version=0)
class Microsoft_Windows_DxgKrnl_440_0(Etw):
    pattern = Struct(
        "MiniportContext" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=441, version=0)
class Microsoft_Windows_DxgKrnl_441_0(Etw):
    pattern = Struct(
        "MiniportContext" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=442, version=1)
class Microsoft_Windows_DxgKrnl_442_1(Etw):
    pattern = Struct(
        "AdapterHandle" / Int64ul,
        "ComponentIndex" / Int32ul,
        "State" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=443, version=0)
class Microsoft_Windows_DxgKrnl_443_0(Etw):
    pattern = Struct(
        "Id" / Int64ul,
        "CurrentTime" / Int64ul,
        "CurrentPowerLevel" / Int32ul,
        "SubmissionTime" / Int64ul,
        "RequestedDeadline" / Int64ul,
        "CompletionDeadline" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=444, version=0)
class Microsoft_Windows_DxgKrnl_444_0(Etw):
    pattern = Struct(
        "Id" / Int64ul,
        "DeadlineType" / Int32ul,
        "Policy" / Int32ul,
        "Flags" / Int32ul,
        "MaxInstances" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=445, version=1)
class Microsoft_Windows_DxgKrnl_445_1(Etw):
    pattern = Struct(
        "pDxgAdapter" / Int64ul,
        "VirtualFunctionIndex" / Int32ul,
        "bSecure" / Int8ul,
        "Status" / Int32ul,
        "FailureType" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=446, version=1)
class Microsoft_Windows_DxgKrnl_446_1(Etw):
    pattern = Struct(
        "pDxgAdapter" / Int64ul,
        "VirtualFunctionIndex" / Int32ul,
        "bSecure" / Int8ul,
        "Status" / Int32ul,
        "FailureType" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=447, version=1)
class Microsoft_Windows_DxgKrnl_447_1(Etw):
    pattern = Struct(
        "pDxgAdapter" / Int64ul,
        "VirtualFunctionIndex" / Int32ul,
        "bSecure" / Int8ul,
        "Status" / Int32ul,
        "FailureType" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1000, version=0)
class Microsoft_Windows_DxgKrnl_1000_0(Etw):
    pattern = Struct(
        "MiniportContext" / Int64ul,
        "MaxChunkPrivateDriverDataSize" / Int32ul,
        "MiracastCaps" / Int32ul,
        "ReturnStatus" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1001, version=0)
class Microsoft_Windows_DxgKrnl_1001_0(Etw):
    pattern = Struct(
        "MiniportContext" / Int64ul,
        "MaxChunkPrivateDriverDataSize" / Int32ul,
        "MiracastCaps" / Int32ul,
        "ReturnStatus" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1002, version=0)
class Microsoft_Windows_DxgKrnl_1002_0(Etw):
    pattern = Struct(
        "MiniportContext" / Int64ul,
        "MiracastContext" / Int64ul,
        "TargetId" / Int32ul,
        "ReturnStatus" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1003, version=0)
class Microsoft_Windows_DxgKrnl_1003_0(Etw):
    pattern = Struct(
        "MiniportContext" / Int64ul,
        "MiracastContext" / Int64ul,
        "TargetId" / Int32ul,
        "ReturnStatus" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1004, version=0)
class Microsoft_Windows_DxgKrnl_1004_0(Etw):
    pattern = Struct(
        "MiniportContext" / Int64ul,
        "MiracastContext" / Int64ul,
        "InputBufferSize" / Int32ul,
        "OutputBufferSize" / Int32ul,
        "ReturnStatus" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1005, version=0)
class Microsoft_Windows_DxgKrnl_1005_0(Etw):
    pattern = Struct(
        "MiniportContext" / Int64ul,
        "MiracastContext" / Int64ul,
        "InputBufferSize" / Int32ul,
        "OutputBufferSize" / Int32ul,
        "ReturnStatus" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1006, version=0)
class Microsoft_Windows_DxgKrnl_1006_0(Etw):
    pattern = Struct(
        "MiniportContext" / Int64ul,
        "MiracastContext" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1007, version=0)
class Microsoft_Windows_DxgKrnl_1007_0(Etw):
    pattern = Struct(
        "MiniportContext" / Int64ul,
        "MiracastContext" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1008, version=0)
class Microsoft_Windows_DxgKrnl_1008_0(Etw):
    pattern = Struct(
        "MiracastLuid" / Int64ul,
        "InputBufferSize" / Int32ul,
        "OutputBufferSize" / Int32ul,
        "Callback" / Int64ul,
        "CallbackContext" / Int64ul,
        "ReturnStatus" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1009, version=0)
class Microsoft_Windows_DxgKrnl_1009_0(Etw):
    pattern = Struct(
        "MiracastLuid" / Int64ul,
        "InputBufferSize" / Int32ul,
        "OutputBufferSize" / Int32ul,
        "Callback" / Int64ul,
        "CallbackContext" / Int64ul,
        "ReturnStatus" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1010, version=0)
class Microsoft_Windows_DxgKrnl_1010_0(Etw):
    pattern = Struct(
        "MiniportContext" / Int64ul,
        "MiracastLuid" / Int64ul,
        "SqmStringEntry" / WString,
        "MiracastStopSessionReason" / Int32ul,
        "StatusForStopReason" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1011, version=0)
class Microsoft_Windows_DxgKrnl_1011_0(Etw):
    pattern = Struct(
        "MiniportContext" / Int64ul,
        "MiracastLuid" / Int64ul,
        "SqmStringEntry" / WString,
        "MiracastStopSessionReason" / Int32ul,
        "StatusForStopReason" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1012, version=0)
class Microsoft_Windows_DxgKrnl_1012_0(Etw):
    pattern = Struct(
        "MiracastLuid" / Int64ul,
        "Synchronous" / Int8ul,
        "InputBufferSize" / Int32ul,
        "OutputBufferSize" / Int32ul,
        "ReturnStatus" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1013, version=0)
class Microsoft_Windows_DxgKrnl_1013_0(Etw):
    pattern = Struct(
        "MiracastLuid" / Int64ul,
        "Synchronous" / Int8ul,
        "InputBufferSize" / Int32ul,
        "OutputBufferSize" / Int32ul,
        "ReturnStatus" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1014, version=0)
class Microsoft_Windows_DxgKrnl_1014_0(Etw):
    pattern = Struct(
        "MiracastLuid" / Int64ul,
        "Synchronous" / Int8ul,
        "InputBufferSize" / Int32ul,
        "OutputBufferSize" / Int32ul,
        "ReturnStatus" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1015, version=0)
class Microsoft_Windows_DxgKrnl_1015_0(Etw):
    pattern = Struct(
        "MiracastLuid" / Int64ul,
        "MiracastStartSessionStage" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1016, version=0)
class Microsoft_Windows_DxgKrnl_1016_0(Etw):
    pattern = Struct(
        "MiracastLuid" / Int64ul,
        "MiracastStopSessionStage" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1017, version=0)
class Microsoft_Windows_DxgKrnl_1017_0(Etw):
    pattern = Struct(
        "MiracastLuid" / Int64ul,
        "MiracastDeviceState" / Int32ul,
        "MiracastDeviceStatus" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1018, version=0)
class Microsoft_Windows_DxgKrnl_1018_0(Etw):
    pattern = Struct(
        "MiracastLuid" / Int64ul,
        "VidPnTargetId" / Int32ul,
        "ChunkType" / Int32ul,
        "FrameNumber" / Int32ul,
        "PartNumber" / Int32ul,
        "ProcessingTime" / Int32ul,
        "EncodeRate" / Int32ul,
        "PrivateDataDriverSize" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1019, version=0)
class Microsoft_Windows_DxgKrnl_1019_0(Etw):
    pattern = Struct(
        "MiniportContext" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1020, version=0)
class Microsoft_Windows_DxgKrnl_1020_0(Etw):
    pattern = Struct(
        "MiracastLuid" / Int64ul,
        "hMiracastDeviceHandle" / Int64ul,
        "pMiracastCallbacks" / Int64ul,
        "ReturnStatus" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1021, version=0)
class Microsoft_Windows_DxgKrnl_1021_0(Etw):
    pattern = Struct(
        "MiracastLuid" / Int64ul,
        "hMiracastDeviceHandle" / Int64ul,
        "pMiracastCallbacks" / Int64ul,
        "ReturnStatus" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1022, version=0)
class Microsoft_Windows_DxgKrnl_1022_0(Etw):
    pattern = Struct(
        "MiracastLuid" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1023, version=0)
class Microsoft_Windows_DxgKrnl_1023_0(Etw):
    pattern = Struct(
        "MiracastLuid" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1024, version=0)
class Microsoft_Windows_DxgKrnl_1024_0(Etw):
    pattern = Struct(
        "MiracastLuid" / Int64ul,
        "CurrentBitRate" / Int64ul,
        "LocalMaxBitRate" / Int64ul,
        "RemoteMaxBitRate" / Int64ul,
        "MiracastSessionInfo" / Int32ul,
        "ReturnStatus" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1025, version=0)
class Microsoft_Windows_DxgKrnl_1025_0(Etw):
    pattern = Struct(
        "MiracastLuid" / Int64ul,
        "CurrentBitRate" / Int64ul,
        "LocalMaxBitRate" / Int64ul,
        "RemoteMaxBitRate" / Int64ul,
        "MiracastSessionInfo" / Int32ul,
        "ReturnStatus" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1026, version=0)
class Microsoft_Windows_DxgKrnl_1026_0(Etw):
    pattern = Struct(
        "MiracastLuid" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1027, version=0)
class Microsoft_Windows_DxgKrnl_1027_0(Etw):
    pattern = Struct(
        "MiracastLuid" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1028, version=0)
class Microsoft_Windows_DxgKrnl_1028_0(Etw):
    pattern = Struct(
        "MiracastLuid" / Int64ul,
        "InputBufferSize" / Int32ul,
        "OutputBufferSize" / Int32ul,
        "ReturnStatus" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1029, version=0)
class Microsoft_Windows_DxgKrnl_1029_0(Etw):
    pattern = Struct(
        "MiracastLuid" / Int64ul,
        "InputBufferSize" / Int32ul,
        "OutputBufferSize" / Int32ul,
        "ReturnStatus" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1030, version=0)
class Microsoft_Windows_DxgKrnl_1030_0(Etw):
    pattern = Struct(
        "MiracastLuid" / Int64ul,
        "MiracastSessionStatus" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1031, version=0)
class Microsoft_Windows_DxgKrnl_1031_0(Etw):
    pattern = Struct(
        "MiracastLuid" / Int64ul,
        "HardwareAccess" / Int8ul,
        "InputBufferSize" / Int32ul,
        "OutputBufferSize" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1032, version=0)
class Microsoft_Windows_DxgKrnl_1032_0(Etw):
    pattern = Struct(
        "MiracastLuid" / Int64ul,
        "TimeoutInMilliseconds" / Int32ul,
        "AdditionalWaitEventCount" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1033, version=0)
class Microsoft_Windows_DxgKrnl_1033_0(Etw):
    pattern = Struct(
        "MiracastLuid" / Int64ul,
        "ChunkType" / Int32ul,
        "FrameNumber" / Int32ul,
        "PartNumber" / Int32ul,
        "ProcessingTime" / Int32ul,
        "EncodeRate" / Int32ul,
        "PrivateDriverDataSize" / Int32ul,
        "OutstandingChunksToProcess" / Int32ul,
        "ReturnStatus" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1034, version=0)
class Microsoft_Windows_DxgKrnl_1034_0(Etw):
    pattern = Struct(
        "MiracastLuid" / Int64ul,
        "pfnDataRateNotify" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1035, version=0)
class Microsoft_Windows_DxgKrnl_1035_0(Etw):
    pattern = Struct(
        "MiracastLuid" / Int64ul,
        "ChunkType" / Int32ul,
        "FrameNumber" / Int32ul,
        "PartNumber" / Int32ul,
        "ProcessingTime" / Int32ul,
        "EncodeRate" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1036, version=0)
class Microsoft_Windows_DxgKrnl_1036_0(Etw):
    pattern = Struct(
        "MiracastLuid" / Int64ul,
        "FrameNumber" / Int32ul,
        "PartNumber" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1037, version=0)
class Microsoft_Windows_DxgKrnl_1037_0(Etw):
    pattern = Struct(
        "MiracastLuid" / Int64ul,
        "ProtocolEvent" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1038, version=0)
class Microsoft_Windows_DxgKrnl_1038_0(Etw):
    pattern = Struct(
        "MiracastLuid" / Int64ul,
        "IoControlCode" / Int32ul,
        "HardwareAccess" / Int8ul,
        "InputBufferSize" / Int32ul,
        "OutputBufferSize" / Int32ul,
        "ReturnStatus" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1039, version=0)
class Microsoft_Windows_DxgKrnl_1039_0(Etw):
    pattern = Struct(
        "MiracastLuid" / Int64ul,
        "IoControlCode" / Int32ul,
        "HardwareAccess" / Int8ul,
        "InputBufferSize" / Int32ul,
        "OutputBufferSize" / Int32ul,
        "ReturnStatus" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1040, version=0)
class Microsoft_Windows_DxgKrnl_1040_0(Etw):
    pattern = Struct(
        "MiracastLuid" / Int64ul,
        "ChunkType" / Int32ul,
        "FrameNumber" / Int32ul,
        "PartNumber" / Int32ul,
        "ProcessingTime" / Int32ul,
        "EncodeRate" / Int32ul,
        "PrivateDataDriverSize" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1041, version=0)
class Microsoft_Windows_DxgKrnl_1041_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "EncoderBitRate" / Int64ul,
        "CurrentMaxTxDataRate" / Int64ul,
        "FailedFrameCount" / Int64ul,
        "MultipleRetryFrameCount" / Int64ul,
        "RetriedFrameCount" / Int64ul,
        "TransmittedFrameCount" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1042, version=0)
class Microsoft_Windows_DxgKrnl_1042_0(Etw):
    pattern = Struct(
        "EncoderBitRate" / Int64ul,
        "MaxLocalRate" / Int64ul,
        "MaxRemoteRate" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1043, version=0)
class Microsoft_Windows_DxgKrnl_1043_0(Etw):
    pattern = Struct(
        "MiracastStartSessionFailPoint" / Int32ul,
        "StartSessionFailureCode" / Int32ul,
        "GraphicsDeviceId" / Int32ul,
        "SinkDeviceInformation" / WString
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1044, version=0)
class Microsoft_Windows_DxgKrnl_1044_0(Etw):
    pattern = Struct(
        "MiracastLuid" / Int64ul,
        "Step" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1045, version=0)
class Microsoft_Windows_DxgKrnl_1045_0(Etw):
    pattern = Struct(
        "StopSessionReason" / Int32ul,
        "StopSessionErrorCode" / Int32ul,
        "GraphicsDeviceId" / Int32ul,
        "SinkDeviceInformation" / WString
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1046, version=0)
class Microsoft_Windows_DxgKrnl_1046_0(Etw):
    pattern = Struct(
        "AssociationId" / Int32ul,
        "GraphicsDeviceId" / Int32ul,
        "SinkDeviceInformation" / WString
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1047, version=0)
class Microsoft_Windows_DxgKrnl_1047_0(Etw):
    pattern = Struct(
        "AssociationId" / Int32ul,
        "GraphicsDeviceId" / Int32ul,
        "SinkDeviceInformation" / WString
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1048, version=0)
class Microsoft_Windows_DxgKrnl_1048_0(Etw):
    pattern = Struct(
        "AssociationId" / Int32ul,
        "GraphicsDeviceId" / Int32ul,
        "SinkDeviceInformation" / WString
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1049, version=0)
class Microsoft_Windows_DxgKrnl_1049_0(Etw):
    pattern = Struct(
        "AssociationId" / Int32ul,
        "GraphicsDeviceId" / Int32ul,
        "SinkDeviceInformation" / WString
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1050, version=0)
class Microsoft_Windows_DxgKrnl_1050_0(Etw):
    pattern = Struct(
        "DroppedFrames" / Int32ul,
        "TotalFrames" / Int32ul,
        "GraphicsDeviceId" / Int32ul,
        "GraphicsDriverVersion" / WString,
        "SinkDeviceInformation" / WString
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1051, version=0)
class Microsoft_Windows_DxgKrnl_1051_0(Etw):
    pattern = Struct(
        "AverageFrameLatency" / Int32ul,
        "TotalFrames" / Int32ul,
        "GraphicsDeviceId" / Int32ul,
        "GraphicsDriverVersion" / WString
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1052, version=0)
class Microsoft_Windows_DxgKrnl_1052_0(Etw):
    pattern = Struct(
        "IFrameRequests" / Int32ul,
        "TotalFrames" / Int32ul,
        "GraphicsDeviceId" / Int32ul,
        "SinkDeviceInformation" / WString
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1053, version=0)
class Microsoft_Windows_DxgKrnl_1053_0(Etw):
    pattern = Struct(
        "GraphicsVendorId" / Int32ul,
        "GraphicsDeviceId" / Int32ul,
        "GraphicsDeviceDescription" / WString,
        "GraphicsDriverVersion" / WString,
        "SinkDeviceInformation" / WString,
        "TotalProcessedFrames" / Int32ul,
        "TotalDroppedFrames" / Int32ul,
        "TotalDriverProcessTime" / Int32ul,
        "TotalIFrameRequests" / Int32ul,
        "TotalDroppedFrameReports" / Int32ul,
        "MaxDroppedFramesInOneBucket" / Int32ul,
        "TotalIFrameRequestReports" / Int32ul,
        "MaxIFrameRequestsInOneBucket" / Int32ul,
        "TotalGraphicsLatencyReport" / Int32ul,
        "MaxIAverageGraphicsLatencyInOneBucket" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1054, version=0)
class Microsoft_Windows_DxgKrnl_1054_0(Etw):
    pattern = Struct(
        "MiracastLuid" / Int64ul,
        "FrameNumber" / Int32ul,
        "PartNumber" / Int32ul,
        "ViolationType" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1055, version=0)
class Microsoft_Windows_DxgKrnl_1055_0(Etw):
    pattern = Struct(
        "AssociationId" / Int32ul,
        "GraphicsDeviceId" / Int32ul,
        "SinkDeviceInformation" / WString
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1056, version=0)
class Microsoft_Windows_DxgKrnl_1056_0(Etw):
    pattern = Struct(
        "pSwapChain" / Int64ul,
        "Status" / Int32ul,
        "bProducer" / Int32sl,
        "hDevice" / Int32ul,
        "SurfaceCount" / Int32ul,
        "hBufferAvailableEvent" / Int64ul,
        "hNtSwapChain" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1057, version=0)
class Microsoft_Windows_DxgKrnl_1057_0(Etw):
    pattern = Struct(
        "pSwapChain" / Int64ul,
        "Status" / Int32ul,
        "bProducer" / Int32sl,
        "hDevice" / Int32ul,
        "hBufferAvailableEvent" / Int64ul,
        "hNtSwapChain" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1058, version=0)
class Microsoft_Windows_DxgKrnl_1058_0(Etw):
    pattern = Struct(
        "pSwapChain" / Int64ul,
        "SurfaceIdx" / Int32ul,
        "hVidMmAllocation" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1059, version=0)
class Microsoft_Windows_DxgKrnl_1059_0(Etw):
    pattern = Struct(
        "pSwapChain" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1060, version=0)
class Microsoft_Windows_DxgKrnl_1060_0(Etw):
    pattern = Struct(
        "pSwapChain" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1061, version=0)
class Microsoft_Windows_DxgKrnl_1061_0(Etw):
    pattern = Struct(
        "pSwapChain" / Int64ul,
        "ProducerEventSignaled" / Int64ul,
        "ClientEventSignaled" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1062, version=0)
class Microsoft_Windows_DxgKrnl_1062_0(Etw):
    pattern = Struct(
        "pSwapChain" / Int64ul,
        "Status" / Int32ul,
        "bProducer" / Int32sl,
        "bReleaseBeforeAcquire" / Int32sl,
        "AcquiredBufferIdx" / Int32ul,
        "AcquireMetadataSize" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1063, version=0)
class Microsoft_Windows_DxgKrnl_1063_0(Etw):
    pattern = Struct(
        "pSwapChain" / Int64ul,
        "Status" / Int32ul,
        "bProducer" / Int32sl,
        "MetadataSize" / Int32ul,
        "EventSignaled" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1064, version=0)
class Microsoft_Windows_DxgKrnl_1064_0(Etw):
    pattern = Struct(
        "pSwapChain" / Int64ul,
        "Status" / Int32ul,
        "bProducer" / Int32sl,
        "bGlobal" / Int32sl,
        "DataCopied" / Int32ul,
        "MetaDataDword1" / Int32ul,
        "MetaDataDword2" / Int32ul,
        "MetaDataDword3" / Int32ul,
        "MetaDataDword4" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1065, version=0)
class Microsoft_Windows_DxgKrnl_1065_0(Etw):
    pattern = Struct(
        "pSwapChain" / Int64ul,
        "Status" / Int32ul,
        "bProducer" / Int32sl,
        "bGlobal" / Int32sl,
        "DataCopied" / Int32ul,
        "MetaDataDword1" / Int32ul,
        "MetaDataDword2" / Int32ul,
        "MetaDataDword3" / Int32ul,
        "MetaDataDword4" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1066, version=0)
class Microsoft_Windows_DxgKrnl_1066_0(Etw):
    pattern = Struct(
        "PresentCount" / Int32sl,
        "PresentRefreshCount" / Int32sl,
        "SyncRefreshCount" / Int32sl,
        "SyncQPCTime" / Int64sl
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1067, version=0)
class Microsoft_Windows_DxgKrnl_1067_0(Etw):
    pattern = Struct(
        "UpdateLocation" / Int32ul,
        "CurRefreshCount" / Int64sl,
        "LastVSyncTime" / Int64sl,
        "LastVSyncTimeSnapped" / Int64sl
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1068, version=0)
class Microsoft_Windows_DxgKrnl_1068_0(Etw):
    pattern = Struct(
        "FrameNumber" / Int32sl,
        "FrameDisplayTime" / Int64sl,
        "PresentOnVSyncCount" / Int32sl
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1069, version=1)
class Microsoft_Windows_DxgKrnl_1069_1(Etw):
    pattern = Struct(
        "pSyncObject" / Int64ul,
        "KMTHandle" / Int64ul,
        "pDxgDevice" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1070, version=1)
class Microsoft_Windows_DxgKrnl_1070_1(Etw):
    pattern = Struct(
        "pSyncObject" / Int64ul,
        "KMTHandle" / Int64ul,
        "pDxgDevice" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1071, version=0)
class Microsoft_Windows_DxgKrnl_1071_0(Etw):
    pattern = Struct(
        "FrameNumber" / Int32sl,
        "FrontOfQueue" / Int8ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1072, version=0)
class Microsoft_Windows_DxgKrnl_1072_0(Etw):
    pattern = Struct(
        "FrameNumber" / Int32sl,
        "FrontOfQueue" / Int8ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1073, version=0)
class Microsoft_Windows_DxgKrnl_1073_0(Etw):
    pattern = Struct(
        "ContextPtr" / Int64ul,
        "hAdapter" / Int64ul,
        "VidPnSourceId" / Int32ul,
        "KeyedMutexCount" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1074, version=0)
class Microsoft_Windows_DxgKrnl_1074_0(Etw):
    pattern = Struct(
        "ContextPtr" / Int64ul,
        "KeyedMutexIdx" / Int32ul,
        "LastPresentTime" / Int64ul,
        "LastMouseUpdateTime" / Int64ul,
        "AccumulatedFrames" / Int32ul,
        "RectsCoalesced" / Int8ul,
        "ProtectedContentMaskedOut" / Int8ul,
        "TotalMetadataBufferSize" / Int32ul,
        "PointerShapeBufferSize" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1075, version=0)
class Microsoft_Windows_DxgKrnl_1075_0(Etw):
    pattern = Struct(
        "ContextPtr" / Int64ul,
        "KeyedMutexIdx" / Int32ul,
        "PresentUpdateStatusCurrent" / Int32ul,
        "bAccumulatedFrameUpdated" / Int8ul,
        "bKeyMutexTriggered" / Int8ul,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1076, version=0)
class Microsoft_Windows_DxgKrnl_1076_0(Etw):
    pattern = Struct(
        "ContextPtr" / Int64ul,
        "KeyedMutexIdx" / Int32ul,
        "UpdateType" / Int32ul,
        "PresentUpdateStatusCurrent" / Int32ul,
        "AccumulatedFrames" / Int32ul,
        "PresentUpdateStatusAccumulated" / Int32ul,
        "bAcquiredMutex" / Int8ul,
        "bConsumerAcquired" / Int8ul,
        "bConsumerDeviceStillProcessingFrame" / Int8ul,
        "bNewUpdateReady" / Int8ul,
        "bAccumulatedFrameUpdated" / Int8ul,
        "bMovedCurrentPresentsToAccumulated" / Int8ul,
        "bKeyedMutexReleasedToConsumer" / Int8ul,
        "bUsedGdiRgn" / Int8ul,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1077, version=0)
class Microsoft_Windows_DxgKrnl_1077_0(Etw):
    pattern = Struct(
        "ContextPtr" / Int64ul,
        "KeyedMutexIdx" / Int32ul,
        "hSrc" / Int64ul,
        "hDst" / Int64ul,
        "BltRectCounts" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1078, version=0)
class Microsoft_Windows_DxgKrnl_1078_0(Etw):
    pattern = Struct(
        "ContextPtr" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1079, version=0)
class Microsoft_Windows_DxgKrnl_1079_0(Etw):
    pattern = Struct(
        "MiniportDeviceContext" / Int64ul,
        "RedirectedForIndirectDisplay" / Int8ul,
        "CertificateType" / Int32ul,
        "CertificateSize" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1080, version=0)
class Microsoft_Windows_DxgKrnl_1080_0(Etw):
    pattern = Struct(
        "MiniportDeviceContext" / Int64ul,
        "RedirectedForIndirectDisplay" / Int8ul,
        "CertificateType" / Int32ul,
        "CertificateSize" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1081, version=0)
class Microsoft_Windows_DxgKrnl_1081_0(Etw):
    pattern = Struct(
        "MiniportDeviceContext" / Int64ul,
        "RedirectedForIndirectDisplay" / Int8ul,
        "VidPnTargetId" / Int32ul,
        "DriverProtectedOutputHandle" / Int64ul,
        "ExternalProtectedOutputHandle" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1082, version=0)
class Microsoft_Windows_DxgKrnl_1082_0(Etw):
    pattern = Struct(
        "MiniportDeviceContext" / Int64ul,
        "RedirectedForIndirectDisplay" / Int8ul,
        "DriverProtectedOutputHandle" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1083, version=0)
class Microsoft_Windows_DxgKrnl_1083_0(Etw):
    pattern = Struct(
        "MiniportDeviceContext" / Int64ul,
        "RedirectedForIndirectDisplay" / Int8ul,
        "DriverProtectedOutputHandle" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1084, version=0)
class Microsoft_Windows_DxgKrnl_1084_0(Etw):
    pattern = Struct(
        "MiniportDeviceContext" / Int64ul,
        "RedirectedForIndirectDisplay" / Int8ul,
        "DriverProtectedOutputHandle" / Int64ul,
        "InformationGuid" / Guid,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1085, version=0)
class Microsoft_Windows_DxgKrnl_1085_0(Etw):
    pattern = Struct(
        "MiniportDeviceContext" / Int64ul,
        "RedirectedForIndirectDisplay" / Int8ul,
        "DriverProtectedOutputHandle" / Int64ul,
        "InformationGuid" / Guid,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1086, version=0)
class Microsoft_Windows_DxgKrnl_1086_0(Etw):
    pattern = Struct(
        "MiniportDeviceContext" / Int64ul,
        "RedirectedForIndirectDisplay" / Int8ul,
        "DriverProtectedOutputHandle" / Int64ul,
        "SettingGuid" / Guid,
        "AdditionalParametersSize" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1087, version=0)
class Microsoft_Windows_DxgKrnl_1087_0(Etw):
    pattern = Struct(
        "MiniportDeviceContext" / Int64ul,
        "RedirectedForIndirectDisplay" / Int8ul,
        "DriverProtectedOutputHandle" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1088, version=0)
class Microsoft_Windows_DxgKrnl_1088_0(Etw):
    pattern = Struct(
        "MiniportDeviceContext" / Int64ul,
        "RedirectedForIndirectDisplay" / Int8ul,
        "DriverProtectedOutputHandle" / Int64ul,
        "ProtectionType" / Int32ul,
        "ProtectionLevel" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1089, version=0)
class Microsoft_Windows_DxgKrnl_1089_0(Etw):
    pattern = Struct(
        "MiniportDeviceContext" / Int64ul,
        "RedirectedForIndirectDisplay" / Int8ul,
        "DriverProtectedOutputHandle" / Int64ul,
        "ConnectorType" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1090, version=0)
class Microsoft_Windows_DxgKrnl_1090_0(Etw):
    pattern = Struct(
        "MiniportDeviceContext" / Int64ul,
        "RedirectedForIndirectDisplay" / Int8ul,
        "DriverProtectedOutputHandle" / Int64ul,
        "SupportedProtectionTypes" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1091, version=0)
class Microsoft_Windows_DxgKrnl_1091_0(Etw):
    pattern = Struct(
        "MiniportDeviceContext" / Int64ul,
        "RedirectedForIndirectDisplay" / Int8ul,
        "DriverProtectedOutputHandle" / Int64ul,
        "ProtectionType" / Int32ul,
        "ProtectionLevel" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1092, version=0)
class Microsoft_Windows_DxgKrnl_1092_0(Etw):
    pattern = Struct(
        "pDxgAdapter" / Int64ul,
        "VidPnSourceId" / Int32ul,
        "Visible" / Int8ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1093, version=0)
class Microsoft_Windows_DxgKrnl_1093_0(Etw):
    pattern = Struct(
        "AdapterLuid" / Int64ul,
        "DisableD3Requests" / Int8ul,
        "GetMiniportStatus" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1094, version=0)
class Microsoft_Windows_DxgKrnl_1094_0(Etw):
    pattern = Struct(
        "MiniportDeviceContext" / Int64ul,
        "Flags" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1095, version=0)
class Microsoft_Windows_DxgKrnl_1095_0(Etw):
    pattern = Struct(
        "MiniportDeviceContext" / Int64ul,
        "Flags" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1096, version=0)
class Microsoft_Windows_DxgKrnl_1096_0(Etw):
    pattern = Struct(
        "MiniportDeviceContext" / Int64ul,
        "Type" / Int32ul,
        "TargetId" / Int32ul,
        "NonDestructiveOnly" / Int8ul,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1097, version=0)
class Microsoft_Windows_DxgKrnl_1097_0(Etw):
    pattern = Struct(
        "MiniportDeviceContext" / Int64ul,
        "Type" / Int32ul,
        "TargetId" / Int32ul,
        "NonDestructiveOnly" / Int8ul,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1098, version=0)
class Microsoft_Windows_DxgKrnl_1098_0(Etw):
    pattern = Struct(
        "MiniportDeviceContext" / Int64ul,
        "ConnectionChangeId" / Int64ul,
        "TargetId" / Int32ul,
        "ConnectionStatus" / Int32ul,
        "TargetType" / Int32ul,
        "NewTargetId" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1099, version=0)
class Microsoft_Windows_DxgKrnl_1099_0(Etw):
    pattern = Struct(
        "MiniportDeviceContext" / Int64ul,
        "ConnectionChangeId" / Int64ul,
        "TargetId" / Int32ul,
        "ConnectionStatus" / Int32ul,
        "TargetType" / Int32ul,
        "NewTargetId" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1100, version=0)
class Microsoft_Windows_DxgKrnl_1100_0(Etw):
    pattern = Struct(
        "DxgAdapter" / Int64ul,
        "Exclusive" / Int8ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1101, version=0)
class Microsoft_Windows_DxgKrnl_1101_0(Etw):
    pattern = Struct(
        "DxgAdapter" / Int64ul,
        "Acquired" / Int8ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1102, version=0)
class Microsoft_Windows_DxgKrnl_1102_0(Etw):
    pattern = Struct(
        "DxgAdapter" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1103, version=0)
class Microsoft_Windows_DxgKrnl_1103_0(Etw):
    pattern = Struct(
        "MiniportDeviceContext" / Int64ul,
        "TargetId" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1104, version=0)
class Microsoft_Windows_DxgKrnl_1104_0(Etw):
    pattern = Struct(
        "MiniportDeviceContext" / Int64ul,
        "TargetId" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1105, version=0)
class Microsoft_Windows_DxgKrnl_1105_0(Etw):
    pattern = Struct(
        "hSyncObj" / Int32ul,
        "VidPnSourceId" / Int32ul,
        "hCompSurface" / Int64ul,
        "CompSurfaceLuid" / Int64ul,
        "Flags" / Int32ul,
        "ReturnStatus" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1106, version=0)
class Microsoft_Windows_DxgKrnl_1106_0(Etw):
    pattern = Struct(
        "VidMmSegment" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1107, version=0)
class Microsoft_Windows_DxgKrnl_1107_0(Etw):
    pattern = Struct(
        "VidMmSegment" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1108, version=0)
class Microsoft_Windows_DxgKrnl_1108_0(Etw):
    pattern = Struct(
        "VidMmGlobalAlloc" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1109, version=0)
class Microsoft_Windows_DxgKrnl_1109_0(Etw):
    pattern = Struct(
        "VidMmGlobalAlloc" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1110, version=0)
class Microsoft_Windows_DxgKrnl_1110_0(Etw):
    pattern = Struct(
        "pSwapChain" / Int64ul,
        "Status" / Int32ul,
        "bProducer" / Int32ul,
        "hSurface" / Int64ul,
        "SurfaceIdx" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1111, version=0)
class Microsoft_Windows_DxgKrnl_1111_0(Etw):
    pattern = Struct(
        "pSwapChain" / Int64ul,
        "Status" / Int32ul,
        "bProducer" / Int32ul,
        "hSurface" / Int64ul,
        "SurfaceIdx" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1112, version=0)
class Microsoft_Windows_DxgKrnl_1112_0(Etw):
    pattern = Struct(
        "pSwapChain" / Int64ul,
        "Status" / Int32ul,
        "bProducer" / Int32ul,
        "hSurface" / Int64ul,
        "SurfaceIdx" / Int32ul,
        "MetadataSize" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1113, version=0)
class Microsoft_Windows_DxgKrnl_1113_0(Etw):
    pattern = Struct(
        "Entry" / Int32ul,
        "Activation" / Int32ul,
        "ProcessName" / CString,
        "Reason" / WString
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1114, version=0)
class Microsoft_Windows_DxgKrnl_1114_0(Etw):
    pattern = Struct(
        "Entry" / Int32ul,
        "Activation" / Int32ul,
        "DAM" / Int32ul,
        "ProcessName" / CString,
        "Reason" / WString,
        "TimeInMS" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=1117, version=0)
class Microsoft_Windows_DxgKrnl_1117_0(Etw):
    pattern = Struct(
        "Entry" / Int32ul,
        "Activation" / Int32ul,
        "DAM" / Int32ul,
        "ProcessName" / CString,
        "Reason" / WString,
        "TimeInMS" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=10000, version=0)
class Microsoft_Windows_DxgKrnl_10000_0(Etw):
    pattern = Struct(
        "PerfTrack_Uniqueness_Id" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=10001, version=0)
class Microsoft_Windows_DxgKrnl_10001_0(Etw):
    pattern = Struct(
        "PerfTrack_Uniqueness_Id" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=10002, version=0)
class Microsoft_Windows_DxgKrnl_10002_0(Etw):
    pattern = Struct(
        "PerfTrack_Uniqueness_Id" / Int32ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=10010, version=0)
class Microsoft_Windows_DxgKrnl_10010_0(Etw):
    pattern = Struct(
        "Misc_ActiveVidPnBasedDisplayModeListSizeSum" / Int64ul,
        "Misc_UniqueModesFromUnionListSizeSum" / Int64ul,
        "CallCount_GetUniqueModesFromUnionList" / Int32ul,
        "CallCount_DXGADAPTER_DdiEnumVidPnCofuncModality" / Int32ul,
        "CallCount_DXGK_VIDPNSOURCEMODESET_INTERFACE_V1_IMPL_AcquirePinnedModeInfo" / Int32ul,
        "CallCount_DXGK_VIDPNSOURCEMODESET_INTERFACE_V1_IMPL_CreateNewModeInfo" / Int32ul,
        "CallCount_DXGK_VIDPNTARGETMODESET_INTERFACE_V1_IMPL_AcquirePinnedModeInfo" / Int32ul,
        "CallCount_DXGK_VIDPNTARGETMODESET_INTERFACE_V1_IMPL_CreateNewModeInfo" / Int32ul,
        "CallCount_DXGK_VIDPNTOPOLOGY_INTERFACE_V1_IMPL_AcquireFirstPathInfo" / Int32ul,
        "CallCount_DXGK_VIDPNTOPOLOGY_INTERFACE_V1_IMPL_AcquireNextPathInfo" / Int32ul,
        "TickCount_GetUniqueModesFromUnionList" / Int64ul
    )


@declare(guid=guid("802ec45a-1e99-4b83-9920-87c98277ba9d"), event_id=10011, version=0)
class Microsoft_Windows_DxgKrnl_10011_0(Etw):
    pattern = Struct(
        "Type" / Int32ul,
        "Source" / Int64ul
    )

