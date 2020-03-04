# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Time-Service-PTP-Provider
GUID : cffb980e-327c-5b87-19c6-62c4c3be2290
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("cffb980e-327c-5b87-19c6-62c4c3be2290"), event_id=512, version=0)
class Microsoft_Windows_Time_Service_PTP_Provider_512_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Address" / WString,
        "MasterClockId" / WString,
        "MasterPortNum" / Int32ul,
        "DomainNumber" / Int32ul,
        "UTCValid" / Int32ul,
        "CurrentUTCOffset" / Int32ul,
        "Flags" / WString,
        "GrandMasterClockId" / WString,
        "StepsRemovedFromGrandMaster" / Int32ul,
        "TimeSourceCode" / WString,
        "LogAnnounceInterval" / Int32sl,
        "ActiveMasterCount" / Int32ul,
        "TickCount" / Int64ul
    )


@declare(guid=guid("cffb980e-327c-5b87-19c6-62c4c3be2290"), event_id=513, version=0)
class Microsoft_Windows_Time_Service_PTP_Provider_513_0(Etw):
    pattern = Struct(
        "BestMasterName" / WString,
        "MasterAddress" / WString,
        "MasterClockId" / WString,
        "MasterPortNum" / Int32ul,
        "DomainNumber" / Int32ul,
        "UTCValid" / Int32ul,
        "CurrentUTCOffset" / Int32ul,
        "Flags" / WString,
        "GrandMasterClockId" / WString,
        "StepsRemovedFromGrandMaster" / Int32ul,
        "TimeSourceCode" / WString,
        "LogAnnounceInterval" / Int32sl,
        "TickCount" / Int64ul
    )


@declare(guid=guid("cffb980e-327c-5b87-19c6-62c4c3be2290"), event_id=514, version=0)
class Microsoft_Windows_Time_Service_PTP_Provider_514_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Address" / WString,
        "AnnounceTimeoutMsec" / Int32ul,
        "MasterClockId" / WString,
        "MasterPortNum" / Int32ul,
        "LogAnnounceInterval" / Int32sl,
        "ActiveMasterCount" / Int32ul,
        "TickCount" / Int64ul
    )


@declare(guid=guid("cffb980e-327c-5b87-19c6-62c4c3be2290"), event_id=515, version=0)
class Microsoft_Windows_Time_Service_PTP_Provider_515_0(Etw):
    pattern = Struct(
        "AllowedMastersList" / WString,
        "AnnounceIntervalMsec" / Int32ul,
        "DelayPollIntervalMsec" / Int32ul,
        "IfTstmp" / Int32ul,
        "BestMasterName" / WString,
        "BMAddress" / WString,
        "BMClockId" / WString,
        "BMPortNum" / Int32ul,
        "BMLastTimeSampleTickCount" / Int64ul,
        "ActiveMasterCount" / Int32ul,
        "MulticastRxEnabled" / Int32ul,
        "TickCount" / Int64ul
    )

