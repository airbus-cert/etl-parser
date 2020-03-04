# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Provisioning-Diagnostics-Provider
GUID : ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=10, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_10_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=11, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_11_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=12, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_12_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HRESULT" / Int32ul,
        "Message2" / WString,
        "Message3" / WString
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=20, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_20_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=21, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_21_0(Etw):
    pattern = Struct(
        "Message1" / WString
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=22, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_22_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=40, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_40_0(Etw):
    pattern = Struct(
        "Message1" / WString
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=42, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_42_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=45, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_45_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=60, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_60_0(Etw):
    pattern = Struct(
        "UInt1" / Int32ul
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=61, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_61_0(Etw):
    pattern = Struct(
        "Message1" / WString
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=62, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_62_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=63, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_63_0(Etw):
    pattern = Struct(
        "Message1" / WString
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=64, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_64_0(Etw):
    pattern = Struct(
        "Message1" / WString
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=65, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_65_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul,
        "Message1" / WString,
        "Uint1" / Int32ul
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=66, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_66_0(Etw):
    pattern = Struct(
        "Message1" / WString
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=67, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_67_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul,
        "Message1" / WString,
        "Uint1" / Int32ul
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=68, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_68_0(Etw):
    pattern = Struct(
        "Message1" / WString
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=69, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_69_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul,
        "Message1" / WString
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=70, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_70_0(Etw):
    pattern = Struct(
        "Int1" / Int32sl
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=71, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_71_0(Etw):
    pattern = Struct(
        "Int1" / Int32sl
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=72, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_72_0(Etw):
    pattern = Struct(
        "Int1" / Int32sl,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=80, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_80_0(Etw):
    pattern = Struct(
        "UInt1" / Int32ul
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=81, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_81_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=82, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_82_0(Etw):
    pattern = Struct(
        "UInt1" / Int32ul
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=83, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_83_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=90, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_90_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=91, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_91_0(Etw):
    pattern = Struct(
        "Message1" / WString
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=92, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_92_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul,
        "Message1" / WString
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=93, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_93_0(Etw):
    pattern = Struct(
        "Message1" / WString
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=94, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_94_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul,
        "Message1" / WString
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=100, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_100_0(Etw):
    pattern = Struct(
        "Message1" / WString
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=101, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_101_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Int1" / Int32sl
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=102, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_102_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul,
        "Message1" / WString
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=103, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_103_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=104, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_104_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul,
        "Message1" / WString
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=106, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_106_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=107, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_107_0(Etw):
    pattern = Struct(
        "Message1" / WString
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=108, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_108_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=109, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_109_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=110, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_110_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul,
        "Message1" / WString
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=112, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_112_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=113, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_113_0(Etw):
    pattern = Struct(
        "Int1" / Int32sl
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=115, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_115_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=153, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_153_0(Etw):
    pattern = Struct(
        "InitialState" / Int32ul,
        "UpdateState" / Int32ul
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=154, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_154_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=155, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_155_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=157, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_157_0(Etw):
    pattern = Struct(
        "UInt1" / Int64ul
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=171, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_171_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=172, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_172_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=173, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_173_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=174, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_174_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=175, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_175_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=176, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_176_0(Etw):
    pattern = Struct(
        "Uint1" / Int32ul,
        "Uint2" / Int32ul
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=177, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_177_0(Etw):
    pattern = Struct(
        "Uint1" / Int32ul,
        "Uint2" / Int32ul
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=178, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_178_0(Etw):
    pattern = Struct(
        "Int1" / Int32sl
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=179, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_179_0(Etw):
    pattern = Struct(
        "State" / Int32ul
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=180, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_180_0(Etw):
    pattern = Struct(
        "State" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=181, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_181_0(Etw):
    pattern = Struct(
        "State" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=182, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_182_0(Etw):
    pattern = Struct(
        "UInt1" / Int32ul
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=184, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_184_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=300, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_300_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=301, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_301_0(Etw):
    pattern = Struct(
        "State" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=302, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_302_0(Etw):
    pattern = Struct(
        "State" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=303, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_303_0(Etw):
    pattern = Struct(
        "State" / Int32ul
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=310, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_310_0(Etw):
    pattern = Struct(
        "Message1" / WString,
        "Message2" / WString,
        "Message3" / WString
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=311, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_311_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=312, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_312_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=313, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_313_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul,
        "Message1" / WString
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=1002, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_1002_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=1005, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_1005_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul,
        "File" / CString,
        "Line" / Int32sl,
        "Message" / WString
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=1006, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_1006_0(Etw):
    pattern = Struct(
        "Message1" / WString
    )


@declare(guid=guid("ed8b9bd3-f66e-4ff2-b86b-75c7925f72a9"), event_id=1008, version=0)
class Microsoft_Windows_Provisioning_Diagnostics_Provider_1008_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )

