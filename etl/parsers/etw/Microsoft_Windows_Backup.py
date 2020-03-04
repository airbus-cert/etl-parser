# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Backup
GUID : 1db28f2e-8f80-4027-8c5a-a11f7f10f62d
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=1, version=0)
class Microsoft_Windows_Backup_1_0(Etw):
    pattern = Struct(
        "BackupTemplateID" / Guid
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=1, version=1)
class Microsoft_Windows_Backup_1_1(Etw):
    pattern = Struct(
        "BackupTemplateID" / Guid,
        "SystemStateBackup" / Int8ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=3, version=0)
class Microsoft_Windows_Backup_3_0(Etw):
    pattern = Struct(
        "TargetDeviceName" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=4, version=0)
class Microsoft_Windows_Backup_4_0(Etw):
    pattern = Struct(
        "BackupTemplateID" / Guid,
        "BackupState" / Int32sl,
        "BackupTarget" / WString,
        "NumOfVolumes" / Int32ul,
        "VolumesInfo" / WString,
        "BackupTime" / Int64ul,
        "HRESULT" / Int32ul,
        "DetailedHRESULT" / Int32ul,
        "SourceSnapStartTime" / Int64ul,
        "SourceSnapEndTime" / Int64ul,
        "PrepareBackupStartTime" / WString,
        "PrepareBackupEndTime" / WString,
        "BackupWriteStartTime" / WString,
        "BackupWriteEndTime" / WString,
        "TargetSnapStartTime" / Int64ul,
        "TargetSnapEndTime" / Int64ul,
        "DVDFormatStartTime" / WString,
        "DVDFormatEndTime" / WString,
        "MediaVerifyStartTime" / WString,
        "MediaVerifyEndTime" / WString,
        "BackupPreviousState" / Int32sl
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=4, version=1)
class Microsoft_Windows_Backup_4_1(Etw):
    pattern = Struct(
        "BackupTemplateID" / Guid,
        "HRESULT" / Int32ul,
        "BackupState" / Int32sl,
        "BackupTarget" / WString,
        "NumOfVolumes" / Int32ul,
        "BackupTime" / Int64ul,
        "HRESULT2" / Int32ul,
        "VolumesInfo" / WString,
        "DetailedHRESULT" / Int32ul,
        "SourceSnapStartTime" / Int64ul,
        "SourceSnapEndTime" / Int64ul,
        "PrepareBackupStartTime" / WString,
        "PrepareBackupEndTime" / WString,
        "BackupWriteStartTime" / WString,
        "BackupWriteEndTime" / WString,
        "TargetSnapStartTime" / Int64ul,
        "TargetSnapEndTime" / Int64ul,
        "DVDFormatStartTime" / WString,
        "DVDFormatEndTime" / WString,
        "MediaVerifyStartTime" / WString,
        "MediaVerifyEndTime" / WString,
        "BackupPreviousState" / Int32sl,
        "ComponentStatus" / WString,
        "SSBEnumerateStartTime" / Int64ul,
        "SSBEnumerateEndTime" / Int64ul,
        "SSBVhdCreationStartTime" / Int64ul,
        "SSBVhdCreationEndTime" / Int64ul,
        "SSBBackupStartTime" / Int64ul,
        "SSBBackupEndTime" / Int64ul,
        "SystemStateBackup" / Int8ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=4, version=2)
class Microsoft_Windows_Backup_4_2(Etw):
    pattern = Struct(
        "BackupTemplateID" / Guid,
        "HRESULT" / Int32ul,
        "BackupState" / Int32sl,
        "BackupTarget" / WString,
        "NumOfVolumes" / Int32ul,
        "BackupTime" / Int64ul,
        "HRESULT2" / Int32ul,
        "VolumesInfo" / WString,
        "DetailedHRESULT" / Int32ul,
        "SourceSnapStartTime" / Int64ul,
        "SourceSnapEndTime" / Int64ul,
        "PrepareBackupStartTime" / WString,
        "PrepareBackupEndTime" / WString,
        "BackupWriteStartTime" / WString,
        "BackupWriteEndTime" / WString,
        "TargetSnapStartTime" / Int64ul,
        "TargetSnapEndTime" / Int64ul,
        "DVDFormatStartTime" / WString,
        "DVDFormatEndTime" / WString,
        "MediaVerifyStartTime" / WString,
        "MediaVerifyEndTime" / WString,
        "BackupPreviousState" / Int32sl,
        "ComponentStatus" / WString,
        "SSBEnumerateStartTime" / Int64ul,
        "SSBEnumerateEndTime" / Int64ul,
        "SSBVhdCreationStartTime" / Int64ul,
        "SSBVhdCreationEndTime" / Int64ul,
        "SSBBackupStartTime" / Int64ul,
        "SSBBackupEndTime" / Int64ul,
        "SystemStateBackup" / WString,
        "BMR" / Int8ul,
        "VssFullBackup" / Int8ul,
        "UserInputBMR" / Int8ul,
        "UserInputSSB" / Int8ul,
        "BackupSuccessLogPath" / WString,
        "BackupFailureLogPath" / WString,
        "EnumerateBackupStartTime" / WString,
        "EnumerateBackupEndTime" / WString,
        "PruneBackupStartTime" / WString,
        "PruneBackupEndTime" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=4, version=3)
class Microsoft_Windows_Backup_4_3(Etw):
    pattern = Struct(
        "BackupTemplateID" / Guid,
        "HRESULT" / Int32ul,
        "DetailedHRESULT" / Int32ul,
        "ErrorMessage" / WString,
        "BackupState" / Int32sl,
        "BackupTime" / Int64ul,
        "BackupTarget" / WString,
        "NumOfVolumes" / Int32ul,
        "VolumesInfo" / WString,
        "SourceSnapStartTime" / Int64ul,
        "SourceSnapEndTime" / Int64ul,
        "PrepareBackupStartTime" / WString,
        "PrepareBackupEndTime" / WString,
        "BackupWriteStartTime" / WString,
        "BackupWriteEndTime" / WString,
        "TargetSnapStartTime" / Int64ul,
        "TargetSnapEndTime" / Int64ul,
        "DVDFormatStartTime" / WString,
        "DVDFormatEndTime" / WString,
        "MediaVerifyStartTime" / WString,
        "MediaVerifyEndTime" / WString,
        "BackupPreviousState" / Int32sl,
        "ComponentStatus" / WString,
        "ComponentInfo" / WString,
        "SSBEnumerateStartTime" / Int64ul,
        "SSBEnumerateEndTime" / Int64ul,
        "SSBVhdCreationStartTime" / Int64ul,
        "SSBVhdCreationEndTime" / Int64ul,
        "SSBBackupStartTime" / Int64ul,
        "SSBBackupEndTime" / Int64ul,
        "SystemStateBackup" / WString,
        "BMR" / WString,
        "VssFullBackup" / Int8ul,
        "UserInputBMR" / Int8ul,
        "UserInputSSB" / Int8ul,
        "BackupSuccessLogPath" / WString,
        "BackupFailureLogPath" / WString,
        "EnumerateBackupStartTime" / WString,
        "EnumerateBackupEndTime" / WString,
        "PruneBackupStartTime" / WString,
        "PruneBackupEndTime" / WString,
        "BackupFlags" / Int32ul,
        "ComponentInfoSummary" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=5, version=0)
class Microsoft_Windows_Backup_5_0(Etw):
    pattern = Struct(
        "BackupTemplateID" / Guid,
        "BackupState" / Int32sl,
        "BackupTarget" / WString,
        "NumOfVolumes" / Int32ul,
        "VolumesInfo" / WString,
        "BackupTime" / Int64ul,
        "HRESULT" / Int32ul,
        "DetailedHRESULT" / Int32ul,
        "SourceSnapStartTime" / Int64ul,
        "SourceSnapEndTime" / Int64ul,
        "PrepareBackupStartTime" / WString,
        "PrepareBackupEndTime" / WString,
        "BackupWriteStartTime" / WString,
        "BackupWriteEndTime" / WString,
        "TargetSnapStartTime" / Int64ul,
        "TargetSnapEndTime" / Int64ul,
        "DVDFormatStartTime" / WString,
        "DVDFormatEndTime" / WString,
        "MediaVerifyStartTime" / WString,
        "MediaVerifyEndTime" / WString,
        "BackupPreviousState" / Int32sl
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=5, version=1)
class Microsoft_Windows_Backup_5_1(Etw):
    pattern = Struct(
        "BackupTemplateID" / Guid,
        "HRESULT" / Int32ul,
        "BackupState" / Int32sl,
        "BackupTarget" / WString,
        "NumOfVolumes" / Int32ul,
        "BackupTime" / Int64ul,
        "HRESULT2" / Int32ul,
        "VolumesInfo" / WString,
        "DetailedHRESULT" / Int32ul,
        "SourceSnapStartTime" / Int64ul,
        "SourceSnapEndTime" / Int64ul,
        "PrepareBackupStartTime" / WString,
        "PrepareBackupEndTime" / WString,
        "BackupWriteStartTime" / WString,
        "BackupWriteEndTime" / WString,
        "TargetSnapStartTime" / Int64ul,
        "TargetSnapEndTime" / Int64ul,
        "DVDFormatStartTime" / WString,
        "DVDFormatEndTime" / WString,
        "MediaVerifyStartTime" / WString,
        "MediaVerifyEndTime" / WString,
        "BackupPreviousState" / Int32sl,
        "ComponentStatus" / WString,
        "SSBEnumerateStartTime" / Int64ul,
        "SSBEnumerateEndTime" / Int64ul,
        "SSBVhdCreationStartTime" / Int64ul,
        "SSBVhdCreationEndTime" / Int64ul,
        "SSBBackupStartTime" / Int64ul,
        "SSBBackupEndTime" / Int64ul,
        "SystemStateBackup" / Int8ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=5, version=2)
class Microsoft_Windows_Backup_5_2(Etw):
    pattern = Struct(
        "BackupTemplateID" / Guid,
        "HRESULT" / Int32ul,
        "BackupState" / Int32sl,
        "BackupTarget" / WString,
        "NumOfVolumes" / Int32ul,
        "BackupTime" / Int64ul,
        "HRESULT2" / Int32ul,
        "VolumesInfo" / WString,
        "DetailedHRESULT" / Int32ul,
        "SourceSnapStartTime" / Int64ul,
        "SourceSnapEndTime" / Int64ul,
        "PrepareBackupStartTime" / WString,
        "PrepareBackupEndTime" / WString,
        "BackupWriteStartTime" / WString,
        "BackupWriteEndTime" / WString,
        "TargetSnapStartTime" / Int64ul,
        "TargetSnapEndTime" / Int64ul,
        "DVDFormatStartTime" / WString,
        "DVDFormatEndTime" / WString,
        "MediaVerifyStartTime" / WString,
        "MediaVerifyEndTime" / WString,
        "BackupPreviousState" / Int32sl,
        "ComponentStatus" / WString,
        "SSBEnumerateStartTime" / Int64ul,
        "SSBEnumerateEndTime" / Int64ul,
        "SSBVhdCreationStartTime" / Int64ul,
        "SSBVhdCreationEndTime" / Int64ul,
        "SSBBackupStartTime" / Int64ul,
        "SSBBackupEndTime" / Int64ul,
        "SystemStateBackup" / WString,
        "BMR" / Int8ul,
        "VssFullBackup" / Int8ul,
        "UserInputBMR" / Int8ul,
        "UserInputSSB" / Int8ul,
        "BackupSuccessLogPath" / WString,
        "BackupFailureLogPath" / WString,
        "EnumerateBackupStartTime" / WString,
        "EnumerateBackupEndTime" / WString,
        "PruneBackupStartTime" / WString,
        "PruneBackupEndTime" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=5, version=3)
