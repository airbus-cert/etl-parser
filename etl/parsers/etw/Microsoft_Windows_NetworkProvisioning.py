# -*- coding: utf-8 -*-
"""
Microsoft-Windows-NetworkProvisioning
GUID : 93a19ab3-fb2c-46eb-91ef-56b0a318b983
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("93a19ab3-fb2c-46eb-91ef-56b0a318b983"), event_id=1000, version=0)
class Microsoft_Windows_NetworkProvisioning_1000_0(Etw):
    pattern = Struct(
        "SizeOfXMLInBytes" / Int64ul
    )


@declare(guid=guid("93a19ab3-fb2c-46eb-91ef-56b0a318b983"), event_id=1001, version=0)
class Microsoft_Windows_NetworkProvisioning_1001_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("93a19ab3-fb2c-46eb-91ef-56b0a318b983"), event_id=1002, version=0)
class Microsoft_Windows_NetworkProvisioning_1002_0(Etw):
    pattern = Struct(
        "Result" / Int32sl
    )


@declare(guid=guid("93a19ab3-fb2c-46eb-91ef-56b0a318b983"), event_id=1003, version=0)
class Microsoft_Windows_NetworkProvisioning_1003_0(Etw):
    pattern = Struct(
        "Result" / Int32sl
    )


@declare(guid=guid("93a19ab3-fb2c-46eb-91ef-56b0a318b983"), event_id=1004, version=0)
class Microsoft_Windows_NetworkProvisioning_1004_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32sl,
        "CarrierId" / WString,
        "SubscriberId" / WString,
        "DeviceId" / WString,
        "Signer" / WString,
        "CertificateIssuer" / WString,
        "CertificateSubject" / WString
    )


@declare(guid=guid("93a19ab3-fb2c-46eb-91ef-56b0a318b983"), event_id=1005, version=0)
class Microsoft_Windows_NetworkProvisioning_1005_0(Etw):
    pattern = Struct(
        "StreamSize" / Int64ul,
        "StreamSizeLimit" / Int64ul
    )


@declare(guid=guid("93a19ab3-fb2c-46eb-91ef-56b0a318b983"), event_id=1006, version=0)
class Microsoft_Windows_NetworkProvisioning_1006_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString,
        "Description" / WString
    )


@declare(guid=guid("93a19ab3-fb2c-46eb-91ef-56b0a318b983"), event_id=1007, version=0)
class Microsoft_Windows_NetworkProvisioning_1007_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Line" / Int32sl,
        "LinePos" / Int32sl,
        "Reason" / WString
    )


@declare(guid=guid("93a19ab3-fb2c-46eb-91ef-56b0a318b983"), event_id=1008, version=0)
class Microsoft_Windows_NetworkProvisioning_1008_0(Etw):
    pattern = Struct(
        "Result" / Int32sl
    )


@declare(guid=guid("93a19ab3-fb2c-46eb-91ef-56b0a318b983"), event_id=2001, version=0)
class Microsoft_Windows_NetworkProvisioning_2001_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32sl,
        "ErrorOccurred" / Int8ul
    )


@declare(guid=guid("93a19ab3-fb2c-46eb-91ef-56b0a318b983"), event_id=2002, version=0)
class Microsoft_Windows_NetworkProvisioning_2002_0(Etw):
    pattern = Struct(
        "BoolResult" / Int8ul
    )


@declare(guid=guid("93a19ab3-fb2c-46eb-91ef-56b0a318b983"), event_id=4001, version=0)
class Microsoft_Windows_NetworkProvisioning_4001_0(Etw):
    pattern = Struct(
        "Result" / Int32sl
    )


@declare(guid=guid("93a19ab3-fb2c-46eb-91ef-56b0a318b983"), event_id=5000, version=0)
class Microsoft_Windows_NetworkProvisioning_5000_0(Etw):
    pattern = Struct(
        "ActivationMethod" / Int32ul,
        "CarrierId" / WString,
        "SubscriberId" / WString,
        "Params" / WString
    )


@declare(guid=guid("93a19ab3-fb2c-46eb-91ef-56b0a318b983"), event_id=5001, version=0)
class Microsoft_Windows_NetworkProvisioning_5001_0(Etw):
    pattern = Struct(
        "ActivationMethod" / Int32ul,
        "CarrierId" / WString,
        "SubscriberId" / WString,
        "Params" / WString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("93a19ab3-fb2c-46eb-91ef-56b0a318b983"), event_id=5002, version=0)
class Microsoft_Windows_NetworkProvisioning_5002_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid
    )


@declare(guid=guid("93a19ab3-fb2c-46eb-91ef-56b0a318b983"), event_id=5003, version=0)
class Microsoft_Windows_NetworkProvisioning_5003_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "RadioState" / Int32ul,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("93a19ab3-fb2c-46eb-91ef-56b0a318b983"), event_id=5004, version=0)
class Microsoft_Windows_NetworkProvisioning_5004_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "RegisterState" / Int32ul
    )


@declare(guid=guid("93a19ab3-fb2c-46eb-91ef-56b0a318b983"), event_id=5005, version=0)
class Microsoft_Windows_NetworkProvisioning_5005_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "ProfileType" / Int32ul,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("93a19ab3-fb2c-46eb-91ef-56b0a318b983"), event_id=5006, version=0)
class Microsoft_Windows_NetworkProvisioning_5006_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "ProfileName" / WString,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("93a19ab3-fb2c-46eb-91ef-56b0a318b983"), event_id=5007, version=0)
class Microsoft_Windows_NetworkProvisioning_5007_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("93a19ab3-fb2c-46eb-91ef-56b0a318b983"), event_id=6001, version=0)
class Microsoft_Windows_NetworkProvisioning_6001_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("93a19ab3-fb2c-46eb-91ef-56b0a318b983"), event_id=6002, version=0)
class Microsoft_Windows_NetworkProvisioning_6002_0(Etw):
    pattern = Struct(
        "CarrierId" / WString,
        "SubscriberId" / WString,
        "AppId" / WString
    )


@declare(guid=guid("93a19ab3-fb2c-46eb-91ef-56b0a318b983"), event_id=9000, version=0)
class Microsoft_Windows_NetworkProvisioning_9000_0(Etw):
    pattern = Struct(
        "HandlerName" / WString
    )


@declare(guid=guid("93a19ab3-fb2c-46eb-91ef-56b0a318b983"), event_id=9001, version=0)
class Microsoft_Windows_NetworkProvisioning_9001_0(Etw):
    pattern = Struct(
        "HandlerName" / WString,
        "ErrorCode" / Int32sl,
        "HasResults" / Int8ul
    )


@declare(guid=guid("93a19ab3-fb2c-46eb-91ef-56b0a318b983"), event_id=9100, version=0)
class Microsoft_Windows_NetworkProvisioning_9100_0(Etw):
    pattern = Struct(
        "HandlerName" / WString
    )


@declare(guid=guid("93a19ab3-fb2c-46eb-91ef-56b0a318b983"), event_id=9101, version=0)
class Microsoft_Windows_NetworkProvisioning_9101_0(Etw):
    pattern = Struct(
        "HandlerName" / WString
    )


@declare(guid=guid("93a19ab3-fb2c-46eb-91ef-56b0a318b983"), event_id=10000, version=0)
class Microsoft_Windows_NetworkProvisioning_10000_0(Etw):
    pattern = Struct(
        "ServiceName" / Int32ul,
        "ErrorCode" / Int32sl
    )


@declare(guid=guid("93a19ab3-fb2c-46eb-91ef-56b0a318b983"), event_id=10001, version=0)
class Microsoft_Windows_NetworkProvisioning_10001_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "ProfileName" / WString,
        "ErrorCode" / Int32sl,
        "ReasonCode" / Int32ul
    )


@declare(guid=guid("93a19ab3-fb2c-46eb-91ef-56b0a318b983"), event_id=10002, version=0)
class Microsoft_Windows_NetworkProvisioning_10002_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "ProfileName" / WString,
        "ErrorCode" / Int32sl,
        "ReasonCode" / Int32ul
    )


@declare(guid=guid("93a19ab3-fb2c-46eb-91ef-56b0a318b983"), event_id=10003, version=0)
class Microsoft_Windows_NetworkProvisioning_10003_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "ProfileName" / WString,
        "ErrorCode" / Int32sl,
        "Parameter" / Int32ul
    )


@declare(guid=guid("93a19ab3-fb2c-46eb-91ef-56b0a318b983"), event_id=11000, version=0)
class Microsoft_Windows_NetworkProvisioning_11000_0(Etw):
    pattern = Struct(
        "Position" / Int64ul,
        "RulesXml" / WString,
        "Reason" / WString
    )


@declare(guid=guid("93a19ab3-fb2c-46eb-91ef-56b0a318b983"), event_id=20000, version=0)
class Microsoft_Windows_NetworkProvisioning_20000_0(Etw):
    pattern = Struct(
        "CallerAppId" / WString,
        "ErrorCode" / Int32sl
    )

