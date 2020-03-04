# -*- coding: utf-8 -*-
"""
Microsoft-Windows-DisplayColorCalibration
GUID : 3239eb6f-c7fc-4953-aa15-646829a4ca4c
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("3239eb6f-c7fc-4953-aa15-646829a4ca4c"), event_id=1, version=0)
class Microsoft_Windows_DisplayColorCalibration_1_0(Etw):
    pattern = Struct(
        "Device" / WString
    )


@declare(guid=guid("3239eb6f-c7fc-4953-aa15-646829a4ca4c"), event_id=2, version=0)
class Microsoft_Windows_DisplayColorCalibration_2_0(Etw):
    pattern = Struct(
        "Device" / WString
    )


@declare(guid=guid("3239eb6f-c7fc-4953-aa15-646829a4ca4c"), event_id=3, version=0)
class Microsoft_Windows_DisplayColorCalibration_3_0(Etw):
    pattern = Struct(
        "Device" / WString,
        "Profile" / WString
    )


@declare(guid=guid("3239eb6f-c7fc-4953-aa15-646829a4ca4c"), event_id=4, version=0)
class Microsoft_Windows_DisplayColorCalibration_4_0(Etw):
    pattern = Struct(
        "Setting" / WString
    )


@declare(guid=guid("3239eb6f-c7fc-4953-aa15-646829a4ca4c"), event_id=5, version=0)
class Microsoft_Windows_DisplayColorCalibration_5_0(Etw):
    pattern = Struct(
        "Setting" / WString,
        "OldValue" / Int32ul,
        "NewValue" / Int32ul
    )


@declare(guid=guid("3239eb6f-c7fc-4953-aa15-646829a4ca4c"), event_id=6, version=0)
class Microsoft_Windows_DisplayColorCalibration_6_0(Etw):
    pattern = Struct(
        "Setting" / WString,
        "OldValue" / Int32ul,
        "NewValue" / Int32ul,
        "RedLuts" / Int16ul,
        "GreenLuts" / Int16ul,
        "BlueLuts" / Int16ul
    )


@declare(guid=guid("3239eb6f-c7fc-4953-aa15-646829a4ca4c"), event_id=7, version=0)
class Microsoft_Windows_DisplayColorCalibration_7_0(Etw):
    pattern = Struct(
        "Setting" / WString,
        "OldRedGain" / Int32ul,
        "NewRedGain" / Int32ul,
        "OldGreenGain" / Int32ul,
        "NewGreenGain" / Int32ul,
        "OldBlueGain" / Int32ul,
        "NewBlueGain" / Int32ul
    )


@declare(guid=guid("3239eb6f-c7fc-4953-aa15-646829a4ca4c"), event_id=8, version=0)
class Microsoft_Windows_DisplayColorCalibration_8_0(Etw):
    pattern = Struct(
        "Setting" / WString,
        "OldRedGain" / Int32ul,
        "NewRedGain" / Int32ul,
        "OldGreenGain" / Int32ul,
        "NewGreenGain" / Int32ul,
        "OldBlueGain" / Int32ul,
        "NewBlueGain" / Int32ul,
        "RedLuts" / Int16ul,
        "GreenLuts" / Int16ul,
        "BlueLuts" / Int16ul
    )


@declare(guid=guid("3239eb6f-c7fc-4953-aa15-646829a4ca4c"), event_id=100, version=0)
class Microsoft_Windows_DisplayColorCalibration_100_0(Etw):
    pattern = Struct(
        "Message" / WString
    )

