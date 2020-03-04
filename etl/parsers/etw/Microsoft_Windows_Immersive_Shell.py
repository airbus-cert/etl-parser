# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Immersive-Shell
GUID : 315a8872-923e-4ea2-9889-33cd4754bf64
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=101, version=0)
class Microsoft_Windows_Immersive_Shell_101_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=102, version=0)
class Microsoft_Windows_Immersive_Shell_102_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=111, version=0)
class Microsoft_Windows_Immersive_Shell_111_0(Etw):
    pattern = Struct(
        "TableEntryIndex" / Int32ul,
        "InitalizationStep" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=112, version=0)
class Microsoft_Windows_Immersive_Shell_112_0(Etw):
    pattern = Struct(
        "TableEntryIndex" / Int32ul,
        "InitalizationStep" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=121, version=0)
class Microsoft_Windows_Immersive_Shell_121_0(Etw):
    pattern = Struct(
        "SystemModeFrom" / Int32sl,
        "SystemSubModeFrom" / Int32sl,
        "SystemModeTo" / Int32sl,
        "SystemSubModeTo" / Int32sl
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=122, version=0)
class Microsoft_Windows_Immersive_Shell_122_0(Etw):
    pattern = Struct(
        "SystemModeFrom" / Int32sl,
        "SystemSubModeFrom" / Int32sl,
        "SystemModeTo" / Int32sl,
        "SystemSubModeTo" / Int32sl
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=123, version=0)
class Microsoft_Windows_Immersive_Shell_123_0(Etw):
    pattern = Struct(
        "ZbandFrom" / Int32sl,
        "ZbandTo" / Int32sl
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=124, version=0)
class Microsoft_Windows_Immersive_Shell_124_0(Etw):
    pattern = Struct(
        "ZbandFrom" / Int32sl,
        "ZbandTo" / Int32sl
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=125, version=0)
class Microsoft_Windows_Immersive_Shell_125_0(Etw):
    pattern = Struct(
        "ListenerIndex" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=126, version=0)
class Microsoft_Windows_Immersive_Shell_126_0(Etw):
    pattern = Struct(
        "ListenerIndex" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=141, version=0)
class Microsoft_Windows_Immersive_Shell_141_0(Etw):
    pattern = Struct(
        "ListenerIndex" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=142, version=0)
class Microsoft_Windows_Immersive_Shell_142_0(Etw):
    pattern = Struct(
        "ListenerIndex" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=153, version=0)
class Microsoft_Windows_Immersive_Shell_153_0(Etw):
    pattern = Struct(
        "BandID" / Int32ul,
        "OuterWorkArea_left" / Int32sl,
        "OuterWorkArea_top" / Int32sl,
        "OuterWorkArea_right" / Int32sl,
        "OuterWorkArea_bottom" / Int32sl,
        "InnerWorkArea_left" / Int32sl,
        "InnerWorkArea_top" / Int32sl,
        "InnerWorkArea_right" / Int32sl,
        "InnerWorkArea_bottom" / Int32sl
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=156, version=0)
class Microsoft_Windows_Immersive_Shell_156_0(Etw):
    pattern = Struct(
        "InvalidationReason" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=161, version=0)
class Microsoft_Windows_Immersive_Shell_161_0(Etw):
    pattern = Struct(
        "FocusedHWND" / Int64ul,
        "IHMPosition_left" / Int32sl,
        "IHMPosition_top" / Int32sl,
        "IHMPosition_right" / Int32sl,
        "IHMPosition_bottom" / Int32sl
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=162, version=0)
class Microsoft_Windows_Immersive_Shell_162_0(Etw):
    pattern = Struct(
        "FocusedHWND" / Int64ul,
        "IHMPosition_left" / Int32sl,
        "IHMPosition_top" / Int32sl,
        "IHMPosition_right" / Int32sl,
        "IHMPosition_bottom" / Int32sl
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=163, version=0)
class Microsoft_Windows_Immersive_Shell_163_0(Etw):
    pattern = Struct(
        "FocusedHWND" / Int64ul,
        "IHMPosition_left" / Int32sl,
        "IHMPosition_top" / Int32sl,
        "IHMPosition_right" / Int32sl,
        "IHMPosition_bottom" / Int32sl
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=165, version=0)
class Microsoft_Windows_Immersive_Shell_165_0(Etw):
    pattern = Struct(
        "NotificationType" / Int32sl,
        "FocusedHWND" / Int64ul,
        "IHMPosition_left" / Int32sl,
        "IHMPosition_top" / Int32sl,
        "IHMPosition_right" / Int32sl,
        "IHMPosition_bottom" / Int32sl
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=166, version=0)
class Microsoft_Windows_Immersive_Shell_166_0(Etw):
    pattern = Struct(
        "NotificationType" / Int32sl,
        "FocusedHWND" / Int64ul,
        "IHMPosition_left" / Int32sl,
        "IHMPosition_top" / Int32sl,
        "IHMPosition_right" / Int32sl,
        "IHMPosition_bottom" / Int32sl
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=171, version=0)
class Microsoft_Windows_Immersive_Shell_171_0(Etw):
    pattern = Struct(
        "AppID" / WString,
        "ApplicationState" / Int32ul,
        "HasActionsMenu" / Int8ul,
        "DesktopTabletModeState" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=173, version=0)
class Microsoft_Windows_Immersive_Shell_173_0(Etw):
    pattern = Struct(
        "Window" / Int32sl,
        "Title" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=181, version=0)
class Microsoft_Windows_Immersive_Shell_181_0(Etw):
    pattern = Struct(
        "Left" / Int32sl,
        "Top" / Int32sl,
        "UIName" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=1013, version=0)
class Microsoft_Windows_Immersive_Shell_1013_0(Etw):
    pattern = Struct(
        "ApplicationId" / WString,
        "NotificationId" / Int32ul,
        "HRESULT" / Int32ul,
        "UnprocessedResourceString" / WString,
        "ProcessedResourceString" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=1027, version=0)
class Microsoft_Windows_Immersive_Shell_1027_0(Etw):
    pattern = Struct(
        "AppID" / WString,
        "NotificationID" / Int32ul,
        "TemplateName" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=1201, version=0)
class Microsoft_Windows_Immersive_Shell_1201_0(Etw):
    pattern = Struct(
        "AppID" / WString,
        "NotificationID" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=1202, version=0)
class Microsoft_Windows_Immersive_Shell_1202_0(Etw):
    pattern = Struct(
        "AppID" / WString,
        "NotificationID" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=1203, version=0)
class Microsoft_Windows_Immersive_Shell_1203_0(Etw):
    pattern = Struct(
        "AppID" / WString,
        "NotificationID" / Int32ul,
        "HRESULT" / Int32ul,
        "Node" / WString,
        "Line" / Int32sl,
        "Position" / Int32sl
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=1310, version=0)
class Microsoft_Windows_Immersive_Shell_1310_0(Etw):
    pattern = Struct(
        "AppUserModelID" / WString,
        "Left" / Int32ul,
        "Top" / Int32ul,
        "Right" / Int32ul,
        "Bottom" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=1317, version=0)
class Microsoft_Windows_Immersive_Shell_1317_0(Etw):
    pattern = Struct(
        "AppUserModelId" / WString,
        "Arguments" / WString,
        "NotificationTargetId" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=1318, version=0)
