# -*- coding: utf-8 -*-
"""
Intel-SST-OED
GUID : 6f789161-d86f-4063-9e66-41f26b5da238
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("6f789161-d86f-4063-9e66-41f26b5da238"), event_id=1, version=0)
class Intel_SST_OED_1_0(Etw):
    pattern = Struct(
        "OldDriverState" / WString,
        "NewDriverState" / WString
    )


@declare(guid=guid("6f789161-d86f-4063-9e66-41f26b5da238"), event_id=2, version=0)
class Intel_SST_OED_2_0(Etw):
    pattern = Struct(
        "OldPowerState" / WString,
        "NewPowerState" / WString,
        "Location" / Int8ul
    )


@declare(guid=guid("6f789161-d86f-4063-9e66-41f26b5da238"), event_id=3, version=0)
class Intel_SST_OED_3_0(Etw):
    pattern = Struct(
        "NewDSPState" / WString,
        "Cores" / Int32ul,
        "CoresStateValue" / Int32ul,
        "Location" / Int8ul
    )


@declare(guid=guid("6f789161-d86f-4063-9e66-41f26b5da238"), event_id=4, version=0)
class Intel_SST_OED_4_0(Etw):
    pattern = Struct(
        "OldFwState" / Int32ul,
        "NewFwState" / Int32ul
    )


@declare(guid=guid("6f789161-d86f-4063-9e66-41f26b5da238"), event_id=6, version=0)
class Intel_SST_OED_6_0(Etw):
    pattern = Struct(
        "HIPCI" / Int64ul,
        "HIPCIE" / Int64ul,
        "Location" / Int8ul,
        "OffsetCount" / Int32ul,
        "OffsetElements" / Int32ul
    )


@declare(guid=guid("6f789161-d86f-4063-9e66-41f26b5da238"), event_id=7, version=0)
class Intel_SST_OED_7_0(Etw):
    pattern = Struct(
        "HIPCT" / Int64ul,
        "HIPCTE" / Int64ul,
        "Location" / Int8ul,
        "OffsetCount" / Int32ul,
        "OffsetElements" / Int32ul
    )


@declare(guid=guid("6f789161-d86f-4063-9e66-41f26b5da238"), event_id=8, version=0)
class Intel_SST_OED_8_0(Etw):
    pattern = Struct(
        "Reason" / WString,
        "Location" / Int8ul
    )


@declare(guid=guid("6f789161-d86f-4063-9e66-41f26b5da238"), event_id=9, version=0)
class Intel_SST_OED_9_0(Etw):
    pattern = Struct(
        "Type" / WString,
        "Size" / Int32ul,
        "Location" / Int8ul
    )


@declare(guid=guid("6f789161-d86f-4063-9e66-41f26b5da238"), event_id=10, version=0)
class Intel_SST_OED_10_0(Etw):
    pattern = Struct(
        "message" / WString,
        "status" / Int32ul
    )


@declare(guid=guid("6f789161-d86f-4063-9e66-41f26b5da238"), event_id=11, version=0)
class Intel_SST_OED_11_0(Etw):
    pattern = Struct(
        "message" / WString,
        "status" / Int32ul
    )


@declare(guid=guid("6f789161-d86f-4063-9e66-41f26b5da238"), event_id=12, version=0)
class Intel_SST_OED_12_0(Etw):
    pattern = Struct(
        "ModuleGUID" / Guid,
        "ModuleTypeCode" / Int32sl,
        "MaxInQueues" / Int32ul,
        "MaxOutQueues" / Int32ul,
        "FreqCount" / Int32ul,
        "SamplingFrequencies" / Int32ul,
        "BitDepthCount" / Int32ul,
        "BitDepths" / Int16ul,
        "ContainerSizeCount" / Int32ul,
        "ContainerSizes" / Int16ul,
        "ChannelConfigCount" / Int32ul,
        "ChannelConfigs" / Int16ul
    )


@declare(guid=guid("6f789161-d86f-4063-9e66-41f26b5da238"), event_id=13, version=0)
class Intel_SST_OED_13_0(Etw):
    pattern = Struct(
        "message" / WString
    )


@declare(guid=guid("6f789161-d86f-4063-9e66-41f26b5da238"), event_id=15, version=0)
class Intel_SST_OED_15_0(Etw):
    pattern = Struct(
        "message" / WString
    )


@declare(guid=guid("6f789161-d86f-4063-9e66-41f26b5da238"), event_id=16, version=0)
class Intel_SST_OED_16_0(Etw):
    pattern = Struct(
        "Mode" / Guid,
        "Pin" / Int8ul
    )


@declare(guid=guid("6f789161-d86f-4063-9e66-41f26b5da238"), event_id=17, version=0)
class Intel_SST_OED_17_0(Etw):
    pattern = Struct(
        "message" / WString,
        "status" / Int32ul
    )


@declare(guid=guid("6f789161-d86f-4063-9e66-41f26b5da238"), event_id=18, version=0)
class Intel_SST_OED_18_0(Etw):
    pattern = Struct(
        "message" / WString,
        "status" / Int32ul
    )


@declare(guid=guid("6f789161-d86f-4063-9e66-41f26b5da238"), event_id=19, version=0)
class Intel_SST_OED_19_0(Etw):
    pattern = Struct(
        "message" / WString,
        "status" / Int32ul
    )


@declare(guid=guid("6f789161-d86f-4063-9e66-41f26b5da238"), event_id=20, version=0)
class Intel_SST_OED_20_0(Etw):
    pattern = Struct(
        "message" / WString,
        "status" / Int32ul
    )


@declare(guid=guid("6f789161-d86f-4063-9e66-41f26b5da238"), event_id=21, version=0)
class Intel_SST_OED_21_0(Etw):
    pattern = Struct(
        "message" / WString,
        "status" / Int32ul
    )


@declare(guid=guid("6f789161-d86f-4063-9e66-41f26b5da238"), event_id=22, version=0)
class Intel_SST_OED_22_0(Etw):
    pattern = Struct(
        "message" / WString,
        "status" / Int32ul
    )


@declare(guid=guid("6f789161-d86f-4063-9e66-41f26b5da238"), event_id=23, version=0)
class Intel_SST_OED_23_0(Etw):
    pattern = Struct(
        "message" / WString,
        "status" / Int32ul
    )


@declare(guid=guid("6f789161-d86f-4063-9e66-41f26b5da238"), event_id=24, version=0)
class Intel_SST_OED_24_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "State" / Int32ul
    )

