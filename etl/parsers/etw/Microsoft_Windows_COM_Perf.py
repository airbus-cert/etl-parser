# -*- coding: utf-8 -*-
"""
Microsoft-Windows-COM-Perf
GUID : b8d6861b-d20f-4eec-bbae-87e0dd80602b
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("b8d6861b-d20f-4eec-bbae-87e0dd80602b"), event_id=13, version=0)
class Microsoft_Windows_COM_Perf_13_0(Etw):
    pattern = Struct(
        "ContractId" / WString,
        "PackageId" / WString,
        "ActivatableClassId" / WString
    )


@declare(guid=guid("b8d6861b-d20f-4eec-bbae-87e0dd80602b"), event_id=14, version=0)
class Microsoft_Windows_COM_Perf_14_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32sl,
        "ContractId" / WString,
        "PackageId" / WString,
        "ActivatableClassId" / WString,
        "InboxAppsRegistrationScope" / Int8ul
    )


@declare(guid=guid("b8d6861b-d20f-4eec-bbae-87e0dd80602b"), event_id=15, version=0)
class Microsoft_Windows_COM_Perf_15_0(Etw):
    pattern = Struct(
        "ContractId" / WString,
        "ExtensionId" / WString
    )


@declare(guid=guid("b8d6861b-d20f-4eec-bbae-87e0dd80602b"), event_id=16, version=0)
class Microsoft_Windows_COM_Perf_16_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32sl,
        "ContractId" / WString,
        "ExtensionId" / WString,
        "InboxAppsRegistrationScope" / Int8ul
    )


@declare(guid=guid("b8d6861b-d20f-4eec-bbae-87e0dd80602b"), event_id=17, version=0)
class Microsoft_Windows_COM_Perf_17_0(Etw):
    pattern = Struct(
        "ContractId" / WString
    )


@declare(guid=guid("b8d6861b-d20f-4eec-bbae-87e0dd80602b"), event_id=18, version=0)
class Microsoft_Windows_COM_Perf_18_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32sl,
        "ContractId" / WString
    )


@declare(guid=guid("b8d6861b-d20f-4eec-bbae-87e0dd80602b"), event_id=19, version=0)
class Microsoft_Windows_COM_Perf_19_0(Etw):
    pattern = Struct(
        "ContractId" / WString,
        "PackageFamilyName" / WString
    )


@declare(guid=guid("b8d6861b-d20f-4eec-bbae-87e0dd80602b"), event_id=20, version=0)
class Microsoft_Windows_COM_Perf_20_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32sl,
        "ContractId" / WString,
        "PackageFamilyName" / WString
    )


@declare(guid=guid("b8d6861b-d20f-4eec-bbae-87e0dd80602b"), event_id=21, version=0)
class Microsoft_Windows_COM_Perf_21_0(Etw):
    pattern = Struct(
        "CustomPropertyKey" / WString
    )


@declare(guid=guid("b8d6861b-d20f-4eec-bbae-87e0dd80602b"), event_id=22, version=0)
class Microsoft_Windows_COM_Perf_22_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32sl,
        "CustomPropertyKey" / WString
    )


@declare(guid=guid("b8d6861b-d20f-4eec-bbae-87e0dd80602b"), event_id=23, version=0)
class Microsoft_Windows_COM_Perf_23_0(Etw):
    pattern = Struct(
        "ContractId" / WString
    )


@declare(guid=guid("b8d6861b-d20f-4eec-bbae-87e0dd80602b"), event_id=24, version=0)
class Microsoft_Windows_COM_Perf_24_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32sl,
        "ContractId" / WString,
        "PackageId" / WString,
        "ActivatableClassId" / WString,
        "InboxAppsRegistrationScope" / Int8ul
    )


@declare(guid=guid("b8d6861b-d20f-4eec-bbae-87e0dd80602b"), event_id=39, version=1)
class Microsoft_Windows_COM_Perf_39_1(Etw):
    pattern = Struct(
        "CallTraceId" / Int32ul,
        "TargetProcessId" / Int32ul,
        "TargetThreadId" / Int32ul,
        "CausalityId" / Guid,
        "TargetMethod" / Int32ul,
        "TargetInterface" / Guid,
        "ProxyInterfacePointer" / Int64ul,
        "ProxyManagerIUnknown" / Int64ul,
        "IPID" / Guid,
        "OID" / Int64ul,
        "CallerLogicalThreadId" / Guid,
        "CallerReturnAddress" / Int64ul,
        "WinrtAsyncPatternMethodIndicator" / Int32ul,
        "FakeSync" / Int8ul
    )


@declare(guid=guid("b8d6861b-d20f-4eec-bbae-87e0dd80602b"), event_id=40, version=0)
class Microsoft_Windows_COM_Perf_40_0(Etw):
    pattern = Struct(
        "CallTraceId" / Int32ul,
        "HRESULT" / Int32sl,
        "SourceOfHRESULT" / Int32ul
    )


@declare(guid=guid("b8d6861b-d20f-4eec-bbae-87e0dd80602b"), event_id=41, version=1)
class Microsoft_Windows_COM_Perf_41_1(Etw):
    pattern = Struct(
        "CallTraceId" / Int32ul,
        "TargetProcessId" / Int32ul,
        "TargetThreadId" / Int32ul,
        "CausalityId" / Guid,
        "TargetMethod" / Int32ul,
        "TargetInterface" / Guid,
        "TargetInterfaceAsyncUuid" / Guid,
        "ProxyInterfacePointer" / Int64ul,
        "ProxyManagerIUnknown" / Int64ul,
        "IPID" / Guid,
        "OID" / Int64ul,
        "CallerLogicalThreadId" / Guid,
        "CallerReturnAddress" / Int64ul
    )


@declare(guid=guid("b8d6861b-d20f-4eec-bbae-87e0dd80602b"), event_id=42, version=0)
class Microsoft_Windows_COM_Perf_42_0(Etw):
    pattern = Struct(
        "CallTraceId" / Int32ul,
        "HRESULT" / Int32sl,
        "SourceOfHRESULT" / Int32ul
    )


@declare(guid=guid("b8d6861b-d20f-4eec-bbae-87e0dd80602b"), event_id=43, version=2)
class Microsoft_Windows_COM_Perf_43_2(Etw):
    pattern = Struct(
        "CallTraceId" / Int32ul,
        "SourceProcessId" / Int32ul,
        "SourceThreadId" / Int32ul,
        "CausalityId" / Guid,
        "TargetMethod" / Int32ul,
        "TargetInterface" / Guid,
        "InterfacePointer" / Int64ul,
        "MethodAddress" / Int64ul,
        "ServerIUnknown" / Int64ul,
        "IPID" / Guid,
        "OID" / Int64ul,
        "WinrtAsyncPatternMethodIndicator" / Int32ul
    )


@declare(guid=guid("b8d6861b-d20f-4eec-bbae-87e0dd80602b"), event_id=44, version=0)
class Microsoft_Windows_COM_Perf_44_0(Etw):
    pattern = Struct(
        "CallTraceId" / Int32ul,
        "HRESULT" / Int32sl,
        "ServerException" / Int32ul
    )


@declare(guid=guid("b8d6861b-d20f-4eec-bbae-87e0dd80602b"), event_id=45, version=1)
class Microsoft_Windows_COM_Perf_45_1(Etw):
    pattern = Struct(
        "CallTraceId" / Int32ul,
        "SourceProcessId" / Int32ul,
        "SourceThreadId" / Int32ul,
        "CausalityId" / Guid,
        "TargetMethod" / Int32ul,
        "TargetInterface" / Guid,
        "TargetInterfaceAsyncUuid" / Guid,
        "InterfacePointer" / Int64ul,
        "MethodAddress" / Int64ul,
        "ServerIUnknown" / Int64ul,
        "IPID" / Guid,
        "OID" / Int64ul
    )


@declare(guid=guid("b8d6861b-d20f-4eec-bbae-87e0dd80602b"), event_id=46, version=0)
class Microsoft_Windows_COM_Perf_46_0(Etw):
    pattern = Struct(
        "CallTraceId" / Int32ul,
        "HRESULT" / Int32sl,
        "ServerException" / Int32ul
    )


@declare(guid=guid("b8d6861b-d20f-4eec-bbae-87e0dd80602b"), event_id=47, version=0)
class Microsoft_Windows_COM_Perf_47_0(Etw):
    pattern = Struct(
        "ApartmentId64" / Int64ul,
        "AptId" / Int32ul,
        "AptKind" / Int8ul,
        "UnloadDelay" / Int32ul
    )


@declare(guid=guid("b8d6861b-d20f-4eec-bbae-87e0dd80602b"), event_id=48, version=0)
class Microsoft_Windows_COM_Perf_48_0(Etw):
    pattern = Struct(
        "ApartmentId64" / Int64ul,
        "AptId" / Int32ul,
        "AptKind" / Int8ul
    )


@declare(guid=guid("b8d6861b-d20f-4eec-bbae-87e0dd80602b"), event_id=49, version=0)
class Microsoft_Windows_COM_Perf_49_0(Etw):
    pattern = Struct(
        "ApartmentId64" / Int64ul,
        "AptId" / Int32ul,
        "AptKind" / Int8ul
    )


@declare(guid=guid("b8d6861b-d20f-4eec-bbae-87e0dd80602b"), event_id=54, version=0)
class Microsoft_Windows_COM_Perf_54_0(Etw):
    pattern = Struct(
        "ContractId" / WString,
        "PackageId" / WString
    )


@declare(guid=guid("b8d6861b-d20f-4eec-bbae-87e0dd80602b"), event_id=55, version=0)
class Microsoft_Windows_COM_Perf_55_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32sl,
        "ContractId" / WString,
        "PackageId" / WString,
        "ActivatableClassId" / WString,
        "InboxAppsRegistrationScope" / Int8ul
    )

