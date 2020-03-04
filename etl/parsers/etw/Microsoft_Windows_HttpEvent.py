# -*- coding: utf-8 -*-
"""
Microsoft-Windows-HttpEvent
GUID : 7b6bc78c-898b-4170-bbf8-1a469ea43fc5
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("7b6bc78c-898b-4170-bbf8-1a469ea43fc5"), event_id=15000, version=0)
class Microsoft_Windows_HttpEvent_15000_0(Etw):
    pattern = Struct(
        "DeviceObject" / WString,
        "LogFile" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7b6bc78c-898b-4170-bbf8-1a469ea43fc5"), event_id=15001, version=0)
class Microsoft_Windows_HttpEvent_15001_0(Etw):
    pattern = Struct(
        "DeviceObject" / WString,
        "SiteId" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7b6bc78c-898b-4170-bbf8-1a469ea43fc5"), event_id=15002, version=0)
class Microsoft_Windows_HttpEvent_15002_0(Etw):
    pattern = Struct(
        "DeviceObject" / WString,
        "LogFile" / WString,
        "SiteId" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7b6bc78c-898b-4170-bbf8-1a469ea43fc5"), event_id=15004, version=0)
class Microsoft_Windows_HttpEvent_15004_0(Etw):
    pattern = Struct(
        "DeviceObject" / WString,
        "LogFile" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7b6bc78c-898b-4170-bbf8-1a469ea43fc5"), event_id=15005, version=0)
class Microsoft_Windows_HttpEvent_15005_0(Etw):
    pattern = Struct(
        "DeviceObject" / WString,
        "Address" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7b6bc78c-898b-4170-bbf8-1a469ea43fc5"), event_id=15006, version=0)
class Microsoft_Windows_HttpEvent_15006_0(Etw):
    pattern = Struct(
        "DeviceObject" / WString,
        "Directory" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7b6bc78c-898b-4170-bbf8-1a469ea43fc5"), event_id=15007, version=0)
class Microsoft_Windows_HttpEvent_15007_0(Etw):
    pattern = Struct(
        "DeviceObject" / WString,
        "Url" / WString
    )


@declare(guid=guid("7b6bc78c-898b-4170-bbf8-1a469ea43fc5"), event_id=15008, version=0)
class Microsoft_Windows_HttpEvent_15008_0(Etw):
    pattern = Struct(
        "DeviceObject" / WString,
        "Url" / WString
    )


@declare(guid=guid("7b6bc78c-898b-4170-bbf8-1a469ea43fc5"), event_id=15010, version=0)
class Microsoft_Windows_HttpEvent_15010_0(Etw):
    pattern = Struct(
        "DeviceObject" / WString,
        "Url" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7b6bc78c-898b-4170-bbf8-1a469ea43fc5"), event_id=15014, version=0)
class Microsoft_Windows_HttpEvent_15014_0(Etw):
    pattern = Struct(
        "DeviceObject" / WString,
        "Address" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7b6bc78c-898b-4170-bbf8-1a469ea43fc5"), event_id=15016, version=0)
class Microsoft_Windows_HttpEvent_15016_0(Etw):
    pattern = Struct(
        "DeviceObject" / WString,
        "SecurityPackage" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7b6bc78c-898b-4170-bbf8-1a469ea43fc5"), event_id=15018, version=0)
class Microsoft_Windows_HttpEvent_15018_0(Etw):
    pattern = Struct(
        "DeviceObject" / WString,
        "LogFile" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7b6bc78c-898b-4170-bbf8-1a469ea43fc5"), event_id=15019, version=0)
class Microsoft_Windows_HttpEvent_15019_0(Etw):
    pattern = Struct(
        "DeviceObject" / WString,
        "Host" / WString
    )


@declare(guid=guid("7b6bc78c-898b-4170-bbf8-1a469ea43fc5"), event_id=15020, version=0)
class Microsoft_Windows_HttpEvent_15020_0(Etw):
    pattern = Struct(
        "DeviceObject" / WString,
        "Host" / WString
    )


@declare(guid=guid("7b6bc78c-898b-4170-bbf8-1a469ea43fc5"), event_id=15021, version=0)
class Microsoft_Windows_HttpEvent_15021_0(Etw):
    pattern = Struct(
        "DeviceObject" / WString,
        "Endpoint" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7b6bc78c-898b-4170-bbf8-1a469ea43fc5"), event_id=15022, version=0)
class Microsoft_Windows_HttpEvent_15022_0(Etw):
    pattern = Struct(
        "DeviceObject" / WString,
        "Status" / WString
    )


@declare(guid=guid("7b6bc78c-898b-4170-bbf8-1a469ea43fc5"), event_id=15300, version=0)
class Microsoft_Windows_HttpEvent_15300_0(Etw):
    pattern = Struct(
        "DeviceObject" / WString,
        "Endpoint" / WString
    )


@declare(guid=guid("7b6bc78c-898b-4170-bbf8-1a469ea43fc5"), event_id=15301, version=0)
class Microsoft_Windows_HttpEvent_15301_0(Etw):
    pattern = Struct(
        "DeviceObject" / WString,
        "Endpoint" / WString
    )


@declare(guid=guid("7b6bc78c-898b-4170-bbf8-1a469ea43fc5"), event_id=15302, version=0)
class Microsoft_Windows_HttpEvent_15302_0(Etw):
    pattern = Struct(
        "DeviceObject" / WString,
        "Endpoint" / WString
    )

