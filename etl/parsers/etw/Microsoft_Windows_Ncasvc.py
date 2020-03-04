# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Ncasvc
GUID : 126ded58-a28d-4113-8e7a-59d7444b2af1
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("126ded58-a28d-4113-8e7a-59d7444b2af1"), event_id=1, version=0)
class Microsoft_Windows_Ncasvc_1_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("126ded58-a28d-4113-8e7a-59d7444b2af1"), event_id=2, version=0)
class Microsoft_Windows_Ncasvc_2_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "Substatus" / Int32ul
    )


@declare(guid=guid("126ded58-a28d-4113-8e7a-59d7444b2af1"), event_id=3, version=0)
class Microsoft_Windows_Ncasvc_3_0(Etw):
    pattern = Struct(
        "ApiFunction" / WString
    )


@declare(guid=guid("126ded58-a28d-4113-8e7a-59d7444b2af1"), event_id=4, version=0)
class Microsoft_Windows_Ncasvc_4_0(Etw):
    pattern = Struct(
        "ApiFunction" / WString,
        "Error" / Int64ul
    )


@declare(guid=guid("126ded58-a28d-4113-8e7a-59d7444b2af1"), event_id=5, version=0)
class Microsoft_Windows_Ncasvc_5_0(Etw):
    pattern = Struct(
        "EvColl" / Int32ul,
        "Old" / Int8ul,
        "New" / Int8ul,
        "UserId" / Int64ul
    )


@declare(guid=guid("126ded58-a28d-4113-8e7a-59d7444b2af1"), event_id=6, version=0)
class Microsoft_Windows_Ncasvc_6_0(Etw):
    pattern = Struct(
        "Type" / Int32ul,
        "Resource" / WString
    )


@declare(guid=guid("126ded58-a28d-4113-8e7a-59d7444b2af1"), event_id=7, version=0)
class Microsoft_Windows_Ncasvc_7_0(Etw):
    pattern = Struct(
        "Type" / Int32ul,
        "Resource" / WString,
        "Result" / Int32ul
    )


@declare(guid=guid("126ded58-a28d-4113-8e7a-59d7444b2af1"), event_id=8, version=0)
class Microsoft_Windows_Ncasvc_8_0(Etw):
    pattern = Struct(
        "Type" / Int32ul,
        "Code" / Int64ul,
        "Error" / Int64ul
    )


@declare(guid=guid("126ded58-a28d-4113-8e7a-59d7444b2af1"), event_id=9, version=0)
class Microsoft_Windows_Ncasvc_9_0(Etw):
    pattern = Struct(
        "Source" / WString
    )


@declare(guid=guid("126ded58-a28d-4113-8e7a-59d7444b2af1"), event_id=10, version=0)
class Microsoft_Windows_Ncasvc_10_0(Etw):
    pattern = Struct(
        "Source" / WString
    )


@declare(guid=guid("126ded58-a28d-4113-8e7a-59d7444b2af1"), event_id=11, version=0)
class Microsoft_Windows_Ncasvc_11_0(Etw):
    pattern = Struct(
        "ModuleName" / WString
    )


@declare(guid=guid("126ded58-a28d-4113-8e7a-59d7444b2af1"), event_id=12, version=0)
class Microsoft_Windows_Ncasvc_12_0(Etw):
    pattern = Struct(
        "ModuleName" / WString,
        "Error" / Int64ul
    )


@declare(guid=guid("126ded58-a28d-4113-8e7a-59d7444b2af1"), event_id=13, version=0)
class Microsoft_Windows_Ncasvc_13_0(Etw):
    pattern = Struct(
        "ModuleName" / WString
    )


@declare(guid=guid("126ded58-a28d-4113-8e7a-59d7444b2af1"), event_id=14, version=0)
class Microsoft_Windows_Ncasvc_14_0(Etw):
    pattern = Struct(
        "ModuleName" / WString
    )


@declare(guid=guid("126ded58-a28d-4113-8e7a-59d7444b2af1"), event_id=15, version=0)
class Microsoft_Windows_Ncasvc_15_0(Etw):
    pattern = Struct(
        "Source" / WString,
        "Info" / WString
    )


@declare(guid=guid("126ded58-a28d-4113-8e7a-59d7444b2af1"), event_id=10001, version=0)
class Microsoft_Windows_Ncasvc_10001_0(Etw):
    pattern = Struct(
        "MachineIdentifier" / Int32ul,
        "SessionIdentifier" / Int32ul,
        "DeploymentIdentifier" / Int32ul,
        "StopState" / Int32ul
    )


@declare(guid=guid("126ded58-a28d-4113-8e7a-59d7444b2af1"), event_id=10002, version=0)
class Microsoft_Windows_Ncasvc_10002_0(Etw):
    pattern = Struct(
        "MachineIdentifier" / Int32ul,
        "SessionIdentifier" / Int32ul,
        "DeploymentIdentifier" / Int32ul,
        "StopState" / Int32ul
    )


