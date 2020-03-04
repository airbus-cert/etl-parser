# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Diagnostics-Performance
GUID : cfc18ec0-96b1-4eba-961b-622caee05b0a
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=100, version=1)
class Microsoft_Windows_Diagnostics_Performance_100_1(Etw):
    pattern = Struct(
        "BootTsVersion" / Int32ul,
        "BootStartTime" / Int64ul,
        "BootEndTime" / Int64ul,
        "SystemBootInstance" / Int32ul,
        "UserBootInstance" / Int32ul,
        "BootTime" / Int32ul,
        "MainPathBootTime" / Int32ul,
        "BootKernelInitTime" / Int32ul,
        "BootDriverInitTime" / Int32ul,
        "BootDevicesInitTime" / Int32ul,
        "BootPrefetchInitTime" / Int32ul,
        "BootPrefetchBytes" / Int32ul,
        "BootAutoChkTime" / Int32ul,
        "BootSmssInitTime" / Int32ul,
        "BootCriticalServicesInitTime" / Int32ul,
        "BootUserProfileProcessingTime" / Int32ul,
        "BootMachineProfileProcessingTime" / Int32ul,
        "BootExplorerInitTime" / Int32ul,
        "BootNumStartupApps" / Int32ul,
        "BootPostBootTime" / Int32ul,
        "BootIsRebootAfterInstall" / Int8ul,
        "BootRootCauseStepImprovementBits" / Int32ul,
        "BootRootCauseGradualImprovementBits" / Int32ul,
        "BootRootCauseStepDegradationBits" / Int32ul,
        "BootRootCauseGradualDegradationBits" / Int32ul,
        "BootIsDegradation" / Int8ul,
        "BootIsStepDegradation" / Int8ul,
        "BootIsGradualDegradation" / Int8ul,
        "BootImprovementDelta" / Int32ul,
        "BootDegradationDelta" / Int32ul,
        "BootIsRootCauseIdentified" / Int8ul
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=100, version=2)
class Microsoft_Windows_Diagnostics_Performance_100_2(Etw):
    pattern = Struct(
        "BootTsVersion" / Int32ul,
        "BootStartTime" / Int64ul,
        "BootEndTime" / Int64ul,
        "SystemBootInstance" / Int32ul,
        "UserBootInstance" / Int32ul,
        "BootTime" / Int32ul,
        "MainPathBootTime" / Int32ul,
        "BootKernelInitTime" / Int32ul,
        "BootDriverInitTime" / Int32ul,
        "BootDevicesInitTime" / Int32ul,
        "BootPrefetchInitTime" / Int32ul,
        "BootPrefetchBytes" / Int32ul,
        "BootAutoChkTime" / Int32ul,
        "BootSmssInitTime" / Int32ul,
        "BootCriticalServicesInitTime" / Int32ul,
        "BootUserProfileProcessingTime" / Int32ul,
        "BootMachineProfileProcessingTime" / Int32ul,
        "BootExplorerInitTime" / Int32ul,
        "BootNumStartupApps" / Int32ul,
        "BootPostBootTime" / Int32ul,
        "BootIsRebootAfterInstall" / Int8ul,
        "BootRootCauseStepImprovementBits" / Int32ul,
        "BootRootCauseGradualImprovementBits" / Int32ul,
        "BootRootCauseStepDegradationBits" / Int32ul,
        "BootRootCauseGradualDegradationBits" / Int32ul,
        "BootIsDegradation" / Int8ul,
        "BootIsStepDegradation" / Int8ul,
        "BootIsGradualDegradation" / Int8ul,
        "BootImprovementDelta" / Int32ul,
        "BootDegradationDelta" / Int32ul,
        "BootIsRootCauseIdentified" / Int8ul,
        "OSLoaderDuration" / Int32ul,
        "BootPNPInitStartTimeMS" / Int32ul,
        "BootPNPInitDuration" / Int32ul,
        "OtherKernelInitDuration" / Int32ul,
        "SystemPNPInitStartTimeMS" / Int32ul,
        "SystemPNPInitDuration" / Int32ul,
        "SessionInitStartTimeMS" / Int32ul,
        "Session0InitDuration" / Int32ul,
        "Session1InitDuration" / Int32ul,
        "SessionInitOtherDuration" / Int32ul,
        "WinLogonStartTimeMS" / Int32ul,
        "OtherLogonInitActivityDuration" / Int32ul,
        "UserLogonWaitDuration" / Int32ul
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=101, version=1)
class Microsoft_Windows_Diagnostics_Performance_101_1(Etw):
    pattern = Struct(
        "StartTime" / Int64ul,
        "NameLength" / Int32ul,
        "Name" / Bytes(lambda this: this.NameLength),
        "FriendlyNameLength" / Int32ul,
        "FriendlyName" / Bytes(lambda this: this.FriendlyNameLength),
        "VersionLength" / Int32ul,
        "Version" / Bytes(lambda this: this.VersionLength),
        "TotalTime" / Int32ul,
        "DegradationTime" / Int32ul,
        "PathLength" / Int32ul,
        "Path" / Bytes(lambda this: this.PathLength),
        "ProductNameLength" / Int32ul,
        "ProductName" / Bytes(lambda this: this.ProductNameLength),
        "CompanyNameLength" / Int32ul,
        "CompanyName" / Bytes(lambda this: this.CompanyNameLength)
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=102, version=1)
class Microsoft_Windows_Diagnostics_Performance_102_1(Etw):
    pattern = Struct(
        "StartTime" / Int64ul,
        "NameLength" / Int32ul,
        "Name" / Bytes(lambda this: this.NameLength),
        "FriendlyNameLength" / Int32ul,
        "FriendlyName" / Bytes(lambda this: this.FriendlyNameLength),
        "VersionLength" / Int32ul,
        "Version" / Bytes(lambda this: this.VersionLength),
        "TotalTime" / Int32ul,
        "DegradationTime" / Int32ul,
        "PathLength" / Int32ul,
        "Path" / Bytes(lambda this: this.PathLength),
        "ProductNameLength" / Int32ul,
        "ProductName" / Bytes(lambda this: this.ProductNameLength),
        "CompanyNameLength" / Int32ul,
        "CompanyName" / Bytes(lambda this: this.CompanyNameLength)
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=103, version=1)
class Microsoft_Windows_Diagnostics_Performance_103_1(Etw):
    pattern = Struct(
        "StartTime" / Int64ul,
        "NameLength" / Int32ul,
        "Name" / Bytes(lambda this: this.NameLength),
        "FriendlyNameLength" / Int32ul,
        "FriendlyName" / Bytes(lambda this: this.FriendlyNameLength),
        "VersionLength" / Int32ul,
        "Version" / Bytes(lambda this: this.VersionLength),
        "TotalTime" / Int32ul,
        "DegradationTime" / Int32ul,
        "PathLength" / Int32ul,
        "Path" / Bytes(lambda this: this.PathLength),
        "ProductNameLength" / Int32ul,
        "ProductName" / Bytes(lambda this: this.ProductNameLength),
        "CompanyNameLength" / Int32ul,
        "CompanyName" / Bytes(lambda this: this.CompanyNameLength)
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=104, version=1)
class Microsoft_Windows_Diagnostics_Performance_104_1(Etw):
    pattern = Struct(
        "StartTime" / Int64ul,
        "NameLength" / Int32ul,
        "Name" / Bytes(lambda this: this.NameLength),
        "TotalTime" / Int32ul,
        "DegradationTime" / Int32ul
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=105, version=1)
class Microsoft_Windows_Diagnostics_Performance_105_1(Etw):
    pattern = Struct(
        "StartTime" / Int64ul,
        "NameLength" / Int32ul,
        "Name" / Bytes(lambda this: this.NameLength),
        "TotalTime" / Int32ul,
        "DegradationTime" / Int32ul
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=106, version=1)
class Microsoft_Windows_Diagnostics_Performance_106_1(Etw):
    pattern = Struct(
        "StartTime" / Int64ul,
        "NameLength" / Int32ul,
        "Name" / Bytes(lambda this: this.NameLength),
        "TotalTime" / Int32ul,
        "DegradationTime" / Int32ul
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=107, version=1)
class Microsoft_Windows_Diagnostics_Performance_107_1(Etw):
    pattern = Struct(
        "StartTime" / Int64ul,
        "NameLength" / Int32ul,
        "Name" / Bytes(lambda this: this.NameLength),
        "TotalTime" / Int32ul,
        "DegradationTime" / Int32ul
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=108, version=1)
class Microsoft_Windows_Diagnostics_Performance_108_1(Etw):
    pattern = Struct(
        "StartTime" / Int64ul,
        "NameLength" / Int32ul,
        "Name" / Bytes(lambda this: this.NameLength),
        "TotalTime" / Int32ul,
        "DegradationTime" / Int32ul
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=109, version=1)
class Microsoft_Windows_Diagnostics_Performance_109_1(Etw):
    pattern = Struct(
        "StartTime" / Int64ul,
        "NameLength" / Int32ul,
        "Name" / Bytes(lambda this: this.NameLength),
        "FriendlyNameLength" / Int32ul,
        "FriendlyName" / Bytes(lambda this: this.FriendlyNameLength),
        "VersionLength" / Int32ul,
        "Version" / Bytes(lambda this: this.VersionLength),
        "TotalTime" / Int32ul,
        "DegradationTime" / Int32ul,
        "PathLength" / Int32ul,
        "Path" / Bytes(lambda this: this.PathLength),
        "ProductNameLength" / Int32ul,
        "ProductName" / Bytes(lambda this: this.ProductNameLength),
        "CompanyNameLength" / Int32ul,
        "CompanyName" / Bytes(lambda this: this.CompanyNameLength)
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=110, version=1)
class Microsoft_Windows_Diagnostics_Performance_110_1(Etw):
    pattern = Struct(
        "StartTime" / Int64ul,
        "NameLength" / Int32ul,
        "Name" / Bytes(lambda this: this.NameLength),
        "TotalTime" / Int32ul,
        "DegradationTime" / Int32ul
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=200, version=1)
class Microsoft_Windows_Diagnostics_Performance_200_1(Etw):
    pattern = Struct(
        "ShutdownTsVersion" / Int32ul,
        "ShutdownStartTime" / Int64ul,
        "ShutdownEndTime" / Int64ul,
        "ShutdownTime" / Int32ul,
        "ShutdownUserSessionTime" / Int32ul,
        "ShutdownUserPolicyTime" / Int32ul,
        "ShutdownUserProfilesTime" / Int32ul,
        "ShutdownSystemSessionsTime" / Int32ul,
        "ShutdownPreShutdownNotificationsTime" / Int32ul,
        "ShutdownServicesTime" / Int32ul,
        "ShutdownKernelTime" / Int32ul,
        "ShutdownRootCauseStepImprovementBits" / Int32ul,
        "ShutdownRootCauseGradualImprovementBits" / Int32ul,
        "ShutdownRootCauseStepDegradationBits" / Int32ul,
        "ShutdownRootCauseGradualDegradationBits" / Int32ul,
        "ShutdownIsDegradation" / Int8ul,
        "ShutdownTimeChange" / Int32sl
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=201, version=1)
class Microsoft_Windows_Diagnostics_Performance_201_1(Etw):
    pattern = Struct(
        "StartTime" / Int64ul,
        "NameLength" / Int32ul,
        "Name" / Bytes(lambda this: this.NameLength),
        "FriendlyNameLength" / Int32ul,
        "FriendlyName" / Bytes(lambda this: this.FriendlyNameLength),
        "VersionLength" / Int32ul,
        "Version" / Bytes(lambda this: this.VersionLength),
        "TotalTime" / Int32ul,
        "DegradationTime" / Int32ul,
        "PathLength" / Int32ul,
        "Path" / Bytes(lambda this: this.PathLength),
        "ProductNameLength" / Int32ul,
        "ProductName" / Bytes(lambda this: this.ProductNameLength),
        "CompanyNameLength" / Int32ul,
        "CompanyName" / Bytes(lambda this: this.CompanyNameLength)
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=202, version=1)
class Microsoft_Windows_Diagnostics_Performance_202_1(Etw):
    pattern = Struct(
        "StartTime" / Int64ul,
        "NameLength" / Int32ul,
        "Name" / Bytes(lambda this: this.NameLength),
        "FriendlyNameLength" / Int32ul,
        "FriendlyName" / Bytes(lambda this: this.FriendlyNameLength),
        "VersionLength" / Int32ul,
        "Version" / Bytes(lambda this: this.VersionLength),
        "TotalTime" / Int32ul,
        "DegradationTime" / Int32ul,
        "PathLength" / Int32ul,
        "Path" / Bytes(lambda this: this.PathLength),
        "ProductNameLength" / Int32ul,
        "ProductName" / Bytes(lambda this: this.ProductNameLength),
        "CompanyNameLength" / Int32ul,
        "CompanyName" / Bytes(lambda this: this.CompanyNameLength)
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=203, version=1)
class Microsoft_Windows_Diagnostics_Performance_203_1(Etw):
    pattern = Struct(
        "StartTime" / Int64ul,
        "NameLength" / Int32ul,
        "Name" / Bytes(lambda this: this.NameLength),
        "FriendlyNameLength" / Int32ul,
        "FriendlyName" / Bytes(lambda this: this.FriendlyNameLength),
        "VersionLength" / Int32ul,
        "Version" / Bytes(lambda this: this.VersionLength),
        "TotalTime" / Int32ul,
        "DegradationTime" / Int32ul,
        "PathLength" / Int32ul,
        "Path" / Bytes(lambda this: this.PathLength),
        "ProductNameLength" / Int32ul,
        "ProductName" / Bytes(lambda this: this.ProductNameLength),
        "CompanyNameLength" / Int32ul,
        "CompanyName" / Bytes(lambda this: this.CompanyNameLength)
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=300, version=1)
class Microsoft_Windows_Diagnostics_Performance_300_1(Etw):
    pattern = Struct(
        "StandbyTsVersion" / Int32ul,
        "StandbyAppCount" / Int32ul,
        "StandbyServicesCount" / Int32ul,
        "StandbyDevicesCount" / Int32ul,
        "StandbyStartTime" / Int64ul,
        "StandbyEndTime" / Int64ul,
        "StandbySuspendTotal" / Int32ul,
        "StandbySuspendTotalChange" / Int32sl,
        "StandbySuspendQueryApps" / Int32ul,
        "StandbySuspendQueryAppsChange" / Int32sl,
        "StandbySuspendQueryServices" / Int32ul,
        "StandbySuspendQueryServicesChange" / Int32sl,
        "StandbySuspendApps" / Int32ul,
        "StandbySuspendAppsChange" / Int32sl,
        "StandbySuspendServices" / Int32ul,
        "StandbySuspendServicesChange" / Int32sl,
        "StandbySuspendShowUI" / Int32ul,
        "StandbySuspendShowUIChange" / Int32sl,
        "StandbySuspendSuperfetchPageIn" / Int32ul,
        "StandbySuspendSuperfetchPageInChange" / Int32sl,
        "StandbySuspendWinlogon" / Int32ul,
        "StandbySuspendWinlogonChange" / Int32sl,
        "StandbySuspendLockPageableSections" / Int32ul,
        "StandbySuspendLockPageableSectionsChange" / Int32sl,
        "StandbySuspendPreSleepCallbacks" / Int32ul,
        "StandbySuspendPreSleepCallbacksChange" / Int32sl,
        "StandbySuspendSwapInWorkerThreads" / Int32ul,
        "StandbySuspendSwapInWorkerThreadsChange" / Int32sl,
        "StandbySuspendQueryDevices" / Int32ul,
        "StandbySuspendQueryDevicesChange" / Int32sl,
        "StandbySuspendFlushVolumes" / Int32ul,
        "StandbySuspendFlushVolumesChange" / Int32sl,
        "StandbySuspendSuspendDevices" / Int32ul,
        "StandbySuspendSuspendDevicesChange" / Int32sl,
        "StandbySuspendHibernateWrite" / Int32ul,
        "StandbySuspendHibernateWriteChange" / Int32sl,
        "ResumeStartTime" / Int64ul,
        "ResumeEndTime" / Int64ul,
        "StandbyResumeTotal" / Int32ul,
        "StandbyResumeTotalChange" / Int32sl,
        "StandbyResumeHibernateRead" / Int32ul,
        "StandbyResumeHibernateReadChange" / Int32sl,
        "StandbyResumeS3BiosInitTime" / Int32ul,
        "StandbyResumeS3BiosInitTimeChange" / Int32sl,
        "StandbyResumeResumeDevices" / Int32ul,
        "StandbyResumeResumeDevicesChange" / Int32sl,
        "StandbyRootCauseDegradationGradual" / Int32ul,
        "StandbyRootCauseImprovementGradual" / Int32ul,
        "StandbyRootCauseDegradationStep" / Int32ul,
        "StandbyRootCauseImprovementStep" / Int32ul,
        "StandbyIsDegradation" / Int8ul,
        "StandbyIsTroubleshooterLaunched" / Int8ul,
        "StandbyIsRootCauseIdentified" / Int8ul
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=301, version=1)
class Microsoft_Windows_Diagnostics_Performance_301_1(Etw):
    pattern = Struct(
        "StartTime" / Int64ul,
        "NameLength" / Int32ul,
        "Name" / Bytes(lambda this: this.NameLength),
        "FriendlyNameLength" / Int32ul,
        "FriendlyName" / Bytes(lambda this: this.FriendlyNameLength),
        "VersionLength" / Int32ul,
        "Version" / Bytes(lambda this: this.VersionLength),
        "TotalTime" / Int32ul,
        "DegradationTime" / Int32ul,
        "PathLength" / Int32ul,
        "Path" / Bytes(lambda this: this.PathLength),
        "ProductNameLength" / Int32ul,
        "ProductName" / Bytes(lambda this: this.ProductNameLength),
        "CompanyNameLength" / Int32ul,
        "CompanyName" / Bytes(lambda this: this.CompanyNameLength)
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=302, version=1)
class Microsoft_Windows_Diagnostics_Performance_302_1(Etw):
    pattern = Struct(
        "StartTime" / Int64ul,
        "NameLength" / Int32ul,
        "Name" / Bytes(lambda this: this.NameLength),
        "FriendlyNameLength" / Int32ul,
        "FriendlyName" / Bytes(lambda this: this.FriendlyNameLength),
        "VersionLength" / Int32ul,
        "Version" / Bytes(lambda this: this.VersionLength),
        "TotalTime" / Int32ul,
        "DegradationTime" / Int32ul,
        "PathLength" / Int32ul,
        "Path" / Bytes(lambda this: this.PathLength),
        "ProductNameLength" / Int32ul,
        "ProductName" / Bytes(lambda this: this.ProductNameLength),
        "CompanyNameLength" / Int32ul,
        "CompanyName" / Bytes(lambda this: this.CompanyNameLength),
        "DeviceNameLength" / Int32ul,
        "DeviceName" / Bytes(lambda this: this.DeviceNameLength),
        "DeviceFriendlyNameLength" / Int32ul,
        "DeviceFriendlyName" / Bytes(lambda this: this.DeviceFriendlyNameLength),
        "DeviceTotalTime" / Int32ul,
        "DeviceDegradationTime" / Int32ul
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=303, version=1)
class Microsoft_Windows_Diagnostics_Performance_303_1(Etw):
    pattern = Struct(
        "StartTime" / Int64ul,
        "NameLength" / Int32ul,
        "Name" / Bytes(lambda this: this.NameLength),
        "FriendlyNameLength" / Int32ul,
        "FriendlyName" / Bytes(lambda this: this.FriendlyNameLength),
        "VersionLength" / Int32ul,
        "Version" / Bytes(lambda this: this.VersionLength),
        "TotalTime" / Int32ul,
        "DegradationTime" / Int32ul,
        "PathLength" / Int32ul,
        "Path" / Bytes(lambda this: this.PathLength),
        "ProductNameLength" / Int32ul,
        "ProductName" / Bytes(lambda this: this.ProductNameLength),
        "CompanyNameLength" / Int32ul,
        "CompanyName" / Bytes(lambda this: this.CompanyNameLength)
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=304, version=1)
class Microsoft_Windows_Diagnostics_Performance_304_1(Etw):
    pattern = Struct(
        "StartTime" / Int64ul,
        "NameLength" / Int32ul,
        "Name" / Bytes(lambda this: this.NameLength),
        "TotalTime" / Int32ul,
        "DegradationTime" / Int32ul
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=305, version=1)
class Microsoft_Windows_Diagnostics_Performance_305_1(Etw):
    pattern = Struct(
        "StartTime" / Int64ul,
        "NameLength" / Int32ul,
        "Name" / Bytes(lambda this: this.NameLength),
        "TotalTime" / Int32ul,
        "DegradationTime" / Int32ul
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=306, version=1)
class Microsoft_Windows_Diagnostics_Performance_306_1(Etw):
    pattern = Struct(
        "StartTime" / Int64ul,
        "NameLength" / Int32ul,
        "Name" / Bytes(lambda this: this.NameLength),
        "TotalTime" / Int32ul,
        "DegradationTime" / Int32ul
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=307, version=1)
class Microsoft_Windows_Diagnostics_Performance_307_1(Etw):
    pattern = Struct(
        "StartTime" / Int64ul,
        "NameLength" / Int32ul,
        "Name" / Bytes(lambda this: this.NameLength),
        "TotalTime" / Int32ul,
        "DegradationTime" / Int32ul
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=308, version=1)
class Microsoft_Windows_Diagnostics_Performance_308_1(Etw):
    pattern = Struct(
        "StartTime" / Int64ul,
        "NameLength" / Int32ul,
        "Name" / Bytes(lambda this: this.NameLength),
        "TotalTime" / Int32ul,
        "DegradationTime" / Int32ul
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=309, version=1)
class Microsoft_Windows_Diagnostics_Performance_309_1(Etw):
    pattern = Struct(
        "StartTime" / Int64ul,
        "NameLength" / Int32ul,
        "Name" / Bytes(lambda this: this.NameLength),
        "TotalTime" / Int32ul,
        "DegradationTime" / Int32ul
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=310, version=1)
class Microsoft_Windows_Diagnostics_Performance_310_1(Etw):
    pattern = Struct(
        "StartTime" / Int64ul,
        "NameLength" / Int32ul,
        "Name" / Bytes(lambda this: this.NameLength),
        "TotalTime" / Int32ul,
        "DegradationTime" / Int32ul
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=350, version=1)
class Microsoft_Windows_Diagnostics_Performance_350_1(Etw):
    pattern = Struct(
        "StartTime" / Int64ul,
        "NameLength" / Int32ul,
        "Name" / Bytes(lambda this: this.NameLength),
        "TotalTime" / Int32ul,
        "DegradationTime" / Int32ul
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=351, version=1)
class Microsoft_Windows_Diagnostics_Performance_351_1(Etw):
    pattern = Struct(
        "StartTime" / Int64ul,
        "NameLength" / Int32ul,
        "Name" / Bytes(lambda this: this.NameLength),
        "FriendlyNameLength" / Int32ul,
        "FriendlyName" / Bytes(lambda this: this.FriendlyNameLength),
        "VersionLength" / Int32ul,
        "Version" / Bytes(lambda this: this.VersionLength),
        "TotalTime" / Int32ul,
        "DegradationTime" / Int32ul,
        "PathLength" / Int32ul,
        "Path" / Bytes(lambda this: this.PathLength),
        "ProductNameLength" / Int32ul,
        "ProductName" / Bytes(lambda this: this.ProductNameLength),
        "CompanyNameLength" / Int32ul,
        "CompanyName" / Bytes(lambda this: this.CompanyNameLength),
        "DeviceNameLength" / Int32ul,
        "DeviceName" / Bytes(lambda this: this.DeviceNameLength),
        "DeviceFriendlyNameLength" / Int32ul,
        "DeviceFriendlyName" / Bytes(lambda this: this.DeviceFriendlyNameLength),
        "DeviceTotalTime" / Int32ul,
        "DeviceDegradationTime" / Int32ul
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=352, version=1)
class Microsoft_Windows_Diagnostics_Performance_352_1(Etw):
    pattern = Struct(
        "StartTime" / Int64ul,
        "NameLength" / Int32ul,
        "Name" / Bytes(lambda this: this.NameLength),
        "TotalTime" / Int32ul,
        "DegradationTime" / Int32ul
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=400, version=1)
class Microsoft_Windows_Diagnostics_Performance_400_1(Etw):
    pattern = Struct(
        "ShellScenarioStartTime" / Int64ul,
        "ShellScenarioEndTime" / Int64ul,
        "ShellSubScenario" / Int32ul,
        "ShellScenarioDuration" / Int32ul,
        "ShellRootCauseBits" / Int32ul,
        "ShellAnalysisResult" / Int32ul,
        "ShellDegradationType" / Int32ul,
        "ShellTsVersion" / Int32ul,
        "ShellMachineUpTimeHours" / Int32ul,
        "ShellMachineSleepPattern" / Int32ul
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=401, version=1)
class Microsoft_Windows_Diagnostics_Performance_401_1(Etw):
    pattern = Struct(
        "StartTime" / Int64ul,
        "NameLength" / Int32ul,
        "Name" / Bytes(lambda this: this.NameLength),
        "FriendlyNameLength" / Int32ul,
        "FriendlyName" / Bytes(lambda this: this.FriendlyNameLength),
        "VersionLength" / Int32ul,
        "Version" / Bytes(lambda this: this.VersionLength),
        "ThreadTime" / Int32ul,
        "BlockedTime" / Int32ul,
        "PercentTime" / Double,
        "PathLength" / Int32ul,
        "Path" / Bytes(lambda this: this.PathLength),
        "ProductNameLength" / Int32ul,
        "ProductName" / Bytes(lambda this: this.ProductNameLength),
        "CompanyNameLength" / Int32ul,
        "CompanyName" / Bytes(lambda this: this.CompanyNameLength)
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=402, version=1)
class Microsoft_Windows_Diagnostics_Performance_402_1(Etw):
    pattern = Struct(
        "StartTime" / Int64ul,
        "NameLength" / Int32ul,
        "Name" / Bytes(lambda this: this.NameLength),
        "FriendlyNameLength" / Int32ul,
        "FriendlyName" / Bytes(lambda this: this.FriendlyNameLength),
        "VersionLength" / Int32ul,
        "Version" / Bytes(lambda this: this.VersionLength),
        "ThreadTime" / Int32ul,
        "BlockedTime" / Int32ul,
        "PercentTime" / Double,
        "PathLength" / Int32ul,
        "Path" / Bytes(lambda this: this.PathLength),
        "ProductNameLength" / Int32ul,
        "ProductName" / Bytes(lambda this: this.ProductNameLength),
        "CompanyNameLength" / Int32ul,
        "CompanyName" / Bytes(lambda this: this.CompanyNameLength)
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=403, version=1)
class Microsoft_Windows_Diagnostics_Performance_403_1(Etw):
    pattern = Struct(
        "StartTime" / Int64ul,
        "NameLength" / Int32ul,
        "Name" / Bytes(lambda this: this.NameLength),
        "FriendlyNameLength" / Int32ul,
        "FriendlyName" / Bytes(lambda this: this.FriendlyNameLength),
        "VersionLength" / Int32ul,
        "Version" / Bytes(lambda this: this.VersionLength),
        "ThreadTime" / Int32ul,
        "BlockedTime" / Int32ul,
        "PercentTime" / Double,
        "PathLength" / Int32ul,
        "Path" / Bytes(lambda this: this.PathLength),
        "ProductNameLength" / Int32ul,
        "ProductName" / Bytes(lambda this: this.ProductNameLength),
        "CompanyNameLength" / Int32ul,
        "CompanyName" / Bytes(lambda this: this.CompanyNameLength)
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=404, version=1)
class Microsoft_Windows_Diagnostics_Performance_404_1(Etw):
    pattern = Struct(
        "StartTime" / Int64ul,
        "NameLength" / Int32ul,
        "Name" / Bytes(lambda this: this.NameLength),
        "FriendlyNameLength" / Int32ul,
        "FriendlyName" / Bytes(lambda this: this.FriendlyNameLength),
        "VersionLength" / Int32ul,
        "Version" / Bytes(lambda this: this.VersionLength),
        "ThreadTime" / Int32ul,
        "BlockedTime" / Int32ul,
        "PercentTime" / Double,
        "PathLength" / Int32ul,
        "Path" / Bytes(lambda this: this.PathLength),
        "ProductNameLength" / Int32ul,
        "ProductName" / Bytes(lambda this: this.ProductNameLength),
        "CompanyNameLength" / Int32ul,
        "CompanyName" / Bytes(lambda this: this.CompanyNameLength)
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=405, version=1)
class Microsoft_Windows_Diagnostics_Performance_405_1(Etw):
    pattern = Struct(
        "StartTime" / Int64ul,
        "NameLength" / Int32ul,
        "Name" / Bytes(lambda this: this.NameLength),
        "FriendlyNameLength" / Int32ul,
        "FriendlyName" / Bytes(lambda this: this.FriendlyNameLength),
        "VersionLength" / Int32ul,
        "Version" / Bytes(lambda this: this.VersionLength),
        "ThreadTime" / Int32ul,
        "BlockedTime" / Int32ul,
        "PercentTime" / Double,
        "PathLength" / Int32ul,
        "Path" / Bytes(lambda this: this.PathLength),
        "ProductNameLength" / Int32ul,
        "ProductName" / Bytes(lambda this: this.ProductNameLength),
        "CompanyNameLength" / Int32ul,
        "CompanyName" / Bytes(lambda this: this.CompanyNameLength)
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=406, version=1)
class Microsoft_Windows_Diagnostics_Performance_406_1(Etw):
    pattern = Struct(
        "StartTime" / Int64ul,
        "NameLength" / Int32ul,
        "Name" / Bytes(lambda this: this.NameLength),
        "FriendlyNameLength" / Int32ul,
        "FriendlyName" / Bytes(lambda this: this.FriendlyNameLength),
        "VersionLength" / Int32ul,
        "Version" / Bytes(lambda this: this.VersionLength),
        "ThreadTime" / Int32ul,
        "BlockedTime" / Int32ul,
        "PercentTime" / Double,
        "PathLength" / Int32ul,
        "Path" / Bytes(lambda this: this.PathLength),
        "ProductNameLength" / Int32ul,
        "ProductName" / Bytes(lambda this: this.ProductNameLength),
        "CompanyNameLength" / Int32ul,
        "CompanyName" / Bytes(lambda this: this.CompanyNameLength)
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=407, version=1)
class Microsoft_Windows_Diagnostics_Performance_407_1(Etw):
    pattern = Struct(
        "StartTime" / Int64ul,
        "NameLength" / Int32ul,
        "Name" / Bytes(lambda this: this.NameLength),
        "FriendlyNameLength" / Int32ul,
        "FriendlyName" / Bytes(lambda this: this.FriendlyNameLength),
        "VersionLength" / Int32ul,
        "Version" / Bytes(lambda this: this.VersionLength),
        "WorkingSetSizeKb" / Int32ul,
        "PeakWorkingSetSizeKb" / Int32ul,
        "ProcessId" / Int32ul,
        "PercentMemory" / Double,
        "PathLength" / Int32ul,
        "Path" / Bytes(lambda this: this.PathLength),
        "ProductNameLength" / Int32ul,
        "ProductName" / Bytes(lambda this: this.ProductNameLength),
        "CompanyNameLength" / Int32ul,
        "CompanyName" / Bytes(lambda this: this.CompanyNameLength)
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=408, version=1)
class Microsoft_Windows_Diagnostics_Performance_408_1(Etw):
    pattern = Struct(
        "StartTime" / Int64ul,
        "WorkingSetSizeKb" / Int32ul,
        "PercentMemory" / Double
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=500, version=1)
class Microsoft_Windows_Diagnostics_Performance_500_1(Etw):
    pattern = Struct(
        "DisplayDeviceFriendlyNameLength" / Int32ul,
        "DisplayDeviceFriendlyName" / Bytes(lambda this: this.DisplayDeviceFriendlyNameLength),
        "MemoryBandwidth" / Int32ul,
        "MemorySize" / Int32ul,
        "Scenario" / Int32ul
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=501, version=1)
class Microsoft_Windows_Diagnostics_Performance_501_1(Etw):
    pattern = Struct(
        "Reason" / Int32ul,
        "Diagnosis" / Int32ul
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=1001, version=0)
class Microsoft_Windows_Diagnostics_Performance_1001_0(Etw):
    pattern = Struct(
        "HResult" / Int32ul
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=1002, version=0)
class Microsoft_Windows_Diagnostics_Performance_1002_0(Etw):
    pattern = Struct(
        "GUID" / Guid,
        "EventId" / Int16ul,
        "InternalState" / Int32ul
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=1003, version=0)
class Microsoft_Windows_Diagnostics_Performance_1003_0(Etw):
    pattern = Struct(
        "NewState" / Int32ul
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=1005, version=0)
class Microsoft_Windows_Diagnostics_Performance_1005_0(Etw):
    pattern = Struct(
        "HResult" / Int32ul
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=1007, version=0)
class Microsoft_Windows_Diagnostics_Performance_1007_0(Etw):
    pattern = Struct(
        "GUID" / Guid,
        "EventId" / Int16ul,
        "InternalState" / Int32ul
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=1011, version=0)
class Microsoft_Windows_Diagnostics_Performance_1011_0(Etw):
    pattern = Struct(
        "HResult" / Int32ul
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=1013, version=0)
class Microsoft_Windows_Diagnostics_Performance_1013_0(Etw):
    pattern = Struct(
        "HResult" / Int32ul
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=1015, version=0)
class Microsoft_Windows_Diagnostics_Performance_1015_0(Etw):
    pattern = Struct(
        "HResult" / Int32ul
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=1020, version=0)
class Microsoft_Windows_Diagnostics_Performance_1020_0(Etw):
    pattern = Struct(
        "HResult" / Int32ul
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=1025, version=0)
class Microsoft_Windows_Diagnostics_Performance_1025_0(Etw):
    pattern = Struct(
        "HResult" / Int32ul
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=1029, version=0)
class Microsoft_Windows_Diagnostics_Performance_1029_0(Etw):
    pattern = Struct(
        "HResult" / Int32ul
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=2005, version=0)
class Microsoft_Windows_Diagnostics_Performance_2005_0(Etw):
    pattern = Struct(
        "HResult" / Int32ul,
        "SnapshotPath" / WString
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=2006, version=0)
class Microsoft_Windows_Diagnostics_Performance_2006_0(Etw):
    pattern = Struct(
        "HResult" / Int32ul,
        "SnapshotPath" / WString
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=2007, version=0)
class Microsoft_Windows_Diagnostics_Performance_2007_0(Etw):
    pattern = Struct(
        "ProviderId" / Guid,
        "EventId" / Int16ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=2008, version=0)
