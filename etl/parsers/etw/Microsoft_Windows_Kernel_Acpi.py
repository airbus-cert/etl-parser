# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Kernel-Acpi
GUID : c514638f-7723-485b-bcfc-96565d735d4a
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("c514638f-7723-485b-bcfc-96565d735d4a"), event_id=1, version=0)
class Microsoft_Windows_Kernel_Acpi_1_0(Etw):
    pattern = Struct(
        "ResourceFlag" / Int8ul,
        "GeneralFlag" / Int8ul,
        "TypeSpecificFlag" / Int8ul,
        "Granularity" / Int64ul,
        "AddressMin" / Int64ul,
        "AddressMax" / Int64ul,
        "AddressTranslation" / Int64ul,
        "AddressLength" / Int64ul
    )


@declare(guid=guid("c514638f-7723-485b-bcfc-96565d735d4a"), event_id=2, version=0)
class Microsoft_Windows_Kernel_Acpi_2_0(Etw):
    pattern = Struct(
        "GpeRegister" / Int32ul,
        "UnexpectedEventMap" / Int8ul
    )


@declare(guid=guid("c514638f-7723-485b-bcfc-96565d735d4a"), event_id=3, version=0)
class Microsoft_Windows_Kernel_Acpi_3_0(Etw):
    pattern = Struct(
        "ThermalZoneDeviceInstanceLength" / Int16ul,
        "ThermalZoneDeviceInstance" / Bytes(lambda this: this.ThermalZoneDeviceInstanceLength),
        "_TMP" / Int32ul,
        "_PSV" / Int32ul,
        "_AC0" / Int32ul,
        "_AC1" / Int32ul,
        "_AC2" / Int32ul,
        "_AC3" / Int32ul,
        "_AC4" / Int32ul,
        "_AC5" / Int32ul,
        "_AC6" / Int32ul,
        "_AC7" / Int32ul,
        "_AC8" / Int32ul,
        "_AC9" / Int32ul,
        "_HOT" / Int32ul,
        "_CRT" / Int32ul
    )


@declare(guid=guid("c514638f-7723-485b-bcfc-96565d735d4a"), event_id=4, version=0)
class Microsoft_Windows_Kernel_Acpi_4_0(Etw):
    pattern = Struct(
        "ThermalZoneDeviceInstanceLength" / Int16ul,
        "ThermalZoneDeviceInstance" / Bytes(lambda this: this.ThermalZoneDeviceInstanceLength),
        "_TMP" / Int32ul,
        "_PSV" / Int32ul,
        "_AC0" / Int32ul,
        "_AC1" / Int32ul,
        "_AC2" / Int32ul,
        "_AC3" / Int32ul,
        "_AC4" / Int32ul,
        "_AC5" / Int32ul,
        "_AC6" / Int32ul,
        "_AC7" / Int32ul,
        "_AC8" / Int32ul,
        "_AC9" / Int32ul,
        "_HOT" / Int32ul,
        "_CRT" / Int32ul
    )


@declare(guid=guid("c514638f-7723-485b-bcfc-96565d735d4a"), event_id=5, version=0)
class Microsoft_Windows_Kernel_Acpi_5_0(Etw):
    pattern = Struct(
        "ThermalZoneDeviceInstanceLength" / Int16ul,
        "ThermalZoneDeviceInstance" / Bytes(lambda this: this.ThermalZoneDeviceInstanceLength),
        "ActiveCoolingLevel" / Int32ul,
        "ActiveCoolingDeviceIndex" / Int32ul,
        "FanDeviceInstanceLength" / Int16ul,
        "FanDeviceInstance" / Bytes(lambda this: this.FanDeviceInstanceLength),
        "PowerStateLength" / Int16ul,
        "PowerState" / Bytes(lambda this: this.PowerStateLength)
    )


@declare(guid=guid("c514638f-7723-485b-bcfc-96565d735d4a"), event_id=6, version=0)
class Microsoft_Windows_Kernel_Acpi_6_0(Etw):
    pattern = Struct(
        "ThermalZoneDeviceInstanceLength" / Int16ul,
        "ThermalZoneDeviceInstance" / Bytes(lambda this: this.ThermalZoneDeviceInstanceLength),
        "ActiveCoolingLevel" / Int32ul,
        "ActiveCoolingDeviceIndex" / Int32ul,
        "FanDeviceInstanceLength" / Int16ul,
        "FanDeviceInstance" / Bytes(lambda this: this.FanDeviceInstanceLength),
        "PowerState" / Int16ul
    )


