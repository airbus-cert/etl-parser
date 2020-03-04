# -*- coding: utf-8 -*-
"""
Microsoft-Windows-WCN-Config-Registrar-Secure
GUID : c100becc-d33a-4a4b-bf23-bbef4663d017
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("c100becc-d33a-4a4b-bf23-bbef4663d017"), event_id=9000, version=0)
class Microsoft_Windows_WCN_Config_Registrar_Secure_9000_0(Etw):
    pattern = Struct(
        "MessageGuid" / Guid,
        "MessageBlobLength" / Int16ul,
        "MessageBlob" / Bytes(lambda this: this.MessageBlobLength)
    )

