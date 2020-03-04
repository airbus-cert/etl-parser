# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Win32k
GUID : 8c416c79-d49b-4f01-a467-e56d3aa8234c
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=1, version=0)
class Microsoft_Windows_Win32k_1_0(Etw):
    pattern = Struct(
        "Hwnd" / Int64ul,
        "Type" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=2, version=0)
class Microsoft_Windows_Win32k_2_0(Etw):
    pattern = Struct(
        "OldThreadId" / Int32ul,
        "NewThreadId" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=3, version=0)
class Microsoft_Windows_Win32k_3_0(Etw):
    pattern = Struct(
        "UIPI_Trace_Header" / Int8ul,
        "Message" / Int32ul,
        "wParam" / Int64ul,
        "lParam" / Int64ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=4, version=0)
class Microsoft_Windows_Win32k_4_0(Etw):
    pattern = Struct(
        "UIPI_Trace_Header" / Int16ul,
        "HookID" / Int32sl,
        "Flags" / Int8sl,
        "nCode" / Int32sl,
        "wParam" / Int64ul,
        "lParam" / Int64ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=5, version=0)
class Microsoft_Windows_Win32k_5_0(Etw):
    pattern = Struct(
        "UIPI_Trace_Header" / Int32ul,
        "WinEvent" / Int32ul,
        "WndHandle" / Int64ul,
        "ObjectID" / Int32ul,
        "ChildID" / Int32ul,
        "SenderTID" / Int32sl,
        "Time" / Int32sl,
        "Flags" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=6, version=0)
class Microsoft_Windows_Win32k_6_0(Etw):
    pattern = Struct(
        "UIPI_Trace_Header" / Int8ul,
        "Handle" / Int64ul,
        "HandleType" / Int32ul,
        "Reserved" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=7, version=0)
class Microsoft_Windows_Win32k_7_0(Etw):
    pattern = Struct(
        "UIPI_Trace_Header" / Int8ul,
        "InputType" / Int32ul,
        "QIL" / Int32ul,
        "QLBN" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=8, version=0)
class Microsoft_Windows_Win32k_8_0(Etw):
    pattern = Struct(
        "UIPI_Trace_Header" / Int8ul,
        "ClipFormat" / Int32ul,
        "ClipIL" / Int32ul,
        "ClipLBN" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=9, version=0)
class Microsoft_Windows_Win32k_9_0(Etw):
    pattern = Struct(
        "UIPI_Trace_Header" / CString,
        "SysErrorType" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=10, version=0)
class Microsoft_Windows_Win32k_10_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "PreviousStateTime" / Int32ul,
        "PreviousState" / Int16ul,
        "NewState" / Int16ul,
        "IsConsoleSession" / Int16ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=11, version=0)
class Microsoft_Windows_Win32k_11_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "IdleAction" / Int32ul,
        "TimeoutValueMs" / Int32ul,
        "IdleStartTime" / Int32ul,
        "IsConsoleSession" / Int16ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=12, version=0)
class Microsoft_Windows_Win32k_12_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "IsConsoleSession" / Int16ul,
        "NewCount" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=13, version=0)
class Microsoft_Windows_Win32k_13_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "IsConsoleSession" / Int16ul,
        "DisplayTimeoutValueMs" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=14, version=0)
class Microsoft_Windows_Win32k_14_0(Etw):
    pattern = Struct(
        "LockId" / Int64ul,
        "LockLevel" / Int32ul,
        "LockName" / WString
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=15, version=0)
class Microsoft_Windows_Win32k_15_0(Etw):
    pattern = Struct(
        "LockId" / Int64ul,
        "LockName" / WString
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=16, version=0)
class Microsoft_Windows_Win32k_16_0(Etw):
    pattern = Struct(
        "LockId" / Int64ul,
        "LockName" / WString
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=17, version=0)
class Microsoft_Windows_Win32k_17_0(Etw):
    pattern = Struct(
        "LockId" / Int64ul,
        "LockName" / WString
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=18, version=0)
class Microsoft_Windows_Win32k_18_0(Etw):
    pattern = Struct(
        "hWnd" / Int64ul,
        "hLogicalSurfSwapChainBind" / Int64ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=19, version=0)
class Microsoft_Windows_Win32k_19_0(Etw):
    pattern = Struct(
        "hWnd" / Int64ul,
        "hLogicalSurfSwapChainBind" / Int64ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=20, version=0)
class Microsoft_Windows_Win32k_20_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "AccruedIdleTime" / Int32ul,
        "DisplayTimeoutValueMs" / Int32ul,
        "ScreenSaverTimeoutValueMs" / Int32ul,
        "DimTimeoutValueMs" / Int32ul,
        "DimBrightnessValue" / Int32ul,
        "NormalBrightnessValue" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=21, version=0)
class Microsoft_Windows_Win32k_21_0(Etw):
    pattern = Struct(
        "hLogicalSurfSwapChainBind" / Int64ul,
        "ConfirmReason" / Int32ul,
        "LastPresentId" / Int32ul,
        "LastFrameCount" / Int32ul,
        "SyncFrameCount" / Int32ul,
        "LastFrameTime" / Int64ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=22, version=0)
class Microsoft_Windows_Win32k_22_0(Etw):
    pattern = Struct(
        "Action" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=23, version=0)
class Microsoft_Windows_Win32k_23_0(Etw):
    pattern = Struct(
        "Action" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=24, version=0)
class Microsoft_Windows_Win32k_24_0(Etw):
    pattern = Struct(
        "Action" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=25, version=0)
class Microsoft_Windows_Win32k_25_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "ProcessIdOwningFocus" / Int32ul,
        "ProcessCreateTimeOwningFocus" / Int64ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=26, version=0)
class Microsoft_Windows_Win32k_26_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "OldProcessId" / Int32ul,
        "NewProcessId" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=27, version=0)
class Microsoft_Windows_Win32k_27_0(Etw):
    pattern = Struct(
        "hWnd" / Int64ul,
        "hSprite" / Int64ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=28, version=0)
class Microsoft_Windows_Win32k_28_0(Etw):
    pattern = Struct(
        "hWnd" / Int64ul,
        "hSprite" / Int64ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=29, version=0)
class Microsoft_Windows_Win32k_29_0(Etw):
    pattern = Struct(
        "hLogicalSurf" / Int64ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=30, version=0)
class Microsoft_Windows_Win32k_30_0(Etw):
    pattern = Struct(
        "hLogicalSurf" / Int64ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=31, version=0)
class Microsoft_Windows_Win32k_31_0(Etw):
    pattern = Struct(
        "hLogicalSurf" / Int64ul,
        "hPhysicalSurf" / Int64ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=32, version=0)
class Microsoft_Windows_Win32k_32_0(Etw):
    pattern = Struct(
        "hLogicalSurf" / Int64ul,
        "hPhysicalSurf" / Int64ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=33, version=0)
class Microsoft_Windows_Win32k_33_0(Etw):
    pattern = Struct(
        "Pending" / Int32ul,
        "dwDirtyFlags" / Int32ul,
        "hLogicalSurf" / Int64ul,
        "uiCookie" / Int64ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=35, version=0)
class Microsoft_Windows_Win32k_35_0(Etw):
    pattern = Struct(
        "CursorThreadId" / Int32ul,
        "CursorProcessId" / Int32ul,
        "SessionId" / Int32ul,
        "CursorType" / Int32ul,
        "DisplayTimeMs" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=36, version=0)
