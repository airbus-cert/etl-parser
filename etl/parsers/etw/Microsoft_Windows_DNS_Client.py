# -*- coding: utf-8 -*-
"""
Microsoft-Windows-DNS-Client
GUID : 1c95126e-7eea-49a9-a3fe-a378b03ddb4d
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=1000, version=0)
class Microsoft_Windows_DNS_Client_1000_0(Etw):
    pattern = Struct(
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=1001, version=0)
class Microsoft_Windows_DNS_Client_1001_0(Etw):
    pattern = Struct(
        "Interface" / WString,
        "TotalServerCount" / Int32ul,
        "Index" / Int32ul,
        "DynamicAddress" / Int8ul,
        "AddressLength" / Int32ul,
        "Address" / Bytes(lambda this: this.AddressLength)
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=1002, version=0)
class Microsoft_Windows_DNS_Client_1002_0(Etw):
    pattern = Struct(
        "Interface" / WString,
        "AddressLength" / Int32ul,
        "Address" / Bytes(lambda this: this.AddressLength)
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=1003, version=0)
class Microsoft_Windows_DNS_Client_1003_0(Etw):
    pattern = Struct(
        "AddressLength" / Int32ul,
        "Address" / Bytes(lambda this: this.AddressLength)
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=1005, version=0)
class Microsoft_Windows_DNS_Client_1005_0(Etw):
    pattern = Struct(
        "AddressLength" / Int32ul,
        "Address" / Bytes(lambda this: this.AddressLength)
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=1007, version=0)
class Microsoft_Windows_DNS_Client_1007_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=1008, version=0)
class Microsoft_Windows_DNS_Client_1008_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=1009, version=0)
class Microsoft_Windows_DNS_Client_1009_0(Etw):
    pattern = Struct(
        "DnsSuffix" / WString,
        "AdSuffix" / WString
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=1010, version=0)
class Microsoft_Windows_DNS_Client_1010_0(Etw):
    pattern = Struct(
        "DnsSuffix" / WString,
        "AdSuffix" / WString
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=1011, version=0)
class Microsoft_Windows_DNS_Client_1011_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=1012, version=0)
class Microsoft_Windows_DNS_Client_1012_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=1013, version=0)
class Microsoft_Windows_DNS_Client_1013_0(Etw):
    pattern = Struct(
        "QueryName" / WString,
        "AddressLength" / Int32ul,
        "Address" / Bytes(lambda this: this.AddressLength)
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=1014, version=0)
class Microsoft_Windows_DNS_Client_1014_0(Etw):
    pattern = Struct(
        "QueryName" / WString,
        "AddressLength" / Int32ul,
        "Address" / Bytes(lambda this: this.AddressLength)
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=1015, version=0)
class Microsoft_Windows_DNS_Client_1015_0(Etw):
    pattern = Struct(
        "QueryName" / WString,
        "AddressLength" / Int32ul,
        "Address" / Bytes(lambda this: this.AddressLength)
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=1016, version=0)
class Microsoft_Windows_DNS_Client_1016_0(Etw):
    pattern = Struct(
        "QueryName" / WString,
        "AddressLength" / Int32ul,
        "Address" / Bytes(lambda this: this.AddressLength)
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=1017, version=0)
class Microsoft_Windows_DNS_Client_1017_0(Etw):
    pattern = Struct(
        "QueryName" / WString,
        "AddressLength" / Int32ul,
        "Address" / Bytes(lambda this: this.AddressLength)
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=1018, version=0)
class Microsoft_Windows_DNS_Client_1018_0(Etw):
    pattern = Struct(
        "QueryName" / WString,
        "AddressLength" / Int32ul,
        "Address" / Bytes(lambda this: this.AddressLength),
        "DnsAddressLength" / Int32ul,
        "DnsAddress" / Bytes(lambda this: this.DnsAddressLength)
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=1019, version=0)
class Microsoft_Windows_DNS_Client_1019_0(Etw):
    pattern = Struct(
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=1020, version=0)
class Microsoft_Windows_DNS_Client_1020_0(Etw):
    pattern = Struct(
        "KeyName" / WString,
        "DnsSecValidationRequired" / Int32ul,
        "DnsQueryOverIPSec" / Int32ul,
        "DnsEncryption" / Int32ul,
        "DirectAccessServerList" / WString,
        "RemoteIPSEC" / Int32ul,
        "RemoteEncryption" / Int32ul,
        "ProxyType" / Int32ul,
        "ProxyName" / WString
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=1021, version=0)
class Microsoft_Windows_DNS_Client_1021_0(Etw):
    pattern = Struct(
        "QueryName" / WString,
        "KeyName" / WString,
        "DnsSecValidationRequired" / Int32ul,
        "DnsQueryOverIPSec" / Int32ul,
        "DnsEncryption" / Int32ul,
        "DirectAccessServerList" / WString,
        "ProxyType" / Int32ul,
        "ProxyName" / WString
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=1022, version=0)
class Microsoft_Windows_DNS_Client_1022_0(Etw):
    pattern = Struct(
        "QueryName" / WString
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=1023, version=0)
class Microsoft_Windows_DNS_Client_1023_0(Etw):
    pattern = Struct(
        "RuleName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=1024, version=0)
class Microsoft_Windows_DNS_Client_1024_0(Etw):
    pattern = Struct(
        "QueryName" / WString,
        "AddressLength" / Int32ul,
        "Address" / Bytes(lambda this: this.AddressLength)
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=1025, version=0)
class Microsoft_Windows_DNS_Client_1025_0(Etw):
    pattern = Struct(
        "QueryName" / WString,
        "AddressLength" / Int32ul,
        "Address" / Bytes(lambda this: this.AddressLength)
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=1026, version=0)
class Microsoft_Windows_DNS_Client_1026_0(Etw):
    pattern = Struct(
        "QueryName" / WString,
        "ResponseQuestion" / WString,
        "AddressLength" / Int32ul,
        "Address" / Bytes(lambda this: this.AddressLength)
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=1027, version=0)
class Microsoft_Windows_DNS_Client_1027_0(Etw):
    pattern = Struct(
        "QueryName" / WString
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=1028, version=0)
class Microsoft_Windows_DNS_Client_1028_0(Etw):
    pattern = Struct(
        "QueryName" / WString,
        "KeyName" / WString,
        "DnsSecValidationRequired" / Int32ul,
        "DnsQueryOverIPSec" / Int32ul,
        "DnsEncryption" / Int32ul,
        "DirectAccessServerList" / WString,
        "ProxyType" / Int32ul,
        "ProxyName" / WString,
        "GenericServerList" / WString,
        "IdnConfig" / Int32ul
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=3000, version=0)
class Microsoft_Windows_DNS_Client_3000_0(Etw):
    pattern = Struct(
        "QueryName" / WString,
        "QueryType" / Int32ul,
        "QueryOptions" / Int64ul
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=3001, version=0)
class Microsoft_Windows_DNS_Client_3001_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=3002, version=0)
class Microsoft_Windows_DNS_Client_3002_0(Etw):
    pattern = Struct(
        "QueryName" / WString,
        "QueryType" / Int32ul,
        "QueryOptions" / Int64ul
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=3003, version=0)
class Microsoft_Windows_DNS_Client_3003_0(Etw):
    pattern = Struct(
        "QueryName" / WString,
        "QueryType" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=3004, version=0)
class Microsoft_Windows_DNS_Client_3004_0(Etw):
    pattern = Struct(
        "QueryName" / WString,
        "QueryType" / Int32ul,
        "QueryOptions" / Int64ul
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=3005, version=0)
class Microsoft_Windows_DNS_Client_3005_0(Etw):
    pattern = Struct(
        "QueryName" / WString,
        "QueryType" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=3006, version=0)
class Microsoft_Windows_DNS_Client_3006_0(Etw):
    pattern = Struct(
        "QueryName" / WString,
        "QueryType" / Int32ul,
        "QueryOptions" / Int64ul,
        "ServerList" / WString,
        "IsNetworkQuery" / Int32ul,
        "NetworkQueryIndex" / Int32ul,
        "InterfaceIndex" / Int32ul,
        "IsAsyncQuery" / Int32ul
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=3007, version=0)
class Microsoft_Windows_DNS_Client_3007_0(Etw):
    pattern = Struct(
        "QueryName" / WString
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=3008, version=0)
class Microsoft_Windows_DNS_Client_3008_0(Etw):
    pattern = Struct(
        "QueryName" / WString,
        "QueryType" / Int32ul,
        "QueryOptions" / Int64ul,
        "QueryStatus" / Int32ul,
        "QueryResults" / WString
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=3009, version=0)
class Microsoft_Windows_DNS_Client_3009_0(Etw):
    pattern = Struct(
        "QueryName" / WString,
        "IsParallelNetworkQuery" / Int32ul,
        "NetworkIndex" / Int32ul,
        "InterfaceCount" / Int32ul,
        "AdapterName" / WString,
        "LocalAddress" / WString,
        "DNSServerAddress" / WString
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=3010, version=0)
class Microsoft_Windows_DNS_Client_3010_0(Etw):
    pattern = Struct(
        "QueryName" / WString,
        "QueryType" / Int32ul,
        "DnsServerIpAddress" / WString
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=3011, version=0)
class Microsoft_Windows_DNS_Client_3011_0(Etw):
    pattern = Struct(
        "QueryName" / WString,
        "QueryType" / Int32ul,
        "DnsServerIpAddress" / WString,
        "ResponseStatus" / Int32ul
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=3012, version=0)
class Microsoft_Windows_DNS_Client_3012_0(Etw):
    pattern = Struct(
        "QueryName" / WString,
        "NetworkIndex" / Int32ul,
        "InterfaceCount" / Int32ul,
        "AdapterName" / WString,
        "LocalAddress" / WString
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=3013, version=0)
class Microsoft_Windows_DNS_Client_3013_0(Etw):
    pattern = Struct(
        "QueryName" / WString,
        "Status" / Int32ul,
        "QueryResults" / WString
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=3014, version=0)
class Microsoft_Windows_DNS_Client_3014_0(Etw):
    pattern = Struct(
        "QueryName" / WString
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=3015, version=0)
class Microsoft_Windows_DNS_Client_3015_0(Etw):
    pattern = Struct(
        "QueryName" / WString
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=3016, version=0)
class Microsoft_Windows_DNS_Client_3016_0(Etw):
    pattern = Struct(
        "QueryName" / WString,
        "QueryType" / Int32ul,
        "QueryOptions" / Int64ul,
        "InterfaceIndex" / Int32ul
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=3018, version=0)
class Microsoft_Windows_DNS_Client_3018_0(Etw):
    pattern = Struct(
        "QueryName" / WString,
        "QueryType" / Int32ul,
        "QueryOptions" / Int64ul,
        "Status" / Int32ul,
        "QueryResults" / WString
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=3019, version=0)
class Microsoft_Windows_DNS_Client_3019_0(Etw):
    pattern = Struct(
        "QueryName" / WString,
        "QueryType" / Int32ul,
        "InterfaceIndex" / Int32ul,
        "NetworkIndex" / Int32ul
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=3020, version=0)
class Microsoft_Windows_DNS_Client_3020_0(Etw):
    pattern = Struct(
        "QueryName" / WString,
        "QueryType" / Int32ul,
        "NetworkIndex" / Int32ul,
        "InterfaceIndex" / Int32ul,
        "Status" / Int32ul,
        "QueryResults" / WString
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=8001, version=0)
class Microsoft_Windows_DNS_Client_8001_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=8002, version=0)
class Microsoft_Windows_DNS_Client_8002_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=8003, version=0)
class Microsoft_Windows_DNS_Client_8003_0(Etw):
    pattern = Struct(
        "AdapterName" / WString,
        "HostName" / WString,
        "AdapterSuffixName" / WString,
        "DnsServerList" / WString,
        "SentUpdateServer" / WString,
        "Ipaddress" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=8004, version=0)
class Microsoft_Windows_DNS_Client_8004_0(Etw):
    pattern = Struct(
        "AdapterName" / WString,
        "HostName" / WString,
        "AdapterSuffixName" / WString,
        "DnsServerList" / WString,
        "SentUpdateServer" / WString,
        "Ipaddress" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=8005, version=0)
class Microsoft_Windows_DNS_Client_8005_0(Etw):
    pattern = Struct(
        "AdapterName" / WString,
        "HostName" / WString,
        "AdapterSuffixName" / WString,
        "DnsServerList" / WString,
        "SentUpdateServer" / WString,
        "Ipaddress" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=8006, version=0)
class Microsoft_Windows_DNS_Client_8006_0(Etw):
    pattern = Struct(
        "AdapterName" / WString,
        "HostName" / WString,
        "AdapterSuffixName" / WString,
        "DnsServerList" / WString,
        "SentUpdateServer" / WString,
        "Ipaddress" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=8007, version=0)
class Microsoft_Windows_DNS_Client_8007_0(Etw):
    pattern = Struct(
        "AdapterName" / WString,
        "HostName" / WString,
        "AdapterSuffixName" / WString,
        "DnsServerList" / WString,
        "SentUpdateServer" / WString,
        "Ipaddress" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=8008, version=0)
class Microsoft_Windows_DNS_Client_8008_0(Etw):
    pattern = Struct(
        "AdapterName" / WString,
        "HostName" / WString,
        "AdapterSuffixName" / WString,
        "DnsServerList" / WString,
        "SentUpdateServer" / WString,
        "Ipaddress" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=8009, version=0)
class Microsoft_Windows_DNS_Client_8009_0(Etw):
    pattern = Struct(
        "AdapterName" / WString,
        "HostName" / WString,
        "AdapterSuffixName" / WString,
        "DnsServerList" / WString,
        "SentUpdateServer" / WString,
        "Ipaddress" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=8010, version=0)
class Microsoft_Windows_DNS_Client_8010_0(Etw):
    pattern = Struct(
        "AdapterName" / WString,
        "HostName" / WString,
        "AdapterSuffixName" / WString,
        "DnsServerList" / WString,
        "SentUpdateServer" / WString,
        "Ipaddress" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=8011, version=0)
class Microsoft_Windows_DNS_Client_8011_0(Etw):
    pattern = Struct(
        "AdapterName" / WString,
        "HostName" / WString,
        "AdapterSuffixName" / WString,
        "DnsServerList" / WString,
        "SentUpdateServer" / WString,
        "Ipaddress" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=8012, version=0)
class Microsoft_Windows_DNS_Client_8012_0(Etw):
    pattern = Struct(
        "AdapterName" / WString,
        "HostName" / WString,
        "AdapterSuffixName" / WString,
        "DnsServerList" / WString,
        "SentUpdateServer" / WString,
        "Ipaddress" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=8013, version=0)
class Microsoft_Windows_DNS_Client_8013_0(Etw):
    pattern = Struct(
        "AdapterName" / WString,
        "HostName" / WString,
        "AdapterSuffixName" / WString,
        "DnsServerList" / WString,
        "SentUpdateServer" / WString,
        "Ipaddress" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=8014, version=0)
class Microsoft_Windows_DNS_Client_8014_0(Etw):
    pattern = Struct(
        "AdapterName" / WString,
        "HostName" / WString,
        "AdapterSuffixName" / WString,
        "DnsServerList" / WString,
        "SentUpdateServer" / WString,
        "Ipaddress" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=8015, version=0)
class Microsoft_Windows_DNS_Client_8015_0(Etw):
    pattern = Struct(
        "AdapterName" / WString,
        "HostName" / WString,
        "AdapterSuffixName" / WString,
        "DnsServerList" / WString,
        "SentUpdateServer" / WString,
        "Ipaddress" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=8016, version=0)
class Microsoft_Windows_DNS_Client_8016_0(Etw):
    pattern = Struct(
        "AdapterName" / WString,
        "HostName" / WString,
        "AdapterSuffixName" / WString,
        "DnsServerList" / WString,
        "SentUpdateServer" / WString,
        "Ipaddress" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=8017, version=0)
class Microsoft_Windows_DNS_Client_8017_0(Etw):
    pattern = Struct(
        "AdapterName" / WString,
        "HostName" / WString,
        "AdapterSuffixName" / WString,
        "DnsServerList" / WString,
        "SentUpdateServer" / WString,
        "Ipaddress" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=8018, version=0)
class Microsoft_Windows_DNS_Client_8018_0(Etw):
    pattern = Struct(
        "AdapterName" / WString,
        "HostName" / WString,
        "AdapterSuffixName" / WString,
        "DnsServerList" / WString,
        "SentUpdateServer" / WString,
        "Ipaddress" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=8019, version=0)
class Microsoft_Windows_DNS_Client_8019_0(Etw):
    pattern = Struct(
        "AdapterName" / WString,
        "HostName" / WString,
        "AdapterSuffixName" / WString,
        "DnsServerList" / WString,
        "SentUpdateServer" / WString,
        "Ipaddress" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=8020, version=0)
class Microsoft_Windows_DNS_Client_8020_0(Etw):
    pattern = Struct(
        "AdapterName" / WString,
        "HostName" / WString,
        "AdapterSuffixName" / WString,
        "DnsServerList" / WString,
        "SentUpdateServer" / WString,
        "Ipaddress" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=8021, version=0)
class Microsoft_Windows_DNS_Client_8021_0(Etw):
    pattern = Struct(
        "AdapterName" / WString,
        "HostName" / WString,
        "AdapterSuffixName" / WString,
        "DnsServerList" / WString,
        "SentUpdateServer" / WString,
        "Ipaddress" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=8022, version=0)
class Microsoft_Windows_DNS_Client_8022_0(Etw):
    pattern = Struct(
        "AdapterName" / WString,
        "HostName" / WString,
        "AdapterSuffixName" / WString,
        "DnsServerList" / WString,
        "SentUpdateServer" / WString,
        "Ipaddress" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=8023, version=0)
class Microsoft_Windows_DNS_Client_8023_0(Etw):
    pattern = Struct(
        "AdapterName" / WString,
        "HostName" / WString,
        "AdapterSuffixName" / WString,
        "DnsServerList" / WString,
        "SentUpdateServer" / WString,
        "Ipaddress" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=8024, version=0)
class Microsoft_Windows_DNS_Client_8024_0(Etw):
    pattern = Struct(
        "AdapterName" / WString,
        "HostName" / WString,
        "AdapterSuffixName" / WString,
        "DnsServerList" / WString,
        "SentUpdateServer" / WString,
        "Ipaddress" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=8025, version=0)
class Microsoft_Windows_DNS_Client_8025_0(Etw):
    pattern = Struct(
        "AdapterName" / WString,
        "HostName" / WString,
        "AdapterSuffixName" / WString,
        "DnsServerList" / WString,
        "SentUpdateServer" / WString,
        "Ipaddress" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=8026, version=0)
class Microsoft_Windows_DNS_Client_8026_0(Etw):
    pattern = Struct(
        "AdapterName" / WString,
        "HostName" / WString,
        "AdapterSuffixName" / WString,
        "DnsServerList" / WString,
        "SentUpdateServer" / WString,
        "Ipaddress" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=8027, version=0)
class Microsoft_Windows_DNS_Client_8027_0(Etw):
    pattern = Struct(
        "AdapterName" / WString,
        "HostName" / WString,
        "AdapterSuffixName" / WString,
        "DnsServerList" / WString,
        "SentUpdateServer" / WString,
        "Ipaddress" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=8028, version=0)
class Microsoft_Windows_DNS_Client_8028_0(Etw):
    pattern = Struct(
        "AdapterName" / WString,
        "HostName" / WString,
        "AdapterSuffixName" / WString,
        "DnsServerList" / WString,
        "SentUpdateServer" / WString,
        "Ipaddress" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=8029, version=0)
class Microsoft_Windows_DNS_Client_8029_0(Etw):
    pattern = Struct(
        "AdapterName" / WString,
        "HostName" / WString,
        "AdapterSuffixName" / WString,
        "DnsServerList" / WString,
        "SentUpdateServer" / WString,
        "Ipaddress" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=8030, version=0)
class Microsoft_Windows_DNS_Client_8030_0(Etw):
    pattern = Struct(
        "AdapterName" / WString,
        "HostName" / WString,
        "AdapterSuffixName" / WString,
        "DnsServerList" / WString,
        "SentUpdateServer" / WString,
        "Ipaddress" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=8031, version=0)
class Microsoft_Windows_DNS_Client_8031_0(Etw):
    pattern = Struct(
        "AdapterName" / WString,
        "HostName" / WString,
        "AdapterSuffixName" / WString,
        "DnsServerList" / WString,
        "SentUpdateServer" / WString,
        "Ipaddress" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=8032, version=0)
class Microsoft_Windows_DNS_Client_8032_0(Etw):
    pattern = Struct(
        "AdapterName" / WString,
        "HostName" / WString,
        "AdapterSuffixName" / WString,
        "DnsServerList" / WString,
        "SentUpdateServer" / WString,
        "Ipaddress" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=8033, version=0)
class Microsoft_Windows_DNS_Client_8033_0(Etw):
    pattern = Struct(
        "AdapterName" / WString,
        "HostName" / WString,
        "AdapterSuffixName" / WString,
        "DnsServerList" / WString,
        "SentUpdateServer" / WString,
        "Ipaddress" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=8034, version=0)
class Microsoft_Windows_DNS_Client_8034_0(Etw):
    pattern = Struct(
        "AdapterName" / WString,
        "HostName" / WString,
        "AdapterSuffixName" / WString,
        "DnsServerList" / WString,
        "SentUpdateServer" / WString,
        "Ipaddress" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=8035, version=0)
class Microsoft_Windows_DNS_Client_8035_0(Etw):
    pattern = Struct(
        "AdapterName" / WString,
        "HostName" / WString,
        "AdapterSuffixName" / WString,
        "DnsServerList" / WString,
        "SentUpdateServer" / WString,
        "Ipaddress" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=8036, version=0)
class Microsoft_Windows_DNS_Client_8036_0(Etw):
    pattern = Struct(
        "AdapterName" / WString,
        "HostName" / WString,
        "AdapterSuffixName" / WString,
        "DnsServerList" / WString,
        "SentUpdateServer" / WString,
        "Ipaddress" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=8037, version=0)
class Microsoft_Windows_DNS_Client_8037_0(Etw):
    pattern = Struct(
        "AdapterName" / WString,
        "HostName" / WString,
        "AdapterSuffixName" / WString,
        "DnsServerList" / WString,
        "SentUpdateServer" / WString,
        "Ipaddress" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=8038, version=0)
class Microsoft_Windows_DNS_Client_8038_0(Etw):
    pattern = Struct(
        "AdapterName" / WString,
        "HostName" / WString,
        "AdapterSuffixName" / WString,
        "DnsServerList" / WString,
        "SentUpdateServer" / WString,
        "Ipaddress" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=60004, version=0)
class Microsoft_Windows_DNS_Client_60004_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=60005, version=0)
class Microsoft_Windows_DNS_Client_60005_0(Etw):
    pattern = Struct(
        "WarningCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=60006, version=0)
class Microsoft_Windows_DNS_Client_60006_0(Etw):
    pattern = Struct(
        "NextState" / Int8ul,
        "Context" / Int32ul
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=60007, version=0)
class Microsoft_Windows_DNS_Client_60007_0(Etw):
    pattern = Struct(
        "Context" / Int32ul,
        "UpdateReasonCode" / Int32ul
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=60008, version=0)
class Microsoft_Windows_DNS_Client_60008_0(Etw):
    pattern = Struct(
        "RuleName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=60101, version=0)
class Microsoft_Windows_DNS_Client_60101_0(Etw):
    pattern = Struct(
        "SourceAddress" / Int32ul,
        "SourcePort" / Int32ul,
        "DestinationAddress" / Int32ul,
        "DestinationPort" / Int32ul,
        "Protocol" / Int32ul,
        "ReferenceContext" / Int32ul
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=60102, version=0)
class Microsoft_Windows_DNS_Client_60102_0(Etw):
    pattern = Struct(
        "SourcePort" / Int32ul,
        "DestinationPort" / Int32ul,
        "Protocol" / Int32ul,
        "ReferenceContext" / Int32ul
    )


@declare(guid=guid("1c95126e-7eea-49a9-a3fe-a378b03ddb4d"), event_id=60103, version=0)
class Microsoft_Windows_DNS_Client_60103_0(Etw):
    pattern = Struct(
        "IfGuid" / Guid,
        "IfIndex" / Int32ul,
        "IfLuid" / Int64ul,
        "ReferenceContext" / Int32ul
    )

