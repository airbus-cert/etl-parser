# -*- coding: utf-8 -*-
"""
AESMService
GUID : ce6e83d3-a7d9-4a91-96e0-e018ad574610
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("ce6e83d3-a7d9-4a91-96e0-e018ad574610"), event_id=0, version=0)
class AESMService_0_0(Etw):
    pattern = Struct(
        "attrAnsiString" / CString
    )


@declare(guid=guid("ce6e83d3-a7d9-4a91-96e0-e018ad574610"), event_id=101, version=0)
class AESMService_101_0(Etw):
    pattern = Struct(
        "attrUnicodeString" / WString
    )


@declare(guid=guid("ce6e83d3-a7d9-4a91-96e0-e018ad574610"), event_id=102, version=0)
class AESMService_102_0(Etw):
    pattern = Struct(
        "attrAnsiString" / CString
    )


@declare(guid=guid("ce6e83d3-a7d9-4a91-96e0-e018ad574610"), event_id=103, version=0)
class AESMService_103_0(Etw):
    pattern = Struct(
        "attrUnicodeString" / WString
    )


@declare(guid=guid("ce6e83d3-a7d9-4a91-96e0-e018ad574610"), event_id=104, version=0)
class AESMService_104_0(Etw):
    pattern = Struct(
        "attrAnsiString" / CString
    )


@declare(guid=guid("ce6e83d3-a7d9-4a91-96e0-e018ad574610"), event_id=105, version=0)
class AESMService_105_0(Etw):
    pattern = Struct(
        "attrAnsiString" / CString
    )


@declare(guid=guid("ce6e83d3-a7d9-4a91-96e0-e018ad574610"), event_id=106, version=0)
class AESMService_106_0(Etw):
    pattern = Struct(
        "attrUnicodeString" / WString
    )


@declare(guid=guid("ce6e83d3-a7d9-4a91-96e0-e018ad574610"), event_id=107, version=0)
class AESMService_107_0(Etw):
    pattern = Struct(
        "attrAnsiString" / CString
    )


@declare(guid=guid("ce6e83d3-a7d9-4a91-96e0-e018ad574610"), event_id=108, version=0)
class AESMService_108_0(Etw):
    pattern = Struct(
        "attrUnicodeString" / WString
    )


@declare(guid=guid("ce6e83d3-a7d9-4a91-96e0-e018ad574610"), event_id=201, version=0)
class AESMService_201_0(Etw):
    pattern = Struct(
        "attrUnicodeString" / WString
    )


@declare(guid=guid("ce6e83d3-a7d9-4a91-96e0-e018ad574610"), event_id=202, version=0)
class AESMService_202_0(Etw):
    pattern = Struct(
        "attrAnsiString" / CString
    )


@declare(guid=guid("ce6e83d3-a7d9-4a91-96e0-e018ad574610"), event_id=203, version=0)
class AESMService_203_0(Etw):
    pattern = Struct(
        "attrUnicodeString" / WString
    )


@declare(guid=guid("ce6e83d3-a7d9-4a91-96e0-e018ad574610"), event_id=204, version=0)
class AESMService_204_0(Etw):
    pattern = Struct(
        "attrAnsiString" / CString
    )


@declare(guid=guid("ce6e83d3-a7d9-4a91-96e0-e018ad574610"), event_id=205, version=0)
class AESMService_205_0(Etw):
    pattern = Struct(
        "attrAnsiString" / CString
    )


@declare(guid=guid("ce6e83d3-a7d9-4a91-96e0-e018ad574610"), event_id=206, version=0)
class AESMService_206_0(Etw):
    pattern = Struct(
        "attrUnicodeString" / WString
    )


@declare(guid=guid("ce6e83d3-a7d9-4a91-96e0-e018ad574610"), event_id=207, version=0)
class AESMService_207_0(Etw):
    pattern = Struct(
        "attrAnsiString" / CString
    )


@declare(guid=guid("ce6e83d3-a7d9-4a91-96e0-e018ad574610"), event_id=208, version=0)
class AESMService_208_0(Etw):
    pattern = Struct(
        "attrUnicodeString" / WString
    )

