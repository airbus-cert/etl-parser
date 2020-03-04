# -*- coding: utf-8 -*-
"""
Microsoft-Windows-USB-USBHUB
GUID : 7426a56b-e2d5-4b30-bdef-b31815c1a74a
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=1, version=0)
class Microsoft_Windows_USB_USBHUB_1_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_USB_HubDescriptor" / Int64ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=2, version=0)
class Microsoft_Windows_USB_USBHUB_2_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / CString,
        "fid_USBHUB_Hub" / Int32sl
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=3, version=0)
class Microsoft_Windows_USB_USBHUB_3_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_USB_HubDescriptor" / Int64ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=10, version=0)
class Microsoft_Windows_USB_USBHUB_10_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PortNumber" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=11, version=0)
class Microsoft_Windows_USB_USBHUB_11_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PortNumber" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=12, version=0)
class Microsoft_Windows_USB_USBHUB_12_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PortNumber" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=13, version=0)
class Microsoft_Windows_USB_USBHUB_13_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PortNumber" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=14, version=0)
class Microsoft_Windows_USB_USBHUB_14_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PortNumber" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=15, version=0)
class Microsoft_Windows_USB_USBHUB_15_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PortNumber" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=16, version=0)
class Microsoft_Windows_USB_USBHUB_16_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PortNumber" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=17, version=0)
class Microsoft_Windows_USB_USBHUB_17_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PortNumber" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=18, version=0)
class Microsoft_Windows_USB_USBHUB_18_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PortNumber" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=19, version=0)
class Microsoft_Windows_USB_USBHUB_19_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PortNumber" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=20, version=0)
class Microsoft_Windows_USB_USBHUB_20_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PortNumber" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=21, version=0)
class Microsoft_Windows_USB_USBHUB_21_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PortNumber" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=22, version=0)
class Microsoft_Windows_USB_USBHUB_22_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PortNumber" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=23, version=0)
class Microsoft_Windows_USB_USBHUB_23_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PortNumber" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=24, version=0)
class Microsoft_Windows_USB_USBHUB_24_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PortNumber" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=25, version=0)
class Microsoft_Windows_USB_USBHUB_25_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PortNumber" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=26, version=0)
class Microsoft_Windows_USB_USBHUB_26_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PortNumber" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=27, version=0)
class Microsoft_Windows_USB_USBHUB_27_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PortNumber" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=28, version=0)
class Microsoft_Windows_USB_USBHUB_28_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PortNumber" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=29, version=0)
class Microsoft_Windows_USB_USBHUB_29_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PortNumber" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=30, version=0)
class Microsoft_Windows_USB_USBHUB_30_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PortNumber" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=31, version=0)
class Microsoft_Windows_USB_USBHUB_31_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PortNumber" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=32, version=0)
class Microsoft_Windows_USB_USBHUB_32_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PortNumber" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=33, version=0)
class Microsoft_Windows_USB_USBHUB_33_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PortNumber" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=34, version=0)
class Microsoft_Windows_USB_USBHUB_34_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PortNumber" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=35, version=0)
class Microsoft_Windows_USB_USBHUB_35_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PortNumber" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=36, version=0)
class Microsoft_Windows_USB_USBHUB_36_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PortNumber" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=37, version=0)
class Microsoft_Windows_USB_USBHUB_37_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PortNumber" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=39, version=0)
class Microsoft_Windows_USB_USBHUB_39_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PortNumber" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=40, version=0)
class Microsoft_Windows_USB_USBHUB_40_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PortNumber" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=41, version=0)
class Microsoft_Windows_USB_USBHUB_41_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PortNumber" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=49, version=0)
class Microsoft_Windows_USB_USBHUB_49_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PortNumber" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=50, version=0)
class Microsoft_Windows_USB_USBHUB_50_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PortNumber" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=51, version=0)
class Microsoft_Windows_USB_USBHUB_51_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PortNumber" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=59, version=0)
class Microsoft_Windows_USB_USBHUB_59_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PortNumber" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=60, version=0)
class Microsoft_Windows_USB_USBHUB_60_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PortNumber" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=61, version=0)
class Microsoft_Windows_USB_USBHUB_61_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PortNumber" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=62, version=0)
class Microsoft_Windows_USB_USBHUB_62_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PortNumber" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=63, version=0)
class Microsoft_Windows_USB_USBHUB_63_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PortNumber" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=64, version=0)
class Microsoft_Windows_USB_USBHUB_64_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PortNumber" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=70, version=0)
class Microsoft_Windows_USB_USBHUB_70_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PortNumber" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=71, version=0)
class Microsoft_Windows_USB_USBHUB_71_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PortNumber" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=80, version=0)
class Microsoft_Windows_USB_USBHUB_80_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PortNumber" / Int32ul,
        "fid_PortAttributes" / Int16ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=81, version=0)
class Microsoft_Windows_USB_USBHUB_81_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PortNumber" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=82, version=0)
class Microsoft_Windows_USB_USBHUB_82_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PortNumber" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=83, version=0)
class Microsoft_Windows_USB_USBHUB_83_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PortNumber" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=84, version=0)
class Microsoft_Windows_USB_USBHUB_84_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PortNumber" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=100, version=0)
class Microsoft_Windows_USB_USBHUB_100_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Device" / Int64sl,
        "fid_USBHUB_Device_State" / Guid,
        "fid_DeviceDescriptor" / Int64ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=101, version=0)
class Microsoft_Windows_USB_USBHUB_101_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / CString,
        "fid_USBHUB_Device" / Int32sl
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=102, version=0)
class Microsoft_Windows_USB_USBHUB_102_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Device" / Int64sl,
        "fid_USBHUB_Device_State" / Guid,
        "fid_DeviceDescriptor" / Int64ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=103, version=0)
class Microsoft_Windows_USB_USBHUB_103_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8sl,
        "fid_USBHUB_Device" / Int32ul,
        "fid_DeviceDescription" / WString
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=110, version=0)
class Microsoft_Windows_USB_USBHUB_110_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8sl,
        "fid_USBHUB_Device" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=111, version=0)
class Microsoft_Windows_USB_USBHUB_111_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8sl,
        "fid_USBHUB_Device" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=112, version=0)
class Microsoft_Windows_USB_USBHUB_112_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8sl,
        "fid_USBHUB_Device" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=113, version=0)
class Microsoft_Windows_USB_USBHUB_113_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8sl,
        "fid_USBHUB_Device" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=114, version=0)
class Microsoft_Windows_USB_USBHUB_114_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8sl,
        "fid_USBHUB_Device" / Int32ul,
        "fid_DeviceDescription" / WString
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=119, version=0)
class Microsoft_Windows_USB_USBHUB_119_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8sl,
        "fid_USBHUB_Device" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=120, version=0)
class Microsoft_Windows_USB_USBHUB_120_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Device" / Int64sl,
        "fid_PowerState" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=121, version=0)
class Microsoft_Windows_USB_USBHUB_121_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Device" / Int64sl,
        "fid_PowerState" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=122, version=0)
class Microsoft_Windows_USB_USBHUB_122_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Device" / Int64sl,
        "fid_PowerState" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=123, version=0)
class Microsoft_Windows_USB_USBHUB_123_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Device" / Int64sl,
        "fid_PowerState" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=130, version=0)
class Microsoft_Windows_USB_USBHUB_130_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8sl,
        "fid_USBHUB_Device" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=139, version=0)
class Microsoft_Windows_USB_USBHUB_139_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8sl,
        "fid_USBHUB_Device" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=140, version=0)
class Microsoft_Windows_USB_USBHUB_140_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8sl,
        "fid_USBHUB_Device" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=149, version=0)
class Microsoft_Windows_USB_USBHUB_149_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8sl,
        "fid_USBHUB_Device" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=150, version=0)
class Microsoft_Windows_USB_USBHUB_150_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PortNumber" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=151, version=0)
class Microsoft_Windows_USB_USBHUB_151_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PortNumber" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=159, version=0)
class Microsoft_Windows_USB_USBHUB_159_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PortNumber" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=160, version=0)
class Microsoft_Windows_USB_USBHUB_160_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PowerState" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=161, version=0)
class Microsoft_Windows_USB_USBHUB_161_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PowerState" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=169, version=0)
class Microsoft_Windows_USB_USBHUB_169_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PowerState" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=170, version=0)
class Microsoft_Windows_USB_USBHUB_170_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PowerState" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=171, version=0)
class Microsoft_Windows_USB_USBHUB_171_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PowerState" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=172, version=0)
class Microsoft_Windows_USB_USBHUB_172_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PortNumber" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=173, version=0)
class Microsoft_Windows_USB_USBHUB_173_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PortNumber" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=174, version=0)
class Microsoft_Windows_USB_USBHUB_174_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PortNumber" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=175, version=0)
class Microsoft_Windows_USB_USBHUB_175_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PortNumber" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=176, version=0)
class Microsoft_Windows_USB_USBHUB_176_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PortNumber" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=177, version=0)
class Microsoft_Windows_USB_USBHUB_177_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PortNumber" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=178, version=0)
class Microsoft_Windows_USB_USBHUB_178_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PortNumber" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=179, version=0)
class Microsoft_Windows_USB_USBHUB_179_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PortNumber" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=180, version=0)
class Microsoft_Windows_USB_USBHUB_180_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PortNumber" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=181, version=0)
class Microsoft_Windows_USB_USBHUB_181_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PortNumber" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=183, version=0)
class Microsoft_Windows_USB_USBHUB_183_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PortNumber" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=184, version=0)
class Microsoft_Windows_USB_USBHUB_184_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PortNumber" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=185, version=0)
class Microsoft_Windows_USB_USBHUB_185_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PortNumber" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=189, version=0)
class Microsoft_Windows_USB_USBHUB_189_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PowerState" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=190, version=0)
class Microsoft_Windows_USB_USBHUB_190_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PowerState" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=199, version=0)
class Microsoft_Windows_USB_USBHUB_199_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PowerState" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=200, version=0)
class Microsoft_Windows_USB_USBHUB_200_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PowerState" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=209, version=0)
class Microsoft_Windows_USB_USBHUB_209_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PowerState" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=210, version=0)
class Microsoft_Windows_USB_USBHUB_210_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int32sl,
        "fid_USBHUB_Hub" / Double,
        "fid_PortNumber" / Int32ul,
        "fid_Class" / Int32ul,
        "fid_NtStatus" / Int32ul,
        "fid_UsbdStatus" / Int32ul,
        "fid_DebugText" / CString
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=211, version=0)
class Microsoft_Windows_USB_USBHUB_211_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PortNumber" / Int32ul,
        "fid_PortStatusChange" / Int16ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=212, version=0)
class Microsoft_Windows_USB_USBHUB_212_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PortNumber" / Int32ul,
        "fid_TimerTag" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=213, version=0)
class Microsoft_Windows_USB_USBHUB_213_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PortNumber" / Int32ul,
        "fid_TimerTag" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=214, version=0)
class Microsoft_Windows_USB_USBHUB_214_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PortNumber" / Int32ul,
        "fid_TimerTag" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=220, version=0)
class Microsoft_Windows_USB_USBHUB_220_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8sl,
        "fid_USBHUB_Device" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=229, version=0)
class Microsoft_Windows_USB_USBHUB_229_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8sl,
        "fid_USBHUB_Device" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=230, version=0)
class Microsoft_Windows_USB_USBHUB_230_0(Etw):
    pattern = Struct(
        "fid_TimeElapsedBeforeLogStart" / Int64ul,
        "fid_USBHUB_HC" / Int32ul,
        "fid_USBHUB_Hub" / Int8ul,
        "fid_PortNumber" / Int32ul,
        "fid_Class" / Int32ul,
        "fid_NtStatus" / Int32ul,
        "fid_UsbdStatus" / Int32ul,
        "fid_DebugText" / CString
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=231, version=0)
class Microsoft_Windows_USB_USBHUB_231_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8sl,
        "fid_USBHUB_Device" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=232, version=0)
class Microsoft_Windows_USB_USBHUB_232_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8sl,
        "fid_USBHUB_Device" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=233, version=0)
class Microsoft_Windows_USB_USBHUB_233_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PortNumber" / Int32ul,
        "fid_Status" / Int32ul
    )


@declare(guid=guid("7426a56b-e2d5-4b30-bdef-b31815c1a74a"), event_id=234, version=0)
class Microsoft_Windows_USB_USBHUB_234_0(Etw):
    pattern = Struct(
        "fid_USBHUB_HC" / Int8ul,
        "fid_USBHUB_Hub" / Int64sl,
        "fid_PortNumber" / Int32ul,
        "fid_Status" / Int32ul
    )

