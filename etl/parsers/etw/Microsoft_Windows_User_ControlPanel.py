# -*- coding: utf-8 -*-
"""
Microsoft-Windows-User-ControlPanel
GUID : 319122a9-1485-4e48-af35-7db2d93b8ad2
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("319122a9-1485-4e48-af35-7db2d93b8ad2"), event_id=8001, version=0)
class Microsoft_Windows_User_ControlPanel_8001_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("319122a9-1485-4e48-af35-7db2d93b8ad2"), event_id=8002, version=0)
class Microsoft_Windows_User_ControlPanel_8002_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("319122a9-1485-4e48-af35-7db2d93b8ad2"), event_id=8003, version=0)
class Microsoft_Windows_User_ControlPanel_8003_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("319122a9-1485-4e48-af35-7db2d93b8ad2"), event_id=8004, version=0)
class Microsoft_Windows_User_ControlPanel_8004_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("319122a9-1485-4e48-af35-7db2d93b8ad2"), event_id=8005, version=0)
class Microsoft_Windows_User_ControlPanel_8005_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("319122a9-1485-4e48-af35-7db2d93b8ad2"), event_id=8006, version=0)
class Microsoft_Windows_User_ControlPanel_8006_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("319122a9-1485-4e48-af35-7db2d93b8ad2"), event_id=8007, version=0)
class Microsoft_Windows_User_ControlPanel_8007_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("319122a9-1485-4e48-af35-7db2d93b8ad2"), event_id=8008, version=0)
class Microsoft_Windows_User_ControlPanel_8008_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("319122a9-1485-4e48-af35-7db2d93b8ad2"), event_id=8009, version=0)
class Microsoft_Windows_User_ControlPanel_8009_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("319122a9-1485-4e48-af35-7db2d93b8ad2"), event_id=8010, version=0)
class Microsoft_Windows_User_ControlPanel_8010_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("319122a9-1485-4e48-af35-7db2d93b8ad2"), event_id=8011, version=0)
class Microsoft_Windows_User_ControlPanel_8011_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("319122a9-1485-4e48-af35-7db2d93b8ad2"), event_id=8012, version=0)
class Microsoft_Windows_User_ControlPanel_8012_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("319122a9-1485-4e48-af35-7db2d93b8ad2"), event_id=8013, version=0)
class Microsoft_Windows_User_ControlPanel_8013_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("319122a9-1485-4e48-af35-7db2d93b8ad2"), event_id=8014, version=0)
class Microsoft_Windows_User_ControlPanel_8014_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("319122a9-1485-4e48-af35-7db2d93b8ad2"), event_id=8015, version=0)
class Microsoft_Windows_User_ControlPanel_8015_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("319122a9-1485-4e48-af35-7db2d93b8ad2"), event_id=8016, version=0)
class Microsoft_Windows_User_ControlPanel_8016_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("319122a9-1485-4e48-af35-7db2d93b8ad2"), event_id=8017, version=0)
class Microsoft_Windows_User_ControlPanel_8017_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("319122a9-1485-4e48-af35-7db2d93b8ad2"), event_id=8018, version=0)
class Microsoft_Windows_User_ControlPanel_8018_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("319122a9-1485-4e48-af35-7db2d93b8ad2"), event_id=8019, version=0)
class Microsoft_Windows_User_ControlPanel_8019_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("319122a9-1485-4e48-af35-7db2d93b8ad2"), event_id=8020, version=0)
class Microsoft_Windows_User_ControlPanel_8020_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("319122a9-1485-4e48-af35-7db2d93b8ad2"), event_id=8021, version=0)
class Microsoft_Windows_User_ControlPanel_8021_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("319122a9-1485-4e48-af35-7db2d93b8ad2"), event_id=8022, version=0)
class Microsoft_Windows_User_ControlPanel_8022_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("319122a9-1485-4e48-af35-7db2d93b8ad2"), event_id=8023, version=0)
class Microsoft_Windows_User_ControlPanel_8023_0(Etw):
    pattern = Struct(
        "SqmSessionGuid" / Guid,
        "SqmID" / Int32ul,
        "SqmType" / Int32ul,
        "SqmDWORDDatapointValue" / Int32ul
    )


@declare(guid=guid("319122a9-1485-4e48-af35-7db2d93b8ad2"), event_id=9001, version=0)
class Microsoft_Windows_User_ControlPanel_9001_0(Etw):
    pattern = Struct(
        "Method" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("319122a9-1485-4e48-af35-7db2d93b8ad2"), event_id=9002, version=0)
class Microsoft_Windows_User_ControlPanel_9002_0(Etw):
    pattern = Struct(
        "Method" / WString,
        "Iteration" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("319122a9-1485-4e48-af35-7db2d93b8ad2"), event_id=25000, version=0)
class Microsoft_Windows_User_ControlPanel_25000_0(Etw):
    pattern = Struct(
        "TaskFlowID" / Int32ul,
        "PageIndex" / Int32ul
    )


@declare(guid=guid("319122a9-1485-4e48-af35-7db2d93b8ad2"), event_id=25001, version=0)
class Microsoft_Windows_User_ControlPanel_25001_0(Etw):
    pattern = Struct(
        "TaskFlowID" / Int32ul,
        "PageIndex" / Int32ul
    )

