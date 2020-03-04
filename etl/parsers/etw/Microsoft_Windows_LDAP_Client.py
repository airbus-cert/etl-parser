# -*- coding: utf-8 -*-
"""
Microsoft-Windows-LDAP-Client
GUID : 099614a5-5dd7-4788-8bc9-e29f43db28fc
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("099614a5-5dd7-4788-8bc9-e29f43db28fc"), event_id=1, version=0)
class Microsoft_Windows_LDAP_Client_1_0(Etw):
    pattern = Struct(
        "Message" / CString
    )


@declare(guid=guid("099614a5-5dd7-4788-8bc9-e29f43db28fc"), event_id=2, version=0)
class Microsoft_Windows_LDAP_Client_2_0(Etw):
    pattern = Struct(
        "Message" / CString
    )


@declare(guid=guid("099614a5-5dd7-4788-8bc9-e29f43db28fc"), event_id=3, version=0)
class Microsoft_Windows_LDAP_Client_3_0(Etw):
    pattern = Struct(
        "Message" / CString
    )


@declare(guid=guid("099614a5-5dd7-4788-8bc9-e29f43db28fc"), event_id=4, version=0)
class Microsoft_Windows_LDAP_Client_4_0(Etw):
    pattern = Struct(
        "Message" / CString
    )


@declare(guid=guid("099614a5-5dd7-4788-8bc9-e29f43db28fc"), event_id=5, version=0)
class Microsoft_Windows_LDAP_Client_5_0(Etw):
    pattern = Struct(
        "Message" / CString
    )


@declare(guid=guid("099614a5-5dd7-4788-8bc9-e29f43db28fc"), event_id=6, version=0)
class Microsoft_Windows_LDAP_Client_6_0(Etw):
    pattern = Struct(
        "Message" / CString
    )


@declare(guid=guid("099614a5-5dd7-4788-8bc9-e29f43db28fc"), event_id=7, version=0)
class Microsoft_Windows_LDAP_Client_7_0(Etw):
    pattern = Struct(
        "Message" / CString
    )


@declare(guid=guid("099614a5-5dd7-4788-8bc9-e29f43db28fc"), event_id=8, version=0)
class Microsoft_Windows_LDAP_Client_8_0(Etw):
    pattern = Struct(
        "Message" / CString
    )


@declare(guid=guid("099614a5-5dd7-4788-8bc9-e29f43db28fc"), event_id=9, version=0)
class Microsoft_Windows_LDAP_Client_9_0(Etw):
    pattern = Struct(
        "Message" / CString
    )


@declare(guid=guid("099614a5-5dd7-4788-8bc9-e29f43db28fc"), event_id=10, version=0)
class Microsoft_Windows_LDAP_Client_10_0(Etw):
    pattern = Struct(
        "Message" / CString
    )


@declare(guid=guid("099614a5-5dd7-4788-8bc9-e29f43db28fc"), event_id=11, version=0)
class Microsoft_Windows_LDAP_Client_11_0(Etw):
    pattern = Struct(
        "Message" / CString
    )


@declare(guid=guid("099614a5-5dd7-4788-8bc9-e29f43db28fc"), event_id=12, version=0)
class Microsoft_Windows_LDAP_Client_12_0(Etw):
    pattern = Struct(
        "Message" / CString
    )


@declare(guid=guid("099614a5-5dd7-4788-8bc9-e29f43db28fc"), event_id=13, version=0)
class Microsoft_Windows_LDAP_Client_13_0(Etw):
    pattern = Struct(
        "Message" / CString
    )


@declare(guid=guid("099614a5-5dd7-4788-8bc9-e29f43db28fc"), event_id=14, version=0)
class Microsoft_Windows_LDAP_Client_14_0(Etw):
    pattern = Struct(
        "Message" / CString
    )


@declare(guid=guid("099614a5-5dd7-4788-8bc9-e29f43db28fc"), event_id=15, version=0)
class Microsoft_Windows_LDAP_Client_15_0(Etw):
    pattern = Struct(
        "Message" / CString
    )


@declare(guid=guid("099614a5-5dd7-4788-8bc9-e29f43db28fc"), event_id=16, version=0)
class Microsoft_Windows_LDAP_Client_16_0(Etw):
    pattern = Struct(
        "Message" / CString
    )


@declare(guid=guid("099614a5-5dd7-4788-8bc9-e29f43db28fc"), event_id=17, version=0)
class Microsoft_Windows_LDAP_Client_17_0(Etw):
    pattern = Struct(
        "Message" / CString
    )


@declare(guid=guid("099614a5-5dd7-4788-8bc9-e29f43db28fc"), event_id=18, version=0)
class Microsoft_Windows_LDAP_Client_18_0(Etw):
    pattern = Struct(
        "Message" / CString
    )


@declare(guid=guid("099614a5-5dd7-4788-8bc9-e29f43db28fc"), event_id=19, version=0)
class Microsoft_Windows_LDAP_Client_19_0(Etw):
    pattern = Struct(
        "Message" / CString
    )


@declare(guid=guid("099614a5-5dd7-4788-8bc9-e29f43db28fc"), event_id=20, version=0)
class Microsoft_Windows_LDAP_Client_20_0(Etw):
    pattern = Struct(
        "Message" / CString
    )


@declare(guid=guid("099614a5-5dd7-4788-8bc9-e29f43db28fc"), event_id=21, version=0)
class Microsoft_Windows_LDAP_Client_21_0(Etw):
    pattern = Struct(
        "Message" / CString
    )


@declare(guid=guid("099614a5-5dd7-4788-8bc9-e29f43db28fc"), event_id=22, version=0)
class Microsoft_Windows_LDAP_Client_22_0(Etw):
    pattern = Struct(
        "Message" / CString
    )


@declare(guid=guid("099614a5-5dd7-4788-8bc9-e29f43db28fc"), event_id=23, version=0)
class Microsoft_Windows_LDAP_Client_23_0(Etw):
    pattern = Struct(
        "Message" / CString
    )


@declare(guid=guid("099614a5-5dd7-4788-8bc9-e29f43db28fc"), event_id=24, version=0)
class Microsoft_Windows_LDAP_Client_24_0(Etw):
    pattern = Struct(
        "Message" / CString
    )


@declare(guid=guid("099614a5-5dd7-4788-8bc9-e29f43db28fc"), event_id=25, version=0)
class Microsoft_Windows_LDAP_Client_25_0(Etw):
    pattern = Struct(
        "Message" / CString
    )


@declare(guid=guid("099614a5-5dd7-4788-8bc9-e29f43db28fc"), event_id=26, version=0)
class Microsoft_Windows_LDAP_Client_26_0(Etw):
    pattern = Struct(
        "Message" / CString
    )


@declare(guid=guid("099614a5-5dd7-4788-8bc9-e29f43db28fc"), event_id=27, version=0)
class Microsoft_Windows_LDAP_Client_27_0(Etw):
    pattern = Struct(
        "Message" / CString
    )


@declare(guid=guid("099614a5-5dd7-4788-8bc9-e29f43db28fc"), event_id=28, version=0)
class Microsoft_Windows_LDAP_Client_28_0(Etw):
    pattern = Struct(
        "Message" / CString
    )


@declare(guid=guid("099614a5-5dd7-4788-8bc9-e29f43db28fc"), event_id=29, version=0)
class Microsoft_Windows_LDAP_Client_29_0(Etw):
    pattern = Struct(
        "Message" / CString
    )


@declare(guid=guid("099614a5-5dd7-4788-8bc9-e29f43db28fc"), event_id=30, version=0)
class Microsoft_Windows_LDAP_Client_30_0(Etw):
    pattern = Struct(
        "ScopeOfSearch" / Int32ul,
        "SearchFilter" / WString,
        "DistinguishedName" / WString,
        "AttributeList" / WString,
        "ProcessId" / Int32ul
    )


@declare(guid=guid("099614a5-5dd7-4788-8bc9-e29f43db28fc"), event_id=31, version=0)
class Microsoft_Windows_LDAP_Client_31_0(Etw):
    pattern = Struct(
        "Message" / CString
    )

