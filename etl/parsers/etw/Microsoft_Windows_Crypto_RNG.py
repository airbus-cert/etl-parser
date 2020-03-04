# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Crypto-RNG
GUID : 54d5ac20-e14f-4fda-92da-ebf7556ff176
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("54d5ac20-e14f-4fda-92da-ebf7556ff176"), event_id=1, version=0)
class Microsoft_Windows_Crypto_RNG_1_0(Etw):
    pattern = Struct(
        "SourceNumber" / Int64ul,
        "SourceName" / WString,
        "SourceType" / Int32ul
    )


@declare(guid=guid("54d5ac20-e14f-4fda-92da-ebf7556ff176"), event_id=2, version=0)
class Microsoft_Windows_Crypto_RNG_2_0(Etw):
    pattern = Struct(
        "SourceNumber" / Int64ul,
        "SourceName" / WString
    )


@declare(guid=guid("54d5ac20-e14f-4fda-92da-ebf7556ff176"), event_id=3, version=0)
class Microsoft_Windows_Crypto_RNG_3_0(Etw):
    pattern = Struct(
        "SourceNumber" / Int64ul,
        "BytesProvided" / Int32ul,
        "EntropyEstimate" / Int32sl,
        "nData" / Int32ul,
        "Data" / Bytes(lambda this: this.nData)
    )


@declare(guid=guid("54d5ac20-e14f-4fda-92da-ebf7556ff176"), event_id=4, version=0)
class Microsoft_Windows_Crypto_RNG_4_0(Etw):
    pattern = Struct(
        "SourceNumber" / Int64ul,
        "ResultStatus" / Int32ul,
        "TimeTaken" / Int64ul
    )


@declare(guid=guid("54d5ac20-e14f-4fda-92da-ebf7556ff176"), event_id=16, version=0)
class Microsoft_Windows_Crypto_RNG_16_0(Etw):
    pattern = Struct(
        "Source" / Int32ul,
        "Policy" / Int32ul,
        "ResultCode" / Int32ul,
        "ResultStatus" / Int32ul,
        "Time" / Int64ul,
        "BytesProvided" / Int32ul,
        "nData" / Int32ul,
        "Data" / Bytes(lambda this: this.nData)
    )


@declare(guid=guid("54d5ac20-e14f-4fda-92da-ebf7556ff176"), event_id=32, version=0)
class Microsoft_Windows_Crypto_RNG_32_0(Etw):
    pattern = Struct(
        "PoolReseedCount" / Int64ul,
        "ReseedType" / Int32ul,
        "nData" / Int32ul,
        "Data" / Bytes(lambda this: this.nData)
    )


@declare(guid=guid("54d5ac20-e14f-4fda-92da-ebf7556ff176"), event_id=33, version=0)
class Microsoft_Windows_Crypto_RNG_33_0(Etw):
    pattern = Struct(
        "PoolNo" / Int32ul,
        "nData" / Int32ul,
        "Data" / Bytes(lambda this: this.nData)
    )


@declare(guid=guid("54d5ac20-e14f-4fda-92da-ebf7556ff176"), event_id=48, version=0)
class Microsoft_Windows_Crypto_RNG_48_0(Etw):
    pattern = Struct(
        "PrngAddress" / Int64ul,
        "nData" / Int32ul,
        "Data" / Bytes(lambda this: this.nData)
    )


@declare(guid=guid("54d5ac20-e14f-4fda-92da-ebf7556ff176"), event_id=49, version=0)
class Microsoft_Windows_Crypto_RNG_49_0(Etw):
    pattern = Struct(
        "PrngAddress" / Int64ul,
        "BytesProduced" / Int64ul,
        "nData" / Int32ul,
        "Data" / Bytes(lambda this: this.nData)
    )

