# -*- coding: utf-8 -*-
"""
Microsoft-Windows-AppLocker
GUID : cbda4dbf-8d5d-4f69-9578-be14aa540d22
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("cbda4dbf-8d5d-4f69-9578-be14aa540d22"), event_id=8000, version=0)
class Microsoft_Windows_AppLocker_8000_0(Etw):
    pattern = Struct(
        "Status" / Int32ul
    )


@declare(guid=guid("cbda4dbf-8d5d-4f69-9578-be14aa540d22"), event_id=8002, version=0)
class Microsoft_Windows_AppLocker_8002_0(Etw):
    pattern = Struct(
        "PolicyNameLength" / Int16ul,
        "PolicyNameBuffer" / Bytes(lambda this: this.PolicyNameLength),
        "RuleId" / Guid,
        "RuleNameLength" / Int16ul,
        "RuleNameBuffer" / Bytes(lambda this: this.RuleNameLength),
        "RuleSddlLength" / Int16ul,
        "RuleSddlBuffer" / Bytes(lambda this: this.RuleSddlLength),
        "TargetUser" / Sid,
        "TargetProcessId" / Int32ul,
        "FilePathLength" / Int16ul,
        "FilePathBuffer" / Bytes(lambda this: this.FilePathLength),
        "FileHashLength" / Int16ul,
        "FileHash" / Bytes(lambda this: this.FileHashLength),
        "FqbnLength" / Int16ul,
        "Fqbn" / Bytes(lambda this: this.FqbnLength),
        "TargetLogonId" / Int64ul,
        "FullFilePathLength" / Int16ul,
        "FullFilePathBuffer" / Bytes(lambda this: this.FullFilePathLength)
    )


@declare(guid=guid("cbda4dbf-8d5d-4f69-9578-be14aa540d22"), event_id=8003, version=0)
class Microsoft_Windows_AppLocker_8003_0(Etw):
    pattern = Struct(
        "PolicyNameLength" / Int16ul,
        "PolicyNameBuffer" / Bytes(lambda this: this.PolicyNameLength),
        "RuleId" / Guid,
        "RuleNameLength" / Int16ul,
        "RuleNameBuffer" / Bytes(lambda this: this.RuleNameLength),
        "RuleSddlLength" / Int16ul,
        "RuleSddlBuffer" / Bytes(lambda this: this.RuleSddlLength),
        "TargetUser" / Sid,
        "TargetProcessId" / Int32ul,
        "FilePathLength" / Int16ul,
        "FilePathBuffer" / Bytes(lambda this: this.FilePathLength),
        "FileHashLength" / Int16ul,
        "FileHash" / Bytes(lambda this: this.FileHashLength),
        "FqbnLength" / Int16ul,
        "Fqbn" / Bytes(lambda this: this.FqbnLength),
        "TargetLogonId" / Int64ul,
        "FullFilePathLength" / Int16ul,
        "FullFilePathBuffer" / Bytes(lambda this: this.FullFilePathLength)
    )


@declare(guid=guid("cbda4dbf-8d5d-4f69-9578-be14aa540d22"), event_id=8004, version=0)
class Microsoft_Windows_AppLocker_8004_0(Etw):
    pattern = Struct(
        "PolicyNameLength" / Int16ul,
        "PolicyNameBuffer" / Bytes(lambda this: this.PolicyNameLength),
        "RuleId" / Guid,
        "RuleNameLength" / Int16ul,
        "RuleNameBuffer" / Bytes(lambda this: this.RuleNameLength),
        "RuleSddlLength" / Int16ul,
        "RuleSddlBuffer" / Bytes(lambda this: this.RuleSddlLength),
        "TargetUser" / Sid,
        "TargetProcessId" / Int32ul,
        "FilePathLength" / Int16ul,
        "FilePathBuffer" / Bytes(lambda this: this.FilePathLength),
        "FileHashLength" / Int16ul,
        "FileHash" / Bytes(lambda this: this.FileHashLength),
        "FqbnLength" / Int16ul,
        "Fqbn" / Bytes(lambda this: this.FqbnLength),
        "TargetLogonId" / Int64ul,
        "FullFilePathLength" / Int16ul,
        "FullFilePathBuffer" / Bytes(lambda this: this.FullFilePathLength)
    )


@declare(guid=guid("cbda4dbf-8d5d-4f69-9578-be14aa540d22"), event_id=8005, version=0)
class Microsoft_Windows_AppLocker_8005_0(Etw):
    pattern = Struct(
        "PolicyNameLength" / Int16ul,
        "PolicyNameBuffer" / Bytes(lambda this: this.PolicyNameLength),
        "RuleId" / Guid,
        "RuleNameLength" / Int16ul,
        "RuleNameBuffer" / Bytes(lambda this: this.RuleNameLength),
        "RuleSddlLength" / Int16ul,
        "RuleSddlBuffer" / Bytes(lambda this: this.RuleSddlLength),
        "TargetUser" / Sid,
        "TargetProcessId" / Int32ul,
        "FilePathLength" / Int16ul,
        "FilePathBuffer" / Bytes(lambda this: this.FilePathLength),
        "FileHashLength" / Int16ul,
        "FileHash" / Bytes(lambda this: this.FileHashLength),
        "FqbnLength" / Int16ul,
        "Fqbn" / Bytes(lambda this: this.FqbnLength),
        "TargetLogonId" / Int64ul,
        "FullFilePathLength" / Int16ul,
        "FullFilePathBuffer" / Bytes(lambda this: this.FullFilePathLength)
    )


@declare(guid=guid("cbda4dbf-8d5d-4f69-9578-be14aa540d22"), event_id=8006, version=0)
class Microsoft_Windows_AppLocker_8006_0(Etw):
    pattern = Struct(
        "PolicyNameLength" / Int16ul,
        "PolicyNameBuffer" / Bytes(lambda this: this.PolicyNameLength),
        "RuleId" / Guid,
        "RuleNameLength" / Int16ul,
        "RuleNameBuffer" / Bytes(lambda this: this.RuleNameLength),
        "RuleSddlLength" / Int16ul,
        "RuleSddlBuffer" / Bytes(lambda this: this.RuleSddlLength),
        "TargetUser" / Sid,
        "TargetProcessId" / Int32ul,
        "FilePathLength" / Int16ul,
        "FilePathBuffer" / Bytes(lambda this: this.FilePathLength),
        "FileHashLength" / Int16ul,
        "FileHash" / Bytes(lambda this: this.FileHashLength),
        "FqbnLength" / Int16ul,
        "Fqbn" / Bytes(lambda this: this.FqbnLength),
        "TargetLogonId" / Int64ul,
        "FullFilePathLength" / Int16ul,
        "FullFilePathBuffer" / Bytes(lambda this: this.FullFilePathLength)
    )


@declare(guid=guid("cbda4dbf-8d5d-4f69-9578-be14aa540d22"), event_id=8007, version=0)
class Microsoft_Windows_AppLocker_8007_0(Etw):
    pattern = Struct(
        "PolicyNameLength" / Int16ul,
        "PolicyNameBuffer" / Bytes(lambda this: this.PolicyNameLength),
        "RuleId" / Guid,
        "RuleNameLength" / Int16ul,
        "RuleNameBuffer" / Bytes(lambda this: this.RuleNameLength),
        "RuleSddlLength" / Int16ul,
        "RuleSddlBuffer" / Bytes(lambda this: this.RuleSddlLength),
        "TargetUser" / Sid,
        "TargetProcessId" / Int32ul,
        "FilePathLength" / Int16ul,
        "FilePathBuffer" / Bytes(lambda this: this.FilePathLength),
        "FileHashLength" / Int16ul,
        "FileHash" / Bytes(lambda this: this.FileHashLength),
        "FqbnLength" / Int16ul,
        "Fqbn" / Bytes(lambda this: this.FqbnLength),
        "TargetLogonId" / Int64ul,
        "FullFilePathLength" / Int16ul,
        "FullFilePathBuffer" / Bytes(lambda this: this.FullFilePathLength)
    )


@declare(guid=guid("cbda4dbf-8d5d-4f69-9578-be14aa540d22"), event_id=8008, version=0)
class Microsoft_Windows_AppLocker_8008_0(Etw):
    pattern = Struct(
        "FilePathLength" / Int16ul,
        "FilePathBuffer" / Bytes(lambda this: this.FilePathLength)
    )


@declare(guid=guid("cbda4dbf-8d5d-4f69-9578-be14aa540d22"), event_id=8009, version=0)
class Microsoft_Windows_AppLocker_8009_0(Etw):
    pattern = Struct(
        "FilePathLength" / Int16ul,
        "FilePathBuffer" / Bytes(lambda this: this.FilePathLength)
    )


@declare(guid=guid("cbda4dbf-8d5d-4f69-9578-be14aa540d22"), event_id=8020, version=0)
class Microsoft_Windows_AppLocker_8020_0(Etw):
    pattern = Struct(
        "PolicyNameLength" / Int16ul,
        "PolicyNameBuffer" / Bytes(lambda this: this.PolicyNameLength),
        "RuleId" / Guid,
        "RuleNameLength" / Int16ul,
        "RuleNameBuffer" / Bytes(lambda this: this.RuleNameLength),
        "RuleSddlLength" / Int16ul,
        "RuleSddlBuffer" / Bytes(lambda this: this.RuleSddlLength),
        "TargetUser" / Sid,
        "TargetProcessId" / Int32ul,
        "PackageLength" / Int16ul,
        "PackageBuffer" / Bytes(lambda this: this.PackageLength),
        "FqbnLength" / Int16ul,
        "Fqbn" / Bytes(lambda this: this.FqbnLength)
    )


@declare(guid=guid("cbda4dbf-8d5d-4f69-9578-be14aa540d22"), event_id=8021, version=0)
class Microsoft_Windows_AppLocker_8021_0(Etw):
    pattern = Struct(
        "PolicyNameLength" / Int16ul,
        "PolicyNameBuffer" / Bytes(lambda this: this.PolicyNameLength),
        "RuleId" / Guid,
        "RuleNameLength" / Int16ul,
        "RuleNameBuffer" / Bytes(lambda this: this.RuleNameLength),
        "RuleSddlLength" / Int16ul,
        "RuleSddlBuffer" / Bytes(lambda this: this.RuleSddlLength),
        "TargetUser" / Sid,
        "TargetProcessId" / Int32ul,
        "PackageLength" / Int16ul,
        "PackageBuffer" / Bytes(lambda this: this.PackageLength),
        "FqbnLength" / Int16ul,
        "Fqbn" / Bytes(lambda this: this.FqbnLength)
    )


@declare(guid=guid("cbda4dbf-8d5d-4f69-9578-be14aa540d22"), event_id=8022, version=0)
class Microsoft_Windows_AppLocker_8022_0(Etw):
    pattern = Struct(
        "PolicyNameLength" / Int16ul,
        "PolicyNameBuffer" / Bytes(lambda this: this.PolicyNameLength),
        "RuleId" / Guid,
        "RuleNameLength" / Int16ul,
        "RuleNameBuffer" / Bytes(lambda this: this.RuleNameLength),
        "RuleSddlLength" / Int16ul,
        "RuleSddlBuffer" / Bytes(lambda this: this.RuleSddlLength),
        "TargetUser" / Sid,
        "TargetProcessId" / Int32ul,
        "PackageLength" / Int16ul,
        "PackageBuffer" / Bytes(lambda this: this.PackageLength),
        "FqbnLength" / Int16ul,
        "Fqbn" / Bytes(lambda this: this.FqbnLength)
    )


@declare(guid=guid("cbda4dbf-8d5d-4f69-9578-be14aa540d22"), event_id=8023, version=0)
class Microsoft_Windows_AppLocker_8023_0(Etw):
    pattern = Struct(
        "PolicyNameLength" / Int16ul,
        "PolicyNameBuffer" / Bytes(lambda this: this.PolicyNameLength),
        "RuleId" / Guid,
        "RuleNameLength" / Int16ul,
        "RuleNameBuffer" / Bytes(lambda this: this.RuleNameLength),
        "RuleSddlLength" / Int16ul,
        "RuleSddlBuffer" / Bytes(lambda this: this.RuleSddlLength),
        "TargetUser" / Sid,
        "TargetProcessId" / Int32ul,
        "PackageLength" / Int16ul,
        "PackageBuffer" / Bytes(lambda this: this.PackageLength),
        "FqbnLength" / Int16ul,
        "Fqbn" / Bytes(lambda this: this.FqbnLength)
    )


@declare(guid=guid("cbda4dbf-8d5d-4f69-9578-be14aa540d22"), event_id=8024, version=0)
class Microsoft_Windows_AppLocker_8024_0(Etw):
    pattern = Struct(
        "PolicyNameLength" / Int16ul,
        "PolicyNameBuffer" / Bytes(lambda this: this.PolicyNameLength),
        "RuleId" / Guid,
        "RuleNameLength" / Int16ul,
        "RuleNameBuffer" / Bytes(lambda this: this.RuleNameLength),
        "RuleSddlLength" / Int16ul,
        "RuleSddlBuffer" / Bytes(lambda this: this.RuleSddlLength),
        "TargetUser" / Sid,
        "TargetProcessId" / Int32ul,
        "PackageLength" / Int16ul,
        "PackageBuffer" / Bytes(lambda this: this.PackageLength),
        "FqbnLength" / Int16ul,
        "Fqbn" / Bytes(lambda this: this.FqbnLength)
    )


@declare(guid=guid("cbda4dbf-8d5d-4f69-9578-be14aa540d22"), event_id=8025, version=0)
class Microsoft_Windows_AppLocker_8025_0(Etw):
    pattern = Struct(
        "PolicyNameLength" / Int16ul,
        "PolicyNameBuffer" / Bytes(lambda this: this.PolicyNameLength),
        "RuleId" / Guid,
        "RuleNameLength" / Int16ul,
        "RuleNameBuffer" / Bytes(lambda this: this.RuleNameLength),
        "RuleSddlLength" / Int16ul,
        "RuleSddlBuffer" / Bytes(lambda this: this.RuleSddlLength),
        "TargetUser" / Sid,
        "TargetProcessId" / Int32ul,
        "PackageLength" / Int16ul,
        "PackageBuffer" / Bytes(lambda this: this.PackageLength),
        "FqbnLength" / Int16ul,
        "Fqbn" / Bytes(lambda this: this.FqbnLength)
    )


@declare(guid=guid("cbda4dbf-8d5d-4f69-9578-be14aa540d22"), event_id=8028, version=0)
class Microsoft_Windows_AppLocker_8028_0(Etw):
    pattern = Struct(
        "FilePathLength" / Int16ul,
        "FilePath" / Bytes(lambda this: this.FilePathLength),
        "Result" / Int32sl,
        "USN" / Int64sl,
        "UserWriteable" / Int8ul
    )


@declare(guid=guid("cbda4dbf-8d5d-4f69-9578-be14aa540d22"), event_id=8029, version=0)
class Microsoft_Windows_AppLocker_8029_0(Etw):
    pattern = Struct(
        "FilePathLength" / Int16ul,
        "FilePath" / Bytes(lambda this: this.FilePathLength),
        "Result" / Int32sl,
        "USN" / Int64sl,
        "UserWriteable" / Int8ul
    )


@declare(guid=guid("cbda4dbf-8d5d-4f69-9578-be14aa540d22"), event_id=8030, version=0)
class Microsoft_Windows_AppLocker_8030_0(Etw):
    pattern = Struct(
        "ImageNameLength" / Int16ul,
        "ImageName" / Bytes(lambda this: this.ImageNameLength),
        "ParentProcessLength" / Int16ul,
        "ParentProcess" / Bytes(lambda this: this.ParentProcessLength),
        "StatusCode" / Int32ul,
        "AppLockerReason" / Int32ul,
        "Bucket" / Int32ul,
        "USN" / Int64ul,
        "NtfsFileIdSize" / Int16ul,
        "NtfsFileId" / Bytes(lambda this: this.NtfsFileIdSize),
        "OriginDataPresent" / Int8ul,
        "SessionId" / Guid,
        "SubSessionId" / Guid,
        "Origin" / Int32ul,
        "Type" / Int32ul,
        "Generation" / Int32ul,
        "SmartScreen" / Int32ul,
        "RevocationID" / Int32ul,
        "DataLength" / Int16ul,
        "Data" / Bytes(lambda this: this.DataLength)
    )


@declare(guid=guid("cbda4dbf-8d5d-4f69-9578-be14aa540d22"), event_id=8031, version=0)
class Microsoft_Windows_AppLocker_8031_0(Etw):
    pattern = Struct(
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "CurrentProcessLength" / Int16ul,
        "CurrentProcess" / Bytes(lambda this: this.CurrentProcessLength),
        "ParentProcessLength" / Int16ul,
        "ParentProcess" / Bytes(lambda this: this.ParentProcessLength),
        "USN" / Int64ul,
        "NtfsFileIdSize" / Int16ul,
        "NtfsFileId" / Bytes(lambda this: this.NtfsFileIdSize),
        "OriginDataPresent" / Int8ul,
        "SessionId" / Guid,
        "Origin" / Int32ul,
        "Type" / Int32ul,
        "Generation" / Int32ul,
        "SmartScreen" / Int32ul,
        "DataLength" / Int16ul,
        "Data" / Bytes(lambda this: this.DataLength)
    )


@declare(guid=guid("cbda4dbf-8d5d-4f69-9578-be14aa540d22"), event_id=8032, version=0)
class Microsoft_Windows_AppLocker_8032_0(Etw):
    pattern = Struct(
        "ImageNameLength" / Int16ul,
        "ImageName" / Bytes(lambda this: this.ImageNameLength),
        "ParentProcessLength" / Int16ul,
        "ParentProcess" / Bytes(lambda this: this.ParentProcessLength),
        "StatusCode" / Int32ul,
        "AppLockerReason" / Int32ul,
        "Bucket" / Int32ul,
        "USN" / Int64ul,
        "NtfsFileIdSize" / Int16ul,
        "NtfsFileId" / Bytes(lambda this: this.NtfsFileIdSize),
        "OriginDataPresent" / Int8ul,
        "SessionId" / Guid,
        "SubSessionId" / Guid,
        "Origin" / Int32ul,
        "Type" / Int32ul,
        "Generation" / Int32ul,
        "SmartScreen" / Int32ul,
        "RevocationID" / Int32ul,
        "DataLength" / Int16ul,
        "Data" / Bytes(lambda this: this.DataLength)
    )


@declare(guid=guid("cbda4dbf-8d5d-4f69-9578-be14aa540d22"), event_id=8033, version=0)
class Microsoft_Windows_AppLocker_8033_0(Etw):
    pattern = Struct(
        "ImageNameLength" / Int16ul,
        "ImageName" / Bytes(lambda this: this.ImageNameLength),
        "ParentProcessLength" / Int16ul,
        "ParentProcess" / Bytes(lambda this: this.ParentProcessLength),
        "StatusCode" / Int32ul,
        "AppLockerReason" / Int32ul,
        "Bucket" / Int32ul,
        "USN" / Int64ul,
        "NtfsFileIdSize" / Int16ul,
        "NtfsFileId" / Bytes(lambda this: this.NtfsFileIdSize),
        "OriginDataPresent" / Int8ul,
        "SessionId" / Guid,
        "SubSessionId" / Guid,
        "Origin" / Int32ul,
        "Type" / Int32ul,
        "Generation" / Int32ul,
        "SmartScreen" / Int32ul,
        "RevocationID" / Int32ul,
        "DataLength" / Int16ul,
        "Data" / Bytes(lambda this: this.DataLength)
    )


@declare(guid=guid("cbda4dbf-8d5d-4f69-9578-be14aa540d22"), event_id=8034, version=0)
class Microsoft_Windows_AppLocker_8034_0(Etw):
    pattern = Struct(
        "ImageNameLength" / Int16ul,
        "ImageName" / Bytes(lambda this: this.ImageNameLength),
        "StatusCode" / Int32ul,
        "Bucket" / Int32ul,
        "OriginDataPresent" / Int8ul,
        "SessionId" / Guid,
        "SubSessionId" / Guid,
        "Origin" / Int32ul,
        "Type" / Int32ul,
        "Generation" / Int32ul,
        "SmartScreen" / Int32ul,
        "RevocationID" / Int32ul,
        "DataLength" / Int16ul,
        "Data" / Bytes(lambda this: this.DataLength)
    )


@declare(guid=guid("cbda4dbf-8d5d-4f69-9578-be14aa540d22"), event_id=8035, version=0)
class Microsoft_Windows_AppLocker_8035_0(Etw):
    pattern = Struct(
        "ImageNameLength" / Int16ul,
        "ImageName" / Bytes(lambda this: this.ImageNameLength),
        "StatusCode" / Int32ul,
        "Bucket" / Int32ul,
        "OriginDataPresent" / Int8ul,
        "SessionId" / Guid,
        "SubSessionId" / Guid,
        "Origin" / Int32ul,
        "Type" / Int32ul,
        "Generation" / Int32ul,
        "SmartScreen" / Int32ul,
        "RevocationID" / Int32ul,
        "DataLength" / Int16ul,
        "Data" / Bytes(lambda this: this.DataLength)
    )


@declare(guid=guid("cbda4dbf-8d5d-4f69-9578-be14aa540d22"), event_id=8036, version=0)
class Microsoft_Windows_AppLocker_8036_0(Etw):
    pattern = Struct(
        "IsApproved" / Int8ul,
        "CLSID" / Guid
    )


@declare(guid=guid("cbda4dbf-8d5d-4f69-9578-be14aa540d22"), event_id=8037, version=0)
class Microsoft_Windows_AppLocker_8037_0(Etw):
    pattern = Struct(
        "FilePathLength" / Int16ul,
        "FilePath" / Bytes(lambda this: this.FilePathLength),
        "Result" / Int32sl,
        "USN" / Int64sl,
        "UserWriteable" / Int8ul
    )


@declare(guid=guid("cbda4dbf-8d5d-4f69-9578-be14aa540d22"), event_id=8038, version=0)
class Microsoft_Windows_AppLocker_8038_0(Etw):
    pattern = Struct(
        "TotalSignatureCount" / Int32ul,
        "Signature" / Int32ul,
        "PublisherNameLength" / Int16ul,
        "PublisherName" / Bytes(lambda this: this.PublisherNameLength),
        "IssuerNameLength" / Int16ul,
        "IssuerName" / Bytes(lambda this: this.IssuerNameLength),
        "PublisherTBSHashSize" / Int32ul,
        "PublisherTBSHash" / Bytes(lambda this: this.PublisherTBSHashSize),
        "IssuerTBSHashSize" / Int32ul,
        "IssuerTBSHash" / Bytes(lambda this: this.IssuerTBSHashSize)
    )