class Microsoft_Windows_Diagnostics_Performance_2008_0(Etw):
    pattern = Struct(
        "ProviderId" / Guid,
        "EventId" / Int16ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=2009, version=0)
class Microsoft_Windows_Diagnostics_Performance_2009_0(Etw):
    pattern = Struct(
        "ProviderId" / Guid,
        "EventId" / Int16ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=2010, version=0)
class Microsoft_Windows_Diagnostics_Performance_2010_0(Etw):
    pattern = Struct(
        "ProviderId" / Guid,
        "EventId" / Int16ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=2011, version=0)
class Microsoft_Windows_Diagnostics_Performance_2011_0(Etw):
    pattern = Struct(
        "ProviderId" / Guid,
        "EventId" / Int16ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=2012, version=0)
class Microsoft_Windows_Diagnostics_Performance_2012_0(Etw):
    pattern = Struct(
        "ProviderId" / Guid,
        "EventId" / Int16ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=2013, version=0)
class Microsoft_Windows_Diagnostics_Performance_2013_0(Etw):
    pattern = Struct(
        "ScenarioGUID" / Guid,
        "HResult" / Int32ul
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=2014, version=0)
class Microsoft_Windows_Diagnostics_Performance_2014_0(Etw):
    pattern = Struct(
        "ScenarioGUID" / Guid,
        "HResult" / Int32ul
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=2015, version=0)
class Microsoft_Windows_Diagnostics_Performance_2015_0(Etw):
    pattern = Struct(
        "ScenarioGUID" / Guid,
        "HResult" / Int32ul
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=2016, version=0)
class Microsoft_Windows_Diagnostics_Performance_2016_0(Etw):
    pattern = Struct(
        "ScenarioGUID" / Guid,
        "HResult" / Int32ul
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=8001, version=0)
class Microsoft_Windows_Diagnostics_Performance_8001_0(Etw):
    pattern = Struct(
        "HResult" / Int32ul
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=8002, version=0)
class Microsoft_Windows_Diagnostics_Performance_8002_0(Etw):
    pattern = Struct(
        "HResult" / Int32ul
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=8004, version=0)
class Microsoft_Windows_Diagnostics_Performance_8004_0(Etw):
    pattern = Struct(
        "HResult" / Int32ul
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=8006, version=0)
class Microsoft_Windows_Diagnostics_Performance_8006_0(Etw):
    pattern = Struct(
        "Path" / WString
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=8007, version=0)
class Microsoft_Windows_Diagnostics_Performance_8007_0(Etw):
    pattern = Struct(
        "Path" / WString
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=8009, version=0)
class Microsoft_Windows_Diagnostics_Performance_8009_0(Etw):
    pattern = Struct(
        "HResult" / Int32ul
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=8012, version=0)
class Microsoft_Windows_Diagnostics_Performance_8012_0(Etw):
    pattern = Struct(
        "HResult" / Int32ul
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=9001, version=0)
class Microsoft_Windows_Diagnostics_Performance_9001_0(Etw):
    pattern = Struct(
        "HResult" / Int32ul
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=9003, version=0)
class Microsoft_Windows_Diagnostics_Performance_9003_0(Etw):
    pattern = Struct(
        "GUID" / Guid,
        "EventId" / Int16ul,
        "InternalState" / Int32ul
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=9005, version=0)
class Microsoft_Windows_Diagnostics_Performance_9005_0(Etw):
    pattern = Struct(
        "NewState" / Int32ul
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=9009, version=0)
class Microsoft_Windows_Diagnostics_Performance_9009_0(Etw):
    pattern = Struct(
        "GUID" / Guid,
        "EventId" / Int16ul,
        "InternalState" / Int32ul
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=9012, version=0)
class Microsoft_Windows_Diagnostics_Performance_9012_0(Etw):
    pattern = Struct(
        "HResult" / Int32ul
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=9015, version=0)
class Microsoft_Windows_Diagnostics_Performance_9015_0(Etw):
    pattern = Struct(
        "HResult" / Int32ul
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=11001, version=0)
class Microsoft_Windows_Diagnostics_Performance_11001_0(Etw):
    pattern = Struct(
        "GUID" / Guid,
        "EventId" / Int16ul,
        "InternalState" / Int32ul
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=11002, version=0)
class Microsoft_Windows_Diagnostics_Performance_11002_0(Etw):
    pattern = Struct(
        "NewState" / Int32ul
    )


@declare(guid=guid("cfc18ec0-96b1-4eba-961b-622caee05b0a"), event_id=11006, version=0)
class Microsoft_Windows_Diagnostics_Performance_11006_0(Etw):
    pattern = Struct(
        "HResult" / Int32ul
    )

