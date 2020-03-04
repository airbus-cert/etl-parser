# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Network-Connection-Broker
GUID : 3eb875eb-8f4a-4800-a00b-e484c97d7551
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("3eb875eb-8f4a-4800-a00b-e484c97d7551"), event_id=1001, version=0)
class Microsoft_Windows_Network_Connection_Broker_1001_0(Etw):
    pattern = Struct(
        "StatusDescription" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("3eb875eb-8f4a-4800-a00b-e484c97d7551"), event_id=1002, version=0)
class Microsoft_Windows_Network_Connection_Broker_1002_0(Etw):
    pattern = Struct(
        "StatusDescription" / WString,
        "RefCount" / Int32ul,
        "FileName" / CString,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3eb875eb-8f4a-4800-a00b-e484c97d7551"), event_id=1003, version=0)
class Microsoft_Windows_Network_Connection_Broker_1003_0(Etw):
    pattern = Struct(
        "StatusDescription" / WString,
        "RefCount" / Int32ul,
        "FileName" / CString,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3eb875eb-8f4a-4800-a00b-e484c97d7551"), event_id=1101, version=0)
class Microsoft_Windows_Network_Connection_Broker_1101_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("3eb875eb-8f4a-4800-a00b-e484c97d7551"), event_id=1102, version=0)
class Microsoft_Windows_Network_Connection_Broker_1102_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("3eb875eb-8f4a-4800-a00b-e484c97d7551"), event_id=1103, version=0)
class Microsoft_Windows_Network_Connection_Broker_1103_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("3eb875eb-8f4a-4800-a00b-e484c97d7551"), event_id=1104, version=0)
class Microsoft_Windows_Network_Connection_Broker_1104_0(Etw):
    pattern = Struct(
        "ContextHandle" / Int64ul,
        "Provider" / Int64ul,
        "ServiceNlmEpoch" / Int64ul,
        "ServiceNlmSignature" / Int64ul,
        "ClientNlmEpoch" / Int64ul,
        "Value" / Int32ul,
        "ValueType" / Int32sl,
        "ScheduleUpdate" / Int8ul,
        "Status" / Int32ul
    )


@declare(guid=guid("3eb875eb-8f4a-4800-a00b-e484c97d7551"), event_id=1105, version=0)
class Microsoft_Windows_Network_Connection_Broker_1105_0(Etw):
    pattern = Struct(
        "NlmEpochBefore" / Int64ul,
        "NlmSignatureBefore" / Int64ul,
        "NlmSignatureStableBefore" / Int8ul,
        "NlmEpochAfter" / Int64ul,
        "NlmSignatureAfter" / Int64ul,
        "NlmSignatureStableAfter" / Int8ul,
        "Value" / Int32ul,
        "ValueType" / Int32sl,
        "ScheduleUpdate" / Int8ul
    )


@declare(guid=guid("3eb875eb-8f4a-4800-a00b-e484c97d7551"), event_id=1106, version=0)
class Microsoft_Windows_Network_Connection_Broker_1106_0(Etw):
    pattern = Struct(
        "Provider" / Int64ul,
        "RequestHolder" / Int64ul
    )


@declare(guid=guid("3eb875eb-8f4a-4800-a00b-e484c97d7551"), event_id=1107, version=0)
class Microsoft_Windows_Network_Connection_Broker_1107_0(Etw):
    pattern = Struct(
        "ContextHandle" / Int64ul,
        "Provider" / Int64ul,
        "RequestHolder" / Int64ul,
        "UpdateRequested" / Int8ul,
        "CompleteCall" / Int8ul,
        "Status" / Int32ul
    )


@declare(guid=guid("3eb875eb-8f4a-4800-a00b-e484c97d7551"), event_id=1108, version=0)
class Microsoft_Windows_Network_Connection_Broker_1108_0(Etw):
    pattern = Struct(
        "Provider" / Int64ul,
        "RequestHolder" / Int64ul,
        "Value" / Int32ul,
        "ValueType" / Int32sl,
        "NlmEpoch" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("3eb875eb-8f4a-4800-a00b-e484c97d7551"), event_id=1109, version=0)
