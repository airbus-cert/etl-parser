# -*- coding: utf-8 -*-
"""
Microsoft-Windows-SruMon
GUID : c8dbf506-e3d3-4822-930d-84c557eb6247
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("c8dbf506-e3d3-4822-930d-84c557eb6247"), event_id=2001, version=0)
class Microsoft_Windows_SruMon_2001_0(Etw):
    pattern = Struct(
        "_DebugString" / WString
    )


@declare(guid=guid("c8dbf506-e3d3-4822-930d-84c557eb6247"), event_id=2002, version=0)
class Microsoft_Windows_SruMon_2002_0(Etw):
    pattern = Struct(
        "_FunctionName" / WString,
        "_Status" / Int32ul
    )


@declare(guid=guid("c8dbf506-e3d3-4822-930d-84c557eb6247"), event_id=2003, version=0)
class Microsoft_Windows_SruMon_2003_0(Etw):
    pattern = Struct(
        "_FunctionName" / WString,
        "_HR" / Int32sl
    )


@declare(guid=guid("c8dbf506-e3d3-4822-930d-84c557eb6247"), event_id=2004, version=0)
class Microsoft_Windows_SruMon_2004_0(Etw):
    pattern = Struct(
        "_TableName" / WString
    )


@declare(guid=guid("c8dbf506-e3d3-4822-930d-84c557eb6247"), event_id=2005, version=0)
class Microsoft_Windows_SruMon_2005_0(Etw):
    pattern = Struct(
        "_FunctionName" / WString,
        "_HR" / Int32sl
    )


@declare(guid=guid("c8dbf506-e3d3-4822-930d-84c557eb6247"), event_id=2006, version=0)
class Microsoft_Windows_SruMon_2006_0(Etw):
    pattern = Struct(
        "_FunctionName" / WString
    )


@declare(guid=guid("c8dbf506-e3d3-4822-930d-84c557eb6247"), event_id=2007, version=0)
class Microsoft_Windows_SruMon_2007_0(Etw):
    pattern = Struct(
        "_FunctionName" / WString
    )


@declare(guid=guid("c8dbf506-e3d3-4822-930d-84c557eb6247"), event_id=2008, version=0)
class Microsoft_Windows_SruMon_2008_0(Etw):
    pattern = Struct(
        "_Status" / WString
    )


@declare(guid=guid("c8dbf506-e3d3-4822-930d-84c557eb6247"), event_id=2009, version=0)
class Microsoft_Windows_SruMon_2009_0(Etw):
    pattern = Struct(
        "_Reset" / WString
    )


@declare(guid=guid("c8dbf506-e3d3-4822-930d-84c557eb6247"), event_id=2010, version=0)
class Microsoft_Windows_SruMon_2010_0(Etw):
    pattern = Struct(
        "_FunctionName" / WString,
        "_ApplicationName" / WString,
        "_InterfaceLuid" / Int64ul,
        "_Costed" / Int8ul,
        "_BytesSent" / Int64ul,
        "_BytesReceived" / Int64ul
    )


@declare(guid=guid("c8dbf506-e3d3-4822-930d-84c557eb6247"), event_id=2011, version=0)
class Microsoft_Windows_SruMon_2011_0(Etw):
    pattern = Struct(
        "_FunctionName" / WString
    )


@declare(guid=guid("c8dbf506-e3d3-4822-930d-84c557eb6247"), event_id=2012, version=0)
class Microsoft_Windows_SruMon_2012_0(Etw):
    pattern = Struct(
        "_InterfaceGuid" / Guid,
        "_InterfaceLuid" / Int64ul,
        "_Application" / WString,
        "_ProfileId" / Int64ul,
        "_ProfileFlags" / Int64ul,
        "_BytesSent" / Int64ul,
        "_BytesReceived" / Int64ul
    )

