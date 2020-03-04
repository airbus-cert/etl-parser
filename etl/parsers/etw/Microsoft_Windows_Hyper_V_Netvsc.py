# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Hyper-V-NetVsc
GUID : 152fbe4b-c7ad-4f68-bada-a4fcc1464f6c
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("152fbe4b-c7ad-4f68-bada-a4fcc1464f6c"), event_id=1, version=0)
class Microsoft_Windows_Hyper_V_NetVsc_1_0(Etw):
    pattern = Struct(
        "VersionLen" / Int32ul,
        "Version" / Bytes(lambda this: this.VersionLen),
        "Status" / Int32ul
    )


@declare(guid=guid("152fbe4b-c7ad-4f68-bada-a4fcc1464f6c"), event_id=2, version=0)
class Microsoft_Windows_Hyper_V_NetVsc_2_0(Etw):
    pattern = Struct(
        "VersionLen" / Int32ul,
        "Version" / Bytes(lambda this: this.VersionLen),
        "Status" / Int32ul
    )


@declare(guid=guid("152fbe4b-c7ad-4f68-bada-a4fcc1464f6c"), event_id=3, version=0)
class Microsoft_Windows_Hyper_V_NetVsc_3_0(Etw):
    pattern = Struct(
        "MiniportNameLen" / Int32ul,
        "MiniportName" / Bytes(lambda this: this.MiniportNameLen)
    )


@declare(guid=guid("152fbe4b-c7ad-4f68-bada-a4fcc1464f6c"), event_id=4, version=0)
class Microsoft_Windows_Hyper_V_NetVsc_4_0(Etw):
    pattern = Struct(
        "MiniportNameLen" / Int32ul,
        "MiniportName" / Bytes(lambda this: this.MiniportNameLen),
        "Status" / Int32ul,
        "UniqueEventValue" / Int32ul
    )


@declare(guid=guid("152fbe4b-c7ad-4f68-bada-a4fcc1464f6c"), event_id=5, version=0)
class Microsoft_Windows_Hyper_V_NetVsc_5_0(Etw):
    pattern = Struct(
        "MiniportNameLen" / Int32ul,
        "MiniportName" / Bytes(lambda this: this.MiniportNameLen),
        "SubkeyNameLen" / Int32ul,
        "SubkeyName" / Bytes(lambda this: this.SubkeyNameLen),
        "Status" / Int32ul
    )


@declare(guid=guid("152fbe4b-c7ad-4f68-bada-a4fcc1464f6c"), event_id=6, version=0)
class Microsoft_Windows_Hyper_V_NetVsc_6_0(Etw):
    pattern = Struct(
        "MiniportNameLen" / Int32ul,
        "MiniportName" / Bytes(lambda this: this.MiniportNameLen)
    )


@declare(guid=guid("152fbe4b-c7ad-4f68-bada-a4fcc1464f6c"), event_id=7, version=0)
class Microsoft_Windows_Hyper_V_NetVsc_7_0(Etw):
    pattern = Struct(
        "MiniportNameLen" / Int32ul,
        "MiniportName" / Bytes(lambda this: this.MiniportNameLen)
    )


@declare(guid=guid("152fbe4b-c7ad-4f68-bada-a4fcc1464f6c"), event_id=8, version=0)
class Microsoft_Windows_Hyper_V_NetVsc_8_0(Etw):
    pattern = Struct(
        "MiniportNameLen" / Int32ul,
        "MiniportName" / Bytes(lambda this: this.MiniportNameLen)
    )


@declare(guid=guid("152fbe4b-c7ad-4f68-bada-a4fcc1464f6c"), event_id=9, version=0)
class Microsoft_Windows_Hyper_V_NetVsc_9_0(Etw):
    pattern = Struct(
        "MiniportNameLen" / Int32ul,
        "MiniportName" / Bytes(lambda this: this.MiniportNameLen)
    )


@declare(guid=guid("152fbe4b-c7ad-4f68-bada-a4fcc1464f6c"), event_id=10, version=0)
class Microsoft_Windows_Hyper_V_NetVsc_10_0(Etw):
    pattern = Struct(
        "MiniportNameLen" / Int32ul,
        "MiniportName" / Bytes(lambda this: this.MiniportNameLen)
    )


@declare(guid=guid("152fbe4b-c7ad-4f68-bada-a4fcc1464f6c"), event_id=11, version=0)
class Microsoft_Windows_Hyper_V_NetVsc_11_0(Etw):
    pattern = Struct(
        "MiniportNameLen" / Int32ul,
        "MiniportName" / Bytes(lambda this: this.MiniportNameLen)
    )


