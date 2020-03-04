# -*- coding: utf-8 -*-
"""
Microsoft-Windows-WCN-Config-Registrar
GUID : c100becf-d33a-4a4b-bf23-bbef4663d017
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("c100becf-d33a-4a4b-bf23-bbef4663d017"), event_id=8000, version=0)
class Microsoft_Windows_WCN_Config_Registrar_8000_0(Etw):
    pattern = Struct(
        "SessionGuid" / Guid,
        "PeerUuid" / Guid,
        "Trigger" / Int32ul
    )


@declare(guid=guid("c100becf-d33a-4a4b-bf23-bbef4663d017"), event_id=8001, version=0)
class Microsoft_Windows_WCN_Config_Registrar_8001_0(Etw):
    pattern = Struct(
        "SessionGuid" / Guid
    )


@declare(guid=guid("c100becf-d33a-4a4b-bf23-bbef4663d017"), event_id=8003, version=0)
class Microsoft_Windows_WCN_Config_Registrar_8003_0(Etw):
    pattern = Struct(
        "SessionGuid" / Guid,
        "MessageGuid" / Guid,
        "MessageBlobLength" / Int16ul,
        "MessageBlob" / Bytes(lambda this: this.MessageBlobLength)
    )


@declare(guid=guid("c100becf-d33a-4a4b-bf23-bbef4663d017"), event_id=8004, version=0)
class Microsoft_Windows_WCN_Config_Registrar_8004_0(Etw):
    pattern = Struct(
        "SessionGuid" / Guid,
        "MessageGuid" / Guid,
        "MessageBlobLength" / Int16ul,
        "MessageBlob" / Bytes(lambda this: this.MessageBlobLength)
    )


@declare(guid=guid("c100becf-d33a-4a4b-bf23-bbef4663d017"), event_id=8010, version=0)
class Microsoft_Windows_WCN_Config_Registrar_8010_0(Etw):
    pattern = Struct(
        "SessionGuid" / Guid
    )


@declare(guid=guid("c100becf-d33a-4a4b-bf23-bbef4663d017"), event_id=8011, version=0)
class Microsoft_Windows_WCN_Config_Registrar_8011_0(Etw):
    pattern = Struct(
        "SessionGuid" / Guid,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("c100becf-d33a-4a4b-bf23-bbef4663d017"), event_id=8020, version=0)
class Microsoft_Windows_WCN_Config_Registrar_8020_0(Etw):
    pattern = Struct(
        "Transport" / WString,
        "TransportSubType" / WString,
        "MessageGuid" / Guid,
        "MessageBlobLength" / Int16ul,
        "MessageBlob" / Bytes(lambda this: this.MessageBlobLength)
    )


@declare(guid=guid("c100becf-d33a-4a4b-bf23-bbef4663d017"), event_id=8021, version=0)
class Microsoft_Windows_WCN_Config_Registrar_8021_0(Etw):
    pattern = Struct(
        "Transport" / WString,
        "TransportSubType" / WString,
        "MessageGuid" / Guid,
        "MessageBlobLength" / Int16ul,
        "MessageBlob" / Bytes(lambda this: this.MessageBlobLength)
    )


@declare(guid=guid("c100becf-d33a-4a4b-bf23-bbef4663d017"), event_id=8030, version=0)
class Microsoft_Windows_WCN_Config_Registrar_8030_0(Etw):
    pattern = Struct(
        "Transport" / WString,
        "MessageBlobLength" / Int16ul,
        "MessageBlob" / Bytes(lambda this: this.MessageBlobLength)
    )


@declare(guid=guid("c100becf-d33a-4a4b-bf23-bbef4663d017"), event_id=8031, version=0)
class Microsoft_Windows_WCN_Config_Registrar_8031_0(Etw):
    pattern = Struct(
        "Transport" / WString,
        "MessageBlobLength" / Int16ul,
        "MessageBlob" / Bytes(lambda this: this.MessageBlobLength)
    )