class Microsoft_Windows_Immersive_Shell_1318_0(Etw):
    pattern = Struct(
        "AppUserModelId" / WString,
        "Arguments" / WString,
        "NotificationTargetId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=1402, version=0)
class Microsoft_Windows_Immersive_Shell_1402_0(Etw):
    pattern = Struct(
        "AppUserModelID" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=1408, version=0)
class Microsoft_Windows_Immersive_Shell_1408_0(Etw):
    pattern = Struct(
        "AppUserModelID" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=1462, version=0)
class Microsoft_Windows_Immersive_Shell_1462_0(Etw):
    pattern = Struct(
        "ID" / Int32ul,
        "Left" / Int32sl,
        "Top" / Int32sl,
        "Right" / Int32sl,
        "Bottom" / Int32sl
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=1463, version=0)
class Microsoft_Windows_Immersive_Shell_1463_0(Etw):
    pattern = Struct(
        "ID" / Int32ul,
        "Left" / Int32sl,
        "Top" / Int32sl,
        "Right" / Int32sl,
        "Bottom" / Int32sl
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=1477, version=0)
class Microsoft_Windows_Immersive_Shell_1477_0(Etw):
    pattern = Struct(
        "HashValue" / Int32ul,
        "HashInput" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=1601, version=0)
class Microsoft_Windows_Immersive_Shell_1601_0(Etw):
    pattern = Struct(
        "AppUserModelID" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=1602, version=0)
class Microsoft_Windows_Immersive_Shell_1602_0(Etw):
    pattern = Struct(
        "AppUserModelID" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=1612, version=0)
class Microsoft_Windows_Immersive_Shell_1612_0(Etw):
    pattern = Struct(
        "StoreType" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=1614, version=0)
class Microsoft_Windows_Immersive_Shell_1614_0(Etw):
    pattern = Struct(
        "ApplicationId" / WString,
        "Arguments" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=1615, version=0)
class Microsoft_Windows_Immersive_Shell_1615_0(Etw):
    pattern = Struct(
        "AppID" / WString,
        "Event" / Int32sl
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=1618, version=0)
class Microsoft_Windows_Immersive_Shell_1618_0(Etw):
    pattern = Struct(
        "ApplicationId" / WString,
        "Arguments" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=1619, version=0)
class Microsoft_Windows_Immersive_Shell_1619_0(Etw):
    pattern = Struct(
        "AHE_TYPE" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=1621, version=0)
class Microsoft_Windows_Immersive_Shell_1621_0(Etw):
    pattern = Struct(
        "ApplicationId" / WString,
        "ExecutionState" / Int32ul,
        "AppState" / Int32ul,
        "Result" / Int32sl
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=1622, version=0)
class Microsoft_Windows_Immersive_Shell_1622_0(Etw):
    pattern = Struct(
        "Operation" / Int32ul,
        "TargetAppID" / WString,
        "RefAppID" / WString,
        "ModifyFlags" / Int32ul,
        "ViewOrSize" / Int32ul,
        "GroupName" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=1623, version=0)
class Microsoft_Windows_Immersive_Shell_1623_0(Etw):
    pattern = Struct(
        "ItemsToProcess" / Int32ul,
        "StartTask" / Int8ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=1624, version=0)
class Microsoft_Windows_Immersive_Shell_1624_0(Etw):
    pattern = Struct(
        "ItemsToProcess" / Int32ul,
        "Retry" / Int8ul,
        "FailedAttempts" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=1626, version=0)
class Microsoft_Windows_Immersive_Shell_1626_0(Etw):
    pattern = Struct(
        "AppID" / WString,
        "Result" / Int32sl
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=1627, version=0)
class Microsoft_Windows_Immersive_Shell_1627_0(Etw):
    pattern = Struct(
        "Package" / WString,
        "Result" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=1628, version=0)
class Microsoft_Windows_Immersive_Shell_1628_0(Etw):
    pattern = Struct(
        "Package" / WString,
        "Result" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=1631, version=0)
class Microsoft_Windows_Immersive_Shell_1631_0(Etw):
    pattern = Struct(
        "Package" / WString,
        "Result" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=1632, version=0)
class Microsoft_Windows_Immersive_Shell_1632_0(Etw):
    pattern = Struct(
        "ApplicationId" / WString,
        "FailedOperation" / WString,
        "Result" / Int32sl
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=1830, version=0)
class Microsoft_Windows_Immersive_Shell_1830_0(Etw):
    pattern = Struct(
        "Result" / Int32ul,
        "AppID" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=1833, version=0)
class Microsoft_Windows_Immersive_Shell_1833_0(Etw):
    pattern = Struct(
        "Result" / Int32ul,
        "AppID" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=1844, version=0)
class Microsoft_Windows_Immersive_Shell_1844_0(Etw):
    pattern = Struct(
        "Language" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=1845, version=0)
class Microsoft_Windows_Immersive_Shell_1845_0(Etw):
    pattern = Struct(
        "Language" / WString,
        "Result" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=1858, version=0)
class Microsoft_Windows_Immersive_Shell_1858_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=1864, version=0)
class Microsoft_Windows_Immersive_Shell_1864_0(Etw):
    pattern = Struct(
        "AppID" / WString,
        "NotificationID" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=1865, version=0)
class Microsoft_Windows_Immersive_Shell_1865_0(Etw):
    pattern = Struct(
        "ApplicationID" / WString,
        "NotificationID" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2100, version=0)
class Microsoft_Windows_Immersive_Shell_2100_0(Etw):
    pattern = Struct(
        "PickerType" / Int32ul,
        "Mode" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2110, version=0)
class Microsoft_Windows_Immersive_Shell_2110_0(Etw):
    pattern = Struct(
        "IsEnabled" / Int8ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2129, version=0)
class Microsoft_Windows_Immersive_Shell_2129_0(Etw):
    pattern = Struct(
        "TotalCount" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2130, version=0)
class Microsoft_Windows_Immersive_Shell_2130_0(Etw):
    pattern = Struct(
        "AppID" / WString,
        "PackageName" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2132, version=0)
class Microsoft_Windows_Immersive_Shell_2132_0(Etw):
    pattern = Struct(
        "AppID" / WString,
        "PackageName" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2133, version=0)
class Microsoft_Windows_Immersive_Shell_2133_0(Etw):
    pattern = Struct(
        "TotalCount" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2134, version=0)
class Microsoft_Windows_Immersive_Shell_2134_0(Etw):
    pattern = Struct(
        "AppID" / WString,
        "PackageName" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2136, version=0)
class Microsoft_Windows_Immersive_Shell_2136_0(Etw):
    pattern = Struct(
        "AppID" / WString,
        "PackageName" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2137, version=0)
class Microsoft_Windows_Immersive_Shell_2137_0(Etw):
    pattern = Struct(
        "TotalCount" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2138, version=0)
class Microsoft_Windows_Immersive_Shell_2138_0(Etw):
    pattern = Struct(
        "AppID" / WString,
        "PackageName" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2140, version=0)
class Microsoft_Windows_Immersive_Shell_2140_0(Etw):
    pattern = Struct(
        "AppID" / WString,
        "PackageName" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2141, version=0)
class Microsoft_Windows_Immersive_Shell_2141_0(Etw):
    pattern = Struct(
        "TotalCount" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2149, version=0)
class Microsoft_Windows_Immersive_Shell_2149_0(Etw):
    pattern = Struct(
        "TotalCount" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2153, version=0)
class Microsoft_Windows_Immersive_Shell_2153_0(Etw):
    pattern = Struct(
        "TotalCount" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2163, version=0)
class Microsoft_Windows_Immersive_Shell_2163_0(Etw):
    pattern = Struct(
        "IsCancelled" / Int8ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2168, version=0)
class Microsoft_Windows_Immersive_Shell_2168_0(Etw):
    pattern = Struct(
        "ClientAllowsUX" / Int8ul,
        "FileIsUpdated" / Int8ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2175, version=0)
class Microsoft_Windows_Immersive_Shell_2175_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2177, version=0)
class Microsoft_Windows_Immersive_Shell_2177_0(Etw):
    pattern = Struct(
        "ContentId" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2178, version=0)
class Microsoft_Windows_Immersive_Shell_2178_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2179, version=0)
class Microsoft_Windows_Immersive_Shell_2179_0(Etw):
    pattern = Struct(
        "FileName" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2201, version=0)
class Microsoft_Windows_Immersive_Shell_2201_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2203, version=0)
class Microsoft_Windows_Immersive_Shell_2203_0(Etw):
    pattern = Struct(
        "AppItemCount" / Int32ul,
        "TotalItemCount" / Int32ul,
        "Result" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2204, version=0)
class Microsoft_Windows_Immersive_Shell_2204_0(Etw):
    pattern = Struct(
        "Index" / Int32ul,
        "AppItemCount" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2205, version=0)
class Microsoft_Windows_Immersive_Shell_2205_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2206, version=0)
class Microsoft_Windows_Immersive_Shell_2206_0(Etw):
    pattern = Struct(
        "Index" / Int32ul,
        "AppItemCount" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2207, version=0)
class Microsoft_Windows_Immersive_Shell_2207_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2208, version=0)
class Microsoft_Windows_Immersive_Shell_2208_0(Etw):
    pattern = Struct(
        "Index" / Int32ul,
        "AppItemCount" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2209, version=0)
class Microsoft_Windows_Immersive_Shell_2209_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2215, version=0)
class Microsoft_Windows_Immersive_Shell_2215_0(Etw):
    pattern = Struct(
        "TargetCount" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2216, version=0)
class Microsoft_Windows_Immersive_Shell_2216_0(Etw):
    pattern = Struct(
        "Index" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2217, version=0)
class Microsoft_Windows_Immersive_Shell_2217_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2219, version=0)
class Microsoft_Windows_Immersive_Shell_2219_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2223, version=0)
class Microsoft_Windows_Immersive_Shell_2223_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2225, version=0)
class Microsoft_Windows_Immersive_Shell_2225_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2227, version=0)
class Microsoft_Windows_Immersive_Shell_2227_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2229, version=0)
class Microsoft_Windows_Immersive_Shell_2229_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2232, version=0)
class Microsoft_Windows_Immersive_Shell_2232_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2235, version=0)
class Microsoft_Windows_Immersive_Shell_2235_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2236, version=0)
class Microsoft_Windows_Immersive_Shell_2236_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2247, version=0)
class Microsoft_Windows_Immersive_Shell_2247_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2248, version=0)
class Microsoft_Windows_Immersive_Shell_2248_0(Etw):
    pattern = Struct(
        "HWND" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2249, version=0)
class Microsoft_Windows_Immersive_Shell_2249_0(Etw):
    pattern = Struct(
        "HWND" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2254, version=0)
class Microsoft_Windows_Immersive_Shell_2254_0(Etw):
    pattern = Struct(
        "Index" / Int32ul,
        "AppItemCount" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2255, version=0)
class Microsoft_Windows_Immersive_Shell_2255_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2259, version=0)
class Microsoft_Windows_Immersive_Shell_2259_0(Etw):
    pattern = Struct(
        "AppID" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2260, version=0)
class Microsoft_Windows_Immersive_Shell_2260_0(Etw):
    pattern = Struct(
        "AppID" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2263, version=0)
class Microsoft_Windows_Immersive_Shell_2263_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2265, version=0)
class Microsoft_Windows_Immersive_Shell_2265_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2267, version=0)
class Microsoft_Windows_Immersive_Shell_2267_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2269, version=0)
class Microsoft_Windows_Immersive_Shell_2269_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2271, version=0)
class Microsoft_Windows_Immersive_Shell_2271_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2302, version=0)
class Microsoft_Windows_Immersive_Shell_2302_0(Etw):
    pattern = Struct(
        "ShowMethod" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2303, version=0)
class Microsoft_Windows_Immersive_Shell_2303_0(Etw):
    pattern = Struct(
        "ShowMethod" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2315, version=0)
class Microsoft_Windows_Immersive_Shell_2315_0(Etw):
    pattern = Struct(
        "ViewFromGuid" / WString,
        "ViewToGuid" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2325, version=0)
class Microsoft_Windows_Immersive_Shell_2325_0(Etw):
    pattern = Struct(
        "RenderedTileCount" / Int32ul,
        "RealizedTileCount" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2327, version=0)
class Microsoft_Windows_Immersive_Shell_2327_0(Etw):
    pattern = Struct(
        "NumOfVisibleTiles" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2335, version=0)
class Microsoft_Windows_Immersive_Shell_2335_0(Etw):
    pattern = Struct(
        "ScenarioId" / Int32ul,
        "ScenarioName" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2336, version=0)
class Microsoft_Windows_Immersive_Shell_2336_0(Etw):
    pattern = Struct(
        "ScenarioId" / Int32ul,
        "ScenarioName" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2362, version=0)
class Microsoft_Windows_Immersive_Shell_2362_0(Etw):
    pattern = Struct(
        "HowDismiss" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2364, version=0)
class Microsoft_Windows_Immersive_Shell_2364_0(Etw):
    pattern = Struct(
        "HowDismissed" / Int32ul,
        "AppName" / WString,
        "PackageName" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2450, version=1)
class Microsoft_Windows_Immersive_Shell_2450_1(Etw):
    pattern = Struct(
        "PsmKey" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2451, version=1)
class Microsoft_Windows_Immersive_Shell_2451_1(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "PackageFullName" / WString,
        "AppUserModelId" / WString,
        "Packed_Hi_RequestedTimeoutExtensionMs16_Flags11_Crashed1_Throttled1_EnforceTimeout1_IsChild1_TimedOut1_Lo" / Int32ul,
        "Packed_Hi_ModeSwitchesToUnthrottledCount2_IoOpportunityTime100Ms10_CpuReadyTime100Ms10_CpuRunningTime100Ms10_Lo" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2463, version=1)
class Microsoft_Windows_Immersive_Shell_2463_1(Etw):
    pattern = Struct(
        "PsmKey" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2464, version=1)
class Microsoft_Windows_Immersive_Shell_2464_1(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "PackageFullName" / WString,
        "AppUserModelId" / WString,
        "PackedResumeDurationsMs_HiWordAppLoWordPackage" / Int32ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2468, version=0)
class Microsoft_Windows_Immersive_Shell_2468_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "Reason" / Int32ul,
        "HiFlags_LoAppCount" / Int32ul,
        "HiThreshold_LoCurrentMetric" / Int32ul,
        "SumOfPrivateWsOrSumOfSwapUsageOrPrivateModifiedSize" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2472, version=0)
class Microsoft_Windows_Immersive_Shell_2472_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "ResumeReason" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2473, version=0)
class Microsoft_Windows_Immersive_Shell_2473_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "OldState" / Int32ul,
        "NewState" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2474, version=0)
class Microsoft_Windows_Immersive_Shell_2474_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "UserRequest" / Int32ul,
        "ExecutionRequest" / Int32ul,
        "KernelRequest" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2480, version=0)
class Microsoft_Windows_Immersive_Shell_2480_0(Etw):
    pattern = Struct(
        "AppUserModelId" / WString,
        "Flags" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2481, version=0)
class Microsoft_Windows_Immersive_Shell_2481_0(Etw):
    pattern = Struct(
        "AppUserModelId" / WString,
        "PendingTaskCompletions" / Int32ul,
        "DeferredTerminate" / Int8ul,
        "Result" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2482, version=0)
class Microsoft_Windows_Immersive_Shell_2482_0(Etw):
    pattern = Struct(
        "PsmKey" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2483, version=0)
class Microsoft_Windows_Immersive_Shell_2483_0(Etw):
    pattern = Struct(
        "PsmKey" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2484, version=1)
class Microsoft_Windows_Immersive_Shell_2484_1(Etw):
    pattern = Struct(
        "PsmKey" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2486, version=1)
class Microsoft_Windows_Immersive_Shell_2486_1(Etw):
    pattern = Struct(
        "PsmKey" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2491, version=0)
class Microsoft_Windows_Immersive_Shell_2491_0(Etw):
    pattern = Struct(
        "TaskCompletionType" / Int32ul,
        "PackageFullName" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2492, version=0)
class Microsoft_Windows_Immersive_Shell_2492_0(Etw):
    pattern = Struct(
        "TaskCompletionType" / Int32ul,
        "PackageFullName" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2495, version=0)
class Microsoft_Windows_Immersive_Shell_2495_0(Etw):
    pattern = Struct(
        "PresentNonBlockingTaskCompletions" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2499, version=0)
class Microsoft_Windows_Immersive_Shell_2499_0(Etw):
    pattern = Struct(
        "Wakes" / Int32ul,
        "PsmKey" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2608, version=0)
class Microsoft_Windows_Immersive_Shell_2608_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2618, version=0)
class Microsoft_Windows_Immersive_Shell_2618_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2671, version=0)
class Microsoft_Windows_Immersive_Shell_2671_0(Etw):
    pattern = Struct(
        "CommandId" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2679, version=0)
class Microsoft_Windows_Immersive_Shell_2679_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2680, version=0)
class Microsoft_Windows_Immersive_Shell_2680_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2690, version=0)
class Microsoft_Windows_Immersive_Shell_2690_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2806, version=0)
class Microsoft_Windows_Immersive_Shell_2806_0(Etw):
    pattern = Struct(
        "ApplicationId" / WString,
        "ActivationParameters" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2823, version=0)
class Microsoft_Windows_Immersive_Shell_2823_0(Etw):
    pattern = Struct(
        "AppID" / WString,
        "NotificationID" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2824, version=0)
class Microsoft_Windows_Immersive_Shell_2824_0(Etw):
    pattern = Struct(
        "AppID" / WString,
        "NotificationID" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2825, version=0)
class Microsoft_Windows_Immersive_Shell_2825_0(Etw):
    pattern = Struct(
        "AppID" / WString,
        "NotificationID" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2827, version=0)
class Microsoft_Windows_Immersive_Shell_2827_0(Etw):
    pattern = Struct(
        "AppID" / WString,
        "NotificationID" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2829, version=0)
class Microsoft_Windows_Immersive_Shell_2829_0(Etw):
    pattern = Struct(
        "AppID" / WString,
        "NotificationID" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=2850, version=0)
class Microsoft_Windows_Immersive_Shell_2850_0(Etw):
    pattern = Struct(
        "AppID" / WString,
        "EncodedFilePath" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=3000, version=0)
class Microsoft_Windows_Immersive_Shell_3000_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=3001, version=0)
class Microsoft_Windows_Immersive_Shell_3001_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=3002, version=0)
class Microsoft_Windows_Immersive_Shell_3002_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=3003, version=0)
class Microsoft_Windows_Immersive_Shell_3003_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=3004, version=0)
class Microsoft_Windows_Immersive_Shell_3004_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=3005, version=0)
class Microsoft_Windows_Immersive_Shell_3005_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=3103, version=0)
class Microsoft_Windows_Immersive_Shell_3103_0(Etw):
    pattern = Struct(
        "ContainerIdentifier" / WString,
        "DeviceIdentifier" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=3150, version=0)
class Microsoft_Windows_Immersive_Shell_3150_0(Etw):
    pattern = Struct(
        "Duration" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=3151, version=0)
class Microsoft_Windows_Immersive_Shell_3151_0(Etw):
    pattern = Struct(
        "Duration" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=3152, version=0)
class Microsoft_Windows_Immersive_Shell_3152_0(Etw):
    pattern = Struct(
        "Duration" / Int32ul,
        "DeviceHardwareID" / WString,
        "Manufacturer" / WString,
        "ModelName" / WString,
        "PrimaryCategory" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=3153, version=0)
class Microsoft_Windows_Immersive_Shell_3153_0(Etw):
    pattern = Struct(
        "Duration" / Int32ul,
        "DeviceHardwareID" / WString,
        "Manufacturer" / WString,
        "ModelName" / WString,
        "PrimaryCategory" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=3154, version=0)
class Microsoft_Windows_Immersive_Shell_3154_0(Etw):
    pattern = Struct(
        "Duration" / Int32ul,
        "DeviceHardwareID" / WString,
        "Manufacturer" / WString,
        "ModelName" / WString,
        "PrimaryCategory" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=3155, version=0)
class Microsoft_Windows_Immersive_Shell_3155_0(Etw):
    pattern = Struct(
        "Duration" / Int32ul,
        "DeviceHardwareID" / WString,
        "Manufacturer" / WString,
        "ModelName" / WString,
        "PrimaryCategory" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=3156, version=0)
class Microsoft_Windows_Immersive_Shell_3156_0(Etw):
    pattern = Struct(
        "Duration" / Int32ul,
        "DeviceHardwareID" / WString,
        "Manufacturer" / WString,
        "ModelName" / WString,
        "PrimaryCategory" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=3157, version=0)
class Microsoft_Windows_Immersive_Shell_3157_0(Etw):
    pattern = Struct(
        "Duration" / Int32ul,
        "DeviceHardwareID" / WString,
        "Manufacturer" / WString,
        "ModelName" / WString,
        "PrimaryCategory" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=3200, version=0)
class Microsoft_Windows_Immersive_Shell_3200_0(Etw):
    pattern = Struct(
        "EdgeUiComponent" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=3203, version=0)
class Microsoft_Windows_Immersive_Shell_3203_0(Etw):
    pattern = Struct(
        "EdgeUiComponent" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=3204, version=0)
class Microsoft_Windows_Immersive_Shell_3204_0(Etw):
    pattern = Struct(
        "EdgeUiComponent" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=3205, version=0)
class Microsoft_Windows_Immersive_Shell_3205_0(Etw):
    pattern = Struct(
        "EdgeUiComponent" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=4015, version=0)
class Microsoft_Windows_Immersive_Shell_4015_0(Etw):
    pattern = Struct(
        "UriSchemeOrFileExtension" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=4018, version=0)
class Microsoft_Windows_Immersive_Shell_4018_0(Etw):
    pattern = Struct(
        "UriSchemeOrFileExtension" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=4020, version=0)
class Microsoft_Windows_Immersive_Shell_4020_0(Etw):
    pattern = Struct(
        "UriSchemeOrFileExtension" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=4022, version=0)
class Microsoft_Windows_Immersive_Shell_4022_0(Etw):
    pattern = Struct(
        "UriSchemeOrFileExtension" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=4023, version=0)
class Microsoft_Windows_Immersive_Shell_4023_0(Etw):
    pattern = Struct(
        "UriSchemeOrFileExtension" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=4024, version=0)
class Microsoft_Windows_Immersive_Shell_4024_0(Etw):
    pattern = Struct(
        "UriSchemeOrFileExtension" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=4302, version=0)
class Microsoft_Windows_Immersive_Shell_4302_0(Etw):
    pattern = Struct(
        "MonitorIdentity" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=4312, version=0)
class Microsoft_Windows_Immersive_Shell_4312_0(Etw):
    pattern = Struct(
        "MonitorIdentity" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=4313, version=0)
class Microsoft_Windows_Immersive_Shell_4313_0(Etw):
    pattern = Struct(
        "MonitorIdentity" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=4316, version=0)
class Microsoft_Windows_Immersive_Shell_4316_0(Etw):
    pattern = Struct(
        "MonitorIdentity" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=4317, version=0)
class Microsoft_Windows_Immersive_Shell_4317_0(Etw):
    pattern = Struct(
        "MonitorIdentity" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=4320, version=0)
class Microsoft_Windows_Immersive_Shell_4320_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=4325, version=0)
class Microsoft_Windows_Immersive_Shell_4325_0(Etw):
    pattern = Struct(
        "MonitorIdentity" / Int32ul,
        "HMonitor" / Int64ul,
        "Left" / Int32ul,
        "Top" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=4326, version=0)
class Microsoft_Windows_Immersive_Shell_4326_0(Etw):
    pattern = Struct(
        "MonitorIdentity" / Int32ul,
        "HMonitor" / Int64ul,
        "Left" / Int32ul,
        "Top" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=4668, version=0)
class Microsoft_Windows_Immersive_Shell_4668_0(Etw):
    pattern = Struct(
        "EntryID" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=4669, version=0)
class Microsoft_Windows_Immersive_Shell_4669_0(Etw):
    pattern = Struct(
        "EntryID" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=4677, version=0)
class Microsoft_Windows_Immersive_Shell_4677_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=5901, version=1)
class Microsoft_Windows_Immersive_Shell_5901_1(Etw):
    pattern = Struct(
        "AppID" / WString,
        "PackageMoniker" / WString,
        "SqmableContractID" / WString,
        "ExeName" / WString,
        "PreviousExecutionState" / Int32ul,
        "Opportunistic" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=5902, version=1)
class Microsoft_Windows_Immersive_Shell_5902_1(Etw):
    pattern = Struct(
        "AppID" / WString,
        "PackageMoniker" / WString,
        "SqmableContractID" / WString,
        "ExeName" / WString,
        "PreviousExecutionState" / Int32ul,
        "Opportunistic" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=5907, version=0)
class Microsoft_Windows_Immersive_Shell_5907_0(Etw):
    pattern = Struct(
        "ActivationOptions" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=5908, version=0)
class Microsoft_Windows_Immersive_Shell_5908_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=5909, version=0)
class Microsoft_Windows_Immersive_Shell_5909_0(Etw):
    pattern = Struct(
        "AppClosed" / Int8ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=5911, version=0)
class Microsoft_Windows_Immersive_Shell_5911_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=5913, version=0)
class Microsoft_Windows_Immersive_Shell_5913_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=5917, version=0)
class Microsoft_Windows_Immersive_Shell_5917_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=5919, version=0)
class Microsoft_Windows_Immersive_Shell_5919_0(Etw):
    pattern = Struct(
        "PackageActivationSettings" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=5921, version=0)
class Microsoft_Windows_Immersive_Shell_5921_0(Etw):
    pattern = Struct(
        "AppId" / WString,
        "ErrorCode" / Int32ul,
        "DialogId" / Guid
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=5922, version=0)
class Microsoft_Windows_Immersive_Shell_5922_0(Etw):
    pattern = Struct(
        "AppId" / WString,
        "ErrorCode" / Int32ul,
        "DialogId" / Guid,
        "DismissMethod" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=5924, version=0)
class Microsoft_Windows_Immersive_Shell_5924_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "TimeOutPeriod" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=5925, version=0)
class Microsoft_Windows_Immersive_Shell_5925_0(Etw):
    pattern = Struct(
        "PsmKey" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=5926, version=0)
class Microsoft_Windows_Immersive_Shell_5926_0(Etw):
    pattern = Struct(
        "PsmKey" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=5927, version=0)
class Microsoft_Windows_Immersive_Shell_5927_0(Etw):
    pattern = Struct(
        "PsmKey" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=5928, version=0)
class Microsoft_Windows_Immersive_Shell_5928_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "WaitSignal" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=5950, version=0)
class Microsoft_Windows_Immersive_Shell_5950_0(Etw):
    pattern = Struct(
        "AppId" / WString,
        "ContractId" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=5951, version=0)
class Microsoft_Windows_Immersive_Shell_5951_0(Etw):
    pattern = Struct(
        "AppId" / WString,
        "ContractId" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=5952, version=0)
class Microsoft_Windows_Immersive_Shell_5952_0(Etw):
    pattern = Struct(
        "AppId" / WString,
        "ContractId" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=5953, version=0)
class Microsoft_Windows_Immersive_Shell_5953_0(Etw):
    pattern = Struct(
        "AppId" / WString,
        "ContractId" / WString,
        "PackageFamilyName" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=5954, version=0)
class Microsoft_Windows_Immersive_Shell_5954_0(Etw):
    pattern = Struct(
        "AppId" / WString,
        "ContractId" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=5955, version=0)
class Microsoft_Windows_Immersive_Shell_5955_0(Etw):
    pattern = Struct(
        "AppId" / WString,
        "ContractId" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=5956, version=0)
class Microsoft_Windows_Immersive_Shell_5956_0(Etw):
    pattern = Struct(
        "AppId" / WString,
        "ContractId" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=5958, version=0)
class Microsoft_Windows_Immersive_Shell_5958_0(Etw):
    pattern = Struct(
        "AppId" / WString,
        "ContractId" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=5959, version=0)
class Microsoft_Windows_Immersive_Shell_5959_0(Etw):
    pattern = Struct(
        "AppId" / WString,
        "ContractId" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=5960, version=0)
class Microsoft_Windows_Immersive_Shell_5960_0(Etw):
    pattern = Struct(
        "AppId" / WString,
        "ContractId" / WString,
        "ErrorCode" / Int32ul,
        "PackageState" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=5961, version=0)
