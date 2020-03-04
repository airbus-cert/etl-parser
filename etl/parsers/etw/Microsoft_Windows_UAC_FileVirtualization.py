# -*- coding: utf-8 -*-
"""
Microsoft-Windows-UAC-FileVirtualization
GUID : c02afc2b-e24e-4449-ad76-bcc2c2575ead
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("c02afc2b-e24e-4449-ad76-bcc2c2575ead"), event_id=2000, version=0)
class Microsoft_Windows_UAC_FileVirtualization_2000_0(Etw):
    pattern = Struct(
        "Error" / Int32ul
    )


@declare(guid=guid("c02afc2b-e24e-4449-ad76-bcc2c2575ead"), event_id=2001, version=0)
class Microsoft_Windows_UAC_FileVirtualization_2001_0(Etw):
    pattern = Struct(
        "Error" / Int32ul
    )


@declare(guid=guid("c02afc2b-e24e-4449-ad76-bcc2c2575ead"), event_id=2002, version=0)
class Microsoft_Windows_UAC_FileVirtualization_2002_0(Etw):
    pattern = Struct(
        "Error" / Int32ul
    )


@declare(guid=guid("c02afc2b-e24e-4449-ad76-bcc2c2575ead"), event_id=2003, version=0)
class Microsoft_Windows_UAC_FileVirtualization_2003_0(Etw):
    pattern = Struct(
        "Error" / Int32ul
    )


@declare(guid=guid("c02afc2b-e24e-4449-ad76-bcc2c2575ead"), event_id=2004, version=0)
class Microsoft_Windows_UAC_FileVirtualization_2004_0(Etw):
    pattern = Struct(
        "Error" / Int32ul
    )


@declare(guid=guid("c02afc2b-e24e-4449-ad76-bcc2c2575ead"), event_id=2005, version=0)
class Microsoft_Windows_UAC_FileVirtualization_2005_0(Etw):
    pattern = Struct(
        "Error" / Int32ul
    )


@declare(guid=guid("c02afc2b-e24e-4449-ad76-bcc2c2575ead"), event_id=2006, version=0)
class Microsoft_Windows_UAC_FileVirtualization_2006_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul,
        "SidLength" / Int32ul,
        "Sid" / Bytes(lambda this: this.SidLength),
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength),
        "ProcessImageNameLength" / Int16ul,
        "ProcessImageNameBuffer" / Bytes(lambda this: this.ProcessImageNameLength),
        "Error" / Int32ul
    )


@declare(guid=guid("c02afc2b-e24e-4449-ad76-bcc2c2575ead"), event_id=2007, version=0)
class Microsoft_Windows_UAC_FileVirtualization_2007_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul,
        "SidLength" / Int32ul,
        "Sid" / Bytes(lambda this: this.SidLength),
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength),
        "ProcessImageNameLength" / Int16ul,
        "ProcessImageNameBuffer" / Bytes(lambda this: this.ProcessImageNameLength),
        "Error" / Int32ul
    )


@declare(guid=guid("c02afc2b-e24e-4449-ad76-bcc2c2575ead"), event_id=2008, version=0)
class Microsoft_Windows_UAC_FileVirtualization_2008_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul,
        "SidLength" / Int32ul,
        "Sid" / Bytes(lambda this: this.SidLength),
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength),
        "ProcessImageNameLength" / Int16ul,
        "ProcessImageNameBuffer" / Bytes(lambda this: this.ProcessImageNameLength),
        "Error" / Int32ul
    )


@declare(guid=guid("c02afc2b-e24e-4449-ad76-bcc2c2575ead"), event_id=2009, version=0)
class Microsoft_Windows_UAC_FileVirtualization_2009_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul,
        "SidLength" / Int32ul,
        "Sid" / Bytes(lambda this: this.SidLength),
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength),
        "ProcessImageNameLength" / Int16ul,
        "ProcessImageNameBuffer" / Bytes(lambda this: this.ProcessImageNameLength),
        "Error" / Int32ul
    )


@declare(guid=guid("c02afc2b-e24e-4449-ad76-bcc2c2575ead"), event_id=2010, version=0)
class Microsoft_Windows_UAC_FileVirtualization_2010_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul,
        "SidLength" / Int32ul,
        "Sid" / Bytes(lambda this: this.SidLength),
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength),
        "ProcessImageNameLength" / Int16ul,
        "ProcessImageNameBuffer" / Bytes(lambda this: this.ProcessImageNameLength),
        "Error" / Int32ul
    )


@declare(guid=guid("c02afc2b-e24e-4449-ad76-bcc2c2575ead"), event_id=2011, version=0)
class Microsoft_Windows_UAC_FileVirtualization_2011_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul,
        "SidLength" / Int32ul,
        "Sid" / Bytes(lambda this: this.SidLength),
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength),
        "ProcessImageNameLength" / Int16ul,
        "ProcessImageNameBuffer" / Bytes(lambda this: this.ProcessImageNameLength),
        "Error" / Int32ul
    )


@declare(guid=guid("c02afc2b-e24e-4449-ad76-bcc2c2575ead"), event_id=2012, version=0)
class Microsoft_Windows_UAC_FileVirtualization_2012_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul,
        "SidLength" / Int32ul,
        "Sid" / Bytes(lambda this: this.SidLength),
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength),
        "ProcessImageNameLength" / Int16ul,
        "ProcessImageNameBuffer" / Bytes(lambda this: this.ProcessImageNameLength),
        "Error" / Int32ul
    )


@declare(guid=guid("c02afc2b-e24e-4449-ad76-bcc2c2575ead"), event_id=2013, version=0)
class Microsoft_Windows_UAC_FileVirtualization_2013_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul,
        "SidLength" / Int32ul,
        "Sid" / Bytes(lambda this: this.SidLength),
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength),
        "ProcessImageNameLength" / Int16ul,
        "ProcessImageNameBuffer" / Bytes(lambda this: this.ProcessImageNameLength),
        "Error" / Int32ul
    )


@declare(guid=guid("c02afc2b-e24e-4449-ad76-bcc2c2575ead"), event_id=2014, version=0)
class Microsoft_Windows_UAC_FileVirtualization_2014_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul,
        "SidLength" / Int32ul,
        "Sid" / Bytes(lambda this: this.SidLength),
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength),
        "ProcessImageNameLength" / Int16ul,
        "ProcessImageNameBuffer" / Bytes(lambda this: this.ProcessImageNameLength),
        "Error" / Int32ul
    )


@declare(guid=guid("c02afc2b-e24e-4449-ad76-bcc2c2575ead"), event_id=2015, version=0)
class Microsoft_Windows_UAC_FileVirtualization_2015_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul,
        "SidLength" / Int32ul,
        "Sid" / Bytes(lambda this: this.SidLength),
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength),
        "ProcessImageNameLength" / Int16ul,
        "ProcessImageNameBuffer" / Bytes(lambda this: this.ProcessImageNameLength),
        "Error" / Int32ul
    )


@declare(guid=guid("c02afc2b-e24e-4449-ad76-bcc2c2575ead"), event_id=2016, version=0)
class Microsoft_Windows_UAC_FileVirtualization_2016_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul,
        "SidLength" / Int32ul,
        "Sid" / Bytes(lambda this: this.SidLength),
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength),
        "ProcessImageNameLength" / Int16ul,
        "ProcessImageNameBuffer" / Bytes(lambda this: this.ProcessImageNameLength),
        "Error" / Int32ul
    )


@declare(guid=guid("c02afc2b-e24e-4449-ad76-bcc2c2575ead"), event_id=2017, version=0)
class Microsoft_Windows_UAC_FileVirtualization_2017_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul,
        "SidLength" / Int32ul,
        "Sid" / Bytes(lambda this: this.SidLength),
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength),
        "ProcessImageNameLength" / Int16ul,
        "ProcessImageNameBuffer" / Bytes(lambda this: this.ProcessImageNameLength),
        "Error" / Int32ul
    )


@declare(guid=guid("c02afc2b-e24e-4449-ad76-bcc2c2575ead"), event_id=2018, version=0)
class Microsoft_Windows_UAC_FileVirtualization_2018_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul,
        "SidLength" / Int32ul,
        "Sid" / Bytes(lambda this: this.SidLength),
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength),
        "ProcessImageNameLength" / Int16ul,
        "ProcessImageNameBuffer" / Bytes(lambda this: this.ProcessImageNameLength),
        "Error" / Int32ul
    )


@declare(guid=guid("c02afc2b-e24e-4449-ad76-bcc2c2575ead"), event_id=2019, version=0)
class Microsoft_Windows_UAC_FileVirtualization_2019_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul,
        "SidLength" / Int32ul,
        "Sid" / Bytes(lambda this: this.SidLength),
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength),
        "ProcessImageNameLength" / Int16ul,
        "ProcessImageNameBuffer" / Bytes(lambda this: this.ProcessImageNameLength),
        "Error" / Int32ul
    )


@declare(guid=guid("c02afc2b-e24e-4449-ad76-bcc2c2575ead"), event_id=4000, version=0)
class Microsoft_Windows_UAC_FileVirtualization_4000_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul,
        "SidLength" / Int32ul,
        "Sid" / Bytes(lambda this: this.SidLength),
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength),
        "ProcessImageNameLength" / Int16ul,
        "ProcessImageNameBuffer" / Bytes(lambda this: this.ProcessImageNameLength),
        "CreateOptions" / Int32ul,
        "DesiredAccess" / Int32ul,
        "IrpMajorFunction" / Int8ul
    )


@declare(guid=guid("c02afc2b-e24e-4449-ad76-bcc2c2575ead"), event_id=4001, version=0)
class Microsoft_Windows_UAC_FileVirtualization_4001_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul,
        "SidLength" / Int32ul,
        "Sid" / Bytes(lambda this: this.SidLength),
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength),
        "ProcessImageNameLength" / Int16ul,
        "ProcessImageNameBuffer" / Bytes(lambda this: this.ProcessImageNameLength),
        "TargetFileNameLength" / Int16ul,
        "TargetFileNameBuffer" / Bytes(lambda this: this.TargetFileNameLength)
    )


@declare(guid=guid("c02afc2b-e24e-4449-ad76-bcc2c2575ead"), event_id=4002, version=0)
class Microsoft_Windows_UAC_FileVirtualization_4002_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul,
        "SidLength" / Int32ul,
        "Sid" / Bytes(lambda this: this.SidLength),
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength),
        "ProcessImageNameLength" / Int16ul,
        "ProcessImageNameBuffer" / Bytes(lambda this: this.ProcessImageNameLength)
    )


@declare(guid=guid("c02afc2b-e24e-4449-ad76-bcc2c2575ead"), event_id=5000, version=0)
class Microsoft_Windows_UAC_FileVirtualization_5000_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul,
        "SidLength" / Int32ul,
        "Sid" / Bytes(lambda this: this.SidLength),
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength),
        "ProcessImageNameLength" / Int16ul,
        "ProcessImageNameBuffer" / Bytes(lambda this: this.ProcessImageNameLength),
        "CreateOptions" / Int32ul,
        "DesiredAccess" / Int32ul,
        "IrpMajorFunction" / Int8ul,
        "Exclusions" / Int32ul
    )


@declare(guid=guid("c02afc2b-e24e-4449-ad76-bcc2c2575ead"), event_id=5002, version=0)
class Microsoft_Windows_UAC_FileVirtualization_5002_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul,
        "SidLength" / Int32ul,
        "Sid" / Bytes(lambda this: this.SidLength),
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength),
        "ProcessImageNameLength" / Int16ul,
        "ProcessImageNameBuffer" / Bytes(lambda this: this.ProcessImageNameLength),
        "CreateOptions" / Int32ul,
        "DesiredAccess" / Int32ul
    )


@declare(guid=guid("c02afc2b-e24e-4449-ad76-bcc2c2575ead"), event_id=5003, version=0)
class Microsoft_Windows_UAC_FileVirtualization_5003_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul,
        "SidLength" / Int32ul,
        "Sid" / Bytes(lambda this: this.SidLength),
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength),
        "ProcessImageNameLength" / Int16ul,
        "ProcessImageNameBuffer" / Bytes(lambda this: this.ProcessImageNameLength)
    )


@declare(guid=guid("c02afc2b-e24e-4449-ad76-bcc2c2575ead"), event_id=5004, version=0)
class Microsoft_Windows_UAC_FileVirtualization_5004_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul,
        "SidLength" / Int32ul,
        "Sid" / Bytes(lambda this: this.SidLength),
        "FileNameLength" / Int16ul,
        "FileNameBuffer" / Bytes(lambda this: this.FileNameLength),
        "ProcessImageNameLength" / Int16ul,
        "ProcessImageNameBuffer" / Bytes(lambda this: this.ProcessImageNameLength)
    )

