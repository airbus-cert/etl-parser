# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Diagnosis-AdvancedTaskManager
GUID : 178dadaf-7ac4-4593-ab3e-a45fda6d0d55
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("178dadaf-7ac4-4593-ab3e-a45fda6d0d55"), event_id=5016, version=0)
class Microsoft_Windows_Diagnosis_AdvancedTaskManager_5016_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "Line" / Int32ul,
        "Address" / Int64ul,
        "Size" / Int64ul
    )


@declare(guid=guid("178dadaf-7ac4-4593-ab3e-a45fda6d0d55"), event_id=5017, version=0)
class Microsoft_Windows_Diagnosis_AdvancedTaskManager_5017_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "Line" / Int32ul,
        "Address" / Int64ul
    )


@declare(guid=guid("178dadaf-7ac4-4593-ab3e-a45fda6d0d55"), event_id=5018, version=0)
class Microsoft_Windows_Diagnosis_AdvancedTaskManager_5018_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "Line" / Int32ul,
        "Address" / Int64ul,
        "Size" / Int64ul,
        "OrigAddress" / Int64ul
    )


@declare(guid=guid("178dadaf-7ac4-4593-ab3e-a45fda6d0d55"), event_id=5100, version=0)
class Microsoft_Windows_Diagnosis_AdvancedTaskManager_5100_0(Etw):
    pattern = Struct(
        "TableId" / Int32ul,
        "ItemPos" / Int32ul,
        "ItemState" / Int32ul,
        "ItemContent" / WString
    )


@declare(guid=guid("178dadaf-7ac4-4593-ab3e-a45fda6d0d55"), event_id=5101, version=0)
class Microsoft_Windows_Diagnosis_AdvancedTaskManager_5101_0(Etw):
    pattern = Struct(
        "TableId" / Int32ul,
        "ItemPos" / Int32ul,
        "ItemState" / Int32ul,
        "ItemContent" / WString
    )


@declare(guid=guid("178dadaf-7ac4-4593-ab3e-a45fda6d0d55"), event_id=5102, version=0)
class Microsoft_Windows_Diagnosis_AdvancedTaskManager_5102_0(Etw):
    pattern = Struct(
        "TableId" / Int32ul,
        "ItemPos" / Int32ul,
        "ItemState" / Int32ul,
        "ItemContent" / WString
    )


@declare(guid=guid("178dadaf-7ac4-4593-ab3e-a45fda6d0d55"), event_id=5103, version=0)
class Microsoft_Windows_Diagnosis_AdvancedTaskManager_5103_0(Etw):
    pattern = Struct(
        "FileName" / CString,
        "Function" / CString,
        "Line" / Int32ul,
        "ErrorText" / WString
    )


@declare(guid=guid("178dadaf-7ac4-4593-ab3e-a45fda6d0d55"), event_id=5202, version=0)
class Microsoft_Windows_Diagnosis_AdvancedTaskManager_5202_0(Etw):
    pattern = Struct(
        "TabId" / Int32ul
    )


@declare(guid=guid("178dadaf-7ac4-4593-ab3e-a45fda6d0d55"), event_id=5203, version=0)
class Microsoft_Windows_Diagnosis_AdvancedTaskManager_5203_0(Etw):
    pattern = Struct(
        "TabId" / Int32ul
    )


@declare(guid=guid("178dadaf-7ac4-4593-ab3e-a45fda6d0d55"), event_id=5204, version=0)
class Microsoft_Windows_Diagnosis_AdvancedTaskManager_5204_0(Etw):
    pattern = Struct(
        "ProcessOrPackageName" / WString,
        "Version" / WString,
        "TimeDateStamp" / Int32ul,
        "ProcessId" / Int32ul
    )


@declare(guid=guid("178dadaf-7ac4-4593-ab3e-a45fda6d0d55"), event_id=5205, version=0)
class Microsoft_Windows_Diagnosis_AdvancedTaskManager_5205_0(Etw):
    pattern = Struct(
        "ProcessOrPackageName" / WString,
        "Version" / WString,
        "TimeDateStamp" / Int32ul,
        "ProcessId" / Int32ul
    )


