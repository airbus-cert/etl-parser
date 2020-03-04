# -*- coding: utf-8 -*-
"""
Microsoft-WindowsPhone-Ufx
GUID : e98ebdbf-3058-4784-8521-47860b1d2b8e
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("e98ebdbf-3058-4784-8521-47860b1d2b8e"), event_id=100, version=0)
class Microsoft_WindowsPhone_Ufx_100_0(Etw):
    pattern = Struct(
        "Str" / CString,
        "Int" / Int32ul
    )


@declare(guid=guid("e98ebdbf-3058-4784-8521-47860b1d2b8e"), event_id=101, version=0)
class Microsoft_WindowsPhone_Ufx_101_0(Etw):
    pattern = Struct(
        "File" / CString,
        "Line" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("e98ebdbf-3058-4784-8521-47860b1d2b8e"), event_id=102, version=0)
class Microsoft_WindowsPhone_Ufx_102_0(Etw):
    pattern = Struct(
        "Function" / CString
    )


@declare(guid=guid("e98ebdbf-3058-4784-8521-47860b1d2b8e"), event_id=103, version=0)
class Microsoft_WindowsPhone_Ufx_103_0(Etw):
    pattern = Struct(
        "Function" / CString
    )


@declare(guid=guid("e98ebdbf-3058-4784-8521-47860b1d2b8e"), event_id=104, version=0)
class Microsoft_WindowsPhone_Ufx_104_0(Etw):
    pattern = Struct(
        "Function" / CString,
        "Message" / CString,
        "IntParam" / Int32ul
    )


@declare(guid=guid("e98ebdbf-3058-4784-8521-47860b1d2b8e"), event_id=105, version=0)
class Microsoft_WindowsPhone_Ufx_105_0(Etw):
    pattern = Struct(
        "Index" / Int32ul,
        "IOCTL" / Int32ul
    )


@declare(guid=guid("e98ebdbf-3058-4784-8521-47860b1d2b8e"), event_id=106, version=0)
class Microsoft_WindowsPhone_Ufx_106_0(Etw):
    pattern = Struct(
        "Function" / CString,
        "Message" / CString
    )


@declare(guid=guid("e98ebdbf-3058-4784-8521-47860b1d2b8e"), event_id=107, version=0)
class Microsoft_WindowsPhone_Ufx_107_0(Etw):
    pattern = Struct(
        "Description" / CString,
        "Direction" / Int32ul,
        "Type" / Int32ul,
        "Recipient" / Int32ul,
        "Request" / Int32ul,
        "wValue" / Int32ul,
        "wIndex" / Int32ul,
        "wLength" / Int32ul
    )


@declare(guid=guid("e98ebdbf-3058-4784-8521-47860b1d2b8e"), event_id=108, version=0)
class Microsoft_WindowsPhone_Ufx_108_0(Etw):
    pattern = Struct(
        "Machine" / CString
    )


@declare(guid=guid("e98ebdbf-3058-4784-8521-47860b1d2b8e"), event_id=109, version=0)
class Microsoft_WindowsPhone_Ufx_109_0(Etw):
    pattern = Struct(
        "Machine" / CString,
        "Type" / CString,
        "State" / CString
    )


@declare(guid=guid("e98ebdbf-3058-4784-8521-47860b1d2b8e"), event_id=110, version=0)
class Microsoft_WindowsPhone_Ufx_110_0(Etw):
    pattern = Struct(
        "Machine" / CString,
        "Type" / CString,
        "Event" / CString,
        "Payload" / Int64ul
    )


@declare(guid=guid("e98ebdbf-3058-4784-8521-47860b1d2b8e"), event_id=111, version=0)
class Microsoft_WindowsPhone_Ufx_111_0(Etw):
    pattern = Struct(
        "Machine" / CString,
        "Event" / CString,
        "Payload" / Int64ul
    )


@declare(guid=guid("e98ebdbf-3058-4784-8521-47860b1d2b8e"), event_id=112, version=0)
class Microsoft_WindowsPhone_Ufx_112_0(Etw):
    pattern = Struct(
        "Machine" / CString,
        "ActionName" / CString
    )


@declare(guid=guid("e98ebdbf-3058-4784-8521-47860b1d2b8e"), event_id=113, version=0)
class Microsoft_WindowsPhone_Ufx_113_0(Etw):
    pattern = Struct(
        "Machine" / CString,
        "Event" / CString,
        "ToState" / CString
    )


@declare(guid=guid("e98ebdbf-3058-4784-8521-47860b1d2b8e"), event_id=114, version=0)
class Microsoft_WindowsPhone_Ufx_114_0(Etw):
    pattern = Struct(
        "Machine" / CString,
        "Exception" / Int32ul
    )


@declare(guid=guid("e98ebdbf-3058-4784-8521-47860b1d2b8e"), event_id=115, version=0)
class Microsoft_WindowsPhone_Ufx_115_0(Etw):
    pattern = Struct(
        "Machine" / CString,
        "NewQueueSize" / Int32ul
    )


@declare(guid=guid("e98ebdbf-3058-4784-8521-47860b1d2b8e"), event_id=116, version=0)
class Microsoft_WindowsPhone_Ufx_116_0(Etw):
    pattern = Struct(
        "Machine" / CString,
        "FromState" / CString
    )


@declare(guid=guid("e98ebdbf-3058-4784-8521-47860b1d2b8e"), event_id=117, version=0)
class Microsoft_WindowsPhone_Ufx_117_0(Etw):
    pattern = Struct(
        "Function" / CString,
        "Message" / CString,
        "IntParam" / Int32ul
    )


@declare(guid=guid("e98ebdbf-3058-4784-8521-47860b1d2b8e"), event_id=118, version=0)
class Microsoft_WindowsPhone_Ufx_118_0(Etw):
    pattern = Struct(
        "Str" / CString
    )


@declare(guid=guid("e98ebdbf-3058-4784-8521-47860b1d2b8e"), event_id=119, version=0)
class Microsoft_WindowsPhone_Ufx_119_0(Etw):
    pattern = Struct(
        "Str" / CString,
        "Int" / Int32ul
    )

