# -*- coding: utf-8 -*-
"""
Microsoft-Windows-WPDClassInstaller
GUID : ad5162d8-daf0-4a25-88a7-01cbeb33902e
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("ad5162d8-daf0-4a25-88a7-01cbeb33902e"), event_id=100, version=0)
class Microsoft_Windows_WPDClassInstaller_100_0(Etw):
    pattern = Struct(
        "InstallFunctionCode" / Int32ul,
        "InstallFunctionName" / WString
    )


@declare(guid=guid("ad5162d8-daf0-4a25-88a7-01cbeb33902e"), event_id=101, version=0)
class Microsoft_Windows_WPDClassInstaller_101_0(Etw):
    pattern = Struct(
        "InstallFunctionCode" / Int32ul,
        "InstallFunctionName" / WString,
        "ReturnCode" / Int32ul
    )


@declare(guid=guid("ad5162d8-daf0-4a25-88a7-01cbeb33902e"), event_id=102, version=0)
class Microsoft_Windows_WPDClassInstaller_102_0(Etw):
    pattern = Struct(
        "DevicePath" / WString
    )


@declare(guid=guid("ad5162d8-daf0-4a25-88a7-01cbeb33902e"), event_id=103, version=0)
class Microsoft_Windows_WPDClassInstaller_103_0(Etw):
    pattern = Struct(
        "DevicePath" / WString,
        "ReturnCode" / Int32ul
    )


@declare(guid=guid("ad5162d8-daf0-4a25-88a7-01cbeb33902e"), event_id=104, version=0)
class Microsoft_Windows_WPDClassInstaller_104_0(Etw):
    pattern = Struct(
        "DevicePath" / WString
    )


@declare(guid=guid("ad5162d8-daf0-4a25-88a7-01cbeb33902e"), event_id=105, version=0)
class Microsoft_Windows_WPDClassInstaller_105_0(Etw):
    pattern = Struct(
        "DevicePath" / WString,
        "ReturnCode" / Int32ul
    )


@declare(guid=guid("ad5162d8-daf0-4a25-88a7-01cbeb33902e"), event_id=201, version=0)
class Microsoft_Windows_WPDClassInstaller_201_0(Etw):
    pattern = Struct(
        "DevicePath" / WString,
        "MetadataLocaleName" / WString,
        "MetadataContentId" / Guid
    )


@declare(guid=guid("ad5162d8-daf0-4a25-88a7-01cbeb33902e"), event_id=202, version=0)
class Microsoft_Windows_WPDClassInstaller_202_0(Etw):
    pattern = Struct(
        "DevicePath" / WString,
        "MetadataLocaleName" / WString,
        "MetadataContentId" / Guid,
        "ReturnCode" / Int32ul
    )


@declare(guid=guid("ad5162d8-daf0-4a25-88a7-01cbeb33902e"), event_id=203, version=0)
class Microsoft_Windows_WPDClassInstaller_203_0(Etw):
    pattern = Struct(
        "DevicePath" / WString,
        "MetadataLocaleName" / WString,
        "MetadataContentId" / Guid,
        "ReturnCode" / Int32ul
    )


@declare(guid=guid("ad5162d8-daf0-4a25-88a7-01cbeb33902e"), event_id=204, version=0)
class Microsoft_Windows_WPDClassInstaller_204_0(Etw):
    pattern = Struct(
        "DevicePath" / WString,
        "ReturnCode" / Int32ul
    )


@declare(guid=guid("ad5162d8-daf0-4a25-88a7-01cbeb33902e"), event_id=205, version=0)
class Microsoft_Windows_WPDClassInstaller_205_0(Etw):
    pattern = Struct(
        "DevicePath" / WString,
        "ServicePath" / WString
    )


@declare(guid=guid("ad5162d8-daf0-4a25-88a7-01cbeb33902e"), event_id=206, version=0)
class Microsoft_Windows_WPDClassInstaller_206_0(Etw):
    pattern = Struct(
        "MetadataLocaleName" / WString,
        "MetadataContentId" / Guid
    )

