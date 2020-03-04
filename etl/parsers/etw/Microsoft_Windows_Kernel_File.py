# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Kernel-File
GUID : edd08927-9cc4-4e65-b970-c2560fb5c289
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("edd08927-9cc4-4e65-b970-c2560fb5c289"), event_id=10, version=0)
class Microsoft_Windows_Kernel_File_10_0(Etw):
    pattern = Struct(
        "FileKey" / Int64ul,
        "FileName" / WString
    )


@declare(guid=guid("edd08927-9cc4-4e65-b970-c2560fb5c289"), event_id=11, version=0)
class Microsoft_Windows_Kernel_File_11_0(Etw):
    pattern = Struct(
        "FileKey" / Int64ul,
        "FileName" / WString
    )


@declare(guid=guid("edd08927-9cc4-4e65-b970-c2560fb5c289"), event_id=12, version=0)
class Microsoft_Windows_Kernel_File_12_0(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "ThreadId" / Int64ul,
        "FileObject" / Int64ul,
        "CreateOptions" / Int32ul,
        "CreateAttributes" / Int32ul,
        "ShareAccess" / Int32ul,
        "FileName" / WString
    )


@declare(guid=guid("edd08927-9cc4-4e65-b970-c2560fb5c289"), event_id=12, version=1)
class Microsoft_Windows_Kernel_File_12_1(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "FileObject" / Int64ul,
        "IssuingThreadId" / Int32ul,
        "CreateOptions" / Int32ul,
        "CreateAttributes" / Int32ul,
        "ShareAccess" / Int32ul,
        "FileName" / WString
    )


@declare(guid=guid("edd08927-9cc4-4e65-b970-c2560fb5c289"), event_id=13, version=0)
class Microsoft_Windows_Kernel_File_13_0(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "ThreadId" / Int64ul,
        "FileObject" / Int64ul,
        "FileKey" / Int64ul
    )


@declare(guid=guid("edd08927-9cc4-4e65-b970-c2560fb5c289"), event_id=13, version=1)
class Microsoft_Windows_Kernel_File_13_1(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "FileObject" / Int64ul,
        "FileKey" / Int64ul,
        "IssuingThreadId" / Int32ul
    )


@declare(guid=guid("edd08927-9cc4-4e65-b970-c2560fb5c289"), event_id=14, version=0)
class Microsoft_Windows_Kernel_File_14_0(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "ThreadId" / Int64ul,
        "FileObject" / Int64ul,
        "FileKey" / Int64ul
    )


@declare(guid=guid("edd08927-9cc4-4e65-b970-c2560fb5c289"), event_id=14, version=1)
class Microsoft_Windows_Kernel_File_14_1(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "FileObject" / Int64ul,
        "FileKey" / Int64ul,
        "IssuingThreadId" / Int32ul
    )


@declare(guid=guid("edd08927-9cc4-4e65-b970-c2560fb5c289"), event_id=15, version=0)
class Microsoft_Windows_Kernel_File_15_0(Etw):
    pattern = Struct(
        "ByteOffset" / Int64ul,
        "Irp" / Int64ul,
        "ThreadId" / Int64ul,
        "FileObject" / Int64ul,
        "FileKey" / Int64ul,
        "IOSize" / Int32ul,
        "IOFlags" / Int32ul
    )


@declare(guid=guid("edd08927-9cc4-4e65-b970-c2560fb5c289"), event_id=15, version=1)
class Microsoft_Windows_Kernel_File_15_1(Etw):
    pattern = Struct(
        "ByteOffset" / Int64ul,
        "Irp" / Int64ul,
        "FileObject" / Int64ul,
        "FileKey" / Int64ul,
        "IssuingThreadId" / Int32ul,
        "IOSize" / Int32ul,
        "IOFlags" / Int32ul,
        "ExtraFlags" / Int32ul
    )


@declare(guid=guid("edd08927-9cc4-4e65-b970-c2560fb5c289"), event_id=16, version=0)
class Microsoft_Windows_Kernel_File_16_0(Etw):
    pattern = Struct(
        "ByteOffset" / Int64ul,
        "Irp" / Int64ul,
        "ThreadId" / Int64ul,
        "FileObject" / Int64ul,
        "FileKey" / Int64ul,
        "IOSize" / Int32ul,
        "IOFlags" / Int32ul
    )