class Microsoft_Windows_Win32k_36_0(Etw):
    pattern = Struct(
        "ThreadId" / Int32ul,
        "Flags" / Int32ul,
        "TimeSinceInputCheckMs" / Int32ul,
        "TimeSinceInputRemoveMs" / Int32ul,
        "TimeSinceOldestInputMs" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=37, version=0)
class Microsoft_Windows_Win32k_37_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul,
        "TimeSinceInputRemoveMs" / Int32ul,
        "TimeSinceOldestInputMs" / Int32ul,
        "ClassName" / WString,
        "TopLevelClassName" / WString,
        "ImagePath" / WString,
        "MessageId" / Int32ul,
        "WParam" / Int64ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=38, version=0)
class Microsoft_Windows_Win32k_38_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul,
        "DelayTimeMs" / Int32ul,
        "TimeSinceInputRemoveMs" / Int32ul,
        "TimeSinceOldestInputMs" / Int32ul,
        "ClassName" / WString,
        "TopLevelClassName" / WString,
        "ImagePath" / WString,
        "MessageId" / Int32ul,
        "WParam" / Int64ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=39, version=0)
class Microsoft_Windows_Win32k_39_0(Etw):
    pattern = Struct(
        "hwndDst" / Int64ul,
        "hwndDstSprite" / Int64ul,
        "hbmDst" / Int64ul,
        "DstLeft" / Int32ul,
        "DstTop" / Int32ul,
        "DstRight" / Int32ul,
        "DstBottom" / Int32ul,
        "hwndSrc" / Int64ul,
        "hwndSrcSprite" / Int64ul,
        "hbmSrc" / Int64ul,
        "SrcLeft" / Int32ul,
        "SrcTop" / Int32ul,
        "SrcRight" / Int32ul,
        "SrcBottom" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=40, version=0)
class Microsoft_Windows_Win32k_40_0(Etw):
    pattern = Struct(
        "hwndDst" / Int64ul,
        "hwndDstSprite" / Int64ul,
        "hbmDst" / Int64ul,
        "DstLeft" / Int32ul,
        "DstTop" / Int32ul,
        "DstRight" / Int32ul,
        "DstBottom" / Int32ul,
        "hwndSrc" / Int64ul,
        "hwndSrcSprite" / Int64ul,
        "hbmSrc" / Int64ul,
        "SrcLeft" / Int32ul,
        "SrcTop" / Int32ul,
        "SrcRight" / Int32ul,
        "SrcBottom" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=41, version=0)
class Microsoft_Windows_Win32k_41_0(Etw):
    pattern = Struct(
        "hwnd" / Int64ul,
        "bitmapCX" / Int32ul,
        "bitmapCY" / Int32ul,
        "DirtyLeft" / Int32ul,
        "DirtyTop" / Int32ul,
        "DirtyRight" / Int32ul,
        "DirtyBottom" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=42, version=0)
class Microsoft_Windows_Win32k_42_0(Etw):
    pattern = Struct(
        "hwnd" / Int64ul,
        "bitmapCX" / Int32ul,
        "bitmapCY" / Int32ul,
        "DirtyLeft" / Int32ul,
        "DirtyTop" / Int32ul,
        "DirtyRight" / Int32ul,
        "DirtyBottom" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=43, version=0)
class Microsoft_Windows_Win32k_43_0(Etw):
    pattern = Struct(
        "hwnd" / Int64ul,
        "FULL" / Int32ul,
        "Left" / Int32ul,
        "Top" / Int32ul,
        "Right" / Int32ul,
        "Bottom" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=44, version=0)
class Microsoft_Windows_Win32k_44_0(Etw):
    pattern = Struct(
        "hwnd" / Int64ul,
        "FULL" / Int32ul,
        "Left" / Int32ul,
        "Top" / Int32ul,
        "Right" / Int32ul,
        "Bottom" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=45, version=0)
class Microsoft_Windows_Win32k_45_0(Etw):
    pattern = Struct(
        "ThreadId" / Int32ul,
        "Flags" / Int32ul,
        "TimeSinceInputCheckMs" / Int32ul,
        "TimeSinceInputRemoveMs" / Int32ul,
        "TimeSinceOldestInputMs" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=46, version=0)
class Microsoft_Windows_Win32k_46_0(Etw):
    pattern = Struct(
        "hWnd" / Int64ul,
        "hLogicalSurf" / Int64ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=47, version=0)
class Microsoft_Windows_Win32k_47_0(Etw):
    pattern = Struct(
        "hWnd" / Int64ul,
        "hLogicalSurf" / Int64ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=48, version=0)
class Microsoft_Windows_Win32k_48_0(Etw):
    pattern = Struct(
        "hLogicalSurf" / Int64ul,
        "bCreated" / Int64ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=49, version=0)
class Microsoft_Windows_Win32k_49_0(Etw):
    pattern = Struct(
        "hDwmSprite" / Int64ul,
        "hLogicalSurf" / Int64ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=50, version=0)
class Microsoft_Windows_Win32k_50_0(Etw):
    pattern = Struct(
        "hDwmSprite" / Int64ul,
        "hLogicalSurf" / Int64ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=51, version=0)
class Microsoft_Windows_Win32k_51_0(Etw):
    pattern = Struct(
        "hLogicalSurf" / Int64ul,
        "hPhysSurf" / Int64ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=52, version=0)
class Microsoft_Windows_Win32k_52_0(Etw):
    pattern = Struct(
        "hPhysicalSurf" / Int64ul,
        "Type" / Int32ul,
        "hDxSharedSurface" / Int64ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=53, version=0)
class Microsoft_Windows_Win32k_53_0(Etw):
    pattern = Struct(
        "hLogicalSurface" / Int64ul,
        "RgnType" / Int32ul,
        "rcBounds" / Int16sl,
        "NumRects" / Int32ul,
        "rcData" / Int64sl
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=54, version=0)
class Microsoft_Windows_Win32k_54_0(Etw):
    pattern = Struct(
        "hLogicalSurfSwapChainBind" / Int64ul,
        "ConfirmReason" / Int32ul,
        "LastPresentId" / Int32ul,
        "LastFrameCount" / Int32ul,
        "SyncFrameCount" / Int32ul,
        "LastFrameTime" / Int64ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=55, version=0)
class Microsoft_Windows_Win32k_55_0(Etw):
    pattern = Struct(
        "hLogicalSurfSwapChainBinding" / Int64ul,
        "luidAdapter" / Int64ul,
        "nWidth" / Int32ul,
        "nHeight" / Int32ul,
        "DxgiColorFormat" / Int32ul,
        "hmonAssociation" / Int64ul,
        "uiPresentLimitSemaphoreId" / Int64ul,
        "cBuffers" / Int32ul,
        "BindingInfoHandle" / Int64sl
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=56, version=0)
class Microsoft_Windows_Win32k_56_0(Etw):
    pattern = Struct(
        "hLogicalSurfSwapChainBinding" / Int64ul,
        "DesktopCompositorProcess" / Int8ul,
        "DesktopCompositorError" / Int8ul,
        "DesktopCompositorRef" / Int8ul,
        "DesktopCompositorStatus" / Int8ul,
        "pEventConfirmed" / Int64ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=57, version=0)
class Microsoft_Windows_Win32k_57_0(Etw):
    pattern = Struct(
        "hLogicalSurfSwapChainBinding" / Int64ul,
        "DesktopCompositorStatus" / Int8ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=58, version=0)
