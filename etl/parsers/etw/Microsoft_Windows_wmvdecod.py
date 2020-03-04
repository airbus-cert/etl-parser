# -*- coding: utf-8 -*-
"""
Microsoft-Windows-wmvdecod
GUID : 55bacc9f-9ac0-46f5-968a-a5a5dd024f8a
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("55bacc9f-9ac0-46f5-968a-a5a5dd024f8a"), event_id=0, version=0)
class Microsoft_Windows_wmvdecod_0_0(Etw):
    pattern = Struct(
        "PictureID" / Int64ul,
        "FrameType" / Int32sl,
        "TaskType" / Int32sl
    )


@declare(guid=guid("55bacc9f-9ac0-46f5-968a-a5a5dd024f8a"), event_id=2, version=0)
class Microsoft_Windows_wmvdecod_2_0(Etw):
    pattern = Struct(
        "FourCC" / Int32ul,
        "Width" / Int32sl,
        "Height" / Int32sl
    )


@declare(guid=guid("55bacc9f-9ac0-46f5-968a-a5a5dd024f8a"), event_id=4, version=0)
class Microsoft_Windows_wmvdecod_4_0(Etw):
    pattern = Struct(
        "FormatSize" / Int32ul,
        "Format" / Bytes(lambda this: this.FormatSize)
    )


@declare(guid=guid("55bacc9f-9ac0-46f5-968a-a5a5dd024f8a"), event_id=6, version=0)
class Microsoft_Windows_wmvdecod_6_0(Etw):
    pattern = Struct(
        "SampleSizeInBytes" / Int32ul,
        "SampleTime" / Int64sl,
        "SampleDuration" / Int64sl
    )


@declare(guid=guid("55bacc9f-9ac0-46f5-968a-a5a5dd024f8a"), event_id=7, version=0)
class Microsoft_Windows_wmvdecod_7_0(Etw):
    pattern = Struct(
        "VOP" / Int32ul,
        "Frame" / Int32ul
    )


@declare(guid=guid("55bacc9f-9ac0-46f5-968a-a5a5dd024f8a"), event_id=8, version=0)
class Microsoft_Windows_wmvdecod_8_0(Etw):
    pattern = Struct(
        "VOP" / Int32ul,
        "Frame" / Int32ul,
        "SampleTime" / Int64sl,
        "SampleDuration" / Int64sl
    )


@declare(guid=guid("55bacc9f-9ac0-46f5-968a-a5a5dd024f8a"), event_id=10, version=0)
class Microsoft_Windows_wmvdecod_10_0(Etw):
    pattern = Struct(
        "SampleTime" / Int64sl,
        "SampleDuration" / Int64sl
    )


@declare(guid=guid("55bacc9f-9ac0-46f5-968a-a5a5dd024f8a"), event_id=13, version=0)
class Microsoft_Windows_wmvdecod_13_0(Etw):
    pattern = Struct(
        "Level" / Int32ul
    )


@declare(guid=guid("55bacc9f-9ac0-46f5-968a-a5a5dd024f8a"), event_id=20, version=0)
class Microsoft_Windows_wmvdecod_20_0(Etw):
    pattern = Struct(
        "TypeIndex" / Int32sl,
        "BufferSize" / Int32ul
    )


@declare(guid=guid("55bacc9f-9ac0-46f5-968a-a5a5dd024f8a"), event_id=21, version=0)
class Microsoft_Windows_wmvdecod_21_0(Etw):
    pattern = Struct(
        "TypeIndex" / Int32sl
    )


@declare(guid=guid("55bacc9f-9ac0-46f5-968a-a5a5dd024f8a"), event_id=33, version=0)
class Microsoft_Windows_wmvdecod_33_0(Etw):
    pattern = Struct(
        "SampleIndex" / Int32ul
    )


@declare(guid=guid("55bacc9f-9ac0-46f5-968a-a5a5dd024f8a"), event_id=34, version=0)
class Microsoft_Windows_wmvdecod_34_0(Etw):
    pattern = Struct(
        "SampleIndex" / Int32ul
    )


@declare(guid=guid("55bacc9f-9ac0-46f5-968a-a5a5dd024f8a"), event_id=35, version=0)
class Microsoft_Windows_wmvdecod_35_0(Etw):
    pattern = Struct(
        "OrigWidth" / Int32sl,
        "OrigHeight" / Int32sl,
        "OrigAspectRatioX" / Int32ul,
        "OrigAspectRatioY" / Int32ul,
        "NewWidth" / Int32sl,
        "NewHeight" / Int32sl,
        "NewAspectRatioX" / Int32ul,
        "NewAspectRatioY" / Int32ul
    )


@declare(guid=guid("55bacc9f-9ac0-46f5-968a-a5a5dd024f8a"), event_id=36, version=0)
class Microsoft_Windows_wmvdecod_36_0(Etw):
    pattern = Struct(
        "SwitchType" / Int32ul
    )


@declare(guid=guid("55bacc9f-9ac0-46f5-968a-a5a5dd024f8a"), event_id=37, version=0)
class Microsoft_Windows_wmvdecod_37_0(Etw):
    pattern = Struct(
        "rtLagTime" / Int64sl,
        "dwDropModeCurrent" / Int32ul,
        "dwPostModeCurrent" / Int32ul,
        "dwDropModeNew" / Int32ul,
        "dwPostModeNew" / Int32ul
    )


@declare(guid=guid("55bacc9f-9ac0-46f5-968a-a5a5dd024f8a"), event_id=38, version=0)
class Microsoft_Windows_wmvdecod_38_0(Etw):
    pattern = Struct(
        "D3DAWARE" / Int32ul
    )