@declare(guid=guid("edd08927-9cc4-4e65-b970-c2560fb5c289"), event_id=16, version=1)
class Microsoft_Windows_Kernel_File_16_1(Etw):
    pattern = Struct(
        "ByteOffset" / Int64ul,
        "Irp" / Int64ul,
        "FileObject" / Int64ul,
        "FileKey" / Int64ul,
        "IssuingThreadId" / Int32ul,
        "IOSize" / Int32ul,
        "IOFlags" / Int32ul,
        "ExtraFlags" / Int32ul
    )


@declare(guid=guid("edd08927-9cc4-4e65-b970-c2560fb5c289"), event_id=17, version=0)
class Microsoft_Windows_Kernel_File_17_0(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "ThreadId" / Int64ul,
        "FileObject" / Int64ul,
        "FileKey" / Int64ul,
        "ExtraInformation" / Int64ul,
        "InfoClass" / Int32ul
    )


@declare(guid=guid("edd08927-9cc4-4e65-b970-c2560fb5c289"), event_id=17, version=1)
class Microsoft_Windows_Kernel_File_17_1(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "FileObject" / Int64ul,
        "FileKey" / Int64ul,
        "ExtraInformation" / Int64ul,
        "IssuingThreadId" / Int32ul,
        "InfoClass" / Int32ul
    )


@declare(guid=guid("edd08927-9cc4-4e65-b970-c2560fb5c289"), event_id=18, version=0)
class Microsoft_Windows_Kernel_File_18_0(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "ThreadId" / Int64ul,
        "FileObject" / Int64ul,
        "FileKey" / Int64ul,
        "ExtraInformation" / Int64ul,
        "InfoClass" / Int32ul
    )


@declare(guid=guid("edd08927-9cc4-4e65-b970-c2560fb5c289"), event_id=18, version=1)
class Microsoft_Windows_Kernel_File_18_1(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "FileObject" / Int64ul,
        "FileKey" / Int64ul,
        "ExtraInformation" / Int64ul,
        "IssuingThreadId" / Int32ul,
        "InfoClass" / Int32ul
    )


@declare(guid=guid("edd08927-9cc4-4e65-b970-c2560fb5c289"), event_id=19, version=0)
class Microsoft_Windows_Kernel_File_19_0(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "ThreadId" / Int64ul,
        "FileObject" / Int64ul,
        "FileKey" / Int64ul,
        "ExtraInformation" / Int64ul,
        "InfoClass" / Int32ul
    )


@declare(guid=guid("edd08927-9cc4-4e65-b970-c2560fb5c289"), event_id=19, version=1)
class Microsoft_Windows_Kernel_File_19_1(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "FileObject" / Int64ul,
        "FileKey" / Int64ul,
        "ExtraInformation" / Int64ul,
        "IssuingThreadId" / Int32ul,
        "InfoClass" / Int32ul
    )


@declare(guid=guid("edd08927-9cc4-4e65-b970-c2560fb5c289"), event_id=20, version=0)
class Microsoft_Windows_Kernel_File_20_0(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "ThreadId" / Int64ul,
        "FileObject" / Int64ul,
        "FileKey" / Int64ul,
        "Length" / Int32ul,
        "InfoClass" / Int32ul,
        "FileIndex" / Int32ul,
        "FileName" / WString
    )


@declare(guid=guid("edd08927-9cc4-4e65-b970-c2560fb5c289"), event_id=20, version=1)
class Microsoft_Windows_Kernel_File_20_1(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "FileObject" / Int64ul,
        "FileKey" / Int64ul,
        "IssuingThreadId" / Int32ul,
        "Length" / Int32ul,
        "InfoClass" / Int32ul,
        "FileIndex" / Int32ul,
        "FileName" / WString
    )


@declare(guid=guid("edd08927-9cc4-4e65-b970-c2560fb5c289"), event_id=21, version=0)
class Microsoft_Windows_Kernel_File_21_0(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "ThreadId" / Int64ul,
        "FileObject" / Int64ul,
        "FileKey" / Int64ul
    )


