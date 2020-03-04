# -*- coding: utf-8 -*-
"""
Microsoft-Windows-DeviceAssociationService
GUID : 56c71c31-cfbd-4cdd-8559-505e042bbbe1
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("56c71c31-cfbd-4cdd-8559-505e042bbbe1"), event_id=5500, version=0)
class Microsoft_Windows_DeviceAssociationService_5500_0(Etw):
    pattern = Struct(
        "DasContext" / Int64ul
    )


@declare(guid=guid("56c71c31-cfbd-4cdd-8559-505e042bbbe1"), event_id=5501, version=0)
class Microsoft_Windows_DeviceAssociationService_5501_0(Etw):
    pattern = Struct(
        "DasContext" / Int64ul
    )


@declare(guid=guid("56c71c31-cfbd-4cdd-8559-505e042bbbe1"), event_id=5502, version=0)
class Microsoft_Windows_DeviceAssociationService_5502_0(Etw):
    pattern = Struct(
        "DasContext" / Int64ul
    )


@declare(guid=guid("56c71c31-cfbd-4cdd-8559-505e042bbbe1"), event_id=5503, version=0)
class Microsoft_Windows_DeviceAssociationService_5503_0(Etw):
    pattern = Struct(
        "DasContext" / Int64ul
    )


@declare(guid=guid("56c71c31-cfbd-4cdd-8559-505e042bbbe1"), event_id=5504, version=0)
class Microsoft_Windows_DeviceAssociationService_5504_0(Etw):
    pattern = Struct(
        "ProviderName" / WString,
        "DasContext" / Int64ul
    )


@declare(guid=guid("56c71c31-cfbd-4cdd-8559-505e042bbbe1"), event_id=5505, version=0)
class Microsoft_Windows_DeviceAssociationService_5505_0(Etw):
    pattern = Struct(
        "ProviderName" / WString,
        "DasContext" / Int64ul
    )


@declare(guid=guid("56c71c31-cfbd-4cdd-8559-505e042bbbe1"), event_id=5700, version=0)
class Microsoft_Windows_DeviceAssociationService_5700_0(Etw):
    pattern = Struct(
        "DasContext" / Int64ul
    )


@declare(guid=guid("56c71c31-cfbd-4cdd-8559-505e042bbbe1"), event_id=5701, version=0)
class Microsoft_Windows_DeviceAssociationService_5701_0(Etw):
    pattern = Struct(
        "DasContext" / Int64ul
    )


@declare(guid=guid("56c71c31-cfbd-4cdd-8559-505e042bbbe1"), event_id=5702, version=0)
class Microsoft_Windows_DeviceAssociationService_5702_0(Etw):
    pattern = Struct(
        "DasContext" / Int64ul
    )


@declare(guid=guid("56c71c31-cfbd-4cdd-8559-505e042bbbe1"), event_id=5703, version=0)
class Microsoft_Windows_DeviceAssociationService_5703_0(Etw):
    pattern = Struct(
        "DasContext" / Int64ul
    )


@declare(guid=guid("56c71c31-cfbd-4cdd-8559-505e042bbbe1"), event_id=5704, version=0)
class Microsoft_Windows_DeviceAssociationService_5704_0(Etw):
    pattern = Struct(
        "DasContext" / Int64ul
    )


@declare(guid=guid("56c71c31-cfbd-4cdd-8559-505e042bbbe1"), event_id=5705, version=0)
class Microsoft_Windows_DeviceAssociationService_5705_0(Etw):
    pattern = Struct(
        "DasContext" / Int64ul
    )


@declare(guid=guid("56c71c31-cfbd-4cdd-8559-505e042bbbe1"), event_id=5706, version=0)
class Microsoft_Windows_DeviceAssociationService_5706_0(Etw):
    pattern = Struct(
        "DasContext" / Int64ul
    )


@declare(guid=guid("56c71c31-cfbd-4cdd-8559-505e042bbbe1"), event_id=5707, version=0)
class Microsoft_Windows_DeviceAssociationService_5707_0(Etw):
    pattern = Struct(
        "DasContext" / Int64ul
    )


@declare(guid=guid("56c71c31-cfbd-4cdd-8559-505e042bbbe1"), event_id=5708, version=0)
class Microsoft_Windows_DeviceAssociationService_5708_0(Etw):
    pattern = Struct(
        "DasContext" / Int64ul
    )


@declare(guid=guid("56c71c31-cfbd-4cdd-8559-505e042bbbe1"), event_id=5709, version=0)
class Microsoft_Windows_DeviceAssociationService_5709_0(Etw):
    pattern = Struct(
        "DasContext" / Int64ul
    )


@declare(guid=guid("56c71c31-cfbd-4cdd-8559-505e042bbbe1"), event_id=5710, version=0)
class Microsoft_Windows_DeviceAssociationService_5710_0(Etw):
    pattern = Struct(
        "DasContext" / Int64ul
    )


@declare(guid=guid("56c71c31-cfbd-4cdd-8559-505e042bbbe1"), event_id=5711, version=0)
class Microsoft_Windows_DeviceAssociationService_5711_0(Etw):
    pattern = Struct(
        "DasContext" / Int64ul
    )


@declare(guid=guid("56c71c31-cfbd-4cdd-8559-505e042bbbe1"), event_id=5712, version=0)
class Microsoft_Windows_DeviceAssociationService_5712_0(Etw):
    pattern = Struct(
        "DasContext" / Int64ul
    )


@declare(guid=guid("56c71c31-cfbd-4cdd-8559-505e042bbbe1"), event_id=5713, version=0)
class Microsoft_Windows_DeviceAssociationService_5713_0(Etw):
    pattern = Struct(
        "DasContext" / Int64ul
    )


@declare(guid=guid("56c71c31-cfbd-4cdd-8559-505e042bbbe1"), event_id=5714, version=0)
class Microsoft_Windows_DeviceAssociationService_5714_0(Etw):
    pattern = Struct(
        "DasContext" / Int64ul
    )


@declare(guid=guid("56c71c31-cfbd-4cdd-8559-505e042bbbe1"), event_id=5715, version=0)
class Microsoft_Windows_DeviceAssociationService_5715_0(Etw):
    pattern = Struct(
        "DasContext" / Int64ul
    )


@declare(guid=guid("56c71c31-cfbd-4cdd-8559-505e042bbbe1"), event_id=5716, version=0)
class Microsoft_Windows_DeviceAssociationService_5716_0(Etw):
    pattern = Struct(
        "DasContext" / Int64ul
    )


@declare(guid=guid("56c71c31-cfbd-4cdd-8559-505e042bbbe1"), event_id=5717, version=0)
class Microsoft_Windows_DeviceAssociationService_5717_0(Etw):
    pattern = Struct(
        "DasContext" / Int64ul
    )


@declare(guid=guid("56c71c31-cfbd-4cdd-8559-505e042bbbe1"), event_id=5718, version=0)
class Microsoft_Windows_DeviceAssociationService_5718_0(Etw):
    pattern = Struct(
        "DasContext" / Int64ul
    )


@declare(guid=guid("56c71c31-cfbd-4cdd-8559-505e042bbbe1"), event_id=5719, version=0)
class Microsoft_Windows_DeviceAssociationService_5719_0(Etw):
    pattern = Struct(
        "DasContext" / Int64ul
    )


@declare(guid=guid("56c71c31-cfbd-4cdd-8559-505e042bbbe1"), event_id=5720, version=0)
class Microsoft_Windows_DeviceAssociationService_5720_0(Etw):
    pattern = Struct(
        "DasContext" / Int64ul
    )


@declare(guid=guid("56c71c31-cfbd-4cdd-8559-505e042bbbe1"), event_id=5721, version=0)
class Microsoft_Windows_DeviceAssociationService_5721_0(Etw):
    pattern = Struct(
        "DasContext" / Int64ul
    )


@declare(guid=guid("56c71c31-cfbd-4cdd-8559-505e042bbbe1"), event_id=5722, version=0)
class Microsoft_Windows_DeviceAssociationService_5722_0(Etw):
    pattern = Struct(
        "DasContext" / Int64ul
    )


@declare(guid=guid("56c71c31-cfbd-4cdd-8559-505e042bbbe1"), event_id=5723, version=0)
class Microsoft_Windows_DeviceAssociationService_5723_0(Etw):
    pattern = Struct(
        "DasContext" / Int64ul
    )


@declare(guid=guid("56c71c31-cfbd-4cdd-8559-505e042bbbe1"), event_id=5724, version=0)
class Microsoft_Windows_DeviceAssociationService_5724_0(Etw):
    pattern = Struct(
        "DasContext" / Int64ul
    )


@declare(guid=guid("56c71c31-cfbd-4cdd-8559-505e042bbbe1"), event_id=5725, version=0)
class Microsoft_Windows_DeviceAssociationService_5725_0(Etw):
    pattern = Struct(
        "DasContext" / Int64ul
    )


@declare(guid=guid("56c71c31-cfbd-4cdd-8559-505e042bbbe1"), event_id=5726, version=0)
class Microsoft_Windows_DeviceAssociationService_5726_0(Etw):
    pattern = Struct(
        "DasContext" / Int64ul
    )


@declare(guid=guid("56c71c31-cfbd-4cdd-8559-505e042bbbe1"), event_id=5727, version=0)
class Microsoft_Windows_DeviceAssociationService_5727_0(Etw):
    pattern = Struct(
        "DasContext" / Int64ul
    )


@declare(guid=guid("56c71c31-cfbd-4cdd-8559-505e042bbbe1"), event_id=5728, version=0)
class Microsoft_Windows_DeviceAssociationService_5728_0(Etw):
    pattern = Struct(
        "DasContext" / Int64ul
    )


@declare(guid=guid("56c71c31-cfbd-4cdd-8559-505e042bbbe1"), event_id=5729, version=0)
class Microsoft_Windows_DeviceAssociationService_5729_0(Etw):
    pattern = Struct(
        "DasContext" / Int64ul
    )


@declare(guid=guid("56c71c31-cfbd-4cdd-8559-505e042bbbe1"), event_id=5730, version=0)
class Microsoft_Windows_DeviceAssociationService_5730_0(Etw):
    pattern = Struct(
        "DasContext" / Int64ul
    )


@declare(guid=guid("56c71c31-cfbd-4cdd-8559-505e042bbbe1"), event_id=5731, version=0)
class Microsoft_Windows_DeviceAssociationService_5731_0(Etw):
    pattern = Struct(
        "DasContext" / Int64ul
    )


@declare(guid=guid("56c71c31-cfbd-4cdd-8559-505e042bbbe1"), event_id=5732, version=0)
class Microsoft_Windows_DeviceAssociationService_5732_0(Etw):
    pattern = Struct(
        "DasContext" / Int64ul
    )


@declare(guid=guid("56c71c31-cfbd-4cdd-8559-505e042bbbe1"), event_id=5733, version=0)
class Microsoft_Windows_DeviceAssociationService_5733_0(Etw):
    pattern = Struct(
        "DasContext" / Int64ul
    )


@declare(guid=guid("56c71c31-cfbd-4cdd-8559-505e042bbbe1"), event_id=5734, version=0)
class Microsoft_Windows_DeviceAssociationService_5734_0(Etw):
    pattern = Struct(
        "DasContext" / Int64ul
    )


@declare(guid=guid("56c71c31-cfbd-4cdd-8559-505e042bbbe1"), event_id=5735, version=0)
class Microsoft_Windows_DeviceAssociationService_5735_0(Etw):
    pattern = Struct(
        "DasContext" / Int64ul
    )


@declare(guid=guid("56c71c31-cfbd-4cdd-8559-505e042bbbe1"), event_id=5736, version=0)
class Microsoft_Windows_DeviceAssociationService_5736_0(Etw):
    pattern = Struct(
        "DasContext" / Int64ul
    )


@declare(guid=guid("56c71c31-cfbd-4cdd-8559-505e042bbbe1"), event_id=5737, version=0)
class Microsoft_Windows_DeviceAssociationService_5737_0(Etw):
    pattern = Struct(
        "DasContext" / Int64ul
    )

