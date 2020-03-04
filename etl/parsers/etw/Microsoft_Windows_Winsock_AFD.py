# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Winsock-AFD
GUID : e53c6823-7bb8-44bb-90dc-3f86090d48a6
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=1, version=0)
class Microsoft_Windows_Winsock_AFD_1_0(Etw):
    pattern = Struct(
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "AddressFamily" / Int32ul,
        "SocketType" / Int32ul,
        "Protocol" / Int32ul,
        "UserModePid" / Int64ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=2, version=0)
class Microsoft_Windows_Winsock_AFD_2_0(Etw):
    pattern = Struct(
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "Address" / Int32ul,
        "Port" / Int16ul,
        "Status" / Int32ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=3, version=0)
class Microsoft_Windows_Winsock_AFD_3_0(Etw):
    pattern = Struct(
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "Port" / Int16ul,
        "Status" / Int32ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=4, version=0)
class Microsoft_Windows_Winsock_AFD_4_0(Etw):
    pattern = Struct(
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "Address" / Int32ul,
        "Port" / Int16ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=5, version=0)
class Microsoft_Windows_Winsock_AFD_5_0(Etw):
    pattern = Struct(
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "Port" / Int16ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=6, version=0)
class Microsoft_Windows_Winsock_AFD_6_0(Etw):
    pattern = Struct(
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "Error" / Int32ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=7, version=0)
class Microsoft_Windows_Winsock_AFD_7_0(Etw):
    pattern = Struct(
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "Reason" / Int32sl
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=8, version=0)
class Microsoft_Windows_Winsock_AFD_8_0(Etw):
    pattern = Struct(
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "Reason" / Int32sl
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=9, version=0)
class Microsoft_Windows_Winsock_AFD_9_0(Etw):
    pattern = Struct(
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "Error" / Int32ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=10, version=0)
class Microsoft_Windows_Winsock_AFD_10_0(Etw):
    pattern = Struct(
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "Error" / Int32ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=11, version=0)
class Microsoft_Windows_Winsock_AFD_11_0(Etw):
    pattern = Struct(
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "Error" / Int32ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=12, version=0)
class Microsoft_Windows_Winsock_AFD_12_0(Etw):
    pattern = Struct(
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "Error" / Int32ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=13, version=0)
class Microsoft_Windows_Winsock_AFD_13_0(Etw):
    pattern = Struct(
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "Error" / Int32ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=14, version=0)
class Microsoft_Windows_Winsock_AFD_14_0(Etw):
    pattern = Struct(
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "Error" / Int32ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=15, version=0)
class Microsoft_Windows_Winsock_AFD_15_0(Etw):
    pattern = Struct(
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "Address" / Int32ul,
        "Port" / Int16ul,
        "Status" / Int32ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=16, version=0)
class Microsoft_Windows_Winsock_AFD_16_0(Etw):
    pattern = Struct(
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "Port" / Int16ul,
        "Status" / Int32ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=17, version=0)
class Microsoft_Windows_Winsock_AFD_17_0(Etw):
    pattern = Struct(
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "Error" / Int32ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=18, version=0)
class Microsoft_Windows_Winsock_AFD_18_0(Etw):
    pattern = Struct(
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "FastPath" / Int8ul,
        "BufferCount" / Int32sl,
        "Buffer" / Int64ul,
        "BufferLength" / Int32ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=19, version=0)
class Microsoft_Windows_Winsock_AFD_19_0(Etw):
    pattern = Struct(
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "FastPath" / Int8ul,
        "BufferCount" / Int32sl,
        "Buffer" / Int64ul,
        "BufferLength" / Int32ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=20, version=0)
class Microsoft_Windows_Winsock_AFD_20_0(Etw):
    pattern = Struct(
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "FastPath" / Int8ul,
        "BufferCount" / Int32sl,
        "Buffer" / Int64ul,
        "BufferLength" / Int32ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=21, version=0)
class Microsoft_Windows_Winsock_AFD_21_0(Etw):
    pattern = Struct(
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "FastPath" / Int8ul,
        "BufferCount" / Int32sl,
        "Buffer" / Int64ul,
        "BufferLength" / Int32ul,
        "Address" / Int32ul,
        "Port" / Int16ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=22, version=0)
class Microsoft_Windows_Winsock_AFD_22_0(Etw):
    pattern = Struct(
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "FastPath" / Int8ul,
        "BufferCount" / Int32sl,
        "Buffer" / Int64ul,
        "BufferLength" / Int32ul,
        "Port" / Int16ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=23, version=0)
class Microsoft_Windows_Winsock_AFD_23_0(Etw):
    pattern = Struct(
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "Buffer" / Int64ul,
        "BufferLength" / Int32ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=24, version=0)
class Microsoft_Windows_Winsock_AFD_24_0(Etw):
    pattern = Struct(
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "Buffer" / Int64ul,
        "BufferLength" / Int32ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=25, version=0)
class Microsoft_Windows_Winsock_AFD_25_0(Etw):
    pattern = Struct(
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "Buffer" / Int64ul,
        "BufferLength" / Int32ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=26, version=0)
class Microsoft_Windows_Winsock_AFD_26_0(Etw):
    pattern = Struct(
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "BufferCount" / Int32sl,
        "Buffer" / Int64ul,
        "BufferLength" / Int32ul,
        "Address" / Int32ul,
        "Port" / Int16ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=27, version=0)
class Microsoft_Windows_Winsock_AFD_27_0(Etw):
    pattern = Struct(
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "BufferCount" / Int32sl,
        "Buffer" / Int64ul,
        "BufferLength" / Int32ul,
        "Port" / Int16ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=28, version=0)
class Microsoft_Windows_Winsock_AFD_28_0(Etw):
    pattern = Struct(
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "Buffer" / Int64ul,
        "BufferLength" / Int32ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=29, version=0)
class Microsoft_Windows_Winsock_AFD_29_0(Etw):
    pattern = Struct(
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "Option" / Int32ul,
        "Value" / Int32ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=30, version=0)
class Microsoft_Windows_Winsock_AFD_30_0(Etw):
    pattern = Struct(
        "Process" / Int64ul,
        "HandleCount" / Int32sl,
        "Timeout" / Int32sl
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=31, version=0)
class Microsoft_Windows_Winsock_AFD_31_0(Etw):
    pattern = Struct(
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "Error" / Int32ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=32, version=0)
class Microsoft_Windows_Winsock_AFD_32_0(Etw):
    pattern = Struct(
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "EventMask" / Int32ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=33, version=0)
class Microsoft_Windows_Winsock_AFD_33_0(Etw):
    pattern = Struct(
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "PacketSize" / Int32sl,
        "Address" / Int32ul,
        "Port" / Int16ul,
        "Reason" / Int32sl
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=34, version=0)
class Microsoft_Windows_Winsock_AFD_34_0(Etw):
    pattern = Struct(
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "PacketSize" / Int32sl,
        "Port" / Int16ul,
        "Reason" / Int32sl
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=35, version=0)
class Microsoft_Windows_Winsock_AFD_35_0(Etw):
    pattern = Struct(
        "Process" / Int64ul,
        "ListenEndpoint" / Int64ul,
        "Address" / Int32ul,
        "Port" / Int16ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=36, version=0)
class Microsoft_Windows_Winsock_AFD_36_0(Etw):
    pattern = Struct(
        "Process" / Int64ul,
        "ListenEndpoint" / Int64ul,
        "Port" / Int16ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=37, version=0)
class Microsoft_Windows_Winsock_AFD_37_0(Etw):
    pattern = Struct(
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "BytesIndicated" / Int32sl
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=38, version=0)
class Microsoft_Windows_Winsock_AFD_38_0(Etw):
    pattern = Struct(
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "Address" / Int32ul,
        "Port" / Int16ul,
        "BytesIndicated" / Int32sl
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=39, version=0)
class Microsoft_Windows_Winsock_AFD_39_0(Etw):
    pattern = Struct(
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "Port" / Int16ul,
        "BytesIndicated" / Int32sl
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=40, version=0)
class Microsoft_Windows_Winsock_AFD_40_0(Etw):
    pattern = Struct(
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "Error" / Int32ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=41, version=0)
class Microsoft_Windows_Winsock_AFD_41_0(Etw):
    pattern = Struct(
        "Process" / Int64ul,
        "Endpoint" / Int64ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=1000, version=0)
