# -*- coding: utf-8 -*-
"""
Microsoft-Windows-CorruptedFileRecovery-Server
GUID : d6f68875-cdf5-43a5-a3e3-53ffd683311c
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("d6f68875-cdf5-43a5-a3e3-53ffd683311c"), event_id=1, version=0)
class Microsoft_Windows_CorruptedFileRecovery_Server_1_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "AppName" / WString
    )


@declare(guid=guid("d6f68875-cdf5-43a5-a3e3-53ffd683311c"), event_id=2, version=0)
class Microsoft_Windows_CorruptedFileRecovery_Server_2_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "AppName" / WString
    )


@declare(guid=guid("d6f68875-cdf5-43a5-a3e3-53ffd683311c"), event_id=3, version=0)
class Microsoft_Windows_CorruptedFileRecovery_Server_3_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "AppName" / WString
    )


@declare(guid=guid("d6f68875-cdf5-43a5-a3e3-53ffd683311c"), event_id=4, version=0)
class Microsoft_Windows_CorruptedFileRecovery_Server_4_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "AppName" / WString
    )


@declare(guid=guid("d6f68875-cdf5-43a5-a3e3-53ffd683311c"), event_id=5, version=0)
class Microsoft_Windows_CorruptedFileRecovery_Server_5_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "AppName" / WString
    )


@declare(guid=guid("d6f68875-cdf5-43a5-a3e3-53ffd683311c"), event_id=6, version=0)
class Microsoft_Windows_CorruptedFileRecovery_Server_6_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "AppName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("d6f68875-cdf5-43a5-a3e3-53ffd683311c"), event_id=7, version=0)
class Microsoft_Windows_CorruptedFileRecovery_Server_7_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "AppName" / WString
    )


@declare(guid=guid("d6f68875-cdf5-43a5-a3e3-53ffd683311c"), event_id=8, version=0)
class Microsoft_Windows_CorruptedFileRecovery_Server_8_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "AppName" / WString
    )


@declare(guid=guid("d6f68875-cdf5-43a5-a3e3-53ffd683311c"), event_id=9, version=0)
class Microsoft_Windows_CorruptedFileRecovery_Server_9_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "AppName" / WString
    )


@declare(guid=guid("d6f68875-cdf5-43a5-a3e3-53ffd683311c"), event_id=10, version=0)
class Microsoft_Windows_CorruptedFileRecovery_Server_10_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "AppName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("d6f68875-cdf5-43a5-a3e3-53ffd683311c"), event_id=11, version=0)
class Microsoft_Windows_CorruptedFileRecovery_Server_11_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "AppName" / WString
    )


@declare(guid=guid("d6f68875-cdf5-43a5-a3e3-53ffd683311c"), event_id=12, version=0)
class Microsoft_Windows_CorruptedFileRecovery_Server_12_0(Etw):
    pattern = Struct(
        "FilePath" / WString,
        "AppName" / WString,
        "ProductName" / WString,
        "ProductVersion" / WString
    )


@declare(guid=guid("d6f68875-cdf5-43a5-a3e3-53ffd683311c"), event_id=13, version=0)
class Microsoft_Windows_CorruptedFileRecovery_Server_13_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "AppName" / WString
    )


@declare(guid=guid("d6f68875-cdf5-43a5-a3e3-53ffd683311c"), event_id=14, version=0)
class Microsoft_Windows_CorruptedFileRecovery_Server_14_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "AppName" / WString
    )


@declare(guid=guid("d6f68875-cdf5-43a5-a3e3-53ffd683311c"), event_id=15, version=0)
class Microsoft_Windows_CorruptedFileRecovery_Server_15_0(Etw):
    pattern = Struct(
        "FilePath" / WString,
        "AppName" / WString,
        "ProductName" / WString,
        "ProductVersion" / WString
    )


@declare(guid=guid("d6f68875-cdf5-43a5-a3e3-53ffd683311c"), event_id=16, version=0)
class Microsoft_Windows_CorruptedFileRecovery_Server_16_0(Etw):
    pattern = Struct(
        "FilePath" / WString,
        "AppName" / WString,
        "ProductName" / WString,
        "ProductVersion" / WString
    )


@declare(guid=guid("d6f68875-cdf5-43a5-a3e3-53ffd683311c"), event_id=17, version=0)
class Microsoft_Windows_CorruptedFileRecovery_Server_17_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "AppName" / WString
    )

