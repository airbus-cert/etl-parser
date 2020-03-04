# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Management-SecureAssessment
GUID : a329cf81-57ec-46ed-ab7c-261a52b0754a
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("a329cf81-57ec-46ed-ab7c-261a52b0754a"), event_id=100, version=0)
class Microsoft_Windows_Management_SecureAssessment_100_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Function" / CString,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("a329cf81-57ec-46ed-ab7c-261a52b0754a"), event_id=101, version=0)
class Microsoft_Windows_Management_SecureAssessment_101_0(Etw):
    pattern = Struct(
        "ProcessName" / WString,
        "TerminationResult" / Int8ul
    )


@declare(guid=guid("a329cf81-57ec-46ed-ab7c-261a52b0754a"), event_id=200, version=0)
class Microsoft_Windows_Management_SecureAssessment_200_0(Etw):
    pattern = Struct(
        "Enable" / Int8ul,
        "CurrentlyEnabled" / Int8ul
    )


@declare(guid=guid("a329cf81-57ec-46ed-ab7c-261a52b0754a"), event_id=201, version=0)
class Microsoft_Windows_Management_SecureAssessment_201_0(Etw):
    pattern = Struct(
        "NewContextCreated" / Int8ul
    )


@declare(guid=guid("a329cf81-57ec-46ed-ab7c-261a52b0754a"), event_id=202, version=0)
class Microsoft_Windows_Management_SecureAssessment_202_0(Etw):
    pattern = Struct(
        "EnrollmentID" / WString
    )


@declare(guid=guid("a329cf81-57ec-46ed-ab7c-261a52b0754a"), event_id=203, version=0)
class Microsoft_Windows_Management_SecureAssessment_203_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("a329cf81-57ec-46ed-ab7c-261a52b0754a"), event_id=204, version=0)
class Microsoft_Windows_Management_SecureAssessment_204_0(Etw):
    pattern = Struct(
        "EnrollmentID" / WString
    )


@declare(guid=guid("a329cf81-57ec-46ed-ab7c-261a52b0754a"), event_id=205, version=0)
class Microsoft_Windows_Management_SecureAssessment_205_0(Etw):
    pattern = Struct(
        "EnrollmentID" / WString,
        "CallerID" / WString
    )


@declare(guid=guid("a329cf81-57ec-46ed-ab7c-261a52b0754a"), event_id=206, version=0)
class Microsoft_Windows_Management_SecureAssessment_206_0(Etw):
    pattern = Struct(
        "Enable" / Int8ul
    )


@declare(guid=guid("a329cf81-57ec-46ed-ab7c-261a52b0754a"), event_id=208, version=0)
class Microsoft_Windows_Management_SecureAssessment_208_0(Etw):
    pattern = Struct(
        "EnrollmentID" / WString
    )