@declare(guid=guid("c514638f-7723-485b-bcfc-96565d735d4a"), event_id=7, version=0)
class Microsoft_Windows_Kernel_Acpi_7_0(Etw):
    pattern = Struct(
        "AmlMethodNameLength" / Int16ul,
        "AmlMethodName" / Bytes(lambda this: this.AmlMethodNameLength),
        "AmlMethodState" / Int16ul,
        "AmlElapsedTime" / Int64ul
    )


@declare(guid=guid("c514638f-7723-485b-bcfc-96565d735d4a"), event_id=8, version=0)
class Microsoft_Windows_Kernel_Acpi_8_0(Etw):
    pattern = Struct(
        "DeviceInstanceLength" / Int16ul,
        "DeviceInstance" / Bytes(lambda this: this.DeviceInstanceLength),
        "PowerState" / Int16ul
    )


@declare(guid=guid("c514638f-7723-485b-bcfc-96565d735d4a"), event_id=9, version=0)
class Microsoft_Windows_Kernel_Acpi_9_0(Etw):
    pattern = Struct(
        "DeviceInstanceLength" / Int16ul,
        "DeviceInstance" / Bytes(lambda this: this.DeviceInstanceLength),
        "Throttle" / Int8ul
    )


@declare(guid=guid("c514638f-7723-485b-bcfc-96565d735d4a"), event_id=10, version=0)
class Microsoft_Windows_Kernel_Acpi_10_0(Etw):
    pattern = Struct(
        "DeviceInstanceLength" / Int16ul,
        "DeviceInstance" / Bytes(lambda this: this.DeviceInstanceLength),
        "PowerState" / Int16ul,
        "Throttle" / Int8ul
    )


@declare(guid=guid("c514638f-7723-485b-bcfc-96565d735d4a"), event_id=11, version=0)
class Microsoft_Windows_Kernel_Acpi_11_0(Etw):
    pattern = Struct(
        "ThermalZoneDeviceInstanceLength" / Int16ul,
        "ThermalZoneDeviceInstance" / Bytes(lambda this: this.ThermalZoneDeviceInstanceLength),
        "Temperature" / Int32ul
    )


@declare(guid=guid("c514638f-7723-485b-bcfc-96565d735d4a"), event_id=12, version=0)
class Microsoft_Windows_Kernel_Acpi_12_0(Etw):
    pattern = Struct(
        "ThermalZoneBiosNameLength" / Int16ul,
        "ThermalZoneBiosName" / Bytes(lambda this: this.ThermalZoneBiosNameLength),
        "_TMP" / Int32ul,
        "_PSV" / Int32ul,
        "_TC1" / Int32ul,
        "_TC2" / Int32ul,
        "_TSP" / Int32ul,
        "_AC0" / Int32ul,
        "_AC1" / Int32ul,
        "_AC2" / Int32ul,
        "_AC3" / Int32ul,
        "_AC4" / Int32ul,
        "_AC5" / Int32ul,
        "_AC6" / Int32ul,
        "_AC7" / Int32ul,
        "_AC8" / Int32ul,
        "_AC9" / Int32ul,
        "_HOT" / Int32ul,
        "_CRT" / Int32ul,
        "_NTT" / Int32ul,
        "_PSLCount" / Int32ul,
        "_PSLEntries" / CString,
        "_TZDCount" / Int32ul,
        "_TZDEntries" / CString,
        "_AL0Count" / Int32ul,
        "_AL0Entries" / CString,
        "_AL1Count" / Int32ul,
        "_AL1Entries" / CString,
        "_AL2Count" / Int32ul,
        "_AL2Entries" / CString,
        "_AL3Count" / Int32ul,
        "_AL3Entries" / CString,
        "_AL4Count" / Int32ul,
        "_AL4Entries" / CString,
        "_AL5Count" / Int32ul,
        "_AL5Entries" / CString,
        "_AL6Count" / Int32ul,
        "_AL6Entries" / CString,
        "_AL7Count" / Int32ul,
        "_AL7Entries" / CString,
        "_AL8Count" / Int32ul,
        "_AL8Entries" / CString,
        "_AL9Count" / Int32ul,
        "_AL9Entries" / CString
    )


