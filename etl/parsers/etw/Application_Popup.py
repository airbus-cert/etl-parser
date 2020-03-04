# -*- coding: utf-8 -*-
"""
Application Popup
GUID : 47bfa2b7-bd54-4fac-b70b-29021084ca8f
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("47bfa2b7-bd54-4fac-b70b-29021084ca8f"), event_id=26, version=0)
class Application_Popup_26_0(Etw):
    pattern = Struct(
        "Caption" / WString,
        "Message" / WString
    )