class Microsoft_Windows_Immersive_Shell_5961_0(Etw):
    pattern = Struct(
        "AppId" / WString,
        "ErrorCode" / Int32sl,
        "PhaseFlags" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=5962, version=0)
class Microsoft_Windows_Immersive_Shell_5962_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=5963, version=0)
class Microsoft_Windows_Immersive_Shell_5963_0(Etw):
    pattern = Struct(
        "AppId" / WString,
        "ContractId" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=5964, version=0)
class Microsoft_Windows_Immersive_Shell_5964_0(Etw):
    pattern = Struct(
        "AppId" / WString,
        "ContractId" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=5965, version=0)
class Microsoft_Windows_Immersive_Shell_5965_0(Etw):
    pattern = Struct(
        "AppId" / WString,
        "ContractId" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=5966, version=0)
class Microsoft_Windows_Immersive_Shell_5966_0(Etw):
    pattern = Struct(
        "AppId" / WString,
        "ContractId" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=5967, version=0)
class Microsoft_Windows_Immersive_Shell_5967_0(Etw):
    pattern = Struct(
        "AppId" / WString,
        "ContractId" / WString,
        "ProcessId" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=5970, version=0)
class Microsoft_Windows_Immersive_Shell_5970_0(Etw):
    pattern = Struct(
        "AppId" / WString,
        "ContractId" / WString,
        "ErrorCode" / Int32ul,
        "FailedBinary" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=5971, version=0)
class Microsoft_Windows_Immersive_Shell_5971_0(Etw):
    pattern = Struct(
        "AppId" / WString,
        "ContractId" / WString,
        "ErrorCode" / Int32ul,
        "FailedBinary" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=5972, version=0)
class Microsoft_Windows_Immersive_Shell_5972_0(Etw):
    pattern = Struct(
        "AppId" / WString,
        "ContractId" / WString,
        "ErrorCode" / Int32ul,
        "FailedBinary" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=5973, version=0)
class Microsoft_Windows_Immersive_Shell_5973_0(Etw):
    pattern = Struct(
        "AppId" / WString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=5974, version=0)
class Microsoft_Windows_Immersive_Shell_5974_0(Etw):
    pattern = Struct(
        "AppId" / WString,
        "ContractId" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=5975, version=0)
class Microsoft_Windows_Immersive_Shell_5975_0(Etw):
    pattern = Struct(
        "AppId" / WString,
        "ContractId" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=5976, version=0)
class Microsoft_Windows_Immersive_Shell_5976_0(Etw):
    pattern = Struct(
        "AppId" / WString,
        "ContractId" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=5977, version=0)
class Microsoft_Windows_Immersive_Shell_5977_0(Etw):
    pattern = Struct(
        "Reserved" / Int32ul,
        "MatchKey" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=5978, version=0)
class Microsoft_Windows_Immersive_Shell_5978_0(Etw):
    pattern = Struct(
        "aamActivationId" / Int64ul,
        "AppId" / WString,
        "MatchKey" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=5979, version=0)
class Microsoft_Windows_Immersive_Shell_5979_0(Etw):
    pattern = Struct(
        "Reserved" / Int32ul,
        "MatchKey" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=5980, version=0)
class Microsoft_Windows_Immersive_Shell_5980_0(Etw):
    pattern = Struct(
        "Reserved" / Int32ul,
        "MatchKey" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=5981, version=0)
class Microsoft_Windows_Immersive_Shell_5981_0(Etw):
    pattern = Struct(
        "Reserved" / Int32ul,
        "ViewId" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=5982, version=0)
class Microsoft_Windows_Immersive_Shell_5982_0(Etw):
    pattern = Struct(
        "Reserved" / Int32ul,
        "ViewId" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=5983, version=0)
class Microsoft_Windows_Immersive_Shell_5983_0(Etw):
    pattern = Struct(
        "AppId" / WString,
        "ContractId" / WString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=5984, version=0)
class Microsoft_Windows_Immersive_Shell_5984_0(Etw):
    pattern = Struct(
        "AppId" / WString,
        "ContractId" / WString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=5985, version=0)
class Microsoft_Windows_Immersive_Shell_5985_0(Etw):
    pattern = Struct(
        "AppId" / WString,
        "ContractId" / WString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=5986, version=0)
class Microsoft_Windows_Immersive_Shell_5986_0(Etw):
    pattern = Struct(
        "AppId" / WString,
        "ContractId" / WString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=5987, version=0)
class Microsoft_Windows_Immersive_Shell_5987_0(Etw):
    pattern = Struct(
        "AppId" / WString,
        "ContractId" / WString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=5988, version=0)
class Microsoft_Windows_Immersive_Shell_5988_0(Etw):
    pattern = Struct(
        "AppId" / WString,
        "ContractId" / WString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=5989, version=0)
class Microsoft_Windows_Immersive_Shell_5989_0(Etw):
    pattern = Struct(
        "AppId" / WString,
        "ContractId" / WString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=5990, version=0)
class Microsoft_Windows_Immersive_Shell_5990_0(Etw):
    pattern = Struct(
        "AppId" / WString,
        "ContractId" / WString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=6252, version=0)
class Microsoft_Windows_Immersive_Shell_6252_0(Etw):
    pattern = Struct(
        "FilePath" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=6501, version=0)
class Microsoft_Windows_Immersive_Shell_6501_0(Etw):
    pattern = Struct(
        "AppUserModelID" / WString,
        "SettingValue" / Int8ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=6502, version=0)
class Microsoft_Windows_Immersive_Shell_6502_0(Etw):
    pattern = Struct(
        "AppUserModelID" / WString,
        "SettingValue" / Int8ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=6503, version=0)
class Microsoft_Windows_Immersive_Shell_6503_0(Etw):
    pattern = Struct(
        "AppUserModelID" / WString,
        "SettingValue" / Int8ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=6506, version=0)
class Microsoft_Windows_Immersive_Shell_6506_0(Etw):
    pattern = Struct(
        "AppUserModelID" / WString,
        "PackageFamilyName" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=6601, version=0)
class Microsoft_Windows_Immersive_Shell_6601_0(Etw):
    pattern = Struct(
        "SessionID" / Int32ul,
        "DeviceInstanceID" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=6606, version=0)
class Microsoft_Windows_Immersive_Shell_6606_0(Etw):
    pattern = Struct(
        "DeviceCount" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=6607, version=0)
class Microsoft_Windows_Immersive_Shell_6607_0(Etw):
    pattern = Struct(
        "DeviceCount" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=6611, version=0)
class Microsoft_Windows_Immersive_Shell_6611_0(Etw):
    pattern = Struct(
        "DeviceInstanceID" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=6612, version=0)
class Microsoft_Windows_Immersive_Shell_6612_0(Etw):
    pattern = Struct(
        "DeviceInstanceID" / WString,
        "Connected" / Int8ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=6616, version=0)
class Microsoft_Windows_Immersive_Shell_6616_0(Etw):
    pattern = Struct(
        "DeviceCount" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=6617, version=0)
class Microsoft_Windows_Immersive_Shell_6617_0(Etw):
    pattern = Struct(
        "DeviceCount" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=6632, version=0)
class Microsoft_Windows_Immersive_Shell_6632_0(Etw):
    pattern = Struct(
        "ContentType" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=6641, version=0)
class Microsoft_Windows_Immersive_Shell_6641_0(Etw):
    pattern = Struct(
        "Count" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=6642, version=0)
class Microsoft_Windows_Immersive_Shell_6642_0(Etw):
    pattern = Struct(
        "Count" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=6645, version=0)
class Microsoft_Windows_Immersive_Shell_6645_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=6648, version=0)
class Microsoft_Windows_Immersive_Shell_6648_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=6651, version=0)
class Microsoft_Windows_Immersive_Shell_6651_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=6690, version=0)
class Microsoft_Windows_Immersive_Shell_6690_0(Etw):
    pattern = Struct(
        "AppId" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=6691, version=0)
class Microsoft_Windows_Immersive_Shell_6691_0(Etw):
    pattern = Struct(
        "AppId" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=6714, version=0)
class Microsoft_Windows_Immersive_Shell_6714_0(Etw):
    pattern = Struct(
        "ApiType" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=6715, version=0)
class Microsoft_Windows_Immersive_Shell_6715_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=6716, version=0)
class Microsoft_Windows_Immersive_Shell_6716_0(Etw):
    pattern = Struct(
        "ApiType" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=6718, version=0)
class Microsoft_Windows_Immersive_Shell_6718_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=6722, version=0)
class Microsoft_Windows_Immersive_Shell_6722_0(Etw):
    pattern = Struct(
        "NumApp" / Int32ul,
        "SetDefault" / Int8ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=6821, version=0)
class Microsoft_Windows_Immersive_Shell_6821_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=6823, version=0)
class Microsoft_Windows_Immersive_Shell_6823_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=6827, version=0)
class Microsoft_Windows_Immersive_Shell_6827_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=6841, version=0)
class Microsoft_Windows_Immersive_Shell_6841_0(Etw):
    pattern = Struct(
        "ApiType" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=6851, version=0)
