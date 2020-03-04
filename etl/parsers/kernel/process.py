# -*- coding: utf-8 -*-
from construct import Struct, Int64ul, Int32ul, Int32sl, RepeatUntil, Byte, Int16ul

from etl.dtyp import Sid
from etl.parsers.kernel.core import declare, Mof
from etl.utils import WString, CString
from etl.wmi import EventTraceGroup


@declare(group=EventTraceGroup.EVENT_TRACE_GROUP_PROCESS, version=3, event_types=[1, 2, 3, 4, 39])
class Process_V3_TypeGroup1(Mof):
    """
    Process Create/Exit Event
    1 : Start
    2 : End
    3 : DCStart
    4 : DCEnd
    39: Defunct
    """
    pattern = Struct(
        "UniqueProcessKey" / Int64ul,       # Pointer
        "ProcessId" / Int32ul,
        "ParentId" / Int32ul,
        "SessionId" / Int32ul,
        "ExitStatus" / Int32sl,
        "DirectoryTableBase" / Int64ul,     # Pointer
        "Sid" / Sid,
        "ImageFileName" / CString,
        "CommandLine" / WString
    )

    def get_image_file_name(self) -> str:
        """
        :return: Image file name
        """
        return bytearray(self.source.ImageFileName[:-1]).decode("utf8")

    def get_command_line(self) -> str:
        """
        :return: Associate command line of starting process
        """
        return bytearray(self.source.CommandLine[:-2]).decode("utf-16le")

    def get_package_full_name(self) -> str:
        """
        :return: Package full name
        """
        return bytearray(self.source.PackageFullName[:-2]).decode("utf-16le")

    def get_application_id(self) -> str:
        """
        :return: Application id
        """
        return bytearray(self.source.PackageFullName[:-2]).decode("utf-16le")

    def get_exit_status(self) -> int:
        """
        :return: exit status when process end
        """
        return self.source.ExitStatus

    def get_process_id(self) -> int:
        """
        :return: Process id
        """
        return self.source.ProcessId

    def get_parent_id(self) -> int:
        """
        :return: Return process id of parent process
        """
        return self.source.ParentId


@declare(group=EventTraceGroup.EVENT_TRACE_GROUP_PROCESS, version=4, event_types=[1, 2, 3, 4, 39])
class Process_V4_TypeGroup1(Mof):
    """
    Process Create/Exit Event
    1 : Start
    2 : End
    3 : DCStart
    4 : DCEnd
    39: Defunct
    """
    pattern = Struct(
        "UniqueProcessKey" / Int64ul,       # Pointer
        "ProcessId" / Int32ul,
        "ParentId" / Int32ul,
        "SessionId" / Int32ul,
        "ExitStatus" / Int32sl,
        "DirectoryTableBase" / Int64ul,     # Pointer
        "Flags" / Int32ul,
        "UserSID_blob" / Byte[16],
        "Sid" / Sid,
        "ImageFileName" / CString,
        "CommandLine" / WString,
        "PackageFullName" / WString,
        "ApplicationId" / WString
    )

    def get_image_file_name(self) -> str:
        """
        :return: Image file name
        """
        return bytearray(self.source.ImageFileName[:-1]).decode("utf8")

    def get_command_line(self) -> str:
        """
        :return: Associate command line of starting process
        """
        return bytearray(self.source.CommandLine[:-2]).decode("utf-16le")

    def get_package_full_name(self) -> str:
        """
        :return: Package full name
        """
        return bytearray(self.source.PackageFullName[:-2]).decode("utf-16le")

    def get_application_id(self) -> str:
        """
        :return: Application id
        """
        return bytearray(self.source.PackageFullName[:-2]).decode("utf-16le")

    def get_exit_status(self) -> int:
        """
        :return: exit status when process end
        """
        return self.source.ExitStatus

    def get_process_id(self) -> int:
        """
        :return: Process id
        """
        return self.source.ProcessId

    def get_parent_id(self) -> int:
        """
        :return: Return process id of parent process
        """
        return self.source.ParentId


@declare(group=EventTraceGroup.EVENT_TRACE_GROUP_PROCESS, version=5, event_types=[39])
class Process_Defunct_TypeGroup1(Process_V4_TypeGroup1):
    """
    Process Zombie Event
    39: Defunct
    """
    pattern = Struct(
        *Process_V4_TypeGroup1.pattern.subcons,
        "ExitTime" / Int64ul
    )


@declare(group=EventTraceGroup.EVENT_TRACE_GROUP_PROCESS, version=3, event_types=[10])
class ImageLoad(Mof):
    """
    This struct has not the correct HookId
    History...
    10: Load
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
        return self.source.ImageBase

    def get_image_size(self) -> int:
        return self.source.ImageSize


@declare(group=EventTraceGroup.EVENT_TRACE_GROUP_PROCESS, version=2, event_types=[11])
class Process_Terminate_TypeGroup1(Mof):
    pattern = Struct(
        "ProcessId" / Int32ul
    )

    def get_process_id(self):
        """
        :return: id of the terminated process
        """
        return self.source.ProcessId
