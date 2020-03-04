# -*- coding: utf-8 -*-
from etl.wmi import EventTraceGroup


class EtlException(Exception):
    """
    BAse exception for all other in etl-parser
    """
    def __init__(self, message):
        super().__init__(message)


class InvalidEtlFileHeader(EtlException):
    """
    Raise when the expected header is not found
    """
    def __init__(self):
        super().__init__("Invalid ETL file header : first chunk is not a valid WmiLogType header")


class GroupNotFound(EtlException):
    """
    Kernel group parser not found into etl-parser library
    Contact team cert@airbus.com or do a PR
    """
    def __init__(self, group: EventTraceGroup):
        super().__init__("No class handle this MOF group : %s"%group)


class VersionNotFound(EtlException):
    """
    Kernel event version parser not found into etl-parser library
    Contact team cert@airbus.com or do a PR
    """
    def __init__(self, group: EventTraceGroup, version: int):
        super().__init__("No class handle this group (%s) version : %s" % (group, version))


class EventTypeNotFound(EtlException):
    """
    Kernel event id parser not found into etl-parser library
    Contact team cert@airbus.com or do a PR
    """
    def __init__(self, group: EventTraceGroup, version: int, event_type: int):
        super().__init__("No class handle this group (%s) in version (%s) for event_type : %s" % (group, version, event_type))


class GuidNotFound(EtlException):
    """
    ETW parser not found into etl-parser library
    Contact team cert@airbus.com or do a PR
    """
    def __init__(self, guid):
        super().__init__("No class handle this ETW provider : (%s)"%guid)


class EventIdNotFound(EtlException):
    """
    ETW parser for this event id is not found into etl-parser library
    Contact team cert@airbus.com or do a PR
    """
    def __init__(self, guid, event_id: int):
        super().__init__("No class handle this ETW provider (%s) for event id : (%s)"%(guid, event_id))


class EtwVersionNotFound(EtlException):
    """
    ETW parser for this version is not found into etl-parser library
    Contact team cert@airbus.com or do a PR
    """
    def __init__(self, guid, event_id: int, version: int):
        super().__init__("No class handle this ETW provider (%s) for event id : (%s) for version : %s"%(guid, event_id, version))


class TlMetaDataNotFound(EtlException):
    """
    Tracelogging meta data not found
    """
    def __init__(self):
        super().__init__("Meta data not found for trace logging parser")


class TlUnhandledTag(EtlException):
    """
    This tag of tracelogging is not handled by etl-parser
    Contact team cert@airbus.com or do a PR
    """
    def __init__(self, tag):
        super().__init__("Cannot read tag type %s"%tag)


class InvalidType(EtlException):
    """
    Meta data type is not handle by converter
    """
    def __init__(self, type):
        super().__init__("The type %s is invalid"%type)