@declare(guid=guid("152fbe4b-c7ad-4f68-bada-a4fcc1464f6c"), event_id=12, version=0)
class Microsoft_Windows_Hyper_V_NetVsc_12_0(Etw):
    pattern = Struct(
        "MiniportNameLen" / Int32ul,
        "MiniportName" / Bytes(lambda this: this.MiniportNameLen)
    )


@declare(guid=guid("152fbe4b-c7ad-4f68-bada-a4fcc1464f6c"), event_id=13, version=0)
class Microsoft_Windows_Hyper_V_NetVsc_13_0(Etw):
    pattern = Struct(
        "MiniportNameLen" / Int32ul,
        "MiniportName" / Bytes(lambda this: this.MiniportNameLen)
    )


@declare(guid=guid("152fbe4b-c7ad-4f68-bada-a4fcc1464f6c"), event_id=14, version=0)
class Microsoft_Windows_Hyper_V_NetVsc_14_0(Etw):
    pattern = Struct(
        "MiniportNameLen" / Int32ul,
        "MiniportName" / Bytes(lambda this: this.MiniportNameLen)
    )


@declare(guid=guid("152fbe4b-c7ad-4f68-bada-a4fcc1464f6c"), event_id=15, version=0)
class Microsoft_Windows_Hyper_V_NetVsc_15_0(Etw):
    pattern = Struct(
        "MiniportNameLen" / Int32ul,
        "MiniportName" / Bytes(lambda this: this.MiniportNameLen),
        "Status" / Int32ul,
        "UniqueEventValue" / Int32ul
    )


@declare(guid=guid("152fbe4b-c7ad-4f68-bada-a4fcc1464f6c"), event_id=16, version=0)
class Microsoft_Windows_Hyper_V_NetVsc_16_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "Operation" / Int32ul,
        "DropReason" / Int32ul,
        "MiniportNameLen" / Int32ul,
        "MiniportName" / Bytes(lambda this: this.MiniportNameLen)
    )


@declare(guid=guid("152fbe4b-c7ad-4f68-bada-a4fcc1464f6c"), event_id=17, version=0)
class Microsoft_Windows_Hyper_V_NetVsc_17_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "DropReason" / Int32ul
    )


@declare(guid=guid("152fbe4b-c7ad-4f68-bada-a4fcc1464f6c"), event_id=18, version=0)
class Microsoft_Windows_Hyper_V_NetVsc_18_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "Direction" / Int32ul,
        "DropReason" / Int32ul,
        "Pointer" / Int64ul,
        "CorrelationId" / Int64ul,
        "IfIndex" / Int32ul
    )


@declare(guid=guid("152fbe4b-c7ad-4f68-bada-a4fcc1464f6c"), event_id=19, version=0)
class Microsoft_Windows_Hyper_V_NetVsc_19_0(Etw):
    pattern = Struct(
        "Direction" / Int32ul,
        "Pointer" / Int64ul,
        "CorrelationId" / Int64ul,
        "IfIndex" / Int32ul
    )


@declare(guid=guid("152fbe4b-c7ad-4f68-bada-a4fcc1464f6c"), event_id=20, version=0)
class Microsoft_Windows_Hyper_V_NetVsc_20_0(Etw):
    pattern = Struct(
        "Direction" / Int32ul,
        "Pointer" / Int64ul,
        "CorrelationId" / Int64ul,
        "IfIndex" / Int32ul
    )


@declare(guid=guid("152fbe4b-c7ad-4f68-bada-a4fcc1464f6c"), event_id=34, version=0)
class Microsoft_Windows_Hyper_V_NetVsc_34_0(Etw):
    pattern = Struct(
        "ClientContext" / Int64ul
    )


@declare(guid=guid("152fbe4b-c7ad-4f68-bada-a4fcc1464f6c"), event_id=35, version=0)
class Microsoft_Windows_Hyper_V_NetVsc_35_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "ClientContext" / Int64ul
    )


@declare(guid=guid("152fbe4b-c7ad-4f68-bada-a4fcc1464f6c"), event_id=36, version=0)
class Microsoft_Windows_Hyper_V_NetVsc_36_0(Etw):
    pattern = Struct(
        "ClientContext" / Int64ul
    )


@declare(guid=guid("152fbe4b-c7ad-4f68-bada-a4fcc1464f6c"), event_id=37, version=0)
class Microsoft_Windows_Hyper_V_NetVsc_37_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "failureReason" / Int32ul,
        "MiniportNameLen" / Int32ul,
        "MiniportName" / Bytes(lambda this: this.MiniportNameLen)
    )


