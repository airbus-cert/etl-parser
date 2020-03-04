# -*- coding: utf-8 -*-
"""
Microsoft-Windows-WindowsUpdateClient
GUID : 945a8954-c147-4acd-923f-40c45405a658
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("945a8954-c147-4acd-923f-40c45405a658"), event_id=17, version=0)
class Microsoft_Windows_WindowsUpdateClient_17_0(Etw):
    pattern = Struct(
        "updatelist" / WString
    )


@declare(guid=guid("945a8954-c147-4acd-923f-40c45405a658"), event_id=18, version=0)
class Microsoft_Windows_WindowsUpdateClient_18_0(Etw):
    pattern = Struct(
        "schedinstalldate" / WString,
        "schedinstalltime" / WString,
        "updatelist" / WString
    )


@declare(guid=guid("945a8954-c147-4acd-923f-40c45405a658"), event_id=19, version=0)
class Microsoft_Windows_WindowsUpdateClient_19_0(Etw):
    pattern = Struct(
        "updateTitle" / WString,
        "updateGuid" / Guid,
        "updateRevisionNumber" / Int32ul
    )


@declare(guid=guid("945a8954-c147-4acd-923f-40c45405a658"), event_id=19, version=1)
class Microsoft_Windows_WindowsUpdateClient_19_1(Etw):
    pattern = Struct(
        "updateTitle" / WString,
        "updateGuid" / Guid,
        "updateRevisionNumber" / Int32ul,
        "serviceGuid" / Guid
    )


@declare(guid=guid("945a8954-c147-4acd-923f-40c45405a658"), event_id=20, version=0)
class Microsoft_Windows_WindowsUpdateClient_20_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "updateTitle" / WString,
        "updateGuid" / Guid,
        "updateRevisionNumber" / Int32ul
    )


@declare(guid=guid("945a8954-c147-4acd-923f-40c45405a658"), event_id=20, version=1)
class Microsoft_Windows_WindowsUpdateClient_20_1(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "updateTitle" / WString,
        "updateGuid" / Guid,
        "updateRevisionNumber" / Int32ul,
        "serviceGuid" / Guid
    )


@declare(guid=guid("945a8954-c147-4acd-923f-40c45405a658"), event_id=21, version=0)
class Microsoft_Windows_WindowsUpdateClient_21_0(Etw):
    pattern = Struct(
        "updatelist" / WString
    )


@declare(guid=guid("945a8954-c147-4acd-923f-40c45405a658"), event_id=22, version=0)
class Microsoft_Windows_WindowsUpdateClient_22_0(Etw):
    pattern = Struct(
        "restarttime" / WString,
        "updatelist" / WString
    )


@declare(guid=guid("945a8954-c147-4acd-923f-40c45405a658"), event_id=23, version=0)
class Microsoft_Windows_WindowsUpdateClient_23_0(Etw):
    pattern = Struct(
        "updateTitle" / WString,
        "updateGuid" / Guid,
        "updateRevisionNumber" / Int32ul
    )


@declare(guid=guid("945a8954-c147-4acd-923f-40c45405a658"), event_id=23, version=1)
class Microsoft_Windows_WindowsUpdateClient_23_1(Etw):
    pattern = Struct(
        "updateTitle" / WString,
        "updateGuid" / Guid,
        "updateRevisionNumber" / Int32ul,
        "serviceGuid" / Guid
    )


@declare(guid=guid("945a8954-c147-4acd-923f-40c45405a658"), event_id=24, version=0)
class Microsoft_Windows_WindowsUpdateClient_24_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "updatelist" / WString,
        "updateGuid" / Guid,
        "updateRevisionNumber" / Int32ul
    )


@declare(guid=guid("945a8954-c147-4acd-923f-40c45405a658"), event_id=24, version=1)
class Microsoft_Windows_WindowsUpdateClient_24_1(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "updatelist" / WString,
        "updateGuid" / Guid,
        "updateRevisionNumber" / Int32ul,
        "serviceGuid" / Guid
    )


@declare(guid=guid("945a8954-c147-4acd-923f-40c45405a658"), event_id=25, version=0)
class Microsoft_Windows_WindowsUpdateClient_25_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul
    )


@declare(guid=guid("945a8954-c147-4acd-923f-40c45405a658"), event_id=25, version=1)
class Microsoft_Windows_WindowsUpdateClient_25_1(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "serviceGuid" / Guid
    )


@declare(guid=guid("945a8954-c147-4acd-923f-40c45405a658"), event_id=26, version=0)
class Microsoft_Windows_WindowsUpdateClient_26_0(Etw):
    pattern = Struct(
        "updateCount" / Int32ul
    )


@declare(guid=guid("945a8954-c147-4acd-923f-40c45405a658"), event_id=26, version=1)
class Microsoft_Windows_WindowsUpdateClient_26_1(Etw):
    pattern = Struct(
        "updateCount" / Int32ul,
        "serviceGuid" / Guid
    )


@declare(guid=guid("945a8954-c147-4acd-923f-40c45405a658"), event_id=31, version=0)
class Microsoft_Windows_WindowsUpdateClient_31_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "updateGuid" / Guid,
        "updateRevisionNumber" / Int32ul
    )


@declare(guid=guid("945a8954-c147-4acd-923f-40c45405a658"), event_id=31, version=1)
class Microsoft_Windows_WindowsUpdateClient_31_1(Etw):
    pattern = Struct(
        "updateTitle" / WString,
        "errorCode" / Int32ul,
        "updateGuid" / Guid,
        "updateRevisionNumber" / Int32ul
    )


@declare(guid=guid("945a8954-c147-4acd-923f-40c45405a658"), event_id=32, version=0)
class Microsoft_Windows_WindowsUpdateClient_32_0(Etw):
    pattern = Struct(
        "serverName" / WString
    )


@declare(guid=guid("945a8954-c147-4acd-923f-40c45405a658"), event_id=33, version=0)
class Microsoft_Windows_WindowsUpdateClient_33_0(Etw):
    pattern = Struct(
        "serverName" / WString
    )


@declare(guid=guid("945a8954-c147-4acd-923f-40c45405a658"), event_id=34, version=0)
class Microsoft_Windows_WindowsUpdateClient_34_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul
    )


@declare(guid=guid("945a8954-c147-4acd-923f-40c45405a658"), event_id=35, version=0)
class Microsoft_Windows_WindowsUpdateClient_35_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul
    )


@declare(guid=guid("945a8954-c147-4acd-923f-40c45405a658"), event_id=36, version=0)
class Microsoft_Windows_WindowsUpdateClient_36_0(Etw):
    pattern = Struct(
        "version1" / WString,
        "version2" / WString
    )


@declare(guid=guid("945a8954-c147-4acd-923f-40c45405a658"), event_id=37, version=0)
class Microsoft_Windows_WindowsUpdateClient_37_0(Etw):
    pattern = Struct(
        "version1" / WString,
        "version2" / WString
    )


@declare(guid=guid("945a8954-c147-4acd-923f-40c45405a658"), event_id=40, version=0)
class Microsoft_Windows_WindowsUpdateClient_40_0(Etw):
    pattern = Struct(
        "updateGuid" / Guid,
        "updateRevisionNumber" / Int32ul
    )


@declare(guid=guid("945a8954-c147-4acd-923f-40c45405a658"), event_id=40, version=1)
class Microsoft_Windows_WindowsUpdateClient_40_1(Etw):
    pattern = Struct(
        "updateGuid" / Guid,
        "updateRevisionNumber" / Int32ul,
        "serviceGuid" / Guid
    )


@declare(guid=guid("945a8954-c147-4acd-923f-40c45405a658"), event_id=41, version=0)
class Microsoft_Windows_WindowsUpdateClient_41_0(Etw):
    pattern = Struct(
        "updateGuid" / Guid,
        "updateRevisionNumber" / Int32ul
    )


@declare(guid=guid("945a8954-c147-4acd-923f-40c45405a658"), event_id=41, version=1)
class Microsoft_Windows_WindowsUpdateClient_41_1(Etw):
    pattern = Struct(
        "updateTitle" / WString,
        "updateGuid" / Guid,
        "updateRevisionNumber" / Int32ul
    )


@declare(guid=guid("945a8954-c147-4acd-923f-40c45405a658"), event_id=42, version=0)
class Microsoft_Windows_WindowsUpdateClient_42_0(Etw):
    pattern = Struct(
        "hc_stateid" / Int32ul,
        "restartDate" / WString,
        "restartTime" / WString
    )


@declare(guid=guid("945a8954-c147-4acd-923f-40c45405a658"), event_id=43, version=0)
class Microsoft_Windows_WindowsUpdateClient_43_0(Etw):
    pattern = Struct(
        "updateTitle" / WString,
        "updateGuid" / Guid,
        "updateRevisionNumber" / Int32ul
    )


@declare(guid=guid("945a8954-c147-4acd-923f-40c45405a658"), event_id=43, version=1)
class Microsoft_Windows_WindowsUpdateClient_43_1(Etw):
    pattern = Struct(
        "updateTitle" / WString,
        "updateGuid" / Guid,
        "updateRevisionNumber" / Int32ul
    )


@declare(guid=guid("945a8954-c147-4acd-923f-40c45405a658"), event_id=44, version=0)
class Microsoft_Windows_WindowsUpdateClient_44_0(Etw):
    pattern = Struct(
        "updateGuid" / Guid,
        "updateRevisionNumber" / Int32ul
    )


@declare(guid=guid("945a8954-c147-4acd-923f-40c45405a658"), event_id=44, version=1)
class Microsoft_Windows_WindowsUpdateClient_44_1(Etw):
    pattern = Struct(
        "updateTitle" / WString,
        "updateGuid" / Guid,
        "updateRevisionNumber" / Int32ul
    )


@declare(guid=guid("945a8954-c147-4acd-923f-40c45405a658"), event_id=209, version=0)
class Microsoft_Windows_WindowsUpdateClient_209_0(Etw):
    pattern = Struct(
        "pdcActivationId" / Int32ul,
        "description" / WString,
        "accessType" / Int8ul,
        "isInteractiveOrAPIDriven" / Int8ul,
        "stopIdleTimer" / Int8ul,
        "networkRefCount" / Int32ul,
        "systemRefCount" / Int32ul
    )


@declare(guid=guid("945a8954-c147-4acd-923f-40c45405a658"), event_id=210, version=0)
class Microsoft_Windows_WindowsUpdateClient_210_0(Etw):
    pattern = Struct(
        "pdcActivationId" / Int32ul,
        "description" / WString,
        "accessType" / Int8ul,
        "isInteractiveOrAPIDriven" / Int8ul,
        "stopIdleTimer" / Int8ul,
        "networkRefCount" / Int32ul,
        "systemRefCount" / Int32ul
    )


@declare(guid=guid("945a8954-c147-4acd-923f-40c45405a658"), event_id=211, version=0)
class Microsoft_Windows_WindowsUpdateClient_211_0(Etw):
    pattern = Struct(
        "pdcActivationId" / Int32ul,
        "description" / WString,
        "accessType" / Int8ul,
        "isInteractiveOrAPIDriven" / Int8ul,
        "stopIdleTimer" / Int8ul,
        "networkRefCount" / Int32ul,
        "systemRefCount" / Int32ul
    )


@declare(guid=guid("945a8954-c147-4acd-923f-40c45405a658"), event_id=212, version=1)
class Microsoft_Windows_WindowsUpdateClient_212_1(Etw):
    pattern = Struct(
        "updateTitle" / WString,
        "updateGuid" / Guid,
        "updateRevisionNumber" / Int32ul,
        "serviceGuid" / Guid
    )


@declare(guid=guid("945a8954-c147-4acd-923f-40c45405a658"), event_id=213, version=0)
class Microsoft_Windows_WindowsUpdateClient_213_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "updatelist" / WString,
        "updateGuid" / Guid,
        "updateRevisionNumber" / Int32ul
    )


@declare(guid=guid("945a8954-c147-4acd-923f-40c45405a658"), event_id=214, version=0)
class Microsoft_Windows_WindowsUpdateClient_214_0(Etw):
    pattern = Struct(
        "updateTitle" / WString,
        "updateGuid" / Guid,
        "updateRevisionNumber" / Int32ul
    )


@declare(guid=guid("945a8954-c147-4acd-923f-40c45405a658"), event_id=215, version=0)
class Microsoft_Windows_WindowsUpdateClient_215_0(Etw):
    pattern = Struct(
        "updateTitle" / WString,
        "updateGuid" / Guid,
        "updateRevisionNumber" / Int32ul
    )