@declare(guid=guid("edd08927-9cc4-4e65-b970-c2560fb5c289"), event_id=21, version=1)
class Microsoft_Windows_Kernel_File_21_1(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "FileObject" / Int64ul,
        "FileKey" / Int64ul,
        "IssuingThreadId" / Int32ul
    )


@declare(guid=guid("edd08927-9cc4-4e65-b970-c2560fb5c289"), event_id=22, version=0)
class Microsoft_Windows_Kernel_File_22_0(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "ThreadId" / Int64ul,
        "FileObject" / Int64ul,
        "FileKey" / Int64ul,
        "ExtraInformation" / Int64ul,
        "InfoClass" / Int32ul
    )


@declare(guid=guid("edd08927-9cc4-4e65-b970-c2560fb5c289"), event_id=22, version=1)
class Microsoft_Windows_Kernel_File_22_1(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "FileObject" / Int64ul,
        "FileKey" / Int64ul,
        "ExtraInformation" / Int64ul,
        "IssuingThreadId" / Int32ul,
        "InfoClass" / Int32ul
    )


@declare(guid=guid("edd08927-9cc4-4e65-b970-c2560fb5c289"), event_id=23, version=0)
class Microsoft_Windows_Kernel_File_23_0(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "ThreadId" / Int64ul,
        "FileObject" / Int64ul,
        "FileKey" / Int64ul,
        "ExtraInformation" / Int64ul,
        "InfoClass" / Int32ul
    )


@declare(guid=guid("edd08927-9cc4-4e65-b970-c2560fb5c289"), event_id=23, version=1)
class Microsoft_Windows_Kernel_File_23_1(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "FileObject" / Int64ul,
        "FileKey" / Int64ul,
        "ExtraInformation" / Int64ul,
        "IssuingThreadId" / Int32ul,
        "InfoClass" / Int32ul
    )


@declare(guid=guid("edd08927-9cc4-4e65-b970-c2560fb5c289"), event_id=24, version=0)
class Microsoft_Windows_Kernel_File_24_0(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "ExtraInformation" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("edd08927-9cc4-4e65-b970-c2560fb5c289"), event_id=25, version=0)
class Microsoft_Windows_Kernel_File_25_0(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "ThreadId" / Int64ul,
        "FileObject" / Int64ul,
        "FileKey" / Int64ul,
        "Length" / Int32ul,
        "InfoClass" / Int32ul,
        "FileIndex" / Int32ul,
        "FileName" / WString
    )


@declare(guid=guid("edd08927-9cc4-4e65-b970-c2560fb5c289"), event_id=25, version=1)
class Microsoft_Windows_Kernel_File_25_1(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "FileObject" / Int64ul,
        "FileKey" / Int64ul,
        "IssuingThreadId" / Int32ul,
        "Length" / Int32ul,
        "InfoClass" / Int32ul,
        "FileIndex" / Int32ul,
        "FileName" / WString
    )


@declare(guid=guid("edd08927-9cc4-4e65-b970-c2560fb5c289"), event_id=26, version=0)
class Microsoft_Windows_Kernel_File_26_0(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "ThreadId" / Int64ul,
        "FileObject" / Int64ul,
        "FileKey" / Int64ul,
        "ExtraInformation" / Int64ul,
        "InfoClass" / Int32ul,
        "FilePath" / WString
    )


@declare(guid=guid("edd08927-9cc4-4e65-b970-c2560fb5c289"), event_id=26, version=1)
class Microsoft_Windows_Kernel_File_26_1(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "FileObject" / Int64ul,
        "FileKey" / Int64ul,
        "ExtraInformation" / Int64ul,
        "IssuingThreadId" / Int32ul,
        "InfoClass" / Int32ul,
        "FilePath" / WString
    )


@declare(guid=guid("edd08927-9cc4-4e65-b970-c2560fb5c289"), event_id=27, version=0)
class Microsoft_Windows_Kernel_File_27_0(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "ThreadId" / Int64ul,
        "FileObject" / Int64ul,
        "FileKey" / Int64ul,
        "ExtraInformation" / Int64ul,
        "InfoClass" / Int32ul,
        "FilePath" / WString
    )