class Microsoft_Windows_Win32k_58_0(Etw):
    pattern = Struct(
        "ProcessId" / Int32ul,
        "FailureStatus" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=59, version=0)
class Microsoft_Windows_Win32k_59_0(Etw):
    pattern = Struct(
        "CallbackCount" / Int8sl,
        "pqmsg" / Int64ul,
        "hwnd" / Int64ul,
        "WParam" / Int64ul,
        "LParam" / Int64ul,
        "message" / Int32ul,
        "inputReadyTimeMs" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=60, version=0)
class Microsoft_Windows_Win32k_60_0(Etw):
    pattern = Struct(
        "CallbackCount" / Int8sl,
        "pqmsg" / Int64ul,
        "hwnd" / Int64ul,
        "WParam" / Int64ul,
        "LParam" / Int64ul,
        "message" / Int32ul,
        "inputReadyTimeMs" / Int32ul,
        "flags" / Int32ul,
        "pidReceiver" / Int32ul,
        "tidReceiver" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=61, version=0)
class Microsoft_Windows_Win32k_61_0(Etw):
    pattern = Struct(
        "CallbackCount" / Int8sl,
        "pqmsg" / Int64ul,
        "hwnd" / Int64ul,
        "WParam" / Int64ul,
        "LParam" / Int64ul,
        "message" / Int32ul,
        "inputReadyTimeMs" / Int32ul,
        "flags" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=62, version=0)
class Microsoft_Windows_Win32k_62_0(Etw):
    pattern = Struct(
        "CallbackCount" / Int8sl,
        "pqmsg" / Int64ul,
        "hwnd" / Int64ul,
        "WParam" / Int64ul,
        "LParam" / Int64ul,
        "message" / Int32ul,
        "inputReadyTimeMs" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=63, version=0)
class Microsoft_Windows_Win32k_63_0(Etw):
    pattern = Struct(
        "CallbackCount" / Int8sl,
        "hwnd" / Int64ul,
        "WParam" / Int64ul,
        "LParam" / Int64ul,
        "message" / Int32ul,
        "inputReadyTimeMs" / Int32ul,
        "flags" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=64, version=0)
class Microsoft_Windows_Win32k_64_0(Etw):
    pattern = Struct(
        "CallbackCount" / Int8sl,
        "pqmsg" / Int64ul,
        "hwnd" / Int64ul,
        "WParam" / Int64ul,
        "LParam" / Int64ul,
        "message" / Int32ul,
        "inputReadyTimeMs" / Int32ul,
        "flags" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=65, version=0)
class Microsoft_Windows_Win32k_65_0(Etw):
    pattern = Struct(
        "CallbackCount" / Int8sl,
        "pqmsg" / Int64ul,
        "hwnd" / Int64ul,
        "WParam" / Int64ul,
        "LParam" / Int64ul,
        "message" / Int32ul,
        "inputReadyTimeMs" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=66, version=0)
class Microsoft_Windows_Win32k_66_0(Etw):
    pattern = Struct(
        "CallbackCount" / Int8sl,
        "pQueue" / Int64ul,
        "ownerThread" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=67, version=0)
class Microsoft_Windows_Win32k_67_0(Etw):
    pattern = Struct(
        "CallbackCount" / Int8sl,
        "pQueue" / Int64ul,
        "ownerThread" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=68, version=0)
class Microsoft_Windows_Win32k_68_0(Etw):
    pattern = Struct(
        "CallbackCount" / Int8sl,
        "api" / Int32sl
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=69, version=0)
class Microsoft_Windows_Win32k_69_0(Etw):
    pattern = Struct(
        "CallbackCount" / Int8sl,
        "api" / Int32sl
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=70, version=0)
class Microsoft_Windows_Win32k_70_0(Etw):
    pattern = Struct(
        "CallbackCount" / Int8sl,
        "pqmsg" / Int64ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=71, version=0)
class Microsoft_Windows_Win32k_71_0(Etw):
    pattern = Struct(
        "CallbackCount" / Int8sl
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=72, version=0)
class Microsoft_Windows_Win32k_72_0(Etw):
    pattern = Struct(
        "DeviceType" / Int32sl,
        "dwFlags" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=73, version=0)
class Microsoft_Windows_Win32k_73_0(Etw):
    pattern = Struct(
        "DeviceType" / Int32sl,
        "dwFlags" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=74, version=0)
class Microsoft_Windows_Win32k_74_0(Etw):
    pattern = Struct(
        "CallbackCount" / Int8sl,
        "hwnd" / Int64ul,
        "hGestureInfo" / Int64ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=75, version=0)
class Microsoft_Windows_Win32k_75_0(Etw):
    pattern = Struct(
        "CallbackCount" / Int8sl,
        "hwnd" / Int64ul,
        "hGestureInfo" / Int64ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=76, version=0)
class Microsoft_Windows_Win32k_76_0(Etw):
    pattern = Struct(
        "CallbackCount" / Int8sl,
        "fGetMessage" / Int32sl,
        "dwFlags" / Int32ul,
        "Message" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=77, version=0)
class Microsoft_Windows_Win32k_77_0(Etw):
    pattern = Struct(
        "CallbackCount" / Int8sl,
        "fGetMessage" / Int32sl
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=78, version=0)
class Microsoft_Windows_Win32k_78_0(Etw):
    pattern = Struct(
        "CallbackCount" / Int8sl,
        "WakeReason" / Int32sl
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=79, version=0)
class Microsoft_Windows_Win32k_79_0(Etw):
    pattern = Struct(
        "Time" / Int32sl,
        "X" / Int32sl,
        "Y" / Int32sl
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=80, version=0)
class Microsoft_Windows_Win32k_80_0(Etw):
    pattern = Struct(
        "Time" / Int32sl,
        "X" / Int32sl,
        "Y" / Int32sl
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=81, version=0)
class Microsoft_Windows_Win32k_81_0(Etw):
    pattern = Struct(
        "CallbackCount" / Int8sl,
        "Time" / Int32sl,
        "X" / Int32sl,
        "Y" / Int32sl
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=82, version=0)
class Microsoft_Windows_Win32k_82_0(Etw):
    pattern = Struct(
        "CallbackCount" / Int8sl,
        "Time" / Int32sl,
        "X" / Int32sl,
        "Y" / Int32sl
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=83, version=0)
class Microsoft_Windows_Win32k_83_0(Etw):
    pattern = Struct(
        "CallbackCount" / Int8sl,
        "pqmsg" / Int64ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=88, version=0)
class Microsoft_Windows_Win32k_88_0(Etw):
    pattern = Struct(
        "CallbackCount" / Int8sl,
        "pqmsg" / Int64ul,
        "WindowDelegated" / Int8ul,
        "WasWindowDelegated" / Int8ul,
        "Delegated" / Int8ul,
        "WasDelegated" / Int8ul,
        "Processed" / Int8ul,
        "fDelayedFree" / Int8ul,
        "hwnd" / Int64ul,
        "WParam" / Int64ul,
        "LParam" / Int64ul,
        "message" / Int32ul,
        "inputReadyTimeMs" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=89, version=0)
class Microsoft_Windows_Win32k_89_0(Etw):
    pattern = Struct(
        "CallbackCount" / Int8sl,
        "message" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=91, version=0)
class Microsoft_Windows_Win32k_91_0(Etw):
    pattern = Struct(
        "CallbackCount" / Int8sl,
        "message" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=92, version=0)
