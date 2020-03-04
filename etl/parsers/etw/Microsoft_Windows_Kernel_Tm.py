# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Kernel-Tm
GUID : 4cec9c95-a65f-4591-b5c4-30100e51d870
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("4cec9c95-a65f-4591-b5c4-30100e51d870"), event_id=1, version=0)
class Microsoft_Windows_Kernel_Tm_1_0(Etw):
    pattern = Struct(
        "TxUow" / Guid,
        "TxDescriptionLength" / Int16ul,
        "TxDescription" / Bytes(lambda this: this.TxDescriptionLength),
        "ClfsStatus" / Int32ul
    )


@declare(guid=guid("4cec9c95-a65f-4591-b5c4-30100e51d870"), event_id=2, version=0)
class Microsoft_Windows_Kernel_Tm_2_0(Etw):
    pattern = Struct(
        "TxUow" / Guid,
        "TxDescriptionLength" / Int16ul,
        "TxDescription" / Bytes(lambda this: this.TxDescriptionLength),
        "RmId" / Guid,
        "RmDescriptionLength" / Int16ul,
        "RmDescription" / Bytes(lambda this: this.RmDescriptionLength)
    )


@declare(guid=guid("4cec9c95-a65f-4591-b5c4-30100e51d870"), event_id=3, version=0)
class Microsoft_Windows_Kernel_Tm_3_0(Etw):
    pattern = Struct(
        "TxUow" / Guid,
        "TxDescriptionLength" / Int16ul,
        "TxDescription" / Bytes(lambda this: this.TxDescriptionLength),
        "TmIdentity" / Guid,
        "TmLogFileNameLength" / Int16ul,
        "TmLogFileName" / Bytes(lambda this: this.TmLogFileNameLength)
    )


@declare(guid=guid("4cec9c95-a65f-4591-b5c4-30100e51d870"), event_id=4, version=0)
class Microsoft_Windows_Kernel_Tm_4_0(Etw):
    pattern = Struct(
        "TmIdentity" / Guid,
        "TmLogFileNameLength" / Int16ul,
        "TmLogFileName" / Bytes(lambda this: this.TmLogFileNameLength),
        "TxUow" / Guid,
        "TxDescriptionLength" / Int16ul,
        "TxDescription" / Bytes(lambda this: this.TxDescriptionLength)
    )

