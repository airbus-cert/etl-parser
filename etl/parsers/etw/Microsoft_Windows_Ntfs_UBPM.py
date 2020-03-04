# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Ntfs-UBPM
GUID : 8e6a5303-a4ce-498f-afdb-e03a8a82b077
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("8e6a5303-a4ce-498f-afdb-e03a8a82b077"), event_id=0, version=0)
class Microsoft_Windows_Ntfs_UBPM_0_0(Etw):
    pattern = Struct(
        "SvSvcCmd" / WString
    )