@declare(guid=guid("178dadaf-7ac4-4593-ab3e-a45fda6d0d55"), event_id=5363, version=0)
class Microsoft_Windows_Diagnosis_AdvancedTaskManager_5363_0(Etw):
    pattern = Struct(
        "PageId" / Int32ul
    )


@declare(guid=guid("178dadaf-7ac4-4593-ab3e-a45fda6d0d55"), event_id=5364, version=0)
class Microsoft_Windows_Diagnosis_AdvancedTaskManager_5364_0(Etw):
    pattern = Struct(
        "PageId" / Int32ul
    )


@declare(guid=guid("178dadaf-7ac4-4593-ab3e-a45fda6d0d55"), event_id=5366, version=0)
class Microsoft_Windows_Diagnosis_AdvancedTaskManager_5366_0(Etw):
    pattern = Struct(
        "ResourceName" / WString,
        "ProcessorCoreCount" / Int32ul,
        "LogicalProcessorCount" / Int32ul,
        "NumaNodeCount" / Int32ul,
        "MaxCPUSpeed" / WString,
        "CurrentCPUSpeed" / WString,
        "Virtualization" / WString
    )


@declare(guid=guid("178dadaf-7ac4-4593-ab3e-a45fda6d0d55"), event_id=5368, version=0)
class Microsoft_Windows_Diagnosis_AdvancedTaskManager_5368_0(Etw):
    pattern = Struct(
        "ResourceName" / WString,
        "MemorySpeed" / WString,
        "SlotsUsed" / WString,
        "AvailableMemory" / WString,
        "CachedMemory" / WString,
        "CommittedMemory" / WString
    )


@declare(guid=guid("178dadaf-7ac4-4593-ab3e-a45fda6d0d55"), event_id=5373, version=0)
class Microsoft_Windows_Diagnosis_AdvancedTaskManager_5373_0(Etw):
    pattern = Struct(
        "PageId" / Int32ul
    )


@declare(guid=guid("178dadaf-7ac4-4593-ab3e-a45fda6d0d55"), event_id=5374, version=0)
class Microsoft_Windows_Diagnosis_AdvancedTaskManager_5374_0(Etw):
    pattern = Struct(
        "PageId" / Int32ul
    )


@declare(guid=guid("178dadaf-7ac4-4593-ab3e-a45fda6d0d55"), event_id=5376, version=0)
class Microsoft_Windows_Diagnosis_AdvancedTaskManager_5376_0(Etw):
    pattern = Struct(
        "OldPageId" / Int32ul,
        "NewPageId" / Int32ul
    )


@declare(guid=guid("178dadaf-7ac4-4593-ab3e-a45fda6d0d55"), event_id=5380, version=0)
class Microsoft_Windows_Diagnosis_AdvancedTaskManager_5380_0(Etw):
    pattern = Struct(
        "DiskCount" / Int32ul
    )


@declare(guid=guid("178dadaf-7ac4-4593-ab3e-a45fda6d0d55"), event_id=5382, version=0)
class Microsoft_Windows_Diagnosis_AdvancedTaskManager_5382_0(Etw):
    pattern = Struct(
        "AdapterCount" / Int32ul
    )


@declare(guid=guid("178dadaf-7ac4-4593-ab3e-a45fda6d0d55"), event_id=5384, version=0)
class Microsoft_Windows_Diagnosis_AdvancedTaskManager_5384_0(Etw):
    pattern = Struct(
        "AdapterCount" / Int32ul
    )


@declare(guid=guid("178dadaf-7ac4-4593-ab3e-a45fda6d0d55"), event_id=5386, version=0)
class Microsoft_Windows_Diagnosis_AdvancedTaskManager_5386_0(Etw):
    pattern = Struct(
        "SSID" / WString,
        "PhysicalNetworkType" / WString,
        "SignalQuality" / Int32ul
    )


@declare(guid=guid("178dadaf-7ac4-4593-ab3e-a45fda6d0d55"), event_id=5388, version=0)
class Microsoft_Windows_Diagnosis_AdvancedTaskManager_5388_0(Etw):
    pattern = Struct(
        "ServiceProvider" / WString,
        "PhysicalNetworkType" / WString,
        "SignalQuality" / Int32ul
    )


@declare(guid=guid("178dadaf-7ac4-4593-ab3e-a45fda6d0d55"), event_id=5389, version=0)
class Microsoft_Windows_Diagnosis_AdvancedTaskManager_5389_0(Etw):
    pattern = Struct(
        "Snap" / Int32ul,
        "CurrentView" / Int32ul
    )