class Microsoft_Windows_Backup_5_3(Etw):
    pattern = Struct(
        "BackupTemplateID" / Guid,
        "HRESULT" / Int32ul,
        "DetailedHRESULT" / Int32ul,
        "ErrorMessage" / WString,
        "BackupState" / Int32sl,
        "BackupTime" / Int64ul,
        "BackupTarget" / WString,
        "NumOfVolumes" / Int32ul,
        "VolumesInfo" / WString,
        "SourceSnapStartTime" / Int64ul,
        "SourceSnapEndTime" / Int64ul,
        "PrepareBackupStartTime" / WString,
        "PrepareBackupEndTime" / WString,
        "BackupWriteStartTime" / WString,
        "BackupWriteEndTime" / WString,
        "TargetSnapStartTime" / Int64ul,
        "TargetSnapEndTime" / Int64ul,
        "DVDFormatStartTime" / WString,
        "DVDFormatEndTime" / WString,
        "MediaVerifyStartTime" / WString,
        "MediaVerifyEndTime" / WString,
        "BackupPreviousState" / Int32sl,
        "ComponentStatus" / WString,
        "ComponentInfo" / WString,
        "SSBEnumerateStartTime" / Int64ul,
        "SSBEnumerateEndTime" / Int64ul,
        "SSBVhdCreationStartTime" / Int64ul,
        "SSBVhdCreationEndTime" / Int64ul,
        "SSBBackupStartTime" / Int64ul,
        "SSBBackupEndTime" / Int64ul,
        "SystemStateBackup" / WString,
        "BMR" / WString,
        "VssFullBackup" / Int8ul,
        "UserInputBMR" / Int8ul,
        "UserInputSSB" / Int8ul,
        "BackupSuccessLogPath" / WString,
        "BackupFailureLogPath" / WString,
        "EnumerateBackupStartTime" / WString,
        "EnumerateBackupEndTime" / WString,
        "PruneBackupStartTime" / WString,
        "PruneBackupEndTime" / WString,
        "BackupFlags" / Int32ul,
        "ComponentInfoSummary" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=7, version=0)
class Microsoft_Windows_Backup_7_0(Etw):
    pattern = Struct(
        "BackupTemplateID" / Guid,
        "BackupState" / Int32sl,
        "BackupTarget" / WString,
        "NumOfVolumes" / Int32ul,
        "VolumesInfo" / WString,
        "BackupTime" / Int64ul,
        "HRESULT" / Int32ul,
        "DetailedHRESULT" / Int32ul,
        "SourceSnapStartTime" / Int64ul,
        "SourceSnapEndTime" / Int64ul,
        "PrepareBackupStartTime" / WString,
        "PrepareBackupEndTime" / WString,
        "BackupWriteStartTime" / WString,
        "BackupWriteEndTime" / WString,
        "TargetSnapStartTime" / Int64ul,
        "TargetSnapEndTime" / Int64ul,
        "DVDFormatStartTime" / WString,
        "DVDFormatEndTime" / WString,
        "MediaVerifyStartTime" / WString,
        "MediaVerifyEndTime" / WString,
        "BackupPreviousState" / Int32sl
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=7, version=1)
class Microsoft_Windows_Backup_7_1(Etw):
    pattern = Struct(
        "BackupTemplateID" / Guid,
        "HRESULT" / Int32ul,
        "BackupState" / Int32sl,
        "BackupTarget" / WString,
        "NumOfVolumes" / Int32ul,
        "BackupTime" / Int64ul,
        "HRESULT2" / Int32ul,
        "VolumesInfo" / WString,
        "DetailedHRESULT" / Int32ul,
        "SourceSnapStartTime" / Int64ul,
        "SourceSnapEndTime" / Int64ul,
        "PrepareBackupStartTime" / WString,
        "PrepareBackupEndTime" / WString,
        "BackupWriteStartTime" / WString,
        "BackupWriteEndTime" / WString,
        "TargetSnapStartTime" / Int64ul,
        "TargetSnapEndTime" / Int64ul,
        "DVDFormatStartTime" / WString,
        "DVDFormatEndTime" / WString,
        "MediaVerifyStartTime" / WString,
        "MediaVerifyEndTime" / WString,
        "BackupPreviousState" / Int32sl,
        "ComponentStatus" / WString,
        "SSBEnumerateStartTime" / Int64ul,
        "SSBEnumerateEndTime" / Int64ul,
        "SSBVhdCreationStartTime" / Int64ul,
        "SSBVhdCreationEndTime" / Int64ul,
        "SSBBackupStartTime" / Int64ul,
        "SSBBackupEndTime" / Int64ul,
        "SystemStateBackup" / Int8ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=7, version=2)
class Microsoft_Windows_Backup_7_2(Etw):
    pattern = Struct(
        "BackupTemplateID" / Guid,
        "HRESULT" / Int32ul,
        "BackupState" / Int32sl,
        "BackupTarget" / WString,
        "NumOfVolumes" / Int32ul,
        "BackupTime" / Int64ul,
        "HRESULT2" / Int32ul,
        "VolumesInfo" / WString,
        "DetailedHRESULT" / Int32ul,
        "SourceSnapStartTime" / Int64ul,
        "SourceSnapEndTime" / Int64ul,
        "PrepareBackupStartTime" / WString,
        "PrepareBackupEndTime" / WString,
        "BackupWriteStartTime" / WString,
        "BackupWriteEndTime" / WString,
        "TargetSnapStartTime" / Int64ul,
        "TargetSnapEndTime" / Int64ul,
        "DVDFormatStartTime" / WString,
        "DVDFormatEndTime" / WString,
        "MediaVerifyStartTime" / WString,
        "MediaVerifyEndTime" / WString,
        "BackupPreviousState" / Int32sl,
        "ComponentStatus" / WString,
        "SSBEnumerateStartTime" / Int64ul,
        "SSBEnumerateEndTime" / Int64ul,
        "SSBVhdCreationStartTime" / Int64ul,
        "SSBVhdCreationEndTime" / Int64ul,
        "SSBBackupStartTime" / Int64ul,
        "SSBBackupEndTime" / Int64ul,
        "SystemStateBackup" / WString,
        "BMR" / Int8ul,
        "VssFullBackup" / Int8ul,
        "UserInputBMR" / Int8ul,
        "UserInputSSB" / Int8ul,
        "BackupSuccessLogPath" / WString,
        "BackupFailureLogPath" / WString,
        "EnumerateBackupStartTime" / WString,
        "EnumerateBackupEndTime" / WString,
        "PruneBackupStartTime" / WString,
        "PruneBackupEndTime" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=7, version=3)
class Microsoft_Windows_Backup_7_3(Etw):
    pattern = Struct(
        "BackupTemplateID" / Guid,
        "HRESULT" / Int32ul,
        "DetailedHRESULT" / Int32ul,
        "ErrorMessage" / WString,
        "BackupState" / Int32sl,
        "BackupTime" / Int64ul,
        "BackupTarget" / WString,
        "NumOfVolumes" / Int32ul,
        "VolumesInfo" / WString,
        "SourceSnapStartTime" / Int64ul,
        "SourceSnapEndTime" / Int64ul,
        "PrepareBackupStartTime" / WString,
        "PrepareBackupEndTime" / WString,
        "BackupWriteStartTime" / WString,
        "BackupWriteEndTime" / WString,
        "TargetSnapStartTime" / Int64ul,
        "TargetSnapEndTime" / Int64ul,
        "DVDFormatStartTime" / WString,
        "DVDFormatEndTime" / WString,
        "MediaVerifyStartTime" / WString,
        "MediaVerifyEndTime" / WString,
        "BackupPreviousState" / Int32sl,
        "ComponentStatus" / WString,
        "ComponentInfo" / WString,
        "SSBEnumerateStartTime" / Int64ul,
        "SSBEnumerateEndTime" / Int64ul,
        "SSBVhdCreationStartTime" / Int64ul,
        "SSBVhdCreationEndTime" / Int64ul,
        "SSBBackupStartTime" / Int64ul,
        "SSBBackupEndTime" / Int64ul,
        "SystemStateBackup" / WString,
        "BMR" / WString,
        "VssFullBackup" / Int8ul,
        "UserInputBMR" / Int8ul,
        "UserInputSSB" / Int8ul,
        "BackupSuccessLogPath" / WString,
        "BackupFailureLogPath" / WString,
        "EnumerateBackupStartTime" / WString,
        "EnumerateBackupEndTime" / WString,
        "PruneBackupStartTime" / WString,
        "PruneBackupEndTime" / WString,
        "BackupFlags" / Int32ul,
        "ComponentInfoSummary" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=8, version=0)
class Microsoft_Windows_Backup_8_0(Etw):
    pattern = Struct(
        "BackupTemplateID" / Guid,
        "BackupState" / Int32sl,
        "BackupTarget" / WString,
        "NumOfVolumes" / Int32ul,
        "VolumesInfo" / WString,
        "BackupTime" / Int64ul,
        "HRESULT" / Int32ul,
        "DetailedHRESULT" / Int32ul,
        "SourceSnapStartTime" / Int64ul,
        "SourceSnapEndTime" / Int64ul,
        "PrepareBackupStartTime" / WString,
        "PrepareBackupEndTime" / WString,
        "BackupWriteStartTime" / WString,
        "BackupWriteEndTime" / WString,
        "TargetSnapStartTime" / Int64ul,
        "TargetSnapEndTime" / Int64ul,
        "DVDFormatStartTime" / WString,
        "DVDFormatEndTime" / WString,
        "MediaVerifyStartTime" / WString,
        "MediaVerifyEndTime" / WString,
        "BackupPreviousState" / Int32sl
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=8, version=1)
class Microsoft_Windows_Backup_8_1(Etw):
    pattern = Struct(
        "BackupTemplateID" / Guid,
        "HRESULT" / Int32ul,
        "BackupState" / Int32sl,
        "BackupTarget" / WString,
        "NumOfVolumes" / Int32ul,
        "BackupTime" / Int64ul,
        "HRESULT2" / Int32ul,
        "VolumesInfo" / WString,
        "DetailedHRESULT" / Int32ul,
        "SourceSnapStartTime" / Int64ul,
        "SourceSnapEndTime" / Int64ul,
        "PrepareBackupStartTime" / WString,
        "PrepareBackupEndTime" / WString,
        "BackupWriteStartTime" / WString,
        "BackupWriteEndTime" / WString,
        "TargetSnapStartTime" / Int64ul,
        "TargetSnapEndTime" / Int64ul,
        "DVDFormatStartTime" / WString,
        "DVDFormatEndTime" / WString,
        "MediaVerifyStartTime" / WString,
        "MediaVerifyEndTime" / WString,
        "BackupPreviousState" / Int32sl,
        "ComponentStatus" / WString,
        "SSBEnumerateStartTime" / Int64ul,
        "SSBEnumerateEndTime" / Int64ul,
        "SSBVhdCreationStartTime" / Int64ul,
        "SSBVhdCreationEndTime" / Int64ul,
        "SSBBackupStartTime" / Int64ul,
        "SSBBackupEndTime" / Int64ul,
        "SystemStateBackup" / Int8ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=8, version=2)
class Microsoft_Windows_Backup_8_2(Etw):
    pattern = Struct(
        "BackupTemplateID" / Guid,
        "HRESULT" / Int32ul,
        "BackupState" / Int32sl,
        "BackupTarget" / WString,
        "NumOfVolumes" / Int32ul,
        "BackupTime" / Int64ul,
        "HRESULT2" / Int32ul,
        "VolumesInfo" / WString,
        "DetailedHRESULT" / Int32ul,
        "SourceSnapStartTime" / Int64ul,
        "SourceSnapEndTime" / Int64ul,
        "PrepareBackupStartTime" / WString,
        "PrepareBackupEndTime" / WString,
        "BackupWriteStartTime" / WString,
        "BackupWriteEndTime" / WString,
        "TargetSnapStartTime" / Int64ul,
        "TargetSnapEndTime" / Int64ul,
        "DVDFormatStartTime" / WString,
        "DVDFormatEndTime" / WString,
        "MediaVerifyStartTime" / WString,
        "MediaVerifyEndTime" / WString,
        "BackupPreviousState" / Int32sl,
        "ComponentStatus" / WString,
        "SSBEnumerateStartTime" / Int64ul,
        "SSBEnumerateEndTime" / Int64ul,
        "SSBVhdCreationStartTime" / Int64ul,
        "SSBVhdCreationEndTime" / Int64ul,
        "SSBBackupStartTime" / Int64ul,
        "SSBBackupEndTime" / Int64ul,
        "SystemStateBackup" / WString,
        "BMR" / Int8ul,
        "VssFullBackup" / Int8ul,
        "UserInputBMR" / Int8ul,
        "UserInputSSB" / Int8ul,
        "BackupSuccessLogPath" / WString,
        "BackupFailureLogPath" / WString,
        "EnumerateBackupStartTime" / WString,
        "EnumerateBackupEndTime" / WString,
        "PruneBackupStartTime" / WString,
        "PruneBackupEndTime" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=8, version=3)
