# -*- coding: utf-8 -*-
"""
DptfAcpiEtwProvider
GUID : 5885720d-f086-4614-a17c-4770c2461af2
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("5885720d-f086-4614-a17c-4770c2461af2"), event_id=0, version=0)
class DptfAcpiEtwProvider_0_0(Etw):
    pattern = Struct(
        "stringPtr" / WString
    )


@declare(guid=guid("5885720d-f086-4614-a17c-4770c2461af2"), event_id=100, version=0)
class DptfAcpiEtwProvider_100_0(Etw):
    pattern = Struct(
        "Interrupt" / Int64ul,
        "MessageID" / Int32ul
    )


@declare(guid=guid("5885720d-f086-4614-a17c-4770c2461af2"), event_id=101, version=0)
class DptfAcpiEtwProvider_101_0(Etw):
    pattern = Struct(
        "Status" / Int8ul
    )


@declare(guid=guid("5885720d-f086-4614-a17c-4770c2461af2"), event_id=102, version=0)
class DptfAcpiEtwProvider_102_0(Etw):
    pattern = Struct(
        "String" / WString
    )


@declare(guid=guid("5885720d-f086-4614-a17c-4770c2461af2"), event_id=103, version=0)
class DptfAcpiEtwProvider_103_0(Etw):
    pattern = Struct(
        "String" / WString
    )


@declare(guid=guid("5885720d-f086-4614-a17c-4770c2461af2"), event_id=104, version=0)
class DptfAcpiEtwProvider_104_0(Etw):
    pattern = Struct(
        "String" / WString
    )


@declare(guid=guid("5885720d-f086-4614-a17c-4770c2461af2"), event_id=105, version=0)
class DptfAcpiEtwProvider_105_0(Etw):
    pattern = Struct(
        "String" / WString
    )


@declare(guid=guid("5885720d-f086-4614-a17c-4770c2461af2"), event_id=106, version=0)
class DptfAcpiEtwProvider_106_0(Etw):
    pattern = Struct(
        "String" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("5885720d-f086-4614-a17c-4770c2461af2"), event_id=107, version=0)
class DptfAcpiEtwProvider_107_0(Etw):
    pattern = Struct(
        "Interrupt" / Int64ul,
        "AssociatedObject" / Int64ul
    )

