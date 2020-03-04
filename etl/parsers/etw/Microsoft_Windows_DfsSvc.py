# -*- coding: utf-8 -*-
"""
Microsoft-Windows-DfsSvc
GUID : 7da4fe0e-fd42-4708-9aa5-89b77a224885
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("7da4fe0e-fd42-4708-9aa5-89b77a224885"), event_id=14318, version=0)
class Microsoft_Windows_DfsSvc_14318_0(Etw):
    pattern = Struct(
        "unused" / WString,
        "path" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7da4fe0e-fd42-4708-9aa5-89b77a224885"), event_id=14500, version=0)
class Microsoft_Windows_DfsSvc_14500_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7da4fe0e-fd42-4708-9aa5-89b77a224885"), event_id=14501, version=0)
class Microsoft_Windows_DfsSvc_14501_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7da4fe0e-fd42-4708-9aa5-89b77a224885"), event_id=14503, version=0)
class Microsoft_Windows_DfsSvc_14503_0(Etw):
    pattern = Struct(
        "childDirectory" / WString,
        "parentDirectory" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7da4fe0e-fd42-4708-9aa5-89b77a224885"), event_id=14504, version=0)
class Microsoft_Windows_DfsSvc_14504_0(Etw):
    pattern = Struct(
        "share" / WString,
        "path" / WString
    )


@declare(guid=guid("7da4fe0e-fd42-4708-9aa5-89b77a224885"), event_id=14505, version=0)
class Microsoft_Windows_DfsSvc_14505_0(Etw):
    pattern = Struct(
        "share" / WString,
        "directory" / WString
    )


@declare(guid=guid("7da4fe0e-fd42-4708-9aa5-89b77a224885"), event_id=14509, version=0)
class Microsoft_Windows_DfsSvc_14509_0(Etw):
    pattern = Struct(
        "share" / WString
    )


@declare(guid=guid("7da4fe0e-fd42-4708-9aa5-89b77a224885"), event_id=14510, version=0)
class Microsoft_Windows_DfsSvc_14510_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7da4fe0e-fd42-4708-9aa5-89b77a224885"), event_id=14511, version=0)
class Microsoft_Windows_DfsSvc_14511_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7da4fe0e-fd42-4708-9aa5-89b77a224885"), event_id=14512, version=0)
class Microsoft_Windows_DfsSvc_14512_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7da4fe0e-fd42-4708-9aa5-89b77a224885"), event_id=14513, version=0)
class Microsoft_Windows_DfsSvc_14513_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7da4fe0e-fd42-4708-9aa5-89b77a224885"), event_id=14514, version=0)
class Microsoft_Windows_DfsSvc_14514_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7da4fe0e-fd42-4708-9aa5-89b77a224885"), event_id=14515, version=0)
class Microsoft_Windows_DfsSvc_14515_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7da4fe0e-fd42-4708-9aa5-89b77a224885"), event_id=14516, version=0)
class Microsoft_Windows_DfsSvc_14516_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7da4fe0e-fd42-4708-9aa5-89b77a224885"), event_id=14517, version=0)
class Microsoft_Windows_DfsSvc_14517_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7da4fe0e-fd42-4708-9aa5-89b77a224885"), event_id=14518, version=0)
class Microsoft_Windows_DfsSvc_14518_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7da4fe0e-fd42-4708-9aa5-89b77a224885"), event_id=14519, version=0)
class Microsoft_Windows_DfsSvc_14519_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7da4fe0e-fd42-4708-9aa5-89b77a224885"), event_id=14520, version=0)
class Microsoft_Windows_DfsSvc_14520_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7da4fe0e-fd42-4708-9aa5-89b77a224885"), event_id=14521, version=0)
class Microsoft_Windows_DfsSvc_14521_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7da4fe0e-fd42-4708-9aa5-89b77a224885"), event_id=14522, version=0)
class Microsoft_Windows_DfsSvc_14522_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7da4fe0e-fd42-4708-9aa5-89b77a224885"), event_id=14524, version=0)
class Microsoft_Windows_DfsSvc_14524_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7da4fe0e-fd42-4708-9aa5-89b77a224885"), event_id=14526, version=0)
class Microsoft_Windows_DfsSvc_14526_0(Etw):
    pattern = Struct(
        "dc" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7da4fe0e-fd42-4708-9aa5-89b77a224885"), event_id=14529, version=0)
class Microsoft_Windows_DfsSvc_14529_0(Etw):
    pattern = Struct(
        "dc" / WString
    )


@declare(guid=guid("7da4fe0e-fd42-4708-9aa5-89b77a224885"), event_id=14530, version=0)
class Microsoft_Windows_DfsSvc_14530_0(Etw):
    pattern = Struct(
        "share" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7da4fe0e-fd42-4708-9aa5-89b77a224885"), event_id=14532, version=0)
class Microsoft_Windows_DfsSvc_14532_0(Etw):
    pattern = Struct(
        "share" / WString
    )


@declare(guid=guid("7da4fe0e-fd42-4708-9aa5-89b77a224885"), event_id=14534, version=0)
class Microsoft_Windows_DfsSvc_14534_0(Etw):
    pattern = Struct(
        "share" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7da4fe0e-fd42-4708-9aa5-89b77a224885"), event_id=14535, version=0)
class Microsoft_Windows_DfsSvc_14535_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7da4fe0e-fd42-4708-9aa5-89b77a224885"), event_id=14538, version=0)
class Microsoft_Windows_DfsSvc_14538_0(Etw):
    pattern = Struct(
        "share" / WString,
        "oldPath" / WString,
        "newPath" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7da4fe0e-fd42-4708-9aa5-89b77a224885"), event_id=14539, version=0)
class Microsoft_Windows_DfsSvc_14539_0(Etw):
    pattern = Struct(
        "share" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7da4fe0e-fd42-4708-9aa5-89b77a224885"), event_id=14540, version=0)
class Microsoft_Windows_DfsSvc_14540_0(Etw):
    pattern = Struct(
        "path" / WString,
        "share" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7da4fe0e-fd42-4708-9aa5-89b77a224885"), event_id=14541, version=0)
class Microsoft_Windows_DfsSvc_14541_0(Etw):
    pattern = Struct(
        "DFSLink" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7da4fe0e-fd42-4708-9aa5-89b77a224885"), event_id=14542, version=0)
class Microsoft_Windows_DfsSvc_14542_0(Etw):
    pattern = Struct(
        "DFSLink" / WString,
        "DFSRoot" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7da4fe0e-fd42-4708-9aa5-89b77a224885"), event_id=14543, version=0)
class Microsoft_Windows_DfsSvc_14543_0(Etw):
    pattern = Struct(
        "DFSLinkDN" / WString
    )


@declare(guid=guid("7da4fe0e-fd42-4708-9aa5-89b77a224885"), event_id=14544, version=0)
class Microsoft_Windows_DfsSvc_14544_0(Etw):
    pattern = Struct(
        "DFSNamespace" / WString,
        "DFSLink1" / WString,
        "DFSLink2" / WString
    )


@declare(guid=guid("7da4fe0e-fd42-4708-9aa5-89b77a224885"), event_id=14545, version=0)
class Microsoft_Windows_DfsSvc_14545_0(Etw):
    pattern = Struct(
        "DFSNamespace" / WString,
        "DFSLink1" / WString
    )


@declare(guid=guid("7da4fe0e-fd42-4708-9aa5-89b77a224885"), event_id=14546, version=0)
class Microsoft_Windows_DfsSvc_14546_0(Etw):
    pattern = Struct(
        "childDirectory" / WString,
        "parentDirectory" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7da4fe0e-fd42-4708-9aa5-89b77a224885"), event_id=14547, version=0)
class Microsoft_Windows_DfsSvc_14547_0(Etw):
    pattern = Struct(
        "DFSNamespace" / WString,
        "DFSFolderPath" / WString,
        "DFSLinkDN1" / WString,
        "DFSLinkDN2" / WString
    )


@declare(guid=guid("7da4fe0e-fd42-4708-9aa5-89b77a224885"), event_id=14548, version=0)
class Microsoft_Windows_DfsSvc_14548_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7da4fe0e-fd42-4708-9aa5-89b77a224885"), event_id=14550, version=0)
class Microsoft_Windows_DfsSvc_14550_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7da4fe0e-fd42-4708-9aa5-89b77a224885"), event_id=14552, version=0)
class Microsoft_Windows_DfsSvc_14552_0(Etw):
    pattern = Struct(
        "DFSRoot" / WString
    )


@declare(guid=guid("7da4fe0e-fd42-4708-9aa5-89b77a224885"), event_id=14553, version=0)
class Microsoft_Windows_DfsSvc_14553_0(Etw):
    pattern = Struct(
        "SMBShare" / WString,
        "__binLength" / Int32ul,
        "binary" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7da4fe0e-fd42-4708-9aa5-89b77a224885"), event_id=14554, version=0)
class Microsoft_Windows_DfsSvc_14554_0(Etw):
    pattern = Struct(
        "SMBShare" / WString
    )

