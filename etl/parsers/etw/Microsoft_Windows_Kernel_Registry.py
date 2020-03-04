# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Kernel-Registry
GUID : 70eb4f03-c1de-4f73-a051-33d13d5413bd
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("70eb4f03-c1de-4f73-a051-33d13d5413bd"), event_id=1, version=0)
class Microsoft_Windows_Kernel_Registry_1_0(Etw):
    pattern = Struct(
        "BaseObject" / Int64ul,
        "KeyObject" / Int64ul,
        "Status" / Int32ul,
        "Disposition" / Int32ul,
        "BaseName" / WString,
        "RelativeName" / WString
    )


@declare(guid=guid("70eb4f03-c1de-4f73-a051-33d13d5413bd"), event_id=2, version=0)
class Microsoft_Windows_Kernel_Registry_2_0(Etw):
    pattern = Struct(
        "BaseObject" / Int64ul,
        "KeyObject" / Int64ul,
        "Status" / Int32ul,
        "Disposition" / Int32ul,
        "BaseName" / WString,
        "RelativeName" / WString
    )


@declare(guid=guid("70eb4f03-c1de-4f73-a051-33d13d5413bd"), event_id=3, version=0)
class Microsoft_Windows_Kernel_Registry_3_0(Etw):
    pattern = Struct(
        "KeyObject" / Int64ul,
        "Status" / Int32ul,
        "KeyName" / WString
    )


@declare(guid=guid("70eb4f03-c1de-4f73-a051-33d13d5413bd"), event_id=4, version=0)
class Microsoft_Windows_Kernel_Registry_4_0(Etw):
    pattern = Struct(
        "KeyObject" / Int64ul,
        "Status" / Int32ul,
        "InfoClass" / Int32ul,
        "DataSize" / Int32ul,
        "KeyName" / WString,
        "CapturedDataSize" / Int16ul,
        "CapturedData" / Bytes(lambda this: this.CapturedDataSize)
    )


@declare(guid=guid("70eb4f03-c1de-4f73-a051-33d13d5413bd"), event_id=5, version=0)
class Microsoft_Windows_Kernel_Registry_5_0(Etw):
    pattern = Struct(
        "KeyObject" / Int64ul,
        "Status" / Int32ul,
        "Type" / Int32ul,
        "DataSize" / Int32ul,
        "KeyName" / WString,
        "ValueName" / WString,
        "CapturedDataSize" / Int16ul,
        "CapturedData" / Bytes(lambda this: this.CapturedDataSize),
        "PreviousDataType" / Int32ul,
        "PreviousDataSize" / Int32ul,
        "PreviousDataCapturedSize" / Int16ul,
        "PreviousData" / Bytes(lambda this: this.PreviousDataCapturedSize)
    )


@declare(guid=guid("70eb4f03-c1de-4f73-a051-33d13d5413bd"), event_id=6, version=0)
class Microsoft_Windows_Kernel_Registry_6_0(Etw):
    pattern = Struct(
        "KeyObject" / Int64ul,
        "Status" / Int32ul,
        "KeyName" / WString,
        "ValueName" / WString
    )


@declare(guid=guid("70eb4f03-c1de-4f73-a051-33d13d5413bd"), event_id=7, version=0)
class Microsoft_Windows_Kernel_Registry_7_0(Etw):
    pattern = Struct(
        "KeyObject" / Int64ul,
        "Status" / Int32ul,
        "InfoClass" / Int32ul,
        "DataSize" / Int32ul,
        "KeyName" / WString,
        "ValueName" / WString,
        "CapturedDataSize" / Int16ul,
        "CapturedData" / Bytes(lambda this: this.CapturedDataSize)
    )


@declare(guid=guid("70eb4f03-c1de-4f73-a051-33d13d5413bd"), event_id=8, version=0)
class Microsoft_Windows_Kernel_Registry_8_0(Etw):
    pattern = Struct(
        "KeyObject" / Int64ul,
        "Status" / Int32ul,
        "Index" / Int32ul,
        "InfoClass" / Int32ul,
        "DataSize" / Int32ul,
        "KeyName" / WString,
        "CapturedDataSize" / Int16ul,
        "CapturedData" / Bytes(lambda this: this.CapturedDataSize)
    )


