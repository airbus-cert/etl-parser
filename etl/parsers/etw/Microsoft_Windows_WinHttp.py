# -*- coding: utf-8 -*-
"""
Microsoft-Windows-WinHttp
GUID : 7d44233d-3055-4b9c-ba64-0d47ca40a232
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("7d44233d-3055-4b9c-ba64-0d47ca40a232"), event_id=1, version=0)
class Microsoft_Windows_WinHttp_1_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("7d44233d-3055-4b9c-ba64-0d47ca40a232"), event_id=2, version=0)
class Microsoft_Windows_WinHttp_2_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("7d44233d-3055-4b9c-ba64-0d47ca40a232"), event_id=4, version=0)
class Microsoft_Windows_WinHttp_4_0(Etw):
    pattern = Struct(
        "loadunloadinfo" / WString
    )


@declare(guid=guid("7d44233d-3055-4b9c-ba64-0d47ca40a232"), event_id=9, version=0)
class Microsoft_Windows_WinHttp_9_0(Etw):
    pattern = Struct(
        "ApiHandle" / Int64ul,
        "Api" / CString
    )


@declare(guid=guid("7d44233d-3055-4b9c-ba64-0d47ca40a232"), event_id=10, version=0)
class Microsoft_Windows_WinHttp_10_0(Etw):
    pattern = Struct(
        "ApiHandle" / Int64ul,
        "Api" / CString,
        "Result" / Int32ul
    )


@declare(guid=guid("7d44233d-3055-4b9c-ba64-0d47ca40a232"), event_id=11, version=0)
class Microsoft_Windows_WinHttp_11_0(Etw):
    pattern = Struct(
        "ApiHandle" / Int64ul,
        "Api" / CString,
        "Result" / Int32ul
    )


@declare(guid=guid("7d44233d-3055-4b9c-ba64-0d47ca40a232"), event_id=12, version=0)
class Microsoft_Windows_WinHttp_12_0(Etw):
    pattern = Struct(
        "ApiHandle" / Int64ul,
        "Api" / CString
    )


@declare(guid=guid("7d44233d-3055-4b9c-ba64-0d47ca40a232"), event_id=13, version=0)
class Microsoft_Windows_WinHttp_13_0(Etw):
    pattern = Struct(
        "ApiHandle" / Int64ul,
        "Api" / CString,
        "Result" / Int32ul
    )


@declare(guid=guid("7d44233d-3055-4b9c-ba64-0d47ca40a232"), event_id=14, version=0)
class Microsoft_Windows_WinHttp_14_0(Etw):
    pattern = Struct(
        "ApiHandle" / Int64ul,
        "Api" / CString,
        "Result" / Int32ul
    )


@declare(guid=guid("7d44233d-3055-4b9c-ba64-0d47ca40a232"), event_id=100, version=0)
class Microsoft_Windows_WinHttp_100_0(Etw):
    pattern = Struct(
        "hRequest" / Int64ul,
        "AuthTargets" / Int32ul,
        "AuthScheme" / Int32ul,
        "UserName" / WString,
        "Password" / WString
    )


@declare(guid=guid("7d44233d-3055-4b9c-ba64-0d47ca40a232"), event_id=801, version=0)
class Microsoft_Windows_WinHttp_801_0(Etw):
    pattern = Struct(
        "_ConnectionNameLength" / Int16ul,
        "ConnectionName" / Bytes(lambda this: this._ConnectionNameLength),
        "DetectFlags" / Int32ul
    )


@declare(guid=guid("7d44233d-3055-4b9c-ba64-0d47ca40a232"), event_id=801, version=1)
class Microsoft_Windows_WinHttp_801_1(Etw):
    pattern = Struct(
        "_ConnectionNameLength" / Int16ul,
        "ConnectionName" / Bytes(lambda this: this._ConnectionNameLength),
        "DetectFlags" / Int32ul
    )


@declare(guid=guid("7d44233d-3055-4b9c-ba64-0d47ca40a232"), event_id=802, version=0)
class Microsoft_Windows_WinHttp_802_0(Etw):
    pattern = Struct(
        "_InterfaceLength" / Int16ul,
        "Interface" / Bytes(lambda this: this._InterfaceLength)
    )


@declare(guid=guid("7d44233d-3055-4b9c-ba64-0d47ca40a232"), event_id=802, version=1)
class Microsoft_Windows_WinHttp_802_1(Etw):
    pattern = Struct(
        "_InterfaceLength" / Int16ul,
        "Interface" / Bytes(lambda this: this._InterfaceLength)
    )


@declare(guid=guid("7d44233d-3055-4b9c-ba64-0d47ca40a232"), event_id=803, version=0)
class Microsoft_Windows_WinHttp_803_0(Etw):
    pattern = Struct(
        "_InterfaceLength" / Int16ul,
        "Interface" / Bytes(lambda this: this._InterfaceLength),
        "_ConfigurationURLLength" / Int16ul,
        "ConfigurationURL" / Bytes(lambda this: this._ConfigurationURLLength)
    )


@declare(guid=guid("7d44233d-3055-4b9c-ba64-0d47ca40a232"), event_id=803, version=1)
class Microsoft_Windows_WinHttp_803_1(Etw):
    pattern = Struct(
        "_InterfaceLength" / Int16ul,
        "Interface" / Bytes(lambda this: this._InterfaceLength),
        "_ConfigurationURLLength" / Int16ul,
        "ConfigurationURL" / Bytes(lambda this: this._ConfigurationURLLength)
    )


@declare(guid=guid("7d44233d-3055-4b9c-ba64-0d47ca40a232"), event_id=804, version=0)
class Microsoft_Windows_WinHttp_804_0(Etw):
    pattern = Struct(
        "_InterfaceLength" / Int16ul,
        "Interface" / Bytes(lambda this: this._InterfaceLength),
        "_ConfigurationURLLength" / Int16ul,
        "ConfigurationURL" / Bytes(lambda this: this._ConfigurationURLLength),
        "Error" / Int32ul
    )


@declare(guid=guid("7d44233d-3055-4b9c-ba64-0d47ca40a232"), event_id=804, version=1)
class Microsoft_Windows_WinHttp_804_1(Etw):
    pattern = Struct(
        "_InterfaceLength" / Int16ul,
        "Interface" / Bytes(lambda this: this._InterfaceLength),
        "_ConfigurationURLLength" / Int16ul,
        "ConfigurationURL" / Bytes(lambda this: this._ConfigurationURLLength),
        "Error" / Int32ul
    )


@declare(guid=guid("7d44233d-3055-4b9c-ba64-0d47ca40a232"), event_id=805, version=0)
class Microsoft_Windows_WinHttp_805_0(Etw):
    pattern = Struct(
        "DetectFlags" / Int32ul
    )


@declare(guid=guid("7d44233d-3055-4b9c-ba64-0d47ca40a232"), event_id=806, version=0)
class Microsoft_Windows_WinHttp_806_0(Etw):
    pattern = Struct(
        "_ConfigurationURLLength" / Int16ul,
        "ConfigurationURL" / Bytes(lambda this: this._ConfigurationURLLength),
        "DetectFlags" / Int32ul
    )


@declare(guid=guid("7d44233d-3055-4b9c-ba64-0d47ca40a232"), event_id=806, version=1)
class Microsoft_Windows_WinHttp_806_1(Etw):
    pattern = Struct(
        "_ConfigurationURLLength" / Int16ul,
        "ConfigurationURL" / Bytes(lambda this: this._ConfigurationURLLength),
        "DetectFlags" / Int32ul
    )


@declare(guid=guid("7d44233d-3055-4b9c-ba64-0d47ca40a232"), event_id=807, version=0)
class Microsoft_Windows_WinHttp_807_0(Etw):
    pattern = Struct(
        "DetectFlags" / Int32ul,
        "Error" / Int32ul
    )


@declare(guid=guid("7d44233d-3055-4b9c-ba64-0d47ca40a232"), event_id=808, version=0)
class Microsoft_Windows_WinHttp_808_0(Etw):
    pattern = Struct(
        "Error" / Int32ul
    )


@declare(guid=guid("7d44233d-3055-4b9c-ba64-0d47ca40a232"), event_id=809, version=0)
class Microsoft_Windows_WinHttp_809_0(Etw):
    pattern = Struct(
        "_ConfigurationURLLength" / Int16ul,
        "ConfigurationURL" / Bytes(lambda this: this._ConfigurationURLLength)
    )


@declare(guid=guid("7d44233d-3055-4b9c-ba64-0d47ca40a232"), event_id=809, version=1)
class Microsoft_Windows_WinHttp_809_1(Etw):
    pattern = Struct(
        "_ConfigurationURLLength" / Int16ul,
        "ConfigurationURL" / Bytes(lambda this: this._ConfigurationURLLength)
    )


@declare(guid=guid("7d44233d-3055-4b9c-ba64-0d47ca40a232"), event_id=810, version=0)
class Microsoft_Windows_WinHttp_810_0(Etw):
    pattern = Struct(
        "_ConfigurationURLLength" / Int16ul,
        "ConfigurationURL" / Bytes(lambda this: this._ConfigurationURLLength)
    )


@declare(guid=guid("7d44233d-3055-4b9c-ba64-0d47ca40a232"), event_id=810, version=1)
class Microsoft_Windows_WinHttp_810_1(Etw):
    pattern = Struct(
        "_ConfigurationURLLength" / Int16ul,
        "ConfigurationURL" / Bytes(lambda this: this._ConfigurationURLLength)
    )


@declare(guid=guid("7d44233d-3055-4b9c-ba64-0d47ca40a232"), event_id=811, version=0)
class Microsoft_Windows_WinHttp_811_0(Etw):
    pattern = Struct(
        "_ConfigurationURLLength" / Int16ul,
        "ConfigurationURL" / Bytes(lambda this: this._ConfigurationURLLength),
        "Error" / Int32ul
    )


@declare(guid=guid("7d44233d-3055-4b9c-ba64-0d47ca40a232"), event_id=811, version=1)
class Microsoft_Windows_WinHttp_811_1(Etw):
    pattern = Struct(
        "_ConfigurationURLLength" / Int16ul,
        "ConfigurationURL" / Bytes(lambda this: this._ConfigurationURLLength),
        "Error" / Int32ul
    )


@declare(guid=guid("7d44233d-3055-4b9c-ba64-0d47ca40a232"), event_id=812, version=0)
class Microsoft_Windows_WinHttp_812_0(Etw):
    pattern = Struct(
        "_ConfigurationURLLength" / Int16ul,
        "ConfigurationURL" / Bytes(lambda this: this._ConfigurationURLLength),
        "_MIMETypeLength" / Int16ul,
        "MIMEType" / Bytes(lambda this: this._MIMETypeLength),
        "Error" / Int32ul
    )


@declare(guid=guid("7d44233d-3055-4b9c-ba64-0d47ca40a232"), event_id=812, version=1)
class Microsoft_Windows_WinHttp_812_1(Etw):
    pattern = Struct(
        "_ConfigurationURLLength" / Int16ul,
        "ConfigurationURL" / Bytes(lambda this: this._ConfigurationURLLength),
        "_MIMETypeLength" / Int16ul,
        "MIMEType" / Bytes(lambda this: this._MIMETypeLength),
        "Error" / Int32ul
    )


@declare(guid=guid("7d44233d-3055-4b9c-ba64-0d47ca40a232"), event_id=813, version=0)
class Microsoft_Windows_WinHttp_813_0(Etw):
    pattern = Struct(
        "_URLLength" / Int16ul,
        "URL" / Bytes(lambda this: this._URLLength)
    )


@declare(guid=guid("7d44233d-3055-4b9c-ba64-0d47ca40a232"), event_id=813, version=1)
class Microsoft_Windows_WinHttp_813_1(Etw):
    pattern = Struct(
        "_URLLength" / Int16ul,
        "URL" / Bytes(lambda this: this._URLLength)
    )


@declare(guid=guid("7d44233d-3055-4b9c-ba64-0d47ca40a232"), event_id=814, version=0)
class Microsoft_Windows_WinHttp_814_0(Etw):
    pattern = Struct(
        "_URLLength" / Int16ul,
        "URL" / Bytes(lambda this: this._URLLength),
        "_ProxyStringLength" / Int16ul,
        "ProxyString" / Bytes(lambda this: this._ProxyStringLength)
    )


@declare(guid=guid("7d44233d-3055-4b9c-ba64-0d47ca40a232"), event_id=814, version=1)
class Microsoft_Windows_WinHttp_814_1(Etw):
    pattern = Struct(
        "_URLLength" / Int16ul,
        "URL" / Bytes(lambda this: this._URLLength),
        "_ProxyStringLength" / Int16ul,
        "ProxyString" / Bytes(lambda this: this._ProxyStringLength)
    )


@declare(guid=guid("7d44233d-3055-4b9c-ba64-0d47ca40a232"), event_id=815, version=0)
class Microsoft_Windows_WinHttp_815_0(Etw):
    pattern = Struct(
        "_URLLength" / Int16ul,
        "URL" / Bytes(lambda this: this._URLLength),
        "Error" / Int32ul
    )


@declare(guid=guid("7d44233d-3055-4b9c-ba64-0d47ca40a232"), event_id=815, version=1)
class Microsoft_Windows_WinHttp_815_1(Etw):
    pattern = Struct(
        "_URLLength" / Int16ul,
        "URL" / Bytes(lambda this: this._URLLength),
        "Error" / Int32ul
    )


@declare(guid=guid("7d44233d-3055-4b9c-ba64-0d47ca40a232"), event_id=819, version=0)
class Microsoft_Windows_WinHttp_819_0(Etw):
    pattern = Struct(
        "WPADNetworkDecision" / Int32ul,
        "NetworkCount" / Int32ul
    )


@declare(guid=guid("7d44233d-3055-4b9c-ba64-0d47ca40a232"), event_id=834, version=0)
class Microsoft_Windows_WinHttp_834_0(Etw):
    pattern = Struct(
        "UniqueId" / Int32ul
    )


@declare(guid=guid("7d44233d-3055-4b9c-ba64-0d47ca40a232"), event_id=835, version=0)
class Microsoft_Windows_WinHttp_835_0(Etw):
    pattern = Struct(
        "UniqueId" / Int32ul
    )


@declare(guid=guid("7d44233d-3055-4b9c-ba64-0d47ca40a232"), event_id=1051, version=0)
class Microsoft_Windows_WinHttp_1051_0(Etw):
    pattern = Struct(
        "Flags" / Int32ul,
        "AddressName" / CString
    )


@declare(guid=guid("7d44233d-3055-4b9c-ba64-0d47ca40a232"), event_id=1052, version=0)
class Microsoft_Windows_WinHttp_1052_0(Etw):
    pattern = Struct(
        "error" / Int32ul,
        "Flags" / Int32ul,
        "AddressName" / CString
    )


@declare(guid=guid("7d44233d-3055-4b9c-ba64-0d47ca40a232"), event_id=12503, version=0)
class Microsoft_Windows_WinHttp_12503_0(Etw):
    pattern = Struct(
        "IdleTime" / Int32ul
    )


@declare(guid=guid("7d44233d-3055-4b9c-ba64-0d47ca40a232"), event_id=12506, version=0)
class Microsoft_Windows_WinHttp_12506_0(Etw):
    pattern = Struct(
        "Functionname" / WString,
        "Errortext" / WString,
        "Errorcode" / WString
    )


@declare(guid=guid("7d44233d-3055-4b9c-ba64-0d47ca40a232"), event_id=12509, version=0)
class Microsoft_Windows_WinHttp_12509_0(Etw):
    pattern = Struct(
        "Transporttype" / WString
    )


@declare(guid=guid("7d44233d-3055-4b9c-ba64-0d47ca40a232"), event_id=12511, version=0)
class Microsoft_Windows_WinHttp_12511_0(Etw):
    pattern = Struct(
        "param1" / WString
    )


@declare(guid=guid("7d44233d-3055-4b9c-ba64-0d47ca40a232"), event_id=12514, version=0)
class Microsoft_Windows_WinHttp_12514_0(Etw):
    pattern = Struct(
        "Exceptioncode" / WString
    )


@declare(guid=guid("7d44233d-3055-4b9c-ba64-0d47ca40a232"), event_id=58999, version=0)
class Microsoft_Windows_WinHttp_58999_0(Etw):
    pattern = Struct(
        "Message" / CString
    )


@declare(guid=guid("7d44233d-3055-4b9c-ba64-0d47ca40a232"), event_id=59995, version=0)
class Microsoft_Windows_WinHttp_59995_0(Etw):
    pattern = Struct(
        "Context" / Int64ul,
        "EtwQueueActionType" / Int32ul
    )


@declare(guid=guid("7d44233d-3055-4b9c-ba64-0d47ca40a232"), event_id=59996, version=0)
class Microsoft_Windows_WinHttp_59996_0(Etw):
    pattern = Struct(
        "Context" / Int64ul,
        "EtwQueueActionType" / Int32ul
    )


@declare(guid=guid("7d44233d-3055-4b9c-ba64-0d47ca40a232"), event_id=59997, version=0)
class Microsoft_Windows_WinHttp_59997_0(Etw):
    pattern = Struct(
        "Context" / Int64ul,
        "EtwQueueActionType" / Int32ul
    )


@declare(guid=guid("7d44233d-3055-4b9c-ba64-0d47ca40a232"), event_id=59998, version=0)
class Microsoft_Windows_WinHttp_59998_0(Etw):
    pattern = Struct(
        "Context" / Int64ul,
        "EtwQueueActionType" / Int32ul
    )


@declare(guid=guid("7d44233d-3055-4b9c-ba64-0d47ca40a232"), event_id=59999, version=0)
class Microsoft_Windows_WinHttp_59999_0(Etw):
    pattern = Struct(
        "File" / CString,
        "Line" / Int32ul,
        "Length" / Int16ul,
        "Message" / Bytes(lambda this: this.Length)
    )

