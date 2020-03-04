# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Folder Redirection
GUID : 7d7b0c39-93f6-4100-bd96-4dda859652c5
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("7d7b0c39-93f6-4100-bd96-4dda859652c5"), event_id=501, version=0)
class Microsoft_Windows_Folder_Redirection_501_0(Etw):
    pattern = Struct(
        "FromFolder" / WString,
        "ToFolder" / WString,
        "Options" / Int32ul
    )


@declare(guid=guid("7d7b0c39-93f6-4100-bd96-4dda859652c5"), event_id=502, version=0)
class Microsoft_Windows_Folder_Redirection_502_0(Etw):
    pattern = Struct(
        "FromFolder" / WString,
        "ToFolder" / WString,
        "Options" / Int32ul,
        "Error" / WString,
        "ErrorDetails" / WString
    )


@declare(guid=guid("7d7b0c39-93f6-4100-bd96-4dda859652c5"), event_id=503, version=0)
class Microsoft_Windows_Folder_Redirection_503_0(Etw):
    pattern = Struct(
        "ErrorDetails" / WString
    )


@declare(guid=guid("7d7b0c39-93f6-4100-bd96-4dda859652c5"), event_id=505, version=0)
class Microsoft_Windows_Folder_Redirection_505_0(Etw):
    pattern = Struct(
        "Folder" / WString,
        "ErrorDetails" / WString
    )


@declare(guid=guid("7d7b0c39-93f6-4100-bd96-4dda859652c5"), event_id=506, version=0)
class Microsoft_Windows_Folder_Redirection_506_0(Etw):
    pattern = Struct(
        "Folder" / WString,
        "ErrorDetails" / WString
    )


@declare(guid=guid("7d7b0c39-93f6-4100-bd96-4dda859652c5"), event_id=507, version=0)
class Microsoft_Windows_Folder_Redirection_507_0(Etw):
    pattern = Struct(
        "Folder" / WString,
        "ErrorDetails" / WString
    )


@declare(guid=guid("7d7b0c39-93f6-4100-bd96-4dda859652c5"), event_id=508, version=0)
class Microsoft_Windows_Folder_Redirection_508_0(Etw):
    pattern = Struct(
        "Folder" / WString,
        "ErrorDetails" / WString
    )


@declare(guid=guid("7d7b0c39-93f6-4100-bd96-4dda859652c5"), event_id=509, version=0)
class Microsoft_Windows_Folder_Redirection_509_0(Etw):
    pattern = Struct(
        "Folder" / WString,
        "Path" / WString,
        "ErrorDetails" / WString
    )


@declare(guid=guid("7d7b0c39-93f6-4100-bd96-4dda859652c5"), event_id=511, version=0)
class Microsoft_Windows_Folder_Redirection_511_0(Etw):
    pattern = Struct(
        "ErrorDetails" / WString
    )


@declare(guid=guid("7d7b0c39-93f6-4100-bd96-4dda859652c5"), event_id=512, version=0)
class Microsoft_Windows_Folder_Redirection_512_0(Etw):
    pattern = Struct(
        "FromFolder" / WString,
        "ToFolder" / WString,
        "Options" / Int32ul
    )


@declare(guid=guid("7d7b0c39-93f6-4100-bd96-4dda859652c5"), event_id=513, version=0)
class Microsoft_Windows_Folder_Redirection_513_0(Etw):
    pattern = Struct(
        "FromFolder" / WString,
        "ToFolder" / WString,
        "Options" / Int32ul,
        "Error" / WString,
        "ErrorDetails" / WString
    )


@declare(guid=guid("7d7b0c39-93f6-4100-bd96-4dda859652c5"), event_id=514, version=0)
class Microsoft_Windows_Folder_Redirection_514_0(Etw):
    pattern = Struct(
        "Folder" / WString,
        "Options" / Int32ul
    )


@declare(guid=guid("7d7b0c39-93f6-4100-bd96-4dda859652c5"), event_id=515, version=0)
class Microsoft_Windows_Folder_Redirection_515_0(Etw):
    pattern = Struct(
        "Folder" / WString,
        "Options" / Int32ul,
        "Error" / WString,
        "ErrorDetails" / WString
    )


@declare(guid=guid("7d7b0c39-93f6-4100-bd96-4dda859652c5"), event_id=516, version=0)
class Microsoft_Windows_Folder_Redirection_516_0(Etw):
    pattern = Struct(
        "Folder" / WString,
        "Options" / Int32ul
    )


@declare(guid=guid("7d7b0c39-93f6-4100-bd96-4dda859652c5"), event_id=517, version=0)
class Microsoft_Windows_Folder_Redirection_517_0(Etw):
    pattern = Struct(
        "Folder" / WString,
        "Options" / Int32ul,
        "Error" / WString,
        "ErrorDetails" / WString
    )


@declare(guid=guid("7d7b0c39-93f6-4100-bd96-4dda859652c5"), event_id=1002, version=0)
class Microsoft_Windows_Folder_Redirection_1002_0(Etw):
    pattern = Struct(
        "GPFlags" / Int32ul
    )


@declare(guid=guid("7d7b0c39-93f6-4100-bd96-4dda859652c5"), event_id=1004, version=0)
class Microsoft_Windows_Folder_Redirection_1004_0(Etw):
    pattern = Struct(
        "ConfigurationFile" / WString
    )


@declare(guid=guid("7d7b0c39-93f6-4100-bd96-4dda859652c5"), event_id=1005, version=0)
class Microsoft_Windows_Folder_Redirection_1005_0(Etw):
    pattern = Struct(
        "Folder" / WString,
        "Options" / Int32ul
    )


@declare(guid=guid("7d7b0c39-93f6-4100-bd96-4dda859652c5"), event_id=1006, version=0)
class Microsoft_Windows_Folder_Redirection_1006_0(Etw):
    pattern = Struct(
        "Folder" / WString,
        "Options" / Int32ul,
        "ParentFolder" / WString,
        "Path" / WString,
        "Group" / WString
    )


@declare(guid=guid("7d7b0c39-93f6-4100-bd96-4dda859652c5"), event_id=1009, version=0)
class Microsoft_Windows_Folder_Redirection_1009_0(Etw):
    pattern = Struct(
        "Error" / Int32ul
    )


@declare(guid=guid("7d7b0c39-93f6-4100-bd96-4dda859652c5"), event_id=1010, version=0)
class Microsoft_Windows_Folder_Redirection_1010_0(Etw):
    pattern = Struct(
        "Result" / WString
    )