class Microsoft_Windows_Immersive_Shell_6851_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul,
        "Quota" / Int32ul,
        "CurrentUsage" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=6852, version=0)
class Microsoft_Windows_Immersive_Shell_6852_0(Etw):
    pattern = Struct(
        "BytesToReduce" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=6853, version=0)
class Microsoft_Windows_Immersive_Shell_6853_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul,
        "BytesReclaimed" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=6854, version=0)
class Microsoft_Windows_Immersive_Shell_6854_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul,
        "Path" / WString,
        "Size" / Int32ul,
        "Visible" / Int8ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=6855, version=0)
class Microsoft_Windows_Immersive_Shell_6855_0(Etw):
    pattern = Struct(
        "NumOrphanFiles" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=6856, version=0)
class Microsoft_Windows_Immersive_Shell_6856_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul,
        "BytesReclaimed" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=6857, version=0)
class Microsoft_Windows_Immersive_Shell_6857_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul,
        "Path" / WString,
        "Size" / Int32ul,
        "Visible" / Int8ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7040, version=0)
class Microsoft_Windows_Immersive_Shell_7040_0(Etw):
    pattern = Struct(
        "RenderedTileCount" / Int32ul,
        "RealizedTileCount" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7155, version=0)
class Microsoft_Windows_Immersive_Shell_7155_0(Etw):
    pattern = Struct(
        "ErrorResult" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7156, version=0)
class Microsoft_Windows_Immersive_Shell_7156_0(Etw):
    pattern = Struct(
        "ErrorResult" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7157, version=0)
class Microsoft_Windows_Immersive_Shell_7157_0(Etw):
    pattern = Struct(
        "ChangeTo" / Int32ul,
        "ErrorResult" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7158, version=0)
class Microsoft_Windows_Immersive_Shell_7158_0(Etw):
    pattern = Struct(
        "ChangeTo" / Int32ul,
        "ErrorResult" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7159, version=0)
class Microsoft_Windows_Immersive_Shell_7159_0(Etw):
    pattern = Struct(
        "ChangeTo" / Int32ul,
        "ErrorResult" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7161, version=0)
class Microsoft_Windows_Immersive_Shell_7161_0(Etw):
    pattern = Struct(
        "ErrorResult" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7165, version=0)
class Microsoft_Windows_Immersive_Shell_7165_0(Etw):
    pattern = Struct(
        "ErrorResult" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7168, version=0)
class Microsoft_Windows_Immersive_Shell_7168_0(Etw):
    pattern = Struct(
        "JSON" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7169, version=0)
class Microsoft_Windows_Immersive_Shell_7169_0(Etw):
    pattern = Struct(
        "JSON" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7170, version=0)
class Microsoft_Windows_Immersive_Shell_7170_0(Etw):
    pattern = Struct(
        "JSON" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7171, version=0)
class Microsoft_Windows_Immersive_Shell_7171_0(Etw):
    pattern = Struct(
        "JSON" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7172, version=0)
class Microsoft_Windows_Immersive_Shell_7172_0(Etw):
    pattern = Struct(
        "JSON" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7173, version=0)
class Microsoft_Windows_Immersive_Shell_7173_0(Etw):
    pattern = Struct(
        "Result" / Int32ul,
        "ImpressionGUID" / WString,
        "TargetId" / WString,
        "ArrowDirection" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7174, version=0)
class Microsoft_Windows_Immersive_Shell_7174_0(Etw):
    pattern = Struct(
        "Result" / Int32ul,
        "ImpressionGUID" / WString,
        "IsVisible" / Int8ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7175, version=0)
class Microsoft_Windows_Immersive_Shell_7175_0(Etw):
    pattern = Struct(
        "Result" / Int32ul,
        "ImpressionGUID" / WString,
        "TargetId" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7176, version=0)
class Microsoft_Windows_Immersive_Shell_7176_0(Etw):
    pattern = Struct(
        "Result" / Int32ul,
        "ImpressionGUID" / WString,
        "IsVisible" / Int8ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7177, version=0)
class Microsoft_Windows_Immersive_Shell_7177_0(Etw):
    pattern = Struct(
        "Result" / Int32ul,
        "ImpressionGUID" / WString,
        "TargetId" / WString,
        "CommandId" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7179, version=0)
class Microsoft_Windows_Immersive_Shell_7179_0(Etw):
    pattern = Struct(
        "ErrorResult" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7183, version=0)
class Microsoft_Windows_Immersive_Shell_7183_0(Etw):
    pattern = Struct(
        "ErrorResult" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7187, version=0)
class Microsoft_Windows_Immersive_Shell_7187_0(Etw):
    pattern = Struct(
        "ErrorResult" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7190, version=0)
class Microsoft_Windows_Immersive_Shell_7190_0(Etw):
    pattern = Struct(
        "JSON" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7191, version=0)
class Microsoft_Windows_Immersive_Shell_7191_0(Etw):
    pattern = Struct(
        "JSON" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7193, version=0)
class Microsoft_Windows_Immersive_Shell_7193_0(Etw):
    pattern = Struct(
        "ErrorResult" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7194, version=0)
class Microsoft_Windows_Immersive_Shell_7194_0(Etw):
    pattern = Struct(
        "Result" / Int32ul,
        "PartialQuery" / WString,
        "SelectedPosition" / Int32ul,
        "MaxQueryLengthWithSuggestion" / Int32ul,
        "Payload" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7196, version=0)
class Microsoft_Windows_Immersive_Shell_7196_0(Etw):
    pattern = Struct(
        "ErrorResult" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7199, version=0)
class Microsoft_Windows_Immersive_Shell_7199_0(Etw):
    pattern = Struct(
        "Result" / Int32ul,
        "ImpressionGUID" / WString,
        "ErrorCode" / Int32ul,
        "Url" / WString,
        "HBT" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7200, version=0)
class Microsoft_Windows_Immersive_Shell_7200_0(Etw):
    pattern = Struct(
        "Result" / Int32ul,
        "ImpressionGUID" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7204, version=0)
class Microsoft_Windows_Immersive_Shell_7204_0(Etw):
    pattern = Struct(
        "DroppedAPIcall" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7206, version=0)
class Microsoft_Windows_Immersive_Shell_7206_0(Etw):
    pattern = Struct(
        "ErrorResult" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7209, version=0)
class Microsoft_Windows_Immersive_Shell_7209_0(Etw):
    pattern = Struct(
        "Result" / Int32ul,
        "ImpressionGUID" / WString,
        "TargetId" / WString,
        "InputMethod" / Int32ul,
        "FirstItemId" / WString,
        "LastItemId" / WString,
        "ViewportFlags" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7210, version=0)
class Microsoft_Windows_Immersive_Shell_7210_0(Etw):
    pattern = Struct(
        "InputMethod" / Int32ul,
        "ViewMode" / Int32ul,
        "Timestamp" / Int64ul,
        "JSON" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7211, version=0)
class Microsoft_Windows_Immersive_Shell_7211_0(Etw):
    pattern = Struct(
        "ImpressionGUID" / WString,
        "Timestamp" / Int64ul,
        "ErrorCode" / Int32ul,
        "Url" / WString,
        "HBT" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7212, version=0)
class Microsoft_Windows_Immersive_Shell_7212_0(Etw):
    pattern = Struct(
        "ImpressionGUID" / WString,
        "Timestamp" / WString,
        "JSON" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7213, version=0)
class Microsoft_Windows_Immersive_Shell_7213_0(Etw):
    pattern = Struct(
        "Body" / WString,
        "QueryString" / WString,
        "Result" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7214, version=0)
class Microsoft_Windows_Immersive_Shell_7214_0(Etw):
    pattern = Struct(
        "EndpointCode" / Int32ul,
        "Hostname" / WString,
        "ObjectName" / WString,
        "UserAgent" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7215, version=0)
class Microsoft_Windows_Immersive_Shell_7215_0(Etw):
    pattern = Struct(
        "HTTPResponseCode" / Int32ul,
        "HTTPHeaders" / WString,
        "HTTPPostPayload" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7219, version=0)
class Microsoft_Windows_Immersive_Shell_7219_0(Etw):
    pattern = Struct(
        "ErrorResult" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7221, version=0)
class Microsoft_Windows_Immersive_Shell_7221_0(Etw):
    pattern = Struct(
        "ErrorResult" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7223, version=0)
class Microsoft_Windows_Immersive_Shell_7223_0(Etw):
    pattern = Struct(
        "ErrorResult" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7227, version=0)
class Microsoft_Windows_Immersive_Shell_7227_0(Etw):
    pattern = Struct(
        "ErrorResult" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7233, version=0)
class Microsoft_Windows_Immersive_Shell_7233_0(Etw):
    pattern = Struct(
        "ErrorResult" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7237, version=0)
class Microsoft_Windows_Immersive_Shell_7237_0(Etw):
    pattern = Struct(
        "ErrorResult" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7242, version=0)
class Microsoft_Windows_Immersive_Shell_7242_0(Etw):
    pattern = Struct(
        "ErrorResult" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7246, version=0)
