# -*- coding: utf-8 -*-
"""
Microsoft-WindowsPhone-UfxSynopsys
GUID : 49b12c7c-4bd5-4f93-bb75-30fce739600b
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("49b12c7c-4bd5-4f93-bb75-30fce739600b"), event_id=100, version=0)
class Microsoft_WindowsPhone_UfxSynopsys_100_0(Etw):
    pattern = Struct(
        "File" / CString,
        "Line" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("49b12c7c-4bd5-4f93-bb75-30fce739600b"), event_id=101, version=0)
class Microsoft_WindowsPhone_UfxSynopsys_101_0(Etw):
    pattern = Struct(
        "Offset" / Int32ul,
        "Value" / Int32ul
    )


@declare(guid=guid("49b12c7c-4bd5-4f93-bb75-30fce739600b"), event_id=102, version=0)
class Microsoft_WindowsPhone_UfxSynopsys_102_0(Etw):
    pattern = Struct(
        "Offset" / Int32ul,
        "Value" / Int32ul
    )


@declare(guid=guid("49b12c7c-4bd5-4f93-bb75-30fce739600b"), event_id=200, version=0)
class Microsoft_WindowsPhone_UfxSynopsys_200_0(Etw):
    pattern = Struct(
        "Stage" / CString,
        "Endpoint" / Int64ul,
        "PhysicalEndpoint" / Int32ul,
        "Request" / Int64ul,
        "Transaction" / Int64ul,
        "BytesRequested" / Int32ul,
        "BytesProgrammed" / Int32ul,
        "BytesTransferred" / Int32ul,
        "SgProgrammed" / Int32ul,
        "SgLength" / Int32ul,
        "TrbProgrammed" / Int32ul,
        "TrbLength" / Int32ul
    )


@declare(guid=guid("49b12c7c-4bd5-4f93-bb75-30fce739600b"), event_id=201, version=0)
class Microsoft_WindowsPhone_UfxSynopsys_201_0(Etw):
    pattern = Struct(
        "Endpoint" / Int64ul,
        "PhysicalEndpoint" / Int32ul,
        "Index" / Int32ul,
        "Word1" / Int32ul,
        "Word2" / Int32ul,
        "Word3" / Int32ul,
        "Word4" / Int32ul
    )


@declare(guid=guid("49b12c7c-4bd5-4f93-bb75-30fce739600b"), event_id=202, version=0)
class Microsoft_WindowsPhone_UfxSynopsys_202_0(Etw):
    pattern = Struct(
        "Name" / CString,
        "Endpoint" / Int64ul,
        "PhysicalEndpoint" / Int32ul,
        "Command" / Int32ul,
        "Parameter0" / Int32ul,
        "Parameter1" / Int32ul,
        "Parameter2" / Int32ul
    )


@declare(guid=guid("49b12c7c-4bd5-4f93-bb75-30fce739600b"), event_id=301, version=0)
class Microsoft_WindowsPhone_UfxSynopsys_301_0(Etw):
    pattern = Struct(
        "fSynopsysEndpoint" / CString,
        "fSynopsysEndpointDescriptor" / Int8ul
    )


@declare(guid=guid("49b12c7c-4bd5-4f93-bb75-30fce739600b"), event_id=302, version=0)
class Microsoft_WindowsPhone_UfxSynopsys_302_0(Etw):
    pattern = Struct(
        "fChargerDetectionErrorInfo" / WString
    )


@declare(guid=guid("49b12c7c-4bd5-4f93-bb75-30fce739600b"), event_id=303, version=0)
class Microsoft_WindowsPhone_UfxSynopsys_303_0(Etw):
    pattern = Struct(
        "fDeterminePortTypeFailed" / WString
    )


@declare(guid=guid("49b12c7c-4bd5-4f93-bb75-30fce739600b"), event_id=304, version=0)
class Microsoft_WindowsPhone_UfxSynopsys_304_0(Etw):
    pattern = Struct(
        "Configuration" / Int32ul,
        "Control" / Int32ul,
        "EnabledEvents" / Int32ul,
        "Status" / Int32ul
    )


@declare(guid=guid("49b12c7c-4bd5-4f93-bb75-30fce739600b"), event_id=305, version=0)
class Microsoft_WindowsPhone_UfxSynopsys_305_0(Etw):
    pattern = Struct(
        "ConnectedStandby" / Int8ul,
        "IdleResidency" / Int8ul,
        "DevicePowerState" / Int32ul,
        "Connected" / Int8ul,
        "UsbPortType" / Int32ul,
        "UsbDeviceState" / Int32ul
    )

