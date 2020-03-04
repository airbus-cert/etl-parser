# -*- coding: utf-8 -*-
"""
Microsoft-Windows-User Profiles General
GUID : db00dfb6-29f9-4a9c-9b3b-1f4f9e7d9770
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("db00dfb6-29f9-4a9c-9b3b-1f4f9e7d9770"), event_id=69, version=0)
class Microsoft_Windows_User_Profiles_General_69_0(Etw):
    pattern = Struct(
        "SourceFile" / WString,
        "SourceTimestamp" / WString,
        "DestinationFile" / WString,
        "DestinationTimestamp" / WString
    )


@declare(guid=guid("db00dfb6-29f9-4a9c-9b3b-1f4f9e7d9770"), event_id=77, version=0)
class Microsoft_Windows_User_Profiles_General_77_0(Etw):
    pattern = Struct(
        "EffectiveSid" / WString,
        "Location" / Int32ul,
        "Code" / Int32ul
    )


@declare(guid=guid("db00dfb6-29f9-4a9c-9b3b-1f4f9e7d9770"), event_id=1006, version=0)
class Microsoft_Windows_User_Profiles_General_1006_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "FileSizeInKb" / Int64ul,
        "SourceLocation" / WString,
        "DestinationLocation" / WString,
        "CopyTimeInSec" / Int64ul
    )


@declare(guid=guid("db00dfb6-29f9-4a9c-9b3b-1f4f9e7d9770"), event_id=1007, version=0)
class Microsoft_Windows_User_Profiles_General_1007_0(Etw):
    pattern = Struct(
        "SourceFile" / WString,
        "SourceTimestamp" / WString,
        "DestinationFile" / WString,
        "DestinationTimestamp" / WString
    )


@declare(guid=guid("db00dfb6-29f9-4a9c-9b3b-1f4f9e7d9770"), event_id=1509, version=0)
class Microsoft_Windows_User_Profiles_General_1509_0(Etw):
    pattern = Struct(
        "Source" / WString,
        "Target" / WString,
        "Error" / WString
    )


@declare(guid=guid("db00dfb6-29f9-4a9c-9b3b-1f4f9e7d9770"), event_id=1600, version=0)
class Microsoft_Windows_User_Profiles_General_1600_0(Etw):
    pattern = Struct(
        "Source" / WString,
        "Target" / WString
    )


@declare(guid=guid("db00dfb6-29f9-4a9c-9b3b-1f4f9e7d9770"), event_id=1601, version=0)
class Microsoft_Windows_User_Profiles_General_1601_0(Etw):
    pattern = Struct(
        "Source" / WString,
        "Target" / WString
    )

