# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Hyper-V-Guest-Drivers-IcSvc
GUID : c18672d1-dc18-4dfd-91e4-170cf37160cf
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("c18672d1-dc18-4dfd-91e4-170cf37160cf"), event_id=1, version=0)
class Microsoft_Windows_Hyper_V_Guest_Drivers_IcSvc_1_0(Etw):
    pattern = Struct(
        "Status" / Int32sl
    )


@declare(guid=guid("c18672d1-dc18-4dfd-91e4-170cf37160cf"), event_id=2, version=0)
class Microsoft_Windows_Hyper_V_Guest_Drivers_IcSvc_2_0(Etw):
    pattern = Struct(
        "Status" / Int32sl
    )


@declare(guid=guid("c18672d1-dc18-4dfd-91e4-170cf37160cf"), event_id=3, version=0)
class Microsoft_Windows_Hyper_V_Guest_Drivers_IcSvc_3_0(Etw):
    pattern = Struct(
        "Status" / Int32sl
    )


@declare(guid=guid("c18672d1-dc18-4dfd-91e4-170cf37160cf"), event_id=4, version=0)
class Microsoft_Windows_Hyper_V_Guest_Drivers_IcSvc_4_0(Etw):
    pattern = Struct(
        "Status" / Int32sl
    )


@declare(guid=guid("c18672d1-dc18-4dfd-91e4-170cf37160cf"), event_id=5, version=0)
class Microsoft_Windows_Hyper_V_Guest_Drivers_IcSvc_5_0(Etw):
    pattern = Struct(
        "Volume" / WString
    )


@declare(guid=guid("c18672d1-dc18-4dfd-91e4-170cf37160cf"), event_id=22, version=0)
class Microsoft_Windows_Hyper_V_Guest_Drivers_IcSvc_22_0(Etw):
    pattern = Struct(
        "Status" / Int32sl
    )


@declare(guid=guid("c18672d1-dc18-4dfd-91e4-170cf37160cf"), event_id=23, version=0)
class Microsoft_Windows_Hyper_V_Guest_Drivers_IcSvc_23_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Writerstatus" / Int32sl,
        "Status" / Int32sl
    )


@declare(guid=guid("c18672d1-dc18-4dfd-91e4-170cf37160cf"), event_id=24, version=0)
class Microsoft_Windows_Hyper_V_Guest_Drivers_IcSvc_24_0(Etw):
    pattern = Struct(
        "DiskNumber" / Int32ul
    )


@declare(guid=guid("c18672d1-dc18-4dfd-91e4-170cf37160cf"), event_id=3584, version=0)
class Microsoft_Windows_Hyper_V_Guest_Drivers_IcSvc_3584_0(Etw):
    pattern = Struct(
        "TraceData" / WString,
        "VmName" / WString,
        "VmId" / WString,
        "StackFrameCount" / Int32ul,
        "StackFrame" / Int64ul,
        "ModuleCount" / Int32ul,
        "Module" / Int32sl
    )


@declare(guid=guid("c18672d1-dc18-4dfd-91e4-170cf37160cf"), event_id=3585, version=0)
class Microsoft_Windows_Hyper_V_Guest_Drivers_IcSvc_3585_0(Etw):
    pattern = Struct(
        "TraceData" / WString,
        "VmName" / WString,
        "VmId" / WString,
        "StackFrameCount" / Int32ul,
        "StackFrame" / Int64ul,
        "ModuleCount" / Int32ul,
        "Module" / Int32sl
    )


@declare(guid=guid("c18672d1-dc18-4dfd-91e4-170cf37160cf"), event_id=3586, version=0)
class Microsoft_Windows_Hyper_V_Guest_Drivers_IcSvc_3586_0(Etw):
    pattern = Struct(
        "TraceData" / WString,
        "VmName" / WString,
        "VmId" / WString,
        "StackFrameCount" / Int32ul,
        "StackFrame" / Int64ul,
        "ModuleCount" / Int32ul,
        "Module" / Int32sl
    )


@declare(guid=guid("c18672d1-dc18-4dfd-91e4-170cf37160cf"), event_id=3587, version=0)
class Microsoft_Windows_Hyper_V_Guest_Drivers_IcSvc_3587_0(Etw):
    pattern = Struct(
        "TraceData" / WString,
        "VmName" / WString,
        "VmId" / WString,
        "StackFrameCount" / Int32ul,
        "StackFrame" / Int64ul,
        "ModuleCount" / Int32ul,
        "Module" / Int32sl
    )