@declare(guid=guid("178dadaf-7ac4-4593-ab3e-a45fda6d0d55"), event_id=5391, version=0)
class Microsoft_Windows_Diagnosis_AdvancedTaskManager_5391_0(Etw):
    pattern = Struct(
        "ChartsOn" / Int32ul,
        "CurrentView" / Int32ul
    )


@declare(guid=guid("178dadaf-7ac4-4593-ab3e-a45fda6d0d55"), event_id=5393, version=0)
class Microsoft_Windows_Diagnosis_AdvancedTaskManager_5393_0(Etw):
    pattern = Struct(
        "OldCount" / Int32ul,
        "NewCount" / Int32ul
    )


@declare(guid=guid("178dadaf-7ac4-4593-ab3e-a45fda6d0d55"), event_id=5395, version=0)
class Microsoft_Windows_Diagnosis_AdvancedTaskManager_5395_0(Etw):
    pattern = Struct(
        "OldCount" / Int32ul,
        "NewCount" / Int32ul
    )


@declare(guid=guid("178dadaf-7ac4-4593-ab3e-a45fda6d0d55"), event_id=5397, version=0)
class Microsoft_Windows_Diagnosis_AdvancedTaskManager_5397_0(Etw):
    pattern = Struct(
        "OldCount" / Int32ul,
        "NewCount" / Int32ul
    )


@declare(guid=guid("178dadaf-7ac4-4593-ab3e-a45fda6d0d55"), event_id=5399, version=0)
class Microsoft_Windows_Diagnosis_AdvancedTaskManager_5399_0(Etw):
    pattern = Struct(
        "OldCount" / Int32ul,
        "NewCount" / Int32ul
    )


@declare(guid=guid("178dadaf-7ac4-4593-ab3e-a45fda6d0d55"), event_id=5401, version=0)
class Microsoft_Windows_Diagnosis_AdvancedTaskManager_5401_0(Etw):
    pattern = Struct(
        "DiskNumber" / Int32ul
    )


@declare(guid=guid("178dadaf-7ac4-4593-ab3e-a45fda6d0d55"), event_id=5402, version=0)
class Microsoft_Windows_Diagnosis_AdvancedTaskManager_5402_0(Etw):
    pattern = Struct(
        "Hresult" / Int32ul,
        "QueryByteReturned" / Int32ul
    )


@declare(guid=guid("178dadaf-7ac4-4593-ab3e-a45fda6d0d55"), event_id=5403, version=0)
class Microsoft_Windows_Diagnosis_AdvancedTaskManager_5403_0(Etw):
    pattern = Struct(
        "ChartId" / WString,
        "FromScaleIndex" / Int32ul,
        "FromScaleString" / WString,
        "ToScaleIndex" / Int32ul,
        "ToScaleString" / WString
    )


@declare(guid=guid("178dadaf-7ac4-4593-ab3e-a45fda6d0d55"), event_id=5404, version=0)
class Microsoft_Windows_Diagnosis_AdvancedTaskManager_5404_0(Etw):
    pattern = Struct(
        "DiskNumber" / Int32ul
    )


@declare(guid=guid("178dadaf-7ac4-4593-ab3e-a45fda6d0d55"), event_id=5405, version=0)
class Microsoft_Windows_Diagnosis_AdvancedTaskManager_5405_0(Etw):
    pattern = Struct(
        "Hresult" / Int32ul,
        "QueryByteReturned" / Int32ul,
        "LengthInByte" / Int64ul
    )


@declare(guid=guid("178dadaf-7ac4-4593-ab3e-a45fda6d0d55"), event_id=5501, version=0)
class Microsoft_Windows_Diagnosis_AdvancedTaskManager_5501_0(Etw):
    pattern = Struct(
        "TabId" / Int32ul
    )


@declare(guid=guid("178dadaf-7ac4-4593-ab3e-a45fda6d0d55"), event_id=5502, version=0)
class Microsoft_Windows_Diagnosis_AdvancedTaskManager_5502_0(Etw):
    pattern = Struct(
        "TabId" / Int32ul
    )


