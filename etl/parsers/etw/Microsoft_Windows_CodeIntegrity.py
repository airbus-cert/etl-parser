# -*- coding: utf-8 -*-
"""
Microsoft-Windows-CodeIntegrity
GUID : 4ee76bd8-3cf4-44a0-a0ac-3937643e37a3
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3001, version=0)
class Microsoft_Windows_CodeIntegrity_3001_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3001, version=1)
class Microsoft_Windows_CodeIntegrity_3001_1(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength),
        "SecureRequired" / Int32ul,
        "RequestedSigningLevel" / Int8ul,
        "ProcessNameLength" / Int16ul,
        "ProcessNameBuffer" / Bytes(lambda this: this.ProcessNameLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3002, version=0)
class Microsoft_Windows_CodeIntegrity_3002_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3002, version=1)
class Microsoft_Windows_CodeIntegrity_3002_1(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength),
        "SecureRequired" / Int32ul,
        "RequestedSigningLevel" / Int8ul,
        "ProcessNameLength" / Int16ul,
        "ProcessNameBuffer" / Bytes(lambda this: this.ProcessNameLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3003, version=0)
class Microsoft_Windows_CodeIntegrity_3003_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3003, version=1)
class Microsoft_Windows_CodeIntegrity_3003_1(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength),
        "SecureRequired" / Int32ul,
        "RequestedSigningLevel" / Int8ul,
        "ProcessNameLength" / Int16ul,
        "ProcessNameBuffer" / Bytes(lambda this: this.ProcessNameLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3004, version=0)
class Microsoft_Windows_CodeIntegrity_3004_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3004, version=1)
class Microsoft_Windows_CodeIntegrity_3004_1(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength),
        "SecureRequired" / Int32ul,
        "RequestedSigningLevel" / Int8ul,
        "ProcessNameLength" / Int16ul,
        "ProcessNameBuffer" / Bytes(lambda this: this.ProcessNameLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3005, version=0)
class Microsoft_Windows_CodeIntegrity_3005_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3005, version=1)
class Microsoft_Windows_CodeIntegrity_3005_1(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength),
        "SecureRequired" / Int32ul,
        "RequestedSigningLevel" / Int8ul,
        "ProcessNameLength" / Int16ul,
        "ProcessNameBuffer" / Bytes(lambda this: this.ProcessNameLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3006, version=0)
class Microsoft_Windows_CodeIntegrity_3006_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength),
        "CatalogNameLength" / Int16ul,
        "CatalogNameBuffer" / Bytes(lambda this: this.CatalogNameLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3007, version=0)
class Microsoft_Windows_CodeIntegrity_3007_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3008, version=0)
class Microsoft_Windows_CodeIntegrity_3008_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength),
        "CatalogNameLength" / Int16ul,
        "CatalogNameBuffer" / Bytes(lambda this: this.CatalogNameLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3009, version=0)
class Microsoft_Windows_CodeIntegrity_3009_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3010, version=0)
class Microsoft_Windows_CodeIntegrity_3010_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3010, version=1)
class Microsoft_Windows_CodeIntegrity_3010_1(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength),
        "Status" / Int32ul
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3011, version=0)
class Microsoft_Windows_CodeIntegrity_3011_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3012, version=0)
class Microsoft_Windows_CodeIntegrity_3012_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3014, version=0)
class Microsoft_Windows_CodeIntegrity_3014_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3014, version=1)
class Microsoft_Windows_CodeIntegrity_3014_1(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3015, version=0)
class Microsoft_Windows_CodeIntegrity_3015_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3016, version=0)
class Microsoft_Windows_CodeIntegrity_3016_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3016, version=1)
class Microsoft_Windows_CodeIntegrity_3016_1(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3017, version=0)
class Microsoft_Windows_CodeIntegrity_3017_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3018, version=0)
class Microsoft_Windows_CodeIntegrity_3018_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3018, version=1)
class Microsoft_Windows_CodeIntegrity_3018_1(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3019, version=0)
class Microsoft_Windows_CodeIntegrity_3019_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3020, version=0)
class Microsoft_Windows_CodeIntegrity_3020_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3020, version=1)
class Microsoft_Windows_CodeIntegrity_3020_1(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3021, version=0)
class Microsoft_Windows_CodeIntegrity_3021_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3021, version=1)
class Microsoft_Windows_CodeIntegrity_3021_1(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength),
        "SecureRequired" / Int32ul,
        "RequestedSigningLevel" / Int8ul,
        "ProcessNameLength" / Int16ul,
        "ProcessNameBuffer" / Bytes(lambda this: this.ProcessNameLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3022, version=0)
class Microsoft_Windows_CodeIntegrity_3022_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3022, version=1)
class Microsoft_Windows_CodeIntegrity_3022_1(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength),
        "SecureRequired" / Int32ul,
        "RequestedSigningLevel" / Int8ul,
        "ProcessNameLength" / Int16ul,
        "ProcessNameBuffer" / Bytes(lambda this: this.ProcessNameLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3023, version=0)
class Microsoft_Windows_CodeIntegrity_3023_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3023, version=1)
class Microsoft_Windows_CodeIntegrity_3023_1(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength),
        "SecureRequired" / Int32ul,
        "RequestedSigningLevel" / Int8ul,
        "ProcessNameLength" / Int16ul,
        "ProcessNameBuffer" / Bytes(lambda this: this.ProcessNameLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3024, version=0)
class Microsoft_Windows_CodeIntegrity_3024_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3025, version=0)
class Microsoft_Windows_CodeIntegrity_3025_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3026, version=0)
class Microsoft_Windows_CodeIntegrity_3026_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3027, version=0)
class Microsoft_Windows_CodeIntegrity_3027_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3028, version=0)
class Microsoft_Windows_CodeIntegrity_3028_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3029, version=1)
class Microsoft_Windows_CodeIntegrity_3029_1(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3030, version=0)
class Microsoft_Windows_CodeIntegrity_3030_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3032, version=0)
class Microsoft_Windows_CodeIntegrity_3032_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3032, version=1)
class Microsoft_Windows_CodeIntegrity_3032_1(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength),
        "SecureRequired" / Int32ul,
        "RequestedSigningLevel" / Int8ul,
        "ProcessNameLength" / Int16ul,
        "ProcessNameBuffer" / Bytes(lambda this: this.ProcessNameLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3033, version=0)
class Microsoft_Windows_CodeIntegrity_3033_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength),
        "ProcessNameLength" / Int16ul,
        "ProcessNameBuffer" / Bytes(lambda this: this.ProcessNameLength),
        "RequestedPolicy" / Int8ul,
        "ValidatedPolicy" / Int8ul,
        "Status" / Int32ul
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3034, version=0)
class Microsoft_Windows_CodeIntegrity_3034_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength),
        "ProcessNameLength" / Int16ul,
        "ProcessNameBuffer" / Bytes(lambda this: this.ProcessNameLength),
        "RequestedPolicy" / Int8ul,
        "ValidatedPolicy" / Int8ul,
        "Status" / Int32ul
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3035, version=0)
class Microsoft_Windows_CodeIntegrity_3035_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3035, version=1)
class Microsoft_Windows_CodeIntegrity_3035_1(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength),
        "SecureRequired" / Int32ul,
        "RequestedSigningLevel" / Int8ul,
        "ProcessNameLength" / Int16ul,
        "ProcessNameBuffer" / Bytes(lambda this: this.ProcessNameLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3036, version=0)
class Microsoft_Windows_CodeIntegrity_3036_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3036, version=1)
class Microsoft_Windows_CodeIntegrity_3036_1(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength),
        "SecureRequired" / Int32ul,
        "RequestedSigningLevel" / Int8ul,
        "ProcessNameLength" / Int16ul,
        "ProcessNameBuffer" / Bytes(lambda this: this.ProcessNameLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3037, version=0)
class Microsoft_Windows_CodeIntegrity_3037_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3037, version=1)
class Microsoft_Windows_CodeIntegrity_3037_1(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength),
        "SecureRequired" / Int32ul,
        "RequestedSigningLevel" / Int8ul,
        "ProcessNameLength" / Int16ul,
        "ProcessNameBuffer" / Bytes(lambda this: this.ProcessNameLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3038, version=0)
class Microsoft_Windows_CodeIntegrity_3038_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3038, version=1)
class Microsoft_Windows_CodeIntegrity_3038_1(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength),
        "SecureRequired" / Int32ul,
        "RequestedSigningLevel" / Int8ul
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3038, version=2)
class Microsoft_Windows_CodeIntegrity_3038_2(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength),
        "SecureRequired" / Int32ul,
        "RequestedSigningLevel" / Int8ul,
        "ProcessNameLength" / Int16ul,
        "ProcessNameBuffer" / Bytes(lambda this: this.ProcessNameLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3039, version=1)
class Microsoft_Windows_CodeIntegrity_3039_1(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3040, version=0)
class Microsoft_Windows_CodeIntegrity_3040_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3041, version=2)
class Microsoft_Windows_CodeIntegrity_3041_2(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "CachedFlags" / Int32ul,
        "CacheSource" / Int8ul,
        "CachedPolicy" / Int8ul
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3042, version=0)
class Microsoft_Windows_CodeIntegrity_3042_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3043, version=1)
class Microsoft_Windows_CodeIntegrity_3043_1(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "CachedFlags" / Int32ul,
        "CacheSource" / Int8ul,
        "CachedPolicy" / Int8ul
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3050, version=0)
class Microsoft_Windows_CodeIntegrity_3050_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3051, version=0)
class Microsoft_Windows_CodeIntegrity_3051_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3052, version=0)
class Microsoft_Windows_CodeIntegrity_3052_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3054, version=0)
class Microsoft_Windows_CodeIntegrity_3054_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3055, version=0)
class Microsoft_Windows_CodeIntegrity_3055_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3057, version=0)
class Microsoft_Windows_CodeIntegrity_3057_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3058, version=0)
class Microsoft_Windows_CodeIntegrity_3058_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3059, version=0)
class Microsoft_Windows_CodeIntegrity_3059_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength),
        "CatalogNameLength" / Int16ul,
        "CatalogNameBuffer" / Bytes(lambda this: this.CatalogNameLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3060, version=0)
class Microsoft_Windows_CodeIntegrity_3060_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength),
        "CatalogNameLength" / Int16ul,
        "CatalogNameBuffer" / Bytes(lambda this: this.CatalogNameLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3061, version=0)
class Microsoft_Windows_CodeIntegrity_3061_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength),
        "CatalogNameLength" / Int16ul,
        "CatalogNameBuffer" / Bytes(lambda this: this.CatalogNameLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3062, version=0)
class Microsoft_Windows_CodeIntegrity_3062_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength),
        "CatalogNameLength" / Int16ul,
        "CatalogNameBuffer" / Bytes(lambda this: this.CatalogNameLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3063, version=0)
class Microsoft_Windows_CodeIntegrity_3063_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength),
        "ProcessNameLength" / Int16ul,
        "ProcessNameBuffer" / Bytes(lambda this: this.ProcessNameLength),
        "RequirementType" / Int8ul,
        "Status" / Int32ul
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3064, version=0)
class Microsoft_Windows_CodeIntegrity_3064_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength),
        "ProcessNameLength" / Int16ul,
        "ProcessNameBuffer" / Bytes(lambda this: this.ProcessNameLength),
        "RequirementType" / Int8ul,
        "Status" / Int32ul
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3065, version=0)
class Microsoft_Windows_CodeIntegrity_3065_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength),
        "ProcessNameLength" / Int16ul,
        "ProcessNameBuffer" / Bytes(lambda this: this.ProcessNameLength),
        "RequirementType" / Int8ul,
        "Status" / Int32ul
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3066, version=0)
class Microsoft_Windows_CodeIntegrity_3066_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength),
        "ProcessNameLength" / Int16ul,
        "ProcessNameBuffer" / Bytes(lambda this: this.ProcessNameLength),
        "RequestedPolicy" / Int8ul,
        "ValidatedPolicy" / Int8ul,
        "Status" / Int32ul
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3067, version=0)
class Microsoft_Windows_CodeIntegrity_3067_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength),
        "ProcessNameLength" / Int16ul,
        "ProcessNameBuffer" / Bytes(lambda this: this.ProcessNameLength),
        "RequestedPolicy" / Int8ul,
        "ValidatedPolicy" / Int8ul,
        "Status" / Int32ul
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3068, version=0)
class Microsoft_Windows_CodeIntegrity_3068_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength),
        "ProcessNameLength" / Int16ul,
        "ProcessNameBuffer" / Bytes(lambda this: this.ProcessNameLength),
        "RequestedPolicy" / Int8ul,
        "ValidatedPolicy" / Int8ul,
        "Status" / Int32ul
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3069, version=0)
class Microsoft_Windows_CodeIntegrity_3069_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3070, version=0)
class Microsoft_Windows_CodeIntegrity_3070_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3071, version=0)
class Microsoft_Windows_CodeIntegrity_3071_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3072, version=0)
class Microsoft_Windows_CodeIntegrity_3072_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3073, version=0)
class Microsoft_Windows_CodeIntegrity_3073_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3074, version=0)
class Microsoft_Windows_CodeIntegrity_3074_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3075, version=0)
class Microsoft_Windows_CodeIntegrity_3075_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength),
        "ProcessNameLength" / Int16ul,
        "ProcessNameBuffer" / Bytes(lambda this: this.ProcessNameLength),
        "RequestedSigningLevel" / Int8ul,
        "ValidatedSigningLevel" / Int8ul,
        "ElapsedTime" / Int64ul,
        "PolicyElapsedTime" / Int64ul,
        "PercentageTime" / Int32ul
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3076, version=0)
class Microsoft_Windows_CodeIntegrity_3076_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "ProcessNameLength" / Int16ul,
        "ProcessName" / Bytes(lambda this: this.ProcessNameLength),
        "RequestedSigningLevel" / Int8ul,
        "ValidatedSigningLevel" / Int8ul,
        "Status" / Int32ul,
        "SHA1HashSize" / Int32ul,
        "SHA1Hash" / Bytes(lambda this: this.SHA1HashSize),
        "SHA256HashSize" / Int32ul,
        "SHA256Hash" / Bytes(lambda this: this.SHA256HashSize),
        "USN" / Int64ul,
        "SISigningScenario" / Int32ul
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3076, version=1)
class Microsoft_Windows_CodeIntegrity_3076_1(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "ProcessNameLength" / Int16ul,
        "ProcessName" / Bytes(lambda this: this.ProcessNameLength),
        "RequestedSigningLevel" / Int8ul,
        "ValidatedSigningLevel" / Int8ul,
        "Status" / Int32ul,
        "SHA1HashSize" / Int32ul,
        "SHA1Hash" / Bytes(lambda this: this.SHA1HashSize),
        "SHA256HashSize" / Int32ul,
        "SHA256Hash" / Bytes(lambda this: this.SHA256HashSize),
        "USN" / Int64ul,
        "SISigningScenario" / Int32ul,
        "PolicyNameLength" / Int16ul,
        "PolicyName" / Bytes(lambda this: this.PolicyNameLength),
        "PolicyIDLength" / Int16ul,
        "PolicyID" / Bytes(lambda this: this.PolicyIDLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3076, version=2)
class Microsoft_Windows_CodeIntegrity_3076_2(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "ProcessNameLength" / Int16ul,
        "ProcessName" / Bytes(lambda this: this.ProcessNameLength),
        "RequestedSigningLevel" / Int8ul,
        "ValidatedSigningLevel" / Int8ul,
        "Status" / Int32ul,
        "SHA1HashSize" / Int32ul,
        "SHA1Hash" / Bytes(lambda this: this.SHA1HashSize),
        "SHA256HashSize" / Int32ul,
        "SHA256Hash" / Bytes(lambda this: this.SHA256HashSize),
        "USN" / Int64ul,
        "SISigningScenario" / Int32ul,
        "PolicyNameLength" / Int16ul,
        "PolicyName" / Bytes(lambda this: this.PolicyNameLength),
        "PolicyIDLength" / Int16ul,
        "PolicyID" / Bytes(lambda this: this.PolicyIDLength),
        "PolicyHashSize" / Int32ul,
        "PolicyHash" / Bytes(lambda this: this.PolicyHashSize)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3076, version=3)
class Microsoft_Windows_CodeIntegrity_3076_3(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "ProcessNameLength" / Int16ul,
        "ProcessName" / Bytes(lambda this: this.ProcessNameLength),
        "RequestedSigningLevel" / Int8ul,
        "ValidatedSigningLevel" / Int8ul,
        "Status" / Int32ul,
        "SHA1HashSize" / Int32ul,
        "SHA1Hash" / Bytes(lambda this: this.SHA1HashSize),
        "SHA256HashSize" / Int32ul,
        "SHA256Hash" / Bytes(lambda this: this.SHA256HashSize),
        "USN" / Int64ul,
        "SISigningScenario" / Int32ul,
        "PolicyNameLength" / Int16ul,
        "PolicyName" / Bytes(lambda this: this.PolicyNameLength),
        "PolicyIDLength" / Int16ul,
        "PolicyID" / Bytes(lambda this: this.PolicyIDLength),
        "PolicyHashSize" / Int32ul,
        "PolicyHash" / Bytes(lambda this: this.PolicyHashSize),
        "OriginalFileNameLength" / Int16ul,
        "OriginalFileName" / Bytes(lambda this: this.OriginalFileNameLength),
        "InternalNameLength" / Int16ul,
        "InternalName" / Bytes(lambda this: this.InternalNameLength),
        "FileDescriptionLength" / Int16ul,
        "FileDescription" / Bytes(lambda this: this.FileDescriptionLength),
        "ProductNameLength" / Int16ul,
        "ProductName" / Bytes(lambda this: this.ProductNameLength),
        "FileVersion" / CString
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3076, version=4)
class Microsoft_Windows_CodeIntegrity_3076_4(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "ProcessNameLength" / Int16ul,
        "ProcessName" / Bytes(lambda this: this.ProcessNameLength),
        "RequestedSigningLevel" / Int8ul,
        "ValidatedSigningLevel" / Int8ul,
        "Status" / Int32ul,
        "SHA1HashSize" / Int32ul,
        "SHA1Hash" / Bytes(lambda this: this.SHA1HashSize),
        "SHA256HashSize" / Int32ul,
        "SHA256Hash" / Bytes(lambda this: this.SHA256HashSize),
        "USN" / Int64ul,
        "SISigningScenario" / Int32ul,
        "PolicyNameLength" / Int16ul,
        "PolicyName" / Bytes(lambda this: this.PolicyNameLength),
        "PolicyIDLength" / Int16ul,
        "PolicyID" / Bytes(lambda this: this.PolicyIDLength),
        "PolicyHashSize" / Int32ul,
        "PolicyHash" / Bytes(lambda this: this.PolicyHashSize),
        "OriginalFileNameLength" / Int16ul,
        "OriginalFileName" / Bytes(lambda this: this.OriginalFileNameLength),
        "InternalNameLength" / Int16ul,
        "InternalName" / Bytes(lambda this: this.InternalNameLength),
        "FileDescriptionLength" / Int16ul,
        "FileDescription" / Bytes(lambda this: this.FileDescriptionLength),
        "ProductNameLength" / Int16ul,
        "ProductName" / Bytes(lambda this: this.ProductNameLength),
        "FileVersion" / CString,
        "PolicyGUID" / Guid
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3076, version=5)
class Microsoft_Windows_CodeIntegrity_3076_5(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "ProcessNameLength" / Int16ul,
        "ProcessName" / Bytes(lambda this: this.ProcessNameLength),
        "RequestedSigningLevel" / Int8ul,
        "ValidatedSigningLevel" / Int8ul,
        "Status" / Int32ul,
        "SHA1HashSize" / Int32ul,
        "SHA1Hash" / Bytes(lambda this: this.SHA1HashSize),
        "SHA256HashSize" / Int32ul,
        "SHA256Hash" / Bytes(lambda this: this.SHA256HashSize),
        "SHA1FlatHashSize" / Int32ul,
        "SHA1FlatHash" / Bytes(lambda this: this.SHA1FlatHashSize),
        "SHA256FlatHashSize" / Int32ul,
        "SHA256FlatHash" / Bytes(lambda this: this.SHA256FlatHashSize),
        "USN" / Int64ul,
        "SISigningScenario" / Int32ul,
        "PolicyNameLength" / Int16ul,
        "PolicyName" / Bytes(lambda this: this.PolicyNameLength),
        "PolicyIDLength" / Int16ul,
        "PolicyID" / Bytes(lambda this: this.PolicyIDLength),
        "PolicyHashSize" / Int32ul,
        "PolicyHash" / Bytes(lambda this: this.PolicyHashSize),
        "OriginalFileNameLength" / Int16ul,
        "OriginalFileName" / Bytes(lambda this: this.OriginalFileNameLength),
        "InternalNameLength" / Int16ul,
        "InternalName" / Bytes(lambda this: this.InternalNameLength),
        "FileDescriptionLength" / Int16ul,
        "FileDescription" / Bytes(lambda this: this.FileDescriptionLength),
        "ProductNameLength" / Int16ul,
        "ProductName" / Bytes(lambda this: this.ProductNameLength),
        "FileVersion" / CString,
        "PolicyGUID" / Guid,
        "UserWriteable" / Int8ul,
        "PackageFamilyNameLength" / Int16ul,
        "PackageFamilyName" / Bytes(lambda this: this.PackageFamilyNameLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3077, version=0)
class Microsoft_Windows_CodeIntegrity_3077_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "ProcessNameLength" / Int16ul,
        "ProcessName" / Bytes(lambda this: this.ProcessNameLength),
        "RequestedSigningLevel" / Int8ul,
        "ValidatedSigningLevel" / Int8ul,
        "Status" / Int32ul,
        "SHA1HashSize" / Int32ul,
        "SHA1Hash" / Bytes(lambda this: this.SHA1HashSize),
        "SHA256HashSize" / Int32ul,
        "SHA256Hash" / Bytes(lambda this: this.SHA256HashSize),
        "USN" / Int64ul,
        "SISigningScenario" / Int32ul
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3077, version=1)
class Microsoft_Windows_CodeIntegrity_3077_1(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "ProcessNameLength" / Int16ul,
        "ProcessName" / Bytes(lambda this: this.ProcessNameLength),
        "RequestedSigningLevel" / Int8ul,
        "ValidatedSigningLevel" / Int8ul,
        "Status" / Int32ul,
        "SHA1HashSize" / Int32ul,
        "SHA1Hash" / Bytes(lambda this: this.SHA1HashSize),
        "SHA256HashSize" / Int32ul,
        "SHA256Hash" / Bytes(lambda this: this.SHA256HashSize),
        "USN" / Int64ul,
        "SISigningScenario" / Int32ul,
        "PolicyNameLength" / Int16ul,
        "PolicyName" / Bytes(lambda this: this.PolicyNameLength),
        "PolicyIDLength" / Int16ul,
        "PolicyID" / Bytes(lambda this: this.PolicyIDLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3077, version=2)
class Microsoft_Windows_CodeIntegrity_3077_2(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "ProcessNameLength" / Int16ul,
        "ProcessName" / Bytes(lambda this: this.ProcessNameLength),
        "RequestedSigningLevel" / Int8ul,
        "ValidatedSigningLevel" / Int8ul,
        "Status" / Int32ul,
        "SHA1HashSize" / Int32ul,
        "SHA1Hash" / Bytes(lambda this: this.SHA1HashSize),
        "SHA256HashSize" / Int32ul,
        "SHA256Hash" / Bytes(lambda this: this.SHA256HashSize),
        "USN" / Int64ul,
        "SISigningScenario" / Int32ul,
        "PolicyNameLength" / Int16ul,
        "PolicyName" / Bytes(lambda this: this.PolicyNameLength),
        "PolicyIDLength" / Int16ul,
        "PolicyID" / Bytes(lambda this: this.PolicyIDLength),
        "PolicyHashSize" / Int32ul,
        "PolicyHash" / Bytes(lambda this: this.PolicyHashSize)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3077, version=3)
class Microsoft_Windows_CodeIntegrity_3077_3(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "ProcessNameLength" / Int16ul,
        "ProcessName" / Bytes(lambda this: this.ProcessNameLength),
        "RequestedSigningLevel" / Int8ul,
        "ValidatedSigningLevel" / Int8ul,
        "Status" / Int32ul,
        "SHA1HashSize" / Int32ul,
        "SHA1Hash" / Bytes(lambda this: this.SHA1HashSize),
        "SHA256HashSize" / Int32ul,
        "SHA256Hash" / Bytes(lambda this: this.SHA256HashSize),
        "USN" / Int64ul,
        "SISigningScenario" / Int32ul,
        "PolicyNameLength" / Int16ul,
        "PolicyName" / Bytes(lambda this: this.PolicyNameLength),
        "PolicyIDLength" / Int16ul,
        "PolicyID" / Bytes(lambda this: this.PolicyIDLength),
        "PolicyHashSize" / Int32ul,
        "PolicyHash" / Bytes(lambda this: this.PolicyHashSize),
        "OriginalFileNameLength" / Int16ul,
        "OriginalFileName" / Bytes(lambda this: this.OriginalFileNameLength),
        "InternalNameLength" / Int16ul,
        "InternalName" / Bytes(lambda this: this.InternalNameLength),
        "FileDescriptionLength" / Int16ul,
        "FileDescription" / Bytes(lambda this: this.FileDescriptionLength),
        "ProductNameLength" / Int16ul,
        "ProductName" / Bytes(lambda this: this.ProductNameLength),
        "FileVersion" / CString
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3077, version=4)
class Microsoft_Windows_CodeIntegrity_3077_4(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "ProcessNameLength" / Int16ul,
        "ProcessName" / Bytes(lambda this: this.ProcessNameLength),
        "RequestedSigningLevel" / Int8ul,
        "ValidatedSigningLevel" / Int8ul,
        "Status" / Int32ul,
        "SHA1HashSize" / Int32ul,
        "SHA1Hash" / Bytes(lambda this: this.SHA1HashSize),
        "SHA256HashSize" / Int32ul,
        "SHA256Hash" / Bytes(lambda this: this.SHA256HashSize),
        "USN" / Int64ul,
        "SISigningScenario" / Int32ul,
        "PolicyNameLength" / Int16ul,
        "PolicyName" / Bytes(lambda this: this.PolicyNameLength),
        "PolicyIDLength" / Int16ul,
        "PolicyID" / Bytes(lambda this: this.PolicyIDLength),
        "PolicyHashSize" / Int32ul,
        "PolicyHash" / Bytes(lambda this: this.PolicyHashSize),
        "OriginalFileNameLength" / Int16ul,
        "OriginalFileName" / Bytes(lambda this: this.OriginalFileNameLength),
        "InternalNameLength" / Int16ul,
        "InternalName" / Bytes(lambda this: this.InternalNameLength),
        "FileDescriptionLength" / Int16ul,
        "FileDescription" / Bytes(lambda this: this.FileDescriptionLength),
        "ProductNameLength" / Int16ul,
        "ProductName" / Bytes(lambda this: this.ProductNameLength),
        "FileVersion" / CString,
        "PolicyGUID" / Guid
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3077, version=5)
class Microsoft_Windows_CodeIntegrity_3077_5(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "ProcessNameLength" / Int16ul,
        "ProcessName" / Bytes(lambda this: this.ProcessNameLength),
        "RequestedSigningLevel" / Int8ul,
        "ValidatedSigningLevel" / Int8ul,
        "Status" / Int32ul,
        "SHA1HashSize" / Int32ul,
        "SHA1Hash" / Bytes(lambda this: this.SHA1HashSize),
        "SHA256HashSize" / Int32ul,
        "SHA256Hash" / Bytes(lambda this: this.SHA256HashSize),
        "SHA1FlatHashSize" / Int32ul,
        "SHA1FlatHash" / Bytes(lambda this: this.SHA1FlatHashSize),
        "SHA256FlatHashSize" / Int32ul,
        "SHA256FlatHash" / Bytes(lambda this: this.SHA256FlatHashSize),
        "USN" / Int64ul,
        "SISigningScenario" / Int32ul,
        "PolicyNameLength" / Int16ul,
        "PolicyName" / Bytes(lambda this: this.PolicyNameLength),
        "PolicyIDLength" / Int16ul,
        "PolicyID" / Bytes(lambda this: this.PolicyIDLength),
        "PolicyHashSize" / Int32ul,
        "PolicyHash" / Bytes(lambda this: this.PolicyHashSize),
        "OriginalFileNameLength" / Int16ul,
        "OriginalFileName" / Bytes(lambda this: this.OriginalFileNameLength),
        "InternalNameLength" / Int16ul,
        "InternalName" / Bytes(lambda this: this.InternalNameLength),
        "FileDescriptionLength" / Int16ul,
        "FileDescription" / Bytes(lambda this: this.FileDescriptionLength),
        "ProductNameLength" / Int16ul,
        "ProductName" / Bytes(lambda this: this.ProductNameLength),
        "FileVersion" / CString,
        "PolicyGUID" / Guid,
        "UserWriteable" / Int8ul,
        "PackageFamilyNameLength" / Int16ul,
        "PackageFamilyName" / Bytes(lambda this: this.PackageFamilyNameLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3078, version=0)
class Microsoft_Windows_CodeIntegrity_3078_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "ProcessNameLength" / Int16ul,
        "ProcessName" / Bytes(lambda this: this.ProcessNameLength),
        "RequestedSigningLevel" / Int8ul,
        "ValidatedSigningLevel" / Int8ul,
        "Status" / Int32ul,
        "SHA1HashSize" / Int32ul,
        "SHA1Hash" / Bytes(lambda this: this.SHA1HashSize),
        "SHA256HashSize" / Int32ul,
        "SHA256Hash" / Bytes(lambda this: this.SHA256HashSize),
        "USN" / Int64ul,
        "SISigningScenario" / Int32ul
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3078, version=1)
class Microsoft_Windows_CodeIntegrity_3078_1(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "ProcessNameLength" / Int16ul,
        "ProcessName" / Bytes(lambda this: this.ProcessNameLength),
        "RequestedSigningLevel" / Int8ul,
        "ValidatedSigningLevel" / Int8ul,
        "Status" / Int32ul,
        "SHA1HashSize" / Int32ul,
        "SHA1Hash" / Bytes(lambda this: this.SHA1HashSize),
        "SHA256HashSize" / Int32ul,
        "SHA256Hash" / Bytes(lambda this: this.SHA256HashSize),
        "USN" / Int64ul,
        "SISigningScenario" / Int32ul,
        "PolicyNameLength" / Int16ul,
        "PolicyName" / Bytes(lambda this: this.PolicyNameLength),
        "PolicyIDLength" / Int16ul,
        "PolicyID" / Bytes(lambda this: this.PolicyIDLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3078, version=2)
class Microsoft_Windows_CodeIntegrity_3078_2(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "ProcessNameLength" / Int16ul,
        "ProcessName" / Bytes(lambda this: this.ProcessNameLength),
        "RequestedSigningLevel" / Int8ul,
        "ValidatedSigningLevel" / Int8ul,
        "Status" / Int32ul,
        "SHA1HashSize" / Int32ul,
        "SHA1Hash" / Bytes(lambda this: this.SHA1HashSize),
        "SHA256HashSize" / Int32ul,
        "SHA256Hash" / Bytes(lambda this: this.SHA256HashSize),
        "USN" / Int64ul,
        "SISigningScenario" / Int32ul,
        "PolicyNameLength" / Int16ul,
        "PolicyName" / Bytes(lambda this: this.PolicyNameLength),
        "PolicyIDLength" / Int16ul,
        "PolicyID" / Bytes(lambda this: this.PolicyIDLength),
        "PolicyHashSize" / Int32ul,
        "PolicyHash" / Bytes(lambda this: this.PolicyHashSize)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3078, version=3)
class Microsoft_Windows_CodeIntegrity_3078_3(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "ProcessNameLength" / Int16ul,
        "ProcessName" / Bytes(lambda this: this.ProcessNameLength),
        "RequestedSigningLevel" / Int8ul,
        "ValidatedSigningLevel" / Int8ul,
        "Status" / Int32ul,
        "SHA1HashSize" / Int32ul,
        "SHA1Hash" / Bytes(lambda this: this.SHA1HashSize),
        "SHA256HashSize" / Int32ul,
        "SHA256Hash" / Bytes(lambda this: this.SHA256HashSize),
        "USN" / Int64ul,
        "SISigningScenario" / Int32ul,
        "PolicyNameLength" / Int16ul,
        "PolicyName" / Bytes(lambda this: this.PolicyNameLength),
        "PolicyIDLength" / Int16ul,
        "PolicyID" / Bytes(lambda this: this.PolicyIDLength),
        "PolicyHashSize" / Int32ul,
        "PolicyHash" / Bytes(lambda this: this.PolicyHashSize),
        "OriginalFileNameLength" / Int16ul,
        "OriginalFileName" / Bytes(lambda this: this.OriginalFileNameLength),
        "InternalNameLength" / Int16ul,
        "InternalName" / Bytes(lambda this: this.InternalNameLength),
        "FileDescriptionLength" / Int16ul,
        "FileDescription" / Bytes(lambda this: this.FileDescriptionLength),
        "ProductNameLength" / Int16ul,
        "ProductName" / Bytes(lambda this: this.ProductNameLength),
        "FileVersion" / CString
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3079, version=0)
class Microsoft_Windows_CodeIntegrity_3079_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "ProcessNameLength" / Int16ul,
        "ProcessName" / Bytes(lambda this: this.ProcessNameLength),
        "RequestedSigningLevel" / Int8ul,
        "ValidatedSigningLevel" / Int8ul,
        "Status" / Int32ul,
        "SHA1HashSize" / Int32ul,
        "SHA1Hash" / Bytes(lambda this: this.SHA1HashSize),
        "SHA256HashSize" / Int32ul,
        "SHA256Hash" / Bytes(lambda this: this.SHA256HashSize),
        "USN" / Int64ul,
        "SISigningScenario" / Int32ul
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3079, version=1)
class Microsoft_Windows_CodeIntegrity_3079_1(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "ProcessNameLength" / Int16ul,
        "ProcessName" / Bytes(lambda this: this.ProcessNameLength),
        "RequestedSigningLevel" / Int8ul,
        "ValidatedSigningLevel" / Int8ul,
        "Status" / Int32ul,
        "SHA1HashSize" / Int32ul,
        "SHA1Hash" / Bytes(lambda this: this.SHA1HashSize),
        "SHA256HashSize" / Int32ul,
        "SHA256Hash" / Bytes(lambda this: this.SHA256HashSize),
        "USN" / Int64ul,
        "SISigningScenario" / Int32ul,
        "PolicyNameLength" / Int16ul,
        "PolicyName" / Bytes(lambda this: this.PolicyNameLength),
        "PolicyIDLength" / Int16ul,
        "PolicyID" / Bytes(lambda this: this.PolicyIDLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3079, version=2)
class Microsoft_Windows_CodeIntegrity_3079_2(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "ProcessNameLength" / Int16ul,
        "ProcessName" / Bytes(lambda this: this.ProcessNameLength),
        "RequestedSigningLevel" / Int8ul,
        "ValidatedSigningLevel" / Int8ul,
        "Status" / Int32ul,
        "SHA1HashSize" / Int32ul,
        "SHA1Hash" / Bytes(lambda this: this.SHA1HashSize),
        "SHA256HashSize" / Int32ul,
        "SHA256Hash" / Bytes(lambda this: this.SHA256HashSize),
        "USN" / Int64ul,
        "SISigningScenario" / Int32ul,
        "PolicyNameLength" / Int16ul,
        "PolicyName" / Bytes(lambda this: this.PolicyNameLength),
        "PolicyIDLength" / Int16ul,
        "PolicyID" / Bytes(lambda this: this.PolicyIDLength),
        "PolicyHashSize" / Int32ul,
        "PolicyHash" / Bytes(lambda this: this.PolicyHashSize)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3079, version=3)
class Microsoft_Windows_CodeIntegrity_3079_3(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "ProcessNameLength" / Int16ul,
        "ProcessName" / Bytes(lambda this: this.ProcessNameLength),
        "RequestedSigningLevel" / Int8ul,
        "ValidatedSigningLevel" / Int8ul,
        "Status" / Int32ul,
        "SHA1HashSize" / Int32ul,
        "SHA1Hash" / Bytes(lambda this: this.SHA1HashSize),
        "SHA256HashSize" / Int32ul,
        "SHA256Hash" / Bytes(lambda this: this.SHA256HashSize),
        "USN" / Int64ul,
        "SISigningScenario" / Int32ul,
        "PolicyNameLength" / Int16ul,
        "PolicyName" / Bytes(lambda this: this.PolicyNameLength),
        "PolicyIDLength" / Int16ul,
        "PolicyID" / Bytes(lambda this: this.PolicyIDLength),
        "PolicyHashSize" / Int32ul,
        "PolicyHash" / Bytes(lambda this: this.PolicyHashSize),
        "OriginalFileNameLength" / Int16ul,
        "OriginalFileName" / Bytes(lambda this: this.OriginalFileNameLength),
        "InternalNameLength" / Int16ul,
        "InternalName" / Bytes(lambda this: this.InternalNameLength),
        "FileDescriptionLength" / Int16ul,
        "FileDescription" / Bytes(lambda this: this.FileDescriptionLength),
        "ProductNameLength" / Int16ul,
        "ProductName" / Bytes(lambda this: this.ProductNameLength),
        "FileVersion" / CString
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3080, version=0)
class Microsoft_Windows_CodeIntegrity_3080_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "ProcessNameLength" / Int16ul,
        "ProcessName" / Bytes(lambda this: this.ProcessNameLength),
        "RequestedSigningLevel" / Int8ul,
        "ValidatedSigningLevel" / Int8ul,
        "Status" / Int32ul,
        "SHA1HashSize" / Int32ul,
        "SHA1Hash" / Bytes(lambda this: this.SHA1HashSize),
        "SHA256HashSize" / Int32ul,
        "SHA256Hash" / Bytes(lambda this: this.SHA256HashSize),
        "USN" / Int64ul,
        "SISigningScenario" / Int32ul
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3080, version=1)
class Microsoft_Windows_CodeIntegrity_3080_1(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "ProcessNameLength" / Int16ul,
        "ProcessName" / Bytes(lambda this: this.ProcessNameLength),
        "RequestedSigningLevel" / Int8ul,
        "ValidatedSigningLevel" / Int8ul,
        "Status" / Int32ul,
        "SHA1HashSize" / Int32ul,
        "SHA1Hash" / Bytes(lambda this: this.SHA1HashSize),
        "SHA256HashSize" / Int32ul,
        "SHA256Hash" / Bytes(lambda this: this.SHA256HashSize),
        "USN" / Int64ul,
        "SISigningScenario" / Int32ul,
        "PolicyNameLength" / Int16ul,
        "PolicyName" / Bytes(lambda this: this.PolicyNameLength),
        "PolicyIDLength" / Int16ul,
        "PolicyID" / Bytes(lambda this: this.PolicyIDLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3080, version=2)
class Microsoft_Windows_CodeIntegrity_3080_2(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "ProcessNameLength" / Int16ul,
        "ProcessName" / Bytes(lambda this: this.ProcessNameLength),
        "RequestedSigningLevel" / Int8ul,
        "ValidatedSigningLevel" / Int8ul,
        "Status" / Int32ul,
        "SHA1HashSize" / Int32ul,
        "SHA1Hash" / Bytes(lambda this: this.SHA1HashSize),
        "SHA256HashSize" / Int32ul,
        "SHA256Hash" / Bytes(lambda this: this.SHA256HashSize),
        "USN" / Int64ul,
        "SISigningScenario" / Int32ul,
        "PolicyNameLength" / Int16ul,
        "PolicyName" / Bytes(lambda this: this.PolicyNameLength),
        "PolicyIDLength" / Int16ul,
        "PolicyID" / Bytes(lambda this: this.PolicyIDLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3080, version=3)
class Microsoft_Windows_CodeIntegrity_3080_3(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "ProcessNameLength" / Int16ul,
        "ProcessName" / Bytes(lambda this: this.ProcessNameLength),
        "RequestedSigningLevel" / Int8ul,
        "ValidatedSigningLevel" / Int8ul,
        "Status" / Int32ul,
        "SHA1HashSize" / Int32ul,
        "SHA1Hash" / Bytes(lambda this: this.SHA1HashSize),
        "SHA256HashSize" / Int32ul,
        "SHA256Hash" / Bytes(lambda this: this.SHA256HashSize),
        "USN" / Int64ul,
        "SISigningScenario" / Int32ul,
        "PolicyNameLength" / Int16ul,
        "PolicyName" / Bytes(lambda this: this.PolicyNameLength),
        "PolicyIDLength" / Int16ul,
        "PolicyID" / Bytes(lambda this: this.PolicyIDLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3080, version=4)
class Microsoft_Windows_CodeIntegrity_3080_4(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "ProcessNameLength" / Int16ul,
        "ProcessName" / Bytes(lambda this: this.ProcessNameLength),
        "RequestedSigningLevel" / Int8ul,
        "ValidatedSigningLevel" / Int8ul,
        "Status" / Int32ul,
        "SHA1HashSize" / Int32ul,
        "SHA1Hash" / Bytes(lambda this: this.SHA1HashSize),
        "SHA256HashSize" / Int32ul,
        "SHA256Hash" / Bytes(lambda this: this.SHA256HashSize),
        "USN" / Int64ul,
        "SISigningScenario" / Int32ul,
        "PolicyNameLength" / Int16ul,
        "PolicyName" / Bytes(lambda this: this.PolicyNameLength),
        "PolicyIDLength" / Int16ul,
        "PolicyID" / Bytes(lambda this: this.PolicyIDLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3080, version=5)
class Microsoft_Windows_CodeIntegrity_3080_5(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "ProcessNameLength" / Int16ul,
        "ProcessName" / Bytes(lambda this: this.ProcessNameLength),
        "RequestedSigningLevel" / Int8ul,
        "ValidatedSigningLevel" / Int8ul,
        "Status" / Int32ul,
        "SHA1HashSize" / Int32ul,
        "SHA1Hash" / Bytes(lambda this: this.SHA1HashSize),
        "SHA256HashSize" / Int32ul,
        "SHA256Hash" / Bytes(lambda this: this.SHA256HashSize),
        "USN" / Int64ul,
        "SISigningScenario" / Int32ul,
        "PolicyNameLength" / Int16ul,
        "PolicyName" / Bytes(lambda this: this.PolicyNameLength),
        "PolicyIDLength" / Int16ul,
        "PolicyID" / Bytes(lambda this: this.PolicyIDLength),
        "PolicyHashSize" / Int32ul,
        "PolicyHash" / Bytes(lambda this: this.PolicyHashSize)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3080, version=6)
class Microsoft_Windows_CodeIntegrity_3080_6(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "ProcessNameLength" / Int16ul,
        "ProcessName" / Bytes(lambda this: this.ProcessNameLength),
        "RequestedSigningLevel" / Int8ul,
        "ValidatedSigningLevel" / Int8ul,
        "Status" / Int32ul,
        "SHA1HashSize" / Int32ul,
        "SHA1Hash" / Bytes(lambda this: this.SHA1HashSize),
        "SHA256HashSize" / Int32ul,
        "SHA256Hash" / Bytes(lambda this: this.SHA256HashSize),
        "USN" / Int64ul,
        "SISigningScenario" / Int32ul,
        "PolicyNameLength" / Int16ul,
        "PolicyName" / Bytes(lambda this: this.PolicyNameLength),
        "PolicyIDLength" / Int16ul,
        "PolicyID" / Bytes(lambda this: this.PolicyIDLength),
        "PolicyHashSize" / Int32ul,
        "PolicyHash" / Bytes(lambda this: this.PolicyHashSize)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3080, version=7)
class Microsoft_Windows_CodeIntegrity_3080_7(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "ProcessNameLength" / Int16ul,
        "ProcessName" / Bytes(lambda this: this.ProcessNameLength),
        "RequestedSigningLevel" / Int8ul,
        "ValidatedSigningLevel" / Int8ul,
        "Status" / Int32ul,
        "SHA1HashSize" / Int32ul,
        "SHA1Hash" / Bytes(lambda this: this.SHA1HashSize),
        "SHA256HashSize" / Int32ul,
        "SHA256Hash" / Bytes(lambda this: this.SHA256HashSize),
        "USN" / Int64ul,
        "SISigningScenario" / Int32ul,
        "PolicyNameLength" / Int16ul,
        "PolicyName" / Bytes(lambda this: this.PolicyNameLength),
        "PolicyIDLength" / Int16ul,
        "PolicyID" / Bytes(lambda this: this.PolicyIDLength),
        "PolicyHashSize" / Int32ul,
        "PolicyHash" / Bytes(lambda this: this.PolicyHashSize)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3080, version=8)
class Microsoft_Windows_CodeIntegrity_3080_8(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "ProcessNameLength" / Int16ul,
        "ProcessName" / Bytes(lambda this: this.ProcessNameLength),
        "RequestedSigningLevel" / Int8ul,
        "ValidatedSigningLevel" / Int8ul,
        "Status" / Int32ul,
        "SHA1HashSize" / Int32ul,
        "SHA1Hash" / Bytes(lambda this: this.SHA1HashSize),
        "SHA256HashSize" / Int32ul,
        "SHA256Hash" / Bytes(lambda this: this.SHA256HashSize),
        "USN" / Int64ul,
        "SISigningScenario" / Int32ul,
        "PolicyNameLength" / Int16ul,
        "PolicyName" / Bytes(lambda this: this.PolicyNameLength),
        "PolicyIDLength" / Int16ul,
        "PolicyID" / Bytes(lambda this: this.PolicyIDLength),
        "PolicyHashSize" / Int32ul,
        "PolicyHash" / Bytes(lambda this: this.PolicyHashSize)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3080, version=9)
class Microsoft_Windows_CodeIntegrity_3080_9(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "ProcessNameLength" / Int16ul,
        "ProcessName" / Bytes(lambda this: this.ProcessNameLength),
        "RequestedSigningLevel" / Int8ul,
        "ValidatedSigningLevel" / Int8ul,
        "Status" / Int32ul,
        "SHA1HashSize" / Int32ul,
        "SHA1Hash" / Bytes(lambda this: this.SHA1HashSize),
        "SHA256HashSize" / Int32ul,
        "SHA256Hash" / Bytes(lambda this: this.SHA256HashSize),
        "USN" / Int64ul,
        "SISigningScenario" / Int32ul,
        "PolicyNameLength" / Int16ul,
        "PolicyName" / Bytes(lambda this: this.PolicyNameLength),
        "PolicyIDLength" / Int16ul,
        "PolicyID" / Bytes(lambda this: this.PolicyIDLength),
        "PolicyHashSize" / Int32ul,
        "PolicyHash" / Bytes(lambda this: this.PolicyHashSize),
        "OriginalFileNameLength" / Int16ul,
        "OriginalFileName" / Bytes(lambda this: this.OriginalFileNameLength),
        "InternalNameLength" / Int16ul,
        "InternalName" / Bytes(lambda this: this.InternalNameLength),
        "FileDescriptionLength" / Int16ul,
        "FileDescription" / Bytes(lambda this: this.FileDescriptionLength),
        "ProductNameLength" / Int16ul,
        "ProductName" / Bytes(lambda this: this.ProductNameLength),
        "FileVersion" / CString
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3080, version=10)
class Microsoft_Windows_CodeIntegrity_3080_10(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "ProcessNameLength" / Int16ul,
        "ProcessName" / Bytes(lambda this: this.ProcessNameLength),
        "RequestedSigningLevel" / Int8ul,
        "ValidatedSigningLevel" / Int8ul,
        "Status" / Int32ul,
        "SHA1HashSize" / Int32ul,
        "SHA1Hash" / Bytes(lambda this: this.SHA1HashSize),
        "SHA256HashSize" / Int32ul,
        "SHA256Hash" / Bytes(lambda this: this.SHA256HashSize),
        "USN" / Int64ul,
        "SISigningScenario" / Int32ul,
        "PolicyNameLength" / Int16ul,
        "PolicyName" / Bytes(lambda this: this.PolicyNameLength),
        "PolicyIDLength" / Int16ul,
        "PolicyID" / Bytes(lambda this: this.PolicyIDLength),
        "PolicyHashSize" / Int32ul,
        "PolicyHash" / Bytes(lambda this: this.PolicyHashSize),
        "OriginalFileNameLength" / Int16ul,
        "OriginalFileName" / Bytes(lambda this: this.OriginalFileNameLength),
        "InternalNameLength" / Int16ul,
        "InternalName" / Bytes(lambda this: this.InternalNameLength),
        "FileDescriptionLength" / Int16ul,
        "FileDescription" / Bytes(lambda this: this.FileDescriptionLength),
        "ProductNameLength" / Int16ul,
        "ProductName" / Bytes(lambda this: this.ProductNameLength),
        "FileVersion" / CString
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3080, version=11)
class Microsoft_Windows_CodeIntegrity_3080_11(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "ProcessNameLength" / Int16ul,
        "ProcessName" / Bytes(lambda this: this.ProcessNameLength),
        "RequestedSigningLevel" / Int8ul,
        "ValidatedSigningLevel" / Int8ul,
        "Status" / Int32ul,
        "SHA1HashSize" / Int32ul,
        "SHA1Hash" / Bytes(lambda this: this.SHA1HashSize),
        "SHA256HashSize" / Int32ul,
        "SHA256Hash" / Bytes(lambda this: this.SHA256HashSize),
        "USN" / Int64ul,
        "SISigningScenario" / Int32ul,
        "PolicyNameLength" / Int16ul,
        "PolicyName" / Bytes(lambda this: this.PolicyNameLength),
        "PolicyIDLength" / Int16ul,
        "PolicyID" / Bytes(lambda this: this.PolicyIDLength),
        "PolicyHashSize" / Int32ul,
        "PolicyHash" / Bytes(lambda this: this.PolicyHashSize),
        "OriginalFileNameLength" / Int16ul,
        "OriginalFileName" / Bytes(lambda this: this.OriginalFileNameLength),
        "InternalNameLength" / Int16ul,
        "InternalName" / Bytes(lambda this: this.InternalNameLength),
        "FileDescriptionLength" / Int16ul,
        "FileDescription" / Bytes(lambda this: this.FileDescriptionLength),
        "ProductNameLength" / Int16ul,
        "ProductName" / Bytes(lambda this: this.ProductNameLength),
        "FileVersion" / CString
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3080, version=12)
class Microsoft_Windows_CodeIntegrity_3080_12(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "ProcessNameLength" / Int16ul,
        "ProcessName" / Bytes(lambda this: this.ProcessNameLength),
        "RequestedSigningLevel" / Int8ul,
        "ValidatedSigningLevel" / Int8ul,
        "Status" / Int32ul,
        "SHA1HashSize" / Int32ul,
        "SHA1Hash" / Bytes(lambda this: this.SHA1HashSize),
        "SHA256HashSize" / Int32ul,
        "SHA256Hash" / Bytes(lambda this: this.SHA256HashSize),
        "USN" / Int64ul,
        "SISigningScenario" / Int32ul,
        "PolicyNameLength" / Int16ul,
        "PolicyName" / Bytes(lambda this: this.PolicyNameLength),
        "PolicyIDLength" / Int16ul,
        "PolicyID" / Bytes(lambda this: this.PolicyIDLength),
        "PolicyHashSize" / Int32ul,
        "PolicyHash" / Bytes(lambda this: this.PolicyHashSize),
        "OriginalFileNameLength" / Int16ul,
        "OriginalFileName" / Bytes(lambda this: this.OriginalFileNameLength),
        "InternalNameLength" / Int16ul,
        "InternalName" / Bytes(lambda this: this.InternalNameLength),
        "FileDescriptionLength" / Int16ul,
        "FileDescription" / Bytes(lambda this: this.FileDescriptionLength),
        "ProductNameLength" / Int16ul,
        "ProductName" / Bytes(lambda this: this.ProductNameLength),
        "FileVersion" / CString
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3081, version=0)
class Microsoft_Windows_CodeIntegrity_3081_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "ProcessNameLength" / Int16ul,
        "ProcessName" / Bytes(lambda this: this.ProcessNameLength),
        "RequestedSigningLevel" / Int8ul,
        "ValidatedSigningLevel" / Int8ul,
        "Status" / Int32ul,
        "SHA1HashSize" / Int32ul,
        "SHA1Hash" / Bytes(lambda this: this.SHA1HashSize),
        "SHA256HashSize" / Int32ul,
        "SHA256Hash" / Bytes(lambda this: this.SHA256HashSize),
        "USN" / Int64ul,
        "SISigningScenario" / Int32ul
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3081, version=1)
class Microsoft_Windows_CodeIntegrity_3081_1(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "ProcessNameLength" / Int16ul,
        "ProcessName" / Bytes(lambda this: this.ProcessNameLength),
        "RequestedSigningLevel" / Int8ul,
        "ValidatedSigningLevel" / Int8ul,
        "Status" / Int32ul,
        "SHA1HashSize" / Int32ul,
        "SHA1Hash" / Bytes(lambda this: this.SHA1HashSize),
        "SHA256HashSize" / Int32ul,
        "SHA256Hash" / Bytes(lambda this: this.SHA256HashSize),
        "USN" / Int64ul,
        "SISigningScenario" / Int32ul,
        "PolicyNameLength" / Int16ul,
        "PolicyName" / Bytes(lambda this: this.PolicyNameLength),
        "PolicyIDLength" / Int16ul,
        "PolicyID" / Bytes(lambda this: this.PolicyIDLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3081, version=2)
class Microsoft_Windows_CodeIntegrity_3081_2(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "ProcessNameLength" / Int16ul,
        "ProcessName" / Bytes(lambda this: this.ProcessNameLength),
        "RequestedSigningLevel" / Int8ul,
        "ValidatedSigningLevel" / Int8ul,
        "Status" / Int32ul,
        "SHA1HashSize" / Int32ul,
        "SHA1Hash" / Bytes(lambda this: this.SHA1HashSize),
        "SHA256HashSize" / Int32ul,
        "SHA256Hash" / Bytes(lambda this: this.SHA256HashSize),
        "USN" / Int64ul,
        "SISigningScenario" / Int32ul,
        "PolicyNameLength" / Int16ul,
        "PolicyName" / Bytes(lambda this: this.PolicyNameLength),
        "PolicyIDLength" / Int16ul,
        "PolicyID" / Bytes(lambda this: this.PolicyIDLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3081, version=3)
class Microsoft_Windows_CodeIntegrity_3081_3(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "ProcessNameLength" / Int16ul,
        "ProcessName" / Bytes(lambda this: this.ProcessNameLength),
        "RequestedSigningLevel" / Int8ul,
        "ValidatedSigningLevel" / Int8ul,
        "Status" / Int32ul,
        "SHA1HashSize" / Int32ul,
        "SHA1Hash" / Bytes(lambda this: this.SHA1HashSize),
        "SHA256HashSize" / Int32ul,
        "SHA256Hash" / Bytes(lambda this: this.SHA256HashSize),
        "USN" / Int64ul,
        "SISigningScenario" / Int32ul,
        "PolicyNameLength" / Int16ul,
        "PolicyName" / Bytes(lambda this: this.PolicyNameLength),
        "PolicyIDLength" / Int16ul,
        "PolicyID" / Bytes(lambda this: this.PolicyIDLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3081, version=4)
class Microsoft_Windows_CodeIntegrity_3081_4(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "ProcessNameLength" / Int16ul,
        "ProcessName" / Bytes(lambda this: this.ProcessNameLength),
        "RequestedSigningLevel" / Int8ul,
        "ValidatedSigningLevel" / Int8ul,
        "Status" / Int32ul,
        "SHA1HashSize" / Int32ul,
        "SHA1Hash" / Bytes(lambda this: this.SHA1HashSize),
        "SHA256HashSize" / Int32ul,
        "SHA256Hash" / Bytes(lambda this: this.SHA256HashSize),
        "USN" / Int64ul,
        "SISigningScenario" / Int32ul,
        "PolicyNameLength" / Int16ul,
        "PolicyName" / Bytes(lambda this: this.PolicyNameLength),
        "PolicyIDLength" / Int16ul,
        "PolicyID" / Bytes(lambda this: this.PolicyIDLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3081, version=5)
class Microsoft_Windows_CodeIntegrity_3081_5(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "ProcessNameLength" / Int16ul,
        "ProcessName" / Bytes(lambda this: this.ProcessNameLength),
        "RequestedSigningLevel" / Int8ul,
        "ValidatedSigningLevel" / Int8ul,
        "Status" / Int32ul,
        "SHA1HashSize" / Int32ul,
        "SHA1Hash" / Bytes(lambda this: this.SHA1HashSize),
        "SHA256HashSize" / Int32ul,
        "SHA256Hash" / Bytes(lambda this: this.SHA256HashSize),
        "USN" / Int64ul,
        "SISigningScenario" / Int32ul,
        "PolicyNameLength" / Int16ul,
        "PolicyName" / Bytes(lambda this: this.PolicyNameLength),
        "PolicyIDLength" / Int16ul,
        "PolicyID" / Bytes(lambda this: this.PolicyIDLength),
        "PolicyHashSize" / Int32ul,
        "PolicyHash" / Bytes(lambda this: this.PolicyHashSize)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3081, version=6)
class Microsoft_Windows_CodeIntegrity_3081_6(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "ProcessNameLength" / Int16ul,
        "ProcessName" / Bytes(lambda this: this.ProcessNameLength),
        "RequestedSigningLevel" / Int8ul,
        "ValidatedSigningLevel" / Int8ul,
        "Status" / Int32ul,
        "SHA1HashSize" / Int32ul,
        "SHA1Hash" / Bytes(lambda this: this.SHA1HashSize),
        "SHA256HashSize" / Int32ul,
        "SHA256Hash" / Bytes(lambda this: this.SHA256HashSize),
        "USN" / Int64ul,
        "SISigningScenario" / Int32ul,
        "PolicyNameLength" / Int16ul,
        "PolicyName" / Bytes(lambda this: this.PolicyNameLength),
        "PolicyIDLength" / Int16ul,
        "PolicyID" / Bytes(lambda this: this.PolicyIDLength),
        "PolicyHashSize" / Int32ul,
        "PolicyHash" / Bytes(lambda this: this.PolicyHashSize)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3081, version=7)
class Microsoft_Windows_CodeIntegrity_3081_7(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "ProcessNameLength" / Int16ul,
        "ProcessName" / Bytes(lambda this: this.ProcessNameLength),
        "RequestedSigningLevel" / Int8ul,
        "ValidatedSigningLevel" / Int8ul,
        "Status" / Int32ul,
        "SHA1HashSize" / Int32ul,
        "SHA1Hash" / Bytes(lambda this: this.SHA1HashSize),
        "SHA256HashSize" / Int32ul,
        "SHA256Hash" / Bytes(lambda this: this.SHA256HashSize),
        "USN" / Int64ul,
        "SISigningScenario" / Int32ul,
        "PolicyNameLength" / Int16ul,
        "PolicyName" / Bytes(lambda this: this.PolicyNameLength),
        "PolicyIDLength" / Int16ul,
        "PolicyID" / Bytes(lambda this: this.PolicyIDLength),
        "PolicyHashSize" / Int32ul,
        "PolicyHash" / Bytes(lambda this: this.PolicyHashSize)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3081, version=8)
class Microsoft_Windows_CodeIntegrity_3081_8(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "ProcessNameLength" / Int16ul,
        "ProcessName" / Bytes(lambda this: this.ProcessNameLength),
        "RequestedSigningLevel" / Int8ul,
        "ValidatedSigningLevel" / Int8ul,
        "Status" / Int32ul,
        "SHA1HashSize" / Int32ul,
        "SHA1Hash" / Bytes(lambda this: this.SHA1HashSize),
        "SHA256HashSize" / Int32ul,
        "SHA256Hash" / Bytes(lambda this: this.SHA256HashSize),
        "USN" / Int64ul,
        "SISigningScenario" / Int32ul,
        "PolicyNameLength" / Int16ul,
        "PolicyName" / Bytes(lambda this: this.PolicyNameLength),
        "PolicyIDLength" / Int16ul,
        "PolicyID" / Bytes(lambda this: this.PolicyIDLength),
        "PolicyHashSize" / Int32ul,
        "PolicyHash" / Bytes(lambda this: this.PolicyHashSize)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3081, version=9)
class Microsoft_Windows_CodeIntegrity_3081_9(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "ProcessNameLength" / Int16ul,
        "ProcessName" / Bytes(lambda this: this.ProcessNameLength),
        "RequestedSigningLevel" / Int8ul,
        "ValidatedSigningLevel" / Int8ul,
        "Status" / Int32ul,
        "SHA1HashSize" / Int32ul,
        "SHA1Hash" / Bytes(lambda this: this.SHA1HashSize),
        "SHA256HashSize" / Int32ul,
        "SHA256Hash" / Bytes(lambda this: this.SHA256HashSize),
        "USN" / Int64ul,
        "SISigningScenario" / Int32ul,
        "PolicyNameLength" / Int16ul,
        "PolicyName" / Bytes(lambda this: this.PolicyNameLength),
        "PolicyIDLength" / Int16ul,
        "PolicyID" / Bytes(lambda this: this.PolicyIDLength),
        "PolicyHashSize" / Int32ul,
        "PolicyHash" / Bytes(lambda this: this.PolicyHashSize),
        "OriginalFileNameLength" / Int16ul,
        "OriginalFileName" / Bytes(lambda this: this.OriginalFileNameLength),
        "InternalNameLength" / Int16ul,
        "InternalName" / Bytes(lambda this: this.InternalNameLength),
        "FileDescriptionLength" / Int16ul,
        "FileDescription" / Bytes(lambda this: this.FileDescriptionLength),
        "ProductNameLength" / Int16ul,
        "ProductName" / Bytes(lambda this: this.ProductNameLength),
        "FileVersion" / CString
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3081, version=10)
class Microsoft_Windows_CodeIntegrity_3081_10(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "ProcessNameLength" / Int16ul,
        "ProcessName" / Bytes(lambda this: this.ProcessNameLength),
        "RequestedSigningLevel" / Int8ul,
        "ValidatedSigningLevel" / Int8ul,
        "Status" / Int32ul,
        "SHA1HashSize" / Int32ul,
        "SHA1Hash" / Bytes(lambda this: this.SHA1HashSize),
        "SHA256HashSize" / Int32ul,
        "SHA256Hash" / Bytes(lambda this: this.SHA256HashSize),
        "USN" / Int64ul,
        "SISigningScenario" / Int32ul,
        "PolicyNameLength" / Int16ul,
        "PolicyName" / Bytes(lambda this: this.PolicyNameLength),
        "PolicyIDLength" / Int16ul,
        "PolicyID" / Bytes(lambda this: this.PolicyIDLength),
        "PolicyHashSize" / Int32ul,
        "PolicyHash" / Bytes(lambda this: this.PolicyHashSize),
        "OriginalFileNameLength" / Int16ul,
        "OriginalFileName" / Bytes(lambda this: this.OriginalFileNameLength),
        "InternalNameLength" / Int16ul,
        "InternalName" / Bytes(lambda this: this.InternalNameLength),
        "FileDescriptionLength" / Int16ul,
        "FileDescription" / Bytes(lambda this: this.FileDescriptionLength),
        "ProductNameLength" / Int16ul,
        "ProductName" / Bytes(lambda this: this.ProductNameLength),
        "FileVersion" / CString
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3081, version=11)
class Microsoft_Windows_CodeIntegrity_3081_11(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "ProcessNameLength" / Int16ul,
        "ProcessName" / Bytes(lambda this: this.ProcessNameLength),
        "RequestedSigningLevel" / Int8ul,
        "ValidatedSigningLevel" / Int8ul,
        "Status" / Int32ul,
        "SHA1HashSize" / Int32ul,
        "SHA1Hash" / Bytes(lambda this: this.SHA1HashSize),
        "SHA256HashSize" / Int32ul,
        "SHA256Hash" / Bytes(lambda this: this.SHA256HashSize),
        "USN" / Int64ul,
        "SISigningScenario" / Int32ul,
        "PolicyNameLength" / Int16ul,
        "PolicyName" / Bytes(lambda this: this.PolicyNameLength),
        "PolicyIDLength" / Int16ul,
        "PolicyID" / Bytes(lambda this: this.PolicyIDLength),
        "PolicyHashSize" / Int32ul,
        "PolicyHash" / Bytes(lambda this: this.PolicyHashSize),
        "OriginalFileNameLength" / Int16ul,
        "OriginalFileName" / Bytes(lambda this: this.OriginalFileNameLength),
        "InternalNameLength" / Int16ul,
        "InternalName" / Bytes(lambda this: this.InternalNameLength),
        "FileDescriptionLength" / Int16ul,
        "FileDescription" / Bytes(lambda this: this.FileDescriptionLength),
        "ProductNameLength" / Int16ul,
        "ProductName" / Bytes(lambda this: this.ProductNameLength),
        "FileVersion" / CString
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3081, version=12)
class Microsoft_Windows_CodeIntegrity_3081_12(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "ProcessNameLength" / Int16ul,
        "ProcessName" / Bytes(lambda this: this.ProcessNameLength),
        "RequestedSigningLevel" / Int8ul,
        "ValidatedSigningLevel" / Int8ul,
        "Status" / Int32ul,
        "SHA1HashSize" / Int32ul,
        "SHA1Hash" / Bytes(lambda this: this.SHA1HashSize),
        "SHA256HashSize" / Int32ul,
        "SHA256Hash" / Bytes(lambda this: this.SHA256HashSize),
        "USN" / Int64ul,
        "SISigningScenario" / Int32ul,
        "PolicyNameLength" / Int16ul,
        "PolicyName" / Bytes(lambda this: this.PolicyNameLength),
        "PolicyIDLength" / Int16ul,
        "PolicyID" / Bytes(lambda this: this.PolicyIDLength),
        "PolicyHashSize" / Int32ul,
        "PolicyHash" / Bytes(lambda this: this.PolicyHashSize),
        "OriginalFileNameLength" / Int16ul,
        "OriginalFileName" / Bytes(lambda this: this.OriginalFileNameLength),
        "InternalNameLength" / Int16ul,
        "InternalName" / Bytes(lambda this: this.InternalNameLength),
        "FileDescriptionLength" / Int16ul,
        "FileDescription" / Bytes(lambda this: this.FileDescriptionLength),
        "ProductNameLength" / Int16ul,
        "ProductName" / Bytes(lambda this: this.ProductNameLength),
        "FileVersion" / CString
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3082, version=0)
class Microsoft_Windows_CodeIntegrity_3082_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3083, version=0)
class Microsoft_Windows_CodeIntegrity_3083_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3084, version=0)
class Microsoft_Windows_CodeIntegrity_3084_0(Etw):
    pattern = Struct(
        "Settings" / Int32ul,
        "Exemption" / Int8ul
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3085, version=0)
class Microsoft_Windows_CodeIntegrity_3085_0(Etw):
    pattern = Struct(
        "Settings" / Int32ul,
        "Exemption" / Int8ul
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3086, version=0)
class Microsoft_Windows_CodeIntegrity_3086_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength),
        "ProcessNameLength" / Int16ul,
        "ProcessNameBuffer" / Bytes(lambda this: this.ProcessNameLength),
        "RequestedPolicy" / Int8ul,
        "ValidatedPolicy" / Int8ul,
        "Status" / Int32ul
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3087, version=0)
class Microsoft_Windows_CodeIntegrity_3087_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength),
        "Status" / Int32ul
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3088, version=0)
class Microsoft_Windows_CodeIntegrity_3088_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "StatusCode" / Int32ul,
        "ManagedInstallerEnabled" / Int8ul,
        "PassesManagedInstaller" / Int8ul,
        "SmartlockerEnabled" / Int8ul,
        "PassesSmartlocker" / Int8ul,
        "DefenderTrust" / Int32sl,
        "AuditEnabled" / Int8ul,
        "PolicyNameLength" / Int16ul,
        "PolicyName" / Bytes(lambda this: this.PolicyNameLength),
        "PolicyIDLength" / Int16ul,
        "PolicyID" / Bytes(lambda this: this.PolicyIDLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3089, version=0)
class Microsoft_Windows_CodeIntegrity_3089_0(Etw):
    pattern = Struct(
        "TotalSignatureCount" / Int32ul,
        "Signature" / Int32ul,
        "HashSize" / Int32ul,
        "Hash" / Bytes(lambda this: this.HashSize),
        "SignatureType" / Int8ul,
        "ValidatedSigningLevel" / Int8ul,
        "VerificationError" / Int8ul,
        "Flags" / Int32ul,
        "PolicyBits" / Int32ul,
        "NotValidBefore" / Int64ul,
        "NotValidAfter" / Int64ul,
        "PublisherNameLength" / Int16ul,
        "PublisherName" / Bytes(lambda this: this.PublisherNameLength),
        "IssuerNameLength" / Int16ul,
        "IssuerName" / Bytes(lambda this: this.IssuerNameLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3089, version=1)
class Microsoft_Windows_CodeIntegrity_3089_1(Etw):
    pattern = Struct(
        "TotalSignatureCount" / Int32ul,
        "Signature" / Int32ul,
        "HashSize" / Int32ul,
        "Hash" / Bytes(lambda this: this.HashSize),
        "PageHash" / Int8ul,
        "SignatureType" / Int8ul,
        "ValidatedSigningLevel" / Int8ul,
        "VerificationError" / Int8ul,
        "Flags" / Int32ul,
        "PolicyBits" / Int32ul,
        "NotValidBefore" / Int64ul,
        "NotValidAfter" / Int64ul,
        "PublisherNameLength" / Int16ul,
        "PublisherName" / Bytes(lambda this: this.PublisherNameLength),
        "IssuerNameLength" / Int16ul,
        "IssuerName" / Bytes(lambda this: this.IssuerNameLength),
        "PublisherTBSHashSize" / Int32ul,
        "PublisherTBSHash" / Bytes(lambda this: this.PublisherTBSHashSize),
        "IssuerTBSHashSize" / Int32ul,
        "IssuerTBSHash" / Bytes(lambda this: this.IssuerTBSHashSize)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3089, version=2)
class Microsoft_Windows_CodeIntegrity_3089_2(Etw):
    pattern = Struct(
        "TotalSignatureCount" / Int32ul,
        "Signature" / Int32ul,
        "CacheState" / Int8ul,
        "HashSize" / Int32ul,
        "Hash" / Bytes(lambda this: this.HashSize),
        "PageHash" / Int8ul,
        "SignatureType" / Int8ul,
        "ValidatedSigningLevel" / Int8ul,
        "VerificationError" / Int8ul,
        "Flags" / Int32ul,
        "PolicyBits" / Int32ul,
        "NotValidBefore" / Int64ul,
        "NotValidAfter" / Int64ul,
        "PublisherNameLength" / Int16ul,
        "PublisherName" / Bytes(lambda this: this.PublisherNameLength),
        "IssuerNameLength" / Int16ul,
        "IssuerName" / Bytes(lambda this: this.IssuerNameLength),
        "PublisherTBSHashSize" / Int32ul,
        "PublisherTBSHash" / Bytes(lambda this: this.PublisherTBSHashSize),
        "IssuerTBSHashSize" / Int32ul,
        "IssuerTBSHash" / Bytes(lambda this: this.IssuerTBSHashSize)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3090, version=0)
class Microsoft_Windows_CodeIntegrity_3090_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "StatusCode" / Int32ul,
        "ManagedInstallerEnabled" / Int8ul,
        "PassesManagedInstaller" / Int8ul,
        "SmartlockerEnabled" / Int8ul,
        "PassesSmartlocker" / Int8ul,
        "DefenderTrust" / Int32sl,
        "AuditEnabled" / Int8ul,
        "PolicyNameLength" / Int16ul,
        "PolicyName" / Bytes(lambda this: this.PolicyNameLength),
        "PolicyIDLength" / Int16ul,
        "PolicyID" / Bytes(lambda this: this.PolicyIDLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3091, version=0)
class Microsoft_Windows_CodeIntegrity_3091_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "StatusCode" / Int32ul,
        "ManagedInstallerEnabled" / Int8ul,
        "PassesManagedInstaller" / Int8ul,
        "SmartlockerEnabled" / Int8ul,
        "PassesSmartlocker" / Int8ul,
        "DefenderTrust" / Int32sl,
        "AuditEnabled" / Int8ul,
        "PolicyNameLength" / Int16ul,
        "PolicyName" / Bytes(lambda this: this.PolicyNameLength),
        "PolicyIDLength" / Int16ul,
        "PolicyID" / Bytes(lambda this: this.PolicyIDLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3092, version=0)
class Microsoft_Windows_CodeIntegrity_3092_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "StatusCode" / Int32ul,
        "ManagedInstallerEnabled" / Int8ul,
        "PassesManagedInstaller" / Int8ul,
        "SmartlockerEnabled" / Int8ul,
        "PassesSmartlocker" / Int8ul,
        "DefenderTrust" / Int32sl,
        "AuditEnabled" / Int8ul,
        "PolicyNameLength" / Int16ul,
        "PolicyName" / Bytes(lambda this: this.PolicyNameLength),
        "PolicyIDLength" / Int16ul,
        "PolicyID" / Bytes(lambda this: this.PolicyIDLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3095, version=0)
class Microsoft_Windows_CodeIntegrity_3095_0(Etw):
    pattern = Struct(
        "PolicyNameLength" / Int16ul,
        "PolicyNameBuffer" / Bytes(lambda this: this.PolicyNameLength),
        "PolicyIdLength" / Int16ul,
        "PolicyIdBuffer" / Bytes(lambda this: this.PolicyIdLength),
        "TypeOfPolicy" / Int32ul,
        "Status" / Int32ul,
        "Options" / Int32ul,
        "PolicyHashSize" / Int32ul,
        "PolicyHash" / Bytes(lambda this: this.PolicyHashSize)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3095, version=1)
class Microsoft_Windows_CodeIntegrity_3095_1(Etw):
    pattern = Struct(
        "PolicyNameLength" / Int16ul,
        "PolicyNameBuffer" / Bytes(lambda this: this.PolicyNameLength),
        "PolicyIdLength" / Int16ul,
        "PolicyIdBuffer" / Bytes(lambda this: this.PolicyIdLength),
        "PolicyGUID" / Guid,
        "Status" / Int32ul,
        "Options" / Int32ul,
        "PolicyHashSize" / Int32ul,
        "PolicyHash" / Bytes(lambda this: this.PolicyHashSize)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3096, version=0)
class Microsoft_Windows_CodeIntegrity_3096_0(Etw):
    pattern = Struct(
        "PolicyNameLength" / Int16ul,
        "PolicyNameBuffer" / Bytes(lambda this: this.PolicyNameLength),
        "PolicyIdLength" / Int16ul,
        "PolicyIdBuffer" / Bytes(lambda this: this.PolicyIdLength),
        "TypeOfPolicy" / Int32ul,
        "Status" / Int32ul,
        "Options" / Int32ul,
        "PolicyHashSize" / Int32ul,
        "PolicyHash" / Bytes(lambda this: this.PolicyHashSize)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3096, version=1)
class Microsoft_Windows_CodeIntegrity_3096_1(Etw):
    pattern = Struct(
        "PolicyNameLength" / Int16ul,
        "PolicyNameBuffer" / Bytes(lambda this: this.PolicyNameLength),
        "PolicyIdLength" / Int16ul,
        "PolicyIdBuffer" / Bytes(lambda this: this.PolicyIdLength),
        "PolicyGUID" / Guid,
        "Status" / Int32ul,
        "Options" / Int32ul,
        "PolicyHashSize" / Int32ul,
        "PolicyHash" / Bytes(lambda this: this.PolicyHashSize)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3097, version=0)
class Microsoft_Windows_CodeIntegrity_3097_0(Etw):
    pattern = Struct(
        "PolicyNameLength" / Int16ul,
        "PolicyNameBuffer" / Bytes(lambda this: this.PolicyNameLength),
        "PolicyIdLength" / Int16ul,
        "PolicyIdBuffer" / Bytes(lambda this: this.PolicyIdLength),
        "TypeOfPolicy" / Int32ul,
        "Status" / Int32ul,
        "Options" / Int32ul,
        "PolicyHashSize" / Int32ul,
        "PolicyHash" / Bytes(lambda this: this.PolicyHashSize)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3097, version=1)
class Microsoft_Windows_CodeIntegrity_3097_1(Etw):
    pattern = Struct(
        "PolicyNameLength" / Int16ul,
        "PolicyNameBuffer" / Bytes(lambda this: this.PolicyNameLength),
        "PolicyIdLength" / Int16ul,
        "PolicyIdBuffer" / Bytes(lambda this: this.PolicyIdLength),
        "PolicyGUID" / Guid,
        "Status" / Int32ul,
        "Options" / Int32ul,
        "PolicyHashSize" / Int32ul,
        "PolicyHash" / Bytes(lambda this: this.PolicyHashSize)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3099, version=0)
class Microsoft_Windows_CodeIntegrity_3099_0(Etw):
    pattern = Struct(
        "PolicyNameLength" / Int16ul,
        "PolicyNameBuffer" / Bytes(lambda this: this.PolicyNameLength),
        "PolicyIdLength" / Int16ul,
        "PolicyIdBuffer" / Bytes(lambda this: this.PolicyIdLength),
        "TypeOfPolicy" / Int32ul,
        "Status" / Int32ul,
        "Options" / Int32ul,
        "PolicyHashSize" / Int32ul,
        "PolicyHash" / Bytes(lambda this: this.PolicyHashSize)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3099, version=1)
class Microsoft_Windows_CodeIntegrity_3099_1(Etw):
    pattern = Struct(
        "PolicyNameLength" / Int16ul,
        "PolicyNameBuffer" / Bytes(lambda this: this.PolicyNameLength),
        "PolicyIdLength" / Int16ul,
        "PolicyIdBuffer" / Bytes(lambda this: this.PolicyIdLength),
        "PolicyGUID" / Guid,
        "Status" / Int32ul,
        "Options" / Int32ul,
        "PolicyHashSize" / Int32ul,
        "PolicyHash" / Bytes(lambda this: this.PolicyHashSize)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3100, version=0)
class Microsoft_Windows_CodeIntegrity_3100_0(Etw):
    pattern = Struct(
        "PolicyNameLength" / Int16ul,
        "PolicyNameBuffer" / Bytes(lambda this: this.PolicyNameLength),
        "PolicyIdLength" / Int16ul,
        "PolicyIdBuffer" / Bytes(lambda this: this.PolicyIdLength),
        "TypeOfPolicy" / Int32ul,
        "Status" / Int32ul,
        "Options" / Int32ul,
        "PolicyHashSize" / Int32ul,
        "PolicyHash" / Bytes(lambda this: this.PolicyHashSize)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3100, version=1)
class Microsoft_Windows_CodeIntegrity_3100_1(Etw):
    pattern = Struct(
        "PolicyNameLength" / Int16ul,
        "PolicyNameBuffer" / Bytes(lambda this: this.PolicyNameLength),
        "PolicyIdLength" / Int16ul,
        "PolicyIdBuffer" / Bytes(lambda this: this.PolicyIdLength),
        "PolicyGUID" / Guid,
        "Status" / Int32ul,
        "Options" / Int32ul,
        "PolicyHashSize" / Int32ul,
        "PolicyHash" / Bytes(lambda this: this.PolicyHashSize)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3101, version=0)
class Microsoft_Windows_CodeIntegrity_3101_0(Etw):
    pattern = Struct(
        "NumberOfPolicies" / Int32ul
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3102, version=0)
class Microsoft_Windows_CodeIntegrity_3102_0(Etw):
    pattern = Struct(
        "NumberOfPolicies" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3103, version=0)
class Microsoft_Windows_CodeIntegrity_3103_0(Etw):
    pattern = Struct(
        "PolicyType" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3103, version=1)
class Microsoft_Windows_CodeIntegrity_3103_1(Etw):
    pattern = Struct(
        "PolicyGUID" / Guid,
        "Status" / Int32ul
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3104, version=0)
class Microsoft_Windows_CodeIntegrity_3104_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength)
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3105, version=0)
class Microsoft_Windows_CodeIntegrity_3105_0(Etw):
    pattern = Struct(
        "PolicyGUID" / Guid
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3106, version=0)
class Microsoft_Windows_CodeIntegrity_3106_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength),
        "Status" / Int32ul
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3107, version=0)
class Microsoft_Windows_CodeIntegrity_3107_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength),
        "Status" / Int32ul
    )


@declare(guid=guid("4ee76bd8-3cf4-44a0-a0ac-3937643e37a3"), event_id=3112, version=0)
class Microsoft_Windows_CodeIntegrity_3112_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength),
        "ProcessNameLength" / Int16ul,
        "ProcessNameBuffer" / Bytes(lambda this: this.ProcessNameLength),
        "RequestedPolicy" / Int8ul,
        "ValidatedPolicy" / Int8ul,
        "Status" / Int32ul
    )

