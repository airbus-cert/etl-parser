# -*- coding: utf-8 -*-
"""
Microsoft-Windows-RPC-FirewallManager
GUID : f997cd11-0fc9-4ab4-acba-bc742a4c0dd3
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("f997cd11-0fc9-4ab4-acba-bc742a4c0dd3"), event_id=2, version=0)
class Microsoft_Windows_RPC_FirewallManager_2_0(Etw):
    pattern = Struct(
        "FilterKey" / WString,
        "ErrorStatus" / WString
    )


@declare(guid=guid("f997cd11-0fc9-4ab4-acba-bc742a4c0dd3"), event_id=3, version=0)
class Microsoft_Windows_RPC_FirewallManager_3_0(Etw):
    pattern = Struct(
        "FilterKey" / WString,
        "ErrorStatus" / WString
    )


@declare(guid=guid("f997cd11-0fc9-4ab4-acba-bc742a4c0dd3"), event_id=4, version=0)
class Microsoft_Windows_RPC_FirewallManager_4_0(Etw):
    pattern = Struct(
        "FilterKey" / WString,
        "ErrorStatus" / WString
    )

