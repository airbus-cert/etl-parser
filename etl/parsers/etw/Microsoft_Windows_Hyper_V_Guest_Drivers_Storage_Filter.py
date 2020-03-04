# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Hyper-V-Guest-Drivers-Storage-Filter
GUID : 0b9fdccc-451c-449c-9bd8-6756fcc6091a
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("0b9fdccc-451c-449c-9bd8-6756fcc6091a"), event_id=1, version=0)
class Microsoft_Windows_Hyper_V_Guest_Drivers_Storage_Filter_1_0(Etw):
    pattern = Struct(
        "NTStatus" / Int32ul
    )


@declare(guid=guid("0b9fdccc-451c-449c-9bd8-6756fcc6091a"), event_id=2, version=0)
class Microsoft_Windows_Hyper_V_Guest_Drivers_Storage_Filter_2_0(Etw):
    pattern = Struct(
        "NTStatus" / Int32ul
    )


@declare(guid=guid("0b9fdccc-451c-449c-9bd8-6756fcc6091a"), event_id=3, version=0)
class Microsoft_Windows_Hyper_V_Guest_Drivers_Storage_Filter_3_0(Etw):
    pattern = Struct(
        "Location" / WString,
        "NTStatus" / Int32ul
    )


@declare(guid=guid("0b9fdccc-451c-449c-9bd8-6756fcc6091a"), event_id=4, version=0)
class Microsoft_Windows_Hyper_V_Guest_Drivers_Storage_Filter_4_0(Etw):
    pattern = Struct(
        "Location" / WString,
        "NTStatus" / Int32ul
    )


@declare(guid=guid("0b9fdccc-451c-449c-9bd8-6756fcc6091a"), event_id=202, version=1)
class Microsoft_Windows_Hyper_V_Guest_Drivers_Storage_Filter_202_1(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "Command" / Int8ul,
        "LengthOfTransferinblocks" / Int64ul,
        "LBA" / Int64ul,
        "OriginalIrp" / Int64ul
    )


@declare(guid=guid("0b9fdccc-451c-449c-9bd8-6756fcc6091a"), event_id=203, version=1)
class Microsoft_Windows_Hyper_V_Guest_Drivers_Storage_Filter_203_1(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "Command" / Int8ul,
        "LengthOfTransferinblocks" / Int64ul,
        "LBA" / Int64ul,
        "OriginalIrp" / Int64ul
    )


@declare(guid=guid("0b9fdccc-451c-449c-9bd8-6756fcc6091a"), event_id=208, version=1)
class Microsoft_Windows_Hyper_V_Guest_Drivers_Storage_Filter_208_1(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "NTStatus" / Int32ul,
        "SrbStatus" / Int8ul,
        "ScsiStatus" / Int8ul,
        "SenseKey" / Int8ul,
        "AddSense" / Int8ul,
        "AddSenseQ" / Int8ul,
        "OriginalIrp" / Int64ul
    )