class Microsoft_Windows_Winsock_AFD_1000_0(Etw):
    pattern = Struct(
        "EnterExit" / Int32ul,
        "Location" / Int32ul,
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "AddressFamily" / Int32ul,
        "SocketType" / Int32ul,
        "Protocol" / Int32ul,
        "ProcessId" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=1001, version=0)
class Microsoft_Windows_Winsock_AFD_1001_0(Etw):
    pattern = Struct(
        "EnterExit" / Int32ul,
        "Location" / Int32ul,
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=1002, version=0)
class Microsoft_Windows_Winsock_AFD_1002_0(Etw):
    pattern = Struct(
        "EnterExit" / Int32ul,
        "Location" / Int32ul,
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=1003, version=0)
class Microsoft_Windows_Winsock_AFD_1003_0(Etw):
    pattern = Struct(
        "EnterExit" / Int32ul,
        "Location" / Int32ul,
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "BufferCount" / Int32ul,
        "Buffer" / Int64ul,
        "BufferLength" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=1004, version=0)
class Microsoft_Windows_Winsock_AFD_1004_0(Etw):
    pattern = Struct(
        "EnterExit" / Int32ul,
        "Location" / Int32ul,
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "BufferCount" / Int32ul,
        "Buffer" / Int64ul,
        "BufferLength" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=1005, version=0)
class Microsoft_Windows_Winsock_AFD_1005_0(Etw):
    pattern = Struct(
        "EnterExit" / Int32ul,
        "Location" / Int32ul,
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "BufferCount" / Int32ul,
        "Buffer" / Int64ul,
        "BufferLength" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=1006, version=0)
class Microsoft_Windows_Winsock_AFD_1006_0(Etw):
    pattern = Struct(
        "EnterExit" / Int32ul,
        "Location" / Int32ul,
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "BufferCount" / Int32ul,
        "Buffer" / Int64ul,
        "BufferLength" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=1007, version=0)
class Microsoft_Windows_Winsock_AFD_1007_0(Etw):
    pattern = Struct(
        "EnterExit" / Int32ul,
        "Location" / Int32ul,
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "BufferCount" / Int32ul,
        "Buffer" / Int64ul,
        "BufferLength" / Int32ul,
        "Status" / Int32ul,
        "AddressLen" / Int32ul,
        "Address" / Bytes(lambda this: this.AddressLen)
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=1009, version=0)
class Microsoft_Windows_Winsock_AFD_1009_0(Etw):
    pattern = Struct(
        "EnterExit" / Int32ul,
        "Location" / Int32ul,
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "BufferCount" / Int32ul,
        "Buffer" / Int64ul,
        "BufferLength" / Int32ul,
        "Status" / Int32ul,
        "AddressLen" / Int32ul,
        "Address" / Bytes(lambda this: this.AddressLen)
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=1011, version=0)
class Microsoft_Windows_Winsock_AFD_1011_0(Etw):
    pattern = Struct(
        "EnterExit" / Int32ul,
        "Location" / Int32ul,
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "BufferCount" / Int32ul,
        "Buffer" / Int64ul,
        "BufferLength" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=1012, version=0)
class Microsoft_Windows_Winsock_AFD_1012_0(Etw):
    pattern = Struct(
        "EnterExit" / Int32ul,
        "Location" / Int32ul,
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "BufferCount" / Int32ul,
        "Buffer" / Int64ul,
        "BufferLength" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=1013, version=0)
class Microsoft_Windows_Winsock_AFD_1013_0(Etw):
    pattern = Struct(
        "EnterExit" / Int32ul,
        "Location" / Int32ul,
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "BufferCount" / Int32ul,
        "Buffer" / Int64ul,
        "BufferLength" / Int32ul,
        "Status" / Int32ul,
        "AddressLen" / Int32ul,
        "Address" / Bytes(lambda this: this.AddressLen)
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=1015, version=0)
class Microsoft_Windows_Winsock_AFD_1015_0(Etw):
    pattern = Struct(
        "EnterExit" / Int32ul,
        "Location" / Int32ul,
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "BufferCount" / Int32ul,
        "Buffer" / Int64ul,
        "BufferLength" / Int32ul,
        "Status" / Int32ul,
        "AddressLen" / Int32ul,
        "Address" / Bytes(lambda this: this.AddressLen)
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=1017, version=0)
class Microsoft_Windows_Winsock_AFD_1017_0(Etw):
    pattern = Struct(
        "EnterExit" / Int32ul,
        "Location" / Int32ul,
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=1018, version=0)
class Microsoft_Windows_Winsock_AFD_1018_0(Etw):
    pattern = Struct(
        "EnterExit" / Int32ul,
        "Location" / Int32ul,
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "Buffer" / Int64ul,
        "BufferLength" / Int32ul,
        "Status" / Int32ul,
        "AddressLen" / Int32ul,
        "Address" / Bytes(lambda this: this.AddressLen)
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=1020, version=0)
class Microsoft_Windows_Winsock_AFD_1020_0(Etw):
    pattern = Struct(
        "EnterExit" / Int32ul,
        "Location" / Int32ul,
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=1021, version=0)
class Microsoft_Windows_Winsock_AFD_1021_0(Etw):
    pattern = Struct(
        "EnterExit" / Int32ul,
        "Location" / Int32ul,
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "Buffer" / Int64ul,
        "BufferLength" / Int32ul,
        "Status" / Int32ul,
        "AddressLen" / Int32ul,
        "Address" / Bytes(lambda this: this.AddressLen)
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=1023, version=0)
class Microsoft_Windows_Winsock_AFD_1023_0(Etw):
    pattern = Struct(
        "EnterExit" / Int32ul,
        "Location" / Int32ul,
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=1024, version=0)
class Microsoft_Windows_Winsock_AFD_1024_0(Etw):
    pattern = Struct(
        "EnterExit" / Int32ul,
        "Location" / Int32ul,
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "Buffer" / Int64ul,
        "BufferLength" / Int32ul,
        "Status" / Int32ul,
        "AddressLen" / Int32ul,
        "Address" / Bytes(lambda this: this.AddressLen),
        "AcceptEndpoint" / Int64ul,
        "CurrentBacklog" / Int32ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=1026, version=0)
class Microsoft_Windows_Winsock_AFD_1026_0(Etw):
    pattern = Struct(
        "EnterExit" / Int32ul,
        "Location" / Int32ul,
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=1027, version=0)
class Microsoft_Windows_Winsock_AFD_1027_0(Etw):
    pattern = Struct(
        "EnterExit" / Int32ul,
        "Location" / Int32ul,
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "Buffer" / Int64ul,
        "BufferLength" / Int32ul,
        "Status" / Int32ul,
        "AddressLen" / Int32ul,
        "Address" / Bytes(lambda this: this.AddressLen),
        "AcceptEndpoint" / Int64ul,
        "CurrentBacklog" / Int32ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=1029, version=0)
class Microsoft_Windows_Winsock_AFD_1029_0(Etw):
    pattern = Struct(
        "EnterExit" / Int32ul,
        "Location" / Int32ul,
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=1030, version=0)
class Microsoft_Windows_Winsock_AFD_1030_0(Etw):
    pattern = Struct(
        "EnterExit" / Int32ul,
        "Location" / Int32ul,
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "Status" / Int32ul,
        "AddressLen" / Int32ul,
        "Address" / Bytes(lambda this: this.AddressLen)
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=1032, version=0)
class Microsoft_Windows_Winsock_AFD_1032_0(Etw):
    pattern = Struct(
        "EnterExit" / Int32ul,
        "Location" / Int32ul,
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "Reason" / Int32ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=1033, version=0)
class Microsoft_Windows_Winsock_AFD_1033_0(Etw):
    pattern = Struct(
        "EnterExit" / Int32ul,
        "Location" / Int32ul,
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "Buffer" / Int64ul,
        "BufferLength" / Int32ul,
        "AddressLen" / Int32ul,
        "Address" / Bytes(lambda this: this.AddressLen),
        "Reason" / Int32ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=1035, version=0)
