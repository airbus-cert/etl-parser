# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Performance-Recorder-Control
GUID : 36b6f488-aad7-48c2-afe3-d4ec2c8b46fa
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("36b6f488-aad7-48c2-afe3-d4ec2c8b46fa"), event_id=102, version=0)
class Microsoft_Windows_Performance_Recorder_Control_102_0(Etw):
    pattern = Struct(
        "ProfileName" / WString,
        "FileName" / WString
    )


@declare(guid=guid("36b6f488-aad7-48c2-afe3-d4ec2c8b46fa"), event_id=114, version=0)
class Microsoft_Windows_Performance_Recorder_Control_114_0(Etw):
    pattern = Struct(
        "TraceMergePropertyName" / WString,
        "FileName" / WString
    )


@declare(guid=guid("36b6f488-aad7-48c2-afe3-d4ec2c8b46fa"), event_id=126, version=0)
class Microsoft_Windows_Performance_Recorder_Control_126_0(Etw):
    pattern = Struct(
        "FileName" / WString
    )


@declare(guid=guid("36b6f488-aad7-48c2-afe3-d4ec2c8b46fa"), event_id=128, version=0)
class Microsoft_Windows_Performance_Recorder_Control_128_0(Etw):
    pattern = Struct(
        "FileName" / WString
    )


@declare(guid=guid("36b6f488-aad7-48c2-afe3-d4ec2c8b46fa"), event_id=148, version=0)
class Microsoft_Windows_Performance_Recorder_Control_148_0(Etw):
    pattern = Struct(
        "FileName" / WString
    )


@declare(guid=guid("36b6f488-aad7-48c2-afe3-d4ec2c8b46fa"), event_id=150, version=0)
class Microsoft_Windows_Performance_Recorder_Control_150_0(Etw):
    pattern = Struct(
        "Provider" / WString,
        "Error" / WString
    )


@declare(guid=guid("36b6f488-aad7-48c2-afe3-d4ec2c8b46fa"), event_id=151, version=0)
class Microsoft_Windows_Performance_Recorder_Control_151_0(Etw):
    pattern = Struct(
        "ProfileIds" / WString
    )


@declare(guid=guid("36b6f488-aad7-48c2-afe3-d4ec2c8b46fa"), event_id=200, version=0)
class Microsoft_Windows_Performance_Recorder_Control_200_0(Etw):
    pattern = Struct(
        "DebugType" / Int32ul,
        "ObjectType" / Int32ul,
        "HResult" / Int32sl,
        "LineNumber" / Int32ul,
        "FileName" / WString,
        "FunctionName" / WString
    )

