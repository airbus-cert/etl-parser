# -*- coding: utf-8 -*-
"""
Microsoft-Windows-CloudStore
GUID : 741bb90c-a7a3-49d6-bd82-1e6b858403f7
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("741bb90c-a7a3-49d6-bd82-1e6b858403f7"), event_id=1, version=0)
class Microsoft_Windows_CloudStore_1_0(Etw):
    pattern = Struct(
        "ProcessName" / WString,
        "Type" / Int32ul,
        "ErrorCode" / Int32ul,
        "File" / CString,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("741bb90c-a7a3-49d6-bd82-1e6b858403f7"), event_id=1000, version=0)
class Microsoft_Windows_CloudStore_1000_0(Etw):
    pattern = Struct(
        "SchemaProvider" / Guid
    )


@declare(guid=guid("741bb90c-a7a3-49d6-bd82-1e6b858403f7"), event_id=1001, version=0)
class Microsoft_Windows_CloudStore_1001_0(Etw):
    pattern = Struct(
        "ProviderCount" / Int32ul
    )


@declare(guid=guid("741bb90c-a7a3-49d6-bd82-1e6b858403f7"), event_id=2001, version=0)
class Microsoft_Windows_CloudStore_2001_0(Etw):
    pattern = Struct(
        "FieldId" / Int16ul,
        "BondDataType" / Int32ul
    )


@declare(guid=guid("741bb90c-a7a3-49d6-bd82-1e6b858403f7"), event_id=2004, version=0)
class Microsoft_Windows_CloudStore_2004_0(Etw):
    pattern = Struct(
        "CorrelationVector" / CString,
        "QualifiedTypeName" / CString,
        "SchemaSize" / Int32ul,
        "Schema" / Bytes(lambda this: this.SchemaSize),
        "ForceLastWriterWins" / Int8ul,
        "OriginalVersion" / Int64ul,
        "OriginalTombstoned" / Int8ul,
        "OriginalSize" / Int32ul,
        "OriginalData" / Bytes(lambda this: this.OriginalSize),
        "TheirsVersion" / Int64ul,
        "TheirsTombstoned" / Int8ul,
        "TheirsSize" / Int32ul,
        "TheirsData" / Bytes(lambda this: this.TheirsSize),
        "YoursVersion" / Int64ul,
        "YoursTombstoned" / Int8ul,
        "YoursSize" / Int32ul,
        "YoursData" / Bytes(lambda this: this.YoursSize),
        "ResolvedVersion" / Int64ul,
        "ResolvedTombstoned" / Int8ul,
        "ResolvedSize" / Int32ul,
        "ResolvedData" / Bytes(lambda this: this.ResolvedSize)
    )


@declare(guid=guid("741bb90c-a7a3-49d6-bd82-1e6b858403f7"), event_id=2007, version=0)
class Microsoft_Windows_CloudStore_2007_0(Etw):
    pattern = Struct(
        "Index" / Int64ul
    )


@declare(guid=guid("741bb90c-a7a3-49d6-bd82-1e6b858403f7"), event_id=2008, version=0)
class Microsoft_Windows_CloudStore_2008_0(Etw):
    pattern = Struct(
        "QualifiedTypeName" / CString,
        "OriginalVersion" / Int64ul,
        "TheirsVersion" / Int64ul,
        "YoursVersion" / Int64ul,
        "ResolvedVersion" / Int64ul
    )


@declare(guid=guid("741bb90c-a7a3-49d6-bd82-1e6b858403f7"), event_id=2009, version=0)
class Microsoft_Windows_CloudStore_2009_0(Etw):
    pattern = Struct(
        "QualifiedTypeName" / CString,
        "Base64String" / CString
    )


@declare(guid=guid("741bb90c-a7a3-49d6-bd82-1e6b858403f7"), event_id=2010, version=0)
class Microsoft_Windows_CloudStore_2010_0(Etw):
    pattern = Struct(
        "QualifiedTypeName" / CString
    )


@declare(guid=guid("741bb90c-a7a3-49d6-bd82-1e6b858403f7"), event_id=2011, version=0)
class Microsoft_Windows_CloudStore_2011_0(Etw):
    pattern = Struct(
        "QualifiedTypeName" / CString,
        "Size" / Int32ul,
        "Data" / Bytes(lambda this: this.Size)
    )


@declare(guid=guid("741bb90c-a7a3-49d6-bd82-1e6b858403f7"), event_id=2012, version=0)
class Microsoft_Windows_CloudStore_2012_0(Etw):
    pattern = Struct(
        "QualifiedTypeName" / CString
    )


@declare(guid=guid("741bb90c-a7a3-49d6-bd82-1e6b858403f7"), event_id=2013, version=0)
class Microsoft_Windows_CloudStore_2013_0(Etw):
    pattern = Struct(
        "QualifiedTypeName" / CString,
        "Base64String" / CString
    )


@declare(guid=guid("741bb90c-a7a3-49d6-bd82-1e6b858403f7"), event_id=3002, version=0)
class Microsoft_Windows_CloudStore_3002_0(Etw):
    pattern = Struct(
        "Id" / CString,
        "Version" / Int64ul
    )


@declare(guid=guid("741bb90c-a7a3-49d6-bd82-1e6b858403f7"), event_id=3003, version=0)
class Microsoft_Windows_CloudStore_3003_0(Etw):
    pattern = Struct(
        "Id" / CString,
        "Version" / Int64ul,
        "Size" / Int64ul
    )


@declare(guid=guid("741bb90c-a7a3-49d6-bd82-1e6b858403f7"), event_id=3004, version=0)
class Microsoft_Windows_CloudStore_3004_0(Etw):
    pattern = Struct(
        "Id" / CString
    )


@declare(guid=guid("741bb90c-a7a3-49d6-bd82-1e6b858403f7"), event_id=3005, version=0)
class Microsoft_Windows_CloudStore_3005_0(Etw):
    pattern = Struct(
        "Id" / CString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("741bb90c-a7a3-49d6-bd82-1e6b858403f7"), event_id=3006, version=0)
class Microsoft_Windows_CloudStore_3006_0(Etw):
    pattern = Struct(
        "Id" / CString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("741bb90c-a7a3-49d6-bd82-1e6b858403f7"), event_id=3007, version=0)
class Microsoft_Windows_CloudStore_3007_0(Etw):
    pattern = Struct(
        "CorrelationVector" / CString,
        "Id" / CString,
        "Version" / Int64ul,
        "Size" / Int32ul,
        "Data" / Bytes(lambda this: this.Size)
    )


@declare(guid=guid("741bb90c-a7a3-49d6-bd82-1e6b858403f7"), event_id=3008, version=0)
class Microsoft_Windows_CloudStore_3008_0(Etw):
    pattern = Struct(
        "CorrelationVector" / CString,
        "Id" / CString,
        "Version" / Int64ul,
        "Size" / Int32ul,
        "Data" / Bytes(lambda this: this.Size)
    )


@declare(guid=guid("741bb90c-a7a3-49d6-bd82-1e6b858403f7"), event_id=3013, version=0)
class Microsoft_Windows_CloudStore_3013_0(Etw):
    pattern = Struct(
        "Id" / CString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("741bb90c-a7a3-49d6-bd82-1e6b858403f7"), event_id=3014, version=0)
class Microsoft_Windows_CloudStore_3014_0(Etw):
    pattern = Struct(
        "Id" / CString,
        "TheirsVersion" / Int64ul,
        "YoursVersion" / Int64ul
    )


@declare(guid=guid("741bb90c-a7a3-49d6-bd82-1e6b858403f7"), event_id=3015, version=0)
class Microsoft_Windows_CloudStore_3015_0(Etw):
    pattern = Struct(
        "CorrelationVector" / CString,
        "Id" / CString,
        "Version" / Int64ul,
        "Size" / Int32ul,
        "Data" / Bytes(lambda this: this.Size)
    )


@declare(guid=guid("741bb90c-a7a3-49d6-bd82-1e6b858403f7"), event_id=3017, version=0)
class Microsoft_Windows_CloudStore_3017_0(Etw):
    pattern = Struct(
        "ObjectName" / WString,
        "CurrentAcl" / WString,
        "ExpectedAcl" / WString
    )


@declare(guid=guid("741bb90c-a7a3-49d6-bd82-1e6b858403f7"), event_id=3020, version=0)
class Microsoft_Windows_CloudStore_3020_0(Etw):
    pattern = Struct(
        "CorrelationVector" / CString,
        "ActivitiesCount" / Int16ul
    )

