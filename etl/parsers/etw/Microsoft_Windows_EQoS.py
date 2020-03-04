# -*- coding: utf-8 -*-
"""
Microsoft-Windows-EQoS
GUID : 54cb22ff-26b4-4393-a8c2-6b0715912c5f
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("54cb22ff-26b4-4393-a8c2-6b0715912c5f"), event_id=1, version=0)
class Microsoft_Windows_EQoS_1_0(Etw):
    pattern = Struct(
        "PolicyType" / Int32ul
    )


@declare(guid=guid("54cb22ff-26b4-4393-a8c2-6b0715912c5f"), event_id=2, version=0)
class Microsoft_Windows_EQoS_2_0(Etw):
    pattern = Struct(
        "PolicyType" / Int32ul
    )


@declare(guid=guid("54cb22ff-26b4-4393-a8c2-6b0715912c5f"), event_id=4, version=0)
class Microsoft_Windows_EQoS_4_0(Etw):
    pattern = Struct(
        "Level" / Int32ul
    )


@declare(guid=guid("54cb22ff-26b4-4393-a8c2-6b0715912c5f"), event_id=9, version=0)
class Microsoft_Windows_EQoS_9_0(Etw):
    pattern = Struct(
        "Setting" / Int32ul
    )


@declare(guid=guid("54cb22ff-26b4-4393-a8c2-6b0715912c5f"), event_id=13, version=0)
class Microsoft_Windows_EQoS_13_0(Etw):
    pattern = Struct(
        "Hours" / Int32ul,
        "Minutes" / Int32ul,
        "Collisions" / Int32ul
    )


@declare(guid=guid("54cb22ff-26b4-4393-a8c2-6b0715912c5f"), event_id=102, version=0)
class Microsoft_Windows_EQoS_102_0(Etw):
    pattern = Struct(
        "PolicyType" / Int32ul,
        "PolicyName" / WString
    )


@declare(guid=guid("54cb22ff-26b4-4393-a8c2-6b0715912c5f"), event_id=104, version=0)
class Microsoft_Windows_EQoS_104_0(Etw):
    pattern = Struct(
        "PolicyType" / Int32ul,
        "PolicyName" / WString
    )


@declare(guid=guid("54cb22ff-26b4-4393-a8c2-6b0715912c5f"), event_id=108, version=0)
class Microsoft_Windows_EQoS_108_0(Etw):
    pattern = Struct(
        "PolicyType" / Int32ul,
        "PolicyName" / WString
    )


@declare(guid=guid("54cb22ff-26b4-4393-a8c2-6b0715912c5f"), event_id=110, version=0)
class Microsoft_Windows_EQoS_110_0(Etw):
    pattern = Struct(
        "PolicyType" / Int32ul,
        "PolicyName" / WString
    )


@declare(guid=guid("54cb22ff-26b4-4393-a8c2-6b0715912c5f"), event_id=200, version=0)
class Microsoft_Windows_EQoS_200_0(Etw):
    pattern = Struct(
        "PolicyType" / Int32ul,
        "NtStatus" / Int32ul
    )


@declare(guid=guid("54cb22ff-26b4-4393-a8c2-6b0715912c5f"), event_id=204, version=0)
class Microsoft_Windows_EQoS_204_0(Etw):
    pattern = Struct(
        "PolicyType" / Int32ul,
        "Index" / Int32ul
    )


@declare(guid=guid("54cb22ff-26b4-4393-a8c2-6b0715912c5f"), event_id=206, version=0)
class Microsoft_Windows_EQoS_206_0(Etw):
    pattern = Struct(
        "PolicyType" / Int32ul,
        "Index" / Int32ul
    )


@declare(guid=guid("54cb22ff-26b4-4393-a8c2-6b0715912c5f"), event_id=208, version=0)
class Microsoft_Windows_EQoS_208_0(Etw):
    pattern = Struct(
        "PolicyType" / Int32ul,
        "Index" / Int32ul
    )


@declare(guid=guid("54cb22ff-26b4-4393-a8c2-6b0715912c5f"), event_id=210, version=0)
class Microsoft_Windows_EQoS_210_0(Etw):
    pattern = Struct(
        "PolicyType" / Int32ul,
        "PolicyFieldName" / WString,
        "PolicyName" / WString
    )


@declare(guid=guid("54cb22ff-26b4-4393-a8c2-6b0715912c5f"), event_id=212, version=0)
class Microsoft_Windows_EQoS_212_0(Etw):
    pattern = Struct(
        "NtStatus" / Int32ul
    )


@declare(guid=guid("54cb22ff-26b4-4393-a8c2-6b0715912c5f"), event_id=213, version=0)
class Microsoft_Windows_EQoS_213_0(Etw):
    pattern = Struct(
        "NtStatus" / Int32ul
    )