@declare(guid=guid("126ded58-a28d-4113-8e7a-59d7444b2af1"), event_id=10003, version=0)
class Microsoft_Windows_Ncasvc_10003_0(Etw):
    pattern = Struct(
        "MachineIdentifier" / Int32ul,
        "SessionIdentifier" / Int32ul,
        "DeploymentIdentifier" / Int32ul,
        "StopState" / Int32ul
    )


@declare(guid=guid("126ded58-a28d-4113-8e7a-59d7444b2af1"), event_id=10004, version=0)
class Microsoft_Windows_Ncasvc_10004_0(Etw):
    pattern = Struct(
        "MachineIdentifier" / Int32ul,
        "SessionIdentifier" / Int32ul,
        "DeploymentIdentifier" / Int32ul,
        "StopState" / Int32ul
    )


@declare(guid=guid("126ded58-a28d-4113-8e7a-59d7444b2af1"), event_id=10005, version=0)
class Microsoft_Windows_Ncasvc_10005_0(Etw):
    pattern = Struct(
        "MachineIdentifier" / Int32ul,
        "SessionIdentifier" / Int32ul,
        "DeploymentIdentifier" / Int32ul,
        "StopState" / Int32ul
    )


@declare(guid=guid("126ded58-a28d-4113-8e7a-59d7444b2af1"), event_id=10006, version=0)
class Microsoft_Windows_Ncasvc_10006_0(Etw):
    pattern = Struct(
        "MachineIdentifier" / Int32ul,
        "SessionIdentifier" / Int32ul,
        "DeploymentIdentifier" / Int32ul,
        "StopState" / Int32ul
    )


@declare(guid=guid("126ded58-a28d-4113-8e7a-59d7444b2af1"), event_id=10007, version=0)
class Microsoft_Windows_Ncasvc_10007_0(Etw):
    pattern = Struct(
        "MachineIdentifier" / Int32ul,
        "SessionIdentifier" / Int32ul,
        "DeploymentIdentifier" / Int32ul,
        "StopState" / Int32ul
    )


@declare(guid=guid("126ded58-a28d-4113-8e7a-59d7444b2af1"), event_id=10008, version=0)
class Microsoft_Windows_Ncasvc_10008_0(Etw):
    pattern = Struct(
        "MachineIdentifier" / Int32ul,
        "SessionIdentifier" / Int32ul,
        "DeploymentIdentifier" / Int32ul,
        "StopState" / Int32ul
    )


@declare(guid=guid("126ded58-a28d-4113-8e7a-59d7444b2af1"), event_id=10009, version=0)
class Microsoft_Windows_Ncasvc_10009_0(Etw):
    pattern = Struct(
        "MachineIdentifier" / Int32ul,
        "SessionIdentifier" / Int32ul,
        "DeploymentIdentifier" / Int32ul,
        "StopState" / Int32ul
    )


@declare(guid=guid("126ded58-a28d-4113-8e7a-59d7444b2af1"), event_id=10010, version=0)
class Microsoft_Windows_Ncasvc_10010_0(Etw):
    pattern = Struct(
        "MachineIdentifier" / Int32ul,
        "SessionIdentifier" / Int32ul,
        "DeploymentIdentifier" / Int32ul,
        "StopState" / Int32ul
    )


@declare(guid=guid("126ded58-a28d-4113-8e7a-59d7444b2af1"), event_id=10011, version=0)
class Microsoft_Windows_Ncasvc_10011_0(Etw):
    pattern = Struct(
        "MachineIdentifier" / Int32ul,
        "SessionIdentifier" / Int32ul,
        "DeploymentIdentifier" / Int32ul,
        "StopState" / Int32ul
    )


@declare(guid=guid("126ded58-a28d-4113-8e7a-59d7444b2af1"), event_id=10012, version=0)
class Microsoft_Windows_Ncasvc_10012_0(Etw):
    pattern = Struct(
        "MachineIdentifier" / Int32ul,
        "SessionIdentifier" / Int32ul,
        "DeploymentIdentifier" / Int32ul,
        "StopState" / Int32ul
    )


@declare(guid=guid("126ded58-a28d-4113-8e7a-59d7444b2af1"), event_id=10013, version=0)
class Microsoft_Windows_Ncasvc_10013_0(Etw):
    pattern = Struct(
        "MachineIdentifier" / Int32ul,
        "SessionIdentifier" / Int32ul,
        "DeploymentIdentifier" / Int32ul,
        "StopState" / Int32ul
    )


@declare(guid=guid("126ded58-a28d-4113-8e7a-59d7444b2af1"), event_id=10014, version=0)
class Microsoft_Windows_Ncasvc_10014_0(Etw):
    pattern = Struct(
        "MachineIdentifier" / Int32ul,
        "SessionIdentifier" / Int32ul,
        "DeploymentIdentifier" / Int32ul,
        "StopState" / Int32ul
    )

