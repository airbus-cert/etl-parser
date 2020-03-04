# -*- coding: utf-8 -*-
"""
Microsoft-Windows-VolumeControl
GUID : 07de7879-1c96-41ce-afbd-c659a0e8e643
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("07de7879-1c96-41ce-afbd-c659a0e8e643"), event_id=102, version=0)
class Microsoft_Windows_VolumeControl_102_0(Etw):
    pattern = Struct(
        "Object" / Int32ul
    )


@declare(guid=guid("07de7879-1c96-41ce-afbd-c659a0e8e643"), event_id=103, version=0)
class Microsoft_Windows_VolumeControl_103_0(Etw):
    pattern = Struct(
        "Object" / Int32ul
    )


@declare(guid=guid("07de7879-1c96-41ce-afbd-c659a0e8e643"), event_id=104, version=0)
class Microsoft_Windows_VolumeControl_104_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "ChangeStamp" / Int32sl
    )


@declare(guid=guid("07de7879-1c96-41ce-afbd-c659a0e8e643"), event_id=105, version=0)
class Microsoft_Windows_VolumeControl_105_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("07de7879-1c96-41ce-afbd-c659a0e8e643"), event_id=106, version=0)
class Microsoft_Windows_VolumeControl_106_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "ChangeStamp" / Int32sl
    )


@declare(guid=guid("07de7879-1c96-41ce-afbd-c659a0e8e643"), event_id=107, version=0)
class Microsoft_Windows_VolumeControl_107_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "PrevChangeStamp" / Int32sl,
        "ChangeStamp" / Int32sl
    )


@declare(guid=guid("07de7879-1c96-41ce-afbd-c659a0e8e643"), event_id=108, version=0)
class Microsoft_Windows_VolumeControl_108_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "m_pUIWorkItem" / Int64ul
    )


@declare(guid=guid("07de7879-1c96-41ce-afbd-c659a0e8e643"), event_id=109, version=0)
class Microsoft_Windows_VolumeControl_109_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "IsChildAccount" / Int8ul,
        "hResult" / Int32sl
    )


@declare(guid=guid("07de7879-1c96-41ce-afbd-c659a0e8e643"), event_id=110, version=0)
class Microsoft_Windows_VolumeControl_110_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "pSystemModalDialog" / Int64ul
    )


@declare(guid=guid("07de7879-1c96-41ce-afbd-c659a0e8e643"), event_id=111, version=0)
class Microsoft_Windows_VolumeControl_111_0(Etw):
    pattern = Struct(
        "object" / Int64ul
    )


@declare(guid=guid("07de7879-1c96-41ce-afbd-c659a0e8e643"), event_id=112, version=0)
class Microsoft_Windows_VolumeControl_112_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "IsChildAccount" / Int8ul
    )


@declare(guid=guid("07de7879-1c96-41ce-afbd-c659a0e8e643"), event_id=113, version=0)
class Microsoft_Windows_VolumeControl_113_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32sl
    )


@declare(guid=guid("07de7879-1c96-41ce-afbd-c659a0e8e643"), event_id=114, version=0)
class Microsoft_Windows_VolumeControl_114_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "AllowsButton" / Int8ul,
        "NotAllowsButton" / Int8ul,
        "OkButton" / Int8ul
    )


@declare(guid=guid("07de7879-1c96-41ce-afbd-c659a0e8e643"), event_id=115, version=0)
class Microsoft_Windows_VolumeControl_115_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "bEngageVolumeLimit" / Int8ul
    )


@declare(guid=guid("07de7879-1c96-41ce-afbd-c659a0e8e643"), event_id=116, version=0)
class Microsoft_Windows_VolumeControl_116_0(Etw):
    pattern = Struct(
        "object" / Int64ul,
        "hResult" / Int32sl
    )

