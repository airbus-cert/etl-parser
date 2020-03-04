# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Diagnosis-ScriptedDiagnosticsProvider
GUID : 9363ccd9-d429-4452-9adb-2501e704b810
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("9363ccd9-d429-4452-9adb-2501e704b810"), event_id=1000, version=0)
class Microsoft_Windows_Diagnosis_ScriptedDiagnosticsProvider_1000_0(Etw):
    pattern = Struct(
        "UILanguage" / WString,
        "ResultSize" / Int64ul
    )


@declare(guid=guid("9363ccd9-d429-4452-9adb-2501e704b810"), event_id=1003, version=0)
class Microsoft_Windows_Diagnosis_ScriptedDiagnosticsProvider_1003_0(Etw):
    pattern = Struct(
        "Error" / Int32ul
    )


@declare(guid=guid("9363ccd9-d429-4452-9adb-2501e704b810"), event_id=1004, version=0)
class Microsoft_Windows_Diagnosis_ScriptedDiagnosticsProvider_1004_0(Etw):
    pattern = Struct(
        "UILanguage" / WString
    )


@declare(guid=guid("9363ccd9-d429-4452-9adb-2501e704b810"), event_id=1011, version=0)
class Microsoft_Windows_Diagnosis_ScriptedDiagnosticsProvider_1011_0(Etw):
    pattern = Struct(
        "Error" / Int32ul
    )


@declare(guid=guid("9363ccd9-d429-4452-9adb-2501e704b810"), event_id=1012, version=0)
class Microsoft_Windows_Diagnosis_ScriptedDiagnosticsProvider_1012_0(Etw):
    pattern = Struct(
        "Error" / Int32ul
    )


@declare(guid=guid("9363ccd9-d429-4452-9adb-2501e704b810"), event_id=1013, version=0)
class Microsoft_Windows_Diagnosis_ScriptedDiagnosticsProvider_1013_0(Etw):
    pattern = Struct(
        "Error" / Int32ul
    )


@declare(guid=guid("9363ccd9-d429-4452-9adb-2501e704b810"), event_id=1017, version=0)
class Microsoft_Windows_Diagnosis_ScriptedDiagnosticsProvider_1017_0(Etw):
    pattern = Struct(
        "QueryRemoteServer" / Int8ul
    )


@declare(guid=guid("9363ccd9-d429-4452-9adb-2501e704b810"), event_id=2000, version=0)
class Microsoft_Windows_Diagnosis_ScriptedDiagnosticsProvider_2000_0(Etw):
    pattern = Struct(
        "IndexPath" / WString
    )


@declare(guid=guid("9363ccd9-d429-4452-9adb-2501e704b810"), event_id=2001, version=0)
class Microsoft_Windows_Diagnosis_ScriptedDiagnosticsProvider_2001_0(Etw):
    pattern = Struct(
        "Error" / Int32ul,
        "IndexPath" / WString
    )


@declare(guid=guid("9363ccd9-d429-4452-9adb-2501e704b810"), event_id=2002, version=0)
class Microsoft_Windows_Diagnosis_ScriptedDiagnosticsProvider_2002_0(Etw):
    pattern = Struct(
        "Error" / Int32ul,
        "Resource" / WString,
        "ResourceId" / Int32sl
    )


@declare(guid=guid("9363ccd9-d429-4452-9adb-2501e704b810"), event_id=3000, version=0)
class Microsoft_Windows_Diagnosis_ScriptedDiagnosticsProvider_3000_0(Etw):
    pattern = Struct(
        "Hostname" / WString,
        "Url" / WString,
        "RequestBody" / CString
    )


@declare(guid=guid("9363ccd9-d429-4452-9adb-2501e704b810"), event_id=3001, version=0)
class Microsoft_Windows_Diagnosis_ScriptedDiagnosticsProvider_3001_0(Etw):
    pattern = Struct(
        "Hostname" / WString,
        "Url" / WString
    )


@declare(guid=guid("9363ccd9-d429-4452-9adb-2501e704b810"), event_id=3002, version=0)
class Microsoft_Windows_Diagnosis_ScriptedDiagnosticsProvider_3002_0(Etw):
    pattern = Struct(
        "Hostname" / WString,
        "Url" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("9363ccd9-d429-4452-9adb-2501e704b810"), event_id=3003, version=0)
class Microsoft_Windows_Diagnosis_ScriptedDiagnosticsProvider_3003_0(Etw):
    pattern = Struct(
        "Hostname" / WString,
        "Url" / WString
    )


