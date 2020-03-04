# -*- coding: utf-8 -*-

"""
:see: https://github.com/tpn/winsdk-10/blob/master/Include/10.0.10240.0/km/wmicore.mof
"""
from abc import ABCMeta
from typing import List, Container

from construct import Struct, Int64ul, Int32ul, Int32sl, Byte, RepeatUntil, Int16ul, Enum

from etl.dtyp import Sid
from etl.error import GroupNotFound, VersionNotFound, EventTypeNotFound
from etl.utils import TimeZoneInformation
from etl.wmi import EventTraceGroup


__mof_factory__ = {}


def declare(*, group: Enum, version: int, event_types: List[int]) -> callable:
    """
    Declare class builder for a particular MOF group version and event types
    :param group: Event trace group
    :param version: version of mof class
    :param event_types: list of event type
    :return: cls
    """
    def wrapper(cls):
        for event_type in event_types:
            if group not in __mof_factory__.keys():
                __mof_factory__[group] = {}
            if version not in __mof_factory__[group].keys():
                __mof_factory__[group][version] = {}

            __mof_factory__[group][version][event_type] = cls
        return cls
    return wrapper


class Mof(metaclass=ABCMeta):
    """
    Top class for inheritance purpose
    """

    # Use construct pattern to parse mof data
    pattern = None

    # Event type handled
    event_types = {
        0: "Name",
        1: "Start",
        2: "End",
        3: "DCStart",
        4: "DCEnd",
        10: "Read",
        11: "Write",
        32: "FileCreate",
        33: "KernelBase",
        34: "HypercallPage",
        35: "FileDelete",
        36: "FileRundown",
        39: "Defunct",
        55: "OpticalRead",
        56: "OpticalWrite"
    }

    def __init__(self, mof_data, event_type: int):
        self.source = self.parse(mof_data)
        self.event_type = event_type

    def parse(self, mof_data) -> Container:
        """
        Parse mof data stream
        :param mof_data: raw mof data
        :return: construct container
        """
        return self.pattern.parse(mof_data)

    def get_event_definition(self):
        """
        :return: name of event definition
        """
        return self.event_types[self.event_type]


def build_mof(group: Enum, version: int, event_type: int, mof_data: bytes) -> Mof:
    """
    The MOF factory
    :param group: event trace group
    :param version: event trace version of mof
    :param event_type: event type handle by mof structure
    :param mof_data: raw mof data
    :return:
    """
    if group not in __mof_factory__.keys():
        raise GroupNotFound(group)

    if version not in __mof_factory__[group].keys():
        raise VersionNotFound(group, version)

    if event_type not in __mof_factory__[group][version].keys():
        raise EventTypeNotFound(group, version, event_type)

    return __mof_factory__[group][version][event_type](mof_data, event_type)



