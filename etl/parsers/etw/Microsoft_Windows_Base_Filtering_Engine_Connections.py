# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Base-Filtering-Engine-Connections
GUID : 121d3da8-baf1-4dcb-929f-2d4c9a47f7ab
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("121d3da8-baf1-4dcb-929f-2d4c9a47f7ab"), event_id=2000, version=0)
class Microsoft_Windows_Base_Filtering_Engine_Connections_2000_0(Etw):
    pattern = Struct(
        "ConnectionId" / Int64ul,
        "MachineAuthenticationMethod" / Int32ul,
        "RemoteMachineAccount" / WString,
        "UserAuthenticationMethod" / Int32ul,
        "RemoteUserAcount" / WString,
        "RemoteIPAddress" / WString,
        "LocalIPAddress" / WString,
        "TechnologyProviderKey" / Guid,
        "IPsecTrafficMode" / Int32ul,
        "DHGroup" / Int32ul,
        "StartTime" / SystemTime
    )


@declare(guid=guid("121d3da8-baf1-4dcb-929f-2d4c9a47f7ab"), event_id=2001, version=0)
class Microsoft_Windows_Base_Filtering_Engine_Connections_2001_0(Etw):
    pattern = Struct(
        "ConnectionId" / Int64ul,
        "MachineAuthenticationMethod" / Int32ul,
        "RemoteMachineAccount" / WString,
        "UserAuthenticationMethod" / Int32ul,
        "RemoteUserAcount" / WString,
        "RemoteIPAddress" / WString,
        "LocalIPAddress" / WString,
        "TechnologyProviderKey" / Guid,
        "IPsecTrafficMode" / Int32ul,
        "BytesTransferredInbound" / Int64ul,
        "BytesTransferredOutbound" / Int64ul,
        "BytesTransferredTotal" / Int64ul,
        "StartTime" / SystemTime,
        "CloseTime" / SystemTime
    )

