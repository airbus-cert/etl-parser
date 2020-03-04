# -*- coding: utf-8 -*-

"""
Utils encompass a lot of well known structure definition
Which can be found in many other type definition
"""

from construct import Struct, Int32sl, Int16sl, Byte, Enum, Check, EnumInteger, Int16ul, Int32ul, RepeatUntil, Computed

"""
Global Unique Identifier
"""
Guid = Struct(
    "data1" / Int32ul,
    "data2" / Int16ul,
    "data3" / Int16ul,
    "data4" / Byte[8]
)

"""
System Time definition in Windows Internal
"""
SystemTime = Struct(
    "year" / Int16sl,
    "month" / Int16sl,
    "day_of_week" / Int16sl,
    "day" / Int16sl,
    "hour" / Int16sl,
    "minute" / Int16sl,
    "second" / Int16sl,
    "milliseconds" / Int16sl
)

"""
TimeZone Information definition in Windows Internal
"""
TimeZoneInformation = Struct(
    "bias" / Int32sl,
    "standard_name" / Byte[64],
    "standard_date" / SystemTime,
    "standard_bias" / Int32sl,
    "delight_name" / Byte[64],
    "delight_date" / SystemTime,
    "delight_bias" / Int32sl
)

PerfinfoGroupMask = Struct(
    "masks" / Int32ul[8]
)

"""
Wide string windows style
"""
WString = Struct(
    "type" / Computed("WString"),
    "string" / RepeatUntil(lambda x, lst, ctx: len(lst) % 2 == 0 and lst[-2:] == [0, 0], Byte)
)

"""
C string style
"""
CString = Struct(
    "type" / Computed("CString"),
    "string" / RepeatUntil(lambda x, lst, ctx: lst[-1:] == [0], Byte)
)


def check_enum(enum: Enum) -> Struct:
    """
    Enforce an enum value to be in enum range
    :param enum: source enum
    :return: Struct
    :raise: construct.core.CheckError
    """
    return Struct(
        "enum" / enum,
        Check(lambda this: not isinstance(this.enum, EnumInteger))
    )