class Microsoft_Windows_Backup_8_3(Etw):
    pattern = Struct(
        "BackupTemplateID" / Guid,
        "HRESULT" / Int32ul,
        "DetailedHRESULT" / Int32ul,
        "ErrorMessage" / WString,
        "BackupState" / Int32sl,
        "BackupTime" / Int64ul,
        "BackupTarget" / WString,
        "NumOfVolumes" / Int32ul,
        "VolumesInfo" / WString,
        "SourceSnapStartTime" / Int64ul,
        "SourceSnapEndTime" / Int64ul,
        "PrepareBackupStartTime" / WString,
        "PrepareBackupEndTime" / WString,
        "BackupWriteStartTime" / WString,
        "BackupWriteEndTime" / WString,
        "TargetSnapStartTime" / Int64ul,
        "TargetSnapEndTime" / Int64ul,
        "DVDFormatStartTime" / WString,
        "DVDFormatEndTime" / WString,
        "MediaVerifyStartTime" / WString,
        "MediaVerifyEndTime" / WString,
        "BackupPreviousState" / Int32sl,
        "ComponentStatus" / WString,
        "ComponentInfo" / WString,
        "SSBEnumerateStartTime" / Int64ul,
        "SSBEnumerateEndTime" / Int64ul,
        "SSBVhdCreationStartTime" / Int64ul,
        "SSBVhdCreationEndTime" / Int64ul,
        "SSBBackupStartTime" / Int64ul,
        "SSBBackupEndTime" / Int64ul,
        "SystemStateBackup" / WString,
        "BMR" / WString,
        "VssFullBackup" / Int8ul,
        "UserInputBMR" / Int8ul,
        "UserInputSSB" / Int8ul,
        "BackupSuccessLogPath" / WString,
        "BackupFailureLogPath" / WString,
        "EnumerateBackupStartTime" / WString,
        "EnumerateBackupEndTime" / WString,
        "PruneBackupStartTime" / WString,
        "PruneBackupEndTime" / WString,
        "BackupFlags" / Int32ul,
        "ComponentInfoSummary" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=9, version=0)
class Microsoft_Windows_Backup_9_0(Etw):
    pattern = Struct(
        "BackupSetId" / Guid,
        "SppErrorCode" / Int32ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=9, version=1)
class Microsoft_Windows_Backup_9_1(Etw):
    pattern = Struct(
        "BackupStartTime" / Int64ul,
        "BackupSetId" / Guid,
        "SppErrorCode" / Int32ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=9, version=2)
class Microsoft_Windows_Backup_9_2(Etw):
    pattern = Struct(
        "BackupStartTime" / Int64ul,
        "BackupSetId" / Guid,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=11, version=0)
class Microsoft_Windows_Backup_11_0(Etw):
    pattern = Struct(
        "BackupSetId" / Guid,
        "VolumeFriendlyName" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=12, version=0)
class Microsoft_Windows_Backup_12_0(Etw):
    pattern = Struct(
        "BackupSetId" / Guid
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=13, version=0)
class Microsoft_Windows_Backup_13_0(Etw):
    pattern = Struct(
        "VolumeGuid" / Guid,
        "VolumeFriendlyName" / WString,
        "BackupSourceNumUnreadableBytes" / Int64sl
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=14, version=0)
class Microsoft_Windows_Backup_14_0(Etw):
    pattern = Struct(
        "BackupTemplateID" / Guid,
        "BackupState" / Int32sl,
        "BackupTarget" / WString,
        "NumOfVolumes" / Int32ul,
        "VolumesInfo" / WString,
        "BackupTime" / Int64ul,
        "HRESULT" / Int32ul,
        "DetailedHRESULT" / Int32ul,
        "SourceSnapStartTime" / Int64ul,
        "SourceSnapEndTime" / Int64ul,
        "PrepareBackupStartTime" / WString,
        "PrepareBackupEndTime" / WString,
        "BackupWriteStartTime" / WString,
        "BackupWriteEndTime" / WString,
        "TargetSnapStartTime" / Int64ul,
        "TargetSnapEndTime" / Int64ul,
        "DVDFormatStartTime" / WString,
        "DVDFormatEndTime" / WString,
        "MediaVerifyStartTime" / WString,
        "MediaVerifyEndTime" / WString,
        "BackupPreviousState" / Int32sl
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=14, version=1)
class Microsoft_Windows_Backup_14_1(Etw):
    pattern = Struct(
        "BackupTemplateID" / Guid,
        "HRESULT" / Int32ul,
        "BackupState" / Int32sl,
        "BackupTarget" / WString,
        "NumOfVolumes" / Int32ul,
        "BackupTime" / Int64ul,
        "HRESULT2" / Int32ul,
        "VolumesInfo" / WString,
        "DetailedHRESULT" / Int32ul,
        "SourceSnapStartTime" / Int64ul,
        "SourceSnapEndTime" / Int64ul,
        "PrepareBackupStartTime" / WString,
        "PrepareBackupEndTime" / WString,
        "BackupWriteStartTime" / WString,
        "BackupWriteEndTime" / WString,
        "TargetSnapStartTime" / Int64ul,
        "TargetSnapEndTime" / Int64ul,
        "DVDFormatStartTime" / WString,
        "DVDFormatEndTime" / WString,
        "MediaVerifyStartTime" / WString,
        "MediaVerifyEndTime" / WString,
        "BackupPreviousState" / Int32sl,
        "ComponentStatus" / WString,
        "SSBEnumerateStartTime" / Int64ul,
        "SSBEnumerateEndTime" / Int64ul,
        "SSBVhdCreationStartTime" / Int64ul,
        "SSBVhdCreationEndTime" / Int64ul,
        "SSBBackupStartTime" / Int64ul,
        "SSBBackupEndTime" / Int64ul,
        "SystemStateBackup" / Int8ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=14, version=2)
class Microsoft_Windows_Backup_14_2(Etw):
    pattern = Struct(
        "BackupTemplateID" / Guid,
        "HRESULT" / Int32ul,
        "BackupState" / Int32sl,
        "BackupTarget" / WString,
        "NumOfVolumes" / Int32ul,
        "BackupTime" / Int64ul,
        "HRESULT2" / Int32ul,
        "VolumesInfo" / WString,
        "DetailedHRESULT" / Int32ul,
        "SourceSnapStartTime" / Int64ul,
        "SourceSnapEndTime" / Int64ul,
        "PrepareBackupStartTime" / WString,
        "PrepareBackupEndTime" / WString,
        "BackupWriteStartTime" / WString,
        "BackupWriteEndTime" / WString,
        "TargetSnapStartTime" / Int64ul,
        "TargetSnapEndTime" / Int64ul,
        "DVDFormatStartTime" / WString,
        "DVDFormatEndTime" / WString,
        "MediaVerifyStartTime" / WString,
        "MediaVerifyEndTime" / WString,
        "BackupPreviousState" / Int32sl,
        "ComponentStatus" / WString,
        "SSBEnumerateStartTime" / Int64ul,
        "SSBEnumerateEndTime" / Int64ul,
        "SSBVhdCreationStartTime" / Int64ul,
        "SSBVhdCreationEndTime" / Int64ul,
        "SSBBackupStartTime" / Int64ul,
        "SSBBackupEndTime" / Int64ul,
        "SystemStateBackup" / WString,
        "BMR" / Int8ul,
        "VssFullBackup" / Int8ul,
        "UserInputBMR" / Int8ul,
        "UserInputSSB" / Int8ul,
        "BackupSuccessLogPath" / WString,
        "BackupFailureLogPath" / WString,
        "EnumerateBackupStartTime" / WString,
        "EnumerateBackupEndTime" / WString,
        "PruneBackupStartTime" / WString,
        "PruneBackupEndTime" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=14, version=3)
class Microsoft_Windows_Backup_14_3(Etw):
    pattern = Struct(
        "BackupTemplateID" / Guid,
        "HRESULT" / Int32ul,
        "DetailedHRESULT" / Int32ul,
        "ErrorMessage" / WString,
        "BackupState" / Int32sl,
        "BackupTime" / Int64ul,
        "BackupTarget" / WString,
        "NumOfVolumes" / Int32ul,
        "VolumesInfo" / WString,
        "SourceSnapStartTime" / Int64ul,
        "SourceSnapEndTime" / Int64ul,
        "PrepareBackupStartTime" / WString,
        "PrepareBackupEndTime" / WString,
        "BackupWriteStartTime" / WString,
        "BackupWriteEndTime" / WString,
        "TargetSnapStartTime" / Int64ul,
        "TargetSnapEndTime" / Int64ul,
        "DVDFormatStartTime" / WString,
        "DVDFormatEndTime" / WString,
        "MediaVerifyStartTime" / WString,
        "MediaVerifyEndTime" / WString,
        "BackupPreviousState" / Int32sl,
        "ComponentStatus" / WString,
        "ComponentInfo" / WString,
        "SSBEnumerateStartTime" / Int64ul,
        "SSBEnumerateEndTime" / Int64ul,
        "SSBVhdCreationStartTime" / Int64ul,
        "SSBVhdCreationEndTime" / Int64ul,
        "SSBBackupStartTime" / Int64ul,
        "SSBBackupEndTime" / Int64ul,
        "SystemStateBackup" / WString,
        "BMR" / WString,
        "VssFullBackup" / Int8ul,
        "UserInputBMR" / Int8ul,
        "UserInputSSB" / Int8ul,
        "BackupSuccessLogPath" / WString,
        "BackupFailureLogPath" / WString,
        "EnumerateBackupStartTime" / WString,
        "EnumerateBackupEndTime" / WString,
        "PruneBackupStartTime" / WString,
        "PruneBackupEndTime" / WString,
        "BackupFlags" / Int32ul,
        "ComponentInfoSummary" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=15, version=0)
class Microsoft_Windows_Backup_15_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=17, version=0)
class Microsoft_Windows_Backup_17_0(Etw):
    pattern = Struct(
        "BackupTime" / Int64ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=17, version=1)
class Microsoft_Windows_Backup_17_1(Etw):
    pattern = Struct(
        "BackupTime" / Int64ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=18, version=0)
class Microsoft_Windows_Backup_18_0(Etw):
    pattern = Struct(
        "BackupTime" / Int64ul,
        "TemplateId" / Guid
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=19, version=0)
class Microsoft_Windows_Backup_19_0(Etw):
    pattern = Struct(
        "BackupTarget" / WString,
        "NumOfVolumes" / Int32ul,
        "VolumeNames" / WString,
        "BackupTime" / Int64ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=19, version=1)
class Microsoft_Windows_Backup_19_1(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul,
        "BackupTime" / Int64ul,
        "BackupTarget" / WString,
        "BackupTime2" / Int64ul,
        "HRESULT2" / Int32ul,
        "NumOfVolumes" / Int32ul,
        "VolumeNames" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=19, version=2)
class Microsoft_Windows_Backup_19_2(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul,
        "BackupTime" / Int64ul,
        "BackupTarget" / WString,
        "BackupTime2" / Int64ul,
        "HRESULT2" / Int32ul,
        "NumOfVolumes" / Int32ul,
        "VolumeNames" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=19, version=3)
class Microsoft_Windows_Backup_19_3(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul,
        "BackupTime" / Int64ul,
        "BackupTarget" / WString,
        "NumOfVolumes" / Int32ul,
        "VolumeNames" / WString,
        "ErrorMessage" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=20, version=0)
class Microsoft_Windows_Backup_20_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul,
        "BackupTime" / Int64ul,
        "BackupTarget" / WString,
        "BackupTime2" / Int64ul,
        "HRESULT2" / Int32ul,
        "NumOfVolumes" / Int32ul,
        "VolumeNames" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=20, version=1)
class Microsoft_Windows_Backup_20_1(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul,
        "BackupTime" / Int64ul,
        "BackupTarget" / WString,
        "NumOfVolumes" / Int32ul,
        "VolumeNames" / WString,
        "ErrorMessage" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=21, version=1)
class Microsoft_Windows_Backup_21_1(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul,
        "BackupTime" / Int64ul,
        "BackupTarget" / WString,
        "BackupTime2" / Int64ul,
        "HRESULT2" / Int32ul,
        "NumOfVolumes" / Int32ul,
        "VolumeNames" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=21, version=2)
class Microsoft_Windows_Backup_21_2(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul,
        "BackupTime" / Int64ul,
        "BackupTarget" / WString,
        "NumOfVolumes" / Int32ul,
        "VolumeNames" / WString,
        "ErrorMessage" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=22, version=1)
class Microsoft_Windows_Backup_22_1(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul,
        "BackupTime" / Int64ul,
        "BackupTarget" / WString,
        "BackupTime2" / Int64ul,
        "HRESULT2" / Int32ul,
        "NumOfVolumes" / Int32ul,
        "VolumeNames" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=22, version=2)
class Microsoft_Windows_Backup_22_2(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul,
        "BackupTime" / Int64ul,
        "BackupTarget" / WString,
        "NumOfVolumes" / Int32ul,
        "VolumeNames" / WString,
        "ErrorMessage" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=23, version=0)
