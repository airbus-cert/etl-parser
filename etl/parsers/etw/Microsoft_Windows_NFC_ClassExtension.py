# -*- coding: utf-8 -*-
"""
Microsoft-Windows-NFC-ClassExtension
GUID : 85c070e6-f9ae-481f-aacb-bc550bfd35a1
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("85c070e6-f9ae-481f-aacb-bc550bfd35a1"), event_id=1, version=1)
class Microsoft_Windows_NFC_ClassExtension_1_1(Etw):
    pattern = Struct(
        "MessageType" / Int8ul,
        "PacketBoundaryFlag" / Int8ul,
        "PacketSize" / Int16ul,
        "RawPacket" / Int8ul
    )


@declare(guid=guid("85c070e6-f9ae-481f-aacb-bc550bfd35a1"), event_id=2, version=1)
class Microsoft_Windows_NFC_ClassExtension_2_1(Etw):
    pattern = Struct(
        "MessageType" / Int8ul,
        "PacketBoundaryFlag" / Int8ul,
        "PacketSize" / Int16ul,
        "RawPacket" / Int8ul
    )


@declare(guid=guid("85c070e6-f9ae-481f-aacb-bc550bfd35a1"), event_id=3, version=1)
class Microsoft_Windows_NFC_ClassExtension_3_1(Etw):
    pattern = Struct(
        "MessageType" / Int8ul,
        "PacketBoundaryFlag" / Int8ul,
        "PacketSize" / Int16ul
    )


@declare(guid=guid("85c070e6-f9ae-481f-aacb-bc550bfd35a1"), event_id=4, version=1)
class Microsoft_Windows_NFC_ClassExtension_4_1(Etw):
    pattern = Struct(
        "MessageType" / Int8ul,
        "PacketBoundaryFlag" / Int8ul,
        "PacketSize" / Int16ul
    )


@declare(guid=guid("85c070e6-f9ae-481f-aacb-bc550bfd35a1"), event_id=101, version=1)
class Microsoft_Windows_NFC_ClassExtension_101_1(Etw):
    pattern = Struct(
        "FileObject" / Int64ul,
        "Role" / Int32ul,
        "Type" / CString,
        "TranslationType" / Int32sl,
        "TNF" / Int8ul
    )


@declare(guid=guid("85c070e6-f9ae-481f-aacb-bc550bfd35a1"), event_id=102, version=1)
class Microsoft_Windows_NFC_ClassExtension_102_1(Etw):
    pattern = Struct(
        "FileObject" / Int64ul,
        "Role" / Int32ul,
        "Type" / CString,
        "TranslationType" / Int32sl,
        "TNF" / Int8ul
    )


@declare(guid=guid("85c070e6-f9ae-481f-aacb-bc550bfd35a1"), event_id=103, version=1)
class Microsoft_Windows_NFC_ClassExtension_103_1(Etw):
    pattern = Struct(
        "FileObject" / Int64ul,
        "PayloadSize" / Int64ul
    )


@declare(guid=guid("85c070e6-f9ae-481f-aacb-bc550bfd35a1"), event_id=104, version=1)
class Microsoft_Windows_NFC_ClassExtension_104_1(Etw):
    pattern = Struct(
        "FileObject" / Int64ul
    )


@declare(guid=guid("85c070e6-f9ae-481f-aacb-bc550bfd35a1"), event_id=105, version=1)
class Microsoft_Windows_NFC_ClassExtension_105_1(Etw):
    pattern = Struct(
        "FileObject" / Int64ul,
        "Status" / Int32ul,
        "Information" / Int64ul
    )


@declare(guid=guid("85c070e6-f9ae-481f-aacb-bc550bfd35a1"), event_id=106, version=1)
class Microsoft_Windows_NFC_ClassExtension_106_1(Etw):
    pattern = Struct(
        "FileObject" / Int64ul
    )


@declare(guid=guid("85c070e6-f9ae-481f-aacb-bc550bfd35a1"), event_id=107, version=1)
class Microsoft_Windows_NFC_ClassExtension_107_1(Etw):
    pattern = Struct(
        "FileObject" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("85c070e6-f9ae-481f-aacb-bc550bfd35a1"), event_id=201, version=1)
class Microsoft_Windows_NFC_ClassExtension_201_1(Etw):
    pattern = Struct(
        "RadioIsOn" / Int8ul
    )


@declare(guid=guid("85c070e6-f9ae-481f-aacb-bc550bfd35a1"), event_id=302, version=1)
class Microsoft_Windows_NFC_ClassExtension_302_1(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("85c070e6-f9ae-481f-aacb-bc550bfd35a1"), event_id=303, version=1)
class Microsoft_Windows_NFC_ClassExtension_303_1(Etw):
    pattern = Struct(
        "Version" / Int32ul
    )


@declare(guid=guid("85c070e6-f9ae-481f-aacb-bc550bfd35a1"), event_id=304, version=1)
class Microsoft_Windows_NFC_ClassExtension_304_1(Etw):
    pattern = Struct(
        "FirmwareFile" / WString,
        "Force" / Int8ul
    )


@declare(guid=guid("85c070e6-f9ae-481f-aacb-bc550bfd35a1"), event_id=305, version=1)
class Microsoft_Windows_NFC_ClassExtension_305_1(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("85c070e6-f9ae-481f-aacb-bc550bfd35a1"), event_id=306, version=1)
class Microsoft_Windows_NFC_ClassExtension_306_1(Etw):
    pattern = Struct(
        "RfArrivalDepartureEvent" / Int32ul
    )


@declare(guid=guid("85c070e6-f9ae-481f-aacb-bc550bfd35a1"), event_id=308, version=1)
class Microsoft_Windows_NFC_ClassExtension_308_1(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "Length" / Int16ul
    )


@declare(guid=guid("85c070e6-f9ae-481f-aacb-bc550bfd35a1"), event_id=309, version=1)
class Microsoft_Windows_NFC_ClassExtension_309_1(Etw):
    pattern = Struct(
        "Length" / Int32ul
    )


@declare(guid=guid("85c070e6-f9ae-481f-aacb-bc550bfd35a1"), event_id=310, version=1)
class Microsoft_Windows_NFC_ClassExtension_310_1(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("85c070e6-f9ae-481f-aacb-bc550bfd35a1"), event_id=401, version=1)
class Microsoft_Windows_NFC_ClassExtension_401_1(Etw):
    pattern = Struct(
        "IdleTimeout" / Int32ul,
        "PollDevInfo" / Int32ul,
        "NfcIp_Mode" / Int8ul,
        "Duration" / Int32ul,
        "LLCP_MIU" / Int16ul,
        "LLCP_LTO" / Int8ul,
        "LLCP_RecvWindowSize" / Int8ul
    )


@declare(guid=guid("85c070e6-f9ae-481f-aacb-bc550bfd35a1"), event_id=402, version=1)
class Microsoft_Windows_NFC_ClassExtension_402_1(Etw):
    pattern = Struct(
        "NfcRadioTurnedOff" / Int8ul,
        "NfcRadioFlightMode" / Int8ul,
        "SERadioTurnedOff" / Int8ul,
        "SERadioFlightMode" / Int8ul
    )