class Microsoft_Windows_Win32k_92_0(Etw):
    pattern = Struct(
        "CallbackCount" / Int8sl,
        "message" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=93, version=0)
class Microsoft_Windows_Win32k_93_0(Etw):
    pattern = Struct(
        "CallbackCount" / Int8sl,
        "message" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=100, version=0)
class Microsoft_Windows_Win32k_100_0(Etw):
    pattern = Struct(
        "CallbackCount" / Int8sl
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=102, version=0)
class Microsoft_Windows_Win32k_102_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "cLineWidth" / Int32ul,
        "TimerStatisticsThreshold" / Int16sl,
        "cElements" / Int32ul,
        "TimerStatisticsInfo" / Int16ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=103, version=0)
class Microsoft_Windows_Win32k_103_0(Etw):
    pattern = Struct(
        "ProcName" / CString,
        "ClassName" / WString,
        "WindowName" / WString,
        "uId" / Int32ul,
        "uElapse" / Int32ul,
        "uType" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=106, version=0)
class Microsoft_Windows_Win32k_106_0(Etw):
    pattern = Struct(
        "ptOffsetX" / Int32sl,
        "ptOffsetY" / Int32sl,
        "pointerId" / Int32sl,
        "cursorId" / Int32sl
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=107, version=0)
class Microsoft_Windows_Win32k_107_0(Etw):
    pattern = Struct(
        "pointerId" / Int32sl,
        "cursorId" / Int32sl,
        "pointerType" / Int32sl,
        "pointerFlags" / Int32sl,
        "touchMask" / Int32sl,
        "ptLocationX" / Int32sl,
        "ptLocationY" / Int32sl,
        "rcContactLeft" / Int32sl,
        "rcContactRight" / Int32sl,
        "rcContactTop" / Int32sl,
        "rcContactBottom" / Int32sl,
        "orientation" / Int32sl
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=108, version=0)
class Microsoft_Windows_Win32k_108_0(Etw):
    pattern = Struct(
        "pointerId" / Int32sl,
        "cursorId" / Int32sl,
        "pointerType" / Int32sl,
        "pointerFlags" / Int32sl,
        "touchMask" / Int32sl,
        "ptLocationX" / Int32sl,
        "ptLocationY" / Int32sl,
        "rcContactLeft" / Int32sl,
        "rcContactRight" / Int32sl,
        "rcContactTop" / Int32sl,
        "rcContactBottom" / Int32sl,
        "orientation" / Int32sl
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=115, version=0)
class Microsoft_Windows_Win32k_115_0(Etw):
    pattern = Struct(
        "ulContactId" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=116, version=0)
class Microsoft_Windows_Win32k_116_0(Etw):
    pattern = Struct(
        "ulContactId" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=117, version=0)
class Microsoft_Windows_Win32k_117_0(Etw):
    pattern = Struct(
        "hwnd" / Int64ul,
        "DirtyLeft" / Int32ul,
        "DirtyTop" / Int32ul,
        "DirtyRight" / Int32ul,
        "DirtyBottom" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=118, version=0)
class Microsoft_Windows_Win32k_118_0(Etw):
    pattern = Struct(
        "hwnd" / Int64ul,
        "Offsetx" / Int32sl,
        "Offsety" / Int32sl
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=119, version=0)
class Microsoft_Windows_Win32k_119_0(Etw):
    pattern = Struct(
        "hwnd" / Int64ul,
        "DirtyLeft" / Int32ul,
        "DirtyTop" / Int32ul,
        "DirtyRight" / Int32ul,
        "DirtyBottom" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=120, version=0)
class Microsoft_Windows_Win32k_120_0(Etw):
    pattern = Struct(
        "hwnd" / Int64ul,
        "DirtyLeft" / Int32ul,
        "DirtyTop" / Int32ul,
        "DirtyRight" / Int32ul,
        "DirtyBottom" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=121, version=0)
class Microsoft_Windows_Win32k_121_0(Etw):
    pattern = Struct(
        "hwnd" / Int64ul,
        "DirtyLeft" / Int32ul,
        "DirtyTop" / Int32ul,
        "DirtyRight" / Int32ul,
        "DirtyBottom" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=122, version=0)
class Microsoft_Windows_Win32k_122_0(Etw):
    pattern = Struct(
        "hSprite" / Int64ul,
        "hWnd" / Int64ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=123, version=0)
class Microsoft_Windows_Win32k_123_0(Etw):
    pattern = Struct(
        "hLogicalSurface" / Int64ul,
        "RgnType" / Int32ul,
        "rcBounds" / Int16sl,
        "NumRects" / Int32ul,
        "rcData" / Int64sl
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=124, version=0)
class Microsoft_Windows_Win32k_124_0(Etw):
    pattern = Struct(
        "hwnd" / Int64ul,
        "DirtyLeft" / Int32ul,
        "DirtyTop" / Int32ul,
        "DirtyRight" / Int32ul,
        "DirtyBottom" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=131, version=0)
class Microsoft_Windows_Win32k_131_0(Etw):
    pattern = Struct(
        "FrameId" / Int32ul,
        "PointerCount" / Int32ul,
        "PendingPointerCount" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=132, version=0)
class Microsoft_Windows_Win32k_132_0(Etw):
    pattern = Struct(
        "FrameId" / Int32ul,
        "PointerCount" / Int32ul,
        "PendingPointerCount" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=133, version=0)
class Microsoft_Windows_Win32k_133_0(Etw):
    pattern = Struct(
        "FrameId" / Int32ul,
        "PointerCount" / Int32ul,
        "PendingPointerCount" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=134, version=0)
class Microsoft_Windows_Win32k_134_0(Etw):
    pattern = Struct(
        "FrameId" / Int32ul,
        "PointerCount" / Int32ul,
        "PendingPointerCount" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=135, version=0)
class Microsoft_Windows_Win32k_135_0(Etw):
    pattern = Struct(
        "FrameId" / Int32ul,
        "PointerCount" / Int32ul,
        "PendingPointerCount" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=136, version=0)
class Microsoft_Windows_Win32k_136_0(Etw):
    pattern = Struct(
        "FrameId" / Int32ul,
        "PointerCount" / Int32ul,
        "PendingPointerCount" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=137, version=0)
class Microsoft_Windows_Win32k_137_0(Etw):
    pattern = Struct(
        "FrameId" / Int32ul,
        "PointerCount" / Int32ul,
        "PendingPointerCount" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=138, version=0)
class Microsoft_Windows_Win32k_138_0(Etw):
    pattern = Struct(
        "FrameId" / Int32ul,
        "PointerCount" / Int32ul,
        "PendingPointerCount" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=139, version=0)
class Microsoft_Windows_Win32k_139_0(Etw):
    pattern = Struct(
        "FrameId" / Int32ul,
        "PointerCount" / Int32ul,
        "PendingPointerCount" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=140, version=0)
class Microsoft_Windows_Win32k_140_0(Etw):
    pattern = Struct(
        "FrameId" / Int32ul,
        "PointerCount" / Int32ul,
        "PendingPointerCount" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=141, version=0)
class Microsoft_Windows_Win32k_141_0(Etw):
    pattern = Struct(
        "pqmsg" / Int64ul,
        "PointerId" / Int32ul,
        "Message" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=142, version=0)
class Microsoft_Windows_Win32k_142_0(Etw):
    pattern = Struct(
        "pqmsg" / Int64ul,
        "PointerId" / Int32ul,
        "Message" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=143, version=0)
class Microsoft_Windows_Win32k_143_0(Etw):
    pattern = Struct(
        "pqmsg" / Int64ul,
        "PointerId" / Int32ul,
        "Message" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=144, version=0)
class Microsoft_Windows_Win32k_144_0(Etw):
    pattern = Struct(
        "pqmsg" / Int64ul,
        "PointerId" / Int32ul,
        "Message" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=149, version=0)
class Microsoft_Windows_Win32k_149_0(Etw):
    pattern = Struct(
        "CallbackCount" / Int8sl,
        "pQueue" / Int64ul,
        "ownerThread" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=150, version=0)
class Microsoft_Windows_Win32k_150_0(Etw):
    pattern = Struct(
        "CallbackCount" / Int8sl,
        "pQueue" / Int64ul,
        "ownerThread" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=151, version=0)
class Microsoft_Windows_Win32k_151_0(Etw):
    pattern = Struct(
        "channelHandle" / Int32ul,
        "pBatch" / Int64ul,
        "batchID" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=152, version=0)
class Microsoft_Windows_Win32k_152_0(Etw):
    pattern = Struct(
        "CallbackCount" / Int8sl,
        "pqmsg" / Int64ul,
        "WindowDelegated" / Int8ul,
        "WasWindowDelegated" / Int8ul,
        "Delegated" / Int8ul,
        "WasDelegated" / Int8ul,
        "Processed" / Int8ul,
        "fDelayedFree" / Int8ul,
        "hwnd" / Int64ul,
        "WParam" / Int64ul,
        "LParam" / Int64ul,
        "message" / Int32ul,
        "inputReadyTimeMs" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=153, version=0)
class Microsoft_Windows_Win32k_153_0(Etw):
    pattern = Struct(
        "CallbackCount" / Int8sl,
        "pqmsg" / Int64ul,
        "WindowDelegated" / Int8ul,
        "WasWindowDelegated" / Int8ul,
        "Delegated" / Int8ul,
        "WasDelegated" / Int8ul,
        "Processed" / Int8ul,
        "fDelayedFree" / Int8ul,
        "hwnd" / Int64ul,
        "WParam" / Int64ul,
        "LParam" / Int64ul,
        "message" / Int32ul,
        "inputReadyTimeMs" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=154, version=0)
class Microsoft_Windows_Win32k_154_0(Etw):
    pattern = Struct(
        "CallbackCount" / Int8sl,
        "pqmsg" / Int64ul,
        "WindowDelegated" / Int8ul,
        "WasWindowDelegated" / Int8ul,
        "Delegated" / Int8ul,
        "WasDelegated" / Int8ul,
        "Processed" / Int8ul,
        "fDelayedFree" / Int8ul,
        "hwnd" / Int64ul,
        "WParam" / Int64ul,
        "LParam" / Int64ul,
        "message" / Int32ul,
        "inputReadyTimeMs" / Int32ul,
        "hdfResponse" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=155, version=0)
class Microsoft_Windows_Win32k_155_0(Etw):
    pattern = Struct(
        "CallbackCount" / Int8sl,
        "pqmsg" / Int64ul,
        "WindowDelegated" / Int8ul,
        "WasWindowDelegated" / Int8ul,
        "Delegated" / Int8ul,
        "WasDelegated" / Int8ul,
        "Processed" / Int8ul,
        "fDelayedFree" / Int8ul,
        "hwnd" / Int64ul,
        "WParam" / Int64ul,
        "LParam" / Int64ul,
        "message" / Int32ul,
        "inputReadyTimeMs" / Int32ul,
        "hdfResponse" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=156, version=0)
class Microsoft_Windows_Win32k_156_0(Etw):
    pattern = Struct(
        "bNew" / Int32ul,
        "ulContactId" / Int32ul,
        "dwCursorId" / Int32ul,
        "X" / Int32sl,
        "Y" / Int32sl
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=157, version=0)
class Microsoft_Windows_Win32k_157_0(Etw):
    pattern = Struct(
        "wCursorId" / Int16ul,
        "wPointerId" / Int16ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=158, version=0)
class Microsoft_Windows_Win32k_158_0(Etw):
    pattern = Struct(
        "wCursorId" / Int16ul,
        "wPointerId" / Int16ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=159, version=0)
class Microsoft_Windows_Win32k_159_0(Etw):
    pattern = Struct(
        "wCursorId" / Int16ul,
        "wPointerId" / Int16ul,
        "dwReason" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=160, version=0)
class Microsoft_Windows_Win32k_160_0(Etw):
    pattern = Struct(
        "Orientation" / Int32ul,
        "SensorOriginated" / Int8ul,
        "ActiveProcessId" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=161, version=0)
class Microsoft_Windows_Win32k_161_0(Etw):
    pattern = Struct(
        "Orientation" / Int32ul,
        "SensorOriginated" / Int8ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=162, version=0)
class Microsoft_Windows_Win32k_162_0(Etw):
    pattern = Struct(
        "pBatch" / Int64ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=163, version=0)
class Microsoft_Windows_Win32k_163_0(Etw):
    pattern = Struct(
        "AcquireQpcCounts" / Int64ul,
        "AcquireTimeUs" / Int32ul,
        "Token" / Int64ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=164, version=0)
class Microsoft_Windows_Win32k_164_0(Etw):
    pattern = Struct(
        "AcquireQpcCounts" / Int64ul,
        "AcquireTimeUs" / Int32ul,
        "Token" / Int64ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=165, version=0)
class Microsoft_Windows_Win32k_165_0(Etw):
    pattern = Struct(
        "AcquireQpcCounts" / Int64ul,
        "AcquireTimeUs" / Int32ul,
        "Token" / Int64ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=166, version=0)
class Microsoft_Windows_Win32k_166_0(Etw):
    pattern = Struct(
        "AcquireQpcCounts" / Int64ul,
        "AcquireTimeUs" / Int32ul,
        "Token" / Int64ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=167, version=0)
class Microsoft_Windows_Win32k_167_0(Etw):
    pattern = Struct(
        "HoldQpcCounts" / Int64ul,
        "HoldTimeMs" / Int32ul,
        "Token" / Int64ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=168, version=0)
class Microsoft_Windows_Win32k_168_0(Etw):
    pattern = Struct(
        "pti" / Int64ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=169, version=0)
class Microsoft_Windows_Win32k_169_0(Etw):
    pattern = Struct(
        "pti" / Int64ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=171, version=0)
class Microsoft_Windows_Win32k_171_0(Etw):
    pattern = Struct(
        "Info" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=172, version=0)
class Microsoft_Windows_Win32k_172_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul,
        "TimeSinceInputRemoveMs" / Int32ul,
        "TimeSinceOldestInputMs" / Int32ul,
        "ClassName" / WString,
        "TopLevelClassName" / WString,
        "PackageMoniker" / WString,
        "AppUserModelId" / WString,
        "MessageId" / Int32ul,
        "WParam" / Int64ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=173, version=0)
class Microsoft_Windows_Win32k_173_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul,
        "DelayTimeMs" / Int32ul,
        "TimeSinceInputRemoveMs" / Int32ul,
        "TimeSinceOldestInputMs" / Int32ul,
        "ClassName" / WString,
        "TopLevelClassName" / WString,
        "PackageMoniker" / WString,
        "AppUserModelId" / WString,
        "MessageId" / Int32ul,
        "WParam" / Int64ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=176, version=0)
