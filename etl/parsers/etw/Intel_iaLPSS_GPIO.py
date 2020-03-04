# -*- coding: utf-8 -*-
"""
Intel-iaLPSS-GPIO
GUID : d386cc7a-620a-41c1-abf5-55018c6c699a
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("d386cc7a-620a-41c1-abf5-55018c6c699a"), event_id=1001, version=1)
class Intel_iaLPSS_GPIO_1001_1(Etw):
    pattern = Struct(
        "WDFDEVICE" / Int64ul
    )


@declare(guid=guid("d386cc7a-620a-41c1-abf5-55018c6c699a"), event_id=1002, version=1)
class Intel_iaLPSS_GPIO_1002_1(Etw):
    pattern = Struct(
        "FxDevice" / Int64ul,
        "IOAddr" / Int64ul,
        "IOLen" / Int32ul
    )


@declare(guid=guid("d386cc7a-620a-41c1-abf5-55018c6c699a"), event_id=1003, version=1)
class Intel_iaLPSS_GPIO_1003_1(Etw):
    pattern = Struct(
        "FailReason" / WString,
        "Status" / Int32ul,
        "WDFDEVICE" / Int64ul
    )


@declare(guid=guid("d386cc7a-620a-41c1-abf5-55018c6c699a"), event_id=1004, version=1)
class Intel_iaLPSS_GPIO_1004_1(Etw):
    pattern = Struct(
        "WDFDEVICE" / Int64ul
    )


@declare(guid=guid("d386cc7a-620a-41c1-abf5-55018c6c699a"), event_id=1040, version=1)
class Intel_iaLPSS_GPIO_1040_1(Etw):
    pattern = Struct(
        "WDFDEVICE" / Int64ul
    )


@declare(guid=guid("d386cc7a-620a-41c1-abf5-55018c6c699a"), event_id=1041, version=1)
class Intel_iaLPSS_GPIO_1041_1(Etw):
    pattern = Struct(
        "WDFDEVICE" / Int64ul
    )


@declare(guid=guid("d386cc7a-620a-41c1-abf5-55018c6c699a"), event_id=1045, version=1)
class Intel_iaLPSS_GPIO_1045_1(Etw):
    pattern = Struct(
        "BankId" / Int32ul,
        "PinCount" / Int16ul,
        "ConnectMode" / Int32ul,
        "PullConfig" / Int32ul
    )


@declare(guid=guid("d386cc7a-620a-41c1-abf5-55018c6c699a"), event_id=1046, version=1)
class Intel_iaLPSS_GPIO_1046_1(Etw):
    pattern = Struct(
        "BankId" / Int32ul,
        "PinCount" / Int32ul,
        "DisconnectMode" / Int32ul
    )


@declare(guid=guid("d386cc7a-620a-41c1-abf5-55018c6c699a"), event_id=1048, version=0)
class Intel_iaLPSS_GPIO_1048_0(Etw):
    pattern = Struct(
        "BankID" / Int32ul,
        "PinValues" / Int32ul
    )


@declare(guid=guid("d386cc7a-620a-41c1-abf5-55018c6c699a"), event_id=1049, version=0)
class Intel_iaLPSS_GPIO_1049_0(Etw):
    pattern = Struct(
        "BankID" / Int32ul,
        "SetValue" / Int64ul,
        "ClearValue" / Int64ul
    )

