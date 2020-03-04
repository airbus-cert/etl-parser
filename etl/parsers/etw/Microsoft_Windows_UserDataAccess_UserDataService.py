# -*- coding: utf-8 -*-
"""
Microsoft-Windows-UserDataAccess-UserDataService
GUID : fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=1, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_1_0(Etw):
    pattern = Struct(
        "P1_HResult" / Int32sl,
        "P2_String" / CString,
        "P3_UInt32" / Int32ul
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=2, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_2_0(Etw):
    pattern = Struct(
        "P1_HResult" / Int32sl,
        "P2_String" / CString,
        "P3_UInt32" / Int32ul
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=3, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_3_0(Etw):
    pattern = Struct(
        "Message" / Int64ul
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=101, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_101_0(Etw):
    pattern = Struct(
        "path" / WString,
        "handle" / Int64ul
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=102, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_102_0(Etw):
    pattern = Struct(
        "handle" / Int64ul
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=103, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_103_0(Etw):
    pattern = Struct(
        "handle" / Int64ul
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=104, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_104_0(Etw):
    pattern = Struct(
        "AppOwnershipId" / Guid,
        "StoreAppOwnershipId" / Guid
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=105, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_105_0(Etw):
    pattern = Struct(
        "Prop_Boolean_1" / Int8ul
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=106, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_106_0(Etw):
    pattern = Struct(
        "Prop_UInt_1" / Int32ul,
        "Prop_UInt_2" / Int32ul,
        "Prop_UInt_3" / Int32ul,
        "Prop_UInt_4" / Int32ul
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=107, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_107_0(Etw):
    pattern = Struct(
        "P1_HResult" / Int32sl
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=108, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_108_0(Etw):
    pattern = Struct(
        "P1_HResult" / Int32sl
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=201, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_201_0(Etw):
    pattern = Struct(
        "handle" / Int64ul,
        "maxnotify" / Int32ul
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=202, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_202_0(Etw):
    pattern = Struct(
        "handle" / Int64ul,
        "requested" / Int32ul,
        "returned" / Int32ul,
        "remaining" / Int32ul,
        "missed" / Int8ul
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=203, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_203_0(Etw):
    pattern = Struct(
        "handle" / Int64ul,
        "readyCount" / Int32ul,
        "lost" / Int8ul
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=204, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_204_0(Etw):
    pattern = Struct(
        "handle" / Int64ul,
        "type" / Int32ul,
        "id" / Int32ul
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=205, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_205_0(Etw):
    pattern = Struct(
        "id" / Int32ul,
        "starttime" / Int64ul
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=206, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_206_0(Etw):
    pattern = Struct(
        "handle" / Int64ul,
        "requested" / Int32ul,
        "returned" / Int32ul,
        "remaining" / Int32ul,
        "missed" / Int8ul
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=301, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_301_0(Etw):
    pattern = Struct(
        "handle" / Int64ul,
        "type" / Int32ul,
        "id" / Int32ul
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=302, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_302_0(Etw):
    pattern = Struct(
        "handle" / Int64ul,
        "type" / Int32ul,
        "id" / Int32ul
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=303, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_303_0(Etw):
    pattern = Struct(
        "handle" / Int64ul,
        "type" / Int32ul,
        "id" / Int32ul
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=304, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_304_0(Etw):
    pattern = Struct(
        "handle" / Int64ul
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=305, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_305_0(Etw):
    pattern = Struct(
        "handle" / Int64ul
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=308, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_308_0(Etw):
    pattern = Struct(
        "Prop_UInt_1" / Int32ul,
        "Prop_UInt_2" / Int32ul,
        "Prop_UInt_3" / Int32ul
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=400, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_400_0(Etw):
    pattern = Struct(
        "handle" / Int64ul
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=401, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_401_0(Etw):
    pattern = Struct(
        "handle" / Int64ul
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=402, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_402_0(Etw):
    pattern = Struct(
        "Prop_UInt_1" / Int32ul,
        "Prop_UInt_2" / Int32ul,
        "Prop_UInt_3" / Int32ul,
        "Prop_UInt_4" / Int32ul
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=403, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_403_0(Etw):
    pattern = Struct(
        "Prop_ULong" / Int64ul,
        "Prop_UInt" / Int32ul
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=404, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_404_0(Etw):
    pattern = Struct(
        "Prop_ULong" / Int64ul
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=405, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_405_0(Etw):
    pattern = Struct(
        "Prop_UInt_1" / Int32ul,
        "Prop_UInt_2" / Int32ul,
        "Prop_UInt_3" / Int32ul
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=406, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_406_0(Etw):
    pattern = Struct(
        "Prop_UInt_1" / Int32ul,
        "Prop_UInt_2" / Int32ul
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=407, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_407_0(Etw):
    pattern = Struct(
        "Prop_Boolean_1" / Int8ul,
        "Prop_Boolean_2" / Int8ul
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=501, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_501_0(Etw):
    pattern = Struct(
        "Prop_UInt_1" / Int32ul,
        "Prop_UInt_2" / Int32ul,
        "Prop_UInt_3" / Int32ul,
        "Prop_UInt_4" / Int32ul
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=502, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_502_0(Etw):
    pattern = Struct(
        "remoteId" / WString
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=503, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_503_0(Etw):
    pattern = Struct(
        "remoteId" / WString,
        "operationId" / Int32ul,
        "requestAmnt" / Int32ul,
        "providedAmnt" / Int32ul,
        "qualifyingAmnt" / Int32ul
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=504, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_504_0(Etw):
    pattern = Struct(
        "deepLink" / WString
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=505, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_505_0(Etw):
    pattern = Struct(
        "deepLink" / WString
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=700, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_700_0(Etw):
    pattern = Struct(
        "handle" / Int64ul
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=701, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_701_0(Etw):
    pattern = Struct(
        "handle" / Int64ul
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=702, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_702_0(Etw):
    pattern = Struct(
        "EventType" / Int32ul,
        "ItemType" / Int32ul
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=705, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_705_0(Etw):
    pattern = Struct(
        "ActivationStatus" / Int32ul
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=706, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_706_0(Etw):
    pattern = Struct(
        "ActivationStatus" / Int32ul
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=707, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_707_0(Etw):
    pattern = Struct(
        "TelString" / WString
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=708, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_708_0(Etw):
    pattern = Struct(
        "TelString" / WString,
        "RcsCapabilityBits" / Int32ul
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=711, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_711_0(Etw):
    pattern = Struct(
        "handle" / Int64ul
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=712, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_712_0(Etw):
    pattern = Struct(
        "handle" / Int64ul
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=713, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_713_0(Etw):
    pattern = Struct(
        "RcsChatId" / WString,
        "isGroup" / Int8ul,
        "TelString" / WString,
        "isComposing" / Int8ul
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=714, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_714_0(Etw):
    pattern = Struct(
        "handle" / Int64ul
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=715, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_715_0(Etw):
    pattern = Struct(
        "handle" / Int64ul
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=716, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_716_0(Etw):
    pattern = Struct(
        "handle" / Int64ul
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=717, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_717_0(Etw):
    pattern = Struct(
        "handle" / Int64ul
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=718, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_718_0(Etw):
    pattern = Struct(
        "serviceType" / Int32ul,
        "isSupported" / Int8ul
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=719, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_719_0(Etw):
    pattern = Struct(
        "AppPackageFamilyName" / WString
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=735, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_735_0(Etw):
    pattern = Struct(
        "Prop_ULong" / Int64ul
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=736, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_736_0(Etw):
    pattern = Struct(
        "Prop_ULong" / Int64ul
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=741, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_741_0(Etw):
    pattern = Struct(
        "Prop_ULong" / Int64ul
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=744, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_744_0(Etw):
    pattern = Struct(
        "Prop_UInt_1" / Int32ul,
        "Prop_UInt_2" / Int32ul
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=745, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_745_0(Etw):
    pattern = Struct(
        "P1_HResult" / Int32sl
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=746, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_746_0(Etw):
    pattern = Struct(
        "P1_HResult" / Int32sl
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=747, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_747_0(Etw):
    pattern = Struct(
        "P1_HResult" / Int32sl
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=748, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_748_0(Etw):
    pattern = Struct(
        "P1_HResult" / Int32sl
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=749, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_749_0(Etw):
    pattern = Struct(
        "P1_HResult" / Int32sl,
        "Prop_ULong" / Int64ul
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=750, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_750_0(Etw):
    pattern = Struct(
        "P1_HResult" / Int32sl,
        "Prop_ULong" / Int64ul
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=751, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_751_0(Etw):
    pattern = Struct(
        "P1_HResult" / Int32sl
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=752, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_752_0(Etw):
    pattern = Struct(
        "Prop_ULong" / Int64ul
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=759, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_759_0(Etw):
    pattern = Struct(
        "P1_UnicodeString" / WString
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=762, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_762_0(Etw):
    pattern = Struct(
        "handle" / Int64ul
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=763, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_763_0(Etw):
    pattern = Struct(
        "handle" / Int64ul
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=1204, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_1204_0(Etw):
    pattern = Struct(
        "AppName" / CString,
        "AccessedString" / CString
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=1205, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_1205_0(Etw):
    pattern = Struct(
        "AppName" / CString,
        "AccessedString" / CString
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=2001, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_2001_0(Etw):
    pattern = Struct(
        "Prop_Boolean_1" / Int8ul,
        "Prop_Boolean_2" / Int8ul
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=2003, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_2003_0(Etw):
    pattern = Struct(
        "Prop_UInt_1" / Int32ul,
        "Prop_UInt_2" / Int32ul,
        "Prop_UInt_3" / Int32ul,
        "Prop_UInt_4" / Int32ul,
        "Prop_UInt_5" / Int32ul
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=2004, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_2004_0(Etw):
    pattern = Struct(
        "Prop_Prop" / Int32ul
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=2005, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_2005_0(Etw):
    pattern = Struct(
        "Prop_UInt_1" / Int32ul,
        "Prop_UInt_2" / Int32ul,
        "Prop_UInt_3" / Int32ul,
        "Prop_UInt_4" / Int32ul,
        "Prop_UInt_5" / Int32ul
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=2006, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_2006_0(Etw):
    pattern = Struct(
        "AppId" / WString,
        "AppDataCleanupReason" / Int32ul
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=2007, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_2007_0(Etw):
    pattern = Struct(
        "AppId" / WString,
        "AppDataCleanupReason" / Int32ul
    )


@declare(guid=guid("fb19ee2c-0d22-4a2e-969e-dd41ae0ce1a9"), event_id=2008, version=0)
class Microsoft_Windows_UserDataAccess_UserDataService_2008_0(Etw):
    pattern = Struct(
        "P1_UnicodeString" / WString
    )

