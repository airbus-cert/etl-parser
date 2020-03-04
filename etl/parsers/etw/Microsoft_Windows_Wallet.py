# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Wallet
GUID : 6ed11b00-c1b5-48cb-aecc-ff72ebefbae8
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("6ed11b00-c1b5-48cb-aecc-ff72ebefbae8"), event_id=104, version=0)
class Microsoft_Windows_Wallet_104_0(Etw):
    pattern = Struct(
        "ItemId" / WString
    )


@declare(guid=guid("6ed11b00-c1b5-48cb-aecc-ff72ebefbae8"), event_id=105, version=0)
class Microsoft_Windows_Wallet_105_0(Etw):
    pattern = Struct(
        "ItemId" / WString
    )


@declare(guid=guid("6ed11b00-c1b5-48cb-aecc-ff72ebefbae8"), event_id=201, version=0)
class Microsoft_Windows_Wallet_201_0(Etw):
    pattern = Struct(
        "ListType" / Int32ul
    )


@declare(guid=guid("6ed11b00-c1b5-48cb-aecc-ff72ebefbae8"), event_id=202, version=0)
class Microsoft_Windows_Wallet_202_0(Etw):
    pattern = Struct(
        "ListType" / Int32ul
    )


@declare(guid=guid("6ed11b00-c1b5-48cb-aecc-ff72ebefbae8"), event_id=203, version=0)
class Microsoft_Windows_Wallet_203_0(Etw):
    pattern = Struct(
        "ListType" / Int32ul
    )


@declare(guid=guid("6ed11b00-c1b5-48cb-aecc-ff72ebefbae8"), event_id=204, version=0)
class Microsoft_Windows_Wallet_204_0(Etw):
    pattern = Struct(
        "ListType" / Int32ul
    )


@declare(guid=guid("6ed11b00-c1b5-48cb-aecc-ff72ebefbae8"), event_id=305, version=0)
class Microsoft_Windows_Wallet_305_0(Etw):
    pattern = Struct(
        "ListType" / Int32ul
    )


@declare(guid=guid("6ed11b00-c1b5-48cb-aecc-ff72ebefbae8"), event_id=306, version=0)
class Microsoft_Windows_Wallet_306_0(Etw):
    pattern = Struct(
        "ListType" / Int32ul
    )


@declare(guid=guid("6ed11b00-c1b5-48cb-aecc-ff72ebefbae8"), event_id=307, version=0)
class Microsoft_Windows_Wallet_307_0(Etw):
    pattern = Struct(
        "ListType" / Int32ul
    )


@declare(guid=guid("6ed11b00-c1b5-48cb-aecc-ff72ebefbae8"), event_id=308, version=0)
class Microsoft_Windows_Wallet_308_0(Etw):
    pattern = Struct(
        "ListType" / Int32ul
    )


@declare(guid=guid("6ed11b00-c1b5-48cb-aecc-ff72ebefbae8"), event_id=309, version=0)
class Microsoft_Windows_Wallet_309_0(Etw):
    pattern = Struct(
        "ItemId" / Int64ul,
        "WalletItemPropertyType" / Int32ul
    )


@declare(guid=guid("6ed11b00-c1b5-48cb-aecc-ff72ebefbae8"), event_id=310, version=0)
class Microsoft_Windows_Wallet_310_0(Etw):
    pattern = Struct(
        "ItemId" / Int64ul,
        "WalletItemPropertyType" / Int32ul
    )


@declare(guid=guid("6ed11b00-c1b5-48cb-aecc-ff72ebefbae8"), event_id=311, version=0)
class Microsoft_Windows_Wallet_311_0(Etw):
    pattern = Struct(
        "ItemId" / Int64ul,
        "WalletItemPropertyType" / Int32ul
    )


@declare(guid=guid("6ed11b00-c1b5-48cb-aecc-ff72ebefbae8"), event_id=312, version=0)
class Microsoft_Windows_Wallet_312_0(Etw):
    pattern = Struct(
        "ItemId" / Int64ul,
        "WalletItemPropertyType" / Int32ul
    )