class Microsoft_Windows_Winsock_AFD_1035_0(Etw):
    pattern = Struct(
        "EnterExit" / Int32ul,
        "Location" / Int32ul,
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "Option" / Int32ul,
        "Value" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=1036, version=0)
class Microsoft_Windows_Winsock_AFD_1036_0(Etw):
    pattern = Struct(
        "EnterExit" / Int32ul,
        "Location" / Int32ul,
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=1037, version=0)
class Microsoft_Windows_Winsock_AFD_1037_0(Etw):
    pattern = Struct(
        "EnterExit" / Int32ul,
        "Location" / Int32ul,
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "Backlog" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=3000, version=0)
class Microsoft_Windows_Winsock_AFD_3000_0(Etw):
    pattern = Struct(
        "EnterExit" / Int32ul,
        "Location" / Int32ul,
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=3001, version=0)
class Microsoft_Windows_Winsock_AFD_3001_0(Etw):
    pattern = Struct(
        "EnterExit" / Int32ul,
        "Location" / Int32ul,
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "Status" / Int32ul,
        "AddressLen" / Int32ul,
        "Address" / Bytes(lambda this: this.AddressLen),
        "CurrentBacklog" / Int32ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=3003, version=0)
class Microsoft_Windows_Winsock_AFD_3003_0(Etw):
    pattern = Struct(
        "EnterExit" / Int32ul,
        "Location" / Int32ul,
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "Buffer" / Int64ul,
        "BufferLength" / Int32ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=3004, version=0)
class Microsoft_Windows_Winsock_AFD_3004_0(Etw):
    pattern = Struct(
        "EnterExit" / Int32ul,
        "Location" / Int32ul,
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "Buffer" / Int64ul,
        "BufferLength" / Int32ul,
        "AddressLen" / Int32ul,
        "Address" / Bytes(lambda this: this.AddressLen)
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=3006, version=0)
class Microsoft_Windows_Winsock_AFD_3006_0(Etw):
    pattern = Struct(
        "EnterExit" / Int32ul,
        "Location" / Int32ul,
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=3007, version=0)
class Microsoft_Windows_Winsock_AFD_3007_0(Etw):
    pattern = Struct(
        "EnterExit" / Int32ul,
        "Location" / Int32ul,
        "Process" / Int64ul,
        "Endpoint" / Int64ul,
        "SendBacklog" / Int32ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=4000, version=0)
class Microsoft_Windows_Winsock_AFD_4000_0(Etw):
    pattern = Struct(
        "RegistrationDomain" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=4001, version=0)
class Microsoft_Windows_Winsock_AFD_4001_0(Etw):
    pattern = Struct(
        "RegistrationDomain" / Int64ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=4002, version=0)
class Microsoft_Windows_Winsock_AFD_4002_0(Etw):
    pattern = Struct(
        "Cq" / Int64ul,
        "RegistrationDomain" / Int64ul,
        "EntryCount" / Int32ul,
        "UserAddress" / Int64ul,
        "SystemAddress" / Int64ul,
        "BufferSize" / Int32ul,
        "CqIndex" / Int32ul,
        "NotificationType" / Int32ul,
        "NotificationHandle" / Int64ul,
        "NotificationObject" / Int64ul,
        "NotificationContext1" / Int64ul,
        "NotificationContext2" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=4003, version=0)
class Microsoft_Windows_Winsock_AFD_4003_0(Etw):
    pattern = Struct(
        "Cq" / Int64ul,
        "Commit" / Int32ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=4004, version=0)
class Microsoft_Windows_Winsock_AFD_4004_0(Etw):
    pattern = Struct(
        "Cq" / Int64ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=4005, version=0)
class Microsoft_Windows_Winsock_AFD_4005_0(Etw):
    pattern = Struct(
        "Cq" / Int64ul,
        "OriginalEntryCount" / Int32ul,
        "OriginalStart" / Int32ul,
        "OriginalEnd" / Int32ul,
        "Commit" / Int32ul,
        "RequestedEntryCount" / Int32ul,
        "UserAddress" / Int64ul,
        "SystemAddress" / Int64ul,
        "BufferSize" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=4006, version=0)
class Microsoft_Windows_Winsock_AFD_4006_0(Etw):
    pattern = Struct(
        "Endpoint" / Int64ul,
        "RioState" / Int64ul,
        "RegistrationDomain" / Int64ul,
        "SendEntryCount" / Int32ul,
        "SendUserAddress" / Int64ul,
        "SendSystemAddress" / Int64ul,
        "SendBufferSize" / Int32ul,
        "ReceiveEntryCount" / Int32ul,
        "ReceiveUserAddress" / Int64ul,
        "ReceiveSystemAddress" / Int64ul,
        "ReceiveBufferSize" / Int32ul,
        "SendCqIndex" / Int32ul,
        "ReceiveCqIndex" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=4007, version=0)
class Microsoft_Windows_Winsock_AFD_4007_0(Etw):
    pattern = Struct(
        "RioState" / Int64ul,
        "ReceiveQueueStart" / Int32ul,
        "ReceiveQueueEnd" / Int32ul,
        "SendQueueStart" / Int32ul,
        "SendQueueEnd" / Int32ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=4008, version=0)
class Microsoft_Windows_Winsock_AFD_4008_0(Etw):
    pattern = Struct(
        "RioState" / Int64ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=4009, version=0)
class Microsoft_Windows_Winsock_AFD_4009_0(Etw):
    pattern = Struct(
        "RioState" / Int64ul,
        "OriginalSendEntryCount" / Int32ul,
        "OriginalSendQueueStart" / Int32ul,
        "OriginalSendQueueEnd" / Int32ul,
        "RequestedSendEntryCount" / Int32ul,
        "SendUserAddress" / Int64ul,
        "SendSystemAddress" / Int64ul,
        "SendBufferSize" / Int32ul,
        "OriginalReceiveEntryCount" / Int32ul,
        "OriginalReceiveQueueStart" / Int32ul,
        "OriginalReceiveQueueEnd" / Int32ul,
        "RequestedReceiveEntryCount" / Int32ul,
        "ReceiveUserAddress" / Int64ul,
        "ReceiveSystemAddress" / Int64ul,
        "ReceiveBufferSize" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=4010, version=0)
class Microsoft_Windows_Winsock_AFD_4010_0(Etw):
    pattern = Struct(
        "Buffer" / Int64ul,
        "RegistrationDomain" / Int64ul,
        "UserAddress" / Int64ul,
        "SystemAddress" / Int64ul,
        "BufferSize" / Int32ul,
        "BufferId" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=4011, version=0)
class Microsoft_Windows_Winsock_AFD_4011_0(Etw):
    pattern = Struct(
        "Buffer" / Int64ul,
        "References" / Int32ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=4012, version=0)
class Microsoft_Windows_Winsock_AFD_4012_0(Etw):
    pattern = Struct(
        "Buffer" / Int64ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=4013, version=0)
class Microsoft_Windows_Winsock_AFD_4013_0(Etw):
    pattern = Struct(
        "RegistrationDomain" / Int64ul,
        "RioState" / Int64ul,
        "BufferId" / Int32ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=4014, version=0)
class Microsoft_Windows_Winsock_AFD_4014_0(Etw):
    pattern = Struct(
        "RegistrationDomain" / Int64ul,
        "RioState" / Int64ul,
        "Buffer" / Int64ul,
        "BufferOffset" / Int32ul,
        "BufferLength" / Int32ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=4015, version=0)
class Microsoft_Windows_Winsock_AFD_4015_0(Etw):
    pattern = Struct(
        "RioState" / Int64ul,
        "BufferType" / Int32ul,
        "SpecifiedLength" / Int32ul,
        "RequiredLength" / Int32ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=4016, version=0)
class Microsoft_Windows_Winsock_AFD_4016_0(Etw):
    pattern = Struct(
        "NameResolutionHandle" / Int64ul,
        "Process" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("e53c6823-7bb8-44bb-90dc-3f86090d48a6"), event_id=4017, version=0)
class Microsoft_Windows_Winsock_AFD_4017_0(Etw):
    pattern = Struct(
        "NameResolutionHandle" / Int64ul,
        "Process" / Int64ul
    )