class Microsoft_Windows_Win32k_176_0(Etw):
    pattern = Struct(
        "ulContactId" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=177, version=0)
class Microsoft_Windows_Win32k_177_0(Etw):
    pattern = Struct(
        "ulContactId" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=178, version=0)
class Microsoft_Windows_Win32k_178_0(Etw):
    pattern = Struct(
        "hLogicalSurface" / Int64ul,
        "RgnType" / Int32ul,
        "rcBounds" / Int16sl,
        "NumRects" / Int32ul,
        "rcData" / Int64sl
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=179, version=0)
class Microsoft_Windows_Win32k_179_0(Etw):
    pattern = Struct(
        "hLogicalSurface" / Int64ul,
        "RgnType" / Int32ul,
        "rcBounds" / Int16sl,
        "NumRects" / Int32ul,
        "rcData" / Int64sl
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=180, version=0)
class Microsoft_Windows_Win32k_180_0(Etw):
    pattern = Struct(
        "hwnd" / Int64ul,
        "DirtyLeft" / Int32ul,
        "DirtyTop" / Int32ul,
        "DirtyRight" / Int32ul,
        "DirtyBottom" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=181, version=0)
class Microsoft_Windows_Win32k_181_0(Etw):
    pattern = Struct(
        "hwnd" / Int64ul,
        "DirtyLeft" / Int32ul,
        "DirtyTop" / Int32ul,
        "DirtyRight" / Int32ul,
        "DirtyBottom" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=182, version=0)
class Microsoft_Windows_Win32k_182_0(Etw):
    pattern = Struct(
        "hwnd" / Int64ul,
        "Offsetx" / Int32sl,
        "Offsety" / Int32sl
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=183, version=0)
class Microsoft_Windows_Win32k_183_0(Etw):
    pattern = Struct(
        "hLogicalSurface" / Int64ul,
        "RgnType" / Int32ul,
        "rcBounds" / Int16sl,
        "NumRects" / Int32ul,
        "rcData" / Int64sl
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=184, version=0)
class Microsoft_Windows_Win32k_184_0(Etw):
    pattern = Struct(
        "FrameId" / Int32ul,
        "PointerCount" / Int32ul,
        "PendingPointerCount" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=185, version=0)
class Microsoft_Windows_Win32k_185_0(Etw):
    pattern = Struct(
        "FrameId" / Int32ul,
        "PointerCount" / Int32ul,
        "PendingPointerCount" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=186, version=0)
class Microsoft_Windows_Win32k_186_0(Etw):
    pattern = Struct(
        "wCursorId" / Int16ul,
        "wPointerId" / Int16ul,
        "dwReason" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=187, version=0)
class Microsoft_Windows_Win32k_187_0(Etw):
    pattern = Struct(
        "Hwnd" / Int64ul,
        "uId" / Int32ul,
        "uElapse" / Int32ul,
        "uCoalescingTolerance" / Int32ul,
        "uType" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=188, version=0)
class Microsoft_Windows_Win32k_188_0(Etw):
    pattern = Struct(
        "Hwnd" / Int64ul,
        "uId" / Int32ul,
        "uElapse" / Int32ul,
        "uType" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=189, version=0)
class Microsoft_Windows_Win32k_189_0(Etw):
    pattern = Struct(
        "Hwnd" / Int64ul,
        "uId" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=190, version=0)
class Microsoft_Windows_Win32k_190_0(Etw):
    pattern = Struct(
        "Hwnd" / Int64ul,
        "uId" / Int32ul,
        "uElapse" / Int32ul,
        "uCoalescingTolerance" / Int32ul,
        "uType" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=191, version=0)
class Microsoft_Windows_Win32k_191_0(Etw):
    pattern = Struct(
        "Hwnd" / Int64ul,
        "uId" / Int32ul,
        "uElapse" / Int32ul,
        "uType" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=198, version=0)
class Microsoft_Windows_Win32k_198_0(Etw):
    pattern = Struct(
        "ScanTime" / Int32sl,
        "dwTime" / Int32sl,
        "QPC" / Int64ul,
        "XRawPosition" / Int32sl,
        "YRawPosition" / Int32sl,
        "XPredictedPosition" / Int32sl,
        "YPredictedPosition" / Int32sl
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=199, version=0)
class Microsoft_Windows_Win32k_199_0(Etw):
    pattern = Struct(
        "wCursorId" / Int16ul,
        "wPointerId" / Int16ul,
        "dwReason" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=200, version=0)
class Microsoft_Windows_Win32k_200_0(Etw):
    pattern = Struct(
        "wCursorId" / Int16ul,
        "wPointerId" / Int16ul,
        "dwReason" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=201, version=1)
class Microsoft_Windows_Win32k_201_1(Etw):
    pattern = Struct(
        "pToken" / Int64ul,
        "pCompositionSurfaceObject" / Int64ul,
        "SwapChainIndex" / Int32ul,
        "PresentCount" / Int64ul,
        "CompositionSurfaceLuid" / Int64ul,
        "BindId" / Int64ul,
        "FlipInterval" / Int32ul,
        "DestWidth" / Int32ul,
        "DestHeight" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=202, version=0)
class Microsoft_Windows_Win32k_202_0(Etw):
    pattern = Struct(
        "pCompositionSurfaceObject" / Int64ul,
        "SwapChainIndex" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=203, version=0)
class Microsoft_Windows_Win32k_203_0(Etw):
    pattern = Struct(
        "CallbackCount" / Int8sl,
        "pqmsg" / Int64ul,
        "pti" / Int64ul,
        "dwQEvent" / Int32ul,
        "hwnd" / Int64ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=204, version=0)
class Microsoft_Windows_Win32k_204_0(Etw):
    pattern = Struct(
        "CallbackCount" / Int8sl,
        "pqmsg" / Int64ul,
        "pti" / Int64ul,
        "dwQEvent" / Int32ul,
        "hwnd" / Int64ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=213, version=0)
class Microsoft_Windows_Win32k_213_0(Etw):
    pattern = Struct(
        "data" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=215, version=0)
class Microsoft_Windows_Win32k_215_0(Etw):
    pattern = Struct(
        "ConvertibleState" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=216, version=0)
class Microsoft_Windows_Win32k_216_0(Etw):
    pattern = Struct(
        "DockState" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=217, version=0)
class Microsoft_Windows_Win32k_217_0(Etw):
    pattern = Struct(
        "ScanTime" / Int32ul,
        "dwTime" / Int32ul,
        "QPCTime" / Int64ul,
        "XLogicalT" / Int32ul,
        "YLogicalT" / Int32ul,
        "XLogicalC" / Int32ul,
        "YLogicalC" / Int32ul,
        "XHimetricT" / Int32ul,
        "YHimetricT" / Int32ul,
        "Button" / Int8ul,
        "Count" / Int32ul,
        "Identifier" / Int32ul,
        "Width" / Int32ul,
        "Height" / Int32ul,
        "Confidence" / Int8ul,
        "Pressure" / Int32ul,
        "DeviceType" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=218, version=0)
class Microsoft_Windows_Win32k_218_0(Etw):
    pattern = Struct(
        "InputTransformList" / Int64ul,
        "PerformanceCount" / Int64ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=219, version=0)
