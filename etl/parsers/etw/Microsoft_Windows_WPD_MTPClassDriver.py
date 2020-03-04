# -*- coding: utf-8 -*-
"""
Microsoft-Windows-WPD-MTPClassDriver
GUID : 21b7c16e-c5af-4a69-a74a-7245481c1b97
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("21b7c16e-c5af-4a69-a74a-7245481c1b97"), event_id=1001, version=0)
class Microsoft_Windows_WPD_MTPClassDriver_1001_0(Etw):
    pattern = Struct(
        "Seconds" / Int32ul
    )


@declare(guid=guid("21b7c16e-c5af-4a69-a74a-7245481c1b97"), event_id=1002, version=0)
class Microsoft_Windows_WPD_MTPClassDriver_1002_0(Etw):
    pattern = Struct(
        "State" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("21b7c16e-c5af-4a69-a74a-7245481c1b97"), event_id=1003, version=0)
class Microsoft_Windows_WPD_MTPClassDriver_1003_0(Etw):
    pattern = Struct(
        "State" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("21b7c16e-c5af-4a69-a74a-7245481c1b97"), event_id=1004, version=0)
class Microsoft_Windows_WPD_MTPClassDriver_1004_0(Etw):
    pattern = Struct(
        "Code" / Int32ul
    )


@declare(guid=guid("21b7c16e-c5af-4a69-a74a-7245481c1b97"), event_id=1005, version=0)
class Microsoft_Windows_WPD_MTPClassDriver_1005_0(Etw):
    pattern = Struct(
        "Manufacturer" / WString,
        "Model" / WString,
        "Version" / WString,
        "HackModel" / Int32ul
    )


@declare(guid=guid("21b7c16e-c5af-4a69-a74a-7245481c1b97"), event_id=1006, version=0)
class Microsoft_Windows_WPD_MTPClassDriver_1006_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("21b7c16e-c5af-4a69-a74a-7245481c1b97"), event_id=1007, version=0)
class Microsoft_Windows_WPD_MTPClassDriver_1007_0(Etw):
    pattern = Struct(
        "Code" / Int32ul,
        "hr" / Int32ul
    )


@declare(guid=guid("21b7c16e-c5af-4a69-a74a-7245481c1b97"), event_id=1008, version=0)
class Microsoft_Windows_WPD_MTPClassDriver_1008_0(Etw):
    pattern = Struct(
        "Code" / Int32ul
    )


@declare(guid=guid("21b7c16e-c5af-4a69-a74a-7245481c1b97"), event_id=1009, version=0)
class Microsoft_Windows_WPD_MTPClassDriver_1009_0(Etw):
    pattern = Struct(
        "ExpectedValue" / Int32ul,
        "ActualValue" / Int32ul
    )


@declare(guid=guid("21b7c16e-c5af-4a69-a74a-7245481c1b97"), event_id=1010, version=0)
class Microsoft_Windows_WPD_MTPClassDriver_1010_0(Etw):
    pattern = Struct(
        "ExpectedValue" / Int32ul,
        "ActualValue" / Int32ul
    )


@declare(guid=guid("21b7c16e-c5af-4a69-a74a-7245481c1b97"), event_id=1011, version=0)
class Microsoft_Windows_WPD_MTPClassDriver_1011_0(Etw):
    pattern = Struct(
        "Code" / Int32ul,
        "Prop" / Int32ul,
        "Offset" / Int32ul
    )


@declare(guid=guid("21b7c16e-c5af-4a69-a74a-7245481c1b97"), event_id=1015, version=0)
class Microsoft_Windows_WPD_MTPClassDriver_1015_0(Etw):
    pattern = Struct(
        "Code" / Int32ul,
        "Prop" / Int32ul,
        "Offset" / Int32ul
    )


@declare(guid=guid("21b7c16e-c5af-4a69-a74a-7245481c1b97"), event_id=1016, version=0)
class Microsoft_Windows_WPD_MTPClassDriver_1016_0(Etw):
    pattern = Struct(
        "Code" / Int32ul,
        "Offset" / Int32ul
    )


@declare(guid=guid("21b7c16e-c5af-4a69-a74a-7245481c1b97"), event_id=1017, version=0)
class Microsoft_Windows_WPD_MTPClassDriver_1017_0(Etw):
    pattern = Struct(
        "Code" / Int32ul,
        "Prop" / Int32ul,
        "Offset" / Int32ul
    )


@declare(guid=guid("21b7c16e-c5af-4a69-a74a-7245481c1b97"), event_id=1022, version=0)
class Microsoft_Windows_WPD_MTPClassDriver_1022_0(Etw):
    pattern = Struct(
        "Offset" / Int32ul
    )


@declare(guid=guid("21b7c16e-c5af-4a69-a74a-7245481c1b97"), event_id=1023, version=0)
class Microsoft_Windows_WPD_MTPClassDriver_1023_0(Etw):
    pattern = Struct(
        "ID" / Int32ul,
        "Offset" / Int32ul
    )


@declare(guid=guid("21b7c16e-c5af-4a69-a74a-7245481c1b97"), event_id=1024, version=0)
class Microsoft_Windows_WPD_MTPClassDriver_1024_0(Etw):
    pattern = Struct(
        "ID" / Int32ul,
        "Offset" / Int32ul
    )


@declare(guid=guid("21b7c16e-c5af-4a69-a74a-7245481c1b97"), event_id=1025, version=0)
class Microsoft_Windows_WPD_MTPClassDriver_1025_0(Etw):
    pattern = Struct(
        "ID" / Int32ul,
        "Offset" / Int32ul
    )


@declare(guid=guid("21b7c16e-c5af-4a69-a74a-7245481c1b97"), event_id=1026, version=0)
class Microsoft_Windows_WPD_MTPClassDriver_1026_0(Etw):
    pattern = Struct(
        "ID" / Int32ul,
        "Offset" / Int32ul
    )


@declare(guid=guid("21b7c16e-c5af-4a69-a74a-7245481c1b97"), event_id=1028, version=0)
class Microsoft_Windows_WPD_MTPClassDriver_1028_0(Etw):
    pattern = Struct(
        "Code" / Int32ul
    )


@declare(guid=guid("21b7c16e-c5af-4a69-a74a-7245481c1b97"), event_id=1029, version=0)
class Microsoft_Windows_WPD_MTPClassDriver_1029_0(Etw):
    pattern = Struct(
        "Expected" / Int32ul,
        "Actual" / Int32ul
    )


@declare(guid=guid("21b7c16e-c5af-4a69-a74a-7245481c1b97"), event_id=1030, version=0)
class Microsoft_Windows_WPD_MTPClassDriver_1030_0(Etw):
    pattern = Struct(
        "Expected" / Int32ul,
        "Actual" / Int32ul
    )


@declare(guid=guid("21b7c16e-c5af-4a69-a74a-7245481c1b97"), event_id=1031, version=0)
class Microsoft_Windows_WPD_MTPClassDriver_1031_0(Etw):
    pattern = Struct(
        "Offset" / Int32ul
    )


@declare(guid=guid("21b7c16e-c5af-4a69-a74a-7245481c1b97"), event_id=1032, version=0)
class Microsoft_Windows_WPD_MTPClassDriver_1032_0(Etw):
    pattern = Struct(
        "Expected" / Int32ul,
        "Actual" / Int32ul
    )


@declare(guid=guid("21b7c16e-c5af-4a69-a74a-7245481c1b97"), event_id=1033, version=0)
class Microsoft_Windows_WPD_MTPClassDriver_1033_0(Etw):
    pattern = Struct(
        "Expected" / Int32ul,
        "Actual" / Int32ul
    )


@declare(guid=guid("21b7c16e-c5af-4a69-a74a-7245481c1b97"), event_id=1034, version=0)
class Microsoft_Windows_WPD_MTPClassDriver_1034_0(Etw):
    pattern = Struct(
        "Offset" / Int32ul
    )


@declare(guid=guid("21b7c16e-c5af-4a69-a74a-7245481c1b97"), event_id=1035, version=0)
class Microsoft_Windows_WPD_MTPClassDriver_1035_0(Etw):
    pattern = Struct(
        "Expected" / Int32ul,
        "Actual" / Int32ul
    )


@declare(guid=guid("21b7c16e-c5af-4a69-a74a-7245481c1b97"), event_id=1036, version=0)
class Microsoft_Windows_WPD_MTPClassDriver_1036_0(Etw):
    pattern = Struct(
        "Expected" / Int32ul,
        "Actual" / Int32ul
    )


@declare(guid=guid("21b7c16e-c5af-4a69-a74a-7245481c1b97"), event_id=1037, version=0)
class Microsoft_Windows_WPD_MTPClassDriver_1037_0(Etw):
    pattern = Struct(
        "Offset" / Int32ul
    )


@declare(guid=guid("21b7c16e-c5af-4a69-a74a-7245481c1b97"), event_id=1038, version=0)
class Microsoft_Windows_WPD_MTPClassDriver_1038_0(Etw):
    pattern = Struct(
        "Expected" / Int32ul,
        "Actual" / Int32ul
    )


@declare(guid=guid("21b7c16e-c5af-4a69-a74a-7245481c1b97"), event_id=1039, version=0)
class Microsoft_Windows_WPD_MTPClassDriver_1039_0(Etw):
    pattern = Struct(
        "Expected" / Int32ul,
        "Actual" / Int32ul
    )


@declare(guid=guid("21b7c16e-c5af-4a69-a74a-7245481c1b97"), event_id=1040, version=0)
class Microsoft_Windows_WPD_MTPClassDriver_1040_0(Etw):
    pattern = Struct(
        "Offset" / Int32ul
    )


@declare(guid=guid("21b7c16e-c5af-4a69-a74a-7245481c1b97"), event_id=1041, version=0)
class Microsoft_Windows_WPD_MTPClassDriver_1041_0(Etw):
    pattern = Struct(
        "PKeyGuid" / WString,
        "PKeyId" / Int32ul
    )


@declare(guid=guid("21b7c16e-c5af-4a69-a74a-7245481c1b97"), event_id=1042, version=0)
class Microsoft_Windows_WPD_MTPClassDriver_1042_0(Etw):
    pattern = Struct(
        "Guid" / WString
    )


@declare(guid=guid("21b7c16e-c5af-4a69-a74a-7245481c1b97"), event_id=1043, version=0)
class Microsoft_Windows_WPD_MTPClassDriver_1043_0(Etw):
    pattern = Struct(
        "Guid" / WString
    )


@declare(guid=guid("21b7c16e-c5af-4a69-a74a-7245481c1b97"), event_id=1044, version=0)
class Microsoft_Windows_WPD_MTPClassDriver_1044_0(Etw):
    pattern = Struct(
        "Guid" / WString
    )


@declare(guid=guid("21b7c16e-c5af-4a69-a74a-7245481c1b97"), event_id=1045, version=0)
class Microsoft_Windows_WPD_MTPClassDriver_1045_0(Etw):
    pattern = Struct(
        "Code" / Int32ul,
        "Prop" / Int32ul
    )


@declare(guid=guid("21b7c16e-c5af-4a69-a74a-7245481c1b97"), event_id=1046, version=0)
class Microsoft_Windows_WPD_MTPClassDriver_1046_0(Etw):
    pattern = Struct(
        "PKeyGuid" / WString,
        "PKeyId" / Int32ul,
        "CurrentCode" / Int32ul,
        "OriginalCode" / Int32ul
    )


@declare(guid=guid("21b7c16e-c5af-4a69-a74a-7245481c1b97"), event_id=1049, version=0)
class Microsoft_Windows_WPD_MTPClassDriver_1049_0(Etw):
    pattern = Struct(
        "Code" / Int32ul
    )


@declare(guid=guid("21b7c16e-c5af-4a69-a74a-7245481c1b97"), event_id=1050, version=0)
class Microsoft_Windows_WPD_MTPClassDriver_1050_0(Etw):
    pattern = Struct(
        "Offset" / Int32ul
    )


@declare(guid=guid("21b7c16e-c5af-4a69-a74a-7245481c1b97"), event_id=1051, version=0)
class Microsoft_Windows_WPD_MTPClassDriver_1051_0(Etw):
    pattern = Struct(
        "Code" / Int32ul
    )


@declare(guid=guid("21b7c16e-c5af-4a69-a74a-7245481c1b97"), event_id=1052, version=0)
class Microsoft_Windows_WPD_MTPClassDriver_1052_0(Etw):
    pattern = Struct(
        "PKeyGuid" / WString,
        "PKeyId" / Int32ul,
        "ID" / Int32ul
    )


@declare(guid=guid("21b7c16e-c5af-4a69-a74a-7245481c1b97"), event_id=1053, version=0)
class Microsoft_Windows_WPD_MTPClassDriver_1053_0(Etw):
    pattern = Struct(
        "PKeyGuid" / WString,
        "ID" / Int32ul
    )


@declare(guid=guid("21b7c16e-c5af-4a69-a74a-7245481c1b97"), event_id=1054, version=0)
class Microsoft_Windows_WPD_MTPClassDriver_1054_0(Etw):
    pattern = Struct(
        "PKeyGuid" / WString,
        "ID" / Int32ul
    )


@declare(guid=guid("21b7c16e-c5af-4a69-a74a-7245481c1b97"), event_id=1055, version=0)
class Microsoft_Windows_WPD_MTPClassDriver_1055_0(Etw):
    pattern = Struct(
        "PKeyGuid" / WString,
        "ID" / Int32ul
    )


@declare(guid=guid("21b7c16e-c5af-4a69-a74a-7245481c1b97"), event_id=1056, version=0)
class Microsoft_Windows_WPD_MTPClassDriver_1056_0(Etw):
    pattern = Struct(
        "Code" / Int32ul
    )


@declare(guid=guid("21b7c16e-c5af-4a69-a74a-7245481c1b97"), event_id=1057, version=0)
class Microsoft_Windows_WPD_MTPClassDriver_1057_0(Etw):
    pattern = Struct(
        "PKeyGuid" / WString,
        "ID" / Int32ul
    )


@declare(guid=guid("21b7c16e-c5af-4a69-a74a-7245481c1b97"), event_id=1058, version=0)
class Microsoft_Windows_WPD_MTPClassDriver_1058_0(Etw):
    pattern = Struct(
        "PKeyGuid" / WString,
        "ID" / Int32ul
    )


@declare(guid=guid("21b7c16e-c5af-4a69-a74a-7245481c1b97"), event_id=1059, version=0)
class Microsoft_Windows_WPD_MTPClassDriver_1059_0(Etw):
    pattern = Struct(
        "ID" / Int32ul,
        "Code" / Int32ul
    )


@declare(guid=guid("21b7c16e-c5af-4a69-a74a-7245481c1b97"), event_id=1060, version=0)
class Microsoft_Windows_WPD_MTPClassDriver_1060_0(Etw):
    pattern = Struct(
        "Offset" / Int32ul
    )


@declare(guid=guid("21b7c16e-c5af-4a69-a74a-7245481c1b97"), event_id=1063, version=0)
class Microsoft_Windows_WPD_MTPClassDriver_1063_0(Etw):
    pattern = Struct(
        "PKeyGuid" / WString,
        "ID" / Int32ul
    )


@declare(guid=guid("21b7c16e-c5af-4a69-a74a-7245481c1b97"), event_id=1065, version=0)
class Microsoft_Windows_WPD_MTPClassDriver_1065_0(Etw):
    pattern = Struct(
        "Code" / Int32ul,
        "Offset" / Int32ul
    )


@declare(guid=guid("21b7c16e-c5af-4a69-a74a-7245481c1b97"), event_id=1066, version=0)
class Microsoft_Windows_WPD_MTPClassDriver_1066_0(Etw):
    pattern = Struct(
        "Code" / Int32ul
    )


@declare(guid=guid("21b7c16e-c5af-4a69-a74a-7245481c1b97"), event_id=1067, version=0)
class Microsoft_Windows_WPD_MTPClassDriver_1067_0(Etw):
    pattern = Struct(
        "Offset" / Int32ul
    )


@declare(guid=guid("21b7c16e-c5af-4a69-a74a-7245481c1b97"), event_id=1068, version=0)
class Microsoft_Windows_WPD_MTPClassDriver_1068_0(Etw):
    pattern = Struct(
        "Offset" / Int32ul
    )


@declare(guid=guid("21b7c16e-c5af-4a69-a74a-7245481c1b97"), event_id=2000, version=0)
class Microsoft_Windows_WPD_MTPClassDriver_2000_0(Etw):
    pattern = Struct(
        "SessionID" / Int32ul,
        "TransactionID" / Int32ul,
        "MTP_Opcode" / Int16ul,
        "MTP_Command_Param_count" / Int32ul,
        "MTP_Command_Params" / Int32ul
    )


@declare(guid=guid("21b7c16e-c5af-4a69-a74a-7245481c1b97"), event_id=2001, version=0)
class Microsoft_Windows_WPD_MTPClassDriver_2001_0(Etw):
    pattern = Struct(
        "SessionID" / Int32ul,
        "TransactionID" / Int32ul,
        "MTP_Opcode" / Int16ul,
        "MTP_Command_Param_count" / Int32ul,
        "MTP_Command_Params" / Int32ul,
        "MTP_Response_Retrieval_HR_From_Transport" / Int32ul,
        "MTP_Response_Code" / Int16ul,
        "MTP_Response_Param_count" / Int32ul,
        "MTP_Response_Params" / Int32ul,
        "MTP_Data_Length" / Int32ul,
        "MTP_Data_Buffer" / Bytes(lambda this: this.MTP_Data_Length)
    )


@declare(guid=guid("21b7c16e-c5af-4a69-a74a-7245481c1b97"), event_id=2002, version=0)
class Microsoft_Windows_WPD_MTPClassDriver_2002_0(Etw):
    pattern = Struct(
        "SessionID" / Int32ul,
        "TransactionID" / Int32ul,
        "MTP_Opcode" / Int16ul,
        "MTP_Command_Param_count" / Int32ul,
        "MTP_Command_Params" / Int32ul,
        "MTP_Response_Code" / Int16ul,
        "MTP_Response_Param_count" / Int32ul,
        "MTP_Response_Params" / Int32ul,
        "MTP_DatatypeOfPropValue" / Int16ul,
        "MTP_Data_Length" / Int32ul,
        "MTP_Data_Buffer" / Bytes(lambda this: this.MTP_Data_Length)
    )


@declare(guid=guid("21b7c16e-c5af-4a69-a74a-7245481c1b97"), event_id=2003, version=0)
class Microsoft_Windows_WPD_MTPClassDriver_2003_0(Etw):
    pattern = Struct(
        "SessionID" / Int32ul,
        "TransactionID" / Int32ul,
        "MTP_Response_Retrieval_HR_From_Transport" / Int32ul,
        "MTP_Response_Code" / Int16ul,
        "MTP_Response_Param_count" / Int32ul,
        "MTP_Response_Params" / Int32ul
    )


@declare(guid=guid("21b7c16e-c5af-4a69-a74a-7245481c1b97"), event_id=2004, version=0)
class Microsoft_Windows_WPD_MTPClassDriver_2004_0(Etw):
    pattern = Struct(
        "SessionID" / Int32ul,
        "TransactionID" / Int32ul,
        "MTP_Event_Retrieval_HR_From_Transport" / Int32ul,
        "MTP_Event_Code" / Int16ul,
        "MTP_Event_Param_count" / Int32ul,
        "MTP_Event_Params" / Int32ul
    )


@declare(guid=guid("21b7c16e-c5af-4a69-a74a-7245481c1b97"), event_id=2005, version=0)
class Microsoft_Windows_WPD_MTPClassDriver_2005_0(Etw):
    pattern = Struct(
        "MTPBulkGetObjProps_size" / Int32ul,
        "MTPBulkGetObjProps_buffer" / Bytes(lambda this: this.MTPBulkGetObjProps_size)
    )


@declare(guid=guid("21b7c16e-c5af-4a69-a74a-7245481c1b97"), event_id=2006, version=0)
class Microsoft_Windows_WPD_MTPClassDriver_2006_0(Etw):
    pattern = Struct(
        "SessionID" / Int32ul,
        "TransactionID" / Int32ul,
        "MTP_Opcode" / Int16ul,
        "MTP_Command_Param_count" / Int32ul,
        "MTP_Command_Params" / Int32ul,
        "MTP_Data_Length" / Int32ul,
        "MTP_Data_Buffer" / Bytes(lambda this: this.MTP_Data_Length)
    )


@declare(guid=guid("21b7c16e-c5af-4a69-a74a-7245481c1b97"), event_id=2007, version=0)
class Microsoft_Windows_WPD_MTPClassDriver_2007_0(Etw):
    pattern = Struct(
        "SessionID" / Int32ul,
        "TransactionID" / Int32ul,
        "MTP_Opcode" / Int16ul,
        "MTP_Command_Param_count" / Int32ul,
        "MTP_Command_Params" / Int32ul,
        "MTP_DatatypeOfPropValue" / Int16ul,
        "MTP_Data_Length" / Int32ul,
        "MTP_Data_Buffer" / Bytes(lambda this: this.MTP_Data_Length)
    )

