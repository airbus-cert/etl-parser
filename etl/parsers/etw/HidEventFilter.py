# -*- coding: utf-8 -*-
"""
HidEventFilter
GUID : dde50426-fa77-4088-8e0c-f2f553fb6843
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("dde50426-fa77-4088-8e0c-f2f553fb6843"), event_id=100, version=1)
class HidEventFilter_100_1(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("dde50426-fa77-4088-8e0c-f2f553fb6843"), event_id=101, version=1)
class HidEventFilter_101_1(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("dde50426-fa77-4088-8e0c-f2f553fb6843"), event_id=102, version=1)
class HidEventFilter_102_1(Etw):
    pattern = Struct(
        "Message" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("dde50426-fa77-4088-8e0c-f2f553fb6843"), event_id=103, version=1)
class HidEventFilter_103_1(Etw):
    pattern = Struct(
        "FunctionName" / WString
    )


@declare(guid=guid("dde50426-fa77-4088-8e0c-f2f553fb6843"), event_id=104, version=1)
class HidEventFilter_104_1(Etw):
    pattern = Struct(
        "FunctionName" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("dde50426-fa77-4088-8e0c-f2f553fb6843"), event_id=105, version=1)
class HidEventFilter_105_1(Etw):
    pattern = Struct(
        "Device" / Int64ul,
        "DeviceInit" / Int64ul
    )


@declare(guid=guid("dde50426-fa77-4088-8e0c-f2f553fb6843"), event_id=106, version=1)
class HidEventFilter_106_1(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("dde50426-fa77-4088-8e0c-f2f553fb6843"), event_id=107, version=1)
class HidEventFilter_107_1(Etw):
    pattern = Struct(
        "Device" / Int64ul,
        "PreviousState" / Int32ul
    )


@declare(guid=guid("dde50426-fa77-4088-8e0c-f2f553fb6843"), event_id=108, version=1)
class HidEventFilter_108_1(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("dde50426-fa77-4088-8e0c-f2f553fb6843"), event_id=109, version=1)
class HidEventFilter_109_1(Etw):
    pattern = Struct(
        "WDFDEVICE" / Int64ul,
        "TargetState" / Int32ul
    )


@declare(guid=guid("dde50426-fa77-4088-8e0c-f2f553fb6843"), event_id=110, version=1)
class HidEventFilter_110_1(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("dde50426-fa77-4088-8e0c-f2f553fb6843"), event_id=111, version=1)
class HidEventFilter_111_1(Etw):
    pattern = Struct(
        "Message" / WString,
        "FeatureDataValue" / Int32ul
    )


@declare(guid=guid("dde50426-fa77-4088-8e0c-f2f553fb6843"), event_id=115, version=1)
class HidEventFilter_115_1(Etw):
    pattern = Struct(
        "Message" / WString,
        "AcpiNotificationValue" / Int32ul
    )


@declare(guid=guid("dde50426-fa77-4088-8e0c-f2f553fb6843"), event_id=117, version=1)
class HidEventFilter_117_1(Etw):
    pattern = Struct(
        "Message" / WString,
        "IndicatorsStatus" / Int32ul
    )


@declare(guid=guid("dde50426-fa77-4088-8e0c-f2f553fb6843"), event_id=127, version=1)
class HidEventFilter_127_1(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "Queue" / Int64ul,
        "OutputBufferLength" / Int64ul,
        "InputBufferLength" / Int64ul,
        "IOCTL" / Int64ul
    )


@declare(guid=guid("dde50426-fa77-4088-8e0c-f2f553fb6843"), event_id=128, version=1)
class HidEventFilter_128_1(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "Status" / Int32ul
    )

