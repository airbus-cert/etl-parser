# -*- coding: utf-8 -*-
"""
Microsoft-Windows-LanguagePackSetup
GUID : 7237fff9-a08a-4804-9c79-4a8704b70b87
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("7237fff9-a08a-4804-9c79-4a8704b70b87"), event_id=1000, version=0)
class Microsoft_Windows_LanguagePackSetup_1000_0(Etw):
    pattern = Struct(
        "Error" / Int32ul
    )


@declare(guid=guid("7237fff9-a08a-4804-9c79-4a8704b70b87"), event_id=1000, version=1)
class Microsoft_Windows_LanguagePackSetup_1000_1(Etw):
    pattern = Struct(
        "Error" / Int32ul
    )


@declare(guid=guid("7237fff9-a08a-4804-9c79-4a8704b70b87"), event_id=1001, version=0)
class Microsoft_Windows_LanguagePackSetup_1001_0(Etw):
    pattern = Struct(
        "Error" / Int32ul
    )


@declare(guid=guid("7237fff9-a08a-4804-9c79-4a8704b70b87"), event_id=1001, version=1)
class Microsoft_Windows_LanguagePackSetup_1001_1(Etw):
    pattern = Struct(
        "Error" / Int32ul
    )


@declare(guid=guid("7237fff9-a08a-4804-9c79-4a8704b70b87"), event_id=1002, version=0)
class Microsoft_Windows_LanguagePackSetup_1002_0(Etw):
    pattern = Struct(
        "Language" / WString,
        "Reason" / Int32ul
    )


@declare(guid=guid("7237fff9-a08a-4804-9c79-4a8704b70b87"), event_id=1003, version=0)
class Microsoft_Windows_LanguagePackSetup_1003_0(Etw):
    pattern = Struct(
        "Error" / Int32ul,
        "Language" / WString
    )


@declare(guid=guid("7237fff9-a08a-4804-9c79-4a8704b70b87"), event_id=1003, version=1)
class Microsoft_Windows_LanguagePackSetup_1003_1(Etw):
    pattern = Struct(
        "Error" / Int32ul,
        "Message" / WString,
        "Language" / WString
    )


@declare(guid=guid("7237fff9-a08a-4804-9c79-4a8704b70b87"), event_id=1004, version=0)
class Microsoft_Windows_LanguagePackSetup_1004_0(Etw):
    pattern = Struct(
        "Parameter" / WString
    )


@declare(guid=guid("7237fff9-a08a-4804-9c79-4a8704b70b87"), event_id=1004, version=1)
class Microsoft_Windows_LanguagePackSetup_1004_1(Etw):
    pattern = Struct(
        "Parameter" / WString
    )


@declare(guid=guid("7237fff9-a08a-4804-9c79-4a8704b70b87"), event_id=1005, version=0)
class Microsoft_Windows_LanguagePackSetup_1005_0(Etw):
    pattern = Struct(
        "Parameter" / WString
    )


@declare(guid=guid("7237fff9-a08a-4804-9c79-4a8704b70b87"), event_id=1005, version=1)
class Microsoft_Windows_LanguagePackSetup_1005_1(Etw):
    pattern = Struct(
        "Parameter" / WString
    )


@declare(guid=guid("7237fff9-a08a-4804-9c79-4a8704b70b87"), event_id=1006, version=0)
class Microsoft_Windows_LanguagePackSetup_1006_0(Etw):
    pattern = Struct(
        "Language" / WString
    )


@declare(guid=guid("7237fff9-a08a-4804-9c79-4a8704b70b87"), event_id=1006, version=1)
class Microsoft_Windows_LanguagePackSetup_1006_1(Etw):
    pattern = Struct(
        "Language" / WString
    )


@declare(guid=guid("7237fff9-a08a-4804-9c79-4a8704b70b87"), event_id=1007, version=0)
class Microsoft_Windows_LanguagePackSetup_1007_0(Etw):
    pattern = Struct(
        "Parameter" / WString
    )


@declare(guid=guid("7237fff9-a08a-4804-9c79-4a8704b70b87"), event_id=1007, version=1)
class Microsoft_Windows_LanguagePackSetup_1007_1(Etw):
    pattern = Struct(
        "Parameter" / WString
    )


@declare(guid=guid("7237fff9-a08a-4804-9c79-4a8704b70b87"), event_id=1008, version=0)
class Microsoft_Windows_LanguagePackSetup_1008_0(Etw):
    pattern = Struct(
        "Language" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("7237fff9-a08a-4804-9c79-4a8704b70b87"), event_id=1008, version=1)
class Microsoft_Windows_LanguagePackSetup_1008_1(Etw):
    pattern = Struct(
        "Language" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("7237fff9-a08a-4804-9c79-4a8704b70b87"), event_id=1009, version=0)
class Microsoft_Windows_LanguagePackSetup_1009_0(Etw):
    pattern = Struct(
        "Language" / WString
    )


@declare(guid=guid("7237fff9-a08a-4804-9c79-4a8704b70b87"), event_id=1009, version=1)
class Microsoft_Windows_LanguagePackSetup_1009_1(Etw):
    pattern = Struct(
        "Language1" / WString,
        "Language2" / WString
    )


@declare(guid=guid("7237fff9-a08a-4804-9c79-4a8704b70b87"), event_id=1010, version=0)
class Microsoft_Windows_LanguagePackSetup_1010_0(Etw):
    pattern = Struct(
        "Error" / WString
    )


@declare(guid=guid("7237fff9-a08a-4804-9c79-4a8704b70b87"), event_id=1013, version=0)
class Microsoft_Windows_LanguagePackSetup_1013_0(Etw):
    pattern = Struct(
        "Language" / WString
    )


@declare(guid=guid("7237fff9-a08a-4804-9c79-4a8704b70b87"), event_id=1014, version=0)
class Microsoft_Windows_LanguagePackSetup_1014_0(Etw):
    pattern = Struct(
        "Language" / WString
    )


@declare(guid=guid("7237fff9-a08a-4804-9c79-4a8704b70b87"), event_id=1015, version=0)
class Microsoft_Windows_LanguagePackSetup_1015_0(Etw):
    pattern = Struct(
        "Language" / WString
    )


@declare(guid=guid("7237fff9-a08a-4804-9c79-4a8704b70b87"), event_id=1016, version=0)
class Microsoft_Windows_LanguagePackSetup_1016_0(Etw):
    pattern = Struct(
        "Language1" / WString,
        "Language2" / WString
    )


@declare(guid=guid("7237fff9-a08a-4804-9c79-4a8704b70b87"), event_id=1017, version=0)
class Microsoft_Windows_LanguagePackSetup_1017_0(Etw):
    pattern = Struct(
        "Language" / WString
    )


@declare(guid=guid("7237fff9-a08a-4804-9c79-4a8704b70b87"), event_id=1018, version=0)
class Microsoft_Windows_LanguagePackSetup_1018_0(Etw):
    pattern = Struct(
        "Language" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("7237fff9-a08a-4804-9c79-4a8704b70b87"), event_id=1040, version=0)
class Microsoft_Windows_LanguagePackSetup_1040_0(Etw):
    pattern = Struct(
        "Language" / WString
    )


@declare(guid=guid("7237fff9-a08a-4804-9c79-4a8704b70b87"), event_id=1041, version=0)
class Microsoft_Windows_LanguagePackSetup_1041_0(Etw):
    pattern = Struct(
        "Language1" / WString,
        "Language2" / WString
    )


@declare(guid=guid("7237fff9-a08a-4804-9c79-4a8704b70b87"), event_id=1042, version=0)
class Microsoft_Windows_LanguagePackSetup_1042_0(Etw):
    pattern = Struct(
        "Language" / WString
    )


@declare(guid=guid("7237fff9-a08a-4804-9c79-4a8704b70b87"), event_id=1043, version=0)
class Microsoft_Windows_LanguagePackSetup_1043_0(Etw):
    pattern = Struct(
        "Language" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("7237fff9-a08a-4804-9c79-4a8704b70b87"), event_id=1060, version=0)
class Microsoft_Windows_LanguagePackSetup_1060_0(Etw):
    pattern = Struct(
        "Language1" / WString,
        "Language2" / WString
    )


@declare(guid=guid("7237fff9-a08a-4804-9c79-4a8704b70b87"), event_id=1061, version=0)
class Microsoft_Windows_LanguagePackSetup_1061_0(Etw):
    pattern = Struct(
        "Language1" / WString,
        "Language2" / WString
    )


@declare(guid=guid("7237fff9-a08a-4804-9c79-4a8704b70b87"), event_id=2000, version=0)
class Microsoft_Windows_LanguagePackSetup_2000_0(Etw):
    pattern = Struct(
        "Language" / WString
    )


@declare(guid=guid("7237fff9-a08a-4804-9c79-4a8704b70b87"), event_id=2000, version=1)
class Microsoft_Windows_LanguagePackSetup_2000_1(Etw):
    pattern = Struct(
        "Language" / WString
    )


@declare(guid=guid("7237fff9-a08a-4804-9c79-4a8704b70b87"), event_id=2001, version=0)
class Microsoft_Windows_LanguagePackSetup_2001_0(Etw):
    pattern = Struct(
        "Language" / WString
    )


@declare(guid=guid("7237fff9-a08a-4804-9c79-4a8704b70b87"), event_id=2001, version=1)
class Microsoft_Windows_LanguagePackSetup_2001_1(Etw):
    pattern = Struct(
        "Language" / WString
    )


@declare(guid=guid("7237fff9-a08a-4804-9c79-4a8704b70b87"), event_id=2002, version=0)
class Microsoft_Windows_LanguagePackSetup_2002_0(Etw):
    pattern = Struct(
        "Language" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("7237fff9-a08a-4804-9c79-4a8704b70b87"), event_id=2002, version=1)
class Microsoft_Windows_LanguagePackSetup_2002_1(Etw):
    pattern = Struct(
        "Language" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("7237fff9-a08a-4804-9c79-4a8704b70b87"), event_id=2003, version=0)
class Microsoft_Windows_LanguagePackSetup_2003_0(Etw):
    pattern = Struct(
        "PreviousLanguage" / WString,
        "NewLanguage" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("7237fff9-a08a-4804-9c79-4a8704b70b87"), event_id=2003, version=1)
class Microsoft_Windows_LanguagePackSetup_2003_1(Etw):
    pattern = Struct(
        "PreviousLanguage" / WString,
        "NewLanguage" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("7237fff9-a08a-4804-9c79-4a8704b70b87"), event_id=2004, version=0)
class Microsoft_Windows_LanguagePackSetup_2004_0(Etw):
    pattern = Struct(
        "PreviousLanguage" / WString,
        "NewLanguage" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("7237fff9-a08a-4804-9c79-4a8704b70b87"), event_id=2007, version=0)
class Microsoft_Windows_LanguagePackSetup_2007_0(Etw):
    pattern = Struct(
        "Language" / WString
    )


@declare(guid=guid("7237fff9-a08a-4804-9c79-4a8704b70b87"), event_id=2008, version=0)
class Microsoft_Windows_LanguagePackSetup_2008_0(Etw):
    pattern = Struct(
        "Language" / WString
    )


@declare(guid=guid("7237fff9-a08a-4804-9c79-4a8704b70b87"), event_id=2009, version=0)
class Microsoft_Windows_LanguagePackSetup_2009_0(Etw):
    pattern = Struct(
        "Language" / WString
    )


@declare(guid=guid("7237fff9-a08a-4804-9c79-4a8704b70b87"), event_id=2010, version=0)
class Microsoft_Windows_LanguagePackSetup_2010_0(Etw):
    pattern = Struct(
        "Language" / WString
    )


@declare(guid=guid("7237fff9-a08a-4804-9c79-4a8704b70b87"), event_id=2011, version=0)
class Microsoft_Windows_LanguagePackSetup_2011_0(Etw):
    pattern = Struct(
        "Language" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("7237fff9-a08a-4804-9c79-4a8704b70b87"), event_id=2012, version=0)
class Microsoft_Windows_LanguagePackSetup_2012_0(Etw):
    pattern = Struct(
        "Language1" / WString,
        "Language2" / WString
    )


@declare(guid=guid("7237fff9-a08a-4804-9c79-4a8704b70b87"), event_id=2013, version=0)
class Microsoft_Windows_LanguagePackSetup_2013_0(Etw):
    pattern = Struct(
        "Language1" / WString,
        "Language2" / WString
    )


@declare(guid=guid("7237fff9-a08a-4804-9c79-4a8704b70b87"), event_id=2014, version=0)
class Microsoft_Windows_LanguagePackSetup_2014_0(Etw):
    pattern = Struct(
        "Error" / Int32ul
    )


@declare(guid=guid("7237fff9-a08a-4804-9c79-4a8704b70b87"), event_id=2015, version=0)
class Microsoft_Windows_LanguagePackSetup_2015_0(Etw):
    pattern = Struct(
        "Language" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("7237fff9-a08a-4804-9c79-4a8704b70b87"), event_id=2016, version=0)
class Microsoft_Windows_LanguagePackSetup_2016_0(Etw):
    pattern = Struct(
        "Language" / WString,
        "Error" / Int32ul
    )


@declare(guid=guid("7237fff9-a08a-4804-9c79-4a8704b70b87"), event_id=3000, version=0)
class Microsoft_Windows_LanguagePackSetup_3000_0(Etw):
    pattern = Struct(
        "Language" / WString
    )


@declare(guid=guid("7237fff9-a08a-4804-9c79-4a8704b70b87"), event_id=3000, version=1)
class Microsoft_Windows_LanguagePackSetup_3000_1(Etw):
    pattern = Struct(
        "Language" / WString
    )


@declare(guid=guid("7237fff9-a08a-4804-9c79-4a8704b70b87"), event_id=3001, version=0)
class Microsoft_Windows_LanguagePackSetup_3001_0(Etw):
    pattern = Struct(
        "Language" / WString
    )


@declare(guid=guid("7237fff9-a08a-4804-9c79-4a8704b70b87"), event_id=3001, version=1)
class Microsoft_Windows_LanguagePackSetup_3001_1(Etw):
    pattern = Struct(
        "Language" / WString
    )


@declare(guid=guid("7237fff9-a08a-4804-9c79-4a8704b70b87"), event_id=3002, version=0)
class Microsoft_Windows_LanguagePackSetup_3002_0(Etw):
    pattern = Struct(
        "Language" / WString
    )


@declare(guid=guid("7237fff9-a08a-4804-9c79-4a8704b70b87"), event_id=4002, version=0)
class Microsoft_Windows_LanguagePackSetup_4002_0(Etw):
    pattern = Struct(
        "BootCount" / Int32ul
    )


@declare(guid=guid("7237fff9-a08a-4804-9c79-4a8704b70b87"), event_id=4003, version=0)
class Microsoft_Windows_LanguagePackSetup_4003_0(Etw):
    pattern = Struct(
        "BootCount" / Int32ul,
        "CurrentSessionRunCount" / Int32ul
    )


@declare(guid=guid("7237fff9-a08a-4804-9c79-4a8704b70b87"), event_id=4016, version=0)
class Microsoft_Windows_LanguagePackSetup_4016_0(Etw):
    pattern = Struct(
        "Language" / WString
    )


@declare(guid=guid("7237fff9-a08a-4804-9c79-4a8704b70b87"), event_id=5000, version=0)
class Microsoft_Windows_LanguagePackSetup_5000_0(Etw):
    pattern = Struct(
        "NewLanguage" / WString,
        "PreviousLanguage" / WString,
        "Flags" / Int32ul,
        "ReturnValue" / Int32ul
    )


@declare(guid=guid("7237fff9-a08a-4804-9c79-4a8704b70b87"), event_id=5001, version=0)
class Microsoft_Windows_LanguagePackSetup_5001_0(Etw):
    pattern = Struct(
        "NewLanguage" / WString,
        "PreviousLanguage" / WString,
        "Flags" / Int32ul,
        "ReturnValue" / Int32ul
    )


@declare(guid=guid("7237fff9-a08a-4804-9c79-4a8704b70b87"), event_id=5002, version=0)
class Microsoft_Windows_LanguagePackSetup_5002_0(Etw):
    pattern = Struct(
        "NewLanguage" / WString,
        "PreviousLanguage" / WString,
        "Flags" / Int32ul,
        "ReturnValue" / Int32ul
    )


@declare(guid=guid("7237fff9-a08a-4804-9c79-4a8704b70b87"), event_id=5003, version=0)
class Microsoft_Windows_LanguagePackSetup_5003_0(Etw):
    pattern = Struct(
        "NewLanguage" / WString,
        "PreviousLanguage" / WString,
        "Flags" / Int32ul,
        "ReturnValue" / Int32ul
    )


@declare(guid=guid("7237fff9-a08a-4804-9c79-4a8704b70b87"), event_id=5004, version=0)
class Microsoft_Windows_LanguagePackSetup_5004_0(Etw):
    pattern = Struct(
        "NewLanguage" / WString,
        "PreviousLanguage" / WString,
        "Flags" / Int32ul,
        "ReturnValue" / Int32ul
    )


@declare(guid=guid("7237fff9-a08a-4804-9c79-4a8704b70b87"), event_id=5005, version=0)
class Microsoft_Windows_LanguagePackSetup_5005_0(Etw):
    pattern = Struct(
        "CallbackAPIName" / WString,
        "ErrorStatus" / Int32ul
    )

