# -*- coding: utf-8 -*-
"""
Microsoft-Windows-NlaSvc
GUID : 63b530f8-29c9-4880-a5b4-b8179096e7b8
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("63b530f8-29c9-4880-a5b4-b8179096e7b8"), event_id=4001, version=0)
class Microsoft_Windows_NlaSvc_4001_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "CurrentOrNextState" / Int8ul
    )


@declare(guid=guid("63b530f8-29c9-4880-a5b4-b8179096e7b8"), event_id=4002, version=0)
class Microsoft_Windows_NlaSvc_4002_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "CurrentOrNextState" / Int8ul
    )


@declare(guid=guid("63b530f8-29c9-4880-a5b4-b8179096e7b8"), event_id=4101, version=0)
class Microsoft_Windows_NlaSvc_4101_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "AdapterName" / WString
    )


@declare(guid=guid("63b530f8-29c9-4880-a5b4-b8179096e7b8"), event_id=4102, version=0)
class Microsoft_Windows_NlaSvc_4102_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "AdapterName" / WString
    )


@declare(guid=guid("63b530f8-29c9-4880-a5b4-b8179096e7b8"), event_id=4103, version=0)
class Microsoft_Windows_NlaSvc_4103_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "MibNotificationType" / Int32ul
    )


@declare(guid=guid("63b530f8-29c9-4880-a5b4-b8179096e7b8"), event_id=4104, version=0)
class Microsoft_Windows_NlaSvc_4104_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "MibNotificationType" / Int32ul
    )


@declare(guid=guid("63b530f8-29c9-4880-a5b4-b8179096e7b8"), event_id=4203, version=0)
class Microsoft_Windows_NlaSvc_4203_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "GatewayIpAddress" / WString
    )


@declare(guid=guid("63b530f8-29c9-4880-a5b4-b8179096e7b8"), event_id=4204, version=0)
class Microsoft_Windows_NlaSvc_4204_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "GatewayIpAddress" / WString,
        "ErrorCode" / Int32ul,
        "NlnsState" / Int32ul,
        "MacAddrLen" / Int16ul,
        "MacAddr" / Bytes(lambda this: this.MacAddrLen)
    )


@declare(guid=guid("63b530f8-29c9-4880-a5b4-b8179096e7b8"), event_id=4205, version=0)
class Microsoft_Windows_NlaSvc_4205_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "GatewayIpAddress" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("63b530f8-29c9-4880-a5b4-b8179096e7b8"), event_id=4251, version=0)
class Microsoft_Windows_NlaSvc_4251_0(Etw):
    pattern = Struct(
        "PluginName" / WString,
        "EntityName" / WString,
        "IndicatedRowCount" / Int16ul,
        "RowsWithInterfacesIndicatedCount" / Int16ul,
        "RowInterfaceGuid" / Guid
    )


@declare(guid=guid("63b530f8-29c9-4880-a5b4-b8179096e7b8"), event_id=4261, version=0)
class Microsoft_Windows_NlaSvc_4261_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "NlaState" / Int32ul
    )


@declare(guid=guid("63b530f8-29c9-4880-a5b4-b8179096e7b8"), event_id=4311, version=0)
class Microsoft_Windows_NlaSvc_4311_0(Etw):
    pattern = Struct(
        "DnsSuffix" / WString,
        "Flags" / Int32ul,
        "ErrorCode" / Int32ul,
        "RetrievedDomain" / WString,
        "RetrievedForest" / WString
    )


@declare(guid=guid("63b530f8-29c9-4880-a5b4-b8179096e7b8"), event_id=4312, version=0)
class Microsoft_Windows_NlaSvc_4312_0(Etw):
    pattern = Struct(
        "DnsSuffix" / WString,
        "Flags" / Int32ul,
        "ErrorCode" / Int32ul,
        "RetrievedDomain" / WString,
        "RetrievedForest" / WString
    )


@declare(guid=guid("63b530f8-29c9-4880-a5b4-b8179096e7b8"), event_id=4313, version=0)
class Microsoft_Windows_NlaSvc_4313_0(Etw):
    pattern = Struct(
        "DnsSuffix" / WString,
        "Flags" / Int32ul,
        "ErrorCode" / Int32ul,
        "RetrievedDomain" / WString,
        "RetrievedForest" / WString
    )


@declare(guid=guid("63b530f8-29c9-4880-a5b4-b8179096e7b8"), event_id=4321, version=0)
class Microsoft_Windows_NlaSvc_4321_0(Etw):
    pattern = Struct(
        "DnsSuffix" / WString,
        "Flags" / Int32ul,
        "ErrorCode" / Int32ul,
        "RetrievedDomain" / WString,
        "RetrievedForest" / WString
    )


@declare(guid=guid("63b530f8-29c9-4880-a5b4-b8179096e7b8"), event_id=4322, version=0)
class Microsoft_Windows_NlaSvc_4322_0(Etw):
    pattern = Struct(
        "DnsSuffix" / WString,
        "Flags" / Int32ul,
        "ErrorCode" / Int32ul,
        "RetrievedDomain" / WString,
        "RetrievedForest" / WString
    )


@declare(guid=guid("63b530f8-29c9-4880-a5b4-b8179096e7b8"), event_id=4323, version=0)
class Microsoft_Windows_NlaSvc_4323_0(Etw):
    pattern = Struct(
        "DnsSuffix" / WString,
        "Flags" / Int32ul,
        "ErrorCode" / Int32ul,
        "RetrievedDomain" / WString,
        "RetrievedForest" / WString
    )


@declare(guid=guid("63b530f8-29c9-4880-a5b4-b8179096e7b8"), event_id=4331, version=0)
class Microsoft_Windows_NlaSvc_4331_0(Etw):
    pattern = Struct(
        "DnsSuffix" / WString,
        "Flags" / Int32ul,
        "ErrorCode" / Int32ul,
        "RetrievedDomain" / WString,
        "RetrievedForest" / WString
    )


@declare(guid=guid("63b530f8-29c9-4880-a5b4-b8179096e7b8"), event_id=4332, version=0)
class Microsoft_Windows_NlaSvc_4332_0(Etw):
    pattern = Struct(
        "DnsSuffix" / WString,
        "Flags" / Int32ul,
        "ErrorCode" / Int32ul,
        "RetrievedDomain" / WString,
        "RetrievedForest" / WString
    )


@declare(guid=guid("63b530f8-29c9-4880-a5b4-b8179096e7b8"), event_id=4333, version=0)
class Microsoft_Windows_NlaSvc_4333_0(Etw):
    pattern = Struct(
        "DnsSuffix" / WString,
        "Flags" / Int32ul,
        "ErrorCode" / Int32ul,
        "RetrievedDomain" / WString,
        "RetrievedForest" / WString
    )


@declare(guid=guid("63b530f8-29c9-4880-a5b4-b8179096e7b8"), event_id=4341, version=0)
class Microsoft_Windows_NlaSvc_4341_0(Etw):
    pattern = Struct(
        "InterfaceName" / WString,
        "Addresses" / WString,
        "TryCount" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("63b530f8-29c9-4880-a5b4-b8179096e7b8"), event_id=4342, version=0)
class Microsoft_Windows_NlaSvc_4342_0(Etw):
    pattern = Struct(
        "InterfaceName" / WString,
        "Addresses" / WString,
        "TryCount" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("63b530f8-29c9-4880-a5b4-b8179096e7b8"), event_id=4343, version=0)
class Microsoft_Windows_NlaSvc_4343_0(Etw):
    pattern = Struct(
        "InterfaceName" / WString,
        "Addresses" / WString,
        "TryCount" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("63b530f8-29c9-4880-a5b4-b8179096e7b8"), event_id=4351, version=0)
class Microsoft_Windows_NlaSvc_4351_0(Etw):
    pattern = Struct(
        "Addresses" / WString,
        "DcName" / WString,
        "TryNumber" / Int32ul,
        "TryCount" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("63b530f8-29c9-4880-a5b4-b8179096e7b8"), event_id=4352, version=0)
class Microsoft_Windows_NlaSvc_4352_0(Etw):
    pattern = Struct(
        "Addresses" / WString,
        "DcName" / WString,
        "TryNumber" / Int32ul,
        "TryCount" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("63b530f8-29c9-4880-a5b4-b8179096e7b8"), event_id=4353, version=0)
class Microsoft_Windows_NlaSvc_4353_0(Etw):
    pattern = Struct(
        "Addresses" / WString,
        "DcName" / WString,
        "TryNumber" / Int32ul,
        "TryCount" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("63b530f8-29c9-4880-a5b4-b8179096e7b8"), event_id=4354, version=0)
class Microsoft_Windows_NlaSvc_4354_0(Etw):
    pattern = Struct(
        "Addresses" / WString,
        "DcName" / WString,
        "TryNumber" / Int32ul,
        "TryCount" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("63b530f8-29c9-4880-a5b4-b8179096e7b8"), event_id=4355, version=0)
class Microsoft_Windows_NlaSvc_4355_0(Etw):
    pattern = Struct(
        "Addresses" / WString,
        "DcName" / WString,
        "TryNumber" / Int32ul,
        "TryCount" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("63b530f8-29c9-4880-a5b4-b8179096e7b8"), event_id=4356, version=0)
class Microsoft_Windows_NlaSvc_4356_0(Etw):
    pattern = Struct(
        "Addresses" / WString,
        "DcName" / WString,
        "TryNumber" / Int32ul,
        "TryCount" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("63b530f8-29c9-4880-a5b4-b8179096e7b8"), event_id=4401, version=0)
class Microsoft_Windows_NlaSvc_4401_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "SignatureLength" / Int16ul,
        "Signature" / Bytes(lambda this: this.SignatureLength),
        "SignatureSource" / Int32ul
    )


@declare(guid=guid("63b530f8-29c9-4880-a5b4-b8179096e7b8"), event_id=4402, version=0)
class Microsoft_Windows_NlaSvc_4402_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "SignatureLength" / Int16ul,
        "Signature" / Bytes(lambda this: this.SignatureLength),
        "SignatureSource" / Int32ul
    )


@declare(guid=guid("63b530f8-29c9-4880-a5b4-b8179096e7b8"), event_id=4403, version=0)
class Microsoft_Windows_NlaSvc_4403_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "SignatureLength" / Int16ul,
        "Signature" / Bytes(lambda this: this.SignatureLength),
        "SignatureSource" / Int32ul
    )


@declare(guid=guid("63b530f8-29c9-4880-a5b4-b8179096e7b8"), event_id=4404, version=0)
class Microsoft_Windows_NlaSvc_4404_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "SignatureLength" / Int16ul,
        "Signature" / Bytes(lambda this: this.SignatureLength),
        "SignatureSource" / Int32ul
    )


@declare(guid=guid("63b530f8-29c9-4880-a5b4-b8179096e7b8"), event_id=4405, version=0)
class Microsoft_Windows_NlaSvc_4405_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "SignatureLength" / Int16ul,
        "Signature" / Bytes(lambda this: this.SignatureLength),
        "SignatureSource" / Int32ul
    )


@declare(guid=guid("63b530f8-29c9-4880-a5b4-b8179096e7b8"), event_id=4407, version=0)
class Microsoft_Windows_NlaSvc_4407_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "AdapterName" / WString
    )


@declare(guid=guid("63b530f8-29c9-4880-a5b4-b8179096e7b8"), event_id=4408, version=0)
class Microsoft_Windows_NlaSvc_4408_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "AdapterName" / WString
    )


@declare(guid=guid("63b530f8-29c9-4880-a5b4-b8179096e7b8"), event_id=4409, version=0)
class Microsoft_Windows_NlaSvc_4409_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "AdapterName" / WString
    )


@declare(guid=guid("63b530f8-29c9-4880-a5b4-b8179096e7b8"), event_id=4410, version=0)
class Microsoft_Windows_NlaSvc_4410_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "SignatureLength" / Int16ul,
        "Signature" / Bytes(lambda this: this.SignatureLength),
        "SignatureSource" / Int32ul
    )


@declare(guid=guid("63b530f8-29c9-4880-a5b4-b8179096e7b8"), event_id=4411, version=0)
class Microsoft_Windows_NlaSvc_4411_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "SignatureLength" / Int16ul,
        "Signature" / Bytes(lambda this: this.SignatureLength),
        "SignatureSource" / Int32ul
    )


@declare(guid=guid("63b530f8-29c9-4880-a5b4-b8179096e7b8"), event_id=4451, version=0)
class Microsoft_Windows_NlaSvc_4451_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "AuthCapUnlikelyReason" / Int32ul,
        "SpeculativeTimeout" / Int32ul
    )


@declare(guid=guid("63b530f8-29c9-4880-a5b4-b8179096e7b8"), event_id=5001, version=0)
class Microsoft_Windows_NlaSvc_5001_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "NlaState" / Int32ul
    )


@declare(guid=guid("63b530f8-29c9-4880-a5b4-b8179096e7b8"), event_id=5002, version=0)
class Microsoft_Windows_NlaSvc_5002_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "SignatureSource" / Int32ul,
        "SignatureCharacteristics" / Int32ul
    )


@declare(guid=guid("63b530f8-29c9-4880-a5b4-b8179096e7b8"), event_id=6101, version=0)
class Microsoft_Windows_NlaSvc_6101_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "AdapterName" / WString
    )


@declare(guid=guid("63b530f8-29c9-4880-a5b4-b8179096e7b8"), event_id=6102, version=0)
class Microsoft_Windows_NlaSvc_6102_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "AdapterName" / WString
    )


@declare(guid=guid("63b530f8-29c9-4880-a5b4-b8179096e7b8"), event_id=6103, version=0)
class Microsoft_Windows_NlaSvc_6103_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "AdapterName" / WString
    )


@declare(guid=guid("63b530f8-29c9-4880-a5b4-b8179096e7b8"), event_id=6104, version=0)
class Microsoft_Windows_NlaSvc_6104_0(Etw):
    pattern = Struct(
        "InterfaceGuid" / Guid,
        "AdapterName" / WString
    )

