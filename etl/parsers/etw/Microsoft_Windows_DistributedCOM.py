# -*- coding: utf-8 -*-
"""
Microsoft-Windows-DistributedCOM
GUID : 1b562e86-b7aa-4131-badc-b6f3a001407e
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("1b562e86-b7aa-4131-badc-b6f3a001407e"), event_id=10000, version=0)
class Microsoft_Windows_DistributedCOM_10000_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )


@declare(guid=guid("1b562e86-b7aa-4131-badc-b6f3a001407e"), event_id=10001, version=0)
class Microsoft_Windows_DistributedCOM_10001_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "param5" / WString
    )


@declare(guid=guid("1b562e86-b7aa-4131-badc-b6f3a001407e"), event_id=10002, version=0)
class Microsoft_Windows_DistributedCOM_10002_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString
    )


@declare(guid=guid("1b562e86-b7aa-4131-badc-b6f3a001407e"), event_id=10003, version=0)
class Microsoft_Windows_DistributedCOM_10003_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString
    )


@declare(guid=guid("1b562e86-b7aa-4131-badc-b6f3a001407e"), event_id=10004, version=0)
class Microsoft_Windows_DistributedCOM_10004_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString
    )


@declare(guid=guid("1b562e86-b7aa-4131-badc-b6f3a001407e"), event_id=10005, version=0)
class Microsoft_Windows_DistributedCOM_10005_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString
    )


@declare(guid=guid("1b562e86-b7aa-4131-badc-b6f3a001407e"), event_id=10006, version=0)
class Microsoft_Windows_DistributedCOM_10006_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )


@declare(guid=guid("1b562e86-b7aa-4131-badc-b6f3a001407e"), event_id=10007, version=0)
class Microsoft_Windows_DistributedCOM_10007_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("1b562e86-b7aa-4131-badc-b6f3a001407e"), event_id=10008, version=0)
class Microsoft_Windows_DistributedCOM_10008_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString
    )


@declare(guid=guid("1b562e86-b7aa-4131-badc-b6f3a001407e"), event_id=10009, version=0)
class Microsoft_Windows_DistributedCOM_10009_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("1b562e86-b7aa-4131-badc-b6f3a001407e"), event_id=10010, version=0)
class Microsoft_Windows_DistributedCOM_10010_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("1b562e86-b7aa-4131-badc-b6f3a001407e"), event_id=10011, version=0)
class Microsoft_Windows_DistributedCOM_10011_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("1b562e86-b7aa-4131-badc-b6f3a001407e"), event_id=10012, version=0)
class Microsoft_Windows_DistributedCOM_10012_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )


@declare(guid=guid("1b562e86-b7aa-4131-badc-b6f3a001407e"), event_id=10014, version=0)
class Microsoft_Windows_DistributedCOM_10014_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("1b562e86-b7aa-4131-badc-b6f3a001407e"), event_id=10015, version=0)
class Microsoft_Windows_DistributedCOM_10015_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "param5" / WString,
        "param6" / WString,
        "param7" / WString,
        "param8" / WString,
        "param9" / WString,
        "param10" / WString
    )


@declare(guid=guid("1b562e86-b7aa-4131-badc-b6f3a001407e"), event_id=10016, version=0)
class Microsoft_Windows_DistributedCOM_10016_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "param5" / WString,
        "param6" / WString,
        "param7" / WString,
        "param8" / WString,
        "param9" / WString,
        "param10" / WString,
        "param11" / WString
    )


@declare(guid=guid("1b562e86-b7aa-4131-badc-b6f3a001407e"), event_id=10017, version=0)
class Microsoft_Windows_DistributedCOM_10017_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "param5" / WString,
        "param6" / WString,
        "param7" / WString,
        "param8" / WString,
        "param9" / WString,
        "param10" / WString
    )


@declare(guid=guid("1b562e86-b7aa-4131-badc-b6f3a001407e"), event_id=10018, version=0)
class Microsoft_Windows_DistributedCOM_10018_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "param5" / WString,
        "param6" / WString,
        "param7" / WString,
        "param8" / WString,
        "param9" / WString
    )


@declare(guid=guid("1b562e86-b7aa-4131-badc-b6f3a001407e"), event_id=10019, version=0)
class Microsoft_Windows_DistributedCOM_10019_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "param5" / WString,
        "param6" / WString,
        "param7" / WString,
        "param8" / WString,
        "param9" / WString
    )


@declare(guid=guid("1b562e86-b7aa-4131-badc-b6f3a001407e"), event_id=10020, version=0)
class Microsoft_Windows_DistributedCOM_10020_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("1b562e86-b7aa-4131-badc-b6f3a001407e"), event_id=10021, version=0)
class Microsoft_Windows_DistributedCOM_10021_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("1b562e86-b7aa-4131-badc-b6f3a001407e"), event_id=10022, version=0)
class Microsoft_Windows_DistributedCOM_10022_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )


@declare(guid=guid("1b562e86-b7aa-4131-badc-b6f3a001407e"), event_id=10023, version=0)
class Microsoft_Windows_DistributedCOM_10023_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("1b562e86-b7aa-4131-badc-b6f3a001407e"), event_id=10024, version=0)
class Microsoft_Windows_DistributedCOM_10024_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("1b562e86-b7aa-4131-badc-b6f3a001407e"), event_id=10026, version=0)
class Microsoft_Windows_DistributedCOM_10026_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )


@declare(guid=guid("1b562e86-b7aa-4131-badc-b6f3a001407e"), event_id=10027, version=0)
class Microsoft_Windows_DistributedCOM_10027_0(Etw):
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


@declare(guid=guid("1b562e86-b7aa-4131-badc-b6f3a001407e"), event_id=10028, version=0)
class Microsoft_Windows_DistributedCOM_10028_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString,
        "param4" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("1b562e86-b7aa-4131-badc-b6f3a001407e"), event_id=10029, version=0)
class Microsoft_Windows_DistributedCOM_10029_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString
    )


@declare(guid=guid("1b562e86-b7aa-4131-badc-b6f3a001407e"), event_id=10030, version=0)
class Microsoft_Windows_DistributedCOM_10030_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "param3" / WString
    )


@declare(guid=guid("1b562e86-b7aa-4131-badc-b6f3a001407e"), event_id=10031, version=0)
class Microsoft_Windows_DistributedCOM_10031_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("1b562e86-b7aa-4131-badc-b6f3a001407e"), event_id=10032, version=0)
class Microsoft_Windows_DistributedCOM_10032_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("1b562e86-b7aa-4131-badc-b6f3a001407e"), event_id=10033, version=0)
class Microsoft_Windows_DistributedCOM_10033_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("1b562e86-b7aa-4131-badc-b6f3a001407e"), event_id=10034, version=0)
class Microsoft_Windows_DistributedCOM_10034_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("1b562e86-b7aa-4131-badc-b6f3a001407e"), event_id=10035, version=0)
class Microsoft_Windows_DistributedCOM_10035_0(Etw):
    pattern = Struct(
        "ProvidedIid" / WString,
        "RequestedIid" / WString,
        "HandlerClsid" / WString,
        "HRESULT" / WString
    )

