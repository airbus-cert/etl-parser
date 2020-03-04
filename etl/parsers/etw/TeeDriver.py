# -*- coding: utf-8 -*-
"""
TeeDriver
GUID : e1da8995-85bc-452b-b62b-0913306a430e
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("e1da8995-85bc-452b-b62b-0913306a430e"), event_id=100, version=0)
class TeeDriver_100_0(Etw):
    pattern = Struct(
        "Function" / CString,
        "NtStatus" / Int32sl
    )


@declare(guid=guid("e1da8995-85bc-452b-b62b-0913306a430e"), event_id=101, version=0)
class TeeDriver_101_0(Etw):
    pattern = Struct(
        "FunctionName" / CString
    )


@declare(guid=guid("e1da8995-85bc-452b-b62b-0913306a430e"), event_id=102, version=0)
class TeeDriver_102_0(Etw):
    pattern = Struct(
        "FunctionName" / CString,
        "status" / Int32ul
    )


@declare(guid=guid("e1da8995-85bc-452b-b62b-0913306a430e"), event_id=103, version=0)
class TeeDriver_103_0(Etw):
    pattern = Struct(
        "PreviousState" / Int32ul
    )


@declare(guid=guid("e1da8995-85bc-452b-b62b-0913306a430e"), event_id=104, version=0)
class TeeDriver_104_0(Etw):
    pattern = Struct(
        "FunctionName" / CString,
        "status" / Int32ul
    )


@declare(guid=guid("e1da8995-85bc-452b-b62b-0913306a430e"), event_id=105, version=0)
class TeeDriver_105_0(Etw):
    pattern = Struct(
        "PreviousState" / Int32ul
    )


@declare(guid=guid("e1da8995-85bc-452b-b62b-0913306a430e"), event_id=106, version=0)
class TeeDriver_106_0(Etw):
    pattern = Struct(
        "FunctionName" / CString,
        "status" / Int32ul
    )


@declare(guid=guid("e1da8995-85bc-452b-b62b-0913306a430e"), event_id=107, version=0)
class TeeDriver_107_0(Etw):
    pattern = Struct(
        "FunctionName" / CString
    )


@declare(guid=guid("e1da8995-85bc-452b-b62b-0913306a430e"), event_id=108, version=0)
class TeeDriver_108_0(Etw):
    pattern = Struct(
        "FunctionName" / CString,
        "status" / Int32ul
    )


@declare(guid=guid("e1da8995-85bc-452b-b62b-0913306a430e"), event_id=109, version=0)
class TeeDriver_109_0(Etw):
    pattern = Struct(
        "Count" / Int32ul
    )


@declare(guid=guid("e1da8995-85bc-452b-b62b-0913306a430e"), event_id=110, version=0)
class TeeDriver_110_0(Etw):
    pattern = Struct(
        "message" / CString,
        "status" / Int32ul
    )


@declare(guid=guid("e1da8995-85bc-452b-b62b-0913306a430e"), event_id=111, version=0)
class TeeDriver_111_0(Etw):
    pattern = Struct(
        "message" / CString,
        "register" / Int32ul,
        "status" / Int32ul
    )


@declare(guid=guid("e1da8995-85bc-452b-b62b-0913306a430e"), event_id=112, version=0)
class TeeDriver_112_0(Etw):
    pattern = Struct(
        "H_CSR" / Int32ul,
        "ME_CSR" / Int32ul,
        "message" / CString
    )


@declare(guid=guid("e1da8995-85bc-452b-b62b-0913306a430e"), event_id=113, version=0)
class TeeDriver_113_0(Etw):
    pattern = Struct(
        "Message" / CString,
        "status" / Int32ul,
        "Function" / CString
    )


@declare(guid=guid("e1da8995-85bc-452b-b62b-0913306a430e"), event_id=114, version=0)
class TeeDriver_114_0(Etw):
    pattern = Struct(
        "header" / Int32ul,
        "length" / Int32ul
    )


@declare(guid=guid("e1da8995-85bc-452b-b62b-0913306a430e"), event_id=115, version=0)
class TeeDriver_115_0(Etw):
    pattern = Struct(
        "header" / Int32ul,
        "length" / Int32ul
    )


@declare(guid=guid("e1da8995-85bc-452b-b62b-0913306a430e"), event_id=116, version=0)
class TeeDriver_116_0(Etw):
    pattern = Struct(
        "status" / Int32ul,
        "hostid" / Int8ul
    )


@declare(guid=guid("e1da8995-85bc-452b-b62b-0913306a430e"), event_id=117, version=0)
class TeeDriver_117_0(Etw):
    pattern = Struct(
        "status" / Int32ul,
        "hostid" / Int8ul
    )


@declare(guid=guid("e1da8995-85bc-452b-b62b-0913306a430e"), event_id=119, version=0)
class TeeDriver_119_0(Etw):
    pattern = Struct(
        "data1" / Int8ul,
        "data2" / Int8ul,
        "data3" / Int8ul,
        "data4" / Int8ul
    )


@declare(guid=guid("e1da8995-85bc-452b-b62b-0913306a430e"), event_id=120, version=0)
class TeeDriver_120_0(Etw):
    pattern = Struct(
        "data1" / Int8ul,
        "data2" / Int8ul,
        "data3" / Int8ul,
        "data4" / Int8ul
    )

