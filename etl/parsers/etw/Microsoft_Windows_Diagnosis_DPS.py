# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Diagnosis-DPS
GUID : 6bba3851-2c7e-4dea-8f54-31e5afd029e3
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("6bba3851-2c7e-4dea-8f54-31e5afd029e3"), event_id=5, version=0)
class Microsoft_Windows_Diagnosis_DPS_5_0(Etw):
    pattern = Struct(
        "ScenarioId" / Guid
    )


@declare(guid=guid("6bba3851-2c7e-4dea-8f54-31e5afd029e3"), event_id=100, version=0)
class Microsoft_Windows_Diagnosis_DPS_100_0(Etw):
    pattern = Struct(
        "ScenarioId" / Guid,
        "InstanceId" / Guid,
        "OriginalActivityId" / Guid,
        "DiagnosticModuleImageName" / WString,
        "DiagnosticModuleId" / Guid
    )


@declare(guid=guid("6bba3851-2c7e-4dea-8f54-31e5afd029e3"), event_id=105, version=0)
class Microsoft_Windows_Diagnosis_DPS_105_0(Etw):
    pattern = Struct(
        "ScenarioId" / Guid,
        "InstanceId" / Guid,
        "OriginalActivityId" / Guid,
        "DiagnosticModuleImageName" / WString,
        "DiagnosticModuleId" / Guid
    )


@declare(guid=guid("6bba3851-2c7e-4dea-8f54-31e5afd029e3"), event_id=110, version=0)
class Microsoft_Windows_Diagnosis_DPS_110_0(Etw):
    pattern = Struct(
        "ScenarioId" / Guid,
        "InstanceId" / Guid,
        "OriginalActivityId" / Guid,
        "DiagnosticModuleImageName" / WString,
        "DiagnosticModuleId" / Guid
    )


@declare(guid=guid("6bba3851-2c7e-4dea-8f54-31e5afd029e3"), event_id=115, version=0)
class Microsoft_Windows_Diagnosis_DPS_115_0(Etw):
    pattern = Struct(
        "ScenarioId" / Guid,
        "InstanceId" / Guid,
        "OriginalActivityId" / Guid,
        "DiagnosticModuleImageName" / WString,
        "ResolutionId" / Guid,
        "ResolutionSID" / Sid,
        "ResolutionSessionId" / Int32ul,
        "ResolutionExpirationDate" / Int64ul,
        "DiagnosticModuleId" / Guid
    )


@declare(guid=guid("6bba3851-2c7e-4dea-8f54-31e5afd029e3"), event_id=120, version=0)
class Microsoft_Windows_Diagnosis_DPS_120_0(Etw):
    pattern = Struct(
        "ScenarioId" / Guid,
        "InstanceId" / Guid,
        "OriginalActivityId" / Guid,
        "DiagnosticModuleImageName" / WString,
        "ResolutionId" / Guid,
        "ResolutionSID" / Sid,
        "ResolutionSessionId" / Int32ul,
        "ResolutionExpirationDate" / Int64ul,
        "DiagnosticModuleId" / Guid
    )


@declare(guid=guid("6bba3851-2c7e-4dea-8f54-31e5afd029e3"), event_id=125, version=0)
class Microsoft_Windows_Diagnosis_DPS_125_0(Etw):
    pattern = Struct(
        "ScenarioId" / Guid,
        "InstanceId" / Guid,
        "OriginalActivityId" / Guid,
        "DiagnosticModuleImageName" / WString,
        "DiagnosticModuleId" / Guid
    )


@declare(guid=guid("6bba3851-2c7e-4dea-8f54-31e5afd029e3"), event_id=126, version=0)
class Microsoft_Windows_Diagnosis_DPS_126_0(Etw):
    pattern = Struct(
        "ScenarioId" / Guid,
        "InstanceId" / Guid,
        "OriginalActivityId" / Guid,
        "DiagnosticModuleImageName" / WString,
        "DiagnosticModuleId" / Guid
    )


@declare(guid=guid("6bba3851-2c7e-4dea-8f54-31e5afd029e3"), event_id=130, version=0)
class Microsoft_Windows_Diagnosis_DPS_130_0(Etw):
    pattern = Struct(
        "ScenarioId" / Guid,
        "InstanceId" / Guid,
        "OriginalActivityId" / Guid,
        "DiagnosticModuleImageName" / WString,
        "DiagnosticModuleId" / Guid
    )


@declare(guid=guid("6bba3851-2c7e-4dea-8f54-31e5afd029e3"), event_id=135, version=0)
class Microsoft_Windows_Diagnosis_DPS_135_0(Etw):
    pattern = Struct(
        "ScenarioId" / Guid,
        "InstanceId" / Guid,
        "OriginalActivityId" / Guid,
        "StatusCode" / Int32ul,
        "DiagnosticModuleImageName" / WString,
        "DiagnosticModuleId" / Guid
    )


@declare(guid=guid("6bba3851-2c7e-4dea-8f54-31e5afd029e3"), event_id=140, version=0)
class Microsoft_Windows_Diagnosis_DPS_140_0(Etw):
    pattern = Struct(
        "FileName" / WString,
        "FunctionName" / WString,
        "LineNumber" / Int32sl,
        "ErrorMessage" / WString
    )


@declare(guid=guid("6bba3851-2c7e-4dea-8f54-31e5afd029e3"), event_id=165, version=0)
class Microsoft_Windows_Diagnosis_DPS_165_0(Etw):
    pattern = Struct(
        "ScenarioId" / Guid,
        "InstanceId" / Guid,
        "OriginalActivityId" / Guid,
        "StatusCode" / Int32ul,
        "DiagnosticModuleImageName" / WString,
        "DiagnosticModuleId" / Guid
    )


@declare(guid=guid("6bba3851-2c7e-4dea-8f54-31e5afd029e3"), event_id=170, version=0)
class Microsoft_Windows_Diagnosis_DPS_170_0(Etw):
    pattern = Struct(
        "ScenarioId" / Guid,
        "InstanceId" / Guid,
        "OriginalActivityId" / Guid,
        "DiagnosticModuleImageName" / WString,
        "StatusCode" / Int32sl,
        "DiagnosticModuleId" / Guid
    )


@declare(guid=guid("6bba3851-2c7e-4dea-8f54-31e5afd029e3"), event_id=175, version=0)
class Microsoft_Windows_Diagnosis_DPS_175_0(Etw):
    pattern = Struct(
        "ScenarioId" / Guid,
        "InstanceId" / Guid,
        "OriginalActivityId" / Guid,
        "DiagnosticModuleImageName" / WString,
        "StatusCode" / Int32sl,
        "DiagnosticModuleId" / Guid
    )


@declare(guid=guid("6bba3851-2c7e-4dea-8f54-31e5afd029e3"), event_id=185, version=0)
class Microsoft_Windows_Diagnosis_DPS_185_0(Etw):
    pattern = Struct(
        "DiagnosticModuleImageName" / WString,
        "DiagnosticModuleId" / Guid,
        "StatusCode" / Int32sl
    )


@declare(guid=guid("6bba3851-2c7e-4dea-8f54-31e5afd029e3"), event_id=5016, version=0)
class Microsoft_Windows_Diagnosis_DPS_5016_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "Line" / Int32ul,
        "Address" / Int64ul,
        "Size" / Int64ul
    )


@declare(guid=guid("6bba3851-2c7e-4dea-8f54-31e5afd029e3"), event_id=5017, version=0)
class Microsoft_Windows_Diagnosis_DPS_5017_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "Line" / Int32ul,
        "Address" / Int64ul
    )

