# -*- coding: utf-8 -*-
"""
Microsoft-Windows-SetupPlatform
GUID : 530fb9b9-c515-4472-9313-fb346f9255e3
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("530fb9b9-c515-4472-9313-fb346f9255e3"), event_id=1001, version=0)
class Microsoft_Windows_SetupPlatform_1001_0(Etw):
    pattern = Struct(
        "Operation" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("530fb9b9-c515-4472-9313-fb346f9255e3"), event_id=1002, version=0)
class Microsoft_Windows_SetupPlatform_1002_0(Etw):
    pattern = Struct(
        "Operation" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("530fb9b9-c515-4472-9313-fb346f9255e3"), event_id=1003, version=0)
class Microsoft_Windows_SetupPlatform_1003_0(Etw):
    pattern = Struct(
        "OfflineWinDir" / WString,
        "MachineSpecific" / Int32ul
    )


@declare(guid=guid("530fb9b9-c515-4472-9313-fb346f9255e3"), event_id=1004, version=0)
class Microsoft_Windows_SetupPlatform_1004_0(Etw):
    pattern = Struct(
        "OfflineWinDir" / WString,
        "MachineSpecific" / Int32ul
    )


@declare(guid=guid("530fb9b9-c515-4472-9313-fb346f9255e3"), event_id=2005, version=0)
class Microsoft_Windows_SetupPlatform_2005_0(Etw):
    pattern = Struct(
        "Installationchoice" / Int32ul,
        "HostOSMajorversion" / Int32ul,
        "HostOSMinorversion" / Int32ul,
        "HostOSBuildnumber" / Int32ul,
        "HostOSServicepackmajornumber" / Int32ul,
        "HostOSServicepackminornumber" / Int32ul
    )

