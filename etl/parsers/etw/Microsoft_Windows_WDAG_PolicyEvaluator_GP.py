# -*- coding: utf-8 -*-
"""
Microsoft-Windows-WDAG-PolicyEvaluator-GP
GUID : e53df8ba-367a-4406-98d5-709ffb169681
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("e53df8ba-367a-4406-98d5-709ffb169681"), event_id=350, version=0)
class Microsoft_Windows_WDAG_PolicyEvaluator_GP_350_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("e53df8ba-367a-4406-98d5-709ffb169681"), event_id=351, version=0)
class Microsoft_Windows_WDAG_PolicyEvaluator_GP_351_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("e53df8ba-367a-4406-98d5-709ffb169681"), event_id=352, version=0)
class Microsoft_Windows_WDAG_PolicyEvaluator_GP_352_0(Etw):
    pattern = Struct(
        "MissingPolicy" / WString
    )


@declare(guid=guid("e53df8ba-367a-4406-98d5-709ffb169681"), event_id=353, version=0)
class Microsoft_Windows_WDAG_PolicyEvaluator_GP_353_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("e53df8ba-367a-4406-98d5-709ffb169681"), event_id=355, version=0)
class Microsoft_Windows_WDAG_PolicyEvaluator_GP_355_0(Etw):
    pattern = Struct(
        "MissingPolicy" / WString
    )


@declare(guid=guid("e53df8ba-367a-4406-98d5-709ffb169681"), event_id=356, version=0)
class Microsoft_Windows_WDAG_PolicyEvaluator_GP_356_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "SecondMessage" / WString
    )

