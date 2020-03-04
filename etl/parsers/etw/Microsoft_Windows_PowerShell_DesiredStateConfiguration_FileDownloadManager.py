# -*- coding: utf-8 -*-
"""
Microsoft-Windows-PowerShell-DesiredStateConfiguration-FileDownloadManager
GUID : aaf67066-0bf8-469f-ab76-275590c434ee
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("aaf67066-0bf8-469f-ab76-275590c434ee"), event_id=4097, version=1)
class Microsoft_Windows_PowerShell_DesiredStateConfiguration_FileDownloadManager_4097_1(Etw):
    pattern = Struct(
        "ExceptionSeen" / WString
    )


@declare(guid=guid("aaf67066-0bf8-469f-ab76-275590c434ee"), event_id=4098, version=1)
class Microsoft_Windows_PowerShell_DesiredStateConfiguration_FileDownloadManager_4098_1(Etw):
    pattern = Struct(
        "ExceptionSeen" / WString
    )


@declare(guid=guid("aaf67066-0bf8-469f-ab76-275590c434ee"), event_id=4099, version=1)
class Microsoft_Windows_PowerShell_DesiredStateConfiguration_FileDownloadManager_4099_1(Etw):
    pattern = Struct(
        "FileName" / WString
    )


@declare(guid=guid("aaf67066-0bf8-469f-ab76-275590c434ee"), event_id=4100, version=1)
class Microsoft_Windows_PowerShell_DesiredStateConfiguration_FileDownloadManager_4100_1(Etw):
    pattern = Struct(
        "FileName" / WString
    )


@declare(guid=guid("aaf67066-0bf8-469f-ab76-275590c434ee"), event_id=4101, version=1)
class Microsoft_Windows_PowerShell_DesiredStateConfiguration_FileDownloadManager_4101_1(Etw):
    pattern = Struct(
        "FileName" / WString
    )


@declare(guid=guid("aaf67066-0bf8-469f-ab76-275590c434ee"), event_id=4102, version=1)
class Microsoft_Windows_PowerShell_DesiredStateConfiguration_FileDownloadManager_4102_1(Etw):
    pattern = Struct(
        "FileName" / WString
    )


@declare(guid=guid("aaf67066-0bf8-469f-ab76-275590c434ee"), event_id=4103, version=1)
class Microsoft_Windows_PowerShell_DesiredStateConfiguration_FileDownloadManager_4103_1(Etw):
    pattern = Struct(
        "FileName" / WString
    )


@declare(guid=guid("aaf67066-0bf8-469f-ab76-275590c434ee"), event_id=4104, version=1)
class Microsoft_Windows_PowerShell_DesiredStateConfiguration_FileDownloadManager_4104_1(Etw):
    pattern = Struct(
        "Checksum" / WString,
        "FileName" / WString
    )


@declare(guid=guid("aaf67066-0bf8-469f-ab76-275590c434ee"), event_id=4106, version=1)
class Microsoft_Windows_PowerShell_DesiredStateConfiguration_FileDownloadManager_4106_1(Etw):
    pattern = Struct(
        "FileName" / WString
    )


@declare(guid=guid("aaf67066-0bf8-469f-ab76-275590c434ee"), event_id=4107, version=1)
class Microsoft_Windows_PowerShell_DesiredStateConfiguration_FileDownloadManager_4107_1(Etw):
    pattern = Struct(
        "GeneratedChecksum" / WString,
        "ExpectedChecksum" / WString,
        "FileName" / WString
    )


@declare(guid=guid("aaf67066-0bf8-469f-ab76-275590c434ee"), event_id=4108, version=1)
class Microsoft_Windows_PowerShell_DesiredStateConfiguration_FileDownloadManager_4108_1(Etw):
    pattern = Struct(
        "FileName" / WString
    )


@declare(guid=guid("aaf67066-0bf8-469f-ab76-275590c434ee"), event_id=4109, version=1)
class Microsoft_Windows_PowerShell_DesiredStateConfiguration_FileDownloadManager_4109_1(Etw):
    pattern = Struct(
        "FileName" / WString
    )


@declare(guid=guid("aaf67066-0bf8-469f-ab76-275590c434ee"), event_id=4110, version=1)
class Microsoft_Windows_PowerShell_DesiredStateConfiguration_FileDownloadManager_4110_1(Etw):
    pattern = Struct(
        "FileName" / WString
    )


@declare(guid=guid("aaf67066-0bf8-469f-ab76-275590c434ee"), event_id=4111, version=1)
class Microsoft_Windows_PowerShell_DesiredStateConfiguration_FileDownloadManager_4111_1(Etw):
    pattern = Struct(
        "SourceFile" / WString,
        "DestFile" / WString
    )


@declare(guid=guid("aaf67066-0bf8-469f-ab76-275590c434ee"), event_id=4112, version=1)
class Microsoft_Windows_PowerShell_DesiredStateConfiguration_FileDownloadManager_4112_1(Etw):
    pattern = Struct(
        "FileName" / WString
    )


@declare(guid=guid("aaf67066-0bf8-469f-ab76-275590c434ee"), event_id=4113, version=1)
class Microsoft_Windows_PowerShell_DesiredStateConfiguration_FileDownloadManager_4113_1(Etw):
    pattern = Struct(
        "FileName" / WString
    )


@declare(guid=guid("aaf67066-0bf8-469f-ab76-275590c434ee"), event_id=4114, version=1)
class Microsoft_Windows_PowerShell_DesiredStateConfiguration_FileDownloadManager_4114_1(Etw):
    pattern = Struct(
        "FileName" / WString
    )


@declare(guid=guid("aaf67066-0bf8-469f-ab76-275590c434ee"), event_id=4115, version=1)
class Microsoft_Windows_PowerShell_DesiredStateConfiguration_FileDownloadManager_4115_1(Etw):
    pattern = Struct(
        "FileName" / WString
    )


@declare(guid=guid("aaf67066-0bf8-469f-ab76-275590c434ee"), event_id=4116, version=1)
class Microsoft_Windows_PowerShell_DesiredStateConfiguration_FileDownloadManager_4116_1(Etw):
    pattern = Struct(
        "FileName" / WString
    )


@declare(guid=guid("aaf67066-0bf8-469f-ab76-275590c434ee"), event_id=4117, version=1)
class Microsoft_Windows_PowerShell_DesiredStateConfiguration_FileDownloadManager_4117_1(Etw):
    pattern = Struct(
        "FileName" / WString
    )


@declare(guid=guid("aaf67066-0bf8-469f-ab76-275590c434ee"), event_id=4118, version=1)
class Microsoft_Windows_PowerShell_DesiredStateConfiguration_FileDownloadManager_4118_1(Etw):
    pattern = Struct(
        "ExceptionSeen" / WString
    )


@declare(guid=guid("aaf67066-0bf8-469f-ab76-275590c434ee"), event_id=4119, version=1)
class Microsoft_Windows_PowerShell_DesiredStateConfiguration_FileDownloadManager_4119_1(Etw):
    pattern = Struct(
        "ExceptionSeen" / WString
    )


@declare(guid=guid("aaf67066-0bf8-469f-ab76-275590c434ee"), event_id=4120, version=1)
class Microsoft_Windows_PowerShell_DesiredStateConfiguration_FileDownloadManager_4120_1(Etw):
    pattern = Struct(
        "FileName" / WString
    )

