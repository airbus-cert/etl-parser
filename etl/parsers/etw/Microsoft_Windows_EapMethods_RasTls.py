# -*- coding: utf-8 -*-
"""
Microsoft-Windows-EapMethods-RasTls
GUID : 9cc0413e-5717-4af5-82eb-6103d8707b45
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("9cc0413e-5717-4af5-82eb-6103d8707b45"), event_id=100, version=0)
class Microsoft_Windows_EapMethods_RasTls_100_0(Etw):
    pattern = Struct(
        "uint1" / Int32ul
    )


@declare(guid=guid("9cc0413e-5717-4af5-82eb-6103d8707b45"), event_id=101, version=0)
class Microsoft_Windows_EapMethods_RasTls_101_0(Etw):
    pattern = Struct(
        "uint1" / Int32ul,
        "uint2" / Int32ul
    )


@declare(guid=guid("9cc0413e-5717-4af5-82eb-6103d8707b45"), event_id=102, version=0)
class Microsoft_Windows_EapMethods_RasTls_102_0(Etw):
    pattern = Struct(
        "uint1" / Int32ul,
        "uint2" / Int32ul
    )


@declare(guid=guid("9cc0413e-5717-4af5-82eb-6103d8707b45"), event_id=103, version=0)
class Microsoft_Windows_EapMethods_RasTls_103_0(Etw):
    pattern = Struct(
        "uint1" / Int32ul,
        "uint2" / Int32ul
    )


@declare(guid=guid("9cc0413e-5717-4af5-82eb-6103d8707b45"), event_id=104, version=0)
class Microsoft_Windows_EapMethods_RasTls_104_0(Etw):
    pattern = Struct(
        "uint1" / Int32ul,
        "uint2" / Int32ul
    )


@declare(guid=guid("9cc0413e-5717-4af5-82eb-6103d8707b45"), event_id=105, version=0)
class Microsoft_Windows_EapMethods_RasTls_105_0(Etw):
    pattern = Struct(
        "uint1" / Int32ul
    )


@declare(guid=guid("9cc0413e-5717-4af5-82eb-6103d8707b45"), event_id=107, version=0)
class Microsoft_Windows_EapMethods_RasTls_107_0(Etw):
    pattern = Struct(
        "CAThumbprint" / WString,
        "ServerName" / WString
    )

