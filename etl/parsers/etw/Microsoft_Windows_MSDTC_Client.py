# -*- coding: utf-8 -*-
"""
Microsoft-Windows-MSDTC Client
GUID : 7a67066e-193f-4d3a-82d3-322fee5259de
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("7a67066e-193f-4d3a-82d3-322fee5259de"), event_id=4098, version=0)
class Microsoft_Windows_MSDTC_Client_4098_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7a67066e-193f-4d3a-82d3-322fee5259de"), event_id=4099, version=0)
class Microsoft_Windows_MSDTC_Client_4099_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7a67066e-193f-4d3a-82d3-322fee5259de"), event_id=4101, version=0)
class Microsoft_Windows_MSDTC_Client_4101_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7a67066e-193f-4d3a-82d3-322fee5259de"), event_id=4113, version=0)
class Microsoft_Windows_MSDTC_Client_4113_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7a67066e-193f-4d3a-82d3-322fee5259de"), event_id=4137, version=0)
class Microsoft_Windows_MSDTC_Client_4137_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7a67066e-193f-4d3a-82d3-322fee5259de"), event_id=4149, version=0)
class Microsoft_Windows_MSDTC_Client_4149_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7a67066e-193f-4d3a-82d3-322fee5259de"), event_id=4150, version=0)
class Microsoft_Windows_MSDTC_Client_4150_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7a67066e-193f-4d3a-82d3-322fee5259de"), event_id=4151, version=0)
class Microsoft_Windows_MSDTC_Client_4151_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7a67066e-193f-4d3a-82d3-322fee5259de"), event_id=4152, version=0)
class Microsoft_Windows_MSDTC_Client_4152_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7a67066e-193f-4d3a-82d3-322fee5259de"), event_id=4153, version=0)
class Microsoft_Windows_MSDTC_Client_4153_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7a67066e-193f-4d3a-82d3-322fee5259de"), event_id=4155, version=0)
class Microsoft_Windows_MSDTC_Client_4155_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7a67066e-193f-4d3a-82d3-322fee5259de"), event_id=4156, version=0)
class Microsoft_Windows_MSDTC_Client_4156_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7a67066e-193f-4d3a-82d3-322fee5259de"), event_id=4209, version=0)
class Microsoft_Windows_MSDTC_Client_4209_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7a67066e-193f-4d3a-82d3-322fee5259de"), event_id=4211, version=0)
class Microsoft_Windows_MSDTC_Client_4211_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7a67066e-193f-4d3a-82d3-322fee5259de"), event_id=4212, version=0)
class Microsoft_Windows_MSDTC_Client_4212_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7a67066e-193f-4d3a-82d3-322fee5259de"), event_id=4213, version=0)
class Microsoft_Windows_MSDTC_Client_4213_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7a67066e-193f-4d3a-82d3-322fee5259de"), event_id=4214, version=0)
class Microsoft_Windows_MSDTC_Client_4214_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7a67066e-193f-4d3a-82d3-322fee5259de"), event_id=4215, version=0)
class Microsoft_Windows_MSDTC_Client_4215_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7a67066e-193f-4d3a-82d3-322fee5259de"), event_id=4216, version=0)
class Microsoft_Windows_MSDTC_Client_4216_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7a67066e-193f-4d3a-82d3-322fee5259de"), event_id=4217, version=0)
class Microsoft_Windows_MSDTC_Client_4217_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7a67066e-193f-4d3a-82d3-322fee5259de"), event_id=4224, version=0)
class Microsoft_Windows_MSDTC_Client_4224_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7a67066e-193f-4d3a-82d3-322fee5259de"), event_id=4225, version=0)
class Microsoft_Windows_MSDTC_Client_4225_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7a67066e-193f-4d3a-82d3-322fee5259de"), event_id=4226, version=0)
class Microsoft_Windows_MSDTC_Client_4226_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7a67066e-193f-4d3a-82d3-322fee5259de"), event_id=4227, version=0)
class Microsoft_Windows_MSDTC_Client_4227_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7a67066e-193f-4d3a-82d3-322fee5259de"), event_id=4233, version=0)
class Microsoft_Windows_MSDTC_Client_4233_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7a67066e-193f-4d3a-82d3-322fee5259de"), event_id=4356, version=0)
class Microsoft_Windows_MSDTC_Client_4356_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7a67066e-193f-4d3a-82d3-322fee5259de"), event_id=4357, version=0)
class Microsoft_Windows_MSDTC_Client_4357_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7a67066e-193f-4d3a-82d3-322fee5259de"), event_id=4358, version=0)
class Microsoft_Windows_MSDTC_Client_4358_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7a67066e-193f-4d3a-82d3-322fee5259de"), event_id=4359, version=0)
class Microsoft_Windows_MSDTC_Client_4359_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7a67066e-193f-4d3a-82d3-322fee5259de"), event_id=4399, version=0)
class Microsoft_Windows_MSDTC_Client_4399_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7a67066e-193f-4d3a-82d3-322fee5259de"), event_id=4400, version=0)
class Microsoft_Windows_MSDTC_Client_4400_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7a67066e-193f-4d3a-82d3-322fee5259de"), event_id=4401, version=0)
class Microsoft_Windows_MSDTC_Client_4401_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7a67066e-193f-4d3a-82d3-322fee5259de"), event_id=4402, version=0)
class Microsoft_Windows_MSDTC_Client_4402_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7a67066e-193f-4d3a-82d3-322fee5259de"), event_id=4403, version=0)
class Microsoft_Windows_MSDTC_Client_4403_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7a67066e-193f-4d3a-82d3-322fee5259de"), event_id=4404, version=0)
class Microsoft_Windows_MSDTC_Client_4404_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7a67066e-193f-4d3a-82d3-322fee5259de"), event_id=4405, version=0)
class Microsoft_Windows_MSDTC_Client_4405_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7a67066e-193f-4d3a-82d3-322fee5259de"), event_id=4406, version=0)
class Microsoft_Windows_MSDTC_Client_4406_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7a67066e-193f-4d3a-82d3-322fee5259de"), event_id=4407, version=0)
class Microsoft_Windows_MSDTC_Client_4407_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7a67066e-193f-4d3a-82d3-322fee5259de"), event_id=4408, version=0)
class Microsoft_Windows_MSDTC_Client_4408_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7a67066e-193f-4d3a-82d3-322fee5259de"), event_id=4409, version=0)
class Microsoft_Windows_MSDTC_Client_4409_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7a67066e-193f-4d3a-82d3-322fee5259de"), event_id=4410, version=0)
class Microsoft_Windows_MSDTC_Client_4410_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7a67066e-193f-4d3a-82d3-322fee5259de"), event_id=4411, version=0)
class Microsoft_Windows_MSDTC_Client_4411_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7a67066e-193f-4d3a-82d3-322fee5259de"), event_id=4412, version=0)
class Microsoft_Windows_MSDTC_Client_4412_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7a67066e-193f-4d3a-82d3-322fee5259de"), event_id=4413, version=0)
class Microsoft_Windows_MSDTC_Client_4413_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7a67066e-193f-4d3a-82d3-322fee5259de"), event_id=4414, version=0)
class Microsoft_Windows_MSDTC_Client_4414_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7a67066e-193f-4d3a-82d3-322fee5259de"), event_id=4415, version=0)
class Microsoft_Windows_MSDTC_Client_4415_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7a67066e-193f-4d3a-82d3-322fee5259de"), event_id=4416, version=0)
class Microsoft_Windows_MSDTC_Client_4416_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7a67066e-193f-4d3a-82d3-322fee5259de"), event_id=4417, version=0)
class Microsoft_Windows_MSDTC_Client_4417_0(Etw):
    pattern = Struct(
        "__binLength" / Int32ul,
        "param1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7a67066e-193f-4d3a-82d3-322fee5259de"), event_id=4424, version=0)
class Microsoft_Windows_MSDTC_Client_4424_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7a67066e-193f-4d3a-82d3-322fee5259de"), event_id=4425, version=0)
class Microsoft_Windows_MSDTC_Client_4425_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7a67066e-193f-4d3a-82d3-322fee5259de"), event_id=4426, version=0)
class Microsoft_Windows_MSDTC_Client_4426_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7a67066e-193f-4d3a-82d3-322fee5259de"), event_id=4427, version=0)
class Microsoft_Windows_MSDTC_Client_4427_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7a67066e-193f-4d3a-82d3-322fee5259de"), event_id=4428, version=0)
class Microsoft_Windows_MSDTC_Client_4428_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7a67066e-193f-4d3a-82d3-322fee5259de"), event_id=4429, version=0)
class Microsoft_Windows_MSDTC_Client_4429_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7a67066e-193f-4d3a-82d3-322fee5259de"), event_id=4431, version=0)
class Microsoft_Windows_MSDTC_Client_4431_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7a67066e-193f-4d3a-82d3-322fee5259de"), event_id=4432, version=0)
class Microsoft_Windows_MSDTC_Client_4432_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7a67066e-193f-4d3a-82d3-322fee5259de"), event_id=4441, version=0)
class Microsoft_Windows_MSDTC_Client_4441_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7a67066e-193f-4d3a-82d3-322fee5259de"), event_id=4442, version=0)
class Microsoft_Windows_MSDTC_Client_4442_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7a67066e-193f-4d3a-82d3-322fee5259de"), event_id=4443, version=0)
class Microsoft_Windows_MSDTC_Client_4443_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7a67066e-193f-4d3a-82d3-322fee5259de"), event_id=4454, version=0)
class Microsoft_Windows_MSDTC_Client_4454_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "param2" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7a67066e-193f-4d3a-82d3-322fee5259de"), event_id=4455, version=0)
class Microsoft_Windows_MSDTC_Client_4455_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7a67066e-193f-4d3a-82d3-322fee5259de"), event_id=4456, version=0)
class Microsoft_Windows_MSDTC_Client_4456_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7a67066e-193f-4d3a-82d3-322fee5259de"), event_id=4457, version=0)
class Microsoft_Windows_MSDTC_Client_4457_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7a67066e-193f-4d3a-82d3-322fee5259de"), event_id=4458, version=0)
class Microsoft_Windows_MSDTC_Client_4458_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7a67066e-193f-4d3a-82d3-322fee5259de"), event_id=4459, version=0)
class Microsoft_Windows_MSDTC_Client_4459_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7a67066e-193f-4d3a-82d3-322fee5259de"), event_id=53284, version=0)
class Microsoft_Windows_MSDTC_Client_53284_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7a67066e-193f-4d3a-82d3-322fee5259de"), event_id=53320, version=0)
class Microsoft_Windows_MSDTC_Client_53320_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )


@declare(guid=guid("7a67066e-193f-4d3a-82d3-322fee5259de"), event_id=53322, version=0)
class Microsoft_Windows_MSDTC_Client_53322_0(Etw):
    pattern = Struct(
        "param1" / WString,
        "__binLength" / Int32ul,
        "param_bin1" / Bytes(lambda this: this.__binLength)
    )

