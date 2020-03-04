# -*- coding: utf-8 -*-
"""
Microsoft-Windows-DXGI
GUID : ca11c036-0102-4a2d-a6ad-f03cfed5d3c9
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=1, version=0)
class Microsoft_Windows_DXGI_1_0(Etw):
    pattern = Struct(
        "pIDXGIFactory" / Int64ul,
        "Mode" / Int32ul,
        "BlockedAdapters" / Int32ul,
        "PnPID" / WString,
        "DriverVersion" / WString
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=2, version=0)
class Microsoft_Windows_DXGI_2_0(Etw):
    pattern = Struct(
        "pIDXGIFactory" / Int64ul,
        "Mode" / Int32ul,
        "BlockedAdapters" / Int32ul,
        "PnPID" / WString,
        "DriverVersion" / WString
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=3, version=0)
class Microsoft_Windows_DXGI_3_0(Etw):
    pattern = Struct(
        "pIDXGIFactory" / Int64ul,
        "Mode" / Int32ul,
        "BlockedAdapters" / Int32ul,
        "PnPID" / WString,
        "DriverVersion" / WString
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=4, version=0)
class Microsoft_Windows_DXGI_4_0(Etw):
    pattern = Struct(
        "pIDXGIAdapter" / Int64ul,
        "pIDXGIFactory" / Int64ul,
        "KMTAdapterHandle" / Int32ul,
        "ThunkDLLHandle" / Int64ul,
        "SharedResources" / Int8ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=5, version=0)
class Microsoft_Windows_DXGI_5_0(Etw):
    pattern = Struct(
        "pIDXGIAdapter" / Int64ul,
        "pIDXGIFactory" / Int64ul,
        "KMTAdapterHandle" / Int32ul,
        "ThunkDLLHandle" / Int64ul,
        "SharedResources" / Int8ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=6, version=0)
class Microsoft_Windows_DXGI_6_0(Etw):
    pattern = Struct(
        "pIDXGIAdapter" / Int64ul,
        "pIDXGIFactory" / Int64ul,
        "KMTAdapterHandle" / Int32ul,
        "ThunkDLLHandle" / Int64ul,
        "SharedResources" / Int8ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=7, version=0)
class Microsoft_Windows_DXGI_7_0(Etw):
    pattern = Struct(
        "pIDXGIOutput" / Int64ul,
        "pIDXGIAdapter" / Int64ul,
        "VidPnSourceID" / Int32ul,
        "GDIDeviceName" / WString
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=8, version=0)
class Microsoft_Windows_DXGI_8_0(Etw):
    pattern = Struct(
        "pIDXGIOutput" / Int64ul,
        "pIDXGIAdapter" / Int64ul,
        "VidPnSourceID" / Int32ul,
        "GDIDeviceName" / WString
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=9, version=0)
class Microsoft_Windows_DXGI_9_0(Etw):
    pattern = Struct(
        "pIDXGIOutput" / Int64ul,
        "pIDXGIAdapter" / Int64ul,
        "VidPnSourceID" / Int32ul,
        "GDIDeviceName" / WString
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=10, version=0)
class Microsoft_Windows_DXGI_10_0(Etw):
    pattern = Struct(
        "pIDXGISwapChain" / Int64ul,
        "pIDXGIFactory" / Int64ul,
        "pIDXGIDevice" / Int64ul,
        "pIDXGIOutput" / Int64ul,
        "UserBackbufferCount" / Int8ul,
        "BackbufferCount" / Int8ul,
        "ppBackBuffers" / Int64ul,
        "pPrimary" / Int64ul,
        "pProxyPrimary" / Int64ul,
        "Width" / Int32ul,
        "Height" / Int32ul,
        "RefreshNumerator" / Int32ul,
        "RefreshDenominator" / Int32ul,
        "Format" / Int32ul,
        "ScanlineOrdering" / Int32ul,
        "Scaling" / Int32ul,
        "SampleCount" / Int32ul,
        "SampleQuality" / Int32ul,
        "Usage" / Int32ul,
        "OutputWindow" / Int64ul,
        "Windowed" / Int8ul,
        "SwapEffect" / Int32ul,
        "Flags" / Int32ul,
        "Redirected" / Int8ul,
        "LogicalSurfaceHandle" / Int64ul,
        "BindId" / Int64ul,
        "BackbufferHandles" / Int64ul,
        "BackbufferEventHandles" / Int64ul,
        "FenceHandle" / Int64ul,
        "FenceValue" / Int64ul,
        "ActualBufferCount" / Int8ul,
        "ActualSwapEffect" / Int32ul,
        "WinFlipProxyBufferCount" / Int8ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=11, version=0)
class Microsoft_Windows_DXGI_11_0(Etw):
    pattern = Struct(
        "pIDXGISwapChain" / Int64ul,
        "pIDXGIFactory" / Int64ul,
        "pIDXGIDevice" / Int64ul,
        "pIDXGIOutput" / Int64ul,
        "UserBackbufferCount" / Int8ul,
        "BackbufferCount" / Int8ul,
        "ppBackBuffers" / Int64ul,
        "pPrimary" / Int64ul,
        "pProxyPrimary" / Int64ul,
        "Width" / Int32ul,
        "Height" / Int32ul,
        "RefreshNumerator" / Int32ul,
        "RefreshDenominator" / Int32ul,
        "Format" / Int32ul,
        "ScanlineOrdering" / Int32ul,
        "Scaling" / Int32ul,
        "SampleCount" / Int32ul,
        "SampleQuality" / Int32ul,
        "Usage" / Int32ul,
        "OutputWindow" / Int64ul,
        "Windowed" / Int8ul,
        "SwapEffect" / Int32ul,
        "Flags" / Int32ul,
        "Redirected" / Int8ul,
        "LogicalSurfaceHandle" / Int64ul,
        "BindId" / Int64ul,
        "BackbufferHandles" / Int64ul,
        "BackbufferEventHandles" / Int64ul,
        "FenceHandle" / Int64ul,
        "FenceValue" / Int64ul,
        "ActualBufferCount" / Int8ul,
        "ActualSwapEffect" / Int32ul,
        "WinFlipProxyBufferCount" / Int8ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=12, version=0)
class Microsoft_Windows_DXGI_12_0(Etw):
    pattern = Struct(
        "pIDXGISwapChain" / Int64ul,
        "pIDXGIFactory" / Int64ul,
        "pIDXGIDevice" / Int64ul,
        "pIDXGIOutput" / Int64ul,
        "UserBackbufferCount" / Int8ul,
        "BackbufferCount" / Int8ul,
        "ppBackBuffers" / Int64ul,
        "pPrimary" / Int64ul,
        "pProxyPrimary" / Int64ul,
        "Width" / Int32ul,
        "Height" / Int32ul,
        "RefreshNumerator" / Int32ul,
        "RefreshDenominator" / Int32ul,
        "Format" / Int32ul,
        "ScanlineOrdering" / Int32ul,
        "Scaling" / Int32ul,
        "SampleCount" / Int32ul,
        "SampleQuality" / Int32ul,
        "Usage" / Int32ul,
        "OutputWindow" / Int64ul,
        "Windowed" / Int8ul,
        "SwapEffect" / Int32ul,
        "Flags" / Int32ul,
        "Redirected" / Int8ul,
        "LogicalSurfaceHandle" / Int64ul,
        "BindId" / Int64ul,
        "BackbufferHandles" / Int64ul,
        "BackbufferEventHandles" / Int64ul,
        "FenceHandle" / Int64ul,
        "FenceValue" / Int64ul,
        "ActualBufferCount" / Int8ul,
        "ActualSwapEffect" / Int32ul,
        "WinFlipProxyBufferCount" / Int8ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=40, version=0)
class Microsoft_Windows_DXGI_40_0(Etw):
    pattern = Struct(
        "Event" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=41, version=0)
class Microsoft_Windows_DXGI_41_0(Etw):
    pattern = Struct(
        "Event" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=42, version=0)
class Microsoft_Windows_DXGI_42_0(Etw):
    pattern = Struct(
        "pIDXGISwapChain" / Int64ul,
        "Flags" / Int32ul,
        "SyncInterval" / Int32ul,
        "DirtyRects" / Int32ul,
        "ScrollRects" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=43, version=0)
class Microsoft_Windows_DXGI_43_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=44, version=0)
class Microsoft_Windows_DXGI_44_0(Etw):
    pattern = Struct(
        "ReturnValue" / Int32ul,
        "PresentCount" / Int32ul,
        "PresentRefreshCount" / Int32ul,
        "SyncRefreshCount" / Int32ul,
        "SyncQPCTime" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=45, version=0)
class Microsoft_Windows_DXGI_45_0(Etw):
    pattern = Struct(
        "pIDXGISwapchain" / Int64ul,
        "OldUserBackbufferCount" / Int8ul,
        "OldBackbufferCount" / Int8ul,
        "ppOldBackBuffers" / Int64ul,
        "pOldPrimary" / Int64ul,
        "pOldProxyPrimary" / Int64ul,
        "OldWidth" / Int32ul,
        "OldHeight" / Int32ul,
        "OldFormat" / Int32ul,
        "OldFlags" / Int32ul,
        "OldRedirected" / Int8ul,
        "OldLogicalSurfaceHandle" / Int64ul,
        "OldBackbufferHandles" / Int64ul,
        "OldFenceHandle" / Int64ul,
        "OldFenceValue" / Int64ul,
        "OldActualbufferCount" / Int8ul,
        "OldWinFlipProxyBufferCount" / Int8ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=46, version=0)
class Microsoft_Windows_DXGI_46_0(Etw):
    pattern = Struct(
        "pIDXGISwapChain" / Int64ul,
        "ReturnValue" / Int32ul,
        "NewUserBackbufferCount" / Int8ul,
        "NewBackbufferCount" / Int8ul,
        "ppNewBackBuffers" / Int64ul,
        "pNewPrimary" / Int64ul,
        "pNewProxyPrimary" / Int64ul,
        "NewWidth" / Int32ul,
        "NewHeight" / Int32ul,
        "NewFormat" / Int32ul,
        "NewFlags" / Int32ul,
        "NewRedirected" / Int8ul,
        "NewLogicalSurfaceHandle" / Int64ul,
        "NewBackbufferHandles" / Int64ul,
        "NewFenceHandle" / Int64ul,
        "NewFenceValue" / Int64ul,
        "NewActualbufferCount" / Int8ul,
        "NewWinFlipProxyBufferCount" / Int8ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=47, version=0)
class Microsoft_Windows_DXGI_47_0(Etw):
    pattern = Struct(
        "pDXGISwapChain" / Int64ul,
        "Width" / Int32ul,
        "Height" / Int32ul,
        "RefreshNumerator" / Int32ul,
        "RefreshDenominator" / Int32ul,
        "Format" / Int32ul,
        "ScanlineOrdering" / Int32ul,
        "Scaling" / Int32ul,
        "Windowed" / Int8ul,
        "pOldPrimary" / Int64ul,
        "pOldProxyPrimary" / Int64ul,
        "OldWinFlipProxyBufferCount" / Int8ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=48, version=0)
class Microsoft_Windows_DXGI_48_0(Etw):
    pattern = Struct(
        "pIDXGISwapChain" / Int64ul,
        "ReturnValue" / Int32ul,
        "pNewPrimary" / Int64ul,
        "pNewProxyPrimary" / Int64ul,
        "NewWinFlipProxyBufferCount" / Int8ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=49, version=0)
class Microsoft_Windows_DXGI_49_0(Etw):
    pattern = Struct(
        "pIDXGISwapChain" / Int64ul,
        "OldWindowed" / Int8ul,
        "pOldOutput" / Int64ul,
        "pOldPrimary" / Int64ul,
        "pOldProxyPrimary" / Int64ul,
        "OldWinFlipProxyBufferCount" / Int8ul,
        "OldSwapEffect" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=50, version=0)
class Microsoft_Windows_DXGI_50_0(Etw):
    pattern = Struct(
        "pIDXGISwapChain" / Int64ul,
        "ReturnValue" / Int32ul,
        "NewWindowed" / Int8ul,
        "pNewOutput" / Int64ul,
        "pNewPrimary" / Int64ul,
        "pNewProxyPrimary" / Int64ul,
        "NewWinFlipProxyBufferCount" / Int8ul,
        "NewSwapEffect" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=51, version=0)
class Microsoft_Windows_DXGI_51_0(Etw):
    pattern = Struct(
        "pIDXGIOutput" / Int64ul,
        "WidthToMatch" / Int32ul,
        "HeightToMatch" / Int32ul,
        "RefreshNumeratorToMatch" / Int32ul,
        "RefreshDenominatorToMatch" / Int32ul,
        "FormatToMatch" / Int32ul,
        "ScanlineOrderingToMatch" / Int32ul,
        "ScalingToMatch" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=52, version=0)
class Microsoft_Windows_DXGI_52_0(Etw):
    pattern = Struct(
        "pIDXGIOutput" / Int64ul,
        "ReturnValue" / Int32ul,
        "WidthResult" / Int32ul,
        "HeightResult" / Int32ul,
        "RefreshNumeratorResult" / Int32ul,
        "RefreshDenominatorResult" / Int32ul,
        "FormatResult" / Int32ul,
        "ScanlineOrderingResult" / Int32ul,
        "ScalingResult" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=53, version=0)
class Microsoft_Windows_DXGI_53_0(Etw):
    pattern = Struct(
        "pIDXGISwapChain" / Int64ul,
        "NewRedirected" / Int8ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=54, version=0)
class Microsoft_Windows_DXGI_54_0(Etw):
    pattern = Struct(
        "pIDXGISwapChain" / Int64ul,
        "BackBufferNumber" / Int32ul,
        "BackBufferHandle" / Int64ul,
        "BackBufferEventHandle" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=55, version=0)
class Microsoft_Windows_DXGI_55_0(Etw):
    pattern = Struct(
        "pIDXGISwapChain" / Int64ul,
        "Flags" / Int32ul,
        "SyncInterval" / Int32ul,
        "NumPlanes" / Int32ul,
        "LayerMask" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=56, version=0)
class Microsoft_Windows_DXGI_56_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=57, version=0)
class Microsoft_Windows_DXGI_57_0(Etw):
    pattern = Struct(
        "pIDXGISwapChain" / Int64ul,
        "NumPlanes" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=58, version=0)
class Microsoft_Windows_DXGI_58_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=59, version=0)
class Microsoft_Windows_DXGI_59_0(Etw):
    pattern = Struct(
        "pIDXGIOutput" / Int64ul,
        "MaxPlanes" / Int32ul,
        "OverlayMaxRGBPlanes" / Int32ul,
        "OverlayMaxYUVPlanes" / Int32ul,
        "OverlayCaps" / Int32ul,
        "PanelFitterMaxRGBPlanes" / Int32ul,
        "PanelFitterCaps" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=60, version=0)
class Microsoft_Windows_DXGI_60_0(Etw):
    pattern = Struct(
        "pIDXGISwapChain" / Int64ul,
        "LayerIndex" / Int32ul,
        "Enabled" / Int8ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=61, version=0)
class Microsoft_Windows_DXGI_61_0(Etw):
    pattern = Struct(
        "pIDXGISwapChain" / Int64ul,
        "KernelSupport" / Int8ul,
        "DriverFailed" / Int8ul,
        "InvalidParam" / Int8ul,
        "NumPlanes" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=62, version=0)
class Microsoft_Windows_DXGI_62_0(Etw):
    pattern = Struct(
        "pIDXGISwapChain" / Int64ul,
        "hResource" / Int64ul,
        "SubResourceIndex" / Int32ul,
        "Flags" / Int32ul,
        "SrcRectleft" / Int32ul,
        "SrcRectright" / Int32ul,
        "SrcRecttop" / Int32ul,
        "SrcRectbottom" / Int32ul,
        "DstRectleft" / Int32ul,
        "DstRectright" / Int32ul,
        "DstRecttop" / Int32ul,
        "DstRectbottom" / Int32ul,
        "ClipRectleft" / Int32ul,
        "ClipRectright" / Int32ul,
        "ClipRecttop" / Int32ul,
        "ClipRectbottom" / Int32ul,
        "Blend" / Int32ul,
        "ColorSpace" / Int32ul,
        "StretchQuality" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=63, version=0)
class Microsoft_Windows_DXGI_63_0(Etw):
    pattern = Struct(
        "pIDXGISwapChain" / Int64ul,
        "Width" / Int32ul,
        "Height" / Int32ul,
        "DXGIFormat" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=64, version=0)
class Microsoft_Windows_DXGI_64_0(Etw):
    pattern = Struct(
        "pIDXGISwapChain" / Int64ul,
        "Enabled" / Int8ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=65, version=0)
class Microsoft_Windows_DXGI_65_0(Etw):
    pattern = Struct(
        "pIDXGISwapChain" / Int64ul,
        "Enabled" / Int8ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=66, version=0)
class Microsoft_Windows_DXGI_66_0(Etw):
    pattern = Struct(
        "pIDXGISwapChain" / Int64ul,
        "Enabled" / Int8ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=67, version=0)
class Microsoft_Windows_DXGI_67_0(Etw):
    pattern = Struct(
        "pIDXGISwapchain" / Int64ul,
        "Result" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=68, version=0)
class Microsoft_Windows_DXGI_68_0(Etw):
    pattern = Struct(
        "pIDXGIOutput" / Int64ul,
        "Format" / Int32ul,
        "ColorSpace" / Int32ul,
        "OutputFlags" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=69, version=0)
class Microsoft_Windows_DXGI_69_0(Etw):
    pattern = Struct(
        "pIDXGISwapchain" / Int64ul,
        "ColorSpace" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=70, version=0)
class Microsoft_Windows_DXGI_70_0(Etw):
    pattern = Struct(
        "Index" / Int32ul,
        "Code" / Int32ul,
        "ThreadId" / Int32ul,
        "Message" / CString
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=71, version=0)
class Microsoft_Windows_DXGI_71_0(Etw):
    pattern = Struct(
        "pIDXGISwapchain" / Int64ul,
        "BackbufferCount" / Int8ul,
        "BackbufferHandles" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=72, version=0)
class Microsoft_Windows_DXGI_72_0(Etw):
    pattern = Struct(
        "pIDXGISwapchain" / Int64ul,
        "KeepExistingContent" / Int8ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=73, version=0)
class Microsoft_Windows_DXGI_73_0(Etw):
    pattern = Struct(
        "pIDXGIFactory" / Int64ul,
        "ReparentingOccurred" / Int8ul,
        "DecidingFactor" / Int32ul,
        "Message" / CString
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=74, version=0)
class Microsoft_Windows_DXGI_74_0(Etw):
    pattern = Struct(
        "pIDXGISwapchain" / Int64ul,
        "m_pPreferredOutput" / Int64ul,
        "NewSyncInterval" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=80, version=0)
class Microsoft_Windows_DXGI_80_0(Etw):
    pattern = Struct(
        "riid" / Guid,
        "ppFactory" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=81, version=0)
class Microsoft_Windows_DXGI_81_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=104, version=0)
class Microsoft_Windows_DXGI_104_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "riid" / Guid,
        "ppvObject" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=105, version=0)
class Microsoft_Windows_DXGI_105_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul,
        "ppvObject" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=106, version=0)
class Microsoft_Windows_DXGI_106_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=107, version=0)
class Microsoft_Windows_DXGI_107_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=108, version=0)
class Microsoft_Windows_DXGI_108_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=109, version=0)
class Microsoft_Windows_DXGI_109_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=110, version=0)
class Microsoft_Windows_DXGI_110_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "uiDataSize" / Int32ul,
        "pData" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=111, version=0)
class Microsoft_Windows_DXGI_111_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=112, version=0)
class Microsoft_Windows_DXGI_112_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "pInterface" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=113, version=0)
class Microsoft_Windows_DXGI_113_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=114, version=0)
class Microsoft_Windows_DXGI_114_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "pDataSize" / Int32ul,
        "pData" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=115, version=0)
class Microsoft_Windows_DXGI_115_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul,
        "pDataSize" / Int32ul,
        "pData" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=116, version=0)
class Microsoft_Windows_DXGI_116_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "riid" / Guid,
        "ppvObject" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=117, version=0)
class Microsoft_Windows_DXGI_117_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul,
        "ppvObject" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=118, version=0)
class Microsoft_Windows_DXGI_118_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "iOutput" / Int32ul,
        "ppOutput" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=119, version=0)
class Microsoft_Windows_DXGI_119_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=120, version=0)
class Microsoft_Windows_DXGI_120_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=121, version=0)
class Microsoft_Windows_DXGI_121_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=122, version=0)
class Microsoft_Windows_DXGI_122_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "pUMDVersion" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=123, version=0)
class Microsoft_Windows_DXGI_123_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=124, version=0)
class Microsoft_Windows_DXGI_124_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "riid" / Guid,
        "ppvObject" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=125, version=0)
class Microsoft_Windows_DXGI_125_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul,
        "ppvObject" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=126, version=0)
class Microsoft_Windows_DXGI_126_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=127, version=0)
class Microsoft_Windows_DXGI_127_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=128, version=0)
class Microsoft_Windows_DXGI_128_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=129, version=0)
class Microsoft_Windows_DXGI_129_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=130, version=0)
class Microsoft_Windows_DXGI_130_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "uiDataSize" / Int32ul,
        "pData" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=131, version=0)
class Microsoft_Windows_DXGI_131_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=132, version=0)
class Microsoft_Windows_DXGI_132_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "pInterface" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=133, version=0)
class Microsoft_Windows_DXGI_133_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=134, version=0)
class Microsoft_Windows_DXGI_134_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "pDataSize" / Int32ul,
        "pData" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=135, version=0)
class Microsoft_Windows_DXGI_135_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul,
        "pDataSize" / Int32ul,
        "pData" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=136, version=0)
class Microsoft_Windows_DXGI_136_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "riid" / Guid,
        "ppvObject" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=137, version=0)
class Microsoft_Windows_DXGI_137_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul,
        "ppvObject" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=138, version=0)
class Microsoft_Windows_DXGI_138_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=139, version=0)
class Microsoft_Windows_DXGI_139_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=140, version=0)
class Microsoft_Windows_DXGI_140_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "EnumFormat" / Int32ul,
        "dwFlags" / Int32ul,
        "pNumModes" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=141, version=0)
class Microsoft_Windows_DXGI_141_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=142, version=0)
class Microsoft_Windows_DXGI_142_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "pConcernedDevice" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=143, version=0)
class Microsoft_Windows_DXGI_143_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=144, version=0)
class Microsoft_Windows_DXGI_144_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=145, version=0)
class Microsoft_Windows_DXGI_145_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=146, version=0)
class Microsoft_Windows_DXGI_146_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "pDevice" / Int64ul,
        "bExclusive" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=147, version=0)
class Microsoft_Windows_DXGI_147_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=148, version=0)
class Microsoft_Windows_DXGI_148_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=150, version=0)
class Microsoft_Windows_DXGI_150_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "pGammaCaps" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=151, version=0)
class Microsoft_Windows_DXGI_151_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=152, version=0)
class Microsoft_Windows_DXGI_152_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=153, version=0)
class Microsoft_Windows_DXGI_153_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=154, version=0)
class Microsoft_Windows_DXGI_154_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=155, version=0)
class Microsoft_Windows_DXGI_155_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=156, version=0)
class Microsoft_Windows_DXGI_156_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "pScanoutSurface" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=157, version=0)
class Microsoft_Windows_DXGI_157_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=158, version=0)
class Microsoft_Windows_DXGI_158_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "pScanoutSurface" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=159, version=0)
class Microsoft_Windows_DXGI_159_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=160, version=0)
class Microsoft_Windows_DXGI_160_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=161, version=0)
class Microsoft_Windows_DXGI_161_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=162, version=0)
class Microsoft_Windows_DXGI_162_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "riid" / Guid,
        "ppvObject" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=163, version=0)
class Microsoft_Windows_DXGI_163_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul,
        "ppvObject" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=164, version=0)
class Microsoft_Windows_DXGI_164_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=165, version=0)
class Microsoft_Windows_DXGI_165_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=166, version=0)
class Microsoft_Windows_DXGI_166_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=167, version=0)
class Microsoft_Windows_DXGI_167_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=168, version=0)
class Microsoft_Windows_DXGI_168_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "uiDataSize" / Int32ul,
        "pData" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=169, version=0)
class Microsoft_Windows_DXGI_169_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=170, version=0)
class Microsoft_Windows_DXGI_170_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "pInterface" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=171, version=0)
class Microsoft_Windows_DXGI_171_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=172, version=0)
class Microsoft_Windows_DXGI_172_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "pDataSize" / Int32ul,
        "pData" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=173, version=0)
class Microsoft_Windows_DXGI_173_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul,
        "pDataSize" / Int32ul,
        "pData" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=174, version=0)
class Microsoft_Windows_DXGI_174_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "riid" / Guid,
        "ppvObject" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=175, version=0)
class Microsoft_Windows_DXGI_175_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul,
        "ppvObject" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=176, version=0)
class Microsoft_Windows_DXGI_176_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "riid" / Guid,
        "ppvObject" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=177, version=0)
class Microsoft_Windows_DXGI_177_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul,
        "ppvObject" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=178, version=0)
class Microsoft_Windows_DXGI_178_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "SyncInterval" / Int32ul,
        "dwFlags" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=179, version=0)
class Microsoft_Windows_DXGI_179_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=180, version=0)
class Microsoft_Windows_DXGI_180_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "iBuffer" / Int32ul,
        "Interface" / Guid,
        "ppSurface" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=181, version=0)
class Microsoft_Windows_DXGI_181_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=182, version=0)
class Microsoft_Windows_DXGI_182_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "bFullscreen" / Int32ul,
        "pTarget" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=183, version=0)
class Microsoft_Windows_DXGI_183_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=184, version=0)
class Microsoft_Windows_DXGI_184_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "pbFullscreen" / Int32ul,
        "ppTarget" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=185, version=0)
class Microsoft_Windows_DXGI_185_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=186, version=0)
class Microsoft_Windows_DXGI_186_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=187, version=0)
class Microsoft_Windows_DXGI_187_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=188, version=0)
class Microsoft_Windows_DXGI_188_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "BufferCount" / Int32ul,
        "Width" / Int32ul,
        "Height" / Int32ul,
        "NewFormat" / Int32ul,
        "SwapChainFalgs" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=189, version=0)
class Microsoft_Windows_DXGI_189_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=190, version=0)
class Microsoft_Windows_DXGI_190_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=191, version=0)
class Microsoft_Windows_DXGI_191_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=192, version=0)
class Microsoft_Windows_DXGI_192_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "ppOutput" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=193, version=0)
class Microsoft_Windows_DXGI_193_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=194, version=0)
class Microsoft_Windows_DXGI_194_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=195, version=0)
class Microsoft_Windows_DXGI_195_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=196, version=0)
class Microsoft_Windows_DXGI_196_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "pLastPresentCount" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=197, version=0)
class Microsoft_Windows_DXGI_197_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=198, version=0)
class Microsoft_Windows_DXGI_198_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "riid" / Guid,
        "ppvObject" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=199, version=0)
class Microsoft_Windows_DXGI_199_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul,
        "ppvObject" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=200, version=0)
class Microsoft_Windows_DXGI_200_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=201, version=0)
class Microsoft_Windows_DXGI_201_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=202, version=0)
class Microsoft_Windows_DXGI_202_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=203, version=0)
class Microsoft_Windows_DXGI_203_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=204, version=0)
class Microsoft_Windows_DXGI_204_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "uiDataSize" / Int32ul,
        "pData" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=205, version=0)
class Microsoft_Windows_DXGI_205_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=206, version=0)
class Microsoft_Windows_DXGI_206_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "pInterface" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=207, version=0)
class Microsoft_Windows_DXGI_207_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=208, version=0)
class Microsoft_Windows_DXGI_208_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "pDataSize" / Int32ul,
        "pData" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=209, version=0)
class Microsoft_Windows_DXGI_209_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul,
        "pDataSize" / Int32ul,
        "pData" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=210, version=0)
class Microsoft_Windows_DXGI_210_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "riid" / Guid,
        "ppvObject" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=211, version=0)
class Microsoft_Windows_DXGI_211_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul,
        "ppvObject" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=212, version=0)
class Microsoft_Windows_DXGI_212_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "iAdapter" / Int32ul,
        "ppAdapterInterface" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=213, version=0)
class Microsoft_Windows_DXGI_213_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=214, version=0)
class Microsoft_Windows_DXGI_214_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "hWnd" / Int64ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=215, version=0)
class Microsoft_Windows_DXGI_215_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=216, version=0)
class Microsoft_Windows_DXGI_216_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "phWnd" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=217, version=0)
class Microsoft_Windows_DXGI_217_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=218, version=0)
class Microsoft_Windows_DXGI_218_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "pDevice" / Int64ul,
        "ppSwapChain" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=219, version=0)
class Microsoft_Windows_DXGI_219_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=220, version=0)
class Microsoft_Windows_DXGI_220_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "hModule" / Int64ul,
        "ppAdapter" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=221, version=0)
class Microsoft_Windows_DXGI_221_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=848, version=0)
class Microsoft_Windows_DXGI_848_0(Etw):
    pattern = Struct(
        "riid" / Guid,
        "ppFactory" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=849, version=0)
class Microsoft_Windows_DXGI_849_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=850, version=0)
class Microsoft_Windows_DXGI_850_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "Width" / Int32ul,
        "Height" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=851, version=0)
class Microsoft_Windows_DXGI_851_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=852, version=0)
class Microsoft_Windows_DXGI_852_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "pWidth" / Int64ul,
        "pHeight" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=853, version=0)
class Microsoft_Windows_DXGI_853_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=854, version=0)
class Microsoft_Windows_DXGI_854_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "BufferToPresent" / Int32ul,
        "SyncInterval" / Int32ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=855, version=0)
class Microsoft_Windows_DXGI_855_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=856, version=0)
class Microsoft_Windows_DXGI_856_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "MaxLatency" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=857, version=0)
class Microsoft_Windows_DXGI_857_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=858, version=0)
class Microsoft_Windows_DXGI_858_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "pMaxLatency" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=859, version=0)
class Microsoft_Windows_DXGI_859_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=860, version=0)
class Microsoft_Windows_DXGI_860_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=861, version=0)
class Microsoft_Windows_DXGI_861_0(Etw):
    pattern = Struct(
        "m_Ret" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=862, version=0)
class Microsoft_Windows_DXGI_862_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "pRect" / Int64ul,
        "Rect" / Int32sl
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=863, version=0)
class Microsoft_Windows_DXGI_863_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=864, version=0)
class Microsoft_Windows_DXGI_864_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "pRect" / Int64ul,
        "Rect" / Int32sl
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=865, version=0)
class Microsoft_Windows_DXGI_865_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=866, version=0)
class Microsoft_Windows_DXGI_866_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "Width" / Int32ul,
        "Height" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=867, version=0)
class Microsoft_Windows_DXGI_867_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=868, version=0)
class Microsoft_Windows_DXGI_868_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "pRect" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=869, version=0)
class Microsoft_Windows_DXGI_869_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=870, version=0)
class Microsoft_Windows_DXGI_870_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "pRect" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=871, version=0)
class Microsoft_Windows_DXGI_871_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=872, version=0)
class Microsoft_Windows_DXGI_872_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "pWidth" / Int64ul,
        "pHeight" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=873, version=0)
class Microsoft_Windows_DXGI_873_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=874, version=0)
class Microsoft_Windows_DXGI_874_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "YCbCrFlags" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=875, version=0)
class Microsoft_Windows_DXGI_875_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=876, version=0)
class Microsoft_Windows_DXGI_876_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=877, version=0)
class Microsoft_Windows_DXGI_877_0(Etw):
    pattern = Struct(
        "YCbCrFlags" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=878, version=0)
class Microsoft_Windows_DXGI_878_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "pMatrix" / Int64ul,
        "Matrix" / Float32l
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=879, version=0)
class Microsoft_Windows_DXGI_879_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=880, version=0)
class Microsoft_Windows_DXGI_880_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "pMatrix" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=881, version=0)
class Microsoft_Windows_DXGI_881_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=882, version=0)
class Microsoft_Windows_DXGI_882_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "SyncInterval" / Int32ul,
        "Flags" / Int32ul,
        "PartnerFlags" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=883, version=0)
class Microsoft_Windows_DXGI_883_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=884, version=0)
class Microsoft_Windows_DXGI_884_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "Duration" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=885, version=0)
class Microsoft_Windows_DXGI_885_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=886, version=0)
class Microsoft_Windows_DXGI_886_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "DesiredPresentDuration" / Int32ul,
        "pClosestSmallerPresentDuration" / Int64ul,
        "pClosestLargerPresentDuration" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=887, version=0)
class Microsoft_Windows_DXGI_887_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=888, version=0)
class Microsoft_Windows_DXGI_888_0(Etw):
    pattern = Struct(
        "pThis" / Int64ul,
        "iOutput" / Int32ul,
        "iOutputType" / Int32ul,
        "ppOutput" / Int64ul
    )


@declare(guid=guid("ca11c036-0102-4a2d-a6ad-f03cfed5d3c9"), event_id=889, version=0)
class Microsoft_Windows_DXGI_889_0(Etw):
    pattern = Struct(
        "m_Ret" / Int32ul
    )

