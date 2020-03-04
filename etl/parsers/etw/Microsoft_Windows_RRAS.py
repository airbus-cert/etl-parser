# -*- coding: utf-8 -*-
"""
Microsoft-Windows-RRAS
GUID : 24989972-0967-4e21-a926-93854033638e
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=1000, version=0)
class Microsoft_Windows_RRAS_1000_0(Etw):
    pattern = Struct(
        "DebugString" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=1001, version=0)
class Microsoft_Windows_RRAS_1001_0(Etw):
    pattern = Struct(
        "DebugString" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=1002, version=0)
class Microsoft_Windows_RRAS_1002_0(Etw):
    pattern = Struct(
        "DebugString" / WString,
        "RoutingDomainID" / Guid,
        "RRASUserName" / WString,
        "PortNo" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=1003, version=0)
class Microsoft_Windows_RRAS_1003_0(Etw):
    pattern = Struct(
        "DebugString" / WString,
        "RoutingDomainID" / Guid,
        "RRASUserName" / WString,
        "PortNo" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=2000, version=0)
class Microsoft_Windows_RRAS_2000_0(Etw):
    pattern = Struct(
        "DebugString" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=2001, version=0)
class Microsoft_Windows_RRAS_2001_0(Etw):
    pattern = Struct(
        "DebugString" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=2002, version=0)
class Microsoft_Windows_RRAS_2002_0(Etw):
    pattern = Struct(
        "DebugString" / WString,
        "RoutingDomainID" / Guid,
        "RRASUserName" / WString,
        "PortNo" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=2003, version=0)
class Microsoft_Windows_RRAS_2003_0(Etw):
    pattern = Struct(
        "DebugString" / WString,
        "RoutingDomainID" / Guid,
        "RRASUserName" / WString,
        "PortNo" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=3000, version=0)
class Microsoft_Windows_RRAS_3000_0(Etw):
    pattern = Struct(
        "DebugString" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=3001, version=0)
class Microsoft_Windows_RRAS_3001_0(Etw):
    pattern = Struct(
        "DebugString" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=3002, version=0)
class Microsoft_Windows_RRAS_3002_0(Etw):
    pattern = Struct(
        "DebugString" / WString,
        "RoutingDomainID" / Guid,
        "RRASUserName" / WString,
        "PortNo" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=3003, version=0)
class Microsoft_Windows_RRAS_3003_0(Etw):
    pattern = Struct(
        "DebugString" / WString,
        "RoutingDomainID" / Guid,
        "RRASUserName" / WString,
        "PortNo" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=4000, version=0)
class Microsoft_Windows_RRAS_4000_0(Etw):
    pattern = Struct(
        "DebugString" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=4001, version=0)
class Microsoft_Windows_RRAS_4001_0(Etw):
    pattern = Struct(
        "DebugString" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=4002, version=0)
class Microsoft_Windows_RRAS_4002_0(Etw):
    pattern = Struct(
        "DebugString" / WString,
        "RoutingDomainID" / Guid,
        "RRASUserName" / WString,
        "PortNo" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=4003, version=0)
class Microsoft_Windows_RRAS_4003_0(Etw):
    pattern = Struct(
        "DebugString" / WString,
        "RoutingDomainID" / Guid,
        "RRASUserName" / WString,
        "PortNo" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=5000, version=0)
class Microsoft_Windows_RRAS_5000_0(Etw):
    pattern = Struct(
        "DebugString" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=5001, version=0)
class Microsoft_Windows_RRAS_5001_0(Etw):
    pattern = Struct(
        "DebugString" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=5002, version=0)
class Microsoft_Windows_RRAS_5002_0(Etw):
    pattern = Struct(
        "DebugString" / WString,
        "RoutingDomainID" / Guid,
        "RRASUserName" / WString,
        "PortNo" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=5003, version=0)
class Microsoft_Windows_RRAS_5003_0(Etw):
    pattern = Struct(
        "DebugString" / WString,
        "RoutingDomainID" / Guid,
        "RRASUserName" / WString,
        "PortNo" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=6000, version=0)
class Microsoft_Windows_RRAS_6000_0(Etw):
    pattern = Struct(
        "DebugString" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=6001, version=0)
class Microsoft_Windows_RRAS_6001_0(Etw):
    pattern = Struct(
        "DebugString" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=6002, version=0)
class Microsoft_Windows_RRAS_6002_0(Etw):
    pattern = Struct(
        "DebugString" / WString,
        "RoutingDomainID" / Guid,
        "RRASUserName" / WString,
        "PortNo" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=6003, version=0)
class Microsoft_Windows_RRAS_6003_0(Etw):
    pattern = Struct(
        "DebugString" / WString,
        "RoutingDomainID" / Guid,
        "RRASUserName" / WString,
        "PortNo" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=6004, version=0)
class Microsoft_Windows_RRAS_6004_0(Etw):
    pattern = Struct(
        "DebugString" / WString,
        "BufferSize" / Int32ul,
        "Buffer" / Bytes(lambda this: this.BufferSize)
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=7000, version=0)
class Microsoft_Windows_RRAS_7000_0(Etw):
    pattern = Struct(
        "DebugString" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=7001, version=0)
class Microsoft_Windows_RRAS_7001_0(Etw):
    pattern = Struct(
        "DebugString" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=7002, version=0)
class Microsoft_Windows_RRAS_7002_0(Etw):
    pattern = Struct(
        "DebugString" / WString,
        "RoutingDomainID" / Guid,
        "RRASUserName" / WString,
        "PortNo" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=7003, version=0)
class Microsoft_Windows_RRAS_7003_0(Etw):
    pattern = Struct(
        "DebugString" / WString,
        "RoutingDomainID" / Guid,
        "RRASUserName" / WString,
        "PortNo" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=8000, version=0)
class Microsoft_Windows_RRAS_8000_0(Etw):
    pattern = Struct(
        "DebugString" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=8001, version=0)
class Microsoft_Windows_RRAS_8001_0(Etw):
    pattern = Struct(
        "DebugString" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=8002, version=0)
class Microsoft_Windows_RRAS_8002_0(Etw):
    pattern = Struct(
        "DebugString" / WString,
        "RoutingDomainID" / Guid,
        "RRASUserName" / WString,
        "PortNo" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=8003, version=0)
class Microsoft_Windows_RRAS_8003_0(Etw):
    pattern = Struct(
        "DebugString" / WString,
        "RoutingDomainID" / Guid,
        "RRASUserName" / WString,
        "PortNo" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=9000, version=0)
class Microsoft_Windows_RRAS_9000_0(Etw):
    pattern = Struct(
        "DebugString" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=9001, version=0)
class Microsoft_Windows_RRAS_9001_0(Etw):
    pattern = Struct(
        "DebugString" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=9002, version=0)
class Microsoft_Windows_RRAS_9002_0(Etw):
    pattern = Struct(
        "DebugString" / WString,
        "RoutingDomainID" / Guid,
        "RRASUserName" / WString,
        "PortNo" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=9003, version=0)
class Microsoft_Windows_RRAS_9003_0(Etw):
    pattern = Struct(
        "DebugString" / WString,
        "RoutingDomainID" / Guid,
        "RRASUserName" / WString,
        "PortNo" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=10000, version=0)
class Microsoft_Windows_RRAS_10000_0(Etw):
    pattern = Struct(
        "DebugString" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=10001, version=0)
class Microsoft_Windows_RRAS_10001_0(Etw):
    pattern = Struct(
        "DebugString" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=10002, version=0)
class Microsoft_Windows_RRAS_10002_0(Etw):
    pattern = Struct(
        "DebugString" / WString,
        "RoutingDomainID" / Guid,
        "RRASUserName" / WString,
        "PortNo" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=10003, version=0)
class Microsoft_Windows_RRAS_10003_0(Etw):
    pattern = Struct(
        "DebugString" / WString,
        "RoutingDomainID" / Guid,
        "RRASUserName" / WString,
        "PortNo" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=11000, version=0)
class Microsoft_Windows_RRAS_11000_0(Etw):
    pattern = Struct(
        "DebugString" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=11001, version=0)
class Microsoft_Windows_RRAS_11001_0(Etw):
    pattern = Struct(
        "DebugString" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=11002, version=0)
class Microsoft_Windows_RRAS_11002_0(Etw):
    pattern = Struct(
        "DebugString" / WString,
        "RoutingDomainID" / Guid,
        "RRASUserName" / WString,
        "PortNo" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=11003, version=0)
class Microsoft_Windows_RRAS_11003_0(Etw):
    pattern = Struct(
        "DebugString" / WString,
        "RoutingDomainID" / Guid,
        "RRASUserName" / WString,
        "PortNo" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=12000, version=0)
class Microsoft_Windows_RRAS_12000_0(Etw):
    pattern = Struct(
        "DebugString" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=12001, version=0)
class Microsoft_Windows_RRAS_12001_0(Etw):
    pattern = Struct(
        "DebugString" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=12002, version=0)
class Microsoft_Windows_RRAS_12002_0(Etw):
    pattern = Struct(
        "DebugString" / WString,
        "RoutingDomainID" / Guid,
        "RRASUserName" / WString,
        "PortNo" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=12003, version=0)
class Microsoft_Windows_RRAS_12003_0(Etw):
    pattern = Struct(
        "DebugString" / WString,
        "RoutingDomainID" / Guid,
        "RRASUserName" / WString,
        "PortNo" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=13000, version=0)
class Microsoft_Windows_RRAS_13000_0(Etw):
    pattern = Struct(
        "DebugString" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=13001, version=0)
class Microsoft_Windows_RRAS_13001_0(Etw):
    pattern = Struct(
        "DebugString" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=13002, version=0)
class Microsoft_Windows_RRAS_13002_0(Etw):
    pattern = Struct(
        "DebugString" / WString,
        "RoutingDomainID" / Guid,
        "RRASUserName" / WString,
        "PortNo" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=13003, version=0)
class Microsoft_Windows_RRAS_13003_0(Etw):
    pattern = Struct(
        "DebugString" / WString,
        "RoutingDomainID" / Guid,
        "RRASUserName" / WString,
        "PortNo" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=14000, version=0)
class Microsoft_Windows_RRAS_14000_0(Etw):
    pattern = Struct(
        "DebugString" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=14001, version=0)
class Microsoft_Windows_RRAS_14001_0(Etw):
    pattern = Struct(
        "DebugString" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=14002, version=0)
class Microsoft_Windows_RRAS_14002_0(Etw):
    pattern = Struct(
        "DebugString" / WString,
        "RoutingDomainID" / Guid,
        "RRASUserName" / WString,
        "PortNo" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=14003, version=0)
class Microsoft_Windows_RRAS_14003_0(Etw):
    pattern = Struct(
        "DebugString" / WString,
        "RoutingDomainID" / Guid,
        "RRASUserName" / WString,
        "PortNo" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=15000, version=0)
class Microsoft_Windows_RRAS_15000_0(Etw):
    pattern = Struct(
        "DebugString" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=15001, version=0)
class Microsoft_Windows_RRAS_15001_0(Etw):
    pattern = Struct(
        "DebugString" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=15002, version=0)
class Microsoft_Windows_RRAS_15002_0(Etw):
    pattern = Struct(
        "DebugString" / WString,
        "RoutingDomainID" / Guid,
        "RRASUserName" / WString,
        "PortNo" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=15003, version=0)
class Microsoft_Windows_RRAS_15003_0(Etw):
    pattern = Struct(
        "DebugString" / WString,
        "RoutingDomainID" / Guid,
        "RRASUserName" / WString,
        "PortNo" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=16000, version=0)
class Microsoft_Windows_RRAS_16000_0(Etw):
    pattern = Struct(
        "DebugString" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=16001, version=0)
class Microsoft_Windows_RRAS_16001_0(Etw):
    pattern = Struct(
        "DebugString" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=16002, version=0)
class Microsoft_Windows_RRAS_16002_0(Etw):
    pattern = Struct(
        "DebugString" / WString,
        "RoutingDomainID" / Guid,
        "RRASUserName" / WString,
        "PortNo" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=16003, version=0)
class Microsoft_Windows_RRAS_16003_0(Etw):
    pattern = Struct(
        "DebugString" / WString,
        "RoutingDomainID" / Guid,
        "RRASUserName" / WString,
        "PortNo" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=16004, version=0)
class Microsoft_Windows_RRAS_16004_0(Etw):
    pattern = Struct(
        "DebugString" / WString,
        "BufferSize" / Int32ul,
        "Buffer" / Bytes(lambda this: this.BufferSize)
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=17000, version=0)
class Microsoft_Windows_RRAS_17000_0(Etw):
    pattern = Struct(
        "DebugString" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=17001, version=0)
class Microsoft_Windows_RRAS_17001_0(Etw):
    pattern = Struct(
        "DebugString" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=17002, version=0)
class Microsoft_Windows_RRAS_17002_0(Etw):
    pattern = Struct(
        "DebugString" / WString,
        "RoutingDomainID" / Guid,
        "RRASUserName" / WString,
        "PortNo" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=17003, version=0)
class Microsoft_Windows_RRAS_17003_0(Etw):
    pattern = Struct(
        "DebugString" / WString,
        "RoutingDomainID" / Guid,
        "RRASUserName" / WString,
        "PortNo" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=18000, version=0)
class Microsoft_Windows_RRAS_18000_0(Etw):
    pattern = Struct(
        "DebugString" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=18001, version=0)
class Microsoft_Windows_RRAS_18001_0(Etw):
    pattern = Struct(
        "DebugString" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=18002, version=0)
class Microsoft_Windows_RRAS_18002_0(Etw):
    pattern = Struct(
        "DebugString" / WString,
        "RoutingDomainID" / Guid,
        "RRASUserName" / WString,
        "PortNo" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=18003, version=0)
class Microsoft_Windows_RRAS_18003_0(Etw):
    pattern = Struct(
        "DebugString" / WString,
        "RoutingDomainID" / Guid,
        "RRASUserName" / WString,
        "PortNo" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=18004, version=0)
class Microsoft_Windows_RRAS_18004_0(Etw):
    pattern = Struct(
        "DebugString" / WString,
        "BufferSize" / Int32ul,
        "Buffer" / Bytes(lambda this: this.BufferSize)
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=19000, version=0)
class Microsoft_Windows_RRAS_19000_0(Etw):
    pattern = Struct(
        "DebugString" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=19001, version=0)
class Microsoft_Windows_RRAS_19001_0(Etw):
    pattern = Struct(
        "DebugString" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=19002, version=0)
class Microsoft_Windows_RRAS_19002_0(Etw):
    pattern = Struct(
        "DebugString" / WString,
        "RoutingDomainID" / Guid,
        "RRASUserName" / WString,
        "PortNo" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=19003, version=0)
class Microsoft_Windows_RRAS_19003_0(Etw):
    pattern = Struct(
        "DebugString" / WString,
        "RoutingDomainID" / Guid,
        "RRASUserName" / WString,
        "PortNo" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=20000, version=0)
class Microsoft_Windows_RRAS_20000_0(Etw):
    pattern = Struct(
        "DebugString" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=20001, version=0)
class Microsoft_Windows_RRAS_20001_0(Etw):
    pattern = Struct(
        "DebugString" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=20002, version=0)
class Microsoft_Windows_RRAS_20002_0(Etw):
    pattern = Struct(
        "DebugString" / WString,
        "RoutingDomainID" / Guid,
        "RRASUserName" / WString,
        "PortNo" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=20003, version=0)
class Microsoft_Windows_RRAS_20003_0(Etw):
    pattern = Struct(
        "DebugString" / WString,
        "RoutingDomainID" / Guid,
        "RRASUserName" / WString,
        "PortNo" / WString
    )


@declare(guid=guid("24989972-0967-4e21-a926-93854033638e"), event_id=20004, version=0)
class Microsoft_Windows_RRAS_20004_0(Etw):
    pattern = Struct(
        "DebugString" / WString,
        "BufferSize" / Int32ul,
        "Buffer" / Bytes(lambda this: this.BufferSize)
    )

