# -*- coding: utf-8 -*-
"""
Microsoft-Windows-MCCS-DavSyncProvider
GUID : 5d86c4e2-8fcd-48d7-a713-9a04609c0189
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("5d86c4e2-8fcd-48d7-a713-9a04609c0189"), event_id=1, version=0)
class Microsoft_Windows_MCCS_DavSyncProvider_1_0(Etw):
    pattern = Struct(
        "P1_HResult" / Int32sl,
        "P2_String" / CString,
        "P3_UInt32" / Int32ul
    )


@declare(guid=guid("5d86c4e2-8fcd-48d7-a713-9a04609c0189"), event_id=2, version=0)
class Microsoft_Windows_MCCS_DavSyncProvider_2_0(Etw):
    pattern = Struct(
        "P1_HResult" / Int32sl,
        "P2_String" / CString,
        "P3_UInt32" / Int32ul
    )


@declare(guid=guid("5d86c4e2-8fcd-48d7-a713-9a04609c0189"), event_id=101, version=0)
class Microsoft_Windows_MCCS_DavSyncProvider_101_0(Etw):
    pattern = Struct(
        "Prop_Id" / Int32ul
    )


@declare(guid=guid("5d86c4e2-8fcd-48d7-a713-9a04609c0189"), event_id=102, version=0)
class Microsoft_Windows_MCCS_DavSyncProvider_102_0(Etw):
    pattern = Struct(
        "Prop_Id" / Int32ul
    )


@declare(guid=guid("5d86c4e2-8fcd-48d7-a713-9a04609c0189"), event_id=103, version=0)
class Microsoft_Windows_MCCS_DavSyncProvider_103_0(Etw):
    pattern = Struct(
        "Prop_Id" / Int32ul,
        "Prop_String" / WString,
        "Prop_Dword" / Int32ul,
        "Prop_Bool" / Int8ul
    )


@declare(guid=guid("5d86c4e2-8fcd-48d7-a713-9a04609c0189"), event_id=104, version=0)
class Microsoft_Windows_MCCS_DavSyncProvider_104_0(Etw):
    pattern = Struct(
        "Prop_Id" / Int32ul,
        "Prop_Dword" / Int32ul
    )


@declare(guid=guid("5d86c4e2-8fcd-48d7-a713-9a04609c0189"), event_id=105, version=0)
class Microsoft_Windows_MCCS_DavSyncProvider_105_0(Etw):
    pattern = Struct(
        "Prop_Id" / Int32ul,
        "Prop_Dword" / Int32ul
    )


@declare(guid=guid("5d86c4e2-8fcd-48d7-a713-9a04609c0189"), event_id=106, version=0)
class Microsoft_Windows_MCCS_DavSyncProvider_106_0(Etw):
    pattern = Struct(
        "Prop_Id" / Int32ul,
        "Prop_String" / WString,
        "Prop_HResult" / Int32sl
    )


@declare(guid=guid("5d86c4e2-8fcd-48d7-a713-9a04609c0189"), event_id=107, version=0)
class Microsoft_Windows_MCCS_DavSyncProvider_107_0(Etw):
    pattern = Struct(
        "Prop_Id" / Int32ul,
        "Prop_String" / WString,
        "Prop_Dword" / Int32ul,
        "Prop_Bool" / Int8ul
    )


@declare(guid=guid("5d86c4e2-8fcd-48d7-a713-9a04609c0189"), event_id=108, version=0)
class Microsoft_Windows_MCCS_DavSyncProvider_108_0(Etw):
    pattern = Struct(
        "Prop_Id" / Int32ul,
        "Prop_Dword" / Int32ul
    )


@declare(guid=guid("5d86c4e2-8fcd-48d7-a713-9a04609c0189"), event_id=109, version=0)
class Microsoft_Windows_MCCS_DavSyncProvider_109_0(Etw):
    pattern = Struct(
        "Prop_Id" / Int32ul,
        "Prop_String" / WString,
        "Prop_HResult" / Int32sl
    )


@declare(guid=guid("5d86c4e2-8fcd-48d7-a713-9a04609c0189"), event_id=110, version=0)
class Microsoft_Windows_MCCS_DavSyncProvider_110_0(Etw):
    pattern = Struct(
        "Prop_Id" / Int32ul,
        "Prop_String1" / WString,
        "Prop_String2" / WString,
        "Prop_Bool" / Int8ul
    )


@declare(guid=guid("5d86c4e2-8fcd-48d7-a713-9a04609c0189"), event_id=111, version=0)
class Microsoft_Windows_MCCS_DavSyncProvider_111_0(Etw):
    pattern = Struct(
        "Prop_Id" / Int32ul,
        "Prop_String1" / WString,
        "Prop_String2" / WString,
        "Prop_Dword" / Int32ul
    )


@declare(guid=guid("5d86c4e2-8fcd-48d7-a713-9a04609c0189"), event_id=112, version=0)
class Microsoft_Windows_MCCS_DavSyncProvider_112_0(Etw):
    pattern = Struct(
        "Prop_Id" / Int32ul,
        "Prop_Dword" / Int32ul
    )


@declare(guid=guid("5d86c4e2-8fcd-48d7-a713-9a04609c0189"), event_id=113, version=0)
class Microsoft_Windows_MCCS_DavSyncProvider_113_0(Etw):
    pattern = Struct(
        "Prop_Id" / Int32ul,
        "Prop_Dword" / Int32ul
    )


@declare(guid=guid("5d86c4e2-8fcd-48d7-a713-9a04609c0189"), event_id=114, version=0)
class Microsoft_Windows_MCCS_DavSyncProvider_114_0(Etw):
    pattern = Struct(
        "Prop_Id" / Int32ul
    )


@declare(guid=guid("5d86c4e2-8fcd-48d7-a713-9a04609c0189"), event_id=115, version=0)
class Microsoft_Windows_MCCS_DavSyncProvider_115_0(Etw):
    pattern = Struct(
        "Prop_Id" / Int32ul,
        "Prop_Dword" / Int32ul
    )


@declare(guid=guid("5d86c4e2-8fcd-48d7-a713-9a04609c0189"), event_id=116, version=0)
class Microsoft_Windows_MCCS_DavSyncProvider_116_0(Etw):
    pattern = Struct(
        "Prop_Id" / Int32ul,
        "Prop_String" / WString,
        "Prop_Dword" / Int32ul
    )


@declare(guid=guid("5d86c4e2-8fcd-48d7-a713-9a04609c0189"), event_id=117, version=0)
class Microsoft_Windows_MCCS_DavSyncProvider_117_0(Etw):
    pattern = Struct(
        "Prop_Id" / Int32ul
    )


@declare(guid=guid("5d86c4e2-8fcd-48d7-a713-9a04609c0189"), event_id=118, version=0)
class Microsoft_Windows_MCCS_DavSyncProvider_118_0(Etw):
    pattern = Struct(
        "Prop_Id" / Int32ul,
        "Prop_Bool" / Int8ul
    )


@declare(guid=guid("5d86c4e2-8fcd-48d7-a713-9a04609c0189"), event_id=119, version=0)
class Microsoft_Windows_MCCS_DavSyncProvider_119_0(Etw):
    pattern = Struct(
        "Prop_Id" / Int32ul
    )


@declare(guid=guid("5d86c4e2-8fcd-48d7-a713-9a04609c0189"), event_id=120, version=0)
class Microsoft_Windows_MCCS_DavSyncProvider_120_0(Etw):
    pattern = Struct(
        "Prop_Id" / Int32ul
    )


@declare(guid=guid("5d86c4e2-8fcd-48d7-a713-9a04609c0189"), event_id=121, version=0)
class Microsoft_Windows_MCCS_DavSyncProvider_121_0(Etw):
    pattern = Struct(
        "Prop_Dword" / Int32ul
    )


@declare(guid=guid("5d86c4e2-8fcd-48d7-a713-9a04609c0189"), event_id=122, version=0)
class Microsoft_Windows_MCCS_DavSyncProvider_122_0(Etw):
    pattern = Struct(
        "Prop_Id" / Int32ul,
        "Prop_String" / WString,
        "Prop_Dword" / Int32ul
    )


@declare(guid=guid("5d86c4e2-8fcd-48d7-a713-9a04609c0189"), event_id=123, version=0)
class Microsoft_Windows_MCCS_DavSyncProvider_123_0(Etw):
    pattern = Struct(
        "Prop_Id" / Int32ul,
        "Prop_String" / WString,
        "Prop_Dword" / Int32ul
    )


@declare(guid=guid("5d86c4e2-8fcd-48d7-a713-9a04609c0189"), event_id=124, version=0)
class Microsoft_Windows_MCCS_DavSyncProvider_124_0(Etw):
    pattern = Struct(
        "Prop_Dword" / Int32ul
    )


@declare(guid=guid("5d86c4e2-8fcd-48d7-a713-9a04609c0189"), event_id=125, version=0)
class Microsoft_Windows_MCCS_DavSyncProvider_125_0(Etw):
    pattern = Struct(
        "Prop_Id" / Int32ul
    )


@declare(guid=guid("5d86c4e2-8fcd-48d7-a713-9a04609c0189"), event_id=126, version=0)
class Microsoft_Windows_MCCS_DavSyncProvider_126_0(Etw):
    pattern = Struct(
        "Prop_Dword" / Int32ul
    )


@declare(guid=guid("5d86c4e2-8fcd-48d7-a713-9a04609c0189"), event_id=127, version=0)
class Microsoft_Windows_MCCS_DavSyncProvider_127_0(Etw):
    pattern = Struct(
        "Prop_Dword" / Int32ul
    )


@declare(guid=guid("5d86c4e2-8fcd-48d7-a713-9a04609c0189"), event_id=128, version=0)
class Microsoft_Windows_MCCS_DavSyncProvider_128_0(Etw):
    pattern = Struct(
        "Prop_Dword" / Int32ul
    )


@declare(guid=guid("5d86c4e2-8fcd-48d7-a713-9a04609c0189"), event_id=129, version=0)
class Microsoft_Windows_MCCS_DavSyncProvider_129_0(Etw):
    pattern = Struct(
        "Prop_Id" / Int32ul,
        "Prop_Dword" / Int32ul
    )


@declare(guid=guid("5d86c4e2-8fcd-48d7-a713-9a04609c0189"), event_id=130, version=0)
class Microsoft_Windows_MCCS_DavSyncProvider_130_0(Etw):
    pattern = Struct(
        "Prop_Id" / Int32ul,
        "Prop_Type" / Int32ul
    )


@declare(guid=guid("5d86c4e2-8fcd-48d7-a713-9a04609c0189"), event_id=131, version=0)
class Microsoft_Windows_MCCS_DavSyncProvider_131_0(Etw):
    pattern = Struct(
        "Prop_Id" / Int32ul,
        "Prop_Type" / Int32ul,
        "Prop_Dword" / Int32ul
    )


@declare(guid=guid("5d86c4e2-8fcd-48d7-a713-9a04609c0189"), event_id=132, version=0)
class Microsoft_Windows_MCCS_DavSyncProvider_132_0(Etw):
    pattern = Struct(
        "Prop_Id" / Int32ul
    )


@declare(guid=guid("5d86c4e2-8fcd-48d7-a713-9a04609c0189"), event_id=133, version=0)
class Microsoft_Windows_MCCS_DavSyncProvider_133_0(Etw):
    pattern = Struct(
        "Prop_Id" / Int32ul,
        "Prop_Bool" / Int8ul
    )


@declare(guid=guid("5d86c4e2-8fcd-48d7-a713-9a04609c0189"), event_id=134, version=0)
class Microsoft_Windows_MCCS_DavSyncProvider_134_0(Etw):
    pattern = Struct(
        "Prop_Id" / Int32ul
    )


@declare(guid=guid("5d86c4e2-8fcd-48d7-a713-9a04609c0189"), event_id=135, version=0)
class Microsoft_Windows_MCCS_DavSyncProvider_135_0(Etw):
    pattern = Struct(
        "Prop_Id" / Int32ul,
        "Prop_String" / WString
    )


@declare(guid=guid("5d86c4e2-8fcd-48d7-a713-9a04609c0189"), event_id=136, version=0)
class Microsoft_Windows_MCCS_DavSyncProvider_136_0(Etw):
    pattern = Struct(
        "Prop_Id1" / Int32ul,
        "Prop_Id2" / Int32ul,
        "Prop_String" / WString
    )


@declare(guid=guid("5d86c4e2-8fcd-48d7-a713-9a04609c0189"), event_id=137, version=0)
class Microsoft_Windows_MCCS_DavSyncProvider_137_0(Etw):
    pattern = Struct(
        "Prop_Id" / Int32ul
    )


@declare(guid=guid("5d86c4e2-8fcd-48d7-a713-9a04609c0189"), event_id=138, version=0)
class Microsoft_Windows_MCCS_DavSyncProvider_138_0(Etw):
    pattern = Struct(
        "Prop_Id" / Int32ul,
        "Prop_Bool" / Int8ul
    )


@declare(guid=guid("5d86c4e2-8fcd-48d7-a713-9a04609c0189"), event_id=168, version=0)
class Microsoft_Windows_MCCS_DavSyncProvider_168_0(Etw):
    pattern = Struct(
        "Prop_Guid" / Guid,
        "Prop_HexInt32" / Int32ul
    )


@declare(guid=guid("5d86c4e2-8fcd-48d7-a713-9a04609c0189"), event_id=171, version=0)
class Microsoft_Windows_MCCS_DavSyncProvider_171_0(Etw):
    pattern = Struct(
        "Prop_String" / WString
    )


@declare(guid=guid("5d86c4e2-8fcd-48d7-a713-9a04609c0189"), event_id=172, version=0)
class Microsoft_Windows_MCCS_DavSyncProvider_172_0(Etw):
    pattern = Struct(
        "Prop_Id" / Int32ul
    )

