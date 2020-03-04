# -*- coding: utf-8 -*-
"""
This event have no public information
We reverse the format, and appears to encompass ETW
"""
from construct import Struct, Int16ul, Const, Int32ul, AlignedStruct, Computed, Bytes, Container

from etl.parsers.etw.core import Etw, build_etw, Guid as EtwGuid
from etl.utils import Guid

WinTraceHeader = Struct(
    "size" / Int16ul,
    "marker" / Const(0x9000, Int16ul),
    "event_id" / Int16ul,
    "flags" / Int16ul,
    "provider_id" / Guid,
    "thread_id" / Int32ul,
    "process_id" / Int32ul
)

WinTraceRecord = AlignedStruct(8,
    "mark1" / Computed(lambda this: this._io.tell()),
    "event_header" / WinTraceHeader,
    "mark2" / Computed(lambda this: this._io.tell()),
    "user_data" / Bytes(lambda this: this.event_header.size - (this.mark2 - this.mark1))
                               )


class WinTrace:
    """
    This is a python wrapper around construct struct to access interesting fields
    """

    def __init__(self, source: Container):
        """
        :param source Container: The EventTraceRecord Container once it's parsed
        """
        self.source = source

    def get_process_id(self) -> int:
        """
        Return the process id of issuer
        :return: process id of issuer
        """
        return self.source.event_header.process_id

    def get_thread_id(self) -> int:
        """
        Return the thread id of issuer
        :return: thread id of issuer
        """
        return self.source.event_header.thread_id

    def parse_etw(self) -> Etw:
        """
        Try to parse user data with known etw format (if it's an ETW log)
        :return: If known build associate Etw class
        :raise: GuidNotFound, EventIdNotFound, EtwVersionNotFound
        """
        guid = EtwGuid(self.source.event_header.provider_id.data1, self.source.event_header.provider_id.data2,
                    self.source.event_header.provider_id.data3, self.source.event_header.provider_id.data4)
        event_id = self.source.event_header.event_id
        version = 0 # this kind of event have no associated version
        user_data = self.source.user_data
        return build_etw(guid, event_id, version, user_data)