class Microsoft_Windows_Immersive_Shell_7246_0(Etw):
    pattern = Struct(
        "ErrorResult" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7249, version=0)
class Microsoft_Windows_Immersive_Shell_7249_0(Etw):
    pattern = Struct(
        "Result" / Int32ul,
        "ImpressionGUID" / WString,
        "ScrollDirection" / Int32ul,
        "InputMethod" / Int32ul,
        "FirstItemId" / WString,
        "LastItemId" / WString,
        "ViewportFlags" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7250, version=0)
class Microsoft_Windows_Immersive_Shell_7250_0(Etw):
    pattern = Struct(
        "Result" / Int32ul,
        "ImpressionGUID" / WString,
        "NewVisibilityState" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7251, version=0)
class Microsoft_Windows_Immersive_Shell_7251_0(Etw):
    pattern = Struct(
        "Result" / Int32ul,
        "ImpressionGUID" / WString,
        "Orientation" / Int32ul,
        "FirstItemId" / WString,
        "LastItemId" / WString,
        "ViewportFlags" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7252, version=0)
class Microsoft_Windows_Immersive_Shell_7252_0(Etw):
    pattern = Struct(
        "Result" / Int32ul,
        "ImpressionGUID" / WString,
        "LayoutAction" / Int32ul,
        "TelemetryId" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7253, version=0)
class Microsoft_Windows_Immersive_Shell_7253_0(Etw):
    pattern = Struct(
        "Result" / Int32ul,
        "ImpressionGUID" / WString,
        "LayoutAction" / Int32ul,
        "ResultType" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7254, version=0)
class Microsoft_Windows_Immersive_Shell_7254_0(Etw):
    pattern = Struct(
        "JSON" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7255, version=0)
class Microsoft_Windows_Immersive_Shell_7255_0(Etw):
    pattern = Struct(
        "JSON" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7256, version=0)
class Microsoft_Windows_Immersive_Shell_7256_0(Etw):
    pattern = Struct(
        "JSON" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7257, version=0)
class Microsoft_Windows_Immersive_Shell_7257_0(Etw):
    pattern = Struct(
        "JSON" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7261, version=0)
class Microsoft_Windows_Immersive_Shell_7261_0(Etw):
    pattern = Struct(
        "ErrorResult" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7263, version=0)
class Microsoft_Windows_Immersive_Shell_7263_0(Etw):
    pattern = Struct(
        "ErrorResult" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7265, version=0)
class Microsoft_Windows_Immersive_Shell_7265_0(Etw):
    pattern = Struct(
        "ErrorResult" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7268, version=0)
class Microsoft_Windows_Immersive_Shell_7268_0(Etw):
    pattern = Struct(
        "Result" / Int32ul,
        "ImpressionGUID" / WString,
        "ErrorCode" / Int32ul,
        "Url" / WString,
        "HBT" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7271, version=0)
class Microsoft_Windows_Immersive_Shell_7271_0(Etw):
    pattern = Struct(
        "ErrorResult" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7274, version=0)
class Microsoft_Windows_Immersive_Shell_7274_0(Etw):
    pattern = Struct(
        "Result" / Int32ul,
        "PartialQuery" / WString,
        "SelectedPosition" / Int32ul,
        "MaxQueryLengthWithSuggestion" / Int32ul,
        "Payload" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7276, version=0)
class Microsoft_Windows_Immersive_Shell_7276_0(Etw):
    pattern = Struct(
        "JSON" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7278, version=0)
class Microsoft_Windows_Immersive_Shell_7278_0(Etw):
    pattern = Struct(
        "ErrorResult" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7282, version=0)
class Microsoft_Windows_Immersive_Shell_7282_0(Etw):
    pattern = Struct(
        "Result" / Int32ul,
        "ImpressionGUID" / WString,
        "DataCenter" / WString,
        "IsAbandoned" / Int8ul,
        "JSONPayload" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7284, version=0)
class Microsoft_Windows_Immersive_Shell_7284_0(Etw):
    pattern = Struct(
        "ErrorResult" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7286, version=0)
class Microsoft_Windows_Immersive_Shell_7286_0(Etw):
    pattern = Struct(
        "ErrorResult" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7287, version=0)
class Microsoft_Windows_Immersive_Shell_7287_0(Etw):
    pattern = Struct(
        "QueryString" / WString,
        "ImpressionGUID" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7288, version=0)
class Microsoft_Windows_Immersive_Shell_7288_0(Etw):
    pattern = Struct(
        "QueryString" / WString,
        "ImpressionGUID" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7289, version=0)
class Microsoft_Windows_Immersive_Shell_7289_0(Etw):
    pattern = Struct(
        "TemplateId" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7293, version=0)
class Microsoft_Windows_Immersive_Shell_7293_0(Etw):
    pattern = Struct(
        "ImpressionGUID" / WString,
        "Timestamp" / Int64ul,
        "ErrorCode" / Int32ul,
        "Url" / WString,
        "HBT" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7380, version=0)
class Microsoft_Windows_Immersive_Shell_7380_0(Etw):
    pattern = Struct(
        "Left" / Int32sl,
        "Top" / Int32sl,
        "Right" / Int32sl,
        "Bottom" / Int32sl
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7381, version=0)
class Microsoft_Windows_Immersive_Shell_7381_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7400, version=0)
class Microsoft_Windows_Immersive_Shell_7400_0(Etw):
    pattern = Struct(
        "JSON" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7402, version=0)
class Microsoft_Windows_Immersive_Shell_7402_0(Etw):
    pattern = Struct(
        "ErrorResult" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7405, version=0)
class Microsoft_Windows_Immersive_Shell_7405_0(Etw):
    pattern = Struct(
        "Result" / Int32ul,
        "ImpressionGUID" / WString,
        "TelemetryID" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7407, version=0)
class Microsoft_Windows_Immersive_Shell_7407_0(Etw):
    pattern = Struct(
        "ErrorResult" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7410, version=0)
class Microsoft_Windows_Immersive_Shell_7410_0(Etw):
    pattern = Struct(
        "Result" / Int32ul,
        "ImpressionGUID" / WString,
        "ErrorCode" / Int32ul,
        "Url" / WString,
        "HBT" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7413, version=0)
class Microsoft_Windows_Immersive_Shell_7413_0(Etw):
    pattern = Struct(
        "ChangeTo" / Int32ul,
        "ErrorResult" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7414, version=0)
class Microsoft_Windows_Immersive_Shell_7414_0(Etw):
    pattern = Struct(
        "ChangeTo" / Int32ul,
        "ErrorResult" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7415, version=0)
class Microsoft_Windows_Immersive_Shell_7415_0(Etw):
    pattern = Struct(
        "Result" / Int32ul,
        "ImpressionGUID" / WString,
        "LayoutAction" / Int32ul,
        "TelemetryId" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7416, version=0)
class Microsoft_Windows_Immersive_Shell_7416_0(Etw):
    pattern = Struct(
        "ImpressionGUID" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7417, version=0)
class Microsoft_Windows_Immersive_Shell_7417_0(Etw):
    pattern = Struct(
        "ImpressionGUID" / WString,
        "Result" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7419, version=0)
class Microsoft_Windows_Immersive_Shell_7419_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7420, version=0)
class Microsoft_Windows_Immersive_Shell_7420_0(Etw):
    pattern = Struct(
        "URL" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7421, version=0)
class Microsoft_Windows_Immersive_Shell_7421_0(Etw):
    pattern = Struct(
        "URL" / WString,
        "Result" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7423, version=0)
class Microsoft_Windows_Immersive_Shell_7423_0(Etw):
    pattern = Struct(
        "ErrorResult" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7425, version=0)
class Microsoft_Windows_Immersive_Shell_7425_0(Etw):
    pattern = Struct(
        "ErrorResult" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7427, version=0)
class Microsoft_Windows_Immersive_Shell_7427_0(Etw):
    pattern = Struct(
        "ErrorResult" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7429, version=0)
class Microsoft_Windows_Immersive_Shell_7429_0(Etw):
    pattern = Struct(
        "ErrorResult" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7432, version=0)
class Microsoft_Windows_Immersive_Shell_7432_0(Etw):
    pattern = Struct(
        "ChangeTo" / WString,
        "ErrorResult" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7434, version=0)
class Microsoft_Windows_Immersive_Shell_7434_0(Etw):
    pattern = Struct(
        "JSON" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7436, version=0)
class Microsoft_Windows_Immersive_Shell_7436_0(Etw):
    pattern = Struct(
        "ErrorResult" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7439, version=0)
class Microsoft_Windows_Immersive_Shell_7439_0(Etw):
    pattern = Struct(
        "Result" / Int32ul,
        "ImpressionGUID" / WString,
        "TelemetryID" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7440, version=0)
class Microsoft_Windows_Immersive_Shell_7440_0(Etw):
    pattern = Struct(
        "Path" / WString,
        "Validation" / Int8ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7441, version=0)
