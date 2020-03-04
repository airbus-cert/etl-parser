# -*- coding: utf-8 -*-

"""
Handle ETW parser logic
"""
from abc import ABCMeta
from typing import List

from construct import Container
from etl.error import GuidNotFound, EventIdNotFound, EtwVersionNotFound

__etw_factory__ = {}


class Guid:
    """
    Guid class for ETW def and management
    """
    def __init__(self, data1: int, data2: int, data3: int, data4: List[int]):
        self.data1 = data1
        self.data2 = data2
        self.data3 = data3
        self.data4 = data4

    def __hash__(self):
        return hash((self.data1, self.data2, self.data3, *self.data4))

    def __eq__(self, other):
        return (self.data1, self.data2, self.data3, self.data4) == (other.data1, other.data2, other.data3, other.data4)

    def __ne__(self, other):
        # Not strictly necessary, but to avoid having both x==y and x!=y
        # True at the same time
        return not (self == other)

    def __str__(self):
        return "%x-%x-%x-%s-%s" % (self.data1, self.data2, self.data3, "".join(["%x"%x for x in self.data4[0:2]]), "".join(["%x"%x for x in self.data4[2:]]))


def guid(guid_str: str) -> Guid:
    """
    Convert guid set as str into data
    :param guid_str:
    :return:
    """
    d1, d2, d3, d4, d5 = guid_str.split("-")
    return Guid(int(d1, 16), int(d2, 16), int(d3, 16), [int(d4[0:2], 16), int(d4[2:4], 16)] + [int(d5[x:x+2], 16) for x in range(0, len(d5), 2)])


def declare(*, guid: Guid, event_id: int, version: int) -> callable:
    """
    Declare class builder for a particular ETW provider identified by its GUID
    :param guid: provider id
    :param event_id: etx event id
    :param version: version of the etw scheme
    :return: cls
    """
    def wrapper(cls):
        if guid not in __etw_factory__.keys():
            __etw_factory__[guid] = {}
        if event_id not in __etw_factory__[guid].keys():
            __etw_factory__[guid][event_id] = {}
        __etw_factory__[guid][event_id][version] = cls
        return cls
    return wrapper


class Etw(metaclass=ABCMeta):
    """
    Base class for all ETW event
    """

    # Use construct pattern to parse event user data
    pattern = None

    def __init__(self, user_data):
        self.source = self.parse(user_data)

    def parse(self, user_data) -> Container:
        """
        Parse mof data stream
        :param user_data: raw mof data
        :return: construct container
        """
        return self.pattern.parse(user_data)


def build_etw(guid: Guid, event_id: int, version: int, user_data: bytes) -> Etw:
    """
    The ETW factory
    :param guid: ETW provider GUID
    :param event_id: Associate event id
    :param version: EtW version
    :param user_data: Event payload
    :return: Etw class
    :raise: GuidNotFound, EventIdNotFound, EtwVersionNotFound
    """

    if guid not in __etw_factory__.keys():
        raise GuidNotFound(guid)

    if event_id not in __etw_factory__[guid].keys():
        raise EventIdNotFound(guid, event_id)

    if version not in __etw_factory__[guid][event_id].keys():
        raise EtwVersionNotFound(guid, event_id, version)

    return __etw_factory__[guid][event_id][version](user_data)
