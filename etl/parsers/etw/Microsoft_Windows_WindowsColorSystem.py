# -*- coding: utf-8 -*-
"""
Microsoft-Windows-WindowsColorSystem
GUID : d53270e3-c8cf-4707-958a-dad20c90073c
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("d53270e3-c8cf-4707-958a-dad20c90073c"), event_id=1, version=0)
class Microsoft_Windows_WindowsColorSystem_1_0(Etw):
    pattern = Struct(
        "Profile" / WString
    )


@declare(guid=guid("d53270e3-c8cf-4707-958a-dad20c90073c"), event_id=2, version=0)
class Microsoft_Windows_WindowsColorSystem_2_0(Etw):
    pattern = Struct(
        "Profile" / WString
    )


@declare(guid=guid("d53270e3-c8cf-4707-958a-dad20c90073c"), event_id=3, version=0)
class Microsoft_Windows_WindowsColorSystem_3_0(Etw):
    pattern = Struct(
        "Profile" / WString,
        "Device" / WString,
        "Scope" / Int32ul
    )


@declare(guid=guid("d53270e3-c8cf-4707-958a-dad20c90073c"), event_id=4, version=0)
class Microsoft_Windows_WindowsColorSystem_4_0(Etw):
    pattern = Struct(
        "Profile" / WString,
        "Device" / WString,
        "Scope" / Int32ul
    )


@declare(guid=guid("d53270e3-c8cf-4707-958a-dad20c90073c"), event_id=5, version=0)
class Microsoft_Windows_WindowsColorSystem_5_0(Etw):
    pattern = Struct(
        "Profile" / WString,
        "Device" / WString,
        "Scope" / Int32ul
    )


@declare(guid=guid("d53270e3-c8cf-4707-958a-dad20c90073c"), event_id=6, version=0)
class Microsoft_Windows_WindowsColorSystem_6_0(Etw):
    pattern = Struct(
        "Device" / WString,
        "Setting" / Int8ul
    )


@declare(guid=guid("d53270e3-c8cf-4707-958a-dad20c90073c"), event_id=8, version=0)
class Microsoft_Windows_WindowsColorSystem_8_0(Etw):
    pattern = Struct(
        "Intent" / Int32ul,
        "Scope" / Int32ul
    )


@declare(guid=guid("d53270e3-c8cf-4707-958a-dad20c90073c"), event_id=9, version=0)
class Microsoft_Windows_WindowsColorSystem_9_0(Etw):
    pattern = Struct(
        "Scope" / Int32ul
    )


@declare(guid=guid("d53270e3-c8cf-4707-958a-dad20c90073c"), event_id=10, version=0)
class Microsoft_Windows_WindowsColorSystem_10_0(Etw):
    pattern = Struct(
        "Intent" / Int32ul,
        "Profile" / WString,
        "Scope" / Int32ul
    )


@declare(guid=guid("d53270e3-c8cf-4707-958a-dad20c90073c"), event_id=11, version=0)
class Microsoft_Windows_WindowsColorSystem_11_0(Etw):
    pattern = Struct(
        "Intent" / Int32ul,
        "Scope" / Int32ul
    )


@declare(guid=guid("d53270e3-c8cf-4707-958a-dad20c90073c"), event_id=12, version=0)
class Microsoft_Windows_WindowsColorSystem_12_0(Etw):
    pattern = Struct(
        "WorkingSpace" / WString,
        "Profile" / WString,
        "Scope" / Int32ul
    )


@declare(guid=guid("d53270e3-c8cf-4707-958a-dad20c90073c"), event_id=13, version=0)
class Microsoft_Windows_WindowsColorSystem_13_0(Etw):
    pattern = Struct(
        "WorkingSpace" / WString,
        "Scope" / Int32ul
    )


@declare(guid=guid("d53270e3-c8cf-4707-958a-dad20c90073c"), event_id=14, version=0)
class Microsoft_Windows_WindowsColorSystem_14_0(Etw):
    pattern = Struct(
        "Profile" / WString,
        "Scope" / Int32ul
    )


@declare(guid=guid("d53270e3-c8cf-4707-958a-dad20c90073c"), event_id=15, version=0)
class Microsoft_Windows_WindowsColorSystem_15_0(Etw):
    pattern = Struct(
        "Scope" / Int32ul
    )


@declare(guid=guid("d53270e3-c8cf-4707-958a-dad20c90073c"), event_id=16, version=0)
class Microsoft_Windows_WindowsColorSystem_16_0(Etw):
    pattern = Struct(
        "Profile" / WString,
        "Reason" / WString
    )


@declare(guid=guid("d53270e3-c8cf-4707-958a-dad20c90073c"), event_id=19, version=0)
class Microsoft_Windows_WindowsColorSystem_19_0(Etw):
    pattern = Struct(
        "Tag" / WString,
        "BCurves" / Int32ul,
        "Matrix" / Int32ul,
        "MCurves" / Int32ul,
        "CLut" / Int32ul,
        "ACurves" / Int32ul
    )


@declare(guid=guid("d53270e3-c8cf-4707-958a-dad20c90073c"), event_id=26, version=0)
class Microsoft_Windows_WindowsColorSystem_26_0(Etw):
    pattern = Struct(
        "RMin" / Float32l,
        "RMax" / Float32l,
        "GMin" / Float32l,
        "GMax" / Float32l,
        "BMin" / Float32l,
        "BMax" / Float32l
    )


@declare(guid=guid("d53270e3-c8cf-4707-958a-dad20c90073c"), event_id=27, version=0)
class Microsoft_Windows_WindowsColorSystem_27_0(Etw):
    pattern = Struct(
        "Min" / Float32l,
        "Max" / Float32l
    )


@declare(guid=guid("d53270e3-c8cf-4707-958a-dad20c90073c"), event_id=28, version=0)
class Microsoft_Windows_WindowsColorSystem_28_0(Etw):
    pattern = Struct(
        "Intent" / Int32ul
    )


@declare(guid=guid("d53270e3-c8cf-4707-958a-dad20c90073c"), event_id=29, version=0)
class Microsoft_Windows_WindowsColorSystem_29_0(Etw):
    pattern = Struct(
        "Intent" / Int32ul
    )


@declare(guid=guid("d53270e3-c8cf-4707-958a-dad20c90073c"), event_id=31, version=0)
class Microsoft_Windows_WindowsColorSystem_31_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("d53270e3-c8cf-4707-958a-dad20c90073c"), event_id=32, version=0)
class Microsoft_Windows_WindowsColorSystem_32_0(Etw):
    pattern = Struct(
        "CdmType" / Int32ul,
        "CdmFileName" / WString,
        "CamType" / Int32ul,
        "CamFileName" / WString,
        "GmmType" / Int32ul,
        "GmmFileName" / WString,
        "Access" / Int32ul,
        "Share" / Int32ul,
        "Creation" / Int32ul
    )


@declare(guid=guid("d53270e3-c8cf-4707-958a-dad20c90073c"), event_id=34, version=0)
class Microsoft_Windows_WindowsColorSystem_34_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("d53270e3-c8cf-4707-958a-dad20c90073c"), event_id=35, version=0)
class Microsoft_Windows_WindowsColorSystem_35_0(Etw):
    pattern = Struct(
        "Size" / Int32ul,
        "Version" / Int32ul,
        "DeviceClass" / WString,
        "ColorSpace" / WString,
        "Pcs" / WString
    )


@declare(guid=guid("d53270e3-c8cf-4707-958a-dad20c90073c"), event_id=37, version=0)
class Microsoft_Windows_WindowsColorSystem_37_0(Etw):
    pattern = Struct(
        "Optimization" / Int32ul
    )


@declare(guid=guid("d53270e3-c8cf-4707-958a-dad20c90073c"), event_id=38, version=0)
class Microsoft_Windows_WindowsColorSystem_38_0(Etw):
    pattern = Struct(
        "LutType" / Int32ul
    )


@declare(guid=guid("d53270e3-c8cf-4707-958a-dad20c90073c"), event_id=39, version=0)
class Microsoft_Windows_WindowsColorSystem_39_0(Etw):
    pattern = Struct(
        "Tag" / WString,
        "LutType" / Int32ul,
        "Class" / WString,
        "Intent" / Int32ul
    )


@declare(guid=guid("d53270e3-c8cf-4707-958a-dad20c90073c"), event_id=40, version=0)
class Microsoft_Windows_WindowsColorSystem_40_0(Etw):
    pattern = Struct(
        "LcsCSType" / Int32ul,
        "LcsIntent" / Int32ul,
        "SourceProfileName" / WString,
        "DestProfileType" / Int32ul,
        "DestProfileName" / WString,
        "TargetProfileType" / Int32ul,
        "TargetProfileName" / WString,
        "Flags" / Int32ul
    )


@declare(guid=guid("d53270e3-c8cf-4707-958a-dad20c90073c"), event_id=41, version=0)
class Microsoft_Windows_WindowsColorSystem_41_0(Etw):
    pattern = Struct(
        "NumProfiles" / Int32ul,
        "NumIntents" / Int32ul,
        "Flags" / Int32ul
    )


@declare(guid=guid("d53270e3-c8cf-4707-958a-dad20c90073c"), event_id=42, version=0)
class Microsoft_Windows_WindowsColorSystem_42_0(Etw):
    pattern = Struct(
        "HXform" / Int32ul
    )


@declare(guid=guid("d53270e3-c8cf-4707-958a-dad20c90073c"), event_id=43, version=0)
class Microsoft_Windows_WindowsColorSystem_43_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("d53270e3-c8cf-4707-958a-dad20c90073c"), event_id=44, version=0)
class Microsoft_Windows_WindowsColorSystem_44_0(Etw):
    pattern = Struct(
        "HXform" / Int32ul,
        "NumColors" / Int32ul,
        "InColorType" / Int32ul,
        "OutColorType" / Int32ul
    )


@declare(guid=guid("d53270e3-c8cf-4707-958a-dad20c90073c"), event_id=45, version=0)
class Microsoft_Windows_WindowsColorSystem_45_0(Etw):
    pattern = Struct(
        "HXform" / Int32ul,
        "NumColors" / Int32ul,
        "NumInChannels" / Int32ul,
        "InDataType" / Int32ul,
        "NumInBytes" / Int32ul,
        "NumOutChannels" / Int32ul,
        "OutDataType" / Int32ul,
        "NumOutBytes" / Int32ul
    )


@declare(guid=guid("d53270e3-c8cf-4707-958a-dad20c90073c"), event_id=46, version=0)
class Microsoft_Windows_WindowsColorSystem_46_0(Etw):
    pattern = Struct(
        "HXform" / Int32ul,
        "InBitmapFormat" / Int32ul,
        "Width" / Int32ul,
        "Height" / Int32ul,
        "InStride" / Int32ul,
        "OutBitmapFormat" / Int32ul,
        "OutStride" / Int32ul
    )


@declare(guid=guid("d53270e3-c8cf-4707-958a-dad20c90073c"), event_id=48, version=0)
class Microsoft_Windows_WindowsColorSystem_48_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("d53270e3-c8cf-4707-958a-dad20c90073c"), event_id=49, version=0)
class Microsoft_Windows_WindowsColorSystem_49_0(Etw):
    pattern = Struct(
        "CalibrationManagementEnabled" / Int8ul
    )


@declare(guid=guid("d53270e3-c8cf-4707-958a-dad20c90073c"), event_id=50, version=0)
class Microsoft_Windows_WindowsColorSystem_50_0(Etw):
    pattern = Struct(
        "DeviceName" / WString,
        "ColorProfileExistsAndContainsCalibrationData" / Int8ul
    )


@declare(guid=guid("d53270e3-c8cf-4707-958a-dad20c90073c"), event_id=51, version=0)
class Microsoft_Windows_WindowsColorSystem_51_0(Etw):
    pattern = Struct(
        "ReturnCode" / Int32ul
    )


@declare(guid=guid("d53270e3-c8cf-4707-958a-dad20c90073c"), event_id=52, version=0)
class Microsoft_Windows_WindowsColorSystem_52_0(Etw):
    pattern = Struct(
        "AdapterGammaAdjustments" / Int8ul,
        "MonitorAdjustments" / Int8ul
    )


@declare(guid=guid("d53270e3-c8cf-4707-958a-dad20c90073c"), event_id=53, version=0)
class Microsoft_Windows_WindowsColorSystem_53_0(Etw):
    pattern = Struct(
        "NewValue" / Int8ul
    )


@declare(guid=guid("d53270e3-c8cf-4707-958a-dad20c90073c"), event_id=57, version=0)
class Microsoft_Windows_WindowsColorSystem_57_0(Etw):
    pattern = Struct(
        "ProfileName" / WString,
        "ReturnCode" / Int32ul
    )


@declare(guid=guid("d53270e3-c8cf-4707-958a-dad20c90073c"), event_id=58, version=0)
class Microsoft_Windows_WindowsColorSystem_58_0(Etw):
    pattern = Struct(
        "ReturnCode" / Int32ul
    )

