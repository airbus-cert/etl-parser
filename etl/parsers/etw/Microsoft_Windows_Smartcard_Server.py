# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Smartcard-Server
GUID : 4fcbf664-a33a-4652-b436-9d558983d955
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("4fcbf664-a33a-4652-b436-9d558983d955"), event_id=1, version=0)
class Microsoft_Windows_Smartcard_Server_1_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("4fcbf664-a33a-4652-b436-9d558983d955"), event_id=201, version=0)
class Microsoft_Windows_Smartcard_Server_201_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("4fcbf664-a33a-4652-b436-9d558983d955"), event_id=204, version=0)
class Microsoft_Windows_Smartcard_Server_204_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("4fcbf664-a33a-4652-b436-9d558983d955"), event_id=205, version=0)
class Microsoft_Windows_Smartcard_Server_205_0(Etw):
    pattern = Struct(
        "Reader" / WString
    )


@declare(guid=guid("4fcbf664-a33a-4652-b436-9d558983d955"), event_id=504, version=0)
class Microsoft_Windows_Smartcard_Server_504_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("4fcbf664-a33a-4652-b436-9d558983d955"), event_id=506, version=0)
class Microsoft_Windows_Smartcard_Server_506_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("4fcbf664-a33a-4652-b436-9d558983d955"), event_id=508, version=0)
class Microsoft_Windows_Smartcard_Server_508_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("4fcbf664-a33a-4652-b436-9d558983d955"), event_id=509, version=0)
class Microsoft_Windows_Smartcard_Server_509_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("4fcbf664-a33a-4652-b436-9d558983d955"), event_id=510, version=0)
class Microsoft_Windows_Smartcard_Server_510_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("4fcbf664-a33a-4652-b436-9d558983d955"), event_id=511, version=0)
class Microsoft_Windows_Smartcard_Server_511_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("4fcbf664-a33a-4652-b436-9d558983d955"), event_id=512, version=0)
class Microsoft_Windows_Smartcard_Server_512_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("4fcbf664-a33a-4652-b436-9d558983d955"), event_id=513, version=0)
class Microsoft_Windows_Smartcard_Server_513_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("4fcbf664-a33a-4652-b436-9d558983d955"), event_id=514, version=0)
class Microsoft_Windows_Smartcard_Server_514_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "Reader" / WString
    )


@declare(guid=guid("4fcbf664-a33a-4652-b436-9d558983d955"), event_id=515, version=0)
class Microsoft_Windows_Smartcard_Server_515_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("4fcbf664-a33a-4652-b436-9d558983d955"), event_id=516, version=0)
class Microsoft_Windows_Smartcard_Server_516_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("4fcbf664-a33a-4652-b436-9d558983d955"), event_id=517, version=0)
class Microsoft_Windows_Smartcard_Server_517_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("4fcbf664-a33a-4652-b436-9d558983d955"), event_id=518, version=0)
class Microsoft_Windows_Smartcard_Server_518_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("4fcbf664-a33a-4652-b436-9d558983d955"), event_id=521, version=0)
class Microsoft_Windows_Smartcard_Server_521_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("4fcbf664-a33a-4652-b436-9d558983d955"), event_id=522, version=0)
class Microsoft_Windows_Smartcard_Server_522_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("4fcbf664-a33a-4652-b436-9d558983d955"), event_id=523, version=0)
class Microsoft_Windows_Smartcard_Server_523_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("4fcbf664-a33a-4652-b436-9d558983d955"), event_id=602, version=0)
class Microsoft_Windows_Smartcard_Server_602_0(Etw):
    pattern = Struct(
        "Reader" / WString
    )


@declare(guid=guid("4fcbf664-a33a-4652-b436-9d558983d955"), event_id=603, version=0)
class Microsoft_Windows_Smartcard_Server_603_0(Etw):
    pattern = Struct(
        "Reader" / WString
    )


@declare(guid=guid("4fcbf664-a33a-4652-b436-9d558983d955"), event_id=604, version=0)
class Microsoft_Windows_Smartcard_Server_604_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("4fcbf664-a33a-4652-b436-9d558983d955"), event_id=605, version=0)
class Microsoft_Windows_Smartcard_Server_605_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("4fcbf664-a33a-4652-b436-9d558983d955"), event_id=606, version=0)
class Microsoft_Windows_Smartcard_Server_606_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("4fcbf664-a33a-4652-b436-9d558983d955"), event_id=607, version=0)
class Microsoft_Windows_Smartcard_Server_607_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("4fcbf664-a33a-4652-b436-9d558983d955"), event_id=608, version=0)
class Microsoft_Windows_Smartcard_Server_608_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("4fcbf664-a33a-4652-b436-9d558983d955"), event_id=609, version=0)
class Microsoft_Windows_Smartcard_Server_609_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("4fcbf664-a33a-4652-b436-9d558983d955"), event_id=610, version=0)
class Microsoft_Windows_Smartcard_Server_610_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "Reader" / WString,
        "IOCTL" / WString,
        "CommandHeader" / WString
    )


@declare(guid=guid("4fcbf664-a33a-4652-b436-9d558983d955"), event_id=612, version=0)
class Microsoft_Windows_Smartcard_Server_612_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("4fcbf664-a33a-4652-b436-9d558983d955"), event_id=615, version=0)
class Microsoft_Windows_Smartcard_Server_615_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("4fcbf664-a33a-4652-b436-9d558983d955"), event_id=616, version=0)
class Microsoft_Windows_Smartcard_Server_616_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "Reader" / WString
    )


@declare(guid=guid("4fcbf664-a33a-4652-b436-9d558983d955"), event_id=617, version=0)
class Microsoft_Windows_Smartcard_Server_617_0(Etw):
    pattern = Struct(
        "Reader" / WString
    )


@declare(guid=guid("4fcbf664-a33a-4652-b436-9d558983d955"), event_id=618, version=0)
class Microsoft_Windows_Smartcard_Server_618_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("4fcbf664-a33a-4652-b436-9d558983d955"), event_id=619, version=0)
class Microsoft_Windows_Smartcard_Server_619_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "Reader" / WString,
        "IOCTL" / WString,
        "CommandHeader" / WString
    )


@declare(guid=guid("4fcbf664-a33a-4652-b436-9d558983d955"), event_id=620, version=0)
class Microsoft_Windows_Smartcard_Server_620_0(Etw):
    pattern = Struct(
        "Message" / WString,
        "Reader" / WString,
        "IOCTL" / WString,
        "CommandHeader" / WString
    )


@declare(guid=guid("4fcbf664-a33a-4652-b436-9d558983d955"), event_id=621, version=0)
class Microsoft_Windows_Smartcard_Server_621_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("4fcbf664-a33a-4652-b436-9d558983d955"), event_id=622, version=0)
class Microsoft_Windows_Smartcard_Server_622_0(Etw):
    pattern = Struct(
        "Message" / WString
    )


@declare(guid=guid("4fcbf664-a33a-4652-b436-9d558983d955"), event_id=623, version=0)
class Microsoft_Windows_Smartcard_Server_623_0(Etw):
    pattern = Struct(
        "Reader" / WString,
        "Timeout" / WString,
        "PID" / WString
    )

