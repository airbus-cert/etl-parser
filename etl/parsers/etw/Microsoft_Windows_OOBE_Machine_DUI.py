# -*- coding: utf-8 -*-
"""
Microsoft-Windows-OOBE-Machine-DUI
GUID : f5dbaa02-15d6-4644-a784-7032d508bf64
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("f5dbaa02-15d6-4644-a784-7032d508bf64"), event_id=5106, version=0)
class Microsoft_Windows_OOBE_Machine_DUI_5106_0(Etw):
    pattern = Struct(
        "PluginName" / WString
    )


@declare(guid=guid("f5dbaa02-15d6-4644-a784-7032d508bf64"), event_id=5107, version=0)
class Microsoft_Windows_OOBE_Machine_DUI_5107_0(Etw):
    pattern = Struct(
        "PluginName" / WString
    )


@declare(guid=guid("f5dbaa02-15d6-4644-a784-7032d508bf64"), event_id=5108, version=0)
class Microsoft_Windows_OOBE_Machine_DUI_5108_0(Etw):
    pattern = Struct(
        "PluginName" / WString
    )


@declare(guid=guid("f5dbaa02-15d6-4644-a784-7032d508bf64"), event_id=5112, version=0)
class Microsoft_Windows_OOBE_Machine_DUI_5112_0(Etw):
    pattern = Struct(
        "DWORD" / Int32ul
    )


@declare(guid=guid("f5dbaa02-15d6-4644-a784-7032d508bf64"), event_id=5113, version=0)
class Microsoft_Windows_OOBE_Machine_DUI_5113_0(Etw):
    pattern = Struct(
        "DWORD" / Int32ul
    )


@declare(guid=guid("f5dbaa02-15d6-4644-a784-7032d508bf64"), event_id=5114, version=0)
class Microsoft_Windows_OOBE_Machine_DUI_5114_0(Etw):
    pattern = Struct(
        "DWORD" / Int32ul
    )


@declare(guid=guid("f5dbaa02-15d6-4644-a784-7032d508bf64"), event_id=5116, version=0)
class Microsoft_Windows_OOBE_Machine_DUI_5116_0(Etw):
    pattern = Struct(
        "val" / Int8ul
    )


@declare(guid=guid("f5dbaa02-15d6-4644-a784-7032d508bf64"), event_id=5117, version=0)
class Microsoft_Windows_OOBE_Machine_DUI_5117_0(Etw):
    pattern = Struct(
        "DWORD" / Int32ul
    )


@declare(guid=guid("f5dbaa02-15d6-4644-a784-7032d508bf64"), event_id=5120, version=0)
class Microsoft_Windows_OOBE_Machine_DUI_5120_0(Etw):
    pattern = Struct(
        "DWORD" / Int32ul
    )


@declare(guid=guid("f5dbaa02-15d6-4644-a784-7032d508bf64"), event_id=5121, version=0)
class Microsoft_Windows_OOBE_Machine_DUI_5121_0(Etw):
    pattern = Struct(
        "DWORD" / Int32ul,
        "Bool" / Int8ul
    )


@declare(guid=guid("f5dbaa02-15d6-4644-a784-7032d508bf64"), event_id=5122, version=0)
class Microsoft_Windows_OOBE_Machine_DUI_5122_0(Etw):
    pattern = Struct(
        "Text" / WString
    )


@declare(guid=guid("f5dbaa02-15d6-4644-a784-7032d508bf64"), event_id=5123, version=0)
class Microsoft_Windows_OOBE_Machine_DUI_5123_0(Etw):
    pattern = Struct(
        "Text" / WString
    )


@declare(guid=guid("f5dbaa02-15d6-4644-a784-7032d508bf64"), event_id=5124, version=0)
class Microsoft_Windows_OOBE_Machine_DUI_5124_0(Etw):
    pattern = Struct(
        "PluginName" / WString
    )


@declare(guid=guid("f5dbaa02-15d6-4644-a784-7032d508bf64"), event_id=5125, version=0)
class Microsoft_Windows_OOBE_Machine_DUI_5125_0(Etw):
    pattern = Struct(
        "PluginName" / WString
    )


@declare(guid=guid("f5dbaa02-15d6-4644-a784-7032d508bf64"), event_id=5128, version=0)
class Microsoft_Windows_OOBE_Machine_DUI_5128_0(Etw):
    pattern = Struct(
        "Text" / WString
    )


@declare(guid=guid("f5dbaa02-15d6-4644-a784-7032d508bf64"), event_id=5129, version=0)
class Microsoft_Windows_OOBE_Machine_DUI_5129_0(Etw):
    pattern = Struct(
        "Text" / WString
    )

