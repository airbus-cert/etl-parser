# -*- coding: utf-8 -*-
"""
Microsoft-User Experience Virtualization-SQM Uploader
GUID : 57003e21-269b-4bdc-8434-b3bf8d57d2d5
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("57003e21-269b-4bdc-8434-b3bf8d57d2d5"), event_id=3, version=0)
class Microsoft_User_Experience_Virtualization_SQM_Uploader_3_0(Etw):
    pattern = Struct(
        "hresult" / Int32ul
    )


@declare(guid=guid("57003e21-269b-4bdc-8434-b3bf8d57d2d5"), event_id=4, version=0)
class Microsoft_User_Experience_Virtualization_SQM_Uploader_4_0(Etw):
    pattern = Struct(
        "WString1" / WString
    )


@declare(guid=guid("57003e21-269b-4bdc-8434-b3bf8d57d2d5"), event_id=6, version=0)
class Microsoft_User_Experience_Virtualization_SQM_Uploader_6_0(Etw):
    pattern = Struct(
        "hr" / Int32ul,
        "filename" / WString,
        "http" / Int32sl
    )


@declare(guid=guid("57003e21-269b-4bdc-8434-b3bf8d57d2d5"), event_id=7, version=0)
class Microsoft_User_Experience_Virtualization_SQM_Uploader_7_0(Etw):
    pattern = Struct(
        "hr" / Int32ul,
        "filename" / WString,
        "http" / Int32sl
    )


@declare(guid=guid("57003e21-269b-4bdc-8434-b3bf8d57d2d5"), event_id=8, version=0)
class Microsoft_User_Experience_Virtualization_SQM_Uploader_8_0(Etw):
    pattern = Struct(
        "error" / Int32ul
    )


@declare(guid=guid("57003e21-269b-4bdc-8434-b3bf8d57d2d5"), event_id=10, version=0)
class Microsoft_User_Experience_Virtualization_SQM_Uploader_10_0(Etw):
    pattern = Struct(
        "String1" / CString
    )


@declare(guid=guid("57003e21-269b-4bdc-8434-b3bf8d57d2d5"), event_id=12, version=0)
class Microsoft_User_Experience_Virtualization_SQM_Uploader_12_0(Etw):
    pattern = Struct(
        "uint32" / Int32ul
    )


@declare(guid=guid("57003e21-269b-4bdc-8434-b3bf8d57d2d5"), event_id=13, version=0)
class Microsoft_User_Experience_Virtualization_SQM_Uploader_13_0(Etw):
    pattern = Struct(
        "WString1" / WString
    )


@declare(guid=guid("57003e21-269b-4bdc-8434-b3bf8d57d2d5"), event_id=14, version=0)
class Microsoft_User_Experience_Virtualization_SQM_Uploader_14_0(Etw):
    pattern = Struct(
        "error" / Int32ul
    )

