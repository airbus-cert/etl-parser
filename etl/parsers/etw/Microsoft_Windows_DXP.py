# -*- coding: utf-8 -*-
"""
Microsoft-Windows-DXP
GUID : 728b8c72-0f0f-4071-9bcc-27cb3b6dacbe
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("728b8c72-0f0f-4071-9bcc-27cb3b6dacbe"), event_id=1, version=0)
class Microsoft_Windows_DXP_1_0(Etw):
    pattern = Struct(
        "DeviceID" / WString
    )


@declare(guid=guid("728b8c72-0f0f-4071-9bcc-27cb3b6dacbe"), event_id=2, version=0)
class Microsoft_Windows_DXP_2_0(Etw):
    pattern = Struct(
        "DeviceID" / WString
    )


@declare(guid=guid("728b8c72-0f0f-4071-9bcc-27cb3b6dacbe"), event_id=3, version=0)
class Microsoft_Windows_DXP_3_0(Etw):
    pattern = Struct(
        "DeviceID" / WString
    )


@declare(guid=guid("728b8c72-0f0f-4071-9bcc-27cb3b6dacbe"), event_id=4, version=0)
class Microsoft_Windows_DXP_4_0(Etw):
    pattern = Struct(
        "DeviceID" / WString
    )


@declare(guid=guid("728b8c72-0f0f-4071-9bcc-27cb3b6dacbe"), event_id=5, version=0)
class Microsoft_Windows_DXP_5_0(Etw):
    pattern = Struct(
        "FileName" / WString
    )


@declare(guid=guid("728b8c72-0f0f-4071-9bcc-27cb3b6dacbe"), event_id=6, version=0)
class Microsoft_Windows_DXP_6_0(Etw):
    pattern = Struct(
        "FileName" / WString
    )


@declare(guid=guid("728b8c72-0f0f-4071-9bcc-27cb3b6dacbe"), event_id=7, version=0)
class Microsoft_Windows_DXP_7_0(Etw):
    pattern = Struct(
        "DeviceID" / WString
    )


@declare(guid=guid("728b8c72-0f0f-4071-9bcc-27cb3b6dacbe"), event_id=8, version=0)
class Microsoft_Windows_DXP_8_0(Etw):
    pattern = Struct(
        "DeviceID" / WString
    )


@declare(guid=guid("728b8c72-0f0f-4071-9bcc-27cb3b6dacbe"), event_id=11, version=0)
class Microsoft_Windows_DXP_11_0(Etw):
    pattern = Struct(
        "DeviceID" / WString
    )


@declare(guid=guid("728b8c72-0f0f-4071-9bcc-27cb3b6dacbe"), event_id=12, version=0)
class Microsoft_Windows_DXP_12_0(Etw):
    pattern = Struct(
        "DeviceID" / WString
    )


@declare(guid=guid("728b8c72-0f0f-4071-9bcc-27cb3b6dacbe"), event_id=13, version=0)
class Microsoft_Windows_DXP_13_0(Etw):
    pattern = Struct(
        "DeviceID" / WString
    )


@declare(guid=guid("728b8c72-0f0f-4071-9bcc-27cb3b6dacbe"), event_id=14, version=0)
class Microsoft_Windows_DXP_14_0(Etw):
    pattern = Struct(
        "DeviceID" / WString
    )


@declare(guid=guid("728b8c72-0f0f-4071-9bcc-27cb3b6dacbe"), event_id=15, version=0)
class Microsoft_Windows_DXP_15_0(Etw):
    pattern = Struct(
        "DeviceID" / WString
    )


@declare(guid=guid("728b8c72-0f0f-4071-9bcc-27cb3b6dacbe"), event_id=16, version=0)
class Microsoft_Windows_DXP_16_0(Etw):
    pattern = Struct(
        "DeviceID" / WString
    )


@declare(guid=guid("728b8c72-0f0f-4071-9bcc-27cb3b6dacbe"), event_id=18, version=0)
class Microsoft_Windows_DXP_18_0(Etw):
    pattern = Struct(
        "DeviceID" / WString
    )


@declare(guid=guid("728b8c72-0f0f-4071-9bcc-27cb3b6dacbe"), event_id=19, version=0)
class Microsoft_Windows_DXP_19_0(Etw):
    pattern = Struct(
        "DeviceID" / WString
    )


@declare(guid=guid("728b8c72-0f0f-4071-9bcc-27cb3b6dacbe"), event_id=20, version=0)
class Microsoft_Windows_DXP_20_0(Etw):
    pattern = Struct(
        "DeviceID" / WString
    )


@declare(guid=guid("728b8c72-0f0f-4071-9bcc-27cb3b6dacbe"), event_id=28, version=0)
class Microsoft_Windows_DXP_28_0(Etw):
    pattern = Struct(
        "DeviceID" / WString
    )


@declare(guid=guid("728b8c72-0f0f-4071-9bcc-27cb3b6dacbe"), event_id=29, version=0)
class Microsoft_Windows_DXP_29_0(Etw):
    pattern = Struct(
        "DeviceID" / WString
    )


@declare(guid=guid("728b8c72-0f0f-4071-9bcc-27cb3b6dacbe"), event_id=31, version=0)
class Microsoft_Windows_DXP_31_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("728b8c72-0f0f-4071-9bcc-27cb3b6dacbe"), event_id=32, version=0)
class Microsoft_Windows_DXP_32_0(Etw):
    pattern = Struct(
        "Object" / Int64ul
    )


@declare(guid=guid("728b8c72-0f0f-4071-9bcc-27cb3b6dacbe"), event_id=33, version=0)
class Microsoft_Windows_DXP_33_0(Etw):
    pattern = Struct(
        "DeviceID" / WString
    )

