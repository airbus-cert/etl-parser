# -*- coding: utf-8 -*-
"""
Microsoft-Windows-TabletPC-InputPanel
GUID : e978f84e-582d-4167-977e-32af52706888
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=189, version=0)
class Microsoft_Windows_TabletPC_InputPanel_189_0(Etw):
    pattern = Struct(
        "Log" / WString
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=215, version=0)
class Microsoft_Windows_TabletPC_InputPanel_215_0(Etw):
    pattern = Struct(
        "OperationType" / Int32sl
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=300, version=0)
class Microsoft_Windows_TabletPC_InputPanel_300_0(Etw):
    pattern = Struct(
        "Mode" / WString,
        "Method" / WString
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=301, version=0)
class Microsoft_Windows_TabletPC_InputPanel_301_0(Etw):
    pattern = Struct(
        "Mode" / WString,
        "Method" / WString,
        "IP_Left" / Int32sl,
        "IP_Top" / Int32sl,
        "IP_Right" / Int32sl,
        "IP_Bottom" / Int32sl,
        "Monitor_Left" / Int32sl,
        "Monitor_Top" / Int32sl,
        "Monitor_Right" / Int32sl,
        "Monitor_Bottom" / Int32sl
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=302, version=0)
class Microsoft_Windows_TabletPC_InputPanel_302_0(Etw):
    pattern = Struct(
        "Method" / WString
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=304, version=0)
class Microsoft_Windows_TabletPC_InputPanel_304_0(Etw):
    pattern = Struct(
        "Mode" / WString
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=308, version=0)
class Microsoft_Windows_TabletPC_InputPanel_308_0(Etw):
    pattern = Struct(
        "HKL" / Int32sl
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=309, version=0)
class Microsoft_Windows_TabletPC_InputPanel_309_0(Etw):
    pattern = Struct(
        "Keyboard" / Int8ul
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=310, version=0)
class Microsoft_Windows_TabletPC_InputPanel_310_0(Etw):
    pattern = Struct(
        "Landscape" / Int8ul
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=410, version=0)
class Microsoft_Windows_TabletPC_InputPanel_410_0(Etw):
    pattern = Struct(
        "Left" / Int32sl,
        "Top" / Int32sl,
        "Right" / Int32sl,
        "Bottom" / Int32sl
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=421, version=0)
class Microsoft_Windows_TabletPC_InputPanel_421_0(Etw):
    pattern = Struct(
        "StoryBoardID" / Int32sl
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=422, version=0)
class Microsoft_Windows_TabletPC_InputPanel_422_0(Etw):
    pattern = Struct(
        "StoryBoardID" / Int32sl
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=423, version=0)
class Microsoft_Windows_TabletPC_InputPanel_423_0(Etw):
    pattern = Struct(
        "StoryBoardID" / Int32sl
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=424, version=0)
class Microsoft_Windows_TabletPC_InputPanel_424_0(Etw):
    pattern = Struct(
        "StoryBoardID" / Int32sl
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=431, version=0)
class Microsoft_Windows_TabletPC_InputPanel_431_0(Etw):
    pattern = Struct(
        "StoryBoardID" / Int32sl
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=451, version=0)
class Microsoft_Windows_TabletPC_InputPanel_451_0(Etw):
    pattern = Struct(
        "AppUserModelID" / WString,
        "PackageFullName" / WString
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=453, version=0)
class Microsoft_Windows_TabletPC_InputPanel_453_0(Etw):
    pattern = Struct(
        "AppUserModelID" / WString,
        "PackageFullName" / WString
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=500, version=0)
class Microsoft_Windows_TabletPC_InputPanel_500_0(Etw):
    pattern = Struct(
        "NumberOfKeys" / Int32ul
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=501, version=0)
class Microsoft_Windows_TabletPC_InputPanel_501_0(Etw):
    pattern = Struct(
        "HKL" / Int32ul,
        "gutter" / Int32ul,
        "IsSplitLayout" / Int8ul,
        "LeftBumpId" / Int32sl,
        "RightBumpId" / Int32sl,
        "left" / Int32sl,
        "top" / Int32sl,
        "right" / Int32sl,
        "bottom" / Int32sl
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=502, version=0)
class Microsoft_Windows_TabletPC_InputPanel_502_0(Etw):
    pattern = Struct(
        "Index" / Int32ul,
        "left" / Int32sl,
        "top" / Int32sl,
        "right" / Int32sl,
        "bottom" / Int32sl,
        "IsLKey" / Int8ul,
        "KeyLocation" / Int32ul,
        "x" / Int32sl,
        "y" / Int32sl
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=610, version=0)
class Microsoft_Windows_TabletPC_InputPanel_610_0(Etw):
    pattern = Struct(
        "Language" / WString,
        "Instance" / Int64sl
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=611, version=0)
class Microsoft_Windows_TabletPC_InputPanel_611_0(Etw):
    pattern = Struct(
        "ToScope" / Int32sl,
        "Instance" / Int64sl
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=612, version=0)
class Microsoft_Windows_TabletPC_InputPanel_612_0(Etw):
    pattern = Struct(
        "FromState" / WString,
        "ToState" / WString
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=613, version=0)
class Microsoft_Windows_TabletPC_InputPanel_613_0(Etw):
    pattern = Struct(
        "PasswordMode" / Int8ul,
        "Instance" / Int64sl
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=614, version=0)
class Microsoft_Windows_TabletPC_InputPanel_614_0(Etw):
    pattern = Struct(
        "LMCapabilites" / WString
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=620, version=0)
class Microsoft_Windows_TabletPC_InputPanel_620_0(Etw):
    pattern = Struct(
        "SequenceNumber" / Int64sl
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=621, version=0)
class Microsoft_Windows_TabletPC_InputPanel_621_0(Etw):
    pattern = Struct(
        "Instance" / Int64sl
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=624, version=0)
class Microsoft_Windows_TabletPC_InputPanel_624_0(Etw):
    pattern = Struct(
        "PreContext" / WString,
        "PostContext" / WString
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=628, version=0)
class Microsoft_Windows_TabletPC_InputPanel_628_0(Etw):
    pattern = Struct(
        "PreContext" / WString,
        "PostContext" / WString
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=632, version=0)
class Microsoft_Windows_TabletPC_InputPanel_632_0(Etw):
    pattern = Struct(
        "SequenceNumber" / Int64sl
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=633, version=0)
class Microsoft_Windows_TabletPC_InputPanel_633_0(Etw):
    pattern = Struct(
        "SequenceNumber" / Int64sl
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=634, version=0)
class Microsoft_Windows_TabletPC_InputPanel_634_0(Etw):
    pattern = Struct(
        "SequenceNumber" / Int64sl
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=635, version=0)
class Microsoft_Windows_TabletPC_InputPanel_635_0(Etw):
    pattern = Struct(
        "SequenceNumber" / Int64sl,
        "Character" / WString,
        "probability" / Float32l
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=636, version=0)
class Microsoft_Windows_TabletPC_InputPanel_636_0(Etw):
    pattern = Struct(
        "SequenceNumber" / Int64sl,
        "Character" / WString
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=656, version=0)
class Microsoft_Windows_TabletPC_InputPanel_656_0(Etw):
    pattern = Struct(
        "TopPrediction" / WString,
        "Alternate1" / WString,
        "Alternate2" / WString,
        "Alternate3" / WString
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=658, version=0)
class Microsoft_Windows_TabletPC_InputPanel_658_0(Etw):
    pattern = Struct(
        "KeyboardState" / Int32sl
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=659, version=0)
class Microsoft_Windows_TabletPC_InputPanel_659_0(Etw):
    pattern = Struct(
        "SequenceNumber" / Int64sl,
        "RawText" / WString,
        "TextBeingReplaced" / WString,
        "FixedText" / WString,
        "FixedTextSuffix" / WString,
        "FluidText" / WString,
        "FixedTextAlternates" / WString
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=664, version=0)
class Microsoft_Windows_TabletPC_InputPanel_664_0(Etw):
    pattern = Struct(
        "Duration" / Int32ul
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=682, version=0)
class Microsoft_Windows_TabletPC_InputPanel_682_0(Etw):
    pattern = Struct(
        "String" / WString
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=684, version=0)
class Microsoft_Windows_TabletPC_InputPanel_684_0(Etw):
    pattern = Struct(
        "String" / WString
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=685, version=0)
class Microsoft_Windows_TabletPC_InputPanel_685_0(Etw):
    pattern = Struct(
        "left" / Int32sl,
        "top" / Int32sl,
        "right" / Int32sl,
        "bottom" / Int32sl
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=686, version=0)
class Microsoft_Windows_TabletPC_InputPanel_686_0(Etw):
    pattern = Struct(
        "left" / Int32sl,
        "top" / Int32sl,
        "right" / Int32sl,
        "bottom" / Int32sl
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=687, version=0)
class Microsoft_Windows_TabletPC_InputPanel_687_0(Etw):
    pattern = Struct(
        "left" / Int32sl,
        "top" / Int32sl,
        "right" / Int32sl,
        "bottom" / Int32sl
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=726, version=0)
class Microsoft_Windows_TabletPC_InputPanel_726_0(Etw):
    pattern = Struct(
        "NewThumbSize" / Int32sl
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=925, version=0)
class Microsoft_Windows_TabletPC_InputPanel_925_0(Etw):
    pattern = Struct(
        "Duration" / Int32ul
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=926, version=0)
class Microsoft_Windows_TabletPC_InputPanel_926_0(Etw):
    pattern = Struct(
        "Duration" / Int32ul
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=927, version=0)
class Microsoft_Windows_TabletPC_InputPanel_927_0(Etw):
    pattern = Struct(
        "Duration" / Int32ul
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=928, version=0)
class Microsoft_Windows_TabletPC_InputPanel_928_0(Etw):
    pattern = Struct(
        "Duration" / Int32ul
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=929, version=0)
class Microsoft_Windows_TabletPC_InputPanel_929_0(Etw):
    pattern = Struct(
        "Duration" / Int32ul
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=930, version=0)
class Microsoft_Windows_TabletPC_InputPanel_930_0(Etw):
    pattern = Struct(
        "Duration" / Int32ul
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=931, version=0)
class Microsoft_Windows_TabletPC_InputPanel_931_0(Etw):
    pattern = Struct(
        "Duration" / Int32ul
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=932, version=0)
class Microsoft_Windows_TabletPC_InputPanel_932_0(Etw):
    pattern = Struct(
        "Duration" / Int32ul
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=933, version=0)
class Microsoft_Windows_TabletPC_InputPanel_933_0(Etw):
    pattern = Struct(
        "Duration" / Int32ul
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=1000, version=0)
class Microsoft_Windows_TabletPC_InputPanel_1000_0(Etw):
    pattern = Struct(
        "ResolutionWidth" / Int32sl,
        "ResolutionHeight" / Int32sl,
        "PhysicalWidthInHiMetric" / Int32sl,
        "PhysicalHeightInHiMetric" / Int32sl
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=1001, version=0)
class Microsoft_Windows_TabletPC_InputPanel_1001_0(Etw):
    pattern = Struct(
        "WaveFileResourceID" / Int32sl
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=1200, version=0)
class Microsoft_Windows_TabletPC_InputPanel_1200_0(Etw):
    pattern = Struct(
        "IMEMode" / Int8ul
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=1201, version=0)
class Microsoft_Windows_TabletPC_InputPanel_1201_0(Etw):
    pattern = Struct(
        "KeyFired" / Int32ul
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=2000, version=0)
class Microsoft_Windows_TabletPC_InputPanel_2000_0(Etw):
    pattern = Struct(
        "fShowIHM" / Int8ul,
        "fPenOrTouch" / Int8ul,
        "fLastTouchInThisControl" / Int8ul,
        "fInPasswordField" / Int8ul,
        "hwndElementFocusEvent" / Int64ul,
        "hwndRootFocusEvent" / Int64ul,
        "dwProcess" / Int32ul,
        "rcBoundLeft" / Int32sl,
        "rcBoundTop" / Int32sl,
        "rcBoundRight" / Int32sl,
        "rcBoundBottom" / Int32sl,
        "fRequireTouchInControl" / Int8ul,
        "fCanProcessEvent" / Int8ul,
        "fOnPersistenceList" / Int8ul
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=2001, version=0)
class Microsoft_Windows_TabletPC_InputPanel_2001_0(Etw):
    pattern = Struct(
        "msg" / Int32ul,
        "lParam" / Int64ul,
        "IsOnEditField" / Int8ul,
        "EventOriginProcess" / Int32ul,
        "OrginType" / Int32ul
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=2002, version=0)
class Microsoft_Windows_TabletPC_InputPanel_2002_0(Etw):
    pattern = Struct(
        "IsRegularKeyPress" / Int8ul
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=2004, version=0)
class Microsoft_Windows_TabletPC_InputPanel_2004_0(Etw):
    pattern = Struct(
        "InLaptopMode" / Int8ul
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=2005, version=0)
class Microsoft_Windows_TabletPC_InputPanel_2005_0(Etw):
    pattern = Struct(
        "eMethod" / Int32sl,
        "ForegroundHwnd" / Int64ul
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=2006, version=0)
class Microsoft_Windows_TabletPC_InputPanel_2006_0(Etw):
    pattern = Struct(
        "ForegroundHwnd" / Int64ul
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=2007, version=0)
class Microsoft_Windows_TabletPC_InputPanel_2007_0(Etw):
    pattern = Struct(
        "ForegroundHwnd" / Int64ul,
        "fOptedIntoFocusTracking" / Int8ul
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=2008, version=0)
class Microsoft_Windows_TabletPC_InputPanel_2008_0(Etw):
    pattern = Struct(
        "Caret_left" / Int32sl,
        "Caret_top" / Int32sl,
        "Caret_right" / Int32sl,
        "Caret_bottom" / Int32sl,
        "CaretWnd_left" / Int32sl,
        "CaretWnd_top" / Int32sl,
        "CaretWnd_right" / Int32sl,
        "CaretWnd_bottom" / Int32sl,
        "Caret_Flags" / Int32ul,
        "CaretHwnd" / Int64ul,
        "CaretVisible" / Int8ul
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=2010, version=0)
class Microsoft_Windows_TabletPC_InputPanel_2010_0(Etw):
    pattern = Struct(
        "hwnd" / Int64ul,
        "fVisible" / Int8ul
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=2011, version=0)
class Microsoft_Windows_TabletPC_InputPanel_2011_0(Etw):
    pattern = Struct(
        "KeyboardType" / Int32ul
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=2012, version=0)
class Microsoft_Windows_TabletPC_InputPanel_2012_0(Etw):
    pattern = Struct(
        "KeyboardType" / Int32ul
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=2020, version=0)
class Microsoft_Windows_TabletPC_InputPanel_2020_0(Etw):
    pattern = Struct(
        "KeyboardCalloutResult" / Int32ul
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=2021, version=0)
class Microsoft_Windows_TabletPC_InputPanel_2021_0(Etw):
    pattern = Struct(
        "UIActionType" / Int32ul
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=2022, version=0)
class Microsoft_Windows_TabletPC_InputPanel_2022_0(Etw):
    pattern = Struct(
        "UIActionType" / Int32ul
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=2023, version=0)
class Microsoft_Windows_TabletPC_InputPanel_2023_0(Etw):
    pattern = Struct(
        "IsSubscribed" / Int32ul
    )


@declare(guid=guid("e978f84e-582d-4167-977e-32af52706888"), event_id=2024, version=0)
class Microsoft_Windows_TabletPC_InputPanel_2024_0(Etw):
    pattern = Struct(
        "OperationType" / Int32ul
    )

