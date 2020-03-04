# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Serial-ClassExtension-V2
GUID : eee173ef-7ed2-45de-9877-01c70a852fbd
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("eee173ef-7ed2-45de-9877-01c70a852fbd"), event_id=1, version=1)
class Microsoft_Windows_Serial_ClassExtension_V2_1_1(Etw):
    pattern = Struct(
        "ControlDeviceName" / WString
    )


@declare(guid=guid("eee173ef-7ed2-45de-9877-01c70a852fbd"), event_id=2, version=1)
class Microsoft_Windows_Serial_ClassExtension_V2_2_1(Etw):
    pattern = Struct(
        "ControlDeviceName" / WString,
        "Status" / Int32ul
    )


@declare(guid=guid("eee173ef-7ed2-45de-9877-01c70a852fbd"), event_id=5, version=1)
class Microsoft_Windows_Serial_ClassExtension_V2_5_1(Etw):
    pattern = Struct(
        "Device" / Int64ul,
        "TransmitTransferSmContext" / Int64ul,
        "ReceiveTransferSmContext" / Int64ul,
        "DeviceInstanceId" / WString
    )


@declare(guid=guid("eee173ef-7ed2-45de-9877-01c70a852fbd"), event_id=7, version=1)
class Microsoft_Windows_Serial_ClassExtension_V2_7_1(Etw):
    pattern = Struct(
        "Device" / Int64ul,
        "TransmitTransferSmContext" / Int64ul,
        "ReceiveTransferSmContext" / Int64ul,
        "DeviceInstanceId" / WString
    )


@declare(guid=guid("eee173ef-7ed2-45de-9877-01c70a852fbd"), event_id=8, version=1)
class Microsoft_Windows_Serial_ClassExtension_V2_8_1(Etw):
    pattern = Struct(
        "Device" / Int64ul
    )


@declare(guid=guid("eee173ef-7ed2-45de-9877-01c70a852fbd"), event_id=9, version=1)
class Microsoft_Windows_Serial_ClassExtension_V2_9_1(Etw):
    pattern = Struct(
        "TransferSmContext" / Int64ul,
        "Event" / Int32ul
    )


@declare(guid=guid("eee173ef-7ed2-45de-9877-01c70a852fbd"), event_id=10, version=1)
class Microsoft_Windows_Serial_ClassExtension_V2_10_1(Etw):
    pattern = Struct(
        "TransferSmContext" / Int64ul,
        "FromState" / Int32ul,
        "Event" / Int32ul,
        "ToState" / Int32ul
    )


@declare(guid=guid("eee173ef-7ed2-45de-9877-01c70a852fbd"), event_id=11, version=1)
class Microsoft_Windows_Serial_ClassExtension_V2_11_1(Etw):
    pattern = Struct(
        "TransferSmContext" / Int64ul,
        "FromState" / Int32ul,
        "Event" / Int32ul,
        "ToState" / Int32ul
    )


@declare(guid=guid("eee173ef-7ed2-45de-9877-01c70a852fbd"), event_id=12, version=1)
class Microsoft_Windows_Serial_ClassExtension_V2_12_1(Etw):
    pattern = Struct(
        "TransferSmContext" / Int64ul,
        "Event" / Int32ul
    )


@declare(guid=guid("eee173ef-7ed2-45de-9877-01c70a852fbd"), event_id=13, version=1)
class Microsoft_Windows_Serial_ClassExtension_V2_13_1(Etw):
    pattern = Struct(
        "TransferSmContext" / Int64ul,
        "FromState" / Int32ul,
        "Event" / Int32ul,
        "ToState" / Int32ul
    )


@declare(guid=guid("eee173ef-7ed2-45de-9877-01c70a852fbd"), event_id=14, version=1)
class Microsoft_Windows_Serial_ClassExtension_V2_14_1(Etw):
    pattern = Struct(
        "TransferSmContext" / Int64ul,
        "FromState" / Int32ul,
        "Event" / Int32ul,
        "ToState" / Int32ul
    )


@declare(guid=guid("eee173ef-7ed2-45de-9877-01c70a852fbd"), event_id=15, version=1)
class Microsoft_Windows_Serial_ClassExtension_V2_15_1(Etw):
    pattern = Struct(
        "Device" / Int64ul,
        "IOCTL" / Int32ul,
        "IOCTLInputBufferLength" / Int32ul,
        "IOCTLInputBuffer" / Bytes(lambda this: this.IOCTLInputBufferLength)
    )


@declare(guid=guid("eee173ef-7ed2-45de-9877-01c70a852fbd"), event_id=16, version=1)
class Microsoft_Windows_Serial_ClassExtension_V2_16_1(Etw):
    pattern = Struct(
        "Device" / Int64ul,
        "IOCTL" / Int32ul,
        "Status" / Int32ul,
        "IOCTLOutputBufferLength" / Int32ul,
        "IOCTLOutputBuffer" / Bytes(lambda this: this.IOCTLOutputBufferLength)
    )


@declare(guid=guid("eee173ef-7ed2-45de-9877-01c70a852fbd"), event_id=17, version=1)
class Microsoft_Windows_Serial_ClassExtension_V2_17_1(Etw):
    pattern = Struct(
        "Device" / Int64ul,
        "Length" / Int64ul
    )


