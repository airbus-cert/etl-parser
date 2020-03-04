# -*- coding: utf-8 -*-
"""
Microsoft-Windows-CertificationAuthorityClient-CertCli
GUID : 98bf1cd3-583e-4926-95ee-a61bf3f46470
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("98bf1cd3-583e-4926-95ee-a61bf3f46470"), event_id=10000, version=0)
class Microsoft_Windows_CertificationAuthorityClient_CertCli_10000_0(Etw):
    pattern = Struct(
        "ServerURL" / WString,
        "FaultString" / WString
    )