class Microsoft_Windows_Backup_23_0(Etw):
    pattern = Struct(
        "BackupTemplateID" / Guid,
        "HRESULT" / Int32ul,
        "BackupState" / Int32sl,
        "BackupTarget" / WString,
        "NumOfVolumes" / Int32ul,
        "BackupTime" / Int64ul,
        "HRESULT2" / Int32ul,
        "VolumesInfo" / WString,
        "DetailedHRESULT" / Int32ul,
        "SourceSnapStartTime" / Int64ul,
        "SourceSnapEndTime" / Int64ul,
        "PrepareBackupStartTime" / WString,
        "PrepareBackupEndTime" / WString,
        "BackupWriteStartTime" / WString,
        "BackupWriteEndTime" / WString,
        "TargetSnapStartTime" / Int64ul,
        "TargetSnapEndTime" / Int64ul,
        "DVDFormatStartTime" / WString,
        "DVDFormatEndTime" / WString,
        "MediaVerifyStartTime" / WString,
        "MediaVerifyEndTime" / WString,
        "BackupPreviousState" / Int32sl,
        "ComponentStatus" / WString,
        "SSBEnumerateStartTime" / Int64ul,
        "SSBEnumerateEndTime" / Int64ul,
        "SSBVhdCreationStartTime" / Int64ul,
        "SSBVhdCreationEndTime" / Int64ul,
        "SSBBackupStartTime" / Int64ul,
        "SSBBackupEndTime" / Int64ul,
        "SystemStateBackup" / WString,
        "BMR" / Int8ul,
        "VssFullBackup" / Int8ul,
        "UserInputBMR" / Int8ul,
        "UserInputSSB" / Int8ul,
        "BackupSuccessLogPath" / WString,
        "BackupFailureLogPath" / WString,
        "EnumerateBackupStartTime" / WString,
        "EnumerateBackupEndTime" / WString,
        "PruneBackupStartTime" / WString,
        "PruneBackupEndTime" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=23, version=1)
class Microsoft_Windows_Backup_23_1(Etw):
    pattern = Struct(
        "BackupTemplateID" / Guid,
        "HRESULT" / Int32ul,
        "DetailedHRESULT" / Int32ul,
        "ErrorMessage" / WString,
        "BackupState" / Int32sl,
        "BackupTime" / Int64ul,
        "BackupTarget" / WString,
        "NumOfVolumes" / Int32ul,
        "VolumesInfo" / WString,
        "SourceSnapStartTime" / Int64ul,
        "SourceSnapEndTime" / Int64ul,
        "PrepareBackupStartTime" / WString,
        "PrepareBackupEndTime" / WString,
        "BackupWriteStartTime" / WString,
        "BackupWriteEndTime" / WString,
        "TargetSnapStartTime" / Int64ul,
        "TargetSnapEndTime" / Int64ul,
        "DVDFormatStartTime" / WString,
        "DVDFormatEndTime" / WString,
        "MediaVerifyStartTime" / WString,
        "MediaVerifyEndTime" / WString,
        "BackupPreviousState" / Int32sl,
        "ComponentStatus" / WString,
        "ComponentInfo" / WString,
        "SSBEnumerateStartTime" / Int64ul,
        "SSBEnumerateEndTime" / Int64ul,
        "SSBVhdCreationStartTime" / Int64ul,
        "SSBVhdCreationEndTime" / Int64ul,
        "SSBBackupStartTime" / Int64ul,
        "SSBBackupEndTime" / Int64ul,
        "SystemStateBackup" / WString,
        "BMR" / WString,
        "VssFullBackup" / Int8ul,
        "UserInputBMR" / Int8ul,
        "UserInputSSB" / Int8ul,
        "BackupSuccessLogPath" / WString,
        "BackupFailureLogPath" / WString,
        "EnumerateBackupStartTime" / WString,
        "EnumerateBackupEndTime" / WString,
        "PruneBackupStartTime" / WString,
        "PruneBackupEndTime" / WString,
        "BackupFlags" / Int32ul,
        "ComponentInfoSummary" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=24, version=0)
class Microsoft_Windows_Backup_24_0(Etw):
    pattern = Struct(
        "VolumeGUID" / Guid,
        "VolumeFriendlyName" / WString,
        "VhdDeleteReason" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=25, version=0)
class Microsoft_Windows_Backup_25_0(Etw):
    pattern = Struct(
        "VolumeGUID" / Guid,
        "VolumeFriendlyName" / WString,
        "VhdDeleteReason" / WString,
        "VhdPath" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=50, version=0)
class Microsoft_Windows_Backup_50_0(Etw):
    pattern = Struct(
        "VolumeFriendlyName" / WString,
        "VolumeAccessPath" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=51, version=0)
class Microsoft_Windows_Backup_51_0(Etw):
    pattern = Struct(
        "VolumeFriendlyName" / WString,
        "VolumeAccessPath" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=52, version=0)
class Microsoft_Windows_Backup_52_0(Etw):
    pattern = Struct(
        "VolumeFriendlyName" / WString,
        "VolumeAccessPath" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=99, version=1)
class Microsoft_Windows_Backup_99_1(Etw):
    pattern = Struct(
        "UserName" / WString,
        "TemplateGuid" / Guid,
        "ScheduleTimesList" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=144, version=0)
class Microsoft_Windows_Backup_144_0(Etw):
    pattern = Struct(
        "VolumeFriendlyName" / WString,
        "VolumeAccessPath" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=146, version=0)
class Microsoft_Windows_Backup_146_0(Etw):
    pattern = Struct(
        "VolumeFriendlyName" / WString,
        "VolumeAccessPath" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=160, version=0)
class Microsoft_Windows_Backup_160_0(Etw):
    pattern = Struct(
        "BackupTarget" / WString,
        "MachineName" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=192, version=0)
class Microsoft_Windows_Backup_192_0(Etw):
    pattern = Struct(
        "BackupSetId" / Guid
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=193, version=0)
class Microsoft_Windows_Backup_193_0(Etw):
    pattern = Struct(
        "BackupSetId" / Guid,
        "RestoreEventId" / Guid,
        "RestoreState" / Int32sl,
        "HRESULT" / Int32ul,
        "DetailedHRESULT" / Int32ul,
        "BackupTargetFriendlyName" / WString,
        "NumOfVolumes" / Int32ul,
        "VolumesInfo" / WString,
        "RestoreTime" / Int64ul,
        "PrepareRestoreTime" / Int32ul,
        "WriteRestoreTime" / Int32ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=193, version=1)
class Microsoft_Windows_Backup_193_1(Etw):
    pattern = Struct(
        "BackupSetId" / Guid,
        "BackupSetTime" / Int64ul,
        "RestoreEventId" / Guid,
        "RestoreState" / Int32sl,
        "HRESULT" / Int32ul,
        "DetailedHRESULT" / Int32ul,
        "BackupTargetFriendlyName" / WString,
        "NumOfVolumes" / Int32ul,
        "RestoreTime" / Int64ul,
        "VolumesInfo" / WString,
        "PrepareRestoreTime" / Int32ul,
        "WriteRestoreTime" / Int32ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=193, version=2)
class Microsoft_Windows_Backup_193_2(Etw):
    pattern = Struct(
        "BackupSetId" / Guid,
        "BackupSetTime" / Int64ul,
        "RestoreEventId" / Guid,
        "RestoreState" / Int32sl,
        "HRESULT" / Int32ul,
        "DetailedHRESULT" / Int32ul,
        "ErrorMessage" / WString,
        "BackupTargetFriendlyName" / WString,
        "NumOfVolumes" / Int32ul,
        "VolumesInfo" / WString,
        "PrepareRestoreTime" / Int32ul,
        "RestoreTime" / Int64ul,
        "WriteRestoreTime" / Int32ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=194, version=0)
class Microsoft_Windows_Backup_194_0(Etw):
    pattern = Struct(
        "BackupSetId" / Guid,
        "RestoreEventId" / Guid,
        "RestoreState" / Int32sl,
        "HRESULT" / Int32ul,
        "DetailedHRESULT" / Int32ul,
        "BackupTargetFriendlyName" / WString,
        "NumOfVolumes" / Int32ul,
        "VolumesInfo" / WString,
        "RestoreTime" / Int64ul,
        "PrepareRestoreTime" / Int32ul,
        "WriteRestoreTime" / Int32ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=194, version=1)
class Microsoft_Windows_Backup_194_1(Etw):
    pattern = Struct(
        "BackupSetId" / Guid,
        "BackupSetTime" / Int64ul,
        "RestoreEventId" / Guid,
        "RestoreState" / Int32sl,
        "HRESULT" / Int32ul,
        "DetailedHRESULT" / Int32ul,
        "BackupTargetFriendlyName" / WString,
        "NumOfVolumes" / Int32ul,
        "RestoreTime" / Int64ul,
        "VolumesInfo" / WString,
        "PrepareRestoreTime" / Int32ul,
        "WriteRestoreTime" / Int32ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=194, version=2)
class Microsoft_Windows_Backup_194_2(Etw):
    pattern = Struct(
        "BackupSetId" / Guid,
        "BackupSetTime" / Int64ul,
        "RestoreEventId" / Guid,
        "RestoreState" / Int32sl,
        "HRESULT" / Int32ul,
        "DetailedHRESULT" / Int32ul,
        "ErrorMessage" / WString,
        "BackupTargetFriendlyName" / WString,
        "NumOfVolumes" / Int32ul,
        "VolumesInfo" / WString,
        "PrepareRestoreTime" / Int32ul,
        "RestoreTime" / Int64ul,
        "WriteRestoreTime" / Int32ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=195, version=0)
class Microsoft_Windows_Backup_195_0(Etw):
    pattern = Struct(
        "BackupSetId" / Guid,
        "RestoreEventId" / Guid,
        "RestoreState" / Int32sl,
        "HRESULT" / Int32ul,
        "DetailedHRESULT" / Int32ul,
        "BackupTargetFriendlyName" / WString,
        "NumOfVolumes" / Int32ul,
        "VolumesInfo" / WString,
        "RestoreTime" / Int64ul,
        "PrepareRestoreTime" / Int32ul,
        "WriteRestoreTime" / Int32ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=195, version=1)
class Microsoft_Windows_Backup_195_1(Etw):
    pattern = Struct(
        "BackupSetId" / Guid,
        "BackupSetTime" / Int64ul,
        "RestoreEventId" / Guid,
        "RestoreState" / Int32sl,
        "HRESULT" / Int32ul,
        "DetailedHRESULT" / Int32ul,
        "BackupTargetFriendlyName" / WString,
        "NumOfVolumes" / Int32ul,
        "RestoreTime" / Int64ul,
        "VolumesInfo" / WString,
        "PrepareRestoreTime" / Int32ul,
        "WriteRestoreTime" / Int32ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=195, version=2)
class Microsoft_Windows_Backup_195_2(Etw):
    pattern = Struct(
        "BackupSetId" / Guid,
        "BackupSetTime" / Int64ul,
        "RestoreEventId" / Guid,
        "RestoreState" / Int32sl,
        "HRESULT" / Int32ul,
        "DetailedHRESULT" / Int32ul,
        "ErrorMessage" / WString,
        "BackupTargetFriendlyName" / WString,
        "NumOfVolumes" / Int32ul,
        "VolumesInfo" / WString,
        "PrepareRestoreTime" / Int32ul,
        "RestoreTime" / Int64ul,
        "WriteRestoreTime" / Int32ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=196, version=0)
class Microsoft_Windows_Backup_196_0(Etw):
    pattern = Struct(
        "BackupSetId" / Guid,
        "RestoreEventId" / Guid,
        "RestoreState" / Int32sl,
        "HRESULT" / Int32ul,
        "DetailedHRESULT" / Int32ul,
        "BackupTargetFriendlyName" / WString,
        "NumOfVolumes" / Int32ul,
        "VolumesInfo" / WString,
        "RestoreTime" / Int64ul,
        "PrepareRestoreTime" / Int32ul,
        "WriteRestoreTime" / Int32ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=196, version=1)
class Microsoft_Windows_Backup_196_1(Etw):
    pattern = Struct(
        "BackupSetId" / Guid,
        "BackupSetTime" / Int64ul,
        "RestoreEventId" / Guid,
        "RestoreState" / Int32sl,
        "HRESULT" / Int32ul,
        "DetailedHRESULT" / Int32ul,
        "BackupTargetFriendlyName" / WString,
        "NumOfVolumes" / Int32ul,
        "RestoreTime" / Int64ul,
        "VolumesInfo" / WString,
        "PrepareRestoreTime" / Int32ul,
        "WriteRestoreTime" / Int32ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=196, version=2)
class Microsoft_Windows_Backup_196_2(Etw):
    pattern = Struct(
        "BackupSetId" / Guid,
        "BackupSetTime" / Int64ul,
        "RestoreEventId" / Guid,
        "RestoreState" / Int32sl,
        "HRESULT" / Int32ul,
        "DetailedHRESULT" / Int32ul,
        "ErrorMessage" / WString,
        "BackupTargetFriendlyName" / WString,
        "NumOfVolumes" / Int32ul,
        "VolumesInfo" / WString,
        "PrepareRestoreTime" / Int32ul,
        "RestoreTime" / Int64ul,
        "WriteRestoreTime" / Int32ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=197, version=0)
