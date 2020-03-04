# -*- coding: utf-8 -*-
"""
Microsoft-Windows-TerminalServices-ServerUSBDevices
GUID : dcbe5aaa-16e2-457c-9337-366950045f0a
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("dcbe5aaa-16e2-457c-9337-366950045f0a"), event_id=2, version=0)
class Microsoft_Windows_TerminalServices_ServerUSBDevices_2_0(Etw):
    pattern = Struct(
        "message" / CString
    )


@declare(guid=guid("dcbe5aaa-16e2-457c-9337-366950045f0a"), event_id=3, version=0)
class Microsoft_Windows_TerminalServices_ServerUSBDevices_3_0(Etw):
    pattern = Struct(
        "message" / CString
    )


@declare(guid=guid("dcbe5aaa-16e2-457c-9337-366950045f0a"), event_id=4, version=0)
class Microsoft_Windows_TerminalServices_ServerUSBDevices_4_0(Etw):
    pattern = Struct(
        "message" / CString
    )


@declare(guid=guid("dcbe5aaa-16e2-457c-9337-366950045f0a"), event_id=5, version=0)
class Microsoft_Windows_TerminalServices_ServerUSBDevices_5_0(Etw):
    pattern = Struct(
        "message" / CString
    )


@declare(guid=guid("dcbe5aaa-16e2-457c-9337-366950045f0a"), event_id=6, version=0)
class Microsoft_Windows_TerminalServices_ServerUSBDevices_6_0(Etw):
    pattern = Struct(
        "message" / CString
    )


@declare(guid=guid("dcbe5aaa-16e2-457c-9337-366950045f0a"), event_id=7, version=0)
class Microsoft_Windows_TerminalServices_ServerUSBDevices_7_0(Etw):
    pattern = Struct(
        "message" / CString
    )


@declare(guid=guid("dcbe5aaa-16e2-457c-9337-366950045f0a"), event_id=8, version=0)
class Microsoft_Windows_TerminalServices_ServerUSBDevices_8_0(Etw):
    pattern = Struct(
        "message" / CString
    )


@declare(guid=guid("dcbe5aaa-16e2-457c-9337-366950045f0a"), event_id=9, version=0)
class Microsoft_Windows_TerminalServices_ServerUSBDevices_9_0(Etw):
    pattern = Struct(
        "message" / CString
    )


@declare(guid=guid("dcbe5aaa-16e2-457c-9337-366950045f0a"), event_id=32, version=0)
class Microsoft_Windows_TerminalServices_ServerUSBDevices_32_0(Etw):
    pattern = Struct(
        "objectPointer" / Int64ul
    )


@declare(guid=guid("dcbe5aaa-16e2-457c-9337-366950045f0a"), event_id=34, version=0)
class Microsoft_Windows_TerminalServices_ServerUSBDevices_34_0(Etw):
    pattern = Struct(
        "objectPointer" / Int64ul
    )


@declare(guid=guid("dcbe5aaa-16e2-457c-9337-366950045f0a"), event_id=35, version=0)
class Microsoft_Windows_TerminalServices_ServerUSBDevices_35_0(Etw):
    pattern = Struct(
        "deviceName" / WString
    )


@declare(guid=guid("dcbe5aaa-16e2-457c-9337-366950045f0a"), event_id=37, version=0)
class Microsoft_Windows_TerminalServices_ServerUSBDevices_37_0(Etw):
    pattern = Struct(
        "deviceName" / WString
    )


@declare(guid=guid("dcbe5aaa-16e2-457c-9337-366950045f0a"), event_id=38, version=0)
class Microsoft_Windows_TerminalServices_ServerUSBDevices_38_0(Etw):
    pattern = Struct(
        "objectPointer" / Int64ul,
        "ntStatus" / Int32ul
    )


@declare(guid=guid("dcbe5aaa-16e2-457c-9337-366950045f0a"), event_id=39, version=0)
class Microsoft_Windows_TerminalServices_ServerUSBDevices_39_0(Etw):
    pattern = Struct(
        "objectPointer" / Int64ul,
        "ntStatus" / Int32ul
    )


@declare(guid=guid("dcbe5aaa-16e2-457c-9337-366950045f0a"), event_id=40, version=0)
class Microsoft_Windows_TerminalServices_ServerUSBDevices_40_0(Etw):
    pattern = Struct(
        "objectPointer" / Int64ul,
        "ntStatus" / Int32ul
    )


@declare(guid=guid("dcbe5aaa-16e2-457c-9337-366950045f0a"), event_id=41, version=0)
class Microsoft_Windows_TerminalServices_ServerUSBDevices_41_0(Etw):
    pattern = Struct(
        "objectPointer" / Int64ul,
        "ntStatus" / Int32ul
    )


@declare(guid=guid("dcbe5aaa-16e2-457c-9337-366950045f0a"), event_id=42, version=0)
class Microsoft_Windows_TerminalServices_ServerUSBDevices_42_0(Etw):
    pattern = Struct(
        "objectPointer" / Int64ul,
        "nameString" / WString
    )


@declare(guid=guid("dcbe5aaa-16e2-457c-9337-366950045f0a"), event_id=43, version=0)
class Microsoft_Windows_TerminalServices_ServerUSBDevices_43_0(Etw):
    pattern = Struct(
        "objectPointer" / Int64ul,
        "ntStatus" / Int32ul
    )


@declare(guid=guid("dcbe5aaa-16e2-457c-9337-366950045f0a"), event_id=44, version=0)
class Microsoft_Windows_TerminalServices_ServerUSBDevices_44_0(Etw):
    pattern = Struct(
        "objectPointer" / Int64ul,
        "ntStatus" / Int32ul
    )

