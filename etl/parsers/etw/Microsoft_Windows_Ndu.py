# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Ndu
GUID : df271536-4298-45e1-b0f2-e88f78619c5d
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("df271536-4298-45e1-b0f2-e88f78619c5d"), event_id=2001, version=0)
class Microsoft_Windows_Ndu_2001_0(Etw):
    pattern = Struct(
        "_DebugString" / WString
    )


@declare(guid=guid("df271536-4298-45e1-b0f2-e88f78619c5d"), event_id=2002, version=0)
class Microsoft_Windows_Ndu_2002_0(Etw):
    pattern = Struct(
        "_FunctionName" / WString,
        "_Status" / Int32ul
    )


@declare(guid=guid("df271536-4298-45e1-b0f2-e88f78619c5d"), event_id=2003, version=0)
class Microsoft_Windows_Ndu_2003_0(Etw):
    pattern = Struct(
        "_IfLuid" / Int64ul,
        "_ProcNum" / Int32ul,
        "_ListIndex" / Int16ul
    )


@declare(guid=guid("df271536-4298-45e1-b0f2-e88f78619c5d"), event_id=2004, version=0)
class Microsoft_Windows_Ndu_2004_0(Etw):
    pattern = Struct(
        "_Direction" / WString,
        "_FlowHandle" / Int64ul,
        "_ExePath" / WString,
        "_SvcTag" / Int32ul,
        "_PkgName" / WString,
        "_UserId" / Sid,
        "_Pid" / Int32ul
    )


@declare(guid=guid("df271536-4298-45e1-b0f2-e88f78619c5d"), event_id=2005, version=0)
class Microsoft_Windows_Ndu_2005_0(Etw):
    pattern = Struct(
        "_FlowHandle" / Int64ul,
        "_RefDeref" / WString
    )


@declare(guid=guid("df271536-4298-45e1-b0f2-e88f78619c5d"), event_id=2006, version=0)
class Microsoft_Windows_Ndu_2006_0(Etw):
    pattern = Struct(
        "_IfLuid" / Int64ul,
        "_ProfileId" / Int32ul,
        "_BytesSent" / Int32ul,
        "_BytesRecvd" / Int32ul
    )


@declare(guid=guid("df271536-4298-45e1-b0f2-e88f78619c5d"), event_id=2007, version=0)
class Microsoft_Windows_Ndu_2007_0(Etw):
    pattern = Struct(
        "_IfLuid" / Int64ul,
        "_FlowHandle" / Int64ul,
        "_BytesSent" / Int32ul,
        "_BytesRecvd" / Int32ul
    )


@declare(guid=guid("df271536-4298-45e1-b0f2-e88f78619c5d"), event_id=2008, version=0)
class Microsoft_Windows_Ndu_2008_0(Etw):
    pattern = Struct(
        "_ExePath" / WString,
        "_SvcTag" / Int32ul,
        "_PkgName" / WString,
        "_UserId" / Sid,
        "_Cookie" / Int32ul,
        "_Quota" / Int32ul
    )


@declare(guid=guid("df271536-4298-45e1-b0f2-e88f78619c5d"), event_id=2009, version=0)
class Microsoft_Windows_Ndu_2009_0(Etw):
    pattern = Struct(
        "_Cookie" / Int32ul
    )


@declare(guid=guid("df271536-4298-45e1-b0f2-e88f78619c5d"), event_id=2010, version=0)
class Microsoft_Windows_Ndu_2010_0(Etw):
    pattern = Struct(
        "_IfLuid" / Int64ul,
        "_ProfileId" / Int32ul,
        "_BytesLimit" / Int64ul
    )


@declare(guid=guid("df271536-4298-45e1-b0f2-e88f78619c5d"), event_id=2011, version=0)
class Microsoft_Windows_Ndu_2011_0(Etw):
    pattern = Struct(
        "_IfLuid" / Int64ul,
        "_ProfileId" / Int32ul
    )


@declare(guid=guid("df271536-4298-45e1-b0f2-e88f78619c5d"), event_id=2012, version=0)
class Microsoft_Windows_Ndu_2012_0(Etw):
    pattern = Struct(
        "_DebugString" / WString
    )


@declare(guid=guid("df271536-4298-45e1-b0f2-e88f78619c5d"), event_id=2013, version=0)
class Microsoft_Windows_Ndu_2013_0(Etw):
    pattern = Struct(
        "_DebugString" / WString
    )


@declare(guid=guid("df271536-4298-45e1-b0f2-e88f78619c5d"), event_id=2014, version=0)
class Microsoft_Windows_Ndu_2014_0(Etw):
    pattern = Struct(
        "_IfLuid" / Int64ul,
        "_ProfileId" / Int32ul,
        "_BytesSent" / Int64ul,
        "_BytesRecvd" / Int64ul,
        "_IsCosted" / Int8ul
    )


@declare(guid=guid("df271536-4298-45e1-b0f2-e88f78619c5d"), event_id=2015, version=0)
class Microsoft_Windows_Ndu_2015_0(Etw):
    pattern = Struct(
        "_IfLuid" / Int64ul,
        "TimeSinceLast" / Int64ul,
        "Energy" / Int64ul,
        "CurrentProc" / Int32ul,
        "BytesTxRx" / Int32ul,
        "Pid" / Int32ul,
        "IfMediaType" / Int8ul
    )


@declare(guid=guid("df271536-4298-45e1-b0f2-e88f78619c5d"), event_id=2016, version=0)
class Microsoft_Windows_Ndu_2016_0(Etw):
    pattern = Struct(
        "ProcId" / Int32ul,
        "Count" / Int32ul
    )

