# -*- coding: utf-8 -*-
"""
Microsoft-Windows-TCPIP
GUID : 2f07e2ee-15db-40f1-90ef-9d7ba282188a
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1001, version=0)
class Microsoft_Windows_TCPIP_1001_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "Endpoint" / Int64ul,
        "AddressFamily" / Int32ul,
        "Pid" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1002, version=0)
class Microsoft_Windows_TCPIP_1002_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "NewState" / Int32ul,
        "RexmitCount" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1003, version=0)
class Microsoft_Windows_TCPIP_1003_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "Status" / Int32ul,
        "AddressFamily" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1004, version=0)
class Microsoft_Windows_TCPIP_1004_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "ISN" / Int32ul,
        "RcvWnd" / Int32ul,
        "RcvWndScale" / Int8ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1005, version=0)
class Microsoft_Windows_TCPIP_1005_0(Etw):
    pattern = Struct(
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1006, version=0)
class Microsoft_Windows_TCPIP_1006_0(Etw):
    pattern = Struct(
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1007, version=0)
class Microsoft_Windows_TCPIP_1007_0(Etw):
    pattern = Struct(
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1008, version=0)
class Microsoft_Windows_TCPIP_1008_0(Etw):
    pattern = Struct(
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1009, version=0)
class Microsoft_Windows_TCPIP_1009_0(Etw):
    pattern = Struct(
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1010, version=0)
class Microsoft_Windows_TCPIP_1010_0(Etw):
    pattern = Struct(
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "Status" / Int32ul,
        "ProcessId" / Int32ul,
        "CompartmentId" / Int32ul,
        "AddressFamily" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1011, version=0)
class Microsoft_Windows_TCPIP_1011_0(Etw):
    pattern = Struct(
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "Status" / Int32ul,
        "ProcessId" / Int32ul,
        "CompartmentId" / Int32ul,
        "AddressFamily" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1012, version=0)
class Microsoft_Windows_TCPIP_1012_0(Etw):
    pattern = Struct(
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "Status" / Int32ul,
        "ProcessId" / Int32ul,
        "CompartmentId" / Int32ul,
        "AddressFamily" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1013, version=0)
class Microsoft_Windows_TCPIP_1013_0(Etw):
    pattern = Struct(
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "Status" / Int32ul,
        "ProcessId" / Int32ul,
        "CompartmentId" / Int32ul,
        "AddressFamily" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1014, version=0)
class Microsoft_Windows_TCPIP_1014_0(Etw):
    pattern = Struct(
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "Status" / Int32ul,
        "ProcessId" / Int32ul,
        "Compartment" / Int32ul,
        "Tcb" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1015, version=0)
class Microsoft_Windows_TCPIP_1015_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "NewState" / Int32ul,
        "RexmitCount" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1016, version=0)
class Microsoft_Windows_TCPIP_1016_0(Etw):
    pattern = Struct(
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "Status" / Int32ul,
        "ProcessId" / Int32ul,
        "Compartment" / Int32ul,
        "Tcb" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1017, version=0)
class Microsoft_Windows_TCPIP_1017_0(Etw):
    pattern = Struct(
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "Status" / Int32ul,
        "ProcessId" / Int32ul,
        "Compartment" / Int32ul,
        "Tcb" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1018, version=0)
class Microsoft_Windows_TCPIP_1018_0(Etw):
    pattern = Struct(
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "Status" / Int32ul,
        "ProcessId" / Int32ul,
        "Compartment" / Int32ul,
        "Tcb" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1019, version=0)
class Microsoft_Windows_TCPIP_1019_0(Etw):
    pattern = Struct(
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "Status" / Int32ul,
        "ProcessId" / Int32ul,
        "Compartment" / Int32ul,
        "Tcb" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1020, version=0)
class Microsoft_Windows_TCPIP_1020_0(Etw):
    pattern = Struct(
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "Status" / Int32ul,
        "ProcessId" / Int32ul,
        "Compartment" / Int32ul,
        "Tcb" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1021, version=0)
class Microsoft_Windows_TCPIP_1021_0(Etw):
    pattern = Struct(
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "Status" / Int32ul,
        "ProcessId" / Int32ul,
        "Compartment" / Int32ul,
        "Tcb" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1022, version=0)
class Microsoft_Windows_TCPIP_1022_0(Etw):
    pattern = Struct(
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "Path" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1023, version=0)
class Microsoft_Windows_TCPIP_1023_0(Etw):
    pattern = Struct(
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "Path" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1024, version=0)
class Microsoft_Windows_TCPIP_1024_0(Etw):
    pattern = Struct(
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "Status" / Int32ul,
        "ProcessId" / Int32ul,
        "Compartment" / Int32ul,
        "Tcb" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1025, version=0)
class Microsoft_Windows_TCPIP_1025_0(Etw):
    pattern = Struct(
        "SynAttacksDetected" / Int32ul,
        "ReassemblyLimitViolations" / Int32ul,
        "ConnectionRateLimitBacklog" / Int32ul,
        "ConnectionRateLimitViolations" / Int32ul,
        "LandAttackSegmentsDropped" / Int32ul,
        "ConnectionRateLimitDepth" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1026, version=0)
class Microsoft_Windows_TCPIP_1026_0(Etw):
    pattern = Struct(
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "Path" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1027, version=0)
class Microsoft_Windows_TCPIP_1027_0(Etw):
    pattern = Struct(
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "Status" / Int32ul,
        "ProcessId" / Int32ul,
        "Compartment" / Int32ul,
        "Tcb" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1028, version=0)
class Microsoft_Windows_TCPIP_1028_0(Etw):
    pattern = Struct(
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "Path" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1029, version=0)
class Microsoft_Windows_TCPIP_1029_0(Etw):
    pattern = Struct(
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "Status" / Int32ul,
        "ProcessId" / Int32ul,
        "Compartment" / Int32ul,
        "Tcb" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1030, version=0)
class Microsoft_Windows_TCPIP_1030_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "NewState" / Int32ul,
        "RexmitCount" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1031, version=0)
class Microsoft_Windows_TCPIP_1031_0(Etw):
    pattern = Struct(
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "Status" / Int32ul,
        "ProcessId" / Int32ul,
        "Compartment" / Int32ul,
        "Tcb" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1032, version=0)
class Microsoft_Windows_TCPIP_1032_0(Etw):
    pattern = Struct(
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "Status" / Int32ul,
        "ProcessId" / Int32ul,
        "Compartment" / Int32ul,
        "Tcb" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1033, version=0)
class Microsoft_Windows_TCPIP_1033_0(Etw):
    pattern = Struct(
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "Status" / Int32ul,
        "ProcessId" / Int32ul,
        "Compartment" / Int32ul,
        "Tcb" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1034, version=0)
class Microsoft_Windows_TCPIP_1034_0(Etw):
    pattern = Struct(
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "Status" / Int32ul,
        "ProcessId" / Int32ul,
        "Compartment" / Int32ul,
        "Tcb" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1035, version=0)
class Microsoft_Windows_TCPIP_1035_0(Etw):
    pattern = Struct(
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "Status" / Int32ul,
        "ProcessId" / Int32ul,
        "Compartment" / Int32ul,
        "Tcb" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1036, version=0)
class Microsoft_Windows_TCPIP_1036_0(Etw):
    pattern = Struct(
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "Status" / Int32ul,
        "ProcessId" / Int32ul,
        "Compartment" / Int32ul,
        "Tcb" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1037, version=0)
class Microsoft_Windows_TCPIP_1037_0(Etw):
    pattern = Struct(
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "Status" / Int32ul,
        "ProcessId" / Int32ul,
        "Compartment" / Int32ul,
        "Tcb" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1038, version=0)
class Microsoft_Windows_TCPIP_1038_0(Etw):
    pattern = Struct(
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "Status" / Int32ul,
        "ProcessId" / Int32ul,
        "Compartment" / Int32ul,
        "Tcb" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1039, version=0)
class Microsoft_Windows_TCPIP_1039_0(Etw):
    pattern = Struct(
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "Status" / Int32ul,
        "ProcessId" / Int32ul,
        "Compartment" / Int32ul,
        "Tcb" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1040, version=0)
class Microsoft_Windows_TCPIP_1040_0(Etw):
    pattern = Struct(
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "Status" / Int32ul,
        "ProcessId" / Int32ul,
        "Compartment" / Int32ul,
        "Tcb" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1041, version=0)
class Microsoft_Windows_TCPIP_1041_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "Delivery" / Int64ul,
        "Request" / Int64ul,
        "NumBytes" / Int64ul,
        "RequestFlags" / Int32ul,
        "Length" / Int64ul,
        "RequestStatus" / Int32ul,
        "IsUrgentDelivery" / Int32ul,
        "FullySatisfiedORDelayedPush" / Int32ul,
        "RcvNxt" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1042, version=0)
class Microsoft_Windows_TCPIP_1042_0(Etw):
    pattern = Struct(
        "Length" / Int64ul,
        "Timeout" / Int64ul,
        "Injected" / WString
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1043, version=0)
class Microsoft_Windows_TCPIP_1043_0(Etw):
    pattern = Struct(
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "Status" / Int32ul,
        "ProcessId" / Int32ul,
        "Compartment" / Int32ul,
        "Tcb" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1044, version=0)
class Microsoft_Windows_TCPIP_1044_0(Etw):
    pattern = Struct(
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "Status" / Int32ul,
        "ProcessId" / Int32ul,
        "Compartment" / Int32ul,
        "Tcb" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1045, version=0)
class Microsoft_Windows_TCPIP_1045_0(Etw):
    pattern = Struct(
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "Status" / Int32ul,
        "ProcessId" / Int32ul,
        "Compartment" / Int32ul,
        "Tcb" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1046, version=0)
class Microsoft_Windows_TCPIP_1046_0(Etw):
    pattern = Struct(
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "Status" / Int32ul,
        "ProcessId" / Int32ul,
        "Compartment" / Int32ul,
        "Tcb" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1047, version=0)
class Microsoft_Windows_TCPIP_1047_0(Etw):
    pattern = Struct(
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "Status" / Int32ul,
        "ProcessId" / Int32ul,
        "Compartment" / Int32ul,
        "Tcb" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1048, version=0)
class Microsoft_Windows_TCPIP_1048_0(Etw):
    pattern = Struct(
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "Status" / Int32ul,
        "ProcessId" / Int32ul,
        "Compartment" / Int32ul,
        "Tcb" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1049, version=0)
class Microsoft_Windows_TCPIP_1049_0(Etw):
    pattern = Struct(
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "Status" / Int32ul,
        "ProcessId" / Int32ul,
        "Compartment" / Int32ul,
        "Tcb" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1050, version=0)
class Microsoft_Windows_TCPIP_1050_0(Etw):
    pattern = Struct(
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "Status" / Int32ul,
        "ProcessId" / Int32ul,
        "Compartment" / Int32ul,
        "Tcb" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1051, version=0)
class Microsoft_Windows_TCPIP_1051_0(Etw):
    pattern = Struct(
        "OldState" / Int32ul,
        "NewState" / Int32ul,
        "SndNxt" / Int32ul,
        "Tcb" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1052, version=0)
class Microsoft_Windows_TCPIP_1052_0(Etw):
    pattern = Struct(
        "ProcessId" / Int32ul,
        "Status" / Int32ul,
        "StartPort" / Int16ul,
        "NumberOfPorts" / Int16ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1053, version=0)
class Microsoft_Windows_TCPIP_1053_0(Etw):
    pattern = Struct(
        "ProcessId" / Int32ul,
        "Status" / Int32ul,
        "StartPort" / Int16ul,
        "NumberOfPorts" / Int16ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1054, version=0)
class Microsoft_Windows_TCPIP_1054_0(Etw):
    pattern = Struct(
        "ProcessId" / Int32ul,
        "Status" / Int32ul,
        "StartPort" / Int16ul,
        "NumberOfPorts" / Int16ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1055, version=0)
class Microsoft_Windows_TCPIP_1055_0(Etw):
    pattern = Struct(
        "SynAttacksDetected" / Int32ul,
        "ReassemblyLimitViolations" / Int32ul,
        "ConnectionRateLimitBacklog" / Int32ul,
        "ConnectionRateLimitViolations" / Int32ul,
        "LandAttackSegmentsDropped" / Int32ul,
        "ConnectionRateLimitDepth" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1056, version=0)
class Microsoft_Windows_TCPIP_1056_0(Etw):
    pattern = Struct(
        "SynAttacksDetected" / Int32ul,
        "ReassemblyLimitViolations" / Int32ul,
        "ConnectionRateLimitBacklog" / Int32ul,
        "ConnectionRateLimitViolations" / Int32ul,
        "LandAttackSegmentsDropped" / Int32ul,
        "ConnectionRateLimitDepth" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1057, version=0)
class Microsoft_Windows_TCPIP_1057_0(Etw):
    pattern = Struct(
        "SynAttacksDetected" / Int32ul,
        "ReassemblyLimitViolations" / Int32ul,
        "ConnectionRateLimitBacklog" / Int32ul,
        "ConnectionRateLimitViolations" / Int32ul,
        "LandAttackSegmentsDropped" / Int32ul,
        "ConnectionRateLimitDepth" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1058, version=0)
class Microsoft_Windows_TCPIP_1058_0(Etw):
    pattern = Struct(
        "SynAttacksDetected" / Int32ul,
        "ReassemblyLimitViolations" / Int32ul,
        "ConnectionRateLimitBacklog" / Int32ul,
        "ConnectionRateLimitViolations" / Int32ul,
        "LandAttackSegmentsDropped" / Int32ul,
        "ConnectionRateLimitDepth" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1059, version=0)
class Microsoft_Windows_TCPIP_1059_0(Etw):
    pattern = Struct(
        "HighMemoryEvent" / Int32ul,
        "HighPagedPoolEvent" / Int32ul,
        "LowMemoryEvent" / Int32ul,
        "LowPagedPoolEvent" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1060, version=0)
class Microsoft_Windows_TCPIP_1060_0(Etw):
    pattern = Struct(
        "HighMemoryEvent" / Int32ul,
        "HighPagedPoolEvent" / Int32ul,
        "LowMemoryEvent" / Int32ul,
        "LowPagedPoolEvent" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1061, version=0)
class Microsoft_Windows_TCPIP_1061_0(Etw):
    pattern = Struct(
        "InterfaceIndex" / Int32ul,
        "AddressFamily" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1062, version=0)
class Microsoft_Windows_TCPIP_1062_0(Etw):
    pattern = Struct(
        "InterfaceIndex" / Int32ul,
        "AddressFamily" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1063, version=0)
class Microsoft_Windows_TCPIP_1063_0(Etw):
    pattern = Struct(
        "SynAttacksDetected" / Int32ul,
        "ReassemblyLimitViolations" / Int32ul,
        "ConnectionRateLimitBacklog" / Int32ul,
        "ConnectionRateLimitViolations" / Int32ul,
        "LandAttackSegmentsDropped" / Int32ul,
        "ConnectionRateLimitDepth" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1064, version=0)
class Microsoft_Windows_TCPIP_1064_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "TimerType" / Int32ul,
        "WaitTimeMilliseconds" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1064, version=1)
class Microsoft_Windows_TCPIP_1064_1(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "TimerType" / Int32ul,
        "WaitTimeMilliseconds" / Int32ul,
        "Processor" / Int32ul,
        "LastInterruptTime" / Int64ul,
        "LastMicroseconds" / Int64ul,
        "CachedKQPCValues" / Int64sl,
        "CachedFrequencyValues" / Int64sl
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1065, version=0)
class Microsoft_Windows_TCPIP_1065_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "TimerType" / Int32ul,
        "WaitTimeMilliseconds" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1066, version=0)
class Microsoft_Windows_TCPIP_1066_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "TimerType" / Int32ul,
        "WaitTimeMilliseconds" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1067, version=0)
class Microsoft_Windows_TCPIP_1067_0(Etw):
    pattern = Struct(
        "IsbSize" / Int32ul,
        "Cwnd" / Int32ul,
        "SndWnd" / Int32ul,
        "SendAvailable" / Int32ul,
        "SSThresh" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1068, version=0)
class Microsoft_Windows_TCPIP_1068_0(Etw):
    pattern = Struct(
        "SourceProcessor" / Int32ul,
        "SourceActivity" / Int32ul,
        "DestinationProcessor" / Int32ul,
        "DestinationActivity" / Int32ul,
        "PartitionMovesRemaining" / Int32ul,
        "TableEntry" / Int8ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1069, version=0)
class Microsoft_Windows_TCPIP_1069_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "Cwnd" / Int32ul,
        "SSThresh" / Int32ul,
        "RttSample" / Int32ul,
        "NumBytes" / Int32ul,
        "SeqNo" / Int32ul,
        "SndUna" / Int32ul,
        "Round" / Int32ul,
        "SRTT" / Int32ul,
        "RTO" / Int32ul,
        "DWnd" / Int32ul,
        "BaseRtt" / Int32ul,
        "DupAckCount" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1070, version=0)
class Microsoft_Windows_TCPIP_1070_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "Cwnd" / Int32ul,
        "SSThresh" / Int32ul,
        "RttSample" / Int32ul,
        "NumBytes" / Int32ul,
        "SeqNo" / Int32ul,
        "SndUna" / Int32ul,
        "Round" / Int32ul,
        "SRTT" / Int32ul,
        "RTO" / Int32ul,
        "DWnd" / Int32ul,
        "BaseRtt" / Int32ul,
        "DupAckCount" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1071, version=0)
class Microsoft_Windows_TCPIP_1071_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "Cwnd" / Int32ul,
        "SSThresh" / Int32ul,
        "RttSample" / Int32ul,
        "NumBytes" / Int32ul,
        "SeqNo" / Int32ul,
        "SndUna" / Int32ul,
        "Round" / Int32ul,
        "SRTT" / Int32ul,
        "RTO" / Int32ul,
        "DWnd" / Int32ul,
        "BaseRtt" / Int32ul,
        "DupAckCount" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1072, version=0)
class Microsoft_Windows_TCPIP_1072_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "Cwnd" / Int32ul,
        "SSThresh" / Int32ul,
        "RttSample" / Int32ul,
        "NumBytes" / Int32ul,
        "SeqNo" / Int32ul,
        "SndUna" / Int32ul,
        "Round" / Int32ul,
        "SRTT" / Int32ul,
        "RTO" / Int32ul,
        "DWnd" / Int32ul,
        "BaseRtt" / Int32ul,
        "DupAckCount" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1073, version=0)
class Microsoft_Windows_TCPIP_1073_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "Cwnd" / Int32ul,
        "SSThresh" / Int32ul,
        "RttSample" / Int32ul,
        "NumBytes" / Int32ul,
        "SeqNo" / Int32ul,
        "SndUna" / Int32ul,
        "Round" / Int32ul,
        "SRTT" / Int32ul,
        "RTO" / Int32ul,
        "DWnd" / Int32ul,
        "BaseRtt" / Int32ul,
        "DupAckCount" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1074, version=0)
class Microsoft_Windows_TCPIP_1074_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "NumBytes" / Int32ul,
        "SeqNo" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1075, version=0)
class Microsoft_Windows_TCPIP_1075_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "Cwnd" / Int32ul,
        "SSThresh" / Int32ul,
        "SndUna" / Int32ul,
        "Mss" / Int32ul,
        "ThAck" / Int32ul,
        "DWnd" / Int32ul,
        "BaseRtt" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1076, version=0)
class Microsoft_Windows_TCPIP_1076_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "Cwnd" / Int32ul,
        "SSThresh" / Int32ul,
        "RttSample" / Int32ul,
        "NumBytes" / Int32ul,
        "SeqNo" / Int32ul,
        "SndUna" / Int32ul,
        "Round" / Int32ul,
        "SRTT" / Int32ul,
        "RTO" / Int32ul,
        "DWnd" / Int32ul,
        "BaseRtt" / Int32ul,
        "DupAckCount" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1077, version=0)
class Microsoft_Windows_TCPIP_1077_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "Cwnd" / Int32ul,
        "SSThresh" / Int32ul,
        "RttSample" / Int32ul,
        "NumBytes" / Int32ul,
        "SeqNo" / Int32ul,
        "SndUna" / Int32ul,
        "Round" / Int32ul,
        "SRTT" / Int32ul,
        "RTO" / Int32ul,
        "DWnd" / Int32ul,
        "BaseRtt" / Int32ul,
        "DupAckCount" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1078, version=0)
class Microsoft_Windows_TCPIP_1078_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "SndUna" / Int32ul,
        "SndMax" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1079, version=0)
class Microsoft_Windows_TCPIP_1079_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "SndUna" / Int32ul,
        "SndMax" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1080, version=0)
class Microsoft_Windows_TCPIP_1080_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "SndUna" / Int32ul,
        "SndMax" / Int32ul,
        "Reason" / WString,
        "IsSack" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1081, version=0)
class Microsoft_Windows_TCPIP_1081_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "SndUna" / Int32ul,
        "SndMax" / Int32ul,
        "Reason" / WString,
        "IsSack" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1082, version=0)
class Microsoft_Windows_TCPIP_1082_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "Cwnd" / Int32ul,
        "SSThresh" / Int32ul,
        "RttSample" / Int32ul,
        "NumBytes" / Int32ul,
        "SeqNo" / Int32ul,
        "SndUna" / Int32ul,
        "Round" / Int32ul,
        "SRTT" / Int32ul,
        "RTO" / Int32ul,
        "DWnd" / Int32ul,
        "BaseRtt" / Int32ul,
        "DupAckCount" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1084, version=0)
class Microsoft_Windows_TCPIP_1084_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "BHMSS" / Int32ul,
        "OriginalMSS" / Int32ul,
        "TraceString" / WString
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1085, version=0)
class Microsoft_Windows_TCPIP_1085_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "BHMSS" / Int32ul,
        "OriginalMSS" / Int32ul,
        "TraceString" / WString
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1086, version=0)
class Microsoft_Windows_TCPIP_1086_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "BHMSS" / Int32ul,
        "OriginalMSS" / Int32ul,
        "TraceString" / WString
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1087, version=0)
class Microsoft_Windows_TCPIP_1087_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "Cwnd" / Int32ul,
        "SSThresh" / Int32ul,
        "RttSample" / Int32ul,
        "NumBytes" / Int32ul,
        "SeqNo" / Int32ul,
        "SndUna" / Int32ul,
        "Round" / Int32ul,
        "SRTT" / Int32ul,
        "RTO" / Int32ul,
        "DWnd" / Int32ul,
        "BaseRtt" / Int32ul,
        "DupAckCount" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1088, version=0)
class Microsoft_Windows_TCPIP_1088_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "Cwnd" / Int32ul,
        "SSThresh" / Int32ul,
        "RttSample" / Int32ul,
        "NumBytes" / Int32ul,
        "SeqNo" / Int32ul,
        "SndUna" / Int32ul,
        "Round" / Int32ul,
        "SRTT" / Int32ul,
        "RTO" / Int32ul,
        "DWnd" / Int32ul,
        "BaseRtt" / Int32ul,
        "DupAckCount" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1089, version=0)
class Microsoft_Windows_TCPIP_1089_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "Status" / Int32ul,
        "AddressFamily" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1090, version=0)
class Microsoft_Windows_TCPIP_1090_0(Etw):
    pattern = Struct(
        "NBL" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1091, version=0)
class Microsoft_Windows_TCPIP_1091_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "Cwnd" / Int32ul,
        "SSThresh" / Int32ul,
        "RttSample" / Int32ul,
        "NumBytes" / Int32ul,
        "SeqNo" / Int32ul,
        "SndUna" / Int32ul,
        "Round" / Int32ul,
        "SRTT" / Int32ul,
        "RTO" / Int32ul,
        "DWnd" / Int32ul,
        "BaseRtt" / Int32ul,
        "DupAckCount" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1092, version=0)
class Microsoft_Windows_TCPIP_1092_0(Etw):
    pattern = Struct(
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "BufferSize" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1093, version=0)
class Microsoft_Windows_TCPIP_1093_0(Etw):
    pattern = Struct(
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "BufferSize" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1094, version=0)
class Microsoft_Windows_TCPIP_1094_0(Etw):
    pattern = Struct(
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "BufferSize" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1095, version=0)
class Microsoft_Windows_TCPIP_1095_0(Etw):
    pattern = Struct(
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "BufferSize" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1096, version=0)
class Microsoft_Windows_TCPIP_1096_0(Etw):
    pattern = Struct(
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "BufferSize" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1097, version=0)
class Microsoft_Windows_TCPIP_1097_0(Etw):
    pattern = Struct(
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "BufferSize" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1098, version=0)
class Microsoft_Windows_TCPIP_1098_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "Cwnd" / Int32ul,
        "SSThresh" / Int32ul,
        "RttSample" / Int32ul,
        "NumBytes" / Int32ul,
        "SeqNo" / Int32ul,
        "SndUna" / Int32ul,
        "Round" / Int32ul,
        "SRTT" / Int32ul,
        "RTO" / Int32ul,
        "DWnd" / Int32ul,
        "BaseRtt" / Int32ul,
        "DupAckCount" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1099, version=0)
class Microsoft_Windows_TCPIP_1099_0(Etw):
    pattern = Struct(
        "TcbState" / Int32ul,
        "OcbState" / Int32ul,
        "SndNxt" / Int32ul,
        "RcvNxt" / Int32ul,
        "Tcb" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1100, version=0)
class Microsoft_Windows_TCPIP_1100_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "TimerValue" / Int32ul,
        "BytesToSend" / Int64ul,
        "SendAvailable" / Int32ul,
        "Cwnd" / Int32ul,
        "MaxSndWnd" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1101, version=0)
class Microsoft_Windows_TCPIP_1101_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "TimerValue" / Int32ul,
        "BytesToSend" / Int64ul,
        "SendAvailable" / Int32ul,
        "Cwnd" / Int32ul,
        "MaxSndWnd" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1102, version=0)
class Microsoft_Windows_TCPIP_1102_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "SndUna" / Int32ul,
        "SndMax" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1103, version=0)
class Microsoft_Windows_TCPIP_1103_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "SndUna" / Int32ul,
        "SndMax" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1104, version=0)
class Microsoft_Windows_TCPIP_1104_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "OptionType" / Int32ul,
        "SoOptionType" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1105, version=0)
class Microsoft_Windows_TCPIP_1105_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "OptionType" / Int32ul,
        "SoOptionType" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1106, version=0)
class Microsoft_Windows_TCPIP_1106_0(Etw):
    pattern = Struct(
        "InterfaceIndex" / Int32ul,
        "TraceString" / CString
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1106, version=1)
class Microsoft_Windows_TCPIP_1106_1(Etw):
    pattern = Struct(
        "InterfaceIndex" / Int32ul,
        "TraceString" / CString,
        "CompartmentId" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1107, version=0)
class Microsoft_Windows_TCPIP_1107_0(Etw):
    pattern = Struct(
        "ModuleNameString" / WString
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1108, version=0)
class Microsoft_Windows_TCPIP_1108_0(Etw):
    pattern = Struct(
        "ModuleNameString" / WString
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1109, version=0)
class Microsoft_Windows_TCPIP_1109_0(Etw):
    pattern = Struct(
        "AllocationObjectString" / WString
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1110, version=0)
class Microsoft_Windows_TCPIP_1110_0(Etw):
    pattern = Struct(
        "AddressFamily" / Int32ul,
        "EnablePMTUDiscovery" / Int8ul,
        "TcpUseRFC1122UrgentPointer" / Int8ul,
        "DisableTaskOffload" / Int8ul,
        "EnablePMTUBHDetect" / Int8ul,
        "DisableTcpChimneyOffload" / Int8ul,
        "DisableRss" / Int8ul,
        "EcnCapability" / Int8ul,
        "TcpMaxDataRetransmissions" / Int8ul,
        "KeepAliveTime" / Int32ul,
        "KeepAliveInterval" / Int32ul,
        "TcpTimedWaitDelay" / Int32ul,
        "SillyWindowTimeout" / Int32ul,
        "TcpFinWait2Delay" / Int32ul,
        "CongestionAlgorithm" / Int8ul,
        "Tcp1323Opts" / Int8ul,
        "AutoTuningLevelLocal" / Int32ul,
        "AutoTuningLevelGroupPolicy" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1111, version=0)
class Microsoft_Windows_TCPIP_1111_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "BytesInSegment" / Int32ul,
        "BytesRemaining" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1112, version=0)
class Microsoft_Windows_TCPIP_1112_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "Status" / Int32ul,
        "Interface" / Int32ul,
        "PMax" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1113, version=0)
class Microsoft_Windows_TCPIP_1113_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "Status" / Int32ul,
        "Interface" / Int32ul,
        "PMax" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1114, version=0)
class Microsoft_Windows_TCPIP_1114_0(Etw):
    pattern = Struct(
        "Interface" / Int32ul,
        "Protocol" / CString,
        "DadState" / Int32ul,
        "DlAddrLength" / Int32ul,
        "DLAddress" / Bytes(lambda this: this.DlAddrLength),
        "IpAddrLength" / Int32ul,
        "IPv4Address" / Int32ul,
        "IPv6Address" / Bytes(lambda this: this.IpAddrLength),
        "IPProtocol" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1114, version=1)
class Microsoft_Windows_TCPIP_1114_1(Etw):
    pattern = Struct(
        "Interface" / Int32ul,
        "Protocol" / CString,
        "DadState" / Int32ul,
        "DlAddrLength" / Int32ul,
        "DLAddress" / Bytes(lambda this: this.DlAddrLength),
        "IpAddrLength" / Int32ul,
        "IPv4Address" / Int32ul,
        "IPv6Address" / Bytes(lambda this: this.IpAddrLength),
        "IPProtocol" / Int32ul,
        "CompartmentId" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1115, version=0)
class Microsoft_Windows_TCPIP_1115_0(Etw):
    pattern = Struct(
        "Interface" / Int32ul,
        "Protocol" / CString,
        "DadState" / Int32ul,
        "DlAddrLength" / Int32ul,
        "DLAddress" / Bytes(lambda this: this.DlAddrLength),
        "IpAddrLength" / Int32ul,
        "IPv4Address" / Int32ul,
        "IPv6Address" / Bytes(lambda this: this.IpAddrLength),
        "IPProtocol" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1115, version=1)
class Microsoft_Windows_TCPIP_1115_1(Etw):
    pattern = Struct(
        "Interface" / Int32ul,
        "Protocol" / CString,
        "DadState" / Int32ul,
        "DlAddrLength" / Int32ul,
        "DLAddress" / Bytes(lambda this: this.DlAddrLength),
        "IpAddrLength" / Int32ul,
        "IPv4Address" / Int32ul,
        "IPv6Address" / Bytes(lambda this: this.IpAddrLength),
        "IPProtocol" / Int32ul,
        "CompartmentId" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1116, version=0)
class Microsoft_Windows_TCPIP_1116_0(Etw):
    pattern = Struct(
        "Interface" / Int32ul,
        "Protocol" / CString,
        "DadState" / Int32ul,
        "DlAddrLength" / Int32ul,
        "DLAddress" / Bytes(lambda this: this.DlAddrLength),
        "IpAddrLength" / Int32ul,
        "IPv4Address" / Int32ul,
        "IPv6Address" / Bytes(lambda this: this.IpAddrLength),
        "IPProtocol" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1116, version=1)
class Microsoft_Windows_TCPIP_1116_1(Etw):
    pattern = Struct(
        "Interface" / Int32ul,
        "Protocol" / CString,
        "DadState" / Int32ul,
        "DlAddrLength" / Int32ul,
        "DLAddress" / Bytes(lambda this: this.DlAddrLength),
        "IpAddrLength" / Int32ul,
        "IPv4Address" / Int32ul,
        "IPv6Address" / Bytes(lambda this: this.IpAddrLength),
        "IPProtocol" / Int32ul,
        "CompartmentId" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1117, version=0)
class Microsoft_Windows_TCPIP_1117_0(Etw):
    pattern = Struct(
        "Listener" / Int64ul,
        "AddressLength" / Int32ul,
        "SocketAddress" / Bytes(lambda this: this.AddressLength),
        "Status" / Int32ul,
        "ProcessId" / Int32ul,
        "CompartmentId" / Int32ul,
        "AddressFamily" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1118, version=0)
class Microsoft_Windows_TCPIP_1118_0(Etw):
    pattern = Struct(
        "Listener" / Int64ul,
        "AddressLength" / Int32ul,
        "SocketAddress" / Bytes(lambda this: this.AddressLength),
        "Status" / Int32ul,
        "ProcessId" / Int32ul,
        "CompartmentId" / Int32ul,
        "AddressFamily" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1119, version=0)
class Microsoft_Windows_TCPIP_1119_0(Etw):
    pattern = Struct(
        "Listener" / Int64ul,
        "AddressLength" / Int32ul,
        "SocketAddress" / Bytes(lambda this: this.AddressLength),
        "Status" / Int32ul,
        "ProcessId" / Int32ul,
        "CompartmentId" / Int32ul,
        "AddressFamily" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1120, version=0)
class Microsoft_Windows_TCPIP_1120_0(Etw):
    pattern = Struct(
        "Listener" / Int64ul,
        "AddressLength" / Int32ul,
        "SocketAddress" / Bytes(lambda this: this.AddressLength),
        "Status" / Int32ul,
        "ProcessId" / Int32ul,
        "CompartmentId" / Int32ul,
        "AddressFamily" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1121, version=0)
class Microsoft_Windows_TCPIP_1121_0(Etw):
    pattern = Struct(
        "Listener" / Int64ul,
        "AddressLength" / Int32ul,
        "SocketAddress" / Bytes(lambda this: this.AddressLength),
        "Status" / Int32ul,
        "ProcessId" / Int32ul,
        "CompartmentId" / Int32ul,
        "AddressFamily" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1122, version=0)
class Microsoft_Windows_TCPIP_1122_0(Etw):
    pattern = Struct(
        "Listener" / Int64ul,
        "AddressLength" / Int32ul,
        "SocketAddress" / Bytes(lambda this: this.AddressLength),
        "Status" / Int32ul,
        "ProcessId" / Int32ul,
        "CompartmentId" / Int32ul,
        "AddressFamily" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1123, version=0)
class Microsoft_Windows_TCPIP_1123_0(Etw):
    pattern = Struct(
        "Listener" / Int64ul,
        "AddressLength" / Int32ul,
        "SocketAddress" / Bytes(lambda this: this.AddressLength),
        "Status" / Int32ul,
        "ProcessId" / Int32ul,
        "CompartmentId" / Int32ul,
        "AddressFamily" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1124, version=0)
class Microsoft_Windows_TCPIP_1124_0(Etw):
    pattern = Struct(
        "Listener" / Int64ul,
        "AddressLength" / Int32ul,
        "SocketAddress" / Bytes(lambda this: this.AddressLength),
        "Status" / Int32ul,
        "ProcessId" / Int32ul,
        "CompartmentId" / Int32ul,
        "AddressFamily" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1127, version=0)
class Microsoft_Windows_TCPIP_1127_0(Etw):
    pattern = Struct(
        "Interface" / Int32ul,
        "Protocol" / CString,
        "DadState" / Int32ul,
        "DlAddrLength" / Int32ul,
        "DLAddress" / Bytes(lambda this: this.DlAddrLength),
        "IpAddrLength" / Int32ul,
        "IPv4Address" / Int32ul,
        "IPv6Address" / Bytes(lambda this: this.IpAddrLength),
        "IPProtocol" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1127, version=1)
class Microsoft_Windows_TCPIP_1127_1(Etw):
    pattern = Struct(
        "Interface" / Int32ul,
        "Protocol" / CString,
        "DadState" / Int32ul,
        "DlAddrLength" / Int32ul,
        "DLAddress" / Bytes(lambda this: this.DlAddrLength),
        "IpAddrLength" / Int32ul,
        "IPv4Address" / Int32ul,
        "IPv6Address" / Bytes(lambda this: this.IpAddrLength),
        "IPProtocol" / Int32ul,
        "CompartmentId" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1128, version=0)
class Microsoft_Windows_TCPIP_1128_0(Etw):
    pattern = Struct(
        "Interface" / Int32ul,
        "Protocol" / CString,
        "DadState" / Int32ul,
        "DlAddrLength" / Int32ul,
        "DLAddress" / Bytes(lambda this: this.DlAddrLength),
        "IpAddrLength" / Int32ul,
        "IPv4Address" / Int32ul,
        "IPv6Address" / Bytes(lambda this: this.IpAddrLength),
        "IPProtocol" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1128, version=1)
class Microsoft_Windows_TCPIP_1128_1(Etw):
    pattern = Struct(
        "Interface" / Int32ul,
        "Protocol" / CString,
        "DadState" / Int32ul,
        "DlAddrLength" / Int32ul,
        "DLAddress" / Bytes(lambda this: this.DlAddrLength),
        "IpAddrLength" / Int32ul,
        "IPv4Address" / Int32ul,
        "IPv6Address" / Bytes(lambda this: this.IpAddrLength),
        "IPProtocol" / Int32ul,
        "CompartmentId" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1130, version=0)
class Microsoft_Windows_TCPIP_1130_0(Etw):
    pattern = Struct(
        "Interface" / Int32ul,
        "OperationalStatus" / Int32ul,
        "Status" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1130, version=1)
class Microsoft_Windows_TCPIP_1130_1(Etw):
    pattern = Struct(
        "Interface" / Int32ul,
        "OperationalStatus" / Int32ul,
        "Status" / Int64ul,
        "CompartmentId" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1136, version=0)
class Microsoft_Windows_TCPIP_1136_0(Etw):
    pattern = Struct(
        "InterfaceIndex" / Int32ul,
        "TraceString" / CString
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1136, version=1)
class Microsoft_Windows_TCPIP_1136_1(Etw):
    pattern = Struct(
        "InterfaceIndex" / Int32ul,
        "TraceString" / CString,
        "CompartmentId" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1137, version=0)
class Microsoft_Windows_TCPIP_1137_0(Etw):
    pattern = Struct(
        "InterfaceIndex" / Int32ul,
        "TraceString" / CString
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1137, version=1)
class Microsoft_Windows_TCPIP_1137_1(Etw):
    pattern = Struct(
        "InterfaceIndex" / Int32ul,
        "TraceString" / CString,
        "CompartmentId" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1138, version=0)
class Microsoft_Windows_TCPIP_1138_0(Etw):
    pattern = Struct(
        "Interface" / Int32ul,
        "Protocol" / CString,
        "DadState" / Int32ul,
        "DlAddrLength" / Int32ul,
        "DLAddress" / Bytes(lambda this: this.DlAddrLength),
        "IpAddrLength" / Int32ul,
        "IPv4Address" / Int32ul,
        "IPv6Address" / Bytes(lambda this: this.IpAddrLength),
        "IPProtocol" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1139, version=0)
class Microsoft_Windows_TCPIP_1139_0(Etw):
    pattern = Struct(
        "Interface" / Int32ul,
        "Protocol" / CString,
        "DadState" / Int32ul,
        "DlAddrLength" / Int32ul,
        "DLAddress" / Bytes(lambda this: this.DlAddrLength),
        "IpAddrLength" / Int32ul,
        "IPv4Address" / Int32ul,
        "IPv6Address" / Bytes(lambda this: this.IpAddrLength),
        "IPProtocol" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1144, version=0)
class Microsoft_Windows_TCPIP_1144_0(Etw):
    pattern = Struct(
        "Interface" / Int32ul,
        "Advertise" / Int32ul,
        "AdvertiseDefaultRoute" / Int32ul,
        "Forward" / Int32ul,
        "ForwardMulticast" / Int32ul,
        "UseNud" / Int32ul,
        "AdvertisingEnabled" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1144, version=1)
class Microsoft_Windows_TCPIP_1144_1(Etw):
    pattern = Struct(
        "Interface" / Int32ul,
        "Advertise" / Int32ul,
        "AdvertiseDefaultRoute" / Int32ul,
        "Forward" / Int32ul,
        "ForwardMulticast" / Int32ul,
        "UseNud" / Int32ul,
        "AdvertisingEnabled" / Int32ul,
        "WeakHostSend" / Int32ul,
        "WeakHostReceive" / Int32ul,
        "CompartmentId" / Int32ul,
        "AddressFamily" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1145, version=0)
class Microsoft_Windows_TCPIP_1145_0(Etw):
    pattern = Struct(
        "Route" / Int64ul,
        "Interface" / Int32ul,
        "DestinationPrefixAddressLength" / Int32ul,
        "NextHopAddressLength" / Int32ul,
        "Protocol" / CString,
        "DestinationPrefixLength" / Int32ul,
        "DestinationPrefix" / Bytes(lambda this: this.DestinationPrefixAddressLength),
        "NextHopAddress" / Bytes(lambda this: this.NextHopAddressLength),
        "ValidLifetime" / Int64ul,
        "PreferredLifetime" / Int64ul,
        "Metric" / Int32ul,
        "Loopback" / Int32ul,
        "AutoconfigureAddress" / Int32ul,
        "Publish" / Int32ul,
        "Immortal" / Int32ul,
        "IPv4DestinationPrefix" / Int32ul,
        "IPv4NextHopAddress" / Int32ul,
        "IPProtocol" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1146, version=0)
class Microsoft_Windows_TCPIP_1146_0(Etw):
    pattern = Struct(
        "Route" / Int64ul,
        "Interface" / Int32ul,
        "DestinationPrefixAddressLength" / Int32ul,
        "NextHopAddressLength" / Int32ul,
        "Protocol" / CString,
        "DestinationPrefixLength" / Int32ul,
        "DestinationPrefix" / Bytes(lambda this: this.DestinationPrefixAddressLength),
        "NextHopAddress" / Bytes(lambda this: this.NextHopAddressLength),
        "ValidLifetime" / Int64ul,
        "PreferredLifetime" / Int64ul,
        "Metric" / Int32ul,
        "Loopback" / Int32ul,
        "AutoconfigureAddress" / Int32ul,
        "Publish" / Int32ul,
        "Immortal" / Int32ul,
        "IPv4DestinationPrefix" / Int32ul,
        "IPv4NextHopAddress" / Int32ul,
        "IPProtocol" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1147, version=0)
class Microsoft_Windows_TCPIP_1147_0(Etw):
    pattern = Struct(
        "Route" / Int64ul,
        "Interface" / Int32ul,
        "DestinationPrefixAddressLength" / Int32ul,
        "NextHopAddressLength" / Int32ul,
        "Protocol" / CString,
        "DestinationPrefixLength" / Int32ul,
        "DestinationPrefix" / Bytes(lambda this: this.DestinationPrefixAddressLength),
        "NextHopAddress" / Bytes(lambda this: this.NextHopAddressLength),
        "ValidLifetime" / Int64ul,
        "PreferredLifetime" / Int64ul,
        "Metric" / Int32ul,
        "Loopback" / Int32ul,
        "AutoconfigureAddress" / Int32ul,
        "Publish" / Int32ul,
        "Immortal" / Int32ul,
        "IPv4DestinationPrefix" / Int32ul,
        "IPv4NextHopAddress" / Int32ul,
        "IPProtocol" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1148, version=0)
class Microsoft_Windows_TCPIP_1148_0(Etw):
    pattern = Struct(
        "Interface" / Int32ul,
        "DlAddrLength" / Int32ul,
        "DlAddress" / Bytes(lambda this: this.DlAddrLength),
        "IpAddrLength" / Int32ul,
        "IPv4Address" / Int32ul,
        "IPv6Address" / Bytes(lambda this: this.IpAddrLength),
        "IPProtocol" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1149, version=0)
class Microsoft_Windows_TCPIP_1149_0(Etw):
    pattern = Struct(
        "Interface" / Int32ul,
        "DlAddrLength" / Int32ul,
        "DlAddress" / Bytes(lambda this: this.DlAddrLength),
        "IpAddrLength" / Int32ul,
        "IPv4Address" / Int32ul,
        "IPv6Address" / Bytes(lambda this: this.IpAddrLength),
        "IPProtocol" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1150, version=0)
class Microsoft_Windows_TCPIP_1150_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "Cwnd" / Int32ul,
        "SSThresh" / Int32ul,
        "RttSample" / Int32ul,
        "NumBytes" / Int32ul,
        "SeqNo" / Int32ul,
        "SndUna" / Int32ul,
        "Round" / Int32ul,
        "SRTT" / Int32ul,
        "RTO" / Int32ul,
        "DWnd" / Int32ul,
        "BaseRtt" / Int32ul,
        "DupAckCount" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1151, version=0)
class Microsoft_Windows_TCPIP_1151_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "Cwnd" / Int32ul,
        "SSThresh" / Int32ul,
        "RttSample" / Int32ul,
        "NumBytes" / Int32ul,
        "SeqNo" / Int32ul,
        "SndUna" / Int32ul,
        "Round" / Int32ul,
        "SRTT" / Int32ul,
        "RTO" / Int32ul,
        "DWnd" / Int32ul,
        "BaseRtt" / Int32ul,
        "DupAckCount" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1152, version=0)
class Microsoft_Windows_TCPIP_1152_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "Cwnd" / Int32ul,
        "SSThresh" / Int32ul,
        "RttSample" / Int32ul,
        "NumBytes" / Int32ul,
        "SeqNo" / Int32ul,
        "SndUna" / Int32ul,
        "Round" / Int32ul,
        "SRTT" / Int32ul,
        "RTO" / Int32ul,
        "DWnd" / Int32ul,
        "BaseRtt" / Int32ul,
        "DupAckCount" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1153, version=0)
class Microsoft_Windows_TCPIP_1153_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "Cwnd" / Int32ul,
        "SSThresh" / Int32ul,
        "RttSample" / Int32ul,
        "NumBytes" / Int32ul,
        "SeqNo" / Int32ul,
        "SndUna" / Int32ul,
        "Round" / Int32ul,
        "SRTT" / Int32ul,
        "RTO" / Int32ul,
        "DWnd" / Int32ul,
        "BaseRtt" / Int32ul,
        "DupAckCount" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1154, version=0)
class Microsoft_Windows_TCPIP_1154_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "Cwnd" / Int32ul,
        "SSThresh" / Int32ul,
        "SndUna" / Int32ul,
        "Mss" / Int32ul,
        "ThAck" / Int32ul,
        "DWnd" / Int32ul,
        "BaseRtt" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1155, version=0)
class Microsoft_Windows_TCPIP_1155_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "Cwnd" / Int32ul,
        "SSThresh" / Int32ul,
        "RttSample" / Int32ul,
        "NumBytes" / Int32ul,
        "SeqNo" / Int32ul,
        "SndUna" / Int32ul,
        "Round" / Int32ul,
        "SRTT" / Int32ul,
        "RTO" / Int32ul,
        "DWnd" / Int32ul,
        "BaseRtt" / Int32ul,
        "DupAckCount" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1156, version=0)
class Microsoft_Windows_TCPIP_1156_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "Delivery" / Int64ul,
        "Request" / Int64ul,
        "NumBytes" / Int64ul,
        "RequestFlags" / Int32ul,
        "Length" / Int64ul,
        "RequestStatus" / Int32ul,
        "IsUrgentDelivery" / Int32ul,
        "FullySatisfiedORDelayedPush" / Int32ul,
        "RcvNxt" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1157, version=0)
class Microsoft_Windows_TCPIP_1157_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "Delivery" / Int64ul,
        "Request" / Int64ul,
        "NumBytes" / Int64ul,
        "RequestFlags" / Int32ul,
        "Length" / Int64ul,
        "RequestStatus" / Int32ul,
        "IsUrgentDelivery" / Int32ul,
        "FullySatisfiedORDelayedPush" / Int32ul,
        "RcvNxt" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1158, version=0)
class Microsoft_Windows_TCPIP_1158_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "Delivery" / Int64ul,
        "Request" / Int64ul,
        "NumBytes" / Int64ul,
        "RequestFlags" / Int32ul,
        "Length" / Int64ul,
        "RequestStatus" / Int32ul,
        "IsUrgentDelivery" / Int32ul,
        "FullySatisfiedORDelayedPush" / Int32ul,
        "RcvNxt" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1159, version=0)
class Microsoft_Windows_TCPIP_1159_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "Injected" / WString,
        "NumBytes" / Int32ul,
        "SndNxt" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1160, version=0)
class Microsoft_Windows_TCPIP_1160_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "Injected" / WString,
        "NumBytes" / Int32ul,
        "SndNxt" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1161, version=0)
class Microsoft_Windows_TCPIP_1161_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "Injected" / WString,
        "NumBytes" / Int32ul,
        "SndNxt" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1162, version=0)
class Microsoft_Windows_TCPIP_1162_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "Status" / Int32ul,
        "AddressFamily" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1163, version=0)
class Microsoft_Windows_TCPIP_1163_0(Etw):
    pattern = Struct(
        "AssignedBlocks" / Int32ul,
        "AllocatedBlocks" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1164, version=0)
class Microsoft_Windows_TCPIP_1164_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "DWnd" / Int32ul,
        "PrevDWnd" / Int32ul,
        "BaseRtt" / Int32ul,
        "AvgRtt" / Int32ul,
        "Cwnd" / Int32ul,
        "DiffWnd" / Int32ul,
        "DwndIncrement" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1165, version=0)
class Microsoft_Windows_TCPIP_1165_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "Gamma" / Int32ul,
        "AverageBacklog" / Int32ul,
        "AverageBacklogAcrossLFP" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1166, version=0)
class Microsoft_Windows_TCPIP_1166_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "SeqNum" / Int32ul,
        "Tick" / Int32ul,
        "RttSample" / Int32ul,
        "NewSrtt" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1167, version=0)
class Microsoft_Windows_TCPIP_1167_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "SeqNum" / Int32ul,
        "Tick" / Int32ul,
        "RttSample" / Int32ul,
        "NewSrtt" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1168, version=0)
class Microsoft_Windows_TCPIP_1168_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "SeqNum" / Int32ul,
        "Tick" / Int32ul,
        "RttSample" / Int32ul,
        "NewSrtt" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1169, version=0)
class Microsoft_Windows_TCPIP_1169_0(Etw):
    pattern = Struct(
        "Endpoint" / Int64ul,
        "NumMessages" / Int32ul,
        "NumBytes" / Int32ul,
        "LocalSockAddrLength" / Int32ul,
        "LocalSockAddr" / Bytes(lambda this: this.LocalSockAddrLength),
        "RemoteSockAddrLength" / Int32ul,
        "RemoteSockAddr" / Bytes(lambda this: this.RemoteSockAddrLength),
        "Pid" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1170, version=0)
class Microsoft_Windows_TCPIP_1170_0(Etw):
    pattern = Struct(
        "Endpoint" / Int64ul,
        "NumMessages" / Int32ul,
        "NumBytes" / Int32ul,
        "LocalSockAddrLength" / Int32ul,
        "LocalSockAddr" / Bytes(lambda this: this.LocalSockAddrLength),
        "RemoteSockAddrLength" / Int32ul,
        "RemoteSockAddr" / Bytes(lambda this: this.RemoteSockAddrLength),
        "Pid" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1171, version=0)
class Microsoft_Windows_TCPIP_1171_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "Delivery" / Int64ul,
        "Request" / Int64ul,
        "NumBytes" / Int64ul,
        "RequestFlags" / Int32ul,
        "Length" / Int64ul,
        "RequestStatus" / Int32ul,
        "IsUrgentDelivery" / Int32ul,
        "FullySatisfiedORDelayedPush" / Int32ul,
        "RcvNxt" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1172, version=0)
class Microsoft_Windows_TCPIP_1172_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "Delivery" / Int64ul,
        "Request" / Int64ul,
        "NumBytes" / Int64ul,
        "RequestFlags" / Int32ul,
        "Length" / Int64ul,
        "RequestStatus" / Int32ul,
        "IsUrgentDelivery" / Int32ul,
        "FullySatisfiedORDelayedPush" / Int32ul,
        "RcvNxt" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1173, version=0)
class Microsoft_Windows_TCPIP_1173_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "Delivery" / Int64ul,
        "Request" / Int64ul,
        "NumBytes" / Int64ul,
        "RequestFlags" / Int32ul,
        "Length" / Int64ul,
        "RequestStatus" / Int32ul,
        "IsUrgentDelivery" / Int32ul,
        "FullySatisfiedORDelayedPush" / Int32ul,
        "RcvNxt" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1174, version=0)
class Microsoft_Windows_TCPIP_1174_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "Delivery" / Int64ul,
        "Request" / Int64ul,
        "NumBytes" / Int64ul,
        "RequestFlags" / Int32ul,
        "Length" / Int64ul,
        "RequestStatus" / Int32ul,
        "IsUrgentDelivery" / Int32ul,
        "FullySatisfiedORDelayedPush" / Int32ul,
        "RcvNxt" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1175, version=0)
class Microsoft_Windows_TCPIP_1175_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "Delivery" / Int64ul,
        "Request" / Int64ul,
        "NumBytes" / Int64ul,
        "RequestFlags" / Int32ul,
        "Length" / Int64ul,
        "RequestStatus" / Int32ul,
        "IsUrgentDelivery" / Int32ul,
        "FullySatisfiedORDelayedPush" / Int32ul,
        "RcvNxt" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1176, version=0)
class Microsoft_Windows_TCPIP_1176_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "Delivery" / Int64ul,
        "Request" / Int64ul,
        "NumBytes" / Int64ul,
        "RequestFlags" / Int32ul,
        "Length" / Int64ul,
        "RequestStatus" / Int32ul,
        "IsUrgentDelivery" / Int32ul,
        "FullySatisfiedORDelayedPush" / Int32ul,
        "RcvNxt" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1178, version=0)
class Microsoft_Windows_TCPIP_1178_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "Delivery" / Int64ul,
        "Request" / Int64ul,
        "NumBytes" / Int64ul,
        "RequestFlags" / Int32ul,
        "Length" / Int64ul,
        "RequestStatus" / Int32ul,
        "IsUrgentDelivery" / Int32ul,
        "FullySatisfiedORDelayedPush" / Int32ul,
        "RcvNxt" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1180, version=0)
class Microsoft_Windows_TCPIP_1180_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "Delivery" / Int64ul,
        "Request" / Int64ul,
        "NumBytes" / Int64ul,
        "RequestFlags" / Int32ul,
        "Length" / Int64ul,
        "RequestStatus" / Int32ul,
        "IsUrgentDelivery" / Int32ul,
        "FullySatisfiedORDelayedPush" / Int32ul,
        "RcvNxt" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1181, version=0)
class Microsoft_Windows_TCPIP_1181_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "Delivery" / Int64ul,
        "Request" / Int64ul,
        "NumBytes" / Int64ul,
        "RequestFlags" / Int32ul,
        "Length" / Int64ul,
        "RequestStatus" / Int32ul,
        "IsUrgentDelivery" / Int32ul,
        "FullySatisfiedORDelayedPush" / Int32ul,
        "RcvNxt" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1182, version=0)
class Microsoft_Windows_TCPIP_1182_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "NewState" / Int32ul,
        "RexmitCount" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1183, version=0)
class Microsoft_Windows_TCPIP_1183_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "NewState" / Int32ul,
        "RexmitCount" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1184, version=0)
class Microsoft_Windows_TCPIP_1184_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "NewState" / Int32ul,
        "RexmitCount" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1185, version=0)
class Microsoft_Windows_TCPIP_1185_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "NewState" / Int32ul,
        "RexmitCount" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1186, version=0)
class Microsoft_Windows_TCPIP_1186_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "NewState" / Int32ul,
        "RexmitCount" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1187, version=0)
class Microsoft_Windows_TCPIP_1187_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "NewState" / Int32ul,
        "RexmitCount" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1188, version=0)
class Microsoft_Windows_TCPIP_1188_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "SndUna" / Int32ul,
        "SndMax" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1189, version=0)
class Microsoft_Windows_TCPIP_1189_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "Delivery" / Int64ul,
        "OldDeliveryState" / Int32ul,
        "NewDeliveryState" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1190, version=0)
class Microsoft_Windows_TCPIP_1190_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "Delivery" / Int64ul,
        "Request" / Int64ul,
        "NumBytes" / Int64ul,
        "RequestFlags" / Int32ul,
        "Length" / Int64ul,
        "RequestStatus" / Int32ul,
        "IsUrgentDelivery" / Int32ul,
        "FullySatisfiedORDelayedPush" / Int32ul,
        "RcvNxt" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1191, version=0)
class Microsoft_Windows_TCPIP_1191_0(Etw):
    pattern = Struct(
        "PortAcquirer" / Int64ul,
        "PortNumber" / Int16ul,
        "WeakReference" / Int32ul,
        "OriginalAcquirer" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1192, version=0)
class Microsoft_Windows_TCPIP_1192_0(Etw):
    pattern = Struct(
        "PortAcquirer" / Int64ul,
        "PortNumber" / Int16ul,
        "WeakReference" / Int32ul,
        "OriginalAcquirer" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1193, version=0)
class Microsoft_Windows_TCPIP_1193_0(Etw):
    pattern = Struct(
        "PortAcquirer" / Int64ul,
        "PortNumber" / Int16ul,
        "WeakReference" / Int32ul,
        "OriginalAcquirer" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1194, version=0)
class Microsoft_Windows_TCPIP_1194_0(Etw):
    pattern = Struct(
        "PortAcquirer" / Int64ul,
        "PortNumber" / Int16ul,
        "WeakReference" / Int32ul,
        "OriginalAcquirer" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1195, version=0)
class Microsoft_Windows_TCPIP_1195_0(Etw):
    pattern = Struct(
        "PortAcquirer" / Int64ul,
        "PortNumber" / Int16ul,
        "WeakReference" / Int32ul,
        "OriginalAcquirer" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1196, version=0)
class Microsoft_Windows_TCPIP_1196_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "SndUna" / Int32ul,
        "SndMax" / Int32ul,
        "Reason" / WString,
        "IsSack" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1197, version=0)
class Microsoft_Windows_TCPIP_1197_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "SndUna" / Int32ul,
        "SndMax" / Int32ul,
        "Reason" / WString,
        "IsSack" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1198, version=0)
class Microsoft_Windows_TCPIP_1198_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "SndUna" / Int32ul,
        "SndMax" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1199, version=0)
class Microsoft_Windows_TCPIP_1199_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "SndUna" / Int32ul,
        "SndMax" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1200, version=0)
class Microsoft_Windows_TCPIP_1200_0(Etw):
    pattern = Struct(
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "Status" / Int32ul,
        "ProcessId" / Int32ul,
        "Compartment" / Int32ul,
        "Tcb" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1201, version=0)
class Microsoft_Windows_TCPIP_1201_0(Etw):
    pattern = Struct(
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "Status" / Int32ul,
        "ProcessId" / Int32ul,
        "Compartment" / Int32ul,
        "Tcb" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1202, version=0)
class Microsoft_Windows_TCPIP_1202_0(Etw):
    pattern = Struct(
        "IfIndex" / Int32ul,
        "LinkSpeed" / Int64ul,
        "IPProtocol" / Int32ul,
        "IPv4Address" / Int32ul,
        "IpAddrLength" / Int32ul,
        "IPv6Address" / Bytes(lambda this: this.IpAddrLength),
        "PhysicalMediumType" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1202, version=1)
class Microsoft_Windows_TCPIP_1202_1(Etw):
    pattern = Struct(
        "IfIndex" / Int32ul,
        "CurrLinkSpeed" / Int64ul,
        "IPProtocol" / Int32ul,
        "IPv4Address" / Int32ul,
        "IpAddrLength" / Int32ul,
        "IPv6Address" / Bytes(lambda this: this.IpAddrLength),
        "PhysicalMediumType" / Int32ul,
        "CompartmentId" / Int32ul,
        "OldLinkSpeed" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1202, version=2)
class Microsoft_Windows_TCPIP_1202_2(Etw):
    pattern = Struct(
        "IfIndex" / Int32ul,
        "CurrLinkSpeed" / Int64ul,
        "IPProtocol" / Int32ul,
        "IPv4Address" / Int32ul,
        "IpAddrLength" / Int32ul,
        "IPv6Address" / Bytes(lambda this: this.IpAddrLength),
        "PhysicalMediumType" / Int32ul,
        "CompartmentId" / Int32ul,
        "OldLinkSpeed" / Int64ul,
        "NetworkCategory" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1202, version=3)
class Microsoft_Windows_TCPIP_1202_3(Etw):
    pattern = Struct(
        "IfIndex" / Int32ul,
        "CurrLinkSpeed" / Int64ul,
        "IPProtocol" / Int32ul,
        "IPv4Address" / Int32ul,
        "IpAddrLength" / Int32ul,
        "IPv6Address" / Bytes(lambda this: this.IpAddrLength),
        "PhysicalMediumType" / Int32ul,
        "CompartmentId" / Int32ul,
        "OldLinkSpeed" / Int64ul,
        "NetworkCategory" / Int32ul,
        "Metric" / Int32ul,
        "Connected" / Int32ul,
        "InternetConnectivityStatus" / Int32ul,
        "Flags" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1203, version=0)
class Microsoft_Windows_TCPIP_1203_0(Etw):
    pattern = Struct(
        "IfIndex" / Int32ul,
        "LinkSpeed" / Int64ul,
        "IPProtocol" / Int32ul,
        "IPv4Address" / Int32ul,
        "IpAddrLength" / Int32ul,
        "IPv6Address" / Bytes(lambda this: this.IpAddrLength),
        "PhysicalMediumType" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1203, version=1)
class Microsoft_Windows_TCPIP_1203_1(Etw):
    pattern = Struct(
        "IfIndex" / Int32ul,
        "CurrLinkSpeed" / Int64ul,
        "IPProtocol" / Int32ul,
        "IPv4Address" / Int32ul,
        "IpAddrLength" / Int32ul,
        "IPv6Address" / Bytes(lambda this: this.IpAddrLength),
        "PhysicalMediumType" / Int32ul,
        "CompartmentId" / Int32ul,
        "OldLinkSpeed" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1203, version=2)
class Microsoft_Windows_TCPIP_1203_2(Etw):
    pattern = Struct(
        "IfIndex" / Int32ul,
        "CurrLinkSpeed" / Int64ul,
        "IPProtocol" / Int32ul,
        "IPv4Address" / Int32ul,
        "IpAddrLength" / Int32ul,
        "IPv6Address" / Bytes(lambda this: this.IpAddrLength),
        "PhysicalMediumType" / Int32ul,
        "CompartmentId" / Int32ul,
        "OldLinkSpeed" / Int64ul,
        "ReceiveLinkSpeed" / Int64ul,
        "MediaConnectState" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1204, version=0)
class Microsoft_Windows_TCPIP_1204_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "SndUna" / Int32ul,
        "SndMax" / Int32ul,
        "Reason" / WString,
        "IsSack" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1205, version=0)
class Microsoft_Windows_TCPIP_1205_0(Etw):
    pattern = Struct(
        "Nbl" / Int64ul,
        "IPTransportProtocol" / Int32ul,
        "AddressFamily" / Int32ul,
        "SourceIPv4Address" / Int32ul,
        "DestIPv4Address" / Int32ul,
        "IPv6SourceIpAddrLength" / Int32ul,
        "IPv6SourceAddress" / Bytes(lambda this: this.IPv6SourceIpAddrLength),
        "IPv6DestIpAddrLength" / Int32ul,
        "IPv6DestAddress" / Bytes(lambda this: this.IPv6DestIpAddrLength),
        "Reason" / Int32ul,
        "NblCount" / Int32ul,
        "IPProtocol" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1206, version=0)
class Microsoft_Windows_TCPIP_1206_0(Etw):
    pattern = Struct(
        "Nbl" / Int64ul,
        "IPTransportProtocol" / Int32ul,
        "AddressFamily" / Int32ul,
        "SourceIPv4Address" / Int32ul,
        "DestIPv4Address" / Int32ul,
        "IPv6SourceIpAddrLength" / Int32ul,
        "IPv6SourceAddress" / Bytes(lambda this: this.IPv6SourceIpAddrLength),
        "IPv6DestIpAddrLength" / Int32ul,
        "IPv6DestAddress" / Bytes(lambda this: this.IPv6DestIpAddrLength),
        "Reason" / Int32ul,
        "NblCount" / Int32ul,
        "IPProtocol" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1207, version=0)
class Microsoft_Windows_TCPIP_1207_0(Etw):
    pattern = Struct(
        "TcpWsdEtwPoint" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1208, version=0)
class Microsoft_Windows_TCPIP_1208_0(Etw):
    pattern = Struct(
        "TcpWsdEtwPoint" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1209, version=0)
class Microsoft_Windows_TCPIP_1209_0(Etw):
    pattern = Struct(
        "TcpWsdEtwPoint" / Int32ul,
        "Tcb" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1210, version=0)
class Microsoft_Windows_TCPIP_1210_0(Etw):
    pattern = Struct(
        "TcpWsdEtwPoint" / Int32ul,
        "Tcb" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1211, version=0)
class Microsoft_Windows_TCPIP_1211_0(Etw):
    pattern = Struct(
        "TcpWsdEtwPoint" / Int32ul,
        "Processor" / Int32ul,
        "Entry" / Int32ul,
        "OldState" / Int32ul,
        "NewState" / Int32ul,
        "ProbeCount" / Int32ul,
        "ProbeCountWs" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1212, version=0)
class Microsoft_Windows_TCPIP_1212_0(Etw):
    pattern = Struct(
        "Profile" / Int32ul,
        "State" / Int32ul,
        "Qualified" / Int32ul,
        "EreQualified" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1213, version=0)
class Microsoft_Windows_TCPIP_1213_0(Etw):
    pattern = Struct(
        "OldEnabledState" / Int32ul,
        "NewEnabledState" / Int32ul,
        "OldThreshold" / Int32ul,
        "NewThreshold" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1214, version=0)
class Microsoft_Windows_TCPIP_1214_0(Etw):
    pattern = Struct(
        "IPTransportProtocol" / Int32ul,
        "AddressFamily" / Int32ul,
        "LocalSockAddrLength" / Int32ul,
        "LocalSockAddr" / Bytes(lambda this: this.LocalSockAddrLength),
        "RemoteSockAddrLength" / Int32ul,
        "RemoteSockAddr" / Bytes(lambda this: this.RemoteSockAddrLength),
        "Reason" / Int32ul,
        "PacketCount" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1215, version=0)
class Microsoft_Windows_TCPIP_1215_0(Etw):
    pattern = Struct(
        "IPTransportProtocol" / Int32ul,
        "AddressFamily" / Int32ul,
        "SourceIPv4Address" / Int32ul,
        "DestIPv4Address" / Int32ul,
        "IPv6SourceIpAddrLength" / Int32ul,
        "IPv6SourceAddress" / Bytes(lambda this: this.IPv6SourceIpAddrLength),
        "IPv6DestIpAddrLength" / Int32ul,
        "IPv6DestAddress" / Bytes(lambda this: this.IPv6DestIpAddrLength),
        "Reason" / Int32ul,
        "PacketCount" / Int32ul,
        "IPProtocol" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1216, version=0)
class Microsoft_Windows_TCPIP_1216_0(Etw):
    pattern = Struct(
        "PhysicalPages" / Int32ul,
        "NonPagedPoolPages" / Int32ul,
        "CurrentWatermark" / Int32ul,
        "PeakWatermark" / Int32ul,
        "HighWatermark" / Int32ul,
        "LowWatermark" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1217, version=0)
class Microsoft_Windows_TCPIP_1217_0(Etw):
    pattern = Struct(
        "LowNppEventState" / Int32ul,
        "HighNppEventState" / Int32ul,
        "EpisodeStartTick" / Int64ul,
        "EpisodeStopTick" / Int64ul,
        "CurrentWatermark" / Int32ul,
        "LowWatermark" / Int32ul,
        "ReentryWatermark" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1218, version=0)
class Microsoft_Windows_TCPIP_1218_0(Etw):
    pattern = Struct(
        "LowNppEventState" / Int32ul,
        "HighNppEventState" / Int32ul,
        "EpisodeStartTick" / Int64ul,
        "EpisodeStopTick" / Int64ul,
        "ReentryWatermark" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1219, version=0)
class Microsoft_Windows_TCPIP_1219_0(Etw):
    pattern = Struct(
        "Epoch" / Int32ul,
        "LowNppEventState" / Int32ul,
        "HighNppEventState" / Int32ul,
        "EpochStartTick" / Int64ul,
        "EpochStopTick" / Int64ul,
        "OldSynDropRate" / Int32ul,
        "NewSynDropRate" / Int32ul,
        "OldTcbAbortionRate" / Int32ul,
        "NewTcbAbortionRate" / Int32ul,
        "CurrentWatermark" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1220, version=0)
class Microsoft_Windows_TCPIP_1220_0(Etw):
    pattern = Struct(
        "Epoch" / Int32ul,
        "LowNppEventState" / Int32ul,
        "HighNppEventState" / Int32ul,
        "EpochStartTick" / Int64ul,
        "EpochStopTick" / Int64ul,
        "SynDropRate" / Int32ul,
        "TcbAbortionRate" / Int32ul,
        "CurrentWatermark" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1221, version=0)
class Microsoft_Windows_TCPIP_1221_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "OldCwnd" / Int32ul,
        "NewCwnd" / Int32ul,
        "Processor" / Int32ul,
        "CurrentTick" / Int32ul,
        "IdleTick" / Int32ul,
        "Rto" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1222, version=0)
class Microsoft_Windows_TCPIP_1222_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "OldCwnd" / Int32ul,
        "NewCwnd" / Int32ul,
        "Processor" / Int32ul,
        "CurrentTick" / Int32ul,
        "IdleTick" / Int32ul,
        "Rto" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1223, version=0)
class Microsoft_Windows_TCPIP_1223_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "TemplateType" / Int32ul,
        "MinRto" / Int32ul,
        "EnableCwndRestart" / Int32ul,
        "InitialCwnd" / Int32ul,
        "CongestionAlgorithm" / Int32ul,
        "MaxDataRetransmissions" / Int32ul,
        "DelayedAckTicks" / Int32ul,
        "DelayedAckFrequency" / Int32ul,
        "Rack" / Int32ul,
        "TailLossProbe" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1224, version=0)
class Microsoft_Windows_TCPIP_1224_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "TemplateType" / Int32ul,
        "Context" / WString
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1225, version=0)
class Microsoft_Windows_TCPIP_1225_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "SndRound" / Int32ul,
        "EcnTotalByteCount" / Int32ul,
        "EcnTotalMarkedCount" / Int32ul,
        "ThAck" / Int32ul,
        "EcnAlpha" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1226, version=0)
class Microsoft_Windows_TCPIP_1226_0(Etw):
    pattern = Struct(
        "IfIndex" / Int32ul,
        "StateV4" / Int32ul,
        "FailureReasonV4" / Int32ul,
        "StateV6" / Int32ul,
        "FailureReasonV6" / Int32ul,
        "Event" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1227, version=0)
class Microsoft_Windows_TCPIP_1227_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "CoalescedSegCount" / Int16ul,
        "DupAckCount" / Int16ul,
        "RscTcpTimestampDelta" / Int32ul,
        "HeaderFlags" / Int16ul,
        "EcnCePresent" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1228, version=0)
class Microsoft_Windows_TCPIP_1228_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "Cause" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1229, version=0)
class Microsoft_Windows_TCPIP_1229_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "OldCwnd" / Int32ul,
        "NewCwnd" / Int32ul,
        "Processor" / Int32ul,
        "CurrentTick" / Int32ul,
        "IdleTick" / Int32ul,
        "Rto" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1230, version=0)
class Microsoft_Windows_TCPIP_1230_0(Etw):
    pattern = Struct(
        "InterfaceIndex" / Int32ul,
        "AddressFamily" / Int16ul,
        "Bind" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1231, version=0)
class Microsoft_Windows_TCPIP_1231_0(Etw):
    pattern = Struct(
        "AdapterIndex" / Int32ul,
        "InterfaceIndex" / Int32ul,
        "PortNumber" / Int32ul,
        "Bind" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1232, version=0)
class Microsoft_Windows_TCPIP_1232_0(Etw):
    pattern = Struct(
        "AdapterIndex" / Int32ul,
        "ExistingInterfaceIndex" / Int32ul,
        "ExistingPortNumber" / Int32ul,
        "ReferenceAdded" / Int8ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1233, version=0)
class Microsoft_Windows_TCPIP_1233_0(Etw):
    pattern = Struct(
        "AdapterIndex" / Int32ul,
        "CapabilitiesFlags" / Int32ul,
        "NumberOfInterruptMessages" / Int32ul,
        "NumberOfReceiveQueues" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1234, version=0)
class Microsoft_Windows_TCPIP_1234_0(Etw):
    pattern = Struct(
        "AdapterIndex" / Int32ul,
        "GroupNumber" / Int16ul,
        "MaximumProcessors" / Int32ul,
        "GroupAffinity" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1235, version=0)
class Microsoft_Windows_TCPIP_1235_0(Etw):
    pattern = Struct(
        "NewAdapterIndex" / Int32ul,
        "ProcessorIndex" / Int32ul,
        "PreviousAdapterIndex" / Int32ul,
        "TriggeringProcessorIndex" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1236, version=0)
class Microsoft_Windows_TCPIP_1236_0(Etw):
    pattern = Struct(
        "PreviousAdapterIndex" / Int32ul,
        "ProcessorIndex" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1237, version=0)
class Microsoft_Windows_TCPIP_1237_0(Etw):
    pattern = Struct(
        "AdapterIndex" / Int32ul,
        "IndirectionIndex" / Int16ul,
        "OldProcessorIndex" / Int32ul,
        "NewProcessorIndex" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1238, version=0)
class Microsoft_Windows_TCPIP_1238_0(Etw):
    pattern = Struct(
        "AdapterIndex" / Int32ul,
        "ProcessorIndex" / Int8ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1239, version=0)
class Microsoft_Windows_TCPIP_1239_0(Etw):
    pattern = Struct(
        "AdapterIndex" / Int32ul,
        "Setting" / Int32ul,
        "Value" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1240, version=0)
class Microsoft_Windows_TCPIP_1240_0(Etw):
    pattern = Struct(
        "InterfaceIndex" / Int32ul,
        "FailureDescription" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1241, version=0)
class Microsoft_Windows_TCPIP_1241_0(Etw):
    pattern = Struct(
        "InterfaceIndex" / Int32ul,
        "AddressFamily" / Int16ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1242, version=0)
class Microsoft_Windows_TCPIP_1242_0(Etw):
    pattern = Struct(
        "AdapterIndex" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1243, version=0)
class Microsoft_Windows_TCPIP_1243_0(Etw):
    pattern = Struct(
        "AdapterIndex" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1244, version=0)
class Microsoft_Windows_TCPIP_1244_0(Etw):
    pattern = Struct(
        "AdapterIndex" / Int32ul,
        "IndirectionTableSize" / Int32ul,
        "IndirectionTable" / Bytes(lambda this: this.IndirectionTableSize),
        "GroupNumber" / Int16ul,
        "ActiveAffinity" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1245, version=0)
class Microsoft_Windows_TCPIP_1245_0(Etw):
    pattern = Struct(
        "InterfaceIndex" / Int32ul,
        "AdapterIndex" / Int32ul,
        "PortNumber" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1246, version=0)
class Microsoft_Windows_TCPIP_1246_0(Etw):
    pattern = Struct(
        "AdapterIndex" / Int32ul,
        "HashInfo" / Int32ul,
        "MaximumProcessors" / Int32ul,
        "GroupNumber" / Int16ul,
        "GroupAffinity" / Int64ul,
        "ActiveAffinity" / Int64ul,
        "ActiveMode" / Int32ul,
        "IndirectionTableSize" / Int32ul,
        "IndirectionTable" / Bytes(lambda this: this.IndirectionTableSize)
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1247, version=0)
class Microsoft_Windows_TCPIP_1247_0(Etw):
    pattern = Struct(
        "InterfaceIndex" / Int32ul,
        "Capability" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1248, version=0)
class Microsoft_Windows_TCPIP_1248_0(Etw):
    pattern = Struct(
        "NdkAdapter" / Int64ul,
        "CqDepth" / Int32ul,
        "CqNotificationContext" / Int64ul,
        "AffinityMask" / Int64ul,
        "AffinityGroup" / Int16ul,
        "RequestContext" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1249, version=0)
class Microsoft_Windows_TCPIP_1249_0(Etw):
    pattern = Struct(
        "RequestContext" / Int64ul,
        "Status" / Int32ul,
        "NdkObject" / Int64ul,
        "CompletionType" / Int32ul,
        "NdkObjectType" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1250, version=0)
class Microsoft_Windows_TCPIP_1250_0(Etw):
    pattern = Struct(
        "NdkObject" / Int64ul,
        "NdkObjectType" / Int32ul,
        "RequestContext" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1251, version=0)
class Microsoft_Windows_TCPIP_1251_0(Etw):
    pattern = Struct(
        "RequestContext" / Int64ul,
        "CompletionType" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1252, version=0)
class Microsoft_Windows_TCPIP_1252_0(Etw):
    pattern = Struct(
        "NdkCq" / Int64ul,
        "CqDepth" / Int32ul,
        "RequestContext" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1253, version=0)
class Microsoft_Windows_TCPIP_1253_0(Etw):
    pattern = Struct(
        "RequestContext" / Int64ul,
        "Status" / Int32ul,
        "CompletionType" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1254, version=0)
class Microsoft_Windows_TCPIP_1254_0(Etw):
    pattern = Struct(
        "NdkCq" / Int64ul,
        "ArmType" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1255, version=0)
class Microsoft_Windows_TCPIP_1255_0(Etw):
    pattern = Struct(
        "NdkCq" / Int64ul,
        "Status" / Int32ul,
        "BytesTransferred" / Int32ul,
        "QpContext" / Int64ul,
        "RequestContext" / Int64ul,
        "ResultIndex" / Int32sl,
        "ResultCount" / Int32sl
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1256, version=0)
class Microsoft_Windows_TCPIP_1256_0(Etw):
    pattern = Struct(
        "NdkPd" / Int64ul,
        "FastRegister" / Int32ul,
        "RequestContext" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1257, version=0)
class Microsoft_Windows_TCPIP_1257_0(Etw):
    pattern = Struct(
        "NdkQp" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1258, version=0)
class Microsoft_Windows_TCPIP_1258_0(Etw):
    pattern = Struct(
        "NdkQp" / Int64ul,
        "RequestContext" / Int64ul,
        "SgeAddress" / Int64ul,
        "SgeLength" / Int32ul,
        "SgeMemoryRegionToken" / Int32ul,
        "NumSge" / Int32sl,
        "Flags" / Int32ul,
        "SgeIndex" / Int32sl
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1259, version=0)
class Microsoft_Windows_TCPIP_1259_0(Etw):
    pattern = Struct(
        "NdkQp" / Int64ul,
        "RequestContext" / Int64ul,
        "SgeAddress" / Int64ul,
        "SgeLength" / Int32ul,
        "SgeMemoryRegionToken" / Int32ul,
        "NumSge" / Int32sl,
        "Flags" / Int32ul,
        "SgeIndex" / Int32sl
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1260, version=0)
class Microsoft_Windows_TCPIP_1260_0(Etw):
    pattern = Struct(
        "NdkMr" / Int64ul,
        "Mdl" / Int64ul,
        "Length" / Int64ul,
        "Flags" / Int32ul,
        "RequestContext" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1261, version=0)
class Microsoft_Windows_TCPIP_1261_0(Etw):
    pattern = Struct(
        "NdkObject" / Int64ul,
        "RequestContext" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1262, version=0)
class Microsoft_Windows_TCPIP_1262_0(Etw):
    pattern = Struct(
        "NdkMr" / Int64ul,
        "AdapterPageCount" / Int32ul,
        "RemoteAccess" / Int32ul,
        "RequestContext" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1263, version=0)
class Microsoft_Windows_TCPIP_1263_0(Etw):
    pattern = Struct(
        "NdkSrq" / Int64ul,
        "SrqDepth" / Int32ul,
        "NotifyThreshold" / Int32ul,
        "RequestContext" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1264, version=0)
class Microsoft_Windows_TCPIP_1264_0(Etw):
    pattern = Struct(
        "NdkConnector" / Int64ul,
        "NdkQp" / Int64ul,
        "SrcSockAddrLength" / Int32ul,
        "SrcSockAddr" / Bytes(lambda this: this.SrcSockAddrLength),
        "DestSockAddrLength" / Int32ul,
        "DestSockAddr" / Bytes(lambda this: this.DestSockAddrLength),
        "IRD" / Int32ul,
        "ORD" / Int32ul,
        "RequestContext" / Int64ul,
        "NdkSharedEndpoint" / Int64ul,
        "PrivateDataLength" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1265, version=0)
class Microsoft_Windows_TCPIP_1265_0(Etw):
    pattern = Struct(
        "NdkConnector" / Int64ul,
        "NdkQp" / Int64ul,
        "SrcSockAddrLength" / Int32ul,
        "SrcSockAddr" / Bytes(lambda this: this.SrcSockAddrLength),
        "DestSockAddrLength" / Int32ul,
        "DestSockAddr" / Bytes(lambda this: this.DestSockAddrLength),
        "IRD" / Int32ul,
        "ORD" / Int32ul,
        "RequestContext" / Int64ul,
        "NdkSharedEndpoint" / Int64ul,
        "PrivateDataLength" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1266, version=0)
class Microsoft_Windows_TCPIP_1266_0(Etw):
    pattern = Struct(
        "NdkConnector" / Int64ul,
        "DisconnectEventContext" / Int64ul,
        "RequestContext" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1267, version=0)
class Microsoft_Windows_TCPIP_1267_0(Etw):
    pattern = Struct(
        "NdkConnector" / Int64ul,
        "NdkQp" / Int64ul,
        "IRD" / Int32ul,
        "ORD" / Int32ul,
        "DisconnectEventContext" / Int64ul,
        "RequestContext" / Int64ul,
        "PrivateDataLength" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1268, version=0)
class Microsoft_Windows_TCPIP_1268_0(Etw):
    pattern = Struct(
        "NdkObject" / Int64ul,
        "RequestContext" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1269, version=0)
class Microsoft_Windows_TCPIP_1269_0(Etw):
    pattern = Struct(
        "NdkListener" / Int64ul,
        "SockAddrLength" / Int32ul,
        "SockAddr" / Bytes(lambda this: this.SockAddrLength),
        "RequestContext" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1270, version=0)
class Microsoft_Windows_TCPIP_1270_0(Etw):
    pattern = Struct(
        "NdkObject" / Int64ul,
        "RequestContext" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1271, version=0)
class Microsoft_Windows_TCPIP_1271_0(Etw):
    pattern = Struct(
        "NdkPd" / Int64ul,
        "SrqDepth" / Int32ul,
        "MaxReceiveRequestSge" / Int32ul,
        "NotifyThreshold" / Int32ul,
        "SrqNotificationContext" / Int64ul,
        "AffinityMask" / Int64ul,
        "AffinityGroup" / Int16ul,
        "RequestContext" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1272, version=0)
class Microsoft_Windows_TCPIP_1272_0(Etw):
    pattern = Struct(
        "NdkPd" / Int64ul,
        "ReceiveCq" / Int64ul,
        "InitiatorCq" / Int64ul,
        "QPContext" / Int64ul,
        "ReceiveQueueDepth" / Int32ul,
        "InitiatorQueueDepth" / Int32ul,
        "MaxReceiveRequestSge" / Int32ul,
        "MaxInitiatorRequestSge" / Int32ul,
        "RequestContext" / Int64ul,
        "NdkSrq" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1273, version=0)
class Microsoft_Windows_TCPIP_1273_0(Etw):
    pattern = Struct(
        "NdkPd" / Int64ul,
        "ReceiveCq" / Int64ul,
        "InitiatorCq" / Int64ul,
        "QPContext" / Int64ul,
        "ReceiveQueueDepth" / Int32ul,
        "InitiatorQueueDepth" / Int32ul,
        "MaxReceiveRequestSge" / Int32ul,
        "MaxInitiatorRequestSge" / Int32ul,
        "RequestContext" / Int64ul,
        "NdkSrq" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1274, version=0)
class Microsoft_Windows_TCPIP_1274_0(Etw):
    pattern = Struct(
        "NdkObject" / Int64ul,
        "RequestContext" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1275, version=0)
class Microsoft_Windows_TCPIP_1275_0(Etw):
    pattern = Struct(
        "NdkListener" / Int64ul,
        "SockAddrLength" / Int32ul,
        "SockAddr" / Bytes(lambda this: this.SockAddrLength),
        "RequestContext" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1276, version=0)
class Microsoft_Windows_TCPIP_1276_0(Etw):
    pattern = Struct(
        "NdkObject" / Int64ul,
        "RequestContext" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1277, version=0)
class Microsoft_Windows_TCPIP_1277_0(Etw):
    pattern = Struct(
        "NdkAdapter" / Int64ul,
        "ConnectEventContext" / Int64ul,
        "RequestContext" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1278, version=0)
class Microsoft_Windows_TCPIP_1278_0(Etw):
    pattern = Struct(
        "NdkAdapter" / Int64ul,
        "Mdl" / Int64ul,
        "Length" / Int64ul,
        "RequestContext" / Int64ul,
        "LAMBuffer" / Int64ul,
        "LAMBufferSize" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1279, version=0)
class Microsoft_Windows_TCPIP_1279_0(Etw):
    pattern = Struct(
        "NdkAdapter" / Int64ul,
        "LAMBuffer" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1280, version=0)
class Microsoft_Windows_TCPIP_1280_0(Etw):
    pattern = Struct(
        "CqNotificationContext" / Int64ul,
        "CqStatus" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1281, version=0)
class Microsoft_Windows_TCPIP_1281_0(Etw):
    pattern = Struct(
        "SrqNotificationContext" / Int64ul,
        "SrqStatus" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1282, version=0)
class Microsoft_Windows_TCPIP_1282_0(Etw):
    pattern = Struct(
        "DisconnectEventContext" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1283, version=0)
class Microsoft_Windows_TCPIP_1283_0(Etw):
    pattern = Struct(
        "ConnectEventContext" / Int64ul,
        "NdkConnector" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1284, version=0)
class Microsoft_Windows_TCPIP_1284_0(Etw):
    pattern = Struct(
        "NdkObject" / Int64ul,
        "NdkObjectType" / Int32ul,
        "TokenType" / Int32ul,
        "Token" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1285, version=0)
class Microsoft_Windows_TCPIP_1285_0(Etw):
    pattern = Struct(
        "NdkObject" / Int64ul,
        "NdkObjectType" / Int32ul,
        "SockAddrType" / Int32ul,
        "SockAddrLength" / Int32ul,
        "SockAddr" / Bytes(lambda this: this.SockAddrLength)
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1286, version=0)
class Microsoft_Windows_TCPIP_1286_0(Etw):
    pattern = Struct(
        "NdkObject" / Int64ul,
        "NdkObjectType" / Int32ul,
        "SockAddrType" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1287, version=0)
class Microsoft_Windows_TCPIP_1287_0(Etw):
    pattern = Struct(
        "NdkConnector" / Int64ul,
        "PrivateDataLength" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1288, version=0)
class Microsoft_Windows_TCPIP_1288_0(Etw):
    pattern = Struct(
        "NdkConnector" / Int64ul,
        "IRD" / Int32ul,
        "ORD" / Int32ul,
        "PrivateDataLength" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1289, version=0)
class Microsoft_Windows_TCPIP_1289_0(Etw):
    pattern = Struct(
        "NdkQp" / Int64ul,
        "RequestContext" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1290, version=0)
class Microsoft_Windows_TCPIP_1290_0(Etw):
    pattern = Struct(
        "NdkQp" / Int64ul,
        "RequestContext" / Int64ul,
        "NdkMr" / Int64ul,
        "NdkMw" / Int64ul,
        "VirtualAddress" / Int64ul,
        "Length" / Int64ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1291, version=0)
class Microsoft_Windows_TCPIP_1291_0(Etw):
    pattern = Struct(
        "NdkQp" / Int64ul,
        "RequestContext" / Int64ul,
        "NdkMr" / Int64ul,
        "AdapterPageCount" / Int32ul,
        "AdapterPageArray" / Int64ul,
        "FBO" / Int32ul,
        "Length" / Int64ul,
        "BaseVirtualAddress" / Int64ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1292, version=0)
class Microsoft_Windows_TCPIP_1292_0(Etw):
    pattern = Struct(
        "NdkQp" / Int64ul,
        "RequestContext" / Int64ul,
        "NdkObject" / Int64ul,
        "NdkObjectType" / Int32ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1293, version=0)
class Microsoft_Windows_TCPIP_1293_0(Etw):
    pattern = Struct(
        "NdkQp" / Int64ul,
        "RequestContext" / Int64ul,
        "SgeAddress" / Int64ul,
        "SgeLength" / Int32ul,
        "SgeMemoryRegionToken" / Int32ul,
        "NumSge" / Int32sl,
        "Flags" / Int32ul,
        "SgeIndex" / Int32sl,
        "RemoteAddress" / Int64ul,
        "RemoteToken" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1294, version=0)
class Microsoft_Windows_TCPIP_1294_0(Etw):
    pattern = Struct(
        "NdkQp" / Int64ul,
        "RequestContext" / Int64ul,
        "SgeAddress" / Int64ul,
        "SgeLength" / Int32ul,
        "SgeMemoryRegionToken" / Int32ul,
        "NumSge" / Int32sl,
        "Flags" / Int32ul,
        "SgeIndex" / Int32sl,
        "RemoteAddress" / Int64ul,
        "RemoteToken" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1295, version=0)
class Microsoft_Windows_TCPIP_1295_0(Etw):
    pattern = Struct(
        "NdkSrq" / Int64ul,
        "RequestContext" / Int64ul,
        "SgeAddress" / Int64ul,
        "SgeLength" / Int32ul,
        "SgeMemoryRegionToken" / Int32ul,
        "NumSge" / Int32sl,
        "Flags" / Int32ul,
        "SgeIndex" / Int32sl
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1296, version=0)
class Microsoft_Windows_TCPIP_1296_0(Etw):
    pattern = Struct(
        "NdkSrq" / Int64ul,
        "RequestContext" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1297, version=0)
class Microsoft_Windows_TCPIP_1297_0(Etw):
    pattern = Struct(
        "InterfaceIndex" / Int32ul,
        "NdkAdapter" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1298, version=0)
class Microsoft_Windows_TCPIP_1298_0(Etw):
    pattern = Struct(
        "NdkAdapter" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1299, version=0)
class Microsoft_Windows_TCPIP_1299_0(Etw):
    pattern = Struct(
        "NdkAdapter" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1300, version=0)
class Microsoft_Windows_TCPIP_1300_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "State" / Int32ul,
        "Pid" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1301, version=0)
class Microsoft_Windows_TCPIP_1301_0(Etw):
    pattern = Struct(
        "InterfaceIndex" / Int32ul,
        "EventDescription" / Int32ul,
        "NDKOperational" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1302, version=0)
class Microsoft_Windows_TCPIP_1302_0(Etw):
    pattern = Struct(
        "AdapterLuid" / Int64ul,
        "PatternFriendlyName" / WString,
        "DlAddrLength" / Int32ul,
        "SrcDLAddress" / Bytes(lambda this: this.DlAddrLength),
        "DestDLAddress" / Bytes(lambda this: this.DlAddrLength),
        "SrcAddress" / Int32ul,
        "DestAddress" / Int32ul,
        "Protocol" / Int32ul,
        "SrcPort" / Int16ul,
        "DestPort" / Int16ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1303, version=0)
class Microsoft_Windows_TCPIP_1303_0(Etw):
    pattern = Struct(
        "AdapterLuid" / Int64ul,
        "PatternFriendlyName" / WString,
        "DlAddrLength" / Int32ul,
        "SrcDLAddress" / Bytes(lambda this: this.DlAddrLength),
        "DestDLAddress" / Bytes(lambda this: this.DlAddrLength),
        "IpAddrLength" / Int32ul,
        "SrcAddress" / Bytes(lambda this: this.IpAddrLength),
        "DestAddress" / Bytes(lambda this: this.IpAddrLength),
        "Protocol" / Int32ul,
        "SrcPort" / Int16ul,
        "DestPort" / Int16ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1304, version=0)
class Microsoft_Windows_TCPIP_1304_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "SilentModeEvent" / Int32ul,
        "Context" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1305, version=0)
class Microsoft_Windows_TCPIP_1305_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "NcmContext" / Int64ul,
        "State" / Int32ul,
        "Pid" / Int32ul,
        "IsLoopback" / Int32ul,
        "ChannelStatus" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1306, version=0)
class Microsoft_Windows_TCPIP_1306_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "NcmContext" / Int64ul,
        "State" / Int32ul,
        "Pid" / Int32ul,
        "IsLoopback" / Int32ul,
        "ChannelStatus" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1307, version=0)
class Microsoft_Windows_TCPIP_1307_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "NcmContext" / Int64ul,
        "Pid" / Int32ul,
        "Status" / Int32ul,
        "PushNotificationGuid" / Guid
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1308, version=0)
class Microsoft_Windows_TCPIP_1308_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "NcmContext" / Int64ul,
        "Pid" / Int32ul,
        "RcvNxt" / Int32ul,
        "Delivered" / Int32ul,
        "Indicated" / Int32ul,
        "FinalEvent" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1309, version=0)
class Microsoft_Windows_TCPIP_1309_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "NcmContext" / Int64ul,
        "State" / Int32ul,
        "Pid" / Int32ul,
        "IsLoopback" / Int32ul,
        "ChannelStatus" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1310, version=0)
class Microsoft_Windows_TCPIP_1310_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "NcmContext" / Int64ul,
        "State" / Int32ul,
        "Pid" / Int32ul,
        "IsLoopback" / Int32ul,
        "ChannelStatus" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1311, version=0)
class Microsoft_Windows_TCPIP_1311_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "SystemReserved" / Int32ul,
        "WolHandle" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1312, version=0)
class Microsoft_Windows_TCPIP_1312_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "SystemReserved" / Int32ul,
        "WolHandle" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1313, version=0)
class Microsoft_Windows_TCPIP_1313_0(Etw):
    pattern = Struct(
        "InterfaceIndex" / Int32ul,
        "AoAcCapable" / Int32ul,
        "BitmapPatternSupported" / Int32ul,
        "ARPNDOffloadSupported" / Int32ul,
        "IPAddressWakeReady" / Int32ul,
        "PatternPriority" / Int32ul,
        "PhysicalMediumType" / Int32ul,
        "IpAddrLength" / Int32ul,
        "IPv4Address" / Int32ul,
        "IPv6Address" / Bytes(lambda this: this.IpAddrLength),
        "IPProtocol" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1314, version=0)
class Microsoft_Windows_TCPIP_1314_0(Etw):
    pattern = Struct(
        "NdkCq" / Int64ul,
        "ModerationInterval" / Int32ul,
        "ModerationCount" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1315, version=0)
class Microsoft_Windows_TCPIP_1315_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "IsRedirected" / Int32ul,
        "WfpFailure" / Int32ul,
        "Status" / Int32ul,
        "WaitStatus" / Int32ul,
        "IpAddrLength" / Int32ul,
        "LocalIPv4Address" / Int32ul,
        "LocalIPv6Address" / Bytes(lambda this: this.IpAddrLength),
        "IPProtocol" / Int32ul,
        "RemoteIPv4Address" / Int32ul,
        "RemoteIPv6Address" / Bytes(lambda this: this.IpAddrLength),
        "SrcPort" / Int16ul,
        "DestPort" / Int16ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1316, version=0)
class Microsoft_Windows_TCPIP_1316_0(Etw):
    pattern = Struct(
        "Interface" / Int32ul,
        "Protocol" / CString,
        "IpAddrLength" / Int32ul,
        "IPv4Address" / Int32ul,
        "IPv6Address" / Bytes(lambda this: this.IpAddrLength),
        "IPProtocol" / Int32ul,
        "CurrentTime" / Int32ul,
        "OldBaseTime" / Int32ul,
        "OldValidTime" / Int32ul,
        "OldPreferredTime" / Int32ul,
        "NewBaseTime" / Int32ul,
        "NewValidTime" / Int32ul,
        "NewPreferredTime" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1317, version=0)
class Microsoft_Windows_TCPIP_1317_0(Etw):
    pattern = Struct(
        "Event" / Int64ul,
        "Type" / Int32ul,
        "Processor" / Int32ul,
        "PowerSource" / Int32ul,
        "OldPartitionCount" / Int32ul,
        "NewPartitionCount" / Int32ul,
        "Progress" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1318, version=0)
class Microsoft_Windows_TCPIP_1318_0(Etw):
    pattern = Struct(
        "Component" / Int32ul,
        "PowerStateTransition" / Int32ul,
        "IndicatingProcessor" / Int32ul,
        "CurrentTick" / Int32ul,
        "CurrentTime" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1319, version=0)
class Microsoft_Windows_TCPIP_1319_0(Etw):
    pattern = Struct(
        "Component" / Int32ul,
        "IndicatingProcessor" / Int32ul,
        "TargetProcessor" / Int32ul,
        "CurrentTick" / Int32ul,
        "NextExpirationTick" / Int32ul,
        "OldScheduledExpiration" / Int64ul,
        "NewScheduledExpiration" / Int64ul,
        "DueTime" / Int64sl,
        "Aperiodic" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1320, version=0)
class Microsoft_Windows_TCPIP_1320_0(Etw):
    pattern = Struct(
        "Component" / Int32ul,
        "TargetProcessor" / Int32ul,
        "CurrentTick" / Int32ul,
        "NextExpiration" / Int32ul,
        "CurrentInterruptTime" / Int64ul,
        "ScheduledExpirationTime" / Int64ul,
        "ExternalTrigger" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1321, version=0)
class Microsoft_Windows_TCPIP_1321_0(Etw):
    pattern = Struct(
        "InterfaceIndex" / Int32ul,
        "TraceString" / CString
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1321, version=1)
class Microsoft_Windows_TCPIP_1321_1(Etw):
    pattern = Struct(
        "InterfaceIndex" / Int32ul,
        "TraceString" / CString,
        "CompartmentId" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1322, version=0)
class Microsoft_Windows_TCPIP_1322_0(Etw):
    pattern = Struct(
        "InterfaceIndex" / Int32ul,
        "TraceString" / CString
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1322, version=1)
class Microsoft_Windows_TCPIP_1322_1(Etw):
    pattern = Struct(
        "InterfaceIndex" / Int32ul,
        "TraceString" / CString,
        "CompartmentId" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1323, version=0)
class Microsoft_Windows_TCPIP_1323_0(Etw):
    pattern = Struct(
        "InterfaceIndex" / Int32ul,
        "TraceString" / CString
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1323, version=1)
class Microsoft_Windows_TCPIP_1323_1(Etw):
    pattern = Struct(
        "InterfaceIndex" / Int32ul,
        "TraceString" / CString,
        "CompartmentId" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1324, version=0)
class Microsoft_Windows_TCPIP_1324_0(Etw):
    pattern = Struct(
        "Interface" / Int32ul,
        "IpAddrLength" / Int32ul,
        "IPAddress" / Bytes(lambda this: this.IpAddrLength),
        "DlAddrLength" / Int32ul,
        "DLAddress" / Bytes(lambda this: this.DlAddrLength),
        "OldNeighborState" / Int32ul,
        "NewNeighborState" / Int32ul,
        "NeighborEvent" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1324, version=1)
class Microsoft_Windows_TCPIP_1324_1(Etw):
    pattern = Struct(
        "Interface" / Int32ul,
        "IpAddrLength" / Int32ul,
        "IPAddress" / Bytes(lambda this: this.IpAddrLength),
        "DlAddrLength" / Int32ul,
        "DLAddress" / Bytes(lambda this: this.DlAddrLength),
        "OldNeighborState" / Int32ul,
        "NewNeighborState" / Int32ul,
        "NeighborEvent" / Int32ul,
        "CompartmentId" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1325, version=0)
class Microsoft_Windows_TCPIP_1325_0(Etw):
    pattern = Struct(
        "Interface" / Int32ul,
        "IpAddrLength" / Int32ul,
        "SourceIPAddress" / Bytes(lambda this: this.IpAddrLength),
        "TargetIPAddress" / Bytes(lambda this: this.IpAddrLength),
        "NeighborEvent" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1325, version=1)
class Microsoft_Windows_TCPIP_1325_1(Etw):
    pattern = Struct(
        "Interface" / Int32ul,
        "IpAddrLength" / Int32ul,
        "SourceIPAddress" / Bytes(lambda this: this.IpAddrLength),
        "TargetIPAddress" / Bytes(lambda this: this.IpAddrLength),
        "NeighborEvent" / Int32ul,
        "CompartmentId" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1326, version=0)
class Microsoft_Windows_TCPIP_1326_0(Etw):
    pattern = Struct(
        "IpAddrLength" / Int32ul,
        "PreferredSourceIPAddress" / Bytes(lambda this: this.IpAddrLength),
        "NonPreferredSourceIPAddress" / Bytes(lambda this: this.IpAddrLength),
        "DestinationIPAddress" / Bytes(lambda this: this.IpAddrLength),
        "CompartmentId" / Int32ul,
        "Rule" / Int32ul,
        "RuleExtension" / Int32ul,
        "RuleName" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1327, version=0)
class Microsoft_Windows_TCPIP_1327_0(Etw):
    pattern = Struct(
        "IpAddrLength" / Int32ul,
        "PreferredSourceIPAddress" / Bytes(lambda this: this.IpAddrLength),
        "PreferredDestinationIPAddress" / Bytes(lambda this: this.IpAddrLength),
        "NonPreferredSourceIPAddress" / Bytes(lambda this: this.IpAddrLength),
        "NonPreferredDestinationIPAddress" / Bytes(lambda this: this.IpAddrLength),
        "SortOption" / Int32ul,
        "RuleType" / CString,
        "RuleMajor" / Int32ul,
        "RuleMinor" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1327, version=1)
class Microsoft_Windows_TCPIP_1327_1(Etw):
    pattern = Struct(
        "IpAddrLength" / Int32ul,
        "PreferredSourceIPAddress" / Bytes(lambda this: this.IpAddrLength),
        "PreferredDestinationIPAddress" / Bytes(lambda this: this.IpAddrLength),
        "NonPreferredSourceIPAddress" / Bytes(lambda this: this.IpAddrLength),
        "NonPreferredDestinationIPAddress" / Bytes(lambda this: this.IpAddrLength),
        "SortOption" / Int32ul,
        "RuleType" / CString,
        "RuleMajor" / Int32ul,
        "RuleMinor" / Int32ul,
        "RuleName" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1328, version=0)
class Microsoft_Windows_TCPIP_1328_0(Etw):
    pattern = Struct(
        "NdkCq" / Int64ul,
        "Status" / Int32ul,
        "BytesTransferred" / Int32ul,
        "QpContext" / Int64ul,
        "RequestContext" / Int64ul,
        "ResultIndex" / Int32sl,
        "ResultCount" / Int32sl,
        "Type" / Int32ul,
        "TypeSpecificCompletionOutput" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1329, version=0)
class Microsoft_Windows_TCPIP_1329_0(Etw):
    pattern = Struct(
        "NdkQp" / Int64ul,
        "RequestContext" / Int64ul,
        "SgeAddress" / Int64ul,
        "SgeLength" / Int32ul,
        "SgeMemoryRegionToken" / Int32ul,
        "NumSge" / Int32sl,
        "Flags" / Int32ul,
        "SgeIndex" / Int32sl,
        "RemoteToken" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1330, version=0)
class Microsoft_Windows_TCPIP_1330_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "Cwnd" / Int32ul,
        "SndWnd" / Int32ul,
        "BytesAcked" / Int32ul,
        "SeqNo" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1331, version=0)
class Microsoft_Windows_TCPIP_1331_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "Cwnd" / Int32ul,
        "SndWnd" / Int32ul,
        "BytesAcked" / Int32ul,
        "SeqNo" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1332, version=0)
class Microsoft_Windows_TCPIP_1332_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "Cwnd" / Int32ul,
        "SndWnd" / Int32ul,
        "BytesSent" / Int32ul,
        "SeqNo" / Int32ul,
        "SRtt" / Int32ul,
        "RttVar" / Int32ul,
        "RTO" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1332, version=1)
class Microsoft_Windows_TCPIP_1332_1(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "Cwnd" / Int32ul,
        "SndWnd" / Int32ul,
        "BytesSent" / Int32ul,
        "SeqNo" / Int32ul,
        "SRtt" / Int32ul,
        "RttVar" / Int32ul,
        "RTO" / Int32ul,
        "RcvWnd" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1333, version=0)
class Microsoft_Windows_TCPIP_1333_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "Cwnd" / Int32ul,
        "SndWnd" / Int32ul,
        "BytesSent" / Int32ul,
        "SeqNo" / Int32ul,
        "SRtt" / Int32ul,
        "RttVar" / Int32ul,
        "RTO" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1333, version=1)
class Microsoft_Windows_TCPIP_1333_1(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "Cwnd" / Int32ul,
        "SndWnd" / Int32ul,
        "BytesSent" / Int32ul,
        "SeqNo" / Int32ul,
        "SRtt" / Int32ul,
        "RttVar" / Int32ul,
        "RTO" / Int32ul,
        "RcvWnd" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1334, version=0)
class Microsoft_Windows_TCPIP_1334_0(Etw):
    pattern = Struct(
        "UdpEndpoint" / Int64ul,
        "NcmContext" / Int64ul,
        "Activated" / Int32ul,
        "Pid" / Int32ul,
        "IsLoopback" / Int32ul,
        "ChannelStatus" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1335, version=0)
class Microsoft_Windows_TCPIP_1335_0(Etw):
    pattern = Struct(
        "UdpEndpoint" / Int64ul,
        "NcmContext" / Int64ul,
        "Activated" / Int32ul,
        "Pid" / Int32ul,
        "IsLoopback" / Int32ul,
        "ChannelStatus" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1336, version=0)
class Microsoft_Windows_TCPIP_1336_0(Etw):
    pattern = Struct(
        "UdpEndpoint" / Int64ul,
        "NcmContext" / Int64ul,
        "Pid" / Int32ul,
        "Status" / Int32ul,
        "PushNotificationGuid" / Guid
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1337, version=0)
class Microsoft_Windows_TCPIP_1337_0(Etw):
    pattern = Struct(
        "UdpEndpoint" / Int64ul,
        "NcmContext" / Int64ul,
        "Pid" / Int32ul,
        "Delivered" / Int32ul,
        "FinalEvent" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1338, version=0)
class Microsoft_Windows_TCPIP_1338_0(Etw):
    pattern = Struct(
        "UdpEndpoint" / Int64ul,
        "NcmContext" / Int64ul,
        "Activated" / Int32ul,
        "Pid" / Int32ul,
        "IsLoopback" / Int32ul,
        "ChannelStatus" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1339, version=0)
class Microsoft_Windows_TCPIP_1339_0(Etw):
    pattern = Struct(
        "UdpEndpoint" / Int64ul,
        "NcmContext" / Int64ul,
        "Activated" / Int32ul,
        "Pid" / Int32ul,
        "IsLoopback" / Int32ul,
        "ChannelStatus" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1340, version=0)
class Microsoft_Windows_TCPIP_1340_0(Etw):
    pattern = Struct(
        "UdpEndpoint" / Int64ul,
        "IpAddrLength" / Int32ul,
        "LocalIPv4Address" / Int32ul,
        "LocalIPv6Address" / Bytes(lambda this: this.IpAddrLength),
        "IPProtocol" / Int32ul,
        "SrcPort" / Int16ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1341, version=0)
class Microsoft_Windows_TCPIP_1341_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "RttSample" / Int32ul,
        "RttVar" / Int32ul,
        "SRTT" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1342, version=0)
class Microsoft_Windows_TCPIP_1342_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "RttSample" / Int32ul,
        "RttVar" / Int32ul,
        "SRTT" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1343, version=0)
class Microsoft_Windows_TCPIP_1343_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "Cwnd" / Int32ul,
        "SSThresh" / Int32ul,
        "DupAckCount" / Int32ul,
        "SeqNo" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1344, version=0)
class Microsoft_Windows_TCPIP_1344_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "Cwnd" / Int32ul,
        "SSThresh" / Int32ul,
        "DupAckCount" / Int32ul,
        "SeqNo" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1345, version=0)
class Microsoft_Windows_TCPIP_1345_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "SeqNo" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1346, version=0)
class Microsoft_Windows_TCPIP_1346_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "SeqNo" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1347, version=0)
class Microsoft_Windows_TCPIP_1347_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "SeqNo" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1348, version=0)
class Microsoft_Windows_TCPIP_1348_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "Cwnd" / Int32ul,
        "SSThresh" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1349, version=0)
class Microsoft_Windows_TCPIP_1349_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "Cwnd" / Int32ul,
        "SSThresh" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1350, version=0)
class Microsoft_Windows_TCPIP_1350_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "Cwnd" / Int32ul,
        "SSThresh" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1351, version=0)
class Microsoft_Windows_TCPIP_1351_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "SndUna" / Int32ul,
        "RexmitCount" / Int32ul,
        "SRTT" / Int32ul,
        "RTO" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1352, version=0)
class Microsoft_Windows_TCPIP_1352_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "DataBytesOut" / Int64ul,
        "DataBytesIn" / Int64ul,
        "DataSegmentsOut" / Int64ul,
        "DataSegmentsIn" / Int64ul,
        "SegmentsOut" / Int64ul,
        "SegmentsIn" / Int64ul,
        "NonRecovDa" / Int32ul,
        "NonRecovDaEpisodes" / Int32ul,
        "DupAcksIn" / Int32ul,
        "BytesRetrans" / Int32ul,
        "Timeouts" / Int32ul,
        "SpuriousRtoDetections" / Int32ul,
        "FastRetran" / Int32ul,
        "MaxSsthresh" / Int32ul,
        "MaxSsCwnd" / Int32ul,
        "MaxCaCwnd" / Int32ul,
        "SndLimTransRwin" / Int32ul,
        "SndLimTimeRwin" / Int32ul,
        "SndLimBytesRwin" / Int64ul,
        "SndLimTransCwnd" / Int32ul,
        "SndLimTimeCwnd" / Int32ul,
        "SndLimBytesCwnd" / Int64ul,
        "SndLimTransSnd" / Int32ul,
        "SndLimTimeRSnd" / Int32ul,
        "SndLimBytesRSnd" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1353, version=0)
class Microsoft_Windows_TCPIP_1353_0(Etw):
    pattern = Struct(
        "AllocationObjectString" / WString,
        "Param1" / Int64ul,
        "Param2" / Int64ul,
        "Param3" / Int32ul,
        "Param4" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1354, version=0)
class Microsoft_Windows_TCPIP_1354_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "SndUna" / Int32ul,
        "SndMax" / Int32ul,
        "SackCount" / Int32ul,
        "SackBytes" / Int32ul,
        "SackInFlight" / Int32ul,
        "SackIsLost" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1355, version=0)
class Microsoft_Windows_TCPIP_1355_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "RequireAddressCoalescing" / Int32ul,
        "LocalPort" / Int16ul,
        "RtcStartPort" / Int16ul,
        "RtcEndPort" / Int16ul,
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1356, version=0)
class Microsoft_Windows_TCPIP_1356_0(Etw):
    pattern = Struct(
        "AssignedFromRtcRange" / Int32ul,
        "Port" / Int16ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1357, version=0)
class Microsoft_Windows_TCPIP_1357_0(Etw):
    pattern = Struct(
        "RequestType" / Int32ul,
        "TcbOrEndpoint" / Int64ul,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "Status" / Int32ul,
        "ProcessId" / Int32ul,
        "InterfaceIndex" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1358, version=0)
class Microsoft_Windows_TCPIP_1358_0(Etw):
    pattern = Struct(
        "InterfaceIndex" / Int32ul,
        "Property" / CString,
        "Value" / Int32ul,
        "InterfaceUpdateEvent" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1358, version=1)
class Microsoft_Windows_TCPIP_1358_1(Etw):
    pattern = Struct(
        "InterfaceIndex" / Int32ul,
        "Property" / CString,
        "Value" / Int32ul,
        "InterfaceUpdateEvent" / Int32ul,
        "CompartmentId" / Int32ul,
        "AddressFamily" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1359, version=0)
class Microsoft_Windows_TCPIP_1359_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "NcmContext" / Int64ul,
        "State" / Int32ul,
        "Pid" / Int32ul,
        "IsLoopback" / Int32ul,
        "IsShutdown" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1360, version=0)
class Microsoft_Windows_TCPIP_1360_0(Etw):
    pattern = Struct(
        "Nbl" / Int64ul,
        "ClonedNbl" / Int64ul,
        "IPTransportProtocol" / Int32ul,
        "AddressFamily" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1361, version=0)
class Microsoft_Windows_TCPIP_1361_0(Etw):
    pattern = Struct(
        "Nbl" / Int64ul,
        "ClonedNbl" / Int64ul,
        "AddressFamily" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1362, version=0)
class Microsoft_Windows_TCPIP_1362_0(Etw):
    pattern = Struct(
        "Interface" / Int32ul,
        "IpAddrLength" / Int32ul,
        "IPAddress" / Bytes(lambda this: this.IpAddrLength),
        "WoLEvent" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1363, version=0)
class Microsoft_Windows_TCPIP_1363_0(Etw):
    pattern = Struct(
        "Interface" / Int32ul,
        "IpAddrLength" / Int32ul,
        "WolHandle" / Int32ul,
        "DestinationIPAddress" / Bytes(lambda this: this.IpAddrLength),
        "TargetIPAddress1" / Bytes(lambda this: this.IpAddrLength),
        "TargetIPAddress2" / Bytes(lambda this: this.IpAddrLength),
        "Flags" / Int32ul,
        "WoLEvent" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1364, version=0)
class Microsoft_Windows_TCPIP_1364_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "NewState" / Int32ul,
        "RexmitCount" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1365, version=0)
class Microsoft_Windows_TCPIP_1365_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "NewState" / Int32ul,
        "RexmitCount" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1366, version=0)
class Microsoft_Windows_TCPIP_1366_0(Etw):
    pattern = Struct(
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1367, version=0)
class Microsoft_Windows_TCPIP_1367_0(Etw):
    pattern = Struct(
        "Nbl" / Int64ul,
        "PathDirection" / Int32ul,
        "TcpIpChecksumNetBufferListInfo" / Int64ul,
        "TcpLargeSendNetBufferListInfo" / Int64ul,
        "Ieee8021QNetBufferListInfo" / Int64ul,
        "NetBufferListHashValue" / Int64ul,
        "NetBufferListHashInfo" / Int64ul,
        "VirtualSubnetInfo" / Int64ul,
        "TcpRecvSegCoalesceInfo" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1367, version=1)
class Microsoft_Windows_TCPIP_1367_1(Etw):
    pattern = Struct(
        "Nbl" / Int64ul,
        "PathDirection" / Int32ul,
        "TcpIpChecksumNetBufferListInfo" / Int64ul,
        "TcpLargeSendNetBufferListInfo" / Int64ul,
        "Ieee8021QNetBufferListInfo" / Int64ul,
        "NetBufferListHashValue" / Int64ul,
        "NetBufferListHashInfo" / Int64ul,
        "VirtualSubnetInfo" / Int64ul,
        "TcpRecvSegCoalesceInfo" / Int64ul,
        "NrtNameResolutionInfo" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1368, version=0)
class Microsoft_Windows_TCPIP_1368_0(Etw):
    pattern = Struct(
        "PID" / Int64ul,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "AddressType" / Int32ul,
        "ScopeLevel" / Int32ul,
        "Port" / Int32ul,
        "EndpointRecord" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1369, version=0)
class Microsoft_Windows_TCPIP_1369_0(Etw):
    pattern = Struct(
        "PID" / Int64ul,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "AddressType" / Int32ul,
        "ScopeLevel" / Int32ul,
        "Port" / Int32ul,
        "EndpointRecord" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1370, version=0)
class Microsoft_Windows_TCPIP_1370_0(Etw):
    pattern = Struct(
        "API" / CString,
        "IpAddrLength" / Int32ul,
        "DestinationAddress" / Bytes(lambda this: this.IpAddrLength),
        "ConstrainSourceAddress" / Bytes(lambda this: this.IpAddrLength),
        "ConstrainInterfaceIndex" / Int32ul,
        "ConstraintOverridden" / Int32ul,
        "ReturnConstrained" / Int32ul,
        "OutgoingInterfaceIndex" / Int32ul,
        "NextHopAddress" / Bytes(lambda this: this.IpAddrLength),
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1371, version=0)
class Microsoft_Windows_TCPIP_1371_0(Etw):
    pattern = Struct(
        "IpAddrLength" / Int32ul,
        "DestinationAddress" / Bytes(lambda this: this.IpAddrLength),
        "ConstrainSourceAddress" / Bytes(lambda this: this.IpAddrLength),
        "ConstrainInterfaceIndex" / Int32ul,
        "OutgoingInterfaceIndex" / Int32ul,
        "ReturnConstrained" / Int32ul,
        "SelectedSourceAddress" / Bytes(lambda this: this.IpAddrLength)
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1372, version=0)
class Microsoft_Windows_TCPIP_1372_0(Etw):
    pattern = Struct(
        "PartitionCount" / Int64ul,
        "PartitionMask" / Int64ul,
        "PartitionId" / Int64ul,
        "NumEntries" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1373, version=0)
class Microsoft_Windows_TCPIP_1373_0(Etw):
    pattern = Struct(
        "OldPartitionCount" / Int64ul,
        "OldPartitionMask" / Int64ul,
        "NewPartitionCount" / Int64ul,
        "NewPartitionMask" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1374, version=0)
class Microsoft_Windows_TCPIP_1374_0(Etw):
    pattern = Struct(
        "AddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.AddressLength),
        "RemotePort" / Int64ul,
        "LocalAddress" / Bytes(lambda this: this.AddressLength),
        "LocalPort" / Int16ul,
        "PartitionId" / Int64ul,
        "NumEntries" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1375, version=0)
class Microsoft_Windows_TCPIP_1375_0(Etw):
    pattern = Struct(
        "AddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.AddressLength),
        "RemotePort" / Int64ul,
        "LocalAddress" / Bytes(lambda this: this.AddressLength),
        "LocalPort" / Int16ul,
        "PartitionId" / Int64ul,
        "NumEntries" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1376, version=0)
class Microsoft_Windows_TCPIP_1376_0(Etw):
    pattern = Struct(
        "HighMemoryEvent" / Int32ul,
        "HighNonPagedPoolEvent" / Int32ul,
        "LowMemoryEvent" / Int32ul,
        "LowNonPagedPoolEvent" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1377, version=0)
class Microsoft_Windows_TCPIP_1377_0(Etw):
    pattern = Struct(
        "HighMemoryEvent" / Int32ul,
        "HighNonPagedPoolEvent" / Int32ul,
        "LowMemoryEvent" / Int32ul,
        "LowNonPagedPoolEvent" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1378, version=0)
class Microsoft_Windows_TCPIP_1378_0(Etw):
    pattern = Struct(
        "HighMemoryEvent" / Int32ul,
        "HighNonPagedPoolEvent" / Int32ul,
        "LowMemoryEvent" / Int32ul,
        "LowNonPagedPoolEvent" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1379, version=0)
class Microsoft_Windows_TCPIP_1379_0(Etw):
    pattern = Struct(
        "HighMemoryEvent" / Int32ul,
        "HighNonPagedPoolEvent" / Int32ul,
        "LowMemoryEvent" / Int32ul,
        "LowNonPagedPoolEvent" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1380, version=0)
class Microsoft_Windows_TCPIP_1380_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "LedbatEvent" / Int32ul,
        "Cwnd" / Int32ul,
        "SsThresh" / Int32ul,
        "SndWnd" / Int32ul,
        "BaseDelayMs" / Int16ul,
        "CurrentDelayMs" / Int16ul,
        "RemainingTimeMs" / Int32ul,
        "DelayBasedCwndFactorPercent" / Int32sl
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1381, version=0)
class Microsoft_Windows_TCPIP_1381_0(Etw):
    pattern = Struct(
        "Endpoint" / Int64ul,
        "NameResContext" / Int64ul,
        "DnsName" / WString,
        "InterfaceIndex" / Int32ul,
        "IpCount" / Int32ul,
        "IpAddr1Length" / Int32ul,
        "IpAddr1" / Bytes(lambda this: this.IpAddr1Length),
        "IpAddr2Length" / Int32ul,
        "IpAddr2" / Bytes(lambda this: this.IpAddr2Length),
        "IpAddr3Length" / Int32ul,
        "IpAddr3" / Bytes(lambda this: this.IpAddr3Length),
        "IpAddr4Length" / Int32ul,
        "IpAddr4" / Bytes(lambda this: this.IpAddr4Length),
        "IpAddr5Length" / Int32ul,
        "IpAddr5" / Bytes(lambda this: this.IpAddr5Length),
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1381, version=1)
class Microsoft_Windows_TCPIP_1381_1(Etw):
    pattern = Struct(
        "EndpointObj" / Int64ul,
        "IsConnectionObj" / Int32ul,
        "NameResContext" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1382, version=0)
class Microsoft_Windows_TCPIP_1382_0(Etw):
    pattern = Struct(
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "Tcb" / Int64ul,
        "NameResContext" / Int64ul,
        "DnsName" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1383, version=0)
class Microsoft_Windows_TCPIP_1383_0(Etw):
    pattern = Struct(
        "CompartmentId" / Int32ul,
        "DestinationAddressLength" / Int32ul,
        "DestinationAddress" / Bytes(lambda this: this.DestinationAddressLength),
        "PrDestinationPrefixLength" / Int32ul,
        "PrDestinationPrefixAddressLength" / Int32ul,
        "PrDestinationPrefix" / Bytes(lambda this: this.PrDestinationPrefixAddressLength),
        "PrNextHopAddressLength" / Int32ul,
        "PrNextHopAddress" / Bytes(lambda this: this.PrNextHopAddressLength),
        "PrInterfaceIndex" / Int32ul,
        "PrInterfaceMetric" / Int32ul,
        "PrRouteMetric" / Int32ul,
        "NonPrDestinationPrefixLength" / Int32ul,
        "NonPrDestinationPrefixAddressLength" / Int32ul,
        "NonPrDestinationPrefix" / Bytes(lambda this: this.NonPrDestinationPrefixAddressLength),
        "NonPrNextHopAddressLength" / Int32ul,
        "NonPrNextHopAddress" / Bytes(lambda this: this.NonPrNextHopAddressLength),
        "NonPrInterfaceIndex" / Int32ul,
        "NonPrInterfaceMetric" / Int32ul,
        "NonPrRouteMetric" / Int32ul,
        "PreferenceReason" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1384, version=0)
class Microsoft_Windows_TCPIP_1384_0(Etw):
    pattern = Struct(
        "CompartmentId" / Int32ul,
        "DestinationAddressLength" / Int32ul,
        "DestinationAddress" / Bytes(lambda this: this.DestinationAddressLength),
        "DestinationPrefixLength" / Int32ul,
        "DestinationPrefixAddressLength" / Int32ul,
        "DestinationPrefix" / Bytes(lambda this: this.DestinationPrefixAddressLength),
        "NextHopAddressLength" / Int32ul,
        "NextHopAddress" / Bytes(lambda this: this.NextHopAddressLength),
        "InterfaceIndex" / Int32ul,
        "RouteMetric" / Int32ul,
        "ConstrainInterfaceIndex" / Int32ul,
        "ConstrainScope" / Int32ul,
        "BlockReason" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1385, version=0)
class Microsoft_Windows_TCPIP_1385_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "SndUna" / Int32ul,
        "SndMax" / Int32ul,
        "SendAvailable" / Int32ul,
        "TailProbeSeq" / Int32ul,
        "TailProbeLast" / Int32ul,
        "ControlsToSend" / Int32ul,
        "ThFlags" / Int8ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1386, version=0)
class Microsoft_Windows_TCPIP_1386_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "TlpEvent" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1387, version=0)
class Microsoft_Windows_TCPIP_1387_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "RackEvent" / Int32ul,
        "RackMinRtt" / Int32ul,
        "RackReoWind" / Int32ul,
        "RackTimeSlotDeltaMin" / Int32ul,
        "SequenceNumber" / Int32ul,
        "Timestamp" / Int32ul,
        "RttSample" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1388, version=0)
class Microsoft_Windows_TCPIP_1388_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "OldState" / Int32ul,
        "NewState" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1389, version=0)
class Microsoft_Windows_TCPIP_1389_0(Etw):
    pattern = Struct(
        "Endpoint" / Int64ul,
        "Status" / Int32ul,
        "ProcessId" / Int32ul,
        "CompartmentId" / Int32ul,
        "AddressFamily" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1390, version=0)
class Microsoft_Windows_TCPIP_1390_0(Etw):
    pattern = Struct(
        "Endpoint" / Int64ul,
        "Status" / Int32ul,
        "ProcessId" / Int32ul,
        "CompartmentId" / Int32ul,
        "AddressFamily" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1391, version=0)
class Microsoft_Windows_TCPIP_1391_0(Etw):
    pattern = Struct(
        "Endpoint" / Int64ul,
        "Status" / Int32ul,
        "ProcessId" / Int32ul,
        "CompartmentId" / Int32ul,
        "AddressFamily" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1392, version=0)
class Microsoft_Windows_TCPIP_1392_0(Etw):
    pattern = Struct(
        "Endpoint" / Int64ul,
        "Status" / Int32ul,
        "ProcessId" / Int32ul,
        "CompartmentId" / Int32ul,
        "AddressFamily" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1393, version=0)
class Microsoft_Windows_TCPIP_1393_0(Etw):
    pattern = Struct(
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "Status" / Int32ul,
        "Endpoint" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1394, version=0)
class Microsoft_Windows_TCPIP_1394_0(Etw):
    pattern = Struct(
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "Status" / Int32ul,
        "Endpoint" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1395, version=0)
class Microsoft_Windows_TCPIP_1395_0(Etw):
    pattern = Struct(
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "Status" / Int32ul,
        "Endpoint" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1396, version=0)
class Microsoft_Windows_TCPIP_1396_0(Etw):
    pattern = Struct(
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "Status" / Int32ul,
        "Endpoint" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1397, version=0)
class Microsoft_Windows_TCPIP_1397_0(Etw):
    pattern = Struct(
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "Status" / Int32ul,
        "Endpoint" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1398, version=0)
class Microsoft_Windows_TCPIP_1398_0(Etw):
    pattern = Struct(
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "Status" / Int32ul,
        "Endpoint" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1399, version=0)
class Microsoft_Windows_TCPIP_1399_0(Etw):
    pattern = Struct(
        "Endpoint" / Int64ul,
        "EndpointAddressLength" / Int32ul,
        "EndpointAddress" / Bytes(lambda this: this.EndpointAddressLength),
        "SendAddressLength" / Int32ul,
        "SendAddress" / Bytes(lambda this: this.SendAddressLength),
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1400, version=0)
class Microsoft_Windows_TCPIP_1400_0(Etw):
    pattern = Struct(
        "Endpoint" / Int64ul,
        "EndpointAddressLength" / Int32ul,
        "EndpointAddress" / Bytes(lambda this: this.EndpointAddressLength),
        "SendAddressLength" / Int32ul,
        "SendAddress" / Bytes(lambda this: this.SendAddressLength),
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1401, version=0)
class Microsoft_Windows_TCPIP_1401_0(Etw):
    pattern = Struct(
        "Endpoint" / Int64ul,
        "EndpointAddressLength" / Int32ul,
        "EndpointAddress" / Bytes(lambda this: this.EndpointAddressLength),
        "SendAddressLength" / Int32ul,
        "SendAddress" / Bytes(lambda this: this.SendAddressLength),
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1403, version=0)
class Microsoft_Windows_TCPIP_1403_0(Etw):
    pattern = Struct(
        "InterfaceIndex" / Int32ul,
        "AddressFamily" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1404, version=0)
class Microsoft_Windows_TCPIP_1404_0(Etw):
    pattern = Struct(
        "InterfaceIndex" / Int32ul,
        "AddressFamily" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1405, version=0)
class Microsoft_Windows_TCPIP_1405_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1406, version=0)
class Microsoft_Windows_TCPIP_1406_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1407, version=0)
class Microsoft_Windows_TCPIP_1407_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1408, version=0)
class Microsoft_Windows_TCPIP_1408_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1409, version=0)
class Microsoft_Windows_TCPIP_1409_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1410, version=0)
class Microsoft_Windows_TCPIP_1410_0(Etw):
    pattern = Struct(
        "FailedQueueString" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1411, version=0)
class Microsoft_Windows_TCPIP_1411_0(Etw):
    pattern = Struct(
        "Endpoint" / Int64ul,
        "EndpointAddressLength" / Int32ul,
        "EndpointAddress" / Bytes(lambda this: this.EndpointAddressLength),
        "SendAddressLength" / Int32ul,
        "SendAddress" / Bytes(lambda this: this.SendAddressLength),
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1412, version=0)
class Microsoft_Windows_TCPIP_1412_0(Etw):
    pattern = Struct(
        "Endpoint" / Int64ul,
        "EndpointAddressLength" / Int32ul,
        "EndpointAddress" / Bytes(lambda this: this.EndpointAddressLength),
        "SendAddressLength" / Int32ul,
        "SendAddress" / Bytes(lambda this: this.SendAddressLength),
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1413, version=0)
class Microsoft_Windows_TCPIP_1413_0(Etw):
    pattern = Struct(
        "Endpoint" / Int64ul,
        "EndpointAddressLength" / Int32ul,
        "EndpointAddress" / Bytes(lambda this: this.EndpointAddressLength),
        "SendAddressLength" / Int32ul,
        "SendAddress" / Bytes(lambda this: this.SendAddressLength),
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1414, version=0)
class Microsoft_Windows_TCPIP_1414_0(Etw):
    pattern = Struct(
        "Endpoint" / Int64ul,
        "EndpointAddressLength" / Int32ul,
        "EndpointAddress" / Bytes(lambda this: this.EndpointAddressLength),
        "SendAddressLength" / Int32ul,
        "SendAddress" / Bytes(lambda this: this.SendAddressLength),
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1415, version=0)
class Microsoft_Windows_TCPIP_1415_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "SndUna" / Int32ul,
        "SackIsLostSeq" / Int32ul,
        "DupAckCount" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1416, version=0)
class Microsoft_Windows_TCPIP_1416_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "SynRcvdLimit" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1417, version=0)
class Microsoft_Windows_TCPIP_1417_0(Etw):
    pattern = Struct(
        "Location" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1418, version=0)
class Microsoft_Windows_TCPIP_1418_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "BytesToSend" / Int32ul,
        "SndNxt" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1419, version=0)
class Microsoft_Windows_TCPIP_1419_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "BytesToSend" / Int32ul,
        "SndNxt" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1420, version=0)
class Microsoft_Windows_TCPIP_1420_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "BytesToSend" / Int32ul,
        "SndNxt" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1421, version=0)
class Microsoft_Windows_TCPIP_1421_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "BytesToSend" / Int32ul,
        "SndNxt" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1422, version=0)
class Microsoft_Windows_TCPIP_1422_0(Etw):
    pattern = Struct(
        "IPTransportProtocol" / Int32ul,
        "PathDirection" / Int32ul,
        "IcmpType" / Int32ul,
        "IcmpCode" / Int32ul,
        "CompartmentId" / Int32ul,
        "SourceAddressLength" / Int32ul,
        "SourceAddress" / Bytes(lambda this: this.SourceAddressLength),
        "DestAddressLength" / Int32ul,
        "DestAddress" / Bytes(lambda this: this.DestAddressLength)
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1423, version=0)
class Microsoft_Windows_TCPIP_1423_0(Etw):
    pattern = Struct(
        "IPTransportProtocol" / Int32ul,
        "PathDirection" / Int32ul,
        "IcmpType" / Int32ul,
        "IcmpCode" / Int32ul,
        "DropReason" / Int32ul,
        "Status" / Int32ul,
        "CompartmentId" / Int32ul,
        "SourceAddressLength" / Int32ul,
        "SourceAddress" / Bytes(lambda this: this.SourceAddressLength),
        "DestAddressLength" / Int32ul,
        "DestAddress" / Bytes(lambda this: this.DestAddressLength)
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1424, version=0)
class Microsoft_Windows_TCPIP_1424_0(Etw):
    pattern = Struct(
        "IPTransportProtocol" / Int32ul,
        "PathDirection" / Int32ul,
        "IcmpType" / Int32ul,
        "IcmpCode" / Int32ul,
        "DropReason" / Int32ul,
        "Status" / Int32ul,
        "CompartmentId" / Int32ul,
        "SourceAddressLength" / Int32ul,
        "SourceAddress" / Bytes(lambda this: this.SourceAddressLength),
        "DestAddressLength" / Int32ul,
        "DestAddress" / Bytes(lambda this: this.DestAddressLength)
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1425, version=0)
class Microsoft_Windows_TCPIP_1425_0(Etw):
    pattern = Struct(
        "Component" / Int32ul,
        "Processor" / Int32ul,
        "CurrentState" / Int32ul,
        "ProcessorUsage" / Int32ul,
        "CurrentTick" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1426, version=0)
class Microsoft_Windows_TCPIP_1426_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "Injected" / WString,
        "NumBytes" / Int32ul,
        "SndNxt" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1427, version=0)
class Microsoft_Windows_TCPIP_1427_0(Etw):
    pattern = Struct(
        "CompartmentId" / Int32ul,
        "AddressFamily" / Int32ul,
        "Private" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1428, version=0)
class Microsoft_Windows_TCPIP_1428_0(Etw):
    pattern = Struct(
        "CompartmentId" / Int32ul,
        "AddressFamily" / Int32ul,
        "Private" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1429, version=0)
class Microsoft_Windows_TCPIP_1429_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "Cwnd" / Int32ul,
        "SndWnd" / Int32ul,
        "BytesAcked" / Int32ul,
        "SeqNo" / Int32ul,
        "InRecovery" / Int8ul,
        "TimeSinceLastLossMS" / Int64ul,
        "CubicCwnd" / Int64ul,
        "AimdCwnd" / Int32ul,
        "K" / Int64ul,
        "Wmax" / Int32ul,
        "LastWmax" / Int32ul,
        "MaxSndWnd" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1429, version=1)
class Microsoft_Windows_TCPIP_1429_1(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "Cwnd" / Int32ul,
        "SndWnd" / Int32ul,
        "BytesAcked" / Int32ul,
        "SeqNo" / Int32ul,
        "InRecovery" / Int8ul,
        "TimeSinceLastLossMS" / Int64ul,
        "CubicCwnd" / Int64ul,
        "AimdCwnd" / Int32ul,
        "K" / Int64ul,
        "Wmax" / Int32ul,
        "LastWmax" / Int32ul,
        "MaxSndWnd" / Int32ul,
        "IsLimitedSlowStart" / Int8ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1430, version=0)
class Microsoft_Windows_TCPIP_1430_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "Cwnd" / Int32ul,
        "SSThresh" / Int32ul,
        "DupAckCount" / Int32ul,
        "SeqNo" / Int32ul,
        "CwrMax" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1431, version=0)
class Microsoft_Windows_TCPIP_1431_0(Etw):
    pattern = Struct(
        "CompartmentId" / Int32ul,
        "AddressFamily" / Int32ul,
        "Private" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1432, version=0)
class Microsoft_Windows_TCPIP_1432_0(Etw):
    pattern = Struct(
        "IfIndex" / Int32ul,
        "CompartmentId" / Int32ul,
        "AddressFamily" / Int32ul,
        "NetworkCategory" / Int32ul,
        "DomainNetworkLocation" / Int32ul,
        "DomainType" / Int32ul,
        "NetworkSignature" / Guid
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1433, version=0)
class Microsoft_Windows_TCPIP_1433_0(Etw):
    pattern = Struct(
        "IfIndex" / Int32ul,
        "CompartmentId" / Int32ul,
        "AddressFamily" / Int32ul,
        "PhysicalMediumType" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1434, version=0)
class Microsoft_Windows_TCPIP_1434_0(Etw):
    pattern = Struct(
        "IfIndex" / Int32ul,
        "CompartmentId" / Int32ul,
        "AddressFamily" / Int32ul,
        "PhysicalMediumType" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1435, version=0)
class Microsoft_Windows_TCPIP_1435_0(Etw):
    pattern = Struct(
        "IfIndex" / Int32ul,
        "CompartmentId" / Int32ul,
        "AddressFamily" / Int32ul,
        "PhysicalMediumType" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1436, version=0)
class Microsoft_Windows_TCPIP_1436_0(Etw):
    pattern = Struct(
        "SubIfIndex" / Int32ul,
        "IfIndex" / Int32ul,
        "CompartmentId" / Int32ul,
        "AddressFamily" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1437, version=0)
class Microsoft_Windows_TCPIP_1437_0(Etw):
    pattern = Struct(
        "SubIfIndex" / Int32ul,
        "IfIndex" / Int32ul,
        "CompartmentId" / Int32ul,
        "AddressFamily" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1438, version=0)
class Microsoft_Windows_TCPIP_1438_0(Etw):
    pattern = Struct(
        "SubIfIndex" / Int32ul,
        "IfIndex" / Int32ul,
        "CompartmentId" / Int32ul,
        "AddressFamily" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1439, version=0)
class Microsoft_Windows_TCPIP_1439_0(Etw):
    pattern = Struct(
        "IfIndex" / Int32ul,
        "CompartmentId" / Int32ul,
        "AddressFamily" / Int32ul,
        "Reason" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1440, version=0)
class Microsoft_Windows_TCPIP_1440_0(Etw):
    pattern = Struct(
        "IfIndex" / Int32ul,
        "CompartmentId" / Int32ul,
        "AddressFamily" / Int32ul,
        "OldConnectivityStatus" / Int32ul,
        "NewConnectivityStatus" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1441, version=0)
class Microsoft_Windows_TCPIP_1441_0(Etw):
    pattern = Struct(
        "SourceAddressLength" / Int32ul,
        "SourceAddress" / Bytes(lambda this: this.SourceAddressLength),
        "IfIndex" / Int32ul,
        "CompartmentId" / Int32ul,
        "Protocol" / CString,
        "Reason" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1442, version=0)
class Microsoft_Windows_TCPIP_1442_0(Etw):
    pattern = Struct(
        "DestinationPrefixAddressLength" / Int32ul,
        "DestinationPrefix" / Bytes(lambda this: this.DestinationPrefixAddressLength),
        "NextHopAddressLength" / Int32ul,
        "NextHopAddress" / Bytes(lambda this: this.NextHopAddressLength),
        "DestinationPrefixLength" / Int32ul,
        "CompartmentId" / Int32ul,
        "IfIndex" / Int32ul,
        "NotifyFlags" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1443, version=0)
class Microsoft_Windows_TCPIP_1443_0(Etw):
    pattern = Struct(
        "IpAddrLength" / Int32ul,
        "IPAddress" / Bytes(lambda this: this.IpAddrLength),
        "DlAddrLength" / Int32ul,
        "DLAddress" / Bytes(lambda this: this.DlAddrLength),
        "IfIndex" / Int32ul,
        "CompartmentId" / Int32ul,
        "NeighborState" / Int32ul,
        "Reason" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1444, version=0)
class Microsoft_Windows_TCPIP_1444_0(Etw):
    pattern = Struct(
        "SourceAddressLength" / Int32ul,
        "SourceAddress" / Bytes(lambda this: this.SourceAddressLength),
        "IfIndex" / Int32ul,
        "CompartmentId" / Int32ul,
        "OldDadState" / Int32ul,
        "NewDadState" / Int32ul,
        "Reason" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1445, version=0)
class Microsoft_Windows_TCPIP_1445_0(Etw):
    pattern = Struct(
        "DestinationPrefixAddressLength" / Int32ul,
        "DestinationPrefix" / Bytes(lambda this: this.DestinationPrefixAddressLength),
        "NextHopAddressLength" / Int32ul,
        "NextHopAddress" / Bytes(lambda this: this.NextHopAddressLength),
        "DestinationPrefixLength" / Int32ul,
        "CompartmentId" / Int32ul,
        "IfIndex" / Int32ul,
        "OldState" / Int32ul,
        "NewState" / Int32ul,
        "OldProbeCount" / Int32ul,
        "NewProbeCount" / Int32ul,
        "OldUnreachablePaths" / Int32ul,
        "NewUnreachablePaths" / Int32ul,
        "OldMovedPaths" / Int32ul,
        "NewMovedPaths" / Int32ul,
        "TotalPaths" / Int32ul,
        "OldStateChangeTick" / Int32ul,
        "NewStateChangeTick" / Int32ul,
        "DgdNeedsReset" / Int32ul,
        "Reason" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1446, version=0)
class Microsoft_Windows_TCPIP_1446_0(Etw):
    pattern = Struct(
        "AddressLength" / Int32ul,
        "Address" / Bytes(lambda this: this.AddressLength),
        "IfIndex" / Int32ul,
        "CompartmentId" / Int32ul,
        "SkipLocal" / Int32ul,
        "SkipOnLink" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1447, version=0)
class Microsoft_Windows_TCPIP_1447_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "Cwnd" / Int32ul,
        "SndWnd" / Int32ul,
        "BytesAvailable" / Int32ul,
        "BytesOutstanding" / Int32ul,
        "ChunkSize" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1448, version=0)
class Microsoft_Windows_TCPIP_1448_0(Etw):
    pattern = Struct(
        "Fallback" / Int64ul,
        "Feature" / Int32ul,
        "Reason" / Int32ul,
        "Confidence" / Int32sl,
        "Successes" / Int32ul,
        "Failures" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1449, version=0)
class Microsoft_Windows_TCPIP_1449_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1450, version=0)
class Microsoft_Windows_TCPIP_1450_0(Etw):
    pattern = Struct(
        "IfIndex" / Int32ul,
        "CompartmentId" / Int32ul,
        "AddressFamily" / Int32ul,
        "Reason" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1451, version=0)
class Microsoft_Windows_TCPIP_1451_0(Etw):
    pattern = Struct(
        "Event" / Int32ul,
        "Interface" / Int32ul,
        "CompartmentId" / Int32ul,
        "RouterAddrLength" / Int32ul,
        "RouterAddress" / Bytes(lambda this: this.RouterAddrLength),
        "DnsAddrLength" / Int32ul,
        "DNSServerAddress" / Bytes(lambda this: this.DnsAddrLength),
        "DNSSuffix" / CString,
        "Lifetime" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1452, version=0)
class Microsoft_Windows_TCPIP_1452_0(Etw):
    pattern = Struct(
        "Interface" / Int32ul,
        "Compartment" / Int32ul,
        "DestinationPrefixAddressLength" / Int32ul,
        "DestinationPrefix" / Bytes(lambda this: this.DestinationPrefixAddressLength),
        "DestinationPrefixLength" / Int32ul,
        "NextHopAddressLength" / Int32ul,
        "NextHopAddress" / Bytes(lambda this: this.NextHopAddressLength),
        "Metric" / Int32ul,
        "State" / Int32ul,
        "Origin" / Int32ul,
        "Age" / Int64ul,
        "ValidLifetime" / Int64ul,
        "PreferredLifetime" / Int64ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1453, version=0)
class Microsoft_Windows_TCPIP_1453_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "Cwnd" / Int32ul,
        "SSThresh" / Int32ul,
        "SndUna" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1454, version=0)
class Microsoft_Windows_TCPIP_1454_0(Etw):
    pattern = Struct(
        "Owner" / Int64ul,
        "InspectHandle" / Int64ul,
        "InspectType" / Int32ul,
        "InspectAction" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1455, version=0)
class Microsoft_Windows_TCPIP_1455_0(Etw):
    pattern = Struct(
        "Owner" / Int64ul,
        "InspectHandle" / Int64ul,
        "InspectType" / Int32ul,
        "InspectPort" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1456, version=0)
class Microsoft_Windows_TCPIP_1456_0(Etw):
    pattern = Struct(
        "Fallback" / Int64ul,
        "Feature" / Int32ul,
        "Failed" / Int32ul,
        "Succeeded" / Int32ul,
        "InProbe" / Int32ul,
        "PathsProbed" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1457, version=0)
class Microsoft_Windows_TCPIP_1457_0(Etw):
    pattern = Struct(
        "Fallback" / Int64ul,
        "Feature" / Int32ul,
        "Failed" / Int32ul,
        "Succeeded" / Int32ul,
        "InProbe" / Int32ul,
        "PathsProbed" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1458, version=0)
class Microsoft_Windows_TCPIP_1458_0(Etw):
    pattern = Struct(
        "Fallback" / Int64ul,
        "Feature" / Int32ul,
        "Failed" / Int32ul,
        "Succeeded" / Int32ul,
        "InProbe" / Int32ul,
        "PathsProbed" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1459, version=0)
class Microsoft_Windows_TCPIP_1459_0(Etw):
    pattern = Struct(
        "Fallback" / Int64ul,
        "Feature" / Int32ul,
        "Failed" / Int32ul,
        "Succeeded" / Int32ul,
        "InProbe" / Int32ul,
        "PathsProbed" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1460, version=0)
class Microsoft_Windows_TCPIP_1460_0(Etw):
    pattern = Struct(
        "Fallback" / Int64ul,
        "Feature" / Int32ul,
        "Failed" / Int32ul,
        "Succeeded" / Int32ul,
        "InProbe" / Int32ul,
        "PathsProbed" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1461, version=0)
class Microsoft_Windows_TCPIP_1461_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "FastopenState" / Int32ul,
        "DataBytesIn" / Int64ul,
        "ShutdownStatus" / Int32ul,
        "ProbeStatus" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1462, version=0)
class Microsoft_Windows_TCPIP_1462_0(Etw):
    pattern = Struct(
        "CompartmentId" / Int32ul,
        "IfIndex" / Int32ul,
        "Feature" / Int32ul,
        "ConnectivityStatus" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1463, version=0)
class Microsoft_Windows_TCPIP_1463_0(Etw):
    pattern = Struct(
        "Feature" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1464, version=0)
class Microsoft_Windows_TCPIP_1464_0(Etw):
    pattern = Struct(
        "BaseEndpoint" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1465, version=0)
class Microsoft_Windows_TCPIP_1465_0(Etw):
    pattern = Struct(
        "Compartment" / Int32ul,
        "DestinationAddrLength" / Int32ul,
        "DestinationAddress" / Bytes(lambda this: this.DestinationAddrLength),
        "ConstrainSourceAddrLength" / Int32ul,
        "ConstrainSourceAddress" / Bytes(lambda this: this.ConstrainSourceAddrLength),
        "ConstrainInterfaceIndex" / Int32ul,
        "ConstraintFlags" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1466, version=0)
class Microsoft_Windows_TCPIP_1466_0(Etw):
    pattern = Struct(
        "AddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.AddressLength),
        "RemoteAddress" / Bytes(lambda this: this.AddressLength),
        "PartitionId" / Int64ul,
        "NumEntries" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1467, version=0)
class Microsoft_Windows_TCPIP_1467_0(Etw):
    pattern = Struct(
        "AddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.AddressLength),
        "RemoteAddress" / Bytes(lambda this: this.AddressLength),
        "PartitionId" / Int64ul,
        "NumEntries" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1468, version=0)
class Microsoft_Windows_TCPIP_1468_0(Etw):
    pattern = Struct(
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "Status" / Int32ul,
        "ProcessId" / Int32ul,
        "Compartment" / Int32ul,
        "Tcb" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1469, version=0)
class Microsoft_Windows_TCPIP_1469_0(Etw):
    pattern = Struct(
        "Feature" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1470, version=0)
class Microsoft_Windows_TCPIP_1470_0(Etw):
    pattern = Struct(
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1471, version=0)
class Microsoft_Windows_TCPIP_1471_0(Etw):
    pattern = Struct(
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "Status" / Int32ul,
        "Endpoint" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1472, version=0)
class Microsoft_Windows_TCPIP_1472_0(Etw):
    pattern = Struct(
        "AcquireType" / Int32ul,
        "Port" / Int16ul,
        "AddressFamily" / Int32ul,
        "Interface" / Int32ul,
        "Compartment" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1473, version=0)
class Microsoft_Windows_TCPIP_1473_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "Location" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1474, version=0)
class Microsoft_Windows_TCPIP_1474_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1475, version=0)
class Microsoft_Windows_TCPIP_1475_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "State" / Int16ul,
        "Cwnd" / Int32ul,
        "SSThresh" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1476, version=0)
class Microsoft_Windows_TCPIP_1476_0(Etw):
    pattern = Struct(
        "Nbl" / Int64ul,
        "Interface" / Int32ul,
        "Compartment" / Int32ul,
        "AddressLength" / Int32ul,
        "DestinationAddress" / Bytes(lambda this: this.AddressLength),
        "SourceAddress" / Bytes(lambda this: this.AddressLength),
        "IPTransportProtocol" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1477, version=0)
class Microsoft_Windows_TCPIP_1477_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "DataBytesOut" / Int64ul,
        "DataBytesIn" / Int64ul,
        "DataSegmentsOut" / Int64ul,
        "DataSegmentsIn" / Int64ul,
        "SegmentsOut" / Int64ul,
        "SegmentsIn" / Int64ul,
        "NonRecovDa" / Int32ul,
        "NonRecovDaEpisodes" / Int32ul,
        "DupAcksIn" / Int32ul,
        "BytesRetrans" / Int32ul,
        "Timeouts" / Int32ul,
        "SpuriousRtoDetections" / Int32ul,
        "FastRetran" / Int32ul,
        "MaxSsthresh" / Int32ul,
        "MaxSsCwnd" / Int32ul,
        "MaxCaCwnd" / Int32ul,
        "SndLimTransRwin" / Int32ul,
        "SndLimTimeRwin" / Int32ul,
        "SndLimBytesRwin" / Int64ul,
        "SndLimTransCwnd" / Int32ul,
        "SndLimTimeCwnd" / Int32ul,
        "SndLimBytesCwnd" / Int64ul,
        "SndLimTransSnd" / Int32ul,
        "SndLimTimeRSnd" / Int32ul,
        "SndLimBytesRSnd" / Int64ul,
        "ConnectionTimeMs" / Int64ul,
        "TimestampsEnabled" / Int32ul,
        "RttUs" / Int32ul,
        "MinRttUs" / Int32ul,
        "MaxRttUs" / Int32ul,
        "SynRetrans" / Int32ul,
        "CongestionAlgorithm" / Int32ul,
        "State" / Int32ul,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "CWnd" / Int32ul,
        "SsThresh" / Int32ul,
        "RcvWnd" / Int32ul,
        "RcvBuf" / Int32ul,
        "SndWnd" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1478, version=0)
class Microsoft_Windows_TCPIP_1478_0(Etw):
    pattern = Struct(
        "PathDirection" / Int32ul,
        "AddressFamily" / Int32ul,
        "Interface" / Int32ul,
        "PacketCount" / Int32ul,
        "Reason" / Int32ul,
        "Data" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1479, version=0)
class Microsoft_Windows_TCPIP_1479_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "IPTransportProtocol" / Int32ul,
        "AddressFamily" / Int32ul,
        "LocalSockAddrLength" / Int32ul,
        "LocalSockAddr" / Bytes(lambda this: this.LocalSockAddrLength),
        "RemoteSockAddrLength" / Int32ul,
        "RemoteSockAddr" / Bytes(lambda this: this.RemoteSockAddrLength),
        "Reason" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1480, version=0)
class Microsoft_Windows_TCPIP_1480_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "LocalSockAddrLength" / Int32ul,
        "LocalSockAddr" / Bytes(lambda this: this.LocalSockAddrLength),
        "RemoteSockAddrLength" / Int32ul,
        "RemoteSockAddr" / Bytes(lambda this: this.RemoteSockAddrLength),
        "TcpState" / Int32ul,
        "ProcessId" / Int32ul,
        "Hour" / Int16ul,
        "Minute" / Int16ul,
        "Second" / Int16ul,
        "Reason" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1481, version=0)
class Microsoft_Windows_TCPIP_1481_0(Etw):
    pattern = Struct(
        "Tcb" / Int64ul,
        "SackIsLostSeq" / Int32ul,
        "SackInFlight" / Int32ul,
        "SackBytes" / Int32ul,
        "SackIsLost" / Int32ul,
        "SsThresh" / Int32ul,
        "HeadSeq" / Int32ul,
        "AckedData" / Int32ul,
        "BytesInFlight" / Int32ul,
        "BytesToSend" / Int64sl,
        "PrrDelivered" / Int32ul,
        "PrrOut" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1482, version=0)
class Microsoft_Windows_TCPIP_1482_0(Etw):
    pattern = Struct(
        "Endpoint" / Int64ul,
        "SegmentSize" / Int32ul,
        "MessageLength" / Int64ul,
        "HwDatagrams" / Int32ul,
        "HwSegments" / Int32ul,
        "SwSegments" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1483, version=0)
class Microsoft_Windows_TCPIP_1483_0(Etw):
    pattern = Struct(
        "Endpoint" / Int64ul,
        "FailureReason" / Int32ul,
        "SegmentSize" / Int32ul,
        "LocalSockAddrLength" / Int32ul,
        "LocalSockAddr" / Bytes(lambda this: this.LocalSockAddrLength),
        "RemoteSockAddrLength" / Int32ul,
        "RemoteSockAddr" / Bytes(lambda this: this.RemoteSockAddrLength)
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1484, version=0)
class Microsoft_Windows_TCPIP_1484_0(Etw):
    pattern = Struct(
        "IfIndex" / Int32ul,
        "AddressFamily" / Int32ul,
        "FailureCode" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1485, version=0)
class Microsoft_Windows_TCPIP_1485_0(Etw):
    pattern = Struct(
        "IfIndex" / Int32ul,
        "AddressFamily" / Int32ul,
        "OID" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1486, version=0)
class Microsoft_Windows_TCPIP_1486_0(Etw):
    pattern = Struct(
        "IfIndex" / Int32ul,
        "AddressFamily" / Int32ul,
        "NdisStatus" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1487, version=0)
class Microsoft_Windows_TCPIP_1487_0(Etw):
    pattern = Struct(
        "SocketOptionLevel" / Int32ul,
        "SocketOptionValue" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1488, version=0)
class Microsoft_Windows_TCPIP_1488_0(Etw):
    pattern = Struct(
        "SocketIoctl" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1489, version=0)
class Microsoft_Windows_TCPIP_1489_0(Etw):
    pattern = Struct(
        "RequestType" / Int32ul,
        "IPv4Address" / Int32ul,
        "IPv4SourceAddress" / Int32ul,
        "IpAddrLength" / Int32ul,
        "IpSourceAddrLength" / Int32ul,
        "IPv6Address" / Bytes(lambda this: this.IpAddrLength),
        "IPv6SourceAddress" / Bytes(lambda this: this.IpSourceAddrLength),
        "FailureReason" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1490, version=0)
class Microsoft_Windows_TCPIP_1490_0(Etw):
    pattern = Struct(
        "RequestType" / Int32ul,
        "IPv4Address" / Int32ul,
        "IPv4SourceAddress" / Int32ul,
        "IpAddrLength" / Int32ul,
        "IpSourceAddrLength" / Int32ul,
        "IPv6Address" / Bytes(lambda this: this.IpAddrLength),
        "IPv6SourceAddress" / Bytes(lambda this: this.IpSourceAddrLength)
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1491, version=0)
class Microsoft_Windows_TCPIP_1491_0(Etw):
    pattern = Struct(
        "MessageType" / Int32ul,
        "IfIndex" / Int32ul,
        "IPv4Address" / Int32ul,
        "IpAddrLength" / Int32ul,
        "IPv6Address" / Bytes(lambda this: this.IpAddrLength),
        "Data" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1492, version=0)
class Microsoft_Windows_TCPIP_1492_0(Etw):
    pattern = Struct(
        "MessageType" / Int32ul,
        "IfIndex" / Int32ul,
        "IPv4Address" / Int32ul,
        "IpAddrLength" / Int32ul,
        "IPv6Address" / Bytes(lambda this: this.IpAddrLength),
        "Data" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1493, version=0)
class Microsoft_Windows_TCPIP_1493_0(Etw):
    pattern = Struct(
        "Ce" / Int32ul,
        "Ect0" / Int32ul,
        "Ect1" / Int32ul,
        "NotEct" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1494, version=0)
class Microsoft_Windows_TCPIP_1494_0(Etw):
    pattern = Struct(
        "InterfaceIndex" / Int32ul,
        "AddressFamily" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1495, version=0)
class Microsoft_Windows_TCPIP_1495_0(Etw):
    pattern = Struct(
        "IfIndex" / Int32ul,
        "AddressFamily" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1496, version=0)
class Microsoft_Windows_TCPIP_1496_0(Etw):
    pattern = Struct(
        "FragmentContextDirection" / Int32ul,
        "IfIndex" / Int32ul,
        "AddressFamily" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1497, version=0)
class Microsoft_Windows_TCPIP_1497_0(Etw):
    pattern = Struct(
        "GroupChangeType" / Int32ul,
        "IfIndex" / Int32ul,
        "IPv4Address" / Int32ul,
        "IpAddrLength" / Int32ul,
        "IPv6Address" / Bytes(lambda this: this.IpAddrLength),
        "Data" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1498, version=0)
class Microsoft_Windows_TCPIP_1498_0(Etw):
    pattern = Struct(
        "IfIndex" / Int32ul,
        "AddressFamily" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1499, version=0)
class Microsoft_Windows_TCPIP_1499_0(Etw):
    pattern = Struct(
        "IfIndex" / Int32ul,
        "IPv4Address" / Int32ul,
        "IpAddrLength" / Int32ul,
        "IPv6Address" / Bytes(lambda this: this.IpAddrLength)
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1500, version=0)
class Microsoft_Windows_TCPIP_1500_0(Etw):
    pattern = Struct(
        "IfIndex" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1501, version=0)
class Microsoft_Windows_TCPIP_1501_0(Etw):
    pattern = Struct(
        "IfIndex" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1502, version=0)
class Microsoft_Windows_TCPIP_1502_0(Etw):
    pattern = Struct(
        "IfIndex" / Int32ul,
        "Field" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1503, version=0)
class Microsoft_Windows_TCPIP_1503_0(Etw):
    pattern = Struct(
        "Release" / Int32ul,
        "IfIndex" / Int32ul,
        "Subtask" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1504, version=0)
class Microsoft_Windows_TCPIP_1504_0(Etw):
    pattern = Struct(
        "IfIndex" / Int32ul,
        "IPv4DestinationAddress" / Int32ul,
        "IPv4NextHop" / Int32ul,
        "IpAddrLength" / Int32ul,
        "IPv6DestinationAddress" / Bytes(lambda this: this.IpAddrLength),
        "IPv6NextHop" / Bytes(lambda this: this.IpAddrLength)
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1505, version=0)
class Microsoft_Windows_TCPIP_1505_0(Etw):
    pattern = Struct(
        "IfIndex" / Int32ul,
        "IpAddrLength" / Int32ul,
        "IPv6Address" / Bytes(lambda this: this.IpAddrLength)
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1506, version=0)
class Microsoft_Windows_TCPIP_1506_0(Etw):
    pattern = Struct(
        "Release" / Int32ul,
        "AddressFamily" / Int32ul,
        "IfIndex" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1507, version=0)
class Microsoft_Windows_TCPIP_1507_0(Etw):
    pattern = Struct(
        "IfIndex" / Int32ul,
        "ReassemblyId" / Int32ul,
        "IPv4SourceAddress" / Int32ul,
        "IPv4DestinationAddress" / Int32ul,
        "IpAddrLength" / Int32ul,
        "IPv6SourceAddress" / Bytes(lambda this: this.IpAddrLength),
        "IPv6DestinationAddress" / Bytes(lambda this: this.IpAddrLength)
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1508, version=0)
class Microsoft_Windows_TCPIP_1508_0(Etw):
    pattern = Struct(
        "Reason" / Int32ul,
        "SocketLevel" / Int32ul,
        "SocketOption" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1509, version=0)
class Microsoft_Windows_TCPIP_1509_0(Etw):
    pattern = Struct(
        "Reason" / Int32ul,
        "Option" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1510, version=0)
class Microsoft_Windows_TCPIP_1510_0(Etw):
    pattern = Struct(
        "Reason" / Int32ul,
        "Option" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1511, version=0)
class Microsoft_Windows_TCPIP_1511_0(Etw):
    pattern = Struct(
        "Reason" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1512, version=0)
class Microsoft_Windows_TCPIP_1512_0(Etw):
    pattern = Struct(
        "Reason" / Int32ul
    )


@declare(guid=guid("2f07e2ee-15db-40f1-90ef-9d7ba282188a"), event_id=1513, version=0)
class Microsoft_Windows_TCPIP_1513_0(Etw):
    pattern = Struct(
        "Reason" / Int32ul
    )

