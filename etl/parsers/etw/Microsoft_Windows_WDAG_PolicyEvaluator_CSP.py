# -*- coding: utf-8 -*-
"""
Microsoft-Windows-WDAG-PolicyEvaluator-CSP
GUID : 64a98c25-9e00-404e-84ad-6700dfe02529
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("64a98c25-9e00-404e-84ad-6700dfe02529"), event_id=300, version=0)
class Microsoft_Windows_WDAG_PolicyEvaluator_CSP_300_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("64a98c25-9e00-404e-84ad-6700dfe02529"), event_id=301, version=0)
class Microsoft_Windows_WDAG_PolicyEvaluator_CSP_301_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("64a98c25-9e00-404e-84ad-6700dfe02529"), event_id=302, version=0)
class Microsoft_Windows_WDAG_PolicyEvaluator_CSP_302_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("64a98c25-9e00-404e-84ad-6700dfe02529"), event_id=350, version=0)
class Microsoft_Windows_WDAG_PolicyEvaluator_CSP_350_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("64a98c25-9e00-404e-84ad-6700dfe02529"), event_id=351, version=0)
class Microsoft_Windows_WDAG_PolicyEvaluator_CSP_351_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("64a98c25-9e00-404e-84ad-6700dfe02529"), event_id=352, version=0)
class Microsoft_Windows_WDAG_PolicyEvaluator_CSP_352_0(Etw):
    pattern = Struct(
        "MissingPolicy" / WString
    )


@declare(guid=guid("64a98c25-9e00-404e-84ad-6700dfe02529"), event_id=353, version=0)
class Microsoft_Windows_WDAG_PolicyEvaluator_CSP_353_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("64a98c25-9e00-404e-84ad-6700dfe02529"), event_id=355, version=0)
class Microsoft_Windows_WDAG_PolicyEvaluator_CSP_355_0(Etw):
    pattern = Struct(
        "MissingPolicy" / WString
    )


@declare(guid=guid("64a98c25-9e00-404e-84ad-6700dfe02529"), event_id=356, version=0)
class Microsoft_Windows_WDAG_PolicyEvaluator_CSP_356_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "SecondMessage" / WString
    )