@declare(guid=guid("9363ccd9-d429-4452-9adb-2501e704b810"), event_id=3004, version=0)
class Microsoft_Windows_Diagnosis_ScriptedDiagnosticsProvider_3004_0(Etw):
    pattern = Struct(
        "Hostname" / WString,
        "Url" / WString
    )


@declare(guid=guid("9363ccd9-d429-4452-9adb-2501e704b810"), event_id=3005, version=0)
class Microsoft_Windows_Diagnosis_ScriptedDiagnosticsProvider_3005_0(Etw):
    pattern = Struct(
        "Hostname" / WString,
        "Url" / WString,
        "ResponseCode" / Int32ul
    )


@declare(guid=guid("9363ccd9-d429-4452-9adb-2501e704b810"), event_id=3006, version=0)
class Microsoft_Windows_Diagnosis_ScriptedDiagnosticsProvider_3006_0(Etw):
    pattern = Struct(
        "Hostname" / WString,
        "Url" / WString
    )


@declare(guid=guid("9363ccd9-d429-4452-9adb-2501e704b810"), event_id=3007, version=0)
class Microsoft_Windows_Diagnosis_ScriptedDiagnosticsProvider_3007_0(Etw):
    pattern = Struct(
        "Hostname" / WString,
        "Url" / WString
    )


@declare(guid=guid("9363ccd9-d429-4452-9adb-2501e704b810"), event_id=3008, version=0)
class Microsoft_Windows_Diagnosis_ScriptedDiagnosticsProvider_3008_0(Etw):
    pattern = Struct(
        "Hostname" / WString,
        "Url" / WString,
        "Reason" / WString
    )


@declare(guid=guid("9363ccd9-d429-4452-9adb-2501e704b810"), event_id=3009, version=0)
class Microsoft_Windows_Diagnosis_ScriptedDiagnosticsProvider_3009_0(Etw):
    pattern = Struct(
        "Hostname" / WString,
        "Url" / WString
    )


@declare(guid=guid("9363ccd9-d429-4452-9adb-2501e704b810"), event_id=3010, version=0)
class Microsoft_Windows_Diagnosis_ScriptedDiagnosticsProvider_3010_0(Etw):
    pattern = Struct(
        "AccessType" / Int32sl,
        "Proxy" / WString,
        "ProxyBypass" / WString
    )


@declare(guid=guid("9363ccd9-d429-4452-9adb-2501e704b810"), event_id=3011, version=0)
class Microsoft_Windows_Diagnosis_ScriptedDiagnosticsProvider_3011_0(Etw):
    pattern = Struct(
        "Error" / Int32ul,
        "AccessType" / Int32sl,
        "Proxy" / WString,
        "ProxyBypass" / WString
    )


@declare(guid=guid("9363ccd9-d429-4452-9adb-2501e704b810"), event_id=3012, version=0)
class Microsoft_Windows_Diagnosis_ScriptedDiagnosticsProvider_3012_0(Etw):
    pattern = Struct(
        "Error" / Int32ul
    )


@declare(guid=guid("9363ccd9-d429-4452-9adb-2501e704b810"), event_id=3013, version=0)
class Microsoft_Windows_Diagnosis_ScriptedDiagnosticsProvider_3013_0(Etw):
    pattern = Struct(
        "Error" / Int32ul
    )


@declare(guid=guid("9363ccd9-d429-4452-9adb-2501e704b810"), event_id=3014, version=0)
class Microsoft_Windows_Diagnosis_ScriptedDiagnosticsProvider_3014_0(Etw):
    pattern = Struct(
        "OSMajorVersion" / Int32sl,
        "OSMinorVersion" / Int32sl,
        "ServicePackMajor" / Int16sl,
        "ServicePackMinor" / Int16sl,
        "BuildNumber" / Int32sl,
        "ProductType" / Int32sl,
        "ProcessorArchitecture" / Int16sl,
        "Culture" / WString,
        "SystemType" / Int8sl,
        "OEM" / WString,
        "Model" / WString,
        "IsMobilePc" / Int8ul,
        "IsInternal" / Int8ul,
        "GeoId" / Int32sl,
        "Family" / WString,
        "OEMSKU" / WString,
        "Version" / WString,
        "BaseBoardOEM" / WString,
        "BaseBoardModel" / WString,
        "BaseBoardVersion" / WString,
        "BIOSVendor" / WString,
        "BIOSVersion" / WString,
        "BIOSReleaseDate" / WString,
        "BIOSMajorRelease" / Int8ul,
        "BIOSMinorRelease" / Int8ul,
        "ECFirmwareMajorRelease" / Int8ul,
        "ECFirmwareMinorRelease" / Int8ul
    )


