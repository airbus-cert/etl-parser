# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Sysprep
GUID : 75ebc33e-77b8-4ba8-9474-4f4a9db2f5c6
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("75ebc33e-77b8-4ba8-9474-4f4a9db2f5c6"), event_id=1001, version=0)
class Microsoft_Windows_Sysprep_1001_0(Etw):
    pattern = Struct(
        "BasePath" / WString,
        "Phase" / WString
    )


@declare(guid=guid("75ebc33e-77b8-4ba8-9474-4f4a9db2f5c6"), event_id=1002, version=0)
class Microsoft_Windows_Sysprep_1002_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("75ebc33e-77b8-4ba8-9474-4f4a9db2f5c6"), event_id=2001, version=0)
class Microsoft_Windows_Sysprep_2001_0(Etw):
    pattern = Struct(
        "DllName" / WString,
        "FunctionName" / CString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("75ebc33e-77b8-4ba8-9474-4f4a9db2f5c6"), event_id=2002, version=0)
class Microsoft_Windows_Sysprep_2002_0(Etw):
    pattern = Struct(
        "DllName" / WString,
        "FunctionName" / CString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("75ebc33e-77b8-4ba8-9474-4f4a9db2f5c6"), event_id=3001, version=0)
class Microsoft_Windows_Sysprep_3001_0(Etw):
    pattern = Struct(
        "ActionFilePath" / WString
    )


@declare(guid=guid("75ebc33e-77b8-4ba8-9474-4f4a9db2f5c6"), event_id=3002, version=0)
class Microsoft_Windows_Sysprep_3002_0(Etw):
    pattern = Struct(
        "ActionFilePath" / WString
    )


@declare(guid=guid("75ebc33e-77b8-4ba8-9474-4f4a9db2f5c6"), event_id=4001, version=0)
class Microsoft_Windows_Sysprep_4001_0(Etw):
    pattern = Struct(
        "ComponentName" / WString
    )


@declare(guid=guid("75ebc33e-77b8-4ba8-9474-4f4a9db2f5c6"), event_id=4002, version=0)
class Microsoft_Windows_Sysprep_4002_0(Etw):
    pattern = Struct(
        "ComponentName" / WString
    )


@declare(guid=guid("75ebc33e-77b8-4ba8-9474-4f4a9db2f5c6"), event_id=5001, version=0)
class Microsoft_Windows_Sysprep_5001_0(Etw):
    pattern = Struct(
        "DirectoryPath" / WString,
        "FilePattern" / WString
    )


@declare(guid=guid("75ebc33e-77b8-4ba8-9474-4f4a9db2f5c6"), event_id=5002, version=0)
class Microsoft_Windows_Sysprep_5002_0(Etw):
    pattern = Struct(
        "DirectoryPath" / WString,
        "FilePattern" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("75ebc33e-77b8-4ba8-9474-4f4a9db2f5c6"), event_id=6001, version=0)
class Microsoft_Windows_Sysprep_6001_0(Etw):
    pattern = Struct(
        "DirectoryPath" / WString
    )


@declare(guid=guid("75ebc33e-77b8-4ba8-9474-4f4a9db2f5c6"), event_id=6002, version=0)
class Microsoft_Windows_Sysprep_6002_0(Etw):
    pattern = Struct(
        "DirectoryPath" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("75ebc33e-77b8-4ba8-9474-4f4a9db2f5c6"), event_id=7001, version=0)
class Microsoft_Windows_Sysprep_7001_0(Etw):
    pattern = Struct(
        "Phase" / WString
    )


@declare(guid=guid("75ebc33e-77b8-4ba8-9474-4f4a9db2f5c6"), event_id=7002, version=0)
class Microsoft_Windows_Sysprep_7002_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )

