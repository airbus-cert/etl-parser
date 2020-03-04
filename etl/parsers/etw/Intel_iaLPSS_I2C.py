# -*- coding: utf-8 -*-
"""
Intel-iaLPSS-I2C
GUID : d4aeac44-ad44-456e-9c90-33f8cdced6af
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("d4aeac44-ad44-456e-9c90-33f8cdced6af"), event_id=1001, version=1)
class Intel_iaLPSS_I2C_1001_1(Etw):
    pattern = Struct(
        "FxDevice" / Int64ul
    )


@declare(guid=guid("d4aeac44-ad44-456e-9c90-33f8cdced6af"), event_id=1002, version=1)
class Intel_iaLPSS_I2C_1002_1(Etw):
    pattern = Struct(
        "FxDevice" / Int64ul,
        "VAddr" / Int64ul,
        "PAddr" / Int64ul
    )


@declare(guid=guid("d4aeac44-ad44-456e-9c90-33f8cdced6af"), event_id=1003, version=1)
class Intel_iaLPSS_I2C_1003_1(Etw):
    pattern = Struct(
        "FailReason" / WString,
        "Status" / Int32ul,
        "WDFDEVICE" / Int64ul
    )


@declare(guid=guid("d4aeac44-ad44-456e-9c90-33f8cdced6af"), event_id=1004, version=1)
class Intel_iaLPSS_I2C_1004_1(Etw):
    pattern = Struct(
        "FxDevice" / Int64ul,
        "VAddr" / Int64ul,
        "PAddr" / Int64ul
    )


@declare(guid=guid("d4aeac44-ad44-456e-9c90-33f8cdced6af"), event_id=1005, version=1)
class Intel_iaLPSS_I2C_1005_1(Etw):
    pattern = Struct(
        "FxDevice" / Int64ul,
        "VAddr" / Int64ul,
        "PAddr" / Int64ul
    )


@declare(guid=guid("d4aeac44-ad44-456e-9c90-33f8cdced6af"), event_id=1006, version=1)
class Intel_iaLPSS_I2C_1006_1(Etw):
    pattern = Struct(
        "FxDevice" / Int64ul,
        "VAddr" / Int64ul,
        "PAddr" / Int64ul
    )


@declare(guid=guid("d4aeac44-ad44-456e-9c90-33f8cdced6af"), event_id=1007, version=1)
class Intel_iaLPSS_I2C_1007_1(Etw):
    pattern = Struct(
        "FxDevice" / Int64ul,
        "VAddr" / Int64ul,
        "PAddr" / Int64ul
    )


@declare(guid=guid("d4aeac44-ad44-456e-9c90-33f8cdced6af"), event_id=1008, version=1)
class Intel_iaLPSS_I2C_1008_1(Etw):
    pattern = Struct(
        "FxDevice" / Int64ul,
        "VAddr" / Int64ul,
        "PAddr" / Int64ul
    )


@declare(guid=guid("d4aeac44-ad44-456e-9c90-33f8cdced6af"), event_id=1009, version=1)
class Intel_iaLPSS_I2C_1009_1(Etw):
    pattern = Struct(
        "pRequest" / Int64ul,
        "pDevice" / Int64ul,
        "pTarget" / Int64ul,
        "IOCTL" / WString,
        "TargetI2CAddress" / Int64ul,
        "MMIO" / Int64ul
    )


@declare(guid=guid("d4aeac44-ad44-456e-9c90-33f8cdced6af"), event_id=1010, version=1)
class Intel_iaLPSS_I2C_1010_1(Etw):
    pattern = Struct(
        "Request" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("d4aeac44-ad44-456e-9c90-33f8cdced6af"), event_id=1011, version=0)
class Intel_iaLPSS_I2C_1011_0(Etw):
    pattern = Struct(
        "WDFDEVICE" / Int64ul,
        "MMIO" / Int64ul
    )


@declare(guid=guid("d4aeac44-ad44-456e-9c90-33f8cdced6af"), event_id=1012, version=1)
class Intel_iaLPSS_I2C_1012_1(Etw):
    pattern = Struct(
        "WDFDEVICE" / Int64ul,
        "MMIO" / Int64ul,
        "Stat" / Int64ul
    )


@declare(guid=guid("d4aeac44-ad44-456e-9c90-33f8cdced6af"), event_id=1013, version=1)
class Intel_iaLPSS_I2C_1013_1(Etw):
    pattern = Struct(
        "WDFDEVICE" / Int64ul,
        "MMIO" / Int64ul
    )


@declare(guid=guid("d4aeac44-ad44-456e-9c90-33f8cdced6af"), event_id=1014, version=1)
class Intel_iaLPSS_I2C_1014_1(Etw):
    pattern = Struct(
        "WDFDEVICE" / Int64ul,
        "MMIO" / Int64ul
    )


@declare(guid=guid("d4aeac44-ad44-456e-9c90-33f8cdced6af"), event_id=1021, version=1)
class Intel_iaLPSS_I2C_1021_1(Etw):
    pattern = Struct(
        "TxDmaEnabler" / Int64ul,
        "RxDmaEnabler" / Int64ul,
        "WDFDevice" / Int64ul,
        "MMIO" / Int64ul,
        "Status" / WString
    )


@declare(guid=guid("d4aeac44-ad44-456e-9c90-33f8cdced6af"), event_id=1022, version=1)
class Intel_iaLPSS_I2C_1022_1(Etw):
    pattern = Struct(
        "MonitorState" / WString,
        "IdleTimeout" / Int64ul,
        "WDFDevice" / Int64ul,
        "MMIO" / Int64ul
    )


@declare(guid=guid("d4aeac44-ad44-456e-9c90-33f8cdced6af"), event_id=1023, version=1)
class Intel_iaLPSS_I2C_1023_1(Etw):
    pattern = Struct(
        "pRequest" / Int64ul,
        "pDevice" / Int64ul,
        "pTarget" / Int64ul,
        "IOCTL" / WString,
        "TargetI2CAddress" / Int64ul,
        "MMIO" / Int64ul
    )


@declare(guid=guid("d4aeac44-ad44-456e-9c90-33f8cdced6af"), event_id=1026, version=1)
class Intel_iaLPSS_I2C_1026_1(Etw):
    pattern = Struct(
        "Direction" / WString,
        "NumMdls" / Int64ul,
        "NumBytes" / Int64ul,
        "WDFDEVICE" / Int64ul,
        "MMIO" / Int64ul
    )


@declare(guid=guid("d4aeac44-ad44-456e-9c90-33f8cdced6af"), event_id=1027, version=1)
class Intel_iaLPSS_I2C_1027_1(Etw):
    pattern = Struct(
        "Direction" / WString,
        "WDFDEVICE" / Int64ul,
        "MMIO" / Int64ul,
        "DMAStatus" / Int32ul,
        "NumBytes" / Int64ul
    )


@declare(guid=guid("d4aeac44-ad44-456e-9c90-33f8cdced6af"), event_id=1029, version=1)
class Intel_iaLPSS_I2C_1029_1(Etw):
    pattern = Struct(
        "WDFDEVICE" / Int64ul,
        "MMIO" / Int64ul
    )

