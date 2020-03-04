# -*- coding: utf-8 -*-
"""
Microsoft-Windows-FileHistory-Catalog
GUID : b447b4dc-7780-11e0-ada3-18a90531a85a
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("b447b4dc-7780-11e0-ada3-18a90531a85a"), event_id=1, version=0)
class Microsoft_Windows_FileHistory_Catalog_1_0(Etw):
    pattern = Struct(
        "CatalogPath" / WString,
        "CatalogPath2" / WString,
        "ReadOnly" / Int32sl
    )


@declare(guid=guid("b447b4dc-7780-11e0-ada3-18a90531a85a"), event_id=2, version=0)
class Microsoft_Windows_FileHistory_Catalog_2_0(Etw):
    pattern = Struct(
        "CatalogPath" / WString,
        "CatalogPath2" / WString,
        "ReadOnly" / Int32sl
    )


@declare(guid=guid("b447b4dc-7780-11e0-ada3-18a90531a85a"), event_id=5, version=0)
class Microsoft_Windows_FileHistory_Catalog_5_0(Etw):
    pattern = Struct(
        "CatalogPath" / WString,
        "CatalogPath2" / WString
    )


@declare(guid=guid("b447b4dc-7780-11e0-ada3-18a90531a85a"), event_id=6, version=0)
class Microsoft_Windows_FileHistory_Catalog_6_0(Etw):
    pattern = Struct(
        "CatalogPath" / WString,
        "CatalogPath2" / WString
    )


@declare(guid=guid("b447b4dc-7780-11e0-ada3-18a90531a85a"), event_id=7, version=0)
class Microsoft_Windows_FileHistory_Catalog_7_0(Etw):
    pattern = Struct(
        "Path" / WString
    )


@declare(guid=guid("b447b4dc-7780-11e0-ada3-18a90531a85a"), event_id=8, version=0)
class Microsoft_Windows_FileHistory_Catalog_8_0(Etw):
    pattern = Struct(
        "Path" / WString
    )


@declare(guid=guid("b447b4dc-7780-11e0-ada3-18a90531a85a"), event_id=9, version=0)
class Microsoft_Windows_FileHistory_Catalog_9_0(Etw):
    pattern = Struct(
        "id" / Int32sl,
        "Path" / WString
    )


@declare(guid=guid("b447b4dc-7780-11e0-ada3-18a90531a85a"), event_id=10, version=0)
class Microsoft_Windows_FileHistory_Catalog_10_0(Etw):
    pattern = Struct(
        "id" / Int32sl,
        "Path" / WString
    )


@declare(guid=guid("b447b4dc-7780-11e0-ada3-18a90531a85a"), event_id=11, version=0)
class Microsoft_Windows_FileHistory_Catalog_11_0(Etw):
    pattern = Struct(
        "id" / Int32sl
    )


@declare(guid=guid("b447b4dc-7780-11e0-ada3-18a90531a85a"), event_id=12, version=0)
class Microsoft_Windows_FileHistory_Catalog_12_0(Etw):
    pattern = Struct(
        "id" / Int32sl
    )


@declare(guid=guid("b447b4dc-7780-11e0-ada3-18a90531a85a"), event_id=13, version=0)
class Microsoft_Windows_FileHistory_Catalog_13_0(Etw):
    pattern = Struct(
        "Path" / WString
    )


@declare(guid=guid("b447b4dc-7780-11e0-ada3-18a90531a85a"), event_id=14, version=0)
class Microsoft_Windows_FileHistory_Catalog_14_0(Etw):
    pattern = Struct(
        "Path" / WString
    )


@declare(guid=guid("b447b4dc-7780-11e0-ada3-18a90531a85a"), event_id=15, version=0)
class Microsoft_Windows_FileHistory_Catalog_15_0(Etw):
    pattern = Struct(
        "id" / Int32sl,
        "Path" / WString
    )


@declare(guid=guid("b447b4dc-7780-11e0-ada3-18a90531a85a"), event_id=16, version=0)
class Microsoft_Windows_FileHistory_Catalog_16_0(Etw):
    pattern = Struct(
        "id" / Int32sl,
        "Path" / WString
    )


@declare(guid=guid("b447b4dc-7780-11e0-ada3-18a90531a85a"), event_id=17, version=0)
class Microsoft_Windows_FileHistory_Catalog_17_0(Etw):
    pattern = Struct(
        "id" / Int32sl
    )


@declare(guid=guid("b447b4dc-7780-11e0-ada3-18a90531a85a"), event_id=18, version=0)
class Microsoft_Windows_FileHistory_Catalog_18_0(Etw):
    pattern = Struct(
        "id" / Int32sl
    )


@declare(guid=guid("b447b4dc-7780-11e0-ada3-18a90531a85a"), event_id=19, version=0)
class Microsoft_Windows_FileHistory_Catalog_19_0(Etw):
    pattern = Struct(
        "Path" / WString,
        "InitialPosition" / Int32sl
    )


@declare(guid=guid("b447b4dc-7780-11e0-ada3-18a90531a85a"), event_id=20, version=0)
class Microsoft_Windows_FileHistory_Catalog_20_0(Etw):
    pattern = Struct(
        "Path" / WString,
        "InitialPosition" / Int32sl
    )


@declare(guid=guid("b447b4dc-7780-11e0-ada3-18a90531a85a"), event_id=21, version=0)
class Microsoft_Windows_FileHistory_Catalog_21_0(Etw):
    pattern = Struct(
        "Path" / WString,
        "BackupSetId" / Int32sl
    )


@declare(guid=guid("b447b4dc-7780-11e0-ada3-18a90531a85a"), event_id=22, version=0)
class Microsoft_Windows_FileHistory_Catalog_22_0(Etw):
    pattern = Struct(
        "Path" / WString,
        "BackupSetId" / Int32sl
    )


@declare(guid=guid("b447b4dc-7780-11e0-ada3-18a90531a85a"), event_id=23, version=0)
class Microsoft_Windows_FileHistory_Catalog_23_0(Etw):
    pattern = Struct(
        "FileRecordId" / Int32sl
    )


@declare(guid=guid("b447b4dc-7780-11e0-ada3-18a90531a85a"), event_id=24, version=0)
class Microsoft_Windows_FileHistory_Catalog_24_0(Etw):
    pattern = Struct(
        "FileRecordId" / Int32sl
    )


@declare(guid=guid("b447b4dc-7780-11e0-ada3-18a90531a85a"), event_id=25, version=0)
class Microsoft_Windows_FileHistory_Catalog_25_0(Etw):
    pattern = Struct(
        "State" / Int32sl,
        "Sort" / Int32sl
    )


@declare(guid=guid("b447b4dc-7780-11e0-ada3-18a90531a85a"), event_id=26, version=0)
class Microsoft_Windows_FileHistory_Catalog_26_0(Etw):
    pattern = Struct(
        "State" / Int32sl,
        "Sort" / Int32sl
    )


@declare(guid=guid("b447b4dc-7780-11e0-ada3-18a90531a85a"), event_id=29, version=0)
class Microsoft_Windows_FileHistory_Catalog_29_0(Etw):
    pattern = Struct(
        "LibraryName" / WString
    )


@declare(guid=guid("b447b4dc-7780-11e0-ada3-18a90531a85a"), event_id=30, version=0)
class Microsoft_Windows_FileHistory_Catalog_30_0(Etw):
    pattern = Struct(
        "LibraryName" / WString
    )


@declare(guid=guid("b447b4dc-7780-11e0-ada3-18a90531a85a"), event_id=31, version=0)
class Microsoft_Windows_FileHistory_Catalog_31_0(Etw):
    pattern = Struct(
        "BackupSetId" / Int32sl
    )


@declare(guid=guid("b447b4dc-7780-11e0-ada3-18a90531a85a"), event_id=32, version=0)
class Microsoft_Windows_FileHistory_Catalog_32_0(Etw):
    pattern = Struct(
        "BackupSetId" / Int32sl
    )


@declare(guid=guid("b447b4dc-7780-11e0-ada3-18a90531a85a"), event_id=33, version=0)
class Microsoft_Windows_FileHistory_Catalog_33_0(Etw):
    pattern = Struct(
        "LibraryName" / WString,
        "BackupSetId" / Int32sl
    )


@declare(guid=guid("b447b4dc-7780-11e0-ada3-18a90531a85a"), event_id=34, version=0)
class Microsoft_Windows_FileHistory_Catalog_34_0(Etw):
    pattern = Struct(
        "LibraryName" / WString,
        "BackupSetId" / Int32sl
    )


@declare(guid=guid("b447b4dc-7780-11e0-ada3-18a90531a85a"), event_id=39, version=0)
class Microsoft_Windows_FileHistory_Catalog_39_0(Etw):
    pattern = Struct(
        "IteratorName" / WString
    )


@declare(guid=guid("b447b4dc-7780-11e0-ada3-18a90531a85a"), event_id=40, version=0)
class Microsoft_Windows_FileHistory_Catalog_40_0(Etw):
    pattern = Struct(
        "IteratorName" / WString
    )


@declare(guid=guid("b447b4dc-7780-11e0-ada3-18a90531a85a"), event_id=41, version=0)
class Microsoft_Windows_FileHistory_Catalog_41_0(Etw):
    pattern = Struct(
        "IteratorName" / WString
    )


@declare(guid=guid("b447b4dc-7780-11e0-ada3-18a90531a85a"), event_id=42, version=0)
class Microsoft_Windows_FileHistory_Catalog_42_0(Etw):
    pattern = Struct(
        "IteratorName" / WString
    )


@declare(guid=guid("b447b4dc-7780-11e0-ada3-18a90531a85a"), event_id=43, version=0)
class Microsoft_Windows_FileHistory_Catalog_43_0(Etw):
    pattern = Struct(
        "BackupSetId" / Int32sl
    )


@declare(guid=guid("b447b4dc-7780-11e0-ada3-18a90531a85a"), event_id=44, version=0)
class Microsoft_Windows_FileHistory_Catalog_44_0(Etw):
    pattern = Struct(
        "BackupSetId" / Int32sl
    )

