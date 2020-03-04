# -*- coding: utf-8 -*-
"""
Microsoft-Windows-EaseOfAccess
GUID : 74b4a4b1-2302-4768-ac5b-9773dd456b08
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("74b4a4b1-2302-4768-ac5b-9773dd456b08"), event_id=39, version=0)
class Microsoft_Windows_EaseOfAccess_39_0(Etw):
    pattern = Struct(
        "Left" / Int32ul,
        "Top" / Int32ul,
        "Right" / Int32ul,
        "Bottom" / Int32ul
    )


@declare(guid=guid("74b4a4b1-2302-4768-ac5b-9773dd456b08"), event_id=41, version=0)
class Microsoft_Windows_EaseOfAccess_41_0(Etw):
    pattern = Struct(
        "SourceLeft" / Int32ul,
        "SourceTop" / Int32ul,
        "SourceRight" / Int32ul,
        "SourceBottom" / Int32ul,
        "DestinationLeft" / Int32ul,
        "DestinationTop" / Int32ul,
        "DestinationRight" / Int32ul,
        "DestinationBottom" / Int32ul
    )


@declare(guid=guid("74b4a4b1-2302-4768-ac5b-9773dd456b08"), event_id=42, version=0)
class Microsoft_Windows_EaseOfAccess_42_0(Etw):
    pattern = Struct(
        "Error" / Int32ul
    )


@declare(guid=guid("74b4a4b1-2302-4768-ac5b-9773dd456b08"), event_id=43, version=0)
class Microsoft_Windows_EaseOfAccess_43_0(Etw):
    pattern = Struct(
        "InitialX" / Int32sl,
        "InitialY" / Int32sl,
        "DestinationX" / Int32sl,
        "DestinationY" / Int32sl,
        "IsTracking" / Int8ul
    )


@declare(guid=guid("74b4a4b1-2302-4768-ac5b-9773dd456b08"), event_id=44, version=0)
class Microsoft_Windows_EaseOfAccess_44_0(Etw):
    pattern = Struct(
        "DestinationX" / Int32sl,
        "DestinationY" / Int32sl,
        "Left" / Int32ul,
        "Top" / Int32ul,
        "Right" / Int32ul,
        "Bottom" / Int32ul,
        "FullscreenTrackingMode" / Int32ul
    )

