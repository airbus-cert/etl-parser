# -*- coding: utf-8 -*-
"""
Microsoft-Windows-CoreSystem-NetProvision-JoinProviderOnline
GUID : 3629dd4d-d6f1-4302-a623-0768b51501c7
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("3629dd4d-d6f1-4302-a623-0768b51501c7"), event_id=4098, version=0)
class Microsoft_Windows_CoreSystem_NetProvision_JoinProviderOnline_4098_0(Etw):
    pattern = Struct(
        "DomainName" / WString,
        "ComputerName" / WString
    )


@declare(guid=guid("3629dd4d-d6f1-4302-a623-0768b51501c7"), event_id=4099, version=0)
class Microsoft_Windows_CoreSystem_NetProvision_JoinProviderOnline_4099_0(Etw):
    pattern = Struct(
        "DomainName" / WString,
        "ComputerName" / WString,
        "NetStatusCode" / Int32ul
    )