class Microsoft_Windows_Immersive_Shell_7441_0(Etw):
    pattern = Struct(
        "Path" / WString,
        "Validation" / Int8ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7442, version=0)
class Microsoft_Windows_Immersive_Shell_7442_0(Etw):
    pattern = Struct(
        "Path" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7443, version=0)
class Microsoft_Windows_Immersive_Shell_7443_0(Etw):
    pattern = Struct(
        "Path" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7444, version=0)
class Microsoft_Windows_Immersive_Shell_7444_0(Etw):
    pattern = Struct(
        "Path" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7445, version=0)
class Microsoft_Windows_Immersive_Shell_7445_0(Etw):
    pattern = Struct(
        "Path" / WString,
        "Result" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7447, version=0)
class Microsoft_Windows_Immersive_Shell_7447_0(Etw):
    pattern = Struct(
        "ErrorResult" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7449, version=0)
class Microsoft_Windows_Immersive_Shell_7449_0(Etw):
    pattern = Struct(
        "ErrorResult" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7453, version=0)
class Microsoft_Windows_Immersive_Shell_7453_0(Etw):
    pattern = Struct(
        "ErrorResult" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7456, version=0)
class Microsoft_Windows_Immersive_Shell_7456_0(Etw):
    pattern = Struct(
        "ChangeTo" / Int32ul,
        "ErrorResult" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7457, version=0)
class Microsoft_Windows_Immersive_Shell_7457_0(Etw):
    pattern = Struct(
        "Result" / Int32ul,
        "ImpressionGUID" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7460, version=0)
class Microsoft_Windows_Immersive_Shell_7460_0(Etw):
    pattern = Struct(
        "Scope" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7461, version=0)
class Microsoft_Windows_Immersive_Shell_7461_0(Etw):
    pattern = Struct(
        "Scope" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7462, version=0)
class Microsoft_Windows_Immersive_Shell_7462_0(Etw):
    pattern = Struct(
        "Result" / Int32ul,
        "ImpressionGUID" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=7701, version=0)
class Microsoft_Windows_Immersive_Shell_7701_0(Etw):
    pattern = Struct(
        "ApplicationWindow" / Int64ul,
        "PID" / Int32ul,
        "AppID" / WString,
        "PriorityForeground" / Int8ul,
        "SystemWindow" / Int64ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=8009, version=0)
class Microsoft_Windows_Immersive_Shell_8009_0(Etw):
    pattern = Struct(
        "ReportedError" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=8010, version=0)
class Microsoft_Windows_Immersive_Shell_8010_0(Etw):
    pattern = Struct(
        "ReportedError" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=8025, version=0)
class Microsoft_Windows_Immersive_Shell_8025_0(Etw):
    pattern = Struct(
        "ActionType" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=8027, version=0)
class Microsoft_Windows_Immersive_Shell_8027_0(Etw):
    pattern = Struct(
        "ReportedError" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=8205, version=0)
class Microsoft_Windows_Immersive_Shell_8205_0(Etw):
    pattern = Struct(
        "PackageId" / WString,
        "ActivatableClassId" / WString,
        "Verb" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=8207, version=0)
class Microsoft_Windows_Immersive_Shell_8207_0(Etw):
    pattern = Struct(
        "AppId" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=8209, version=0)
class Microsoft_Windows_Immersive_Shell_8209_0(Etw):
    pattern = Struct(
        "AppId" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=8215, version=0)
class Microsoft_Windows_Immersive_Shell_8215_0(Etw):
    pattern = Struct(
        "AppId" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=8216, version=0)
class Microsoft_Windows_Immersive_Shell_8216_0(Etw):
    pattern = Struct(
        "AppId" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=8222, version=0)
class Microsoft_Windows_Immersive_Shell_8222_0(Etw):
    pattern = Struct(
        "AppId" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=9950, version=0)
class Microsoft_Windows_Immersive_Shell_9950_0(Etw):
    pattern = Struct(
        "CallerModule" / WString,
        "ObjectModule" / WString,
        "CLSID" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=9951, version=0)
class Microsoft_Windows_Immersive_Shell_9951_0(Etw):
    pattern = Struct(
        "SxSModule" / WString,
        "CLSID" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=10000, version=0)
class Microsoft_Windows_Immersive_Shell_10000_0(Etw):
    pattern = Struct(
        "hWnd" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=11100, version=0)
class Microsoft_Windows_Immersive_Shell_11100_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "Priority" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=11110, version=0)
class Microsoft_Windows_Immersive_Shell_11110_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "PackageFullName" / WString,
        "AppUserModelId" / WString,
        "Flags" / Int32ul,
        "TerminateReason" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=11111, version=0)
class Microsoft_Windows_Immersive_Shell_11111_0(Etw):
    pattern = Struct(
        "NTSTATUS" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=11115, version=0)
class Microsoft_Windows_Immersive_Shell_11115_0(Etw):
    pattern = Struct(
        "PsmKey" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=11116, version=0)
class Microsoft_Windows_Immersive_Shell_11116_0(Etw):
    pattern = Struct(
        "PsmKey" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=11118, version=0)
class Microsoft_Windows_Immersive_Shell_11118_0(Etw):
    pattern = Struct(
        "PsmKey" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=11119, version=0)
class Microsoft_Windows_Immersive_Shell_11119_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "PackageFullName" / WString,
        "AppUserModelId" / WString,
        "PackedResumeDurationsMs_HiWordAppLoWordPackage" / Int32ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=11120, version=0)
class Microsoft_Windows_Immersive_Shell_11120_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "ExecutionReason" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=11121, version=0)
class Microsoft_Windows_Immersive_Shell_11121_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "ExecutionReason" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=11122, version=0)
class Microsoft_Windows_Immersive_Shell_11122_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "ExecutionReason" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=11123, version=0)
class Microsoft_Windows_Immersive_Shell_11123_0(Etw):
    pattern = Struct(
        "PsmKey" / WString,
        "HRESULT" / Int32ul,
        "Reason" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=11202, version=0)
class Microsoft_Windows_Immersive_Shell_11202_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=11204, version=0)
class Microsoft_Windows_Immersive_Shell_11204_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=11205, version=0)
class Microsoft_Windows_Immersive_Shell_11205_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=11206, version=0)
class Microsoft_Windows_Immersive_Shell_11206_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=11207, version=0)
class Microsoft_Windows_Immersive_Shell_11207_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=11208, version=0)
class Microsoft_Windows_Immersive_Shell_11208_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=11209, version=0)
class Microsoft_Windows_Immersive_Shell_11209_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=11210, version=0)
class Microsoft_Windows_Immersive_Shell_11210_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=11211, version=0)
class Microsoft_Windows_Immersive_Shell_11211_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=11212, version=0)
class Microsoft_Windows_Immersive_Shell_11212_0(Etw):
    pattern = Struct(
        "ProviderDisplayName" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=11213, version=0)
class Microsoft_Windows_Immersive_Shell_11213_0(Etw):
    pattern = Struct(
        "ProviderDisplayName" / WString,
        "AccountName" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=11214, version=0)
class Microsoft_Windows_Immersive_Shell_11214_0(Etw):
    pattern = Struct(
        "Resource" / WString,
        "Identity" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=11215, version=0)
class Microsoft_Windows_Immersive_Shell_11215_0(Etw):
    pattern = Struct(
        "CommandId" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=11301, version=0)
class Microsoft_Windows_Immersive_Shell_11301_0(Etw):
    pattern = Struct(
        "ConnectionGUID" / Guid,
        "AppID" / WString,
        "AppArguments" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=11302, version=0)
class Microsoft_Windows_Immersive_Shell_11302_0(Etw):
    pattern = Struct(
        "ConnectionGUID" / Guid,
        "AppID" / WString,
        "AppArguments" / WString
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=11303, version=0)
class Microsoft_Windows_Immersive_Shell_11303_0(Etw):
    pattern = Struct(
        "ConnectionGUID" / Guid,
        "DeadlineHigh" / Int32ul,
        "DeadlineLow" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=11304, version=0)
class Microsoft_Windows_Immersive_Shell_11304_0(Etw):
    pattern = Struct(
        "ConnectionGUID" / Guid,
        "DeadlineHigh" / Int32ul,
        "DeadlineLow" / Int32ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=11305, version=0)
class Microsoft_Windows_Immersive_Shell_11305_0(Etw):
    pattern = Struct(
        "ConnectionGUID" / Guid,
        "AppID" / WString,
        "AppArguments" / WString,
        "AppAlreadyRunning" / Int8ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=11306, version=0)
class Microsoft_Windows_Immersive_Shell_11306_0(Etw):
    pattern = Struct(
        "ConnectionGUID" / Guid,
        "NewHWND" / Int64ul,
        "NewHWNDIsSplashScreen" / Int8ul,
        "CrossFaded" / Int8ul
    )


@declare(guid=guid("315a8872-923e-4ea2-9889-33cd4754bf64"), event_id=11307, version=0)
class Microsoft_Windows_Immersive_Shell_11307_0(Etw):
    pattern = Struct(
        "ConnectionGUID" / Guid,
        "NewName" / WString
    )

