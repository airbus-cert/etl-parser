# -*- coding: utf-8 -*-
"""
Microsoft-Windows-WPD-CompositeClassDriver
GUID : 355c44fe-0c8e-4bf8-be28-8bc7b5a42720
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("355c44fe-0c8e-4bf8-be28-8bc7b5a42720"), event_id=100, version=0)
class Microsoft_Windows_WPD_CompositeClassDriver_100_0(Etw):
    pattern = Struct(
        "TransportSymbolicLink" / WString
    )


@declare(guid=guid("355c44fe-0c8e-4bf8-be28-8bc7b5a42720"), event_id=101, version=0)
class Microsoft_Windows_WPD_CompositeClassDriver_101_0(Etw):
    pattern = Struct(
        "TransportSymbolicLink" / WString
    )


@declare(guid=guid("355c44fe-0c8e-4bf8-be28-8bc7b5a42720"), event_id=102, version=0)
class Microsoft_Windows_WPD_CompositeClassDriver_102_0(Etw):
    pattern = Struct(
        "TransportSymbolicLink" / WString
    )


@declare(guid=guid("355c44fe-0c8e-4bf8-be28-8bc7b5a42720"), event_id=103, version=0)
class Microsoft_Windows_WPD_CompositeClassDriver_103_0(Etw):
    pattern = Struct(
        "TransportSymbolicLink" / WString
    )


@declare(guid=guid("355c44fe-0c8e-4bf8-be28-8bc7b5a42720"), event_id=104, version=0)
class Microsoft_Windows_WPD_CompositeClassDriver_104_0(Etw):
    pattern = Struct(
        "ReferenceString" / WString
    )


@declare(guid=guid("355c44fe-0c8e-4bf8-be28-8bc7b5a42720"), event_id=105, version=0)
class Microsoft_Windows_WPD_CompositeClassDriver_105_0(Etw):
    pattern = Struct(
        "ReferenceString" / WString
    )


@declare(guid=guid("355c44fe-0c8e-4bf8-be28-8bc7b5a42720"), event_id=200, version=0)
class Microsoft_Windows_WPD_CompositeClassDriver_200_0(Etw):
    pattern = Struct(
        "TransportSymbolicLink" / WString
    )


@declare(guid=guid("355c44fe-0c8e-4bf8-be28-8bc7b5a42720"), event_id=201, version=0)
class Microsoft_Windows_WPD_CompositeClassDriver_201_0(Etw):
    pattern = Struct(
        "TransportSymbolicLink" / WString
    )


@declare(guid=guid("355c44fe-0c8e-4bf8-be28-8bc7b5a42720"), event_id=202, version=0)
class Microsoft_Windows_WPD_CompositeClassDriver_202_0(Etw):
    pattern = Struct(
        "InterfaceGUID" / Guid,
        "ReferenceString" / WString
    )


@declare(guid=guid("355c44fe-0c8e-4bf8-be28-8bc7b5a42720"), event_id=203, version=0)
class Microsoft_Windows_WPD_CompositeClassDriver_203_0(Etw):
    pattern = Struct(
        "InterfaceGUID" / Guid,
        "ReferenceString" / WString
    )


@declare(guid=guid("355c44fe-0c8e-4bf8-be28-8bc7b5a42720"), event_id=301, version=0)
class Microsoft_Windows_WPD_CompositeClassDriver_301_0(Etw):
    pattern = Struct(
        "TransportSymbolicLink" / WString
    )


@declare(guid=guid("355c44fe-0c8e-4bf8-be28-8bc7b5a42720"), event_id=302, version=0)
class Microsoft_Windows_WPD_CompositeClassDriver_302_0(Etw):
    pattern = Struct(
        "TransportSymbolicLink" / WString
    )


@declare(guid=guid("355c44fe-0c8e-4bf8-be28-8bc7b5a42720"), event_id=303, version=0)
class Microsoft_Windows_WPD_CompositeClassDriver_303_0(Etw):
    pattern = Struct(
        "ExpectedSize" / Int64ul,
        "ActualSize" / Int64ul
    )


@declare(guid=guid("355c44fe-0c8e-4bf8-be28-8bc7b5a42720"), event_id=304, version=0)
class Microsoft_Windows_WPD_CompositeClassDriver_304_0(Etw):
    pattern = Struct(
        "ExpectedSize" / Int64ul,
        "ActualSize" / Int64ul
    )


@declare(guid=guid("355c44fe-0c8e-4bf8-be28-8bc7b5a42720"), event_id=305, version=0)
class Microsoft_Windows_WPD_CompositeClassDriver_305_0(Etw):
    pattern = Struct(
        "ExpectedSize" / Int64ul,
        "ActualSize" / Int64ul
    )


@declare(guid=guid("355c44fe-0c8e-4bf8-be28-8bc7b5a42720"), event_id=308, version=0)
class Microsoft_Windows_WPD_CompositeClassDriver_308_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("355c44fe-0c8e-4bf8-be28-8bc7b5a42720"), event_id=309, version=0)
class Microsoft_Windows_WPD_CompositeClassDriver_309_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("355c44fe-0c8e-4bf8-be28-8bc7b5a42720"), event_id=310, version=0)
class Microsoft_Windows_WPD_CompositeClassDriver_310_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("355c44fe-0c8e-4bf8-be28-8bc7b5a42720"), event_id=311, version=0)
class Microsoft_Windows_WPD_CompositeClassDriver_311_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("355c44fe-0c8e-4bf8-be28-8bc7b5a42720"), event_id=312, version=0)
class Microsoft_Windows_WPD_CompositeClassDriver_312_0(Etw):
    pattern = Struct(
        "ExpectedSize" / Int64ul,
        "ActualSize" / Int64ul
    )


@declare(guid=guid("355c44fe-0c8e-4bf8-be28-8bc7b5a42720"), event_id=313, version=0)
class Microsoft_Windows_WPD_CompositeClassDriver_313_0(Etw):
    pattern = Struct(
        "ExpectedSize" / Int64ul,
        "ActualSize" / Int64ul
    )

