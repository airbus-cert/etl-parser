# -*- coding: utf-8 -*-
from construct import Struct, Int64ul, RepeatUntil, Byte

from etl.parsers.kernel.core import declare, Mof
from etl.utils import WString
from etl.wmi import EventTraceGroup


@declare(group=EventTraceGroup.EVENT_TRACE_GROUP_FILE, version=2, event_types=[0, 32, 35, 36])
class FileIo_V2_Name(Mof):
    """
    File Name
    0 : Name
    32: FileCreate
    35: FileDelete
    36: FileRundown
    """
    pattern = Struct(
        "FileObject" / Int64ul,
        "FileName" / WString
    )

    def get_file_name(self) -> str:
        """
        :return: Associate filename
        """
        return bytearray(self.source.FileName[:-2]).decode("utf-16le")
