# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Remotefs-Rdbss
GUID : 1a870028-f191-4699-8473-6fcd299eab77
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("1a870028-f191-4699-8473-6fcd299eab77"), event_id=100, version=0)
class Microsoft_Windows_Remotefs_Rdbss_100_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("1a870028-f191-4699-8473-6fcd299eab77"), event_id=401, version=0)
class Microsoft_Windows_Remotefs_Rdbss_401_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("1a870028-f191-4699-8473-6fcd299eab77"), event_id=30001, version=0)
class Microsoft_Windows_Remotefs_Rdbss_30001_0(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "RxContext" / Int64ul,
        "Fcb" / Int64ul,
        "Fobx" / Int64ul,
        "FileObject" / Int64ul,
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "MajorFunction" / Int16ul
    )


@declare(guid=guid("1a870028-f191-4699-8473-6fcd299eab77"), event_id=30002, version=0)
class Microsoft_Windows_Remotefs_Rdbss_30002_0(Etw):
    pattern = Struct(
        "Irp" / Int64ul,
        "RxContext" / Int64ul,
        "Fcb" / Int64ul,
        "Fobx" / Int64ul,
        "FileObject" / Int64ul,
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "MajorFunction" / Int16ul,
        "Status" / Int32ul
    )


@declare(guid=guid("1a870028-f191-4699-8473-6fcd299eab77"), event_id=30003, version=0)
class Microsoft_Windows_Remotefs_Rdbss_30003_0(Etw):
    pattern = Struct(
        "FileObject" / Int64ul,
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "MajorFunction" / Int16ul
    )


@declare(guid=guid("1a870028-f191-4699-8473-6fcd299eab77"), event_id=30004, version=0)
class Microsoft_Windows_Remotefs_Rdbss_30004_0(Etw):
    pattern = Struct(
        "FileObject" / Int64ul,
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "MajorFunction" / Int16ul,
        "Status" / Int32ul
    )


@declare(guid=guid("1a870028-f191-4699-8473-6fcd299eab77"), event_id=30005, version=0)
class Microsoft_Windows_Remotefs_Rdbss_30005_0(Etw):
    pattern = Struct(
        "RxContext" / Int64ul
    )


@declare(guid=guid("1a870028-f191-4699-8473-6fcd299eab77"), event_id=30006, version=0)
class Microsoft_Windows_Remotefs_Rdbss_30006_0(Etw):
    pattern = Struct(
        "RxContext" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("1a870028-f191-4699-8473-6fcd299eab77"), event_id=30007, version=0)
class Microsoft_Windows_Remotefs_Rdbss_30007_0(Etw):
    pattern = Struct(
        "RxContext" / Int64ul,
        "Fcb" / Int64ul,
        "Mode" / Int32ul
    )


@declare(guid=guid("1a870028-f191-4699-8473-6fcd299eab77"), event_id=30008, version=0)
class Microsoft_Windows_Remotefs_Rdbss_30008_0(Etw):
    pattern = Struct(
        "RxContext" / Int64ul,
        "Fcb" / Int64ul
    )


@declare(guid=guid("1a870028-f191-4699-8473-6fcd299eab77"), event_id=30009, version=0)
class Microsoft_Windows_Remotefs_Rdbss_30009_0(Etw):
    pattern = Struct(
        "RxContext" / Int64ul,
        "FileObject" / Int64ul
    )


@declare(guid=guid("1a870028-f191-4699-8473-6fcd299eab77"), event_id=30010, version=0)
class Microsoft_Windows_Remotefs_Rdbss_30010_0(Etw):
    pattern = Struct(
        "RxContext" / Int64ul,
        "FileObject" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("1a870028-f191-4699-8473-6fcd299eab77"), event_id=30011, version=0)
class Microsoft_Windows_Remotefs_Rdbss_30011_0(Etw):
    pattern = Struct(
        "RxContext" / Int64ul,
        "FileObject" / Int64ul
    )


