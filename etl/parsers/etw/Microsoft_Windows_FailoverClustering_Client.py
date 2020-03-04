# -*- coding: utf-8 -*-
"""
Microsoft-Windows-FailoverClustering-Client
GUID : a82fda5d-745f-409c-b0fe-18ae0678a0e0
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("a82fda5d-745f-409c-b0fe-18ae0678a0e0"), event_id=1, version=0)
class Microsoft_Windows_FailoverClustering_Client_1_0(Etw):
    pattern = Struct(
        "Parameter1" / WString
    )


@declare(guid=guid("a82fda5d-745f-409c-b0fe-18ae0678a0e0"), event_id=2, version=0)
class Microsoft_Windows_FailoverClustering_Client_2_0(Etw):
    pattern = Struct(
        "Parameter1" / WString
    )


@declare(guid=guid("a82fda5d-745f-409c-b0fe-18ae0678a0e0"), event_id=3, version=0)
class Microsoft_Windows_FailoverClustering_Client_3_0(Etw):
    pattern = Struct(
        "Parameter1" / WString
    )


@declare(guid=guid("a82fda5d-745f-409c-b0fe-18ae0678a0e0"), event_id=4, version=0)
class Microsoft_Windows_FailoverClustering_Client_4_0(Etw):
    pattern = Struct(
        "Parameter1" / WString
    )


@declare(guid=guid("a82fda5d-745f-409c-b0fe-18ae0678a0e0"), event_id=5, version=0)
class Microsoft_Windows_FailoverClustering_Client_5_0(Etw):
    pattern = Struct(
        "Parameter1" / WString
    )


@declare(guid=guid("a82fda5d-745f-409c-b0fe-18ae0678a0e0"), event_id=6, version=0)
class Microsoft_Windows_FailoverClustering_Client_6_0(Etw):
    pattern = Struct(
        "Parameter1" / WString
    )


@declare(guid=guid("a82fda5d-745f-409c-b0fe-18ae0678a0e0"), event_id=7, version=0)
class Microsoft_Windows_FailoverClustering_Client_7_0(Etw):
    pattern = Struct(
        "Parameter1" / WString
    )


@declare(guid=guid("a82fda5d-745f-409c-b0fe-18ae0678a0e0"), event_id=8, version=0)
class Microsoft_Windows_FailoverClustering_Client_8_0(Etw):
    pattern = Struct(
        "Parameter1" / WString
    )


@declare(guid=guid("a82fda5d-745f-409c-b0fe-18ae0678a0e0"), event_id=9, version=0)
class Microsoft_Windows_FailoverClustering_Client_9_0(Etw):
    pattern = Struct(
        "Parameter1" / WString
    )


@declare(guid=guid("a82fda5d-745f-409c-b0fe-18ae0678a0e0"), event_id=16, version=0)
class Microsoft_Windows_FailoverClustering_Client_16_0(Etw):
    pattern = Struct(
        "Parameter1" / WString
    )


@declare(guid=guid("a82fda5d-745f-409c-b0fe-18ae0678a0e0"), event_id=17, version=0)
class Microsoft_Windows_FailoverClustering_Client_17_0(Etw):
    pattern = Struct(
        "Parameter1" / WString
    )


@declare(guid=guid("a82fda5d-745f-409c-b0fe-18ae0678a0e0"), event_id=18, version=0)
class Microsoft_Windows_FailoverClustering_Client_18_0(Etw):
    pattern = Struct(
        "Parameter1" / WString
    )


@declare(guid=guid("a82fda5d-745f-409c-b0fe-18ae0678a0e0"), event_id=19, version=0)
class Microsoft_Windows_FailoverClustering_Client_19_0(Etw):
    pattern = Struct(
        "Parameter1" / WString
    )


@declare(guid=guid("a82fda5d-745f-409c-b0fe-18ae0678a0e0"), event_id=20, version=0)
class Microsoft_Windows_FailoverClustering_Client_20_0(Etw):
    pattern = Struct(
        "Parameter1" / WString
    )


@declare(guid=guid("a82fda5d-745f-409c-b0fe-18ae0678a0e0"), event_id=21, version=0)
class Microsoft_Windows_FailoverClustering_Client_21_0(Etw):
    pattern = Struct(
        "Parameter1" / WString
    )


@declare(guid=guid("a82fda5d-745f-409c-b0fe-18ae0678a0e0"), event_id=22, version=0)
class Microsoft_Windows_FailoverClustering_Client_22_0(Etw):
    pattern = Struct(
        "Parameter1" / WString
    )


@declare(guid=guid("a82fda5d-745f-409c-b0fe-18ae0678a0e0"), event_id=23, version=0)
class Microsoft_Windows_FailoverClustering_Client_23_0(Etw):
    pattern = Struct(
        "Parameter1" / WString
    )


@declare(guid=guid("a82fda5d-745f-409c-b0fe-18ae0678a0e0"), event_id=24, version=0)
class Microsoft_Windows_FailoverClustering_Client_24_0(Etw):
    pattern = Struct(
        "Parameter1" / WString
    )


@declare(guid=guid("a82fda5d-745f-409c-b0fe-18ae0678a0e0"), event_id=25, version=0)
class Microsoft_Windows_FailoverClustering_Client_25_0(Etw):
    pattern = Struct(
        "Parameter1" / WString
    )


@declare(guid=guid("a82fda5d-745f-409c-b0fe-18ae0678a0e0"), event_id=32, version=0)
class Microsoft_Windows_FailoverClustering_Client_32_0(Etw):
    pattern = Struct(
        "Parameter1" / WString
    )


@declare(guid=guid("a82fda5d-745f-409c-b0fe-18ae0678a0e0"), event_id=33, version=0)
class Microsoft_Windows_FailoverClustering_Client_33_0(Etw):
    pattern = Struct(
        "Parameter1" / WString
    )


@declare(guid=guid("a82fda5d-745f-409c-b0fe-18ae0678a0e0"), event_id=34, version=0)
class Microsoft_Windows_FailoverClustering_Client_34_0(Etw):
    pattern = Struct(
        "Parameter1" / WString
    )


@declare(guid=guid("a82fda5d-745f-409c-b0fe-18ae0678a0e0"), event_id=35, version=0)
class Microsoft_Windows_FailoverClustering_Client_35_0(Etw):
    pattern = Struct(
        "Parameter1" / WString
    )


@declare(guid=guid("a82fda5d-745f-409c-b0fe-18ae0678a0e0"), event_id=36, version=0)
class Microsoft_Windows_FailoverClustering_Client_36_0(Etw):
    pattern = Struct(
        "Parameter1" / WString
    )


@declare(guid=guid("a82fda5d-745f-409c-b0fe-18ae0678a0e0"), event_id=37, version=0)
class Microsoft_Windows_FailoverClustering_Client_37_0(Etw):
    pattern = Struct(
        "Parameter1" / WString
    )


@declare(guid=guid("a82fda5d-745f-409c-b0fe-18ae0678a0e0"), event_id=38, version=0)
class Microsoft_Windows_FailoverClustering_Client_38_0(Etw):
    pattern = Struct(
        "Parameter1" / WString
    )


@declare(guid=guid("a82fda5d-745f-409c-b0fe-18ae0678a0e0"), event_id=39, version=0)
class Microsoft_Windows_FailoverClustering_Client_39_0(Etw):
    pattern = Struct(
        "Parameter1" / WString
    )


@declare(guid=guid("a82fda5d-745f-409c-b0fe-18ae0678a0e0"), event_id=40, version=0)
class Microsoft_Windows_FailoverClustering_Client_40_0(Etw):
    pattern = Struct(
        "Parameter1" / WString
    )


@declare(guid=guid("a82fda5d-745f-409c-b0fe-18ae0678a0e0"), event_id=41, version=0)
class Microsoft_Windows_FailoverClustering_Client_41_0(Etw):
    pattern = Struct(
        "Parameter1" / WString
    )


@declare(guid=guid("a82fda5d-745f-409c-b0fe-18ae0678a0e0"), event_id=48, version=0)
class Microsoft_Windows_FailoverClustering_Client_48_0(Etw):
    pattern = Struct(
        "Parameter1" / WString
    )


@declare(guid=guid("a82fda5d-745f-409c-b0fe-18ae0678a0e0"), event_id=49, version=0)
class Microsoft_Windows_FailoverClustering_Client_49_0(Etw):
    pattern = Struct(
        "Parameter1" / WString
    )


@declare(guid=guid("a82fda5d-745f-409c-b0fe-18ae0678a0e0"), event_id=50, version=0)
class Microsoft_Windows_FailoverClustering_Client_50_0(Etw):
    pattern = Struct(
        "Parameter1" / WString
    )


@declare(guid=guid("a82fda5d-745f-409c-b0fe-18ae0678a0e0"), event_id=51, version=0)
class Microsoft_Windows_FailoverClustering_Client_51_0(Etw):
    pattern = Struct(
        "Parameter1" / WString
    )


@declare(guid=guid("a82fda5d-745f-409c-b0fe-18ae0678a0e0"), event_id=52, version=0)
class Microsoft_Windows_FailoverClustering_Client_52_0(Etw):
    pattern = Struct(
        "Parameter1" / WString
    )


@declare(guid=guid("a82fda5d-745f-409c-b0fe-18ae0678a0e0"), event_id=53, version=0)
class Microsoft_Windows_FailoverClustering_Client_53_0(Etw):
    pattern = Struct(
        "Parameter1" / WString
    )


@declare(guid=guid("a82fda5d-745f-409c-b0fe-18ae0678a0e0"), event_id=54, version=0)
class Microsoft_Windows_FailoverClustering_Client_54_0(Etw):
    pattern = Struct(
        "Parameter1" / WString
    )


@declare(guid=guid("a82fda5d-745f-409c-b0fe-18ae0678a0e0"), event_id=55, version=0)
class Microsoft_Windows_FailoverClustering_Client_55_0(Etw):
    pattern = Struct(
        "Parameter1" / WString
    )


@declare(guid=guid("a82fda5d-745f-409c-b0fe-18ae0678a0e0"), event_id=56, version=0)
class Microsoft_Windows_FailoverClustering_Client_56_0(Etw):
    pattern = Struct(
        "Parameter1" / WString
    )


@declare(guid=guid("a82fda5d-745f-409c-b0fe-18ae0678a0e0"), event_id=57, version=0)
class Microsoft_Windows_FailoverClustering_Client_57_0(Etw):
    pattern = Struct(
        "Parameter1" / WString
    )


@declare(guid=guid("a82fda5d-745f-409c-b0fe-18ae0678a0e0"), event_id=64, version=0)
class Microsoft_Windows_FailoverClustering_Client_64_0(Etw):
    pattern = Struct(
        "Parameter1" / WString
    )


@declare(guid=guid("a82fda5d-745f-409c-b0fe-18ae0678a0e0"), event_id=65, version=0)
class Microsoft_Windows_FailoverClustering_Client_65_0(Etw):
    pattern = Struct(
        "Parameter1" / WString
    )


@declare(guid=guid("a82fda5d-745f-409c-b0fe-18ae0678a0e0"), event_id=66, version=0)
class Microsoft_Windows_FailoverClustering_Client_66_0(Etw):
    pattern = Struct(
        "Parameter1" / WString
    )


@declare(guid=guid("a82fda5d-745f-409c-b0fe-18ae0678a0e0"), event_id=67, version=0)
class Microsoft_Windows_FailoverClustering_Client_67_0(Etw):
    pattern = Struct(
        "Parameter1" / WString
    )


@declare(guid=guid("a82fda5d-745f-409c-b0fe-18ae0678a0e0"), event_id=68, version=0)
class Microsoft_Windows_FailoverClustering_Client_68_0(Etw):
    pattern = Struct(
        "Parameter1" / WString
    )


@declare(guid=guid("a82fda5d-745f-409c-b0fe-18ae0678a0e0"), event_id=69, version=0)
class Microsoft_Windows_FailoverClustering_Client_69_0(Etw):
    pattern = Struct(
        "Parameter1" / WString
    )


@declare(guid=guid("a82fda5d-745f-409c-b0fe-18ae0678a0e0"), event_id=70, version=0)
class Microsoft_Windows_FailoverClustering_Client_70_0(Etw):
    pattern = Struct(
        "Parameter1" / WString
    )


@declare(guid=guid("a82fda5d-745f-409c-b0fe-18ae0678a0e0"), event_id=71, version=0)
class Microsoft_Windows_FailoverClustering_Client_71_0(Etw):
    pattern = Struct(
        "Parameter1" / WString
    )


@declare(guid=guid("a82fda5d-745f-409c-b0fe-18ae0678a0e0"), event_id=72, version=0)
class Microsoft_Windows_FailoverClustering_Client_72_0(Etw):
    pattern = Struct(
        "Parameter1" / WString
    )


@declare(guid=guid("a82fda5d-745f-409c-b0fe-18ae0678a0e0"), event_id=73, version=0)
class Microsoft_Windows_FailoverClustering_Client_73_0(Etw):
    pattern = Struct(
        "Parameter1" / WString
    )


@declare(guid=guid("a82fda5d-745f-409c-b0fe-18ae0678a0e0"), event_id=80, version=0)
class Microsoft_Windows_FailoverClustering_Client_80_0(Etw):
    pattern = Struct(
        "Parameter1" / WString
    )


@declare(guid=guid("a82fda5d-745f-409c-b0fe-18ae0678a0e0"), event_id=81, version=0)
class Microsoft_Windows_FailoverClustering_Client_81_0(Etw):
    pattern = Struct(
        "Parameter1" / WString
    )

