# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Kernel-Process
GUID : 22fb2cd6-0e7b-422b-a0c7-2fad1fd0e716
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("22fb2cd6-0e7b-422b-a0c7-2fad1fd0e716"), event_id=1, version=0)
class Microsoft_Windows_Kernel_Process_1_0(Etw):
    pattern = Struct(
        "ProcessID" / Int32ul,
        "CreateTime" / Int64ul,
        "ParentProcessID" / Int32ul,
        "SessionID" / Int32ul,
        "ImageName" / WString
    )


@declare(guid=guid("22fb2cd6-0e7b-422b-a0c7-2fad1fd0e716"), event_id=1, version=1)
class Microsoft_Windows_Kernel_Process_1_1(Etw):
    pattern = Struct(
        "ProcessID" / Int32ul,
        "CreateTime" / Int64ul,
        "ParentProcessID" / Int32ul,
        "SessionID" / Int32ul,
        "Flags" / Int32ul,
        "ImageName" / WString
    )


@declare(guid=guid("22fb2cd6-0e7b-422b-a0c7-2fad1fd0e716"), event_id=1, version=2)
class Microsoft_Windows_Kernel_Process_1_2(Etw):
    pattern = Struct(
        "ProcessID" / Int32ul,
        "CreateTime" / Int64ul,
        "ParentProcessID" / Int32ul,
        "SessionID" / Int32ul,
        "Flags" / Int32ul,
        "ImageName" / WString,
        "ImageChecksum" / Int32ul,
        "TimeDateStamp" / Int32ul,
        "PackageFullName" / WString,
        "PackageRelativeAppId" / WString
    )


@declare(guid=guid("22fb2cd6-0e7b-422b-a0c7-2fad1fd0e716"), event_id=1, version=3)
class Microsoft_Windows_Kernel_Process_1_3(Etw):
    pattern = Struct(
        "ProcessID" / Int32ul,
        "ProcessSequenceNumber" / Int64ul,
        "CreateTime" / Int64ul,
        "ParentProcessID" / Int32ul,
        "ParentProcessSequenceNumber" / Int64ul,
        "SessionID" / Int32ul,
        "Flags" / Int32ul,
        "ProcessTokenElevationType" / Int32ul,
        "ProcessTokenIsElevated" / Int32ul,
        "MandatoryLabel" / Sid,
        "ImageName" / WString,
        "ImageChecksum" / Int32ul,
        "TimeDateStamp" / Int32ul,
        "PackageFullName" / WString,
        "PackageRelativeAppId" / WString
    )


@declare(guid=guid("22fb2cd6-0e7b-422b-a0c7-2fad1fd0e716"), event_id=2, version=0)
class Microsoft_Windows_Kernel_Process_2_0(Etw):
    pattern = Struct(
        "ProcessID" / Int32ul,
        "CreateTime" / Int64ul,
        "ExitTime" / Int64ul,
        "ExitCode" / Int32ul,
        "TokenElevationType" / Int32ul,
        "HandleCount" / Int32ul,
        "CommitCharge" / Int64ul,
        "CommitPeak" / Int64ul,
        "ImageName" / CString
    )


@declare(guid=guid("22fb2cd6-0e7b-422b-a0c7-2fad1fd0e716"), event_id=2, version=1)
class Microsoft_Windows_Kernel_Process_2_1(Etw):
    pattern = Struct(
        "ProcessID" / Int32ul,
        "CreateTime" / Int64ul,
        "ExitTime" / Int64ul,
        "ExitCode" / Int32ul,
        "TokenElevationType" / Int32ul,
        "HandleCount" / Int32ul,
        "CommitCharge" / Int64ul,
        "CommitPeak" / Int64ul,
        "CPUCycleCount" / Int64ul,
        "ReadOperationCount" / Int32ul,
        "WriteOperationCount" / Int32ul,
        "ReadTransferKiloBytes" / Int32ul,
        "WriteTransferKiloBytes" / Int32ul,
        "HardFaultCount" / Int32ul,
        "ImageName" / CString
    )


