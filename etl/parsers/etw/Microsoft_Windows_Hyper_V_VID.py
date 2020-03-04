# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Hyper-V-VID
GUID : 5931d877-4860-4ee7-a95c-610a5f0d1407
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=1101, version=0)
class Microsoft_Windows_Hyper_V_VID_1101_0(Etw):
    pattern = Struct(
        "Parameter0" / Int64sl,
        "Parameter1" / Int64sl,
        "Parameter2" / Int64sl
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=1102, version=0)
class Microsoft_Windows_Hyper_V_VID_1102_0(Etw):
    pattern = Struct(
        "Parameter0" / Int64sl,
        "Parameter1" / Int64sl,
        "Parameter2" / Int64sl
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=1103, version=0)
class Microsoft_Windows_Hyper_V_VID_1103_0(Etw):
    pattern = Struct(
        "Parameter0" / Int64sl,
        "Parameter1" / Int64sl,
        "Parameter2" / Int64sl
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=1104, version=0)
class Microsoft_Windows_Hyper_V_VID_1104_0(Etw):
    pattern = Struct(
        "Parameter0" / Int64sl,
        "Parameter1" / Int64sl,
        "Parameter2" / Int64sl
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=1105, version=0)
class Microsoft_Windows_Hyper_V_VID_1105_0(Etw):
    pattern = Struct(
        "Parameter0" / Int64sl,
        "Parameter1" / Int64sl
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=1106, version=0)
class Microsoft_Windows_Hyper_V_VID_1106_0(Etw):
    pattern = Struct(
        "Parameter0" / Int64sl,
        "Parameter1" / Int64sl,
        "Parameter2" / Int64sl
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=1107, version=0)
class Microsoft_Windows_Hyper_V_VID_1107_0(Etw):
    pattern = Struct(
        "Parameter0" / Int64sl,
        "Parameter1" / Int64sl,
        "Parameter2" / Int64sl
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=1108, version=0)
class Microsoft_Windows_Hyper_V_VID_1108_0(Etw):
    pattern = Struct(
        "Parameter0" / Int64sl,
        "Parameter1" / Int64sl,
        "Parameter2" / Int64sl
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=1109, version=0)
class Microsoft_Windows_Hyper_V_VID_1109_0(Etw):
    pattern = Struct(
        "Parameter0" / Int64sl,
        "Parameter1" / Int64sl,
        "Parameter2" / Int64sl
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=1110, version=0)
class Microsoft_Windows_Hyper_V_VID_1110_0(Etw):
    pattern = Struct(
        "Parameter0" / Int64sl,
        "Parameter1" / Int64sl,
        "Parameter2" / Int64sl
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=1111, version=0)
class Microsoft_Windows_Hyper_V_VID_1111_0(Etw):
    pattern = Struct(
        "Parameter0" / Int64sl,
        "Parameter1" / Int64sl,
        "Parameter2" / Int64sl
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=3000, version=0)
class Microsoft_Windows_Hyper_V_VID_3000_0(Etw):
    pattern = Struct(
        "PartitionId" / WString,
        "Parameter0" / Int64sl
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5001, version=0)
class Microsoft_Windows_Hyper_V_VID_5001_0(Etw):
    pattern = Struct(
        "Parameter0" / Int64sl,
        "Parameter1" / Int64sl
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5002, version=0)
class Microsoft_Windows_Hyper_V_VID_5002_0(Etw):
    pattern = Struct(
        "Parameter0" / Int64sl,
        "Parameter1" / Int64sl,
        "Parameter2" / Int64sl,
        "Parameter3" / Int64sl,
        "Parameter4" / Int64sl,
        "Parameter5" / Int64sl,
        "Parameter6" / Int64sl
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5003, version=0)
class Microsoft_Windows_Hyper_V_VID_5003_0(Etw):
    pattern = Struct(
        "Parameter0" / Int64sl,
        "Parameter1" / Int64sl
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5004, version=0)
class Microsoft_Windows_Hyper_V_VID_5004_0(Etw):
    pattern = Struct(
        "Parameter0" / Int64sl,
        "Parameter1" / Int64sl,
        "Parameter2" / Int64sl
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5005, version=0)
class Microsoft_Windows_Hyper_V_VID_5005_0(Etw):
    pattern = Struct(
        "Parameter0" / Int64sl,
        "Parameter1" / Int64sl
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5006, version=0)
class Microsoft_Windows_Hyper_V_VID_5006_0(Etw):
    pattern = Struct(
        "Parameter0" / Int64sl,
        "Parameter1" / Int64sl,
        "Parameter2" / Int64sl
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5007, version=0)
class Microsoft_Windows_Hyper_V_VID_5007_0(Etw):
    pattern = Struct(
        "Parameter0" / Int64sl
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5008, version=0)
class Microsoft_Windows_Hyper_V_VID_5008_0(Etw):
    pattern = Struct(
        "Parameter0" / Int64sl
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5009, version=0)
class Microsoft_Windows_Hyper_V_VID_5009_0(Etw):
    pattern = Struct(
        "Parameter0" / Int64sl,
        "Parameter1" / Int64sl
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5010, version=0)
class Microsoft_Windows_Hyper_V_VID_5010_0(Etw):
    pattern = Struct(
        "Parameter0" / Int64sl,
        "Parameter1" / Int64sl,
        "Parameter2" / Int64sl
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5011, version=0)
class Microsoft_Windows_Hyper_V_VID_5011_0(Etw):
    pattern = Struct(
        "Parameter0" / Int64sl,
        "Parameter1" / Int64sl
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5012, version=0)
class Microsoft_Windows_Hyper_V_VID_5012_0(Etw):
    pattern = Struct(
        "Parameter0" / Int64sl,
        "Parameter1" / Int64sl,
        "Parameter2" / Int64sl
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5013, version=0)
class Microsoft_Windows_Hyper_V_VID_5013_0(Etw):
    pattern = Struct(
        "Parameter0" / Int64sl
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5014, version=0)
class Microsoft_Windows_Hyper_V_VID_5014_0(Etw):
    pattern = Struct(
        "Parameter0" / Int64sl,
        "Parameter1" / Int64sl
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5017, version=0)
class Microsoft_Windows_Hyper_V_VID_5017_0(Etw):
    pattern = Struct(
        "Parameter0" / Int64sl
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5018, version=0)
class Microsoft_Windows_Hyper_V_VID_5018_0(Etw):
    pattern = Struct(
        "Parameter0" / Int64sl
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5019, version=0)
class Microsoft_Windows_Hyper_V_VID_5019_0(Etw):
    pattern = Struct(
        "Parameter0" / Int64sl,
        "Parameter1" / Int64sl
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5020, version=0)
class Microsoft_Windows_Hyper_V_VID_5020_0(Etw):
    pattern = Struct(
        "Parameter0" / Int64sl,
        "Parameter1" / Int64sl,
        "Parameter2" / Int64sl
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5021, version=0)
class Microsoft_Windows_Hyper_V_VID_5021_0(Etw):
    pattern = Struct(
        "Parameter0" / Int64sl,
        "Parameter1" / Int64sl
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5022, version=0)
class Microsoft_Windows_Hyper_V_VID_5022_0(Etw):
    pattern = Struct(
        "Parameter0" / Int64sl,
        "Parameter1" / Int64sl,
        "Parameter2" / Int64sl
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5023, version=0)
class Microsoft_Windows_Hyper_V_VID_5023_0(Etw):
    pattern = Struct(
        "Parameter0" / Int64sl,
        "Parameter1" / Int64sl
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5024, version=0)
class Microsoft_Windows_Hyper_V_VID_5024_0(Etw):
    pattern = Struct(
        "Parameter0" / Int64sl,
        "Parameter1" / Int64sl,
        "Parameter2" / Int64sl
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5025, version=0)
class Microsoft_Windows_Hyper_V_VID_5025_0(Etw):
    pattern = Struct(
        "Parameter0" / Int64sl,
        "Parameter1" / Int64sl
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5026, version=0)
class Microsoft_Windows_Hyper_V_VID_5026_0(Etw):
    pattern = Struct(
        "Parameter0" / Int64sl,
        "Parameter1" / Int64sl,
        "Parameter2" / Int64sl
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5029, version=0)
class Microsoft_Windows_Hyper_V_VID_5029_0(Etw):
    pattern = Struct(
        "Parameter0" / Int64sl,
        "Parameter1" / Int64sl
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5030, version=0)
class Microsoft_Windows_Hyper_V_VID_5030_0(Etw):
    pattern = Struct(
        "Parameter0" / Int64sl,
        "Parameter1" / Int64sl,
        "Parameter2" / Int64sl
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5031, version=0)
class Microsoft_Windows_Hyper_V_VID_5031_0(Etw):
    pattern = Struct(
        "Parameter0" / Int64sl,
        "Parameter1" / Int64sl
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5032, version=0)
class Microsoft_Windows_Hyper_V_VID_5032_0(Etw):
    pattern = Struct(
        "Parameter0" / Int64sl,
        "Parameter1" / Int64sl,
        "Parameter2" / Int64sl
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5033, version=0)
class Microsoft_Windows_Hyper_V_VID_5033_0(Etw):
    pattern = Struct(
        "Parameter0" / Int64sl,
        "Parameter1" / Int64sl
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5034, version=0)
class Microsoft_Windows_Hyper_V_VID_5034_0(Etw):
    pattern = Struct(
        "Parameter0" / Int64sl,
        "Parameter1" / Int64sl,
        "Parameter2" / Int64sl
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5035, version=0)
class Microsoft_Windows_Hyper_V_VID_5035_0(Etw):
    pattern = Struct(
        "Parameter0" / Int64sl,
        "Parameter1" / Int64sl,
        "Parameter2" / Int64sl
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5036, version=0)
class Microsoft_Windows_Hyper_V_VID_5036_0(Etw):
    pattern = Struct(
        "Parameter0" / Int64sl,
        "Parameter1" / Int64sl,
        "Parameter2" / Int64sl,
        "Parameter3" / Int64sl
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5037, version=0)
class Microsoft_Windows_Hyper_V_VID_5037_0(Etw):
    pattern = Struct(
        "PhysicalAddress" / Int64ul,
        "PlatformDirected" / Int8ul
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5038, version=0)
class Microsoft_Windows_Hyper_V_VID_5038_0(Etw):
    pattern = Struct(
        "PhysicalAddress" / Int64ul,
        "PlatformDirected" / Int8ul,
        "PartitionFriendlyName" / WString,
        "PartitionName" / WString,
        "Consumed" / Int8ul
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5039, version=0)
class Microsoft_Windows_Hyper_V_VID_5039_0(Etw):
    pattern = Struct(
        "PhysicalAddress" / Int64ul,
        "PlatformDirected" / Int8ul,
        "PartitionFriendlyName" / WString,
        "PartitionName" / WString,
        "Consumed" / Int8ul
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5040, version=0)
class Microsoft_Windows_Hyper_V_VID_5040_0(Etw):
    pattern = Struct(
        "PhysicalAddress" / Int64ul,
        "PlatformDirected" / Int8ul
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5041, version=0)
class Microsoft_Windows_Hyper_V_VID_5041_0(Etw):
    pattern = Struct(
        "PhysicalAddress" / Int64ul,
        "PlatformDirected" / Int8ul
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5042, version=0)
class Microsoft_Windows_Hyper_V_VID_5042_0(Etw):
    pattern = Struct(
        "PhysicalAddress" / Int64ul,
        "PlatformDirected" / Int8ul,
        "PartitionFriendlyName" / WString,
        "PartitionName" / WString,
        "Consumed" / Int8ul
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5043, version=0)
class Microsoft_Windows_Hyper_V_VID_5043_0(Etw):
    pattern = Struct(
        "PhysicalAddress" / Int64ul,
        "PlatformDirected" / Int8ul,
        "PartitionFriendlyName" / WString,
        "PartitionName" / WString,
        "Consumed" / Int8ul
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5044, version=0)
class Microsoft_Windows_Hyper_V_VID_5044_0(Etw):
    pattern = Struct(
        "PartitionId" / WString,
        "Parameter0" / Int64sl
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5045, version=0)
class Microsoft_Windows_Hyper_V_VID_5045_0(Etw):
    pattern = Struct(
        "PartitionId" / WString,
        "Parameter0" / Int64sl
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5046, version=0)
class Microsoft_Windows_Hyper_V_VID_5046_0(Etw):
    pattern = Struct(
        "LowAddress" / Int64ul,
        "HighAddress" / Int64ul,
        "SkipBytes" / Int64ul,
        "TotalBytes" / Int64ul,
        "CacheType" / Int32ul,
        "NodeIndex" / Int8ul,
        "Flags" / Int32ul,
        "MemoryPartition" / Int64ul,
        "PartitionGuid" / Guid
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5047, version=0)
class Microsoft_Windows_Hyper_V_VID_5047_0(Etw):
    pattern = Struct(
        "Mdl" / Int64ul,
        "TotalBytes" / Int64ul
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5048, version=0)
class Microsoft_Windows_Hyper_V_VID_5048_0(Etw):
    pattern = Struct(
        "MbpArraySize" / Int64ul,
        "PartitionGuid" / Guid
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5049, version=0)
class Microsoft_Windows_Hyper_V_VID_5049_0(Etw):
    pattern = Struct(
        "Status" / Int64ul
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5050, version=0)
class Microsoft_Windows_Hyper_V_VID_5050_0(Etw):
    pattern = Struct(
        "PageCountToBack" / Int64ul,
        "KsrBlockId" / Int64ul,
        "PartitionGuid" / Guid
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5051, version=0)
class Microsoft_Windows_Hyper_V_VID_5051_0(Etw):
    pattern = Struct(
        "MbpArraySize" / Int64ul,
        "KsrRunCount" / Int32ul,
        "Status" / Int64ul
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5052, version=0)
class Microsoft_Windows_Hyper_V_VID_5052_0(Etw):
    pattern = Struct(
        "KsrMemoryRunCount" / Int32ul,
        "PartitionGuid" / Guid
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5053, version=0)
class Microsoft_Windows_Hyper_V_VID_5053_0(Etw):
    pattern = Struct(
        "Status" / Int64ul
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5054, version=0)
class Microsoft_Windows_Hyper_V_VID_5054_0(Etw):
    pattern = Struct(
        "MbpArraySize" / Int64ul,
        "KsrRunCount" / Int32ul,
        "PartitionGuid" / Guid
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5056, version=0)
class Microsoft_Windows_Hyper_V_VID_5056_0(Etw):
    pattern = Struct(
        "PartitionGuid" / Guid
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5057, version=0)
class Microsoft_Windows_Hyper_V_VID_5057_0(Etw):
    pattern = Struct(
        "Status" / Int64ul
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5058, version=0)
class Microsoft_Windows_Hyper_V_VID_5058_0(Etw):
    pattern = Struct(
        "KsrPersisted" / Int8sl,
        "PartitionGuid" / Guid
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5059, version=0)
class Microsoft_Windows_Hyper_V_VID_5059_0(Etw):
    pattern = Struct(
        "Status" / Int64ul
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5060, version=0)
class Microsoft_Windows_Hyper_V_VID_5060_0(Etw):
    pattern = Struct(
        "KsrPersisted" / Int8sl,
        "PartitionGuid" / Guid
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5061, version=0)
class Microsoft_Windows_Hyper_V_VID_5061_0(Etw):
    pattern = Struct(
        "Status" / Int64ul
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5062, version=0)
class Microsoft_Windows_Hyper_V_VID_5062_0(Etw):
    pattern = Struct(
        "StartGpaPage" / Int64ul,
        "StartMbp" / Int64ul,
        "MbpCount" / Int64ul,
        "InterceptOverrideFlags" / Int32ul,
        "PartitionGuid" / Guid
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5063, version=0)
class Microsoft_Windows_Hyper_V_VID_5063_0(Etw):
    pattern = Struct(
        "Status" / Int64ul
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5064, version=0)
class Microsoft_Windows_Hyper_V_VID_5064_0(Etw):
    pattern = Struct(
        "FirstPage" / Int64ul,
        "LastPage" / Int64ul,
        "PartitionGuid" / Guid
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5065, version=0)
class Microsoft_Windows_Hyper_V_VID_5065_0(Etw):
    pattern = Struct(
        "Status" / Int64ul
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5066, version=0)
class Microsoft_Windows_Hyper_V_VID_5066_0(Etw):
    pattern = Struct(
        "PartitionGuid" / Guid
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5068, version=0)
class Microsoft_Windows_Hyper_V_VID_5068_0(Etw):
    pattern = Struct(
        "Parameter0" / Int64sl,
        "Parameter1" / Int64sl
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5069, version=0)
class Microsoft_Windows_Hyper_V_VID_5069_0(Etw):
    pattern = Struct(
        "Parameter0" / Int64sl,
        "Parameter1" / Int64sl,
        "Parameter2" / Int64sl
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5070, version=0)
class Microsoft_Windows_Hyper_V_VID_5070_0(Etw):
    pattern = Struct(
        "Parameter0" / Int64sl,
        "Parameter1" / Int64sl
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5071, version=0)
class Microsoft_Windows_Hyper_V_VID_5071_0(Etw):
    pattern = Struct(
        "Parameter0" / Int64sl,
        "Parameter1" / Int64sl,
        "Parameter2" / Int64sl
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5072, version=0)
class Microsoft_Windows_Hyper_V_VID_5072_0(Etw):
    pattern = Struct(
        "TotalPages" / Int64ul,
        "PlatformDirected" / Int8ul
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5073, version=0)
class Microsoft_Windows_Hyper_V_VID_5073_0(Etw):
    pattern = Struct(
        "PhysicalAddress" / Int64ul,
        "PlatformDirected" / Int8ul,
        "PartitionFriendlyName" / WString,
        "PartitionName" / WString,
        "Consumed" / Int8ul
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5074, version=0)
class Microsoft_Windows_Hyper_V_VID_5074_0(Etw):
    pattern = Struct(
        "PhysicalAddress" / Int64ul,
        "PlatformDirected" / Int8ul,
        "PartitionFriendlyName" / WString,
        "PartitionName" / WString,
        "Consumed" / Int8ul
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5075, version=0)
class Microsoft_Windows_Hyper_V_VID_5075_0(Etw):
    pattern = Struct(
        "PhysicalAddress" / Int64ul,
        "PlatformDirected" / Int8ul,
        "PartitionFriendlyName" / WString,
        "PartitionName" / WString,
        "Consumed" / Int8ul
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5076, version=0)
class Microsoft_Windows_Hyper_V_VID_5076_0(Etw):
    pattern = Struct(
        "PhysicalAddress" / Int64ul,
        "PlatformDirected" / Int8ul
    )


@declare(guid=guid("5931d877-4860-4ee7-a95c-610a5f0d1407"), event_id=5077, version=0)
class Microsoft_Windows_Hyper_V_VID_5077_0(Etw):
    pattern = Struct(
        "TotalPages" / Int64ul,
        "PlatformDirected" / Int8ul,
        "PartitionFriendlyName" / WString,
        "PartitionName" / WString,
        "Consumed" / Int8ul
    )

