# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Crypto-DSSEnh
GUID : 43dad447-735f-4829-a6ff-9829a87419ff
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("43dad447-735f-4829-a6ff-9829a87419ff"), event_id=1, version=0)
class Microsoft_Windows_Crypto_DSSEnh_1_0(Etw):
    pattern = Struct(
        "OperationType" / Int32ul,
        "ProcessName" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("43dad447-735f-4829-a6ff-9829a87419ff"), event_id=2, version=0)
class Microsoft_Windows_Crypto_DSSEnh_2_0(Etw):
    pattern = Struct(
        "ProcessName" / WString,
        "ProviderType" / Int32ul,
        "MachineKeyset" / Int32ul,
        "AppContainer" / Int8ul,
        "Status" / Int32ul,
        "ErrorDescription" / WString
    )


@declare(guid=guid("43dad447-735f-4829-a6ff-9829a87419ff"), event_id=3, version=0)
class Microsoft_Windows_Crypto_DSSEnh_3_0(Etw):
    pattern = Struct(
        "ProcessName" / WString,
        "MachineKeyset" / Int8ul,
        "DesiredAccess" / Int32ul,
        "UserStorageArea" / WString,
        "FileName" / WString,
        "Status" / Int32ul,
        "ErrorDescription" / WString
    )


@declare(guid=guid("43dad447-735f-4829-a6ff-9829a87419ff"), event_id=4, version=0)
class Microsoft_Windows_Crypto_DSSEnh_4_0(Etw):
    pattern = Struct(
        "ProcessName" / WString,
        "UserStoragePath" / WString,
        "FileName" / WString,
        "Status" / Int32ul,
        "ErrorDescription" / WString
    )


@declare(guid=guid("43dad447-735f-4829-a6ff-9829a87419ff"), event_id=5, version=0)
class Microsoft_Windows_Crypto_DSSEnh_5_0(Etw):
    pattern = Struct(
        "ProcessName" / WString,
        "UserStoragePath" / WString,
        "FileName" / CString,
        "AppContainer" / Int8ul,
        "Status" / Int32ul,
        "ErrorDescription" / WString
    )


@declare(guid=guid("43dad447-735f-4829-a6ff-9829a87419ff"), event_id=6, version=0)
class Microsoft_Windows_Crypto_DSSEnh_6_0(Etw):
    pattern = Struct(
        "ProcessName" / WString,
        "MachineKeyset" / Int8ul,
        "FilePath" / WString,
        "DesiredAccess" / Int32ul,
        "ShareMode" / Int32ul,
        "CreationDisposition" / Int32ul,
        "Attributes" / Int32ul,
        "Status" / Int32ul,
        "ErrorDescription" / WString
    )


@declare(guid=guid("43dad447-735f-4829-a6ff-9829a87419ff"), event_id=7, version=0)
class Microsoft_Windows_Crypto_DSSEnh_7_0(Etw):
    pattern = Struct(
        "ProcessName" / WString,
        "FileName" / WString,
        "ProviderType" / Int32ul,
        "MachineKeyset" / Int8ul,
        "SecurityInformation" / Int32ul,
        "AppContainer" / Int8ul,
        "Status" / Int32ul,
        "ErrorDescription" / WString
    )


@declare(guid=guid("43dad447-735f-4829-a6ff-9829a87419ff"), event_id=8, version=0)
class Microsoft_Windows_Crypto_DSSEnh_8_0(Etw):
    pattern = Struct(
        "ProcessName" / WString,
        "FilePath" / WString,
        "DesiredAccess" / Int32ul,
        "ShareMode" / Int32ul,
        "CreationDisposition" / Int32ul,
        "Attributes" / Int32ul,
        "Status" / Int32ul,
        "ErrorDescription" / WString
    )


@declare(guid=guid("43dad447-735f-4829-a6ff-9829a87419ff"), event_id=9, version=0)
class Microsoft_Windows_Crypto_DSSEnh_9_0(Etw):
    pattern = Struct(
        "ProcessName" / WString,
        "FilePath" / WString,
        "Status" / Int32ul,
        "ErrorDescription" / WString
    )


@declare(guid=guid("43dad447-735f-4829-a6ff-9829a87419ff"), event_id=10, version=0)
class Microsoft_Windows_Crypto_DSSEnh_10_0(Etw):
    pattern = Struct(
        "ProcessName" / WString,
        "ProviderType" / Int32ul,
        "ContainerName" / CString,
        "MachineKeyset" / Int8ul,
        "Status" / Int32ul,
        "ErrorDescription" / WString
    )


@declare(guid=guid("43dad447-735f-4829-a6ff-9829a87419ff"), event_id=11, version=0)
class Microsoft_Windows_Crypto_DSSEnh_11_0(Etw):
    pattern = Struct(
        "ProcessName" / WString,
        "ProviderType" / Int32ul,
        "ContainerName" / WString,
        "MachineKeyset" / Int8ul,
        "Status" / Int32ul,
        "ErrorDescription" / WString
    )


@declare(guid=guid("43dad447-735f-4829-a6ff-9829a87419ff"), event_id=12, version=0)
class Microsoft_Windows_Crypto_DSSEnh_12_0(Etw):
    pattern = Struct(
        "ProcessName" / WString,
        "ProviderType" / Int32ul,
        "ContainerName" / CString,
        "MachineKeyset" / Int8ul,
        "AppContainer" / Int8ul,
        "Status" / Int32ul,
        "ErrorDescription" / WString
    )


@declare(guid=guid("43dad447-735f-4829-a6ff-9829a87419ff"), event_id=13, version=0)
class Microsoft_Windows_Crypto_DSSEnh_13_0(Etw):
    pattern = Struct(
        "ProcessName" / WString,
        "ProviderType" / Int32ul,
        "ContainerName" / CString,
        "MachineKeyset" / Int8ul
    )


@declare(guid=guid("43dad447-735f-4829-a6ff-9829a87419ff"), event_id=14, version=0)
class Microsoft_Windows_Crypto_DSSEnh_14_0(Etw):
    pattern = Struct(
        "ProcessName" / WString,
        "ProviderType" / Int32ul,
        "ContainerName" / WString,
        "MachineKeyset" / Int8ul
    )


@declare(guid=guid("43dad447-735f-4829-a6ff-9829a87419ff"), event_id=15, version=0)
class Microsoft_Windows_Crypto_DSSEnh_15_0(Etw):
    pattern = Struct(
        "ProcessName" / WString,
        "ProviderType" / Int32ul,
        "ContainerName" / CString,
        "MachineKeyset" / Int8ul,
        "AppContainer" / Int8ul
    )

