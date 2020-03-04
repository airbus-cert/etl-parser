# -*- coding: utf-8 -*-
"""
Microsoft-Windows-TerminalServices-ClientUSBDevices
GUID : 6e400999-5b82-475f-b800-cef6fe361539
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("6e400999-5b82-475f-b800-cef6fe361539"), event_id=2, version=0)
class Microsoft_Windows_TerminalServices_ClientUSBDevices_2_0(Etw):
    pattern = Struct(
        "message" / CString
    )


@declare(guid=guid("6e400999-5b82-475f-b800-cef6fe361539"), event_id=3, version=0)
class Microsoft_Windows_TerminalServices_ClientUSBDevices_3_0(Etw):
    pattern = Struct(
        "message" / CString
    )


@declare(guid=guid("6e400999-5b82-475f-b800-cef6fe361539"), event_id=4, version=0)
class Microsoft_Windows_TerminalServices_ClientUSBDevices_4_0(Etw):
    pattern = Struct(
        "message" / CString
    )


@declare(guid=guid("6e400999-5b82-475f-b800-cef6fe361539"), event_id=5, version=0)
class Microsoft_Windows_TerminalServices_ClientUSBDevices_5_0(Etw):
    pattern = Struct(
        "message" / CString
    )


@declare(guid=guid("6e400999-5b82-475f-b800-cef6fe361539"), event_id=6, version=0)
class Microsoft_Windows_TerminalServices_ClientUSBDevices_6_0(Etw):
    pattern = Struct(
        "message" / CString
    )


@declare(guid=guid("6e400999-5b82-475f-b800-cef6fe361539"), event_id=7, version=0)
class Microsoft_Windows_TerminalServices_ClientUSBDevices_7_0(Etw):
    pattern = Struct(
        "message" / CString
    )


@declare(guid=guid("6e400999-5b82-475f-b800-cef6fe361539"), event_id=8, version=0)
class Microsoft_Windows_TerminalServices_ClientUSBDevices_8_0(Etw):
    pattern = Struct(
        "message" / CString
    )


@declare(guid=guid("6e400999-5b82-475f-b800-cef6fe361539"), event_id=9, version=0)
class Microsoft_Windows_TerminalServices_ClientUSBDevices_9_0(Etw):
    pattern = Struct(
        "message" / CString
    )


@declare(guid=guid("6e400999-5b82-475f-b800-cef6fe361539"), event_id=46, version=0)
class Microsoft_Windows_TerminalServices_ClientUSBDevices_46_0(Etw):
    pattern = Struct(
        "deviceName" / WString
    )

