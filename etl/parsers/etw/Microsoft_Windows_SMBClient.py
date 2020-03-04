# -*- coding: utf-8 -*-
"""
Microsoft-Windows-SMBClient
GUID : 988c59c5-0a1c-45b6-a555-0c62276e327d
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=101, version=0)
class Microsoft_Windows_SMBClient_101_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=201, version=0)
class Microsoft_Windows_SMBClient_201_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=301, version=0)
class Microsoft_Windows_SMBClient_301_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=401, version=0)
class Microsoft_Windows_SMBClient_401_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=501, version=0)
class Microsoft_Windows_SMBClient_501_0(Etw):
    pattern = Struct(
        "ErrorCode" / Int32ul,
        "Location" / Int32ul,
        "Context" / Int32ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=2000, version=0)
class Microsoft_Windows_SMBClient_2000_0(Etw):
    pattern = Struct(
        "ReassembledEventID" / Int16ul,
        "FragmentSize" / Int32ul,
        "FragmentData" / Bytes(lambda this: this.FragmentSize)
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=20001, version=0)
class Microsoft_Windows_SMBClient_20001_0(Etw):
    pattern = Struct(
        "CurrentOrNextState" / Int8ul,
        "Context" / Int32ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30103, version=0)
class Microsoft_Windows_SMBClient_30103_0(Etw):
    pattern = Struct(
        "RxContext" / Int64ul,
        "Exchange" / Int64ul,
        "ListHead" / Int64ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30104, version=0)
class Microsoft_Windows_SMBClient_30104_0(Etw):
    pattern = Struct(
        "RxContext" / Int64ul,
        "Exchange" / Int64ul,
        "ExchangeState" / Int32ul,
        "ExchangeStatus" / Int32ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30105, version=0)
class Microsoft_Windows_SMBClient_30105_0(Etw):
    pattern = Struct(
        "BufferCtxt" / Int64ul,
        "Exchange" / Int64ul,
        "MidCharge" / Int32ul,
        "Window" / Int64ul,
        "CurrentWindowLimit" / Int32ul,
        "ThrottlingWindowLimit" / Int32ul,
        "CurrentWindowSize" / Int32ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30106, version=0)
class Microsoft_Windows_SMBClient_30106_0(Etw):
    pattern = Struct(
        "BufferCtxt" / Int64ul,
        "Exchange" / Int64ul,
        "MidCharge" / Int32ul,
        "Window" / Int64ul,
        "CurrentWindowLimit" / Int32ul,
        "ThrottlingWindowLimit" / Int32ul,
        "CurrentWindowSize" / Int32ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30108, version=0)
class Microsoft_Windows_SMBClient_30108_0(Etw):
    pattern = Struct(
        "Window" / Int64ul,
        "HungSession" / Int32ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30109, version=0)
class Microsoft_Windows_SMBClient_30109_0(Etw):
    pattern = Struct(
        "BufferCtxt" / Int64ul,
        "Exchange" / Int64ul,
        "MidCharge" / Int32ul,
        "Window" / Int64ul,
        "CurrentWindowLimit" / Int32ul,
        "ThrottlingWindowLimit" / Int32ul,
        "CurrentWindowSize" / Int32ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30110, version=0)
class Microsoft_Windows_SMBClient_30110_0(Etw):
    pattern = Struct(
        "ServerNameLength" / Int16ul,
        "ServerName" / Bytes(lambda this: this.ServerNameLength),
        "MidWindow" / Int64ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30111, version=0)
class Microsoft_Windows_SMBClient_30111_0(Etw):
    pattern = Struct(
        "MidWindow" / Int64ul,
        "CurrentWindowSize" / Int32ul,
        "CurrentWindowLimit" / Int32ul,
        "ThrottlingWindowLimit" / Int32ul,
        "OldestPendingMid" / Int64ul,
        "NextAvailableMid" / Int64ul,
        "CreditsGranted" / Int32sl
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30112, version=0)
class Microsoft_Windows_SMBClient_30112_0(Etw):
    pattern = Struct(
        "ServerNameLength" / Int16ul,
        "ServerName" / Bytes(lambda this: this.ServerNameLength),
        "MidWindow" / Int64ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30113, version=0)
class Microsoft_Windows_SMBClient_30113_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "VcEndpoint" / Int64ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30114, version=0)
class Microsoft_Windows_SMBClient_30114_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "VcEndpoint" / Int64ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30203, version=0)
class Microsoft_Windows_SMBClient_30203_0(Etw):
    pattern = Struct(
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "VcEndpoint" / Int64ul,
        "Socket" / Int64ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30204, version=0)
class Microsoft_Windows_SMBClient_30204_0(Etw):
    pattern = Struct(
        "VcEndpoint" / Int64ul,
        "Socket" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30205, version=0)
class Microsoft_Windows_SMBClient_30205_0(Etw):
    pattern = Struct(
        "VcEndpoint" / Int64ul,
        "Socket" / Int64ul,
        "SendMdl" / Int64ul,
        "SendLength" / Int32ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30206, version=0)
class Microsoft_Windows_SMBClient_30206_0(Etw):
    pattern = Struct(
        "VcEndpoint" / Int64ul,
        "Socket" / Int64ul,
        "SendMdl" / Int64ul,
        "SendLength" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30207, version=0)
class Microsoft_Windows_SMBClient_30207_0(Etw):
    pattern = Struct(
        "VcEndpoint" / Int64ul,
        "Socket" / Int64ul,
        "SendMdl" / Int64ul,
        "SendLength" / Int32ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30208, version=0)
class Microsoft_Windows_SMBClient_30208_0(Etw):
    pattern = Struct(
        "VcEndpoint" / Int64ul,
        "Socket" / Int64ul,
        "SendMdl" / Int64ul,
        "SendLength" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30209, version=0)
class Microsoft_Windows_SMBClient_30209_0(Etw):
    pattern = Struct(
        "VcEndpoint" / Int64ul,
        "Socket" / Int64ul,
        "Smb2Fobx" / Int64ul,
        "Status" / Int32ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30210, version=0)
class Microsoft_Windows_SMBClient_30210_0(Etw):
    pattern = Struct(
        "VcEndpoint" / Int64ul,
        "Socket" / Int64ul,
        "SendMdl" / Int64ul,
        "SendLength" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30211, version=0)
class Microsoft_Windows_SMBClient_30211_0(Etw):
    pattern = Struct(
        "VcEndpoint" / Int64ul,
        "Socket" / Int64ul,
        "SendMdl" / Int64ul,
        "SendLength" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30401, version=0)
class Microsoft_Windows_SMBClient_30401_0(Etw):
    pattern = Struct(
        "SessionEntry" / Int64ul,
        "ServerNameLength" / Int16ul,
        "ServerName" / Bytes(lambda this: this.ServerNameLength)
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30402, version=0)
class Microsoft_Windows_SMBClient_30402_0(Etw):
    pattern = Struct(
        "SessionEntry" / Int64ul,
        "ServerNameLength" / Int16ul,
        "ServerName" / Bytes(lambda this: this.ServerNameLength)
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30403, version=0)
class Microsoft_Windows_SMBClient_30403_0(Etw):
    pattern = Struct(
        "Fcb" / Int64ul,
        "SrvOpen" / Int64ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30404, version=0)
class Microsoft_Windows_SMBClient_30404_0(Etw):
    pattern = Struct(
        "Fcb" / Int64ul,
        "SrvOpen" / Int64ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30405, version=0)
class Microsoft_Windows_SMBClient_30405_0(Etw):
    pattern = Struct(
        "Fcb" / Int64ul,
        "SrvOpen" / Int64ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30406, version=0)
class Microsoft_Windows_SMBClient_30406_0(Etw):
    pattern = Struct(
        "Count" / Int32ul,
        "Command" / CString,
        "MessageId" / Int64ul,
        "SessionId" / Int64ul,
        "TreeId" / Int32ul,
        "MidCharge" / Int16ul,
        "CreditRequested" / Int16ul,
        "SendLength" / Int32ul,
        "VcEndpoint" / Int64ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30407, version=0)
class Microsoft_Windows_SMBClient_30407_0(Etw):
    pattern = Struct(
        "Command" / CString,
        "MessageId" / Int64ul,
        "AsyncId" / Int64ul,
        "SessionId" / Int64ul,
        "TreeId" / Int32ul,
        "CreditGranted" / Int16ul,
        "Status" / Int32ul,
        "VcEndpoint" / Int64ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30408, version=0)
class Microsoft_Windows_SMBClient_30408_0(Etw):
    pattern = Struct(
        "Command" / CString,
        "MessageId" / Int64ul,
        "AsyncId" / Int64ul,
        "SessionId" / Int64ul,
        "TreeId" / Int32ul,
        "CreditGranted" / Int16ul,
        "Status" / Int32ul,
        "VcEndpoint" / Int64ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30409, version=0)
class Microsoft_Windows_SMBClient_30409_0(Etw):
    pattern = Struct(
        "Command" / CString,
        "MessageId" / Int64ul,
        "AsyncId" / Int64ul,
        "SessionId" / Int64ul,
        "TreeId" / Int32ul,
        "CreditGranted" / Int16ul,
        "Status" / Int32ul,
        "VcEndpoint" / Int64ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30410, version=0)
class Microsoft_Windows_SMBClient_30410_0(Etw):
    pattern = Struct(
        "RegName" / WString,
        "RegValue" / Int32ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30501, version=0)
class Microsoft_Windows_SMBClient_30501_0(Etw):
    pattern = Struct(
        "RxContext" / Int64ul,
        "Fcb" / Int64ul,
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "Status" / Int32ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30502, version=0)
class Microsoft_Windows_SMBClient_30502_0(Etw):
    pattern = Struct(
        "RxContext" / Int64ul,
        "Fcb" / Int64ul,
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "Status" / Int32ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30503, version=0)
class Microsoft_Windows_SMBClient_30503_0(Etw):
    pattern = Struct(
        "RxContext" / Int64ul,
        "Fcb" / Int64ul,
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "Status" / Int32ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30504, version=0)
class Microsoft_Windows_SMBClient_30504_0(Etw):
    pattern = Struct(
        "RxContext" / Int64ul,
        "Fcb" / Int64ul,
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "Status" / Int32ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30505, version=0)
class Microsoft_Windows_SMBClient_30505_0(Etw):
    pattern = Struct(
        "RxContext" / Int64ul,
        "Fcb" / Int64ul,
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "Status" / Int32ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30506, version=0)
class Microsoft_Windows_SMBClient_30506_0(Etw):
    pattern = Struct(
        "RxContext" / Int64ul,
        "Fcb" / Int64ul,
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "Status" / Int32ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30507, version=0)
class Microsoft_Windows_SMBClient_30507_0(Etw):
    pattern = Struct(
        "RxContext" / Int64ul,
        "Fcb" / Int64ul,
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "Status" / Int32ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30508, version=0)
class Microsoft_Windows_SMBClient_30508_0(Etw):
    pattern = Struct(
        "RxContext" / Int64ul,
        "Fcb" / Int64ul,
        "FileNameLength" / Int16ul,
        "FileName" / Bytes(lambda this: this.FileNameLength),
        "Status" / Int32ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30600, version=0)
class Microsoft_Windows_SMBClient_30600_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "OldState" / Int16ul,
        "NewState" / Int16ul,
        "Status" / Int32ul,
        "NameLength" / Int16ul,
        "ObjectName" / Bytes(lambda this: this.NameLength)
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30601, version=0)
class Microsoft_Windows_SMBClient_30601_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "OldState" / Int16ul,
        "NewState" / Int16ul,
        "Status" / Int32ul,
        "NameLength" / Int16ul,
        "ObjectName" / Bytes(lambda this: this.NameLength)
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30603, version=0)
class Microsoft_Windows_SMBClient_30603_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "PersistentFID" / Int64ul,
        "VolatileFID" / Int64ul,
        "CreateGUID" / Guid,
        "OldState" / Int16ul,
        "NewState" / Int16ul,
        "Status" / Int32ul,
        "Reason" / Int32ul,
        "ShareNameLength" / Int16ul,
        "ShareName" / Bytes(lambda this: this.ShareNameLength),
        "ObjectNameLength" / Int16ul,
        "ObjectName" / Bytes(lambda this: this.ObjectNameLength),
        "PreviousStatus" / Int32ul,
        "PreviousReason" / Int32ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30604, version=0)
class Microsoft_Windows_SMBClient_30604_0(Etw):
    pattern = Struct(
        "Days" / Int32ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30611, version=2)
class Microsoft_Windows_SMBClient_30611_2(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "PersistentFID" / Int64ul,
        "VolatileFID" / Int64ul,
        "CreateGUID" / Guid,
        "OldState" / Int16ul,
        "NewState" / Int16ul,
        "Status" / Int32ul,
        "Reason" / Int32ul,
        "ShareNameLength" / Int16ul,
        "ShareName" / Bytes(lambda this: this.ShareNameLength),
        "ObjectNameLength" / Int16ul,
        "ObjectName" / Bytes(lambda this: this.ObjectNameLength),
        "PreviousStatus" / Int32ul,
        "PreviousReason" / Int32ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30612, version=2)
class Microsoft_Windows_SMBClient_30612_2(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "PersistentFID" / Int64ul,
        "VolatileFID" / Int64ul,
        "CreateGUID" / Guid,
        "OldState" / Int16ul,
        "NewState" / Int16ul,
        "Status" / Int32ul,
        "Reason" / Int32ul,
        "ShareNameLength" / Int16ul,
        "ShareName" / Bytes(lambda this: this.ShareNameLength),
        "ObjectNameLength" / Int16ul,
        "ObjectName" / Bytes(lambda this: this.ObjectNameLength),
        "PreviousStatus" / Int32ul,
        "PreviousReason" / Int32ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30613, version=0)
class Microsoft_Windows_SMBClient_30613_0(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "PersistentFID" / Int64ul,
        "VolatileFID" / Int64ul,
        "CreateGUID" / Guid,
        "OldState" / Int16ul,
        "NewState" / Int16ul,
        "Status" / Int32ul,
        "Reason" / Int32ul,
        "ShareNameLength" / Int16ul,
        "ShareName" / Bytes(lambda this: this.ShareNameLength),
        "ObjectNameLength" / Int16ul,
        "ObjectName" / Bytes(lambda this: this.ObjectNameLength),
        "PreviousStatus" / Int32ul,
        "PreviousReason" / Int32ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30701, version=0)
class Microsoft_Windows_SMBClient_30701_0(Etw):
    pattern = Struct(
        "ServerNameLength" / Int16ul,
        "ServerName" / Bytes(lambda this: this.ServerNameLength)
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30702, version=0)
class Microsoft_Windows_SMBClient_30702_0(Etw):
    pattern = Struct(
        "ServerNameLength" / Int16ul,
        "ServerName" / Bytes(lambda this: this.ServerNameLength),
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "Status" / Int32ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30703, version=0)
class Microsoft_Windows_SMBClient_30703_0(Etw):
    pattern = Struct(
        "ServerNameLength" / Int16ul,
        "ServerName" / Bytes(lambda this: this.ServerNameLength),
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "Status" / Int32ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30704, version=0)
class Microsoft_Windows_SMBClient_30704_0(Etw):
    pattern = Struct(
        "ServerNameLength" / Int16ul,
        "ServerName" / Bytes(lambda this: this.ServerNameLength),
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "Status" / Int32ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30705, version=0)
class Microsoft_Windows_SMBClient_30705_0(Etw):
    pattern = Struct(
        "ServerNameLength" / Int16ul,
        "ServerName" / Bytes(lambda this: this.ServerNameLength),
        "LocalAddressLength" / Int32ul,
        "LocalAddress" / Bytes(lambda this: this.LocalAddressLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength),
        "Status" / Int32ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30800, version=0)
class Microsoft_Windows_SMBClient_30800_0(Etw):
    pattern = Struct(
        "Reason" / Int32ul,
        "Status" / Int32ul,
        "ServerNameLength" / Int16ul,
        "ServerName" / Bytes(lambda this: this.ServerNameLength)
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30801, version=0)
class Microsoft_Windows_SMBClient_30801_0(Etw):
    pattern = Struct(
        "Reason" / Int32ul,
        "Status" / Int32ul,
        "ServerNameLength" / Int16ul,
        "ServerName" / Bytes(lambda this: this.ServerNameLength)
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30802, version=0)
class Microsoft_Windows_SMBClient_30802_0(Etw):
    pattern = Struct(
        "Reason" / Int32ul,
        "Status" / Int32ul,
        "ServerNameLength" / Int16ul,
        "ServerName" / Bytes(lambda this: this.ServerNameLength)
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30803, version=0)
class Microsoft_Windows_SMBClient_30803_0(Etw):
    pattern = Struct(
        "Reason" / Int32ul,
        "Status" / Int32ul,
        "ServerNameLength" / Int16ul,
        "ServerName" / Bytes(lambda this: this.ServerNameLength),
        "AddressLength" / Int32ul,
        "Address" / Bytes(lambda this: this.AddressLength),
        "ConnectionType" / Int32ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30803, version=2)
class Microsoft_Windows_SMBClient_30803_2(Etw):
    pattern = Struct(
        "Reason" / Int32ul,
        "Status" / Int32ul,
        "ServerNameLength" / Int16ul,
        "ServerName" / Bytes(lambda this: this.ServerNameLength),
        "AddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.AddressLength),
        "LocalAddress" / Bytes(lambda this: this.AddressLength),
        "InstanceNameLength" / Int16ul,
        "InstanceName" / Bytes(lambda this: this.InstanceNameLength),
        "ConnectionType" / Int32ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30804, version=0)
class Microsoft_Windows_SMBClient_30804_0(Etw):
    pattern = Struct(
        "Reason" / Int32ul,
        "Status" / Int32ul,
        "ServerNameLength" / Int16ul,
        "ServerName" / Bytes(lambda this: this.ServerNameLength),
        "AddressLength" / Int32ul,
        "Address" / Bytes(lambda this: this.AddressLength),
        "ConnectionType" / Int32ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30805, version=2)
class Microsoft_Windows_SMBClient_30805_2(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "SessionId" / Int64ul,
        "TreeId" / Int32ul,
        "ServerNameLength" / Int16ul,
        "ServerName" / Bytes(lambda this: this.ServerNameLength),
        "AddressLength" / Int32ul,
        "Address" / Bytes(lambda this: this.AddressLength)
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30806, version=2)
class Microsoft_Windows_SMBClient_30806_2(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "SessionId" / Int64ul,
        "TreeId" / Int32ul,
        "ServerNameLength" / Int16ul,
        "ServerName" / Bytes(lambda this: this.ServerNameLength),
        "AddressLength" / Int32ul,
        "Address" / Bytes(lambda this: this.AddressLength)
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30807, version=2)
class Microsoft_Windows_SMBClient_30807_2(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "SessionId" / Int64ul,
        "TreeId" / Int32ul,
        "ServerNameLength" / Int16ul,
        "ServerName" / Bytes(lambda this: this.ServerNameLength),
        "AddressLength" / Int32ul,
        "Address" / Bytes(lambda this: this.AddressLength)
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30808, version=2)
class Microsoft_Windows_SMBClient_30808_2(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "SessionId" / Int64ul,
        "TreeId" / Int32ul,
        "ServerNameLength" / Int16ul,
        "ServerName" / Bytes(lambda this: this.ServerNameLength),
        "AddressLength" / Int32ul,
        "Address" / Bytes(lambda this: this.AddressLength)
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30809, version=0)
class Microsoft_Windows_SMBClient_30809_0(Etw):
    pattern = Struct(
        "Smb2Command" / Int16ul,
        "MessageId" / Int64ul,
        "SessionId" / Int64ul,
        "TreeId" / Int32ul,
        "ServerNameLength" / Int16ul,
        "ServerName" / Bytes(lambda this: this.ServerNameLength),
        "Status" / Int32ul,
        "InstanceNameLength" / Int16ul,
        "InstanceName" / Bytes(lambda this: this.InstanceNameLength),
        "RetryCount" / Int32ul,
        "ElapsedTimeInMs" / Int32ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30810, version=0)
class Microsoft_Windows_SMBClient_30810_0(Etw):
    pattern = Struct(
        "NameLength" / Int16ul,
        "Name" / Bytes(lambda this: this.NameLength),
        "IfIndex" / Int32ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30811, version=0)
class Microsoft_Windows_SMBClient_30811_0(Etw):
    pattern = Struct(
        "NameLength" / Int16ul,
        "Name" / Bytes(lambda this: this.NameLength),
        "IfIndex" / Int32ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30812, version=0)
class Microsoft_Windows_SMBClient_30812_0(Etw):
    pattern = Struct(
        "ServerNameLength" / Int16ul,
        "ServerName" / Bytes(lambda this: this.ServerNameLength)
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30813, version=0)
class Microsoft_Windows_SMBClient_30813_0(Etw):
    pattern = Struct(
        "ServerNameLength" / Int16ul,
        "ServerName" / Bytes(lambda this: this.ServerNameLength)
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30814, version=0)
class Microsoft_Windows_SMBClient_30814_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "ShareType" / Int8ul,
        "NameLength" / Int16ul,
        "Name" / Bytes(lambda this: this.NameLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength)
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30815, version=0)
class Microsoft_Windows_SMBClient_30815_0(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "ShareType" / Int8ul,
        "NameLength" / Int16ul,
        "Name" / Bytes(lambda this: this.NameLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength)
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30816, version=0)
class Microsoft_Windows_SMBClient_30816_0(Etw):
    pattern = Struct(
        "Reason" / Int32ul,
        "Status" / Int32ul,
        "ServerNameLength" / Int16ul,
        "ServerName" / Bytes(lambda this: this.ServerNameLength)
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30817, version=0)
class Microsoft_Windows_SMBClient_30817_0(Etw):
    pattern = Struct(
        "Reason" / Int32ul,
        "Status" / Int32ul,
        "ShareNameLength" / Int16ul,
        "ShareName" / Bytes(lambda this: this.ShareNameLength),
        "ObjectNameLength" / Int16ul,
        "ObjectName" / Bytes(lambda this: this.ObjectNameLength)
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30818, version=0)
class Microsoft_Windows_SMBClient_30818_0(Etw):
    pattern = Struct(
        "ServerNameLength" / Int16ul,
        "ServerName" / Bytes(lambda this: this.ServerNameLength)
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30819, version=2)
class Microsoft_Windows_SMBClient_30819_2(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "ShareType" / Int8ul,
        "NameLength" / Int16ul,
        "Name" / Bytes(lambda this: this.NameLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength)
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30820, version=2)
class Microsoft_Windows_SMBClient_30820_2(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "ShareType" / Int8ul,
        "NameLength" / Int16ul,
        "Name" / Bytes(lambda this: this.NameLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength)
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30821, version=2)
class Microsoft_Windows_SMBClient_30821_2(Etw):
    pattern = Struct(
        "Status" / Int32ul,
        "ShareType" / Int8ul,
        "NameLength" / Int16ul,
        "Name" / Bytes(lambda this: this.NameLength),
        "RemoteAddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.RemoteAddressLength)
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30822, version=0)
class Microsoft_Windows_SMBClient_30822_0(Etw):
    pattern = Struct(
        "Reason" / Int32ul,
        "Status" / Int32ul,
        "ServerNameLength" / Int16ul,
        "ServerName" / Bytes(lambda this: this.ServerNameLength),
        "AddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.AddressLength),
        "LocalAddress" / Bytes(lambda this: this.AddressLength),
        "InstanceNameLength" / Int16ul,
        "InstanceName" / Bytes(lambda this: this.InstanceNameLength),
        "ConnectionType" / Int32ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30823, version=2)
class Microsoft_Windows_SMBClient_30823_2(Etw):
    pattern = Struct(
        "Reason" / Int32ul,
        "Status" / Int32ul,
        "ServerNameLength" / Int16ul,
        "ServerName" / Bytes(lambda this: this.ServerNameLength),
        "AddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.AddressLength),
        "LocalAddress" / Bytes(lambda this: this.AddressLength),
        "InstanceNameLength" / Int16ul,
        "InstanceName" / Bytes(lambda this: this.InstanceNameLength),
        "ConnectionType" / Int32ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30824, version=1)
class Microsoft_Windows_SMBClient_30824_1(Etw):
    pattern = Struct(
        "Reason" / Int32ul,
        "Status" / Int32ul,
        "ServerNameLength" / Int16ul,
        "ServerName" / Bytes(lambda this: this.ServerNameLength),
        "AddressLength" / Int32ul,
        "RemoteAddress" / Bytes(lambda this: this.AddressLength),
        "LocalAddress" / Bytes(lambda this: this.AddressLength),
        "InstanceNameLength" / Int16ul,
        "InstanceName" / Bytes(lambda this: this.InstanceNameLength),
        "ConnectionType" / Int32ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30825, version=1)
class Microsoft_Windows_SMBClient_30825_1(Etw):
    pattern = Struct(
        "Reason" / Int32ul,
        "ServerNameLength" / Int16ul,
        "ServerName" / Bytes(lambda this: this.ServerNameLength),
        "InstanceNameLength" / Int16ul,
        "InstanceName" / Bytes(lambda this: this.InstanceNameLength)
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30900, version=2)
class Microsoft_Windows_SMBClient_30900_2(Etw):
    pattern = Struct(
        "Object" / Int64ul,
        "PersistentFID" / Int64ul,
        "VolatileFID" / Int64ul,
        "CreateGUID" / Guid,
        "OldState" / Int16ul,
        "NewState" / Int16ul,
        "Status" / Int32ul,
        "Reason" / Int32ul,
        "ShareNameLength" / Int16ul,
        "ShareName" / Bytes(lambda this: this.ShareNameLength),
        "ObjectNameLength" / Int16ul,
        "ObjectName" / Bytes(lambda this: this.ObjectNameLength),
        "PreviousStatus" / Int32ul,
        "PreviousReason" / Int32ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30904, version=2)
class Microsoft_Windows_SMBClient_30904_2(Etw):
    pattern = Struct(
        "ServerNameLength" / Int16ul,
        "ServerName" / Bytes(lambda this: this.ServerNameLength)
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30905, version=2)
class Microsoft_Windows_SMBClient_30905_2(Etw):
    pattern = Struct(
        "ServerNameLength" / Int16ul,
        "ServerName" / Bytes(lambda this: this.ServerNameLength)
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30906, version=0)
class Microsoft_Windows_SMBClient_30906_0(Etw):
    pattern = Struct(
        "IrpCode" / Int8ul,
        "RestartCount" / Int32ul,
        "ShareNameLength" / Int16ul,
        "ShareName" / Bytes(lambda this: this.ShareNameLength),
        "ObjectNameLength" / Int16ul,
        "ObjectName" / Bytes(lambda this: this.ObjectNameLength),
        "Status" / Int32ul,
        "Reason" / Int32ul,
        "HistoryCount" / Int32ul,
        "HistoryEntry" / Int64ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30907, version=0)
class Microsoft_Windows_SMBClient_30907_0(Etw):
    pattern = Struct(
        "RegName" / WString,
        "RegValue" / Int32ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30908, version=0)
class Microsoft_Windows_SMBClient_30908_0(Etw):
    pattern = Struct(
        "RegName" / WString,
        "RegValue" / Int32ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30909, version=0)
class Microsoft_Windows_SMBClient_30909_0(Etw):
    pattern = Struct(
        "ServerNameLength" / Int16ul,
        "ServerName" / Bytes(lambda this: this.ServerNameLength)
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30910, version=0)
class Microsoft_Windows_SMBClient_30910_0(Etw):
    pattern = Struct(
        "ServerNameLength" / Int16ul,
        "ServerName" / Bytes(lambda this: this.ServerNameLength)
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=30911, version=0)
class Microsoft_Windows_SMBClient_30911_0(Etw):
    pattern = Struct(
        "CipherSuiteOrder" / WString
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=31000, version=0)
class Microsoft_Windows_SMBClient_31000_0(Etw):
    pattern = Struct(
        "Reason" / Int32ul,
        "Status" / Int32ul,
        "SecurityStatus" / Int32ul,
        "LogonId" / Int64ul,
        "ServerNameLength" / Int16ul,
        "ServerName" / Bytes(lambda this: this.ServerNameLength),
        "PrincipalNameLength" / Int16ul,
        "PrincipalName" / Bytes(lambda this: this.PrincipalNameLength),
        "UserNameLength" / Int16ul,
        "UserName" / Bytes(lambda this: this.UserNameLength)
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=31001, version=0)
class Microsoft_Windows_SMBClient_31001_0(Etw):
    pattern = Struct(
        "Reason" / Int32ul,
        "Status" / Int32ul,
        "SecurityStatus" / Int32ul,
        "LogonId" / Int64ul,
        "ServerNameLength" / Int16ul,
        "ServerName" / Bytes(lambda this: this.ServerNameLength),
        "PrincipalNameLength" / Int16ul,
        "PrincipalName" / Bytes(lambda this: this.PrincipalNameLength),
        "UserNameLength" / Int16ul,
        "UserName" / Bytes(lambda this: this.UserNameLength)
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=31002, version=0)
class Microsoft_Windows_SMBClient_31002_0(Etw):
    pattern = Struct(
        "Reason" / Int32ul,
        "Status" / Int32ul,
        "ServerNameLength" / Int16ul,
        "ServerName" / Bytes(lambda this: this.ServerNameLength)
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=31003, version=0)
class Microsoft_Windows_SMBClient_31003_0(Etw):
    pattern = Struct(
        "RegName" / WString,
        "RegValue" / Int32ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=31010, version=0)
class Microsoft_Windows_SMBClient_31010_0(Etw):
    pattern = Struct(
        "Reason" / Int32ul,
        "Status" / Int32ul,
        "ShareNameLength" / Int16ul,
        "ShareName" / Bytes(lambda this: this.ShareNameLength),
        "ObjectNameLength" / Int16ul,
        "ObjectName" / Bytes(lambda this: this.ObjectNameLength)
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=31012, version=0)
class Microsoft_Windows_SMBClient_31012_0(Etw):
    pattern = Struct(
        "Dialect" / Int16ul,
        "SecurityMode" / Int16ul,
        "Capabilities" / Int32ul,
        "Guid" / Guid,
        "Dialect2" / Int16ul,
        "SecurityMode2" / Int16ul,
        "Capabilities2" / Int32ul,
        "Guid2" / Guid
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=31013, version=0)
class Microsoft_Windows_SMBClient_31013_0(Etw):
    pattern = Struct(
        "Smb2Command" / Int16ul,
        "MessageId" / Int64ul,
        "SessionId" / Int64ul,
        "TreeId" / Int32ul,
        "ServerNameLength" / Int16ul,
        "ServerName" / Bytes(lambda this: this.ServerNameLength),
        "Status" / Int32ul,
        "MessageSize" / Int32ul,
        "FragmentOffset" / Int32ul,
        "FragmentSize" / Int32ul,
        "FragmentData" / Bytes(lambda this: this.FragmentSize)
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=31014, version=0)
class Microsoft_Windows_SMBClient_31014_0(Etw):
    pattern = Struct(
        "Smb2Command" / Int16ul,
        "MessageId" / Int64ul,
        "SessionId" / Int64ul,
        "TreeId" / Int32ul,
        "ServerNameLength" / Int16ul,
        "ServerName" / Bytes(lambda this: this.ServerNameLength),
        "Status" / Int32ul,
        "InstanceNameLength" / Int16ul,
        "InstanceName" / Bytes(lambda this: this.InstanceNameLength),
        "RetryCount" / Int32ul,
        "ElapsedTimeInMs" / Int32ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=31015, version=0)
class Microsoft_Windows_SMBClient_31015_0(Etw):
    pattern = Struct(
        "Smb2Command" / Int16ul,
        "MessageId" / Int64ul,
        "SessionId" / Int64ul,
        "TreeId" / Int32ul,
        "ServerNameLength" / Int16ul,
        "ServerName" / Bytes(lambda this: this.ServerNameLength),
        "Status" / Int32ul,
        "InstanceNameLength" / Int16ul,
        "InstanceName" / Bytes(lambda this: this.InstanceNameLength),
        "RetryCount" / Int32ul,
        "ElapsedTimeInMs" / Int32ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=31016, version=0)
class Microsoft_Windows_SMBClient_31016_0(Etw):
    pattern = Struct(
        "RegName" / WString,
        "RegValue" / Int32ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=31017, version=0)
class Microsoft_Windows_SMBClient_31017_0(Etw):
    pattern = Struct(
        "UserNameLength" / Int16ul,
        "UserName" / Bytes(lambda this: this.UserNameLength),
        "ServerNameLength" / Int16ul,
        "ServerName" / Bytes(lambda this: this.ServerNameLength)
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=31018, version=0)
class Microsoft_Windows_SMBClient_31018_0(Etw):
    pattern = Struct(
        "RegName" / WString,
        "RegValue" / Int32ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=31019, version=0)
class Microsoft_Windows_SMBClient_31019_0(Etw):
    pattern = Struct(
        "Reason" / Int32ul,
        "Status" / Int32ul,
        "SecurityStatus" / Int32ul,
        "LogonId" / Int64ul,
        "ServerNameLength" / Int16ul,
        "ServerName" / Bytes(lambda this: this.ServerNameLength),
        "UserNameLength" / Int16ul,
        "UserName" / Bytes(lambda this: this.UserNameLength),
        "OldAuthProtocolId" / Int16ul,
        "NewAuthProtocolId" / Int16ul,
        "OldMutualAuthState" / Int8ul,
        "NewMutualAuthState" / Int8ul,
        "ClusteredServer" / Int8ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=32000, version=0)
class Microsoft_Windows_SMBClient_32000_0(Etw):
    pattern = Struct(
        "Reason" / Int32ul,
        "Dialect" / Int16ul,
        "ServerNameLength" / Int16ul,
        "ServerName" / Bytes(lambda this: this.ServerNameLength)
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=32002, version=0)
class Microsoft_Windows_SMBClient_32002_0(Etw):
    pattern = Struct(
        "Reason" / Int32ul,
        "Dialect" / Int16ul,
        "SecurityMode" / Int16ul,
        "ServerNameLength" / Int16ul,
        "ServerName" / Bytes(lambda this: this.ServerNameLength)
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=32003, version=0)
class Microsoft_Windows_SMBClient_32003_0(Etw):
    pattern = Struct(
        "Days" / Int32ul
    )


@declare(guid=guid("988c59c5-0a1c-45b6-a555-0c62276e327d"), event_id=40000, version=0)
class Microsoft_Windows_SMBClient_40000_0(Etw):
    pattern = Struct(
        "ConnectionType" / Int32ul,
        "PeerAddressLength" / Int32ul,
        "PeerAddress" / Bytes(lambda this: this.PeerAddressLength),
        "PacketSize" / Int32ul,
        "PacketData" / Bytes(lambda this: this.PacketSize)
    )