@declare(guid=guid("152fbe4b-c7ad-4f68-bada-a4fcc1464f6c"), event_id=38, version=0)
class Microsoft_Windows_Hyper_V_NetVsc_38_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "NetEvent" / Int32ul,
        "failureReason" / Int32ul,
        "MiniportNameLen" / Int32ul,
        "MiniportName" / Bytes(lambda this: this.MiniportNameLen)
    )


@declare(guid=guid("152fbe4b-c7ad-4f68-bada-a4fcc1464f6c"), event_id=39, version=0)
class Microsoft_Windows_Hyper_V_NetVsc_39_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "failureReason" / Int32ul
    )


@declare(guid=guid("152fbe4b-c7ad-4f68-bada-a4fcc1464f6c"), event_id=40, version=0)
class Microsoft_Windows_Hyper_V_NetVsc_40_0(Etw):
    pattern = Struct(
        "Task" / Int32ul,
        "MemoryRequired" / Int32ul
    )


@declare(guid=guid("152fbe4b-c7ad-4f68-bada-a4fcc1464f6c"), event_id=41, version=0)
class Microsoft_Windows_Hyper_V_NetVsc_41_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "RequestHandled" / Int8ul,
        "IfIndex" / Int32ul,
        "MiniportNameLen" / Int32ul,
        "MiniportName" / Bytes(lambda this: this.MiniportNameLen),
        "VfAdapterNameLen" / Int32ul,
        "VfAdapterName" / Bytes(lambda this: this.VfAdapterNameLen)
    )


@declare(guid=guid("152fbe4b-c7ad-4f68-bada-a4fcc1464f6c"), event_id=42, version=0)
class Microsoft_Windows_Hyper_V_NetVsc_42_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "RequestHandled" / Int8ul,
        "IfIndex" / Int32ul,
        "MiniportNameLen" / Int32ul,
        "MiniportName" / Bytes(lambda this: this.MiniportNameLen),
        "VfAdapterNameLen" / Int32ul,
        "VfAdapterName" / Bytes(lambda this: this.VfAdapterNameLen)
    )


@declare(guid=guid("152fbe4b-c7ad-4f68-bada-a4fcc1464f6c"), event_id=43, version=0)
class Microsoft_Windows_Hyper_V_NetVsc_43_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "NetEvent" / Int32ul,
        "failureReason" / Int32ul,
        "MiniportNameLen" / Int32ul,
        "MiniportName" / Bytes(lambda this: this.MiniportNameLen)
    )


@declare(guid=guid("152fbe4b-c7ad-4f68-bada-a4fcc1464f6c"), event_id=44, version=0)
class Microsoft_Windows_Hyper_V_NetVsc_44_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "NdkEnabled" / Int8ul,
        "MiniportNameLen" / Int32ul,
        "MiniportName" / Bytes(lambda this: this.MiniportNameLen)
    )


@declare(guid=guid("152fbe4b-c7ad-4f68-bada-a4fcc1464f6c"), event_id=45, version=0)
class Microsoft_Windows_Hyper_V_NetVsc_45_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "NdkEnabled" / Int8ul,
        "MiniportNameLen" / Int32ul,
        "MiniportName" / Bytes(lambda this: this.MiniportNameLen)
    )


@declare(guid=guid("152fbe4b-c7ad-4f68-bada-a4fcc1464f6c"), event_id=46, version=0)
class Microsoft_Windows_Hyper_V_NetVsc_46_0(Etw):
    pattern = Struct(
        "VfAdapterNameLen" / Int32ul,
        "VfAdapterName" / Bytes(lambda this: this.VfAdapterNameLen)
    )


@declare(guid=guid("152fbe4b-c7ad-4f68-bada-a4fcc1464f6c"), event_id=47, version=0)
class Microsoft_Windows_Hyper_V_NetVsc_47_0(Etw):
    pattern = Struct(
        "VfAdapterNameLen" / Int32ul,
        "VfAdapterName" / Bytes(lambda this: this.VfAdapterNameLen)
    )


@declare(guid=guid("152fbe4b-c7ad-4f68-bada-a4fcc1464f6c"), event_id=48, version=0)
class Microsoft_Windows_Hyper_V_NetVsc_48_0(Etw):
    pattern = Struct(
        "VfAdapterNameLen" / Int32ul,
        "VfAdapterName" / Bytes(lambda this: this.VfAdapterNameLen)
    )

