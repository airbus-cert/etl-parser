# -*- coding: utf-8 -*-
from construct import Struct, Int64ul, Int32ul, Byte, Int16ul, RepeatUntil

from etl.parsers.kernel.core import declare, Mof
from etl.utils import WString
from etl.wmi import EventTraceGroup


@declare(group=EventTraceGroup.EVENT_TRACE_GROUP_IMAGE, version=2, event_types=[33])
class KernelImageBase(Mof):
    pattern = Struct(
        "ImageBase" / Int64ul
    )

    def get_kernel_image_base(self) -> int:
        """
        :return: Return the kernel image base
        """
        return self.source.ImageBase


@declare(group=EventTraceGroup.EVENT_TRACE_GROUP_IMAGE, version=2, event_types=[34])
class HyperCallPage(Mof):
    pattern = Struct(
        "HypercallPageVa" / Int64ul
    )

    def get_hypercall_page_va(self):
        """
        :return: HyperCall page virtual address
        """
        return self.source.HypercallPageVa


@declare(group=EventTraceGroup.EVENT_TRACE_GROUP_IMAGE, version=3, event_types=[10, 2, 3, 4])
class ImageLoad(Mof):
    """
    Event use to notify module loading
    10: Load
    2 : Unload
    3 : DCStart
    4 : DCEnd
    """
    pattern = Struct(
        "ImageBase" / Int64ul,
        "ImageSize" / Int64ul,
        "ProcessId" / Int32ul,
        "ImageChecksum" / Int32ul,
        "TimeDateStamp" / Int32ul,
        "SignatureLevel" / Byte,
        "SignatureType" / Byte,
        "Reserved0" / Int16ul,
        "DefaultBase" / Int64ul,
        "Reserved1" / Int32ul,
        "Reserved2" / Int32ul,
        "Reserved3" / Int32ul,
        "Reserved4" / Int32ul,
        "FileName" / WString
    )

    def get_image_filename(self) -> str:
        """
        :return: Return image file name
        """
        return bytearray(self.source.FileName[:-2]).decode("utf-16le")

    def get_process_id(self) -> int:
        """
        :return: id of loader process
        """
        return self.source.ProcessId

    def get_image_base(self) -> int:
        """
        :return: Image base address
        """
        return self.source.ImageBase

    def get_image_size(self) -> int:
        """
        :return: Size of image in bytes
        """
        return self.source.ImageSize