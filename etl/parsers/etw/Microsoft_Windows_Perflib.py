# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Perflib
GUID : 13b197bd-7cee-4b4e-8dd0-59314ce374ce
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("13b197bd-7cee-4b4e-8dd0-59314ce374ce"), event_id=1000, version=0)
class Microsoft_Windows_Perflib_1000_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("13b197bd-7cee-4b4e-8dd0-59314ce374ce"), event_id=1000, version=1)
class Microsoft_Windows_Perflib_1000_1(Etw):
    pattern = Struct(
        "User" / WString,
        "Module" / WString
    )


@declare(guid=guid("13b197bd-7cee-4b4e-8dd0-59314ce374ce"), event_id=1001, version=0)
class Microsoft_Windows_Perflib_1001_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("13b197bd-7cee-4b4e-8dd0-59314ce374ce"), event_id=1001, version=1)
class Microsoft_Windows_Perflib_1001_1(Etw):
    pattern = Struct(
        "Library" / WString,
        "Service" / WString,
        "Size" / Int32ul
    )


@declare(guid=guid("13b197bd-7cee-4b4e-8dd0-59314ce374ce"), event_id=1002, version=0)
class Microsoft_Windows_Perflib_1002_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("13b197bd-7cee-4b4e-8dd0-59314ce374ce"), event_id=1002, version=1)
class Microsoft_Windows_Perflib_1002_1(Etw):
    pattern = Struct(
        "Library" / WString,
        "Service" / WString
    )


@declare(guid=guid("13b197bd-7cee-4b4e-8dd0-59314ce374ce"), event_id=1003, version=0)
class Microsoft_Windows_Perflib_1003_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("13b197bd-7cee-4b4e-8dd0-59314ce374ce"), event_id=1003, version=1)
class Microsoft_Windows_Perflib_1003_1(Etw):
    pattern = Struct(
        "Library" / WString,
        "Service" / WString,
        "ObjectCount" / Int32ul
    )


@declare(guid=guid("13b197bd-7cee-4b4e-8dd0-59314ce374ce"), event_id=1004, version=0)
class Microsoft_Windows_Perflib_1004_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("13b197bd-7cee-4b4e-8dd0-59314ce374ce"), event_id=1004, version=1)
class Microsoft_Windows_Perflib_1004_1(Etw):
    pattern = Struct(
        "Library" / WString,
        "Service" / WString,
        "ObjectIndex" / Int32ul
    )


@declare(guid=guid("13b197bd-7cee-4b4e-8dd0-59314ce374ce"), event_id=1005, version=0)
class Microsoft_Windows_Perflib_1005_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("13b197bd-7cee-4b4e-8dd0-59314ce374ce"), event_id=1005, version=1)
class Microsoft_Windows_Perflib_1005_1(Etw):
    pattern = Struct(
        "ProcName" / CString,
        "Library" / WString,
        "Service" / WString,
        "Win32Error" / Int32ul
    )


@declare(guid=guid("13b197bd-7cee-4b4e-8dd0-59314ce374ce"), event_id=1006, version=0)
class Microsoft_Windows_Perflib_1006_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("13b197bd-7cee-4b4e-8dd0-59314ce374ce"), event_id=1006, version=1)
class Microsoft_Windows_Perflib_1006_1(Etw):
    pattern = Struct(
        "ProcName" / CString,
        "Library" / WString,
        "Service" / WString,
        "Win32Error" / Int32ul
    )


@declare(guid=guid("13b197bd-7cee-4b4e-8dd0-59314ce374ce"), event_id=1007, version=0)
class Microsoft_Windows_Perflib_1007_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("13b197bd-7cee-4b4e-8dd0-59314ce374ce"), event_id=1007, version=1)
class Microsoft_Windows_Perflib_1007_1(Etw):
    pattern = Struct(
        "ProcName" / CString,
        "Library" / WString,
        "Service" / WString,
        "Win32Error" / Int32ul
    )


@declare(guid=guid("13b197bd-7cee-4b4e-8dd0-59314ce374ce"), event_id=1008, version=0)
class Microsoft_Windows_Perflib_1008_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("13b197bd-7cee-4b4e-8dd0-59314ce374ce"), event_id=1008, version=1)
class Microsoft_Windows_Perflib_1008_1(Etw):
    pattern = Struct(
        "Service" / WString,
        "Library" / WString,
        "Win32Error" / Int32ul
    )


