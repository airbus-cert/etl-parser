# -*- coding: utf-8 -*-
"""
Microsoft-Windows-EDP-Audit-Regular
GUID : 50f99b2d-96d2-421f-be4c-222c4140da9f
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("50f99b2d-96d2-421f-be4c-222c4140da9f"), event_id=201, version=0)
class Microsoft_Windows_EDP_Audit_Regular_201_0(Etw):
    pattern = Struct(
        "UserId" / Sid,
        "Policy" / WString,
        "Justification" / WString,
        "SourceEnterpriseId" / WString,
        "SourceAppName" / WString,
        "DestinationEnterpriseId" / WString,
        "DestinationAppName" / WString,
        "DataInfo" / WString
    )


@declare(guid=guid("50f99b2d-96d2-421f-be4c-222c4140da9f"), event_id=301, version=0)
class Microsoft_Windows_EDP_Audit_Regular_301_0(Etw):
    pattern = Struct(
        "UserId" / Sid,
        "Policy" / WString,
        "Object" / WString,
        "Action" / Int32ul,
        "SourceName" / WString,
        "SourceEnterpriseId" / WString,
        "DestinationName" / WString,
        "DestinationEnterpriseId" / WString,
        "ApplicationName" / WString
    )