@declare(guid=guid("9363ccd9-d429-4452-9adb-2501e704b810"), event_id=4000, version=0)
class Microsoft_Windows_Diagnosis_ScriptedDiagnosticsProvider_4000_0(Etw):
    pattern = Struct(
        "IndexPath" / WString
    )


@declare(guid=guid("9363ccd9-d429-4452-9adb-2501e704b810"), event_id=4001, version=0)
class Microsoft_Windows_Diagnosis_ScriptedDiagnosticsProvider_4001_0(Etw):
    pattern = Struct(
        "IndexPath" / WString
    )


@declare(guid=guid("9363ccd9-d429-4452-9adb-2501e704b810"), event_id=4007, version=0)
class Microsoft_Windows_Diagnosis_ScriptedDiagnosticsProvider_4007_0(Etw):
    pattern = Struct(
        "Error" / Int32ul
    )


@declare(guid=guid("9363ccd9-d429-4452-9adb-2501e704b810"), event_id=4009, version=0)
class Microsoft_Windows_Diagnosis_ScriptedDiagnosticsProvider_4009_0(Etw):
    pattern = Struct(
        "Error" / Int32ul
    )


@declare(guid=guid("9363ccd9-d429-4452-9adb-2501e704b810"), event_id=4011, version=0)
class Microsoft_Windows_Diagnosis_ScriptedDiagnosticsProvider_4011_0(Etw):
    pattern = Struct(
        "Error" / Int32ul
    )


@declare(guid=guid("9363ccd9-d429-4452-9adb-2501e704b810"), event_id=4013, version=0)
class Microsoft_Windows_Diagnosis_ScriptedDiagnosticsProvider_4013_0(Etw):
    pattern = Struct(
        "Error" / Int32ul
    )


@declare(guid=guid("9363ccd9-d429-4452-9adb-2501e704b810"), event_id=4015, version=0)
class Microsoft_Windows_Diagnosis_ScriptedDiagnosticsProvider_4015_0(Etw):
    pattern = Struct(
        "Error" / Int32ul
    )


@declare(guid=guid("9363ccd9-d429-4452-9adb-2501e704b810"), event_id=4016, version=0)
class Microsoft_Windows_Diagnosis_ScriptedDiagnosticsProvider_4016_0(Etw):
    pattern = Struct(
        "Hostname" / WString,
        "Url" / WString
    )


@declare(guid=guid("9363ccd9-d429-4452-9adb-2501e704b810"), event_id=4017, version=0)
class Microsoft_Windows_Diagnosis_ScriptedDiagnosticsProvider_4017_0(Etw):
    pattern = Struct(
        "Hostname" / WString,
        "Url" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("9363ccd9-d429-4452-9adb-2501e704b810"), event_id=4018, version=0)
class Microsoft_Windows_Diagnosis_ScriptedDiagnosticsProvider_4018_0(Etw):
    pattern = Struct(
        "Hostname" / WString,
        "Url" / WString,
        "RequestBody" / CString
    )


@declare(guid=guid("9363ccd9-d429-4452-9adb-2501e704b810"), event_id=4019, version=0)
class Microsoft_Windows_Diagnosis_ScriptedDiagnosticsProvider_4019_0(Etw):
    pattern = Struct(
        "HttpError" / Int32ul,
        "Error" / Int32ul
    )


@declare(guid=guid("9363ccd9-d429-4452-9adb-2501e704b810"), event_id=4020, version=0)
class Microsoft_Windows_Diagnosis_ScriptedDiagnosticsProvider_4020_0(Etw):
    pattern = Struct(
        "Hostname" / WString,
        "Url" / WString,
        "RequestBody" / CString
    )


@declare(guid=guid("9363ccd9-d429-4452-9adb-2501e704b810"), event_id=4021, version=0)
class Microsoft_Windows_Diagnosis_ScriptedDiagnosticsProvider_4021_0(Etw):
    pattern = Struct(
        "Hostname" / WString,
        "Url" / WString,
        "RequestBody" / CString,
        "Error" / Int32ul
    )


@declare(guid=guid("9363ccd9-d429-4452-9adb-2501e704b810"), event_id=4022, version=0)
class Microsoft_Windows_Diagnosis_ScriptedDiagnosticsProvider_4022_0(Etw):
    pattern = Struct(
        "Method" / CString
    )


@declare(guid=guid("9363ccd9-d429-4452-9adb-2501e704b810"), event_id=4023, version=0)
class Microsoft_Windows_Diagnosis_ScriptedDiagnosticsProvider_4023_0(Etw):
    pattern = Struct(
        "Method" / CString
    )