@declare(guid=guid("13b197bd-7cee-4b4e-8dd0-59314ce374ce"), event_id=1009, version=0)
class Microsoft_Windows_Perflib_1009_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("13b197bd-7cee-4b4e-8dd0-59314ce374ce"), event_id=1009, version=1)
class Microsoft_Windows_Perflib_1009_1(Etw):
    pattern = Struct(
        "Library" / WString,
        "Service" / WString,
        "ExceptionCode" / Int32ul,
        "ExceptionAddress" / Int64ul
    )


@declare(guid=guid("13b197bd-7cee-4b4e-8dd0-59314ce374ce"), event_id=1010, version=0)
class Microsoft_Windows_Perflib_1010_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("13b197bd-7cee-4b4e-8dd0-59314ce374ce"), event_id=1010, version=1)
class Microsoft_Windows_Perflib_1010_1(Etw):
    pattern = Struct(
        "Library" / WString,
        "Service" / WString,
        "ExceptionCode" / Int32ul,
        "ExceptionAddress" / Int64ul
    )


@declare(guid=guid("13b197bd-7cee-4b4e-8dd0-59314ce374ce"), event_id=1011, version=0)
class Microsoft_Windows_Perflib_1011_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("13b197bd-7cee-4b4e-8dd0-59314ce374ce"), event_id=1011, version=1)
class Microsoft_Windows_Perflib_1011_1(Etw):
    pattern = Struct(
        "Library" / WString,
        "Service" / WString,
        "ExceptionCode" / Int32ul,
        "ExceptionAddress" / Int64ul
    )


@declare(guid=guid("13b197bd-7cee-4b4e-8dd0-59314ce374ce"), event_id=1013, version=0)
class Microsoft_Windows_Perflib_1013_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("13b197bd-7cee-4b4e-8dd0-59314ce374ce"), event_id=1013, version=1)
class Microsoft_Windows_Perflib_1013_1(Etw):
    pattern = Struct(
        "Library" / WString,
        "Service" / WString,
        "Size" / Int32ul
    )


@declare(guid=guid("13b197bd-7cee-4b4e-8dd0-59314ce374ce"), event_id=1014, version=1)
class Microsoft_Windows_Perflib_1014_1(Etw):
    pattern = Struct(
        "Service" / WString,
        "Library" / WString,
        "Win32Error" / Int32ul
    )


@declare(guid=guid("13b197bd-7cee-4b4e-8dd0-59314ce374ce"), event_id=1015, version=0)
class Microsoft_Windows_Perflib_1015_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("13b197bd-7cee-4b4e-8dd0-59314ce374ce"), event_id=1015, version=1)
class Microsoft_Windows_Perflib_1015_1(Etw):
    pattern = Struct(
        "Service" / WString,
        "Library" / WString
    )


@declare(guid=guid("13b197bd-7cee-4b4e-8dd0-59314ce374ce"), event_id=1016, version=0)
class Microsoft_Windows_Perflib_1016_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("13b197bd-7cee-4b4e-8dd0-59314ce374ce"), event_id=1016, version=1)
class Microsoft_Windows_Perflib_1016_1(Etw):
    pattern = Struct(
        "Library" / WString,
        "Service" / WString,
        "Buffer" / Int64ul,
        "BytesLeft" / Int32ul
    )


@declare(guid=guid("13b197bd-7cee-4b4e-8dd0-59314ce374ce"), event_id=1017, version=0)
class Microsoft_Windows_Perflib_1017_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("13b197bd-7cee-4b4e-8dd0-59314ce374ce"), event_id=1017, version=1)
class Microsoft_Windows_Perflib_1017_1(Etw):
    pattern = Struct(
        "Service" / WString
    )


@declare(guid=guid("13b197bd-7cee-4b4e-8dd0-59314ce374ce"), event_id=1018, version=0)
class Microsoft_Windows_Perflib_1018_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("13b197bd-7cee-4b4e-8dd0-59314ce374ce"), event_id=1018, version=1)
class Microsoft_Windows_Perflib_1018_1(Etw):
    pattern = Struct(
        "Service" / WString
    )


@declare(guid=guid("13b197bd-7cee-4b4e-8dd0-59314ce374ce"), event_id=1019, version=0)
class Microsoft_Windows_Perflib_1019_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("13b197bd-7cee-4b4e-8dd0-59314ce374ce"), event_id=1019, version=1)
class Microsoft_Windows_Perflib_1019_1(Etw):
    pattern = Struct(
        "Library" / WString,
        "Service" / WString,
        "ObjectIndex" / Int32ul
    )


@declare(guid=guid("13b197bd-7cee-4b4e-8dd0-59314ce374ce"), event_id=1020, version=0)
class Microsoft_Windows_Perflib_1020_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("13b197bd-7cee-4b4e-8dd0-59314ce374ce"), event_id=1020, version=1)
class Microsoft_Windows_Perflib_1020_1(Etw):
    pattern = Struct(
        "Library" / WString,
        "Service" / WString,
        "BufferSize" / Int32ul,
        "RequiredSize" / Int32ul
    )


@declare(guid=guid("13b197bd-7cee-4b4e-8dd0-59314ce374ce"), event_id=1021, version=0)
class Microsoft_Windows_Perflib_1021_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("13b197bd-7cee-4b4e-8dd0-59314ce374ce"), event_id=1021, version=1)
class Microsoft_Windows_Perflib_1021_1(Etw):
    pattern = Struct(
        "Library" / WString,
        "Win32Error" / Int32ul
    )


@declare(guid=guid("13b197bd-7cee-4b4e-8dd0-59314ce374ce"), event_id=1022, version=0)
class Microsoft_Windows_Perflib_1022_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("13b197bd-7cee-4b4e-8dd0-59314ce374ce"), event_id=1022, version=1)
class Microsoft_Windows_Perflib_1022_1(Etw):
    pattern = Struct(
        "Library" / WString,
        "Win32Error" / Int32ul
    )


@declare(guid=guid("13b197bd-7cee-4b4e-8dd0-59314ce374ce"), event_id=1023, version=0)
class Microsoft_Windows_Perflib_1023_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("13b197bd-7cee-4b4e-8dd0-59314ce374ce"), event_id=1023, version=1)
class Microsoft_Windows_Perflib_1023_1(Etw):
    pattern = Struct(
        "Library" / WString,
        "Win32Error" / Int32ul
    )


@declare(guid=guid("13b197bd-7cee-4b4e-8dd0-59314ce374ce"), event_id=2000, version=0)
class Microsoft_Windows_Perflib_2000_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("13b197bd-7cee-4b4e-8dd0-59314ce374ce"), event_id=2000, version=1)
class Microsoft_Windows_Perflib_2000_1(Etw):
    pattern = Struct(
        "Library" / WString,
        "Service" / WString,
        "BytesLeft" / Int32ul,
        "BytesAvailable" / Int32ul
    )


@declare(guid=guid("13b197bd-7cee-4b4e-8dd0-59314ce374ce"), event_id=2001, version=0)
class Microsoft_Windows_Perflib_2001_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("13b197bd-7cee-4b4e-8dd0-59314ce374ce"), event_id=2001, version=1)
class Microsoft_Windows_Perflib_2001_1(Etw):
    pattern = Struct(
        "Service" / WString,
        "Win32Error" / Int32ul,
        "NTSTATUS" / Int32ul
    )


@declare(guid=guid("13b197bd-7cee-4b4e-8dd0-59314ce374ce"), event_id=2002, version=0)
class Microsoft_Windows_Perflib_2002_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("13b197bd-7cee-4b4e-8dd0-59314ce374ce"), event_id=2002, version=1)
class Microsoft_Windows_Perflib_2002_1(Etw):
    pattern = Struct(
        "Service" / WString,
        "Library" / WString
    )


@declare(guid=guid("13b197bd-7cee-4b4e-8dd0-59314ce374ce"), event_id=2003, version=0)
class Microsoft_Windows_Perflib_2003_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("13b197bd-7cee-4b4e-8dd0-59314ce374ce"), event_id=2003, version=1)
class Microsoft_Windows_Perflib_2003_1(Etw):
    pattern = Struct(
        "Library" / WString,
        "Service" / WString
    )


@declare(guid=guid("13b197bd-7cee-4b4e-8dd0-59314ce374ce"), event_id=3003, version=0)
class Microsoft_Windows_Perflib_3003_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("13b197bd-7cee-4b4e-8dd0-59314ce374ce"), event_id=3003, version=1)
class Microsoft_Windows_Perflib_3003_1(Etw):
    pattern = Struct(
        "ProcName" / CString,
        "Service" / WString
    )

