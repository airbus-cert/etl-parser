# -*- coding: utf-8 -*-
"""
Microsoft-Windows-D3D10Level9
GUID : 7e7d3382-023c-43cb-95d2-6f0ca6d70381
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("7e7d3382-023c-43cb-95d2-6f0ca6d70381"), event_id=1, version=0)
class Microsoft_Windows_D3D10Level9_1_0(Etw):
    pattern = Struct(
        "D3D10Level9Resource" / Int64ul,
        "m_hDX9Resource" / Int64ul,
        "Usage" / Int32ul
    )


@declare(guid=guid("7e7d3382-023c-43cb-95d2-6f0ca6d70381"), event_id=2, version=0)
class Microsoft_Windows_D3D10Level9_2_0(Etw):
    pattern = Struct(
        "D3D10Level9Resource" / Int64ul,
        "m_hDX9Resource" / Int64ul,
        "Usage" / Int32ul
    )


@declare(guid=guid("7e7d3382-023c-43cb-95d2-6f0ca6d70381"), event_id=3, version=0)
class Microsoft_Windows_D3D10Level9_3_0(Etw):
    pattern = Struct(
        "D3D10Level9Resource" / Int64ul,
        "m_hDX9Resource" / Int64ul,
        "Usage" / Int32ul
    )

