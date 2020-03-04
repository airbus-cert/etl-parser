# -*- coding: utf-8 -*-
"""
Microsoft-Windows-WWAN-NDISUIO-EVENTS
GUID : b3eee223-d0a9-40cd-adfc-50f1888138ab
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("b3eee223-d0a9-40cd-adfc-50f1888138ab"), event_id=1003, version=0)
class Microsoft_Windows_WWAN_NDISUIO_EVENTS_1003_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("b3eee223-d0a9-40cd-adfc-50f1888138ab"), event_id=1004, version=0)
class Microsoft_Windows_WWAN_NDISUIO_EVENTS_1004_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "OIDorStatus" / Int32ul,
        "RequestID" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("b3eee223-d0a9-40cd-adfc-50f1888138ab"), event_id=1005, version=0)
class Microsoft_Windows_WWAN_NDISUIO_EVENTS_1005_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "OIDorStatus" / Int32ul,
        "RequestID" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("b3eee223-d0a9-40cd-adfc-50f1888138ab"), event_id=1006, version=0)
class Microsoft_Windows_WWAN_NDISUIO_EVENTS_1006_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "OIDorStatus" / Int32ul,
        "BufferSize" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )

