# -*- coding: utf-8 -*-
"""
Microsoft-Windows-ApplicationExperienceInfrastructure
GUID : 5ec13d8e-4b3f-422e-a7e7-3121a1d90c7a
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("5ec13d8e-4b3f-422e-a7e7-3121a1d90c7a"), event_id=1, version=0)
class Microsoft_Windows_ApplicationExperienceInfrastructure_1_0(Etw):
    pattern = Struct(
        "DBType" / Int32ul,
        "AppNameCount" / Int32ul,
        "AppName" / Bytes(lambda this: this.AppNameCount),
        "VendorNameCount" / Int32ul,
        "VendorName" / Bytes(lambda this: this.VendorNameCount),
        "SummaryCount" / Int32ul,
        "Summary" / Bytes(lambda this: this.SummaryCount),
        "SessionID" / Int32ul
    )


@declare(guid=guid("5ec13d8e-4b3f-422e-a7e7-3121a1d90c7a"), event_id=2, version=0)
class Microsoft_Windows_ApplicationExperienceInfrastructure_2_0(Etw):
    pattern = Struct(
        "DBType" / Int32ul,
        "AppNameCount" / Int32ul,
        "AppName" / Bytes(lambda this: this.AppNameCount),
        "VendorNameCount" / Int32ul,
        "VendorName" / Bytes(lambda this: this.VendorNameCount),
        "SummaryCount" / Int32ul,
        "Summary" / Bytes(lambda this: this.SummaryCount),
        "SessionID" / Int32ul
    )


@declare(guid=guid("5ec13d8e-4b3f-422e-a7e7-3121a1d90c7a"), event_id=3, version=0)
class Microsoft_Windows_ApplicationExperienceInfrastructure_3_0(Etw):
    pattern = Struct(
        "DBType" / Int32ul,
        "AppNameCount" / Int32ul,
        "AppName" / Bytes(lambda this: this.AppNameCount),
        "VendorNameCount" / Int32ul,
        "VendorName" / Bytes(lambda this: this.VendorNameCount),
        "SummaryCount" / Int32ul,
        "Summary" / Bytes(lambda this: this.SummaryCount),
        "SessionID" / Int32ul
    )