@declare(guid=guid("70eb4f03-c1de-4f73-a051-33d13d5413bd"), event_id=9, version=0)
class Microsoft_Windows_Kernel_Registry_9_0(Etw):
    pattern = Struct(
        "KeyObject" / Int64ul,
        "Status" / Int32ul,
        "Index" / Int32ul,
        "InfoClass" / Int32ul,
        "DataSize" / Int32ul,
        "KeyName" / WString,
        "CapturedDataSize" / Int16ul,
        "CapturedData" / Bytes(lambda this: this.CapturedDataSize)
    )


@declare(guid=guid("70eb4f03-c1de-4f73-a051-33d13d5413bd"), event_id=10, version=0)
class Microsoft_Windows_Kernel_Registry_10_0(Etw):
    pattern = Struct(
        "KeyObject" / Int64ul,
        "Status" / Int32ul,
        "EntryCount" / Int32ul,
        "DataSize" / Int32ul,
        "KeyName" / WString
    )


@declare(guid=guid("70eb4f03-c1de-4f73-a051-33d13d5413bd"), event_id=11, version=0)
class Microsoft_Windows_Kernel_Registry_11_0(Etw):
    pattern = Struct(
        "KeyObject" / Int64ul,
        "Status" / Int32ul,
        "InfoClass" / Int32ul,
        "DataSize" / Int32ul,
        "KeyName" / WString,
        "CapturedDataSize" / Int16ul,
        "CapturedData" / Bytes(lambda this: this.CapturedDataSize)
    )


@declare(guid=guid("70eb4f03-c1de-4f73-a051-33d13d5413bd"), event_id=12, version=0)
class Microsoft_Windows_Kernel_Registry_12_0(Etw):
    pattern = Struct(
        "KeyObject" / Int64ul,
        "Status" / Int32ul,
        "KeyName" / WString
    )


@declare(guid=guid("70eb4f03-c1de-4f73-a051-33d13d5413bd"), event_id=13, version=0)
class Microsoft_Windows_Kernel_Registry_13_0(Etw):
    pattern = Struct(
        "KeyObject" / Int64ul,
        "Status" / Int32ul,
        "KeyName" / WString
    )


@declare(guid=guid("70eb4f03-c1de-4f73-a051-33d13d5413bd"), event_id=14, version=0)
class Microsoft_Windows_Kernel_Registry_14_0(Etw):
    pattern = Struct(
        "KeyObject" / Int64ul,
        "Status" / Int32ul,
        "KeyName" / WString
    )


@declare(guid=guid("70eb4f03-c1de-4f73-a051-33d13d5413bd"), event_id=15, version=0)
class Microsoft_Windows_Kernel_Registry_15_0(Etw):
    pattern = Struct(
        "KeyObject" / Int64ul,
        "Status" / Int32ul,
        "KeyName" / WString
    )


@declare(guid=guid("70eb4f03-c1de-4f73-a051-33d13d5413bd"), event_id=17, version=0)
class Microsoft_Windows_Kernel_Registry_17_0(Etw):
    pattern = Struct(
        "HiveFilePath" / WString,
        "FileSize" / Int32ul
    )


@declare(guid=guid("70eb4f03-c1de-4f73-a051-33d13d5413bd"), event_id=18, version=0)
class Microsoft_Windows_Kernel_Registry_18_0(Etw):
    pattern = Struct(
        "TotalEntrySize" / Int32ul,
        "BytesRecovered" / Int32ul
    )


@declare(guid=guid("70eb4f03-c1de-4f73-a051-33d13d5413bd"), event_id=19, version=0)
class Microsoft_Windows_Kernel_Registry_19_0(Etw):
    pattern = Struct(
        "StatusCode" / Int32ul
    )


