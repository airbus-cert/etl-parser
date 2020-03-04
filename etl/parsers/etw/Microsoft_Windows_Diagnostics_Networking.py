# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Diagnostics-Networking
GUID : 36c23e18-0e66-11d9-bbeb-505054503030
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("36c23e18-0e66-11d9-bbeb-505054503030"), event_id=1000, version=0)
class Microsoft_Windows_Diagnostics_Networking_1000_0(Etw):
    pattern = Struct(
        "HelperClassName" / WString,
        "NumberOfAttributes" / Int32ul,
        "HelperClassAttributes" / WString
    )


@declare(guid=guid("36c23e18-0e66-11d9-bbeb-505054503030"), event_id=2000, version=0)
class Microsoft_Windows_Diagnostics_Networking_2000_0(Etw):
    pattern = Struct(
        "ResultHR" / Int32ul
    )


@declare(guid=guid("36c23e18-0e66-11d9-bbeb-505054503030"), event_id=2100, version=0)
class Microsoft_Windows_Diagnostics_Networking_2100_0(Etw):
    pattern = Struct(
        "ResultHR" / Int32ul
    )


@declare(guid=guid("36c23e18-0e66-11d9-bbeb-505054503030"), event_id=2200, version=0)
class Microsoft_Windows_Diagnostics_Networking_2200_0(Etw):
    pattern = Struct(
        "ResultHR" / Int32ul
    )


@declare(guid=guid("36c23e18-0e66-11d9-bbeb-505054503030"), event_id=2300, version=0)
class Microsoft_Windows_Diagnostics_Networking_2300_0(Etw):
    pattern = Struct(
        "ResultHR" / Int32ul
    )


@declare(guid=guid("36c23e18-0e66-11d9-bbeb-505054503030"), event_id=2400, version=0)
class Microsoft_Windows_Diagnostics_Networking_2400_0(Etw):
    pattern = Struct(
        "ResultHR" / Int32ul
    )


@declare(guid=guid("36c23e18-0e66-11d9-bbeb-505054503030"), event_id=2500, version=0)
class Microsoft_Windows_Diagnostics_Networking_2500_0(Etw):
    pattern = Struct(
        "ResultHR" / Int32ul
    )


@declare(guid=guid("36c23e18-0e66-11d9-bbeb-505054503030"), event_id=3000, version=0)
class Microsoft_Windows_Diagnostics_Networking_3000_0(Etw):
    pattern = Struct(
        "ResultHR" / Int32ul
    )


@declare(guid=guid("36c23e18-0e66-11d9-bbeb-505054503030"), event_id=3100, version=0)
class Microsoft_Windows_Diagnostics_Networking_3100_0(Etw):
    pattern = Struct(
        "ResultHR" / Int32ul
    )


@declare(guid=guid("36c23e18-0e66-11d9-bbeb-505054503030"), event_id=4000, version=0)
class Microsoft_Windows_Diagnostics_Networking_4000_0(Etw):
    pattern = Struct(
        "RepairOption" / WString,
        "RepairGUID" / Guid,
        "SecondsRequired" / Int32ul,
        "SIDTypeRequired" / Int32ul
    )


@declare(guid=guid("36c23e18-0e66-11d9-bbeb-505054503030"), event_id=4000, version=1)
class Microsoft_Windows_Diagnostics_Networking_4000_1(Etw):
    pattern = Struct(
        "RootCause" / WString,
        "RootCauseGUID" / Guid,
        "RepairOption" / WString,
        "RepairGUID" / Guid,
        "SecondsRequired" / Int32ul,
        "SIDTypeRequired" / Int32ul,
        "HelperClassName" / WString,
        "InterfaceDesc" / WString,
        "InterfaceGUID" / Guid
    )


@declare(guid=guid("36c23e18-0e66-11d9-bbeb-505054503030"), event_id=4200, version=0)
class Microsoft_Windows_Diagnostics_Networking_4200_0(Etw):
    pattern = Struct(
        "ResultHR" / Int32ul
    )


@declare(guid=guid("36c23e18-0e66-11d9-bbeb-505054503030"), event_id=5000, version=0)
class Microsoft_Windows_Diagnostics_Networking_5000_0(Etw):
    pattern = Struct(
        "RepairOption" / WString,
        "RepairGUID" / Guid,
        "SecondsRequired" / Int32ul,
        "SIDTypeRequired" / Int32ul,
        "HelperClassName" / WString
    )


@declare(guid=guid("36c23e18-0e66-11d9-bbeb-505054503030"), event_id=5000, version=1)
class Microsoft_Windows_Diagnostics_Networking_5000_1(Etw):
    pattern = Struct(
        "RootCause" / WString,
        "RootCauseGUID" / Guid,
        "RepairOption" / WString,
        "RepairGUID" / Guid,
        "SecondsRequired" / Int32ul,
        "SIDTypeRequired" / Int32ul,
        "HelperClassName" / WString,
        "InterfaceDesc" / WString,
        "InterfaceGUID" / Guid
    )


@declare(guid=guid("36c23e18-0e66-11d9-bbeb-505054503030"), event_id=5100, version=0)
class Microsoft_Windows_Diagnostics_Networking_5100_0(Etw):
    pattern = Struct(
        "RepairOption" / WString,
        "RepairGUID" / Guid,
        "SecondsRequired" / Int32ul,
        "SIDTypeRequired" / Int32ul,
        "HelperClassName" / WString
    )


