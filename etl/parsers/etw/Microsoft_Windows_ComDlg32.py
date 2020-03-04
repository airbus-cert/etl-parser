# -*- coding: utf-8 -*-
"""
Microsoft-Windows-ComDlg32
GUID : 7f912b92-21ad-496e-b97a-88622a72bc42
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("7f912b92-21ad-496e-b97a-88622a72bc42"), event_id=40120, version=0)
class Microsoft_Windows_ComDlg32_40120_0(Etw):
    pattern = Struct(
        "FamiliesAdded" / Int32ul
    )

