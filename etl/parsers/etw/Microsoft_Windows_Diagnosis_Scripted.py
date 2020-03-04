# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Diagnosis-Scripted
GUID : e1dd7e52-621d-44e3-a1ad-0370c2b25946
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("e1dd7e52-621d-44e3-a1ad-0370c2b25946"), event_id=1, version=0)
class Microsoft_Windows_Diagnosis_Scripted_1_0(Etw):
    pattern = Struct(
        "PackagePath" / WString,
        "PackageId" / WString
    )


@declare(guid=guid("e1dd7e52-621d-44e3-a1ad-0370c2b25946"), event_id=101, version=0)
class Microsoft_Windows_Diagnosis_Scripted_101_0(Etw):
    pattern = Struct(
        "PackagePath" / WString
    )


@declare(guid=guid("e1dd7e52-621d-44e3-a1ad-0370c2b25946"), event_id=102, version=0)
class Microsoft_Windows_Diagnosis_Scripted_102_0(Etw):
    pattern = Struct(
        "PackagePath" / WString
    )


@declare(guid=guid("e1dd7e52-621d-44e3-a1ad-0370c2b25946"), event_id=103, version=0)
class Microsoft_Windows_Diagnosis_Scripted_103_0(Etw):
    pattern = Struct(
        "PackageId" / WString
    )


@declare(guid=guid("e1dd7e52-621d-44e3-a1ad-0370c2b25946"), event_id=104, version=0)
class Microsoft_Windows_Diagnosis_Scripted_104_0(Etw):
    pattern = Struct(
        "PackageId" / WString
    )


@declare(guid=guid("e1dd7e52-621d-44e3-a1ad-0370c2b25946"), event_id=105, version=0)
class Microsoft_Windows_Diagnosis_Scripted_105_0(Etw):
    pattern = Struct(
        "PackageId" / WString,
        "ResolutionId" / WString
    )


@declare(guid=guid("e1dd7e52-621d-44e3-a1ad-0370c2b25946"), event_id=106, version=0)
class Microsoft_Windows_Diagnosis_Scripted_106_0(Etw):
    pattern = Struct(
        "PackageId" / WString,
        "ResolutionId" / WString
    )


@declare(guid=guid("e1dd7e52-621d-44e3-a1ad-0370c2b25946"), event_id=107, version=0)
class Microsoft_Windows_Diagnosis_Scripted_107_0(Etw):
    pattern = Struct(
        "PackageId" / WString
    )


@declare(guid=guid("e1dd7e52-621d-44e3-a1ad-0370c2b25946"), event_id=108, version=0)
class Microsoft_Windows_Diagnosis_Scripted_108_0(Etw):
    pattern = Struct(
        "PackageId" / WString
    )


@declare(guid=guid("e1dd7e52-621d-44e3-a1ad-0370c2b25946"), event_id=201, version=0)
class Microsoft_Windows_Diagnosis_Scripted_201_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("e1dd7e52-621d-44e3-a1ad-0370c2b25946"), event_id=301, version=0)
class Microsoft_Windows_Diagnosis_Scripted_301_0(Etw):
    pattern = Struct(
        "FunctionName" / WString,
        "LineNumber" / Int32sl,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("e1dd7e52-621d-44e3-a1ad-0370c2b25946"), event_id=401, version=0)
class Microsoft_Windows_Diagnosis_Scripted_401_0(Etw):
    pattern = Struct(
        "PackageId" / WString,
        "RootCauseId" / WString
    )


@declare(guid=guid("e1dd7e52-621d-44e3-a1ad-0370c2b25946"), event_id=402, version=0)
class Microsoft_Windows_Diagnosis_Scripted_402_0(Etw):
    pattern = Struct(
        "PackageId" / WString,
        "RootCauseId" / WString
    )

