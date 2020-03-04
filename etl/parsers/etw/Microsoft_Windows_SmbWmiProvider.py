# -*- coding: utf-8 -*-
"""
Microsoft-Windows-SmbWmiProvider
GUID : 50b9e206-9d55-4092-92e8-f157a8235799
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("50b9e206-9d55-4092-92e8-f157a8235799"), event_id=0, version=0)
class Microsoft_Windows_SmbWmiProvider_0_0(Etw):
    pattern = Struct(
        "FunctionName" / WString,
        "MiError" / Int32ul,
        "Win32Error" / Int32ul
    )


@declare(guid=guid("50b9e206-9d55-4092-92e8-f157a8235799"), event_id=1, version=0)
class Microsoft_Windows_SmbWmiProvider_1_0(Etw):
    pattern = Struct(
        "Message" / WString
    )