@declare(guid=guid("c514638f-7723-485b-bcfc-96565d735d4a"), event_id=12, version=1)
class Microsoft_Windows_Kernel_Acpi_12_1(Etw):
    pattern = Struct(
        "ThermalZoneBiosNameLength" / Int16ul,
        "ThermalZoneBiosName" / Bytes(lambda this: this.ThermalZoneBiosNameLength),
        "_TMP" / Int32ul,
        "_PSV" / Int32ul,
        "_TC1" / Int32ul,
        "_TC2" / Int32ul,
        "_TSP" / Int32ul,
        "_AC0" / Int32ul,
        "_AC1" / Int32ul,
        "_AC2" / Int32ul,
        "_AC3" / Int32ul,
        "_AC4" / Int32ul,
        "_AC5" / Int32ul,
        "_AC6" / Int32ul,
        "_AC7" / Int32ul,
        "_AC8" / Int32ul,
        "_AC9" / Int32ul,
        "_HOT" / Int32ul,
        "_CRT" / Int32ul,
        "_NTT" / Int32ul,
        "_PSLCount" / Int32ul,
        "_PSLEntries" / CString,
        "_TZDCount" / Int32ul,
        "_TZDEntries" / CString,
        "_AL0Count" / Int32ul,
        "_AL0Entries" / CString,
        "_AL1Count" / Int32ul,
        "_AL1Entries" / CString,
        "_AL2Count" / Int32ul,
        "_AL2Entries" / CString,
        "_AL3Count" / Int32ul,
        "_AL3Entries" / CString,
        "_AL4Count" / Int32ul,
        "_AL4Entries" / CString,
        "_AL5Count" / Int32ul,
        "_AL5Entries" / CString,
        "_AL6Count" / Int32ul,
        "_AL6Entries" / CString,
        "_AL7Count" / Int32ul,
        "_AL7Entries" / CString,
        "_AL8Count" / Int32ul,
        "_AL8Entries" / CString,
        "_AL9Count" / Int32ul,
        "_AL9Entries" / CString,
        "MinimumThrottle" / Int32ul
    )


@declare(guid=guid("c514638f-7723-485b-bcfc-96565d735d4a"), event_id=12, version=2)
class Microsoft_Windows_Kernel_Acpi_12_2(Etw):
    pattern = Struct(
        "ThermalZoneBiosNameLength" / Int16ul,
        "ThermalZoneBiosName" / Bytes(lambda this: this.ThermalZoneBiosNameLength),
        "_TMP" / Int32ul,
        "_PSV" / Int32ul,
        "_TC1" / Int32ul,
        "_TC2" / Int32ul,
        "_TSP" / Int32ul,
        "_AC0" / Int32ul,
        "_AC1" / Int32ul,
        "_AC2" / Int32ul,
        "_AC3" / Int32ul,
        "_AC4" / Int32ul,
        "_AC5" / Int32ul,
        "_AC6" / Int32ul,
        "_AC7" / Int32ul,
        "_AC8" / Int32ul,
        "_AC9" / Int32ul,
        "_HOT" / Int32ul,
        "_CRT" / Int32ul,
        "_NTT" / Int32ul,
        "_PSLCount" / Int32ul,
        "_PSLEntries" / CString,
        "_TZDCount" / Int32ul,
        "_TZDEntries" / CString,
        "_AL0Count" / Int32ul,
        "_AL0Entries" / CString,
        "_AL1Count" / Int32ul,
        "_AL1Entries" / CString,
        "_AL2Count" / Int32ul,
        "_AL2Entries" / CString,
        "_AL3Count" / Int32ul,
        "_AL3Entries" / CString,
        "_AL4Count" / Int32ul,
        "_AL4Entries" / CString,
        "_AL5Count" / Int32ul,
        "_AL5Entries" / CString,
        "_AL6Count" / Int32ul,
        "_AL6Entries" / CString,
        "_AL7Count" / Int32ul,
        "_AL7Entries" / CString,
        "_AL8Count" / Int32ul,
        "_AL8Entries" / CString,
        "_AL9Count" / Int32ul,
        "_AL9Entries" / CString,
        "MinimumThrottle" / Int32ul,
        "_CR3" / Int32ul,
        "_TFP" / Int32ul,
        "OverThrottleThreshold" / Int32ul
    )


