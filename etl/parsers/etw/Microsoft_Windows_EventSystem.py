# -*- coding: utf-8 -*-
"""
Microsoft-Windows-EventSystem
GUID : 899daace-4868-4295-afcd-9eb8fb497561
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("899daace-4868-4295-afcd-9eb8fb497561"), event_id=512, version=0)
class Microsoft_Windows_EventSystem_512_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("899daace-4868-4295-afcd-9eb8fb497561"), event_id=4354, version=0)
class Microsoft_Windows_EventSystem_4354_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "param5" / WString,
        "param6" / WString,
        "param7" / WString
    )


@declare(guid=guid("899daace-4868-4295-afcd-9eb8fb497561"), event_id=4355, version=0)
class Microsoft_Windows_EventSystem_4355_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )


@declare(guid=guid("899daace-4868-4295-afcd-9eb8fb497561"), event_id=4356, version=0)
class Microsoft_Windows_EventSystem_4356_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )


@declare(guid=guid("899daace-4868-4295-afcd-9eb8fb497561"), event_id=4357, version=0)
class Microsoft_Windows_EventSystem_4357_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "param5" / WString
    )


@declare(guid=guid("899daace-4868-4295-afcd-9eb8fb497561"), event_id=4358, version=0)
class Microsoft_Windows_EventSystem_4358_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("899daace-4868-4295-afcd-9eb8fb497561"), event_id=4359, version=0)
class Microsoft_Windows_EventSystem_4359_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString
    )


@declare(guid=guid("899daace-4868-4295-afcd-9eb8fb497561"), event_id=4361, version=0)
class Microsoft_Windows_EventSystem_4361_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("899daace-4868-4295-afcd-9eb8fb497561"), event_id=4362, version=0)
class Microsoft_Windows_EventSystem_4362_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("899daace-4868-4295-afcd-9eb8fb497561"), event_id=4609, version=0)
class Microsoft_Windows_EventSystem_4609_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )


@declare(guid=guid("899daace-4868-4295-afcd-9eb8fb497561"), event_id=4610, version=0)
class Microsoft_Windows_EventSystem_4610_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )


@declare(guid=guid("899daace-4868-4295-afcd-9eb8fb497561"), event_id=4611, version=0)
class Microsoft_Windows_EventSystem_4611_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("899daace-4868-4295-afcd-9eb8fb497561"), event_id=4612, version=0)
class Microsoft_Windows_EventSystem_4612_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("899daace-4868-4295-afcd-9eb8fb497561"), event_id=4613, version=0)
class Microsoft_Windows_EventSystem_4613_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "param5" / WString
    )


@declare(guid=guid("899daace-4868-4295-afcd-9eb8fb497561"), event_id=4614, version=0)
class Microsoft_Windows_EventSystem_4614_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )


@declare(guid=guid("899daace-4868-4295-afcd-9eb8fb497561"), event_id=4615, version=0)
class Microsoft_Windows_EventSystem_4615_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "param5" / WString
    )


@declare(guid=guid("899daace-4868-4295-afcd-9eb8fb497561"), event_id=4616, version=0)
class Microsoft_Windows_EventSystem_4616_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "param5" / WString
    )


@declare(guid=guid("899daace-4868-4295-afcd-9eb8fb497561"), event_id=4619, version=0)
class Microsoft_Windows_EventSystem_4619_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )


@declare(guid=guid("899daace-4868-4295-afcd-9eb8fb497561"), event_id=4620, version=0)
class Microsoft_Windows_EventSystem_4620_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString
    )


@declare(guid=guid("899daace-4868-4295-afcd-9eb8fb497561"), event_id=4621, version=0)
class Microsoft_Windows_EventSystem_4621_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "param5" / WString
    )


@declare(guid=guid("899daace-4868-4295-afcd-9eb8fb497561"), event_id=4622, version=0)
class Microsoft_Windows_EventSystem_4622_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("899daace-4868-4295-afcd-9eb8fb497561"), event_id=4623, version=0)
class Microsoft_Windows_EventSystem_4623_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString
    )


@declare(guid=guid("899daace-4868-4295-afcd-9eb8fb497561"), event_id=4624, version=0)
class Microsoft_Windows_EventSystem_4624_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "param5" / WString
    )


@declare(guid=guid("899daace-4868-4295-afcd-9eb8fb497561"), event_id=4625, version=0)
class Microsoft_Windows_EventSystem_4625_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )


@declare(guid=guid("899daace-4868-4295-afcd-9eb8fb497561"), event_id=4626, version=0)
class Microsoft_Windows_EventSystem_4626_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "param5" / WString,
        "param6" / WString,
        "param7" / WString
    )


@declare(guid=guid("899daace-4868-4295-afcd-9eb8fb497561"), event_id=4627, version=0)
class Microsoft_Windows_EventSystem_4627_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "param5" / WString,
        "param6" / WString,
        "param7" / WString,
        "param8" / WString
    )


@declare(guid=guid("899daace-4868-4295-afcd-9eb8fb497561"), event_id=4628, version=0)
class Microsoft_Windows_EventSystem_4628_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )


@declare(guid=guid("899daace-4868-4295-afcd-9eb8fb497561"), event_id=4629, version=0)
class Microsoft_Windows_EventSystem_4629_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "param5" / WString,
        "param6" / WString
    )