class Microsoft_Windows_Backup_197_0(Etw):
    pattern = Struct(
        "BackupSetId" / Guid,
        "RestoreEventId" / Guid,
        "RestoreState" / Int32sl,
        "HRESULT" / Int32ul,
        "DetailedHRESULT" / Int32ul,
        "BackupTargetFriendlyName" / WString,
        "NumOfVolumes" / Int32ul,
        "VolumesInfo" / WString,
        "RestoreTime" / Int64ul,
        "PrepareRestoreTime" / Int32ul,
        "WriteRestoreTime" / Int32ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=197, version=1)
class Microsoft_Windows_Backup_197_1(Etw):
    pattern = Struct(
        "BackupSetId" / Guid,
        "BackupSetTime" / Int64ul,
        "RestoreEventId" / Guid,
        "RestoreState" / Int32sl,
        "HRESULT" / Int32ul,
        "DetailedHRESULT" / Int32ul,
        "BackupTargetFriendlyName" / WString,
        "NumOfVolumes" / Int32ul,
        "RestoreTime" / Int64ul,
        "VolumesInfo" / WString,
        "PrepareRestoreTime" / Int32ul,
        "WriteRestoreTime" / Int32ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=197, version=2)
class Microsoft_Windows_Backup_197_2(Etw):
    pattern = Struct(
        "BackupSetId" / Guid,
        "BackupSetTime" / Int64ul,
        "RestoreEventId" / Guid,
        "RestoreState" / Int32sl,
        "HRESULT" / Int32ul,
        "DetailedHRESULT" / Int32ul,
        "ErrorMessage" / WString,
        "BackupTargetFriendlyName" / WString,
        "NumOfVolumes" / Int32ul,
        "VolumesInfo" / WString,
        "PrepareRestoreTime" / Int32ul,
        "RestoreTime" / Int64ul,
        "WriteRestoreTime" / Int32ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=198, version=0)
class Microsoft_Windows_Backup_198_0(Etw):
    pattern = Struct(
        "VolumeFriendlyName" / WString,
        "VolumeAccessPath" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=199, version=0)
class Microsoft_Windows_Backup_199_0(Etw):
    pattern = Struct(
        "VolumeFriendlyName" / WString,
        "VolumeAccessPath" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=208, version=0)
class Microsoft_Windows_Backup_208_0(Etw):
    pattern = Struct(
        "BackupSetId" / Guid,
        "RestoreEventId" / Guid,
        "FileRestoreTargetPath" / WString,
        "RestoreState" / Int32sl,
        "HRESULT" / Int32ul,
        "DetailedHRESULT" / Int32ul,
        "NumOfFiles" / Int32ul,
        "FilesInfo" / WString,
        "RestoreTime" / Int64ul,
        "MountVhdTime" / Int32ul,
        "PreparePassTime" / Int32ul,
        "WriteFilesTime" / Int32ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=208, version=1)
class Microsoft_Windows_Backup_208_1(Etw):
    pattern = Struct(
        "BackupSetId" / Guid,
        "BackupSetTime" / Int64ul,
        "RestoreEventId" / Guid,
        "FileRestoreTargetPath" / WString,
        "RestoreState" / Int32sl,
        "HRESULT" / Int32ul,
        "DetailedHRESULT" / Int32ul,
        "NumOfFiles" / Int32ul,
        "FilesInfo" / WString,
        "RestoreTime" / Int64ul,
        "FileSuccessLogPath" / WString,
        "FileFailureLogPath" / WString,
        "MountVhdTime" / Int32ul,
        "PreparePassTime" / Int32ul,
        "WriteFilesTime" / Int32ul,
        "BackupLocation" / WString,
        "TotalDataTransferred" / Int64ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=208, version=2)
class Microsoft_Windows_Backup_208_2(Etw):
    pattern = Struct(
        "BackupSetId" / Guid,
        "BackupSetTime" / Int64ul,
        "RestoreEventId" / Guid,
        "FileRestoreTargetPath" / WString,
        "RestoreState" / Int32sl,
        "HRESULT" / Int32ul,
        "DetailedHRESULT" / Int32ul,
        "NumOfFiles" / Int32ul,
        "FilesInfo" / WString,
        "RestoreTime" / Int64ul,
        "FileSuccessLogPath" / WString,
        "FileFailureLogPath" / WString,
        "MountVhdTime" / Int32ul,
        "PreparePassTime" / Int32ul,
        "WriteFilesTime" / Int32ul,
        "BackupLocation" / WString,
        "TotalDataTransferred" / Int64ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=209, version=0)
class Microsoft_Windows_Backup_209_0(Etw):
    pattern = Struct(
        "BackupSetId" / Guid,
        "RestoreEventId" / Guid,
        "FileRestoreTargetPath" / WString,
        "RestoreState" / Int32sl,
        "HRESULT" / Int32ul,
        "DetailedHRESULT" / Int32ul,
        "NumOfFiles" / Int32ul,
        "FilesInfo" / WString,
        "RestoreTime" / Int64ul,
        "MountVhdTime" / Int32ul,
        "PreparePassTime" / Int32ul,
        "WriteFilesTime" / Int32ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=210, version=0)
class Microsoft_Windows_Backup_210_0(Etw):
    pattern = Struct(
        "BackupSetId" / Guid,
        "RestoreEventId" / Guid,
        "FileRestoreTargetPath" / WString,
        "RestoreState" / Int32sl,
        "HRESULT" / Int32ul,
        "DetailedHRESULT" / Int32ul,
        "NumOfFiles" / Int32ul,
        "FilesInfo" / WString,
        "RestoreTime" / Int64ul,
        "MountVhdTime" / Int32ul,
        "PreparePassTime" / Int32ul,
        "WriteFilesTime" / Int32ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=211, version=0)
class Microsoft_Windows_Backup_211_0(Etw):
    pattern = Struct(
        "BackupSetId" / Guid,
        "RestoreEventId" / Guid,
        "FileRestoreTargetPath" / WString,
        "RestoreState" / Int32sl,
        "HRESULT" / Int32ul,
        "DetailedHRESULT" / Int32ul,
        "NumOfFiles" / Int32ul,
        "FilesInfo" / WString,
        "RestoreTime" / Int64ul,
        "MountVhdTime" / Int32ul,
        "PreparePassTime" / Int32ul,
        "WriteFilesTime" / Int32ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=212, version=0)
class Microsoft_Windows_Backup_212_0(Etw):
    pattern = Struct(
        "BackupSetId" / Guid,
        "RestoreEventId" / Guid,
        "FileRestoreTargetPath" / WString,
        "RestoreState" / Int32sl,
        "HRESULT" / Int32ul,
        "DetailedHRESULT" / Int32ul,
        "NumOfFiles" / Int32ul,
        "FilesInfo" / WString,
        "RestoreTime" / Int64ul,
        "MountVhdTime" / Int32ul,
        "PreparePassTime" / Int32ul,
        "WriteFilesTime" / Int32ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=213, version=0)
class Microsoft_Windows_Backup_213_0(Etw):
    pattern = Struct(
        "BackupSetId" / Guid,
        "VolumeToMount" / Guid,
        "NeedNetworkShare" / Int8ul,
        "HRESULT" / Int32ul,
        "TimeTakenToMount" / Int32ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=213, version=1)
class Microsoft_Windows_Backup_213_1(Etw):
    pattern = Struct(
        "BackupSetId" / Guid,
        "VolumeToMount" / Guid,
        "NeedNetworkShare" / Int8ul,
        "HRESULT" / Int32ul,
        "TimeTakenToMount" / Int32ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=214, version=0)
class Microsoft_Windows_Backup_214_0(Etw):
    pattern = Struct(
        "BackupSetId" / Guid,
        "BackupSetTime" / Int64ul,
        "RestoreEventId" / Guid,
        "FileRestoreTargetPath" / WString,
        "RestoreState" / Int32sl,
        "HRESULT" / Int32ul,
        "DetailedHRESULT" / Int32ul,
        "NumOfFiles" / Int32ul,
        "FilesInfo" / WString,
        "RestoreTime" / Int64ul,
        "FileSuccessLogPath" / WString,
        "FileFailureLogPath" / WString,
        "MountVhdTime" / Int32ul,
        "PreparePassTime" / Int32ul,
        "WriteFilesTime" / Int32ul,
        "BackupLocation" / WString,
        "TotalDataTransferred" / Int64ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=214, version=1)
class Microsoft_Windows_Backup_214_1(Etw):
    pattern = Struct(
        "BackupSetId" / Guid,
        "BackupSetTime" / Int64ul,
        "RestoreEventId" / Guid,
        "FileRestoreTargetPath" / WString,
        "RestoreState" / Int32sl,
        "HRESULT" / Int32ul,
        "DetailedHRESULT" / Int32ul,
        "NumOfFiles" / Int32ul,
        "FilesInfo" / WString,
        "RestoreTime" / Int64ul,
        "FileSuccessLogPath" / WString,
        "FileFailureLogPath" / WString,
        "MountVhdTime" / Int32ul,
        "PreparePassTime" / Int32ul,
        "WriteFilesTime" / Int32ul,
        "BackupLocation" / WString,
        "TotalDataTransferred" / Int64ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=215, version=0)
class Microsoft_Windows_Backup_215_0(Etw):
    pattern = Struct(
        "BackupSetId" / Guid,
        "BackupSetTime" / Int64ul,
        "RestoreEventId" / Guid,
        "FileRestoreTargetPath" / WString,
        "RestoreState" / Int32sl,
        "HRESULT" / Int32ul,
        "DetailedHRESULT" / Int32ul,
        "NumOfFiles" / Int32ul,
        "FilesInfo" / WString,
        "RestoreTime" / Int64ul,
        "FileSuccessLogPath" / WString,
        "FileFailureLogPath" / WString,
        "MountVhdTime" / Int32ul,
        "PreparePassTime" / Int32ul,
        "WriteFilesTime" / Int32ul,
        "BackupLocation" / WString,
        "TotalDataTransferred" / Int64ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=215, version=1)
class Microsoft_Windows_Backup_215_1(Etw):
    pattern = Struct(
        "BackupSetId" / Guid,
        "BackupSetTime" / Int64ul,
        "RestoreEventId" / Guid,
        "FileRestoreTargetPath" / WString,
        "RestoreState" / Int32sl,
        "HRESULT" / Int32ul,
        "DetailedHRESULT" / Int32ul,
        "NumOfFiles" / Int32ul,
        "FilesInfo" / WString,
        "RestoreTime" / Int64ul,
        "FileSuccessLogPath" / WString,
        "FileFailureLogPath" / WString,
        "MountVhdTime" / Int32ul,
        "PreparePassTime" / Int32ul,
        "WriteFilesTime" / Int32ul,
        "BackupLocation" / WString,
        "TotalDataTransferred" / Int64ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=216, version=0)
class Microsoft_Windows_Backup_216_0(Etw):
    pattern = Struct(
        "BackupSetId" / Guid,
        "BackupSetTime" / Int64ul,
        "RestoreEventId" / Guid,
        "FileRestoreTargetPath" / WString,
        "RestoreState" / Int32sl,
        "HRESULT" / Int32ul,
        "DetailedHRESULT" / Int32ul,
        "NumOfFiles" / Int32ul,
        "FilesInfo" / WString,
        "RestoreTime" / Int64ul,
        "FileSuccessLogPath" / WString,
        "FileFailureLogPath" / WString,
        "MountVhdTime" / Int32ul,
        "PreparePassTime" / Int32ul,
        "WriteFilesTime" / Int32ul,
        "BackupLocation" / WString,
        "TotalDataTransferred" / Int64ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=216, version=1)
class Microsoft_Windows_Backup_216_1(Etw):
    pattern = Struct(
        "BackupSetId" / Guid,
        "BackupSetTime" / Int64ul,
        "RestoreEventId" / Guid,
        "FileRestoreTargetPath" / WString,
        "RestoreState" / Int32sl,
        "HRESULT" / Int32ul,
        "DetailedHRESULT" / Int32ul,
        "NumOfFiles" / Int32ul,
        "FilesInfo" / WString,
        "RestoreTime" / Int64ul,
        "FileSuccessLogPath" / WString,
        "FileFailureLogPath" / WString,
        "MountVhdTime" / Int32ul,
        "PreparePassTime" / Int32ul,
        "WriteFilesTime" / Int32ul,
        "BackupLocation" / WString,
        "TotalDataTransferred" / Int64ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=217, version=0)
