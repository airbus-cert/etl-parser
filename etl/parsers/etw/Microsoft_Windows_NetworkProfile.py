# -*- coding: utf-8 -*-
"""
Microsoft-Windows-NetworkProfile
GUID : fbcfac3f-8459-419f-8e48-1f0b49cdb85e
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("fbcfac3f-8459-419f-8e48-1f0b49cdb85e"), event_id=4001, version=0)
class Microsoft_Windows_NetworkProfile_4001_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "CurrentOrNextState" / Int8ul
    )


@declare(guid=guid("fbcfac3f-8459-419f-8e48-1f0b49cdb85e"), event_id=4002, version=0)
class Microsoft_Windows_NetworkProfile_4002_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "CurrentOrNextState" / Int8ul
    )


@declare(guid=guid("fbcfac3f-8459-419f-8e48-1f0b49cdb85e"), event_id=4003, version=0)
class Microsoft_Windows_NetworkProfile_4003_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "CurrentOrNextState" / Int8ul
    )


@declare(guid=guid("fbcfac3f-8459-419f-8e48-1f0b49cdb85e"), event_id=4004, version=0)
class Microsoft_Windows_NetworkProfile_4004_0(Etw):
    pattern = Struct(
        "NewInternetConnectionProfile" / Int8ul,
        "ConnectionCostChanged" / Int8ul,
        "DomainConnectivityLevelChanged" / Int8ul,
        "NetworkConnectivityLevelChanged" / Int8ul,
        "HostNameChanged" / Int8ul,
        "WwanRegistrationStateChanged" / Int8ul,
        "TetheringOperationalStateChanged" / Int8ul,
        "TetheringClientCountChanged" / Int8ul
    )


@declare(guid=guid("fbcfac3f-8459-419f-8e48-1f0b49cdb85e"), event_id=10000, version=0)
class Microsoft_Windows_NetworkProfile_10000_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Description" / WString,
        "Guid" / Guid,
        "Type" / Int32ul,
        "State" / Int32ul,
        "Category" / Int32ul
    )


@declare(guid=guid("fbcfac3f-8459-419f-8e48-1f0b49cdb85e"), event_id=10001, version=0)
class Microsoft_Windows_NetworkProfile_10001_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Description" / WString,
        "Guid" / Guid,
        "Type" / Int32ul,
        "State" / Int32ul,
        "Category" / Int32ul
    )


@declare(guid=guid("fbcfac3f-8459-419f-8e48-1f0b49cdb85e"), event_id=10002, version=0)
class Microsoft_Windows_NetworkProfile_10002_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Description" / WString,
        "Guid" / Guid,
        "Type" / Int32ul,
        "State" / Int32ul,
        "Category" / Int32ul
    )


@declare(guid=guid("fbcfac3f-8459-419f-8e48-1f0b49cdb85e"), event_id=10003, version=0)
class Microsoft_Windows_NetworkProfile_10003_0(Etw):
    pattern = Struct(
        "NetworkProfileEventState" / Int32ul,
        "Guid" / Guid
    )


@declare(guid=guid("fbcfac3f-8459-419f-8e48-1f0b49cdb85e"), event_id=10004, version=0)
class Microsoft_Windows_NetworkProfile_10004_0(Etw):
    pattern = Struct(
        "NetworkProfileEventState" / Int32ul,
        "Guid" / Guid
    )


@declare(guid=guid("fbcfac3f-8459-419f-8e48-1f0b49cdb85e"), event_id=10005, version=0)
class Microsoft_Windows_NetworkProfile_10005_0(Etw):
    pattern = Struct(
        "NetworkProfileEventState" / Int32ul,
        "Guid" / Guid
    )


@declare(guid=guid("fbcfac3f-8459-419f-8e48-1f0b49cdb85e"), event_id=10006, version=0)
class Microsoft_Windows_NetworkProfile_10006_0(Etw):
    pattern = Struct(
        "NetworkProfileEventState" / Int32ul,
        "Guid" / Guid
    )


@declare(guid=guid("fbcfac3f-8459-419f-8e48-1f0b49cdb85e"), event_id=10007, version=0)
class Microsoft_Windows_NetworkProfile_10007_0(Etw):
    pattern = Struct(
        "NetworkProfileEventState" / Int32ul,
        "Guid" / Guid
    )


@declare(guid=guid("fbcfac3f-8459-419f-8e48-1f0b49cdb85e"), event_id=10008, version=0)
class Microsoft_Windows_NetworkProfile_10008_0(Etw):
    pattern = Struct(
        "NetworkProfileEventState" / Int32ul,
        "Guid" / Guid
    )


@declare(guid=guid("fbcfac3f-8459-419f-8e48-1f0b49cdb85e"), event_id=20001, version=0)
class Microsoft_Windows_NetworkProfile_20001_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32sl,
        "Context" / Int32ul
    )


@declare(guid=guid("fbcfac3f-8459-419f-8e48-1f0b49cdb85e"), event_id=20002, version=0)
class Microsoft_Windows_NetworkProfile_20002_0(Etw):
    pattern = Struct(
        "ProfileGuid" / Guid,
        "InterfaceGuid" / Guid,
        "Category" / Int32ul,
        "ErrorCodev4" / Int32sl,
        "ErrorCodev6" / Int32sl,
        "Context" / Int32ul
    )


@declare(guid=guid("fbcfac3f-8459-419f-8e48-1f0b49cdb85e"), event_id=20003, version=0)
class Microsoft_Windows_NetworkProfile_20003_0(Etw):
    pattern = Struct(
        "InternetPresent" / Int8ul,
        "WnfStatusCode" / Int32ul
    )


@declare(guid=guid("fbcfac3f-8459-419f-8e48-1f0b49cdb85e"), event_id=20004, version=0)
class Microsoft_Windows_NetworkProfile_20004_0(Etw):
    pattern = Struct(
        "FreeNetworkPresent" / Int8ul,
        "WnfStatusCode" / Int32ul
    )