@declare(guid=guid("178dadaf-7ac4-4593-ab3e-a45fda6d0d55"), event_id=5504, version=0)
class Microsoft_Windows_Diagnosis_AdvancedTaskManager_5504_0(Etw):
    pattern = Struct(
        "PageId" / Int32ul
    )


@declare(guid=guid("178dadaf-7ac4-4593-ab3e-a45fda6d0d55"), event_id=5652, version=0)
class Microsoft_Windows_Diagnosis_AdvancedTaskManager_5652_0(Etw):
    pattern = Struct(
        "NewItems" / Int32ul,
        "UpdatedItems" / Int32ul
    )


@declare(guid=guid("178dadaf-7ac4-4593-ab3e-a45fda6d0d55"), event_id=5654, version=0)
class Microsoft_Windows_Diagnosis_AdvancedTaskManager_5654_0(Etw):
    pattern = Struct(
        "NewItems" / Int32ul,
        "UpdatedItems" / Int32ul
    )


@declare(guid=guid("178dadaf-7ac4-4593-ab3e-a45fda6d0d55"), event_id=5656, version=0)
class Microsoft_Windows_Diagnosis_AdvancedTaskManager_5656_0(Etw):
    pattern = Struct(
        "NewItems" / Int32ul,
        "UpdatedItems" / Int32ul
    )


@declare(guid=guid("178dadaf-7ac4-4593-ab3e-a45fda6d0d55"), event_id=5658, version=0)
class Microsoft_Windows_Diagnosis_AdvancedTaskManager_5658_0(Etw):
    pattern = Struct(
        "NewItems" / Int32ul,
        "UpdatedItems" / Int32ul
    )


@declare(guid=guid("178dadaf-7ac4-4593-ab3e-a45fda6d0d55"), event_id=5660, version=0)
class Microsoft_Windows_Diagnosis_AdvancedTaskManager_5660_0(Etw):
    pattern = Struct(
        "NewItems" / Int32ul,
        "UpdatedItems" / Int32ul
    )


@declare(guid=guid("178dadaf-7ac4-4593-ab3e-a45fda6d0d55"), event_id=6002, version=0)
class Microsoft_Windows_Diagnosis_AdvancedTaskManager_6002_0(Etw):
    pattern = Struct(
        "ItemType" / Int64ul,
        "MenuId" / Int32ul
    )


@declare(guid=guid("178dadaf-7ac4-4593-ab3e-a45fda6d0d55"), event_id=6004, version=0)
class Microsoft_Windows_Diagnosis_AdvancedTaskManager_6004_0(Etw):
    pattern = Struct(
        "ItemType" / Int64ul
    )


@declare(guid=guid("178dadaf-7ac4-4593-ab3e-a45fda6d0d55"), event_id=6005, version=0)
class Microsoft_Windows_Diagnosis_AdvancedTaskManager_6005_0(Etw):
    pattern = Struct(
        "ProcessId" / Int32ul
    )


@declare(guid=guid("178dadaf-7ac4-4593-ab3e-a45fda6d0d55"), event_id=6006, version=0)
class Microsoft_Windows_Diagnosis_AdvancedTaskManager_6006_0(Etw):
    pattern = Struct(
        "ProcessId" / Int32ul
    )


@declare(guid=guid("178dadaf-7ac4-4593-ab3e-a45fda6d0d55"), event_id=6007, version=0)
class Microsoft_Windows_Diagnosis_AdvancedTaskManager_6007_0(Etw):
    pattern = Struct(
        "WindowHandle" / Int32ul
    )


@declare(guid=guid("178dadaf-7ac4-4593-ab3e-a45fda6d0d55"), event_id=6008, version=0)
class Microsoft_Windows_Diagnosis_AdvancedTaskManager_6008_0(Etw):
    pattern = Struct(
        "WindowHandle" / Int32ul
    )


@declare(guid=guid("178dadaf-7ac4-4593-ab3e-a45fda6d0d55"), event_id=6009, version=0)
class Microsoft_Windows_Diagnosis_AdvancedTaskManager_6009_0(Etw):
    pattern = Struct(
        "ServiceName" / WString
    )


@declare(guid=guid("178dadaf-7ac4-4593-ab3e-a45fda6d0d55"), event_id=6010, version=0)
class Microsoft_Windows_Diagnosis_AdvancedTaskManager_6010_0(Etw):
    pattern = Struct(
        "ServiceName" / WString
    )


@declare(guid=guid("178dadaf-7ac4-4593-ab3e-a45fda6d0d55"), event_id=6019, version=0)
class Microsoft_Windows_Diagnosis_AdvancedTaskManager_6019_0(Etw):
    pattern = Struct(
        "FromTab" / Int32ul,
        "ToTab" / Int32ul
    )


@declare(guid=guid("178dadaf-7ac4-4593-ab3e-a45fda6d0d55"), event_id=6021, version=0)
class Microsoft_Windows_Diagnosis_AdvancedTaskManager_6021_0(Etw):
    pattern = Struct(
        "FromTab" / Int32ul,
        "ToTab" / Int32ul
    )


@declare(guid=guid("178dadaf-7ac4-4593-ab3e-a45fda6d0d55"), event_id=6023, version=0)
class Microsoft_Windows_Diagnosis_AdvancedTaskManager_6023_0(Etw):
    pattern = Struct(
        "CommandId" / Int32ul
    )


@declare(guid=guid("178dadaf-7ac4-4593-ab3e-a45fda6d0d55"), event_id=7001, version=0)
class Microsoft_Windows_Diagnosis_AdvancedTaskManager_7001_0(Etw):
    pattern = Struct(
        "CountOfItemsInStartupXML" / Int32ul
    )


@declare(guid=guid("178dadaf-7ac4-4593-ab3e-a45fda6d0d55"), event_id=7102, version=0)
class Microsoft_Windows_Diagnosis_AdvancedTaskManager_7102_0(Etw):
    pattern = Struct(
        "SrumProvider" / Int32ul
    )


@declare(guid=guid("178dadaf-7ac4-4593-ab3e-a45fda6d0d55"), event_id=7103, version=0)
class Microsoft_Windows_Diagnosis_AdvancedTaskManager_7103_0(Etw):
    pattern = Struct(
        "SrumProvider" / Int32ul
    )


@declare(guid=guid("178dadaf-7ac4-4593-ab3e-a45fda6d0d55"), event_id=7104, version=0)
class Microsoft_Windows_Diagnosis_AdvancedTaskManager_7104_0(Etw):
    pattern = Struct(
        "InterfaceLUID" / Int64ul,
        "ProfileIndex" / Int32ul
    )


@declare(guid=guid("178dadaf-7ac4-4593-ab3e-a45fda6d0d55"), event_id=7105, version=0)
class Microsoft_Windows_Diagnosis_AdvancedTaskManager_7105_0(Etw):
    pattern = Struct(
        "InterfaceLUID" / Int64ul,
        "ProfileIndex" / Int32ul
    )


@declare(guid=guid("178dadaf-7ac4-4593-ab3e-a45fda6d0d55"), event_id=7106, version=0)
class Microsoft_Windows_Diagnosis_AdvancedTaskManager_7106_0(Etw):
    pattern = Struct(
        "PackageInstallPath" / WString
    )


@declare(guid=guid("178dadaf-7ac4-4593-ab3e-a45fda6d0d55"), event_id=7107, version=0)
class Microsoft_Windows_Diagnosis_AdvancedTaskManager_7107_0(Etw):
    pattern = Struct(
        "PackageInstallPath" / WString
    )


@declare(guid=guid("178dadaf-7ac4-4593-ab3e-a45fda6d0d55"), event_id=7109, version=0)
class Microsoft_Windows_Diagnosis_AdvancedTaskManager_7109_0(Etw):
    pattern = Struct(
        "PackageName" / WString,
        "LongDisplayName" / WString
    )


@declare(guid=guid("178dadaf-7ac4-4593-ab3e-a45fda6d0d55"), event_id=7111, version=0)
class Microsoft_Windows_Diagnosis_AdvancedTaskManager_7111_0(Etw):
    pattern = Struct(
        "ExePath" / WString
    )


@declare(guid=guid("178dadaf-7ac4-4593-ab3e-a45fda6d0d55"), event_id=7112, version=0)
class Microsoft_Windows_Diagnosis_AdvancedTaskManager_7112_0(Etw):
    pattern = Struct(
        "SrumProvider" / Int32ul,
        "SrumRecordSetCount" / Int64ul
    )

