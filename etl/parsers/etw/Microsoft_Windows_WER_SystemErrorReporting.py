# -*- coding: utf-8 -*-
"""
Microsoft-Windows-WER-SystemErrorReporting
GUID : abce23e7-de45-4366-8631-84fa6c525952
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("abce23e7-de45-4366-8631-84fa6c525952"), event_id=1000, version=0)
class Microsoft_Windows_WER_SystemErrorReporting_1000_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("abce23e7-de45-4366-8631-84fa6c525952"), event_id=1001, version=0)
class Microsoft_Windows_WER_SystemErrorReporting_1001_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )


@declare(guid=guid("abce23e7-de45-4366-8631-84fa6c525952"), event_id=1018, version=0)
class Microsoft_Windows_WER_SystemErrorReporting_1018_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString
    )

