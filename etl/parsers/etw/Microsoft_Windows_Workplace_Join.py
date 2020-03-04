# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Workplace Join
GUID : 76ab12d5-c986-4e60-9d7c-2a092b284cdd
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("76ab12d5-c986-4e60-9d7c-2a092b284cdd"), event_id=100, version=0)
class Microsoft_Windows_Workplace_Join_100_0(Etw):
    pattern = Struct(
        "ActivityId" / WString,
        "JWT" / WString
    )


@declare(guid=guid("76ab12d5-c986-4e60-9d7c-2a092b284cdd"), event_id=101, version=0)
class Microsoft_Windows_Workplace_Join_101_0(Etw):
    pattern = Struct(
        "ServiceUri" / WString
    )


@declare(guid=guid("76ab12d5-c986-4e60-9d7c-2a092b284cdd"), event_id=102, version=0)
class Microsoft_Windows_Workplace_Join_102_0(Etw):
    pattern = Struct(
        "ExitCode" / Int32ul,
        "ErrorMessage" / WString,
        "ServiceUri" / WString
    )


@declare(guid=guid("76ab12d5-c986-4e60-9d7c-2a092b284cdd"), event_id=103, version=0)
class Microsoft_Windows_Workplace_Join_103_0(Etw):
    pattern = Struct(
        "HttpStatus" / Int32sl,
        "ServiceUri" / WString,
        "TraceId" / WString
    )


@declare(guid=guid("76ab12d5-c986-4e60-9d7c-2a092b284cdd"), event_id=104, version=0)
class Microsoft_Windows_Workplace_Join_104_0(Etw):
    pattern = Struct(
        "ExitCode" / Int32ul,
        "ZoneUriIsAddedTo" / WString,
        "ZoneUriExistsIn" / WString,
        "Uri" / WString
    )


@declare(guid=guid("76ab12d5-c986-4e60-9d7c-2a092b284cdd"), event_id=200, version=0)
class Microsoft_Windows_Workplace_Join_200_0(Etw):
    pattern = Struct(
        "ExitCode" / Int32ul,
        "ActivityId" / WString,
        "SoapResponse" / WString,
        "ErrorMessage" / WString,
        "RegistrationServiceUri" / WString
    )


@declare(guid=guid("76ab12d5-c986-4e60-9d7c-2a092b284cdd"), event_id=201, version=0)
class Microsoft_Windows_Workplace_Join_201_0(Etw):
    pattern = Struct(
        "ActivityId" / WString,
        "SoapResponse" / WString,
        "RegistrationServiceUri" / WString
    )


@declare(guid=guid("76ab12d5-c986-4e60-9d7c-2a092b284cdd"), event_id=300, version=0)
class Microsoft_Windows_Workplace_Join_300_0(Etw):
    pattern = Struct(
        "ExitCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("76ab12d5-c986-4e60-9d7c-2a092b284cdd"), event_id=400, version=0)
class Microsoft_Windows_Workplace_Join_400_0(Etw):
    pattern = Struct(
        "ExitCode" / Int32ul,
        "ErrorCodeText" / WString,
        "ErrorMessage" / WString,
        "ErrorData" / WString
    )


@declare(guid=guid("76ab12d5-c986-4e60-9d7c-2a092b284cdd"), event_id=401, version=0)
class Microsoft_Windows_Workplace_Join_401_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "Data" / WString
    )

