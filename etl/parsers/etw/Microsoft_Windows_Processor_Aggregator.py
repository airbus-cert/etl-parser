# -*- coding: utf-8 -*-
"""
Microsoft-Windows-Processor-Aggregator
GUID : cba16cf2-2fab-49f8-89ae-894e718649e7
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("cba16cf2-2fab-49f8-89ae-894e718649e7"), event_id=1, version=0)
class Microsoft_Windows_Processor_Aggregator_1_0(Etw):
    pattern = Struct(
        "NumProcessors" / Int32ul
    )


@declare(guid=guid("cba16cf2-2fab-49f8-89ae-894e718649e7"), event_id=2, version=0)
class Microsoft_Windows_Processor_Aggregator_2_0(Etw):
    pattern = Struct(
        "Requested" / Int32ul,
        "Acknowledged" / Int32ul,
        "IsSuccess" / Int8ul
    )

