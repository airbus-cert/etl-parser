# -*- coding: utf-8 -*-
"""
Microsoft-Windows-MSMPEG2ADEC
GUID : 51311de3-d55e-454a-9c58-43dc7b4c01d2
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("51311de3-d55e-454a-9c58-43dc7b4c01d2"), event_id=3, version=0)
class Microsoft_Windows_MSMPEG2ADEC_3_0(Etw):
    pattern = Struct(
        "srcSamplingRate" / Int32ul,
        "AudioMode" / Int8sl
    )


@declare(guid=guid("51311de3-d55e-454a-9c58-43dc7b4c01d2"), event_id=4, version=0)
class Microsoft_Windows_MSMPEG2ADEC_4_0(Etw):
    pattern = Struct(
        "BlobVer" / Int32ul,
        "LicensorIndex" / Int32ul
    )


@declare(guid=guid("51311de3-d55e-454a-9c58-43dc7b4c01d2"), event_id=10, version=0)
class Microsoft_Windows_MSMPEG2ADEC_10_0(Etw):
    pattern = Struct(
        "dwordarg" / Int32ul
    )


@declare(guid=guid("51311de3-d55e-454a-9c58-43dc7b4c01d2"), event_id=11, version=0)
class Microsoft_Windows_MSMPEG2ADEC_11_0(Etw):
    pattern = Struct(
        "dwordarg" / Int32ul
    )


@declare(guid=guid("51311de3-d55e-454a-9c58-43dc7b4c01d2"), event_id=12, version=0)
class Microsoft_Windows_MSMPEG2ADEC_12_0(Etw):
    pattern = Struct(
        "dwordarg" / Int32ul
    )


@declare(guid=guid("51311de3-d55e-454a-9c58-43dc7b4c01d2"), event_id=13, version=0)
class Microsoft_Windows_MSMPEG2ADEC_13_0(Etw):
    pattern = Struct(
        "dwordarg" / Int32ul
    )


@declare(guid=guid("51311de3-d55e-454a-9c58-43dc7b4c01d2"), event_id=14, version=0)
class Microsoft_Windows_MSMPEG2ADEC_14_0(Etw):
    pattern = Struct(
        "dwordarg" / Int32ul
    )


@declare(guid=guid("51311de3-d55e-454a-9c58-43dc7b4c01d2"), event_id=15, version=0)
class Microsoft_Windows_MSMPEG2ADEC_15_0(Etw):
    pattern = Struct(
        "dwordarg" / Int32ul
    )


@declare(guid=guid("51311de3-d55e-454a-9c58-43dc7b4c01d2"), event_id=16, version=0)
class Microsoft_Windows_MSMPEG2ADEC_16_0(Etw):
    pattern = Struct(
        "dwordarg" / Int32ul
    )