@declare(guid=guid("22fb2cd6-0e7b-422b-a0c7-2fad1fd0e716"), event_id=2, version=2)
class Microsoft_Windows_Kernel_Process_2_2(Etw):
    pattern = Struct(
        "ProcessID" / Int32ul,
        "ProcessSequenceNumber" / Int64ul,
        "CreateTime" / Int64ul,
        "ExitTime" / Int64ul,
        "ExitCode" / Int32ul,
        "TokenElevationType" / Int32ul,
        "HandleCount" / Int32ul,
        "CommitCharge" / Int64ul,
        "CommitPeak" / Int64ul,
        "CPUCycleCount" / Int64ul,
        "ReadOperationCount" / Int32ul,
        "WriteOperationCount" / Int32ul,
        "ReadTransferKiloBytes" / Int32ul,
        "WriteTransferKiloBytes" / Int32ul,
        "HardFaultCount" / Int32ul,
        "ImageName" / CString
    )


@declare(guid=guid("22fb2cd6-0e7b-422b-a0c7-2fad1fd0e716"), event_id=3, version=0)
class Microsoft_Windows_Kernel_Process_3_0(Etw):
    pattern = Struct(
        "ProcessID" / Int32ul,
        "ThreadID" / Int32ul,
        "StackBase" / Int64ul,
        "StackLimit" / Int64ul,
        "UserStackBase" / Int64ul,
        "UserStackLimit" / Int64ul,
        "StartAddr" / Int64ul,
        "Win32StartAddr" / Int64ul,
        "TebBase" / Int64ul
    )


@declare(guid=guid("22fb2cd6-0e7b-422b-a0c7-2fad1fd0e716"), event_id=3, version=1)
class Microsoft_Windows_Kernel_Process_3_1(Etw):
    pattern = Struct(
        "ProcessID" / Int32ul,
        "ThreadID" / Int32ul,
        "StackBase" / Int64ul,
        "StackLimit" / Int64ul,
        "UserStackBase" / Int64ul,
        "UserStackLimit" / Int64ul,
        "StartAddr" / Int64ul,
        "Win32StartAddr" / Int64ul,
        "TebBase" / Int64ul,
        "SubProcessTag" / Int32ul
    )


@declare(guid=guid("22fb2cd6-0e7b-422b-a0c7-2fad1fd0e716"), event_id=4, version=0)
class Microsoft_Windows_Kernel_Process_4_0(Etw):
    pattern = Struct(
        "ProcessID" / Int32ul,
        "ThreadID" / Int32ul,
        "StackBase" / Int64ul,
        "StackLimit" / Int64ul,
        "UserStackBase" / Int64ul,
        "UserStackLimit" / Int64ul,
        "StartAddr" / Int64ul,
        "Win32StartAddr" / Int64ul,
        "TebBase" / Int64ul
    )


@declare(guid=guid("22fb2cd6-0e7b-422b-a0c7-2fad1fd0e716"), event_id=4, version=1)
class Microsoft_Windows_Kernel_Process_4_1(Etw):
    pattern = Struct(
        "ProcessID" / Int32ul,
        "ThreadID" / Int32ul,
        "StackBase" / Int64ul,
        "StackLimit" / Int64ul,
        "UserStackBase" / Int64ul,
        "UserStackLimit" / Int64ul,
        "StartAddr" / Int64ul,
        "Win32StartAddr" / Int64ul,
        "TebBase" / Int64ul,
        "SubProcessTag" / Int32ul,
        "CycleTime" / Int64ul
    )


@declare(guid=guid("22fb2cd6-0e7b-422b-a0c7-2fad1fd0e716"), event_id=5, version=0)
class Microsoft_Windows_Kernel_Process_5_0(Etw):
    pattern = Struct(
        "ImageBase" / Int64ul,
        "ImageSize" / Int64ul,
        "ProcessID" / Int32ul,
        "ImageCheckSum" / Int32ul,
        "TimeDateStamp" / Int32ul,
        "DefaultBase" / Int64ul,
        "ImageName" / WString
    )


@declare(guid=guid("22fb2cd6-0e7b-422b-a0c7-2fad1fd0e716"), event_id=6, version=0)
class Microsoft_Windows_Kernel_Process_6_0(Etw):
    pattern = Struct(
        "ImageBase" / Int64ul,
        "ImageSize" / Int64ul,
        "ProcessID" / Int32ul,
        "ImageCheckSum" / Int32ul,
        "TimeDateStamp" / Int32ul,
        "DefaultBase" / Int64ul,
        "ImageName" / WString
    )


@declare(guid=guid("22fb2cd6-0e7b-422b-a0c7-2fad1fd0e716"), event_id=7, version=0)
class Microsoft_Windows_Kernel_Process_7_0(Etw):
    pattern = Struct(
        "ProcessID" / Int32ul,
        "ThreadID" / Int32ul,
        "OldPriority" / Int8ul,
        "NewPriority" / Int8ul
    )


@declare(guid=guid("22fb2cd6-0e7b-422b-a0c7-2fad1fd0e716"), event_id=8, version=0)
class Microsoft_Windows_Kernel_Process_8_0(Etw):
    pattern = Struct(
        "ProcessID" / Int32ul,
        "ThreadID" / Int32ul,
        "OldPriority" / Int8ul,
        "NewPriority" / Int8ul
    )


@declare(guid=guid("22fb2cd6-0e7b-422b-a0c7-2fad1fd0e716"), event_id=9, version=0)
class Microsoft_Windows_Kernel_Process_9_0(Etw):
    pattern = Struct(
        "ProcessID" / Int32ul,
        "ThreadID" / Int32ul,
        "OldPriority" / Int8ul,
        "NewPriority" / Int8ul
    )


@declare(guid=guid("22fb2cd6-0e7b-422b-a0c7-2fad1fd0e716"), event_id=10, version=0)
class Microsoft_Windows_Kernel_Process_10_0(Etw):
    pattern = Struct(
        "ProcessID" / Int32ul,
        "ThreadID" / Int32ul,
        "OldPriority" / Int8ul,
        "NewPriority" / Int8ul
    )


@declare(guid=guid("22fb2cd6-0e7b-422b-a0c7-2fad1fd0e716"), event_id=11, version=0)
class Microsoft_Windows_Kernel_Process_11_0(Etw):
    pattern = Struct(
        "FrozenProcessID" / Int32ul
    )


@declare(guid=guid("22fb2cd6-0e7b-422b-a0c7-2fad1fd0e716"), event_id=11, version=1)
class Microsoft_Windows_Kernel_Process_11_1(Etw):
    pattern = Struct(
        "FrozenProcessID" / Int32ul,
        "CreateTime" / Int64ul
    )


@declare(guid=guid("22fb2cd6-0e7b-422b-a0c7-2fad1fd0e716"), event_id=12, version=0)
class Microsoft_Windows_Kernel_Process_12_0(Etw):
    pattern = Struct(
        "FrozenProcessID" / Int32ul
    )


@declare(guid=guid("22fb2cd6-0e7b-422b-a0c7-2fad1fd0e716"), event_id=12, version=1)
class Microsoft_Windows_Kernel_Process_12_1(Etw):
    pattern = Struct(
        "FrozenProcessID" / Int32ul,
        "CreateTime" / Int64ul
    )


@declare(guid=guid("22fb2cd6-0e7b-422b-a0c7-2fad1fd0e716"), event_id=13, version=0)
class Microsoft_Windows_Kernel_Process_13_0(Etw):
    pattern = Struct(
        "ContainerID" / Guid,
        "JobID" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("22fb2cd6-0e7b-422b-a0c7-2fad1fd0e716"), event_id=14, version=0)
class Microsoft_Windows_Kernel_Process_14_0(Etw):
    pattern = Struct(
        "ContainerID" / Guid,
        "JobID" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("22fb2cd6-0e7b-422b-a0c7-2fad1fd0e716"), event_id=15, version=0)
class Microsoft_Windows_Kernel_Process_15_0(Etw):
    pattern = Struct(
        "ProcessID" / Int32ul,
        "CreateTime" / Int64ul,
        "ParentProcessID" / Int32ul,
        "SessionID" / Int32ul,
        "Flags" / Int32ul,
        "ImageName" / WString,
        "ImageChecksum" / Int32ul,
        "TimeDateStamp" / Int32ul,
        "PackageFullName" / WString,
        "PackageRelativeAppId" / WString
    )


@declare(guid=guid("22fb2cd6-0e7b-422b-a0c7-2fad1fd0e716"), event_id=15, version=1)
class Microsoft_Windows_Kernel_Process_15_1(Etw):
    pattern = Struct(
        "ProcessID" / Int32ul,
        "ProcessSequenceNumber" / Int64ul,
        "CreateTime" / Int64ul,
        "ParentProcessID" / Int32ul,
        "ParentProcessSequenceNumber" / Int64ul,
        "SessionID" / Int32ul,
        "Flags" / Int32ul,
        "ProcessTokenElevationType" / Int32ul,
        "ProcessTokenIsElevated" / Int32ul,
        "MandatoryLabel" / Sid,
        "ImageName" / WString,
        "ImageChecksum" / Int32ul,
        "TimeDateStamp" / Int32ul,
        "PackageFullName" / WString,
        "PackageRelativeAppId" / WString
    )


@declare(guid=guid("22fb2cd6-0e7b-422b-a0c7-2fad1fd0e716"), event_id=17, version=0)
class Microsoft_Windows_Kernel_Process_17_0(Etw):
    pattern = Struct(
        "JobID" / Int32ul,
        "DiskIoAttribution" / Int64ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("22fb2cd6-0e7b-422b-a0c7-2fad1fd0e716"), event_id=18, version=0)
class Microsoft_Windows_Kernel_Process_18_0(Etw):
    pattern = Struct(
        "JobID" / Int32ul,
        "DiskIoAttribution" / Int64ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("22fb2cd6-0e7b-422b-a0c7-2fad1fd0e716"), event_id=19, version=0)
class Microsoft_Windows_Kernel_Process_19_0(Etw):
    pattern = Struct(
        "JobID" / Int32ul,
        "IoRateControl" / Int64ul,
        "ControlType" / Int32ul,
        "RateType" / Int32ul,
        "RateAmount" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("22fb2cd6-0e7b-422b-a0c7-2fad1fd0e716"), event_id=19, version=1)
class Microsoft_Windows_Kernel_Process_19_1(Etw):
    pattern = Struct(
        "JobID" / Int32ul,
        "IoRateControl" / Int64ul,
        "MaxIops" / Int64ul,
        "MaxBandwidth" / Int64ul,
        "MaxTimePercent" / Int64ul,
        "ReservationIops" / Int64ul,
        "ReservationBandwidth" / Int64ul,
        "ReservationTimePercent" / Int64ul,
        "CriticalReservationIops" / Int64ul,
        "CriticalReservationBandwidth" / Int64ul,
        "CriticalReservationTimePercent" / Int64ul,
        "ControlFlags" / Int32ul,
        "VolumeName" / WString,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("22fb2cd6-0e7b-422b-a0c7-2fad1fd0e716"), event_id=19, version=2)
class Microsoft_Windows_Kernel_Process_19_2(Etw):
    pattern = Struct(
        "JobID" / Int32ul,
        "IoRateControl" / Int64ul,
        "MaxIops" / Int64ul,
        "MaxBandwidth" / Int64ul,
        "MaxTimePercent" / Int64ul,
        "ReservationIops" / Int64ul,
        "ReservationBandwidth" / Int64ul,
        "ReservationTimePercent" / Int64ul,
        "CriticalReservationIops" / Int64ul,
        "CriticalReservationBandwidth" / Int64ul,
        "CriticalReservationTimePercent" / Int64ul,
        "SoftMaxIops" / Int64ul,
        "SoftMaxBandwidth" / Int64ul,
        "SoftMaxTimePercent" / Int64ul,
        "ControlFlags" / Int32ul,
        "VolumeName" / WString,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("22fb2cd6-0e7b-422b-a0c7-2fad1fd0e716"), event_id=20, version=0)
