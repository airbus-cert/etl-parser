# -*- coding: utf-8 -*-
"""
Microsoft-Windows-EFS
GUID : 3663a992-84be-40ea-bba9-90c7ed544222
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=1, version=0)
class Microsoft_Windows_EFS_1_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul,
        "Param" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=2, version=0)
class Microsoft_Windows_EFS_2_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul,
        "Param1" / Int32ul,
        "Param2" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=3, version=0)
class Microsoft_Windows_EFS_3_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul,
        "Param1" / Int32ul,
        "Param2" / Int32ul,
        "Param3" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=4, version=0)
class Microsoft_Windows_EFS_4_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul,
        "Param" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=256, version=0)
class Microsoft_Windows_EFS_256_0(Etw):
    pattern = Struct(
        "CertValidated" / Int32ul,
        "cbHash" / Int32ul,
        "pbHash" / CString,
        "ContainerName" / WString,
        "ProviderName" / WString,
        "DisplayInformation" / WString,
        "dwCapabilities" / CString,
        "bIsCurrentKey" / CString,
        "eKeyType" / CString
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=257, version=0)
class Microsoft_Windows_EFS_257_0(Etw):
    pattern = Struct(
        "CertValidated" / Int32ul,
        "cbHash" / Int32ul,
        "pbHash" / CString,
        "ContainerName" / WString,
        "ProviderName" / WString,
        "DisplayInformation" / WString,
        "dwCapabilities" / CString,
        "bIsCurrentKey" / CString,
        "eKeyType" / CString
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=258, version=0)
class Microsoft_Windows_EFS_258_0(Etw):
    pattern = Struct(
        "CertValidated" / Int32ul,
        "cbHash" / Int32ul,
        "pbHash" / CString,
        "ContainerName" / WString,
        "ProviderName" / WString,
        "DisplayInformation" / WString,
        "dwCapabilities" / CString,
        "bIsCurrentKey" / CString,
        "eKeyType" / CString
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=259, version=0)
class Microsoft_Windows_EFS_259_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=260, version=0)
class Microsoft_Windows_EFS_260_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=261, version=0)
class Microsoft_Windows_EFS_261_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=262, version=0)
class Microsoft_Windows_EFS_262_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=263, version=0)
class Microsoft_Windows_EFS_263_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=264, version=0)
class Microsoft_Windows_EFS_264_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=265, version=0)
class Microsoft_Windows_EFS_265_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=272, version=0)
class Microsoft_Windows_EFS_272_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=273, version=0)
class Microsoft_Windows_EFS_273_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=274, version=0)
class Microsoft_Windows_EFS_274_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=275, version=0)
class Microsoft_Windows_EFS_275_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=276, version=0)
class Microsoft_Windows_EFS_276_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=277, version=0)
class Microsoft_Windows_EFS_277_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=278, version=0)
class Microsoft_Windows_EFS_278_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=279, version=0)
class Microsoft_Windows_EFS_279_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=280, version=0)
class Microsoft_Windows_EFS_280_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=281, version=0)
class Microsoft_Windows_EFS_281_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=288, version=0)
class Microsoft_Windows_EFS_288_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=289, version=0)
class Microsoft_Windows_EFS_289_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=290, version=0)
class Microsoft_Windows_EFS_290_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=512, version=0)
class Microsoft_Windows_EFS_512_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul,
        "Param" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=513, version=0)
class Microsoft_Windows_EFS_513_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=514, version=0)
class Microsoft_Windows_EFS_514_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=515, version=0)
class Microsoft_Windows_EFS_515_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=516, version=0)
class Microsoft_Windows_EFS_516_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=517, version=0)
class Microsoft_Windows_EFS_517_0(Etw):
    pattern = Struct(
        "CertValidated" / Int32ul,
        "cbHash" / Int32ul,
        "pbHash" / CString,
        "ContainerName" / WString,
        "ProviderName" / WString,
        "DisplayInformation" / WString,
        "dwCapabilities" / CString,
        "bIsCurrentKey" / CString,
        "eKeyType" / CString
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=518, version=0)
class Microsoft_Windows_EFS_518_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=519, version=0)
class Microsoft_Windows_EFS_519_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=520, version=0)
class Microsoft_Windows_EFS_520_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=521, version=0)
class Microsoft_Windows_EFS_521_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=768, version=0)
class Microsoft_Windows_EFS_768_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=769, version=0)
class Microsoft_Windows_EFS_769_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=770, version=0)
class Microsoft_Windows_EFS_770_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=771, version=0)
class Microsoft_Windows_EFS_771_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul,
        "Param" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=772, version=0)
class Microsoft_Windows_EFS_772_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=773, version=0)
class Microsoft_Windows_EFS_773_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=774, version=0)
class Microsoft_Windows_EFS_774_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=775, version=0)
class Microsoft_Windows_EFS_775_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=776, version=0)
class Microsoft_Windows_EFS_776_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=777, version=0)
class Microsoft_Windows_EFS_777_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=784, version=0)
class Microsoft_Windows_EFS_784_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=785, version=0)
class Microsoft_Windows_EFS_785_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=786, version=0)
class Microsoft_Windows_EFS_786_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=787, version=0)
class Microsoft_Windows_EFS_787_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=788, version=0)
class Microsoft_Windows_EFS_788_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=789, version=0)
class Microsoft_Windows_EFS_789_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=790, version=0)
class Microsoft_Windows_EFS_790_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=791, version=0)
class Microsoft_Windows_EFS_791_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=792, version=0)
class Microsoft_Windows_EFS_792_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=793, version=0)
class Microsoft_Windows_EFS_793_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=800, version=0)
class Microsoft_Windows_EFS_800_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=801, version=0)
class Microsoft_Windows_EFS_801_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=802, version=0)
class Microsoft_Windows_EFS_802_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=803, version=0)
class Microsoft_Windows_EFS_803_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=804, version=0)
class Microsoft_Windows_EFS_804_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=805, version=0)
class Microsoft_Windows_EFS_805_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=1024, version=0)
class Microsoft_Windows_EFS_1024_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=1040, version=0)
class Microsoft_Windows_EFS_1040_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=1041, version=0)
class Microsoft_Windows_EFS_1041_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=1042, version=0)
class Microsoft_Windows_EFS_1042_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=1280, version=0)
class Microsoft_Windows_EFS_1280_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul,
        "Param1" / Int32ul,
        "Param2" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=1281, version=0)
class Microsoft_Windows_EFS_1281_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul,
        "Param1" / Int32ul,
        "Param2" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=1282, version=0)
class Microsoft_Windows_EFS_1282_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul,
        "DomainName" / WString,
        "UserName" / WString,
        "AttackId" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=1283, version=0)
class Microsoft_Windows_EFS_1283_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=1284, version=0)
class Microsoft_Windows_EFS_1284_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=1536, version=0)
class Microsoft_Windows_EFS_1536_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=1537, version=0)
class Microsoft_Windows_EFS_1537_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=1538, version=0)
class Microsoft_Windows_EFS_1538_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=1539, version=0)
class Microsoft_Windows_EFS_1539_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=1540, version=0)
class Microsoft_Windows_EFS_1540_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=1541, version=0)
class Microsoft_Windows_EFS_1541_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=1542, version=0)
class Microsoft_Windows_EFS_1542_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=1543, version=0)
class Microsoft_Windows_EFS_1543_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=1544, version=0)
class Microsoft_Windows_EFS_1544_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=1545, version=0)
class Microsoft_Windows_EFS_1545_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul,
        "Param1" / Int32ul,
        "Param2" / Int32ul,
        "Param3" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=4096, version=0)
class Microsoft_Windows_EFS_4096_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=4097, version=0)
class Microsoft_Windows_EFS_4097_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=4098, version=0)
class Microsoft_Windows_EFS_4098_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=4099, version=0)
class Microsoft_Windows_EFS_4099_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=4100, version=0)
class Microsoft_Windows_EFS_4100_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=4101, version=0)
class Microsoft_Windows_EFS_4101_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=4102, version=0)
class Microsoft_Windows_EFS_4102_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=4353, version=0)
class Microsoft_Windows_EFS_4353_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=4354, version=0)
class Microsoft_Windows_EFS_4354_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=4355, version=0)
class Microsoft_Windows_EFS_4355_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=4356, version=0)
class Microsoft_Windows_EFS_4356_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=4357, version=0)
class Microsoft_Windows_EFS_4357_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=4358, version=0)
class Microsoft_Windows_EFS_4358_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul,
        "Param1" / WString
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=4359, version=0)
class Microsoft_Windows_EFS_4359_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul,
        "Param1" / WString
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=4360, version=0)
class Microsoft_Windows_EFS_4360_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul,
        "Param1" / WString
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=4361, version=0)
class Microsoft_Windows_EFS_4361_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul,
        "Param1" / WString
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=4368, version=0)
class Microsoft_Windows_EFS_4368_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul,
        "Param1" / WString
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=4369, version=0)
class Microsoft_Windows_EFS_4369_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul,
        "Param1" / WString,
        "Param2" / WString
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=4370, version=0)
class Microsoft_Windows_EFS_4370_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul,
        "Param1" / WString,
        "Param2" / WString
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=4371, version=0)
class Microsoft_Windows_EFS_4371_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul,
        "Param1" / WString,
        "Param2" / WString
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=4372, version=0)
class Microsoft_Windows_EFS_4372_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul,
        "Param1" / WString,
        "Param2" / WString
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=4373, version=0)
class Microsoft_Windows_EFS_4373_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul,
        "Param1" / WString,
        "Param2" / WString
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=4374, version=0)
class Microsoft_Windows_EFS_4374_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul,
        "Param1" / WString,
        "Param2" / WString
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=4375, version=0)
class Microsoft_Windows_EFS_4375_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=4376, version=0)
class Microsoft_Windows_EFS_4376_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=4377, version=0)
class Microsoft_Windows_EFS_4377_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul,
        "Param" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=4378, version=0)
class Microsoft_Windows_EFS_4378_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul,
        "Param" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=4379, version=0)
class Microsoft_Windows_EFS_4379_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=4380, version=0)
class Microsoft_Windows_EFS_4380_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=4381, version=0)
class Microsoft_Windows_EFS_4381_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=4382, version=0)
class Microsoft_Windows_EFS_4382_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=4383, version=0)
class Microsoft_Windows_EFS_4383_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=4384, version=0)
class Microsoft_Windows_EFS_4384_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=4385, version=0)
class Microsoft_Windows_EFS_4385_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=4386, version=0)
class Microsoft_Windows_EFS_4386_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=4387, version=0)
class Microsoft_Windows_EFS_4387_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=4388, version=0)
class Microsoft_Windows_EFS_4388_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=4389, version=0)
class Microsoft_Windows_EFS_4389_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=4390, version=0)
class Microsoft_Windows_EFS_4390_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=4391, version=0)
class Microsoft_Windows_EFS_4391_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=4392, version=0)
class Microsoft_Windows_EFS_4392_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=4393, version=0)
class Microsoft_Windows_EFS_4393_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=4400, version=0)
class Microsoft_Windows_EFS_4400_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=4401, version=0)
class Microsoft_Windows_EFS_4401_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=4402, version=0)
class Microsoft_Windows_EFS_4402_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=4403, version=0)
class Microsoft_Windows_EFS_4403_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=4404, version=0)
class Microsoft_Windows_EFS_4404_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=4405, version=0)
class Microsoft_Windows_EFS_4405_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul,
        "Param1" / WString
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=4406, version=0)
class Microsoft_Windows_EFS_4406_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul,
        "Param1" / WString,
        "Param2" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=4407, version=0)
class Microsoft_Windows_EFS_4407_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul,
        "Param1" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=4408, version=0)
class Microsoft_Windows_EFS_4408_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul,
        "Param1" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=4409, version=0)
class Microsoft_Windows_EFS_4409_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul,
        "Param1" / WString
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=4410, version=0)
class Microsoft_Windows_EFS_4410_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul,
        "Param1" / WString
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=4411, version=0)
class Microsoft_Windows_EFS_4411_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul,
        "Param1" / WString,
        "Param2" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=4412, version=0)
class Microsoft_Windows_EFS_4412_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul,
        "Param1" / WString,
        "Param2" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=4413, version=0)
class Microsoft_Windows_EFS_4413_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul,
        "Param1" / WString,
        "Param2" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=4414, version=0)
class Microsoft_Windows_EFS_4414_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul,
        "Param1" / WString,
        "Param2" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=4415, version=0)
class Microsoft_Windows_EFS_4415_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul,
        "Param1" / WString,
        "Param2" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=4416, version=0)
class Microsoft_Windows_EFS_4416_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul,
        "Param1" / WString,
        "Param2" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=4417, version=0)
class Microsoft_Windows_EFS_4417_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul,
        "Param1" / WString,
        "Param2" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=4418, version=0)
class Microsoft_Windows_EFS_4418_0(Etw):
    pattern = Struct(
        "FileNumber" / Int32ul,
        "LineNumber" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=4419, version=0)
class Microsoft_Windows_EFS_4419_0(Etw):
    pattern = Struct(
        "ThreadId" / Int32ul,
        "File" / CString,
        "LineNumber" / Int32ul,
        "HRESULT" / Int32ul,
        "Message" / WString
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=7000, version=0)
class Microsoft_Windows_EFS_7000_0(Etw):
    pattern = Struct(
        "Reason" / WString
    )


@declare(guid=guid("3663a992-84be-40ea-bba9-90c7ed544222"), event_id=7002, version=0)
class Microsoft_Windows_EFS_7002_0(Etw):
    pattern = Struct(
        "Reason" / WString
    )

