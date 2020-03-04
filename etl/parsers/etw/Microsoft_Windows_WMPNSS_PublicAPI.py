# -*- coding: utf-8 -*-
"""
Microsoft-Windows-WMPNSS-PublicAPI
GUID : 614696c9-85af-4e64-b389-d2c0db4ff87b
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("614696c9-85af-4e64-b389-d2c0db4ff87b"), event_id=100, version=0)
class Microsoft_Windows_WMPNSS_PublicAPI_100_0(Etw):
    pattern = Struct(
        "Enable" / Int8ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("614696c9-85af-4e64-b389-d2c0db4ff87b"), event_id=101, version=0)
class Microsoft_Windows_WMPNSS_PublicAPI_101_0(Etw):
    pattern = Struct(
        "Enable" / Int8ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("614696c9-85af-4e64-b389-d2c0db4ff87b"), event_id=102, version=0)
class Microsoft_Windows_WMPNSS_PublicAPI_102_0(Etw):
    pattern = Struct(
        "Enable" / Int8ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("614696c9-85af-4e64-b389-d2c0db4ff87b"), event_id=103, version=0)
class Microsoft_Windows_WMPNSS_PublicAPI_103_0(Etw):
    pattern = Struct(
        "Enable" / Int8ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("614696c9-85af-4e64-b389-d2c0db4ff87b"), event_id=104, version=0)
class Microsoft_Windows_WMPNSS_PublicAPI_104_0(Etw):
    pattern = Struct(
        "LibraryName" / WString,
        "HResult" / Int32ul
    )


@declare(guid=guid("614696c9-85af-4e64-b389-d2c0db4ff87b"), event_id=105, version=0)
class Microsoft_Windows_WMPNSS_PublicAPI_105_0(Etw):
    pattern = Struct(
        "LibraryName" / WString,
        "HResult" / Int32ul
    )


@declare(guid=guid("614696c9-85af-4e64-b389-d2c0db4ff87b"), event_id=106, version=0)
class Microsoft_Windows_WMPNSS_PublicAPI_106_0(Etw):
    pattern = Struct(
        "LibraryName" / WString,
        "HResult" / Int32ul
    )


@declare(guid=guid("614696c9-85af-4e64-b389-d2c0db4ff87b"), event_id=107, version=0)
class Microsoft_Windows_WMPNSS_PublicAPI_107_0(Etw):
    pattern = Struct(
        "LibraryName" / WString,
        "HResult" / Int32ul
    )


@declare(guid=guid("614696c9-85af-4e64-b389-d2c0db4ff87b"), event_id=108, version=0)
class Microsoft_Windows_WMPNSS_PublicAPI_108_0(Etw):
    pattern = Struct(
        "Enable" / Int8ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("614696c9-85af-4e64-b389-d2c0db4ff87b"), event_id=109, version=0)
class Microsoft_Windows_WMPNSS_PublicAPI_109_0(Etw):
    pattern = Struct(
        "Enable" / Int8ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("614696c9-85af-4e64-b389-d2c0db4ff87b"), event_id=110, version=0)
class Microsoft_Windows_WMPNSS_PublicAPI_110_0(Etw):
    pattern = Struct(
        "Enable" / Int8ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("614696c9-85af-4e64-b389-d2c0db4ff87b"), event_id=111, version=0)
class Microsoft_Windows_WMPNSS_PublicAPI_111_0(Etw):
    pattern = Struct(
        "Enable" / Int8ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("614696c9-85af-4e64-b389-d2c0db4ff87b"), event_id=112, version=0)
class Microsoft_Windows_WMPNSS_PublicAPI_112_0(Etw):
    pattern = Struct(
        "Enable" / Int8ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("614696c9-85af-4e64-b389-d2c0db4ff87b"), event_id=113, version=0)
class Microsoft_Windows_WMPNSS_PublicAPI_113_0(Etw):
    pattern = Struct(
        "Enable" / Int8ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("614696c9-85af-4e64-b389-d2c0db4ff87b"), event_id=114, version=0)
class Microsoft_Windows_WMPNSS_PublicAPI_114_0(Etw):
    pattern = Struct(
        "Enable" / Int8ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("614696c9-85af-4e64-b389-d2c0db4ff87b"), event_id=115, version=0)
class Microsoft_Windows_WMPNSS_PublicAPI_115_0(Etw):
    pattern = Struct(
        "Enable" / Int8ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("614696c9-85af-4e64-b389-d2c0db4ff87b"), event_id=116, version=0)
class Microsoft_Windows_WMPNSS_PublicAPI_116_0(Etw):
    pattern = Struct(
        "Enable" / Int8ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("614696c9-85af-4e64-b389-d2c0db4ff87b"), event_id=117, version=0)
class Microsoft_Windows_WMPNSS_PublicAPI_117_0(Etw):
    pattern = Struct(
        "Enable" / Int8ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("614696c9-85af-4e64-b389-d2c0db4ff87b"), event_id=118, version=0)
class Microsoft_Windows_WMPNSS_PublicAPI_118_0(Etw):
    pattern = Struct(
        "Enable" / Int8ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("614696c9-85af-4e64-b389-d2c0db4ff87b"), event_id=119, version=0)
class Microsoft_Windows_WMPNSS_PublicAPI_119_0(Etw):
    pattern = Struct(
        "Enable" / Int8ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("614696c9-85af-4e64-b389-d2c0db4ff87b"), event_id=120, version=0)
class Microsoft_Windows_WMPNSS_PublicAPI_120_0(Etw):
    pattern = Struct(
        "Enable" / Int8ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("614696c9-85af-4e64-b389-d2c0db4ff87b"), event_id=121, version=0)
class Microsoft_Windows_WMPNSS_PublicAPI_121_0(Etw):
    pattern = Struct(
        "Enable" / Int8ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("614696c9-85af-4e64-b389-d2c0db4ff87b"), event_id=122, version=0)
class Microsoft_Windows_WMPNSS_PublicAPI_122_0(Etw):
    pattern = Struct(
        "Enable" / Int8ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("614696c9-85af-4e64-b389-d2c0db4ff87b"), event_id=123, version=0)
class Microsoft_Windows_WMPNSS_PublicAPI_123_0(Etw):
    pattern = Struct(
        "Enable" / Int8ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("614696c9-85af-4e64-b389-d2c0db4ff87b"), event_id=124, version=0)
class Microsoft_Windows_WMPNSS_PublicAPI_124_0(Etw):
    pattern = Struct(
        "MACAddress" / WString,
        "FriendlyName" / WString,
        "Authorize" / Int8ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("614696c9-85af-4e64-b389-d2c0db4ff87b"), event_id=125, version=0)
class Microsoft_Windows_WMPNSS_PublicAPI_125_0(Etw):
    pattern = Struct(
        "MACAddress" / WString,
        "FriendlyName" / WString,
        "Authorize" / Int8ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("614696c9-85af-4e64-b389-d2c0db4ff87b"), event_id=126, version=0)
class Microsoft_Windows_WMPNSS_PublicAPI_126_0(Etw):
    pattern = Struct(
        "MACAddress" / WString,
        "Authorize" / Int8ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("614696c9-85af-4e64-b389-d2c0db4ff87b"), event_id=127, version=0)
class Microsoft_Windows_WMPNSS_PublicAPI_127_0(Etw):
    pattern = Struct(
        "MACAddress" / WString,
        "Authorize" / Int8ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("614696c9-85af-4e64-b389-d2c0db4ff87b"), event_id=128, version=0)
class Microsoft_Windows_WMPNSS_PublicAPI_128_0(Etw):
    pattern = Struct(
        "Devices" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("614696c9-85af-4e64-b389-d2c0db4ff87b"), event_id=129, version=0)
class Microsoft_Windows_WMPNSS_PublicAPI_129_0(Etw):
    pattern = Struct(
        "Devices" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("614696c9-85af-4e64-b389-d2c0db4ff87b"), event_id=130, version=0)
class Microsoft_Windows_WMPNSS_PublicAPI_130_0(Etw):
    pattern = Struct(
        "Enable" / Int8ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("614696c9-85af-4e64-b389-d2c0db4ff87b"), event_id=131, version=0)
class Microsoft_Windows_WMPNSS_PublicAPI_131_0(Etw):
    pattern = Struct(
        "Enable" / Int8ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("614696c9-85af-4e64-b389-d2c0db4ff87b"), event_id=132, version=0)
class Microsoft_Windows_WMPNSS_PublicAPI_132_0(Etw):
    pattern = Struct(
        "DeviceID" / WString,
        "HResult" / Int32ul
    )


@declare(guid=guid("614696c9-85af-4e64-b389-d2c0db4ff87b"), event_id=133, version=0)
class Microsoft_Windows_WMPNSS_PublicAPI_133_0(Etw):
    pattern = Struct(
        "DeviceID" / WString,
        "HResult" / Int32ul
    )


@declare(guid=guid("614696c9-85af-4e64-b389-d2c0db4ff87b"), event_id=134, version=0)
class Microsoft_Windows_WMPNSS_PublicAPI_134_0(Etw):
    pattern = Struct(
        "SecurityGroup" / WString,
        "HResult" / Int32ul
    )


@declare(guid=guid("614696c9-85af-4e64-b389-d2c0db4ff87b"), event_id=135, version=0)
class Microsoft_Windows_WMPNSS_PublicAPI_135_0(Etw):
    pattern = Struct(
        "SecurityGroup" / WString,
        "HResult" / Int32ul
    )


@declare(guid=guid("614696c9-85af-4e64-b389-d2c0db4ff87b"), event_id=136, version=0)
class Microsoft_Windows_WMPNSS_PublicAPI_136_0(Etw):
    pattern = Struct(
        "SecurityGroup" / WString,
        "HResult" / Int32ul
    )


@declare(guid=guid("614696c9-85af-4e64-b389-d2c0db4ff87b"), event_id=137, version=0)
class Microsoft_Windows_WMPNSS_PublicAPI_137_0(Etw):
    pattern = Struct(
        "SecurityGroup" / WString,
        "HResult" / Int32ul
    )

