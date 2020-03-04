# -*- coding: utf-8 -*-
"""
Microsoft-Windows-WPD-MTPUS
GUID : dcfc4489-9ce0-403c-99df-a05422c60898
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("dcfc4489-9ce0-403c-99df-a05422c60898"), event_id=100, version=0)
class Microsoft_Windows_WPD_MTPUS_100_0(Etw):
    pattern = Struct(
        "MTPUSLength" / Int32ul,
        "MTPUSData" / Bytes(lambda this: this.MTPUSLength)
    )


@declare(guid=guid("dcfc4489-9ce0-403c-99df-a05422c60898"), event_id=101, version=0)
class Microsoft_Windows_WPD_MTPUS_101_0(Etw):
    pattern = Struct(
        "MTPUSLength" / Int32ul,
        "MTPUSData" / Bytes(lambda this: this.MTPUSLength)
    )


@declare(guid=guid("dcfc4489-9ce0-403c-99df-a05422c60898"), event_id=102, version=0)
class Microsoft_Windows_WPD_MTPUS_102_0(Etw):
    pattern = Struct(
        "MTPUSLength" / Int32ul,
        "MTPUSData" / Bytes(lambda this: this.MTPUSLength)
    )


@declare(guid=guid("dcfc4489-9ce0-403c-99df-a05422c60898"), event_id=103, version=0)
class Microsoft_Windows_WPD_MTPUS_103_0(Etw):
    pattern = Struct(
        "MTPUSLength" / Int32ul,
        "MTPUSData" / Bytes(lambda this: this.MTPUSLength)
    )


@declare(guid=guid("dcfc4489-9ce0-403c-99df-a05422c60898"), event_id=104, version=0)
class Microsoft_Windows_WPD_MTPUS_104_0(Etw):
    pattern = Struct(
        "MTPUSLength" / Int32ul,
        "MTPUSData" / Bytes(lambda this: this.MTPUSLength)
    )


@declare(guid=guid("dcfc4489-9ce0-403c-99df-a05422c60898"), event_id=105, version=0)
class Microsoft_Windows_WPD_MTPUS_105_0(Etw):
    pattern = Struct(
        "WINUSB_SETUP_PACKET_LENGTH" / Int16ul,
        "WINUSB_SETUP_PACKET" / Bytes(lambda this: this.WINUSB_SETUP_PACKET_LENGTH),
        "ControlTransferBufferLength" / Int32ul,
        "ControlTransferBuffer" / Bytes(lambda this: this.ControlTransferBufferLength)
    )


@declare(guid=guid("dcfc4489-9ce0-403c-99df-a05422c60898"), event_id=106, version=0)
class Microsoft_Windows_WPD_MTPUS_106_0(Etw):
    pattern = Struct(
        "WINUSB_SETUP_PACKET_LENGTH" / Int16ul,
        "WINUSB_SETUP_PACKET" / Bytes(lambda this: this.WINUSB_SETUP_PACKET_LENGTH)
    )


@declare(guid=guid("dcfc4489-9ce0-403c-99df-a05422c60898"), event_id=107, version=0)
class Microsoft_Windows_WPD_MTPUS_107_0(Etw):
    pattern = Struct(
        "WINUSB_SETUP_PACKET_LENGTH" / Int16ul,
        "WINUSB_SETUP_PACKET" / Bytes(lambda this: this.WINUSB_SETUP_PACKET_LENGTH),
        "ControlTransferBufferLength" / Int32ul,
        "ControlTransferBuffer" / Bytes(lambda this: this.ControlTransferBufferLength)
    )


@declare(guid=guid("dcfc4489-9ce0-403c-99df-a05422c60898"), event_id=200, version=0)
class Microsoft_Windows_WPD_MTPUS_200_0(Etw):
    pattern = Struct(
        "MTPUSLength" / Int32ul,
        "MTPUSData" / Bytes(lambda this: this.MTPUSLength)
    )


@declare(guid=guid("dcfc4489-9ce0-403c-99df-a05422c60898"), event_id=201, version=0)
class Microsoft_Windows_WPD_MTPUS_201_0(Etw):
    pattern = Struct(
        "MTPUSLength" / Int32ul,
        "MTPUSData" / Bytes(lambda this: this.MTPUSLength)
    )


@declare(guid=guid("dcfc4489-9ce0-403c-99df-a05422c60898"), event_id=202, version=0)
class Microsoft_Windows_WPD_MTPUS_202_0(Etw):
    pattern = Struct(
        "MTPUSLength" / Int32ul,
        "MTPUSData" / Bytes(lambda this: this.MTPUSLength)
    )


@declare(guid=guid("dcfc4489-9ce0-403c-99df-a05422c60898"), event_id=203, version=0)
class Microsoft_Windows_WPD_MTPUS_203_0(Etw):
    pattern = Struct(
        "MTPUSLength" / Int32ul,
        "MTPUSData" / Bytes(lambda this: this.MTPUSLength)
    )


@declare(guid=guid("dcfc4489-9ce0-403c-99df-a05422c60898"), event_id=204, version=0)
class Microsoft_Windows_WPD_MTPUS_204_0(Etw):
    pattern = Struct(
        "MTPUSLength" / Int32ul,
        "MTPUSData" / Bytes(lambda this: this.MTPUSLength)
    )


@declare(guid=guid("dcfc4489-9ce0-403c-99df-a05422c60898"), event_id=205, version=0)
class Microsoft_Windows_WPD_MTPUS_205_0(Etw):
    pattern = Struct(
        "MTPUSLength" / Int32ul,
        "MTPUSData" / Bytes(lambda this: this.MTPUSLength)
    )


@declare(guid=guid("dcfc4489-9ce0-403c-99df-a05422c60898"), event_id=206, version=0)
class Microsoft_Windows_WPD_MTPUS_206_0(Etw):
    pattern = Struct(
        "MTPUSLength" / Int32ul,
        "MTPUSData" / Bytes(lambda this: this.MTPUSLength)
    )


@declare(guid=guid("dcfc4489-9ce0-403c-99df-a05422c60898"), event_id=207, version=0)
class Microsoft_Windows_WPD_MTPUS_207_0(Etw):
    pattern = Struct(
        "MTPUSLength" / Int32ul,
        "MTPUSData" / Bytes(lambda this: this.MTPUSLength)
    )


@declare(guid=guid("dcfc4489-9ce0-403c-99df-a05422c60898"), event_id=208, version=0)
class Microsoft_Windows_WPD_MTPUS_208_0(Etw):
    pattern = Struct(
        "MTPUSLength" / Int32ul,
        "MTPUSData" / Bytes(lambda this: this.MTPUSLength)
    )

