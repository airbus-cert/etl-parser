# -*- coding: utf-8 -*-
"""
Microsoft-Windows-WMPNSS-Service
GUID : 6a2dc7c1-930a-4fb5-bb44-80b30aebed6c
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=1001, version=0)
class Microsoft_Windows_WMPNSS_Service_1001_0(Etw):
    pattern = Struct(
        "ChangeCount" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=1002, version=0)
class Microsoft_Windows_WMPNSS_Service_1002_0(Etw):
    pattern = Struct(
        "ChangeCount" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=1003, version=0)
class Microsoft_Windows_WMPNSS_Service_1003_0(Etw):
    pattern = Struct(
        "ID" / WString,
        "Criteria" / WString,
        "StartIndex" / Int32ul,
        "RequestedCount" / Int32ul,
        "Filter" / WString,
        "SortCriteria" / WString,
        "ReturnedCount" / Int32ul,
        "TotalMatches" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=1004, version=0)
class Microsoft_Windows_WMPNSS_Service_1004_0(Etw):
    pattern = Struct(
        "ID" / WString,
        "Criteria" / WString,
        "StartIndex" / Int32ul,
        "RequestedCount" / Int32ul,
        "Filter" / WString,
        "SortCriteria" / WString,
        "ReturnedCount" / Int32ul,
        "TotalMatches" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=1007, version=0)
class Microsoft_Windows_WMPNSS_Service_1007_0(Etw):
    pattern = Struct(
        "PublishAllAlbumArts" / Int8ul,
        "FilterItemCount" / Int32ul,
        "SortItemCount" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=1008, version=0)
class Microsoft_Windows_WMPNSS_Service_1008_0(Etw):
    pattern = Struct(
        "PublishAllAlbumArts" / Int8ul,
        "FilterItemCount" / Int32ul,
        "SortItemCount" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=1011, version=0)
class Microsoft_Windows_WMPNSS_Service_1011_0(Etw):
    pattern = Struct(
        "WrittenCount" / Int32ul,
        "TotalResultLength" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=1012, version=0)
class Microsoft_Windows_WMPNSS_Service_1012_0(Etw):
    pattern = Struct(
        "WrittenCount" / Int32ul,
        "TotalResultLength" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=1015, version=0)
class Microsoft_Windows_WMPNSS_Service_1015_0(Etw):
    pattern = Struct(
        "ID" / WString,
        "Criteria" / WString,
        "StartIndex" / Int32ul,
        "RequestedCount" / Int32ul,
        "Filter" / WString,
        "SortCriteria" / WString,
        "ReturnedCount" / Int32ul,
        "TotalMatches" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=1016, version=0)
class Microsoft_Windows_WMPNSS_Service_1016_0(Etw):
    pattern = Struct(
        "ID" / WString,
        "Criteria" / WString,
        "StartIndex" / Int32ul,
        "RequestedCount" / Int32ul,
        "Filter" / WString,
        "SortCriteria" / WString,
        "ReturnedCount" / Int32ul,
        "TotalMatches" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=1019, version=0)
class Microsoft_Windows_WMPNSS_Service_1019_0(Etw):
    pattern = Struct(
        "PublishAllAlbumArts" / Int8ul,
        "FilterItemCount" / Int32ul,
        "SortItemCount" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=1020, version=0)
class Microsoft_Windows_WMPNSS_Service_1020_0(Etw):
    pattern = Struct(
        "PublishAllAlbumArts" / Int8ul,
        "FilterItemCount" / Int32ul,
        "SortItemCount" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=1023, version=0)
class Microsoft_Windows_WMPNSS_Service_1023_0(Etw):
    pattern = Struct(
        "WrittenCount" / Int32ul,
        "TotalResultLength" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=1024, version=0)
class Microsoft_Windows_WMPNSS_Service_1024_0(Etw):
    pattern = Struct(
        "WrittenCount" / Int32ul,
        "TotalResultLength" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=1027, version=0)
class Microsoft_Windows_WMPNSS_Service_1027_0(Etw):
    pattern = Struct(
        "PublishAllAlbumArts" / Int8ul,
        "Count" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=1028, version=0)
class Microsoft_Windows_WMPNSS_Service_1028_0(Etw):
    pattern = Struct(
        "PublishAllAlbumArts" / Int8ul,
        "Count" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=1029, version=0)
class Microsoft_Windows_WMPNSS_Service_1029_0(Etw):
    pattern = Struct(
        "Element" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=1030, version=0)
class Microsoft_Windows_WMPNSS_Service_1030_0(Etw):
    pattern = Struct(
        "Element" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=1031, version=0)
class Microsoft_Windows_WMPNSS_Service_1031_0(Etw):
    pattern = Struct(
        "ElementValue" / Int32ul,
        "Index" / Int32ul,
        "ElementExists" / Int8ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=1032, version=0)
class Microsoft_Windows_WMPNSS_Service_1032_0(Etw):
    pattern = Struct(
        "ElementValue" / Int32ul,
        "Index" / Int32ul,
        "ElementExists" / Int8ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=1033, version=0)
class Microsoft_Windows_WMPNSS_Service_1033_0(Etw):
    pattern = Struct(
        "CompatFlags" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=1034, version=0)
class Microsoft_Windows_WMPNSS_Service_1034_0(Etw):
    pattern = Struct(
        "CompatFlags" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=1035, version=0)
class Microsoft_Windows_WMPNSS_Service_1035_0(Etw):
    pattern = Struct(
        "CompatFlags" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=1036, version=0)
class Microsoft_Windows_WMPNSS_Service_1036_0(Etw):
    pattern = Struct(
        "CompatFlags" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=1037, version=0)
class Microsoft_Windows_WMPNSS_Service_1037_0(Etw):
    pattern = Struct(
        "Count" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=1038, version=0)
class Microsoft_Windows_WMPNSS_Service_1038_0(Etw):
    pattern = Struct(
        "Count" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=1039, version=0)
class Microsoft_Windows_WMPNSS_Service_1039_0(Etw):
    pattern = Struct(
        "Value" / Int32ul,
        "AttributesWritten" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=1040, version=0)
class Microsoft_Windows_WMPNSS_Service_1040_0(Etw):
    pattern = Struct(
        "Value" / Int32ul,
        "AttributesWritten" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=1041, version=0)
class Microsoft_Windows_WMPNSS_Service_1041_0(Etw):
    pattern = Struct(
        "ElementValue" / Int32ul,
        "Index" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=1042, version=0)
class Microsoft_Windows_WMPNSS_Service_1042_0(Etw):
    pattern = Struct(
        "ElementValue" / Int32ul,
        "Index" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=1043, version=0)
class Microsoft_Windows_WMPNSS_Service_1043_0(Etw):
    pattern = Struct(
        "ElementValue" / Int32ul,
        "Index" / Int32ul,
        "AttributeValue" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=1044, version=0)
class Microsoft_Windows_WMPNSS_Service_1044_0(Etw):
    pattern = Struct(
        "ElementValue" / Int32ul,
        "Index" / Int32ul,
        "AttributeValue" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=1045, version=0)
class Microsoft_Windows_WMPNSS_Service_1045_0(Etw):
    pattern = Struct(
        "ElementValue" / Int32ul,
        "Index" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=1046, version=0)
class Microsoft_Windows_WMPNSS_Service_1046_0(Etw):
    pattern = Struct(
        "ElementValue" / Int32ul,
        "Index" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=1047, version=0)
class Microsoft_Windows_WMPNSS_Service_1047_0(Etw):
    pattern = Struct(
        "ElementValue" / Int32ul,
        "IsSelected" / Int8ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=1048, version=0)
class Microsoft_Windows_WMPNSS_Service_1048_0(Etw):
    pattern = Struct(
        "ElementValue" / Int32ul,
        "IsSelected" / Int8ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=1049, version=0)
class Microsoft_Windows_WMPNSS_Service_1049_0(Etw):
    pattern = Struct(
        "Value" / Int32ul,
        "AttributesWritten" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=1050, version=0)
class Microsoft_Windows_WMPNSS_Service_1050_0(Etw):
    pattern = Struct(
        "Value" / Int32ul,
        "AttributesWritten" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=1051, version=0)
class Microsoft_Windows_WMPNSS_Service_1051_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=1052, version=0)
class Microsoft_Windows_WMPNSS_Service_1052_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=1053, version=0)
class Microsoft_Windows_WMPNSS_Service_1053_0(Etw):
    pattern = Struct(
        "ID" / WString,
        "CurrentTagValue" / WString,
        "NewTagValue" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=1054, version=0)
class Microsoft_Windows_WMPNSS_Service_1054_0(Etw):
    pattern = Struct(
        "ID" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=2001, version=0)
class Microsoft_Windows_WMPNSS_Service_2001_0(Etw):
    pattern = Struct(
        "IsDeviceGiven" / Int8ul,
        "IsDeviceAuthorized" / Int8ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=2002, version=0)
class Microsoft_Windows_WMPNSS_Service_2002_0(Etw):
    pattern = Struct(
        "IsDeviceGiven" / Int8ul,
        "IsDeviceAuthorized" / Int8ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=2005, version=0)
class Microsoft_Windows_WMPNSS_Service_2005_0(Etw):
    pattern = Struct(
        "IsDeviceGiven" / Int8ul,
        "IsDeviceValidated" / Int8ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=2006, version=0)
class Microsoft_Windows_WMPNSS_Service_2006_0(Etw):
    pattern = Struct(
        "IsDeviceGiven" / Int8ul,
        "IsDeviceValidated" / Int8ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=2007, version=0)
class Microsoft_Windows_WMPNSS_Service_2007_0(Etw):
    pattern = Struct(
        "IsAllowed" / Int8ul,
        "IsValidated" / Int8ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=2008, version=0)
class Microsoft_Windows_WMPNSS_Service_2008_0(Etw):
    pattern = Struct(
        "IsAllowed" / Int8ul,
        "IsValidated" / Int8ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=2009, version=0)
class Microsoft_Windows_WMPNSS_Service_2009_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=2010, version=0)
class Microsoft_Windows_WMPNSS_Service_2010_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=2011, version=0)
class Microsoft_Windows_WMPNSS_Service_2011_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=2012, version=0)
class Microsoft_Windows_WMPNSS_Service_2012_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=2013, version=0)
class Microsoft_Windows_WMPNSS_Service_2013_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=2014, version=0)
class Microsoft_Windows_WMPNSS_Service_2014_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=2015, version=0)
class Microsoft_Windows_WMPNSS_Service_2015_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=2016, version=0)
class Microsoft_Windows_WMPNSS_Service_2016_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=2017, version=0)
class Microsoft_Windows_WMPNSS_Service_2017_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=2018, version=0)
class Microsoft_Windows_WMPNSS_Service_2018_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=3001, version=0)
class Microsoft_Windows_WMPNSS_Service_3001_0(Etw):
    pattern = Struct(
        "ElementCount" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=3002, version=0)
class Microsoft_Windows_WMPNSS_Service_3002_0(Etw):
    pattern = Struct(
        "ElementCount" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=3003, version=0)
class Microsoft_Windows_WMPNSS_Service_3003_0(Etw):
    pattern = Struct(
        "ElementCount" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=3004, version=0)
class Microsoft_Windows_WMPNSS_Service_3004_0(Etw):
    pattern = Struct(
        "ElementCount" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=3005, version=0)
class Microsoft_Windows_WMPNSS_Service_3005_0(Etw):
    pattern = Struct(
        "ElementCount" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=3006, version=0)
class Microsoft_Windows_WMPNSS_Service_3006_0(Etw):
    pattern = Struct(
        "ElementCount" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=3007, version=0)
class Microsoft_Windows_WMPNSS_Service_3007_0(Etw):
    pattern = Struct(
        "ElementCount" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=3008, version=0)
class Microsoft_Windows_WMPNSS_Service_3008_0(Etw):
    pattern = Struct(
        "ElementCount" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=3009, version=0)
class Microsoft_Windows_WMPNSS_Service_3009_0(Etw):
    pattern = Struct(
        "NetEvent" / Int64ul,
        "Callback" / Int64ul,
        "State" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=3010, version=0)
class Microsoft_Windows_WMPNSS_Service_3010_0(Etw):
    pattern = Struct(
        "NetEvent" / Int64ul,
        "Callback" / Int64ul,
        "State" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=3011, version=0)
class Microsoft_Windows_WMPNSS_Service_3011_0(Etw):
    pattern = Struct(
        "Address" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=3012, version=0)
class Microsoft_Windows_WMPNSS_Service_3012_0(Etw):
    pattern = Struct(
        "Address" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=3013, version=0)
class Microsoft_Windows_WMPNSS_Service_3013_0(Etw):
    pattern = Struct(
        "NetEvent" / Int64ul,
        "Callback" / Int64ul,
        "State" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=3014, version=0)
class Microsoft_Windows_WMPNSS_Service_3014_0(Etw):
    pattern = Struct(
        "NetEvent" / Int64ul,
        "Callback" / Int64ul,
        "State" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=3015, version=0)
class Microsoft_Windows_WMPNSS_Service_3015_0(Etw):
    pattern = Struct(
        "Address" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=3016, version=0)
class Microsoft_Windows_WMPNSS_Service_3016_0(Etw):
    pattern = Struct(
        "Address" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=3017, version=0)
class Microsoft_Windows_WMPNSS_Service_3017_0(Etw):
    pattern = Struct(
        "NetEvent" / Int64ul,
        "Callback" / Int64ul,
        "State" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=3018, version=0)
class Microsoft_Windows_WMPNSS_Service_3018_0(Etw):
    pattern = Struct(
        "NetEvent" / Int64ul,
        "Callback" / Int64ul,
        "State" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=3019, version=0)
class Microsoft_Windows_WMPNSS_Service_3019_0(Etw):
    pattern = Struct(
        "Address" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=3020, version=0)
class Microsoft_Windows_WMPNSS_Service_3020_0(Etw):
    pattern = Struct(
        "Address" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=3021, version=0)
class Microsoft_Windows_WMPNSS_Service_3021_0(Etw):
    pattern = Struct(
        "NetEvent" / Int64ul,
        "Callback" / Int64ul,
        "State" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=3022, version=0)
class Microsoft_Windows_WMPNSS_Service_3022_0(Etw):
    pattern = Struct(
        "NetEvent" / Int64ul,
        "Callback" / Int64ul,
        "State" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=3023, version=0)
class Microsoft_Windows_WMPNSS_Service_3023_0(Etw):
    pattern = Struct(
        "Address" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=3024, version=0)
class Microsoft_Windows_WMPNSS_Service_3024_0(Etw):
    pattern = Struct(
        "Address" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=3025, version=0)
class Microsoft_Windows_WMPNSS_Service_3025_0(Etw):
    pattern = Struct(
        "IsAlbumArt" / Int8ul,
        "IsStream" / Int8ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=3026, version=0)
class Microsoft_Windows_WMPNSS_Service_3026_0(Etw):
    pattern = Struct(
        "IsAlbumArt" / Int8ul,
        "IsStream" / Int8ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=3027, version=0)
class Microsoft_Windows_WMPNSS_Service_3027_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=3028, version=0)
class Microsoft_Windows_WMPNSS_Service_3028_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=3029, version=0)
class Microsoft_Windows_WMPNSS_Service_3029_0(Etw):
    pattern = Struct(
        "IsAlbumArt" / Int8ul,
        "IsTranscode" / Int8ul,
        "FormatID" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=3030, version=0)
class Microsoft_Windows_WMPNSS_Service_3030_0(Etw):
    pattern = Struct(
        "IsAlbumArt" / Int8ul,
        "IsTranscode" / Int8ul,
        "FormatID" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=3031, version=0)
class Microsoft_Windows_WMPNSS_Service_3031_0(Etw):
    pattern = Struct(
        "NetEvent" / Int64ul,
        "Callback" / Int64ul,
        "State" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=3032, version=0)
class Microsoft_Windows_WMPNSS_Service_3032_0(Etw):
    pattern = Struct(
        "NetEvent" / Int64ul,
        "Callback" / Int64ul,
        "State" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=3033, version=0)
class Microsoft_Windows_WMPNSS_Service_3033_0(Etw):
    pattern = Struct(
        "Address" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=3034, version=0)
class Microsoft_Windows_WMPNSS_Service_3034_0(Etw):
    pattern = Struct(
        "Address" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=3035, version=0)
class Microsoft_Windows_WMPNSS_Service_3035_0(Etw):
    pattern = Struct(
        "ID" / Int64ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=4001, version=0)
class Microsoft_Windows_WMPNSS_Service_4001_0(Etw):
    pattern = Struct(
        "ContainerID" / WString,
        "Sort" / WString,
        "OnlyItemsInSearchResults" / Int8ul,
        "SortItemCount" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=4002, version=0)
class Microsoft_Windows_WMPNSS_Service_4002_0(Etw):
    pattern = Struct(
        "ContainerID" / WString,
        "Sort" / WString,
        "OnlyItemsInSearchResults" / Int8ul,
        "SortItemCount" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=4003, version=0)
class Microsoft_Windows_WMPNSS_Service_4003_0(Etw):
    pattern = Struct(
        "ContainerID" / WString,
        "UPnPClassToReturn" / WString,
        "Query" / WString,
        "OnlyItemsInSearchResults" / Int8ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=4004, version=0)
class Microsoft_Windows_WMPNSS_Service_4004_0(Etw):
    pattern = Struct(
        "ContainerID" / WString,
        "UPnPClassToReturn" / WString,
        "Query" / WString,
        "OnlyItemsInSearchResults" / Int8ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=4005, version=0)
class Microsoft_Windows_WMPNSS_Service_4005_0(Etw):
    pattern = Struct(
        "ClassName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=4006, version=0)
class Microsoft_Windows_WMPNSS_Service_4006_0(Etw):
    pattern = Struct(
        "ClassName" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=4007, version=0)
class Microsoft_Windows_WMPNSS_Service_4007_0(Etw):
    pattern = Struct(
        "TotalRetry" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=4008, version=0)
class Microsoft_Windows_WMPNSS_Service_4008_0(Etw):
    pattern = Struct(
        "TotalRetry" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=4009, version=0)
class Microsoft_Windows_WMPNSS_Service_4009_0(Etw):
    pattern = Struct(
        "ContainerID" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=4010, version=0)
class Microsoft_Windows_WMPNSS_Service_4010_0(Etw):
    pattern = Struct(
        "ContainerID" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=4011, version=0)
class Microsoft_Windows_WMPNSS_Service_4011_0(Etw):
    pattern = Struct(
        "ContainerID" / WString,
        "RefID" / WString,
        "StartIndex" / Int32ul,
        "RequestedCount" / Int32ul,
        "TotalMatches" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=4012, version=0)
class Microsoft_Windows_WMPNSS_Service_4012_0(Etw):
    pattern = Struct(
        "ContainerID" / WString,
        "RefID" / WString,
        "StartIndex" / Int32ul,
        "RequestedCount" / Int32ul,
        "TotalMatches" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=4013, version=0)
class Microsoft_Windows_WMPNSS_Service_4013_0(Etw):
    pattern = Struct(
        "ContainerID" / WString,
        "StartIndex" / Int32ul,
        "RequestedCount" / Int32ul,
        "SortItemCount" / Int32ul,
        "TotalMatches" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=4014, version=0)
class Microsoft_Windows_WMPNSS_Service_4014_0(Etw):
    pattern = Struct(
        "ContainerID" / WString,
        "StartIndex" / Int32ul,
        "RequestedCount" / Int32ul,
        "SortItemCount" / Int32ul,
        "TotalMatches" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=4015, version=0)
class Microsoft_Windows_WMPNSS_Service_4015_0(Etw):
    pattern = Struct(
        "ContainerID" / WString,
        "ItemsOnly" / Int8ul,
        "StartIndex" / Int32ul,
        "RequestedCount" / Int32ul,
        "SortItemCount" / Int32ul,
        "TotalMatches" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=4016, version=0)
class Microsoft_Windows_WMPNSS_Service_4016_0(Etw):
    pattern = Struct(
        "ContainerID" / WString,
        "ItemsOnly" / Int8ul,
        "StartIndex" / Int32ul,
        "RequestedCount" / Int32ul,
        "SortItemCount" / Int32ul,
        "TotalMatches" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=4017, version=0)
class Microsoft_Windows_WMPNSS_Service_4017_0(Etw):
    pattern = Struct(
        "Count" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=4018, version=0)
class Microsoft_Windows_WMPNSS_Service_4018_0(Etw):
    pattern = Struct(
        "Count" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=4019, version=0)
class Microsoft_Windows_WMPNSS_Service_4019_0(Etw):
    pattern = Struct(
        "Index" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=4020, version=0)
class Microsoft_Windows_WMPNSS_Service_4020_0(Etw):
    pattern = Struct(
        "Index" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=4021, version=0)
class Microsoft_Windows_WMPNSS_Service_4021_0(Etw):
    pattern = Struct(
        "BrowseIndex" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=4022, version=0)
class Microsoft_Windows_WMPNSS_Service_4022_0(Etw):
    pattern = Struct(
        "BrowseIndex" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=4023, version=0)
class Microsoft_Windows_WMPNSS_Service_4023_0(Etw):
    pattern = Struct(
        "StartingIndex" / Int32ul,
        "RequestedCount" / Int32ul,
        "SortItemCount" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=4024, version=0)
class Microsoft_Windows_WMPNSS_Service_4024_0(Etw):
    pattern = Struct(
        "StartingIndex" / Int32ul,
        "RequestedCount" / Int32ul,
        "SortItemCount" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=4025, version=0)
class Microsoft_Windows_WMPNSS_Service_4025_0(Etw):
    pattern = Struct(
        "BrowseChildren" / Int8ul,
        "BrowseIndex" / Int32ul,
        "RequestedCount" / Int32ul,
        "SortItemCount" / Int32ul,
        "ItemCount" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=4026, version=0)
class Microsoft_Windows_WMPNSS_Service_4026_0(Etw):
    pattern = Struct(
        "BrowseChildren" / Int8ul,
        "BrowseIndex" / Int32ul,
        "RequestedCount" / Int32ul,
        "SortItemCount" / Int32ul,
        "ItemCount" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=4027, version=0)
class Microsoft_Windows_WMPNSS_Service_4027_0(Etw):
    pattern = Struct(
        "SortItemCount" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=4028, version=0)
class Microsoft_Windows_WMPNSS_Service_4028_0(Etw):
    pattern = Struct(
        "SortItemCount" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=4029, version=0)
class Microsoft_Windows_WMPNSS_Service_4029_0(Etw):
    pattern = Struct(
        "ElementValue" / Int32ul,
        "Index" / Int32ul,
        "AttributeValue" / Int32ul,
        "MaxLength" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=4030, version=0)
class Microsoft_Windows_WMPNSS_Service_4030_0(Etw):
    pattern = Struct(
        "ElementValue" / Int32ul,
        "Index" / Int32ul,
        "AttributeValue" / Int32ul,
        "MaxLength" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=4031, version=0)
class Microsoft_Windows_WMPNSS_Service_4031_0(Etw):
    pattern = Struct(
        "ElementValue" / Int32ul,
        "Index" / Int32ul,
        "AttributeValue" / Int32ul,
        "MaxLength" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=4032, version=0)
class Microsoft_Windows_WMPNSS_Service_4032_0(Etw):
    pattern = Struct(
        "ElementValue" / Int32ul,
        "Index" / Int32ul,
        "AttributeValue" / Int32ul,
        "MaxLength" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=4033, version=0)
class Microsoft_Windows_WMPNSS_Service_4033_0(Etw):
    pattern = Struct(
        "RemoteMACAddress" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=4034, version=0)
class Microsoft_Windows_WMPNSS_Service_4034_0(Etw):
    pattern = Struct(
        "ElementValue" / Int32ul,
        "Index" / Int32ul,
        "AttributeValue" / Int32ul,
        "MaxLength" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=4035, version=0)
class Microsoft_Windows_WMPNSS_Service_4035_0(Etw):
    pattern = Struct(
        "ElementValue" / Int32ul,
        "Index" / Int32ul,
        "AttributeValue" / Int32ul,
        "MaxLength" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=4036, version=0)
class Microsoft_Windows_WMPNSS_Service_4036_0(Etw):
    pattern = Struct(
        "Index" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=4037, version=0)
class Microsoft_Windows_WMPNSS_Service_4037_0(Etw):
    pattern = Struct(
        "Index" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=4038, version=0)
class Microsoft_Windows_WMPNSS_Service_4038_0(Etw):
    pattern = Struct(
        "CountAdded" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=4039, version=0)
class Microsoft_Windows_WMPNSS_Service_4039_0(Etw):
    pattern = Struct(
        "CountAdded" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=4040, version=0)
class Microsoft_Windows_WMPNSS_Service_4040_0(Etw):
    pattern = Struct(
        "ElementValue" / Int32ul,
        "Index" / Int32ul,
        "AttributeValue" / Int32ul,
        "MaxLength" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=4041, version=0)
class Microsoft_Windows_WMPNSS_Service_4041_0(Etw):
    pattern = Struct(
        "ElementValue" / Int32ul,
        "Index" / Int32ul,
        "AttributeValue" / Int32ul,
        "MaxLength" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=4042, version=0)
class Microsoft_Windows_WMPNSS_Service_4042_0(Etw):
    pattern = Struct(
        "CountAdded" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=4043, version=0)
class Microsoft_Windows_WMPNSS_Service_4043_0(Etw):
    pattern = Struct(
        "CountAdded" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=4044, version=0)
class Microsoft_Windows_WMPNSS_Service_4044_0(Etw):
    pattern = Struct(
        "ElementValue" / Int32ul,
        "Index" / Int32ul,
        "AttributeValue" / Int32ul,
        "MaxLength" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=4045, version=0)
class Microsoft_Windows_WMPNSS_Service_4045_0(Etw):
    pattern = Struct(
        "ElementValue" / Int32ul,
        "Index" / Int32ul,
        "AttributeValue" / Int32ul,
        "MaxLength" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=4046, version=0)
class Microsoft_Windows_WMPNSS_Service_4046_0(Etw):
    pattern = Struct(
        "ElementValue" / Int32ul,
        "Index" / Int32ul,
        "AttributeValue" / Int32ul,
        "MaxLength" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=4047, version=0)
class Microsoft_Windows_WMPNSS_Service_4047_0(Etw):
    pattern = Struct(
        "ElementValue" / Int32ul,
        "Index" / Int32ul,
        "AttributeValue" / Int32ul,
        "MaxLength" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=4048, version=0)
class Microsoft_Windows_WMPNSS_Service_4048_0(Etw):
    pattern = Struct(
        "WMPAtom" / Int32ul,
        "ReturnedCount" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=4049, version=0)
class Microsoft_Windows_WMPNSS_Service_4049_0(Etw):
    pattern = Struct(
        "WMPAtom" / Int32ul,
        "ReturnedCount" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=4050, version=0)
class Microsoft_Windows_WMPNSS_Service_4050_0(Etw):
    pattern = Struct(
        "OnlyItemsInSearchResults" / Int8ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=4051, version=0)
class Microsoft_Windows_WMPNSS_Service_4051_0(Etw):
    pattern = Struct(
        "OnlyItemsInSearchResults" / Int8ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=4052, version=0)
class Microsoft_Windows_WMPNSS_Service_4052_0(Etw):
    pattern = Struct(
        "WMPAtom" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=4053, version=0)
class Microsoft_Windows_WMPNSS_Service_4053_0(Etw):
    pattern = Struct(
        "WMPAtom" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=4054, version=0)
class Microsoft_Windows_WMPNSS_Service_4054_0(Etw):
    pattern = Struct(
        "Index" / Int32ul,
        "WMPAtom" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=4055, version=0)
class Microsoft_Windows_WMPNSS_Service_4055_0(Etw):
    pattern = Struct(
        "Index" / Int32ul,
        "WMPAtom" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=4056, version=0)
class Microsoft_Windows_WMPNSS_Service_4056_0(Etw):
    pattern = Struct(
        "Address" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=4057, version=0)
class Microsoft_Windows_WMPNSS_Service_4057_0(Etw):
    pattern = Struct(
        "Address" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=4058, version=0)
class Microsoft_Windows_WMPNSS_Service_4058_0(Etw):
    pattern = Struct(
        "Address" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=4059, version=0)
class Microsoft_Windows_WMPNSS_Service_4059_0(Etw):
    pattern = Struct(
        "Address" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=4060, version=0)
class Microsoft_Windows_WMPNSS_Service_4060_0(Etw):
    pattern = Struct(
        "Address" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=4061, version=0)
class Microsoft_Windows_WMPNSS_Service_4061_0(Etw):
    pattern = Struct(
        "Address" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=4062, version=0)
class Microsoft_Windows_WMPNSS_Service_4062_0(Etw):
    pattern = Struct(
        "ID" / WString,
        "BrowseType" / Int32ul,
        "StartIndex" / Int32ul,
        "RequestedCount" / Int32ul,
        "FilterItemCount" / Int32ul,
        "SortItemCount" / Int32ul,
        "TotalMatches" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=4063, version=0)
class Microsoft_Windows_WMPNSS_Service_4063_0(Etw):
    pattern = Struct(
        "ID" / WString,
        "BrowseType" / Int32ul,
        "StartIndex" / Int32ul,
        "RequestedCount" / Int32ul,
        "FilterItemCount" / Int32ul,
        "SortItemCount" / Int32ul,
        "TotalMatches" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=4064, version=0)
class Microsoft_Windows_WMPNSS_Service_4064_0(Etw):
    pattern = Struct(
        "RemoteMACAddress" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=4065, version=0)
class Microsoft_Windows_WMPNSS_Service_4065_0(Etw):
    pattern = Struct(
        "ID" / WString,
        "Query" / WString,
        "StartIndex" / Int32ul,
        "RequestedCount" / Int32ul,
        "FilterItemCount" / Int32ul,
        "SortItemCount" / Int32ul,
        "TotalMatches" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=4066, version=0)
class Microsoft_Windows_WMPNSS_Service_4066_0(Etw):
    pattern = Struct(
        "ID" / WString,
        "Query" / WString,
        "StartIndex" / Int32ul,
        "RequestedCount" / Int32ul,
        "FilterItemCount" / Int32ul,
        "SortItemCount" / Int32ul,
        "TotalMatches" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=5001, version=0)
class Microsoft_Windows_WMPNSS_Service_5001_0(Etw):
    pattern = Struct(
        "Address" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=5002, version=0)
class Microsoft_Windows_WMPNSS_Service_5002_0(Etw):
    pattern = Struct(
        "Address" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=5003, version=0)
class Microsoft_Windows_WMPNSS_Service_5003_0(Etw):
    pattern = Struct(
        "Address" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=5004, version=0)
class Microsoft_Windows_WMPNSS_Service_5004_0(Etw):
    pattern = Struct(
        "Address" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=5005, version=0)
class Microsoft_Windows_WMPNSS_Service_5005_0(Etw):
    pattern = Struct(
        "Address" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=5006, version=0)
class Microsoft_Windows_WMPNSS_Service_5006_0(Etw):
    pattern = Struct(
        "Address" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=5007, version=0)
class Microsoft_Windows_WMPNSS_Service_5007_0(Etw):
    pattern = Struct(
        "Address" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=5008, version=0)
class Microsoft_Windows_WMPNSS_Service_5008_0(Etw):
    pattern = Struct(
        "Address" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=5009, version=0)
class Microsoft_Windows_WMPNSS_Service_5009_0(Etw):
    pattern = Struct(
        "Count" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=5010, version=0)
class Microsoft_Windows_WMPNSS_Service_5010_0(Etw):
    pattern = Struct(
        "Count" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=5011, version=0)
class Microsoft_Windows_WMPNSS_Service_5011_0(Etw):
    pattern = Struct(
        "Count" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=5012, version=0)
class Microsoft_Windows_WMPNSS_Service_5012_0(Etw):
    pattern = Struct(
        "Count" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=5013, version=0)
class Microsoft_Windows_WMPNSS_Service_5013_0(Etw):
    pattern = Struct(
        "Count" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=5014, version=0)
class Microsoft_Windows_WMPNSS_Service_5014_0(Etw):
    pattern = Struct(
        "Count" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=5015, version=0)
class Microsoft_Windows_WMPNSS_Service_5015_0(Etw):
    pattern = Struct(
        "Count" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=5016, version=0)
class Microsoft_Windows_WMPNSS_Service_5016_0(Etw):
    pattern = Struct(
        "Count" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=5017, version=0)
class Microsoft_Windows_WMPNSS_Service_5017_0(Etw):
    pattern = Struct(
        "RequestsOutstanding" / Int32ul,
        "TimeContentRequestsBecameZero" / Int64ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=5020, version=0)
class Microsoft_Windows_WMPNSS_Service_5020_0(Etw):
    pattern = Struct(
        "DeviceType" / Int32ul,
        "DevicesRemoved" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=5021, version=0)
class Microsoft_Windows_WMPNSS_Service_5021_0(Etw):
    pattern = Struct(
        "DeviceType" / Int32ul,
        "DevicesRemoved" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=5022, version=0)
class Microsoft_Windows_WMPNSS_Service_5022_0(Etw):
    pattern = Struct(
        "KeepAwake" / Int8ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=5023, version=0)
class Microsoft_Windows_WMPNSS_Service_5023_0(Etw):
    pattern = Struct(
        "KeepAwake" / Int8ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=5024, version=0)
class Microsoft_Windows_WMPNSS_Service_5024_0(Etw):
    pattern = Struct(
        "IdleSecondsUntilMemoryFlush" / Int32ul,
        "TimeContentRequestsBecameZero" / Int64ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=5025, version=0)
class Microsoft_Windows_WMPNSS_Service_5025_0(Etw):
    pattern = Struct(
        "IdleSecondsUntilMemoryFlush" / Int32ul,
        "TimeContentRequestsBecameZero" / Int64ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=6001, version=0)
class Microsoft_Windows_WMPNSS_Service_6001_0(Etw):
    pattern = Struct(
        "MACAddress" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=6002, version=0)
class Microsoft_Windows_WMPNSS_Service_6002_0(Etw):
    pattern = Struct(
        "MACAddress" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=6003, version=0)
class Microsoft_Windows_WMPNSS_Service_6003_0(Etw):
    pattern = Struct(
        "Address" / Int64ul,
        "MACAddress" / WString,
        "SockAddr" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=6004, version=0)
class Microsoft_Windows_WMPNSS_Service_6004_0(Etw):
    pattern = Struct(
        "Address" / Int64ul,
        "MACAddress" / WString,
        "SockAddr" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=6005, version=0)
class Microsoft_Windows_WMPNSS_Service_6005_0(Etw):
    pattern = Struct(
        "Address" / Int64ul,
        "MACAddress" / WString,
        "SockAddr" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=6006, version=0)
class Microsoft_Windows_WMPNSS_Service_6006_0(Etw):
    pattern = Struct(
        "Address" / Int64ul,
        "MACAddress" / WString,
        "SockAddr" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=6007, version=0)
class Microsoft_Windows_WMPNSS_Service_6007_0(Etw):
    pattern = Struct(
        "Address" / Int64ul,
        "MACAddress" / WString,
        "SockAddr" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=6008, version=0)
class Microsoft_Windows_WMPNSS_Service_6008_0(Etw):
    pattern = Struct(
        "Address" / Int64ul,
        "MACAddress" / WString,
        "SockAddr" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=6009, version=0)
class Microsoft_Windows_WMPNSS_Service_6009_0(Etw):
    pattern = Struct(
        "Address" / Int64ul,
        "MACAddress" / WString,
        "SockAddr" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=6010, version=0)
class Microsoft_Windows_WMPNSS_Service_6010_0(Etw):
    pattern = Struct(
        "Address" / Int64ul,
        "MACAddress" / WString,
        "SockAddr" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=6011, version=0)
class Microsoft_Windows_WMPNSS_Service_6011_0(Etw):
    pattern = Struct(
        "Address" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=6012, version=0)
class Microsoft_Windows_WMPNSS_Service_6012_0(Etw):
    pattern = Struct(
        "Address" / Int64ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=6013, version=0)
class Microsoft_Windows_WMPNSS_Service_6013_0(Etw):
    pattern = Struct(
        "Address" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=6101, version=0)
class Microsoft_Windows_WMPNSS_Service_6101_0(Etw):
    pattern = Struct(
        "ServerOrRenderer" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=6102, version=0)
class Microsoft_Windows_WMPNSS_Service_6102_0(Etw):
    pattern = Struct(
        "ServerOrRenderer" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=6103, version=0)
class Microsoft_Windows_WMPNSS_Service_6103_0(Etw):
    pattern = Struct(
        "ServerOrRenderer" / Int32ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=6104, version=0)
class Microsoft_Windows_WMPNSS_Service_6104_0(Etw):
    pattern = Struct(
        "ServerOrRenderer" / Int32ul,
        "IUPnPDevice" / Int64ul,
        "NetworkGUID" / Guid
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=6105, version=0)
class Microsoft_Windows_WMPNSS_Service_6105_0(Etw):
    pattern = Struct(
        "ServerOrRenderer" / Int32ul,
        "IUPnPDevice" / Int64ul,
        "UDN" / WString,
        "FriendlyName" / WString,
        "IsFunctionalDMR" / Int8ul,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=6106, version=0)
class Microsoft_Windows_WMPNSS_Service_6106_0(Etw):
    pattern = Struct(
        "TotalDevicesAdded" / Int32ul,
        "DeviceFunctionalCount" / Int32ul,
        "TotalUDNRenderersAdded" / Int32ul,
        "UDNRenderersFunctionalCount" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=6107, version=0)
class Microsoft_Windows_WMPNSS_Service_6107_0(Etw):
    pattern = Struct(
        "ServerOrRenderer" / Int32ul,
        "UDN" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=6108, version=0)
class Microsoft_Windows_WMPNSS_Service_6108_0(Etw):
    pattern = Struct(
        "ServerOrRenderer" / Int32ul,
        "UDN" / WString,
        "ErrorCode" / Int32ul,
        "FailureReason" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=6109, version=0)
class Microsoft_Windows_WMPNSS_Service_6109_0(Etw):
    pattern = Struct(
        "IUPnPDevice" / Int64ul,
        "HasAVTransport" / Int8ul,
        "HasRenderingControl" / Int8ul,
        "HasConnectionManager" / Int8ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=6110, version=0)
class Microsoft_Windows_WMPNSS_Service_6110_0(Etw):
    pattern = Struct(
        "RMEClientID" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=6111, version=0)
class Microsoft_Windows_WMPNSS_Service_6111_0(Etw):
    pattern = Struct(
        "RMEClientID" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=6112, version=0)
class Microsoft_Windows_WMPNSS_Service_6112_0(Etw):
    pattern = Struct(
        "RMEClientID" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=6113, version=0)
class Microsoft_Windows_WMPNSS_Service_6113_0(Etw):
    pattern = Struct(
        "RMEClientID" / WString,
        "ErrorCode" / Int32ul
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=14100, version=0)
class Microsoft_Windows_WMPNSS_Service_14100_0(Etw):
    pattern = Struct(
        "ErrorCode" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=14101, version=0)
class Microsoft_Windows_WMPNSS_Service_14101_0(Etw):
    pattern = Struct(
        "ErrorCode" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=14102, version=0)
class Microsoft_Windows_WMPNSS_Service_14102_0(Etw):
    pattern = Struct(
        "ServiceName" / WString,
        "ErrorCode" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=14103, version=0)
class Microsoft_Windows_WMPNSS_Service_14103_0(Etw):
    pattern = Struct(
        "ServiceName" / WString,
        "ErrorCode" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=14104, version=0)
class Microsoft_Windows_WMPNSS_Service_14104_0(Etw):
    pattern = Struct(
        "URI" / WString,
        "IPAddress" / WString,
        "ErrorCode" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=14200, version=0)
class Microsoft_Windows_WMPNSS_Service_14200_0(Etw):
    pattern = Struct(
        "ServiceName" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=14201, version=0)
class Microsoft_Windows_WMPNSS_Service_14201_0(Etw):
    pattern = Struct(
        "ServiceName" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=14202, version=0)
class Microsoft_Windows_WMPNSS_Service_14202_0(Etw):
    pattern = Struct(
        "ServiceName" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=14203, version=0)
class Microsoft_Windows_WMPNSS_Service_14203_0(Etw):
    pattern = Struct(
        "ServiceName" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=14204, version=0)
class Microsoft_Windows_WMPNSS_Service_14204_0(Etw):
    pattern = Struct(
        "ServiceName" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=14205, version=0)
class Microsoft_Windows_WMPNSS_Service_14205_0(Etw):
    pattern = Struct(
        "ServiceName" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=14206, version=0)
class Microsoft_Windows_WMPNSS_Service_14206_0(Etw):
    pattern = Struct(
        "FriendlyName" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=14207, version=0)
class Microsoft_Windows_WMPNSS_Service_14207_0(Etw):
    pattern = Struct(
        "FriendlyName" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=14210, version=0)
class Microsoft_Windows_WMPNSS_Service_14210_0(Etw):
    pattern = Struct(
        "FriendlyName" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=14300, version=0)
class Microsoft_Windows_WMPNSS_Service_14300_0(Etw):
    pattern = Struct(
        "ServiceName" / WString,
        "ErrorCode" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=14301, version=0)
class Microsoft_Windows_WMPNSS_Service_14301_0(Etw):
    pattern = Struct(
        "ServiceName" / WString,
        "ErrorCode" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=14302, version=0)
class Microsoft_Windows_WMPNSS_Service_14302_0(Etw):
    pattern = Struct(
        "ServiceName" / WString,
        "ErrorCode" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=14303, version=0)
class Microsoft_Windows_WMPNSS_Service_14303_0(Etw):
    pattern = Struct(
        "ServiceName" / WString,
        "ErrorCode" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=14304, version=0)
class Microsoft_Windows_WMPNSS_Service_14304_0(Etw):
    pattern = Struct(
        "ServiceName" / WString,
        "ErrorCode1" / WString,
        "ErrorCode2" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=14305, version=0)
class Microsoft_Windows_WMPNSS_Service_14305_0(Etw):
    pattern = Struct(
        "ServiceName" / WString,
        "ErrorCode1" / WString,
        "ErrorCode2" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=14306, version=0)
class Microsoft_Windows_WMPNSS_Service_14306_0(Etw):
    pattern = Struct(
        "ServiceName" / WString,
        "ErrorCode1" / WString,
        "ErrorCode2" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=14307, version=0)
class Microsoft_Windows_WMPNSS_Service_14307_0(Etw):
    pattern = Struct(
        "ServiceName" / WString,
        "ErrorCode" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=14308, version=0)
class Microsoft_Windows_WMPNSS_Service_14308_0(Etw):
    pattern = Struct(
        "ServiceName" / WString,
        "ErrorCode" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=14309, version=0)
class Microsoft_Windows_WMPNSS_Service_14309_0(Etw):
    pattern = Struct(
        "ServiceName" / WString,
        "ErrorCode" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=14310, version=0)
class Microsoft_Windows_WMPNSS_Service_14310_0(Etw):
    pattern = Struct(
        "ServiceName" / WString,
        "ErrorCode" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=14311, version=0)
class Microsoft_Windows_WMPNSS_Service_14311_0(Etw):
    pattern = Struct(
        "ServiceName" / WString,
        "ErrorCode" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=14312, version=0)
class Microsoft_Windows_WMPNSS_Service_14312_0(Etw):
    pattern = Struct(
        "ServiceName" / WString,
        "ErrorCode" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=14313, version=0)
class Microsoft_Windows_WMPNSS_Service_14313_0(Etw):
    pattern = Struct(
        "ServiceName" / WString,
        "ErrorCode" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=14314, version=0)
class Microsoft_Windows_WMPNSS_Service_14314_0(Etw):
    pattern = Struct(
        "ServiceName" / WString,
        "ErrorCode" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=14315, version=0)
class Microsoft_Windows_WMPNSS_Service_14315_0(Etw):
    pattern = Struct(
        "ServiceName" / WString,
        "ErrorCode" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=14316, version=0)
class Microsoft_Windows_WMPNSS_Service_14316_0(Etw):
    pattern = Struct(
        "ServiceName" / WString,
        "ErrorCode" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=14317, version=0)
class Microsoft_Windows_WMPNSS_Service_14317_0(Etw):
    pattern = Struct(
        "ServiceName" / WString,
        "ErrorCode" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=14318, version=0)
class Microsoft_Windows_WMPNSS_Service_14318_0(Etw):
    pattern = Struct(
        "ServiceName" / WString,
        "ErrorCode" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=14319, version=0)
class Microsoft_Windows_WMPNSS_Service_14319_0(Etw):
    pattern = Struct(
        "ServiceName" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=14320, version=0)
class Microsoft_Windows_WMPNSS_Service_14320_0(Etw):
    pattern = Struct(
        "ServiceName" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=14321, version=0)
class Microsoft_Windows_WMPNSS_Service_14321_0(Etw):
    pattern = Struct(
        "ServiceName" / WString,
        "ErrorCode" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=14322, version=0)
class Microsoft_Windows_WMPNSS_Service_14322_0(Etw):
    pattern = Struct(
        "ServiceName" / WString,
        "ErrorCode" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=14323, version=0)
class Microsoft_Windows_WMPNSS_Service_14323_0(Etw):
    pattern = Struct(
        "ServiceName" / WString,
        "ErrorCode" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=14326, version=0)
class Microsoft_Windows_WMPNSS_Service_14326_0(Etw):
    pattern = Struct(
        "ServiceName" / WString,
        "ErrorCode" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=14327, version=0)
class Microsoft_Windows_WMPNSS_Service_14327_0(Etw):
    pattern = Struct(
        "ServiceName" / WString,
        "ErrorCode" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=14328, version=0)
class Microsoft_Windows_WMPNSS_Service_14328_0(Etw):
    pattern = Struct(
        "ServiceName" / WString,
        "ErrorCode" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=14329, version=0)
class Microsoft_Windows_WMPNSS_Service_14329_0(Etw):
    pattern = Struct(
        "ServiceName" / WString,
        "ErrorCode" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=14330, version=0)
class Microsoft_Windows_WMPNSS_Service_14330_0(Etw):
    pattern = Struct(
        "ServiceName" / WString,
        "ErrorCode" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=14331, version=0)
class Microsoft_Windows_WMPNSS_Service_14331_0(Etw):
    pattern = Struct(
        "ServiceName" / WString,
        "ErrorCode" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=14333, version=0)
class Microsoft_Windows_WMPNSS_Service_14333_0(Etw):
    pattern = Struct(
        "ServiceName" / WString,
        "ErrorCode" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=14337, version=0)
class Microsoft_Windows_WMPNSS_Service_14337_0(Etw):
    pattern = Struct(
        "ServiceName" / WString,
        "ErrorCode" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=14338, version=0)
class Microsoft_Windows_WMPNSS_Service_14338_0(Etw):
    pattern = Struct(
        "ErrorCode" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=14339, version=0)
class Microsoft_Windows_WMPNSS_Service_14339_0(Etw):
    pattern = Struct(
        "ErrorCode" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=14340, version=0)
class Microsoft_Windows_WMPNSS_Service_14340_0(Etw):
    pattern = Struct(
        "ErrorCode" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=14341, version=0)
class Microsoft_Windows_WMPNSS_Service_14341_0(Etw):
    pattern = Struct(
        "ErrorCode" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=14342, version=0)
class Microsoft_Windows_WMPNSS_Service_14342_0(Etw):
    pattern = Struct(
        "ErrorCode" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=14343, version=0)
class Microsoft_Windows_WMPNSS_Service_14343_0(Etw):
    pattern = Struct(
        "ErrorCode" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=14345, version=0)
class Microsoft_Windows_WMPNSS_Service_14345_0(Etw):
    pattern = Struct(
        "ErrorCode" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=14346, version=0)
class Microsoft_Windows_WMPNSS_Service_14346_0(Etw):
    pattern = Struct(
        "ErrorCode" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=14347, version=0)
class Microsoft_Windows_WMPNSS_Service_14347_0(Etw):
    pattern = Struct(
        "ErrorCode" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=14348, version=0)
class Microsoft_Windows_WMPNSS_Service_14348_0(Etw):
    pattern = Struct(
        "ErrorCode" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=14349, version=0)
class Microsoft_Windows_WMPNSS_Service_14349_0(Etw):
    pattern = Struct(
        "ErrorCode" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=14351, version=0)
class Microsoft_Windows_WMPNSS_Service_14351_0(Etw):
    pattern = Struct(
        "MDEID" / WString,
        "ErrorCode" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=14352, version=0)
class Microsoft_Windows_WMPNSS_Service_14352_0(Etw):
    pattern = Struct(
        "MDEID" / WString,
        "ErrorCode" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=14353, version=0)
class Microsoft_Windows_WMPNSS_Service_14353_0(Etw):
    pattern = Struct(
        "MDEID" / WString,
        "ErrorCode" / WString,
        "URL" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=14354, version=0)
class Microsoft_Windows_WMPNSS_Service_14354_0(Etw):
    pattern = Struct(
        "MDEID" / WString,
        "ErrorCode" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=14355, version=0)
class Microsoft_Windows_WMPNSS_Service_14355_0(Etw):
    pattern = Struct(
        "MDEID" / WString,
        "ErrorCode" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=14356, version=0)
class Microsoft_Windows_WMPNSS_Service_14356_0(Etw):
    pattern = Struct(
        "MDEID" / WString,
        "ErrorCode" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=14357, version=0)
class Microsoft_Windows_WMPNSS_Service_14357_0(Etw):
    pattern = Struct(
        "MDEID" / WString,
        "ErrorCode" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=14358, version=0)
class Microsoft_Windows_WMPNSS_Service_14358_0(Etw):
    pattern = Struct(
        "MDEID" / WString,
        "ErrorCode" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=14359, version=0)
class Microsoft_Windows_WMPNSS_Service_14359_0(Etw):
    pattern = Struct(
        "MDEID" / WString,
        "ErrorCode" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=14360, version=0)
class Microsoft_Windows_WMPNSS_Service_14360_0(Etw):
    pattern = Struct(
        "ErrorCode" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=14361, version=0)
class Microsoft_Windows_WMPNSS_Service_14361_0(Etw):
    pattern = Struct(
        "ErrorCode" / WString
    )


@declare(guid=guid("6a2dc7c1-930a-4fb5-bb44-80b30aebed6c"), event_id=14372, version=0)
class Microsoft_Windows_WMPNSS_Service_14372_0(Etw):
    pattern = Struct(
        "MDEID" / WString,
        "ErrorCode" / WString
    )

