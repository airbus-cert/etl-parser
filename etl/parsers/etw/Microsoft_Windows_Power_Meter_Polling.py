# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Power-Meter-Polling
GUID : 306c4e0b-e148-543d-315b-c618eb93157c
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("306c4e0b-e148-543d-315b-c618eb93157c"), event_id=1, version=0)
class Microsoft_Windows_Power_Meter_Polling_1_0(Etw):
    pattern = Struct(
        "MeterId" / Int64ul,
        "DefaultSamplingPeriodInMs" / Int64ul,
        "MeterNameLength" / Int32ul,
        "MeterName" / Bytes(lambda this: this.MeterNameLength),
        "MeteredHardwareCount" / Int32ul,
        "MeteredHardwareName" / WString
    )


@declare(guid=guid("306c4e0b-e148-543d-315b-c618eb93157c"), event_id=2, version=0)
class Microsoft_Windows_Power_Meter_Polling_2_0(Etw):
    pattern = Struct(
        "MeterId" / Int64ul,
        "DefaultSamplingPeriodInMs" / Int64ul,
        "ChannelNameLength" / Int32ul,
        "ChannelName" / Bytes(lambda this: this.ChannelNameLength)
    )


@declare(guid=guid("306c4e0b-e148-543d-315b-c618eb93157c"), event_id=3, version=0)
class Microsoft_Windows_Power_Meter_Polling_3_0(Etw):
    pattern = Struct(
        "MeterId" / Int64ul,
        "Value" / Int32ul
    )


@declare(guid=guid("306c4e0b-e148-543d-315b-c618eb93157c"), event_id=4, version=0)
class Microsoft_Windows_Power_Meter_Polling_4_0(Etw):
    pattern = Struct(
        "MeterId" / Int64ul,
        "AbsoluteEnergy" / Int64ul,
        "AbsoluteTime" / Int64ul
    )


@declare(guid=guid("306c4e0b-e148-543d-315b-c618eb93157c"), event_id=5, version=0)
class Microsoft_Windows_Power_Meter_Polling_5_0(Etw):
    pattern = Struct(
        "MeterType" / Int32ul,
        "PeriodInMs" / Int32ul
    )


@declare(guid=guid("306c4e0b-e148-543d-315b-c618eb93157c"), event_id=6, version=0)
class Microsoft_Windows_Power_Meter_Polling_6_0(Etw):
    pattern = Struct(
        "MeterType" / Int32ul,
        "PeriodInMs" / Int32ul
    )

