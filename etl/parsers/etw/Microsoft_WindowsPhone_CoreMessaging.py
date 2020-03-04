# -*- coding: utf-8 -*-
"""
Microsoft-WindowsPhone-CoreMessaging
GUID : 922cdcf3-6123-42da-a877-1a24f23e39c5
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("922cdcf3-6123-42da-a877-1a24f23e39c5"), event_id=1000, version=0)
class Microsoft_WindowsPhone_CoreMessaging_1000_0(Etw):
    pattern = Struct(
        "hex" / Int32ul
    )


@declare(guid=guid("922cdcf3-6123-42da-a877-1a24f23e39c5"), event_id=1001, version=0)
class Microsoft_WindowsPhone_CoreMessaging_1001_0(Etw):
    pattern = Struct(
        "hex" / Int32ul
    )


@declare(guid=guid("922cdcf3-6123-42da-a877-1a24f23e39c5"), event_id=2908, version=0)
class Microsoft_WindowsPhone_CoreMessaging_2908_0(Etw):
    pattern = Struct(
        "pwsz" / WString
    )


@declare(guid=guid("922cdcf3-6123-42da-a877-1a24f23e39c5"), event_id=3214, version=0)
class Microsoft_WindowsPhone_CoreMessaging_3214_0(Etw):
    pattern = Struct(
        "InternalPriority" / Int32ul
    )


@declare(guid=guid("922cdcf3-6123-42da-a877-1a24f23e39c5"), event_id=3215, version=0)
class Microsoft_WindowsPhone_CoreMessaging_3215_0(Etw):
    pattern = Struct(
        "InternalPriority" / Int32ul
    )


@declare(guid=guid("922cdcf3-6123-42da-a877-1a24f23e39c5"), event_id=3216, version=0)
class Microsoft_WindowsPhone_CoreMessaging_3216_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "InternalPriority" / Int32ul,
        "InternalPriority2" / Int32ul
    )


@declare(guid=guid("922cdcf3-6123-42da-a877-1a24f23e39c5"), event_id=3220, version=0)
class Microsoft_WindowsPhone_CoreMessaging_3220_0(Etw):
    pattern = Struct(
        "hex" / Int32ul
    )


@declare(guid=guid("922cdcf3-6123-42da-a877-1a24f23e39c5"), event_id=3221, version=0)
class Microsoft_WindowsPhone_CoreMessaging_3221_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("922cdcf3-6123-42da-a877-1a24f23e39c5"), event_id=3222, version=0)
class Microsoft_WindowsPhone_CoreMessaging_3222_0(Etw):
    pattern = Struct(
        "fBool" / Int8ul,
        "unParam" / Int64ul
    )


@declare(guid=guid("922cdcf3-6123-42da-a877-1a24f23e39c5"), event_id=3223, version=0)
class Microsoft_WindowsPhone_CoreMessaging_3223_0(Etw):
    pattern = Struct(
        "unParam" / Int64ul
    )


@declare(guid=guid("922cdcf3-6123-42da-a877-1a24f23e39c5"), event_id=3224, version=0)
class Microsoft_WindowsPhone_CoreMessaging_3224_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "UserPriority" / Int32ul
    )


@declare(guid=guid("922cdcf3-6123-42da-a877-1a24f23e39c5"), event_id=3225, version=0)
class Microsoft_WindowsPhone_CoreMessaging_3225_0(Etw):
    pattern = Struct(
        "RunMode" / Int32ul,
        "fBool" / Int8ul
    )


@declare(guid=guid("922cdcf3-6123-42da-a877-1a24f23e39c5"), event_id=3226, version=0)
class Microsoft_WindowsPhone_CoreMessaging_3226_0(Etw):
    pattern = Struct(
        "param" / Int32sl
    )


@declare(guid=guid("922cdcf3-6123-42da-a877-1a24f23e39c5"), event_id=3227, version=0)
class Microsoft_WindowsPhone_CoreMessaging_3227_0(Etw):
    pattern = Struct(
        "UserPriority" / Int32ul
    )


@declare(guid=guid("922cdcf3-6123-42da-a877-1a24f23e39c5"), event_id=3228, version=0)
class Microsoft_WindowsPhone_CoreMessaging_3228_0(Etw):
    pattern = Struct(
        "fBool" / Int8ul
    )


@declare(guid=guid("922cdcf3-6123-42da-a877-1a24f23e39c5"), event_id=3418, version=0)
class Microsoft_WindowsPhone_CoreMessaging_3418_0(Etw):
    pattern = Struct(
        "pwsz" / WString
    )


@declare(guid=guid("922cdcf3-6123-42da-a877-1a24f23e39c5"), event_id=3420, version=0)
class Microsoft_WindowsPhone_CoreMessaging_3420_0(Etw):
    pattern = Struct(
        "pwsz" / WString
    )


@declare(guid=guid("922cdcf3-6123-42da-a877-1a24f23e39c5"), event_id=3424, version=0)
class Microsoft_WindowsPhone_CoreMessaging_3424_0(Etw):
    pattern = Struct(
        "pwsz" / WString
    )


@declare(guid=guid("922cdcf3-6123-42da-a877-1a24f23e39c5"), event_id=3434, version=0)
class Microsoft_WindowsPhone_CoreMessaging_3434_0(Etw):
    pattern = Struct(
        "pwsz" / WString
    )


@declare(guid=guid("922cdcf3-6123-42da-a877-1a24f23e39c5"), event_id=3436, version=0)
class Microsoft_WindowsPhone_CoreMessaging_3436_0(Etw):
    pattern = Struct(
        "pwsz" / WString
    )


@declare(guid=guid("922cdcf3-6123-42da-a877-1a24f23e39c5"), event_id=3438, version=0)
class Microsoft_WindowsPhone_CoreMessaging_3438_0(Etw):
    pattern = Struct(
        "pwsz" / WString,
        "unParam" / Int32ul
    )


@declare(guid=guid("922cdcf3-6123-42da-a877-1a24f23e39c5"), event_id=3440, version=0)
class Microsoft_WindowsPhone_CoreMessaging_3440_0(Etw):
    pattern = Struct(
        "pwsz" / WString
    )


@declare(guid=guid("922cdcf3-6123-42da-a877-1a24f23e39c5"), event_id=3442, version=0)
class Microsoft_WindowsPhone_CoreMessaging_3442_0(Etw):
    pattern = Struct(
        "pwsz" / WString,
        "unParam" / Int32ul,
        "unParam2" / Int64ul
    )


@declare(guid=guid("922cdcf3-6123-42da-a877-1a24f23e39c5"), event_id=3444, version=0)
class Microsoft_WindowsPhone_CoreMessaging_3444_0(Etw):
    pattern = Struct(
        "pwsz" / WString,
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("922cdcf3-6123-42da-a877-1a24f23e39c5"), event_id=3446, version=0)
class Microsoft_WindowsPhone_CoreMessaging_3446_0(Etw):
    pattern = Struct(
        "pwsz" / WString,
        "unParam" / Int32ul,
        "unParam2" / Int32ul,
        "unParam3" / Int32ul
    )


@declare(guid=guid("922cdcf3-6123-42da-a877-1a24f23e39c5"), event_id=3450, version=0)
class Microsoft_WindowsPhone_CoreMessaging_3450_0(Etw):
    pattern = Struct(
        "pwsz" / WString,
        "unParam" / Int32ul,
        "unParam2" / Int64ul
    )


@declare(guid=guid("922cdcf3-6123-42da-a877-1a24f23e39c5"), event_id=3454, version=0)
class Microsoft_WindowsPhone_CoreMessaging_3454_0(Etw):
    pattern = Struct(
        "pwsz" / WString,
        "unParam" / Int32ul
    )


@declare(guid=guid("922cdcf3-6123-42da-a877-1a24f23e39c5"), event_id=3456, version=0)
class Microsoft_WindowsPhone_CoreMessaging_3456_0(Etw):
    pattern = Struct(
        "pwsz" / WString,
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("922cdcf3-6123-42da-a877-1a24f23e39c5"), event_id=4010, version=0)
class Microsoft_WindowsPhone_CoreMessaging_4010_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("922cdcf3-6123-42da-a877-1a24f23e39c5"), event_id=4011, version=0)
class Microsoft_WindowsPhone_CoreMessaging_4011_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("922cdcf3-6123-42da-a877-1a24f23e39c5"), event_id=4020, version=0)
class Microsoft_WindowsPhone_CoreMessaging_4020_0(Etw):
    pattern = Struct(
        "ExternalPriority" / Int32ul,
        "unParam" / Int32ul,
        "hex" / Int32ul,
        "hex2" / Int32ul
    )


@declare(guid=guid("922cdcf3-6123-42da-a877-1a24f23e39c5"), event_id=4021, version=0)
class Microsoft_WindowsPhone_CoreMessaging_4021_0(Etw):
    pattern = Struct(
        "hex" / Int32ul,
        "hex2" / Int32ul
    )


@declare(guid=guid("922cdcf3-6123-42da-a877-1a24f23e39c5"), event_id=4022, version=0)
class Microsoft_WindowsPhone_CoreMessaging_4022_0(Etw):
    pattern = Struct(
        "ExternalPriority" / Int32ul
    )


@declare(guid=guid("922cdcf3-6123-42da-a877-1a24f23e39c5"), event_id=4031, version=0)
class Microsoft_WindowsPhone_CoreMessaging_4031_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("922cdcf3-6123-42da-a877-1a24f23e39c5"), event_id=4041, version=0)
class Microsoft_WindowsPhone_CoreMessaging_4041_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("922cdcf3-6123-42da-a877-1a24f23e39c5"), event_id=4042, version=0)
class Microsoft_WindowsPhone_CoreMessaging_4042_0(Etw):
    pattern = Struct(
        "ExternalPriority" / Int32ul,
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("922cdcf3-6123-42da-a877-1a24f23e39c5"), event_id=4043, version=0)
class Microsoft_WindowsPhone_CoreMessaging_4043_0(Etw):
    pattern = Struct(
        "ExternalPriority" / Int32ul,
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("922cdcf3-6123-42da-a877-1a24f23e39c5"), event_id=4045, version=0)
class Microsoft_WindowsPhone_CoreMessaging_4045_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul,
        "unParam3" / Int32ul
    )


@declare(guid=guid("922cdcf3-6123-42da-a877-1a24f23e39c5"), event_id=4051, version=0)
class Microsoft_WindowsPhone_CoreMessaging_4051_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("922cdcf3-6123-42da-a877-1a24f23e39c5"), event_id=4052, version=0)
class Microsoft_WindowsPhone_CoreMessaging_4052_0(Etw):
    pattern = Struct(
        "ExternalPriority" / Int32ul,
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("922cdcf3-6123-42da-a877-1a24f23e39c5"), event_id=4053, version=0)
class Microsoft_WindowsPhone_CoreMessaging_4053_0(Etw):
    pattern = Struct(
        "ExternalPriority" / Int32ul,
        "unParam" / Int32ul,
        "unParam2" / Int32ul
    )


@declare(guid=guid("922cdcf3-6123-42da-a877-1a24f23e39c5"), event_id=4055, version=0)
class Microsoft_WindowsPhone_CoreMessaging_4055_0(Etw):
    pattern = Struct(
        "unParam" / Int32ul,
        "unParam2" / Int32ul,
        "unParam3" / Int32ul,
        "unParam4" / Int32ul
    )


@declare(guid=guid("922cdcf3-6123-42da-a877-1a24f23e39c5"), event_id=5050, version=0)
class Microsoft_WindowsPhone_CoreMessaging_5050_0(Etw):
    pattern = Struct(
        "pwsz" / WString
    )


@declare(guid=guid("922cdcf3-6123-42da-a877-1a24f23e39c5"), event_id=7000, version=0)
class Microsoft_WindowsPhone_CoreMessaging_7000_0(Etw):
    pattern = Struct(
        "pwsz" / WString,
        "RegisteredObjectType" / Int32ul,
        "RegistrarScope" / Int32ul,
        "hex" / Int32ul,
        "hex2" / Int32ul,
        "hex3" / Int32ul
    )


@declare(guid=guid("922cdcf3-6123-42da-a877-1a24f23e39c5"), event_id=7001, version=0)
class Microsoft_WindowsPhone_CoreMessaging_7001_0(Etw):
    pattern = Struct(
        "pwsz" / WString,
        "RegisteredObjectType" / Int32ul,
        "RegistrarScope" / Int32ul,
        "hex" / Int32ul,
        "hex2" / Int32ul,
        "hex3" / Int32ul,
        "fBool" / Int8ul
    )


@declare(guid=guid("922cdcf3-6123-42da-a877-1a24f23e39c5"), event_id=7002, version=0)
class Microsoft_WindowsPhone_CoreMessaging_7002_0(Etw):
    pattern = Struct(
        "hex" / Int32ul,
        "hex2" / Int32ul,
        "guid" / Guid
    )


@declare(guid=guid("922cdcf3-6123-42da-a877-1a24f23e39c5"), event_id=7003, version=0)
class Microsoft_WindowsPhone_CoreMessaging_7003_0(Etw):
    pattern = Struct(
        "pwsz" / WString
    )


@declare(guid=guid("922cdcf3-6123-42da-a877-1a24f23e39c5"), event_id=7004, version=0)
class Microsoft_WindowsPhone_CoreMessaging_7004_0(Etw):
    pattern = Struct(
        "pwsz" / WString
    )


@declare(guid=guid("922cdcf3-6123-42da-a877-1a24f23e39c5"), event_id=7005, version=0)
class Microsoft_WindowsPhone_CoreMessaging_7005_0(Etw):
    pattern = Struct(
        "hex" / Int32ul,
        "hex2" / Int32ul,
        "hex3" / Int32ul
    )


@declare(guid=guid("922cdcf3-6123-42da-a877-1a24f23e39c5"), event_id=7006, version=0)
class Microsoft_WindowsPhone_CoreMessaging_7006_0(Etw):
    pattern = Struct(
        "hex" / Int32ul
    )


@declare(guid=guid("922cdcf3-6123-42da-a877-1a24f23e39c5"), event_id=7007, version=0)
class Microsoft_WindowsPhone_CoreMessaging_7007_0(Etw):
    pattern = Struct(
        "hex" / Int32ul,
        "hex2" / Int32ul
    )


@declare(guid=guid("922cdcf3-6123-42da-a877-1a24f23e39c5"), event_id=7008, version=0)
class Microsoft_WindowsPhone_CoreMessaging_7008_0(Etw):
    pattern = Struct(
        "hex" / Int32ul,
        "hex2" / Int32ul
    )


@declare(guid=guid("922cdcf3-6123-42da-a877-1a24f23e39c5"), event_id=8000, version=0)
class Microsoft_WindowsPhone_CoreMessaging_8000_0(Etw):
    pattern = Struct(
        "ptr1" / Int64ul,
        "ptr2" / Int64ul,
        "ptr3" / Int64ul
    )


@declare(guid=guid("922cdcf3-6123-42da-a877-1a24f23e39c5"), event_id=8001, version=0)
class Microsoft_WindowsPhone_CoreMessaging_8001_0(Etw):
    pattern = Struct(
        "ptr1" / Int64ul,
        "ptr2" / Int64ul,
        "ptr3" / Int64ul,
        "hex" / Int32ul
    )


@declare(guid=guid("922cdcf3-6123-42da-a877-1a24f23e39c5"), event_id=8002, version=0)
class Microsoft_WindowsPhone_CoreMessaging_8002_0(Etw):
    pattern = Struct(
        "ptr" / Int64ul,
        "hex" / Int32ul,
        "fBool1" / Int8ul,
        "fBool2" / Int8ul
    )


@declare(guid=guid("922cdcf3-6123-42da-a877-1a24f23e39c5"), event_id=8003, version=0)
class Microsoft_WindowsPhone_CoreMessaging_8003_0(Etw):
    pattern = Struct(
        "ptr1" / Int64ul,
        "ptr2" / Int64ul,
        "fBool" / Int8ul
    )


@declare(guid=guid("922cdcf3-6123-42da-a877-1a24f23e39c5"), event_id=8004, version=0)
class Microsoft_WindowsPhone_CoreMessaging_8004_0(Etw):
    pattern = Struct(
        "ptr1" / Int64ul,
        "ptr2" / Int64ul
    )


@declare(guid=guid("922cdcf3-6123-42da-a877-1a24f23e39c5"), event_id=8005, version=0)
class Microsoft_WindowsPhone_CoreMessaging_8005_0(Etw):
    pattern = Struct(
        "ptr1" / Int64ul,
        "ptr2" / Int64ul
    )


@declare(guid=guid("922cdcf3-6123-42da-a877-1a24f23e39c5"), event_id=8007, version=0)
class Microsoft_WindowsPhone_CoreMessaging_8007_0(Etw):
    pattern = Struct(
        "ptr1" / Int64ul,
        "ptr2" / Int64ul
    )


@declare(guid=guid("922cdcf3-6123-42da-a877-1a24f23e39c5"), event_id=20000, version=0)
class Microsoft_WindowsPhone_CoreMessaging_20000_0(Etw):
    pattern = Struct(
        "pwsz" / WString,
        "hex" / Int32ul,
        "pwsz2" / WString
    )


@declare(guid=guid("922cdcf3-6123-42da-a877-1a24f23e39c5"), event_id=20001, version=0)
class Microsoft_WindowsPhone_CoreMessaging_20001_0(Etw):
    pattern = Struct(
        "pwsz" / WString,
        "RegisteredObjectType" / Int32ul,
        "RegistrarScope" / Int32ul
    )


@declare(guid=guid("922cdcf3-6123-42da-a877-1a24f23e39c5"), event_id=20002, version=0)
class Microsoft_WindowsPhone_CoreMessaging_20002_0(Etw):
    pattern = Struct(
        "hex" / Int32ul,
        "hex2" / Int32ul,
        "guid" / Guid
    )


@declare(guid=guid("922cdcf3-6123-42da-a877-1a24f23e39c5"), event_id=20003, version=0)
class Microsoft_WindowsPhone_CoreMessaging_20003_0(Etw):
    pattern = Struct(
        "hex" / Int32ul,
        "hex2" / Int32ul
    )


@declare(guid=guid("922cdcf3-6123-42da-a877-1a24f23e39c5"), event_id=20004, version=0)
class Microsoft_WindowsPhone_CoreMessaging_20004_0(Etw):
    pattern = Struct(
        "pwsz" / WString,
        "hresult" / Int32sl
    )


@declare(guid=guid("922cdcf3-6123-42da-a877-1a24f23e39c5"), event_id=20005, version=0)
class Microsoft_WindowsPhone_CoreMessaging_20005_0(Etw):
    pattern = Struct(
        "pwsz" / WString
    )

