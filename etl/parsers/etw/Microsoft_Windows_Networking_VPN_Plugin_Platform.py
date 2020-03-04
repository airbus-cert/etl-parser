# -*- coding: utf-8 -*-
"""
Microsoft-Windows Networking VPN Plugin Platform
GUID : e5fc4a0f-7198-492f-9b0f-88fdcbfded48
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("e5fc4a0f-7198-492f-9b0f-88fdcbfded48"), event_id=2001, version=0)
class Microsoft_Windows_Networking_VPN_Plugin_Platform_2001_0(Etw):
    pattern = Struct(
        "Plugin" / Sid,
        "Profile" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("e5fc4a0f-7198-492f-9b0f-88fdcbfded48"), event_id=2002, version=0)
class Microsoft_Windows_Networking_VPN_Plugin_Platform_2002_0(Etw):
    pattern = Struct(
        "Plugin" / Sid,
        "InitialProfile" / WString,
        "InitialEventType" / Int32ul
    )


@declare(guid=guid("e5fc4a0f-7198-492f-9b0f-88fdcbfded48"), event_id=2003, version=0)
class Microsoft_Windows_Networking_VPN_Plugin_Platform_2003_0(Etw):
    pattern = Struct(
        "Plugin" / Sid,
        "InitialProfile" / WString,
        "InitialEventType" / Int32ul,
        "NumPacketsSent" / Int32ul,
        "NumPacketsReceived" / Int32ul,
        "LastError" / Int32ul
    )


@declare(guid=guid("e5fc4a0f-7198-492f-9b0f-88fdcbfded48"), event_id=2004, version=0)
class Microsoft_Windows_Networking_VPN_Plugin_Platform_2004_0(Etw):
    pattern = Struct(
        "Profile" / WString,
        "Message" / WString
    )


@declare(guid=guid("e5fc4a0f-7198-492f-9b0f-88fdcbfded48"), event_id=2005, version=0)
class Microsoft_Windows_Networking_VPN_Plugin_Platform_2005_0(Etw):
    pattern = Struct(
        "profileName" / WString,
        "NetworkName" / WString
    )


@declare(guid=guid("e5fc4a0f-7198-492f-9b0f-88fdcbfded48"), event_id=2006, version=0)
class Microsoft_Windows_Networking_VPN_Plugin_Platform_2006_0(Etw):
    pattern = Struct(
        "string" / WString
    )


@declare(guid=guid("e5fc4a0f-7198-492f-9b0f-88fdcbfded48"), event_id=2007, version=0)
class Microsoft_Windows_Networking_VPN_Plugin_Platform_2007_0(Etw):
    pattern = Struct(
        "string" / WString
    )


@declare(guid=guid("e5fc4a0f-7198-492f-9b0f-88fdcbfded48"), event_id=2008, version=0)
class Microsoft_Windows_Networking_VPN_Plugin_Platform_2008_0(Etw):
    pattern = Struct(
        "string" / WString
    )


@declare(guid=guid("e5fc4a0f-7198-492f-9b0f-88fdcbfded48"), event_id=2009, version=0)
class Microsoft_Windows_Networking_VPN_Plugin_Platform_2009_0(Etw):
    pattern = Struct(
        "string" / WString
    )


@declare(guid=guid("e5fc4a0f-7198-492f-9b0f-88fdcbfded48"), event_id=2010, version=0)
class Microsoft_Windows_Networking_VPN_Plugin_Platform_2010_0(Etw):
    pattern = Struct(
        "string" / WString
    )


@declare(guid=guid("e5fc4a0f-7198-492f-9b0f-88fdcbfded48"), event_id=2011, version=0)
class Microsoft_Windows_Networking_VPN_Plugin_Platform_2011_0(Etw):
    pattern = Struct(
        "string" / WString
    )


@declare(guid=guid("e5fc4a0f-7198-492f-9b0f-88fdcbfded48"), event_id=2012, version=0)
class Microsoft_Windows_Networking_VPN_Plugin_Platform_2012_0(Etw):
    pattern = Struct(
        "string" / WString
    )


@declare(guid=guid("e5fc4a0f-7198-492f-9b0f-88fdcbfded48"), event_id=2013, version=0)
class Microsoft_Windows_Networking_VPN_Plugin_Platform_2013_0(Etw):
    pattern = Struct(
        "string" / WString
    )


@declare(guid=guid("e5fc4a0f-7198-492f-9b0f-88fdcbfded48"), event_id=2014, version=0)
class Microsoft_Windows_Networking_VPN_Plugin_Platform_2014_0(Etw):
    pattern = Struct(
        "string" / WString
    )


@declare(guid=guid("e5fc4a0f-7198-492f-9b0f-88fdcbfded48"), event_id=2015, version=0)
class Microsoft_Windows_Networking_VPN_Plugin_Platform_2015_0(Etw):
    pattern = Struct(
        "string" / WString
    )


@declare(guid=guid("e5fc4a0f-7198-492f-9b0f-88fdcbfded48"), event_id=2016, version=0)
class Microsoft_Windows_Networking_VPN_Plugin_Platform_2016_0(Etw):
    pattern = Struct(
        "string" / WString
    )


@declare(guid=guid("e5fc4a0f-7198-492f-9b0f-88fdcbfded48"), event_id=2017, version=0)
class Microsoft_Windows_Networking_VPN_Plugin_Platform_2017_0(Etw):
    pattern = Struct(
        "string" / WString
    )


@declare(guid=guid("e5fc4a0f-7198-492f-9b0f-88fdcbfded48"), event_id=2018, version=0)
class Microsoft_Windows_Networking_VPN_Plugin_Platform_2018_0(Etw):
    pattern = Struct(
        "string" / WString
    )


@declare(guid=guid("e5fc4a0f-7198-492f-9b0f-88fdcbfded48"), event_id=2019, version=0)
class Microsoft_Windows_Networking_VPN_Plugin_Platform_2019_0(Etw):
    pattern = Struct(
        "plugin" / Sid,
        "profile" / WString
    )


@declare(guid=guid("e5fc4a0f-7198-492f-9b0f-88fdcbfded48"), event_id=2020, version=0)
class Microsoft_Windows_Networking_VPN_Plugin_Platform_2020_0(Etw):
    pattern = Struct(
        "plugin" / Sid,
        "profile" / WString
    )


@declare(guid=guid("e5fc4a0f-7198-492f-9b0f-88fdcbfded48"), event_id=2021, version=0)
class Microsoft_Windows_Networking_VPN_Plugin_Platform_2021_0(Etw):
    pattern = Struct(
        "plugin" / Sid,
        "profile" / WString
    )


@declare(guid=guid("e5fc4a0f-7198-492f-9b0f-88fdcbfded48"), event_id=2022, version=0)
class Microsoft_Windows_Networking_VPN_Plugin_Platform_2022_0(Etw):
    pattern = Struct(
        "plugin" / Sid,
        "profile" / WString
    )


@declare(guid=guid("e5fc4a0f-7198-492f-9b0f-88fdcbfded48"), event_id=2023, version=0)
class Microsoft_Windows_Networking_VPN_Plugin_Platform_2023_0(Etw):
    pattern = Struct(
        "plugin" / Sid,
        "profile" / WString
    )


@declare(guid=guid("e5fc4a0f-7198-492f-9b0f-88fdcbfded48"), event_id=2024, version=0)
class Microsoft_Windows_Networking_VPN_Plugin_Platform_2024_0(Etw):
    pattern = Struct(
        "plugin" / Sid,
        "profile" / WString
    )


@declare(guid=guid("e5fc4a0f-7198-492f-9b0f-88fdcbfded48"), event_id=2025, version=0)
class Microsoft_Windows_Networking_VPN_Plugin_Platform_2025_0(Etw):
    pattern = Struct(
        "plugin" / Sid,
        "profile" / WString
    )


@declare(guid=guid("e5fc4a0f-7198-492f-9b0f-88fdcbfded48"), event_id=2026, version=0)
class Microsoft_Windows_Networking_VPN_Plugin_Platform_2026_0(Etw):
    pattern = Struct(
        "plugin" / Sid,
        "profile" / WString
    )


@declare(guid=guid("e5fc4a0f-7198-492f-9b0f-88fdcbfded48"), event_id=2027, version=0)
class Microsoft_Windows_Networking_VPN_Plugin_Platform_2027_0(Etw):
    pattern = Struct(
        "plugin" / Sid,
        "profile" / WString
    )


@declare(guid=guid("e5fc4a0f-7198-492f-9b0f-88fdcbfded48"), event_id=2028, version=0)
class Microsoft_Windows_Networking_VPN_Plugin_Platform_2028_0(Etw):
    pattern = Struct(
        "string" / WString
    )


@declare(guid=guid("e5fc4a0f-7198-492f-9b0f-88fdcbfded48"), event_id=2029, version=0)
class Microsoft_Windows_Networking_VPN_Plugin_Platform_2029_0(Etw):
    pattern = Struct(
        "string" / WString
    )


@declare(guid=guid("e5fc4a0f-7198-492f-9b0f-88fdcbfded48"), event_id=2030, version=0)
class Microsoft_Windows_Networking_VPN_Plugin_Platform_2030_0(Etw):
    pattern = Struct(
        "string" / WString
    )


@declare(guid=guid("e5fc4a0f-7198-492f-9b0f-88fdcbfded48"), event_id=2031, version=0)
class Microsoft_Windows_Networking_VPN_Plugin_Platform_2031_0(Etw):
    pattern = Struct(
        "Error" / Int32ul
    )


@declare(guid=guid("e5fc4a0f-7198-492f-9b0f-88fdcbfded48"), event_id=2032, version=0)
class Microsoft_Windows_Networking_VPN_Plugin_Platform_2032_0(Etw):
    pattern = Struct(
        "Error" / Int32ul
    )