@declare(guid=guid("c514638f-7723-485b-bcfc-96565d735d4a"), event_id=12, version=3)
class Microsoft_Windows_Kernel_Acpi_12_3(Etw):
    pattern = Struct(
        "ThermalZoneBiosNameLength" / Int16ul,
        "ThermalZoneBiosName" / Bytes(lambda this: this.ThermalZoneBiosNameLength),
        "_TMP" / Int32ul,
        "_PSV" / Int32ul,
        "_TC1" / Int32ul,
        "_TC2" / Int32ul,
        "_TSP" / Int32ul,
        "_AC0" / Int32ul,
        "_AC1" / Int32ul,
        "_AC2" / Int32ul,
        "_AC3" / Int32ul,
        "_AC4" / Int32ul,
        "_AC5" / Int32ul,
        "_AC6" / Int32ul,
        "_AC7" / Int32ul,
        "_AC8" / Int32ul,
        "_AC9" / Int32ul,
        "_HOT" / Int32ul,
        "_CRT" / Int32ul,
        "_NTT" / Int32ul,
        "_PSLCount" / Int32ul,
        "_PSLEntries" / CString,
        "_TZDCount" / Int32ul,
        "_TZDEntries" / CString,
        "_AL0Count" / Int32ul,
        "_AL0Entries" / CString,
        "_AL1Count" / Int32ul,
        "_AL1Entries" / CString,
        "_AL2Count" / Int32ul,
        "_AL2Entries" / CString,
        "_AL3Count" / Int32ul,
        "_AL3Entries" / CString,
        "_AL4Count" / Int32ul,
        "_AL4Entries" / CString,
        "_AL5Count" / Int32ul,
        "_AL5Entries" / CString,
        "_AL6Count" / Int32ul,
        "_AL6Entries" / CString,
        "_AL7Count" / Int32ul,
        "_AL7Entries" / CString,
        "_AL8Count" / Int32ul,
        "_AL8Entries" / CString,
        "_AL9Count" / Int32ul,
        "_AL9Entries" / CString,
        "MinimumThrottle" / Int32ul,
        "_CR3" / Int32ul,
        "_TFP" / Int32ul,
        "OverThrottleThreshold" / Int32ul,
        "DescriptionLength" / Int16ul,
        "Description" / Bytes(lambda this: this.DescriptionLength)
    )


@declare(guid=guid("c514638f-7723-485b-bcfc-96565d735d4a"), event_id=12, version=4)
class Microsoft_Windows_Kernel_Acpi_12_4(Etw):
    pattern = Struct(
        "ThermalZoneBiosNameLength" / Int16ul,
        "ThermalZoneBiosName" / Bytes(lambda this: this.ThermalZoneBiosNameLength),
        "_TMP" / Int32ul,
        "_PSV" / Int32ul,
        "_TC1" / Int32ul,
        "_TC2" / Int32ul,
        "_TSP" / Int32ul,
        "_AC0" / Int32ul,
        "_AC1" / Int32ul,
        "_AC2" / Int32ul,
        "_AC3" / Int32ul,
        "_AC4" / Int32ul,
        "_AC5" / Int32ul,
        "_AC6" / Int32ul,
        "_AC7" / Int32ul,
        "_AC8" / Int32ul,
        "_AC9" / Int32ul,
        "_HOT" / Int32ul,
        "_CRT" / Int32ul,
        "_NTT" / Int32ul,
        "_PSLCount" / Int32ul,
        "_PSLEntries" / CString,
        "_TZDCount" / Int32ul,
        "_TZDEntries" / CString,
        "_AL0Count" / Int32ul,
        "_AL0Entries" / CString,
        "_AL1Count" / Int32ul,
        "_AL1Entries" / CString,
        "_AL2Count" / Int32ul,
        "_AL2Entries" / CString,
        "_AL3Count" / Int32ul,
        "_AL3Entries" / CString,
        "_AL4Count" / Int32ul,
        "_AL4Entries" / CString,
        "_AL5Count" / Int32ul,
        "_AL5Entries" / CString,
        "_AL6Count" / Int32ul,
        "_AL6Entries" / CString,
        "_AL7Count" / Int32ul,
        "_AL7Entries" / CString,
        "_AL8Count" / Int32ul,
        "_AL8Entries" / CString,
        "_AL9Count" / Int32ul,
        "_AL9Entries" / CString,
        "MinimumThrottle" / Int32ul,
        "_CR3" / Int32ul,
        "_TFP" / Int32ul,
        "OverThrottleThreshold" / Int32ul,
        "DescriptionLength" / Int16ul,
        "Description" / Bytes(lambda this: this.DescriptionLength),
        "_TZP" / Int32ul
    )


@declare(guid=guid("c514638f-7723-485b-bcfc-96565d735d4a"), event_id=13, version=0)
class Microsoft_Windows_Kernel_Acpi_13_0(Etw):
    pattern = Struct(
        "FanBiosNameLength" / Int16ul,
        "FanBiosName" / Bytes(lambda this: this.FanBiosNameLength),
        "FstSupported" / Int8ul,
        "PowerState" / Int16ul,
        "Control" / Int32ul
    )


@declare(guid=guid("c514638f-7723-485b-bcfc-96565d735d4a"), event_id=14, version=0)
class Microsoft_Windows_Kernel_Acpi_14_0(Etw):
    pattern = Struct(
        "FanBiosNameLength" / Int16ul,
        "FanBiosName" / Bytes(lambda this: this.FanBiosNameLength),
        "PowerState" / Int16ul
    )


@declare(guid=guid("c514638f-7723-485b-bcfc-96565d735d4a"), event_id=15, version=0)
class Microsoft_Windows_Kernel_Acpi_15_0(Etw):
    pattern = Struct(
        "FanBiosNameLength" / Int16ul,
        "FanBiosName" / Bytes(lambda this: this.FanBiosNameLength),
        "Control" / Int32ul
    )


@declare(guid=guid("c514638f-7723-485b-bcfc-96565d735d4a"), event_id=16, version=0)
class Microsoft_Windows_Kernel_Acpi_16_0(Etw):
    pattern = Struct(
        "ThermalZoneDeviceInstanceLength" / Int16ul,
        "ThermalZoneDeviceInstance" / Bytes(lambda this: this.ThermalZoneDeviceInstanceLength),
        "DeviceInstanceLength" / Int16ul,
        "DeviceInstance" / Bytes(lambda this: this.DeviceInstanceLength),
        "PowerState" / Int16ul
    )


@declare(guid=guid("c514638f-7723-485b-bcfc-96565d735d4a"), event_id=17, version=0)
class Microsoft_Windows_Kernel_Acpi_17_0(Etw):
    pattern = Struct(
        "ThermalZoneDeviceInstanceLength" / Int16ul,
        "ThermalZoneDeviceInstance" / Bytes(lambda this: this.ThermalZoneDeviceInstanceLength),
        "DeviceInstanceLength" / Int16ul,
        "DeviceInstance" / Bytes(lambda this: this.DeviceInstanceLength),
        "PowerState" / Int16ul
    )


@declare(guid=guid("c514638f-7723-485b-bcfc-96565d735d4a"), event_id=18, version=0)
class Microsoft_Windows_Kernel_Acpi_18_0(Etw):
    pattern = Struct(
        "ThermalZoneDeviceInstanceLength" / Int16ul,
        "ThermalZoneDeviceInstance" / Bytes(lambda this: this.ThermalZoneDeviceInstanceLength),
        "DeviceInstanceLength" / Int16ul,
        "DeviceInstance" / Bytes(lambda this: this.DeviceInstanceLength),
        "ThrottleLimit" / Int8ul
    )


@declare(guid=guid("c514638f-7723-485b-bcfc-96565d735d4a"), event_id=19, version=0)
class Microsoft_Windows_Kernel_Acpi_19_0(Etw):
    pattern = Struct(
        "ThermalZoneDeviceInstanceLength" / Int16ul,
        "ThermalZoneDeviceInstance" / Bytes(lambda this: this.ThermalZoneDeviceInstanceLength),
        "DeviceInstanceLength" / Int16ul,
        "DeviceInstance" / Bytes(lambda this: this.DeviceInstanceLength),
        "ThrottleLimit" / Int8ul
    )


@declare(guid=guid("c514638f-7723-485b-bcfc-96565d735d4a"), event_id=20, version=0)
class Microsoft_Windows_Kernel_Acpi_20_0(Etw):
    pattern = Struct(
        "DeviceBiosNameLength" / Int16ul,
        "DeviceBiosName" / Bytes(lambda this: this.DeviceBiosNameLength),
        "DeviceResetType" / Int16ul,
        "Status" / Int32ul
    )


@declare(guid=guid("c514638f-7723-485b-bcfc-96565d735d4a"), event_id=21, version=0)
class Microsoft_Windows_Kernel_Acpi_21_0(Etw):
    pattern = Struct(
        "AcpiOverrideType" / Int16ul
    )


@declare(guid=guid("c514638f-7723-485b-bcfc-96565d735d4a"), event_id=22, version=0)
class Microsoft_Windows_Kernel_Acpi_22_0(Etw):
    pattern = Struct(
        "Scope" / WString,
        "Object" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("c514638f-7723-485b-bcfc-96565d735d4a"), event_id=23, version=0)
class Microsoft_Windows_Kernel_Acpi_23_0(Etw):
    pattern = Struct(
        "AmlMethodNameLength" / Int16ul,
        "AmlMethodName" / Bytes(lambda this: this.AmlMethodNameLength),
        "Frequency" / Int64ul
    )

