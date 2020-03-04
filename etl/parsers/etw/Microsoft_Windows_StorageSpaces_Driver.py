# -*- coding: utf-8 -*-
"""
Microsoft-Windows-StorageSpaces-Driver
GUID : 595f7f52-c90a-4026-a125-8eb5e083f15e
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=102, version=0)
class Microsoft_Windows_StorageSpaces_Driver_102_0(Etw):
    pattern = Struct(
        "Id" / Guid,
        "Status" / Int32ul
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=103, version=0)
class Microsoft_Windows_StorageSpaces_Driver_103_0(Etw):
    pattern = Struct(
        "Id" / Guid,
        "Status" / Int32ul
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=104, version=0)
class Microsoft_Windows_StorageSpaces_Driver_104_0(Etw):
    pattern = Struct(
        "Id" / Guid,
        "Status" / Int32ul
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=200, version=0)
class Microsoft_Windows_StorageSpaces_Driver_200_0(Etw):
    pattern = Struct(
        "Id" / Guid,
        "Status" / Int32ul
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=202, version=0)
class Microsoft_Windows_StorageSpaces_Driver_202_0(Etw):
    pattern = Struct(
        "Id" / Guid,
        "Status" / Int32ul
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=203, version=0)
class Microsoft_Windows_StorageSpaces_Driver_203_0(Etw):
    pattern = Struct(
        "Id" / Guid,
        "Status" / Int32ul,
        "DeviceNumber" / Int32sl,
        "DriveManufacturer" / WString,
        "DriveModel" / WString,
        "DriveSerial" / WString,
        "EnclosureManufacturer" / WString,
        "EnclosureModel" / WString,
        "EnclosureSerial" / WString,
        "Slot" / Int32sl
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=204, version=0)
class Microsoft_Windows_StorageSpaces_Driver_204_0(Etw):
    pattern = Struct(
        "Id" / Guid,
        "Key" / Int8ul,
        "Asc" / Int8ul,
        "Ascq" / Int8ul,
        "DeviceNumber" / Int32sl,
        "DriveManufacturer" / WString,
        "DriveModel" / WString,
        "DriveSerial" / WString,
        "EnclosureManufacturer" / WString,
        "EnclosureModel" / WString,
        "EnclosureSerial" / WString,
        "Slot" / Int32sl
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=205, version=0)
class Microsoft_Windows_StorageSpaces_Driver_205_0(Etw):
    pattern = Struct(
        "Id" / Guid,
        "DriveManufacturer" / WString,
        "DriveModel" / WString,
        "DriveSerial" / WString,
        "EnclosureManufacturer" / WString,
        "EnclosureModel" / WString,
        "EnclosureSerial" / WString,
        "Slot" / Int32sl
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=206, version=0)
class Microsoft_Windows_StorageSpaces_Driver_206_0(Etw):
    pattern = Struct(
        "Id" / Guid,
        "Reason" / Int8ul,
        "Status" / Int32ul,
        "State" / Int32ul
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=300, version=0)
class Microsoft_Windows_StorageSpaces_Driver_300_0(Etw):
    pattern = Struct(
        "Id1" / Guid,
        "Id2" / Guid,
        "Status" / Int32ul
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=301, version=0)
class Microsoft_Windows_StorageSpaces_Driver_301_0(Etw):
    pattern = Struct(
        "Id" / Guid,
        "Status" / Int32ul
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=302, version=0)
class Microsoft_Windows_StorageSpaces_Driver_302_0(Etw):
    pattern = Struct(
        "Id" / Guid,
        "Status" / Int32ul
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=303, version=0)
class Microsoft_Windows_StorageSpaces_Driver_303_0(Etw):
    pattern = Struct(
        "UserId" / Guid,
        "Id" / Guid,
        "ColumnData" / CString
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=304, version=0)
class Microsoft_Windows_StorageSpaces_Driver_304_0(Etw):
    pattern = Struct(
        "Id" / Guid
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=305, version=0)
class Microsoft_Windows_StorageSpaces_Driver_305_0(Etw):
    pattern = Struct(
        "Id" / Guid
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=306, version=0)
class Microsoft_Windows_StorageSpaces_Driver_306_0(Etw):
    pattern = Struct(
        "Id" / Guid,
        "Status" / Int32ul
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=307, version=0)
class Microsoft_Windows_StorageSpaces_Driver_307_0(Etw):
    pattern = Struct(
        "Id" / Guid,
        "Status" / Int32ul
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=309, version=0)
class Microsoft_Windows_StorageSpaces_Driver_309_0(Etw):
    pattern = Struct(
        "Id" / Guid,
        "Status" / Int32ul
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=310, version=0)
class Microsoft_Windows_StorageSpaces_Driver_310_0(Etw):
    pattern = Struct(
        "Id" / Guid,
        "Status" / Int32ul
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=311, version=0)
class Microsoft_Windows_StorageSpaces_Driver_311_0(Etw):
    pattern = Struct(
        "Id" / Guid,
        "Status" / Int32ul
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=312, version=0)
class Microsoft_Windows_StorageSpaces_Driver_312_0(Etw):
    pattern = Struct(
        "Id" / Guid,
        "Status" / Int32ul
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=313, version=0)
class Microsoft_Windows_StorageSpaces_Driver_313_0(Etw):
    pattern = Struct(
        "Id" / Guid
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=400, version=0)
class Microsoft_Windows_StorageSpaces_Driver_400_0(Etw):
    pattern = Struct(
        "Id" / Guid,
        "Path" / Int32sl,
        "EnclosureManufacturer" / WString,
        "EnclosureModel" / WString,
        "EnclosureSerial" / WString,
        "EnclosureRevision" / WString
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=401, version=0)
class Microsoft_Windows_StorageSpaces_Driver_401_0(Etw):
    pattern = Struct(
        "Id" / Guid,
        "Path" / Int32sl,
        "EnclosureManufacturer" / WString,
        "EnclosureModel" / WString,
        "EnclosureSerial" / WString,
        "EnclosureRevision" / WString
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=402, version=0)
class Microsoft_Windows_StorageSpaces_Driver_402_0(Etw):
    pattern = Struct(
        "Id" / Guid,
        "OldHealth" / Int32ul,
        "NewHealth" / Int32ul,
        "EnclosureManufacturer" / WString,
        "EnclosureModel" / WString,
        "EnclosureSerial" / WString,
        "EnclosureRevision" / WString
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=403, version=0)
class Microsoft_Windows_StorageSpaces_Driver_403_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "EnclosureManufacturer" / WString,
        "EnclosureModel" / WString,
        "EnclosureSerial" / WString,
        "EnclosureRevision" / WString
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=1000, version=0)
class Microsoft_Windows_StorageSpaces_Driver_1000_0(Etw):
    pattern = Struct(
        "Id" / Guid,
        "Function" / CString,
        "Line" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=1001, version=0)
class Microsoft_Windows_StorageSpaces_Driver_1001_0(Etw):
    pattern = Struct(
        "PoolId" / Guid,
        "Transaction" / Int32ul,
        "SequenceNumber" / Int64ul
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=1002, version=0)
class Microsoft_Windows_StorageSpaces_Driver_1002_0(Etw):
    pattern = Struct(
        "PoolId" / Guid,
        "Transaction" / Int32ul,
        "Status" / Int32ul,
        "SequenceNumber" / Int64ul
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=1003, version=0)
class Microsoft_Windows_StorageSpaces_Driver_1003_0(Etw):
    pattern = Struct(
        "SpaceId" / Guid,
        "Transaction" / Int32ul,
        "SequenceNumber" / Int64ul
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=1004, version=0)
class Microsoft_Windows_StorageSpaces_Driver_1004_0(Etw):
    pattern = Struct(
        "SpaceId" / Guid,
        "Transaction" / Int32ul,
        "Status" / Int32ul,
        "SequenceNumber" / Int64ul
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=1005, version=0)
class Microsoft_Windows_StorageSpaces_Driver_1005_0(Etw):
    pattern = Struct(
        "Code" / Int32ul
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=1006, version=0)
class Microsoft_Windows_StorageSpaces_Driver_1006_0(Etw):
    pattern = Struct(
        "Code" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=1007, version=0)
class Microsoft_Windows_StorageSpaces_Driver_1007_0(Etw):
    pattern = Struct(
        "Id" / Guid
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=1008, version=0)
class Microsoft_Windows_StorageSpaces_Driver_1008_0(Etw):
    pattern = Struct(
        "Id" / Guid
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=1009, version=0)
class Microsoft_Windows_StorageSpaces_Driver_1009_0(Etw):
    pattern = Struct(
        "Id" / Guid,
        "BytesProcessed" / Int64ul
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=1010, version=0)
class Microsoft_Windows_StorageSpaces_Driver_1010_0(Etw):
    pattern = Struct(
        "Id" / Guid,
        "Offset" / Int64ul,
        "Length" / Int32ul
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=1011, version=0)
class Microsoft_Windows_StorageSpaces_Driver_1011_0(Etw):
    pattern = Struct(
        "ConfigId" / Guid,
        "DriveCount" / Int32ul,
        "DriveIds" / WString
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=1012, version=0)
class Microsoft_Windows_StorageSpaces_Driver_1012_0(Etw):
    pattern = Struct(
        "ConfigId" / Guid,
        "ScmCount" / Int32ul,
        "SsdCount" / Int32ul,
        "HddCount" / Int32ul,
        "TotalCount" / Int32ul,
        "AddCount" / Int32ul,
        "RemoveCount" / Int32ul,
        "DriveIds" / WString
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=1013, version=0)
class Microsoft_Windows_StorageSpaces_Driver_1013_0(Etw):
    pattern = Struct(
        "Id" / Guid,
        "SpaceOffset" / Int64ul,
        "ColumnToReallocate" / Int32ul,
        "CopyToReallocate" / Int32ul,
        "ColumnMissingFdInfo" / Int32ul,
        "CopyMissingFdInfo" / Int32ul
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=1014, version=0)
class Microsoft_Windows_StorageSpaces_Driver_1014_0(Etw):
    pattern = Struct(
        "Id" / Guid
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=1015, version=0)
class Microsoft_Windows_StorageSpaces_Driver_1015_0(Etw):
    pattern = Struct(
        "Id" / Guid,
        "TotalPathsCount" / Int32ul,
        "PresentPathsCount" / Int32ul,
        "ConfigurationData" / CString
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=1016, version=0)
class Microsoft_Windows_StorageSpaces_Driver_1016_0(Etw):
    pattern = Struct(
        "Id" / Guid,
        "TotalPathsCount" / Int32ul,
        "PresentPathsCount" / Int32ul,
        "ConfigurationData" / CString
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=1017, version=0)
class Microsoft_Windows_StorageSpaces_Driver_1017_0(Etw):
    pattern = Struct(
        "Duration" / Int64ul,
        "Frame0" / Int32ul,
        "Frame1" / Int32ul,
        "Frame2" / Int32ul,
        "Frame3" / Int32ul
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=1018, version=0)
class Microsoft_Windows_StorageSpaces_Driver_1018_0(Etw):
    pattern = Struct(
        "Duration" / Int64ul,
        "Frame0" / Int32ul,
        "Frame1" / Int32ul,
        "Frame2" / Int32ul,
        "Frame3" / Int32ul
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=1019, version=0)
class Microsoft_Windows_StorageSpaces_Driver_1019_0(Etw):
    pattern = Struct(
        "SpaceId" / Guid,
        "LogType" / Int32ul,
        "Copy" / Int32ul,
        "Lsn" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=1020, version=0)
class Microsoft_Windows_StorageSpaces_Driver_1020_0(Etw):
    pattern = Struct(
        "Id" / Guid,
        "Manufacturer" / WString,
        "Model" / WString,
        "Serial" / WString,
        "Revision" / WString,
        "DriveCount" / Int32ul,
        "DriveIoSummary" / Int32sl
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=1021, version=0)
class Microsoft_Windows_StorageSpaces_Driver_1021_0(Etw):
    pattern = Struct(
        "PoolId" / Guid,
        "SpaceId" / Guid,
        "SequenceNumber" / Int64ul
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=1022, version=0)
class Microsoft_Windows_StorageSpaces_Driver_1022_0(Etw):
    pattern = Struct(
        "PoolId" / Guid,
        "SpaceId" / Guid,
        "SequenceNumber" / Int64ul
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=1023, version=0)
class Microsoft_Windows_StorageSpaces_Driver_1023_0(Etw):
    pattern = Struct(
        "SpaceId" / Guid,
        "NumberOfEntries" / Int32ul,
        "Limit" / Int32ul
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=1024, version=0)
class Microsoft_Windows_StorageSpaces_Driver_1024_0(Etw):
    pattern = Struct(
        "SpaceId" / Guid,
        "Limit" / Int32ul
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=1025, version=0)
class Microsoft_Windows_StorageSpaces_Driver_1025_0(Etw):
    pattern = Struct(
        "SpaceId" / Guid,
        "Operation" / Int8ul,
        "Status" / Int32ul
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=1026, version=0)
class Microsoft_Windows_StorageSpaces_Driver_1026_0(Etw):
    pattern = Struct(
        "SpaceId" / Guid,
        "LogType" / Int32ul,
        "Operation" / Int8ul,
        "Status" / Int32ul
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=1027, version=0)
class Microsoft_Windows_StorageSpaces_Driver_1027_0(Etw):
    pattern = Struct(
        "SpaceId" / Guid,
        "PoolId" / Guid,
        "IoStateCountSize" / Int16ul,
        "IoStateCount" / Int64sl,
        "IoStateBytesSize" / Int16ul,
        "IoStateBytes" / Int64sl,
        "IoReasonCountSize" / Int16ul,
        "IoReasonCount" / Int64sl,
        "IoReasonBytesSize" / Int16ul,
        "IoReasonBytes" / Int64sl,
        "RepairReplacementCount" / Int64sl,
        "RebalanceReplacementCount" / Int64sl,
        "FailedReplacementCount" / Int64sl,
        "ScopeRegenerationCount" / Int64sl,
        "RepairReplacementBytes" / Int64sl,
        "RebalanceReplacementBytes" / Int64sl,
        "FailedReplacementBytes" / Int64sl,
        "ScopeRegenerationBytes" / Int64sl,
        "NeedRepairPhase2Count" / Int64sl,
        "NeedRepairPhase6Count" / Int64sl,
        "RepairPhasesSize" / Int16ul,
        "RepairPhases" / Int64sl,
        "RepairStatusSize" / Int16ul,
        "RepairStatus" / Int32ul
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=2000, version=0)
class Microsoft_Windows_StorageSpaces_Driver_2000_0(Etw):
    pattern = Struct(
        "SpaceId" / Guid,
        "Irp" / Int64ul,
        "Packet" / Int64ul,
        "Offset" / Int64ul,
        "Length" / Int32ul,
        "Function" / Int8ul,
        "Operation" / Int8ul,
        "State" / Int8ul
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=2001, version=0)
class Microsoft_Windows_StorageSpaces_Driver_2001_0(Etw):
    pattern = Struct(
        "SpaceId" / Guid,
        "Irp" / Int64ul,
        "Packet" / Int64ul,
        "Status" / Int32ul,
        "Latency" / Int64ul
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=2002, version=0)
class Microsoft_Windows_StorageSpaces_Driver_2002_0(Etw):
    pattern = Struct(
        "SpaceId" / Guid,
        "Irp" / Int64ul,
        "Packet" / Int64ul
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=2003, version=0)
class Microsoft_Windows_StorageSpaces_Driver_2003_0(Etw):
    pattern = Struct(
        "SpaceId" / Guid,
        "Irp" / Int64ul,
        "Packet" / Int64ul,
        "Status" / Int32ul,
        "Latency" / Int64ul
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=2004, version=0)
class Microsoft_Windows_StorageSpaces_Driver_2004_0(Etw):
    pattern = Struct(
        "SpaceId" / Guid,
        "Irp" / Int64ul,
        "Action" / Int32ul,
        "RangesCount" / Int32ul,
        "Ranges" / Int16sl
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=2005, version=0)
class Microsoft_Windows_StorageSpaces_Driver_2005_0(Etw):
    pattern = Struct(
        "SpaceId" / Guid,
        "Irp" / Int64ul,
        "Packet" / Int64ul,
        "Status" / Int32ul,
        "Latency" / Int64ul
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=2006, version=0)
class Microsoft_Windows_StorageSpaces_Driver_2006_0(Etw):
    pattern = Struct(
        "SpaceId" / Guid,
        "TopPacketIrp" / Int64ul,
        "TopPacket" / Int64ul,
        "DriveId" / Guid,
        "Irp" / Int64ul,
        "Packet" / Int64ul,
        "Offset" / Int64ul,
        "Length" / Int32ul,
        "Function" / Int8ul,
        "HistoryCount" / Int32ul,
        "History" / Float32l
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=2007, version=0)
class Microsoft_Windows_StorageSpaces_Driver_2007_0(Etw):
    pattern = Struct(
        "SpaceId" / Guid,
        "TopPacketIrp" / Int64ul,
        "TopPacket" / Int64ul,
        "DriveId" / Guid,
        "Irp" / Int64ul,
        "Packet" / Int64ul,
        "Status" / Int32ul,
        "Latency" / Int64ul
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=2008, version=0)
class Microsoft_Windows_StorageSpaces_Driver_2008_0(Etw):
    pattern = Struct(
        "SpaceId" / Guid,
        "TopPacketIrp" / Int64ul,
        "TopPacket" / Int64ul,
        "DriveId" / Guid,
        "Irp" / Int64ul,
        "Packet" / Int64ul,
        "HistoryCount" / Int32ul,
        "History" / Int32ul
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=2009, version=0)
class Microsoft_Windows_StorageSpaces_Driver_2009_0(Etw):
    pattern = Struct(
        "SpaceId" / Guid,
        "TopPacketIrp" / Int64ul,
        "TopPacket" / Int64ul,
        "DriveId" / Guid,
        "Irp" / Int64ul,
        "Packet" / Int64ul,
        "Status" / Int32ul,
        "Latency" / Int64ul
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=2010, version=0)
class Microsoft_Windows_StorageSpaces_Driver_2010_0(Etw):
    pattern = Struct(
        "SpaceId" / Guid,
        "TopPacketIrp" / Int64ul,
        "TopPacket" / Int64ul,
        "DriveId" / Guid,
        "Irp" / Int64ul,
        "Packet" / Int64ul,
        "RangesCount" / Int32ul,
        "Ranges" / Int64ul,
        "HistoryCount" / Int32ul,
        "History" / Double
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=2011, version=0)
class Microsoft_Windows_StorageSpaces_Driver_2011_0(Etw):
    pattern = Struct(
        "SpaceId" / Guid,
        "TopPacketIrp" / Int64ul,
        "TopPacket" / Int64ul,
        "DriveId" / Guid,
        "Irp" / Int64ul,
        "Packet" / Int64ul,
        "Status" / Int32ul,
        "Latency" / Int64ul
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=2100, version=0)
class Microsoft_Windows_StorageSpaces_Driver_2100_0(Etw):
    pattern = Struct(
        "SpaceId" / Guid,
        "LogType" / Int32ul,
        "UsedBytes" / Int64ul
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=2101, version=0)
class Microsoft_Windows_StorageSpaces_Driver_2101_0(Etw):
    pattern = Struct(
        "SpaceId" / Guid,
        "LogType" / Int32ul,
        "Lsn" / Int64ul,
        "Length" / Int32ul,
        "Reason" / Int8ul
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=2102, version=0)
class Microsoft_Windows_StorageSpaces_Driver_2102_0(Etw):
    pattern = Struct(
        "SpaceId" / Guid,
        "LogType" / Int32ul,
        "StartLsn" / Int32ul,
        "Lsn" / Int32ul
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=2103, version=0)
class Microsoft_Windows_StorageSpaces_Driver_2103_0(Etw):
    pattern = Struct(
        "SpaceId" / Guid,
        "LogType" / Int32ul,
        "Lsn" / Int64ul,
        "Length" / Int32ul,
        "Reason" / Int8ul
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=2104, version=0)
class Microsoft_Windows_StorageSpaces_Driver_2104_0(Etw):
    pattern = Struct(
        "SpaceId" / Guid,
        "LogType" / Int32ul,
        "StartLsn" / Int32ul,
        "Lsn" / Int32ul
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=2200, version=0)
class Microsoft_Windows_StorageSpaces_Driver_2200_0(Etw):
    pattern = Struct(
        "SpaceId" / Guid,
        "Offset" / Int64ul,
        "DataCount" / Int32ul,
        "DataBytes" / Int32ul,
        "TotalCount" / Int32ul,
        "TotalBytes" / Int32ul,
        "IsOptimized" / Int8ul
    )


@declare(guid=guid("595f7f52-c90a-4026-a125-8eb5e083f15e"), event_id=2300, version=0)
class Microsoft_Windows_StorageSpaces_Driver_2300_0(Etw):
    pattern = Struct(
        "SpaceId" / Guid,
        "Operation" / Int32ul,
        "Length" / Int32ul,
        "DiskOffset" / Int64ul,
        "RelativeOffset" / Int64ul,
        "CacheOffset" / Int64ul,
        "Status" / Int32ul
    )

