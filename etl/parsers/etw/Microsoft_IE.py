# -*- coding: utf-8 -*-
"""
Microsoft-IE
GUID : 9e3b3947-ca5d-4614-91a2-7b624e0e7244
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=1, version=0)
class Microsoft_IE_1_0(Etw):
    pattern = Struct(
        "DOC" / Int64ul,
        "Markup" / Int64ul,
        "left" / Int32sl,
        "top" / Int32sl,
        "right" / Int32sl,
        "bottom" / Int32sl
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=1, version=1)
class Microsoft_IE_1_1(Etw):
    pattern = Struct(
        "DOC" / Int64ul,
        "Markup" / Int64ul,
        "left" / Int32sl,
        "top" / Int32sl,
        "right" / Int32sl,
        "bottom" / Int32sl,
        "EventContextId" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=2, version=0)
class Microsoft_IE_2_0(Etw):
    pattern = Struct(
        "HWND" / Int64ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=2, version=1)
class Microsoft_IE_2_1(Etw):
    pattern = Struct(
        "HWND" / Int64ul,
        "Flags" / Int32ul,
        "EventContextId" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=3, version=0)
class Microsoft_IE_3_0(Etw):
    pattern = Struct(
        "View" / Int64ul,
        "grfLAYOUT" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=3, version=1)
class Microsoft_IE_3_1(Etw):
    pattern = Struct(
        "View" / Int64ul,
        "grfLAYOUT" / Int32ul,
        "EventContextId" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=4, version=0)
class Microsoft_IE_4_0(Etw):
    pattern = Struct(
        "DOC" / Int64ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=4, version=1)
class Microsoft_IE_4_1(Etw):
    pattern = Struct(
        "DOC" / Int64ul,
        "Flags" / Int32ul,
        "EventContextId" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=5, version=0)
class Microsoft_IE_5_0(Etw):
    pattern = Struct(
        "AddressName" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=6, version=0)
class Microsoft_IE_6_0(Etw):
    pattern = Struct(
        "AddressName" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=7, version=0)
class Microsoft_IE_7_0(Etw):
    pattern = Struct(
        "AddressName" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=7, version=1)
class Microsoft_IE_7_1(Etw):
    pattern = Struct(
        "AddressName" / WString,
        "EventContextId" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=8, version=0)
class Microsoft_IE_8_0(Etw):
    pattern = Struct(
        "AddressName" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=8, version=1)
class Microsoft_IE_8_1(Etw):
    pattern = Struct(
        "AddressName" / WString,
        "EventContextId" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=9, version=0)
class Microsoft_IE_9_0(Etw):
    pattern = Struct(
        "AddressName" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=9, version=1)
class Microsoft_IE_9_1(Etw):
    pattern = Struct(
        "AddressName" / WString,
        "EventContextId" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=10, version=0)
class Microsoft_IE_10_0(Etw):
    pattern = Struct(
        "AddressName" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=10, version=1)
class Microsoft_IE_10_1(Etw):
    pattern = Struct(
        "AddressName" / WString,
        "EventContextId" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=32, version=0)
class Microsoft_IE_32_0(Etw):
    pattern = Struct(
        "AddressName" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=33, version=0)
class Microsoft_IE_33_0(Etw):
    pattern = Struct(
        "AddressName" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=34, version=0)
class Microsoft_IE_34_0(Etw):
    pattern = Struct(
        "ThisPtr" / Int64ul,
        "URL" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=35, version=0)
class Microsoft_IE_35_0(Etw):
    pattern = Struct(
        "ThisPtr" / Int64ul,
        "URL" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=36, version=0)
class Microsoft_IE_36_0(Etw):
    pattern = Struct(
        "ThisPtr" / Int64ul,
        "PCL" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=37, version=0)
class Microsoft_IE_37_0(Etw):
    pattern = Struct(
        "dwCode" / Int32ul,
        "dwPos" / Int32ul,
        "dwMax" / Int32ul,
        "Text" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=38, version=0)
class Microsoft_IE_38_0(Etw):
    pattern = Struct(
        "DOC" / Int64ul,
        "dwCode" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=39, version=0)
class Microsoft_IE_39_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul,
        "Text" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=40, version=0)
class Microsoft_IE_40_0(Etw):
    pattern = Struct(
        "dwCode" / Int32ul,
        "dwPos" / Int32ul,
        "dwMax" / Int32ul,
        "Text" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=41, version=0)
class Microsoft_IE_41_0(Etw):
    pattern = Struct(
        "DOC" / Int64ul,
        "HtmlTag" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=42, version=0)
class Microsoft_IE_42_0(Etw):
    pattern = Struct(
        "DOC" / Int64ul,
        "HtmlTag" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=43, version=0)
class Microsoft_IE_43_0(Etw):
    pattern = Struct(
        "DOC" / Int64ul,
        "Length" / Int32ul,
        "SRC" / Bytes(lambda this: this.Length)
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=44, version=0)
class Microsoft_IE_44_0(Etw):
    pattern = Struct(
        "dw" / Int32ul,
        "HWND" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=45, version=0)
class Microsoft_IE_45_0(Etw):
    pattern = Struct(
        "dw" / Int32ul,
        "HWND" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=46, version=0)
class Microsoft_IE_46_0(Etw):
    pattern = Struct(
        "cPts" / Int32ul,
        "HWND" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=47, version=0)
class Microsoft_IE_47_0(Etw):
    pattern = Struct(
        "cPts" / Int32ul,
        "HWND" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=48, version=0)
class Microsoft_IE_48_0(Etw):
    pattern = Struct(
        "HTMPOST" / Int64ul,
        "Flags" / Int32ul,
        "Line" / Int32ul,
        "Offset" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=49, version=0)
class Microsoft_IE_49_0(Etw):
    pattern = Struct(
        "HTMPOST" / Int64ul,
        "Flags" / Int32ul,
        "Line" / Int32ul,
        "Offset" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=50, version=0)
class Microsoft_IE_50_0(Etw):
    pattern = Struct(
        "HTMPOST" / Int64ul,
        "OneExec2PT3ST4Run" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=51, version=0)
class Microsoft_IE_51_0(Etw):
    pattern = Struct(
        "HTMPOST" / Int64ul,
        "Zero" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=52, version=0)
class Microsoft_IE_52_0(Etw):
    pattern = Struct(
        "HTMPOST" / Int64ul,
        "Zero" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=53, version=0)
class Microsoft_IE_53_0(Etw):
    pattern = Struct(
        "HTMPOST" / Int64ul,
        "Error" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=54, version=0)
class Microsoft_IE_54_0(Etw):
    pattern = Struct(
        "Length" / Int32ul,
        "Script" / Bytes(lambda this: this.Length),
        "IsInline" / Int8ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=55, version=0)
class Microsoft_IE_55_0(Etw):
    pattern = Struct(
        "SourceIndex" / Int32ul,
        "NumElemsAdded" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=56, version=0)
class Microsoft_IE_56_0(Etw):
    pattern = Struct(
        "Markup" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=57, version=0)
class Microsoft_IE_57_0(Etw):
    pattern = Struct(
        "Markup" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=58, version=0)
class Microsoft_IE_58_0(Etw):
    pattern = Struct(
        "Markup" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=59, version=0)
class Microsoft_IE_59_0(Etw):
    pattern = Struct(
        "Markup" / Int64ul,
        "Zero" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=60, version=0)
class Microsoft_IE_60_0(Etw):
    pattern = Struct(
        "Markup" / Int64ul,
        "HR" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=61, version=0)
class Microsoft_IE_61_0(Etw):
    pattern = Struct(
        "Markup" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=62, version=0)
class Microsoft_IE_62_0(Etw):
    pattern = Struct(
        "Markup" / Int64ul,
        "HR" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=63, version=0)
class Microsoft_IE_63_0(Etw):
    pattern = Struct(
        "Zero2" / Int64ul,
        "Zero1" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=64, version=0)
class Microsoft_IE_64_0(Etw):
    pattern = Struct(
        "Zero2" / Int64ul,
        "Zero1" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=65, version=0)
class Microsoft_IE_65_0(Etw):
    pattern = Struct(
        "CDoc" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=66, version=0)
class Microsoft_IE_66_0(Etw):
    pattern = Struct(
        "CView" / Int64ul,
        "fSynchronousRedraw" / Int32ul,
        "left" / Int32ul,
        "top" / Int32ul,
        "right" / Int32ul,
        "bottom" / Int32ul,
        "fInvalChildWindows" / Int32ul,
        "fPostRender" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=67, version=0)
class Microsoft_IE_67_0(Etw):
    pattern = Struct(
        "CView" / Int64ul,
        "fSynchronousRedraw" / Int32ul,
        "left" / Int32ul,
        "top" / Int32ul,
        "right" / Int32ul,
        "bottom" / Int32ul,
        "fInvalChildWindows" / Int32ul,
        "fPostRender" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=68, version=0)
class Microsoft_IE_68_0(Etw):
    pattern = Struct(
        "HRGN" / Int32ul,
        "dwFlags" / Int32ul,
        "left" / Int32ul,
        "top" / Int32ul,
        "right" / Int32ul,
        "bottom" / Int32ul,
        "NoUpdSink" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=69, version=0)
class Microsoft_IE_69_0(Etw):
    pattern = Struct(
        "fParseNow" / Int32ul,
        "Length" / Int32ul,
        "Script" / Bytes(lambda this: this.Length)
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=70, version=0)
class Microsoft_IE_70_0(Etw):
    pattern = Struct(
        "window" / Int64ul,
        "FlagsOrResult" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=71, version=0)
class Microsoft_IE_71_0(Etw):
    pattern = Struct(
        "window" / Int64ul,
        "FlagsOrResult" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=72, version=0)
class Microsoft_IE_72_0(Etw):
    pattern = Struct(
        "zero" / Int32ul,
        "zero1" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=73, version=0)
class Microsoft_IE_73_0(Etw):
    pattern = Struct(
        "CHtmPrePtr" / Int64ul,
        "Object" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=74, version=0)
class Microsoft_IE_74_0(Etw):
    pattern = Struct(
        "HR" / Int32ul,
        "CHtmPrePtr" / Int64ul,
        "fDataPend" / Int32ul,
        "fSuspended" / Int32ul,
        "Object" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=75, version=0)
class Microsoft_IE_75_0(Etw):
    pattern = Struct(
        "CImgTaskPtr" / Int64ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=76, version=0)
class Microsoft_IE_76_0(Etw):
    pattern = Struct(
        "CImgTaskPtr" / Int64ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=77, version=0)
class Microsoft_IE_77_0(Etw):
    pattern = Struct(
        "CImgTaskPtr" / Int64ul,
        "cbRead" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=78, version=0)
class Microsoft_IE_78_0(Etw):
    pattern = Struct(
        "CImgTaskPtr" / Int64ul,
        "cbRead" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=79, version=0)
class Microsoft_IE_79_0(Etw):
    pattern = Struct(
        "CDwnTaskPtr" / Int64ul,
        "Zero" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=80, version=0)
class Microsoft_IE_80_0(Etw):
    pattern = Struct(
        "CDwnTaskPtr" / Int64ul,
        "Zero" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=81, version=0)
class Microsoft_IE_81_0(Etw):
    pattern = Struct(
        "CDwnTaskPtr" / Int64ul,
        "Zero" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=82, version=0)
class Microsoft_IE_82_0(Etw):
    pattern = Struct(
        "CDoc" / Int64ul,
        "Nesting" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=83, version=0)
class Microsoft_IE_83_0(Etw):
    pattern = Struct(
        "CDoc" / Int64ul,
        "Nesting" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=84, version=0)
class Microsoft_IE_84_0(Etw):
    pattern = Struct(
        "CDoc" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=84, version=1)
class Microsoft_IE_84_1(Etw):
    pattern = Struct(
        "CDoc" / Int64ul,
        "EventContextId" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=85, version=0)
class Microsoft_IE_85_0(Etw):
    pattern = Struct(
        "CDoc" / Int64ul,
        "HR" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=85, version=1)
class Microsoft_IE_85_1(Etw):
    pattern = Struct(
        "CDoc" / Int64ul,
        "HR" / Int32ul,
        "EventContextId" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=86, version=0)
class Microsoft_IE_86_0(Etw):
    pattern = Struct(
        "PtrIn" / Int64ul,
        "dwTimeout" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=87, version=0)
class Microsoft_IE_87_0(Etw):
    pattern = Struct(
        "PtrOut" / Int64ul,
        "ExitCode" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=88, version=0)
class Microsoft_IE_88_0(Etw):
    pattern = Struct(
        "PtrIn" / Int64ul,
        "dwTimeout" / Int32ul,
        "Object" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=88, version=1)
class Microsoft_IE_88_1(Etw):
    pattern = Struct(
        "PtrIn" / Int64ul,
        "dwTimeout" / Int32ul,
        "Object" / Int64ul,
        "EventContextId" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=89, version=0)
class Microsoft_IE_89_0(Etw):
    pattern = Struct(
        "PtrOut" / Int64ul,
        "ExitCode" / Int32ul,
        "Object" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=89, version=1)
class Microsoft_IE_89_1(Etw):
    pattern = Struct(
        "PtrOut" / Int64ul,
        "ExitCode" / Int32ul,
        "Object" / Int64ul,
        "EventContextId" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=90, version=0)
class Microsoft_IE_90_0(Etw):
    pattern = Struct(
        "CImgTaskPtr" / Int64ul,
        "URL" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=92, version=0)
class Microsoft_IE_92_0(Etw):
    pattern = Struct(
        "Buffer" / Int64ul,
        "Depth" / Int32ul,
        "Width" / Int32ul,
        "Height" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=100, version=0)
class Microsoft_IE_100_0(Etw):
    pattern = Struct(
        "left" / Int32ul,
        "top" / Int32ul,
        "right" / Int32ul,
        "bottom" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=101, version=0)
class Microsoft_IE_101_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=102, version=0)
class Microsoft_IE_102_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=103, version=0)
class Microsoft_IE_103_0(Etw):
    pattern = Struct(
        "Storage" / Int64ul,
        "Key" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=104, version=0)
class Microsoft_IE_104_0(Etw):
    pattern = Struct(
        "Storage" / Int64ul,
        "Key" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=105, version=0)
class Microsoft_IE_105_0(Etw):
    pattern = Struct(
        "Storage" / Int64ul,
        "Key" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=106, version=0)
class Microsoft_IE_106_0(Etw):
    pattern = Struct(
        "Storage" / Int64ul,
        "Key" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=107, version=0)
class Microsoft_IE_107_0(Etw):
    pattern = Struct(
        "Storage" / Int64ul,
        "Key" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=108, version=0)
class Microsoft_IE_108_0(Etw):
    pattern = Struct(
        "Storage" / Int64ul,
        "Key" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=109, version=0)
class Microsoft_IE_109_0(Etw):
    pattern = Struct(
        "StorageHelper" / Int64ul,
        "Domain" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=110, version=0)
class Microsoft_IE_110_0(Etw):
    pattern = Struct(
        "StorageHelper" / Int64ul,
        "Domain" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=111, version=0)
class Microsoft_IE_111_0(Etw):
    pattern = Struct(
        "StorageHelper" / Int64ul,
        "Domain" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=112, version=0)
class Microsoft_IE_112_0(Etw):
    pattern = Struct(
        "StorageHelper" / Int64ul,
        "Domain" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=113, version=0)
class Microsoft_IE_113_0(Etw):
    pattern = Struct(
        "StorageListHelper" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=114, version=0)
class Microsoft_IE_114_0(Etw):
    pattern = Struct(
        "StorageListHelper" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=115, version=0)
class Microsoft_IE_115_0(Etw):
    pattern = Struct(
        "StorageListHelper" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=116, version=0)
class Microsoft_IE_116_0(Etw):
    pattern = Struct(
        "StorageListHelper" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=117, version=0)
class Microsoft_IE_117_0(Etw):
    pattern = Struct(
        "Thunk" / Int64ul,
        "GrfDex" / Int32ul,
        "Zero1" / Int32ul,
        "Zero2" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=118, version=0)
class Microsoft_IE_118_0(Etw):
    pattern = Struct(
        "Thunk" / Int64ul,
        "hr" / Int32ul,
        "DispID" / Int32ul,
        "Versioned" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=119, version=0)
class Microsoft_IE_119_0(Etw):
    pattern = Struct(
        "Thunk" / Int64ul,
        "DispID" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=120, version=0)
class Microsoft_IE_120_0(Etw):
    pattern = Struct(
        "Thunk" / Int64ul,
        "DispID" / Int32ul,
        "Derived" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=121, version=0)
class Microsoft_IE_121_0(Etw):
    pattern = Struct(
        "VTable" / Int64ul,
        "MethodType" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=122, version=0)
class Microsoft_IE_122_0(Etw):
    pattern = Struct(
        "Instance" / Int64ul,
        "OptionalArgs" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=123, version=0)
class Microsoft_IE_123_0(Etw):
    pattern = Struct(
        "Parser" / Int64ul,
        "ParserType" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=123, version=1)
class Microsoft_IE_123_1(Etw):
    pattern = Struct(
        "Parser" / Int64ul,
        "ParserType" / Int32ul,
        "ParseType" / Int32ul,
        "URL" / WString,
        "IsInline" / Int8ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=123, version=2)
class Microsoft_IE_123_2(Etw):
    pattern = Struct(
        "Parser" / Int64ul,
        "ParserType" / Int32ul,
        "ParseType" / Int32ul,
        "URL" / WString,
        "IsInline" / Int8ul,
        "EventContextId" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=124, version=0)
class Microsoft_IE_124_0(Etw):
    pattern = Struct(
        "Parser" / Int64ul,
        "ParserType" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=124, version=1)
class Microsoft_IE_124_1(Etw):
    pattern = Struct(
        "Parser" / Int64ul,
        "ParserType" / Int32ul,
        "ParseType" / Int32ul,
        "URL" / WString,
        "IsInline" / Int8ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=124, version=2)
class Microsoft_IE_124_2(Etw):
    pattern = Struct(
        "Parser" / Int64ul,
        "ParserType" / Int32ul,
        "ParseType" / Int32ul,
        "URL" / WString,
        "IsInline" / Int8ul,
        "EventContextId" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=125, version=0)
class Microsoft_IE_125_0(Etw):
    pattern = Struct(
        "TreeNode" / Int64ul,
        "NodeType" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=125, version=1)
class Microsoft_IE_125_1(Etw):
    pattern = Struct(
        "TreeNode" / Int64ul,
        "NodeType" / Int32ul,
        "EventContextId" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=126, version=0)
class Microsoft_IE_126_0(Etw):
    pattern = Struct(
        "TreeNode" / Int64ul,
        "NodeType" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=126, version=1)
class Microsoft_IE_126_1(Etw):
    pattern = Struct(
        "TreeNode" / Int64ul,
        "NodeType" / Int32ul,
        "EventContextId" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=127, version=0)
class Microsoft_IE_127_0(Etw):
    pattern = Struct(
        "Element" / Int64ul,
        "Zero" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=128, version=0)
class Microsoft_IE_128_0(Etw):
    pattern = Struct(
        "Element" / Int64ul,
        "Zero" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=129, version=0)
class Microsoft_IE_129_0(Etw):
    pattern = Struct(
        "Element" / Int64ul,
        "Zero" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=130, version=0)
class Microsoft_IE_130_0(Etw):
    pattern = Struct(
        "Element" / Int64ul,
        "Zero" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=131, version=0)
class Microsoft_IE_131_0(Etw):
    pattern = Struct(
        "Element" / Int64ul,
        "Zero" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=132, version=0)
class Microsoft_IE_132_0(Etw):
    pattern = Struct(
        "Element" / Int64ul,
        "Zero" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=133, version=0)
class Microsoft_IE_133_0(Etw):
    pattern = Struct(
        "Cache" / Int64ul,
        "Index" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=134, version=0)
class Microsoft_IE_134_0(Etw):
    pattern = Struct(
        "Cache" / Int64ul,
        "Index" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=135, version=0)
class Microsoft_IE_135_0(Etw):
    pattern = Struct(
        "Cache" / Int64ul,
        "Index" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=136, version=0)
class Microsoft_IE_136_0(Etw):
    pattern = Struct(
        "Cache" / Int64ul,
        "Index" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=137, version=0)
class Microsoft_IE_137_0(Etw):
    pattern = Struct(
        "View" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=138, version=0)
class Microsoft_IE_138_0(Etw):
    pattern = Struct(
        "View" / Int64ul,
        "Exit" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=139, version=0)
class Microsoft_IE_139_0(Etw):
    pattern = Struct(
        "View" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=140, version=0)
class Microsoft_IE_140_0(Etw):
    pattern = Struct(
        "View" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=141, version=0)
class Microsoft_IE_141_0(Etw):
    pattern = Struct(
        "URL" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=142, version=0)
class Microsoft_IE_142_0(Etw):
    pattern = Struct(
        "URL" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=143, version=0)
class Microsoft_IE_143_0(Etw):
    pattern = Struct(
        "URL" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=144, version=0)
class Microsoft_IE_144_0(Etw):
    pattern = Struct(
        "URL" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=145, version=0)
class Microsoft_IE_145_0(Etw):
    pattern = Struct(
        "Storage" / Int64ul,
        "Key" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=146, version=0)
class Microsoft_IE_146_0(Etw):
    pattern = Struct(
        "Storage" / Int64ul,
        "Key" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=147, version=0)
class Microsoft_IE_147_0(Etw):
    pattern = Struct(
        "Storage" / Int64ul,
        "Key" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=148, version=0)
class Microsoft_IE_148_0(Etw):
    pattern = Struct(
        "Storage" / Int64ul,
        "Key" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=150, version=0)
class Microsoft_IE_150_0(Etw):
    pattern = Struct(
        "CWindow" / Int64ul,
        "Markup" / Int64ul,
        "EventName" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=151, version=0)
class Microsoft_IE_151_0(Etw):
    pattern = Struct(
        "COleSite" / Int64ul,
        "CLSID" / Guid,
        "left" / Int32ul,
        "top" / Int32ul,
        "right" / Int32ul,
        "bottom" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=157, version=0)
class Microsoft_IE_157_0(Etw):
    pattern = Struct(
        "CDoc" / Int64ul,
        "Nesting" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=158, version=0)
class Microsoft_IE_158_0(Etw):
    pattern = Struct(
        "CDoc" / Int64ul,
        "Nesting" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=165, version=0)
class Microsoft_IE_165_0(Etw):
    pattern = Struct(
        "CXmlPrePtr" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=166, version=0)
class Microsoft_IE_166_0(Etw):
    pattern = Struct(
        "HR" / Int32ul,
        "CXmlPrePtr" / Int64ul,
        "fDataPend" / Int32ul,
        "fSuspended" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=167, version=0)
class Microsoft_IE_167_0(Etw):
    pattern = Struct(
        "HR" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=168, version=0)
class Microsoft_IE_168_0(Etw):
    pattern = Struct(
        "Element" / Int64ul,
        "Zero" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=169, version=0)
class Microsoft_IE_169_0(Etw):
    pattern = Struct(
        "Element" / Int64ul,
        "Zero" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=170, version=0)
class Microsoft_IE_170_0(Etw):
    pattern = Struct(
        "Element" / Int64ul,
        "Zero" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=171, version=0)
class Microsoft_IE_171_0(Etw):
    pattern = Struct(
        "Element" / Int64ul,
        "Zero" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=172, version=0)
class Microsoft_IE_172_0(Etw):
    pattern = Struct(
        "Element" / Int64ul,
        "Zero" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=173, version=0)
class Microsoft_IE_173_0(Etw):
    pattern = Struct(
        "Element" / Int64ul,
        "Zero" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=174, version=0)
class Microsoft_IE_174_0(Etw):
    pattern = Struct(
        "Element" / Int64ul,
        "Zero" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=175, version=0)
class Microsoft_IE_175_0(Etw):
    pattern = Struct(
        "Element" / Int64ul,
        "Zero" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=178, version=0)
class Microsoft_IE_178_0(Etw):
    pattern = Struct(
        "RenderTarget" / Int64ul,
        "TargetSurfaceBaseType" / Int32ul,
        "TargetSurfaceSubType" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=179, version=0)
class Microsoft_IE_179_0(Etw):
    pattern = Struct(
        "RenderTarget" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=180, version=0)
class Microsoft_IE_180_0(Etw):
    pattern = Struct(
        "ImgInfo" / Int64ul,
        "ImgTask" / Int64ul,
        "ImgCacheEntry" / Int64ul,
        "Width" / Int32ul,
        "Height" / Int32ul,
        "CompressedSize" / Int32ul,
        "BitCount" / Int32ul,
        "ChromaSubsampling" / Int16ul,
        "URL" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=181, version=0)
class Microsoft_IE_181_0(Etw):
    pattern = Struct(
        "ImgCacheEntry" / Int64ul,
        "ImgInfo" / Int64ul,
        "FrameIndex" / Int32ul,
        "ImgBits" / Int64ul,
        "ImgBitsSize" / Int32ul,
        "Width" / Int32ul,
        "Height" / Int32ul,
        "BitCount" / Int8ul,
        "IsSolidColor" / Int8ul,
        "IsTransparent" / Int8ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=182, version=0)
class Microsoft_IE_182_0(Etw):
    pattern = Struct(
        "ImgCacheEntry" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=183, version=0)
class Microsoft_IE_183_0(Etw):
    pattern = Struct(
        "ImgCacheEntry" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=184, version=0)
class Microsoft_IE_184_0(Etw):
    pattern = Struct(
        "ImgCacheEntry" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=185, version=0)
class Microsoft_IE_185_0(Etw):
    pattern = Struct(
        "DwnInfo" / Int64ul,
        "HitDwnInfo" / Int64ul,
        "IsHitDwnInfoActive" / Int8ul,
        "URL" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=186, version=0)
class Microsoft_IE_186_0(Etw):
    pattern = Struct(
        "ImgCacheEntry" / Int64ul,
        "DestLeft" / Float32l,
        "DestTop" / Float32l,
        "DestRight" / Float32l,
        "DestBottom" / Float32l,
        "ScaledSizeWidth" / Float32l,
        "ScaledSizeHeight" / Float32l,
        "TranslateX" / Float32l,
        "TranslateY" / Float32l,
        "Opacity" / Float32l,
        "Tiled" / Int32ul,
        "UnscaledSizeWidth" / Int32ul,
        "UnscaledSizeHeight" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=187, version=0)
class Microsoft_IE_187_0(Etw):
    pattern = Struct(
        "DwnInfo" / Int64ul,
        "DecodeFlags" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=192, version=0)
class Microsoft_IE_192_0(Etw):
    pattern = Struct(
        "CurrentX" / Int32sl,
        "CurrentY" / Int32sl,
        "DeltaX" / Int32sl,
        "DeltaY" / Int32sl
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=194, version=0)
class Microsoft_IE_194_0(Etw):
    pattern = Struct(
        "TimeSinceStartUs" / Int32ul,
        "ExpectedFrameTimeUs" / Int32ul,
        "LastScrollTimeUs" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=197, version=0)
class Microsoft_IE_197_0(Etw):
    pattern = Struct(
        "Allocator" / Int64ul,
        "Allocation" / Int64ul,
        "Size" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=198, version=0)
class Microsoft_IE_198_0(Etw):
    pattern = Struct(
        "Allocator" / Int64ul,
        "Allocation" / Int64ul,
        "Size" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=199, version=0)
class Microsoft_IE_199_0(Etw):
    pattern = Struct(
        "Allocator" / Int64ul,
        "Allocation" / Int64ul,
        "Size" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=200, version=0)
class Microsoft_IE_200_0(Etw):
    pattern = Struct(
        "Allocator" / Int64ul,
        "Allocation" / Int64ul,
        "Size" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=201, version=0)
class Microsoft_IE_201_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "TimerId" / Int32ul,
        "DeltaMs" / Int32sl,
        "PeriodMs" / Int32sl,
        "CurrentTimeMs" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=201, version=1)
class Microsoft_IE_201_1(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "TimerId" / Int32ul,
        "DeltaMs" / Int32sl,
        "PeriodMs" / Int32sl,
        "CurrentTimeMs" / Int64ul,
        "Flags" / Int32ul,
        "Callback" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=202, version=0)
class Microsoft_IE_202_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "TimerId" / Int32ul,
        "DeltaMs" / Int32sl,
        "PeriodMs" / Int32sl,
        "CurrentTimeMs" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=202, version=1)
class Microsoft_IE_202_1(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "TimerId" / Int32ul,
        "DeltaMs" / Int32sl,
        "PeriodMs" / Int32sl,
        "CurrentTimeMs" / Int64ul,
        "Flags" / Int32ul,
        "Callback" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=203, version=0)
class Microsoft_IE_203_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "TimerId" / Int32ul,
        "DeltaMs" / Int32sl,
        "PeriodMs" / Int32sl,
        "CurrentTimeMs" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=203, version=1)
class Microsoft_IE_203_1(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "TimerId" / Int32ul,
        "DeltaMs" / Int32sl,
        "PeriodMs" / Int32sl,
        "CurrentTimeMs" / Int64ul,
        "Flags" / Int32ul,
        "Callback" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=204, version=0)
class Microsoft_IE_204_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "CurrentTimeMs" / Int64ul,
        "DeltaMs" / Int32sl,
        "BeatPeriodMs" / Int32ul,
        "RefreshMultipleUs" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=205, version=0)
class Microsoft_IE_205_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "CurrentTimeMs" / Int64ul,
        "DeltaMs" / Int32sl,
        "BeatPeriodMs" / Int32ul,
        "RefreshMultipleUs" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=206, version=0)
class Microsoft_IE_206_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "CurrentTimeMs" / Int64ul,
        "DeltaMs" / Int32sl,
        "BeatPeriodMs" / Int32ul,
        "RefreshMultipleUs" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=207, version=0)
class Microsoft_IE_207_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Value" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=208, version=0)
class Microsoft_IE_208_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Value" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=209, version=0)
class Microsoft_IE_209_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Value" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=211, version=0)
class Microsoft_IE_211_0(Etw):
    pattern = Struct(
        "Name" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=212, version=0)
class Microsoft_IE_212_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "StartMark" / WString,
        "EndMark" / WString,
        "Duration" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=213, version=0)
class Microsoft_IE_213_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Value" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=214, version=0)
class Microsoft_IE_214_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Value" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=216, version=0)
class Microsoft_IE_216_0(Etw):
    pattern = Struct(
        "MediaEngineID" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=217, version=0)
class Microsoft_IE_217_0(Etw):
    pattern = Struct(
        "MediaEngineID" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=218, version=0)
class Microsoft_IE_218_0(Etw):
    pattern = Struct(
        "MediaEngineID" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=219, version=0)
class Microsoft_IE_219_0(Etw):
    pattern = Struct(
        "MediaEngineID" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=220, version=0)
class Microsoft_IE_220_0(Etw):
    pattern = Struct(
        "MediaEngineID" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=221, version=0)
class Microsoft_IE_221_0(Etw):
    pattern = Struct(
        "MediaEngineID" / Int32ul,
        "Time" / Float32l
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=222, version=0)
class Microsoft_IE_222_0(Etw):
    pattern = Struct(
        "MediaEngineID" / Int32ul,
        "hrResult" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=223, version=0)
class Microsoft_IE_223_0(Etw):
    pattern = Struct(
        "MediaEngineID" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=224, version=0)
class Microsoft_IE_224_0(Etw):
    pattern = Struct(
        "MediaEngineID" / Int32ul,
        "Rate" / Float32l
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=225, version=0)
class Microsoft_IE_225_0(Etw):
    pattern = Struct(
        "MediaEngineID" / Int32ul,
        "majortype" / Guid,
        "subtype" / Guid
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=226, version=0)
class Microsoft_IE_226_0(Etw):
    pattern = Struct(
        "MediaEngineID" / Int32ul,
        "format" / Int32ul,
        "width" / Int32ul,
        "height" / Int32ul,
        "frameratenum" / Int32ul,
        "framerateden" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=227, version=0)
class Microsoft_IE_227_0(Etw):
    pattern = Struct(
        "MediaEngineID" / Int32ul,
        "numchannels" / Int32ul,
        "samplespersec" / Int32ul,
        "bitspersample" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=228, version=0)
class Microsoft_IE_228_0(Etw):
    pattern = Struct(
        "MediaEngineID" / Int32ul,
        "left" / Int32ul,
        "top" / Int32ul,
        "right" / Int32ul,
        "bottom" / Int32ul,
        "sampletime" / Int64ul,
        "processtime" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=229, version=0)
class Microsoft_IE_229_0(Etw):
    pattern = Struct(
        "MediaEngineID" / Int32ul,
        "reason" / Int32ul,
        "sampletime" / Int64ul,
        "processtime" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=230, version=0)
class Microsoft_IE_230_0(Etw):
    pattern = Struct(
        "MediaEngineID" / Int32ul,
        "lag" / Int64sl
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=235, version=0)
class Microsoft_IE_235_0(Etw):
    pattern = Struct(
        "MediaEngineID" / Int32ul,
        "sampletime" / Int64ul,
        "dataPresented" / Float32l
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=236, version=0)
class Microsoft_IE_236_0(Etw):
    pattern = Struct(
        "MediaEngineID" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=237, version=0)
class Microsoft_IE_237_0(Etw):
    pattern = Struct(
        "MediaEngineID" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=238, version=0)
class Microsoft_IE_238_0(Etw):
    pattern = Struct(
        "ImgInfo" / Int64ul,
        "ImgTask" / Int64ul,
        "ImgCacheEntry" / Int64ul,
        "Width" / Int32ul,
        "Height" / Int32ul,
        "CompressedSize" / Int32ul,
        "BitCount" / Int32ul,
        "ChromaSubsampling" / Int16ul,
        "URL" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=239, version=0)
class Microsoft_IE_239_0(Etw):
    pattern = Struct(
        "DwnInfo" / Int64ul,
        "DecodeFlags" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=242, version=0)
class Microsoft_IE_242_0(Etw):
    pattern = Struct(
        "TimerMan" / Int64ul,
        "Info" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=243, version=0)
class Microsoft_IE_243_0(Etw):
    pattern = Struct(
        "TimerMan" / Int64ul,
        "Info" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=244, version=0)
class Microsoft_IE_244_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Value" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=245, version=0)
class Microsoft_IE_245_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Value" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=246, version=0)
class Microsoft_IE_246_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Value" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=247, version=0)
class Microsoft_IE_247_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Value" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=248, version=0)
class Microsoft_IE_248_0(Etw):
    pattern = Struct(
        "Presenter" / Int64ul,
        "x" / Int32ul,
        "y" / Int32ul,
        "width" / Int32ul,
        "height" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=249, version=0)
class Microsoft_IE_249_0(Etw):
    pattern = Struct(
        "Presenter" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=250, version=0)
class Microsoft_IE_250_0(Etw):
    pattern = Struct(
        "MediaEngineID" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=251, version=0)
class Microsoft_IE_251_0(Etw):
    pattern = Struct(
        "MediaEngineID" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=252, version=0)
class Microsoft_IE_252_0(Etw):
    pattern = Struct(
        "DestRight" / Float32l,
        "DestBottom" / Float32l
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=253, version=0)
class Microsoft_IE_253_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=254, version=0)
class Microsoft_IE_254_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=255, version=0)
class Microsoft_IE_255_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=338, version=0)
class Microsoft_IE_338_0(Etw):
    pattern = Struct(
        "Doc" / Int64ul,
        "MessageId" / Int32ul,
        "PointerId" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=339, version=0)
class Microsoft_IE_339_0(Etw):
    pattern = Struct(
        "Doc" / Int64ul,
        "MessageId" / Int32ul,
        "PointerId" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=340, version=0)
class Microsoft_IE_340_0(Etw):
    pattern = Struct(
        "EventType" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=341, version=0)
class Microsoft_IE_341_0(Etw):
    pattern = Struct(
        "EventType" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=342, version=0)
class Microsoft_IE_342_0(Etw):
    pattern = Struct(
        "TotalStoryboardCount" / Int32ul,
        "IndependentStoryboardCount" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=343, version=0)
class Microsoft_IE_343_0(Etw):
    pattern = Struct(
        "NumberOfUpdates" / Int32ul,
        "NumberOfUpdateSkips" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=348, version=0)
class Microsoft_IE_348_0(Etw):
    pattern = Struct(
        "MediaElementId" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=349, version=0)
class Microsoft_IE_349_0(Etw):
    pattern = Struct(
        "MediaElementId" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=350, version=0)
class Microsoft_IE_350_0(Etw):
    pattern = Struct(
        "MediaElementId" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=351, version=0)
class Microsoft_IE_351_0(Etw):
    pattern = Struct(
        "MediaElementId" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=352, version=0)
class Microsoft_IE_352_0(Etw):
    pattern = Struct(
        "MediaElementId" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=353, version=0)
class Microsoft_IE_353_0(Etw):
    pattern = Struct(
        "MediaElementId" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=354, version=0)
class Microsoft_IE_354_0(Etw):
    pattern = Struct(
        "MediaElementId" / Int32ul,
        "PositionInPercentage" / Double
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=355, version=0)
class Microsoft_IE_355_0(Etw):
    pattern = Struct(
        "MediaElementId" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=356, version=0)
class Microsoft_IE_356_0(Etw):
    pattern = Struct(
        "MediaElementId" / Int32ul,
        "TimeDurationInSecs" / Double
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=357, version=0)
class Microsoft_IE_357_0(Etw):
    pattern = Struct(
        "MediaElementId" / Int32ul,
        "TimeDurationInSecs" / Double
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=358, version=0)
class Microsoft_IE_358_0(Etw):
    pattern = Struct(
        "MediaElementId" / Int32ul,
        "PositionInPercentage" / Double
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=359, version=0)
class Microsoft_IE_359_0(Etw):
    pattern = Struct(
        "MediaElementId" / Int32ul,
        "TimeInSecs" / Double
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=360, version=0)
class Microsoft_IE_360_0(Etw):
    pattern = Struct(
        "MediaElementId" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=361, version=0)
class Microsoft_IE_361_0(Etw):
    pattern = Struct(
        "MediaElementId" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=362, version=0)
class Microsoft_IE_362_0(Etw):
    pattern = Struct(
        "MediaElementId" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=363, version=0)
class Microsoft_IE_363_0(Etw):
    pattern = Struct(
        "MediaElementId" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=364, version=0)
class Microsoft_IE_364_0(Etw):
    pattern = Struct(
        "MediaElementId" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=365, version=0)
class Microsoft_IE_365_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=366, version=0)
class Microsoft_IE_366_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=375, version=0)
class Microsoft_IE_375_0(Etw):
    pattern = Struct(
        "Element" / Int64ul,
        "Tooltip" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=397, version=0)
class Microsoft_IE_397_0(Etw):
    pattern = Struct(
        "DispNode" / Int64ul,
        "DispLayer" / Int64ul,
        "left" / Int32sl,
        "top" / Int32sl,
        "right" / Int32sl,
        "bottom" / Int32sl,
        "ElementDDTId" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=404, version=0)
class Microsoft_IE_404_0(Etw):
    pattern = Struct(
        "MediaElementId" / Int32ul,
        "MediaElementIdAttribute" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=405, version=0)
class Microsoft_IE_405_0(Etw):
    pattern = Struct(
        "MediaElementId" / Int32ul,
        "MediaElementIdAttribute" / WString,
        "UniqueDeviceName" / WString,
        "FriendlyDeviceName" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=406, version=0)
class Microsoft_IE_406_0(Etw):
    pattern = Struct(
        "MediaElementId" / Int32ul,
        "MediaElementIdAttribute" / WString,
        "UniqueDeviceName" / WString,
        "FriendlyDeviceName" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=407, version=0)
class Microsoft_IE_407_0(Etw):
    pattern = Struct(
        "MediaElementId" / Int32ul,
        "MediaElementIdAttribute" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=408, version=1)
class Microsoft_IE_408_1(Etw):
    pattern = Struct(
        "AnimationClientObject" / Int64ul,
        "StoryboardObject" / Int64ul,
        "TreeNode" / Int64ul,
        "DurationInSeconds" / Double,
        "DelayInSeconds" / Double,
        "NumberOfProperties" / Int32ul,
        "AnimationName" / WString,
        "DDTObject" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=409, version=0)
class Microsoft_IE_409_0(Etw):
    pattern = Struct(
        "AnimationClientObject" / Int64ul,
        "TreeNode" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=410, version=1)
class Microsoft_IE_410_1(Etw):
    pattern = Struct(
        "TransitionClientObject" / Int64ul,
        "StoryboardObject" / Int64ul,
        "TreeNode" / Int64ul,
        "DurationInSeconds" / Double,
        "DelayInSeconds" / Double,
        "DISPID" / Int32ul,
        "IsReversal" / Int8ul,
        "DDTObject" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=411, version=0)
class Microsoft_IE_411_0(Etw):
    pattern = Struct(
        "AnimationClientObject" / Int64ul,
        "TreeNode" / Int64ul,
        "DISPID" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=430, version=0)
class Microsoft_IE_430_0(Etw):
    pattern = Struct(
        "WindowObject" / Int64ul,
        "IsPrimary" / Int32ul,
        "URL" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=431, version=0)
class Microsoft_IE_431_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "TimerId" / Int32ul,
        "Callback" / Int64ul,
        "Timeout" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=432, version=0)
class Microsoft_IE_432_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "TimerId" / Int32ul,
        "Callback" / Int64ul,
        "Timeout" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=433, version=0)
class Microsoft_IE_433_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "TimerId" / Int32ul,
        "Callback" / Int64ul,
        "Timeout" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=434, version=0)
class Microsoft_IE_434_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "TimerId" / Int32ul,
        "Callback" / Int64ul,
        "Timeout" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=435, version=0)
class Microsoft_IE_435_0(Etw):
    pattern = Struct(
        "MediaElementId" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=436, version=0)
class Microsoft_IE_436_0(Etw):
    pattern = Struct(
        "MediaElementId" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=437, version=0)
class Microsoft_IE_437_0(Etw):
    pattern = Struct(
        "MediaElementId" / Int32ul,
        "AnimationGroupId" / Int32ul,
        "VisualizationId" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=438, version=0)
class Microsoft_IE_438_0(Etw):
    pattern = Struct(
        "MediaElementId" / Int32ul,
        "AnimationGroupId" / Int32ul,
        "VisualizationId" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=439, version=0)
class Microsoft_IE_439_0(Etw):
    pattern = Struct(
        "MediaElementId" / Int32ul,
        "StartTimeDurationInSecs" / Double,
        "EndTimeDurationInSecs" / Double,
        "ProgressStartLevelInPercentage" / Int32sl,
        "ProgressEndLevelInPercentage" / Int32sl
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=440, version=0)
class Microsoft_IE_440_0(Etw):
    pattern = Struct(
        "GripperID" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=441, version=0)
class Microsoft_IE_441_0(Etw):
    pattern = Struct(
        "GripperID" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=456, version=0)
class Microsoft_IE_456_0(Etw):
    pattern = Struct(
        "ScrollbarLayerId" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=457, version=0)
class Microsoft_IE_457_0(Etw):
    pattern = Struct(
        "Clsid" / Guid,
        "Url" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=458, version=0)
class Microsoft_IE_458_0(Etw):
    pattern = Struct(
        "Clsid" / Guid
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=459, version=0)
class Microsoft_IE_459_0(Etw):
    pattern = Struct(
        "MediaElementId" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=460, version=0)
class Microsoft_IE_460_0(Etw):
    pattern = Struct(
        "MediaElementId" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=461, version=0)
class Microsoft_IE_461_0(Etw):
    pattern = Struct(
        "MediaElementId" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=462, version=0)
class Microsoft_IE_462_0(Etw):
    pattern = Struct(
        "AnimationID" / Int64ul,
        "AnimationInstanceObject" / Int64ul,
        "AnimationPropertyId" / Int32ul,
        "IsTransition" / Int8ul,
        "QPCScheduleTime" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=463, version=0)
class Microsoft_IE_463_0(Etw):
    pattern = Struct(
        "AnimationID" / Int64ul,
        "AnimationInstanceObject" / Int64ul,
        "TreeNode" / Int64ul,
        "PreviousAnimationState" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=464, version=0)
class Microsoft_IE_464_0(Etw):
    pattern = Struct(
        "AnimationID" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=464, version=2)
class Microsoft_IE_464_2(Etw):
    pattern = Struct(
        "CIndependentAnimation" / Int64ul,
        "ReasonCode" / Int32ul,
        "Description" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=465, version=0)
class Microsoft_IE_465_0(Etw):
    pattern = Struct(
        "DispNode" / Int64ul,
        "DispLayer" / Int64ul,
        "left" / Int32sl,
        "top" / Int32sl,
        "right" / Int32sl,
        "bottom" / Int32sl,
        "ElementDDTId" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=466, version=0)
class Microsoft_IE_466_0(Etw):
    pattern = Struct(
        "Scroller" / Int64ul,
        "RectType" / Int32sl,
        "left" / Int32sl,
        "top" / Int32sl,
        "right" / Int32sl,
        "bottom" / Int32sl
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=467, version=0)
class Microsoft_IE_467_0(Etw):
    pattern = Struct(
        "MediaElementId" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=468, version=0)
class Microsoft_IE_468_0(Etw):
    pattern = Struct(
        "CActiveScriptHolder" / Int64ul,
        "CMarkup" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=469, version=0)
class Microsoft_IE_469_0(Etw):
    pattern = Struct(
        "CActiveScriptHolder" / Int64ul,
        "CMarkup" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=470, version=0)
class Microsoft_IE_470_0(Etw):
    pattern = Struct(
        "CActiveScriptHolder" / Int64ul,
        "CMarkup" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=471, version=0)
class Microsoft_IE_471_0(Etw):
    pattern = Struct(
        "CActiveScriptHolder" / Int64ul,
        "CMarkup" / Int64ul,
        "HR" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=472, version=0)
class Microsoft_IE_472_0(Etw):
    pattern = Struct(
        "CScriptCollection" / Int64ul,
        "CMarkup" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=473, version=0)
class Microsoft_IE_473_0(Etw):
    pattern = Struct(
        "CScriptCollection" / Int64ul,
        "CMarkup" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=474, version=0)
class Microsoft_IE_474_0(Etw):
    pattern = Struct(
        "CScriptCollection" / Int64ul,
        "CMarkup" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=475, version=0)
class Microsoft_IE_475_0(Etw):
    pattern = Struct(
        "CScriptCollection" / Int64ul,
        "CMarkup" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=476, version=0)
class Microsoft_IE_476_0(Etw):
    pattern = Struct(
        "CActiveScriptHolder" / Int64ul,
        "CMarkup" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=477, version=0)
class Microsoft_IE_477_0(Etw):
    pattern = Struct(
        "CActiveScriptHolder" / Int64ul,
        "CMarkup" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=478, version=0)
class Microsoft_IE_478_0(Etw):
    pattern = Struct(
        "ScriptContext" / Int64ul,
        "FunctionId" / Int32ul,
        "Undefer" / Int8ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=479, version=0)
class Microsoft_IE_479_0(Etw):
    pattern = Struct(
        "View" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=480, version=0)
class Microsoft_IE_480_0(Etw):
    pattern = Struct(
        "View" / Int64ul,
        "ContextElement" / Int64ul,
        "Flags" / Int32ul,
        "MessageId" / Int32ul,
        "left" / Int32ul,
        "top" / Int32ul,
        "right" / Int32ul,
        "bottom" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=481, version=0)
class Microsoft_IE_481_0(Etw):
    pattern = Struct(
        "View" / Int64ul,
        "HTC" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=482, version=0)
class Microsoft_IE_482_0(Etw):
    pattern = Struct(
        "View" / Int64ul,
        "Nodes" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=483, version=0)
class Microsoft_IE_483_0(Etw):
    pattern = Struct(
        "View" / Int64ul,
        "UniqueSubtrees" / Int32ul,
        "UpdatedSubtrees" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=484, version=0)
class Microsoft_IE_484_0(Etw):
    pattern = Struct(
        "CDispNode" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=485, version=0)
class Microsoft_IE_485_0(Etw):
    pattern = Struct(
        "CDispNode" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=486, version=0)
class Microsoft_IE_486_0(Etw):
    pattern = Struct(
        "CDoc" / Int64ul,
        "CElement" / Int64ul,
        "ElementTag" / Int32ul,
        "PrimaryTouchHandler" / Int8ul,
        "IndpendentlyComposed" / Int8ul,
        "TouchConfiguration" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=487, version=0)
class Microsoft_IE_487_0(Etw):
    pattern = Struct(
        "CDoc" / Int64ul,
        "MsgID" / Int32ul,
        "x" / Int32ul,
        "y" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=488, version=0)
class Microsoft_IE_488_0(Etw):
    pattern = Struct(
        "CDoc" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=489, version=0)
class Microsoft_IE_489_0(Etw):
    pattern = Struct(
        "PointerID" / Int32sl
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=490, version=0)
class Microsoft_IE_490_0(Etw):
    pattern = Struct(
        "PointerID" / Int32sl
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=491, version=0)
class Microsoft_IE_491_0(Etw):
    pattern = Struct(
        "PointerID" / Int32sl,
        "DependentRegion" / Int8ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=492, version=0)
class Microsoft_IE_492_0(Etw):
    pattern = Struct(
        "OldState" / Int32ul,
        "NewState" / Int32ul,
        "SuspendTimer" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=493, version=0)
class Microsoft_IE_493_0(Etw):
    pattern = Struct(
        "AnimationClientObject" / Int64ul,
        "TreeNode" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=493, version=2)
class Microsoft_IE_493_2(Etw):
    pattern = Struct(
        "AnimationClientObject" / Int64ul,
        "TreeNode" / Int64ul,
        "ReasonCode" / Int32ul,
        "Description" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=494, version=0)
class Microsoft_IE_494_0(Etw):
    pattern = Struct(
        "AnimationClientObject" / Int64ul,
        "TreeNode" / Int64ul,
        "DISPID" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=494, version=2)
class Microsoft_IE_494_2(Etw):
    pattern = Struct(
        "AnimationClientObject" / Int64ul,
        "TreeNode" / Int64ul,
        "DISPID" / Int32ul,
        "ReasonCode" / Int32ul,
        "Description" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=495, version=0)
class Microsoft_IE_495_0(Etw):
    pattern = Struct(
        "URL" / WString,
        "DataSize" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=496, version=0)
class Microsoft_IE_496_0(Etw):
    pattern = Struct(
        "IntersectingLayerNode" / Int64ul,
        "NewImplicitLayerNode" / Int64ul,
        "ImplicitLayerCount" / Int32sl
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=498, version=0)
class Microsoft_IE_498_0(Etw):
    pattern = Struct(
        "Doc" / Int64ul,
        "PointerID" / Int32sl,
        "Timer" / Int8ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=499, version=0)
class Microsoft_IE_499_0(Etw):
    pattern = Struct(
        "DispNode" / Int64ul,
        "DispLayer" / Int64ul,
        "SBLayer" / Int64ul,
        "LayerWidth" / Int32sl,
        "LayerHeight" / Int32sl,
        "GlobalLayerLeft" / Int32sl,
        "GlobalLayerTop" / Int32sl,
        "GlobalLayerRight" / Int32sl,
        "GlobalLayerBottom" / Int32sl,
        "DestinationType" / Int32sl,
        "Flags" / Int32ul,
        "TransformM11" / Float32l,
        "TransformM12" / Float32l,
        "TransformM21" / Float32l,
        "TransformM22" / Float32l,
        "TransformDx" / Float32l,
        "TransformDy" / Float32l
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=500, version=0)
class Microsoft_IE_500_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=501, version=0)
class Microsoft_IE_501_0(Etw):
    pattern = Struct(
        "SBLayer" / Int64ul,
        "DCompSurface" / Int64ul,
        "Width" / Int32sl,
        "Height" / Int32sl,
        "AlphaMode" / Int32ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=502, version=0)
class Microsoft_IE_502_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=503, version=0)
class Microsoft_IE_503_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "RectsLength" / Int16ul,
        "Rects" / Bytes(lambda this: this.RectsLength)
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=504, version=0)
class Microsoft_IE_504_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "RectsLength" / Int16ul,
        "Rects" / Bytes(lambda this: this.RectsLength)
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=505, version=0)
class Microsoft_IE_505_0(Etw):
    pattern = Struct(
        "left" / Int32ul,
        "top" / Int32ul,
        "right" / Int32ul,
        "bottom" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=506, version=0)
class Microsoft_IE_506_0(Etw):
    pattern = Struct(
        "Scroller" / Int64ul,
        "RectType" / Int32sl,
        "left" / Int32sl,
        "top" / Int32sl,
        "right" / Int32sl,
        "bottom" / Int32sl
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=508, version=0)
class Microsoft_IE_508_0(Etw):
    pattern = Struct(
        "Success" / Int8ul,
        "MatchType" / Int32ul,
        "Uri" / WString,
        "TextContent" / WString,
        "FileVersion" / Int32ul,
        "RuleID" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=510, version=0)
class Microsoft_IE_510_0(Etw):
    pattern = Struct(
        "Success" / Int8ul,
        "MatchType" / Int32ul,
        "Uri" / WString,
        "TextContent" / WString,
        "FileVersion" / Int32ul,
        "RuleID" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=512, version=0)
class Microsoft_IE_512_0(Etw):
    pattern = Struct(
        "CView" / Int64ul,
        "ElementsInvalidated" / Int32ul,
        "InvalidationFlags" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=513, version=0)
class Microsoft_IE_513_0(Etw):
    pattern = Struct(
        "URL" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=514, version=0)
class Microsoft_IE_514_0(Etw):
    pattern = Struct(
        "DispNode" / Int64ul,
        "NodeDescription" / WString,
        "ReasonCode" / Int32sl,
        "ReasonDescription" / WString,
        "DispNode2" / Int64ul,
        "NodeDescription2" / WString,
        "CandidacyCode" / Int32sl
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=515, version=0)
class Microsoft_IE_515_0(Etw):
    pattern = Struct(
        "DispNode" / Int64ul,
        "NodeDescription" / WString,
        "HasDependentCompositionEffect" / Int8ul,
        "HasRoundedBorders" / Int8ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=516, version=0)
class Microsoft_IE_516_0(Etw):
    pattern = Struct(
        "DispNode" / Int64ul,
        "NodeDescription" / WString,
        "ReasonCode" / Int32sl
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=517, version=0)
class Microsoft_IE_517_0(Etw):
    pattern = Struct(
        "MediaElementId" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=518, version=0)
class Microsoft_IE_518_0(Etw):
    pattern = Struct(
        "MediaElementId" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=519, version=0)
class Microsoft_IE_519_0(Etw):
    pattern = Struct(
        "MediaElementId" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=520, version=0)
class Microsoft_IE_520_0(Etw):
    pattern = Struct(
        "MediaElementId" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=523, version=0)
class Microsoft_IE_523_0(Etw):
    pattern = Struct(
        "AnimationInstanceObject" / Int64ul,
        "AnimationStoryboardObject" / Int64ul,
        "DISPID" / Int32ul,
        "IsTransition" / Int8ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=524, version=0)
class Microsoft_IE_524_0(Etw):
    pattern = Struct(
        "AnimationInstanceObject" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=525, version=0)
class Microsoft_IE_525_0(Etw):
    pattern = Struct(
        "CHTMLCanvasElement" / Int64ul,
        "Operation" / Int32ul,
        "canvasWidth" / Int32ul,
        "canvasHeight" / Int32ul,
        "DestLeft" / Float32l,
        "DestTop" / Float32l,
        "ScaledSizeWidth" / Float32l,
        "ScaledSizeHeight" / Float32l
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=526, version=0)
class Microsoft_IE_526_0(Etw):
    pattern = Struct(
        "EventType" / WString,
        "EventParam" / Int64ul,
        "EventTarget" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=526, version=1)
class Microsoft_IE_526_1(Etw):
    pattern = Struct(
        "EventType" / WString,
        "EventParam" / Int64ul,
        "EventTarget" / Int64ul,
        "EventContextId" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=527, version=0)
class Microsoft_IE_527_0(Etw):
    pattern = Struct(
        "EventType" / WString,
        "EventParam" / Int64ul,
        "EventTarget" / Int64ul,
        "PropagationStatus" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=527, version=1)
class Microsoft_IE_527_1(Etw):
    pattern = Struct(
        "EventType" / WString,
        "EventParam" / Int64ul,
        "EventTarget" / Int64ul,
        "PropagationStatus" / Int32ul,
        "EventContextId" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=528, version=0)
class Microsoft_IE_528_0(Etw):
    pattern = Struct(
        "EventType" / WString,
        "EventParam" / Int64ul,
        "EventTarget" / Int64ul,
        "EventPhase" / Int16ul,
        "PropagationStatus" / Int32ul,
        "ListenerUsesCapture" / Int8ul,
        "FunctionId" / Int32ul,
        "Object" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=528, version=1)
class Microsoft_IE_528_1(Etw):
    pattern = Struct(
        "EventType" / WString,
        "EventParam" / Int64ul,
        "EventTarget" / Int64ul,
        "EventPhase" / Int16ul,
        "PropagationStatus" / Int32ul,
        "ListenerUsesCapture" / Int8ul,
        "FunctionId" / Int32ul,
        "Object" / Int64ul,
        "ScriptContextId" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=529, version=0)
class Microsoft_IE_529_0(Etw):
    pattern = Struct(
        "EventType" / WString,
        "EventParam" / Int64ul,
        "EventTarget" / Int64ul,
        "EventPhase" / Int16ul,
        "PropagationStatus" / Int32ul,
        "ListenerUsesCapture" / Int8ul,
        "FunctionId" / Int32ul,
        "Object" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=529, version=1)
class Microsoft_IE_529_1(Etw):
    pattern = Struct(
        "EventType" / WString,
        "EventParam" / Int64ul,
        "EventTarget" / Int64ul,
        "EventPhase" / Int16ul,
        "PropagationStatus" / Int32ul,
        "ListenerUsesCapture" / Int8ul,
        "FunctionId" / Int32ul,
        "Object" / Int64ul,
        "ScriptContextId" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=530, version=0)
class Microsoft_IE_530_0(Etw):
    pattern = Struct(
        "TimerType" / Int32ul,
        "CallbackCookie" / Int32ul,
        "FunctionId" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=530, version=1)
class Microsoft_IE_530_1(Etw):
    pattern = Struct(
        "TimerType" / Int32ul,
        "CallbackCookie" / Int32ul,
        "FunctionId" / Int32ul,
        "TimeoutValue" / Int32ul,
        "ScriptContextId" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=530, version=2)
class Microsoft_IE_530_2(Etw):
    pattern = Struct(
        "TimerType" / Int32ul,
        "CallbackCookie" / Int32ul,
        "FunctionId" / Int32ul,
        "TimeoutValue" / Int32ul,
        "ScriptContextId" / Int64ul,
        "EventContextId" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=531, version=0)
class Microsoft_IE_531_0(Etw):
    pattern = Struct(
        "TimerType" / Int32ul,
        "CallbackCookie" / Int32ul,
        "FunctionId" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=531, version=1)
class Microsoft_IE_531_1(Etw):
    pattern = Struct(
        "TimerType" / Int32ul,
        "CallbackCookie" / Int32ul,
        "FunctionId" / Int32ul,
        "TimeoutValue" / Int32ul,
        "ScriptContextId" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=531, version=2)
class Microsoft_IE_531_2(Etw):
    pattern = Struct(
        "TimerType" / Int32ul,
        "CallbackCookie" / Int32ul,
        "FunctionId" / Int32ul,
        "TimeoutValue" / Int32ul,
        "ScriptContextId" / Int64ul,
        "EventContextId" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=532, version=0)
class Microsoft_IE_532_0(Etw):
    pattern = Struct(
        "ACount" / Int16ul,
        "objectInstance" / Int64ul,
        "property" / Int64ul,
        "StringValue" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=533, version=0)
class Microsoft_IE_533_0(Etw):
    pattern = Struct(
        "ACount" / Int16ul,
        "A" / Bytes(lambda this: this.ACount)
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=534, version=0)
class Microsoft_IE_534_0(Etw):
    pattern = Struct(
        "ACount" / Int16ul,
        "A" / Bytes(lambda this: this.ACount)
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=535, version=0)
class Microsoft_IE_535_0(Etw):
    pattern = Struct(
        "ACount" / Int16ul,
        "A" / Bytes(lambda this: this.ACount)
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=536, version=0)
class Microsoft_IE_536_0(Etw):
    pattern = Struct(
        "left" / Int32sl,
        "top" / Int32sl,
        "right" / Int32sl,
        "bottom" / Int32sl,
        "TouchTarget" / Int64ul,
        "Scenario" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=537, version=0)
class Microsoft_IE_537_0(Etw):
    pattern = Struct(
        "_fBusy" / Int8ul,
        "fBusy" / Int8ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=538, version=0)
class Microsoft_IE_538_0(Etw):
    pattern = Struct(
        "DispNode" / Int64ul,
        "NodeDescription" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=539, version=0)
class Microsoft_IE_539_0(Etw):
    pattern = Struct(
        "Current_URL" / WString,
        "Prefetch_or_Prerender_URL" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=540, version=0)
class Microsoft_IE_540_0(Etw):
    pattern = Struct(
        "Current_URL" / WString,
        "Prefetch_or_Prerender_URL" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=541, version=0)
class Microsoft_IE_541_0(Etw):
    pattern = Struct(
        "Current_URL" / WString,
        "Prefetch_or_Prerender_URL" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=542, version=0)
class Microsoft_IE_542_0(Etw):
    pattern = Struct(
        "Prefetch_or_Prerender_URL" / WString,
        "Termination_Reason" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=543, version=0)
class Microsoft_IE_543_0(Etw):
    pattern = Struct(
        "Current_URL" / WString,
        "Prefetch_or_Prerender_URL" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=544, version=0)
class Microsoft_IE_544_0(Etw):
    pattern = Struct(
        "Current_URL" / WString,
        "Prefetch_or_Prerender_URL" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=545, version=0)
class Microsoft_IE_545_0(Etw):
    pattern = Struct(
        "Current_URL" / WString,
        "Prefetch_or_Prerender_URL" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=546, version=0)
class Microsoft_IE_546_0(Etw):
    pattern = Struct(
        "Prefetch_or_Prerender_URL" / WString,
        "Termination_Reason" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=547, version=0)
class Microsoft_IE_547_0(Etw):
    pattern = Struct(
        "Current_URL" / WString,
        "Prefetch_or_Prerender_URL" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=548, version=0)
class Microsoft_IE_548_0(Etw):
    pattern = Struct(
        "Current_URL" / WString,
        "Prefetch_or_Prerender_URL" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=550, version=0)
class Microsoft_IE_550_0(Etw):
    pattern = Struct(
        "ContentTypes" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=551, version=0)
class Microsoft_IE_551_0(Etw):
    pattern = Struct(
        "Prerender_URL" / WString,
        "Deferred_Item" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=552, version=0)
class Microsoft_IE_552_0(Etw):
    pattern = Struct(
        "Prerender_URL" / WString,
        "Deferred_Item" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=553, version=0)
class Microsoft_IE_553_0(Etw):
    pattern = Struct(
        "WPGeneralTracingStr" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=555, version=0)
class Microsoft_IE_555_0(Etw):
    pattern = Struct(
        "RenderTask" / Int64ul,
        "QueueDepth" / Int32ul,
        "OnUIThread" / Int8ul,
        "Async" / Int8ul,
        "Description" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=556, version=0)
class Microsoft_IE_556_0(Etw):
    pattern = Struct(
        "RenderTask" / Int64ul,
        "Skipped" / Int8ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=557, version=0)
class Microsoft_IE_557_0(Etw):
    pattern = Struct(
        "RenderTask" / Int64ul,
        "Skipped" / Int8ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=558, version=0)
class Microsoft_IE_558_0(Etw):
    pattern = Struct(
        "RenderThread" / Int64ul,
        "State" / Int32ul,
        "ExtraInfo" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=562, version=0)
class Microsoft_IE_562_0(Etw):
    pattern = Struct(
        "EntityType" / Int32ul,
        "StartIndex" / Int32ul,
        "EndIndex" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=571, version=0)
class Microsoft_IE_571_0(Etw):
    pattern = Struct(
        "URL" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=572, version=0)
class Microsoft_IE_572_0(Etw):
    pattern = Struct(
        "URL" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=573, version=0)
class Microsoft_IE_573_0(Etw):
    pattern = Struct(
        "URL" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=574, version=0)
class Microsoft_IE_574_0(Etw):
    pattern = Struct(
        "FailureFlags" / Int32ul,
        "URL" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=575, version=0)
class Microsoft_IE_575_0(Etw):
    pattern = Struct(
        "XHR" / Int64ul,
        "Method" / WString,
        "Url" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=576, version=0)
class Microsoft_IE_576_0(Etw):
    pattern = Struct(
        "XHR" / Int64ul,
        "OperationID" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=579, version=0)
class Microsoft_IE_579_0(Etw):
    pattern = Struct(
        "MediaQuery" / WString,
        "FunctionId" / Int32ul,
        "ScriptContextId" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=579, version=1)
class Microsoft_IE_579_1(Etw):
    pattern = Struct(
        "MediaQuery" / WString,
        "FunctionId" / Int32ul,
        "ScriptContextId" / Int64ul,
        "EventContextId" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=580, version=0)
class Microsoft_IE_580_0(Etw):
    pattern = Struct(
        "MediaQuery" / WString,
        "FunctionId" / Int32ul,
        "ScriptContextId" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=580, version=1)
class Microsoft_IE_580_1(Etw):
    pattern = Struct(
        "MediaQuery" / WString,
        "FunctionId" / Int32ul,
        "ScriptContextId" / Int64ul,
        "EventContextId" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=581, version=0)
class Microsoft_IE_581_0(Etw):
    pattern = Struct(
        "Parser" / Int64ul,
        "Stream" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=582, version=0)
class Microsoft_IE_582_0(Etw):
    pattern = Struct(
        "Parser" / Int64ul,
        "Stream" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=583, version=0)
class Microsoft_IE_583_0(Etw):
    pattern = Struct(
        "Parser" / Int64ul,
        "Stream" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=584, version=0)
class Microsoft_IE_584_0(Etw):
    pattern = Struct(
        "Parser" / Int64ul,
        "Stream" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=585, version=0)
class Microsoft_IE_585_0(Etw):
    pattern = Struct(
        "Parser" / Int64ul,
        "Stream" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=586, version=0)
class Microsoft_IE_586_0(Etw):
    pattern = Struct(
        "Parser" / Int64ul,
        "Stream" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=587, version=0)
class Microsoft_IE_587_0(Etw):
    pattern = Struct(
        "Parser" / Int64ul,
        "Stream" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=588, version=0)
class Microsoft_IE_588_0(Etw):
    pattern = Struct(
        "Parser" / Int64ul,
        "Stream" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=589, version=0)
class Microsoft_IE_589_0(Etw):
    pattern = Struct(
        "Parser" / Int64ul,
        "Stream" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=590, version=0)
class Microsoft_IE_590_0(Etw):
    pattern = Struct(
        "Parser" / Int64ul,
        "Stream" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=591, version=0)
class Microsoft_IE_591_0(Etw):
    pattern = Struct(
        "Parser" / Int64ul,
        "Stream" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=592, version=0)
class Microsoft_IE_592_0(Etw):
    pattern = Struct(
        "Parser" / Int64ul,
        "Stream" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=593, version=0)
class Microsoft_IE_593_0(Etw):
    pattern = Struct(
        "Parser" / Int64ul,
        "Stream" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=594, version=0)
class Microsoft_IE_594_0(Etw):
    pattern = Struct(
        "Parser" / Int64ul,
        "Stream" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=609, version=0)
class Microsoft_IE_609_0(Etw):
    pattern = Struct(
        "CDoc" / Int64ul,
        "CMarkup" / Int64ul,
        "URL" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=609, version=1)
class Microsoft_IE_609_1(Etw):
    pattern = Struct(
        "CDoc" / Int64ul,
        "CMarkup" / Int64ul,
        "URL" / WString,
        "EventContextId" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=610, version=0)
class Microsoft_IE_610_0(Etw):
    pattern = Struct(
        "Manager" / Int64ul,
        "ID" / Int32ul,
        "WorkerObject" / Int64ul,
        "WorkerScope" / Int64ul,
        "URL" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=611, version=0)
class Microsoft_IE_611_0(Etw):
    pattern = Struct(
        "Manager" / Int64ul,
        "ID" / Int32ul,
        "WorkerObject" / Int64ul,
        "WorkerScope" / Int64ul,
        "URL" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=612, version=0)
class Microsoft_IE_612_0(Etw):
    pattern = Struct(
        "Manager" / Int64ul,
        "ID" / Int32ul,
        "WorkerObject" / Int64ul,
        "WorkerScope" / Int64ul,
        "URL" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=613, version=0)
class Microsoft_IE_613_0(Etw):
    pattern = Struct(
        "MessagePort" / Int64ul,
        "Owner" / Int64ul,
        "OwnerType" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=614, version=0)
class Microsoft_IE_614_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=615, version=0)
class Microsoft_IE_615_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=616, version=0)
class Microsoft_IE_616_0(Etw):
    pattern = Struct(
        "RenderTask" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=617, version=0)
class Microsoft_IE_617_0(Etw):
    pattern = Struct(
        "RenderTask" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=618, version=0)
class Microsoft_IE_618_0(Etw):
    pattern = Struct(
        "IsDocVisible" / Int8ul,
        "NotifyFrame" / Int8ul,
        "HR" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=619, version=0)
class Microsoft_IE_619_0(Etw):
    pattern = Struct(
        "IsDocVisible" / Int8ul,
        "NotifyFrame" / Int8ul,
        "HR" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=620, version=0)
class Microsoft_IE_620_0(Etw):
    pattern = Struct(
        "SuspendLevel" / Int32ul,
        "HR" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=621, version=0)
class Microsoft_IE_621_0(Etw):
    pattern = Struct(
        "SuspendLevel" / Int32ul,
        "HR" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=622, version=0)
class Microsoft_IE_622_0(Etw):
    pattern = Struct(
        "Visible" / Int8ul,
        "IsDocInvisible" / Int8ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=623, version=0)
class Microsoft_IE_623_0(Etw):
    pattern = Struct(
        "Visible" / Int8ul,
        "IsDocInvisible" / Int8ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=624, version=0)
class Microsoft_IE_624_0(Etw):
    pattern = Struct(
        "ElementDDTId" / Int64ul,
        "StyleProperty" / WString,
        "NewValue" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=637, version=0)
class Microsoft_IE_637_0(Etw):
    pattern = Struct(
        "CGarbageTracker" / Int64ul,
        "ResourceType" / Int32ul,
        "Reason" / Int32ul,
        "RequestedGCType" / Int32ul,
        "GCType" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=640, version=0)
class Microsoft_IE_640_0(Etw):
    pattern = Struct(
        "CDoc" / Int64ul,
        "PrimaryCMarkup" / Int64ul,
        "SourceContext" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=641, version=0)
class Microsoft_IE_641_0(Etw):
    pattern = Struct(
        "CDoc" / Int64ul,
        "PrimaryCMarkup" / Int64ul,
        "SourceContext" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=642, version=0)
class Microsoft_IE_642_0(Etw):
    pattern = Struct(
        "CDoc" / Int64ul,
        "PrimaryCMarkup" / Int64ul,
        "SourceContext" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=643, version=0)
class Microsoft_IE_643_0(Etw):
    pattern = Struct(
        "FunctionId" / Int32ul,
        "ScriptContextId" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=643, version=1)
class Microsoft_IE_643_1(Etw):
    pattern = Struct(
        "FunctionId" / Int32ul,
        "ScriptContextId" / Int64ul,
        "EventContextId" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=644, version=1)
class Microsoft_IE_644_1(Etw):
    pattern = Struct(
        "EventContextId" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=645, version=0)
class Microsoft_IE_645_0(Etw):
    pattern = Struct(
        "TargetElementDdtId" / Int64ul,
        "Type" / Int16ul,
        "ChangedAttributeName" / WString,
        "AddedChildCount" / Int32ul,
        "RemovedChildCount" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=645, version=1)
class Microsoft_IE_645_1(Etw):
    pattern = Struct(
        "TargetElementDdtId" / Int64ul,
        "Type" / Int16ul,
        "ChangedAttributeName" / WString,
        "AddedChildCount" / Int32ul,
        "RemovedChildCount" / Int32ul,
        "EventContextId" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=646, version=0)
class Microsoft_IE_646_0(Etw):
    pattern = Struct(
        "HrErrorDescription" / CString,
        "ThisPtr" / Int64ul,
        "HR" / Int32sl
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=647, version=0)
class Microsoft_IE_647_0(Etw):
    pattern = Struct(
        "WinErrorDescription" / CString,
        "ThisPtr" / Int64ul,
        "WinError" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=648, version=0)
class Microsoft_IE_648_0(Etw):
    pattern = Struct(
        "ErrorDescription" / CString,
        "ThisPtr" / Int64ul,
        "HR" / Int32sl
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=649, version=0)
class Microsoft_IE_649_0(Etw):
    pattern = Struct(
        "InfoDescription" / CString,
        "ThisPtr" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=650, version=0)
class Microsoft_IE_650_0(Etw):
    pattern = Struct(
        "InfoDescription" / CString,
        "StringParam" / WString,
        "ThisPtr" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=651, version=0)
class Microsoft_IE_651_0(Etw):
    pattern = Struct(
        "WarningDescription" / CString,
        "StringParam" / WString,
        "ThisPtr" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=652, version=0)
class Microsoft_IE_652_0(Etw):
    pattern = Struct(
        "WarningDescription" / CString,
        "DwordParam" / Int32ul,
        "ThisPtr" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=653, version=0)
class Microsoft_IE_653_0(Etw):
    pattern = Struct(
        "InfoDescription" / CString,
        "ThisPtr" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=654, version=0)
class Microsoft_IE_654_0(Etw):
    pattern = Struct(
        "ErrorDescription" / CString,
        "ThisPtr" / Int64ul,
        "HR" / Int32sl
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=655, version=0)
class Microsoft_IE_655_0(Etw):
    pattern = Struct(
        "Width" / Int32ul,
        "Height" / Int32ul,
        "PresenterWidth" / Int32ul,
        "PresenterHeight" / Int32ul,
        "ScaleFactor" / Float32l,
        "DisableDComp" / Int32ul,
        "DCompState" / Int32ul,
        "ThisPtr" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=656, version=0)
class Microsoft_IE_656_0(Etw):
    pattern = Struct(
        "Width" / Int32ul,
        "Height" / Int32ul,
        "PresenterWidth" / Int32ul,
        "PresenterHeight" / Int32ul,
        "ScaleFactor" / Float32l,
        "DisableDComp" / Int32ul,
        "DCompState" / Int32ul,
        "ThisPtr" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=657, version=0)
class Microsoft_IE_657_0(Etw):
    pattern = Struct(
        "CDoc" / Int64ul,
        "BaseOpticalZoom" / Float32l,
        "BaseOpticalZoomDefault" / Float32l,
        "HostDpiAware" / Int8ul,
        "StaticViewportSizeApplied" / Int8ul,
        "AtViewportHasDeviceWidthOrHeight" / Int8ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=658, version=0)
class Microsoft_IE_658_0(Etw):
    pattern = Struct(
        "CView" / Int64ul,
        "VisualViewportWidth" / Int32sl,
        "VisualViewportHeight" / Int32sl,
        "LayoutViewportWidth" / Int32sl,
        "LayoutViewportHeight" / Int32sl,
        "BaseOpticalZoom" / Float32l,
        "IsClamping" / Int8ul,
        "HasAtViewportRule" / Int8ul,
        "HasDeviceWidthOrHeight" / Int8ul,
        "ViewportControllerEnabled" / Int8ul,
        "HasHorizontalScrollbar" / Int8ul,
        "HasVerticalScrollbar" / Int8ul,
        "UpdateUnitInfoZoomOnly" / Int8ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=659, version=0)
class Microsoft_IE_659_0(Etw):
    pattern = Struct(
        "CView" / Int64ul,
        "FixedLayoutWidthOld" / Float32l,
        "FixedLayoutWidthNew" / Float32l
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=660, version=0)
class Microsoft_IE_660_0(Etw):
    pattern = Struct(
        "CView" / Int64ul,
        "IsEnabled" / Int8ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=661, version=0)
class Microsoft_IE_661_0(Etw):
    pattern = Struct(
        "CView" / Int64ul,
        "IsEnabled" / Int8ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=662, version=0)
class Microsoft_IE_662_0(Etw):
    pattern = Struct(
        "PreviousStatus" / Int32ul,
        "CurrentStatus" / Int32ul,
        "TouchTargetPtr" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=663, version=0)
class Microsoft_IE_663_0(Etw):
    pattern = Struct(
        "ManualGestureConfiguration" / Int32ul,
        "PointerID" / Int16ul,
        "IsIHTThread" / Int8ul,
        "CDMScrollableTouchTarget" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=664, version=0)
class Microsoft_IE_664_0(Etw):
    pattern = Struct(
        "IsIHTThread" / Int8ul,
        "mat_11" / Float32l,
        "mat_12" / Float32l,
        "mat_21" / Float32l,
        "mat_22" / Float32l,
        "mat_31" / Float32l,
        "mat_32" / Float32l,
        "CDMTouchTarget" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=665, version=0)
class Microsoft_IE_665_0(Etw):
    pattern = Struct(
        "IsIHTThread" / Int8ul,
        "mat_11" / Float32l,
        "mat_12" / Float32l,
        "mat_21" / Float32l,
        "mat_22" / Float32l,
        "mat_31" / Float32l,
        "mat_32" / Float32l,
        "CDMTouchTarget" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=666, version=0)
class Microsoft_IE_666_0(Etw):
    pattern = Struct(
        "HwndWorker" / Int64ul,
        "PointerID" / Int16ul,
        "ClientX" / Int32ul,
        "ClientY" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=667, version=0)
class Microsoft_IE_667_0(Etw):
    pattern = Struct(
        "ViewportOffsetWidth" / Float32l,
        "ViewportOffsetHeight" / Float32l,
        "LayoutViewportOffsetWidth" / Float32l,
        "LayoutViewportOffsetHeight" / Float32l,
        "ZoomLevel" / Float32l,
        "CDMScrollableTouchTargetHandler" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=668, version=0)
class Microsoft_IE_668_0(Etw):
    pattern = Struct(
        "ViewportOffsetWidth" / Float32l,
        "ViewportOffsetHeight" / Float32l,
        "ZoomLevel" / Float32l,
        "CDMScrollableTouchTargetHandler" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=669, version=0)
class Microsoft_IE_669_0(Etw):
    pattern = Struct(
        "MsgID" / Int32ul,
        "CDMScrollableTouchTargetHandler" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=670, version=0)
class Microsoft_IE_670_0(Etw):
    pattern = Struct(
        "FromStatus" / Int32ul,
        "ToStatus" / Int32ul,
        "CDMTouchTargetHandler" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=671, version=0)
class Microsoft_IE_671_0(Etw):
    pattern = Struct(
        "GenericInfo" / Int32ul,
        "ThisPtr" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=672, version=0)
class Microsoft_IE_672_0(Etw):
    pattern = Struct(
        "IDispLayer" / Int64ul,
        "CDMCrossSlideDraggableTouchTarget" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=673, version=0)
class Microsoft_IE_673_0(Etw):
    pattern = Struct(
        "IDispLayer" / Int64ul,
        "fIsDraggingRequested" / Int8ul,
        "CDMCrossSlideDraggableTouchTarget" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=674, version=0)
class Microsoft_IE_674_0(Etw):
    pattern = Struct(
        "IDispLayer" / Int64ul,
        "CDMCrossSlideDraggableTouchTarget" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=675, version=0)
class Microsoft_IE_675_0(Etw):
    pattern = Struct(
        "IDispLayer" / Int64ul,
        "CDMCrossSlideDraggableTouchTarget" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=676, version=0)
class Microsoft_IE_676_0(Etw):
    pattern = Struct(
        "ViewportOffsetWidth" / Float32l,
        "ViewportOffsetHeight" / Float32l,
        "ZoomLevel" / Float32l,
        "CDMCrossSlideDraggableTouchTargetHandler" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=677, version=0)
class Microsoft_IE_677_0(Etw):
    pattern = Struct(
        "DManipInteractionType" / Int32ul,
        "CDMHoldDraggableTouchTarget" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=678, version=0)
class Microsoft_IE_678_0(Etw):
    pattern = Struct(
        "DManipDragDropConfiguration" / Int32ul,
        "CDMDraggableTouchTarget" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=679, version=0)
class Microsoft_IE_679_0(Etw):
    pattern = Struct(
        "PreviousStatus" / Int32ul,
        "CurrentStatus" / Int32ul,
        "CDMDraggableTouchTarget" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=680, version=0)
class Microsoft_IE_680_0(Etw):
    pattern = Struct(
        "PointerID" / Int16ul,
        "IsIHTThread" / Int8ul,
        "CDMDraggableTouchTarget" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=681, version=0)
class Microsoft_IE_681_0(Etw):
    pattern = Struct(
        "fIsDraggingRequested" / Int8ul,
        "fIsPreviewCurrentlyDisplayed" / Int8ul,
        "CDMDraggableTouchTarget" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=682, version=0)
class Microsoft_IE_682_0(Etw):
    pattern = Struct(
        "rcWidth" / Int32sl,
        "rcHeight" / Int32sl,
        "CDMDraggableTouchTarget" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=683, version=0)
class Microsoft_IE_683_0(Etw):
    pattern = Struct(
        "PreviousStatus" / Int32ul,
        "CurrentStatus" / Int32ul,
        "TouchTargetPtr" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=684, version=0)
class Microsoft_IE_684_0(Etw):
    pattern = Struct(
        "fTouchStarting" / Int8ul,
        "CDMDraggableTouchTarget" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=685, version=0)
class Microsoft_IE_685_0(Etw):
    pattern = Struct(
        "CElement" / Int64ul,
        "CDMDraggableTouchTargetHandler" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=686, version=0)
class Microsoft_IE_686_0(Etw):
    pattern = Struct(
        "SharedMemoryHandle" / Int32ul,
        "TotalBufferSizeInBytes" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=687, version=0)
class Microsoft_IE_687_0(Etw):
    pattern = Struct(
        "FailureHresult" / Int32ul,
        "TotalBufferSizeInBytes" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=688, version=0)
class Microsoft_IE_688_0(Etw):
    pattern = Struct(
        "SharedMemoryHandle" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=689, version=0)
class Microsoft_IE_689_0(Etw):
    pattern = Struct(
        "SharedMemoryHandle" / Int32ul,
        "FailureHresult" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=690, version=0)
class Microsoft_IE_690_0(Etw):
    pattern = Struct(
        "FailureReason" / Int32ul,
        "FailureHresult" / Int32ul,
        "TargetURL" / WString,
        "EmulationMode" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=694, version=0)
class Microsoft_IE_694_0(Etw):
    pattern = Struct(
        "pNodeFirstTap" / Int64ul,
        "pointX" / Int32sl,
        "pointY" / Int32sl
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=695, version=0)
class Microsoft_IE_695_0(Etw):
    pattern = Struct(
        "Reason" / Int32ul,
        "DesiredOffsetX" / Float32l,
        "DesiredOffsetY" / Float32l,
        "DesiredZoomFactor" / Float32l
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=696, version=0)
class Microsoft_IE_696_0(Etw):
    pattern = Struct(
        "pNodeHit" / Int64ul,
        "fAllowed" / Int8ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=697, version=0)
class Microsoft_IE_697_0(Etw):
    pattern = Struct(
        "fPotentialDoubleTap" / Int8ul,
        "fDoubleTapTimerPending" / Int8ul,
        "pMessageTime" / Int32ul,
        "MaxTimeForSecondTap" / Int64ul,
        "FirstTapPointX" / Int32sl,
        "FirstTapPointY" / Int32sl,
        "SecondTapPointX" / Int32sl,
        "SecondTapPointY" / Int32sl,
        "fIsDoubleClick" / Int8ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=698, version=0)
class Microsoft_IE_698_0(Etw):
    pattern = Struct(
        "AnimationClientObject" / Int64ul,
        "AnimationInstanceObject" / Int64ul,
        "DISPID" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=699, version=0)
class Microsoft_IE_699_0(Etw):
    pattern = Struct(
        "DispNode" / Int64ul,
        "IndAnimationInstanceObject" / Int64ul,
        "DISPID" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=700, version=0)
class Microsoft_IE_700_0(Etw):
    pattern = Struct(
        "Msg" / Int32ul,
        "TimeStamp" / Int64ul,
        "PointerId" / Int32ul,
        "FrameId" / Int32ul,
        "PointerType" / Int32ul,
        "ScreenX" / Int32ul,
        "ScreenY" / Int32ul,
        "ClientX" / Int32ul,
        "ClientY" / Int32ul,
        "ButtonChanged" / Int32ul,
        "ButtonState" / Int32ul,
        "PointerFlags" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=701, version=0)
class Microsoft_IE_701_0(Etw):
    pattern = Struct(
        "Element" / Int64ul,
        "DropEffect" / Int32sl,
        "ScreenLocationX" / Int32sl,
        "ScreenLocationY" / Int32sl
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=702, version=0)
class Microsoft_IE_702_0(Etw):
    pattern = Struct(
        "Element" / Int64ul,
        "DropEffect" / Int32sl,
        "ScreenLocationX" / Int32sl,
        "ScreenLocationY" / Int32sl
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=703, version=0)
class Microsoft_IE_703_0(Etw):
    pattern = Struct(
        "Element" / Int64ul,
        "DropEffect" / Int32sl,
        "ScreenLocationX" / Int32sl,
        "ScreenLocationY" / Int32sl
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=704, version=0)
class Microsoft_IE_704_0(Etw):
    pattern = Struct(
        "Element" / Int64ul,
        "DropEffect" / Int32sl,
        "ScreenLocationX" / Int32sl,
        "ScreenLocationY" / Int32sl
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=705, version=0)
class Microsoft_IE_705_0(Etw):
    pattern = Struct(
        "Element" / Int64ul,
        "DropEffect" / Int32sl,
        "ScreenLocationX" / Int32sl,
        "ScreenLocationY" / Int32sl
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=706, version=0)
class Microsoft_IE_706_0(Etw):
    pattern = Struct(
        "Element" / Int64ul,
        "DropEffect" / Int32sl,
        "ScreenLocationX" / Int32sl,
        "ScreenLocationY" / Int32sl
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=707, version=0)
class Microsoft_IE_707_0(Etw):
    pattern = Struct(
        "Element" / Int64ul,
        "DropEffect" / Int32sl,
        "ScreenLocationX" / Int32sl,
        "ScreenLocationY" / Int32sl
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=708, version=0)
class Microsoft_IE_708_0(Etw):
    pattern = Struct(
        "Element" / Int64ul,
        "PreviousState" / Int32ul,
        "CurrentState" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=709, version=0)
class Microsoft_IE_709_0(Etw):
    pattern = Struct(
        "Element" / Int64ul,
        "PreviousState" / Int32ul,
        "CurrentState" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=710, version=0)
class Microsoft_IE_710_0(Etw):
    pattern = Struct(
        "DragPreview" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=711, version=0)
class Microsoft_IE_711_0(Etw):
    pattern = Struct(
        "DragPreview" / Int64ul,
        "FailureHresult" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=712, version=0)
class Microsoft_IE_712_0(Etw):
    pattern = Struct(
        "DragPreview" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=713, version=0)
class Microsoft_IE_713_0(Etw):
    pattern = Struct(
        "DragPreview" / Int64ul,
        "FailureHresult" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=714, version=0)
class Microsoft_IE_714_0(Etw):
    pattern = Struct(
        "DragPreview" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=715, version=0)
class Microsoft_IE_715_0(Etw):
    pattern = Struct(
        "DragPreview" / Int64ul,
        "FailureHresult" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=716, version=0)
class Microsoft_IE_716_0(Etw):
    pattern = Struct(
        "DragPreview" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=717, version=0)
class Microsoft_IE_717_0(Etw):
    pattern = Struct(
        "DragPreview" / Int64ul,
        "FailureHresult" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=718, version=0)
class Microsoft_IE_718_0(Etw):
    pattern = Struct(
        "TouchDragDropHelper" / Int64ul,
        "Element" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=719, version=0)
class Microsoft_IE_719_0(Etw):
    pattern = Struct(
        "TouchDragDropHelper" / Int64ul,
        "Element" / Int64ul,
        "FailureHresult" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=720, version=0)
class Microsoft_IE_720_0(Etw):
    pattern = Struct(
        "TouchDragDropHelper" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=721, version=0)
class Microsoft_IE_721_0(Etw):
    pattern = Struct(
        "TouchDragDropHelper" / Int64ul,
        "FailureHresult" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=722, version=0)
class Microsoft_IE_722_0(Etw):
    pattern = Struct(
        "TouchDragDropHelper" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=723, version=0)
class Microsoft_IE_723_0(Etw):
    pattern = Struct(
        "TouchDragDropHelper" / Int64ul,
        "FailureHresult" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=724, version=0)
class Microsoft_IE_724_0(Etw):
    pattern = Struct(
        "TouchDragDropHelper" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=725, version=0)
class Microsoft_IE_725_0(Etw):
    pattern = Struct(
        "TouchDragDropHelper" / Int64ul,
        "FailureHresult" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=726, version=0)
class Microsoft_IE_726_0(Etw):
    pattern = Struct(
        "TouchDragDropHelper" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=727, version=0)
class Microsoft_IE_727_0(Etw):
    pattern = Struct(
        "TouchDragDropHelper" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=728, version=0)
class Microsoft_IE_728_0(Etw):
    pattern = Struct(
        "FlipAhead_Target_URL" / WString,
        "Target_Source_Method" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=730, version=0)
class Microsoft_IE_730_0(Etw):
    pattern = Struct(
        "CMarkup" / Int64ul,
        "Canceled" / Int8ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=731, version=0)
class Microsoft_IE_731_0(Etw):
    pattern = Struct(
        "CMarkup" / Int64ul,
        "RefreshLevel" / Int32ul,
        "Canceled" / Int8ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=732, version=0)
class Microsoft_IE_732_0(Etw):
    pattern = Struct(
        "CMarkup" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=733, version=0)
class Microsoft_IE_733_0(Etw):
    pattern = Struct(
        "CMarkup" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=734, version=0)
class Microsoft_IE_734_0(Etw):
    pattern = Struct(
        "CMarkup" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=735, version=0)
class Microsoft_IE_735_0(Etw):
    pattern = Struct(
        "CMarkup" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=736, version=0)
class Microsoft_IE_736_0(Etw):
    pattern = Struct(
        "CMarkup" / Int64ul,
        "hrReason" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=737, version=0)
class Microsoft_IE_737_0(Etw):
    pattern = Struct(
        "CMarkup" / Int64ul,
        "RedirectURL" / WString,
        "StatusCode" / Int32ul,
        "Canceled" / Int8ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=738, version=0)
class Microsoft_IE_738_0(Etw):
    pattern = Struct(
        "CMarkup" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=739, version=0)
class Microsoft_IE_739_0(Etw):
    pattern = Struct(
        "CMarkup" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=740, version=0)
class Microsoft_IE_740_0(Etw):
    pattern = Struct(
        "CMemoryProtector" / Int64ul,
        "StackSize" / Int64ul,
        "Blocks" / Int64ul,
        "Bytes" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=741, version=0)
class Microsoft_IE_741_0(Etw):
    pattern = Struct(
        "CMemoryProtector" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=742, version=0)
class Microsoft_IE_742_0(Etw):
    pattern = Struct(
        "CMemoryProtector" / Int64ul,
        "StackSize" / Int64ul,
        "Blocks" / Int64ul,
        "Bytes" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=743, version=0)
class Microsoft_IE_743_0(Etw):
    pattern = Struct(
        "CMemoryProtector" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=744, version=0)
class Microsoft_IE_744_0(Etw):
    pattern = Struct(
        "CMemoryProtector" / Int64ul,
        "Blocks" / Int64ul,
        "Bytes" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=745, version=0)
class Microsoft_IE_745_0(Etw):
    pattern = Struct(
        "CMemoryProtector" / Int64ul,
        "MarkedBlocks" / Int64ul,
        "MarkedBytes" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=746, version=0)
class Microsoft_IE_746_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul,
        "Left" / Int32ul,
        "Right" / Int32ul,
        "Top" / Int32ul,
        "Bottom" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=747, version=0)
class Microsoft_IE_747_0(Etw):
    pattern = Struct(
        "CContentSecurityPolicy" / Int64ul,
        "PolicyType" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=748, version=0)
class Microsoft_IE_748_0(Etw):
    pattern = Struct(
        "CContentSecurityPolicy" / Int64ul,
        "PolicyType" / Int32ul,
        "Added" / Int8ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=749, version=0)
class Microsoft_IE_749_0(Etw):
    pattern = Struct(
        "CContentSecurityPolicy" / Int64ul,
        "ResourceDirectiveType" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=750, version=0)
class Microsoft_IE_750_0(Etw):
    pattern = Struct(
        "CContentSecurityPolicy" / Int64ul,
        "ResourceDirectiveType" / Int32ul,
        "Allowed" / Int8ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=751, version=0)
class Microsoft_IE_751_0(Etw):
    pattern = Struct(
        "URL" / WString,
        "PermissionType" / Int32ul,
        "PermissionState" / Int32ul,
        "IsPrimaryResponse" / Int8ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=752, version=0)
class Microsoft_IE_752_0(Etw):
    pattern = Struct(
        "DownloadedURL" / WString,
        "BindInfo" / Int64ul,
        "CHtmPre" / Int64ul,
        "CPre" / Int64ul,
        "CDoc" / Int64ul,
        "CWindow" / Int64ul,
        "WindowURL" / WString,
        "URL" / WString,
        "Line" / Int32ul,
        "Offset" / Int32ul,
        "Speculative" / Int8ul,
        "LookAhead" / Int8ul,
        "PreParserRestarted" / Int8ul,
        "Context" / Int32ul,
        "Initiator" / Int32ul,
        "Source" / Int32ul,
        "LookAheadCount" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=753, version=0)
class Microsoft_IE_753_0(Etw):
    pattern = Struct(
        "PID" / Int32ul,
        "TID" / Int32ul,
        "SourceUrl" / WString,
        "TargetUrl" / WString,
        "Func" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=754, version=0)
class Microsoft_IE_754_0(Etw):
    pattern = Struct(
        "ThisPtr" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=755, version=0)
class Microsoft_IE_755_0(Etw):
    pattern = Struct(
        "ThisPtr" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=756, version=0)
class Microsoft_IE_756_0(Etw):
    pattern = Struct(
        "HR" / Int32sl,
        "ThisPtr" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=757, version=0)
class Microsoft_IE_757_0(Etw):
    pattern = Struct(
        "ICEState" / WString,
        "ThisPtr" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=758, version=0)
class Microsoft_IE_758_0(Etw):
    pattern = Struct(
        "DTLSState" / WString,
        "ThisPtr" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=759, version=0)
class Microsoft_IE_759_0(Etw):
    pattern = Struct(
        "SampleQueueType" / CString,
        "ThisPtr" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=760, version=0)
class Microsoft_IE_760_0(Etw):
    pattern = Struct(
        "DroppedSampleCount" / Int64ul,
        "ThisPtr" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=761, version=0)
class Microsoft_IE_761_0(Etw):
    pattern = Struct(
        "SampleCount" / Int64ul,
        "CurrentTimeMSec" / Int64ul,
        "ThisPtr" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=762, version=0)
class Microsoft_IE_762_0(Etw):
    pattern = Struct(
        "SampleCount" / Int64ul,
        "CurrentTimeMSec" / Int64ul,
        "ThisPtr" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=763, version=0)
class Microsoft_IE_763_0(Etw):
    pattern = Struct(
        "SampleCount" / Int64ul,
        "CurrentTimeMSec" / Int64ul,
        "ThisPtr" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=764, version=0)
class Microsoft_IE_764_0(Etw):
    pattern = Struct(
        "SampleCount" / Int64ul,
        "CurrentTimeMSec" / Int64ul,
        "ThisPtr" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=765, version=0)
class Microsoft_IE_765_0(Etw):
    pattern = Struct(
        "SampleCount" / Int64ul,
        "CurrentTimeMSec" / Int64ul,
        "ThisPtr" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=766, version=0)
class Microsoft_IE_766_0(Etw):
    pattern = Struct(
        "SampleCount" / Int64ul,
        "CurrentTimeMSec" / Int64ul,
        "ThisPtr" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=767, version=0)
class Microsoft_IE_767_0(Etw):
    pattern = Struct(
        "SelectorType" / Int32ul,
        "Selector" / WString,
        "TargetType" / Int32ul,
        "Target" / Int64ul,
        "IsQueryAll" / Int8ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=768, version=0)
class Microsoft_IE_768_0(Etw):
    pattern = Struct(
        "Type" / Int32ul,
        "Budget" / Int32ul,
        "Current" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=769, version=0)
class Microsoft_IE_769_0(Etw):
    pattern = Struct(
        "Type" / Int32ul,
        "Budget" / Int32ul,
        "Current" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=770, version=0)
class Microsoft_IE_770_0(Etw):
    pattern = Struct(
        "Width" / Int32ul,
        "Height" / Int32ul,
        "VideoElement" / Int64ul,
        "RemoteMediaStreamTrack" / Int64ul,
        "ThisPtr" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=771, version=0)
class Microsoft_IE_771_0(Etw):
    pattern = Struct(
        "DriftedTimeMSec" / Int64ul,
        "LastSampleEndTimeMSec" / Int64ul,
        "CurrentPresentationClockTimeMSec" / Int64ul,
        "AudioDriftDroppedSampleCount" / Int64ul,
        "ThisPtr" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=772, version=0)
class Microsoft_IE_772_0(Etw):
    pattern = Struct(
        "LastSampleEndTimeMSec" / Int64ul,
        "CurrentPresentationClockTimeMSec" / Int64ul,
        "AudioDriftDroppedSampleCount" / Int64ul,
        "ThisPtr" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=773, version=0)
class Microsoft_IE_773_0(Etw):
    pattern = Struct(
        "SampleRequstedCount" / Int64ul,
        "SampleDeliveredCount" / Int64ul,
        "SampleReceivedCount" / Int64ul,
        "SampleDroppedCount" / Int64ul,
        "TrackKind" / Int32ul,
        "ThisPtr" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=774, version=0)
class Microsoft_IE_774_0(Etw):
    pattern = Struct(
        "SampleRequstedCount" / Int64ul,
        "SampleDeliveredCount" / Int64ul,
        "SampleReceivedCount" / Int64ul,
        "SampleDroppedCount" / Int64ul,
        "TrackKind" / Int32ul,
        "ThisPtr" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=775, version=0)
class Microsoft_IE_775_0(Etw):
    pattern = Struct(
        "SampleRequstedCount" / Int64ul,
        "SampleDeliveredCount" / Int64ul,
        "SampleReceivedCount" / Int64ul,
        "SampleDroppedCount" / Int64ul,
        "TrackKind" / Int32ul,
        "ThisPtr" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=776, version=0)
class Microsoft_IE_776_0(Etw):
    pattern = Struct(
        "SampleRequstedCount" / Int64ul,
        "SampleDeliveredCount" / Int64ul,
        "SampleReceivedCount" / Int64ul,
        "SampleDroppedCount" / Int64ul,
        "TrackKind" / Int32ul,
        "ThisPtr" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=777, version=0)
class Microsoft_IE_777_0(Etw):
    pattern = Struct(
        "OutstandingStatsRequestCount" / Int64ul,
        "HrTask" / Int32ul,
        "ThisPtr" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=778, version=0)
class Microsoft_IE_778_0(Etw):
    pattern = Struct(
        "OutstandingStatsRequestCount" / Int64ul,
        "HrTask" / Int32ul,
        "ThisPtr" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=779, version=0)
class Microsoft_IE_779_0(Etw):
    pattern = Struct(
        "OutstandingStatsRequestCount" / Int64ul,
        "HrTask" / Int32ul,
        "ThisPtr" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=780, version=0)
class Microsoft_IE_780_0(Etw):
    pattern = Struct(
        "OutstandingStatsRequestCount" / Int64ul,
        "HrTask" / Int32ul,
        "ThisPtr" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=781, version=0)
class Microsoft_IE_781_0(Etw):
    pattern = Struct(
        "OutstandingStatsRequestCount" / Int64ul,
        "HrTask" / Int32ul,
        "ThisPtr" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=782, version=0)
class Microsoft_IE_782_0(Etw):
    pattern = Struct(
        "OutstandingStatsRequestCount" / Int64ul,
        "HrTask" / Int32ul,
        "ThisPtr" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=783, version=0)
class Microsoft_IE_783_0(Etw):
    pattern = Struct(
        "SampleRequstedCount" / Int64ul,
        "SampleDeliveredCount" / Int64ul,
        "SampleReceivedCount" / Int64ul,
        "SampleDroppedCount" / Int64ul,
        "TrackKind" / Int32ul,
        "ThisPtr" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=784, version=0)
class Microsoft_IE_784_0(Etw):
    pattern = Struct(
        "SampleRequstedCount" / Int64ul,
        "SampleDeliveredCount" / Int64ul,
        "SampleReceivedCount" / Int64ul,
        "SampleDroppedCount" / Int64ul,
        "TrackKind" / Int32ul,
        "ThisPtr" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=785, version=0)
class Microsoft_IE_785_0(Etw):
    pattern = Struct(
        "SampleRequstedCount" / Int64ul,
        "SampleDeliveredCount" / Int64ul,
        "SampleReceivedCount" / Int64ul,
        "SampleDroppedCount" / Int64ul,
        "TrackKind" / Int32ul,
        "ThisPtr" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=786, version=0)
class Microsoft_IE_786_0(Etw):
    pattern = Struct(
        "SampleRequstedCount" / Int64ul,
        "SampleDeliveredCount" / Int64ul,
        "SampleReceivedCount" / Int64ul,
        "SampleDroppedCount" / Int64ul,
        "TrackKind" / Int32ul,
        "ThisPtr" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=787, version=0)
class Microsoft_IE_787_0(Etw):
    pattern = Struct(
        "Domain" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=800, version=0)
class Microsoft_IE_800_0(Etw):
    pattern = Struct(
        "MethodName" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=801, version=0)
class Microsoft_IE_801_0(Etw):
    pattern = Struct(
        "MethodName" / WString,
        "HR" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=802, version=0)
class Microsoft_IE_802_0(Etw):
    pattern = Struct(
        "MethodName" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=803, version=0)
class Microsoft_IE_803_0(Etw):
    pattern = Struct(
        "MethodName" / WString,
        "HR" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=804, version=0)
class Microsoft_IE_804_0(Etw):
    pattern = Struct(
        "Reason" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=805, version=0)
class Microsoft_IE_805_0(Etw):
    pattern = Struct(
        "HandleType" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=806, version=0)
class Microsoft_IE_806_0(Etw):
    pattern = Struct(
        "HR" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=807, version=0)
class Microsoft_IE_807_0(Etw):
    pattern = Struct(
        "ProcessName" / WString,
        "PID" / Int32ul,
        "FileName" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=808, version=0)
class Microsoft_IE_808_0(Etw):
    pattern = Struct(
        "CurrentRound" / Int64ul,
        "CallsToProcess" / Int64ul,
        "CurrentTimeMs" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=809, version=0)
class Microsoft_IE_809_0(Etw):
    pattern = Struct(
        "CurrentRound" / Int64ul,
        "CallsToProcess" / Int64ul,
        "CurrentTimeMs" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=810, version=2)
class Microsoft_IE_810_2(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "TimerId" / Int32ul,
        "DeltaMs" / Int32sl,
        "PeriodMs" / Int32sl,
        "CurrentTimeMs" / Int64ul,
        "Flags" / Int32ul,
        "Callback" / Int64ul,
        "Visibility" / Int8ul,
        "TimerRound" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=811, version=0)
class Microsoft_IE_811_0(Etw):
    pattern = Struct(
        "JsVarInstance" / Int64ul,
        "ThisPointer" / Int64ul,
        "SSN" / Int32ul,
        "RefAfterChange" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=812, version=0)
class Microsoft_IE_812_0(Etw):
    pattern = Struct(
        "JsVarInstance" / Int64ul,
        "ThisPointer" / Int64ul,
        "SSN" / Int32ul,
        "RefAfterChange" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=813, version=0)
class Microsoft_IE_813_0(Etw):
    pattern = Struct(
        "JsVarInstance" / Int64ul,
        "ThisPointer" / Int64ul,
        "SSN" / Int32ul,
        "RefAfterChange" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=814, version=0)
class Microsoft_IE_814_0(Etw):
    pattern = Struct(
        "JsVarInstance" / Int64ul,
        "ThisPointer" / Int64ul,
        "SSN" / Int32ul,
        "RefAfterChange" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=815, version=0)
class Microsoft_IE_815_0(Etw):
    pattern = Struct(
        "JsVarInstance" / Int64ul,
        "ThisPointer" / Int64ul,
        "SSN" / Int32ul,
        "RefAfterChange" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=816, version=0)
class Microsoft_IE_816_0(Etw):
    pattern = Struct(
        "JsVarInstance" / Int64ul,
        "ThisPointer" / Int64ul,
        "SSN" / Int32ul,
        "RefAfterChange" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=817, version=0)
class Microsoft_IE_817_0(Etw):
    pattern = Struct(
        "StorageCategory" / Int8ul,
        "HandleType" / Int32ul,
        "Handle" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=818, version=0)
class Microsoft_IE_818_0(Etw):
    pattern = Struct(
        "StorageCategory" / Int8ul,
        "HandleType" / Int32ul,
        "Handle" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=819, version=0)
class Microsoft_IE_819_0(Etw):
    pattern = Struct(
        "StorageCategory" / Int8ul,
        "HandleType" / Int32ul,
        "Handle" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=820, version=0)
class Microsoft_IE_820_0(Etw):
    pattern = Struct(
        "StorageCategory" / Int8ul,
        "Method" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=821, version=0)
class Microsoft_IE_821_0(Etw):
    pattern = Struct(
        "StorageCategory" / Int8ul,
        "Method" / Int32ul,
        "HR" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=822, version=0)
class Microsoft_IE_822_0(Etw):
    pattern = Struct(
        "TaskName" / CString,
        "ObjectPointer" / Int64ul,
        "DelayTime" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=823, version=0)
class Microsoft_IE_823_0(Etw):
    pattern = Struct(
        "TaskName" / CString,
        "ScriptExecutionTime" / Int32ul,
        "IsIgnoredInTelemetry" / Int8ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=824, version=0)
class Microsoft_IE_824_0(Etw):
    pattern = Struct(
        "TaskName" / CString,
        "ObjectPointer" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=825, version=0)
class Microsoft_IE_825_0(Etw):
    pattern = Struct(
        "TaskName" / CString,
        "ObjectPointer" / Int64ul,
        "DelayTime" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=826, version=0)
class Microsoft_IE_826_0(Etw):
    pattern = Struct(
        "TaskName" / CString,
        "ScriptExecutionTime" / Int32ul,
        "IsIgnoredInTelemetry" / Int8ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=827, version=0)
class Microsoft_IE_827_0(Etw):
    pattern = Struct(
        "WindowObject" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=828, version=0)
class Microsoft_IE_828_0(Etw):
    pattern = Struct(
        "WindowObject" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=829, version=0)
class Microsoft_IE_829_0(Etw):
    pattern = Struct(
        "WindowObject" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=830, version=0)
class Microsoft_IE_830_0(Etw):
    pattern = Struct(
        "URL" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=831, version=0)
class Microsoft_IE_831_0(Etw):
    pattern = Struct(
        "URL" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=832, version=0)
class Microsoft_IE_832_0(Etw):
    pattern = Struct(
        "URL" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=833, version=0)
class Microsoft_IE_833_0(Etw):
    pattern = Struct(
        "Priority" / Int32sl
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=834, version=0)
class Microsoft_IE_834_0(Etw):
    pattern = Struct(
        "Priority" / Int32sl,
        "NestingLevel" / Int32sl
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=835, version=0)
class Microsoft_IE_835_0(Etw):
    pattern = Struct(
        "TaskQueueIndex" / Int32sl,
        "NestingLevel" / Int32sl,
        "TaskConsideredReadyTimeInUs" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=836, version=0)
class Microsoft_IE_836_0(Etw):
    pattern = Struct(
        "TaskQueueIndex" / Int32sl,
        "NestingLevel" / Int32sl,
        "TaskConsideredReadyTimeInUs" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=837, version=0)
class Microsoft_IE_837_0(Etw):
    pattern = Struct(
        "IsPerformingMicrotaskCheckpoint" / Int8ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=838, version=0)
class Microsoft_IE_838_0(Etw):
    pattern = Struct(
        "IsPerformingMicrotaskCheckpoint" / Int8ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=839, version=0)
class Microsoft_IE_839_0(Etw):
    pattern = Struct(
        "TaskQueueIndex" / Int32sl,
        "PendingTaskCount" / Int32sl
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=840, version=0)
class Microsoft_IE_840_0(Etw):
    pattern = Struct(
        "State" / WString,
        "ThisPtr" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=841, version=0)
class Microsoft_IE_841_0(Etw):
    pattern = Struct(
        "State" / WString,
        "ThisPtr" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=842, version=0)
class Microsoft_IE_842_0(Etw):
    pattern = Struct(
        "State" / WString,
        "ThisPtr" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=843, version=0)
class Microsoft_IE_843_0(Etw):
    pattern = Struct(
        "Candidate" / WString,
        "Mid" / WString,
        "SdpMLineIndex" / Int16ul,
        "ThisPtr" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=844, version=0)
class Microsoft_IE_844_0(Etw):
    pattern = Struct(
        "Candidate" / WString,
        "Mid" / WString,
        "SdpMLineIndex" / Int16ul,
        "ThisPtr" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=845, version=0)
class Microsoft_IE_845_0(Etw):
    pattern = Struct(
        "WindowObject" / Int64ul,
        "X" / Float32l,
        "Y" / Float32l,
        "Flags" / Int32sl,
        "DocumentObject" / Int64ul,
        "RelativeToLayoutViewport" / Int8ul,
        "SameMarkup" / Int8ul,
        "ClipToViewport" / Int8ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=846, version=0)
class Microsoft_IE_846_0(Etw):
    pattern = Struct(
        "WindowObject" / Int64ul,
        "X" / Float32l,
        "Y" / Float32l,
        "Flags" / Int32sl,
        "DocumentObject" / Int64ul,
        "RelativeToLayoutViewport" / Int8ul,
        "SameMarkup" / Int8ul,
        "ClipToViewport" / Int8ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=847, version=0)
class Microsoft_IE_847_0(Etw):
    pattern = Struct(
        "CPowerStateController" / Int64ul,
        "CDoc" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=848, version=0)
class Microsoft_IE_848_0(Etw):
    pattern = Struct(
        "CPowerStateController" / Int64ul,
        "CDoc" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=849, version=0)
class Microsoft_IE_849_0(Etw):
    pattern = Struct(
        "CPowerStateController" / Int64ul,
        "CDoc" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=850, version=0)
class Microsoft_IE_850_0(Etw):
    pattern = Struct(
        "CPowerStateController" / Int64ul,
        "CDoc" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=851, version=0)
class Microsoft_IE_851_0(Etw):
    pattern = Struct(
        "CPowerStateController" / Int64ul,
        "CDoc" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=852, version=0)
class Microsoft_IE_852_0(Etw):
    pattern = Struct(
        "CPowerStateController" / Int64ul,
        "CDoc" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=854, version=0)
class Microsoft_IE_854_0(Etw):
    pattern = Struct(
        "AllowExecution" / Int8ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=857, version=0)
class Microsoft_IE_857_0(Etw):
    pattern = Struct(
        "CancelledLowPri" / Int8ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=859, version=0)
class Microsoft_IE_859_0(Etw):
    pattern = Struct(
        "Element" / Int64ul,
        "Zero" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=860, version=0)
class Microsoft_IE_860_0(Etw):
    pattern = Struct(
        "CommandList" / Int64ul,
        "NumCommands" / Int32ul,
        "BytesUsed" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=862, version=0)
class Microsoft_IE_862_0(Etw):
    pattern = Struct(
        "FlushReason" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=863, version=0)
class Microsoft_IE_863_0(Etw):
    pattern = Struct(
        "PayloadSize" / Int32ul,
        "Header" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=864, version=0)
class Microsoft_IE_864_0(Etw):
    pattern = Struct(
        "Result" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=866, version=0)
class Microsoft_IE_866_0(Etw):
    pattern = Struct(
        "Container" / Int64ul,
        "Capacity" / Int32ul,
        "InUse" / Int32ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=867, version=0)
class Microsoft_IE_867_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Value" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=868, version=0)
class Microsoft_IE_868_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Value" / Int64ul
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=869, version=0)
class Microsoft_IE_869_0(Etw):
    pattern = Struct(
        "ExtensionId" / WString,
        "ScriptType" / Int32ul,
        "CorrelationId" / WString
    )


@declare(guid=guid("9e3b3947-ca5d-4614-91a2-7b624e0e7244"), event_id=870, version=0)
class Microsoft_IE_870_0(Etw):
    pattern = Struct(
        "ExtensionId" / WString,
        "ScriptType" / Int32ul,
        "ScriptExecutionTime" / Double,
        "CorrelationId" / WString
    )