@declare(guid=guid("edd08927-9cc4-4e65-b970-c2560fb5c289"), event_id=27, version=1)
class Microsoft_Windows_Kernel_File_27_1(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "FileObject" / Int64ul,
        "FileKey" / Int64ul,
        "ExtraInformation" / Int64ul,
        "IssuingThreadId" / Int32ul,
        "InfoClass" / Int32ul,
        "FilePath" / WString
    )


@declare(guid=guid("edd08927-9cc4-4e65-b970-c2560fb5c289"), event_id=28, version=0)
class Microsoft_Windows_Kernel_File_28_0(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "ThreadId" / Int64ul,
        "FileObject" / Int64ul,
        "FileKey" / Int64ul,
        "ExtraInformation" / Int64ul,
        "InfoClass" / Int32ul,
        "FilePath" / WString
    )


@declare(guid=guid("edd08927-9cc4-4e65-b970-c2560fb5c289"), event_id=28, version=1)
class Microsoft_Windows_Kernel_File_28_1(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "FileObject" / Int64ul,
        "FileKey" / Int64ul,
        "ExtraInformation" / Int64ul,
        "IssuingThreadId" / Int32ul,
        "InfoClass" / Int32ul,
        "FilePath" / WString
    )


@declare(guid=guid("edd08927-9cc4-4e65-b970-c2560fb5c289"), event_id=29, version=0)
class Microsoft_Windows_Kernel_File_29_0(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "ThreadId" / Int64ul,
        "FileObject" / Int64ul,
        "FileKey" / Int64ul,
        "ExtraInformation" / Int64ul,
        "InfoClass" / Int32ul
    )


@declare(guid=guid("edd08927-9cc4-4e65-b970-c2560fb5c289"), event_id=29, version=1)
class Microsoft_Windows_Kernel_File_29_1(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "FileObject" / Int64ul,
        "FileKey" / Int64ul,
        "ExtraInformation" / Int64ul,
        "IssuingThreadId" / Int32ul,
        "InfoClass" / Int32ul
    )


@declare(guid=guid("edd08927-9cc4-4e65-b970-c2560fb5c289"), event_id=30, version=0)
class Microsoft_Windows_Kernel_File_30_0(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "ThreadId" / Int64ul,
        "FileObject" / Int64ul,
        "CreateOptions" / Int32ul,
        "CreateAttributes" / Int32ul,
        "ShareAccess" / Int32ul,
        "FileName" / WString
    )


@declare(guid=guid("edd08927-9cc4-4e65-b970-c2560fb5c289"), event_id=30, version=1)
class Microsoft_Windows_Kernel_File_30_1(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "FileObject" / Int64ul,
        "IssuingThreadId" / Int32ul,
        "CreateOptions" / Int32ul,
        "CreateAttributes" / Int32ul,
        "ShareAccess" / Int32ul,
        "FileName" / WString
    )


@declare(guid=guid("edd08927-9cc4-4e65-b970-c2560fb5c289"), event_id=31, version=1)
class Microsoft_Windows_Kernel_File_31_1(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "FileObject" / Int64ul,
        "FileKey" / Int64ul,
        "ExtraInformation" / Int64ul,
        "IssuingThreadId" / Int32ul,
        "InfoClass" / Int32ul
    )


@declare(guid=guid("edd08927-9cc4-4e65-b970-c2560fb5c289"), event_id=32, version=1)
class Microsoft_Windows_Kernel_File_32_1(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "FileObject" / Int64ul,
        "FileKey" / Int64ul,
        "ExtraInformation" / Int64ul,
        "IssuingThreadId" / Int32ul,
        "InfoClass" / Int32ul
    )


@declare(guid=guid("edd08927-9cc4-4e65-b970-c2560fb5c289"), event_id=33, version=1)
class Microsoft_Windows_Kernel_File_33_1(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "FileObject" / Int64ul,
        "FileKey" / Int64ul,
        "ExtraInformation" / Int64ul,
        "IssuingThreadId" / Int32ul,
        "InfoClass" / Int32ul
    )


@declare(guid=guid("edd08927-9cc4-4e65-b970-c2560fb5c289"), event_id=34, version=1)
class Microsoft_Windows_Kernel_File_34_1(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "FileObject" / Int64ul,
        "FileKey" / Int64ul,
        "ExtraInformation" / Int64ul,
        "IssuingThreadId" / Int32ul,
        "InfoClass" / Int32ul
    )

