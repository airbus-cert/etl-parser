# -*- coding: utf-8 -*-
"""
Microsoft-Windows-LimitsManagement
GUID : 73aa0094-facb-4aeb-bd1d-a7b98dd5c799
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("73aa0094-facb-4aeb-bd1d-a7b98dd5c799"), event_id=1, version=0)
class Microsoft_Windows_LimitsManagement_1_0(Etw):
    pattern = Struct(
        "Token" / Int64ul,
        "Type" / Int32ul,
        "LowerThreshold" / Int32ul,
        "UpperThreshold" / Int32ul,
        "Value" / Int32ul,
        "Mitigating" / Int8ul,
        "Name" / WString
    )


@declare(guid=guid("73aa0094-facb-4aeb-bd1d-a7b98dd5c799"), event_id=2, version=0)
class Microsoft_Windows_LimitsManagement_2_0(Etw):
    pattern = Struct(
        "Token" / Int64ul,
        "Type" / Int32ul,
        "LowerThreshold" / Int32ul,
        "UpperThreshold" / Int32ul,
        "Value" / Int32ul,
        "Mitigating" / Int8ul,
        "Name" / WString
    )


@declare(guid=guid("73aa0094-facb-4aeb-bd1d-a7b98dd5c799"), event_id=3, version=0)
class Microsoft_Windows_LimitsManagement_3_0(Etw):
    pattern = Struct(
        "Token" / Int64ul,
        "Value" / Int32ul
    )


@declare(guid=guid("73aa0094-facb-4aeb-bd1d-a7b98dd5c799"), event_id=4, version=0)
class Microsoft_Windows_LimitsManagement_4_0(Etw):
    pattern = Struct(
        "Token" / Int64ul,
        "Mitigating" / Int8ul
    )


@declare(guid=guid("73aa0094-facb-4aeb-bd1d-a7b98dd5c799"), event_id=5, version=0)
class Microsoft_Windows_LimitsManagement_5_0(Etw):
    pattern = Struct(
        "Token" / Int64ul,
        "LowerThreshold" / Int32ul,
        "UpperThreshold" / Int32ul
    )


@declare(guid=guid("73aa0094-facb-4aeb-bd1d-a7b98dd5c799"), event_id=6, version=0)
class Microsoft_Windows_LimitsManagement_6_0(Etw):
    pattern = Struct(
        "Token" / Int64ul
    )


@declare(guid=guid("73aa0094-facb-4aeb-bd1d-a7b98dd5c799"), event_id=7, version=0)
class Microsoft_Windows_LimitsManagement_7_0(Etw):
    pattern = Struct(
        "Event" / Int32ul,
        "Type" / Int32ul,
        "LowerThreshold" / Int32ul,
        "UpperThreshold" / Int32ul,
        "Value" / Int32ul,
        "Initiator" / WString
    )


@declare(guid=guid("73aa0094-facb-4aeb-bd1d-a7b98dd5c799"), event_id=8, version=0)
class Microsoft_Windows_LimitsManagement_8_0(Etw):
    pattern = Struct(
        "Token" / Int64ul,
        "Name" / WString,
        "Parameters" / WString
    )


@declare(guid=guid("73aa0094-facb-4aeb-bd1d-a7b98dd5c799"), event_id=9, version=0)
class Microsoft_Windows_LimitsManagement_9_0(Etw):
    pattern = Struct(
        "Token" / Int64ul,
        "Name" / WString,
        "Parameters" / WString
    )


@declare(guid=guid("73aa0094-facb-4aeb-bd1d-a7b98dd5c799"), event_id=10, version=0)
class Microsoft_Windows_LimitsManagement_10_0(Etw):
    pattern = Struct(
        "Token" / Int64ul
    )


@declare(guid=guid("73aa0094-facb-4aeb-bd1d-a7b98dd5c799"), event_id=11, version=0)
class Microsoft_Windows_LimitsManagement_11_0(Etw):
    pattern = Struct(
        "Token" / Int64ul,
        "Type" / Int32ul,
        "DisengagedValue" / Int32ul,
        "FullyEngagedValue" / Int32ul,
        "Value" / Int32ul,
        "Name" / WString
    )


@declare(guid=guid("73aa0094-facb-4aeb-bd1d-a7b98dd5c799"), event_id=12, version=0)
class Microsoft_Windows_LimitsManagement_12_0(Etw):
    pattern = Struct(
        "Token" / Int64ul,
        "Type" / Int32ul,
        "DisengagedValue" / Int32ul,
        "FullyEngagedValue" / Int32ul,
        "Value" / Int32ul,
        "Name" / WString
    )


@declare(guid=guid("73aa0094-facb-4aeb-bd1d-a7b98dd5c799"), event_id=13, version=0)
class Microsoft_Windows_LimitsManagement_13_0(Etw):
    pattern = Struct(
        "Token" / Int64ul,
        "Value" / Int32ul
    )


@declare(guid=guid("73aa0094-facb-4aeb-bd1d-a7b98dd5c799"), event_id=14, version=0)
class Microsoft_Windows_LimitsManagement_14_0(Etw):
    pattern = Struct(
        "Token" / Int64ul
    )

