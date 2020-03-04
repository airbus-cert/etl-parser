# -*- coding: utf-8 -*-
"""
Microsoft-Windows-OverlayFilter
GUID : 46c78e5c-a213-46a8-8a6b-622f6916201d
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("46c78e5c-a213-46a8-8a6b-622f6916201d"), event_id=24832, version=0)
class Microsoft_Windows_OverlayFilter_24832_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength),
        "DataSourceId" / Int64sl,
        "Status" / Int32ul
    )


@declare(guid=guid("46c78e5c-a213-46a8-8a6b-622f6916201d"), event_id=24833, version=0)
class Microsoft_Windows_OverlayFilter_24833_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength),
        "BlockNumber" / Int32ul,
        "BlockLength" / Int32ul
    )


@declare(guid=guid("46c78e5c-a213-46a8-8a6b-622f6916201d"), event_id=24834, version=0)
class Microsoft_Windows_OverlayFilter_24834_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength),
        "FileOffset" / Int64sl,
        "ReadSize" / Int32ul
    )


@declare(guid=guid("46c78e5c-a213-46a8-8a6b-622f6916201d"), event_id=24835, version=0)
class Microsoft_Windows_OverlayFilter_24835_0(Etw):
    pattern = Struct(
        "volume" / WString
    )


@declare(guid=guid("46c78e5c-a213-46a8-8a6b-622f6916201d"), event_id=24836, version=0)
class Microsoft_Windows_OverlayFilter_24836_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("46c78e5c-a213-46a8-8a6b-622f6916201d"), event_id=24837, version=0)
class Microsoft_Windows_OverlayFilter_24837_0(Etw):
    pattern = Struct(
        "wimHashFile" / WString,
        "wimFile" / WString
    )


@declare(guid=guid("46c78e5c-a213-46a8-8a6b-622f6916201d"), event_id=24838, version=0)
class Microsoft_Windows_OverlayFilter_24838_0(Etw):
    pattern = Struct(
        "wimHashFile" / WString,
        "wimFile" / WString
    )


@declare(guid=guid("46c78e5c-a213-46a8-8a6b-622f6916201d"), event_id=24839, version=0)
class Microsoft_Windows_OverlayFilter_24839_0(Etw):
    pattern = Struct(
        "wimHashFile" / WString,
        "wimFile" / WString
    )


@declare(guid=guid("46c78e5c-a213-46a8-8a6b-622f6916201d"), event_id=24840, version=0)
class Microsoft_Windows_OverlayFilter_24840_0(Etw):
    pattern = Struct(
        "filename" / WString,
        "offset" / Int64ul
    )


@declare(guid=guid("46c78e5c-a213-46a8-8a6b-622f6916201d"), event_id=24841, version=0)
class Microsoft_Windows_OverlayFilter_24841_0(Etw):
    pattern = Struct(
        "filename" / WString,
        "offset" / Int64ul
    )


@declare(guid=guid("46c78e5c-a213-46a8-8a6b-622f6916201d"), event_id=24842, version=0)
class Microsoft_Windows_OverlayFilter_24842_0(Etw):
    pattern = Struct(
        "hr" / Int32ul
    )


@declare(guid=guid("46c78e5c-a213-46a8-8a6b-622f6916201d"), event_id=24843, version=0)
class Microsoft_Windows_OverlayFilter_24843_0(Etw):
    pattern = Struct(
        "wimHashFile" / WString,
        "wimFile" / WString,
        "hr" / Int32sl
    )


@declare(guid=guid("46c78e5c-a213-46a8-8a6b-622f6916201d"), event_id=24844, version=0)
class Microsoft_Windows_OverlayFilter_24844_0(Etw):
    pattern = Struct(
        "wimHashFile" / WString,
        "wimFile" / WString,
        "hr" / Int32sl
    )


@declare(guid=guid("46c78e5c-a213-46a8-8a6b-622f6916201d"), event_id=24845, version=0)
class Microsoft_Windows_OverlayFilter_24845_0(Etw):
    pattern = Struct(
        "wimHashFile" / WString,
        "wimFile" / WString,
        "hr" / Int32sl
    )


@declare(guid=guid("46c78e5c-a213-46a8-8a6b-622f6916201d"), event_id=24846, version=0)
class Microsoft_Windows_OverlayFilter_24846_0(Etw):
    pattern = Struct(
        "wimHashFile" / WString,
        "wimFile" / WString,
        "hr" / Int32sl
    )


@declare(guid=guid("46c78e5c-a213-46a8-8a6b-622f6916201d"), event_id=24847, version=0)
class Microsoft_Windows_OverlayFilter_24847_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength),
        "DataSourceId" / Int64sl
    )


@declare(guid=guid("46c78e5c-a213-46a8-8a6b-622f6916201d"), event_id=24848, version=0)
class Microsoft_Windows_OverlayFilter_24848_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength),
        "DataSourceId" / Int64sl
    )