class Microsoft_Windows_Network_Connection_Broker_1109_0(Etw):
    pattern = Struct(
        "Provider" / Int64ul,
        "RefCount" / Int32ul,
        "FileName" / CString,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3eb875eb-8f4a-4800-a00b-e484c97d7551"), event_id=1110, version=0)
class Microsoft_Windows_Network_Connection_Broker_1110_0(Etw):
    pattern = Struct(
        "Provider" / Int64ul,
        "RefCount" / Int32ul,
        "FileName" / CString,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3eb875eb-8f4a-4800-a00b-e484c97d7551"), event_id=1111, version=0)
class Microsoft_Windows_Network_Connection_Broker_1111_0(Etw):
    pattern = Struct(
        "Provider" / Int64ul,
        "RefCount" / Int32ul,
        "FileName" / CString,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3eb875eb-8f4a-4800-a00b-e484c97d7551"), event_id=1112, version=0)
class Microsoft_Windows_Network_Connection_Broker_1112_0(Etw):
    pattern = Struct(
        "Provider" / Int64ul,
        "RefCount" / Int32ul,
        "FileName" / CString,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3eb875eb-8f4a-4800-a00b-e484c97d7551"), event_id=1113, version=0)
class Microsoft_Windows_Network_Connection_Broker_1113_0(Etw):
    pattern = Struct(
        "Description" / WString,
        "Appprovidedtime" / Int32ul,
        "Currentkeepalivetime" / Int32ul,
        "Loweredkeepalivetime" / Int32ul,
        "WNStestinputtime" / Int32ul
    )


@declare(guid=guid("3eb875eb-8f4a-4800-a00b-e484c97d7551"), event_id=1114, version=0)
class Microsoft_Windows_Network_Connection_Broker_1114_0(Etw):
    pattern = Struct(
        "LogMessage" / WString
    )


@declare(guid=guid("3eb875eb-8f4a-4800-a00b-e484c97d7551"), event_id=1115, version=0)
class Microsoft_Windows_Network_Connection_Broker_1115_0(Etw):
    pattern = Struct(
        "StatusDescription" / WString,
        "RefCount" / Int32ul,
        "FileName" / CString,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3eb875eb-8f4a-4800-a00b-e484c97d7551"), event_id=1116, version=0)
class Microsoft_Windows_Network_Connection_Broker_1116_0(Etw):
    pattern = Struct(
        "StatusDescription" / WString,
        "RefCount" / Int32ul,
        "FileName" / CString,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3eb875eb-8f4a-4800-a00b-e484c97d7551"), event_id=1117, version=0)
class Microsoft_Windows_Network_Connection_Broker_1117_0(Etw):
    pattern = Struct(
        "PackageName" / WString,
        "Fired" / Int8ul
    )


@declare(guid=guid("3eb875eb-8f4a-4800-a00b-e484c97d7551"), event_id=2001, version=0)
class Microsoft_Windows_Network_Connection_Broker_2001_0(Etw):
    pattern = Struct(
        "EventId" / Guid,
        "AppName" / WString
    )


@declare(guid=guid("3eb875eb-8f4a-4800-a00b-e484c97d7551"), event_id=2002, version=0)
class Microsoft_Windows_Network_Connection_Broker_2002_0(Etw):
    pattern = Struct(
        "EventId" / Guid,
        "AppName" / WString
    )


@declare(guid=guid("3eb875eb-8f4a-4800-a00b-e484c97d7551"), event_id=2003, version=0)
class Microsoft_Windows_Network_Connection_Broker_2003_0(Etw):
    pattern = Struct(
        "EventId" / Guid,
        "SocketId" / WString,
        "AppName" / WString,
        "AddressFamily" / Int32sl,
        "SocketType" / Int32sl,
        "Protocol" / Int32sl,
        "IsTcpListener" / Int8ul
    )


@declare(guid=guid("3eb875eb-8f4a-4800-a00b-e484c97d7551"), event_id=2004, version=0)
class Microsoft_Windows_Network_Connection_Broker_2004_0(Etw):
    pattern = Struct(
        "EventId" / Guid,
        "SocketId" / WString,
        "AppName" / WString
    )


@declare(guid=guid("3eb875eb-8f4a-4800-a00b-e484c97d7551"), event_id=2005, version=0)
class Microsoft_Windows_Network_Connection_Broker_2005_0(Etw):
    pattern = Struct(
        "BrokerEventId" / Guid,
        "AppName" / WString
    )


@declare(guid=guid("3eb875eb-8f4a-4800-a00b-e484c97d7551"), event_id=2006, version=0)
class Microsoft_Windows_Network_Connection_Broker_2006_0(Etw):
    pattern = Struct(
        "BrokerEventId" / Guid,
        "AppName" / WString,
        "CallReason" / Int32sl
    )


@declare(guid=guid("3eb875eb-8f4a-4800-a00b-e484c97d7551"), event_id=2007, version=0)
class Microsoft_Windows_Network_Connection_Broker_2007_0(Etw):
    pattern = Struct(
        "BrokerEventId" / Guid,
        "AppName" / WString,
        "CallReason" / Int32sl
    )


@declare(guid=guid("3eb875eb-8f4a-4800-a00b-e484c97d7551"), event_id=2008, version=0)
class Microsoft_Windows_Network_Connection_Broker_2008_0(Etw):
    pattern = Struct(
        "BrokerEventId" / Guid,
        "AppName" / WString,
        "CallReason" / Int32sl
    )


@declare(guid=guid("3eb875eb-8f4a-4800-a00b-e484c97d7551"), event_id=2009, version=0)
class Microsoft_Windows_Network_Connection_Broker_2009_0(Etw):
    pattern = Struct(
        "BrokerEventId" / Guid,
        "SocketId" / WString,
        "SocketType" / Int32sl,
        "TriggerReason" / Int32sl,
        "Status" / Int32sl
    )


@declare(guid=guid("3eb875eb-8f4a-4800-a00b-e484c97d7551"), event_id=2010, version=0)
class Microsoft_Windows_Network_Connection_Broker_2010_0(Etw):
    pattern = Struct(
        "BrokerEventId" / Guid,
        "Status" / Int32sl
    )


@declare(guid=guid("3eb875eb-8f4a-4800-a00b-e484c97d7551"), event_id=2011, version=0)
class Microsoft_Windows_Network_Connection_Broker_2011_0(Etw):
    pattern = Struct(
        "BrokerEventId" / Guid,
        "SocketId" / WString,
        "Status" / Int32sl
    )


@declare(guid=guid("3eb875eb-8f4a-4800-a00b-e484c97d7551"), event_id=2012, version=0)
class Microsoft_Windows_Network_Connection_Broker_2012_0(Etw):
    pattern = Struct(
        "AppName" / WString,
        "Status" / Int32sl,
        "NumSockets" / Int32sl
    )