@declare(guid=guid("36c23e18-0e66-11d9-bbeb-505054503030"), event_id=5100, version=1)
class Microsoft_Windows_Diagnostics_Networking_5100_1(Etw):
    pattern = Struct(
        "RootCause" / WString,
        "RootCauseGUID" / Guid,
        "RepairOption" / WString,
        "RepairGUID" / Guid,
        "SecondsRequired" / Int32ul,
        "SIDTypeRequired" / Int32ul,
        "HelperClassName" / WString,
        "InterfaceDesc" / WString,
        "InterfaceGUID" / Guid
    )


@declare(guid=guid("36c23e18-0e66-11d9-bbeb-505054503030"), event_id=5200, version=0)
class Microsoft_Windows_Diagnostics_Networking_5200_0(Etw):
    pattern = Struct(
        "RepairOption" / WString,
        "RepairGUID" / Guid,
        "SecondsRequired" / Int32ul,
        "SIDTypeRequired" / Int32ul
    )


@declare(guid=guid("36c23e18-0e66-11d9-bbeb-505054503030"), event_id=5200, version=1)
class Microsoft_Windows_Diagnostics_Networking_5200_1(Etw):
    pattern = Struct(
        "RootCause" / WString,
        "RootCauseGUID" / Guid,
        "RepairOption" / WString,
        "RepairGUID" / Guid,
        "SecondsRequired" / Int32ul,
        "SIDTypeRequired" / Int32ul,
        "HelperClassName" / WString,
        "InterfaceDesc" / WString,
        "InterfaceGUID" / Guid
    )


@declare(guid=guid("36c23e18-0e66-11d9-bbeb-505054503030"), event_id=5300, version=0)
class Microsoft_Windows_Diagnostics_Networking_5300_0(Etw):
    pattern = Struct(
        "ResultHR" / Int32ul
    )


@declare(guid=guid("36c23e18-0e66-11d9-bbeb-505054503030"), event_id=6000, version=0)
class Microsoft_Windows_Diagnostics_Networking_6000_0(Etw):
    pattern = Struct(
        "HelperClassName" / WString,
        "EventDescription" / WString,
        "EventVerbosity" / Int16ul
    )


@declare(guid=guid("36c23e18-0e66-11d9-bbeb-505054503030"), event_id=6100, version=0)
class Microsoft_Windows_Diagnostics_Networking_6100_0(Etw):
    pattern = Struct(
        "HelperClassName" / WString,
        "EventDescription" / WString,
        "EventVerbosity" / Int16ul
    )


@declare(guid=guid("36c23e18-0e66-11d9-bbeb-505054503030"), event_id=6200, version=0)
class Microsoft_Windows_Diagnostics_Networking_6200_0(Etw):
    pattern = Struct(
        "HelperClassName" / WString,
        "EventDescription" / WString,
        "EventVerbosity" / Int16ul
    )


@declare(guid=guid("36c23e18-0e66-11d9-bbeb-505054503030"), event_id=7000, version=0)
class Microsoft_Windows_Diagnostics_Networking_7000_0(Etw):
    pattern = Struct(
        "DebugMessage" / WString
    )


@declare(guid=guid("36c23e18-0e66-11d9-bbeb-505054503030"), event_id=7010, version=0)
class Microsoft_Windows_Diagnostics_Networking_7010_0(Etw):
    pattern = Struct(
        "DebugMessage" / WString
    )


@declare(guid=guid("36c23e18-0e66-11d9-bbeb-505054503030"), event_id=7020, version=0)
class Microsoft_Windows_Diagnostics_Networking_7020_0(Etw):
    pattern = Struct(
        "DebugMessage" / WString
    )


@declare(guid=guid("36c23e18-0e66-11d9-bbeb-505054503030"), event_id=7030, version=0)
class Microsoft_Windows_Diagnostics_Networking_7030_0(Etw):
    pattern = Struct(
        "DebugMessage" / WString
    )


@declare(guid=guid("36c23e18-0e66-11d9-bbeb-505054503030"), event_id=7040, version=0)
class Microsoft_Windows_Diagnostics_Networking_7040_0(Etw):
    pattern = Struct(
        "DebugMessage" / WString
    )


@declare(guid=guid("36c23e18-0e66-11d9-bbeb-505054503030"), event_id=7050, version=0)
class Microsoft_Windows_Diagnostics_Networking_7050_0(Etw):
    pattern = Struct(
        "DebugMessage" / WString
    )


@declare(guid=guid("36c23e18-0e66-11d9-bbeb-505054503030"), event_id=7100, version=0)
class Microsoft_Windows_Diagnostics_Networking_7100_0(Etw):
    pattern = Struct(
        "DebugMessage" / WString
    )


@declare(guid=guid("36c23e18-0e66-11d9-bbeb-505054503030"), event_id=8103, version=0)
class Microsoft_Windows_Diagnostics_Networking_8103_0(Etw):
    pattern = Struct(
        "HelperClassName" / WString
    )


@declare(guid=guid("36c23e18-0e66-11d9-bbeb-505054503030"), event_id=8104, version=0)
class Microsoft_Windows_Diagnostics_Networking_8104_0(Etw):
    pattern = Struct(
        "HelperClassName" / WString
    )


@declare(guid=guid("36c23e18-0e66-11d9-bbeb-505054503030"), event_id=8107, version=0)
class Microsoft_Windows_Diagnostics_Networking_8107_0(Etw):
    pattern = Struct(
        "HelperClassName" / WString
    )


@declare(guid=guid("36c23e18-0e66-11d9-bbeb-505054503030"), event_id=8108, version=0)
class Microsoft_Windows_Diagnostics_Networking_8108_0(Etw):
    pattern = Struct(
        "HelperClassName" / WString
    )

