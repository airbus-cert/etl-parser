# -*- coding: utf-8 -*-
"""
Microsoft-Windows-DUSER
GUID : 8429e243-345b-47c1-8a91-2c94caf0daab
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("8429e243-345b-47c1-8a91-2c94caf0daab"), event_id=4, version=0)
class Microsoft_Windows_DUSER_4_0(Etw):
    pattern = Struct(
        "cAdaptors" / Int32sl
    )


@declare(guid=guid("8429e243-345b-47c1-8a91-2c94caf0daab"), event_id=12, version=0)
class Microsoft_Windows_DUSER_12_0(Etw):
    pattern = Struct(
        "hGadget" / Int32ul,
        "pVisual" / Int64ul,
        "fRoot" / Int8ul
    )


@declare(guid=guid("8429e243-345b-47c1-8a91-2c94caf0daab"), event_id=13, version=0)
class Microsoft_Windows_DUSER_13_0(Etw):
    pattern = Struct(
        "hGadget" / Int32ul,
        "pVisual" / Int64ul,
        "fRoot" / Int8ul,
        "nWidth" / Int32sl,
        "nHeight" / Int32sl,
        "fIsCopy" / Int8ul
    )


@declare(guid=guid("8429e243-345b-47c1-8a91-2c94caf0daab"), event_id=14, version=0)
class Microsoft_Windows_DUSER_14_0(Etw):
    pattern = Struct(
        "hGadget" / Int32ul,
        "pVisual" / Int64ul,
        "fRoot" / Int8ul
    )


@declare(guid=guid("8429e243-345b-47c1-8a91-2c94caf0daab"), event_id=15, version=0)
class Microsoft_Windows_DUSER_15_0(Etw):
    pattern = Struct(
        "nNumberOfPendingDeletions" / Int32sl
    )


@declare(guid=guid("8429e243-345b-47c1-8a91-2c94caf0daab"), event_id=16, version=0)
class Microsoft_Windows_DUSER_16_0(Etw):
    pattern = Struct(
        "nNumberOfPendingDeletions" / Int32sl
    )


@declare(guid=guid("8429e243-345b-47c1-8a91-2c94caf0daab"), event_id=17, version=0)
class Microsoft_Windows_DUSER_17_0(Etw):
    pattern = Struct(
        "hGadget" / Int32ul,
        "pVisual" / Int64ul,
        "fRoot" / Int8ul
    )


@declare(guid=guid("8429e243-345b-47c1-8a91-2c94caf0daab"), event_id=18, version=0)
class Microsoft_Windows_DUSER_18_0(Etw):
    pattern = Struct(
        "hGadget" / Int32ul,
        "pVisual" / Int64ul,
        "fRoot" / Int8ul
    )


@declare(guid=guid("8429e243-345b-47c1-8a91-2c94caf0daab"), event_id=19, version=0)
class Microsoft_Windows_DUSER_19_0(Etw):
    pattern = Struct(
        "hGadget" / Int32ul,
        "pVisual" / Int64ul,
        "fRoot" / Int8ul,
        "nWidth" / Int32sl,
        "nHeight" / Int32sl,
        "fIsCopy" / Int8ul
    )


@declare(guid=guid("8429e243-345b-47c1-8a91-2c94caf0daab"), event_id=20, version=0)
class Microsoft_Windows_DUSER_20_0(Etw):
    pattern = Struct(
        "hGadget" / Int32ul,
        "pVisual" / Int64ul,
        "fRoot" / Int8ul,
        "nWidth" / Int32sl,
        "nHeight" / Int32sl,
        "fIsCopy" / Int8ul
    )


@declare(guid=guid("8429e243-345b-47c1-8a91-2c94caf0daab"), event_id=21, version=0)
class Microsoft_Windows_DUSER_21_0(Etw):
    pattern = Struct(
        "hGadget" / Int32ul,
        "pVisual" / Int64ul,
        "fRoot" / Int8ul,
        "nWidth" / Int32sl,
        "nHeight" / Int32sl,
        "fIsCopy" / Int8ul
    )


@declare(guid=guid("8429e243-345b-47c1-8a91-2c94caf0daab"), event_id=22, version=0)
class Microsoft_Windows_DUSER_22_0(Etw):
    pattern = Struct(
        "hGadget" / Int32ul,
        "pVisual" / Int64ul,
        "fRoot" / Int8ul,
        "nWidth" / Int32sl,
        "nHeight" / Int32sl,
        "fIsCopy" / Int8ul
    )


@declare(guid=guid("8429e243-345b-47c1-8a91-2c94caf0daab"), event_id=24, version=0)
class Microsoft_Windows_DUSER_24_0(Etw):
    pattern = Struct(
        "hGadget" / Int32ul
    )


@declare(guid=guid("8429e243-345b-47c1-8a91-2c94caf0daab"), event_id=25, version=0)
class Microsoft_Windows_DUSER_25_0(Etw):
    pattern = Struct(
        "hGadget" / Int32ul,
        "fNewLayered" / Int8ul,
        "nVisualsCount" / Int32sl
    )


@declare(guid=guid("8429e243-345b-47c1-8a91-2c94caf0daab"), event_id=26, version=0)
class Microsoft_Windows_DUSER_26_0(Etw):
    pattern = Struct(
        "cTrans" / Int32ul,
        "dwTicket" / Int32ul
    )


@declare(guid=guid("8429e243-345b-47c1-8a91-2c94caf0daab"), event_id=27, version=0)
class Microsoft_Windows_DUSER_27_0(Etw):
    pattern = Struct(
        "cTrans" / Int32ul,
        "dwTicket" / Int32ul
    )


@declare(guid=guid("8429e243-345b-47c1-8a91-2c94caf0daab"), event_id=28, version=0)
class Microsoft_Windows_DUSER_28_0(Etw):
    pattern = Struct(
        "hGadget" / Int32ul,
        "pVisual" / Int64ul,
        "nWidth" / Int32sl,
        "nHeight" / Int32sl
    )


@declare(guid=guid("8429e243-345b-47c1-8a91-2c94caf0daab"), event_id=29, version=0)
class Microsoft_Windows_DUSER_29_0(Etw):
    pattern = Struct(
        "hGadget" / Int32ul,
        "pVisual" / Int64ul,
        "nWidth" / Int32sl,
        "nHeight" / Int32sl
    )


@declare(guid=guid("8429e243-345b-47c1-8a91-2c94caf0daab"), event_id=30, version=0)
class Microsoft_Windows_DUSER_30_0(Etw):
    pattern = Struct(
        "hGadget" / Int32ul,
        "pVisual" / Int64ul,
        "pDCompVisual" / Int64ul
    )


@declare(guid=guid("8429e243-345b-47c1-8a91-2c94caf0daab"), event_id=31, version=0)
class Microsoft_Windows_DUSER_31_0(Etw):
    pattern = Struct(
        "hGadget" / Int32ul,
        "pVisual" / Int64ul,
        "pDCompVisual" / Int64ul
    )


@declare(guid=guid("8429e243-345b-47c1-8a91-2c94caf0daab"), event_id=32, version=0)
class Microsoft_Windows_DUSER_32_0(Etw):
    pattern = Struct(
        "hGadget" / Int32ul,
        "pVisual" / Int64ul,
        "pDCompVisual" / Int64ul
    )


@declare(guid=guid("8429e243-345b-47c1-8a91-2c94caf0daab"), event_id=33, version=0)
class Microsoft_Windows_DUSER_33_0(Etw):
    pattern = Struct(
        "hGadget" / Int32ul,
        "pChildVisual" / Int64ul,
        "fDescendantVisualOfNewVisual" / Int8ul,
        "pDCompVisual" / Int64ul
    )


@declare(guid=guid("8429e243-345b-47c1-8a91-2c94caf0daab"), event_id=34, version=0)
class Microsoft_Windows_DUSER_34_0(Etw):
    pattern = Struct(
        "hGadget" / Int32ul,
        "pVisual" / Int64ul,
        "m_pParent" / Int64ul
    )


@declare(guid=guid("8429e243-345b-47c1-8a91-2c94caf0daab"), event_id=35, version=0)
class Microsoft_Windows_DUSER_35_0(Etw):
    pattern = Struct(
        "hGadget" / Int32ul,
        "pVisual" / Int64ul,
        "pDCompVisual" / Int64ul
    )


@declare(guid=guid("8429e243-345b-47c1-8a91-2c94caf0daab"), event_id=36, version=0)
class Microsoft_Windows_DUSER_36_0(Etw):
    pattern = Struct(
        "hGadget" / Int32ul,
        "pVisual" / Int64ul,
        "pDCompVisual" / Int64ul
    )


@declare(guid=guid("8429e243-345b-47c1-8a91-2c94caf0daab"), event_id=37, version=0)
class Microsoft_Windows_DUSER_37_0(Etw):
    pattern = Struct(
        "hGadget" / Int32ul,
        "pVisual" / Int64ul,
        "pDCompVisual" / Int64ul
    )


@declare(guid=guid("8429e243-345b-47c1-8a91-2c94caf0daab"), event_id=38, version=0)
class Microsoft_Windows_DUSER_38_0(Etw):
    pattern = Struct(
        "hGadget" / Int32ul,
        "pVisual" / Int64ul,
        "pNewChild" / Int64ul
    )


@declare(guid=guid("8429e243-345b-47c1-8a91-2c94caf0daab"), event_id=39, version=0)
class Microsoft_Windows_DUSER_39_0(Etw):
    pattern = Struct(
        "hGadget" / Int32ul,
        "pVisual" / Int64ul,
        "pNewChild" / Int64ul
    )


@declare(guid=guid("8429e243-345b-47c1-8a91-2c94caf0daab"), event_id=40, version=0)
class Microsoft_Windows_DUSER_40_0(Etw):
    pattern = Struct(
        "cTrans" / Int32ul,
        "dwTicket" / Int32ul
    )


@declare(guid=guid("8429e243-345b-47c1-8a91-2c94caf0daab"), event_id=41, version=0)
class Microsoft_Windows_DUSER_41_0(Etw):
    pattern = Struct(
        "cTrans" / Int32ul,
        "dwTicket" / Int32ul
    )


@declare(guid=guid("8429e243-345b-47c1-8a91-2c94caf0daab"), event_id=42, version=0)
class Microsoft_Windows_DUSER_42_0(Etw):
    pattern = Struct(
        "hGadget" / Int32ul,
        "pVisual" / Int64ul,
        "nAnimType" / Int32sl
    )


@declare(guid=guid("8429e243-345b-47c1-8a91-2c94caf0daab"), event_id=43, version=0)
class Microsoft_Windows_DUSER_43_0(Etw):
    pattern = Struct(
        "cTrans" / Int32ul,
        "psbUIA" / Int64ul,
        "dwTicket" / Int32ul
    )


@declare(guid=guid("8429e243-345b-47c1-8a91-2c94caf0daab"), event_id=44, version=0)
class Microsoft_Windows_DUSER_44_0(Etw):
    pattern = Struct(
        "cTrans" / Int32ul,
        "psbUIA" / Int64ul,
        "dwTicket" / Int32ul
    )


@declare(guid=guid("8429e243-345b-47c1-8a91-2c94caf0daab"), event_id=45, version=0)
class Microsoft_Windows_DUSER_45_0(Etw):
    pattern = Struct(
        "hGadget" / Int32ul,
        "pVisual" / Int64ul,
        "nVar" / Int32sl
    )


@declare(guid=guid("8429e243-345b-47c1-8a91-2c94caf0daab"), event_id=46, version=0)
class Microsoft_Windows_DUSER_46_0(Etw):
    pattern = Struct(
        "nSize" / Int32sl
    )


@declare(guid=guid("8429e243-345b-47c1-8a91-2c94caf0daab"), event_id=47, version=0)
class Microsoft_Windows_DUSER_47_0(Etw):
    pattern = Struct(
        "nSize" / Int32sl
    )


@declare(guid=guid("8429e243-345b-47c1-8a91-2c94caf0daab"), event_id=48, version=0)
class Microsoft_Windows_DUSER_48_0(Etw):
    pattern = Struct(
        "nSize" / Int32sl
    )


@declare(guid=guid("8429e243-345b-47c1-8a91-2c94caf0daab"), event_id=49, version=0)
class Microsoft_Windows_DUSER_49_0(Etw):
    pattern = Struct(
        "hGadget" / Int32ul,
        "m_pVisual" / Int64ul,
        "nVisuals" / Int32sl
    )


@declare(guid=guid("8429e243-345b-47c1-8a91-2c94caf0daab"), event_id=50, version=0)
class Microsoft_Windows_DUSER_50_0(Etw):
    pattern = Struct(
        "hGadget" / Int32ul,
        "m_pVisual" / Int64ul,
        "nVisuals" / Int32sl
    )


@declare(guid=guid("8429e243-345b-47c1-8a91-2c94caf0daab"), event_id=51, version=0)
class Microsoft_Windows_DUSER_51_0(Etw):
    pattern = Struct(
        "dwTicket" / Int32ul
    )


@declare(guid=guid("8429e243-345b-47c1-8a91-2c94caf0daab"), event_id=52, version=0)
class Microsoft_Windows_DUSER_52_0(Etw):
    pattern = Struct(
        "dwTicket" / Int32ul
    )


@declare(guid=guid("8429e243-345b-47c1-8a91-2c94caf0daab"), event_id=53, version=0)
class Microsoft_Windows_DUSER_53_0(Etw):
    pattern = Struct(
        "cTrans" / Int32ul,
        "psbUIA" / Int64ul,
        "dwTicket" / Int32ul
    )


@declare(guid=guid("8429e243-345b-47c1-8a91-2c94caf0daab"), event_id=54, version=0)
class Microsoft_Windows_DUSER_54_0(Etw):
    pattern = Struct(
        "nVisuals" / Int32sl
    )


@declare(guid=guid("8429e243-345b-47c1-8a91-2c94caf0daab"), event_id=55, version=0)
class Microsoft_Windows_DUSER_55_0(Etw):
    pattern = Struct(
        "PointerID" / Int32ul
    )


@declare(guid=guid("8429e243-345b-47c1-8a91-2c94caf0daab"), event_id=56, version=0)
class Microsoft_Windows_DUSER_56_0(Etw):
    pattern = Struct(
        "hGadget" / Int32ul,
        "nCode" / Int32ul,
        "fCopy" / Int8ul,
        "fRemainLayered" / Int8ul
    )


@declare(guid=guid("8429e243-345b-47c1-8a91-2c94caf0daab"), event_id=71, version=0)
class Microsoft_Windows_DUSER_71_0(Etw):
    pattern = Struct(
        "surfaceId" / Int64ul,
        "surfaceX" / Int32sl,
        "surfaceY" / Int32sl,
        "surfaceWidth" / Int32sl,
        "surfaceHeight" / Int32sl,
        "containerId" / Int64ul,
        "containerWidth" / Int32sl,
        "containerHeight" / Int32sl,
        "pRegionSurface" / Int64ul,
        "pSurface" / Int64ul
    )


@declare(guid=guid("8429e243-345b-47c1-8a91-2c94caf0daab"), event_id=72, version=0)
class Microsoft_Windows_DUSER_72_0(Etw):
    pattern = Struct(
        "pRegionSurface" / Int64ul,
        "pSurface" / Int64ul
    )


@declare(guid=guid("8429e243-345b-47c1-8a91-2c94caf0daab"), event_id=75, version=0)
class Microsoft_Windows_DUSER_75_0(Etw):
    pattern = Struct(
        "flProcessingDelay" / Float32l,
        "nNumberOfStoryboards" / Int32sl,
        "nNumberOfVisuals" / Int32sl
    )


@declare(guid=guid("8429e243-345b-47c1-8a91-2c94caf0daab"), event_id=76, version=0)
class Microsoft_Windows_DUSER_76_0(Etw):
    pattern = Struct(
        "cTrans" / Int32ul,
        "uTransIndex" / Int32ul,
        "dwTicket" / Int32ul,
        "hGadget" / Int32ul,
        "nProperty" / Int32ul,
        "pTransitionVisual" / Int64ul,
        "pDCompVisual" / Int64ul
    )


@declare(guid=guid("8429e243-345b-47c1-8a91-2c94caf0daab"), event_id=77, version=0)
class Microsoft_Windows_DUSER_77_0(Etw):
    pattern = Struct(
        "nHResult" / Int32sl,
        "hGadget" / Int32ul,
        "fIsCopy" / Int8ul,
        "pTransitionVisual" / Int64ul,
        "pDCompVisual" / Int64ul,
        "pEffectGroup" / Int64ul
    )


@declare(guid=guid("8429e243-345b-47c1-8a91-2c94caf0daab"), event_id=78, version=0)
class Microsoft_Windows_DUSER_78_0(Etw):
    pattern = Struct(
        "pTransitionVisual" / Int64ul,
        "pDCompVisual" / Int64ul,
        "nTransformType" / Int32sl,
        "pTransform" / Int64ul,
        "fAnimation" / Int8ul
    )


@declare(guid=guid("8429e243-345b-47c1-8a91-2c94caf0daab"), event_id=79, version=0)
class Microsoft_Windows_DUSER_79_0(Etw):
    pattern = Struct(
        "pStoryboard" / Int64ul,
        "nAnimationId" / Int32sl,
        "nStoryboardId" / Int32sl,
        "nCode" / Int32sl,
        "flProcessingDelay" / Float32l
    )


@declare(guid=guid("8429e243-345b-47c1-8a91-2c94caf0daab"), event_id=80, version=0)
class Microsoft_Windows_DUSER_80_0(Etw):
    pattern = Struct(
        "pStoryboard" / Int64ul,
        "nAnimationId" / Int32sl,
        "nStoryboardId" / Int32sl,
        "nCode" / Int32sl,
        "flProcessingDelay" / Float32l
    )


@declare(guid=guid("8429e243-345b-47c1-8a91-2c94caf0daab"), event_id=81, version=0)
class Microsoft_Windows_DUSER_81_0(Etw):
    pattern = Struct(
        "surfaceId" / Int64ul,
        "surfaceX" / Int32sl,
        "surfaceY" / Int32sl
    )


@declare(guid=guid("8429e243-345b-47c1-8a91-2c94caf0daab"), event_id=82, version=0)
class Microsoft_Windows_DUSER_82_0(Etw):
    pattern = Struct(
        "surfaceId" / Int64ul
    )


@declare(guid=guid("8429e243-345b-47c1-8a91-2c94caf0daab"), event_id=83, version=0)
class Microsoft_Windows_DUSER_83_0(Etw):
    pattern = Struct(
        "hGadget" / Int64ul,
        "nWidth" / Int32sl,
        "nHeight" / Int32sl,
        "hAncestorGadget" / Int64ul,
        "nAncestorWidth" / Int32sl,
        "nAncestorHeight" / Int32sl
    )


@declare(guid=guid("8429e243-345b-47c1-8a91-2c94caf0daab"), event_id=84, version=0)
class Microsoft_Windows_DUSER_84_0(Etw):
    pattern = Struct(
        "surfaceId" / Int64ul,
        "surfaceX" / Int32sl,
        "surfaceY" / Int32sl,
        "surfaceWidth" / Int32sl,
        "surfaceHeight" / Int32sl
    )


@declare(guid=guid("8429e243-345b-47c1-8a91-2c94caf0daab"), event_id=85, version=0)
class Microsoft_Windows_DUSER_85_0(Etw):
    pattern = Struct(
        "PointerHitTestID" / Int32ul
    )

