# -*- coding: utf-8 -*-
"""
Microsoft-Windows-StorageManagement-WSP-Spaces
GUID : 88c09888-118d-48fc-8863-e1c6d39ca4df
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("88c09888-118d-48fc-8863-e1c6d39ca4df"), event_id=2000, version=0)
class Microsoft_Windows_StorageManagement_WSP_Spaces_2000_0(Etw):
    pattern = Struct(
        "SubsystemID" / WString,
        "SubsystemURI" / WString,
        "Username" / WString,
        "ErrorCode" / Int32ul,
        "ErrorString" / WString
    )


@declare(guid=guid("88c09888-118d-48fc-8863-e1c6d39ca4df"), event_id=2003, version=0)
class Microsoft_Windows_StorageManagement_WSP_Spaces_2003_0(Etw):
    pattern = Struct(
        "ClassName" / WString,
        "MethodName" / WString,
        "ObjectId" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("88c09888-118d-48fc-8863-e1c6d39ca4df"), event_id=2004, version=0)
class Microsoft_Windows_StorageManagement_WSP_Spaces_2004_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("88c09888-118d-48fc-8863-e1c6d39ca4df"), event_id=2005, version=0)
class Microsoft_Windows_StorageManagement_WSP_Spaces_2005_0(Etw):
    pattern = Struct(
        "JobName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("88c09888-118d-48fc-8863-e1c6d39ca4df"), event_id=2006, version=0)
class Microsoft_Windows_StorageManagement_WSP_Spaces_2006_0(Etw):
    pattern = Struct(
        "ClassName" / WString,
        "ObjectId" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("88c09888-118d-48fc-8863-e1c6d39ca4df"), event_id=2007, version=0)
class Microsoft_Windows_StorageManagement_WSP_Spaces_2007_0(Etw):
    pattern = Struct(
        "ClassName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("88c09888-118d-48fc-8863-e1c6d39ca4df"), event_id=2008, version=0)
class Microsoft_Windows_StorageManagement_WSP_Spaces_2008_0(Etw):
    pattern = Struct(
        "ClassName" / WString,
        "MethodName" / WString,
        "ObjectId" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("88c09888-118d-48fc-8863-e1c6d39ca4df"), event_id=2009, version=0)
class Microsoft_Windows_StorageManagement_WSP_Spaces_2009_0(Etw):
    pattern = Struct(
        "ComputerName" / WString,
        "ErrorCode" / Int32ul,
        "SecondaryErrorCode" / Int32ul
    )

