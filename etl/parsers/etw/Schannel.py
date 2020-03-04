# -*- coding: utf-8 -*-
"""
Schannel
GUID : 1f678132-5938-4686-9fdc-c8ff68f15c85
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("1f678132-5938-4686-9fdc-c8ff68f15c85"), event_id=36865, version=0)
class Schannel_36865_0(Etw):
    pattern = Struct(
        "ModuleName" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("1f678132-5938-4686-9fdc-c8ff68f15c85"), event_id=36867, version=0)
class Schannel_36867_0(Etw):
    pattern = Struct(
        "Type" / WString,
        "__binLength" / Int32ul,
        "binaryData" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("1f678132-5938-4686-9fdc-c8ff68f15c85"), event_id=36868, version=0)
class Schannel_36868_0(Etw):
    pattern = Struct(
        "Type" / WString,
        "CSPName" / WString,
        "CSPType" / Int32ul,
        "KeyName" / WString,
        "KeyType" / WString,
        "KeyFlags" / Int32ul,
        "__binLength" / Int32ul,
        "EncodedCert" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("1f678132-5938-4686-9fdc-c8ff68f15c85"), event_id=36869, version=0)
class Schannel_36869_0(Etw):
    pattern = Struct(
        "Type" / WString,
        "__binLength" / Int32ul,
        "binaryData" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("1f678132-5938-4686-9fdc-c8ff68f15c85"), event_id=36870, version=0)
class Schannel_36870_0(Etw):
    pattern = Struct(
        "Type" / WString,
        "ErrorCode" / Int32ul,
        "ErrorStatus" / Int32ul
    )


@declare(guid=guid("1f678132-5938-4686-9fdc-c8ff68f15c85"), event_id=36871, version=0)
class Schannel_36871_0(Etw):
    pattern = Struct(
        "Type" / WString,
        "ErrorState" / Int32ul
    )


@declare(guid=guid("1f678132-5938-4686-9fdc-c8ff68f15c85"), event_id=36872, version=0)
class Schannel_36872_0(Etw):
    pattern = Struct(
        "Type" / WString,
        "ErrorCode" / Int32ul,
        "CertFlags" / Int32ul,
        "__binLength" / Int32ul,
        "CredContext" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("1f678132-5938-4686-9fdc-c8ff68f15c85"), event_id=36874, version=0)
class Schannel_36874_0(Etw):
    pattern = Struct(
        "Protocol" / WString
    )


@declare(guid=guid("1f678132-5938-4686-9fdc-c8ff68f15c85"), event_id=36876, version=0)
class Schannel_36876_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "__binLength" / Int32ul,
        "pCertificateContext" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("1f678132-5938-4686-9fdc-c8ff68f15c85"), event_id=36877, version=0)
class Schannel_36877_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "__binLength" / Int32ul,
        "pCertificateContext" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("1f678132-5938-4686-9fdc-c8ff68f15c85"), event_id=36878, version=0)
class Schannel_36878_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "__binLength" / Int32ul,
        "pCertificateContext" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("1f678132-5938-4686-9fdc-c8ff68f15c85"), event_id=36879, version=0)
class Schannel_36879_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "__binLength" / Int32ul,
        "pCertificateContext" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("1f678132-5938-4686-9fdc-c8ff68f15c85"), event_id=36880, version=0)
class Schannel_36880_0(Etw):
    pattern = Struct(
        "Type" / WString,
        "Protocol" / WString,
        "CipherSuite" / Int32ul,
        "ExchangeStrength" / Int32ul,
        "ContextHandle" / Int64ul,
        "TargetName" / WString,
        "LocalCertSubjectName" / WString,
        "RemoteCertSubjectName" / WString
    )


@declare(guid=guid("1f678132-5938-4686-9fdc-c8ff68f15c85"), event_id=36881, version=0)
class Schannel_36881_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "certificateContext" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("1f678132-5938-4686-9fdc-c8ff68f15c85"), event_id=36882, version=0)
class Schannel_36882_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "certificateContext" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("1f678132-5938-4686-9fdc-c8ff68f15c85"), event_id=36883, version=0)
class Schannel_36883_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "certificateContext" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("1f678132-5938-4686-9fdc-c8ff68f15c85"), event_id=36884, version=0)
class Schannel_36884_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "__binLength" / Int32ul,
        "certificateContext" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("1f678132-5938-4686-9fdc-c8ff68f15c85"), event_id=36887, version=0)
class Schannel_36887_0(Etw):
    pattern = Struct(
        "AlertDesc" / Int32ul
    )


@declare(guid=guid("1f678132-5938-4686-9fdc-c8ff68f15c85"), event_id=36888, version=0)
class Schannel_36888_0(Etw):
    pattern = Struct(
        "AlertDesc" / Int32ul,
        "ErrorState" / Int32ul,
        "TargetName" / WString
    )


@declare(guid=guid("1f678132-5938-4686-9fdc-c8ff68f15c85"), event_id=36889, version=0)
class Schannel_36889_0(Etw):
    pattern = Struct(
        "Type" / WString,
        "ErrorCode" / Int32ul,
        "__binLength" / Int32ul,
        "CredContext" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("1f678132-5938-4686-9fdc-c8ff68f15c85"), event_id=36912, version=0)
class Schannel_36912_0(Etw):
    pattern = Struct(
        "Path" / WString
    )