class Microsoft_Windows_Backup_217_0(Etw):
    pattern = Struct(
        "BackupSetId" / Guid,
        "BackupSetTime" / Int64ul,
        "RestoreEventId" / Guid,
        "FileRestoreTargetPath" / WString,
        "RestoreState" / Int32sl,
        "HRESULT" / Int32ul,
        "DetailedHRESULT" / Int32ul,
        "NumOfFiles" / Int32ul,
        "FilesInfo" / WString,
        "RestoreTime" / Int64ul,
        "FileSuccessLogPath" / WString,
        "FileFailureLogPath" / WString,
        "MountVhdTime" / Int32ul,
        "PreparePassTime" / Int32ul,
        "WriteFilesTime" / Int32ul,
        "BackupLocation" / WString,
        "TotalDataTransferred" / Int64ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=217, version=1)
class Microsoft_Windows_Backup_217_1(Etw):
    pattern = Struct(
        "BackupSetId" / Guid,
        "BackupSetTime" / Int64ul,
        "RestoreEventId" / Guid,
        "FileRestoreTargetPath" / WString,
        "RestoreState" / Int32sl,
        "HRESULT" / Int32ul,
        "DetailedHRESULT" / Int32ul,
        "NumOfFiles" / Int32ul,
        "FilesInfo" / WString,
        "RestoreTime" / Int64ul,
        "FileSuccessLogPath" / WString,
        "FileFailureLogPath" / WString,
        "MountVhdTime" / Int32ul,
        "PreparePassTime" / Int32ul,
        "WriteFilesTime" / Int32ul,
        "BackupLocation" / WString,
        "TotalDataTransferred" / Int64ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=224, version=0)
class Microsoft_Windows_Backup_224_0(Etw):
    pattern = Struct(
        "BackupSetId" / Guid,
        "BackupSetTime" / Int64ul,
        "RestoreEventId" / Guid,
        "RecoveryFromSSB" / Int8ul,
        "BackupTargetPath" / WString,
        "AppRestoreAlternateTargetPath" / WString,
        "RestoreState" / Int32sl,
        "HRESULT" / Int32ul,
        "DetailedHRESULT" / Int32ul,
        "RestoreTime" / Int64ul,
        "NumOfComponents" / Int32ul,
        "FileSuccessLogPath" / WString,
        "FileFailureLogPath" / WString,
        "AppsInfo" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=224, version=1)
class Microsoft_Windows_Backup_224_1(Etw):
    pattern = Struct(
        "BackupSetId" / Guid,
        "BackupSetTime" / Int64ul,
        "RestoreEventId" / Guid,
        "RecoveryFromSSB" / Int8ul,
        "BackupTargetPath" / WString,
        "AppRestoreAlternateTargetPath" / WString,
        "RestoreState" / Int32sl,
        "HRESULT" / Int32ul,
        "DetailedHRESULT" / Int32ul,
        "RestoreTime" / Int64ul,
        "NumOfComponents" / Int32ul,
        "FileSuccessLogPath" / WString,
        "FileFailureLogPath" / WString,
        "AppsInfo" / WString,
        "AlternateLocationRecovery" / Int8ul,
        "RecreatePath" / Int8ul,
        "ComponentInfoSummary" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=225, version=0)
class Microsoft_Windows_Backup_225_0(Etw):
    pattern = Struct(
        "BackupSetId" / Guid,
        "BackupSetTime" / Int64ul,
        "RestoreEventId" / Guid,
        "RecoveryFromSSB" / Int8ul,
        "BackupTargetPath" / WString,
        "AppRestoreAlternateTargetPath" / WString,
        "RestoreState" / Int32sl,
        "HRESULT" / Int32ul,
        "DetailedHRESULT" / Int32ul,
        "RestoreTime" / Int64ul,
        "NumOfComponents" / Int32ul,
        "FileSuccessLogPath" / WString,
        "FileFailureLogPath" / WString,
        "AppsInfo" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=225, version=1)
class Microsoft_Windows_Backup_225_1(Etw):
    pattern = Struct(
        "BackupSetId" / Guid,
        "BackupSetTime" / Int64ul,
        "RestoreEventId" / Guid,
        "RecoveryFromSSB" / Int8ul,
        "BackupTargetPath" / WString,
        "AppRestoreAlternateTargetPath" / WString,
        "RestoreState" / Int32sl,
        "HRESULT" / Int32ul,
        "DetailedHRESULT" / Int32ul,
        "RestoreTime" / Int64ul,
        "NumOfComponents" / Int32ul,
        "FileSuccessLogPath" / WString,
        "FileFailureLogPath" / WString,
        "AppsInfo" / WString,
        "AlternateLocationRecovery" / Int8ul,
        "RecreatePath" / Int8ul,
        "ComponentInfoSummary" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=226, version=0)
class Microsoft_Windows_Backup_226_0(Etw):
    pattern = Struct(
        "BackupSetId" / Guid,
        "BackupSetTime" / Int64ul,
        "RestoreEventId" / Guid,
        "RecoveryFromSSB" / Int8ul,
        "BackupTargetPath" / WString,
        "AppRestoreAlternateTargetPath" / WString,
        "RestoreState" / Int32sl,
        "HRESULT" / Int32ul,
        "DetailedHRESULT" / Int32ul,
        "RestoreTime" / Int64ul,
        "NumOfComponents" / Int32ul,
        "FileSuccessLogPath" / WString,
        "FileFailureLogPath" / WString,
        "AppsInfo" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=226, version=1)
class Microsoft_Windows_Backup_226_1(Etw):
    pattern = Struct(
        "BackupSetId" / Guid,
        "BackupSetTime" / Int64ul,
        "RestoreEventId" / Guid,
        "RecoveryFromSSB" / Int8ul,
        "BackupTargetPath" / WString,
        "AppRestoreAlternateTargetPath" / WString,
        "RestoreState" / Int32sl,
        "HRESULT" / Int32ul,
        "DetailedHRESULT" / Int32ul,
        "RestoreTime" / Int64ul,
        "NumOfComponents" / Int32ul,
        "FileSuccessLogPath" / WString,
        "FileFailureLogPath" / WString,
        "AppsInfo" / WString,
        "AlternateLocationRecovery" / Int8ul,
        "RecreatePath" / Int8ul,
        "ComponentInfoSummary" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=227, version=0)
class Microsoft_Windows_Backup_227_0(Etw):
    pattern = Struct(
        "BackupSetId" / Guid,
        "BackupSetTime" / Int64ul,
        "RestoreEventId" / Guid,
        "RecoveryFromSSB" / Int8ul,
        "BackupTargetPath" / WString,
        "AppRestoreAlternateTargetPath" / WString,
        "RestoreState" / Int32sl,
        "HRESULT" / Int32ul,
        "DetailedHRESULT" / Int32ul,
        "RestoreTime" / Int64ul,
        "NumOfComponents" / Int32ul,
        "FileSuccessLogPath" / WString,
        "FileFailureLogPath" / WString,
        "AppsInfo" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=227, version=1)
class Microsoft_Windows_Backup_227_1(Etw):
    pattern = Struct(
        "BackupSetId" / Guid,
        "BackupSetTime" / Int64ul,
        "RestoreEventId" / Guid,
        "RecoveryFromSSB" / Int8ul,
        "BackupTargetPath" / WString,
        "AppRestoreAlternateTargetPath" / WString,
        "RestoreState" / Int32sl,
        "HRESULT" / Int32ul,
        "DetailedHRESULT" / Int32ul,
        "RestoreTime" / Int64ul,
        "NumOfComponents" / Int32ul,
        "FileSuccessLogPath" / WString,
        "FileFailureLogPath" / WString,
        "AppsInfo" / WString,
        "AlternateLocationRecovery" / Int8ul,
        "RecreatePath" / Int8ul,
        "ComponentInfoSummary" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=228, version=0)
class Microsoft_Windows_Backup_228_0(Etw):
    pattern = Struct(
        "BackupSetId" / Guid,
        "BackupSetTime" / Int64ul,
        "RestoreEventId" / Guid,
        "RecoveryFromSSB" / Int8ul,
        "BackupTargetPath" / WString,
        "AppRestoreAlternateTargetPath" / WString,
        "RestoreState" / Int32sl,
        "HRESULT" / Int32ul,
        "DetailedHRESULT" / Int32ul,
        "RestoreTime" / Int64ul,
        "NumOfComponents" / Int32ul,
        "FileSuccessLogPath" / WString,
        "FileFailureLogPath" / WString,
        "AppsInfo" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=228, version=1)
class Microsoft_Windows_Backup_228_1(Etw):
    pattern = Struct(
        "BackupSetId" / Guid,
        "BackupSetTime" / Int64ul,
        "RestoreEventId" / Guid,
        "RecoveryFromSSB" / Int8ul,
        "BackupTargetPath" / WString,
        "AppRestoreAlternateTargetPath" / WString,
        "RestoreState" / Int32sl,
        "HRESULT" / Int32ul,
        "DetailedHRESULT" / Int32ul,
        "RestoreTime" / Int64ul,
        "NumOfComponents" / Int32ul,
        "FileSuccessLogPath" / WString,
        "FileFailureLogPath" / WString,
        "AppsInfo" / WString,
        "AlternateLocationRecovery" / Int8ul,
        "RecreatePath" / Int8ul,
        "ComponentInfoSummary" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=240, version=0)
class Microsoft_Windows_Backup_240_0(Etw):
    pattern = Struct(
        "RestoreTime" / Int64ul,
        "BackupSetID" / Guid,
        "BackupSetTime" / Int64ul,
        "RestoreType" / Int32sl,
        "AlternateRestoreTarget" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=241, version=0)
class Microsoft_Windows_Backup_241_0(Etw):
    pattern = Struct(
        "RestoreTime" / Int64ul,
        "HRESULT" / Int32ul,
        "DetailedHRESULT" / Int32ul,
        "RestoreType" / Int32ul,
        "SysvolRestoreType" / Int32ul,
        "BackupSetID" / Guid,
        "BackupSetTime" / Int64ul,
        "NumOfVolumes" / Int32ul,
        "VolumesInfo" / WString,
        "NumOfWriters" / Int32ul,
        "WritersInfo" / WString,
        "NoOfFilesProcessed" / Int64ul,
        "NoOfFilesFailed" / Int64ul,
        "NoOfBytesProcessed" / Int64ul,
        "TotalNumOfBytes" / Int64ul,
        "EnumerateStartTime" / Int64ul,
        "EnumerateEndTime" / Int64ul,
        "RestoreStartTime" / Int64ul,
        "RestoreEndTime" / Int64ul,
        "DeleteStartTime" / Int64ul,
        "DeleteEndTime" / Int64ul,
        "RestoreSuccessLogPath" / WString,
        "RestoreFailureLogPath" / WString,
        "RestoreCLIOutputLogPath" / WString,
        "TargetAccessPath" / WString,
        "AlternateRecoveryPath" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=241, version=1)
class Microsoft_Windows_Backup_241_1(Etw):
    pattern = Struct(
        "RestoreTime" / Int64ul,
        "HRESULT" / Int32ul,
        "DetailedHRESULT" / Int32ul,
        "RestoreType" / Int32ul,
        "SysvolRestoreType" / Int32ul,
        "BackupSetID" / Guid,
        "BackupSetTime" / Int64ul,
        "NumOfVolumes" / Int32ul,
        "VolumesInfo" / WString,
        "NumOfWriters" / Int32ul,
        "WritersInfo" / WString,
        "NoOfFilesProcessed" / Int64ul,
        "NoOfFilesFailed" / Int64ul,
        "NoOfBytesProcessed" / Int64ul,
        "TotalNumOfBytes" / Int64ul,
        "EnumerateStartTime" / Int64ul,
        "EnumerateEndTime" / Int64ul,
        "RestoreStartTime" / Int64ul,
        "RestoreEndTime" / Int64ul,
        "DeleteStartTime" / Int64ul,
        "DeleteEndTime" / Int64ul,
        "RestoreSuccessLogPath" / WString,
        "RestoreFailureLogPath" / WString,
        "RestoreCLIOutputLogPath" / WString,
        "TargetAccessPath" / WString,
        "AlternateRecoveryPath" / WString,
        "ErrorMessage" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=242, version=0)
class Microsoft_Windows_Backup_242_0(Etw):
    pattern = Struct(
        "RestoreTime" / Int64ul,
        "HRESULT" / Int32ul,
        "DetailedHRESULT" / Int32ul,
        "RestoreType" / Int32ul,
        "SysvolRestoreType" / Int32ul,
        "BackupSetID" / Guid,
        "BackupSetTime" / Int64ul,
        "NumOfVolumes" / Int32ul,
        "VolumesInfo" / WString,
        "NumOfWriters" / Int32ul,
        "WritersInfo" / WString,
        "NoOfFilesProcessed" / Int64ul,
        "NoOfFilesFailed" / Int64ul,
        "NoOfBytesProcessed" / Int64ul,
        "TotalNumOfBytes" / Int64ul,
        "EnumerateStartTime" / Int64ul,
        "EnumerateEndTime" / Int64ul,
        "RestoreStartTime" / Int64ul,
        "RestoreEndTime" / Int64ul,
        "DeleteStartTime" / Int64ul,
        "DeleteEndTime" / Int64ul,
        "RestoreSuccessLogPath" / WString,
        "RestoreFailureLogPath" / WString,
        "RestoreCLIOutputLogPath" / WString,
        "TargetAccessPath" / WString,
        "AlternateRecoveryPath" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=242, version=1)
