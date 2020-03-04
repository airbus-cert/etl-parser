# -*- coding: utf-8 -*-
"""
Microsoft-Windows-EapMethods-Ttls
GUID : d710d46c-235d-4798-ac20-9f83e1dcd557
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("d710d46c-235d-4798-ac20-9f83e1dcd557"), event_id=204, version=0)
class Microsoft_Windows_EapMethods_Ttls_204_0(Etw):
    pattern = Struct(
        "CAThumbprint" / WString,
        "ServerName" / WString
    )