@declare(guid=guid("9363ccd9-d429-4452-9adb-2501e704b810"), event_id=4025, version=0)
class Microsoft_Windows_Diagnosis_ScriptedDiagnosticsProvider_4025_0(Etw):
    pattern = Struct(
        "Error" / Int32ul
    )


@declare(guid=guid("9363ccd9-d429-4452-9adb-2501e704b810"), event_id=4026, version=0)
class Microsoft_Windows_Diagnosis_ScriptedDiagnosticsProvider_4026_0(Etw):
    pattern = Struct(
        "Resource" / WString
    )


@declare(guid=guid("9363ccd9-d429-4452-9adb-2501e704b810"), event_id=4027, version=0)
class Microsoft_Windows_Diagnosis_ScriptedDiagnosticsProvider_4027_0(Etw):
    pattern = Struct(
        "Resource" / WString
    )


@declare(guid=guid("9363ccd9-d429-4452-9adb-2501e704b810"), event_id=5000, version=0)
class Microsoft_Windows_Diagnosis_ScriptedDiagnosticsProvider_5000_0(Etw):
    pattern = Struct(
        "Method" / CString
    )


@declare(guid=guid("9363ccd9-d429-4452-9adb-2501e704b810"), event_id=5001, version=0)
class Microsoft_Windows_Diagnosis_ScriptedDiagnosticsProvider_5001_0(Etw):
    pattern = Struct(
        "Method" / CString,
        "Value" / WString
    )


@declare(guid=guid("9363ccd9-d429-4452-9adb-2501e704b810"), event_id=5002, version=0)
class Microsoft_Windows_Diagnosis_ScriptedDiagnosticsProvider_5002_0(Etw):
    pattern = Struct(
        "Method" / CString,
        "Value" / Int8ul
    )


@declare(guid=guid("9363ccd9-d429-4452-9adb-2501e704b810"), event_id=5004, version=0)
class Microsoft_Windows_Diagnosis_ScriptedDiagnosticsProvider_5004_0(Etw):
    pattern = Struct(
        "Method" / CString,
        "Value" / Int32sl
    )


@declare(guid=guid("9363ccd9-d429-4452-9adb-2501e704b810"), event_id=5005, version=0)
class Microsoft_Windows_Diagnosis_ScriptedDiagnosticsProvider_5005_0(Etw):
    pattern = Struct(
        "Method" / CString,
        "Value" / WString
    )


@declare(guid=guid("9363ccd9-d429-4452-9adb-2501e704b810"), event_id=5006, version=0)
class Microsoft_Windows_Diagnosis_ScriptedDiagnosticsProvider_5006_0(Etw):
    pattern = Struct(
        "Method" / CString,
        "Value" / Int8ul
    )


@declare(guid=guid("9363ccd9-d429-4452-9adb-2501e704b810"), event_id=5008, version=0)
class Microsoft_Windows_Diagnosis_ScriptedDiagnosticsProvider_5008_0(Etw):
    pattern = Struct(
        "Method" / CString,
        "Value" / Int32sl
    )


@declare(guid=guid("9363ccd9-d429-4452-9adb-2501e704b810"), event_id=5009, version=0)
class Microsoft_Windows_Diagnosis_ScriptedDiagnosticsProvider_5009_0(Etw):
    pattern = Struct(
        "Method" / CString,
        "Value" / Int64ul
    )


@declare(guid=guid("9363ccd9-d429-4452-9adb-2501e704b810"), event_id=5010, version=0)
class Microsoft_Windows_Diagnosis_ScriptedDiagnosticsProvider_5010_0(Etw):
    pattern = Struct(
        "Method" / CString
    )


@declare(guid=guid("9363ccd9-d429-4452-9adb-2501e704b810"), event_id=5011, version=0)
class Microsoft_Windows_Diagnosis_ScriptedDiagnosticsProvider_5011_0(Etw):
    pattern = Struct(
        "Method" / CString,
        "Error" / Int32ul,
        "Parameter" / CString
    )


@declare(guid=guid("9363ccd9-d429-4452-9adb-2501e704b810"), event_id=5012, version=0)
class Microsoft_Windows_Diagnosis_ScriptedDiagnosticsProvider_5012_0(Etw):
    pattern = Struct(
        "Method" / CString,
        "Error" / Int32ul
    )


@declare(guid=guid("9363ccd9-d429-4452-9adb-2501e704b810"), event_id=5013, version=0)
class Microsoft_Windows_Diagnosis_ScriptedDiagnosticsProvider_5013_0(Etw):
    pattern = Struct(
        "Method" / CString,
        "Value" / Int64ul
    )


@declare(guid=guid("9363ccd9-d429-4452-9adb-2501e704b810"), event_id=5014, version=0)
class Microsoft_Windows_Diagnosis_ScriptedDiagnosticsProvider_5014_0(Etw):
    pattern = Struct(
        "Method" / CString,
        "Error" / Int32ul,
        "Index" / Int64ul
    )


@declare(guid=guid("9363ccd9-d429-4452-9adb-2501e704b810"), event_id=5015, version=0)
class Microsoft_Windows_Diagnosis_ScriptedDiagnosticsProvider_5015_0(Etw):
    pattern = Struct(
        "Method" / CString,
        "Index" / Int64ul,
        "Count" / Int64ul
    )


@declare(guid=guid("9363ccd9-d429-4452-9adb-2501e704b810"), event_id=5016, version=0)
class Microsoft_Windows_Diagnosis_ScriptedDiagnosticsProvider_5016_0(Etw):
    pattern = Struct(
        "Method" / CString,
        "Error" / Int32ul,
        "Type" / Int32sl,
        "Value" / WString
    )


@declare(guid=guid("9363ccd9-d429-4452-9adb-2501e704b810"), event_id=5017, version=0)
class Microsoft_Windows_Diagnosis_ScriptedDiagnosticsProvider_5017_0(Etw):
    pattern = Struct(
        "Method" / CString,
        "ItemsAdded" / Int64ul,
        "Count" / Int64ul
    )


@declare(guid=guid("9363ccd9-d429-4452-9adb-2501e704b810"), event_id=5018, version=0)
class Microsoft_Windows_Diagnosis_ScriptedDiagnosticsProvider_5018_0(Etw):
    pattern = Struct(
        "Method" / CString,
        "Error" / Int32ul,
        "Id" / WString,
        "Publisher" / WString,
        "Version" / WString
    )


@declare(guid=guid("9363ccd9-d429-4452-9adb-2501e704b810"), event_id=5019, version=0)
class Microsoft_Windows_Diagnosis_ScriptedDiagnosticsProvider_5019_0(Etw):
    pattern = Struct(
        "Parameter" / Int32ul,
        "Value" / WString
    )


@declare(guid=guid("9363ccd9-d429-4452-9adb-2501e704b810"), event_id=5020, version=0)
class Microsoft_Windows_Diagnosis_ScriptedDiagnosticsProvider_5020_0(Etw):
    pattern = Struct(
        "Id" / WString,
        "Publisher" / WString,
        "Version" / WString,
        "Url" / WString
    )


@declare(guid=guid("9363ccd9-d429-4452-9adb-2501e704b810"), event_id=5021, version=0)
class Microsoft_Windows_Diagnosis_ScriptedDiagnosticsProvider_5021_0(Etw):
    pattern = Struct(
        "Error" / Int32ul,
        "IndexPath" / WString
    )


@declare(guid=guid("9363ccd9-d429-4452-9adb-2501e704b810"), event_id=5022, version=0)
class Microsoft_Windows_Diagnosis_ScriptedDiagnosticsProvider_5022_0(Etw):
    pattern = Struct(
        "Name" / CString,
        "Address" / Int64ul
    )


@declare(guid=guid("9363ccd9-d429-4452-9adb-2501e704b810"), event_id=5023, version=0)
class Microsoft_Windows_Diagnosis_ScriptedDiagnosticsProvider_5023_0(Etw):
    pattern = Struct(
        "Name" / CString,
        "Address" / Int64ul
    )


@declare(guid=guid("9363ccd9-d429-4452-9adb-2501e704b810"), event_id=5024, version=0)
class Microsoft_Windows_Diagnosis_ScriptedDiagnosticsProvider_5024_0(Etw):
    pattern = Struct(
        "Name" / CString,
        "Address" / Int64ul,
        "RefCount" / Int32ul
    )


@declare(guid=guid("9363ccd9-d429-4452-9adb-2501e704b810"), event_id=5025, version=0)
class Microsoft_Windows_Diagnosis_ScriptedDiagnosticsProvider_5025_0(Etw):
    pattern = Struct(
        "Name" / CString,
        "Address" / Int64ul,
        "RefCount" / Int32ul
    )


@declare(guid=guid("9363ccd9-d429-4452-9adb-2501e704b810"), event_id=5026, version=0)
class Microsoft_Windows_Diagnosis_ScriptedDiagnosticsProvider_5026_0(Etw):
    pattern = Struct(
        "Error" / Int32ul,
        "IndexPath" / WString
    )