class Microsoft_Windows_Backup_242_1(Etw):
    pattern = Struct(
        "RestoreTime" / Int64ul,
        "HRESULT" / Int32ul,
        "DetailedHRESULT" / Int32ul,
        "RestoreType" / Int32ul,
        "SysvolRestoreType" / Int32ul,
        "BackupSetID" / Guid,
        "BackupSetTime" / Int64ul,
        "NumOfVolumes" / Int32ul,
        "VolumesInfo" / WString,
        "NumOfWriters" / Int32ul,
        "WritersInfo" / WString,
        "NoOfFilesProcessed" / Int64ul,
        "NoOfFilesFailed" / Int64ul,
        "NoOfBytesProcessed" / Int64ul,
        "TotalNumOfBytes" / Int64ul,
        "EnumerateStartTime" / Int64ul,
        "EnumerateEndTime" / Int64ul,
        "RestoreStartTime" / Int64ul,
        "RestoreEndTime" / Int64ul,
        "DeleteStartTime" / Int64ul,
        "DeleteEndTime" / Int64ul,
        "RestoreSuccessLogPath" / WString,
        "RestoreFailureLogPath" / WString,
        "RestoreCLIOutputLogPath" / WString,
        "TargetAccessPath" / WString,
        "AlternateRecoveryPath" / WString,
        "ErrorMessage" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=243, version=0)
class Microsoft_Windows_Backup_243_0(Etw):
    pattern = Struct(
        "RestoreTime" / Int64ul,
        "HRESULT" / Int32ul,
        "DetailedHRESULT" / Int32ul,
        "RestoreType" / Int32ul,
        "SysvolRestoreType" / Int32ul,
        "BackupSetID" / Guid,
        "BackupSetTime" / Int64ul,
        "NumOfVolumes" / Int32ul,
        "VolumesInfo" / WString,
        "NumOfWriters" / Int32ul,
        "WritersInfo" / WString,
        "NoOfFilesProcessed" / Int64ul,
        "NoOfFilesFailed" / Int64ul,
        "NoOfBytesProcessed" / Int64ul,
        "TotalNumOfBytes" / Int64ul,
        "EnumerateStartTime" / Int64ul,
        "EnumerateEndTime" / Int64ul,
        "RestoreStartTime" / Int64ul,
        "RestoreEndTime" / Int64ul,
        "DeleteStartTime" / Int64ul,
        "DeleteEndTime" / Int64ul,
        "RestoreSuccessLogPath" / WString,
        "RestoreFailureLogPath" / WString,
        "RestoreCLIOutputLogPath" / WString,
        "TargetAccessPath" / WString,
        "AlternateRecoveryPath" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=243, version=1)
class Microsoft_Windows_Backup_243_1(Etw):
    pattern = Struct(
        "RestoreTime" / Int64ul,
        "HRESULT" / Int32ul,
        "DetailedHRESULT" / Int32ul,
        "RestoreType" / Int32ul,
        "SysvolRestoreType" / Int32ul,
        "BackupSetID" / Guid,
        "BackupSetTime" / Int64ul,
        "NumOfVolumes" / Int32ul,
        "VolumesInfo" / WString,
        "NumOfWriters" / Int32ul,
        "WritersInfo" / WString,
        "NoOfFilesProcessed" / Int64ul,
        "NoOfFilesFailed" / Int64ul,
        "NoOfBytesProcessed" / Int64ul,
        "TotalNumOfBytes" / Int64ul,
        "EnumerateStartTime" / Int64ul,
        "EnumerateEndTime" / Int64ul,
        "RestoreStartTime" / Int64ul,
        "RestoreEndTime" / Int64ul,
        "DeleteStartTime" / Int64ul,
        "DeleteEndTime" / Int64ul,
        "RestoreSuccessLogPath" / WString,
        "RestoreFailureLogPath" / WString,
        "RestoreCLIOutputLogPath" / WString,
        "TargetAccessPath" / WString,
        "AlternateRecoveryPath" / WString,
        "ErrorMessage" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=244, version=0)
class Microsoft_Windows_Backup_244_0(Etw):
    pattern = Struct(
        "RestoreTime" / Int64ul,
        "HRESULT" / Int32ul,
        "DetailedHRESULT" / Int32ul,
        "RestoreType" / Int32ul,
        "SysvolRestoreType" / Int32ul,
        "BackupSetID" / Guid,
        "BackupSetTime" / Int64ul,
        "NumOfVolumes" / Int32ul,
        "VolumesInfo" / WString,
        "NumOfWriters" / Int32ul,
        "WritersInfo" / WString,
        "NoOfFilesProcessed" / Int64ul,
        "NoOfFilesFailed" / Int64ul,
        "NoOfBytesProcessed" / Int64ul,
        "TotalNumOfBytes" / Int64ul,
        "EnumerateStartTime" / Int64ul,
        "EnumerateEndTime" / Int64ul,
        "RestoreStartTime" / Int64ul,
        "RestoreEndTime" / Int64ul,
        "DeleteStartTime" / Int64ul,
        "DeleteEndTime" / Int64ul,
        "RestoreSuccessLogPath" / WString,
        "RestoreFailureLogPath" / WString,
        "RestoreCLIOutputLogPath" / WString,
        "TargetAccessPath" / WString,
        "AlternateRecoveryPath" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=244, version=1)
class Microsoft_Windows_Backup_244_1(Etw):
    pattern = Struct(
        "RestoreTime" / Int64ul,
        "HRESULT" / Int32ul,
        "DetailedHRESULT" / Int32ul,
        "RestoreType" / Int32ul,
        "SysvolRestoreType" / Int32ul,
        "BackupSetID" / Guid,
        "BackupSetTime" / Int64ul,
        "NumOfVolumes" / Int32ul,
        "VolumesInfo" / WString,
        "NumOfWriters" / Int32ul,
        "WritersInfo" / WString,
        "NoOfFilesProcessed" / Int64ul,
        "NoOfFilesFailed" / Int64ul,
        "NoOfBytesProcessed" / Int64ul,
        "TotalNumOfBytes" / Int64ul,
        "EnumerateStartTime" / Int64ul,
        "EnumerateEndTime" / Int64ul,
        "RestoreStartTime" / Int64ul,
        "RestoreEndTime" / Int64ul,
        "DeleteStartTime" / Int64ul,
        "DeleteEndTime" / Int64ul,
        "RestoreSuccessLogPath" / WString,
        "RestoreFailureLogPath" / WString,
        "RestoreCLIOutputLogPath" / WString,
        "TargetAccessPath" / WString,
        "AlternateRecoveryPath" / WString,
        "ErrorMessage" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=245, version=0)
class Microsoft_Windows_Backup_245_0(Etw):
    pattern = Struct(
        "RestoreTime" / Int64ul,
        "HRESULT" / Int32ul,
        "DetailedHRESULT" / Int32ul,
        "RestoreType" / Int32ul,
        "SysvolRestoreType" / Int32ul,
        "BackupSetID" / Guid,
        "BackupSetTime" / Int64ul,
        "NumOfVolumes" / Int32ul,
        "VolumesInfo" / WString,
        "NumOfWriters" / Int32ul,
        "WritersInfo" / WString,
        "NoOfFilesProcessed" / Int64ul,
        "NoOfFilesFailed" / Int64ul,
        "NoOfBytesProcessed" / Int64ul,
        "TotalNumOfBytes" / Int64ul,
        "EnumerateStartTime" / Int64ul,
        "EnumerateEndTime" / Int64ul,
        "RestoreStartTime" / Int64ul,
        "RestoreEndTime" / Int64ul,
        "DeleteStartTime" / Int64ul,
        "DeleteEndTime" / Int64ul,
        "RestoreSuccessLogPath" / WString,
        "RestoreFailureLogPath" / WString,
        "RestoreCLIOutputLogPath" / WString,
        "TargetAccessPath" / WString,
        "AlternateRecoveryPath" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=245, version=1)
class Microsoft_Windows_Backup_245_1(Etw):
    pattern = Struct(
        "RestoreTime" / Int64ul,
        "HRESULT" / Int32ul,
        "DetailedHRESULT" / Int32ul,
        "RestoreType" / Int32ul,
        "SysvolRestoreType" / Int32ul,
        "BackupSetID" / Guid,
        "BackupSetTime" / Int64ul,
        "NumOfVolumes" / Int32ul,
        "VolumesInfo" / WString,
        "NumOfWriters" / Int32ul,
        "WritersInfo" / WString,
        "NoOfFilesProcessed" / Int64ul,
        "NoOfFilesFailed" / Int64ul,
        "NoOfBytesProcessed" / Int64ul,
        "TotalNumOfBytes" / Int64ul,
        "EnumerateStartTime" / Int64ul,
        "EnumerateEndTime" / Int64ul,
        "RestoreStartTime" / Int64ul,
        "RestoreEndTime" / Int64ul,
        "DeleteStartTime" / Int64ul,
        "DeleteEndTime" / Int64ul,
        "RestoreSuccessLogPath" / WString,
        "RestoreFailureLogPath" / WString,
        "RestoreCLIOutputLogPath" / WString,
        "TargetAccessPath" / WString,
        "AlternateRecoveryPath" / WString,
        "ErrorMessage" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=517, version=0)
class Microsoft_Windows_Backup_517_0(Etw):
    pattern = Struct(
        "BackupTime" / Int64ul,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=517, version=1)
class Microsoft_Windows_Backup_517_1(Etw):
    pattern = Struct(
        "BackupTime" / Int64ul,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=518, version=0)
class Microsoft_Windows_Backup_518_0(Etw):
    pattern = Struct(
        "BackupTime" / Int64ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=518, version=1)
class Microsoft_Windows_Backup_518_1(Etw):
    pattern = Struct(
        "BackupTime" / Int64ul,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=519, version=0)
class Microsoft_Windows_Backup_519_0(Etw):
    pattern = Struct(
        "BackupTime" / Int64ul,
        "FailedVolumeNames" / WString,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=519, version=1)
class Microsoft_Windows_Backup_519_1(Etw):
    pattern = Struct(
        "BackupTime" / Int64ul,
        "FailedVolumeNames" / WString,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=521, version=0)
class Microsoft_Windows_Backup_521_0(Etw):
    pattern = Struct(
        "BackupTime" / Int64ul,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=521, version=2)
class Microsoft_Windows_Backup_521_2(Etw):
    pattern = Struct(
        "BackupTime" / Int64ul,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=522, version=0)
class Microsoft_Windows_Backup_522_0(Etw):
    pattern = Struct(
        "BackupTargetFriendlyName" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=523, version=0)
class Microsoft_Windows_Backup_523_0(Etw):
    pattern = Struct(
        "BackupTarget" / WString,
        "MachineName" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=525, version=0)
class Microsoft_Windows_Backup_525_0(Etw):
    pattern = Struct(
        "VolumeGuid" / Guid,
        "VolumeFriendlyName" / WString,
        "BackupSourceNumUnreadableBytes" / Int64sl
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=526, version=0)
class Microsoft_Windows_Backup_526_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=527, version=0)
class Microsoft_Windows_Backup_527_0(Etw):
    pattern = Struct(
        "BackupTime" / Int64ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=527, version=1)
class Microsoft_Windows_Backup_527_1(Etw):
    pattern = Struct(
        "BackupTime" / Int64ul,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=528, version=1)
class Microsoft_Windows_Backup_528_1(Etw):
    pattern = Struct(
        "BackupTime" / Int64ul,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=528, version=2)
class Microsoft_Windows_Backup_528_2(Etw):
    pattern = Struct(
        "BackupTime" / Int64ul,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=544, version=0)
class Microsoft_Windows_Backup_544_0(Etw):
    pattern = Struct(
        "BackupTime" / Int64ul,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=545, version=0)
class Microsoft_Windows_Backup_545_0(Etw):
    pattern = Struct(
        "BackupTime" / Int64ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=546, version=0)
class Microsoft_Windows_Backup_546_0(Etw):
    pattern = Struct(
        "BackupTime" / Int64ul,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=547, version=0)
class Microsoft_Windows_Backup_547_0(Etw):
    pattern = Struct(
        "BackupTime" / Int64ul,
        "FailedVolumeNames" / WString,
        "BackupFailureLogPath" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=561, version=0)
