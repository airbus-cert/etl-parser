# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Shsvcs
GUID : 059c3e04-5535-4929-85e1-93030e78f47b
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("059c3e04-5535-4929-85e1-93030e78f47b"), event_id=11505, version=0)
class Microsoft_Windows_Shsvcs_11505_0(Etw):
    pattern = Struct(
        "ContainerIdentifier" / WString,
        "DeviceIdentifier" / WString
    )


@declare(guid=guid("059c3e04-5535-4929-85e1-93030e78f47b"), event_id=11507, version=0)
class Microsoft_Windows_Shsvcs_11507_0(Etw):
    pattern = Struct(
        "ContainerIdentifier" / WString,
        "DeviceIdentifier" / WString
    )


@declare(guid=guid("059c3e04-5535-4929-85e1-93030e78f47b"), event_id=11509, version=0)
class Microsoft_Windows_Shsvcs_11509_0(Etw):
    pattern = Struct(
        "ContainerIdentifier" / WString,
        "DeviceIdentifier" / WString
    )


@declare(guid=guid("059c3e04-5535-4929-85e1-93030e78f47b"), event_id=11511, version=0)
class Microsoft_Windows_Shsvcs_11511_0(Etw):
    pattern = Struct(
        "ContainerIdentifier" / WString,
        "DeviceIdentifier" / WString
    )


@declare(guid=guid("059c3e04-5535-4929-85e1-93030e78f47b"), event_id=11513, version=0)
class Microsoft_Windows_Shsvcs_11513_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "DesiredAccess" / Int32ul
    )

