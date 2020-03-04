# -*- coding: utf-8 -*-
"""
Microsoft-Windows-IdCtrls
GUID : 6d7662a9-034e-4b1f-a167-67819c401632
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("6d7662a9-034e-4b1f-a167-67819c401632"), event_id=5001, version=0)
class Microsoft_Windows_IdCtrls_5001_0(Etw):
    pattern = Struct(
        "URL" / WString
    )


@declare(guid=guid("6d7662a9-034e-4b1f-a167-67819c401632"), event_id=5002, version=0)
class Microsoft_Windows_IdCtrls_5002_0(Etw):
    pattern = Struct(
        "URL" / WString
    )


@declare(guid=guid("6d7662a9-034e-4b1f-a167-67819c401632"), event_id=5003, version=0)
class Microsoft_Windows_IdCtrls_5003_0(Etw):
    pattern = Struct(
        "URL" / WString,
        "TargetFrameName" / WString,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("6d7662a9-034e-4b1f-a167-67819c401632"), event_id=5004, version=0)
class Microsoft_Windows_IdCtrls_5004_0(Etw):
    pattern = Struct(
        "URL" / WString,
        "ReferrerUrl" / WString,
        "Flags" / Int32ul
    )


@declare(guid=guid("6d7662a9-034e-4b1f-a167-67819c401632"), event_id=5005, version=0)
class Microsoft_Windows_IdCtrls_5005_0(Etw):
    pattern = Struct(
        "WizardID" / Int32ul,
        "URL" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("6d7662a9-034e-4b1f-a167-67819c401632"), event_id=5006, version=0)
class Microsoft_Windows_IdCtrls_5006_0(Etw):
    pattern = Struct(
        "Method" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("6d7662a9-034e-4b1f-a167-67819c401632"), event_id=5007, version=0)
class Microsoft_Windows_IdCtrls_5007_0(Etw):
    pattern = Struct(
        "Method" / WString,
        "String" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("6d7662a9-034e-4b1f-a167-67819c401632"), event_id=5008, version=0)
class Microsoft_Windows_IdCtrls_5008_0(Etw):
    pattern = Struct(
        "DISPID" / Int32ul,
        "ArgErr" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("6d7662a9-034e-4b1f-a167-67819c401632"), event_id=5009, version=0)
class Microsoft_Windows_IdCtrls_5009_0(Etw):
    pattern = Struct(
        "SecurityProblem" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("6d7662a9-034e-4b1f-a167-67819c401632"), event_id=5010, version=0)
class Microsoft_Windows_IdCtrls_5010_0(Etw):
    pattern = Struct(
        "WizardID" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("6d7662a9-034e-4b1f-a167-67819c401632"), event_id=5011, version=0)
class Microsoft_Windows_IdCtrls_5011_0(Etw):
    pattern = Struct(
        "URL" / WString,
        "Action" / Int32ul,
        "Policy" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("6d7662a9-034e-4b1f-a167-67819c401632"), event_id=5012, version=0)
class Microsoft_Windows_IdCtrls_5012_0(Etw):
    pattern = Struct(
        "CLSID" / Guid,
        "URL" / WString
    )


@declare(guid=guid("6d7662a9-034e-4b1f-a167-67819c401632"), event_id=5013, version=0)
class Microsoft_Windows_IdCtrls_5013_0(Etw):
    pattern = Struct(
        "CLSID" / Guid,
        "URL" / WString
    )


@declare(guid=guid("6d7662a9-034e-4b1f-a167-67819c401632"), event_id=5014, version=0)
class Microsoft_Windows_IdCtrls_5014_0(Etw):
    pattern = Struct(
        "CLSID" / Guid,
        "URL" / WString
    )


@declare(guid=guid("6d7662a9-034e-4b1f-a167-67819c401632"), event_id=5015, version=0)
class Microsoft_Windows_IdCtrls_5015_0(Etw):
    pattern = Struct(
        "CLSID" / Guid,
        "URL" / WString
    )


@declare(guid=guid("6d7662a9-034e-4b1f-a167-67819c401632"), event_id=5016, version=0)
class Microsoft_Windows_IdCtrls_5016_0(Etw):
    pattern = Struct(
        "CLSID" / Guid,
        "URL" / WString
    )


@declare(guid=guid("6d7662a9-034e-4b1f-a167-67819c401632"), event_id=5017, version=0)
class Microsoft_Windows_IdCtrls_5017_0(Etw):
    pattern = Struct(
        "URL" / WString
    )


@declare(guid=guid("6d7662a9-034e-4b1f-a167-67819c401632"), event_id=5018, version=0)
class Microsoft_Windows_IdCtrls_5018_0(Etw):
    pattern = Struct(
        "URL" / WString
    )


@declare(guid=guid("6d7662a9-034e-4b1f-a167-67819c401632"), event_id=5019, version=0)
class Microsoft_Windows_IdCtrls_5019_0(Etw):
    pattern = Struct(
        "URL" / WString
    )


@declare(guid=guid("6d7662a9-034e-4b1f-a167-67819c401632"), event_id=5020, version=0)
class Microsoft_Windows_IdCtrls_5020_0(Etw):
    pattern = Struct(
        "URL" / WString
    )


@declare(guid=guid("6d7662a9-034e-4b1f-a167-67819c401632"), event_id=5021, version=0)
class Microsoft_Windows_IdCtrls_5021_0(Etw):
    pattern = Struct(
        "cx" / Int32ul,
        "cy" / Int32ul
    )


@declare(guid=guid("6d7662a9-034e-4b1f-a167-67819c401632"), event_id=5022, version=0)
class Microsoft_Windows_IdCtrls_5022_0(Etw):
    pattern = Struct(
        "Method" / WString
    )


@declare(guid=guid("6d7662a9-034e-4b1f-a167-67819c401632"), event_id=5023, version=0)
class Microsoft_Windows_IdCtrls_5023_0(Etw):
    pattern = Struct(
        "Method" / WString,
        "String" / WString
    )


@declare(guid=guid("6d7662a9-034e-4b1f-a167-67819c401632"), event_id=5024, version=0)
class Microsoft_Windows_IdCtrls_5024_0(Etw):
    pattern = Struct(
        "Method" / WString,
        "String" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("6d7662a9-034e-4b1f-a167-67819c401632"), event_id=5027, version=0)
class Microsoft_Windows_IdCtrls_5027_0(Etw):
    pattern = Struct(
        "Method" / WString,
        "String" / WString,
        "ExtendedString" / WString,
        "HRESULT" / Int32ul
    )

