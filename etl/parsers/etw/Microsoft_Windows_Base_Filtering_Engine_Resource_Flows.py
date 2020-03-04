# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Base-Filtering-Engine-Resource-Flows
GUID : 92765247-03a9-4ae3-a575-b42264616e78
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("92765247-03a9-4ae3-a575-b42264616e78"), event_id=2002, version=0)
class Microsoft_Windows_Base_Filtering_Engine_Resource_Flows_2002_0(Etw):
    pattern = Struct(
        "ConnectionUsedId" / Int64ul,
        "Protocol" / Int8ul,
        "RemotePort" / Int16ul,
        "LocalPort" / Int16ul,
        "StartTime" / Int64ul
    )


@declare(guid=guid("92765247-03a9-4ae3-a575-b42264616e78"), event_id=2003, version=0)
class Microsoft_Windows_Base_Filtering_Engine_Resource_Flows_2003_0(Etw):
    pattern = Struct(
        "ConnectionUsedId" / Int64ul,
        "Protocol" / Int8ul,
        "RemotePort" / Int16ul,
        "LocalPort" / Int16ul,
        "StartTime" / Int64ul,
        "CloseTime" / Int64ul
    )


@declare(guid=guid("92765247-03a9-4ae3-a575-b42264616e78"), event_id=2004, version=0)
class Microsoft_Windows_Base_Filtering_Engine_Resource_Flows_2004_0(Etw):
    pattern = Struct(
        "ConnectionUsedId" / Int64ul,
        "Protocol" / Int8ul,
        "RemoteIPAddress" / Int32ul,
        "LocalIPAddress" / Int32ul,
        "RemotePort" / Int16ul,
        "LocalPort" / Int16ul,
        "StartTime" / Int64ul
    )


@declare(guid=guid("92765247-03a9-4ae3-a575-b42264616e78"), event_id=2005, version=0)
class Microsoft_Windows_Base_Filtering_Engine_Resource_Flows_2005_0(Etw):
    pattern = Struct(
        "ConnectionUsedId" / Int64ul,
        "Protocol" / Int8ul,
        "RemoteIPAddress" / Int32ul,
        "LocalIPAddress" / Int32ul,
        "RemotePort" / Int16ul,
        "LocalPort" / Int16ul,
        "StartTime" / Int64ul,
        "CloseTime" / Int64ul
    )

