# -*- coding: utf-8 -*-
"""
Microsoft-Windows-SMBDirect
GUID : db66ea65-b7bb-4ca9-8748-334cb5c32400
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("db66ea65-b7bb-4ca9-8748-334cb5c32400"), event_id=1, version=1)
class Microsoft_Windows_SMBDirect_1_1(Etw):
    pattern = Struct(
        "AdapterAlias" / WString,
        "RequiredSges" / Int32ul,
        "AdapterSupportedSges" / Int32ul
    )


@declare(guid=guid("db66ea65-b7bb-4ca9-8748-334cb5c32400"), event_id=2, version=1)
class Microsoft_Windows_SMBDirect_2_1(Etw):
    pattern = Struct(
        "AdapterAlias" / WString,
        "RequiredSges" / Int32ul,
        "AdapterSupportedSges" / Int32ul
    )


@declare(guid=guid("db66ea65-b7bb-4ca9-8748-334cb5c32400"), event_id=3, version=1)
class Microsoft_Windows_SMBDirect_3_1(Etw):
    pattern = Struct(
        "AdapterAlias" / WString,
        "RequiredSges" / Int32ul,
        "AdapterSupportedSges" / Int32ul
    )


@declare(guid=guid("db66ea65-b7bb-4ca9-8748-334cb5c32400"), event_id=4, version=1)
class Microsoft_Windows_SMBDirect_4_1(Etw):
    pattern = Struct(
        "RegistryKeyName" / WString,
        "SettingName" / WString,
        "MinValidValue" / Int32ul,
        "MaxValidValue" / Int32ul,
        "DefaultValue" / Int32ul
    )


@declare(guid=guid("db66ea65-b7bb-4ca9-8748-334cb5c32400"), event_id=5, version=1)
class Microsoft_Windows_SMBDirect_5_1(Etw):
    pattern = Struct(
        "AdapterAlias" / WString,
        "RegistryKeyName" / WString,
        "SettingName" / WString,
        "Value" / Int32ul,
        "ClosestAdapterSupportedValue" / Int32ul
    )


@declare(guid=guid("db66ea65-b7bb-4ca9-8748-334cb5c32400"), event_id=6, version=1)
class Microsoft_Windows_SMBDirect_6_1(Etw):
    pattern = Struct(
        "SocketID" / Guid,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "AdapterAlias" / WString,
        "TimeoutInMs" / Int32ul
    )


@declare(guid=guid("db66ea65-b7bb-4ca9-8748-334cb5c32400"), event_id=7, version=1)
class Microsoft_Windows_SMBDirect_7_1(Etw):
    pattern = Struct(
        "BaseAffinityNode" / Int32ul,
        "MaxAffinityNode" / Int32ul
    )


@declare(guid=guid("db66ea65-b7bb-4ca9-8748-334cb5c32400"), event_id=300, version=1)
class Microsoft_Windows_SMBDirect_300_1(Etw):
    pattern = Struct(
        "SocketID" / Guid,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength)
    )


@declare(guid=guid("db66ea65-b7bb-4ca9-8748-334cb5c32400"), event_id=301, version=1)
class Microsoft_Windows_SMBDirect_301_1(Etw):
    pattern = Struct(
        "SocketID" / Guid,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength)
    )


@declare(guid=guid("db66ea65-b7bb-4ca9-8748-334cb5c32400"), event_id=302, version=1)
class Microsoft_Windows_SMBDirect_302_1(Etw):
    pattern = Struct(
        "SocketID" / Guid,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "Status" / Int32ul
    )


@declare(guid=guid("db66ea65-b7bb-4ca9-8748-334cb5c32400"), event_id=303, version=1)
class Microsoft_Windows_SMBDirect_303_1(Etw):
    pattern = Struct(
        "SocketID" / Guid,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength)
    )


@declare(guid=guid("db66ea65-b7bb-4ca9-8748-334cb5c32400"), event_id=304, version=1)
class Microsoft_Windows_SMBDirect_304_1(Etw):
    pattern = Struct(
        "SocketID" / Guid,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "Status" / Int32ul
    )


@declare(guid=guid("db66ea65-b7bb-4ca9-8748-334cb5c32400"), event_id=305, version=1)
class Microsoft_Windows_SMBDirect_305_1(Etw):
    pattern = Struct(
        "SocketID" / Guid,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "Status" / Int32ul
    )


@declare(guid=guid("db66ea65-b7bb-4ca9-8748-334cb5c32400"), event_id=306, version=1)
class Microsoft_Windows_SMBDirect_306_1(Etw):
    pattern = Struct(
        "SocketID" / Guid,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "MinVersion" / Int16ul,
        "MaxVersion" / Int16ul,
        "PeerMinVersion" / Int16ul,
        "PeerMaxVersion" / Int16ul
    )


@declare(guid=guid("db66ea65-b7bb-4ca9-8748-334cb5c32400"), event_id=350, version=1)
class Microsoft_Windows_SMBDirect_350_1(Etw):
    pattern = Struct(
        "ListenSocketID" / Guid,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength)
    )


@declare(guid=guid("db66ea65-b7bb-4ca9-8748-334cb5c32400"), event_id=351, version=1)
class Microsoft_Windows_SMBDirect_351_1(Etw):
    pattern = Struct(
        "ListenSocketID" / Guid,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength)
    )


@declare(guid=guid("db66ea65-b7bb-4ca9-8748-334cb5c32400"), event_id=352, version=1)
class Microsoft_Windows_SMBDirect_352_1(Etw):
    pattern = Struct(
        "ListenSocketID" / Guid,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength)
    )


@declare(guid=guid("db66ea65-b7bb-4ca9-8748-334cb5c32400"), event_id=353, version=1)
class Microsoft_Windows_SMBDirect_353_1(Etw):
    pattern = Struct(
        "SocketID" / Guid,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength)
    )


@declare(guid=guid("db66ea65-b7bb-4ca9-8748-334cb5c32400"), event_id=354, version=1)
class Microsoft_Windows_SMBDirect_354_1(Etw):
    pattern = Struct(
        "SocketID" / Guid,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "Status" / Int32ul
    )


@declare(guid=guid("db66ea65-b7bb-4ca9-8748-334cb5c32400"), event_id=355, version=1)
class Microsoft_Windows_SMBDirect_355_1(Etw):
    pattern = Struct(
        "SocketID" / Guid,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength)
    )


@declare(guid=guid("db66ea65-b7bb-4ca9-8748-334cb5c32400"), event_id=356, version=1)
class Microsoft_Windows_SMBDirect_356_1(Etw):
    pattern = Struct(
        "SocketID" / Guid,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength)
    )


@declare(guid=guid("db66ea65-b7bb-4ca9-8748-334cb5c32400"), event_id=357, version=1)
class Microsoft_Windows_SMBDirect_357_1(Etw):
    pattern = Struct(
        "SocketID" / Guid,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "Status" / Int32ul
    )


@declare(guid=guid("db66ea65-b7bb-4ca9-8748-334cb5c32400"), event_id=358, version=1)
class Microsoft_Windows_SMBDirect_358_1(Etw):
    pattern = Struct(
        "SocketID" / Guid,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "Status" / Int32ul
    )


@declare(guid=guid("db66ea65-b7bb-4ca9-8748-334cb5c32400"), event_id=400, version=1)
class Microsoft_Windows_SMBDirect_400_1(Etw):
    pattern = Struct(
        "SocketID" / Guid,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength)
    )


@declare(guid=guid("db66ea65-b7bb-4ca9-8748-334cb5c32400"), event_id=401, version=2)
class Microsoft_Windows_SMBDirect_401_2(Etw):
    pattern = Struct(
        "SocketID" / Guid,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "SocketState" / Int32ul
    )


@declare(guid=guid("db66ea65-b7bb-4ca9-8748-334cb5c32400"), event_id=402, version=2)
class Microsoft_Windows_SMBDirect_402_2(Etw):
    pattern = Struct(
        "SocketID" / Guid,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength)
    )


@declare(guid=guid("db66ea65-b7bb-4ca9-8748-334cb5c32400"), event_id=403, version=1)
class Microsoft_Windows_SMBDirect_403_1(Etw):
    pattern = Struct(
        "SocketID" / Guid,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength)
    )


@declare(guid=guid("db66ea65-b7bb-4ca9-8748-334cb5c32400"), event_id=404, version=1)
class Microsoft_Windows_SMBDirect_404_1(Etw):
    pattern = Struct(
        "SocketID" / Guid
    )


@declare(guid=guid("db66ea65-b7bb-4ca9-8748-334cb5c32400"), event_id=450, version=1)
class Microsoft_Windows_SMBDirect_450_1(Etw):
    pattern = Struct(
        "SocketID" / Guid,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength)
    )


@declare(guid=guid("db66ea65-b7bb-4ca9-8748-334cb5c32400"), event_id=451, version=1)
class Microsoft_Windows_SMBDirect_451_1(Etw):
    pattern = Struct(
        "SocketID" / Guid,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength)
    )


@declare(guid=guid("db66ea65-b7bb-4ca9-8748-334cb5c32400"), event_id=452, version=1)
class Microsoft_Windows_SMBDirect_452_1(Etw):
    pattern = Struct(
        "SocketID" / Guid,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength)
    )


@declare(guid=guid("db66ea65-b7bb-4ca9-8748-334cb5c32400"), event_id=453, version=1)
class Microsoft_Windows_SMBDirect_453_1(Etw):
    pattern = Struct(
        "SocketID" / Guid,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength)
    )


@declare(guid=guid("db66ea65-b7bb-4ca9-8748-334cb5c32400"), event_id=454, version=1)
class Microsoft_Windows_SMBDirect_454_1(Etw):
    pattern = Struct(
        "SocketID" / Guid,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength)
    )


@declare(guid=guid("db66ea65-b7bb-4ca9-8748-334cb5c32400"), event_id=455, version=1)
class Microsoft_Windows_SMBDirect_455_1(Etw):
    pattern = Struct(
        "SocketID" / Guid,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength)
    )


@declare(guid=guid("db66ea65-b7bb-4ca9-8748-334cb5c32400"), event_id=456, version=1)
class Microsoft_Windows_SMBDirect_456_1(Etw):
    pattern = Struct(
        "SocketID" / Guid,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "PeerSendCreditsGranted" / Int32ul,
        "PeerSendCredits" / Int32ul
    )


@declare(guid=guid("db66ea65-b7bb-4ca9-8748-334cb5c32400"), event_id=457, version=1)
class Microsoft_Windows_SMBDirect_457_1(Etw):
    pattern = Struct(
        "SocketID" / Guid,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "SendCreditsReceived" / Int32ul,
        "SendCreditsAccepted" / Int32ul,
        "SendCredits" / Int32ul
    )


@declare(guid=guid("db66ea65-b7bb-4ca9-8748-334cb5c32400"), event_id=500, version=1)
class Microsoft_Windows_SMBDirect_500_1(Etw):
    pattern = Struct(
        "SocketID" / Guid,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "Type" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("db66ea65-b7bb-4ca9-8748-334cb5c32400"), event_id=501, version=1)
class Microsoft_Windows_SMBDirect_501_1(Etw):
    pattern = Struct(
        "SocketID" / Guid,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "Type" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("db66ea65-b7bb-4ca9-8748-334cb5c32400"), event_id=502, version=1)
class Microsoft_Windows_SMBDirect_502_1(Etw):
    pattern = Struct(
        "SocketID" / Guid,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "Status" / Int32ul
    )


@declare(guid=guid("db66ea65-b7bb-4ca9-8748-334cb5c32400"), event_id=503, version=1)
class Microsoft_Windows_SMBDirect_503_1(Etw):
    pattern = Struct(
        "SocketID" / Guid,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "Status" / Int32ul
    )


@declare(guid=guid("db66ea65-b7bb-4ca9-8748-334cb5c32400"), event_id=1000, version=1)
class Microsoft_Windows_SMBDirect_1000_1(Etw):
    pattern = Struct(
        "SocketID" / Guid,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength)
    )


@declare(guid=guid("db66ea65-b7bb-4ca9-8748-334cb5c32400"), event_id=1001, version=1)
class Microsoft_Windows_SMBDirect_1001_1(Etw):
    pattern = Struct(
        "SocketID" / Guid,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength)
    )


@declare(guid=guid("db66ea65-b7bb-4ca9-8748-334cb5c32400"), event_id=1002, version=1)
class Microsoft_Windows_SMBDirect_1002_1(Etw):
    pattern = Struct(
        "SocketID" / Guid,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength)
    )


@declare(guid=guid("db66ea65-b7bb-4ca9-8748-334cb5c32400"), event_id=1003, version=1)
class Microsoft_Windows_SMBDirect_1003_1(Etw):
    pattern = Struct(
        "SocketID" / Guid,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength)
    )


@declare(guid=guid("db66ea65-b7bb-4ca9-8748-334cb5c32400"), event_id=1004, version=1)
class Microsoft_Windows_SMBDirect_1004_1(Etw):
    pattern = Struct(
        "SocketID" / Guid,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength)
    )


@declare(guid=guid("db66ea65-b7bb-4ca9-8748-334cb5c32400"), event_id=1005, version=1)
class Microsoft_Windows_SMBDirect_1005_1(Etw):
    pattern = Struct(
        "SocketID" / Guid,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "Type" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("db66ea65-b7bb-4ca9-8748-334cb5c32400"), event_id=1006, version=1)
class Microsoft_Windows_SMBDirect_1006_1(Etw):
    pattern = Struct(
        "SocketID" / Guid
    )


@declare(guid=guid("db66ea65-b7bb-4ca9-8748-334cb5c32400"), event_id=1007, version=1)
class Microsoft_Windows_SMBDirect_1007_1(Etw):
    pattern = Struct(
        "SocketID" / Guid,
        "Status" / Int32ul
    )


@declare(guid=guid("db66ea65-b7bb-4ca9-8748-334cb5c32400"), event_id=1008, version=1)
class Microsoft_Windows_SMBDirect_1008_1(Etw):
    pattern = Struct(
        "SocketID" / Guid,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "ProtocolVersion" / Int16ul,
        "MaxReadWriteSize" / Int32ul,
        "MaxReceiveSize" / Int32ul,
        "MaxFragmentedReceiveSize" / Int32ul,
        "MaxSendSize" / Int32ul,
        "MaxFragmentedSendSize" / Int32ul,
        "InboundReadDepth" / Int32ul,
        "OutboundReadDepth" / Int32ul
    )


@declare(guid=guid("db66ea65-b7bb-4ca9-8748-334cb5c32400"), event_id=1009, version=1)
class Microsoft_Windows_SMBDirect_1009_1(Etw):
    pattern = Struct(
        "SocketID" / Guid,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "Status" / Int32ul
    )


@declare(guid=guid("db66ea65-b7bb-4ca9-8748-334cb5c32400"), event_id=1010, version=1)
class Microsoft_Windows_SMBDirect_1010_1(Etw):
    pattern = Struct(
        "SocketID" / Guid,
        "Count" / Int32ul,
        "IntervalInMicroSeconds" / Int32ul
    )


@declare(guid=guid("db66ea65-b7bb-4ca9-8748-334cb5c32400"), event_id=1011, version=1)
class Microsoft_Windows_SMBDirect_1011_1(Etw):
    pattern = Struct(
        "SocketID" / Guid,
        "Count" / Int32ul,
        "IntervalInMicroSeconds" / Int32ul
    )


@declare(guid=guid("db66ea65-b7bb-4ca9-8748-334cb5c32400"), event_id=9500, version=1)
class Microsoft_Windows_SMBDirect_9500_1(Etw):
    pattern = Struct(
        "AdapterAlias" / WString,
        "NdkMajorVer" / Int16ul,
        "NdkMinorVer" / Int16ul,
        "VendorId" / Int32ul,
        "DeviceId" / Int32ul,
        "MaxRegistrationSize" / Int64ul,
        "MaxWindowSize" / Int64ul,
        "FrmrPageCount" / Int32ul,
        "MaxInitiatorRequestSge" / Int32ul,
        "MaxReceiveRequestSge" / Int32ul,
        "MaxReadRequestSge" / Int32ul,
        "MaxTransferLength" / Int32ul,
        "MaxInlineDataSize" / Int32ul,
        "MaxInboundReadLimit" / Int32ul,
        "MaxOutboundReadLimit" / Int32ul,
        "MaxReceiveQueueDepth" / Int32ul,
        "MaxInitiatorQueueDepth" / Int32ul,
        "MaxSrqDepth" / Int32ul,
        "MaxCqDepth" / Int32ul,
        "LargeRequestThreshold" / Int32ul,
        "MaxCallerData" / Int32ul,
        "MaxCalleeData" / Int32ul,
        "AdapterFlags" / Int32ul
    )


@declare(guid=guid("db66ea65-b7bb-4ca9-8748-334cb5c32400"), event_id=10000, version=1)
class Microsoft_Windows_SMBDirect_10000_1(Etw):
    pattern = Struct(
        "SocketID" / Guid,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "MinVersion" / Int16ul,
        "MaxVersion" / Int16ul,
        "Reserved" / Int16ul,
        "CreditsRequested" / Int16ul,
        "PreferredSendSize" / Int32ul,
        "MaxReceiveSize" / Int32ul,
        "MaxFragmentReassemblyBufferSize" / Int32ul
    )


@declare(guid=guid("db66ea65-b7bb-4ca9-8748-334cb5c32400"), event_id=10001, version=1)
class Microsoft_Windows_SMBDirect_10001_1(Etw):
    pattern = Struct(
        "SocketID" / Guid,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "MinVersion" / Int16ul,
        "MaxVersion" / Int16ul,
        "Reserved" / Int16ul,
        "CreditsRequested" / Int16ul,
        "PreferredSendSize" / Int32ul,
        "MaxReceiveSize" / Int32ul,
        "MaxFragmentReassemblyBufferSize" / Int32ul
    )


@declare(guid=guid("db66ea65-b7bb-4ca9-8748-334cb5c32400"), event_id=10002, version=1)
class Microsoft_Windows_SMBDirect_10002_1(Etw):
    pattern = Struct(
        "SocketID" / Guid,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "MinVersion" / Int16ul,
        "MaxVersion" / Int16ul,
        "NegotiatedVersion" / Int16ul,
        "Reserved" / Int16ul,
        "CreditsRequested" / Int16ul,
        "CreditsGranted" / Int16ul,
        "Status" / Int32ul,
        "MaxReadWriteSize" / Int32ul,
        "PreferredSendSize" / Int32ul,
        "MaxReceiveSize" / Int32ul,
        "MaxFragmentReassemblyBufferSize" / Int32ul
    )


@declare(guid=guid("db66ea65-b7bb-4ca9-8748-334cb5c32400"), event_id=10003, version=1)
class Microsoft_Windows_SMBDirect_10003_1(Etw):
    pattern = Struct(
        "SocketID" / Guid,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "MinVersion" / Int16ul,
        "MaxVersion" / Int16ul,
        "NegotiatedVersion" / Int16ul,
        "Reserved" / Int16ul,
        "CreditsRequested" / Int16ul,
        "CreditsGranted" / Int16ul,
        "Status" / Int32ul,
        "MaxReadWriteSize" / Int32ul,
        "PreferredSendSize" / Int32ul,
        "MaxReceiveSize" / Int32ul,
        "MaxFragmentReassemblyBufferSize" / Int32ul
    )


@declare(guid=guid("db66ea65-b7bb-4ca9-8748-334cb5c32400"), event_id=10004, version=1)
class Microsoft_Windows_SMBDirect_10004_1(Etw):
    pattern = Struct(
        "SocketID" / Guid,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "CreditsRequested" / Int16ul,
        "CreditsGranted" / Int16ul,
        "Flags" / Int16ul,
        "Reserved" / Int16ul,
        "RemainingDataLength" / Int32ul,
        "DataOffset" / Int32ul,
        "DataLength" / Int32ul
    )


@declare(guid=guid("db66ea65-b7bb-4ca9-8748-334cb5c32400"), event_id=10005, version=1)
class Microsoft_Windows_SMBDirect_10005_1(Etw):
    pattern = Struct(
        "SocketID" / Guid,
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "CreditsRequested" / Int16ul,
        "CreditsGranted" / Int16ul,
        "Flags" / Int16ul,
        "Reserved" / Int16ul,
        "RemainingDataLength" / Int32ul,
        "DataOffset" / Int32ul,
        "DataLength" / Int32ul
    )