@declare(guid=guid("eee173ef-7ed2-45de-9877-01c70a852fbd"), event_id=18, version=1)
class Microsoft_Windows_Serial_ClassExtension_V2_18_1(Etw):
    pattern = Struct(
        "Device" / Int64ul,
        "Status" / Int32ul,
        "Information" / Int64ul
    )


@declare(guid=guid("eee173ef-7ed2-45de-9877-01c70a852fbd"), event_id=19, version=1)
class Microsoft_Windows_Serial_ClassExtension_V2_19_1(Etw):
    pattern = Struct(
        "Device" / Int64ul,
        "Offset" / Int64ul,
        "Length" / Int32ul,
        "TransferModeEvent" / Int32ul,
        "Payload" / Bytes(lambda this: this.Length)
    )


@declare(guid=guid("eee173ef-7ed2-45de-9877-01c70a852fbd"), event_id=20, version=1)
class Microsoft_Windows_Serial_ClassExtension_V2_20_1(Etw):
    pattern = Struct(
        "Device" / Int64ul,
        "Length" / Int64ul
    )


@declare(guid=guid("eee173ef-7ed2-45de-9877-01c70a852fbd"), event_id=21, version=1)
class Microsoft_Windows_Serial_ClassExtension_V2_21_1(Etw):
    pattern = Struct(
        "Device" / Int64ul,
        "Status" / Int32ul,
        "Information" / Int64ul
    )


@declare(guid=guid("eee173ef-7ed2-45de-9877-01c70a852fbd"), event_id=22, version=1)
class Microsoft_Windows_Serial_ClassExtension_V2_22_1(Etw):
    pattern = Struct(
        "Device" / Int64ul,
        "Offset" / Int64ul,
        "Length" / Int32ul,
        "TransferModeEvent" / Int32ul,
        "Payload" / Bytes(lambda this: this.Length)
    )


@declare(guid=guid("eee173ef-7ed2-45de-9877-01c70a852fbd"), event_id=23, version=1)
class Microsoft_Windows_Serial_ClassExtension_V2_23_1(Etw):
    pattern = Struct(
        "Device" / Int64ul,
        "BytesSaved" / Int32ul,
        "TotalBytes" / Int32ul
    )


@declare(guid=guid("eee173ef-7ed2-45de-9877-01c70a852fbd"), event_id=24, version=1)
class Microsoft_Windows_Serial_ClassExtension_V2_24_1(Etw):
    pattern = Struct(
        "Device" / Int64ul,
        "TargetState" / Int32ul
    )


@declare(guid=guid("eee173ef-7ed2-45de-9877-01c70a852fbd"), event_id=25, version=1)
class Microsoft_Windows_Serial_ClassExtension_V2_25_1(Etw):
    pattern = Struct(
        "Device" / Int64ul,
        "TargetState" / Int32ul
    )


@declare(guid=guid("eee173ef-7ed2-45de-9877-01c70a852fbd"), event_id=26, version=1)
class Microsoft_Windows_Serial_ClassExtension_V2_26_1(Etw):
    pattern = Struct(
        "Device" / Int64ul,
        "TargetState" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("eee173ef-7ed2-45de-9877-01c70a852fbd"), event_id=27, version=1)
class Microsoft_Windows_Serial_ClassExtension_V2_27_1(Etw):
    pattern = Struct(
        "Device" / Int64ul,
        "TargetState" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("eee173ef-7ed2-45de-9877-01c70a852fbd"), event_id=28, version=1)
class Microsoft_Windows_Serial_ClassExtension_V2_28_1(Etw):
    pattern = Struct(
        "Device" / Int64ul,
        "Event" / Int32ul
    )


@declare(guid=guid("eee173ef-7ed2-45de-9877-01c70a852fbd"), event_id=29, version=1)
class Microsoft_Windows_Serial_ClassExtension_V2_29_1(Etw):
    pattern = Struct(
        "TransferSmContext" / Int64ul,
        "Event" / Int32ul
    )


@declare(guid=guid("eee173ef-7ed2-45de-9877-01c70a852fbd"), event_id=30, version=1)
class Microsoft_Windows_Serial_ClassExtension_V2_30_1(Etw):
    pattern = Struct(
        "TransferSmContext" / Int64ul,
        "FromState" / Int32ul,
        "Event" / Int32ul,
        "ToState" / Int32ul
    )


@declare(guid=guid("eee173ef-7ed2-45de-9877-01c70a852fbd"), event_id=31, version=1)
class Microsoft_Windows_Serial_ClassExtension_V2_31_1(Etw):
    pattern = Struct(
        "TransferSmContext" / Int64ul,
        "Event" / Int32ul
    )


@declare(guid=guid("eee173ef-7ed2-45de-9877-01c70a852fbd"), event_id=32, version=1)
class Microsoft_Windows_Serial_ClassExtension_V2_32_1(Etw):
    pattern = Struct(
        "TransferSmContext" / Int64ul,
        "FromState" / Int32ul,
        "Event" / Int32ul,
        "ToState" / Int32ul
    )

