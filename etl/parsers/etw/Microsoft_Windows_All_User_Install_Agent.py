# -*- coding: utf-8 -*-
"""
Microsoft-Windows-All-User-Install-Agent
GUID : d2e990da-8504-4702-a5e5-367fc2f823bf
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("d2e990da-8504-4702-a5e5-367fc2f823bf"), event_id=1287, version=0)
class Microsoft_Windows_All_User_Install_Agent_1287_0(Etw):
    pattern = Struct(
        "Param1" / WString
    )


@declare(guid=guid("d2e990da-8504-4702-a5e5-367fc2f823bf"), event_id=1288, version=0)
class Microsoft_Windows_All_User_Install_Agent_1288_0(Etw):
    pattern = Struct(
        "PackageMoniker" / WString,
        "UserSid" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("d2e990da-8504-4702-a5e5-367fc2f823bf"), event_id=1300, version=0)
class Microsoft_Windows_All_User_Install_Agent_1300_0(Etw):
    pattern = Struct(
        "UserSid" / WString,
        "Error" / Int32ul,
        "location" / Int32sl
    )


@declare(guid=guid("d2e990da-8504-4702-a5e5-367fc2f823bf"), event_id=1301, version=0)
class Microsoft_Windows_All_User_Install_Agent_1301_0(Etw):
    pattern = Struct(
        "Param1" / WString
    )


@declare(guid=guid("d2e990da-8504-4702-a5e5-367fc2f823bf"), event_id=1302, version=0)
class Microsoft_Windows_All_User_Install_Agent_1302_0(Etw):
    pattern = Struct(
        "NumberOfPackages" / Int32sl,
        "UserSid" / WString
    )


@declare(guid=guid("d2e990da-8504-4702-a5e5-367fc2f823bf"), event_id=1303, version=0)
class Microsoft_Windows_All_User_Install_Agent_1303_0(Etw):
    pattern = Struct(
        "UserSid" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("d2e990da-8504-4702-a5e5-367fc2f823bf"), event_id=1304, version=0)
class Microsoft_Windows_All_User_Install_Agent_1304_0(Etw):
    pattern = Struct(
        "Package" / WString,
        "UserSid" / WString
    )


@declare(guid=guid("d2e990da-8504-4702-a5e5-367fc2f823bf"), event_id=1305, version=0)
class Microsoft_Windows_All_User_Install_Agent_1305_0(Etw):
    pattern = Struct(
        "Package" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("d2e990da-8504-4702-a5e5-367fc2f823bf"), event_id=1306, version=0)
class Microsoft_Windows_All_User_Install_Agent_1306_0(Etw):
    pattern = Struct(
        "Package" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("d2e990da-8504-4702-a5e5-367fc2f823bf"), event_id=1307, version=0)
class Microsoft_Windows_All_User_Install_Agent_1307_0(Etw):
    pattern = Struct(
        "Package" / WString
    )

