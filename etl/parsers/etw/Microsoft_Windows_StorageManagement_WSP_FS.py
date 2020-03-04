# -*- coding: utf-8 -*-
"""
Microsoft-Windows-StorageManagement-WSP-FS
GUID : 435f8e4b-8cc4-430e-9796-28cae4976576
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("435f8e4b-8cc4-430e-9796-28cae4976576"), event_id=8448, version=0)
class Microsoft_Windows_StorageManagement_WSP_FS_8448_0(Etw):
    pattern = Struct(
        "Parameter1" / WString
    )


@declare(guid=guid("435f8e4b-8cc4-430e-9796-28cae4976576"), event_id=8449, version=0)
class Microsoft_Windows_StorageManagement_WSP_FS_8449_0(Etw):
    pattern = Struct(
        "Parameter1" / WString
    )


@declare(guid=guid("435f8e4b-8cc4-430e-9796-28cae4976576"), event_id=8450, version=0)
class Microsoft_Windows_StorageManagement_WSP_FS_8450_0(Etw):
    pattern = Struct(
        "Parameter1" / WString
    )


@declare(guid=guid("435f8e4b-8cc4-430e-9796-28cae4976576"), event_id=8451, version=0)
class Microsoft_Windows_StorageManagement_WSP_FS_8451_0(Etw):
    pattern = Struct(
        "Parameter1" / WString
    )


@declare(guid=guid("435f8e4b-8cc4-430e-9796-28cae4976576"), event_id=8452, version=0)
class Microsoft_Windows_StorageManagement_WSP_FS_8452_0(Etw):
    pattern = Struct(
        "Parameter1" / WString
    )