class Microsoft_Windows_Kernel_Process_20_0(Etw):
    pattern = Struct(
        "JobID" / Int32ul,
        "IoRateControl" / Int64ul,
        "ControlType" / Int32ul,
        "RateType" / Int32ul,
        "RateAmount" / Int32ul,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("22fb2cd6-0e7b-422b-a0c7-2fad1fd0e716"), event_id=20, version=1)
class Microsoft_Windows_Kernel_Process_20_1(Etw):
    pattern = Struct(
        "JobID" / Int32ul,
        "IoRateControl" / Int64ul,
        "MaxIops" / Int64ul,
        "MaxBandwidth" / Int64ul,
        "MaxTimePercent" / Int64ul,
        "ReservationIops" / Int64ul,
        "ReservationBandwidth" / Int64ul,
        "ReservationTimePercent" / Int64ul,
        "CriticalReservationIops" / Int64ul,
        "CriticalReservationBandwidth" / Int64ul,
        "CriticalReservationTimePercent" / Int64ul,
        "ControlFlags" / Int32ul,
        "VolumeName" / WString,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("22fb2cd6-0e7b-422b-a0c7-2fad1fd0e716"), event_id=20, version=2)
class Microsoft_Windows_Kernel_Process_20_2(Etw):
    pattern = Struct(
        "JobID" / Int32ul,
        "IoRateControl" / Int64ul,
        "MaxIops" / Int64ul,
        "MaxBandwidth" / Int64ul,
        "MaxTimePercent" / Int64ul,
        "ReservationIops" / Int64ul,
        "ReservationBandwidth" / Int64ul,
        "ReservationTimePercent" / Int64ul,
        "CriticalReservationIops" / Int64ul,
        "CriticalReservationBandwidth" / Int64ul,
        "CriticalReservationTimePercent" / Int64ul,
        "SoftMaxIops" / Int64ul,
        "SoftMaxBandwidth" / Int64ul,
        "SoftMaxTimePercent" / Int64ul,
        "ControlFlags" / Int32ul,
        "VolumeName" / WString,
        "StatusCode" / Int32ul
    )


@declare(guid=guid("22fb2cd6-0e7b-422b-a0c7-2fad1fd0e716"), event_id=21, version=0)
class Microsoft_Windows_Kernel_Process_21_0(Etw):
    pattern = Struct(
        "OldWorkOnBehalfThreadID" / Int32ul,
        "NewWorkOnBehalfThreadID" / Int32ul
    )


@declare(guid=guid("22fb2cd6-0e7b-422b-a0c7-2fad1fd0e716"), event_id=22, version=0)
class Microsoft_Windows_Kernel_Process_22_0(Etw):
    pattern = Struct(
        "ContainerID" / Guid,
        "JobID" / Int32ul,
        "State" / Int16ul
    )


@declare(guid=guid("22fb2cd6-0e7b-422b-a0c7-2fad1fd0e716"), event_id=23, version=0)
class Microsoft_Windows_Kernel_Process_23_0(Etw):
    pattern = Struct(
        "ContainerID" / Guid,
        "JobID" / Int32ul,
        "MonitorName" / WString
    )


@declare(guid=guid("22fb2cd6-0e7b-422b-a0c7-2fad1fd0e716"), event_id=24, version=0)
class Microsoft_Windows_Kernel_Process_24_0(Etw):
    pattern = Struct(
        "ContainerID" / Guid,
        "JobID" / Int32ul,
        "Status" / Int32ul,
        "MonitorName" / WString
    )


@declare(guid=guid("22fb2cd6-0e7b-422b-a0c7-2fad1fd0e716"), event_id=25, version=0)
class Microsoft_Windows_Kernel_Process_25_0(Etw):
    pattern = Struct(
        "ContainerID" / Guid,
        "JobID" / Int32ul,
        "MonitorName" / WString
    )


@declare(guid=guid("22fb2cd6-0e7b-422b-a0c7-2fad1fd0e716"), event_id=26, version=0)
class Microsoft_Windows_Kernel_Process_26_0(Etw):
    pattern = Struct(
        "ContainerID" / Guid,
        "JobID" / Int32ul,
        "MonitorName" / WString
    )

