# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Wordpad
GUID : 54ffd262-99fe-4576-96e7-1adb500370dc
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("54ffd262-99fe-4576-96e7-1adb500370dc"), event_id=3, version=0)
class Microsoft_Windows_Wordpad_3_0(Etw):
    pattern = Struct(
        "StringParam" / WString
    )


@declare(guid=guid("54ffd262-99fe-4576-96e7-1adb500370dc"), event_id=7, version=0)
class Microsoft_Windows_Wordpad_7_0(Etw):
    pattern = Struct(
        "StringParam" / WString
    )


@declare(guid=guid("54ffd262-99fe-4576-96e7-1adb500370dc"), event_id=8, version=0)
class Microsoft_Windows_Wordpad_8_0(Etw):
    pattern = Struct(
        "StringParam" / WString
    )


@declare(guid=guid("54ffd262-99fe-4576-96e7-1adb500370dc"), event_id=9, version=0)
class Microsoft_Windows_Wordpad_9_0(Etw):
    pattern = Struct(
        "StringParam" / WString
    )


@declare(guid=guid("54ffd262-99fe-4576-96e7-1adb500370dc"), event_id=11, version=0)
class Microsoft_Windows_Wordpad_11_0(Etw):
    pattern = Struct(
        "HResultParam" / Int32ul
    )


@declare(guid=guid("54ffd262-99fe-4576-96e7-1adb500370dc"), event_id=12, version=0)
class Microsoft_Windows_Wordpad_12_0(Etw):
    pattern = Struct(
        "HResultParam" / Int32ul,
        "StringParam" / WString
    )


@declare(guid=guid("54ffd262-99fe-4576-96e7-1adb500370dc"), event_id=13, version=0)
class Microsoft_Windows_Wordpad_13_0(Etw):
    pattern = Struct(
        "StringParam" / WString
    )


@declare(guid=guid("54ffd262-99fe-4576-96e7-1adb500370dc"), event_id=20, version=0)
class Microsoft_Windows_Wordpad_20_0(Etw):
    pattern = Struct(
        "StringParam" / WString
    )


@declare(guid=guid("54ffd262-99fe-4576-96e7-1adb500370dc"), event_id=21, version=0)
class Microsoft_Windows_Wordpad_21_0(Etw):
    pattern = Struct(
        "StringParam" / WString,
        "HResultParam" / Int32ul
    )


@declare(guid=guid("54ffd262-99fe-4576-96e7-1adb500370dc"), event_id=22, version=0)
class Microsoft_Windows_Wordpad_22_0(Etw):
    pattern = Struct(
        "StringParam" / WString,
        "DWordParam" / Int64ul
    )


@declare(guid=guid("54ffd262-99fe-4576-96e7-1adb500370dc"), event_id=23, version=0)
class Microsoft_Windows_Wordpad_23_0(Etw):
    pattern = Struct(
        "LivePreviewType" / Int32sl
    )


@declare(guid=guid("54ffd262-99fe-4576-96e7-1adb500370dc"), event_id=25, version=0)
class Microsoft_Windows_Wordpad_25_0(Etw):
    pattern = Struct(
        "LivePreviewType" / Int32sl
    )


@declare(guid=guid("54ffd262-99fe-4576-96e7-1adb500370dc"), event_id=27, version=0)
class Microsoft_Windows_Wordpad_27_0(Etw):
    pattern = Struct(
        "LivePreviewType" / Int32sl
    )


@declare(guid=guid("54ffd262-99fe-4576-96e7-1adb500370dc"), event_id=35, version=0)
class Microsoft_Windows_Wordpad_35_0(Etw):
    pattern = Struct(
        "StringParam" / WString
    )


@declare(guid=guid("54ffd262-99fe-4576-96e7-1adb500370dc"), event_id=36, version=0)
class Microsoft_Windows_Wordpad_36_0(Etw):
    pattern = Struct(
        "StringParam" / WString,
        "HResultParam" / Int32ul
    )


@declare(guid=guid("54ffd262-99fe-4576-96e7-1adb500370dc"), event_id=37, version=0)
class Microsoft_Windows_Wordpad_37_0(Etw):
    pattern = Struct(
        "HResultParam" / Int32ul
    )


@declare(guid=guid("54ffd262-99fe-4576-96e7-1adb500370dc"), event_id=38, version=0)
class Microsoft_Windows_Wordpad_38_0(Etw):
    pattern = Struct(
        "StringParam" / WString
    )


@declare(guid=guid("54ffd262-99fe-4576-96e7-1adb500370dc"), event_id=45, version=0)
class Microsoft_Windows_Wordpad_45_0(Etw):
    pattern = Struct(
        "StringParam" / WString
    )


@declare(guid=guid("54ffd262-99fe-4576-96e7-1adb500370dc"), event_id=46, version=0)
class Microsoft_Windows_Wordpad_46_0(Etw):
    pattern = Struct(
        "HResultParam" / Int32ul
    )

