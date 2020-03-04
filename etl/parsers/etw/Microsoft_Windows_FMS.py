# -*- coding: utf-8 -*-
"""
Microsoft-Windows-FMS
GUID : dea07764-0790-44de-b9c4-49677b17174f
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("dea07764-0790-44de-b9c4-49677b17174f"), event_id=2015, version=0)
class Microsoft_Windows_FMS_2015_0(Etw):
    pattern = Struct(
        "ApiName" / WString
    )


@declare(guid=guid("dea07764-0790-44de-b9c4-49677b17174f"), event_id=2016, version=0)
class Microsoft_Windows_FMS_2016_0(Etw):
    pattern = Struct(
        "ApiName" / WString
    )


@declare(guid=guid("dea07764-0790-44de-b9c4-49677b17174f"), event_id=40000, version=0)
class Microsoft_Windows_FMS_40000_0(Etw):
    pattern = Struct(
        "ApiName" / WString
    )


@declare(guid=guid("dea07764-0790-44de-b9c4-49677b17174f"), event_id=40001, version=0)
class Microsoft_Windows_FMS_40001_0(Etw):
    pattern = Struct(
        "ApiName" / WString
    )


@declare(guid=guid("dea07764-0790-44de-b9c4-49677b17174f"), event_id=40002, version=0)
class Microsoft_Windows_FMS_40002_0(Etw):
    pattern = Struct(
        "ApiName" / WString
    )


@declare(guid=guid("dea07764-0790-44de-b9c4-49677b17174f"), event_id=40003, version=0)
class Microsoft_Windows_FMS_40003_0(Etw):
    pattern = Struct(
        "ApiName" / WString
    )


@declare(guid=guid("dea07764-0790-44de-b9c4-49677b17174f"), event_id=40004, version=0)
class Microsoft_Windows_FMS_40004_0(Etw):
    pattern = Struct(
        "ApiName" / WString
    )


@declare(guid=guid("dea07764-0790-44de-b9c4-49677b17174f"), event_id=40005, version=0)
class Microsoft_Windows_FMS_40005_0(Etw):
    pattern = Struct(
        "ApiName" / WString
    )


@declare(guid=guid("dea07764-0790-44de-b9c4-49677b17174f"), event_id=40006, version=0)
class Microsoft_Windows_FMS_40006_0(Etw):
    pattern = Struct(
        "ApiName" / WString
    )


@declare(guid=guid("dea07764-0790-44de-b9c4-49677b17174f"), event_id=40007, version=0)
class Microsoft_Windows_FMS_40007_0(Etw):
    pattern = Struct(
        "ApiName" / WString
    )


@declare(guid=guid("dea07764-0790-44de-b9c4-49677b17174f"), event_id=40008, version=0)
class Microsoft_Windows_FMS_40008_0(Etw):
    pattern = Struct(
        "ApiName" / WString
    )


@declare(guid=guid("dea07764-0790-44de-b9c4-49677b17174f"), event_id=40009, version=0)
class Microsoft_Windows_FMS_40009_0(Etw):
    pattern = Struct(
        "ApiName" / WString
    )


@declare(guid=guid("dea07764-0790-44de-b9c4-49677b17174f"), event_id=40010, version=0)
class Microsoft_Windows_FMS_40010_0(Etw):
    pattern = Struct(
        "ApiName" / WString
    )


@declare(guid=guid("dea07764-0790-44de-b9c4-49677b17174f"), event_id=40011, version=0)
class Microsoft_Windows_FMS_40011_0(Etw):
    pattern = Struct(
        "ApiName" / WString
    )

