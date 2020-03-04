# -*- coding: utf-8 -*-
"""
Microsoft-Windows-AIT
GUID : 6addabf4-8c54-4eab-bf4f-fbef61b62eb0
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("6addabf4-8c54-4eab-bf4f-fbef61b62eb0"), event_id=1, version=0)
class Microsoft_Windows_AIT_1_0(Etw):
    pattern = Struct(
        "FeatureGuid" / Guid
    )


@declare(guid=guid("6addabf4-8c54-4eab-bf4f-fbef61b62eb0"), event_id=2, version=0)
class Microsoft_Windows_AIT_2_0(Etw):
    pattern = Struct(
        "cchParentImagePathIncludingNull" / Int16ul,
        "FeatureGuid" / Guid,
        "ParentImagePath" / Bytes(lambda this: this.cchParentImagePathIncludingNull)
    )


@declare(guid=guid("6addabf4-8c54-4eab-bf4f-fbef61b62eb0"), event_id=3, version=0)
class Microsoft_Windows_AIT_3_0(Etw):
    pattern = Struct(
        "cchAppPathIncludingNull" / Int16ul,
        "AppPath" / Bytes(lambda this: this.cchAppPathIncludingNull)
    )


@declare(guid=guid("6addabf4-8c54-4eab-bf4f-fbef61b62eb0"), event_id=4, version=0)
class Microsoft_Windows_AIT_4_0(Etw):
    pattern = Struct(
        "cchIdStringIncludingNull" / Int16ul,
        "cchDllPathIncludingNull" / Int16ul,
        "Category" / Int32ul,
        "ManifestVersion" / Int32ul,
        "IdString" / Bytes(lambda this: this.cchIdStringIncludingNull),
        "DllPath" / Bytes(lambda this: this.cchDllPathIncludingNull)
    )


@declare(guid=guid("6addabf4-8c54-4eab-bf4f-fbef61b62eb0"), event_id=5, version=0)
class Microsoft_Windows_AIT_5_0(Etw):
    pattern = Struct(
        "cchIdStringIncludingNull" / Int16ul,
        "Category" / Int32ul,
        "ManifestVersion" / Int32ul,
        "IdString" / Bytes(lambda this: this.cchIdStringIncludingNull)
    )


@declare(guid=guid("6addabf4-8c54-4eab-bf4f-fbef61b62eb0"), event_id=7, version=0)
class Microsoft_Windows_AIT_7_0(Etw):
    pattern = Struct(
        "FeatureGuid" / Guid,
        "CallerIdType" / Int32ul,
        "cchImagePath" / Int16ul,
        "ImagePath" / Bytes(lambda this: this.cchImagePath)
    )

