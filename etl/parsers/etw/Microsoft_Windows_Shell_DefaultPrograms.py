# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Shell-DefaultPrograms
GUID : 65d99466-7a8e-489c-b8e1-962bc945031e
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("65d99466-7a8e-489c-b8e1-962bc945031e"), event_id=1, version=0)
class Microsoft_Windows_Shell_DefaultPrograms_1_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("65d99466-7a8e-489c-b8e1-962bc945031e"), event_id=2, version=0)
class Microsoft_Windows_Shell_DefaultPrograms_2_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("65d99466-7a8e-489c-b8e1-962bc945031e"), event_id=3, version=0)
class Microsoft_Windows_Shell_DefaultPrograms_3_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("65d99466-7a8e-489c-b8e1-962bc945031e"), event_id=4, version=0)
class Microsoft_Windows_Shell_DefaultPrograms_4_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("65d99466-7a8e-489c-b8e1-962bc945031e"), event_id=5, version=0)
class Microsoft_Windows_Shell_DefaultPrograms_5_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("65d99466-7a8e-489c-b8e1-962bc945031e"), event_id=6, version=0)
class Microsoft_Windows_Shell_DefaultPrograms_6_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("65d99466-7a8e-489c-b8e1-962bc945031e"), event_id=7, version=0)
class Microsoft_Windows_Shell_DefaultPrograms_7_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("65d99466-7a8e-489c-b8e1-962bc945031e"), event_id=8, version=0)
class Microsoft_Windows_Shell_DefaultPrograms_8_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )

