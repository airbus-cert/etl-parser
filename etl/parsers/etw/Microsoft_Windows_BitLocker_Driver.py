# -*- coding: utf-8 -*-
"""
Microsoft-Windows-BitLocker-Driver
GUID : 651df93b-5053-4d1e-94c5-f6e6d25908d0
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24577, version=0)
class Microsoft_Windows_BitLocker_Driver_24577_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24578, version=0)
class Microsoft_Windows_BitLocker_Driver_24578_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24579, version=0)
class Microsoft_Windows_BitLocker_Driver_24579_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24580, version=0)
class Microsoft_Windows_BitLocker_Driver_24580_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24581, version=0)
class Microsoft_Windows_BitLocker_Driver_24581_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24582, version=0)
class Microsoft_Windows_BitLocker_Driver_24582_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24583, version=0)
class Microsoft_Windows_BitLocker_Driver_24583_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24584, version=0)
class Microsoft_Windows_BitLocker_Driver_24584_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24585, version=0)
class Microsoft_Windows_BitLocker_Driver_24585_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24586, version=0)
class Microsoft_Windows_BitLocker_Driver_24586_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24587, version=0)
class Microsoft_Windows_BitLocker_Driver_24587_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24588, version=0)
class Microsoft_Windows_BitLocker_Driver_24588_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24589, version=0)
class Microsoft_Windows_BitLocker_Driver_24589_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24590, version=0)
class Microsoft_Windows_BitLocker_Driver_24590_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24591, version=0)
class Microsoft_Windows_BitLocker_Driver_24591_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24592, version=0)
class Microsoft_Windows_BitLocker_Driver_24592_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24593, version=0)
class Microsoft_Windows_BitLocker_Driver_24593_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24594, version=0)
class Microsoft_Windows_BitLocker_Driver_24594_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24595, version=0)
class Microsoft_Windows_BitLocker_Driver_24595_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24596, version=0)
class Microsoft_Windows_BitLocker_Driver_24596_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul,
        "VolumeGUID" / Guid,
        "OptionalGUID" / Guid,
        "Flags" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24597, version=0)
class Microsoft_Windows_BitLocker_Driver_24597_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul,
        "VolumeGUID" / Guid,
        "OptionalGUID" / Guid,
        "Flags" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24598, version=0)
class Microsoft_Windows_BitLocker_Driver_24598_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul,
        "VolumeGUID" / Guid,
        "OptionalGUID" / Guid,
        "Flags" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24599, version=0)
class Microsoft_Windows_BitLocker_Driver_24599_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul,
        "VolumeGUID" / Guid,
        "OptionalGUID" / Guid,
        "Flags" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24600, version=0)
class Microsoft_Windows_BitLocker_Driver_24600_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul,
        "VolumeGUID" / Guid,
        "OptionalGUID" / Guid,
        "Flags" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24601, version=0)
class Microsoft_Windows_BitLocker_Driver_24601_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul,
        "VolumeGUID" / Guid,
        "OptionalGUID" / Guid,
        "Flags" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24602, version=0)
class Microsoft_Windows_BitLocker_Driver_24602_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul,
        "VolumeGUID" / Guid,
        "OptionalGUID" / Guid,
        "Flags" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24603, version=0)
class Microsoft_Windows_BitLocker_Driver_24603_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul,
        "VolumeGUID" / Guid,
        "OptionalGUID" / Guid,
        "Flags" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24604, version=0)
class Microsoft_Windows_BitLocker_Driver_24604_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul,
        "VolumeGUID" / Guid,
        "OptionalGUID" / Guid,
        "Flags" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24605, version=0)
class Microsoft_Windows_BitLocker_Driver_24605_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul,
        "VolumeGUID" / Guid,
        "OptionalGUID" / Guid,
        "Flags" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24606, version=0)
class Microsoft_Windows_BitLocker_Driver_24606_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul,
        "VolumeGUID" / Guid,
        "OptionalGUID" / Guid,
        "Flags" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24607, version=0)
class Microsoft_Windows_BitLocker_Driver_24607_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul,
        "VolumeGUID" / Guid,
        "OptionalGUID" / Guid,
        "Flags" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24608, version=0)
class Microsoft_Windows_BitLocker_Driver_24608_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul,
        "VolumeGUID" / Guid,
        "OptionalGUID" / Guid,
        "Flags" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24609, version=0)
class Microsoft_Windows_BitLocker_Driver_24609_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24610, version=0)
class Microsoft_Windows_BitLocker_Driver_24610_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24611, version=0)
class Microsoft_Windows_BitLocker_Driver_24611_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24612, version=0)
class Microsoft_Windows_BitLocker_Driver_24612_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24613, version=0)
class Microsoft_Windows_BitLocker_Driver_24613_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24614, version=0)
class Microsoft_Windows_BitLocker_Driver_24614_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24615, version=0)
class Microsoft_Windows_BitLocker_Driver_24615_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24616, version=0)
class Microsoft_Windows_BitLocker_Driver_24616_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24617, version=0)
class Microsoft_Windows_BitLocker_Driver_24617_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24618, version=0)
class Microsoft_Windows_BitLocker_Driver_24618_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24619, version=0)
class Microsoft_Windows_BitLocker_Driver_24619_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24620, version=0)
class Microsoft_Windows_BitLocker_Driver_24620_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24621, version=0)
class Microsoft_Windows_BitLocker_Driver_24621_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24622, version=0)
class Microsoft_Windows_BitLocker_Driver_24622_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24623, version=0)
class Microsoft_Windows_BitLocker_Driver_24623_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24624, version=0)
class Microsoft_Windows_BitLocker_Driver_24624_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24625, version=0)
class Microsoft_Windows_BitLocker_Driver_24625_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24626, version=0)
class Microsoft_Windows_BitLocker_Driver_24626_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24627, version=0)
class Microsoft_Windows_BitLocker_Driver_24627_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul,
        "VolumeGUID" / Guid,
        "OptionalGUID" / Guid,
        "Flags" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24628, version=0)
class Microsoft_Windows_BitLocker_Driver_24628_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul,
        "VolumeGUID" / Guid,
        "OptionalGUID" / Guid,
        "Flags" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24629, version=0)
class Microsoft_Windows_BitLocker_Driver_24629_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul,
        "VolumeGUID" / Guid,
        "OptionalGUID" / Guid,
        "Flags" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24630, version=0)
class Microsoft_Windows_BitLocker_Driver_24630_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul,
        "VolumeGUID" / Guid,
        "OptionalGUID" / Guid,
        "Flags" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24631, version=0)
class Microsoft_Windows_BitLocker_Driver_24631_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul,
        "VolumeGUID" / Guid,
        "OptionalGUID" / Guid,
        "Flags" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24632, version=0)
class Microsoft_Windows_BitLocker_Driver_24632_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul,
        "VolumeGUID" / Guid,
        "OptionalGUID" / Guid,
        "Flags" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24633, version=0)
class Microsoft_Windows_BitLocker_Driver_24633_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul,
        "VolumeGUID" / Guid,
        "OptionalGUID" / Guid,
        "Flags" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24634, version=0)
class Microsoft_Windows_BitLocker_Driver_24634_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul,
        "VolumeGUID" / Guid,
        "OptionalGUID" / Guid,
        "Flags" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24635, version=0)
class Microsoft_Windows_BitLocker_Driver_24635_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul,
        "VolumeGUID" / Guid,
        "OptionalGUID" / Guid,
        "Flags" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24636, version=0)
class Microsoft_Windows_BitLocker_Driver_24636_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul,
        "VolumeGUID" / Guid,
        "OptionalGUID" / Guid,
        "Flags" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24637, version=0)
class Microsoft_Windows_BitLocker_Driver_24637_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul,
        "VolumeGUID" / Guid,
        "OptionalGUID" / Guid,
        "Flags" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24638, version=0)
class Microsoft_Windows_BitLocker_Driver_24638_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul,
        "VolumeGUID" / Guid,
        "OptionalGUID" / Guid,
        "Flags" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24639, version=0)
class Microsoft_Windows_BitLocker_Driver_24639_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul,
        "VolumeGUID" / Guid,
        "OptionalGUID" / Guid,
        "Flags" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24640, version=0)
class Microsoft_Windows_BitLocker_Driver_24640_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul,
        "VolumeGUID" / Guid,
        "OptionalGUID" / Guid,
        "Flags" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24641, version=0)
class Microsoft_Windows_BitLocker_Driver_24641_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul,
        "VolumeGUID" / Guid,
        "OptionalGUID" / Guid,
        "Flags" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24642, version=0)
class Microsoft_Windows_BitLocker_Driver_24642_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24643, version=0)
class Microsoft_Windows_BitLocker_Driver_24643_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul,
        "VolumeGUID" / Guid,
        "OptionalGUID" / Guid,
        "Flags" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24644, version=0)
class Microsoft_Windows_BitLocker_Driver_24644_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24645, version=0)
class Microsoft_Windows_BitLocker_Driver_24645_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul,
        "VolumeGUID" / Guid,
        "OptionalGUID" / Guid,
        "Flags" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24646, version=0)
class Microsoft_Windows_BitLocker_Driver_24646_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24647, version=0)
class Microsoft_Windows_BitLocker_Driver_24647_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24648, version=0)
class Microsoft_Windows_BitLocker_Driver_24648_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24649, version=0)
class Microsoft_Windows_BitLocker_Driver_24649_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24650, version=0)
class Microsoft_Windows_BitLocker_Driver_24650_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24651, version=0)
class Microsoft_Windows_BitLocker_Driver_24651_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24652, version=0)
class Microsoft_Windows_BitLocker_Driver_24652_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul,
        "VolumeGUID" / Guid,
        "OptionalGUID" / Guid,
        "Flags" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24653, version=0)
class Microsoft_Windows_BitLocker_Driver_24653_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul,
        "VolumeGUID" / Guid,
        "OptionalGUID" / Guid,
        "Flags" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24654, version=0)
class Microsoft_Windows_BitLocker_Driver_24654_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul,
        "VolumeGUID" / Guid,
        "OptionalGUID" / Guid,
        "Flags" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24655, version=0)
class Microsoft_Windows_BitLocker_Driver_24655_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24656, version=0)
class Microsoft_Windows_BitLocker_Driver_24656_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24657, version=0)
class Microsoft_Windows_BitLocker_Driver_24657_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul,
        "VolumeGUID" / Guid,
        "OptionalGUID" / Guid,
        "Flags" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24658, version=0)
class Microsoft_Windows_BitLocker_Driver_24658_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul,
        "VolumeGUID" / Guid,
        "OptionalGUID" / Guid,
        "Flags" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24659, version=0)
class Microsoft_Windows_BitLocker_Driver_24659_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul,
        "VolumeGUID" / Guid,
        "OptionalGUID" / Guid,
        "Flags" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24660, version=0)
class Microsoft_Windows_BitLocker_Driver_24660_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24661, version=0)
class Microsoft_Windows_BitLocker_Driver_24661_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24662, version=0)
class Microsoft_Windows_BitLocker_Driver_24662_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24663, version=0)
class Microsoft_Windows_BitLocker_Driver_24663_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24664, version=0)
class Microsoft_Windows_BitLocker_Driver_24664_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24665, version=0)
class Microsoft_Windows_BitLocker_Driver_24665_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24666, version=0)
class Microsoft_Windows_BitLocker_Driver_24666_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24667, version=0)
class Microsoft_Windows_BitLocker_Driver_24667_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24668, version=0)
class Microsoft_Windows_BitLocker_Driver_24668_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24669, version=0)
class Microsoft_Windows_BitLocker_Driver_24669_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24670, version=0)
class Microsoft_Windows_BitLocker_Driver_24670_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24671, version=0)
class Microsoft_Windows_BitLocker_Driver_24671_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24672, version=0)
class Microsoft_Windows_BitLocker_Driver_24672_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul,
        "VolumeGUID" / Guid,
        "OptionalGUID" / Guid,
        "Flags" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24673, version=0)
class Microsoft_Windows_BitLocker_Driver_24673_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24674, version=0)
class Microsoft_Windows_BitLocker_Driver_24674_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24675, version=0)
class Microsoft_Windows_BitLocker_Driver_24675_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24676, version=0)
class Microsoft_Windows_BitLocker_Driver_24676_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24677, version=0)
class Microsoft_Windows_BitLocker_Driver_24677_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24678, version=0)
class Microsoft_Windows_BitLocker_Driver_24678_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24679, version=0)
class Microsoft_Windows_BitLocker_Driver_24679_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24680, version=0)
class Microsoft_Windows_BitLocker_Driver_24680_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24681, version=0)
class Microsoft_Windows_BitLocker_Driver_24681_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24682, version=0)
class Microsoft_Windows_BitLocker_Driver_24682_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24683, version=0)
class Microsoft_Windows_BitLocker_Driver_24683_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24684, version=0)
class Microsoft_Windows_BitLocker_Driver_24684_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24685, version=0)
class Microsoft_Windows_BitLocker_Driver_24685_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )


@declare(guid=guid("651df93b-5053-4d1e-94c5-f6e6d25908d0"), event_id=24686, version=0)
class Microsoft_Windows_BitLocker_Driver_24686_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Volume" / WString,
        "WritePhase" / Int32ul
    )

