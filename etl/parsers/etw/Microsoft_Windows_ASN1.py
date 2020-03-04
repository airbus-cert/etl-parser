# -*- coding: utf-8 -*-
"""
Microsoft-Windows-ASN1
GUID : d92ef8ac-99dd-4ab8-b91d-c6eba85f3755
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("d92ef8ac-99dd-4ab8-b91d-c6eba85f3755"), event_id=1, version=0)
class Microsoft_Windows_ASN1_1_0(Etw):
    pattern = Struct(
        "Module" / WString,
        "PDU" / Int32ul,
        "Object" / CString,
        "Status" / Int32ul,
        "TotalEncodedLength" / Int32ul,
        "EncodedLength" / Int32ul,
        "Encoded" / Bytes(lambda this: this.EncodedLength)
    )

