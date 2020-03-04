# -*- coding: utf-8 -*-
"""
Microsoft-Windows-AppxPackagingOM
GUID : ba723d81-0d0c-4f1e-80c8-54740f508ddf
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=100, version=0)
class Microsoft_Windows_AppxPackagingOM_100_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul,
        "reason" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=101, version=0)
class Microsoft_Windows_AppxPackagingOM_101_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "name" / WString,
        "xmlNamespace" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=102, version=0)
class Microsoft_Windows_AppxPackagingOM_102_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=103, version=0)
class Microsoft_Windows_AppxPackagingOM_103_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=104, version=0)
class Microsoft_Windows_AppxPackagingOM_104_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=105, version=0)
class Microsoft_Windows_AppxPackagingOM_105_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=106, version=0)
class Microsoft_Windows_AppxPackagingOM_106_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=107, version=0)
class Microsoft_Windows_AppxPackagingOM_107_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=110, version=0)
class Microsoft_Windows_AppxPackagingOM_110_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=111, version=0)
class Microsoft_Windows_AppxPackagingOM_111_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul,
        "logo" / WString,
        "field" / WString,
        "value" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=112, version=0)
class Microsoft_Windows_AppxPackagingOM_112_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=113, version=0)
class Microsoft_Windows_AppxPackagingOM_113_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=114, version=0)
class Microsoft_Windows_AppxPackagingOM_114_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=115, version=0)
class Microsoft_Windows_AppxPackagingOM_115_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=116, version=0)
class Microsoft_Windows_AppxPackagingOM_116_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=117, version=0)
class Microsoft_Windows_AppxPackagingOM_117_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul,
        "elementName" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=118, version=0)
class Microsoft_Windows_AppxPackagingOM_118_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul,
        "elementName" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=119, version=0)
class Microsoft_Windows_AppxPackagingOM_119_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul,
        "elementName" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=120, version=0)
class Microsoft_Windows_AppxPackagingOM_120_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul,
        "elementName" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=121, version=0)
class Microsoft_Windows_AppxPackagingOM_121_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul,
        "elementName" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=122, version=0)
class Microsoft_Windows_AppxPackagingOM_122_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=123, version=0)
class Microsoft_Windows_AppxPackagingOM_123_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul,
        "reason" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=124, version=0)
class Microsoft_Windows_AppxPackagingOM_124_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul,
        "value" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=126, version=0)
class Microsoft_Windows_AppxPackagingOM_126_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul,
        "fullValue" / WString,
        "fieldValue" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=127, version=0)
class Microsoft_Windows_AppxPackagingOM_127_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul,
        "fieldName" / WString,
        "fieldValue" / WString,
        "duplicateLineNumber" / Int32ul,
        "duplicateColumnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=128, version=0)
class Microsoft_Windows_AppxPackagingOM_128_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "reason" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=129, version=0)
class Microsoft_Windows_AppxPackagingOM_129_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul,
        "value" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=130, version=0)
class Microsoft_Windows_AppxPackagingOM_130_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul,
        "value" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=131, version=0)
class Microsoft_Windows_AppxPackagingOM_131_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=132, version=0)
class Microsoft_Windows_AppxPackagingOM_132_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=133, version=0)
class Microsoft_Windows_AppxPackagingOM_133_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul,
        "attributeName1" / WString,
        "attributeName2" / WString,
        "elementName" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=134, version=0)
class Microsoft_Windows_AppxPackagingOM_134_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul,
        "attributeName1" / WString,
        "attributeName2" / WString,
        "elementName" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=135, version=0)
class Microsoft_Windows_AppxPackagingOM_135_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul,
        "xmlNamespace" / WString,
        "reason" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=139, version=0)
class Microsoft_Windows_AppxPackagingOM_139_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul,
        "elementName" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=140, version=0)
class Microsoft_Windows_AppxPackagingOM_140_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul,
        "attributeName1" / WString,
        "attributeName2" / WString,
        "elementName" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=141, version=0)
class Microsoft_Windows_AppxPackagingOM_141_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=142, version=0)
class Microsoft_Windows_AppxPackagingOM_142_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul,
        "elementName" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=143, version=0)
class Microsoft_Windows_AppxPackagingOM_143_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=144, version=0)
class Microsoft_Windows_AppxPackagingOM_144_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=145, version=0)
class Microsoft_Windows_AppxPackagingOM_145_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=146, version=0)
class Microsoft_Windows_AppxPackagingOM_146_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=147, version=0)
class Microsoft_Windows_AppxPackagingOM_147_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=150, version=0)
class Microsoft_Windows_AppxPackagingOM_150_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "expectedValue" / WString,
        "actualValue" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=151, version=0)
class Microsoft_Windows_AppxPackagingOM_151_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "expectedValue" / WString,
        "actualValue" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=152, version=0)
class Microsoft_Windows_AppxPackagingOM_152_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=153, version=0)
class Microsoft_Windows_AppxPackagingOM_153_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=154, version=0)
class Microsoft_Windows_AppxPackagingOM_154_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=155, version=0)
class Microsoft_Windows_AppxPackagingOM_155_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=156, version=0)
class Microsoft_Windows_AppxPackagingOM_156_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=157, version=0)
class Microsoft_Windows_AppxPackagingOM_157_0(Etw):
    pattern = Struct(
        "subjectName" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=158, version=0)
class Microsoft_Windows_AppxPackagingOM_158_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul,
        "elementName" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=159, version=0)
class Microsoft_Windows_AppxPackagingOM_159_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=160, version=0)
class Microsoft_Windows_AppxPackagingOM_160_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "expectedValue" / WString,
        "actualValue" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=161, version=0)
class Microsoft_Windows_AppxPackagingOM_161_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "expectedValue" / WString,
        "actualValue" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=162, version=0)
class Microsoft_Windows_AppxPackagingOM_162_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "packageName" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=163, version=0)
class Microsoft_Windows_AppxPackagingOM_163_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=164, version=0)
class Microsoft_Windows_AppxPackagingOM_164_0(Etw):
    pattern = Struct(
        "subjectName" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=165, version=0)
class Microsoft_Windows_AppxPackagingOM_165_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "fileId" / Int64ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=170, version=0)
class Microsoft_Windows_AppxPackagingOM_170_0(Etw):
    pattern = Struct(
        "packageFullName" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=171, version=0)
class Microsoft_Windows_AppxPackagingOM_171_0(Etw):
    pattern = Struct(
        "packageFullName" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=172, version=0)
class Microsoft_Windows_AppxPackagingOM_172_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "fileName" / WString,
        "packageFullName" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=173, version=0)
class Microsoft_Windows_AppxPackagingOM_173_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "currentFileName" / WString,
        "currentPackageFullName" / WString,
        "conflictingFileName" / WString,
        "conflictingPackageFullName" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=174, version=0)
class Microsoft_Windows_AppxPackagingOM_174_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "currentFileName" / WString,
        "currentPackageFullName" / WString,
        "conflictingFileName" / WString,
        "conflictingPackageFullName" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=175, version=0)
class Microsoft_Windows_AppxPackagingOM_175_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "fileName" / WString,
        "packageFullName" / WString,
        "expectedValue" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=176, version=0)
class Microsoft_Windows_AppxPackagingOM_176_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "fileName" / WString,
        "packageFullName" / WString,
        "expectedValue" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=177, version=0)
class Microsoft_Windows_AppxPackagingOM_177_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "fileName" / WString,
        "packageFullName" / WString,
        "expectedValue" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=178, version=0)
class Microsoft_Windows_AppxPackagingOM_178_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=179, version=0)
class Microsoft_Windows_AppxPackagingOM_179_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=180, version=0)
class Microsoft_Windows_AppxPackagingOM_180_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul,
        "extensionCategoryName" / WString,
        "attributeName" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=182, version=0)
class Microsoft_Windows_AppxPackagingOM_182_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=183, version=0)
class Microsoft_Windows_AppxPackagingOM_183_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=184, version=0)
class Microsoft_Windows_AppxPackagingOM_184_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=185, version=0)
class Microsoft_Windows_AppxPackagingOM_185_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=186, version=0)
class Microsoft_Windows_AppxPackagingOM_186_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=187, version=0)
class Microsoft_Windows_AppxPackagingOM_187_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=188, version=0)
class Microsoft_Windows_AppxPackagingOM_188_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=189, version=0)
class Microsoft_Windows_AppxPackagingOM_189_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=190, version=0)
class Microsoft_Windows_AppxPackagingOM_190_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=191, version=0)
class Microsoft_Windows_AppxPackagingOM_191_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul,
        "value" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=192, version=0)
class Microsoft_Windows_AppxPackagingOM_192_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul,
        "value" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=193, version=0)
class Microsoft_Windows_AppxPackagingOM_193_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul,
        "targetDeviceFamily" / WString,
        "version" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=195, version=0)
class Microsoft_Windows_AppxPackagingOM_195_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=196, version=0)
class Microsoft_Windows_AppxPackagingOM_196_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=197, version=0)
class Microsoft_Windows_AppxPackagingOM_197_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=198, version=0)
class Microsoft_Windows_AppxPackagingOM_198_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=199, version=0)
class Microsoft_Windows_AppxPackagingOM_199_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=200, version=0)
class Microsoft_Windows_AppxPackagingOM_200_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=201, version=0)
class Microsoft_Windows_AppxPackagingOM_201_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul,
        "value" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=202, version=0)
class Microsoft_Windows_AppxPackagingOM_202_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=203, version=0)
class Microsoft_Windows_AppxPackagingOM_203_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=204, version=0)
class Microsoft_Windows_AppxPackagingOM_204_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=205, version=0)
class Microsoft_Windows_AppxPackagingOM_205_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=206, version=0)
class Microsoft_Windows_AppxPackagingOM_206_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=207, version=0)
class Microsoft_Windows_AppxPackagingOM_207_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=208, version=0)
class Microsoft_Windows_AppxPackagingOM_208_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=209, version=0)
class Microsoft_Windows_AppxPackagingOM_209_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=210, version=0)
class Microsoft_Windows_AppxPackagingOM_210_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=211, version=0)
class Microsoft_Windows_AppxPackagingOM_211_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=212, version=0)
class Microsoft_Windows_AppxPackagingOM_212_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=213, version=0)
class Microsoft_Windows_AppxPackagingOM_213_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=214, version=0)
class Microsoft_Windows_AppxPackagingOM_214_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=215, version=0)
class Microsoft_Windows_AppxPackagingOM_215_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=216, version=0)
class Microsoft_Windows_AppxPackagingOM_216_0(Etw):
    pattern = Struct(
        "namespace" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=217, version=0)
class Microsoft_Windows_AppxPackagingOM_217_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=218, version=0)
class Microsoft_Windows_AppxPackagingOM_218_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=219, version=0)
class Microsoft_Windows_AppxPackagingOM_219_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul,
        "value" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=220, version=0)
class Microsoft_Windows_AppxPackagingOM_220_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul,
        "value" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=221, version=0)
class Microsoft_Windows_AppxPackagingOM_221_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=222, version=0)
class Microsoft_Windows_AppxPackagingOM_222_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul,
        "mainPackageName" / WString,
        "mainPackagePublisher" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=223, version=0)
class Microsoft_Windows_AppxPackagingOM_223_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=224, version=0)
class Microsoft_Windows_AppxPackagingOM_224_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=225, version=0)
class Microsoft_Windows_AppxPackagingOM_225_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=226, version=0)
class Microsoft_Windows_AppxPackagingOM_226_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=227, version=0)
class Microsoft_Windows_AppxPackagingOM_227_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=228, version=0)
class Microsoft_Windows_AppxPackagingOM_228_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=229, version=0)
class Microsoft_Windows_AppxPackagingOM_229_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul,
        "reason" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=230, version=0)
class Microsoft_Windows_AppxPackagingOM_230_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=231, version=0)
class Microsoft_Windows_AppxPackagingOM_231_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=232, version=0)
class Microsoft_Windows_AppxPackagingOM_232_0(Etw):
    pattern = Struct(
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul,
        "ignoredElement" / WString,
        "xpathToRequiredChildElement" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=233, version=0)
class Microsoft_Windows_AppxPackagingOM_233_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul,
        "extensionCategoryName" / WString,
        "attributeName" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=234, version=0)
class Microsoft_Windows_AppxPackagingOM_234_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=235, version=0)
class Microsoft_Windows_AppxPackagingOM_235_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "fileName" / WString,
        "packageFullName" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=236, version=0)
class Microsoft_Windows_AppxPackagingOM_236_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=237, version=0)
class Microsoft_Windows_AppxPackagingOM_237_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul,
        "reason" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=238, version=0)
class Microsoft_Windows_AppxPackagingOM_238_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "reason" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=239, version=0)
class Microsoft_Windows_AppxPackagingOM_239_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=240, version=0)
class Microsoft_Windows_AppxPackagingOM_240_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=241, version=0)
class Microsoft_Windows_AppxPackagingOM_241_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul,
        "value" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=242, version=0)
class Microsoft_Windows_AppxPackagingOM_242_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul,
        "value" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=243, version=0)
class Microsoft_Windows_AppxPackagingOM_243_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul,
        "extensionCategoryName" / WString,
        "attributeName" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=244, version=0)
class Microsoft_Windows_AppxPackagingOM_244_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=245, version=0)
class Microsoft_Windows_AppxPackagingOM_245_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=246, version=0)
class Microsoft_Windows_AppxPackagingOM_246_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=247, version=0)
class Microsoft_Windows_AppxPackagingOM_247_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul,
        "reason" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=248, version=0)
class Microsoft_Windows_AppxPackagingOM_248_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "reason" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=249, version=0)
class Microsoft_Windows_AppxPackagingOM_249_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=250, version=0)
class Microsoft_Windows_AppxPackagingOM_250_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=251, version=0)
class Microsoft_Windows_AppxPackagingOM_251_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=252, version=0)
class Microsoft_Windows_AppxPackagingOM_252_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=253, version=0)
class Microsoft_Windows_AppxPackagingOM_253_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=254, version=0)
class Microsoft_Windows_AppxPackagingOM_254_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=255, version=0)
class Microsoft_Windows_AppxPackagingOM_255_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul,
        "value" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=256, version=0)
class Microsoft_Windows_AppxPackagingOM_256_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=257, version=0)
class Microsoft_Windows_AppxPackagingOM_257_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul,
        "value" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=258, version=0)
class Microsoft_Windows_AppxPackagingOM_258_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul,
        "value" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=259, version=0)
class Microsoft_Windows_AppxPackagingOM_259_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul,
        "value" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=260, version=0)
class Microsoft_Windows_AppxPackagingOM_260_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "currentFileName" / WString,
        "currentPackageFullName" / WString,
        "conflictingFileName" / WString,
        "conflictingPackageFullName" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=261, version=0)
class Microsoft_Windows_AppxPackagingOM_261_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=262, version=0)
class Microsoft_Windows_AppxPackagingOM_262_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=263, version=0)
class Microsoft_Windows_AppxPackagingOM_263_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul,
        "extensionCategoryName" / WString,
        "attributeName" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=264, version=0)
class Microsoft_Windows_AppxPackagingOM_264_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=265, version=0)
class Microsoft_Windows_AppxPackagingOM_265_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "lineNumber" / Int32ul,
        "columnNumber" / Int32ul,
        "attributeName" / WString,
        "attributeValue" / WString,
        "attributeLength" / Int32ul,
        "buildVersion" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=300, version=0)
class Microsoft_Windows_AppxPackagingOM_300_0(Etw):
    pattern = Struct(
        "zipMode" / Int8ul,
        "hashMethod" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=301, version=0)
class Microsoft_Windows_AppxPackagingOM_301_0(Etw):
    pattern = Struct(
        "fileCount" / Int64ul,
        "totalSize" / Int64ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=302, version=0)
class Microsoft_Windows_AppxPackagingOM_302_0(Etw):
    pattern = Struct(
        "fileName" / WString,
        "contentType" / WString,
        "compressionOption" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=308, version=0)
class Microsoft_Windows_AppxPackagingOM_308_0(Etw):
    pattern = Struct(
        "fileName" / WString,
        "size" / Int64ul,
        "compressionOption" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=310, version=0)
class Microsoft_Windows_AppxPackagingOM_310_0(Etw):
    pattern = Struct(
        "readerOptions" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=312, version=0)
class Microsoft_Windows_AppxPackagingOM_312_0(Etw):
    pattern = Struct(
        "requestCount" / Int32ul,
        "priority" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=318, version=0)
class Microsoft_Windows_AppxPackagingOM_318_0(Etw):
    pattern = Struct(
        "value" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=319, version=0)
class Microsoft_Windows_AppxPackagingOM_319_0(Etw):
    pattern = Struct(
        "value" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=362, version=0)
class Microsoft_Windows_AppxPackagingOM_362_0(Etw):
    pattern = Struct(
        "capabilitySid" / Sid
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=363, version=0)
class Microsoft_Windows_AppxPackagingOM_363_0(Etw):
    pattern = Struct(
        "capabilitySid" / Sid,
        "result" / Int32ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=390, version=0)
class Microsoft_Windows_AppxPackagingOM_390_0(Etw):
    pattern = Struct(
        "packageFullName" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=391, version=0)
class Microsoft_Windows_AppxPackagingOM_391_0(Etw):
    pattern = Struct(
        "packageFullName" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=392, version=0)
class Microsoft_Windows_AppxPackagingOM_392_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "fileName" / WString,
        "packageFullName" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=393, version=0)
class Microsoft_Windows_AppxPackagingOM_393_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "fileName" / WString,
        "packageFullName" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=394, version=0)
class Microsoft_Windows_AppxPackagingOM_394_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "fileName" / WString,
        "packageFullName" / WString,
        "expectedValue" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=395, version=0)
class Microsoft_Windows_AppxPackagingOM_395_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "fileName" / WString,
        "packageFullName" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=396, version=0)
class Microsoft_Windows_AppxPackagingOM_396_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "currentFileName" / WString,
        "currentPackageFullName" / WString,
        "attributeName" / WString,
        "expectedValue" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=397, version=0)
class Microsoft_Windows_AppxPackagingOM_397_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "fileName" / WString,
        "packageFullName" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=398, version=0)
class Microsoft_Windows_AppxPackagingOM_398_0(Etw):
    pattern = Struct(
        "errorCode" / Int32ul,
        "currentFileName" / WString,
        "currentPackageFullName" / WString,
        "currentManifestLineNumber" / Int32ul,
        "currentManifestColumnNumber" / Int32ul,
        "referenceFileName" / WString,
        "referencePackageFullName" / WString,
        "referenceManifestLineNumber" / Int32ul,
        "referenceManifestColumnNumber" / Int32ul,
        "xPathToMismatchLocation" / WString
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=424, version=0)
class Microsoft_Windows_AppxPackagingOM_424_0(Etw):
    pattern = Struct(
        "fileCount" / Int64ul
    )


@declare(guid=guid("ba723d81-0d0c-4f1e-80c8-54740f508ddf"), event_id=426, version=0)
class Microsoft_Windows_AppxPackagingOM_426_0(Etw):
    pattern = Struct(
        "fileName" / WString,
        "contentType" / WString,
        "compressionOption" / Int32ul
    )

