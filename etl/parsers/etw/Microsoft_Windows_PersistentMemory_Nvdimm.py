# -*- coding: utf-8 -*-
"""
Microsoft-Windows-PersistentMemory-Nvdimm
GUID : a7f2235f-be51-51ed-decf-f4498812a9a2
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("a7f2235f-be51-51ed-decf-f4498812a9a2"), event_id=201, version=1)
class Microsoft_Windows_PersistentMemory_Nvdimm_201_1(Etw):
    pattern = Struct(
        "DeviceGuid" / Guid,
        "NfitHandle" / Int32ul,
        "Reason" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("a7f2235f-be51-51ed-decf-f4498812a9a2"), event_id=202, version=1)
class Microsoft_Windows_PersistentMemory_Nvdimm_202_1(Etw):
    pattern = Struct(
        "DeviceGuid" / Guid,
        "NfitHandle" / Int32ul
    )


@declare(guid=guid("a7f2235f-be51-51ed-decf-f4498812a9a2"), event_id=203, version=1)
class Microsoft_Windows_PersistentMemory_Nvdimm_203_1(Etw):
    pattern = Struct(
        "DeviceGuid" / Guid,
        "NfitHandle" / Int32ul,
        "UnsafeShutdownCount" / Int32ul,
        "BaselineUnsafeShutdownCount" / Int32ul
    )


@declare(guid=guid("a7f2235f-be51-51ed-decf-f4498812a9a2"), event_id=205, version=1)
class Microsoft_Windows_PersistentMemory_Nvdimm_205_1(Etw):
    pattern = Struct(
        "DeviceGuid" / Guid,
        "NfitHandle" / Int32ul,
        "SlotNumber" / Int32ul,
        "VendorId" / CString,
        "ProductId" / CString,
        "SerialNumber" / CString,
        "Location" / WString,
        "NtStatus" / Int32ul
    )


@declare(guid=guid("a7f2235f-be51-51ed-decf-f4498812a9a2"), event_id=206, version=2)
class Microsoft_Windows_PersistentMemory_Nvdimm_206_2(Etw):
    pattern = Struct(
        "DeviceGuid" / Guid,
        "NfitHandle" / Int32ul,
        "SlotNumber" / Int32ul,
        "VendorId" / CString,
        "ProductId" / CString,
        "SerialNumber" / CString,
        "Location" / WString,
        "SaveFailed" / Int8ul,
        "RestoreFailed" / Int8ul,
        "PlatformFlushFailed" / Int8ul,
        "ArmFailed" / Int8ul,
        "TechnologySpecificDetails" / Int64ul
    )


@declare(guid=guid("a7f2235f-be51-51ed-decf-f4498812a9a2"), event_id=207, version=2)
class Microsoft_Windows_PersistentMemory_Nvdimm_207_2(Etw):
    pattern = Struct(
        "DeviceGuid" / Guid,
        "NfitHandle" / Int32ul,
        "SlotNumber" / Int32ul,
        "VendorId" / CString,
        "ProductId" / CString,
        "SerialNumber" / CString,
        "Location" / WString,
        "SaveFailed" / Int8ul,
        "RestoreFailed" / Int8ul,
        "PlatformFlushFailed" / Int8ul,
        "ArmFailed" / Int8ul,
        "TechnologySpecificDetails" / Int64ul
    )


@declare(guid=guid("a7f2235f-be51-51ed-decf-f4498812a9a2"), event_id=300, version=2)
class Microsoft_Windows_PersistentMemory_Nvdimm_300_2(Etw):
    pattern = Struct(
        "DeviceGuid" / Guid,
        "NfitHandle" / Int32ul,
        "SlotNumber" / Int32ul,
        "VendorId" / CString,
        "ProductId" / CString,
        "SerialNumber" / CString,
        "Location" / WString,
        "LostPersistence" / Int8ul,
        "WarningThresholdExceeded" / Int8ul,
        "PersistenceRestored" / Int8ul,
        "BelowWarningThreshold" / Int8ul,
        "ModuleHealth_VoltageRegulatorFailed" / Int8ul,
        "ModuleHealth_VddLost" / Int8ul,
        "ModuleHealth_VppLost" / Int8ul,
        "ModuleHealth_VttLost" / Int8ul,
        "ModuleHealth_DramNotInSelfRefresh" / Int8ul,
        "ModuleHealth_ControllerHardwareError" / Int8ul,
        "ModuleHealth_NvmControllerError" / Int8ul,
        "ModuleHealth_NvmLifetimeError" / Int8ul,
        "ModuleHealth_NotEnoughEnergyForSave" / Int8ul,
        "ModuleHealth_InvalidFirmwareError" / Int8ul,
        "ModuleHealth_ConfigDataError" / Int8ul,
        "ModuleHealth_NoEnergySourcePresent" / Int8ul,
        "ModuleHealth_EnergySourcePolicyNotSet" / Int8ul,
        "ModuleHealth_EnergySourceHardwareError" / Int8ul,
        "ModuleHealth_EnergySourceHealthAssessmentError" / Int8ul,
        "EncodedModuleTemperature" / Int32ul,
        "ErrorThreshold_NvmLifetimeError" / Int8ul,
        "ErrorThreshold_EnergySourceLifetimeError" / Int8ul,
        "ErrorThreshold_EnergySourceTemperatureError" / Int8ul,
        "WarningThreshold_NvmLifetimeWarning" / Int8ul,
        "WarningThreshold_EnergySourceLifetimeWarning" / Int8ul,
        "WarningThreshold_EnergySourceTemperatureWarning" / Int8ul,
        "NvmLifetimePercentage" / Int32ul,
        "UncorrectableMemoryErrorCount" / Int32ul,
        "CorrectableMemoryErrorAboveThresholdEventCount" / Int32ul,
        "LastBackup_TriggerInformation" / Int32ul,
        "LastBackup_SaveFailureInformation" / Int32ul
    )


@declare(guid=guid("a7f2235f-be51-51ed-decf-f4498812a9a2"), event_id=301, version=2)
class Microsoft_Windows_PersistentMemory_Nvdimm_301_2(Etw):
    pattern = Struct(
        "DeviceGuid" / Guid,
        "NfitHandle" / Int32ul,
        "SlotNumber" / Int32ul,
        "VendorId" / CString,
        "ProductId" / CString,
        "SerialNumber" / CString,
        "Location" / WString,
        "LostPersistence" / Int8ul,
        "WarningThresholdExceeded" / Int8ul,
        "PersistenceRestored" / Int8ul,
        "BelowWarningThreshold" / Int8ul,
        "ModuleHealth_VoltageRegulatorFailed" / Int8ul,
        "ModuleHealth_VddLost" / Int8ul,
        "ModuleHealth_VppLost" / Int8ul,
        "ModuleHealth_VttLost" / Int8ul,
        "ModuleHealth_DramNotInSelfRefresh" / Int8ul,
        "ModuleHealth_ControllerHardwareError" / Int8ul,
        "ModuleHealth_NvmControllerError" / Int8ul,
        "ModuleHealth_NvmLifetimeError" / Int8ul,
        "ModuleHealth_NotEnoughEnergyForSave" / Int8ul,
        "ModuleHealth_InvalidFirmwareError" / Int8ul,
        "ModuleHealth_ConfigDataError" / Int8ul,
        "ModuleHealth_NoEnergySourcePresent" / Int8ul,
        "ModuleHealth_EnergySourcePolicyNotSet" / Int8ul,
        "ModuleHealth_EnergySourceHardwareError" / Int8ul,
        "ModuleHealth_EnergySourceHealthAssessmentError" / Int8ul,
        "EncodedModuleTemperature" / Int32ul,
        "ErrorThreshold_NvmLifetimeError" / Int8ul,
        "ErrorThreshold_EnergySourceLifetimeError" / Int8ul,
        "ErrorThreshold_EnergySourceTemperatureError" / Int8ul,
        "WarningThreshold_NvmLifetimeWarning" / Int8ul,
        "WarningThreshold_EnergySourceLifetimeWarning" / Int8ul,
        "WarningThreshold_EnergySourceTemperatureWarning" / Int8ul,
        "NvmLifetimePercentage" / Int32ul,
        "UncorrectableMemoryErrorCount" / Int32ul,
        "CorrectableMemoryErrorAboveThresholdEventCount" / Int32ul,
        "LastBackup_TriggerInformation" / Int32ul,
        "LastBackup_SaveFailureInformation" / Int32ul
    )


@declare(guid=guid("a7f2235f-be51-51ed-decf-f4498812a9a2"), event_id=302, version=2)
class Microsoft_Windows_PersistentMemory_Nvdimm_302_2(Etw):
    pattern = Struct(
        "DeviceGuid" / Guid,
        "NfitHandle" / Int32ul,
        "SlotNumber" / Int32ul,
        "VendorId" / CString,
        "ProductId" / CString,
        "SerialNumber" / CString,
        "Location" / WString,
        "LostPersistence" / Int8ul,
        "WarningThresholdExceeded" / Int8ul,
        "PersistenceRestored" / Int8ul,
        "BelowWarningThreshold" / Int8ul,
        "ModuleHealth_VoltageRegulatorFailed" / Int8ul,
        "ModuleHealth_VddLost" / Int8ul,
        "ModuleHealth_VppLost" / Int8ul,
        "ModuleHealth_VttLost" / Int8ul,
        "ModuleHealth_DramNotInSelfRefresh" / Int8ul,
        "ModuleHealth_ControllerHardwareError" / Int8ul,
        "ModuleHealth_NvmControllerError" / Int8ul,
        "ModuleHealth_NvmLifetimeError" / Int8ul,
        "ModuleHealth_NotEnoughEnergyForSave" / Int8ul,
        "ModuleHealth_InvalidFirmwareError" / Int8ul,
        "ModuleHealth_ConfigDataError" / Int8ul,
        "ModuleHealth_NoEnergySourcePresent" / Int8ul,
        "ModuleHealth_EnergySourcePolicyNotSet" / Int8ul,
        "ModuleHealth_EnergySourceHardwareError" / Int8ul,
        "ModuleHealth_EnergySourceHealthAssessmentError" / Int8ul,
        "EncodedModuleTemperature" / Int32ul,
        "ErrorThreshold_NvmLifetimeError" / Int8ul,
        "ErrorThreshold_EnergySourceLifetimeError" / Int8ul,
        "ErrorThreshold_EnergySourceTemperatureError" / Int8ul,
        "WarningThreshold_NvmLifetimeWarning" / Int8ul,
        "WarningThreshold_EnergySourceLifetimeWarning" / Int8ul,
        "WarningThreshold_EnergySourceTemperatureWarning" / Int8ul,
        "NvmLifetimePercentage" / Int32ul,
        "UncorrectableMemoryErrorCount" / Int32ul,
        "CorrectableMemoryErrorAboveThresholdEventCount" / Int32ul,
        "LastBackup_TriggerInformation" / Int32ul,
        "LastBackup_SaveFailureInformation" / Int32ul
    )


@declare(guid=guid("a7f2235f-be51-51ed-decf-f4498812a9a2"), event_id=303, version=1)
class Microsoft_Windows_PersistentMemory_Nvdimm_303_1(Etw):
    pattern = Struct(
        "DeviceGuid" / Guid,
        "NfitHandle" / Int32ul,
        "SlotNumber" / Int32ul,
        "VendorId" / CString,
        "ProductId" / CString,
        "SerialNumber" / CString,
        "Location" / WString,
        "MemoryEventCount" / Int32ul
    )


@declare(guid=guid("a7f2235f-be51-51ed-decf-f4498812a9a2"), event_id=304, version=1)
class Microsoft_Windows_PersistentMemory_Nvdimm_304_1(Etw):
    pattern = Struct(
        "DeviceGuid" / Guid,
        "NfitHandle" / Int32ul,
        "SlotNumber" / Int32ul,
        "VendorId" / CString,
        "ProductId" / CString,
        "SerialNumber" / CString,
        "Location" / WString,
        "MemoryEventCount" / Int32ul
    )


@declare(guid=guid("a7f2235f-be51-51ed-decf-f4498812a9a2"), event_id=305, version=2)
class Microsoft_Windows_PersistentMemory_Nvdimm_305_2(Etw):
    pattern = Struct(
        "DeviceGuid" / Guid,
        "NfitHandle" / Int32ul,
        "SlotNumber" / Int32ul,
        "VendorId" / CString,
        "ProductId" / CString,
        "SerialNumber" / CString,
        "Location" / WString,
        "LostPersistence" / Int8ul,
        "WarningThresholdExceeded" / Int8ul,
        "PersistenceRestored" / Int8ul,
        "BelowWarningThreshold" / Int8ul,
        "ModuleHealth_VoltageRegulatorFailed" / Int8ul,
        "ModuleHealth_VddLost" / Int8ul,
        "ModuleHealth_VppLost" / Int8ul,
        "ModuleHealth_VttLost" / Int8ul,
        "ModuleHealth_DramNotInSelfRefresh" / Int8ul,
        "ModuleHealth_ControllerHardwareError" / Int8ul,
        "ModuleHealth_NvmControllerError" / Int8ul,
        "ModuleHealth_NvmLifetimeError" / Int8ul,
        "ModuleHealth_NotEnoughEnergyForSave" / Int8ul,
        "ModuleHealth_InvalidFirmwareError" / Int8ul,
        "ModuleHealth_ConfigDataError" / Int8ul,
        "ModuleHealth_NoEnergySourcePresent" / Int8ul,
        "ModuleHealth_EnergySourcePolicyNotSet" / Int8ul,
        "ModuleHealth_EnergySourceHardwareError" / Int8ul,
        "ModuleHealth_EnergySourceHealthAssessmentError" / Int8ul,
        "EncodedModuleTemperature" / Int32ul,
        "ErrorThreshold_NvmLifetimeError" / Int8ul,
        "ErrorThreshold_EnergySourceLifetimeError" / Int8ul,
        "ErrorThreshold_EnergySourceTemperatureError" / Int8ul,
        "WarningThreshold_NvmLifetimeWarning" / Int8ul,
        "WarningThreshold_EnergySourceLifetimeWarning" / Int8ul,
        "WarningThreshold_EnergySourceTemperatureWarning" / Int8ul,
        "NvmLifetimePercentage" / Int32ul,
        "UncorrectableMemoryErrorCount" / Int32ul,
        "CorrectableMemoryErrorAboveThresholdEventCount" / Int32ul,
        "LastBackup_TriggerInformation" / Int32ul,
        "LastBackup_SaveFailureInformation" / Int32ul
    )


@declare(guid=guid("a7f2235f-be51-51ed-decf-f4498812a9a2"), event_id=306, version=0)
class Microsoft_Windows_PersistentMemory_Nvdimm_306_0(Etw):
    pattern = Struct(
        "DeviceGuid" / Guid,
        "Message" / CString
    )


@declare(guid=guid("a7f2235f-be51-51ed-decf-f4498812a9a2"), event_id=400, version=1)
class Microsoft_Windows_PersistentMemory_Nvdimm_400_1(Etw):
    pattern = Struct(
        "DeviceGuid" / Guid,
        "NfitHandle" / Int32ul,
        "LostDataPersistence" / Int8ul,
        "LostWritePersistence" / Int8ul,
        "FatalError" / Int8ul,
        "LostDataPersistenceImminent" / Int8ul,
        "LostWritePersistenceImminent" / Int8ul,
        "FatalErrorImminent" / Int8ul,
        "NvdimmNotArmed" / Int8ul
    )


@declare(guid=guid("a7f2235f-be51-51ed-decf-f4498812a9a2"), event_id=401, version=1)
class Microsoft_Windows_PersistentMemory_Nvdimm_401_1(Etw):
    pattern = Struct(
        "DeviceGuid" / Guid,
        "NfitHandle" / Int32ul,
        "LostDataPersistence" / Int8ul,
        "LostWritePersistence" / Int8ul,
        "FatalError" / Int8ul,
        "LostDataPersistenceImminent" / Int8ul,
        "LostWritePersistenceImminent" / Int8ul,
        "FatalErrorImminent" / Int8ul,
        "NvdimmNotArmed" / Int8ul
    )


@declare(guid=guid("a7f2235f-be51-51ed-decf-f4498812a9a2"), event_id=402, version=1)
class Microsoft_Windows_PersistentMemory_Nvdimm_402_1(Etw):
    pattern = Struct(
        "DeviceGuid" / Guid,
        "NfitHandle" / Int32ul,
        "LostDataPersistence" / Int8ul,
        "LostWritePersistence" / Int8ul,
        "FatalError" / Int8ul,
        "LostDataPersistenceImminent" / Int8ul,
        "LostWritePersistenceImminent" / Int8ul,
        "FatalErrorImminent" / Int8ul,
        "NvdimmNotArmed" / Int8ul
    )


@declare(guid=guid("a7f2235f-be51-51ed-decf-f4498812a9a2"), event_id=403, version=1)
class Microsoft_Windows_PersistentMemory_Nvdimm_403_1(Etw):
    pattern = Struct(
        "DeviceGuid" / Guid,
        "NfitHandle" / Int32ul,
        "LostDataPersistence" / Int8ul,
        "LostWritePersistence" / Int8ul,
        "FatalError" / Int8ul,
        "LostDataPersistenceImminent" / Int8ul,
        "LostWritePersistenceImminent" / Int8ul,
        "FatalErrorImminent" / Int8ul,
        "NvdimmNotArmed" / Int8ul
    )


@declare(guid=guid("a7f2235f-be51-51ed-decf-f4498812a9a2"), event_id=404, version=1)
class Microsoft_Windows_PersistentMemory_Nvdimm_404_1(Etw):
    pattern = Struct(
        "DeviceGuid" / Guid,
        "NfitHandle" / Int32ul,
        "LostDataPersistence" / Int8ul,
        "LostWritePersistence" / Int8ul,
        "FatalError" / Int8ul,
        "LostDataPersistenceImminent" / Int8ul,
        "LostWritePersistenceImminent" / Int8ul,
        "FatalErrorImminent" / Int8ul,
        "NvdimmNotArmed" / Int8ul
    )


@declare(guid=guid("a7f2235f-be51-51ed-decf-f4498812a9a2"), event_id=405, version=1)
class Microsoft_Windows_PersistentMemory_Nvdimm_405_1(Etw):
    pattern = Struct(
        "DeviceGuid" / Guid,
        "NfitHandle" / Int32ul,
        "LostDataPersistence" / Int8ul,
        "LostWritePersistence" / Int8ul,
        "FatalError" / Int8ul,
        "LostDataPersistenceImminent" / Int8ul,
        "LostWritePersistenceImminent" / Int8ul,
        "FatalErrorImminent" / Int8ul,
        "NvdimmNotArmed" / Int8ul
    )


@declare(guid=guid("a7f2235f-be51-51ed-decf-f4498812a9a2"), event_id=406, version=1)
class Microsoft_Windows_PersistentMemory_Nvdimm_406_1(Etw):
    pattern = Struct(
        "DeviceGuid" / Guid,
        "NfitHandle" / Int32ul,
        "LostDataPersistence" / Int8ul,
        "LostWritePersistence" / Int8ul,
        "FatalError" / Int8ul,
        "LostDataPersistenceImminent" / Int8ul,
        "LostWritePersistenceImminent" / Int8ul,
        "FatalErrorImminent" / Int8ul,
        "NvdimmNotArmed" / Int8ul
    )


@declare(guid=guid("a7f2235f-be51-51ed-decf-f4498812a9a2"), event_id=407, version=1)
class Microsoft_Windows_PersistentMemory_Nvdimm_407_1(Etw):
    pattern = Struct(
        "DeviceGuid" / Guid,
        "NfitHandle" / Int32ul,
        "LostDataPersistence" / Int8ul,
        "LostWritePersistence" / Int8ul,
        "FatalError" / Int8ul,
        "LostDataPersistenceImminent" / Int8ul,
        "LostWritePersistenceImminent" / Int8ul,
        "FatalErrorImminent" / Int8ul,
        "NvdimmNotArmed" / Int8ul
    )


@declare(guid=guid("a7f2235f-be51-51ed-decf-f4498812a9a2"), event_id=501, version=2)
class Microsoft_Windows_PersistentMemory_Nvdimm_501_2(Etw):
    pattern = Struct(
        "DeviceGuid" / Guid,
        "NfitHandle" / Int32ul,
        "SlotNumber" / Int32ul,
        "VendorId" / CString,
        "ProductId" / CString,
        "SerialNumber" / CString,
        "Location" / WString,
        "FatalStatus" / Int8ul,
        "CriticalStatus" / Int8ul,
        "NonCriticalStatus" / Int8ul,
        "SpareBlocksRemainingPercentage" / Int32ul,
        "LifetimePercentageUsed" / Int32ul,
        "AlarmTrip_SpareBlocksRemaining" / Int8ul,
        "AlarmTrip_MediaTemperature" / Int8ul,
        "AlarmTrip_ControllerTemperature" / Int8ul,
        "MediaTemperatureInMultiple" / Int32sl,
        "ControllerTemperatureInMultiple" / Int32sl,
        "UnsafeShutdownCount" / Int32ul,
        "AitDramStatus" / Int32ul,
        "LastShutdownStatus" / Int32ul,
        "HealthCheckStatus" / Int32ul,
        "IsEnergyBacked" / Int8ul,
        "EnergySourceFailed" / Int32ul,
        "EnergySourceHealthCheckStatus" / Int32ul,
        "VendorSpecificDataSize" / Int32ul,
        "VendorSpecificData" / Bytes(lambda this: this.VendorSpecificDataSize)
    )


@declare(guid=guid("a7f2235f-be51-51ed-decf-f4498812a9a2"), event_id=502, version=2)
class Microsoft_Windows_PersistentMemory_Nvdimm_502_2(Etw):
    pattern = Struct(
        "DeviceGuid" / Guid,
        "NfitHandle" / Int32ul,
        "SlotNumber" / Int32ul,
        "VendorId" / CString,
        "ProductId" / CString,
        "SerialNumber" / CString,
        "Location" / WString,
        "FatalStatus" / Int8ul,
        "CriticalStatus" / Int8ul,
        "NonCriticalStatus" / Int8ul,
        "SpareBlocksRemainingPercentage" / Int32ul,
        "LifetimePercentageUsed" / Int32ul,
        "AlarmTrip_SpareBlocksRemaining" / Int8ul,
        "AlarmTrip_MediaTemperature" / Int8ul,
        "AlarmTrip_ControllerTemperature" / Int8ul,
        "MediaTemperatureInMultiple" / Int32sl,
        "ControllerTemperatureInMultiple" / Int32sl,
        "UnsafeShutdownCount" / Int32ul,
        "AitDramStatus" / Int32ul,
        "LastShutdownStatus" / Int32ul,
        "HealthCheckStatus" / Int32ul,
        "IsEnergyBacked" / Int8ul,
        "EnergySourceFailed" / Int32ul,
        "EnergySourceHealthCheckStatus" / Int32ul,
        "VendorSpecificDataSize" / Int32ul,
        "VendorSpecificData" / Bytes(lambda this: this.VendorSpecificDataSize)
    )


@declare(guid=guid("a7f2235f-be51-51ed-decf-f4498812a9a2"), event_id=503, version=2)
class Microsoft_Windows_PersistentMemory_Nvdimm_503_2(Etw):
    pattern = Struct(
        "DeviceGuid" / Guid,
        "NfitHandle" / Int32ul,
        "SlotNumber" / Int32ul,
        "VendorId" / CString,
        "ProductId" / CString,
        "SerialNumber" / CString,
        "Location" / WString,
        "FatalStatus" / Int8ul,
        "CriticalStatus" / Int8ul,
        "NonCriticalStatus" / Int8ul,
        "SpareBlocksRemainingPercentage" / Int32ul,
        "LifetimePercentageUsed" / Int32ul,
        "AlarmTrip_SpareBlocksRemaining" / Int8ul,
        "AlarmTrip_MediaTemperature" / Int8ul,
        "AlarmTrip_ControllerTemperature" / Int8ul,
        "MediaTemperatureInMultiple" / Int32sl,
        "ControllerTemperatureInMultiple" / Int32sl,
        "UnsafeShutdownCount" / Int32ul,
        "AitDramStatus" / Int32ul,
        "LastShutdownStatus" / Int32ul,
        "HealthCheckStatus" / Int32ul,
        "IsEnergyBacked" / Int8ul,
        "EnergySourceFailed" / Int32ul,
        "EnergySourceHealthCheckStatus" / Int32ul,
        "VendorSpecificDataSize" / Int32ul,
        "VendorSpecificData" / Bytes(lambda this: this.VendorSpecificDataSize)
    )


@declare(guid=guid("a7f2235f-be51-51ed-decf-f4498812a9a2"), event_id=504, version=2)
class Microsoft_Windows_PersistentMemory_Nvdimm_504_2(Etw):
    pattern = Struct(
        "DeviceGuid" / Guid,
        "NfitHandle" / Int32ul,
        "SlotNumber" / Int32ul,
        "VendorId" / CString,
        "ProductId" / CString,
        "SerialNumber" / CString,
        "Location" / WString,
        "FatalStatus" / Int8ul,
        "CriticalStatus" / Int8ul,
        "NonCriticalStatus" / Int8ul,
        "SpareBlocksRemainingPercentage" / Int32ul,
        "LifetimePercentageUsed" / Int32ul,
        "AlarmTrip_SpareBlocksRemaining" / Int8ul,
        "AlarmTrip_MediaTemperature" / Int8ul,
        "AlarmTrip_ControllerTemperature" / Int8ul,
        "MediaTemperatureInMultiple" / Int32sl,
        "ControllerTemperatureInMultiple" / Int32sl,
        "UnsafeShutdownCount" / Int32ul,
        "AitDramStatus" / Int32ul,
        "LastShutdownStatus" / Int32ul,
        "HealthCheckStatus" / Int32ul,
        "IsEnergyBacked" / Int8ul,
        "EnergySourceFailed" / Int32ul,
        "EnergySourceHealthCheckStatus" / Int32ul,
        "VendorSpecificDataSize" / Int32ul,
        "VendorSpecificData" / Bytes(lambda this: this.VendorSpecificDataSize)
    )


@declare(guid=guid("a7f2235f-be51-51ed-decf-f4498812a9a2"), event_id=505, version=2)
class Microsoft_Windows_PersistentMemory_Nvdimm_505_2(Etw):
    pattern = Struct(
        "DeviceGuid" / Guid,
        "NfitHandle" / Int32ul,
        "SlotNumber" / Int32ul,
        "VendorId" / CString,
        "ProductId" / CString,
        "SerialNumber" / CString,
        "Location" / WString,
        "FatalStatus" / Int8ul,
        "CriticalStatus" / Int8ul,
        "NonCriticalStatus" / Int8ul,
        "SpareBlocksRemainingPercentage" / Int32ul,
        "LifetimePercentageUsed" / Int32ul,
        "AlarmTrip_SpareBlocksRemaining" / Int8ul,
        "AlarmTrip_MediaTemperature" / Int8ul,
        "AlarmTrip_ControllerTemperature" / Int8ul,
        "MediaTemperatureInMultiple" / Int32sl,
        "ControllerTemperatureInMultiple" / Int32sl,
        "UnsafeShutdownCount" / Int32ul,
        "AitDramStatus" / Int32ul,
        "LastShutdownStatus" / Int32ul,
        "HealthCheckStatus" / Int32ul,
        "IsEnergyBacked" / Int8ul,
        "EnergySourceFailed" / Int32ul,
        "EnergySourceHealthCheckStatus" / Int32ul,
        "VendorSpecificDataSize" / Int32ul,
        "VendorSpecificData" / Bytes(lambda this: this.VendorSpecificDataSize)
    )


@declare(guid=guid("a7f2235f-be51-51ed-decf-f4498812a9a2"), event_id=506, version=2)
class Microsoft_Windows_PersistentMemory_Nvdimm_506_2(Etw):
    pattern = Struct(
        "DeviceGuid" / Guid,
        "NfitHandle" / Int32ul,
        "SlotNumber" / Int32ul,
        "VendorId" / CString,
        "ProductId" / CString,
        "SerialNumber" / CString,
        "Location" / WString,
        "FatalStatus" / Int8ul,
        "CriticalStatus" / Int8ul,
        "NonCriticalStatus" / Int8ul,
        "SpareBlocksRemainingPercentage" / Int32ul,
        "LifetimePercentageUsed" / Int32ul,
        "AlarmTrip_SpareBlocksRemaining" / Int8ul,
        "AlarmTrip_MediaTemperature" / Int8ul,
        "AlarmTrip_ControllerTemperature" / Int8ul,
        "MediaTemperatureInMultiple" / Int32sl,
        "ControllerTemperatureInMultiple" / Int32sl,
        "UnsafeShutdownCount" / Int32ul,
        "AitDramStatus" / Int32ul,
        "LastShutdownStatus" / Int32ul,
        "HealthCheckStatus" / Int32ul,
        "IsEnergyBacked" / Int8ul,
        "EnergySourceFailed" / Int32ul,
        "EnergySourceHealthCheckStatus" / Int32ul,
        "VendorSpecificDataSize" / Int32ul,
        "VendorSpecificData" / Bytes(lambda this: this.VendorSpecificDataSize)
    )


@declare(guid=guid("a7f2235f-be51-51ed-decf-f4498812a9a2"), event_id=507, version=2)
class Microsoft_Windows_PersistentMemory_Nvdimm_507_2(Etw):
    pattern = Struct(
        "DeviceGuid" / Guid,
        "NfitHandle" / Int32ul,
        "SlotNumber" / Int32ul,
        "VendorId" / CString,
        "ProductId" / CString,
        "SerialNumber" / CString,
        "Location" / WString,
        "FatalStatus" / Int8ul,
        "CriticalStatus" / Int8ul,
        "NonCriticalStatus" / Int8ul,
        "SpareBlocksRemainingPercentage" / Int32ul,
        "LifetimePercentageUsed" / Int32ul,
        "AlarmTrip_SpareBlocksRemaining" / Int8ul,
        "AlarmTrip_MediaTemperature" / Int8ul,
        "AlarmTrip_ControllerTemperature" / Int8ul,
        "MediaTemperatureInMultiple" / Int32sl,
        "ControllerTemperatureInMultiple" / Int32sl,
        "UnsafeShutdownCount" / Int32ul,
        "AitDramStatus" / Int32ul,
        "LastShutdownStatus" / Int32ul,
        "HealthCheckStatus" / Int32ul,
        "IsEnergyBacked" / Int8ul,
        "EnergySourceFailed" / Int32ul,
        "EnergySourceHealthCheckStatus" / Int32ul,
        "VendorSpecificDataSize" / Int32ul,
        "VendorSpecificData" / Bytes(lambda this: this.VendorSpecificDataSize)
    )


@declare(guid=guid("a7f2235f-be51-51ed-decf-f4498812a9a2"), event_id=508, version=2)
class Microsoft_Windows_PersistentMemory_Nvdimm_508_2(Etw):
    pattern = Struct(
        "DeviceGuid" / Guid,
        "NfitHandle" / Int32ul,
        "SlotNumber" / Int32ul,
        "VendorId" / CString,
        "ProductId" / CString,
        "SerialNumber" / CString,
        "Location" / WString,
        "FatalStatus" / Int8ul,
        "CriticalStatus" / Int8ul,
        "NonCriticalStatus" / Int8ul,
        "SpareBlocksRemainingPercentage" / Int32ul,
        "LifetimePercentageUsed" / Int32ul,
        "AlarmTrip_SpareBlocksRemaining" / Int8ul,
        "AlarmTrip_MediaTemperature" / Int8ul,
        "AlarmTrip_ControllerTemperature" / Int8ul,
        "MediaTemperatureInMultiple" / Int32sl,
        "ControllerTemperatureInMultiple" / Int32sl,
        "UnsafeShutdownCount" / Int32ul,
        "AitDramStatus" / Int32ul,
        "LastShutdownStatus" / Int32ul,
        "HealthCheckStatus" / Int32ul,
        "IsEnergyBacked" / Int8ul,
        "EnergySourceFailed" / Int32ul,
        "EnergySourceHealthCheckStatus" / Int32ul,
        "VendorSpecificDataSize" / Int32ul,
        "VendorSpecificData" / Bytes(lambda this: this.VendorSpecificDataSize)
    )


@declare(guid=guid("a7f2235f-be51-51ed-decf-f4498812a9a2"), event_id=509, version=1)
class Microsoft_Windows_PersistentMemory_Nvdimm_509_1(Etw):
    pattern = Struct(
        "DeviceGuid" / Guid,
        "NfitHandle" / Int32ul,
        "SlotNumber" / Int32ul,
        "VendorId" / CString,
        "ProductId" / CString,
        "SerialNumber" / CString,
        "Location" / WString,
        "SecurityState" / Int32ul
    )


@declare(guid=guid("a7f2235f-be51-51ed-decf-f4498812a9a2"), event_id=900, version=0)
class Microsoft_Windows_PersistentMemory_Nvdimm_900_0(Etw):
    pattern = Struct(
        "DeviceGuid" / Guid,
        "Message" / CString
    )

