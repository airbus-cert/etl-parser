# -*- coding: utf-8 -*-
"""
Microsoft-Windows-EDP-Audit-TCB
GUID : 287d59b6-79ba-4741-a08b-2fedeede6435
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("287d59b6-79ba-4741-a08b-2fedeede6435"), event_id=101, version=0)
class Microsoft_Windows_EDP_Audit_TCB_101_0(Etw):
    pattern = Struct(
        "UserId" / Sid,
        "Policy" / WString,
        "Justification" / WString,
        "PreviousEnterpriseId" / WString,
        "FilePath" / WString
    )

