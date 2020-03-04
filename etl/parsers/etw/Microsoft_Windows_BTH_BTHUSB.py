# -*- coding: utf-8 -*-
"""
Microsoft-Windows-BTH-BTHUSB
GUID : 33693e1d-246a-471b-83be-3e75f47a832d
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("33693e1d-246a-471b-83be-3e75f47a832d"), event_id=1, version=0)
class Microsoft_Windows_BTH_BTHUSB_1_0(Etw):
    pattern = Struct(
        "fid_BTHUSB_HC" / Int8sl,
        "fid_BTHUSB_HC_SELECTIVE_SUSPEND" / Int16sl,
        "fid_BTHUSB_HC_Pdo_Name" / WString
    )


@declare(guid=guid("33693e1d-246a-471b-83be-3e75f47a832d"), event_id=2, version=0)
class Microsoft_Windows_BTH_BTHUSB_2_0(Etw):
    pattern = Struct(
        "BIP_Type" / Int8ul,
        "BIP_Length" / Int32ul
    )


@declare(guid=guid("33693e1d-246a-471b-83be-3e75f47a832d"), event_id=3, version=0)
class Microsoft_Windows_BTH_BTHUSB_3_0(Etw):
    pattern = Struct(
        "BIP_Type" / Int8ul,
        "BIP_Length" / Int32ul
    )

