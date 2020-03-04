# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Hyper-V-VmSwitch
GUID : 67dc0d66-3695-47c0-9642-33f76f7bd7ad
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=1, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_1_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=2, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_2_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=3, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_3_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=4, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_4_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "UniqueEvent" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=5, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_5_0(Etw):
    pattern = Struct(
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen)
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=6, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_6_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "UniqueEvent" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=7, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_7_0(Etw):
    pattern = Struct(
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen)
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=8, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_8_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "UniqueEvent" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=9, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_9_0(Etw):
    pattern = Struct(
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "Flags" / Int32ul,
        "OwnerService" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=10, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_10_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "UniqueEvent" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=11, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_11_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "UniqueEvent" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=12, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_12_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "PortNameLen" / Int32ul,
        "PortName" / Bytes(lambda this: this.PortNameLen),
        "PortFNameLen" / Int32ul,
        "PortFName" / Bytes(lambda this: this.PortFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "UniqueEvent" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=13, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_13_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "UniqueEvent" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=14, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_14_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "UniqueEvent" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=15, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_15_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "PortNameLen" / Int32ul,
        "PortName" / Bytes(lambda this: this.PortNameLen),
        "PortFNameLen" / Int32ul,
        "PortFName" / Bytes(lambda this: this.PortFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "UniqueEvent" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=16, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_16_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "UniqueEvent" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=17, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_17_0(Etw):
    pattern = Struct(
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "PortNameLen" / Int32ul,
        "PortName" / Bytes(lambda this: this.PortNameLen),
        "PortFNameLen" / Int32ul,
        "PortFName" / Bytes(lambda this: this.PortFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen)
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=18, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_18_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "PortNameLen" / Int32ul,
        "PortName" / Bytes(lambda this: this.PortNameLen),
        "PortFNameLen" / Int32ul,
        "PortFName" / Bytes(lambda this: this.PortFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "UniqueEvent" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=19, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_19_0(Etw):
    pattern = Struct(
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen)
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=20, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_20_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "UniqueEvent" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=21, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_21_0(Etw):
    pattern = Struct(
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen)
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=22, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_22_0(Etw):
    pattern = Struct(
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen)
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=23, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_23_0(Etw):
    pattern = Struct(
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen)
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=24, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_24_0(Etw):
    pattern = Struct(
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen)
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=25, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_25_0(Etw):
    pattern = Struct(
        "MacAddressLen" / Int32ul,
        "MacAddress" / Bytes(lambda this: this.MacAddressLen),
        "Port1NameLen" / Int32ul,
        "Port1Name" / Bytes(lambda this: this.Port1NameLen),
        "Port1FNameLen" / Int32ul,
        "Port1FName" / Bytes(lambda this: this.Port1FNameLen),
        "Port2NameLen" / Int32ul,
        "Port2Name" / Bytes(lambda this: this.Port2NameLen),
        "Port2FNameLen" / Int32ul,
        "Port2FName" / Bytes(lambda this: this.Port2FNameLen)
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=26, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_26_0(Etw):
    pattern = Struct(
        "VMNameLen" / Int32ul,
        "VMName" / Bytes(lambda this: this.VMNameLen),
        "VMIdLen" / Int32ul,
        "VMId" / Bytes(lambda this: this.VMIdLen),
        "ServerVersionLen" / Int32ul,
        "ServerVersion" / Bytes(lambda this: this.ServerVersionLen),
        "ClientVersionLen" / Int32ul,
        "ClientVersion" / Bytes(lambda this: this.ClientVersionLen)
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=28, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_28_0(Etw):
    pattern = Struct(
        "MacAddressLen" / Int32ul,
        "MacAddress" / Bytes(lambda this: this.MacAddressLen),
        "Port1NameLen" / Int32ul,
        "Port1Name" / Bytes(lambda this: this.Port1NameLen),
        "Port1FNameLen" / Int32ul,
        "Port1FName" / Bytes(lambda this: this.Port1FNameLen),
        "Port2NameLen" / Int32ul,
        "Port2Name" / Bytes(lambda this: this.Port2NameLen),
        "Port2FNameLen" / Int32ul,
        "Port2FName" / Bytes(lambda this: this.Port2FNameLen)
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=29, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_29_0(Etw):
    pattern = Struct(
        "MacAddressLen" / Int32ul,
        "MacAddress" / Bytes(lambda this: this.MacAddressLen),
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen)
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=30, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_30_0(Etw):
    pattern = Struct(
        "MacAddressLen" / Int32ul,
        "MacAddress" / Bytes(lambda this: this.MacAddressLen),
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen)
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=31, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_31_0(Etw):
    pattern = Struct(
        "MacAddressLen" / Int32ul,
        "MacAddress" / Bytes(lambda this: this.MacAddressLen),
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen)
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=32, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_32_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "PortNameLen" / Int32ul,
        "PortName" / Bytes(lambda this: this.PortNameLen),
        "PortFNameLen" / Int32ul,
        "PortFName" / Bytes(lambda this: this.PortFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "UniqueEvent" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=33, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_33_0(Etw):
    pattern = Struct(
        "VMNameLen" / Int32ul,
        "VMName" / Bytes(lambda this: this.VMNameLen),
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "PortNameLen" / Int32ul,
        "PortName" / Bytes(lambda this: this.PortNameLen),
        "PortFNameLen" / Int32ul,
        "PortFName" / Bytes(lambda this: this.PortFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen)
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=34, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_34_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "PortNameLen" / Int32ul,
        "PortName" / Bytes(lambda this: this.PortNameLen),
        "PortFNameLen" / Int32ul,
        "PortFName" / Bytes(lambda this: this.PortFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "UniqueEvent" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=35, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_35_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "PortNameLen" / Int32ul,
        "PortName" / Bytes(lambda this: this.PortNameLen),
        "PortFNameLen" / Int32ul,
        "PortFName" / Bytes(lambda this: this.PortFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "UniqueEvent" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=36, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_36_0(Etw):
    pattern = Struct(
        "PortNameLen" / Int32ul,
        "PortName" / Bytes(lambda this: this.PortNameLen),
        "PortFNameLen" / Int32ul,
        "PortFName" / Bytes(lambda this: this.PortFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "AclNameLen" / Int32ul,
        "AclName" / Bytes(lambda this: this.AclNameLen)
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=37, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_37_0(Etw):
    pattern = Struct(
        "IpsecOffloadInboundDropReason" / Int32ul,
        "PortNameLen" / Int32ul,
        "PortName" / Bytes(lambda this: this.PortNameLen),
        "PortFNameLen" / Int32ul,
        "PortFName" / Bytes(lambda this: this.PortFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "DestAddressLen" / Int32ul,
        "DestAddress" / Bytes(lambda this: this.DestAddressLen),
        "SPI" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=38, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_38_0(Etw):
    pattern = Struct(
        "PortNameLen" / Int32ul,
        "PortName" / Bytes(lambda this: this.PortNameLen),
        "PortFNameLen" / Int32ul,
        "PortFName" / Bytes(lambda this: this.PortFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "DestAddressLen" / Int32ul,
        "DestAddress" / Bytes(lambda this: this.DestAddressLen),
        "SPI" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=39, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_39_0(Etw):
    pattern = Struct(
        "PortNameLen" / Int32ul,
        "PortName" / Bytes(lambda this: this.PortNameLen),
        "PortFNameLen" / Int32ul,
        "PortFName" / Bytes(lambda this: this.PortFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "OffloadHandle" / Int64ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=40, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_40_0(Etw):
    pattern = Struct(
        "IpsecSaOffloadFailureReason" / Int32ul,
        "PortNameLen" / Int32ul,
        "PortName" / Bytes(lambda this: this.PortNameLen),
        "PortFNameLen" / Int32ul,
        "PortFName" / Bytes(lambda this: this.PortFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "Status" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=41, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_41_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "UniqueEvent" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=42, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_42_0(Etw):
    pattern = Struct(
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "Flags" / Int32ul,
        "OwnerService" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=43, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_43_0(Etw):
    pattern = Struct(
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "Flags" / Int32ul,
        "OwnerService" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=44, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_44_0(Etw):
    pattern = Struct(
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "VmqIndex" / Int32ul,
        "SourceProcIndex" / Int32ul,
        "DestinationProcIndex" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=45, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_45_0(Etw):
    pattern = Struct(
        "PortNameLen" / Int32ul,
        "PortName" / Bytes(lambda this: this.PortNameLen),
        "PortFNameLen" / Int32ul,
        "PortFName" / Bytes(lambda this: this.PortFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen)
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=46, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_46_0(Etw):
    pattern = Struct(
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "PortNameLen" / Int32ul,
        "PortName" / Bytes(lambda this: this.PortNameLen),
        "PortFNameLen" / Int32ul,
        "PortFName" / Bytes(lambda this: this.PortFNameLen)
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=47, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_47_0(Etw):
    pattern = Struct(
        "CurrentTime" / Int64ul,
        "BytesSent" / Int32ul,
        "BytesDropped" / Int32ul,
        "NewSendWindow" / Int32ul,
        "MinSendWindow" / Int32ul,
        "Weight" / Int32ul,
        "SBytesRequested" / Int64sl,
        "DropRate" / Int32ul,
        "IdleIntervals" / Int64ul,
        "RcSendWindow" / Int32ul,
        "RcEpisodeLength" / Int32ul,
        "RcStatMuxFactor" / Int32ul,
        "RcExitThreshold" / Int32ul,
        "AverageMaxBytesRequested" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=48, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_48_0(Etw):
    pattern = Struct(
        "CurrentTime" / Int64ul,
        "ActiveFlows" / Int32ul,
        "ActiveWeight" / Int32ul,
        "NewSendWindow" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=49, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_49_0(Etw):
    pattern = Struct(
        "FlowConformanceEvent" / Int32ul,
        "CurrentTime" / Int64ul,
        "LastConformanceTime" / Int64ul,
        "PeakConformanceTime" / Int64ul,
        "Tokens" / Int64ul,
        "MaxTokens" / Int64ul,
        "Rate" / Int64ul,
        "LastConformanceCredits" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=50, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_50_0(Etw):
    pattern = Struct(
        "FlowSendQueueEvent" / Int32ul,
        "CurrentTime" / Int64ul,
        "IdleTime" / Int64ul,
        "DelayTime" / Int64ul,
        "BytesRequested" / Int32ul,
        "BytesSent" / Int32ul,
        "BytesQueued" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=51, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_51_0(Etw):
    pattern = Struct(
        "TimerEvent" / Int32ul,
        "TimerId" / Int32ul,
        "CurrentTime" / Int64ul,
        "SetTime" / Int64ul,
        "RunTime" / Int64ul,
        "FlowsProcessed" / Int32ul,
        "NblsSent" / Int32ul,
        "NblsDropped" / Int32ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=52, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_52_0(Etw):
    pattern = Struct(
        "CurrentTime" / Int64ul,
        "BytesRequested" / Int32ul,
        "BytesCompleted" / Int32ul,
        "BytesInQueue" / Int32ul,
        "BufferAvailable" / Int64sl,
        "BetaTerm" / Int64sl,
        "AlphaTerm" / Int64sl,
        "DeltaSendWindow" / Int64sl,
        "NewSendWindow" / Int64sl
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=53, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_53_0(Etw):
    pattern = Struct(
        "DropReason" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=54, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_54_0(Etw):
    pattern = Struct(
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "DropReason" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=55, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_55_0(Etw):
    pattern = Struct(
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "DropReason" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=56, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_56_0(Etw):
    pattern = Struct(
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "BufferAddress" / Int64ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=57, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_57_0(Etw):
    pattern = Struct(
        "SrcNicNameLen" / Int32ul,
        "SrcNicName" / Bytes(lambda this: this.SrcNicNameLen),
        "SrcNicFNameLen" / Int32ul,
        "SrcNicFName" / Bytes(lambda this: this.SrcNicFNameLen),
        "DestNicNameLen" / Int32ul,
        "DestNicName" / Bytes(lambda this: this.DestNicNameLen),
        "DestNicFNameLen" / Int32ul,
        "DestNicFName" / Bytes(lambda this: this.DestNicFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "BufferAddress" / Int64ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=58, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_58_0(Etw):
    pattern = Struct(
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "BufferAddress" / Int64ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=59, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_59_0(Etw):
    pattern = Struct(
        "ExtensionNameLen" / Int32ul,
        "ExtensionName" / Bytes(lambda this: this.ExtensionNameLen),
        "SrcNicNameLen" / Int32ul,
        "SrcNicName" / Bytes(lambda this: this.SrcNicNameLen),
        "SrcNicFNameLen" / Int32ul,
        "SrcNicFName" / Bytes(lambda this: this.SrcNicFNameLen),
        "DestNicNameLen" / Int32ul,
        "DestNicName" / Bytes(lambda this: this.DestNicNameLen),
        "DestNicFNameLen" / Int32ul,
        "DestNicFName" / Bytes(lambda this: this.DestNicFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen)
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=60, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_60_0(Etw):
    pattern = Struct(
        "SrcNicNameLen" / Int32ul,
        "SrcNicName" / Bytes(lambda this: this.SrcNicNameLen),
        "SrcNicFNameLen" / Int32ul,
        "SrcNicFName" / Bytes(lambda this: this.SrcNicFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "ExtensionGuidLen" / Int32ul,
        "ExtensionGuid" / Bytes(lambda this: this.ExtensionGuidLen),
        "ExtensionFriendlyNameLen" / Int32ul,
        "ExtensionFriendlyName" / Bytes(lambda this: this.ExtensionFriendlyNameLen),
        "ReasonLen" / Int32ul,
        "Reason" / Bytes(lambda this: this.ReasonLen)
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=61, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_61_0(Etw):
    pattern = Struct(
        "ExtensionNameLength" / Int32ul,
        "ExtensionName" / Bytes(lambda this: this.ExtensionNameLength),
        "ExtensionId" / Guid,
        "FeatureClassId" / Guid,
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "VMNameLen" / Int32ul,
        "VMName" / Bytes(lambda this: this.VMNameLen),
        "VMIdLen" / Int32ul,
        "VMId" / Bytes(lambda this: this.VMIdLen)
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=62, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_62_0(Etw):
    pattern = Struct(
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "Flags" / Int32ul,
        "OwnerService" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=63, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_63_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "UniqueEvent" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=64, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_64_0(Etw):
    pattern = Struct(
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "Flags" / Int32ul,
        "OwnerService" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=65, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_65_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "UniqueEvent" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=66, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_66_0(Etw):
    pattern = Struct(
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "Flags" / Int32ul,
        "OwnerService" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=67, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_67_0(Etw):
    pattern = Struct(
        "PortNameLen" / Int32ul,
        "PortName" / Bytes(lambda this: this.PortNameLen),
        "PortFNameLen" / Int32ul,
        "PortFName" / Bytes(lambda this: this.PortFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "Flags" / Int32ul,
        "OwnerService" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=68, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_68_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "PortNameLen" / Int32ul,
        "PortName" / Bytes(lambda this: this.PortNameLen),
        "PortFNameLen" / Int32ul,
        "PortFName" / Bytes(lambda this: this.PortFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "UniqueEvent" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=69, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_69_0(Etw):
    pattern = Struct(
        "PortNameLen" / Int32ul,
        "PortName" / Bytes(lambda this: this.PortNameLen),
        "PortFNameLen" / Int32ul,
        "PortFName" / Bytes(lambda this: this.PortFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "Flags" / Int32ul,
        "OwnerService" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=70, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_70_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "PortNameLen" / Int32ul,
        "PortName" / Bytes(lambda this: this.PortNameLen),
        "PortFNameLen" / Int32ul,
        "PortFName" / Bytes(lambda this: this.PortFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "UniqueEvent" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=71, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_71_0(Etw):
    pattern = Struct(
        "PortNameLen" / Int32ul,
        "PortName" / Bytes(lambda this: this.PortNameLen),
        "PortFNameLen" / Int32ul,
        "PortFName" / Bytes(lambda this: this.PortFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "Flags" / Int32ul,
        "OwnerService" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=72, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_72_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "PortNameLen" / Int32ul,
        "PortName" / Bytes(lambda this: this.PortNameLen),
        "PortFNameLen" / Int32ul,
        "PortFName" / Bytes(lambda this: this.PortFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "UniqueEvent" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=73, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_73_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "PortNameLen" / Int32ul,
        "PortName" / Bytes(lambda this: this.PortNameLen),
        "PortFNameLen" / Int32ul,
        "PortFName" / Bytes(lambda this: this.PortFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "UniqueEvent" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=74, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_74_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "PortNameLen" / Int32ul,
        "PortName" / Bytes(lambda this: this.PortNameLen),
        "PortFNameLen" / Int32ul,
        "PortFName" / Bytes(lambda this: this.PortFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "UniqueEvent" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=75, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_75_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "PortNameLen" / Int32ul,
        "PortName" / Bytes(lambda this: this.PortNameLen),
        "PortFNameLen" / Int32ul,
        "PortFName" / Bytes(lambda this: this.PortFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "UniqueEvent" / Int32ul,
        "Operation" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=76, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_76_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "Operation" / Int32ul,
        "UniqueEvent" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=77, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_77_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "UniqueEvent" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=78, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_78_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "PortNameLen" / Int32ul,
        "PortName" / Bytes(lambda this: this.PortNameLen),
        "PortFNameLen" / Int32ul,
        "PortFName" / Bytes(lambda this: this.PortFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "PropertyId" / Guid,
        "InstanceId" / Guid,
        "UniqueEvent" / Int32ul,
        "Operation" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=79, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_79_0(Etw):
    pattern = Struct(
        "PortNameLen" / Int32ul,
        "PortName" / Bytes(lambda this: this.PortNameLen),
        "PortFNameLen" / Int32ul,
        "PortFName" / Bytes(lambda this: this.PortFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "PropertyId" / Guid,
        "InstanceId" / Guid,
        "Operation" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=80, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_80_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "PropertyId" / Guid,
        "InstanceId" / Guid,
        "UniqueEvent" / Int32ul,
        "Operation" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=81, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_81_0(Etw):
    pattern = Struct(
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "PropertyId" / Guid,
        "InstanceId" / Guid,
        "Operation" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=82, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_82_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "PortNameLen" / Int32ul,
        "PortName" / Bytes(lambda this: this.PortNameLen),
        "PortFNameLen" / Int32ul,
        "PortFName" / Bytes(lambda this: this.PortFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "Reservation" / Int64sl,
        "Weight" / Int64sl,
        "Limit" / Int64sl,
        "BurstLimit" / Int64sl,
        "BurstSize" / Int64sl,
        "FailReason" / Int32ul,
        "Operation" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=83, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_83_0(Etw):
    pattern = Struct(
        "PortNameLen" / Int32ul,
        "PortName" / Bytes(lambda this: this.PortNameLen),
        "PortFNameLen" / Int32ul,
        "PortFName" / Bytes(lambda this: this.PortFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "Reservation" / Int64sl,
        "Weight" / Int64sl,
        "Limit" / Int64sl,
        "BurstLimit" / Int64sl,
        "BurstSize" / Int64sl,
        "Operation" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=84, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_84_0(Etw):
    pattern = Struct(
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "Status" / Int32ul,
        "Reservation" / Int64sl,
        "Weight" / Int64sl
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=85, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_85_0(Etw):
    pattern = Struct(
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "Status" / Int32ul,
        "Reservation" / Int64sl,
        "Weight" / Int64sl
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=86, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_86_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "PortNameLen" / Int32ul,
        "PortName" / Bytes(lambda this: this.PortNameLen),
        "PortFNameLen" / Int32ul,
        "PortFName" / Bytes(lambda this: this.PortFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "PropertyId" / Guid,
        "InstanceId" / Guid,
        "UniqueEvent" / Int32ul,
        "Operation" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=87, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_87_0(Etw):
    pattern = Struct(
        "PortNameLen" / Int32ul,
        "PortName" / Bytes(lambda this: this.PortNameLen),
        "PortFNameLen" / Int32ul,
        "PortFName" / Bytes(lambda this: this.PortFNameLen),
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen)
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=88, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_88_0(Etw):
    pattern = Struct(
        "PortNameLen" / Int32ul,
        "PortName" / Bytes(lambda this: this.PortNameLen),
        "PortFNameLen" / Int32ul,
        "PortFName" / Bytes(lambda this: this.PortFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "AllowMacSpoofing" / Int8ul,
        "EnableDhcpGuard" / Int8ul,
        "EnableRouterGuard" / Int8ul,
        "MonitorMode" / Int32ul,
        "MonitorSession" / Int32ul,
        "AllowIeeePriorityTag" / Int8ul,
        "VirtualSubnetId" / Int32ul,
        "AllowTeaming" / Int8ul,
        "StormLimit" / Int32ul,
        "DynamicIPAddressLimit" / Int32ul,
        "EnableFixSpeed10G" / Int8ul,
        "FailReason" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=89, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_89_0(Etw):
    pattern = Struct(
        "PortNameLen" / Int32ul,
        "PortName" / Bytes(lambda this: this.PortNameLen),
        "PortFNameLen" / Int32ul,
        "PortFName" / Bytes(lambda this: this.PortFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "AllowMacSpoofing" / Int8ul,
        "EnableDhcpGuard" / Int8ul,
        "EnableRouterGuard" / Int8ul,
        "MonitorMode" / Int32ul,
        "MonitorSession" / Int32ul,
        "AllowIeeePriorityTag" / Int8ul,
        "VirtualSubnetId" / Int32ul,
        "AllowTeaming" / Int8ul,
        "StormLimit" / Int32ul,
        "DynamicIPAddressLimit" / Int32ul,
        "EnableFixSpeed10G" / Int8ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=90, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_90_0(Etw):
    pattern = Struct(
        "PortNameLen" / Int32ul,
        "PortName" / Bytes(lambda this: this.PortNameLen),
        "PortFNameLen" / Int32ul,
        "PortFName" / Bytes(lambda this: this.PortFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "Direction" / Int32ul,
        "Applicability" / Int32ul,
        "Type" / Int32ul,
        "Action" / Int32ul,
        "LocalAddrLen" / Int32ul,
        "LocalAddr" / Bytes(lambda this: this.LocalAddrLen),
        "LocalPrefix" / Int32ul,
        "RemoteAddrLen" / Int32ul,
        "RemoteAddr" / Bytes(lambda this: this.RemoteAddrLen),
        "RemotePrefix" / Int32ul,
        "FailReason" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=91, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_91_0(Etw):
    pattern = Struct(
        "PortNameLen" / Int32ul,
        "PortName" / Bytes(lambda this: this.PortNameLen),
        "PortFNameLen" / Int32ul,
        "PortFName" / Bytes(lambda this: this.PortFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "Direction" / Int32ul,
        "Applicability" / Int32ul,
        "Type" / Int32ul,
        "Action" / Int32ul,
        "LocalAddrLen" / Int32ul,
        "LocalAddr" / Bytes(lambda this: this.LocalAddrLen),
        "LocalPrefix" / Int32ul,
        "RemoteAddrLen" / Int32ul,
        "RemoteAddr" / Bytes(lambda this: this.RemoteAddrLen),
        "RemotePrefix" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=92, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_92_0(Etw):
    pattern = Struct(
        "PortNameLen" / Int32ul,
        "PortName" / Bytes(lambda this: this.PortNameLen),
        "PortFNameLen" / Int32ul,
        "PortFName" / Bytes(lambda this: this.PortFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "PropertyId" / Guid,
        "InstanceId" / Guid,
        "Operation" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=93, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_93_0(Etw):
    pattern = Struct(
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "PropertyId" / Guid,
        "InstanceId" / Guid,
        "Operation" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=94, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_94_0(Etw):
    pattern = Struct(
        "PortNameLen" / Int32ul,
        "PortName" / Bytes(lambda this: this.PortNameLen),
        "PortFNameLen" / Int32ul,
        "PortFName" / Bytes(lambda this: this.PortFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "IPSecOffloadLimit" / Int32ul,
        "VMQOffloadWeight" / Int32ul,
        "IovOffloadWeight" / Int32ul,
        "QueuePairs" / Int32ul,
        "InterruptModeration" / Int32ul,
        "FailReason" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=95, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_95_0(Etw):
    pattern = Struct(
        "PortNameLen" / Int32ul,
        "PortName" / Bytes(lambda this: this.PortNameLen),
        "PortFNameLen" / Int32ul,
        "PortFName" / Bytes(lambda this: this.PortFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "FailReason" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=96, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_96_0(Etw):
    pattern = Struct(
        "PortNameLen" / Int32ul,
        "PortName" / Bytes(lambda this: this.PortNameLen),
        "PortFNameLen" / Int32ul,
        "PortFName" / Bytes(lambda this: this.PortFNameLen),
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen)
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=97, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_97_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "FailReason" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=98, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_98_0(Etw):
    pattern = Struct(
        "ExtensionId" / Guid,
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "PortNameLen" / Int32ul,
        "PortName" / Bytes(lambda this: this.PortNameLen),
        "PortFNameLen" / Int32ul,
        "PortFName" / Bytes(lambda this: this.PortFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen)
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=99, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_99_0(Etw):
    pattern = Struct(
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "PortNameLen" / Int32ul,
        "PortName" / Bytes(lambda this: this.PortNameLen),
        "PortFNameLen" / Int32ul,
        "PortFName" / Bytes(lambda this: this.PortFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen)
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=100, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_100_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "Reservation" / Int64sl,
        "Weight" / Int64sl,
        "FailReason" / Int32ul,
        "Operation" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=101, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_101_0(Etw):
    pattern = Struct(
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "Reservation" / Int64sl,
        "Weight" / Int64sl,
        "Operation" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=102, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_102_0(Etw):
    pattern = Struct(
        "VMNameLen" / Int32ul,
        "VMName" / Bytes(lambda this: this.VMNameLen),
        "VMIdLen" / Int32ul,
        "VMId" / Bytes(lambda this: this.VMIdLen)
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=103, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_103_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "PropertyId" / Guid,
        "InstanceId" / Guid,
        "UniqueEvent" / Int32ul,
        "Operation" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=104, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_104_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "Operation" / Int32ul,
        "UniqueEvent" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=105, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_105_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "PortNameLen" / Int32ul,
        "PortName" / Bytes(lambda this: this.PortNameLen),
        "PortFNameLen" / Int32ul,
        "PortFName" / Bytes(lambda this: this.PortFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "UniqueEvent" / Int32ul,
        "Operation" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=106, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_106_0(Etw):
    pattern = Struct(
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "QueueMode" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=107, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_107_0(Etw):
    pattern = Struct(
        "DataOidTarget" / Int32ul,
        "Oid" / Int32ul,
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen)
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=108, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_108_0(Etw):
    pattern = Struct(
        "DataOidTarget" / Int32ul,
        "Oid" / Int32ul,
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "Status" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=109, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_109_0(Etw):
    pattern = Struct(
        "DataOidTarget" / Int32ul,
        "Oid" / Int32ul,
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "SrcNicNameLen" / Int32ul,
        "SrcNicName" / Bytes(lambda this: this.SrcNicNameLen),
        "SrcNicFNameLen" / Int32ul,
        "SrcNicFName" / Bytes(lambda this: this.SrcNicFNameLen),
        "SrcNicIndex" / Int32ul,
        "DstNicNameLen" / Int32ul,
        "DstNicName" / Bytes(lambda this: this.DstNicNameLen),
        "DstNicFNameLen" / Int32ul,
        "DstNicFName" / Bytes(lambda this: this.DstNicFNameLen),
        "DstNicIndex" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=110, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_110_0(Etw):
    pattern = Struct(
        "DataOidTarget" / Int32ul,
        "Oid" / Int32ul,
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "SrcNicNameLen" / Int32ul,
        "SrcNicName" / Bytes(lambda this: this.SrcNicNameLen),
        "SrcNicFNameLen" / Int32ul,
        "SrcNicFName" / Bytes(lambda this: this.SrcNicFNameLen),
        "SrcNicIndex" / Int32ul,
        "DstNicNameLen" / Int32ul,
        "DstNicName" / Bytes(lambda this: this.DstNicNameLen),
        "DstNicFNameLen" / Int32ul,
        "DstNicFName" / Bytes(lambda this: this.DstNicFNameLen),
        "DstNicIndex" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=111, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_111_0(Etw):
    pattern = Struct(
        "StatusTarget" / Int32ul,
        "Oid" / Int32ul,
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen)
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=112, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_112_0(Etw):
    pattern = Struct(
        "StatusTarget" / Int32ul,
        "Oid" / Int32ul,
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "SrcNicNameLen" / Int32ul,
        "SrcNicName" / Bytes(lambda this: this.SrcNicNameLen),
        "SrcNicFNameLen" / Int32ul,
        "SrcNicFName" / Bytes(lambda this: this.SrcNicFNameLen),
        "SrcNicIndex" / Int32ul,
        "DstNicNameLen" / Int32ul,
        "DstNicName" / Bytes(lambda this: this.DstNicNameLen),
        "DstNicFNameLen" / Int32ul,
        "DstNicFName" / Bytes(lambda this: this.DstNicFNameLen),
        "DstNicIndex" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=113, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_113_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "FailReason" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=114, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_114_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "FailReason" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=115, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_115_0(Etw):
    pattern = Struct(
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen)
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=116, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_116_0(Etw):
    pattern = Struct(
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "NicIndex" / Int32ul,
        "NetCfgInstanceId" / Guid,
        "Status" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=117, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_117_0(Etw):
    pattern = Struct(
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "NicIndex" / Int32ul,
        "NetCfgInstanceId" / Guid,
        "Status" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=118, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_118_0(Etw):
    pattern = Struct(
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "ConfigurationType" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=119, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_119_0(Etw):
    pattern = Struct(
        "PortNameLen" / Int32ul,
        "PortName" / Bytes(lambda this: this.PortNameLen),
        "PortFNameLen" / Int32ul,
        "PortFName" / Bytes(lambda this: this.PortFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen)
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=120, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_120_0(Etw):
    pattern = Struct(
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen)
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=121, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_121_0(Etw):
    pattern = Struct(
        "PortNameLen" / Int32ul,
        "PortName" / Bytes(lambda this: this.PortNameLen),
        "PortFNameLen" / Int32ul,
        "PortFName" / Bytes(lambda this: this.PortFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen)
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=122, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_122_0(Etw):
    pattern = Struct(
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "QueueMode" / Int32ul,
        "Status" / Int32ul,
        "FailReason" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=123, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_123_0(Etw):
    pattern = Struct(
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "LinkSpeed" / Int64ul,
        "VmqSupported" / Int8ul,
        "dynamicVmqSupported" / Int8ul,
        "QueueMode" / Int32ul,
        "EnabledFilterTypes" / Int32ul,
        "EnabledQueueTypes" / Int32ul,
        "SupportedQueueProperties" / Int32ul,
        "SupportedFilterTests" / Int32ul,
        "SupportedHeaders" / Int32ul,
        "SupportedMacHeaderFields" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=124, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_124_0(Etw):
    pattern = Struct(
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen)
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=125, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_125_0(Etw):
    pattern = Struct(
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen)
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=126, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_126_0(Etw):
    pattern = Struct(
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen)
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=127, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_127_0(Etw):
    pattern = Struct(
        "PortNameLen" / Int32ul,
        "PortName" / Bytes(lambda this: this.PortNameLen),
        "PortFNameLen" / Int32ul,
        "PortFName" / Bytes(lambda this: this.PortFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "FailReason" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=128, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_128_0(Etw):
    pattern = Struct(
        "PortNameLen" / Int32ul,
        "PortName" / Bytes(lambda this: this.PortNameLen),
        "PortFNameLen" / Int32ul,
        "PortFName" / Bytes(lambda this: this.PortFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "FailReason" / Int32ul,
        "Ext1" / Int32ul,
        "Ext2" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=129, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_129_0(Etw):
    pattern = Struct(
        "PortNameLen" / Int32ul,
        "PortName" / Bytes(lambda this: this.PortNameLen),
        "PortFNameLen" / Int32ul,
        "PortFName" / Bytes(lambda this: this.PortFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "FailReason" / Int32ul,
        "RoutingDomainGuidLen" / Int32ul,
        "RoutingDomainGuid" / Bytes(lambda this: this.RoutingDomainGuidLen),
        "RoutingDomainNameLen" / Int32ul,
        "RoutingDomainName" / Bytes(lambda this: this.RoutingDomainNameLen),
        "Ext1" / Int32ul,
        "Ext2" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=130, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_130_0(Etw):
    pattern = Struct(
        "PortNameLen" / Int32ul,
        "PortName" / Bytes(lambda this: this.PortNameLen),
        "PortFNameLen" / Int32ul,
        "PortFName" / Bytes(lambda this: this.PortFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "Direction" / Int32ul,
        "Action" / Int32ul,
        "LocalIPAddrLen" / Int32ul,
        "LocalIPAddr" / Bytes(lambda this: this.LocalIPAddrLen),
        "RemoteIPAddrLen" / Int32ul,
        "RemoteIPAddr" / Bytes(lambda this: this.RemoteIPAddrLen),
        "LocalPortLen" / Int32ul,
        "LocalPort" / Bytes(lambda this: this.LocalPortLen),
        "RemotePortLen" / Int32ul,
        "RemotePort" / Bytes(lambda this: this.RemotePortLen),
        "Protocol" / Int32ul,
        "Weight" / Int32ul,
        "Stateful" / Int8ul,
        "IdleSessionTimeout" / Int32ul,
        "VirtualSubnetId" / Int32ul,
        "FailReason" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=131, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_131_0(Etw):
    pattern = Struct(
        "PortNameLen" / Int32ul,
        "PortName" / Bytes(lambda this: this.PortNameLen),
        "PortFNameLen" / Int32ul,
        "PortFName" / Bytes(lambda this: this.PortFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "Direction" / Int32ul,
        "Weight" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=132, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_132_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "UniqueEvent" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=133, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_133_0(Etw):
    pattern = Struct(
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "ProcIndex" / Int32ul,
        "VmqIndex" / Int32ul,
        "RssQueueIndex" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=134, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_134_0(Etw):
    pattern = Struct(
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "ProcIndex" / Int32ul,
        "VmqIndex" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=135, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_135_0(Etw):
    pattern = Struct(
        "ProcIndex" / Int32ul,
        "ProcUtil" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=136, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_136_0(Etw):
    pattern = Struct(
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "VmqIndex" / Int32ul,
        "RssQueueIndex" / Int32ul,
        "ProcIndex" / Int32ul,
        "QueueLoad" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=137, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_137_0(Etw):
    pattern = Struct(
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "VmqIndex" / Int32ul,
        "RssQueueIndex" / Int32ul,
        "ProcIndex" / Int32ul,
        "QueueLoad" / Int32ul,
        "SafeThreshold" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=138, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_138_0(Etw):
    pattern = Struct(
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "VmqIndex" / Int32ul,
        "ProcIndex" / Int32ul,
        "QueueLoad" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=139, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_139_0(Etw):
    pattern = Struct(
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "VmqIndex" / Int32ul,
        "ProcIndex" / Int32ul,
        "QueueLoad" / Int32ul,
        "SafeThreshold" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=140, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_140_0(Etw):
    pattern = Struct(
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "VmqIndex" / Int32ul,
        "RssQueueIndex" / Int32ul,
        "ReceiveProcIndex" / Int32ul,
        "SendProcIndex" / Int32ul,
        "DestinationReceiveProcIndex" / Int32ul,
        "DestinationSendProcIndex" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=141, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_141_0(Etw):
    pattern = Struct(
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "IsActivate" / Int32ul,
        "VmqIndex" / Int32ul,
        "ProcIndex" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=142, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_142_0(Etw):
    pattern = Struct(
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "FailReason" / Int32ul,
        "Status" / Int32ul,
        "Flags" / Int32ul,
        "BaseCpuNumber" / Int32ul,
        "HashInformation" / Int32ul,
        "IndirectionTableSize" / Int32ul,
        "IndirectionTableOffset" / Int32ul,
        "HashSecretKeySize" / Int32ul,
        "HashSecretKeyOffset" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=143, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_143_0(Etw):
    pattern = Struct(
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "Flags" / Int32ul,
        "BaseCpuNumber" / Int32ul,
        "HashInformation" / Int32ul,
        "IndirectionTableSize" / Int32ul,
        "IndirectionTableOffset" / Int32ul,
        "HashSecretKeySize" / Int32ul,
        "HashSecretKeyOffset" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=144, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_144_0(Etw):
    pattern = Struct(
        "FailReason" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=145, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_145_0(Etw):
    pattern = Struct(
        "FailReason" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=146, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_146_0(Etw):
    pattern = Struct(
        "FailReason" / Int32ul,
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "PtNicNameLen" / Int32ul,
        "PtNicName" / Bytes(lambda this: this.PtNicNameLen),
        "PtNicFNameLen" / Int32ul,
        "PtNicFName" / Bytes(lambda this: this.PtNicFNameLen)
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=147, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_147_0(Etw):
    pattern = Struct(
        "FailReason" / Int32ul,
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "PtNicNameLen" / Int32ul,
        "PtNicName" / Bytes(lambda this: this.PtNicNameLen),
        "PtNicFNameLen" / Int32ul,
        "PtNicFName" / Bytes(lambda this: this.PtNicFNameLen)
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=148, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_148_0(Etw):
    pattern = Struct(
        "FailReason" / Int32ul,
        "NdisOid" / Int32ul,
        "Status" / Int32ul,
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "PtNicNameLen" / Int32ul,
        "PtNicName" / Bytes(lambda this: this.PtNicNameLen),
        "PtNicFNameLen" / Int32ul,
        "PtNicFName" / Bytes(lambda this: this.PtNicFNameLen)
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=149, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_149_0(Etw):
    pattern = Struct(
        "FailReason" / Int32ul,
        "NetEvent" / Int32ul,
        "Status" / Int32ul,
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen)
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=150, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_150_0(Etw):
    pattern = Struct(
        "FailReason" / Int32ul,
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "PtNicNameLen" / Int32ul,
        "PtNicName" / Bytes(lambda this: this.PtNicNameLen),
        "PtNicFNameLen" / Int32ul,
        "PtNicFName" / Bytes(lambda this: this.PtNicFNameLen)
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=151, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_151_0(Etw):
    pattern = Struct(
        "FailReason" / Int32ul,
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "PtNicNameLen" / Int32ul,
        "PtNicName" / Bytes(lambda this: this.PtNicNameLen),
        "PtNicFNameLen" / Int32ul,
        "PtNicFName" / Bytes(lambda this: this.PtNicFNameLen)
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=152, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_152_0(Etw):
    pattern = Struct(
        "OldMember" / Guid,
        "NewMember" / Guid
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=153, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_153_0(Etw):
    pattern = Struct(
        "Member" / Guid,
        "Status" / Int32sl
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=154, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_154_0(Etw):
    pattern = Struct(
        "Member" / Guid,
        "Status" / Int32sl
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=155, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_155_0(Etw):
    pattern = Struct(
        "Member" / Guid,
        "Status" / Int32sl
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=156, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_156_0(Etw):
    pattern = Struct(
        "Member" / Guid,
        "Status" / Int32sl
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=157, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_157_0(Etw):
    pattern = Struct(
        "TeamNic" / Int64ul,
        "Member" / Guid
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=158, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_158_0(Etw):
    pattern = Struct(
        "Member" / Guid,
        "Status" / Int32sl
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=159, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_159_0(Etw):
    pattern = Struct(
        "TeamNic" / Int64ul,
        "Status" / Int32sl
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=160, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_160_0(Etw):
    pattern = Struct(
        "Member" / Guid,
        "Status" / Int32sl
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=161, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_161_0(Etw):
    pattern = Struct(
        "Status" / Int32sl
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=162, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_162_0(Etw):
    pattern = Struct(
        "Member" / Guid,
        "Status" / Int32sl
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=163, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_163_0(Etw):
    pattern = Struct(
        "Aggregator" / Int64ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=164, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_164_0(Etw):
    pattern = Struct(
        "TeamNic" / Int64ul,
        "Member" / Guid,
        "Status" / Int32sl
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=165, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_165_0(Etw):
    pattern = Struct(
        "TeamNic" / Int64ul,
        "StatusBufferLen" / Int32ul,
        "StatusBuffer" / Bytes(lambda this: this.StatusBufferLen)
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=166, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_166_0(Etw):
    pattern = Struct(
        "TeamNic" / Int64ul,
        "Receiver" / Int64ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=167, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_167_0(Etw):
    pattern = Struct(
        "TeamNic" / Int64ul,
        "Receiver" / Int64ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=168, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_168_0(Etw):
    pattern = Struct(
        "TeamNic" / Int64ul,
        "Status" / Int32sl
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=169, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_169_0(Etw):
    pattern = Struct(
        "TeamNic" / Int64ul,
        "Aggregator" / Int64ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=170, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_170_0(Etw):
    pattern = Struct(
        "TeamNic" / Int64ul,
        "Member" / Guid,
        "Status" / Int32sl
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=171, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_171_0(Etw):
    pattern = Struct(
        "TeamNic" / Int64ul,
        "Status" / Int32sl
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=173, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_173_0(Etw):
    pattern = Struct(
        "Member" / Guid,
        "OldAggregator" / Int64ul,
        "NewAggregator" / Int64ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=174, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_174_0(Etw):
    pattern = Struct(
        "Member" / Guid,
        "Status" / Int32sl
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=175, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_175_0(Etw):
    pattern = Struct(
        "Member" / Guid,
        "Status" / Int32sl
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=176, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_176_0(Etw):
    pattern = Struct(
        "Member" / Guid,
        "BufferLen" / Int32ul,
        "Buffer" / Bytes(lambda this: this.BufferLen)
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=177, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_177_0(Etw):
    pattern = Struct(
        "Member" / Guid,
        "OldState" / Int32ul,
        "NewState" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=178, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_178_0(Etw):
    pattern = Struct(
        "Member" / Guid,
        "OldState" / Int32ul,
        "NewState" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=179, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_179_0(Etw):
    pattern = Struct(
        "Member" / Guid,
        "OldState" / Int32ul,
        "NewState" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=180, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_180_0(Etw):
    pattern = Struct(
        "Member" / Guid,
        "BufferLen" / Int32ul,
        "Buffer" / Bytes(lambda this: this.BufferLen)
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=181, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_181_0(Etw):
    pattern = Struct(
        "Member" / Guid,
        "OldAggregator" / Int64ul,
        "NewAggregator" / Int64ul,
        "Ready" / Int8ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=182, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_182_0(Etw):
    pattern = Struct(
        "Member" / Guid,
        "OldAggregator" / Int64ul,
        "NewAggregator" / Int64ul,
        "Ready" / Int8ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=183, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_183_0(Etw):
    pattern = Struct(
        "Member" / Guid,
        "ChurnType" / Int32sl,
        "OldState" / Int32sl,
        "NewState" / Int32sl
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=184, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_184_0(Etw):
    pattern = Struct(
        "DriverObject" / WString,
        "Member" / WString
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=185, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_185_0(Etw):
    pattern = Struct(
        "DriverObject" / WString,
        "Member" / WString
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=186, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_186_0(Etw):
    pattern = Struct(
        "DriverObject" / WString,
        "Member" / WString
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=187, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_187_0(Etw):
    pattern = Struct(
        "DriverObject" / WString,
        "Member" / WString
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=188, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_188_0(Etw):
    pattern = Struct(
        "DriverObject" / WString,
        "Member" / WString
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=189, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_189_0(Etw):
    pattern = Struct(
        "DriverObject" / WString,
        "Member" / WString
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=190, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_190_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "UniqueEvent" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=191, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_191_0(Etw):
    pattern = Struct(
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen)
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=192, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_192_0(Etw):
    pattern = Struct(
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen)
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=193, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_193_0(Etw):
    pattern = Struct(
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen)
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=194, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_194_0(Etw):
    pattern = Struct(
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "Operation" / Int32ul,
        "FailureCode" / Int32ul,
        "FailureReason" / Int32ul,
        "Ext1" / Int32ul,
        "Ext2" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=195, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_195_0(Etw):
    pattern = Struct(
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "Operation" / Int32ul,
        "FailureCode" / Int32ul,
        "FailureReason" / Int32ul,
        "Ext1" / Int32ul,
        "HeaderType" / Int32ul,
        "HeaderRevision" / Int32ul,
        "HeaderSize" / Int32ul,
        "ExtensionId" / Guid,
        "FeatureId" / Guid,
        "SaveDataSize" / Int32ul,
        "SaveDataSizeOverflow" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=196, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_196_0(Etw):
    pattern = Struct(
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "Operation" / Int32ul,
        "FailureCode" / Int32ul,
        "FailureReason" / Int32ul,
        "Ext1" / Int32ul,
        "HeaderType" / Int32ul,
        "HeaderRevision" / Int32ul,
        "HeaderSize" / Int32ul,
        "ExtensionId" / Guid,
        "FeatureId" / Guid,
        "SaveDataSize" / Int32ul,
        "SaveDataSizeOverflow" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=197, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_197_0(Etw):
    pattern = Struct(
        "VlanID" / Int32ul,
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "FailReason" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=198, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_198_0(Etw):
    pattern = Struct(
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "Status" / Int32ul,
        "FailureReason" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=199, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_199_0(Etw):
    pattern = Struct(
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "Status" / Int32ul,
        "FailureReason" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=200, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_200_0(Etw):
    pattern = Struct(
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "Status" / Int32ul,
        "FailureReason" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=201, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_201_0(Etw):
    pattern = Struct(
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "Status" / Int32ul,
        "FailureReason" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=202, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_202_0(Etw):
    pattern = Struct(
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen)
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=203, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_203_0(Etw):
    pattern = Struct(
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen)
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=204, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_204_0(Etw):
    pattern = Struct(
        "FilterId" / Int32ul,
        "vPortId" / Int32ul,
        "Status" / Int32ul,
        "VportsSupported" / Int8ul,
        "EmbeddedTeaming" / Int8ul,
        "NicIndex" / Int32ul,
        "DstVPortId" / Int32ul,
        "VlanId" / Int32ul,
        "MacLength" / Int32ul,
        "MacAddress" / Bytes(lambda this: this.MacLength)
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=205, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_205_0(Etw):
    pattern = Struct(
        "FilterId" / Int32ul,
        "SrcVPortId" / Int32ul,
        "Status" / Int32ul,
        "VportsSupported" / Int8ul,
        "EmbeddedTeaming" / Int8ul,
        "NicIndex" / Int32ul,
        "DstVPortId" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=206, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_206_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFriendlyNameLen" / Int32ul,
        "SwitchFriendlyName" / Bytes(lambda this: this.SwitchFriendlyNameLen),
        "TeamingMode" / Int32ul,
        "LoadBalancingAlgorithm" / Int32ul,
        "VmqSumOfQueues" / Int8ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=207, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_207_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFriendlyNameLen" / Int32ul,
        "SwitchFriendlyName" / Bytes(lambda this: this.SwitchFriendlyNameLen),
        "TeamingMode" / Int32ul,
        "LoadBalancingAlgorithm" / Int32ul,
        "VmqSumOfQueues" / Int8ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=208, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_208_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFriendlyNameLen" / Int32ul,
        "SwitchFriendlyName" / Bytes(lambda this: this.SwitchFriendlyNameLen),
        "TeamingMode" / Int32ul,
        "LoadBalancingAlgorithm" / Int32ul,
        "VmqSumOfQueues" / Int8ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=209, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_209_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFriendlyNameLen" / Int32ul,
        "SwitchFriendlyName" / Bytes(lambda this: this.SwitchFriendlyNameLen),
        "TeamingMode" / Int32ul,
        "LoadBalancingAlgorithm" / Int32ul,
        "VmqSumOfQueues" / Int8ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=210, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_210_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFriendlyNameLen" / Int32ul,
        "SwitchFriendlyName" / Bytes(lambda this: this.SwitchFriendlyNameLen),
        "TeamingMode" / Int32ul,
        "LoadBalancingAlgorithm" / Int32ul,
        "VmqSumOfQueues" / Int8ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=211, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_211_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFriendlyNameLen" / Int32ul,
        "SwitchFriendlyName" / Bytes(lambda this: this.SwitchFriendlyNameLen),
        "TeamingMode" / Int32ul,
        "LoadBalancingAlgorithm" / Int32ul,
        "VmqSumOfQueues" / Int8ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=212, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_212_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFriendlyNameLen" / Int32ul,
        "SwitchFriendlyName" / Bytes(lambda this: this.SwitchFriendlyNameLen),
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFriendlyNameLen" / Int32ul,
        "NicFriendlyName" / Bytes(lambda this: this.NicFriendlyNameLen),
        "NicIndex" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=213, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_213_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFriendlyNameLen" / Int32ul,
        "SwitchFriendlyName" / Bytes(lambda this: this.SwitchFriendlyNameLen),
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFriendlyNameLen" / Int32ul,
        "NicFriendlyName" / Bytes(lambda this: this.NicFriendlyNameLen),
        "NicIndex" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=214, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_214_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFriendlyNameLen" / Int32ul,
        "SwitchFriendlyName" / Bytes(lambda this: this.SwitchFriendlyNameLen),
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFriendlyNameLen" / Int32ul,
        "NicFriendlyName" / Bytes(lambda this: this.NicFriendlyNameLen),
        "NicIndex" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=215, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_215_0(Etw):
    pattern = Struct(
        "FilterId" / Int32ul,
        "vPortId" / Int32ul,
        "Status" / Int32ul,
        "VportsSupported" / Int8ul,
        "EmbeddedTeaming" / Int8ul,
        "NicIndex" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=216, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_216_0(Etw):
    pattern = Struct(
        "FailReason" / Int32ul,
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "PtNicNameLen" / Int32ul,
        "PtNicName" / Bytes(lambda this: this.PtNicNameLen),
        "PtNicFNameLen" / Int32ul,
        "PtNicFName" / Bytes(lambda this: this.PtNicFNameLen)
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=217, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_217_0(Etw):
    pattern = Struct(
        "FailReason" / Int32ul,
        "NetEvent" / Int32ul,
        "Status" / Int32ul,
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen)
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=218, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_218_0(Etw):
    pattern = Struct(
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "PortNameLen" / Int32ul,
        "PortName" / Bytes(lambda this: this.PortNameLen),
        "PortFNameLen" / Int32ul,
        "PortFName" / Bytes(lambda this: this.PortFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "RoutingDomainCount" / Int32ul,
        "MultiTenantStackEnabled" / Int8ul,
        "Status" / Int32ul,
        "Ext1" / Int32ul,
        "Ext2" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=219, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_219_0(Etw):
    pattern = Struct(
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "PortNameLen" / Int32ul,
        "PortName" / Bytes(lambda this: this.PortNameLen),
        "PortFNameLen" / Int32ul,
        "PortFName" / Bytes(lambda this: this.PortFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "RoutingDomainCount" / Int32ul,
        "MultiTenantStackEnabled" / Int8ul,
        "Status" / Int32ul,
        "Ext1" / Int32ul,
        "Ext2" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=220, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_220_0(Etw):
    pattern = Struct(
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "PortNameLen" / Int32ul,
        "PortName" / Bytes(lambda this: this.PortNameLen),
        "PortFNameLen" / Int32ul,
        "PortFName" / Bytes(lambda this: this.PortFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "NicStatus" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=221, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_221_0(Etw):
    pattern = Struct(
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "PortNameLen" / Int32ul,
        "PortName" / Bytes(lambda this: this.PortNameLen),
        "PortFNameLen" / Int32ul,
        "PortFName" / Bytes(lambda this: this.PortFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "ObjectState" / Int32ul,
        "NicState" / Int32ul,
        "NicPaused" / Int8ul,
        "BuffersNotReady" / Int8ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=222, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_222_0(Etw):
    pattern = Struct(
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "PortNameLen" / Int32ul,
        "PortName" / Bytes(lambda this: this.PortNameLen),
        "PortFNameLen" / Int32ul,
        "PortFName" / Bytes(lambda this: this.PortFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "ObjectState" / Int32ul,
        "NicState" / Int32ul,
        "NicPaused" / Int8ul,
        "BuffersNotReady" / Int8ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=223, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_223_0(Etw):
    pattern = Struct(
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen)
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=224, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_224_0(Etw):
    pattern = Struct(
        "PortNameLen" / Int32ul,
        "PortName" / Bytes(lambda this: this.PortNameLen),
        "PortFNameLen" / Int32ul,
        "PortFName" / Bytes(lambda this: this.PortFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen)
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=225, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_225_0(Etw):
    pattern = Struct(
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "FailReason" / Int32ul,
        "Status" / Int32ul,
        "Flags" / Int32ul,
        "BaseCpuNumber" / Int32ul,
        "HashInformation" / Int32ul,
        "IndirectionTableSize" / Int32ul,
        "IndirectionTableOffset" / Int32ul,
        "HashSecretKeySize" / Int32ul,
        "HashSecretKeyOffset" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=226, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_226_0(Etw):
    pattern = Struct(
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "Flags" / Int32ul,
        "BaseCpuNumber" / Int32ul,
        "HashInformation" / Int32ul,
        "IndirectionTableSize" / Int32ul,
        "IndirectionTableOffset" / Int32ul,
        "HashSecretKeySize" / Int32ul,
        "HashSecretKeyOffset" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=227, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_227_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "DefaultQueueVrssEnabled" / Int8ul,
        "DefaultQueueVmmqEnabled" / Int8ul,
        "DefaultQueueVrssMaxQueuePairs" / Int32sl,
        "DefaultQueueVrssMinQueuePairs" / Int32sl,
        "DefaultQueueVrssQueueSchedulingMode" / Int32ul,
        "DefaultQueueVrssExcludePrimaryProcessor" / Int8ul,
        "DefaultQueueVrssIndependentHostSpreading" / Int8ul,
        "FailReason" / Int32ul,
        "Operation" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=228, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_228_0(Etw):
    pattern = Struct(
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "DefaultQueueVrssEnabled" / Int8ul,
        "DefaultQueueVmmqEnabled" / Int8ul,
        "DefaultQueueVrssMaxQueuePairs" / Int32sl,
        "DefaultQueueVrssMinQueuePairs" / Int32sl,
        "DefaultQueueVrssQueueSchedulingMode" / Int32ul,
        "DefaultQueueVrssExcludePrimaryProcessor" / Int8ul,
        "DefaultQueueVrssIndependentHostSpreading" / Int8ul,
        "Operation" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=229, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_229_0(Etw):
    pattern = Struct(
        "FailReason" / Int32ul,
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFriendlyNameLen" / Int32ul,
        "SwitchFriendlyName" / Bytes(lambda this: this.SwitchFriendlyNameLen),
        "MemberAdapterNameLen" / Int32ul,
        "MemberAdapterName" / Bytes(lambda this: this.MemberAdapterNameLen),
        "MemberAdapterFriendlyNameLen" / Int32ul,
        "MemberAdapterFriendlyName" / Bytes(lambda this: this.MemberAdapterFriendlyNameLen),
        "NicIndex" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=230, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_230_0(Etw):
    pattern = Struct(
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFriendlyNameLen" / Int32ul,
        "SwitchFriendlyName" / Bytes(lambda this: this.SwitchFriendlyNameLen),
        "NvgreEnabled" / Int8ul,
        "VxLanEnabled" / Int8ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=231, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_231_0(Etw):
    pattern = Struct(
        "MacAddressLen" / Int32ul,
        "MacAddress" / Bytes(lambda this: this.MacAddressLen),
        "MemberAdapterNameLen" / Int32ul,
        "MemberAdapterName" / Bytes(lambda this: this.MemberAdapterNameLen),
        "MemberAdapterFriendlyNameLen" / Int32ul,
        "MemberAdapterFriendlyName" / Bytes(lambda this: this.MemberAdapterFriendlyNameLen),
        "TimeDiff" / Int64sl
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=232, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_232_0(Etw):
    pattern = Struct(
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "PortNameLen" / Int32ul,
        "PortName" / Bytes(lambda this: this.PortNameLen),
        "PortFNameLen" / Int32ul,
        "PortFName" / Bytes(lambda this: this.PortFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen)
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=233, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_233_0(Etw):
    pattern = Struct(
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "Operation" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=234, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_234_0(Etw):
    pattern = Struct(
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "PortNameLen" / Int32ul,
        "PortName" / Bytes(lambda this: this.PortNameLen)
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=235, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_235_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "PortNameLen" / Int32ul,
        "PortName" / Bytes(lambda this: this.PortNameLen),
        "UniqueEvent" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=236, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_236_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "UniqueEvent" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=237, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_237_0(Etw):
    pattern = Struct(
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "Reason" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=238, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_238_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "UniqueEvent" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=239, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_239_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "UniqueEvent" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=240, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_240_0(Etw):
    pattern = Struct(
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "BufferAddress" / Int64ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=241, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_241_0(Etw):
    pattern = Struct(
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "BufferAddress" / Int64ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=242, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_242_0(Etw):
    pattern = Struct(
        "SrcNicNameLen" / Int32ul,
        "SrcNicName" / Bytes(lambda this: this.SrcNicNameLen),
        "SrcNicFNameLen" / Int32ul,
        "SrcNicFName" / Bytes(lambda this: this.SrcNicFNameLen),
        "DestNicNameLen" / Int32ul,
        "DestNicName" / Bytes(lambda this: this.DestNicNameLen),
        "DestNicFNameLen" / Int32ul,
        "DestNicFName" / Bytes(lambda this: this.DestNicFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "BufferAddress" / Int64ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=243, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_243_0(Etw):
    pattern = Struct(
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "AvailableAddressFilters" / Int32ul,
        "RequestedVlanIDs" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=244, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_244_0(Etw):
    pattern = Struct(
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "AvailableAddressFilters" / Int32ul,
        "RequestedVlanIDs" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=245, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_245_0(Etw):
    pattern = Struct(
        "FilterId" / Int32ul,
        "vPortId" / Int32ul,
        "Status" / Int32ul,
        "VportsSupported" / Int8ul,
        "EmbeddedTeaming" / Int8ul,
        "NicIndex" / Int32ul,
        "DstVPortId" / Int32ul,
        "VlanId" / Int32ul,
        "MacLength" / Int32ul,
        "MacAddress" / Bytes(lambda this: this.MacLength)
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=246, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_246_0(Etw):
    pattern = Struct(
        "FilterId" / Int32ul,
        "SrcVPortId" / Int32ul,
        "Status" / Int32ul,
        "VportsSupported" / Int8ul,
        "EmbeddedTeaming" / Int8ul,
        "NicIndex" / Int32ul,
        "DstVPortId" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=247, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_247_0(Etw):
    pattern = Struct(
        "FilterId" / Int32ul,
        "vPortId" / Int32ul,
        "Status" / Int32ul,
        "VportsSupported" / Int8ul,
        "EmbeddedTeaming" / Int8ul,
        "NicIndex" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=248, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_248_0(Etw):
    pattern = Struct(
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "Status" / Int32ul,
        "FailureReason" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=249, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_249_0(Etw):
    pattern = Struct(
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "Status" / Int32ul,
        "FailureReason" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=250, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_250_0(Etw):
    pattern = Struct(
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "Status" / Int32ul,
        "FailureReason" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=251, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_251_0(Etw):
    pattern = Struct(
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "Status" / Int32ul,
        "FailureReason" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=252, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_252_0(Etw):
    pattern = Struct(
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "ProcessorIndex" / Int32ul,
        "QueueSizeMBytes" / Int32ul,
        "QueueLimitMBytes" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=253, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_253_0(Etw):
    pattern = Struct(
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "ProcessorIndex" / Int32ul,
        "QueueSizeMBytes" / Int32ul,
        "QueueLimitMBytes" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=254, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_254_0(Etw):
    pattern = Struct(
        "FailReason" / Int32ul,
        "NetEvent" / Int32ul,
        "Status" / Int32ul,
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen)
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=255, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_255_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "PortNameLen" / Int32ul,
        "PortName" / Bytes(lambda this: this.PortNameLen),
        "PortFNameLen" / Int32ul,
        "PortFName" / Bytes(lambda this: this.PortFNameLen),
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "RdmaWeight" / Int32ul,
        "FailReason" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=256, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_256_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "PortNameLen" / Int32ul,
        "PortName" / Bytes(lambda this: this.PortNameLen),
        "PortFNameLen" / Int32ul,
        "PortFName" / Bytes(lambda this: this.PortFNameLen),
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "RdmaWeight" / Int32ul,
        "FailReason" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=257, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_257_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "PortNameLen" / Int32ul,
        "PortName" / Bytes(lambda this: this.PortNameLen),
        "PortFNameLen" / Int32ul,
        "PortFName" / Bytes(lambda this: this.PortFNameLen),
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "RdmaWeight" / Int32ul,
        "FailReason" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=258, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_258_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "UniqueEvent" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=259, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_259_0(Etw):
    pattern = Struct(
        "NdisOid" / Int32ul,
        "OidFailureStatus" / Int32ul,
        "FailureMode" / Int32ul,
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "PtNicFNameLen" / Int32ul,
        "PtNicFName" / Bytes(lambda this: this.PtNicFNameLen)
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=260, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_260_0(Etw):
    pattern = Struct(
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "VmqIndex" / Int32ul,
        "RssQueueIndex" / Int16sl,
        "NdisStatus" / Int32sl
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=261, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_261_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "DropLowResourcesPackets" / Int8ul,
        "FailReason" / Int32ul,
        "Operation" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=262, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_262_0(Etw):
    pattern = Struct(
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "DropLowResourcesPackets" / Int8ul,
        "Operation" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=263, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_263_0(Etw):
    pattern = Struct(
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen)
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=264, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_264_0(Etw):
    pattern = Struct(
        "PortNameLen" / Int32ul,
        "PortName" / Bytes(lambda this: this.PortNameLen),
        "PortFNameLen" / Int32ul,
        "PortFName" / Bytes(lambda this: this.PortFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "Flags" / Int32ul,
        "OwnerService" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=265, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_265_0(Etw):
    pattern = Struct(
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen)
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=266, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_266_0(Etw):
    pattern = Struct(
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen)
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=267, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_267_0(Etw):
    pattern = Struct(
        "IoctlCode" / Int32ul,
        "ElapsedTime" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=268, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_268_0(Etw):
    pattern = Struct(
        "ConnectivityState" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=269, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_269_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "UniqueEvent" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=270, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_270_0(Etw):
    pattern = Struct(
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen)
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=275, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_275_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "PortNameLen" / Int32ul,
        "PortName" / Bytes(lambda this: this.PortNameLen),
        "PortFNameLen" / Int32ul,
        "PortFName" / Bytes(lambda this: this.PortFNameLen),
        "SwitchNameLen" / Int32ul,
        "SwitchName" / Bytes(lambda this: this.SwitchNameLen),
        "SwitchFNameLen" / Int32ul,
        "SwitchFName" / Bytes(lambda this: this.SwitchFNameLen),
        "UniqueEvent" / Int32ul
    )


@declare(guid=guid("67dc0d66-3695-47c0-9642-33f76f7bd7ad"), event_id=276, version=0)
class Microsoft_Windows_Hyper_V_VmSwitch_276_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "NicNameLen" / Int32ul,
        "NicName" / Bytes(lambda this: this.NicNameLen),
        "NicFNameLen" / Int32ul,
        "NicFName" / Bytes(lambda this: this.NicFNameLen),
        "UniqueEvent" / Int32ul
    )

