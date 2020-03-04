# -*- coding: utf-8 -*-
"""
Microsoft-Windows-PerfOS
GUID : f82fb576-e941-4956-a2c7-a0cf83f6450a
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("f82fb576-e941-4956-a2c7-a0cf83f6450a"), event_id=1000, version=1)
class Microsoft_Windows_PerfOS_1000_1(Etw):
    pattern = Struct(
        "Win32Error" / Int32ul
    )


@declare(guid=guid("f82fb576-e941-4956-a2c7-a0cf83f6450a"), event_id=2000, version=1)
class Microsoft_Windows_PerfOS_2000_1(Etw):
    pattern = Struct(
        "NTSTATUS" / Int32ul
    )


@declare(guid=guid("f82fb576-e941-4956-a2c7-a0cf83f6450a"), event_id=2001, version=1)
class Microsoft_Windows_PerfOS_2001_1(Etw):
    pattern = Struct(
        "NTSTATUS" / Int32ul
    )


@declare(guid=guid("f82fb576-e941-4956-a2c7-a0cf83f6450a"), event_id=2002, version=0)
class Microsoft_Windows_PerfOS_2002_0(Etw):
    pattern = Struct(
        "NTSTATUS" / Int32ul
    )


@declare(guid=guid("f82fb576-e941-4956-a2c7-a0cf83f6450a"), event_id=2003, version=2)
class Microsoft_Windows_PerfOS_2003_2(Etw):
    pattern = Struct(
        "NTSTATUS" / Int32ul
    )


@declare(guid=guid("f82fb576-e941-4956-a2c7-a0cf83f6450a"), event_id=2004, version=1)
class Microsoft_Windows_PerfOS_2004_1(Etw):
    pattern = Struct(
        "NTSTATUS" / Int32ul
    )


@declare(guid=guid("f82fb576-e941-4956-a2c7-a0cf83f6450a"), event_id=2005, version=1)
class Microsoft_Windows_PerfOS_2005_1(Etw):
    pattern = Struct(
        "NTSTATUS" / Int32ul
    )


@declare(guid=guid("f82fb576-e941-4956-a2c7-a0cf83f6450a"), event_id=2006, version=1)
class Microsoft_Windows_PerfOS_2006_1(Etw):
    pattern = Struct(
        "NTSTATUS" / Int32ul
    )


@declare(guid=guid("f82fb576-e941-4956-a2c7-a0cf83f6450a"), event_id=2008, version=1)
class Microsoft_Windows_PerfOS_2008_1(Etw):
    pattern = Struct(
        "NTSTATUS" / Int32ul
    )


@declare(guid=guid("f82fb576-e941-4956-a2c7-a0cf83f6450a"), event_id=2009, version=1)
class Microsoft_Windows_PerfOS_2009_1(Etw):
    pattern = Struct(
        "NTSTATUS" / Int32ul
    )


@declare(guid=guid("f82fb576-e941-4956-a2c7-a0cf83f6450a"), event_id=2010, version=1)
class Microsoft_Windows_PerfOS_2010_1(Etw):
    pattern = Struct(
        "NTSTATUS" / Int32ul
    )


@declare(guid=guid("f82fb576-e941-4956-a2c7-a0cf83f6450a"), event_id=2011, version=1)
class Microsoft_Windows_PerfOS_2011_1(Etw):
    pattern = Struct(
        "NTSTATUS" / Int32ul
    )


@declare(guid=guid("f82fb576-e941-4956-a2c7-a0cf83f6450a"), event_id=2012, version=1)
class Microsoft_Windows_PerfOS_2012_1(Etw):
    pattern = Struct(
        "NTSTATUS" / Int32ul
    )


@declare(guid=guid("f82fb576-e941-4956-a2c7-a0cf83f6450a"), event_id=2013, version=1)
class Microsoft_Windows_PerfOS_2013_1(Etw):
    pattern = Struct(
        "NTSTATUS" / Int32ul
    )


@declare(guid=guid("f82fb576-e941-4956-a2c7-a0cf83f6450a"), event_id=2014, version=1)
class Microsoft_Windows_PerfOS_2014_1(Etw):
    pattern = Struct(
        "NTSTATUS" / Int32ul
    )


@declare(guid=guid("f82fb576-e941-4956-a2c7-a0cf83f6450a"), event_id=2015, version=1)
class Microsoft_Windows_PerfOS_2015_1(Etw):
    pattern = Struct(
        "NTSTATUS" / Int32ul
    )


@declare(guid=guid("f82fb576-e941-4956-a2c7-a0cf83f6450a"), event_id=2016, version=1)
class Microsoft_Windows_PerfOS_2016_1(Etw):
    pattern = Struct(
        "NTSTATUS" / Int32ul
    )


@declare(guid=guid("f82fb576-e941-4956-a2c7-a0cf83f6450a"), event_id=2017, version=1)
class Microsoft_Windows_PerfOS_2017_1(Etw):
    pattern = Struct(
        "NTSTATUS" / Int32ul
    )


@declare(guid=guid("f82fb576-e941-4956-a2c7-a0cf83f6450a"), event_id=8199, version=1)
class Microsoft_Windows_PerfOS_8199_1(Etw):
    pattern = Struct(
        "NTSTATUS" / Int32ul
    )