class Microsoft_Windows_Backup_561_0(Etw):
    pattern = Struct(
        "BackupTime" / Int64ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=564, version=0)
class Microsoft_Windows_Backup_564_0(Etw):
    pattern = Struct(
        "BackupTime" / Int64ul,
        "BackupTargetFriendlyName" / WString,
        "BackupUserName" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=565, version=0)
class Microsoft_Windows_Backup_565_0(Etw):
    pattern = Struct(
        "ComponentName" / WString,
        "LogicalPath" / WString,
        "ApplicationId" / WString,
        "BackupTime" / Int64ul,
        "WriterId" / Guid,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=608, version=0)
class Microsoft_Windows_Backup_608_0(Etw):
    pattern = Struct(
        "BackupTargetList" / WString,
        "BackupTime" / Int64ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=609, version=0)
class Microsoft_Windows_Backup_609_0(Etw):
    pattern = Struct(
        "BackupTargetList" / WString,
        "BackupTime" / Int64ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=611, version=0)
class Microsoft_Windows_Backup_611_0(Etw):
    pattern = Struct(
        "BackupTargetList" / WString,
        "BackupTime" / Int64ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=658, version=0)
class Microsoft_Windows_Backup_658_0(Etw):
    pattern = Struct(
        "BackupTargetFriendlyName" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=704, version=0)
class Microsoft_Windows_Backup_704_0(Etw):
    pattern = Struct(
        "RestoreTargetNameList" / WString,
        "RestoreTime" / Int64ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=706, version=0)
class Microsoft_Windows_Backup_706_0(Etw):
    pattern = Struct(
        "RestoreTargetNameList" / WString,
        "RestoreTime" / Int64ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=707, version=0)
class Microsoft_Windows_Backup_707_0(Etw):
    pattern = Struct(
        "RestoreTargetNameList" / WString,
        "RestoreTime" / Int64ul,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=707, version=1)
class Microsoft_Windows_Backup_707_1(Etw):
    pattern = Struct(
        "RestoreTargetNameList" / WString,
        "RestoreTime" / Int64ul,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=708, version=0)
class Microsoft_Windows_Backup_708_0(Etw):
    pattern = Struct(
        "RestoreTargetNameList" / WString,
        "RestoreTime" / Int64ul,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=708, version=1)
class Microsoft_Windows_Backup_708_1(Etw):
    pattern = Struct(
        "RestoreTargetNameList" / WString,
        "RestoreTime" / Int64ul,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=709, version=0)
class Microsoft_Windows_Backup_709_0(Etw):
    pattern = Struct(
        "RestoreTargetNameList" / WString,
        "RestoreTime" / Int64ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=710, version=0)
class Microsoft_Windows_Backup_710_0(Etw):
    pattern = Struct(
        "RestoreTargetNameList" / WString,
        "RestoreTime" / Int64ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=711, version=0)
class Microsoft_Windows_Backup_711_0(Etw):
    pattern = Struct(
        "RestoreTargetNameList" / WString,
        "RestoreTime" / Int64ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=721, version=0)
class Microsoft_Windows_Backup_721_0(Etw):
    pattern = Struct(
        "RestoreTargetNameList" / WString,
        "RestoreTime" / Int64ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=722, version=0)
class Microsoft_Windows_Backup_722_0(Etw):
    pattern = Struct(
        "RestoreTargetNameList" / WString,
        "RestoreTime" / Int64ul,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=722, version=1)
class Microsoft_Windows_Backup_722_1(Etw):
    pattern = Struct(
        "RestoreTargetNameList" / WString,
        "RestoreTime" / Int64ul,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=723, version=0)
class Microsoft_Windows_Backup_723_0(Etw):
    pattern = Struct(
        "RestoreTargetNameList" / WString,
        "RestoreTime" / Int64ul,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=723, version=1)
class Microsoft_Windows_Backup_723_1(Etw):
    pattern = Struct(
        "RestoreTargetNameList" / WString,
        "RestoreTime" / Int64ul,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=724, version=0)
class Microsoft_Windows_Backup_724_0(Etw):
    pattern = Struct(
        "RestoreTargetNameList" / WString,
        "RestoreTime" / Int64ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=737, version=0)
class Microsoft_Windows_Backup_737_0(Etw):
    pattern = Struct(
        "RestoreTargetNameList" / WString,
        "RestoreTime" / Int64ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=738, version=0)
class Microsoft_Windows_Backup_738_0(Etw):
    pattern = Struct(
        "RestoreTargetNameList" / WString,
        "RestoreTime" / Int64ul,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=738, version=1)
class Microsoft_Windows_Backup_738_1(Etw):
    pattern = Struct(
        "RestoreTargetNameList" / WString,
        "RestoreTime" / Int64ul,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=739, version=0)
class Microsoft_Windows_Backup_739_0(Etw):
    pattern = Struct(
        "RestoreTargetNameList" / WString,
        "RestoreTime" / Int64ul,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=739, version=1)
class Microsoft_Windows_Backup_739_1(Etw):
    pattern = Struct(
        "RestoreTargetNameList" / WString,
        "RestoreTime" / Int64ul,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=740, version=0)
class Microsoft_Windows_Backup_740_0(Etw):
    pattern = Struct(
        "RestoreTargetNameList" / WString,
        "RestoreTime" / Int64ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=755, version=0)
class Microsoft_Windows_Backup_755_0(Etw):
    pattern = Struct(
        "HandleInstallErrorCode" / Int32ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=756, version=0)
class Microsoft_Windows_Backup_756_0(Etw):
    pattern = Struct(
        "UnknownRequestCode" / Int32ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=769, version=0)
class Microsoft_Windows_Backup_769_0(Etw):
    pattern = Struct(
        "RestoreTime" / Int64ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=770, version=0)
class Microsoft_Windows_Backup_770_0(Etw):
    pattern = Struct(
        "RestoreTime" / Int64ul,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=770, version=1)
class Microsoft_Windows_Backup_770_1(Etw):
    pattern = Struct(
        "RestoreTime" / Int64ul,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=771, version=0)
class Microsoft_Windows_Backup_771_0(Etw):
    pattern = Struct(
        "RestoreTime" / Int64ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=772, version=0)
class Microsoft_Windows_Backup_772_0(Etw):
    pattern = Struct(
        "RestoreTime" / Int64ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=773, version=0)
class Microsoft_Windows_Backup_773_0(Etw):
    pattern = Struct(
        "RestoreTime" / Int64ul,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=773, version=1)
class Microsoft_Windows_Backup_773_1(Etw):
    pattern = Struct(
        "RestoreTime" / Int64ul,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=774, version=0)
class Microsoft_Windows_Backup_774_0(Etw):
    pattern = Struct(
        "RestoreTime" / Int64ul,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=774, version=1)
class Microsoft_Windows_Backup_774_1(Etw):
    pattern = Struct(
        "RestoreTime" / Int64ul,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=1025, version=1)
class Microsoft_Windows_Backup_1025_1(Etw):
    pattern = Struct(
        "BackupSetId" / Guid,
        "BackupSetTime" / Int64ul,
        "RestoreEventId" / Guid,
        "RecoveryFromSSB" / Int8ul,
        "BackupTargetPath" / WString,
        "AppRestoreAlternateTargetPath" / WString,
        "RestoreState" / Int32sl,
        "HRESULT" / Int32ul,
        "DetailedHRESULT" / Int32ul,
        "RestoreTime" / Int64ul,
        "NumOfComponents" / Int32ul,
        "FileSuccessLogPath" / WString,
        "FileFailureLogPath" / WString,
        "AppsInfo" / WString,
        "AlternateLocationRecovery" / Int8ul,
        "RecreatePath" / Int8ul,
        "ComponentInfoSummary" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=1026, version=1)
class Microsoft_Windows_Backup_1026_1(Etw):
    pattern = Struct(
        "BackupSetId" / Guid,
        "BackupSetTime" / Int64ul,
        "RestoreEventId" / Guid,
        "RecoveryFromSSB" / Int8ul,
        "BackupTargetPath" / WString,
        "AppRestoreAlternateTargetPath" / WString,
        "RestoreState" / Int32sl,
        "HRESULT" / Int32ul,
        "DetailedHRESULT" / Int32ul,
        "RestoreTime" / Int64ul,
        "NumOfComponents" / Int32ul,
        "FileSuccessLogPath" / WString,
        "FileFailureLogPath" / WString,
        "AppsInfo" / WString,
        "AlternateLocationRecovery" / Int8ul,
        "RecreatePath" / Int8ul,
        "ComponentInfoSummary" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=1027, version=1)
class Microsoft_Windows_Backup_1027_1(Etw):
    pattern = Struct(
        "BackupSetId" / Guid,
        "BackupSetTime" / Int64ul,
        "RestoreEventId" / Guid,
        "RecoveryFromSSB" / Int8ul,
        "BackupTargetPath" / WString,
        "AppRestoreAlternateTargetPath" / WString,
        "RestoreState" / Int32sl,
        "HRESULT" / Int32ul,
        "DetailedHRESULT" / Int32ul,
        "RestoreTime" / Int64ul,
        "NumOfComponents" / Int32ul,
        "FileSuccessLogPath" / WString,
        "FileFailureLogPath" / WString,
        "AppsInfo" / WString,
        "AlternateLocationRecovery" / Int8ul,
        "RecreatePath" / Int8ul,
        "ComponentInfoSummary" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=1028, version=1)
class Microsoft_Windows_Backup_1028_1(Etw):
    pattern = Struct(
        "BackupSetId" / Guid,
        "BackupSetTime" / Int64ul,
        "RestoreEventId" / Guid,
        "RecoveryFromSSB" / Int8ul,
        "BackupTargetPath" / WString,
        "AppRestoreAlternateTargetPath" / WString,
        "RestoreState" / Int32sl,
        "HRESULT" / Int32ul,
        "DetailedHRESULT" / Int32ul,
        "RestoreTime" / Int64ul,
        "NumOfComponents" / Int32ul,
        "FileSuccessLogPath" / WString,
        "FileFailureLogPath" / WString,
        "AppsInfo" / WString,
        "AlternateLocationRecovery" / Int8ul,
        "RecreatePath" / Int8ul,
        "ComponentInfoSummary" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=1029, version=1)
class Microsoft_Windows_Backup_1029_1(Etw):
    pattern = Struct(
        "BackupSetId" / Guid,
        "BackupSetTime" / Int64ul,
        "RestoreEventId" / Guid,
        "RecoveryFromSSB" / Int8ul,
        "BackupTargetPath" / WString,
        "AppRestoreAlternateTargetPath" / WString,
        "RestoreState" / Int32sl,
        "HRESULT" / Int32ul,
        "DetailedHRESULT" / Int32ul,
        "RestoreTime" / Int64ul,
        "NumOfComponents" / Int32ul,
        "FileSuccessLogPath" / WString,
        "FileFailureLogPath" / WString,
        "AppsInfo" / WString,
        "AlternateLocationRecovery" / Int8ul,
        "RecreatePath" / Int8ul,
        "ComponentInfoSummary" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=1040, version=0)
class Microsoft_Windows_Backup_1040_0(Etw):
    pattern = Struct(
        "RestoreTargetNameList" / WString,
        "RestoreTime" / Int64ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=1041, version=1)
class Microsoft_Windows_Backup_1041_1(Etw):
    pattern = Struct(
        "RestoreTargetNameList" / WString,
        "RestoreTime" / Int64ul,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=1042, version=1)
class Microsoft_Windows_Backup_1042_1(Etw):
    pattern = Struct(
        "RestoreTargetNameList" / WString,
        "RestoreTime" / Int64ul,
        "ErrorCode" / Int32ul,
        "ErrorMessage" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=1043, version=0)
class Microsoft_Windows_Backup_1043_0(Etw):
    pattern = Struct(
        "RestoreTargetNameList" / WString,
        "RestoreTime" / Int64ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=1044, version=1)
class Microsoft_Windows_Backup_1044_1(Etw):
    pattern = Struct(
        "ResourceDll" / WString,
        "SnapinId" / Guid,
        "ProviderNameId" / Int32ul,
        "ProviderIconId" / Int32ul
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=1281, version=1)
class Microsoft_Windows_Backup_1281_1(Etw):
    pattern = Struct(
        "SnapinId" / Guid,
        "StatusInfo" / WString
    )


@declare(guid=guid("1db28f2e-8f80-4027-8c5a-a11f7f10f62d"), event_id=1282, version=1)
class Microsoft_Windows_Backup_1282_1(Etw):
    pattern = Struct(
        "ResourceDll" / WString,
        "SnapinId" / Guid,
        "ProviderNameId" / Int32ul,
        "ProviderIconId" / Int32ul
    )

