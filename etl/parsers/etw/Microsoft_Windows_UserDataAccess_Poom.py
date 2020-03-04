# -*- coding: utf-8 -*-
"""
Microsoft-Windows-UserDataAccess-Poom
GUID : 0bd19909-eb6f-4b16-8074-6dce803f091d
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("0bd19909-eb6f-4b16-8074-6dce803f091d"), event_id=1, version=0)
class Microsoft_Windows_UserDataAccess_Poom_1_0(Etw):
    pattern = Struct(
        "P1_HResult" / Int32sl,
        "P2_String" / CString,
        "P3_UInt32" / Int32ul
    )


@declare(guid=guid("0bd19909-eb6f-4b16-8074-6dce803f091d"), event_id=2, version=0)
class Microsoft_Windows_UserDataAccess_Poom_2_0(Etw):
    pattern = Struct(
        "P1_HResult" / Int32sl,
        "P2_String" / CString,
        "P3_UInt32" / Int32ul
    )


@declare(guid=guid("0bd19909-eb6f-4b16-8074-6dce803f091d"), event_id=1000, version=0)
class Microsoft_Windows_UserDataAccess_Poom_1000_0(Etw):
    pattern = Struct(
        "Message" / Int64ul
    )


@declare(guid=guid("0bd19909-eb6f-4b16-8074-6dce803f091d"), event_id=2000, version=0)
class Microsoft_Windows_UserDataAccess_Poom_2000_0(Etw):
    pattern = Struct(
        "Prop_Process_UnicodeString" / WString,
        "Prop_ErrorCode" / Int32ul
    )


@declare(guid=guid("0bd19909-eb6f-4b16-8074-6dce803f091d"), event_id=2002, version=0)
class Microsoft_Windows_UserDataAccess_Poom_2002_0(Etw):
    pattern = Struct(
        "Prop_Handle" / Int32ul,
        "Prop_HRESULT" / Int32ul,
        "Prop_UINT" / Int32ul
    )


@declare(guid=guid("0bd19909-eb6f-4b16-8074-6dce803f091d"), event_id=2003, version=0)
class Microsoft_Windows_UserDataAccess_Poom_2003_0(Etw):
    pattern = Struct(
        "Prop_Handle" / Int32ul,
        "Prop_HRESULT" / Int32ul
    )


@declare(guid=guid("0bd19909-eb6f-4b16-8074-6dce803f091d"), event_id=2009, version=0)
class Microsoft_Windows_UserDataAccess_Poom_2009_0(Etw):
    pattern = Struct(
        "Prop_UInt32" / Int32ul
    )


@declare(guid=guid("0bd19909-eb6f-4b16-8074-6dce803f091d"), event_id=2010, version=0)
class Microsoft_Windows_UserDataAccess_Poom_2010_0(Etw):
    pattern = Struct(
        "Prop_UInt32" / Int32ul
    )


@declare(guid=guid("0bd19909-eb6f-4b16-8074-6dce803f091d"), event_id=2011, version=0)
class Microsoft_Windows_UserDataAccess_Poom_2011_0(Etw):
    pattern = Struct(
        "Prop_Handle" / Int32ul,
        "Prop_HRESULT" / Int32ul,
        "Prop_UINT" / Int32ul
    )


@declare(guid=guid("0bd19909-eb6f-4b16-8074-6dce803f091d"), event_id=2012, version=0)
class Microsoft_Windows_UserDataAccess_Poom_2012_0(Etw):
    pattern = Struct(
        "Prop_Handle" / Int32ul,
        "Prop_HRESULT" / Int32ul,
        "Prop_UINT" / Int32ul
    )


@declare(guid=guid("0bd19909-eb6f-4b16-8074-6dce803f091d"), event_id=2013, version=0)
class Microsoft_Windows_UserDataAccess_Poom_2013_0(Etw):
    pattern = Struct(
        "Prop_UInt32" / Int32ul
    )


@declare(guid=guid("0bd19909-eb6f-4b16-8074-6dce803f091d"), event_id=2014, version=0)
class Microsoft_Windows_UserDataAccess_Poom_2014_0(Etw):
    pattern = Struct(
        "Prop_HexInt1" / Int32ul,
        "Prop_Bool" / Int8ul,
        "Prop_HexInt2" / Int32ul,
        "Prop_HexInt3" / Int32ul
    )


@declare(guid=guid("0bd19909-eb6f-4b16-8074-6dce803f091d"), event_id=2016, version=0)
class Microsoft_Windows_UserDataAccess_Poom_2016_0(Etw):
    pattern = Struct(
        "P1_UInt32" / Int32ul,
        "P2_String" / WString,
        "P3_UInt32" / Int32ul
    )


@declare(guid=guid("0bd19909-eb6f-4b16-8074-6dce803f091d"), event_id=2017, version=0)
class Microsoft_Windows_UserDataAccess_Poom_2017_0(Etw):
    pattern = Struct(
        "P1_UInt32" / Int32ul,
        "P2_String" / WString,
        "P3_UInt32" / Int32ul,
        "P4_UInt32" / Int32ul
    )


@declare(guid=guid("0bd19909-eb6f-4b16-8074-6dce803f091d"), event_id=2018, version=0)
class Microsoft_Windows_UserDataAccess_Poom_2018_0(Etw):
    pattern = Struct(
        "Prop_UInt32" / Int32ul,
        "Prop_Hex_UInt32" / Int32ul
    )


@declare(guid=guid("0bd19909-eb6f-4b16-8074-6dce803f091d"), event_id=2019, version=0)
class Microsoft_Windows_UserDataAccess_Poom_2019_0(Etw):
    pattern = Struct(
        "P1_HexInt" / Int32ul,
        "P2_UnicodeString" / WString
    )


@declare(guid=guid("0bd19909-eb6f-4b16-8074-6dce803f091d"), event_id=2020, version=0)
class Microsoft_Windows_UserDataAccess_Poom_2020_0(Etw):
    pattern = Struct(
        "Prop_UInt32" / Int32ul
    )


@declare(guid=guid("0bd19909-eb6f-4b16-8074-6dce803f091d"), event_id=2021, version=0)
class Microsoft_Windows_UserDataAccess_Poom_2021_0(Etw):
    pattern = Struct(
        "Prop_UInt32" / Int32ul
    )


@declare(guid=guid("0bd19909-eb6f-4b16-8074-6dce803f091d"), event_id=2022, version=0)
class Microsoft_Windows_UserDataAccess_Poom_2022_0(Etw):
    pattern = Struct(
        "Prop_UInt32" / Int32ul,
        "Prop_Hex_UInt32" / Int32ul
    )


@declare(guid=guid("0bd19909-eb6f-4b16-8074-6dce803f091d"), event_id=5000, version=0)
class Microsoft_Windows_UserDataAccess_Poom_5000_0(Etw):
    pattern = Struct(
        "Prop_CriticalSection_Name" / WString,
        "Prop_TimeHeld" / Int64ul,
        "Prop_ReleaseFunction" / Int32ul
    )


@declare(guid=guid("0bd19909-eb6f-4b16-8074-6dce803f091d"), event_id=5001, version=0)
class Microsoft_Windows_UserDataAccess_Poom_5001_0(Etw):
    pattern = Struct(
        "Prop_UInt32" / Int32ul,
        "Prop_Hex_UInt32" / Int32ul
    )


@declare(guid=guid("0bd19909-eb6f-4b16-8074-6dce803f091d"), event_id=6000, version=0)
class Microsoft_Windows_UserDataAccess_Poom_6000_0(Etw):
    pattern = Struct(
        "P1_UInt32" / Int32ul,
        "P2_UInt32" / Int32ul,
        "P3_UInt32" / Int32ul
    )


@declare(guid=guid("0bd19909-eb6f-4b16-8074-6dce803f091d"), event_id=6001, version=0)
class Microsoft_Windows_UserDataAccess_Poom_6001_0(Etw):
    pattern = Struct(
        "P1_UInt32" / Int32ul,
        "P2_UInt32" / Int32ul,
        "P3_UInt32" / Int32ul
    )


@declare(guid=guid("0bd19909-eb6f-4b16-8074-6dce803f091d"), event_id=6002, version=0)
class Microsoft_Windows_UserDataAccess_Poom_6002_0(Etw):
    pattern = Struct(
        "P1_UInt32" / Int32ul,
        "P2_UInt32" / Int32ul,
        "P3_UInt32" / Int32ul
    )


@declare(guid=guid("0bd19909-eb6f-4b16-8074-6dce803f091d"), event_id=6003, version=0)
class Microsoft_Windows_UserDataAccess_Poom_6003_0(Etw):
    pattern = Struct(
        "P1_UInt32" / Int32ul,
        "P2_UInt32" / Int32ul,
        "P3_UInt32" / Int32ul
    )

