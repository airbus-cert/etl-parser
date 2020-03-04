# -*- coding: utf-8 -*-
"""
Microsoft-Windows-NDIS
GUID : cdead503-17f5-4a3e-b7ae-df8cc2902eb9
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10000, version=0)
class Microsoft_Windows_NDIS_10000_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "NetLuid" / Int64ul,
        "Request" / Int64ul,
        "LowerIf" / Guid
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10001, version=0)
class Microsoft_Windows_NDIS_10001_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "NetLuid" / Int64ul,
        "Request" / Int64ul,
        "LowerIf" / Guid
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10002, version=0)
class Microsoft_Windows_NDIS_10002_0(Etw):
    pattern = Struct(
        "DeviceName" / WString
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10003, version=0)
class Microsoft_Windows_NDIS_10003_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10004, version=0)
class Microsoft_Windows_NDIS_10004_0(Etw):
    pattern = Struct(
        "DeviceName" / WString
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10005, version=0)
class Microsoft_Windows_NDIS_10005_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10006, version=0)
class Microsoft_Windows_NDIS_10006_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "NetLuid" / Int64ul,
        "ProtocolName" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10007, version=0)
class Microsoft_Windows_NDIS_10007_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "IfLuid" / Int64ul,
        "ReferenceContext" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10008, version=0)
class Microsoft_Windows_NDIS_10008_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "NetLuid" / Int64ul,
        "Request" / Int64ul,
        "Status" / Int32ul,
        "Location" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10009, version=0)
class Microsoft_Windows_NDIS_10009_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "IfLuid" / Int64ul,
        "ReferenceContext" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10010, version=0)
class Microsoft_Windows_NDIS_10010_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "NetLuid" / Int64ul,
        "Request" / Int64ul,
        "Status" / Int32ul,
        "Location" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10011, version=0)
class Microsoft_Windows_NDIS_10011_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "NetLuid" / Int64ul,
        "Error" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10012, version=0)
class Microsoft_Windows_NDIS_10012_0(Etw):
    pattern = Struct(
        "CompartmentId" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10013, version=0)
class Microsoft_Windows_NDIS_10013_0(Etw):
    pattern = Struct(
        "IfType" / Int32ul,
        "NetLuid" / Int64ul,
        "StructType" / Int32ul,
        "ParameterLen" / Int32ul,
        "ParameterOffset" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10014, version=0)
class Microsoft_Windows_NDIS_10014_0(Etw):
    pattern = Struct(
        "IfType" / Int32ul,
        "NetLuid" / Int64ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10015, version=0)
class Microsoft_Windows_NDIS_10015_0(Etw):
    pattern = Struct(
        "NetworkId" / Guid
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10016, version=0)
class Microsoft_Windows_NDIS_10016_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "IfLuid" / Int64ul,
        "ReferenceContext" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10017, version=0)
class Microsoft_Windows_NDIS_10017_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "NetLuid" / Int64ul,
        "ProtocolName" / WString
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10018, version=0)
class Microsoft_Windows_NDIS_10018_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "NetLuid" / Int64ul,
        "Request" / Int64ul,
        "Status" / Int32ul,
        "Location" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10019, version=0)
class Microsoft_Windows_NDIS_10019_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "IfLuid" / Int64ul,
        "ReferenceContext" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10020, version=0)
class Microsoft_Windows_NDIS_10020_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "IfLuid" / Int64ul,
        "ReferenceContext" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10021, version=0)
class Microsoft_Windows_NDIS_10021_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "IfLuid" / Int64ul,
        "ReferenceContext" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10022, version=0)
class Microsoft_Windows_NDIS_10022_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10023, version=0)
class Microsoft_Windows_NDIS_10023_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "NetLuid" / Int64ul,
        "Type" / Int32ul,
        "State" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10024, version=0)
class Microsoft_Windows_NDIS_10024_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "NetLuid" / Int64ul,
        "IrpMinorFunction" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10025, version=0)
class Microsoft_Windows_NDIS_10025_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "NetLuid" / Int64ul,
        "IrpMinorFunction" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10026, version=0)
class Microsoft_Windows_NDIS_10026_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "NetLuid" / Int64ul,
        "Error" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10027, version=0)
class Microsoft_Windows_NDIS_10027_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10028, version=0)
class Microsoft_Windows_NDIS_10028_0(Etw):
    pattern = Struct(
        "MiniportIfGuid" / Guid,
        "MiniportIfIndex" / Int32ul,
        "MiniportNetLuid" / Int64ul,
        "FilterIfGuid" / Guid,
        "FilterIfIndex" / Int32ul,
        "FilterNetLuid" / Int64ul,
        "OriginalMediaType" / Int32ul,
        "NewMediaType" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10029, version=0)
class Microsoft_Windows_NDIS_10029_0(Etw):
    pattern = Struct(
        "FilterName" / WString,
        "Reason" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10030, version=0)
class Microsoft_Windows_NDIS_10030_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10031, version=0)
class Microsoft_Windows_NDIS_10031_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "IfLuid" / Int64ul,
        "ReferenceContext" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10032, version=0)
class Microsoft_Windows_NDIS_10032_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "NetLuid" / Int64ul,
        "Reason" / Int32ul,
        "State" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10033, version=0)
class Microsoft_Windows_NDIS_10033_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "NetLuid" / Int64ul,
        "Reason" / Int32ul,
        "State" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10034, version=0)
class Microsoft_Windows_NDIS_10034_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul,
        "DeviceName" / WString
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10035, version=0)
class Microsoft_Windows_NDIS_10035_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "NetLuid" / Int64ul,
        "Type" / Int32ul,
        "State" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10037, version=0)
class Microsoft_Windows_NDIS_10037_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "NetLuid" / Int64ul,
        "Error" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10038, version=0)
class Microsoft_Windows_NDIS_10038_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10039, version=0)
class Microsoft_Windows_NDIS_10039_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10040, version=0)
class Microsoft_Windows_NDIS_10040_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "NetLuid" / Int64ul,
        "StateFlags" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10041, version=0)
class Microsoft_Windows_NDIS_10041_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "NetLuid" / Int64ul,
        "StateFlags" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10042, version=0)
class Microsoft_Windows_NDIS_10042_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10043, version=0)
class Microsoft_Windows_NDIS_10043_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "NetLuid" / Int64ul,
        "Action" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10044, version=0)
class Microsoft_Windows_NDIS_10044_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "NetLuid" / Int64ul,
        "Error" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10045, version=0)
class Microsoft_Windows_NDIS_10045_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "NetLuid" / Int64ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10046, version=0)
class Microsoft_Windows_NDIS_10046_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "NetLuid" / Int64ul,
        "Type" / Int32ul,
        "State" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10047, version=0)
class Microsoft_Windows_NDIS_10047_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "IfLuid" / Int64ul,
        "ReferenceContext" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10048, version=0)
class Microsoft_Windows_NDIS_10048_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "NetLuid" / Int64ul,
        "SystemState" / Int32ul,
        "DeviceState" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10049, version=0)
class Microsoft_Windows_NDIS_10049_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "NetLuid" / Int64ul,
        "Type" / Int32ul,
        "State" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10050, version=0)
class Microsoft_Windows_NDIS_10050_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "NetLuid" / Int64ul,
        "Error" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10052, version=0)
class Microsoft_Windows_NDIS_10052_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "NetLuid" / Int64ul,
        "Oid" / Int32ul,
        "Status" / Int32ul,
        "Location" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10053, version=0)
class Microsoft_Windows_NDIS_10053_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "IfLuid" / Int64ul,
        "ReferenceContext" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10054, version=0)
class Microsoft_Windows_NDIS_10054_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "NetLuid" / Int64ul,
        "Reason" / Int32ul,
        "Port" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10055, version=0)
class Microsoft_Windows_NDIS_10055_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "IfLuid" / Int64ul,
        "ReferenceContext" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10056, version=0)
class Microsoft_Windows_NDIS_10056_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "NetLuid" / Int64ul,
        "Error" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10057, version=0)
class Microsoft_Windows_NDIS_10057_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "NetLuid" / Int64ul,
        "Error" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10058, version=0)
class Microsoft_Windows_NDIS_10058_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "IfLuid" / Int64ul,
        "ReferenceContext" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10059, version=0)
class Microsoft_Windows_NDIS_10059_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "IfLuid" / Int64ul,
        "ReferenceContext" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10060, version=0)
class Microsoft_Windows_NDIS_10060_0(Etw):
    pattern = Struct(
        "Context" / Int32ul,
        "State" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10061, version=0)
class Microsoft_Windows_NDIS_10061_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "IfLuid" / Int64ul,
        "ReferenceContext" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10062, version=0)
class Microsoft_Windows_NDIS_10062_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "IfLuid" / Int64ul,
        "ReferenceContext" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10063, version=0)
class Microsoft_Windows_NDIS_10063_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "IfLuid" / Int64ul,
        "ReferenceContext" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10064, version=0)
class Microsoft_Windows_NDIS_10064_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "IfLuid" / Int64ul,
        "ReferenceContext" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10065, version=0)
class Microsoft_Windows_NDIS_10065_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "NetLuid" / Int64ul,
        "SystemState" / Int32ul,
        "DeviceState" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10066, version=0)
class Microsoft_Windows_NDIS_10066_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "IfLuid" / Int64ul,
        "ReferenceContext" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10067, version=0)
class Microsoft_Windows_NDIS_10067_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "IfLuid" / Int64ul,
        "ReferenceContext" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10068, version=0)
class Microsoft_Windows_NDIS_10068_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "IfLuid" / Int64ul,
        "ReferenceContext" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10069, version=0)
class Microsoft_Windows_NDIS_10069_0(Etw):
    pattern = Struct(
        "Layer" / Int32ul,
        "ProtocolName" / WString,
        "DeviceName" / WString
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10070, version=0)
class Microsoft_Windows_NDIS_10070_0(Etw):
    pattern = Struct(
        "Layer" / Int32ul,
        "ProtocolName" / WString,
        "DeviceName" / WString
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10071, version=0)
class Microsoft_Windows_NDIS_10071_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "IfLuid" / Int64ul,
        "ReferenceContext" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10072, version=0)
class Microsoft_Windows_NDIS_10072_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "IfLuid" / Int64ul,
        "ReferenceContext" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10073, version=0)
class Microsoft_Windows_NDIS_10073_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "IfLuid" / Int64ul,
        "ReferenceContext" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10074, version=0)
class Microsoft_Windows_NDIS_10074_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "NetLuid" / Int64ul,
        "Error" / Int32ul,
        "Oid" / Int32ul,
        "Set" / Int8ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10075, version=0)
class Microsoft_Windows_NDIS_10075_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10076, version=0)
class Microsoft_Windows_NDIS_10076_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "NetLuid" / Int64ul,
        "Error" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10077, version=0)
class Microsoft_Windows_NDIS_10077_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10078, version=0)
class Microsoft_Windows_NDIS_10078_0(Etw):
    pattern = Struct(
        "OpenRef" / Int64ul,
        "Packet" / Int64ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10079, version=0)
class Microsoft_Windows_NDIS_10079_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "NetLuid" / Int64ul,
        "CompletedAtOpen" / Int8ul,
        "Open" / Int64ul,
        "Request" / Int64ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10080, version=0)
class Microsoft_Windows_NDIS_10080_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "NetLuid" / Int64ul,
        "Error" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10081, version=0)
class Microsoft_Windows_NDIS_10081_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "NetLuid" / Int64ul,
        "Error" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10082, version=0)
class Microsoft_Windows_NDIS_10082_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "NetLuid" / Int64ul,
        "Error" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10083, version=0)
class Microsoft_Windows_NDIS_10083_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "NetLuid" / Int64ul,
        "Error" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10084, version=0)
class Microsoft_Windows_NDIS_10084_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "NetLuid" / Int64ul,
        "Open" / Int64ul,
        "OriginalMediaType" / Int32ul,
        "ExpectedMediaType" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10085, version=0)
class Microsoft_Windows_NDIS_10085_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "NetLuid" / Int64ul,
        "Open" / Int64ul,
        "OriginalMediaType" / Int32ul,
        "ExpectedMediaType" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10086, version=0)
class Microsoft_Windows_NDIS_10086_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "NetLuid" / Int64ul,
        "Error" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10087, version=0)
class Microsoft_Windows_NDIS_10087_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "NetLuid" / Int64ul,
        "Type" / Int32ul,
        "State" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10088, version=0)
class Microsoft_Windows_NDIS_10088_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "NetLuid" / Int64ul,
        "Transport" / WString,
        "PnPEvent" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10089, version=0)
class Microsoft_Windows_NDIS_10089_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "IfLuid" / Int64ul,
        "ReferenceContext" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10090, version=0)
class Microsoft_Windows_NDIS_10090_0(Etw):
    pattern = Struct(
        "ProtocolName" / WString,
        "Reason" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10091, version=0)
class Microsoft_Windows_NDIS_10091_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "IfLuid" / Int64ul,
        "ReferenceContext" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10092, version=0)
class Microsoft_Windows_NDIS_10092_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "NetLuid" / Int64ul,
        "Error" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10093, version=0)
class Microsoft_Windows_NDIS_10093_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "IfLuid" / Int64ul,
        "ReferenceContext" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10094, version=0)
class Microsoft_Windows_NDIS_10094_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "NetLuid" / Int64ul,
        "AdapterName" / WString,
        "Error" / Int32ul,
        "ErrorValueCount" / Int32ul,
        "ErrorValues" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10095, version=0)
class Microsoft_Windows_NDIS_10095_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "NetLuid" / Int64ul,
        "Request" / Int64ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10096, version=0)
class Microsoft_Windows_NDIS_10096_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "NetLuid" / Int64ul,
        "Reason" / Int32ul,
        "Port" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10097, version=0)
class Microsoft_Windows_NDIS_10097_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "IfLuid" / Int64ul,
        "ReferenceContext" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10098, version=0)
class Microsoft_Windows_NDIS_10098_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "NetLuid" / Int64ul,
        "Error" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10099, version=0)
class Microsoft_Windows_NDIS_10099_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "NetLuid" / Int64ul,
        "Error" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10100, version=0)
class Microsoft_Windows_NDIS_10100_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "IfLuid" / Int64ul,
        "ReferenceContext" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10101, version=0)
class Microsoft_Windows_NDIS_10101_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "NetLuid" / Int64ul,
        "Request" / Int64ul,
        "CompleteRequest" / Int8ul,
        "Status" / Int32ul,
        "Oid" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10102, version=0)
class Microsoft_Windows_NDIS_10102_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "NetLuid" / Int64ul,
        "Request" / Int64ul,
        "Status" / Int32ul,
        "Location" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10103, version=0)
class Microsoft_Windows_NDIS_10103_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "State" / Int8ul,
        "Location" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10104, version=0)
class Microsoft_Windows_NDIS_10104_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "NetLuid" / Int64ul,
        "Flags" / Int32ul,
        "PnPFlags" / Int32ul,
        "DevicePowerState" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10105, version=0)
class Microsoft_Windows_NDIS_10105_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "NetLuid" / Int64ul,
        "Flags" / Int32ul,
        "PnPFlags" / Int32ul,
        "DevicePowerState" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10106, version=0)
class Microsoft_Windows_NDIS_10106_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "NetLuid" / Int64ul,
        "OperationalStatus" / Int32ul,
        "OperationalStatusFlags" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10107, version=0)
class Microsoft_Windows_NDIS_10107_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "NetLuid" / Int64ul,
        "OperationalStatus" / Int32ul,
        "OperationalStatusFlags" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10108, version=0)
class Microsoft_Windows_NDIS_10108_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "NetLuid" / Int64ul,
        "ChangeType" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10109, version=0)
class Microsoft_Windows_NDIS_10109_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "NetLuid" / Int64ul,
        "RequestType" / Int32ul,
        "Status" / Int32ul,
        "Location" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10110, version=0)
class Microsoft_Windows_NDIS_10110_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "NetLuid" / Int64ul,
        "RequestType" / Int32ul,
        "Status" / Int32ul,
        "Location" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10111, version=0)
class Microsoft_Windows_NDIS_10111_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "NetLuid" / Int64ul,
        "RequestType" / Int32ul,
        "Status" / Int32ul,
        "Location" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10112, version=0)
class Microsoft_Windows_NDIS_10112_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "NetLuid" / Int64ul,
        "RequestType" / Int32ul,
        "Status" / Int32ul,
        "Location" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10113, version=0)
class Microsoft_Windows_NDIS_10113_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "NetLuid" / Int64ul,
        "RequestType" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10114, version=0)
class Microsoft_Windows_NDIS_10114_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "NetLuid" / Int64ul,
        "RequestType" / Int32ul,
        "LowerIf" / Guid
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10115, version=0)
class Microsoft_Windows_NDIS_10115_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "NetLuid" / Int64ul,
        "RequestType" / Int32ul,
        "LowerIf" / Guid
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10200, version=0)
class Microsoft_Windows_NDIS_10200_0(Etw):
    pattern = Struct(
        "NetLuidIndex" / Int32ul,
        "FunctionType" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10201, version=0)
class Microsoft_Windows_NDIS_10201_0(Etw):
    pattern = Struct(
        "NetLuidIndex" / Int32ul,
        "FunctionType" / Int32ul,
        "Duration" / Int64ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10202, version=0)
class Microsoft_Windows_NDIS_10202_0(Etw):
    pattern = Struct(
        "NetLuidIndex" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10203, version=0)
class Microsoft_Windows_NDIS_10203_0(Etw):
    pattern = Struct(
        "NetLuidIndex" / Int32ul,
        "Duration" / Int64ul,
        "NumberOfNbls" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10204, version=0)
class Microsoft_Windows_NDIS_10204_0(Etw):
    pattern = Struct(
        "NetLuidIndex" / Int32ul,
        "CurrentProcessorIndex" / Int32ul,
        "NumberOfNetBufferLists" / Int32ul,
        "ProcessingDurationMilliseconds" / Int32ul,
        "PreviousLimit" / Int32ul,
        "NewLimit" / Int32ul,
        "IndividualMeasurement" / Int32ul,
        "CummulativeMeasurement" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10300, version=0)
class Microsoft_Windows_NDIS_10300_0(Etw):
    pattern = Struct(
        "NetLuidIndex" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10301, version=0)
class Microsoft_Windows_NDIS_10301_0(Etw):
    pattern = Struct(
        "NetLuidIndex" / Int32ul,
        "NdisStatusCode" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10302, version=0)
class Microsoft_Windows_NDIS_10302_0(Etw):
    pattern = Struct(
        "NetLuidIndex" / Int32ul,
        "ResumeReason" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10303, version=0)
class Microsoft_Windows_NDIS_10303_0(Etw):
    pattern = Struct(
        "InterfaceLuid" / Int64ul,
        "ComponentId" / Int32ul,
        "ComponentRefCount" / Int32ul,
        "InterfaceRefCount" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10304, version=0)
class Microsoft_Windows_NDIS_10304_0(Etw):
    pattern = Struct(
        "InterfaceLuid" / Int64ul,
        "ComponentId" / Int32ul,
        "ComponentRefCount" / Int32ul,
        "InterfaceRefCount" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10305, version=0)
class Microsoft_Windows_NDIS_10305_0(Etw):
    pattern = Struct(
        "IfLuid" / Int64ul,
        "WakeReason" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10306, version=0)
class Microsoft_Windows_NDIS_10306_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "IfLuid" / Int64ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10307, version=0)
class Microsoft_Windows_NDIS_10307_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "IfLuid" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10308, version=0)
class Microsoft_Windows_NDIS_10308_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "IfLuid" / Int64ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10309, version=0)
class Microsoft_Windows_NDIS_10309_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "IfLuid" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10310, version=0)
class Microsoft_Windows_NDIS_10310_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "IfLuid" / Int64ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10311, version=0)
class Microsoft_Windows_NDIS_10311_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "IfLuid" / Int64ul,
        "AdapterName" / WString,
        "MiniportEventEnum" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10312, version=0)
class Microsoft_Windows_NDIS_10312_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "State" / Int8ul,
        "Location" / Int32ul,
        "MiniportIfGuid" / Guid,
        "MiniportAdapterName" / WString,
        "FilterInstanceName" / WString,
        "FilterFriendlyName" / WString
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10314, version=0)
class Microsoft_Windows_NDIS_10314_0(Etw):
    pattern = Struct(
        "Duration" / Int64ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10315, version=0)
class Microsoft_Windows_NDIS_10315_0(Etw):
    pattern = Struct(
        "IfIndex" / Int32ul,
        "IfLuid" / Int64ul,
        "ActiveTime" / Int64ul,
        "PowerTransitionCount" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10316, version=0)
class Microsoft_Windows_NDIS_10316_0(Etw):
    pattern = Struct(
        "InterfaceLuid" / Int64ul,
        "ComponentId" / Int32ul,
        "ActiveTime" / Int64ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10317, version=0)
class Microsoft_Windows_NDIS_10317_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "IfLuid" / Int64ul,
        "AdapterName" / WString,
        "MiniportEventEnum" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10320, version=0)
class Microsoft_Windows_NDIS_10320_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "NetLuid" / Int64ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10321, version=0)
class Microsoft_Windows_NDIS_10321_0(Etw):
    pattern = Struct(
        "NetLuid" / Int64ul,
        "ComponentId" / Int32ul,
        "RefcountValue" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10322, version=0)
class Microsoft_Windows_NDIS_10322_0(Etw):
    pattern = Struct(
        "NetLuid" / Int64ul,
        "StopFlags" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10323, version=0)
class Microsoft_Windows_NDIS_10323_0(Etw):
    pattern = Struct(
        "IfIndex" / Int32ul,
        "IfLuid" / Int64ul,
        "PowerStateFrom" / WString,
        "PowerStateTo" / WString,
        "IfInUnicastPackets" / Int64ul,
        "IfOutUnicastPackets" / Int64ul,
        "IfInMulticastPackets" / Int64ul,
        "IfOutMulticastPackets" / Int64ul,
        "IfInBroadcastPackets" / Int64ul,
        "IfOutBroadcastPackets" / Int64ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10324, version=0)
class Microsoft_Windows_NDIS_10324_0(Etw):
    pattern = Struct(
        "ScenarioInstanceId" / Int8ul,
        "ParentGuid" / Guid,
        "BlockerGuid" / Guid,
        "PhysicalDeviceNode" / Int64ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10325, version=0)
class Microsoft_Windows_NDIS_10325_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "WakePacketSize" / Int32ul,
        "WakePacketPayload" / Bytes(lambda this: this.WakePacketSize)
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10400, version=0)
class Microsoft_Windows_NDIS_10400_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "IfLuid" / Int64ul,
        "AdapterName" / WString,
        "ResetReason" / Int32ul,
        "ResetCount" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=10401, version=0)
class Microsoft_Windows_NDIS_10401_0(Etw):
    pattern = Struct(
        "NetLuid" / Int64ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=60001, version=0)
class Microsoft_Windows_NDIS_60001_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=60002, version=0)
class Microsoft_Windows_NDIS_60002_0(Etw):
    pattern = Struct(
        "WarningCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=60003, version=0)
class Microsoft_Windows_NDIS_60003_0(Etw):
    pattern = Struct(
        "NextState" / Int8ul,
        "Context" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=60004, version=0)
class Microsoft_Windows_NDIS_60004_0(Etw):
    pattern = Struct(
        "Context" / Int32ul,
        "UpdateReasonCode" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=60101, version=0)
class Microsoft_Windows_NDIS_60101_0(Etw):
    pattern = Struct(
        "SourceAddress" / Int32ul,
        "SourcePort" / Int32ul,
        "DestinationAddress" / Int32ul,
        "DestinationPort" / Int32ul,
        "Protocol" / Int32ul,
        "ReferenceContext" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=60102, version=0)
class Microsoft_Windows_NDIS_60102_0(Etw):
    pattern = Struct(
        "SourcePort" / Int32ul,
        "DestinationPort" / Int32ul,
        "Protocol" / Int32ul,
        "ReferenceContext" / Int32ul
    )


@declare(guid=guid("cdead503-17f5-4a3e-b7ae-df8cc2902eb9"), event_id=60103, version=0)
class Microsoft_Windows_NDIS_60103_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "IfLuid" / Int64ul,
        "ReferenceContext" / Int32ul
    )

