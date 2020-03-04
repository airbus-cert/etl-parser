# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Bluetooth-Policy
GUID : 0602ecef-6381-4bc0-aeda-eb9bb919b276
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("0602ecef-6381-4bc0-aeda-eb9bb919b276"), event_id=1, version=0)
class Microsoft_Windows_Bluetooth_Policy_1_0(Etw):
    pattern = Struct(
        "PolicyPath" / WString,
        "PolicyName" / WString,
        "PolicyValue" / WString
    )


@declare(guid=guid("0602ecef-6381-4bc0-aeda-eb9bb919b276"), event_id=2, version=0)
class Microsoft_Windows_Bluetooth_Policy_2_0(Etw):
    pattern = Struct(
        "PolicyPath" / WString,
        "PolicyName" / WString,
        "PolicyState" / WString
    )


@declare(guid=guid("0602ecef-6381-4bc0-aeda-eb9bb919b276"), event_id=3, version=0)
class Microsoft_Windows_Bluetooth_Policy_3_0(Etw):
    pattern = Struct(
        "PolicyPath" / WString,
        "PolicyName" / WString,
        "PolicyState" / WString
    )


@declare(guid=guid("0602ecef-6381-4bc0-aeda-eb9bb919b276"), event_id=4, version=0)
class Microsoft_Windows_Bluetooth_Policy_4_0(Etw):
    pattern = Struct(
        "PolicyPath" / WString,
        "PolicyName" / WString,
        "PolicyState" / WString
    )


@declare(guid=guid("0602ecef-6381-4bc0-aeda-eb9bb919b276"), event_id=5, version=0)
class Microsoft_Windows_Bluetooth_Policy_5_0(Etw):
    pattern = Struct(
        "PolicyPath" / WString,
        "PolicyName" / WString,
        "PolicyState" / WString,
        "RadioName" / WString
    )


@declare(guid=guid("0602ecef-6381-4bc0-aeda-eb9bb919b276"), event_id=6, version=0)
class Microsoft_Windows_Bluetooth_Policy_6_0(Etw):
    pattern = Struct(
        "BtAddr" / Int64ul,
        "Service" / WString
    )


@declare(guid=guid("0602ecef-6381-4bc0-aeda-eb9bb919b276"), event_id=7, version=0)
class Microsoft_Windows_Bluetooth_Policy_7_0(Etw):
    pattern = Struct(
        "Accepted" / WString,
        "ServiceGuid" / Guid,
        "BtAddr" / Int64ul,
        "PolicyPath" / WString,
        "PolicyName" / WString
    )


@declare(guid=guid("0602ecef-6381-4bc0-aeda-eb9bb919b276"), event_id=8, version=0)
class Microsoft_Windows_Bluetooth_Policy_8_0(Etw):
    pattern = Struct(
        "Accepted" / WString,
        "Psm" / Int16sl,
        "BtAddr" / Int64ul,
        "PolicyPath" / WString,
        "PolicyName" / WString
    )


@declare(guid=guid("0602ecef-6381-4bc0-aeda-eb9bb919b276"), event_id=9, version=0)
class Microsoft_Windows_Bluetooth_Policy_9_0(Etw):
    pattern = Struct(
        "bthAddr" / Int64ul
    )


@declare(guid=guid("0602ecef-6381-4bc0-aeda-eb9bb919b276"), event_id=10, version=0)
class Microsoft_Windows_Bluetooth_Policy_10_0(Etw):
    pattern = Struct(
        "bthAddr" / Int64ul
    )