@declare(guid=guid("70eb4f03-c1de-4f73-a051-33d13d5413bd"), event_id=20, version=0)
class Microsoft_Windows_Kernel_Registry_20_0(Etw):
    pattern = Struct(
        "HiveFilePath" / WString,
        "HiveMountPoint" / WString
    )


@declare(guid=guid("70eb4f03-c1de-4f73-a051-33d13d5413bd"), event_id=21, version=0)
class Microsoft_Windows_Kernel_Registry_21_0(Etw):
    pattern = Struct(
        "StatusCode" / Int32ul
    )


@declare(guid=guid("70eb4f03-c1de-4f73-a051-33d13d5413bd"), event_id=22, version=0)
class Microsoft_Windows_Kernel_Registry_22_0(Etw):
    pattern = Struct(
        "HiveFilePath" / WString,
        "HiveMountPoint" / WString,
        "FlushFlags" / Int32ul
    )


@declare(guid=guid("70eb4f03-c1de-4f73-a051-33d13d5413bd"), event_id=24, version=0)
class Microsoft_Windows_Kernel_Registry_24_0(Etw):
    pattern = Struct(
        "BytesGathered" / Int32ul
    )


@declare(guid=guid("70eb4f03-c1de-4f73-a051-33d13d5413bd"), event_id=25, version=0)
class Microsoft_Windows_Kernel_Registry_25_0(Etw):
    pattern = Struct(
        "BytesGathered" / Int32ul
    )


@declare(guid=guid("70eb4f03-c1de-4f73-a051-33d13d5413bd"), event_id=26, version=0)
class Microsoft_Windows_Kernel_Registry_26_0(Etw):
    pattern = Struct(
        "WritesIssued" / Int32ul,
        "BytesWritten" / Int32ul
    )


@declare(guid=guid("70eb4f03-c1de-4f73-a051-33d13d5413bd"), event_id=27, version=0)
class Microsoft_Windows_Kernel_Registry_27_0(Etw):
    pattern = Struct(
        "WritesIssued" / Int32ul,
        "BytesWritten" / Int32ul
    )


@declare(guid=guid("70eb4f03-c1de-4f73-a051-33d13d5413bd"), event_id=31, version=0)
class Microsoft_Windows_Kernel_Registry_31_0(Etw):
    pattern = Struct(
        "StatusCode" / Int32ul
    )


@declare(guid=guid("70eb4f03-c1de-4f73-a051-33d13d5413bd"), event_id=37, version=0)
class Microsoft_Windows_Kernel_Registry_37_0(Etw):
    pattern = Struct(
        "SourceFile" / WString,
        "Flags" / Int32ul
    )


@declare(guid=guid("70eb4f03-c1de-4f73-a051-33d13d5413bd"), event_id=38, version=0)
class Microsoft_Windows_Kernel_Registry_38_0(Etw):
    pattern = Struct(
        "StatusCode" / Int32ul
    )


@declare(guid=guid("70eb4f03-c1de-4f73-a051-33d13d5413bd"), event_id=39, version=0)
class Microsoft_Windows_Kernel_Registry_39_0(Etw):
    pattern = Struct(
        "SourceFile" / WString,
        "Flags" / Int32ul
    )


@declare(guid=guid("70eb4f03-c1de-4f73-a051-33d13d5413bd"), event_id=40, version=0)
class Microsoft_Windows_Kernel_Registry_40_0(Etw):
    pattern = Struct(
        "StatusCode" / Int32ul
    )


@declare(guid=guid("70eb4f03-c1de-4f73-a051-33d13d5413bd"), event_id=41, version=0)
class Microsoft_Windows_Kernel_Registry_41_0(Etw):
    pattern = Struct(
        "SourceKeyPath" / WString
    )


@declare(guid=guid("70eb4f03-c1de-4f73-a051-33d13d5413bd"), event_id=45, version=0)
class Microsoft_Windows_Kernel_Registry_45_0(Etw):
    pattern = Struct(
        "StatusCode" / Int32ul
    )