@declare(guid=guid("1a870028-f191-4699-8473-6fcd299eab77"), event_id=30012, version=0)
class Microsoft_Windows_Remotefs_Rdbss_30012_0(Etw):
    pattern = Struct(
        "RxContext" / Int64ul,
        "FileObject" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("1a870028-f191-4699-8473-6fcd299eab77"), event_id=30013, version=0)
class Microsoft_Windows_Remotefs_Rdbss_30013_0(Etw):
    pattern = Struct(
        "RxContext" / Int64ul,
        "FileObject" / Int64ul
    )


@declare(guid=guid("1a870028-f191-4699-8473-6fcd299eab77"), event_id=30014, version=0)
class Microsoft_Windows_Remotefs_Rdbss_30014_0(Etw):
    pattern = Struct(
        "RxContext" / Int64ul,
        "FileObject" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("1a870028-f191-4699-8473-6fcd299eab77"), event_id=30015, version=0)
class Microsoft_Windows_Remotefs_Rdbss_30015_0(Etw):
    pattern = Struct(
        "Fcb" / Int64ul
    )


@declare(guid=guid("1a870028-f191-4699-8473-6fcd299eab77"), event_id=30016, version=0)
class Microsoft_Windows_Remotefs_Rdbss_30016_0(Etw):
    pattern = Struct(
        "Fcb" / Int64ul
    )


@declare(guid=guid("1a870028-f191-4699-8473-6fcd299eab77"), event_id=30017, version=0)
class Microsoft_Windows_Remotefs_Rdbss_30017_0(Etw):
    pattern = Struct(
        "Fcb" / Int64ul
    )


@declare(guid=guid("1a870028-f191-4699-8473-6fcd299eab77"), event_id=30018, version=0)
class Microsoft_Windows_Remotefs_Rdbss_30018_0(Etw):
    pattern = Struct(
        "Fcb" / Int64ul
    )


@declare(guid=guid("1a870028-f191-4699-8473-6fcd299eab77"), event_id=30019, version=0)
class Microsoft_Windows_Remotefs_Rdbss_30019_0(Etw):
    pattern = Struct(
        "RxContext" / Int64ul,
        "LogicalPathFromLength" / Int16ul,
        "LogicalPathFrom" / Bytes(lambda this: this.LogicalPathFromLength),
        "PhysicalPathFromLength" / Int16ul,
        "PhysicalPathFrom" / Bytes(lambda this: this.PhysicalPathFromLength),
        "LogicalPathToLength" / Int16ul,
        "LogicalPathTo" / Bytes(lambda this: this.LogicalPathToLength),
        "PhysicalPathToLength" / Int16ul,
        "PhysicalPathTo" / Bytes(lambda this: this.PhysicalPathToLength)
    )


@declare(guid=guid("1a870028-f191-4699-8473-6fcd299eab77"), event_id=30020, version=0)
class Microsoft_Windows_Remotefs_Rdbss_30020_0(Etw):
    pattern = Struct(
        "RxContext" / Int64ul,
        "LogicalPathFromLength" / Int16ul,
        "LogicalPathFrom" / Bytes(lambda this: this.LogicalPathFromLength),
        "PhysicalPathFromLength" / Int16ul,
        "PhysicalPathFrom" / Bytes(lambda this: this.PhysicalPathFromLength),
        "LogicalPathToLength" / Int16ul,
        "LogicalPathTo" / Bytes(lambda this: this.LogicalPathToLength),
        "PhysicalPathToLength" / Int16ul,
        "PhysicalPathTo" / Bytes(lambda this: this.PhysicalPathToLength)
    )


@declare(guid=guid("1a870028-f191-4699-8473-6fcd299eab77"), event_id=30301, version=0)
class Microsoft_Windows_Remotefs_Rdbss_30301_0(Etw):
    pattern = Struct(
        "Fcb" / Int64ul,
        "SrvOpen" / Int64ul,
        "Fobx" / Int64ul
    )


@declare(guid=guid("1a870028-f191-4699-8473-6fcd299eab77"), event_id=30302, version=0)
class Microsoft_Windows_Remotefs_Rdbss_30302_0(Etw):
    pattern = Struct(
        "Fcb" / Int64ul,
        "SrvOpen" / Int64ul,
        "Fobx" / Int64ul
    )

