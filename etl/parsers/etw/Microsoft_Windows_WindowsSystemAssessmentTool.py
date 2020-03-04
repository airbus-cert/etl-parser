# -*- coding: utf-8 -*-
"""
Microsoft-Windows-WindowsSystemAssessmentTool
GUID : 11a75546-3234-465e-bec8-2d301cb501ac
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("11a75546-3234-465e-bec8-2d301cb501ac"), event_id=0, version=0)
class Microsoft_Windows_WindowsSystemAssessmentTool_0_0(Etw):
    pattern = Struct(
        "TestV1" / Int32ul,
        "TestV2" / Int32ul,
        "TestV3" / Int32ul,
        "TestV4" / WString
    )


@declare(guid=guid("11a75546-3234-465e-bec8-2d301cb501ac"), event_id=1, version=0)
class Microsoft_Windows_WindowsSystemAssessmentTool_1_0(Etw):
    pattern = Struct(
        "StartTimeOfDay" / Int64ul
    )


@declare(guid=guid("11a75546-3234-465e-bec8-2d301cb501ac"), event_id=2, version=0)
class Microsoft_Windows_WindowsSystemAssessmentTool_2_0(Etw):
    pattern = Struct(
        "CommandLineSize" / Int16ul,
        "CommandLine" / Bytes(lambda this: this.CommandLineSize)
    )


@declare(guid=guid("11a75546-3234-465e-bec8-2d301cb501ac"), event_id=3, version=0)
class Microsoft_Windows_WindowsSystemAssessmentTool_3_0(Etw):
    pattern = Struct(
        "ExitCode" / Int32ul
    )


@declare(guid=guid("11a75546-3234-465e-bec8-2d301cb501ac"), event_id=4, version=0)
class Microsoft_Windows_WindowsSystemAssessmentTool_4_0(Etw):
    pattern = Struct(
        "Win32Error" / Int32ul,
        "CantMsgSize" / Int16ul,
        "CantMsg" / Bytes(lambda this: this.CantMsgSize)
    )


@declare(guid=guid("11a75546-3234-465e-bec8-2d301cb501ac"), event_id=5, version=0)
class Microsoft_Windows_WindowsSystemAssessmentTool_5_0(Etw):
    pattern = Struct(
        "FailingHresult" / Int32ul,
        "FailingInterfaceCLSID" / Guid,
        "SourceSize" / Int16ul,
        "Source" / Bytes(lambda this: this.SourceSize),
        "InfterfaceSize" / Int16ul,
        "Interface" / Bytes(lambda this: this.InfterfaceSize),
        "ErrorMsgSize" / Int16ul,
        "ErrorMsg" / Bytes(lambda this: this.ErrorMsgSize),
        "CantMsgSize" / Int16ul,
        "CantMsg" / Bytes(lambda this: this.CantMsgSize)
    )


@declare(guid=guid("11a75546-3234-465e-bec8-2d301cb501ac"), event_id=6, version=0)
class Microsoft_Windows_WindowsSystemAssessmentTool_6_0(Etw):
    pattern = Struct(
        "ErrorMsgSize" / Int16ul,
        "ErrorMsg" / Bytes(lambda this: this.ErrorMsgSize)
    )


@declare(guid=guid("11a75546-3234-465e-bec8-2d301cb501ac"), event_id=7, version=0)
class Microsoft_Windows_WindowsSystemAssessmentTool_7_0(Etw):
    pattern = Struct(
        "FailingHresult" / Int32ul,
        "ErrorMsgSize" / Int16ul,
        "ErrorMsg" / Bytes(lambda this: this.ErrorMsgSize),
        "CantMsgSize" / Int16ul,
        "CantMsg" / Bytes(lambda this: this.CantMsgSize)
    )


@declare(guid=guid("11a75546-3234-465e-bec8-2d301cb501ac"), event_id=8, version=0)
class Microsoft_Windows_WindowsSystemAssessmentTool_8_0(Etw):
    pattern = Struct(
        "MessageSize" / Int16ul,
        "Message" / Bytes(lambda this: this.MessageSize)
    )


@declare(guid=guid("11a75546-3234-465e-bec8-2d301cb501ac"), event_id=9, version=0)
class Microsoft_Windows_WindowsSystemAssessmentTool_9_0(Etw):
    pattern = Struct(
        "PhaseID" / Int16ul,
        "DescriptionSize" / Int16ul,
        "Description" / Bytes(lambda this: this.DescriptionSize)
    )


@declare(guid=guid("11a75546-3234-465e-bec8-2d301cb501ac"), event_id=10, version=0)
class Microsoft_Windows_WindowsSystemAssessmentTool_10_0(Etw):
    pattern = Struct(
        "PhaseID" / Int16ul
    )

