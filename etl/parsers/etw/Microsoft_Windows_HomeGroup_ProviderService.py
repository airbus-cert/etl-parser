# -*- coding: utf-8 -*-
"""
Microsoft-Windows-HomeGroup-ProviderService
GUID : c9bdb4eb-9287-4c8e-8378-6896f0d1c5ef
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("c9bdb4eb-9287-4c8e-8378-6896f0d1c5ef"), event_id=5001, version=0)
class Microsoft_Windows_HomeGroup_ProviderService_5001_0(Etw):
    pattern = Struct(
        "Error" / WString
    )


@declare(guid=guid("c9bdb4eb-9287-4c8e-8378-6896f0d1c5ef"), event_id=5002, version=0)
class Microsoft_Windows_HomeGroup_ProviderService_5002_0(Etw):
    pattern = Struct(
        "Error" / WString
    )


@declare(guid=guid("c9bdb4eb-9287-4c8e-8378-6896f0d1c5ef"), event_id=5003, version=0)
class Microsoft_Windows_HomeGroup_ProviderService_5003_0(Etw):
    pattern = Struct(
        "Error" / WString
    )


@declare(guid=guid("c9bdb4eb-9287-4c8e-8378-6896f0d1c5ef"), event_id=5004, version=0)
class Microsoft_Windows_HomeGroup_ProviderService_5004_0(Etw):
    pattern = Struct(
        "Error" / WString,
        "Message" / WString
    )


@declare(guid=guid("c9bdb4eb-9287-4c8e-8378-6896f0d1c5ef"), event_id=5005, version=0)
class Microsoft_Windows_HomeGroup_ProviderService_5005_0(Etw):
    pattern = Struct(
        "Error" / WString
    )


@declare(guid=guid("c9bdb4eb-9287-4c8e-8378-6896f0d1c5ef"), event_id=5008, version=0)
class Microsoft_Windows_HomeGroup_ProviderService_5008_0(Etw):
    pattern = Struct(
        "Error" / WString,
        "Message" / WString
    )


@declare(guid=guid("c9bdb4eb-9287-4c8e-8378-6896f0d1c5ef"), event_id=5009, version=0)
class Microsoft_Windows_HomeGroup_ProviderService_5009_0(Etw):
    pattern = Struct(
        "Error" / WString
    )


@declare(guid=guid("c9bdb4eb-9287-4c8e-8378-6896f0d1c5ef"), event_id=5011, version=0)
class Microsoft_Windows_HomeGroup_ProviderService_5011_0(Etw):
    pattern = Struct(
        "Error" / WString
    )


@declare(guid=guid("c9bdb4eb-9287-4c8e-8378-6896f0d1c5ef"), event_id=5012, version=0)
class Microsoft_Windows_HomeGroup_ProviderService_5012_0(Etw):
    pattern = Struct(
        "Error" / WString
    )


@declare(guid=guid("c9bdb4eb-9287-4c8e-8378-6896f0d1c5ef"), event_id=5013, version=0)
class Microsoft_Windows_HomeGroup_ProviderService_5013_0(Etw):
    pattern = Struct(
        "HomeGroupID" / Guid,
        "OldStatus" / Int32ul,
        "NewStatus" / Int32ul
    )


@declare(guid=guid("c9bdb4eb-9287-4c8e-8378-6896f0d1c5ef"), event_id=5015, version=0)
class Microsoft_Windows_HomeGroup_ProviderService_5015_0(Etw):
    pattern = Struct(
        "Error" / WString
    )


@declare(guid=guid("c9bdb4eb-9287-4c8e-8378-6896f0d1c5ef"), event_id=5016, version=0)
class Microsoft_Windows_HomeGroup_ProviderService_5016_0(Etw):
    pattern = Struct(
        "Error" / WString
    )


@declare(guid=guid("c9bdb4eb-9287-4c8e-8378-6896f0d1c5ef"), event_id=5017, version=0)
class Microsoft_Windows_HomeGroup_ProviderService_5017_0(Etw):
    pattern = Struct(
        "Error" / WString,
        "Message" / WString
    )