class Microsoft_Windows_Win32k_219_0(Etw):
    pattern = Struct(
        "CallbackCount" / Int8sl,
        "WakeReason" / Int32sl
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=223, version=0)
class Microsoft_Windows_Win32k_223_0(Etw):
    pattern = Struct(
        "Hwnd" / Int64ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=224, version=0)
class Microsoft_Windows_Win32k_224_0(Etw):
    pattern = Struct(
        "hDCompInputHandle" / Int64ul,
        "Hwnd" / Int64ul,
        "XformQPCTime" / Int64ul,
        "XformStored" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=225, version=0)
class Microsoft_Windows_Win32k_225_0(Etw):
    pattern = Struct(
        "Hwnd" / Int64ul,
        "XformQPCTime" / Int64ul,
        "XformUpdated" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=233, version=0)
class Microsoft_Windows_Win32k_233_0(Etw):
    pattern = Struct(
        "LastKeyDownTime" / Int32ul,
        "LastKeyUpTime" / Int32ul,
        "TapTime" / Int32ul,
        "Blocked" / Int8ul,
        "Feature" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=236, version=0)
class Microsoft_Windows_Win32k_236_0(Etw):
    pattern = Struct(
        "deviceType" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=241, version=0)
class Microsoft_Windows_Win32k_241_0(Etw):
    pattern = Struct(
        "ContactId" / Int32ul,
        "OnUp" / Int8ul,
        "NeedsUp" / Int8ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=242, version=0)
class Microsoft_Windows_Win32k_242_0(Etw):
    pattern = Struct(
        "ContactId" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=249, version=0)
class Microsoft_Windows_Win32k_249_0(Etw):
    pattern = Struct(
        "CurtainsOn" / Int8ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=250, version=0)
class Microsoft_Windows_Win32k_250_0(Etw):
    pattern = Struct(
        "Top" / Int32ul,
        "Left" / Int32ul,
        "Right" / Int32ul,
        "Enabled" / Int8ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=254, version=0)
class Microsoft_Windows_Win32k_254_0(Etw):
    pattern = Struct(
        "RenderSourceProcessName" / CString,
        "RenderSourcePackageName" / WString,
        "RenderTargetProcessName" / CString,
        "RenderTargetPackageName" / WString
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=255, version=0)
class Microsoft_Windows_Win32k_255_0(Etw):
    pattern = Struct(
        "iCursorDim" / Int32ul,
        "cx" / Int32ul,
        "cy" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=258, version=0)
class Microsoft_Windows_Win32k_258_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "NewProcessId" / Int32ul,
        "NewProcessCreateTime" / Int64ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=259, version=0)
class Microsoft_Windows_Win32k_259_0(Etw):
    pattern = Struct(
        "SessionId" / Int32ul,
        "OldProcessId" / Int32ul,
        "OldProcessCreateTime" / Int64ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=260, version=0)
class Microsoft_Windows_Win32k_260_0(Etw):
    pattern = Struct(
        "SourceProcessName" / WString,
        "SourceType" / Int32ul,
        "FontSourcePath" / WString,
        "Blocked" / Int8ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=301, version=0)
class Microsoft_Windows_Win32k_301_0(Etw):
    pattern = Struct(
        "pCompositionSurfaceObject" / Int64ul,
        "SwapChainIndex" / Int32ul,
        "PresentCount" / Int32ul,
        "FenceValue" / Int64ul,
        "NewState" / Int32ul,
        "IndependentFlip" / Int8ul,
        "SkipIndependentFlip" / Int8ul,
        "CompositionSurfaceLuid" / Int64ul,
        "BindId" / Int64ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=400, version=0)
class Microsoft_Windows_Win32k_400_0(Etw):
    pattern = Struct(
        "channelHandle" / Int32ul,
        "pBatch" / Int64ul,
        "batchID" / Int32ul,
        "submissionTime" / Int64ul,
        "submissionDeadline" / Int64ul,
        "deferReason" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=412, version=0)
class Microsoft_Windows_Win32k_412_0(Etw):
    pattern = Struct(
        "hConnection" / Int64ul,
        "SyncRefreshCount" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=413, version=0)
class Microsoft_Windows_Win32k_413_0(Etw):
    pattern = Struct(
        "SyncRefreshCount" / Int32ul,
        "PresentCount" / Int32ul,
        "CompositionSurfaceLuid" / Int64ul,
        "BindId" / Int64ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=414, version=0)
class Microsoft_Windows_Win32k_414_0(Etw):
    pattern = Struct(
        "FrameId" / Int32ul,
        "PointerCount" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=415, version=0)
class Microsoft_Windows_Win32k_415_0(Etw):
    pattern = Struct(
        "FrameId" / Int32ul,
        "PointerCount" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=416, version=0)
class Microsoft_Windows_Win32k_416_0(Etw):
    pattern = Struct(
        "AcquireQpcCounts" / Int64ul,
        "AcquireTimeUs" / Int32ul,
        "Token" / Int64ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=417, version=0)
class Microsoft_Windows_Win32k_417_0(Etw):
    pattern = Struct(
        "AcquireQpcCounts" / Int64ul,
        "AcquireTimeUs" / Int32ul,
        "Token" / Int64ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=418, version=0)
class Microsoft_Windows_Win32k_418_0(Etw):
    pattern = Struct(
        "Location" / Int32sl
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=419, version=0)
class Microsoft_Windows_Win32k_419_0(Etw):
    pattern = Struct(
        "Location" / Int32sl
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=420, version=0)
class Microsoft_Windows_Win32k_420_0(Etw):
    pattern = Struct(
        "Location" / Int32sl
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=421, version=0)
class Microsoft_Windows_Win32k_421_0(Etw):
    pattern = Struct(
        "Location" / Int32sl
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=422, version=0)
class Microsoft_Windows_Win32k_422_0(Etw):
    pattern = Struct(
        "Location" / Int32sl
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=423, version=0)
class Microsoft_Windows_Win32k_423_0(Etw):
    pattern = Struct(
        "Location" / Int32sl
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=424, version=0)
class Microsoft_Windows_Win32k_424_0(Etw):
    pattern = Struct(
        "Location" / Int32sl
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=425, version=0)
class Microsoft_Windows_Win32k_425_0(Etw):
    pattern = Struct(
        "Location" / Int32sl
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=426, version=0)
class Microsoft_Windows_Win32k_426_0(Etw):
    pattern = Struct(
        "SourceProcessId" / Int32ul,
        "SourceThreadId" / Int32ul,
        "SourceProcessName" / CString,
        "DestinationHwnd" / Int64ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=427, version=0)
class Microsoft_Windows_Win32k_427_0(Etw):
    pattern = Struct(
        "SyscallName" / CString,
        "AppContainerSid" / WString,
        "ProcessCommandLine" / WString,
        "FilterSetId" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=428, version=0)
class Microsoft_Windows_Win32k_428_0(Etw):
    pattern = Struct(
        "SPIAction" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=429, version=0)
class Microsoft_Windows_Win32k_429_0(Etw):
    pattern = Struct(
        "Instance" / Int64ul,
        "WatchdogType" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=430, version=0)
class Microsoft_Windows_Win32k_430_0(Etw):
    pattern = Struct(
        "Instance" / Int64ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=431, version=0)
class Microsoft_Windows_Win32k_431_0(Etw):
    pattern = Struct(
        "CalloutType" / Int32sl,
        "Status" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=432, version=0)
class Microsoft_Windows_Win32k_432_0(Etw):
    pattern = Struct(
        "CalloutType" / Int32sl,
        "Status" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=433, version=0)
class Microsoft_Windows_Win32k_433_0(Etw):
    pattern = Struct(
        "PowerTaskState" / Int32sl,
        "Status" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=434, version=0)
class Microsoft_Windows_Win32k_434_0(Etw):
    pattern = Struct(
        "PowerTaskState" / Int32sl,
        "Status" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=435, version=0)
class Microsoft_Windows_Win32k_435_0(Etw):
    pattern = Struct(
        "EventNumber" / Int32sl,
        "Code" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=436, version=0)
class Microsoft_Windows_Win32k_436_0(Etw):
    pattern = Struct(
        "EventNumber" / Int32sl,
        "Code" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=437, version=0)
class Microsoft_Windows_Win32k_437_0(Etw):
    pattern = Struct(
        "Address" / Int64ul,
        "EventNumber" / Int32sl,
        "Code" / Int64ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=438, version=0)
class Microsoft_Windows_Win32k_438_0(Etw):
    pattern = Struct(
        "Address" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=439, version=0)
class Microsoft_Windows_Win32k_439_0(Etw):
    pattern = Struct(
        "Address" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=440, version=0)
class Microsoft_Windows_Win32k_440_0(Etw):
    pattern = Struct(
        "Address" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=441, version=0)
class Microsoft_Windows_Win32k_441_0(Etw):
    pattern = Struct(
        "NeedWaitForRit" / Int8ul,
        "NeedPowerOnGdi" / Int8ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=443, version=0)
class Microsoft_Windows_Win32k_443_0(Etw):
    pattern = Struct(
        "Channel" / Int32ul,
        "InternalHandle" / Int32ul,
        "ExternalHandle" / Int32ul,
        "InternalHandleAndChannel" / Int64ul,
        "ExternalHandleAndChannel" / Int64ul,
        "ResourceType" / Int32ul,
        "CreateShared" / Int8ul,
        "OpenShared" / Int8ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=444, version=0)
class Microsoft_Windows_Win32k_444_0(Etw):
    pattern = Struct(
        "Channel" / Int32ul,
        "InternalHandle" / Int32ul,
        "ExternalHandle" / Int32ul,
        "ResourceType" / Int32ul,
        "PropertyId" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=445, version=0)
class Microsoft_Windows_Win32k_445_0(Etw):
    pattern = Struct(
        "CommandType" / Int32ul,
        "status" / Int64ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=446, version=0)
class Microsoft_Windows_Win32k_446_0(Etw):
    pattern = Struct(
        "CommandsCount" / Int64ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=450, version=0)
class Microsoft_Windows_Win32k_450_0(Etw):
    pattern = Struct(
        "Channel" / Int32ul,
        "VisualInternalHandle" / Int32ul,
        "InteractionInternalHandle" / Int32ul,
        "VisualInternalHandleAndChannel" / Int64ul,
        "InteractionInternalHandleAndChannel" / Int64ul,
        "ResourceType" / Int32ul,
        "DefaultInteraction" / Int8ul,
        "Reason" / WString
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=451, version=0)
class Microsoft_Windows_Win32k_451_0(Etw):
    pattern = Struct(
        "Channel" / Int32ul,
        "VisualInternalHandle" / Int32ul,
        "InteractionInternalHandle" / Int32ul,
        "VisualInternalHandleAndChannel" / Int64ul,
        "InteractionInternalHandleAndChannel" / Int64ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=452, version=0)
class Microsoft_Windows_Win32k_452_0(Etw):
    pattern = Struct(
        "HandleValue" / Int64ul,
        "HandleType" / Int32ul,
        "SessionId" / Int32ul,
        "OwnerProcessId" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=453, version=0)
class Microsoft_Windows_Win32k_453_0(Etw):
    pattern = Struct(
        "HandleValue" / Int64ul,
        "HandleType" / Int32ul,
        "SessionId" / Int32ul,
        "OwnerProcessId" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=454, version=0)
class Microsoft_Windows_Win32k_454_0(Etw):
    pattern = Struct(
        "HandleValue" / Int64ul,
        "HandleType" / Int32ul,
        "SessionId" / Int32ul,
        "OwnerProcessId" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=455, version=0)
class Microsoft_Windows_Win32k_455_0(Etw):
    pattern = Struct(
        "HandleValue" / Int64ul,
        "HandleType" / Int32ul,
        "SessionId" / Int32ul,
        "OwnerProcessId" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=456, version=0)
class Microsoft_Windows_Win32k_456_0(Etw):
    pattern = Struct(
        "HandleValue" / Int64ul,
        "HandleType" / Int32ul,
        "SessionId" / Int32ul,
        "OwnerProcessId" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=457, version=0)
class Microsoft_Windows_Win32k_457_0(Etw):
    pattern = Struct(
        "HandleValue" / Int64ul,
        "HandleType" / Int32ul,
        "SessionId" / Int32ul,
        "OwnerProcessId" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=458, version=0)
class Microsoft_Windows_Win32k_458_0(Etw):
    pattern = Struct(
        "PreviousHandleValue" / Int64ul,
        "NewHandleValue" / Int64ul,
        "HandleType" / Int32ul,
        "SessionId" / Int32ul,
        "OwnerProcessId" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=500, version=0)
class Microsoft_Windows_Win32k_500_0(Etw):
    pattern = Struct(
        "PresentId" / Int64ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=501, version=0)
class Microsoft_Windows_Win32k_501_0(Etw):
    pattern = Struct(
        "PresentId" / Int64ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=502, version=0)
class Microsoft_Windows_Win32k_502_0(Etw):
    pattern = Struct(
        "PresentId" / Int64ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=503, version=0)
class Microsoft_Windows_Win32k_503_0(Etw):
    pattern = Struct(
        "PresentId" / Int64ul,
        "TokenResult" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=1000, version=0)
class Microsoft_Windows_Win32k_1000_0(Etw):
    pattern = Struct(
        "eventMin" / Int32ul,
        "eventMax" / Int32ul,
        "idEventProcess" / Int32ul,
        "idEventThread" / Int32ul,
        "Flags" / Int32ul,
        "HookInstance" / Int64ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=1001, version=0)
class Microsoft_Windows_Win32k_1001_0(Etw):
    pattern = Struct(
        "ReturnValue" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=1002, version=0)
class Microsoft_Windows_Win32k_1002_0(Etw):
    pattern = Struct(
        "FilterType" / Int32ul,
        "pstrLib" / WString,
        "hmod" / Int64ul,
        "pfnFilterProc" / Int64ul,
        "ReturnValue" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=1003, version=0)
class Microsoft_Windows_Win32k_1003_0(Etw):
    pattern = Struct(
        "PID" / Int32ul,
        "MsSinceLastKeyEvent" / Int32ul,
        "BackgroundCallCount" / Int32ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=2000, version=0)
class Microsoft_Windows_Win32k_2000_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul,
        "ProcessId" / Int32ul,
        "ProcessCreateTime" / Int64ul,
        "ProcessStartKey" / Int64ul
    )


@declare(guid=guid("8c416c79-d49b-4f01-a467-e56d3aa8234c"), event_id=10002, version=0)
class Microsoft_Windows_Win32k_10002_0(Etw):
    pattern = Struct(
        "hWnd" / Int32ul,
        "Packed_High_Height_Low_Width" / Int32ul,
        "PRAID" / WString,
        "PackageFullName" / WString
    )

