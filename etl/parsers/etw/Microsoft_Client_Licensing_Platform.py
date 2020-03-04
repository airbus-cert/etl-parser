# -*- coding: utf-8 -*-
"""
Microsoft-Client-Licensing-Platform
GUID : b6cc0d55-9ecc-49a8-b929-2b9022426f2a
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("b6cc0d55-9ecc-49a8-b929-2b9022426f2a"), event_id=19, version=0)
class Microsoft_Client_Licensing_Platform_19_0(Etw):
    pattern = Struct(
        "ID" / Int32sl
    )


@declare(guid=guid("b6cc0d55-9ecc-49a8-b929-2b9022426f2a"), event_id=20, version=0)
class Microsoft_Client_Licensing_Platform_20_0(Etw):
    pattern = Struct(
        "ID" / Int32sl
    )


@declare(guid=guid("b6cc0d55-9ecc-49a8-b929-2b9022426f2a"), event_id=100, version=0)
class Microsoft_Client_Licensing_Platform_100_0(Etw):
    pattern = Struct(
        "Data" / WString
    )


@declare(guid=guid("b6cc0d55-9ecc-49a8-b929-2b9022426f2a"), event_id=101, version=0)
class Microsoft_Client_Licensing_Platform_101_0(Etw):
    pattern = Struct(
        "Data" / WString
    )


@declare(guid=guid("b6cc0d55-9ecc-49a8-b929-2b9022426f2a"), event_id=103, version=0)
class Microsoft_Client_Licensing_Platform_103_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("b6cc0d55-9ecc-49a8-b929-2b9022426f2a"), event_id=104, version=0)
class Microsoft_Client_Licensing_Platform_104_0(Etw):
    pattern = Struct(
        "Data" / WString
    )


@declare(guid=guid("b6cc0d55-9ecc-49a8-b929-2b9022426f2a"), event_id=106, version=0)
class Microsoft_Client_Licensing_Platform_106_0(Etw):
    pattern = Struct(
        "PackageName" / WString,
        "UserId" / WString,
        "LicenseId" / WString,
        "AssociateId" / WString
    )


@declare(guid=guid("b6cc0d55-9ecc-49a8-b929-2b9022426f2a"), event_id=107, version=0)
class Microsoft_Client_Licensing_Platform_107_0(Etw):
    pattern = Struct(
        "Data" / WString
    )


@declare(guid=guid("b6cc0d55-9ecc-49a8-b929-2b9022426f2a"), event_id=110, version=0)
class Microsoft_Client_Licensing_Platform_110_0(Etw):
    pattern = Struct(
        "Type" / Int32sl,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("b6cc0d55-9ecc-49a8-b929-2b9022426f2a"), event_id=111, version=0)
class Microsoft_Client_Licensing_Platform_111_0(Etw):
    pattern = Struct(
        "LicenseId" / WString,
        "Type" / Int32sl,
        "PackageName" / WString,
        "UserId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("b6cc0d55-9ecc-49a8-b929-2b9022426f2a"), event_id=112, version=0)
class Microsoft_Client_Licensing_Platform_112_0(Etw):
    pattern = Struct(
        "LicenseId" / WString,
        "Type" / Int32sl,
        "PackageName" / WString,
        "UserId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("b6cc0d55-9ecc-49a8-b929-2b9022426f2a"), event_id=113, version=0)
class Microsoft_Client_Licensing_Platform_113_0(Etw):
    pattern = Struct(
        "LicenseId" / WString,
        "Type" / Int32sl,
        "PackageName" / WString,
        "UserId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("b6cc0d55-9ecc-49a8-b929-2b9022426f2a"), event_id=114, version=0)
class Microsoft_Client_Licensing_Platform_114_0(Etw):
    pattern = Struct(
        "LicenseId" / WString,
        "Type" / Int32sl,
        "PackageName" / WString,
        "UserId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("b6cc0d55-9ecc-49a8-b929-2b9022426f2a"), event_id=115, version=0)
class Microsoft_Client_Licensing_Platform_115_0(Etw):
    pattern = Struct(
        "PackageName" / WString,
        "UserId" / WString,
        "Type" / Int32sl,
        "LicenseId" / WString,
        "AssociateId" / WString
    )


@declare(guid=guid("b6cc0d55-9ecc-49a8-b929-2b9022426f2a"), event_id=116, version=0)
class Microsoft_Client_Licensing_Platform_116_0(Etw):
    pattern = Struct(
        "PackageName" / WString,
        "UserId" / WString,
        "LicenseId" / WString,
        "AssociateId" / WString
    )


@declare(guid=guid("b6cc0d55-9ecc-49a8-b929-2b9022426f2a"), event_id=117, version=0)
class Microsoft_Client_Licensing_Platform_117_0(Etw):
    pattern = Struct(
        "PackageName" / WString,
        "UserId" / WString,
        "LicenseId" / WString,
        "AssociateId" / WString
    )


@declare(guid=guid("b6cc0d55-9ecc-49a8-b929-2b9022426f2a"), event_id=118, version=0)
class Microsoft_Client_Licensing_Platform_118_0(Etw):
    pattern = Struct(
        "LicenseId" / WString,
        "AssociateId" / WString,
        "DeviceId" / WString
    )


@declare(guid=guid("b6cc0d55-9ecc-49a8-b929-2b9022426f2a"), event_id=119, version=0)
class Microsoft_Client_Licensing_Platform_119_0(Etw):
    pattern = Struct(
        "LicenseId" / WString,
        "Type" / Int32sl
    )


@declare(guid=guid("b6cc0d55-9ecc-49a8-b929-2b9022426f2a"), event_id=120, version=0)
class Microsoft_Client_Licensing_Platform_120_0(Etw):
    pattern = Struct(
        "LicenseId" / WString,
        "Type" / Int32sl,
        "PackageName" / WString,
        "UserId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("b6cc0d55-9ecc-49a8-b929-2b9022426f2a"), event_id=150, version=0)
class Microsoft_Client_Licensing_Platform_150_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("b6cc0d55-9ecc-49a8-b929-2b9022426f2a"), event_id=151, version=0)
class Microsoft_Client_Licensing_Platform_151_0(Etw):
    pattern = Struct(
        "Data" / WString
    )


@declare(guid=guid("b6cc0d55-9ecc-49a8-b929-2b9022426f2a"), event_id=157, version=0)
class Microsoft_Client_Licensing_Platform_157_0(Etw):
    pattern = Struct(
        "PackageName" / WString,
        "LicenseId" / WString
    )


@declare(guid=guid("b6cc0d55-9ecc-49a8-b929-2b9022426f2a"), event_id=158, version=0)
class Microsoft_Client_Licensing_Platform_158_0(Etw):
    pattern = Struct(
        "PackageName" / WString,
        "LicenseId" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("b6cc0d55-9ecc-49a8-b929-2b9022426f2a"), event_id=159, version=0)
class Microsoft_Client_Licensing_Platform_159_0(Etw):
    pattern = Struct(
        "PackageName" / WString,
        "LicenseId" / WString
    )


@declare(guid=guid("b6cc0d55-9ecc-49a8-b929-2b9022426f2a"), event_id=160, version=0)
class Microsoft_Client_Licensing_Platform_160_0(Etw):
    pattern = Struct(
        "PackageName" / WString,
        "LicenseId" / WString,
        "Type" / Int32sl
    )


@declare(guid=guid("b6cc0d55-9ecc-49a8-b929-2b9022426f2a"), event_id=170, version=0)
class Microsoft_Client_Licensing_Platform_170_0(Etw):
    pattern = Struct(
        "Namespace" / WString,
        "VariableName" / WString,
        "AssociateId" / WString
    )


@declare(guid=guid("b6cc0d55-9ecc-49a8-b929-2b9022426f2a"), event_id=171, version=0)
class Microsoft_Client_Licensing_Platform_171_0(Etw):
    pattern = Struct(
        "Namespace" / WString,
        "VariableName" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("b6cc0d55-9ecc-49a8-b929-2b9022426f2a"), event_id=172, version=0)
class Microsoft_Client_Licensing_Platform_172_0(Etw):
    pattern = Struct(
        "Arguments" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("b6cc0d55-9ecc-49a8-b929-2b9022426f2a"), event_id=173, version=0)
class Microsoft_Client_Licensing_Platform_173_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("b6cc0d55-9ecc-49a8-b929-2b9022426f2a"), event_id=174, version=0)
class Microsoft_Client_Licensing_Platform_174_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )

