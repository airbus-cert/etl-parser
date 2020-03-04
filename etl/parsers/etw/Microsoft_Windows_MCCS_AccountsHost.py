# -*- coding: utf-8 -*-
"""
Microsoft-Windows-MCCS-AccountsHost
GUID : 04eccf8e-8490-4ad1-8ed5-0ae7750e69e6
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("04eccf8e-8490-4ad1-8ed5-0ae7750e69e6"), event_id=1, version=0)
class Microsoft_Windows_MCCS_AccountsHost_1_0(Etw):
    pattern = Struct(
        "P1_HexInt32" / Int32sl,
        "P2_String" / CString,
        "P3_UInt32" / Int32ul
    )


@declare(guid=guid("04eccf8e-8490-4ad1-8ed5-0ae7750e69e6"), event_id=2, version=0)
class Microsoft_Windows_MCCS_AccountsHost_2_0(Etw):
    pattern = Struct(
        "P1_HexInt32" / Int32sl,
        "P2_String" / CString,
        "P3_UInt32" / Int32ul
    )


@declare(guid=guid("04eccf8e-8490-4ad1-8ed5-0ae7750e69e6"), event_id=2000, version=0)
class Microsoft_Windows_MCCS_AccountsHost_2000_0(Etw):
    pattern = Struct(
        "Prop_String" / WString,
        "Prop_UInt32" / Int32ul
    )


@declare(guid=guid("04eccf8e-8490-4ad1-8ed5-0ae7750e69e6"), event_id=2051, version=0)
class Microsoft_Windows_MCCS_AccountsHost_2051_0(Etw):
    pattern = Struct(
        "Prop_UInt32_1" / Int32ul,
        "Prop_UInt32_2" / Int32ul
    )


@declare(guid=guid("04eccf8e-8490-4ad1-8ed5-0ae7750e69e6"), event_id=2052, version=0)
class Microsoft_Windows_MCCS_AccountsHost_2052_0(Etw):
    pattern = Struct(
        "Prop_UInt32_1" / Int32ul,
        "Prop_UInt32_2" / Int32ul
    )


@declare(guid=guid("04eccf8e-8490-4ad1-8ed5-0ae7750e69e6"), event_id=2053, version=0)
class Microsoft_Windows_MCCS_AccountsHost_2053_0(Etw):
    pattern = Struct(
        "Prop_UInt32_1" / Int32ul,
        "Prop_UInt32_2" / Int32ul
    )


@declare(guid=guid("04eccf8e-8490-4ad1-8ed5-0ae7750e69e6"), event_id=2061, version=0)
class Microsoft_Windows_MCCS_AccountsHost_2061_0(Etw):
    pattern = Struct(
        "Prop_String" / WString,
        "Prop_UInt32" / Int32ul
    )


@declare(guid=guid("04eccf8e-8490-4ad1-8ed5-0ae7750e69e6"), event_id=4010, version=0)
class Microsoft_Windows_MCCS_AccountsHost_4010_0(Etw):
    pattern = Struct(
        "Prop_UInt32" / Int32ul
    )


@declare(guid=guid("04eccf8e-8490-4ad1-8ed5-0ae7750e69e6"), event_id=4011, version=0)
class Microsoft_Windows_MCCS_AccountsHost_4011_0(Etw):
    pattern = Struct(
        "Prop_UInt32" / Int32ul
    )


@declare(guid=guid("04eccf8e-8490-4ad1-8ed5-0ae7750e69e6"), event_id=4012, version=0)
class Microsoft_Windows_MCCS_AccountsHost_4012_0(Etw):
    pattern = Struct(
        "Prop_UInt32" / Int32ul
    )


@declare(guid=guid("04eccf8e-8490-4ad1-8ed5-0ae7750e69e6"), event_id=4014, version=0)
class Microsoft_Windows_MCCS_AccountsHost_4014_0(Etw):
    pattern = Struct(
        "Int32" / Int32sl
    )


@declare(guid=guid("04eccf8e-8490-4ad1-8ed5-0ae7750e69e6"), event_id=4015, version=0)
class Microsoft_Windows_MCCS_AccountsHost_4015_0(Etw):
    pattern = Struct(
        "Int32" / Int32sl
    )


@declare(guid=guid("04eccf8e-8490-4ad1-8ed5-0ae7750e69e6"), event_id=4016, version=0)
class Microsoft_Windows_MCCS_AccountsHost_4016_0(Etw):
    pattern = Struct(
        "Int32" / Int32sl
    )


@declare(guid=guid("04eccf8e-8490-4ad1-8ed5-0ae7750e69e6"), event_id=4017, version=0)
class Microsoft_Windows_MCCS_AccountsHost_4017_0(Etw):
    pattern = Struct(
        "Prop_String" / WString
    )


@declare(guid=guid("04eccf8e-8490-4ad1-8ed5-0ae7750e69e6"), event_id=4018, version=0)
class Microsoft_Windows_MCCS_AccountsHost_4018_0(Etw):
    pattern = Struct(
        "Prop_String" / WString
    )


@declare(guid=guid("04eccf8e-8490-4ad1-8ed5-0ae7750e69e6"), event_id=4019, version=0)
class Microsoft_Windows_MCCS_AccountsHost_4019_0(Etw):
    pattern = Struct(
        "Prop_ptr" / Int64ul
    )


@declare(guid=guid("04eccf8e-8490-4ad1-8ed5-0ae7750e69e6"), event_id=4023, version=0)
class Microsoft_Windows_MCCS_AccountsHost_4023_0(Etw):
    pattern = Struct(
        "Prop_UInt32" / Int32ul
    )


@declare(guid=guid("04eccf8e-8490-4ad1-8ed5-0ae7750e69e6"), event_id=4024, version=0)
class Microsoft_Windows_MCCS_AccountsHost_4024_0(Etw):
    pattern = Struct(
        "Prop_UInt32" / Int32ul
    )


@declare(guid=guid("04eccf8e-8490-4ad1-8ed5-0ae7750e69e6"), event_id=4025, version=0)
class Microsoft_Windows_MCCS_AccountsHost_4025_0(Etw):
    pattern = Struct(
        "Prop_uint" / Int32ul,
        "Prop_hr" / Int32sl
    )


@declare(guid=guid("04eccf8e-8490-4ad1-8ed5-0ae7750e69e6"), event_id=4026, version=0)
class Microsoft_Windows_MCCS_AccountsHost_4026_0(Etw):
    pattern = Struct(
        "Prop_hr" / Int32sl
    )


@declare(guid=guid("04eccf8e-8490-4ad1-8ed5-0ae7750e69e6"), event_id=4027, version=0)
class Microsoft_Windows_MCCS_AccountsHost_4027_0(Etw):
    pattern = Struct(
        "Prop_String" / WString
    )


@declare(guid=guid("04eccf8e-8490-4ad1-8ed5-0ae7750e69e6"), event_id=4028, version=0)
class Microsoft_Windows_MCCS_AccountsHost_4028_0(Etw):
    pattern = Struct(
        "Prop_String" / WString
    )


@declare(guid=guid("04eccf8e-8490-4ad1-8ed5-0ae7750e69e6"), event_id=4029, version=0)
class Microsoft_Windows_MCCS_AccountsHost_4029_0(Etw):
    pattern = Struct(
        "Prop_String" / WString
    )


@declare(guid=guid("04eccf8e-8490-4ad1-8ed5-0ae7750e69e6"), event_id=4030, version=0)
class Microsoft_Windows_MCCS_AccountsHost_4030_0(Etw):
    pattern = Struct(
        "Prop_String" / WString
    )


@declare(guid=guid("04eccf8e-8490-4ad1-8ed5-0ae7750e69e6"), event_id=4031, version=0)
class Microsoft_Windows_MCCS_AccountsHost_4031_0(Etw):
    pattern = Struct(
        "Prop_String" / WString
    )


@declare(guid=guid("04eccf8e-8490-4ad1-8ed5-0ae7750e69e6"), event_id=4032, version=0)
class Microsoft_Windows_MCCS_AccountsHost_4032_0(Etw):
    pattern = Struct(
        "Prop_String" / WString
    )


@declare(guid=guid("04eccf8e-8490-4ad1-8ed5-0ae7750e69e6"), event_id=4033, version=0)
class Microsoft_Windows_MCCS_AccountsHost_4033_0(Etw):
    pattern = Struct(
        "Prop_String" / WString
    )


@declare(guid=guid("04eccf8e-8490-4ad1-8ed5-0ae7750e69e6"), event_id=4034, version=0)
class Microsoft_Windows_MCCS_AccountsHost_4034_0(Etw):
    pattern = Struct(
        "Prop_String" / WString
    )


@declare(guid=guid("04eccf8e-8490-4ad1-8ed5-0ae7750e69e6"), event_id=4036, version=0)
class Microsoft_Windows_MCCS_AccountsHost_4036_0(Etw):
    pattern = Struct(
        "Prop_String" / WString
    )


@declare(guid=guid("04eccf8e-8490-4ad1-8ed5-0ae7750e69e6"), event_id=4047, version=0)
class Microsoft_Windows_MCCS_AccountsHost_4047_0(Etw):
    pattern = Struct(
        "Prop_string" / WString,
        "Prop_int" / Int32sl
    )


@declare(guid=guid("04eccf8e-8490-4ad1-8ed5-0ae7750e69e6"), event_id=4048, version=0)
class Microsoft_Windows_MCCS_AccountsHost_4048_0(Etw):
    pattern = Struct(
        "Prop_String" / WString
    )


@declare(guid=guid("04eccf8e-8490-4ad1-8ed5-0ae7750e69e6"), event_id=4052, version=0)
class Microsoft_Windows_MCCS_AccountsHost_4052_0(Etw):
    pattern = Struct(
        "Prop_ptr" / Int64ul,
        "Prop_unit" / Int32ul
    )


@declare(guid=guid("04eccf8e-8490-4ad1-8ed5-0ae7750e69e6"), event_id=4053, version=0)
class Microsoft_Windows_MCCS_AccountsHost_4053_0(Etw):
    pattern = Struct(
        "Prop_ptr" / Int64ul
    )


@declare(guid=guid("04eccf8e-8490-4ad1-8ed5-0ae7750e69e6"), event_id=4054, version=0)
class Microsoft_Windows_MCCS_AccountsHost_4054_0(Etw):
    pattern = Struct(
        "Prop_ptr" / Int64ul
    )


@declare(guid=guid("04eccf8e-8490-4ad1-8ed5-0ae7750e69e6"), event_id=4055, version=0)
class Microsoft_Windows_MCCS_AccountsHost_4055_0(Etw):
    pattern = Struct(
        "Prop_string" / CString
    )


@declare(guid=guid("04eccf8e-8490-4ad1-8ed5-0ae7750e69e6"), event_id=4056, version=0)
class Microsoft_Windows_MCCS_AccountsHost_4056_0(Etw):
    pattern = Struct(
        "Prop_UInt32" / Int32ul
    )


@declare(guid=guid("04eccf8e-8490-4ad1-8ed5-0ae7750e69e6"), event_id=4057, version=0)
class Microsoft_Windows_MCCS_AccountsHost_4057_0(Etw):
    pattern = Struct(
        "Prop_UINT_1" / Int32ul,
        "Prop_UINT_2" / Int32ul
    )


@declare(guid=guid("04eccf8e-8490-4ad1-8ed5-0ae7750e69e6"), event_id=5001, version=0)
class Microsoft_Windows_MCCS_AccountsHost_5001_0(Etw):
    pattern = Struct(
        "Prop_UInt32" / Int32ul
    )


@declare(guid=guid("04eccf8e-8490-4ad1-8ed5-0ae7750e69e6"), event_id=5003, version=0)
class Microsoft_Windows_MCCS_AccountsHost_5003_0(Etw):
    pattern = Struct(
        "P1_HexInt32" / Int32sl,
        "P2_String" / CString,
        "P3_UInt32" / Int32ul
    )


@declare(guid=guid("04eccf8e-8490-4ad1-8ed5-0ae7750e69e6"), event_id=5004, version=0)
class Microsoft_Windows_MCCS_AccountsHost_5004_0(Etw):
    pattern = Struct(
        "Prop_UInt32" / Int32ul
    )


@declare(guid=guid("04eccf8e-8490-4ad1-8ed5-0ae7750e69e6"), event_id=5006, version=0)
class Microsoft_Windows_MCCS_AccountsHost_5006_0(Etw):
    pattern = Struct(
        "Prop_UInt32" / Int32ul
    )


@declare(guid=guid("04eccf8e-8490-4ad1-8ed5-0ae7750e69e6"), event_id=7001, version=0)
class Microsoft_Windows_MCCS_AccountsHost_7001_0(Etw):
    pattern = Struct(
        "Prop_String" / WString
    )


@declare(guid=guid("04eccf8e-8490-4ad1-8ed5-0ae7750e69e6"), event_id=7002, version=0)
class Microsoft_Windows_MCCS_AccountsHost_7002_0(Etw):
    pattern = Struct(
        "Prop_String" / WString,
        "Prop_UInt32" / Int32ul
    )


@declare(guid=guid("04eccf8e-8490-4ad1-8ed5-0ae7750e69e6"), event_id=7003, version=0)
class Microsoft_Windows_MCCS_AccountsHost_7003_0(Etw):
    pattern = Struct(
        "Prop_String" / WString,
        "Prop_UInt32" / Int32ul
    )


@declare(guid=guid("04eccf8e-8490-4ad1-8ed5-0ae7750e69e6"), event_id=7005, version=0)
class Microsoft_Windows_MCCS_AccountsHost_7005_0(Etw):
    pattern = Struct(
        "Prop_String" / WString
    )


@declare(guid=guid("04eccf8e-8490-4ad1-8ed5-0ae7750e69e6"), event_id=7006, version=0)
class Microsoft_Windows_MCCS_AccountsHost_7006_0(Etw):
    pattern = Struct(
        "Prop_String" / WString,
        "Prop_UInt32" / Int32ul
    )


@declare(guid=guid("04eccf8e-8490-4ad1-8ed5-0ae7750e69e6"), event_id=7007, version=0)
class Microsoft_Windows_MCCS_AccountsHost_7007_0(Etw):
    pattern = Struct(
        "Prop_String" / WString,
        "Prop_UInt32_1" / Int32ul,
        "Prop_UInt32_2" / Int32ul
    )


@declare(guid=guid("04eccf8e-8490-4ad1-8ed5-0ae7750e69e6"), event_id=7008, version=0)
class Microsoft_Windows_MCCS_AccountsHost_7008_0(Etw):
    pattern = Struct(
        "Prop_String" / WString,
        "Prop_UInt32" / Int32ul
    )


@declare(guid=guid("04eccf8e-8490-4ad1-8ed5-0ae7750e69e6"), event_id=7009, version=0)
class Microsoft_Windows_MCCS_AccountsHost_7009_0(Etw):
    pattern = Struct(
        "Prop_UINT_1" / Int32ul,
        "Prop_UINT_2" / Int32ul
    )


@declare(guid=guid("04eccf8e-8490-4ad1-8ed5-0ae7750e69e6"), event_id=7010, version=0)
class Microsoft_Windows_MCCS_AccountsHost_7010_0(Etw):
    pattern = Struct(
        "Prop_UInt32_1" / Int32ul,
        "Prop_UInt32_2" / Int32ul
    )


@declare(guid=guid("04eccf8e-8490-4ad1-8ed5-0ae7750e69e6"), event_id=7011, version=0)
class Microsoft_Windows_MCCS_AccountsHost_7011_0(Etw):
    pattern = Struct(
        "Prop_UInt32_1" / Int32ul,
        "Prop_UInt32_2" / Int32ul
    )


@declare(guid=guid("04eccf8e-8490-4ad1-8ed5-0ae7750e69e6"), event_id=7012, version=0)
class Microsoft_Windows_MCCS_AccountsHost_7012_0(Etw):
    pattern = Struct(
        "Prop_String" / WString
    )


@declare(guid=guid("04eccf8e-8490-4ad1-8ed5-0ae7750e69e6"), event_id=7015, version=0)
class Microsoft_Windows_MCCS_AccountsHost_7015_0(Etw):
    pattern = Struct(
        "Prop_UInt32" / Int32ul
    )


@declare(guid=guid("04eccf8e-8490-4ad1-8ed5-0ae7750e69e6"), event_id=7022, version=0)
class Microsoft_Windows_MCCS_AccountsHost_7022_0(Etw):
    pattern = Struct(
        "P1_HexInt32" / Int32sl,
        "P2_String" / CString,
        "P3_UInt32" / Int32ul
    )


@declare(guid=guid("04eccf8e-8490-4ad1-8ed5-0ae7750e69e6"), event_id=7023, version=0)
class Microsoft_Windows_MCCS_AccountsHost_7023_0(Etw):
    pattern = Struct(
        "Prop_UInt32" / Int32ul
    )


@declare(guid=guid("04eccf8e-8490-4ad1-8ed5-0ae7750e69e6"), event_id=7024, version=0)
class Microsoft_Windows_MCCS_AccountsHost_7024_0(Etw):
    pattern = Struct(
        "Prop_UInt32_1" / Int32ul,
        "Prop_UInt32_2" / Int32ul
    )


@declare(guid=guid("04eccf8e-8490-4ad1-8ed5-0ae7750e69e6"), event_id=7025, version=0)
class Microsoft_Windows_MCCS_AccountsHost_7025_0(Etw):
    pattern = Struct(
        "Prop_String1" / WString,
        "Prop_UInt32_2" / Int32ul,
        "Prop_String3" / CString,
        "Prop_UInt32_4" / Int32ul,
        "Prop_UInt32_5" / Int32ul,
        "Prop_UInt32_6" / Int32ul
    )


@declare(guid=guid("04eccf8e-8490-4ad1-8ed5-0ae7750e69e6"), event_id=7026, version=0)
class Microsoft_Windows_MCCS_AccountsHost_7026_0(Etw):
    pattern = Struct(
        "Prop_String" / WString
    )


@declare(guid=guid("04eccf8e-8490-4ad1-8ed5-0ae7750e69e6"), event_id=7027, version=0)
class Microsoft_Windows_MCCS_AccountsHost_7027_0(Etw):
    pattern = Struct(
        "Prop_String" / WString
    )


@declare(guid=guid("04eccf8e-8490-4ad1-8ed5-0ae7750e69e6"), event_id=7028, version=0)
class Microsoft_Windows_MCCS_AccountsHost_7028_0(Etw):
    pattern = Struct(
        "Prop_String1" / WString,
        "Prop_UInt32_2" / Int32ul,
        "Prop_String3" / CString,
        "Prop_UInt32_4" / Int32ul,
        "Prop_UInt32_5" / Int32ul,
        "Prop_UInt32_6" / Int32ul
    )


@declare(guid=guid("04eccf8e-8490-4ad1-8ed5-0ae7750e69e6"), event_id=7029, version=0)
class Microsoft_Windows_MCCS_AccountsHost_7029_0(Etw):
    pattern = Struct(
        "Prop_String" / WString,
        "Prop_UInt32" / Int32ul
    )


@declare(guid=guid("04eccf8e-8490-4ad1-8ed5-0ae7750e69e6"), event_id=7030, version=0)
class Microsoft_Windows_MCCS_AccountsHost_7030_0(Etw):
    pattern = Struct(
        "Prop_String" / WString,
        "Prop_UInt32_1" / Int32ul,
        "Prop_UInt32_2" / Int32ul
    )


@declare(guid=guid("04eccf8e-8490-4ad1-8ed5-0ae7750e69e6"), event_id=7031, version=0)
class Microsoft_Windows_MCCS_AccountsHost_7031_0(Etw):
    pattern = Struct(
        "Prop_SubmissionID0" / Int64ul,
        "Prop_SubmissionID1" / Int64ul
    )


@declare(guid=guid("04eccf8e-8490-4ad1-8ed5-0ae7750e69e6"), event_id=7032, version=0)
class Microsoft_Windows_MCCS_AccountsHost_7032_0(Etw):
    pattern = Struct(
        "Prop_SubmissionID0" / Int64ul,
        "Prop_SubmissionID1" / Int64ul
    )


@declare(guid=guid("04eccf8e-8490-4ad1-8ed5-0ae7750e69e6"), event_id=7033, version=0)
class Microsoft_Windows_MCCS_AccountsHost_7033_0(Etw):
    pattern = Struct(
        "Prop_SubmissionID0" / Int64ul,
        "Prop_SubmissionID1" / Int64ul
    )


@declare(guid=guid("04eccf8e-8490-4ad1-8ed5-0ae7750e69e6"), event_id=7034, version=0)
class Microsoft_Windows_MCCS_AccountsHost_7034_0(Etw):
    pattern = Struct(
        "Prop_SubmissionID0" / Int64ul,
        "Prop_SubmissionID1" / Int64ul
    )


@declare(guid=guid("04eccf8e-8490-4ad1-8ed5-0ae7750e69e6"), event_id=7035, version=0)
class Microsoft_Windows_MCCS_AccountsHost_7035_0(Etw):
    pattern = Struct(
        "Prop_SubmissionID0" / Int64ul,
        "Prop_SubmissionID1" / Int64ul
    )


@declare(guid=guid("04eccf8e-8490-4ad1-8ed5-0ae7750e69e6"), event_id=7036, version=0)
class Microsoft_Windows_MCCS_AccountsHost_7036_0(Etw):
    pattern = Struct(
        "Prop_String" / WString
    )

