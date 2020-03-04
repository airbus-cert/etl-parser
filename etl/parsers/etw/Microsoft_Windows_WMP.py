# -*- coding: utf-8 -*-
"""
Microsoft-Windows-WMP
GUID : f3f14ff3-7b80-4868-91d0-d77e497b025e
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=62, version=0)
class Microsoft_Windows_WMP_62_0(Etw):
    pattern = Struct(
        "CmdLine" / WString
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=63, version=0)
class Microsoft_Windows_WMP_63_0(Etw):
    pattern = Struct(
        "CmdLine" / WString
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=66, version=0)
class Microsoft_Windows_WMP_66_0(Etw):
    pattern = Struct(
        "SkinPath" / WString
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=67, version=0)
class Microsoft_Windows_WMP_67_0(Etw):
    pattern = Struct(
        "SkinPath" / WString
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=74, version=0)
class Microsoft_Windows_WMP_74_0(Etw):
    pattern = Struct(
        "ModeSwitcherOption" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=82, version=0)
class Microsoft_Windows_WMP_82_0(Etw):
    pattern = Struct(
        "EventType" / WString,
        "NewState" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=84, version=0)
class Microsoft_Windows_WMP_84_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=85, version=0)
class Microsoft_Windows_WMP_85_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=86, version=0)
class Microsoft_Windows_WMP_86_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=87, version=0)
class Microsoft_Windows_WMP_87_0(Etw):
    pattern = Struct(
        "Value1" / WString,
        "Value2" / WString
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=88, version=0)
class Microsoft_Windows_WMP_88_0(Etw):
    pattern = Struct(
        "Value1" / WString,
        "Value2" / WString
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=89, version=0)
class Microsoft_Windows_WMP_89_0(Etw):
    pattern = Struct(
        "Value1" / WString,
        "Value2" / WString
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=97, version=0)
class Microsoft_Windows_WMP_97_0(Etw):
    pattern = Struct(
        "DeviceName" / WString,
        "PnPID" / WString
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=99, version=0)
class Microsoft_Windows_WMP_99_0(Etw):
    pattern = Struct(
        "FilesFound" / Int32ul,
        "FilesAdded" / Int32ul,
        "FilesSkipped" / Int32ul,
        "DirectoriesFound" / Int32ul,
        "DirectoriesRemoved" / Int32ul,
        "Levels" / Int32ul,
        "ElapsedTime" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=100, version=0)
class Microsoft_Windows_WMP_100_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Value" / WString
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=101, version=0)
class Microsoft_Windows_WMP_101_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Value" / WString
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=102, version=0)
class Microsoft_Windows_WMP_102_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Value" / WString
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=103, version=0)
class Microsoft_Windows_WMP_103_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Value" / WString
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=104, version=0)
class Microsoft_Windows_WMP_104_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Value" / WString
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=105, version=0)
class Microsoft_Windows_WMP_105_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Value" / WString
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=106, version=0)
class Microsoft_Windows_WMP_106_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Value" / WString
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=107, version=0)
class Microsoft_Windows_WMP_107_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Value" / WString
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=108, version=0)
class Microsoft_Windows_WMP_108_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Value" / WString
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=110, version=0)
class Microsoft_Windows_WMP_110_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=149, version=0)
class Microsoft_Windows_WMP_149_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=150, version=0)
class Microsoft_Windows_WMP_150_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Value" / WString
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=151, version=0)
class Microsoft_Windows_WMP_151_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Value" / WString,
        "Index" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=152, version=0)
class Microsoft_Windows_WMP_152_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Value" / WString,
        "Index" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=153, version=0)
class Microsoft_Windows_WMP_153_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Value" / WString
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=154, version=0)
class Microsoft_Windows_WMP_154_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Value" / WString
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=155, version=0)
class Microsoft_Windows_WMP_155_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Value" / WString,
        "Index" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=156, version=0)
class Microsoft_Windows_WMP_156_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Value" / WString,
        "Index" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=157, version=0)
class Microsoft_Windows_WMP_157_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=158, version=0)
class Microsoft_Windows_WMP_158_0(Etw):
    pattern = Struct(
        "Value" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=200, version=0)
class Microsoft_Windows_WMP_200_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Value" / WString
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=201, version=0)
class Microsoft_Windows_WMP_201_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Value" / WString
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=202, version=0)
class Microsoft_Windows_WMP_202_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Value" / WString
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=205, version=0)
class Microsoft_Windows_WMP_205_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Value" / WString
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=206, version=0)
class Microsoft_Windows_WMP_206_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=207, version=0)
class Microsoft_Windows_WMP_207_0(Etw):
    pattern = Struct(
        "SourceFile" / WString
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=220, version=0)
class Microsoft_Windows_WMP_220_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Value" / WString
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=221, version=0)
class Microsoft_Windows_WMP_221_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Value" / WString
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=250, version=0)
class Microsoft_Windows_WMP_250_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Value" / WString
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=251, version=0)
class Microsoft_Windows_WMP_251_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Value" / WString
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=252, version=0)
class Microsoft_Windows_WMP_252_0(Etw):
    pattern = Struct(
        "Name" / WString,
        "Value" / WString
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=280, version=0)
class Microsoft_Windows_WMP_280_0(Etw):
    pattern = Struct(
        "ToolbarID" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=281, version=0)
class Microsoft_Windows_WMP_281_0(Etw):
    pattern = Struct(
        "ToolbarID" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=282, version=0)
class Microsoft_Windows_WMP_282_0(Etw):
    pattern = Struct(
        "ButtonID" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=283, version=0)
class Microsoft_Windows_WMP_283_0(Etw):
    pattern = Struct(
        "ButtonID" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=284, version=0)
class Microsoft_Windows_WMP_284_0(Etw):
    pattern = Struct(
        "Tooltip" / WString
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=300, version=0)
class Microsoft_Windows_WMP_300_0(Etw):
    pattern = Struct(
        "Category" / WString,
        "Skinformation" / WString
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=305, version=0)
class Microsoft_Windows_WMP_305_0(Etw):
    pattern = Struct(
        "Value1" / WString,
        "Value2" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=306, version=0)
class Microsoft_Windows_WMP_306_0(Etw):
    pattern = Struct(
        "Value1" / WString,
        "Value2" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=307, version=0)
class Microsoft_Windows_WMP_307_0(Etw):
    pattern = Struct(
        "Value1" / WString,
        "Value2" / WString
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=308, version=0)
class Microsoft_Windows_WMP_308_0(Etw):
    pattern = Struct(
        "Value1" / WString,
        "Value2" / WString
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=309, version=0)
class Microsoft_Windows_WMP_309_0(Etw):
    pattern = Struct(
        "Int1" / Int32ul,
        "Int2" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=310, version=0)
class Microsoft_Windows_WMP_310_0(Etw):
    pattern = Struct(
        "Int1" / Int32ul,
        "Int2" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=311, version=0)
class Microsoft_Windows_WMP_311_0(Etw):
    pattern = Struct(
        "Value1" / WString,
        "Value2" / WString
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=312, version=0)
class Microsoft_Windows_WMP_312_0(Etw):
    pattern = Struct(
        "Int1" / Int32ul,
        "Int2" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=313, version=0)
class Microsoft_Windows_WMP_313_0(Etw):
    pattern = Struct(
        "Value1" / WString,
        "Value2" / Int32ul,
        "Value3" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=314, version=0)
class Microsoft_Windows_WMP_314_0(Etw):
    pattern = Struct(
        "Value1" / WString,
        "Value2" / WString,
        "Value3" / WString
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=315, version=0)
class Microsoft_Windows_WMP_315_0(Etw):
    pattern = Struct(
        "Value1" / WString,
        "Value2" / WString,
        "Value3" / WString
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=316, version=0)
class Microsoft_Windows_WMP_316_0(Etw):
    pattern = Struct(
        "Value1" / WString,
        "Value2" / WString
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=317, version=0)
class Microsoft_Windows_WMP_317_0(Etw):
    pattern = Struct(
        "Value1" / WString,
        "Value2" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=325, version=0)
class Microsoft_Windows_WMP_325_0(Etw):
    pattern = Struct(
        "URL" / WString
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=326, version=0)
class Microsoft_Windows_WMP_326_0(Etw):
    pattern = Struct(
        "URL" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=327, version=0)
class Microsoft_Windows_WMP_327_0(Etw):
    pattern = Struct(
        "Bandwidth" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=328, version=0)
class Microsoft_Windows_WMP_328_0(Etw):
    pattern = Struct(
        "Bandwidth" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=350, version=0)
class Microsoft_Windows_WMP_350_0(Etw):
    pattern = Struct(
        "URL" / WString
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=351, version=0)
class Microsoft_Windows_WMP_351_0(Etw):
    pattern = Struct(
        "URL" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=352, version=0)
class Microsoft_Windows_WMP_352_0(Etw):
    pattern = Struct(
        "URL" / WString
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=353, version=0)
class Microsoft_Windows_WMP_353_0(Etw):
    pattern = Struct(
        "Offset" / Int32ul,
        "RequestedCount" / Int32ul,
        "ResponseCount" / Int32ul,
        "TotalCount" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=356, version=0)
class Microsoft_Windows_WMP_356_0(Etw):
    pattern = Struct(
        "ContainerID" / WString,
        "Query" / WString
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=357, version=0)
class Microsoft_Windows_WMP_357_0(Etw):
    pattern = Struct(
        "ContainerID" / WString,
        "Query" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=358, version=0)
class Microsoft_Windows_WMP_358_0(Etw):
    pattern = Struct(
        "ID" / WString
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=359, version=0)
class Microsoft_Windows_WMP_359_0(Etw):
    pattern = Struct(
        "ID" / WString
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=360, version=0)
class Microsoft_Windows_WMP_360_0(Etw):
    pattern = Struct(
        "DeviceID" / WString,
        "ObjectID" / WString
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=361, version=0)
class Microsoft_Windows_WMP_361_0(Etw):
    pattern = Struct(
        "DeviceID" / WString,
        "ObjectID" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=362, version=0)
class Microsoft_Windows_WMP_362_0(Etw):
    pattern = Struct(
        "ID" / WString,
        "Item" / Int32ul,
        "Atom" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=363, version=0)
class Microsoft_Windows_WMP_363_0(Etw):
    pattern = Struct(
        "ID" / WString,
        "Item" / Int32ul,
        "Atom" / Int32ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=364, version=0)
class Microsoft_Windows_WMP_364_0(Etw):
    pattern = Struct(
        "ServerUDN" / WString,
        "Offline" / Int8ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=365, version=0)
class Microsoft_Windows_WMP_365_0(Etw):
    pattern = Struct(
        "ID" / WString
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=366, version=0)
class Microsoft_Windows_WMP_366_0(Etw):
    pattern = Struct(
        "ID" / WString
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=367, version=0)
class Microsoft_Windows_WMP_367_0(Etw):
    pattern = Struct(
        "ID" / WString
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=368, version=0)
class Microsoft_Windows_WMP_368_0(Etw):
    pattern = Struct(
        "ID" / WString
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=369, version=0)
class Microsoft_Windows_WMP_369_0(Etw):
    pattern = Struct(
        "DeviceID" / WString,
        "ObjectID" / WString
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=370, version=0)
class Microsoft_Windows_WMP_370_0(Etw):
    pattern = Struct(
        "IWMMediaLibrary" / Int64ul,
        "EnableSharing" / Int8ul,
        "UpdateACLs" / Int8ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=371, version=0)
class Microsoft_Windows_WMP_371_0(Etw):
    pattern = Struct(
        "IWMMediaLibrary" / Int64ul,
        "EnableSharing" / Int8ul,
        "UpdateACLs" / Int8ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=372, version=0)
class Microsoft_Windows_WMP_372_0(Etw):
    pattern = Struct(
        "IgnoreUPnPDiscovery" / Int8ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=373, version=0)
class Microsoft_Windows_WMP_373_0(Etw):
    pattern = Struct(
        "IgnoreUPnPDiscovery" / Int8ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=374, version=0)
class Microsoft_Windows_WMP_374_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=375, version=0)
class Microsoft_Windows_WMP_375_0(Etw):
    pattern = Struct(
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=376, version=0)
class Microsoft_Windows_WMP_376_0(Etw):
    pattern = Struct(
        "IUPnPDevice" / Int64ul,
        "UDN" / WString,
        "FriendlyName" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=377, version=0)
class Microsoft_Windows_WMP_377_0(Etw):
    pattern = Struct(
        "IUPnPDevice" / Int64ul,
        "UDN" / WString,
        "FriendlyName" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=378, version=0)
class Microsoft_Windows_WMP_378_0(Etw):
    pattern = Struct(
        "IUPnPDevice" / Int64ul,
        "UDN" / WString,
        "FriendlyName" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=379, version=0)
class Microsoft_Windows_WMP_379_0(Etw):
    pattern = Struct(
        "IUPnPDevice" / Int64ul,
        "UDN" / WString,
        "FriendlyName" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=380, version=0)
class Microsoft_Windows_WMP_380_0(Etw):
    pattern = Struct(
        "UDN" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=381, version=0)
class Microsoft_Windows_WMP_381_0(Etw):
    pattern = Struct(
        "UDN" / WString,
        "IHMEService" / Int64ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=382, version=0)
class Microsoft_Windows_WMP_382_0(Etw):
    pattern = Struct(
        "UDN" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=383, version=0)
class Microsoft_Windows_WMP_383_0(Etw):
    pattern = Struct(
        "UDN" / WString,
        "IUPnPDevice" / Int64ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=384, version=0)
class Microsoft_Windows_WMP_384_0(Etw):
    pattern = Struct(
        "UDN" / WString,
        "IUPnPDevice" / Int64ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=385, version=0)
class Microsoft_Windows_WMP_385_0(Etw):
    pattern = Struct(
        "UDN" / WString,
        "IUPnPDevice" / Int64ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=386, version=0)
class Microsoft_Windows_WMP_386_0(Etw):
    pattern = Struct(
        "UDN" / WString,
        "IUPnPDevice" / Int64ul,
        "IHMEService" / Int64ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=388, version=0)
class Microsoft_Windows_WMP_388_0(Etw):
    pattern = Struct(
        "RMEDeviceFinder" / Int64ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=389, version=0)
class Microsoft_Windows_WMP_389_0(Etw):
    pattern = Struct(
        "IHMEService" / Int64ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=390, version=0)
class Microsoft_Windows_WMP_390_0(Etw):
    pattern = Struct(
        "IHMEService" / Int64ul,
        "UDN" / WString
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=391, version=0)
class Microsoft_Windows_WMP_391_0(Etw):
    pattern = Struct(
        "IHMEService" / Int64ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=392, version=0)
class Microsoft_Windows_WMP_392_0(Etw):
    pattern = Struct(
        "IUPnPDevice" / Int64ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=393, version=0)
class Microsoft_Windows_WMP_393_0(Etw):
    pattern = Struct(
        "IUPnPDevice" / Int64ul,
        "UDN" / WString,
        "FriendlyName" / WString,
        "CDSVersion" / Int32ul,
        "IsSearchable" / Int8ul,
        "SupportsRME" / Int8ul,
        "SupportsWakeOnLAN" / Int8ul,
        "IHMEProvider" / Int64ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=394, version=0)
class Microsoft_Windows_WMP_394_0(Etw):
    pattern = Struct(
        "CHMEProvider" / Int64ul,
        "IHMECDS" / Int64ul,
        "UDN" / WString,
        "RAMCacheId" / Int32ul,
        "IsAuthorized" / Int8ul,
        "FireEvent" / Int8ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=395, version=0)
class Microsoft_Windows_WMP_395_0(Etw):
    pattern = Struct(
        "CHMEProvider" / Int64ul,
        "IHMECDS" / Int64ul,
        "UDN" / WString,
        "RAMCacheId" / Int32ul,
        "IsAuthorized" / Int8ul,
        "FireEvent" / Int8ul,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=396, version=0)
class Microsoft_Windows_WMP_396_0(Etw):
    pattern = Struct(
        "CHMEProvider" / Int64ul,
        "IHMECDS" / Int64ul,
        "UDN" / WString,
        "RAMCacheId" / Int32ul,
        "IsAuthorized" / Int8ul,
        "IsZombie" / Int8ul,
        "FireEvent" / Int8ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=397, version=0)
class Microsoft_Windows_WMP_397_0(Etw):
    pattern = Struct(
        "CHMEProvider" / Int64ul,
        "IHMECDS" / Int64ul,
        "UDN" / WString,
        "RAMCacheId" / Int32ul,
        "IsAuthorized" / Int8ul,
        "IsZombie" / Int8ul,
        "FireEvent" / Int8ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=398, version=0)
class Microsoft_Windows_WMP_398_0(Etw):
    pattern = Struct(
        "RAMCacheId" / Int32ul,
        "IsAdding" / Int8ul,
        "FireEvent" / Int8ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=400, version=0)
class Microsoft_Windows_WMP_400_0(Etw):
    pattern = Struct(
        "SourcePath" / WString,
        "TargetPath" / WString
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=401, version=0)
class Microsoft_Windows_WMP_401_0(Etw):
    pattern = Struct(
        "SourcePath" / WString,
        "TargetPath" / WString
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=403, version=0)
class Microsoft_Windows_WMP_403_0(Etw):
    pattern = Struct(
        "SourcePath" / WString,
        "TargetPath" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=406, version=0)
class Microsoft_Windows_WMP_406_0(Etw):
    pattern = Struct(
        "SourceFile" / WString,
        "IsDRM" / Int8ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=407, version=0)
class Microsoft_Windows_WMP_407_0(Etw):
    pattern = Struct(
        "SourceFile" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=408, version=0)
class Microsoft_Windows_WMP_408_0(Etw):
    pattern = Struct(
        "SourceFile" / WString
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=409, version=0)
class Microsoft_Windows_WMP_409_0(Etw):
    pattern = Struct(
        "SourceFile" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=410, version=0)
class Microsoft_Windows_WMP_410_0(Etw):
    pattern = Struct(
        "SourceFile" / WString
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=411, version=0)
class Microsoft_Windows_WMP_411_0(Etw):
    pattern = Struct(
        "SourceFile" / WString,
        "HRESULT" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=413, version=0)
class Microsoft_Windows_WMP_413_0(Etw):
    pattern = Struct(
        "numberofDMRsFound" / Int32ul,
        "result" / Int32ul,
        "failureReason" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=415, version=0)
class Microsoft_Windows_WMP_415_0(Etw):
    pattern = Struct(
        "UDN" / WString,
        "result" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=416, version=0)
class Microsoft_Windows_WMP_416_0(Etw):
    pattern = Struct(
        "UDN" / WString,
        "result" / Int32ul,
        "failureReason" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=418, version=0)
class Microsoft_Windows_WMP_418_0(Etw):
    pattern = Struct(
        "result" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=419, version=0)
class Microsoft_Windows_WMP_419_0(Etw):
    pattern = Struct(
        "URI" / WString,
        "URIMetadata" / WString
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=420, version=0)
class Microsoft_Windows_WMP_420_0(Etw):
    pattern = Struct(
        "result" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=426, version=0)
class Microsoft_Windows_WMP_426_0(Etw):
    pattern = Struct(
        "result" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=428, version=0)
class Microsoft_Windows_WMP_428_0(Etw):
    pattern = Struct(
        "result" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=430, version=0)
class Microsoft_Windows_WMP_430_0(Etw):
    pattern = Struct(
        "result" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=432, version=0)
class Microsoft_Windows_WMP_432_0(Etw):
    pattern = Struct(
        "result" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=434, version=0)
class Microsoft_Windows_WMP_434_0(Etw):
    pattern = Struct(
        "result" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=435, version=0)
class Microsoft_Windows_WMP_435_0(Etw):
    pattern = Struct(
        "IsChecked" / Int8ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=436, version=0)
class Microsoft_Windows_WMP_436_0(Etw):
    pattern = Struct(
        "IsChecked" / Int8ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=437, version=0)
class Microsoft_Windows_WMP_437_0(Etw):
    pattern = Struct(
        "IsChecked" / Int8ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=439, version=0)
class Microsoft_Windows_WMP_439_0(Etw):
    pattern = Struct(
        "result" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=441, version=0)
class Microsoft_Windows_WMP_441_0(Etw):
    pattern = Struct(
        "result" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=450, version=0)
class Microsoft_Windows_WMP_450_0(Etw):
    pattern = Struct(
        "ProtocolHandler" / Int64ul,
        "URL" / WString,
        "IInternetProtocolSink" / Int64ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=451, version=0)
class Microsoft_Windows_WMP_451_0(Etw):
    pattern = Struct(
        "ProtocolHandler" / Int64ul,
        "IInternetProtocolSink" / Int64ul,
        "UDN" / WString,
        "ServiceID" / WString,
        "ObjectID" / WString,
        "IHMECDS" / Int64ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=452, version=0)
class Microsoft_Windows_WMP_452_0(Etw):
    pattern = Struct(
        "ProtocolHandler" / Int64ul,
        "IInternetProtocolSink" / Int64ul,
        "UDN" / WString,
        "ServiceID" / WString,
        "ObjectID" / WString,
        "HResult" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=453, version=0)
class Microsoft_Windows_WMP_453_0(Etw):
    pattern = Struct(
        "ProtocolHandler" / Int64ul,
        "UDN" / WString,
        "ObjectID" / WString,
        "IHMECDS" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=454, version=0)
class Microsoft_Windows_WMP_454_0(Etw):
    pattern = Struct(
        "ProtocolHandler" / Int64ul,
        "UDN" / WString,
        "ObjectID" / WString,
        "ASX" / CString,
        "HResult" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=455, version=0)
class Microsoft_Windows_WMP_455_0(Etw):
    pattern = Struct(
        "ProtocolHandler" / Int64ul,
        "UDN" / WString,
        "ObjectID" / WString,
        "IHMECDS" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=456, version=0)
class Microsoft_Windows_WMP_456_0(Etw):
    pattern = Struct(
        "PlaylistMgr" / Int64ul,
        "URL" / WString
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=457, version=0)
class Microsoft_Windows_WMP_457_0(Etw):
    pattern = Struct(
        "PlaylistMgr" / Int64ul,
        "URL" / WString,
        "IWMPPlaylist" / Int64ul,
        "HResult" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=461, version=0)
class Microsoft_Windows_WMP_461_0(Etw):
    pattern = Struct(
        "result" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=462, version=0)
class Microsoft_Windows_WMP_462_0(Etw):
    pattern = Struct(
        "instanceID" / Int64ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=463, version=0)
class Microsoft_Windows_WMP_463_0(Etw):
    pattern = Struct(
        "result" / Int32ul,
        "instanceID" / Int64ul,
        "Track" / Int64sl,
        "TrackDuration" / WString,
        "MetaData" / WString,
        "TrackURI" / WString
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=465, version=0)
class Microsoft_Windows_WMP_465_0(Etw):
    pattern = Struct(
        "result" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=467, version=0)
class Microsoft_Windows_WMP_467_0(Etw):
    pattern = Struct(
        "result" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=469, version=0)
class Microsoft_Windows_WMP_469_0(Etw):
    pattern = Struct(
        "result" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=471, version=0)
class Microsoft_Windows_WMP_471_0(Etw):
    pattern = Struct(
        "result" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=473, version=0)
class Microsoft_Windows_WMP_473_0(Etw):
    pattern = Struct(
        "result" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=475, version=0)
class Microsoft_Windows_WMP_475_0(Etw):
    pattern = Struct(
        "result" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=477, version=0)
class Microsoft_Windows_WMP_477_0(Etw):
    pattern = Struct(
        "result" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=479, version=0)
class Microsoft_Windows_WMP_479_0(Etw):
    pattern = Struct(
        "result" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=481, version=0)
class Microsoft_Windows_WMP_481_0(Etw):
    pattern = Struct(
        "result" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=483, version=0)
class Microsoft_Windows_WMP_483_0(Etw):
    pattern = Struct(
        "result" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=490, version=0)
class Microsoft_Windows_WMP_490_0(Etw):
    pattern = Struct(
        "Key" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=491, version=0)
class Microsoft_Windows_WMP_491_0(Etw):
    pattern = Struct(
        "Key" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=492, version=0)
class Microsoft_Windows_WMP_492_0(Etw):
    pattern = Struct(
        "Key" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=493, version=0)
class Microsoft_Windows_WMP_493_0(Etw):
    pattern = Struct(
        "Key" / Int32ul
    )


@declare(guid=guid("f3f14ff3-7b80-4868-91d0-d77e497b025e"), event_id=1615, version=0)
class Microsoft_Windows_WMP_1615_0(Etw):
    pattern = Struct(
        "DeviceName" / WString,
        "PnPID" / WString
    )

