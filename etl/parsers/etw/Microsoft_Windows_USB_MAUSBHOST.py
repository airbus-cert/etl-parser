# -*- coding: utf-8 -*-
"""
Microsoft-Windows-USB-MAUSBHOST
GUID : 7725b5f9-1f2e-4e21-baeb-b2af4690bc87
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=3, version=0)
class Microsoft_Windows_USB_MAUSBHOST_3_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_WdfDevicePowerState" / Int32ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=4, version=0)
class Microsoft_Windows_USB_MAUSBHOST_4_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_UsbTtHubDevice" / Int64ul,
        "fid_UsbDevice" / Int64ul,
        "DeviceSpeed" / Int32ul,
        "PortPathDepth" / Int32ul,
        "PortPath" / Int32ul,
        "fid_MaUsbDeviceHandle" / Int32ul,
        "fid_DeviceIsHub" / Int32ul,
        "fid_NumberOfPorts" / Int32ul,
        "fid_NumberOfTTs" / Int32ul,
        "fid_USB_Device_Descriptor" / Float32l
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=5, version=0)
class Microsoft_Windows_USB_MAUSBHOST_5_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_UsbDevice" / Int64ul,
        "fid_Endpoint" / Int64ul,
        "fid_USB_Endpoint_Descriptor" / Float32l,
        "fid_IsLinkManaged" / Int8ul,
        "fid_CreditConsumptionUnit" / Int16ul,
        "fid_BufferSize" / Int32ul,
        "fid_IsochProgrammingDelay" / Int16ul,
        "fid_IsochResponseDelay" / Int16ul,
        "fid_IsochSegmentsPerFrame" / Int32ul,
        "fid_MaxIsochSegmentSize" / Int32ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=6, version=0)
class Microsoft_Windows_USB_MAUSBHOST_6_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_WdfDevicePowerState" / Int32ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=7, version=0)
class Microsoft_Windows_USB_MAUSBHOST_7_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_WdfDevicePowerState" / Int32ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=8, version=0)
class Microsoft_Windows_USB_MAUSBHOST_8_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_UsbTtHubDevice" / Int64ul,
        "fid_UsbDevice" / Int64ul,
        "DeviceSpeed" / Int32ul,
        "PortPathDepth" / Int32ul,
        "PortPath" / Int32ul,
        "fid_MaUsbDeviceHandle" / Int32ul,
        "fid_DeviceIsHub" / Int32ul,
        "fid_NumberOfPorts" / Int32ul,
        "fid_NumberOfTTs" / Int32ul,
        "fid_USB_Device_Descriptor" / Float32l
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=9, version=0)
class Microsoft_Windows_USB_MAUSBHOST_9_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_UsbTtHubDevice" / Int64ul,
        "fid_UsbDevice" / Int64ul,
        "DeviceSpeed" / Int32ul,
        "PortPathDepth" / Int32ul,
        "PortPath" / Int32ul,
        "fid_MaUsbDeviceHandle" / Int32ul,
        "fid_DeviceIsHub" / Int32ul,
        "fid_NumberOfPorts" / Int32ul,
        "fid_NumberOfTTs" / Int32ul,
        "fid_USB_Device_Descriptor" / Float32l
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=10, version=0)
class Microsoft_Windows_USB_MAUSBHOST_10_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_UsbTtHubDevice" / Int64ul,
        "fid_UsbDevice" / Int64ul,
        "DeviceSpeed" / Int32ul,
        "PortPathDepth" / Int32ul,
        "PortPath" / Int32ul,
        "fid_MaUsbDeviceHandle" / Int32ul,
        "fid_DeviceIsHub" / Int32ul,
        "fid_NumberOfPorts" / Int32ul,
        "fid_NumberOfTTs" / Int32ul,
        "fid_USB_Device_Descriptor" / Float32l
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=11, version=0)
class Microsoft_Windows_USB_MAUSBHOST_11_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_UsbDevice" / Int64ul,
        "fid_Endpoint" / Int64ul,
        "fid_USB_Endpoint_Descriptor" / Int8ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=12, version=0)
class Microsoft_Windows_USB_MAUSBHOST_12_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_UsbDevice" / Int64ul,
        "fid_Endpoint" / Int64ul,
        "fid_USB_Endpoint_Descriptor" / Int8ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=13, version=0)
class Microsoft_Windows_USB_MAUSBHOST_13_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_UsbDevice" / Int64ul,
        "fid_Endpoint" / Int64ul,
        "fid_USB_Endpoint_Descriptor" / Int8ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=15, version=0)
class Microsoft_Windows_USB_MAUSBHOST_15_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_DeviceState" / Int32ul,
        "fid_PowerAction" / Int32ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=16, version=0)
class Microsoft_Windows_USB_MAUSBHOST_16_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_DeviceState" / Int32ul,
        "fid_PowerAction" / Int32ul,
        "fid_NtStatus" / Int32ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=17, version=0)
class Microsoft_Windows_USB_MAUSBHOST_17_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_DeviceState" / Int32ul,
        "fid_PowerAction" / Int32ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=18, version=0)
class Microsoft_Windows_USB_MAUSBHOST_18_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_DeviceState" / Int32ul,
        "fid_PowerAction" / Int32ul,
        "fid_NtStatus" / Int32ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=19, version=0)
class Microsoft_Windows_USB_MAUSBHOST_19_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=20, version=0)
class Microsoft_Windows_USB_MAUSBHOST_20_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_NtStatus" / Int32ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=21, version=0)
class Microsoft_Windows_USB_MAUSBHOST_21_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_Capability" / Guid,
        "fid_NtStatus" / Int32ul,
        "fid_NumStaticStreams" / Int32ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=50, version=0)
class Microsoft_Windows_USB_MAUSBHOST_50_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_WdfRequest" / Int64ul,
        "fid_SubType" / Int8ul,
        "fid_DeviceHandle" / Int16ul,
        "fid_DeviceAddress" / Int8ul,
        "fid_Ssid" / Int8ul,
        "fid_StatusCode" / Int8ul,
        "fid_DialogToken" / Int16ul,
        "fid_NtStatus" / Int32ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=51, version=0)
class Microsoft_Windows_USB_MAUSBHOST_51_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_WdfRequest" / Int64ul,
        "fid_SubType" / Int8ul,
        "fid_DeviceHandle" / Int16ul,
        "fid_DeviceAddress" / Int8ul,
        "fid_Ssid" / Int8ul,
        "fid_StatusCode" / Int8ul,
        "fid_DialogToken" / Int16ul,
        "fid_NtStatus" / Int32ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=52, version=0)
class Microsoft_Windows_USB_MAUSBHOST_52_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_WdfRequest" / Int64ul,
        "fid_SubType" / Int8ul,
        "fid_DeviceHandle" / Int16ul,
        "fid_DeviceAddress" / Int8ul,
        "fid_Ssid" / Int8ul,
        "fid_StatusCode" / Int8ul,
        "fid_DialogToken" / Int16ul,
        "fid_NtStatus" / Int32ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=53, version=0)
class Microsoft_Windows_USB_MAUSBHOST_53_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_WdfRequest" / Int64ul,
        "fid_SubType" / Int8ul,
        "fid_DeviceHandle" / Int16ul,
        "fid_DeviceAddress" / Int8ul,
        "fid_Ssid" / Int8ul,
        "fid_StatusCode" / Int8ul,
        "fid_DialogToken" / Int16ul,
        "fid_NtStatus" / Int32ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=54, version=0)
class Microsoft_Windows_USB_MAUSBHOST_54_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_Error" / Int32ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=55, version=0)
class Microsoft_Windows_USB_MAUSBHOST_55_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_ExpectedSubtype" / Int32ul,
        "fid_ActualSubtype" / Int32ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=56, version=0)
class Microsoft_Windows_USB_MAUSBHOST_56_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_Subtype" / Int32ul,
        "fid_NtStatus" / Int32ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=57, version=0)
class Microsoft_Windows_USB_MAUSBHOST_57_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_Subtype" / Int32ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=58, version=0)
class Microsoft_Windows_USB_MAUSBHOST_58_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_Subtype" / Int32ul,
        "fid_NtStatus" / Int32ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=59, version=0)
class Microsoft_Windows_USB_MAUSBHOST_59_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_Subtype" / Int32ul,
        "fid_Size" / Int32ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=60, version=0)
class Microsoft_Windows_USB_MAUSBHOST_60_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_UsbDevice" / Int64ul,
        "fid_Endpoint" / Int64ul,
        "fid_ObjectHandle" / Int64ul,
        "fid_TransitionType" / Int32ul,
        "fid_SourceState" / Int32ul,
        "fid_Event" / Int32ul,
        "fid_TargetState" / Int32ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=61, version=0)
class Microsoft_Windows_USB_MAUSBHOST_61_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_UsbDevice" / Int64ul,
        "fid_Endpoint" / Int64ul,
        "fid_ObjectHandle" / Int64ul,
        "fid_Exception" / Int32ul,
        "fid_State" / Int32ul,
        "fid_Event" / Int32ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=62, version=0)
class Microsoft_Windows_USB_MAUSBHOST_62_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_UsbDevice" / Int64ul,
        "fid_Endpoint" / Int64ul,
        "fid_ObjectHandle" / Int64ul,
        "fid_TransitionType" / Int32ul,
        "fid_SourceState" / Int32ul,
        "fid_Event" / Int32ul,
        "fid_TargetState" / Int32ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=63, version=0)
class Microsoft_Windows_USB_MAUSBHOST_63_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_UsbDevice" / Int64ul,
        "fid_Endpoint" / Int64ul,
        "fid_ObjectHandle" / Int64ul,
        "fid_Exception" / Int32ul,
        "fid_State" / Int32ul,
        "fid_Event" / Int32ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=64, version=0)
class Microsoft_Windows_USB_MAUSBHOST_64_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_UsbDevice" / Int64ul,
        "fid_Endpoint" / Int64ul,
        "fid_ObjectHandle" / Int64ul,
        "fid_TransitionType" / Int32ul,
        "fid_SourceState" / Int32ul,
        "fid_Event" / Int32ul,
        "fid_TargetState" / Int32ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=65, version=0)
class Microsoft_Windows_USB_MAUSBHOST_65_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_UsbDevice" / Int64ul,
        "fid_Endpoint" / Int64ul,
        "fid_ObjectHandle" / Int64ul,
        "fid_Exception" / Int32ul,
        "fid_State" / Int32ul,
        "fid_Event" / Int32ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=66, version=0)
class Microsoft_Windows_USB_MAUSBHOST_66_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_UsbDevice" / Int64ul,
        "fid_Endpoint" / Int64ul,
        "fid_ObjectHandle" / Int64ul,
        "fid_TransitionType" / Int32ul,
        "fid_SourceState" / Int32ul,
        "fid_Event" / Int32ul,
        "fid_TargetState" / Int32ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=67, version=0)
class Microsoft_Windows_USB_MAUSBHOST_67_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_UsbDevice" / Int64ul,
        "fid_Endpoint" / Int64ul,
        "fid_ObjectHandle" / Int64ul,
        "fid_Exception" / Int32ul,
        "fid_State" / Int32ul,
        "fid_Event" / Int32ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=70, version=0)
class Microsoft_Windows_USB_MAUSBHOST_70_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_UsbDevice" / Int64ul,
        "fid_Endpoint" / Int64ul,
        "fid_MaUsbEndpointHandle" / Int16ul,
        "fid_UsbTransferRequest" / Int64ul,
        "fid_TransferType" / Int32ul,
        "fid_TransferDirection" / Int32ul,
        "fid_TransferBufferLength" / Int32ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=71, version=0)
class Microsoft_Windows_USB_MAUSBHOST_71_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_UsbDevice" / Int64ul,
        "fid_Endpoint" / Int64ul,
        "fid_MaUsbEndpointHandle" / Int16ul,
        "fid_UsbTransferRequest" / Int64ul,
        "fid_BytesTransferred" / Int32ul,
        "fid_NtStatus" / Int32ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=72, version=0)
class Microsoft_Windows_USB_MAUSBHOST_72_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_UsbDevice" / Int64ul,
        "fid_Endpoint" / Int64ul,
        "fid_UsbTransferRequest" / Int64ul,
        "fid_EndpointHandle" / Int16ul,
        "fid_TransferType" / Int32ul,
        "fid_TransferDirection" / Int32ul,
        "fid_RemainingSizeOrCredit" / Int32ul,
        "fid_BytesTotal" / Int32ul,
        "fid_RequestId" / Int8ul,
        "fid_SequenceNumber" / Int32ul,
        "fid_FlagBitRetry" / Int8ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=73, version=0)
class Microsoft_Windows_USB_MAUSBHOST_73_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_UsbDevice" / Int64ul,
        "fid_Endpoint" / Int64ul,
        "fid_UsbTransferRequest" / Int64ul,
        "fid_EndpointHandle" / Int16ul,
        "fid_TransferType" / Int32ul,
        "fid_TransferDirection" / Int32ul,
        "fid_RequestId" / Int8ul,
        "fid_SequenceNumber" / Int32ul,
        "fid_MaUsbStatus" / Int32ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=74, version=0)
class Microsoft_Windows_USB_MAUSBHOST_74_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_UsbDevice" / Int64ul,
        "fid_Endpoint" / Int64ul,
        "fid_EndpointHandle" / Int16ul,
        "fid_TransferType" / Int32ul,
        "fid_TransferDirection" / Int32ul,
        "fid_RequestId" / Int8ul,
        "fid_SequenceNumber" / Int32ul,
        "fid_Length" / Int16ul,
        "fid_MaUsbStatus" / Int32ul,
        "fid_AckRequest" / Int8ul,
        "fid_FlagBitRetry" / Int8ul,
        "fid_RemainingSizeOrCredit" / Int32ul,
        "fid_EndOfTransfer" / Int8ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=75, version=0)
class Microsoft_Windows_USB_MAUSBHOST_75_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_MAUSB_Device_Speed_Capability_Descriptor" / CString
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=76, version=0)
class Microsoft_Windows_USB_MAUSBHOST_76_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_MAUSB_Device_P_Out_Capability_Descriptor" / CString
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=77, version=0)
class Microsoft_Windows_USB_MAUSBHOST_77_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_MAUSB_Device_Speed_Capability_Descriptor" / CString
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=78, version=0)
class Microsoft_Windows_USB_MAUSBHOST_78_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_MAUSB_Device_Synch_Capability_Descriptor" / CString
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=79, version=0)
class Microsoft_Windows_USB_MAUSBHOST_79_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_MAUSB_Device_Container_Id_Capability_Descriptor" / CString
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=80, version=0)
class Microsoft_Windows_USB_MAUSBHOST_80_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_MAUSB_Device_Link_Sleep_Capability_Descriptor" / CString
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=100, version=0)
class Microsoft_Windows_USB_MAUSBHOST_100_0(Etw):
    pattern = Struct(
        "fid_WdfRequest" / Int64ul,
        "fid_Irp" / Int64ul,
        "fid_IoChannelHandle" / Int64ul,
        "fid_NumberOfBytes" / Int64ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=101, version=0)
class Microsoft_Windows_USB_MAUSBHOST_101_0(Etw):
    pattern = Struct(
        "fid_WdfRequest" / Int64ul,
        "fid_Irp" / Int64ul,
        "fid_NumberOfBytes" / Int64ul,
        "fid_NtStatus" / Int32ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=102, version=0)
class Microsoft_Windows_USB_MAUSBHOST_102_0(Etw):
    pattern = Struct(
        "fid_WdfRequest" / Int64ul,
        "fid_IoChannelHandle" / Int64ul,
        "fid_NumberOfBytes" / Int64ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=103, version=0)
class Microsoft_Windows_USB_MAUSBHOST_103_0(Etw):
    pattern = Struct(
        "fid_WdfRequest" / Int64ul,
        "fid_NumberOfBytes" / Int64ul,
        "fid_NtStatus" / Int32ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=104, version=0)
class Microsoft_Windows_USB_MAUSBHOST_104_0(Etw):
    pattern = Struct(
        "fid_FdoContext" / Int64ul,
        "fid_LocalAddressLength" / Int32ul,
        "fid_LocalAddress" / Bytes(lambda this: this.fid_LocalAddressLength),
        "fid_RemoteAddressLength" / Int32ul,
        "fid_RemoteAddress" / Bytes(lambda this: this.fid_RemoteAddressLength),
        "fid_NtStatus" / Int32ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=105, version=0)
class Microsoft_Windows_USB_MAUSBHOST_105_0(Etw):
    pattern = Struct(
        "fid_FdoContext" / Int64ul,
        "fid_NtStatus" / Int32ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=106, version=0)
class Microsoft_Windows_USB_MAUSBHOST_106_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_UsbTtHubDevice" / Int64ul,
        "fid_UsbDevice" / Int64ul,
        "DeviceSpeed" / Int32ul,
        "PortPathDepth" / Int32ul,
        "PortPath" / Int32ul,
        "fid_MaUsbDeviceHandle" / Int32ul,
        "fid_DeviceIsHub" / Int32ul,
        "fid_NumberOfPorts" / Int32ul,
        "fid_NumberOfTTs" / Int32ul,
        "fid_USB_Device_Descriptor" / Float32l
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=108, version=0)
class Microsoft_Windows_USB_MAUSBHOST_108_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_ControllerResetReason" / Int32ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=109, version=0)
class Microsoft_Windows_USB_MAUSBHOST_109_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_UsbDevice" / Int64ul,
        "fid_Endpoint" / Int64ul,
        "fid_USB_Endpoint_Descriptor" / Float32l,
        "fid_IsLinkManaged" / Int8ul,
        "fid_CreditConsumptionUnit" / Int16ul,
        "fid_BufferSize" / Int32ul,
        "fid_IsochProgrammingDelay" / Int16ul,
        "fid_IsochResponseDelay" / Int16ul,
        "fid_IsochSegmentsPerFrame" / Int32ul,
        "fid_MaxIsochSegmentSize" / Int32ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=110, version=0)
class Microsoft_Windows_USB_MAUSBHOST_110_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_UsbDevice" / Int64ul,
        "fid_Endpoint" / Int64ul,
        "fid_ObjectHandle" / Int64ul,
        "fid_TransitionType" / Int32ul,
        "fid_SourceState" / Int32ul,
        "fid_Event" / Int32ul,
        "fid_TargetState" / Int32ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=111, version=0)
class Microsoft_Windows_USB_MAUSBHOST_111_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_UsbDevice" / Int64ul,
        "fid_Endpoint" / Int64ul,
        "fid_ObjectHandle" / Int64ul,
        "fid_Exception" / Int32ul,
        "fid_State" / Int32ul,
        "fid_Event" / Int32ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=112, version=0)
class Microsoft_Windows_USB_MAUSBHOST_112_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_UsbDevice" / Int64ul,
        "fid_Endpoint" / Int64ul,
        "fid_ObjectHandle" / Int64ul,
        "fid_TransitionType" / Int32ul,
        "fid_SourceState" / Int32ul,
        "fid_Event" / Int32ul,
        "fid_TargetState" / Int32ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=113, version=0)
class Microsoft_Windows_USB_MAUSBHOST_113_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_UsbDevice" / Int64ul,
        "fid_Endpoint" / Int64ul,
        "fid_ObjectHandle" / Int64ul,
        "fid_Exception" / Int32ul,
        "fid_State" / Int32ul,
        "fid_Event" / Int32ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=114, version=0)
class Microsoft_Windows_USB_MAUSBHOST_114_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_UsbDevice" / Int64ul,
        "fid_Endpoint" / Int64ul,
        "fid_EndpointHandle" / Int16ul,
        "fid_TransferType" / Int32ul,
        "fid_TransferDirection" / Int32ul,
        "fid_RequestId" / Int8ul,
        "fid_SequenceNumber" / Int32ul,
        "fid_Length" / Int16ul,
        "fid_MaUsbStatus" / Int32ul,
        "fid_AckRequest" / Int8ul,
        "fid_NegativeCredit" / Int8ul,
        "fid_EndOfTransfer" / Int8ul,
        "fid_NumberOfIsochHeaders" / Int16ul,
        "fid_MTDValid" / Int8ul,
        "fid_ASAPDelivery" / Int8ul,
        "fid_PresentationTime" / Int32ul,
        "fid_NumberOfIsochSegments" / Int16ul,
        "fid_NominalBusInterval" / Int32ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=115, version=0)
class Microsoft_Windows_USB_MAUSBHOST_115_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_UsbDevice" / Int64ul,
        "fid_Endpoint" / Int64ul,
        "fid_EndpointHandle" / Int16ul,
        "fid_TransferType" / Int32ul,
        "fid_TransferDirection" / Int32ul,
        "fid_RequestId" / Int8ul,
        "fid_SequenceNumber" / Int32ul,
        "fid_Length" / Int16ul,
        "fid_MaUsbStatus" / Int32ul,
        "fid_AckRequest" / Int8ul,
        "fid_NegativeCredit" / Int8ul,
        "fid_EndOfTransfer" / Int8ul,
        "fid_NumberOfIsochHeaders" / Int16ul,
        "fid_MTDValid" / Int8ul,
        "fid_ASAPDelivery" / Int8ul,
        "fid_PresentationTime" / Int32ul,
        "fid_NumberOfIsochSegments" / Int16ul,
        "fid_NominalBusInterval" / Int32ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=116, version=0)
class Microsoft_Windows_USB_MAUSBHOST_116_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_PortNumber" / Int16ul,
        "fid_RemotePortNumber" / Int16ul,
        "fid_IsUdp" / Int8ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=117, version=0)
class Microsoft_Windows_USB_MAUSBHOST_117_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_PortNumber" / Int16ul,
        "fid_RemotePortNumber" / Int16ul,
        "fid_IsUdp" / Int8ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=118, version=0)
class Microsoft_Windows_USB_MAUSBHOST_118_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_UsbDevice" / Int64ul,
        "fid_Endpoint" / Int64ul,
        "fid_USB_Endpoint_Descriptor" / Float32l,
        "fid_IsLinkManaged" / Int8ul,
        "fid_CreditConsumptionUnit" / Int16ul,
        "fid_BufferSize" / Int32ul,
        "fid_IsochProgrammingDelay" / Int16ul,
        "fid_IsochResponseDelay" / Int16ul,
        "fid_IsochSegmentsPerFrame" / Int32ul,
        "fid_MaxIsochSegmentSize" / Int32ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=119, version=0)
class Microsoft_Windows_USB_MAUSBHOST_119_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_MAUSB_Device_Speed_Capability_Descriptor" / CString
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=120, version=0)
class Microsoft_Windows_USB_MAUSBHOST_120_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_MAUSB_Device_P_Out_Capability_Descriptor" / CString
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=121, version=0)
class Microsoft_Windows_USB_MAUSBHOST_121_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_MAUSB_Device_Speed_Capability_Descriptor" / CString
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=122, version=0)
class Microsoft_Windows_USB_MAUSBHOST_122_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_MAUSB_Device_Synch_Capability_Descriptor" / CString
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=123, version=0)
class Microsoft_Windows_USB_MAUSBHOST_123_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_MAUSB_Device_Container_Id_Capability_Descriptor" / CString
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=124, version=0)
class Microsoft_Windows_USB_MAUSBHOST_124_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_MAUSB_Device_Link_Sleep_Capability_Descriptor" / CString
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=125, version=0)
class Microsoft_Windows_USB_MAUSBHOST_125_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_NumberOfEndpoints" / Int16ul,
        "fid_NumberOfDevices" / Int8ul,
        "fid_NumberOfStreams" / Int8ul,
        "fid_DeviceType" / Int8ul,
        "fid_MaxOutstandingTransferRequests" / Int16ul,
        "fid_MaxOutstandingManagementRequests" / Int16ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=201, version=0)
class Microsoft_Windows_USB_MAUSBHOST_201_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_HeaderVersion" / Int8ul,
        "fid_HeaderFlagBitHost" / Int8ul,
        "fid_HeaderFlagBitRetry" / Int8ul,
        "fid_HeaderFlagBitTimeStamp" / Int8ul,
        "fid_HeaderSubType" / Int8ul,
        "fid_HeaderType" / Int8ul,
        "fid_HeaderLength" / Int16ul,
        "fid_HeaderDeviceHandle" / Int16ul,
        "fid_HeaderDeviceAddress" / Int8ul,
        "fid_HeaderSSID" / Int8ul,
        "fid_HeaderStatusCode" / Int8ul,
        "fid_HeaderDialogToken" / Int16ul,
        "fid_ResponseTimeout" / Int16ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=202, version=0)
class Microsoft_Windows_USB_MAUSBHOST_202_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_HeaderVersion" / Int8ul,
        "fid_HeaderFlagBitHost" / Int8ul,
        "fid_HeaderFlagBitRetry" / Int8ul,
        "fid_HeaderFlagBitTimeStamp" / Int8ul,
        "fid_HeaderSubType" / Int8ul,
        "fid_HeaderType" / Int8ul,
        "fid_HeaderLength" / Int16ul,
        "fid_HeaderDeviceHandle" / Int16ul,
        "fid_HeaderDeviceAddress" / Int8ul,
        "fid_HeaderSSID" / Int8ul,
        "fid_HeaderStatusCode" / Int8ul,
        "fid_HeaderDialogToken" / Int16ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=203, version=0)
class Microsoft_Windows_USB_MAUSBHOST_203_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_HeaderVersion" / Int8ul,
        "fid_HeaderFlagBitHost" / Int8ul,
        "fid_HeaderFlagBitRetry" / Int8ul,
        "fid_HeaderFlagBitTimeStamp" / Int8ul,
        "fid_HeaderSubType" / Int8ul,
        "fid_HeaderType" / Int8ul,
        "fid_HeaderLength" / Int16ul,
        "fid_HeaderDeviceHandle" / Int16ul,
        "fid_HeaderDeviceAddress" / Int8ul,
        "fid_HeaderSSID" / Int8ul,
        "fid_HeaderStatusCode" / Int8ul,
        "fid_HeaderDialogToken" / Int16ul,
        "fid_RouteStringPort1" / Int8ul,
        "fid_RouteStringPort2" / Int8ul,
        "fid_RouteStringPort3" / Int8ul,
        "fid_RouteStringPort4" / Int8ul,
        "fid_RouteStringPort5" / Int8ul,
        "fid_USBSpeed" / Int8ul,
        "fid_HubDeviceHandle" / Int16ul,
        "fid_ParentHSHubDeviceHandle" / Int16ul,
        "fid_ParentHSHubPort" / Int8ul,
        "fid_MTT" / Int8ul,
        "fid_LaneSpeedExponent" / Int8ul,
        "fid_SublinkType" / Int8ul,
        "fid_LaneCount" / Int8ul,
        "fid_LinkProtocol" / Int8ul,
        "fid_LaneSpeedMantissa" / Int16ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=204, version=0)
class Microsoft_Windows_USB_MAUSBHOST_204_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_HeaderVersion" / Int8ul,
        "fid_HeaderFlagBitHost" / Int8ul,
        "fid_HeaderFlagBitRetry" / Int8ul,
        "fid_HeaderFlagBitTimeStamp" / Int8ul,
        "fid_HeaderSubType" / Int8ul,
        "fid_HeaderType" / Int8ul,
        "fid_HeaderLength" / Int16ul,
        "fid_HeaderDeviceHandle" / Int16ul,
        "fid_HeaderDeviceAddress" / Int8ul,
        "fid_HeaderSSID" / Int8ul,
        "fid_HeaderStatusCode" / Int8ul,
        "fid_HeaderDialogToken" / Int16ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=205, version=0)
class Microsoft_Windows_USB_MAUSBHOST_205_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_HeaderVersion" / Int8ul,
        "fid_HeaderFlagBitHost" / Int8ul,
        "fid_HeaderFlagBitRetry" / Int8ul,
        "fid_HeaderFlagBitTimeStamp" / Int8ul,
        "fid_HeaderSubType" / Int8ul,
        "fid_HeaderType" / Int8ul,
        "fid_HeaderLength" / Int16ul,
        "fid_HeaderDeviceHandle" / Int16ul,
        "fid_HeaderDeviceAddress" / Int8ul,
        "fid_HeaderSSID" / Int8ul,
        "fid_HeaderStatusCode" / Int8ul,
        "fid_HeaderDialogToken" / Int16ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=206, version=0)
class Microsoft_Windows_USB_MAUSBHOST_206_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_HeaderVersion" / Int8ul,
        "fid_HeaderFlagBitHost" / Int8ul,
        "fid_HeaderFlagBitRetry" / Int8ul,
        "fid_HeaderFlagBitTimeStamp" / Int8ul,
        "fid_HeaderSubType" / Int8ul,
        "fid_HeaderType" / Int8ul,
        "fid_HeaderLength" / Int16ul,
        "fid_HeaderDeviceHandle" / Int16ul,
        "fid_HeaderDeviceAddress" / Int8ul,
        "fid_HeaderSSID" / Int8ul,
        "fid_HeaderStatusCode" / Int8ul,
        "fid_HeaderDialogToken" / Int16ul,
        "fid_USBDeviceHandle" / Int16ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=207, version=0)
class Microsoft_Windows_USB_MAUSBHOST_207_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_HeaderVersion" / Int8ul,
        "fid_HeaderFlagBitHost" / Int8ul,
        "fid_HeaderFlagBitRetry" / Int8ul,
        "fid_HeaderFlagBitTimeStamp" / Int8ul,
        "fid_HeaderSubType" / Int8ul,
        "fid_HeaderType" / Int8ul,
        "fid_HeaderLength" / Int16ul,
        "fid_HeaderDeviceHandle" / Int16ul,
        "fid_HeaderDeviceAddress" / Int8ul,
        "fid_HeaderSSID" / Int8ul,
        "fid_HeaderStatusCode" / Int8ul,
        "fid_HeaderDialogToken" / Int16ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=208, version=0)
class Microsoft_Windows_USB_MAUSBHOST_208_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_HeaderVersion" / Int8ul,
        "fid_HeaderFlagBitHost" / Int8ul,
        "fid_HeaderFlagBitRetry" / Int8ul,
        "fid_HeaderFlagBitTimeStamp" / Int8ul,
        "fid_HeaderSubType" / Int8ul,
        "fid_HeaderType" / Int8ul,
        "fid_HeaderLength" / Int16ul,
        "fid_HeaderDeviceHandle" / Int16ul,
        "fid_HeaderDeviceAddress" / Int8ul,
        "fid_HeaderSSID" / Int8ul,
        "fid_HeaderStatusCode" / Int8ul,
        "fid_HeaderDialogToken" / Int16ul,
        "fid_EP0Handle" / Int16ul,
        "fid_MaxPacketSize" / Int16ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=209, version=0)
class Microsoft_Windows_USB_MAUSBHOST_209_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_HeaderVersion" / Int8ul,
        "fid_HeaderFlagBitHost" / Int8ul,
        "fid_HeaderFlagBitRetry" / Int8ul,
        "fid_HeaderFlagBitTimeStamp" / Int8ul,
        "fid_HeaderSubType" / Int8ul,
        "fid_HeaderType" / Int8ul,
        "fid_HeaderLength" / Int16ul,
        "fid_HeaderDeviceHandle" / Int16ul,
        "fid_HeaderDeviceAddress" / Int8ul,
        "fid_HeaderSSID" / Int8ul,
        "fid_HeaderStatusCode" / Int8ul,
        "fid_HeaderDialogToken" / Int16ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=210, version=0)
class Microsoft_Windows_USB_MAUSBHOST_210_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_HeaderVersion" / Int8ul,
        "fid_HeaderFlagBitHost" / Int8ul,
        "fid_HeaderFlagBitRetry" / Int8ul,
        "fid_HeaderFlagBitTimeStamp" / Int8ul,
        "fid_HeaderSubType" / Int8ul,
        "fid_HeaderType" / Int8ul,
        "fid_HeaderLength" / Int16ul,
        "fid_HeaderDeviceHandle" / Int16ul,
        "fid_HeaderDeviceAddress" / Int8ul,
        "fid_HeaderSSID" / Int8ul,
        "fid_HeaderStatusCode" / Int8ul,
        "fid_HeaderDialogToken" / Int16ul,
        "fid_NumberOfEpHandlesToInactivate" / Int8ul,
        "fid_SuspendFlag" / Int8ul,
        "fid_EndpointHandle" / Int16ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=211, version=0)
class Microsoft_Windows_USB_MAUSBHOST_211_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_HeaderVersion" / Int8ul,
        "fid_HeaderFlagBitHost" / Int8ul,
        "fid_HeaderFlagBitRetry" / Int8ul,
        "fid_HeaderFlagBitTimeStamp" / Int8ul,
        "fid_HeaderSubType" / Int8ul,
        "fid_HeaderType" / Int8ul,
        "fid_HeaderLength" / Int16ul,
        "fid_HeaderDeviceHandle" / Int16ul,
        "fid_HeaderDeviceAddress" / Int8ul,
        "fid_HeaderSSID" / Int8ul,
        "fid_HeaderStatusCode" / Int8ul,
        "fid_HeaderDialogToken" / Int16ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=212, version=0)
class Microsoft_Windows_USB_MAUSBHOST_212_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_HeaderVersion" / Int8ul,
        "fid_HeaderFlagBitHost" / Int8ul,
        "fid_HeaderFlagBitRetry" / Int8ul,
        "fid_HeaderFlagBitTimeStamp" / Int8ul,
        "fid_HeaderSubType" / Int8ul,
        "fid_HeaderType" / Int8ul,
        "fid_HeaderLength" / Int16ul,
        "fid_HeaderDeviceHandle" / Int16ul,
        "fid_HeaderDeviceAddress" / Int8ul,
        "fid_HeaderSSID" / Int8ul,
        "fid_HeaderStatusCode" / Int8ul,
        "fid_HeaderDialogToken" / Int16ul,
        "fid_UpdateDevReqFields" / Int32ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=213, version=0)
class Microsoft_Windows_USB_MAUSBHOST_213_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_HeaderVersion" / Int8ul,
        "fid_HeaderFlagBitHost" / Int8ul,
        "fid_HeaderFlagBitRetry" / Int8ul,
        "fid_HeaderFlagBitTimeStamp" / Int8ul,
        "fid_HeaderSubType" / Int8ul,
        "fid_HeaderType" / Int8ul,
        "fid_HeaderLength" / Int16ul,
        "fid_HeaderDeviceHandle" / Int16ul,
        "fid_HeaderDeviceAddress" / Int8ul,
        "fid_HeaderSSID" / Int8ul,
        "fid_HeaderStatusCode" / Int8ul,
        "fid_HeaderDialogToken" / Int16ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=214, version=0)
class Microsoft_Windows_USB_MAUSBHOST_214_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_HeaderVersion" / Int8ul,
        "fid_HeaderFlagBitHost" / Int8ul,
        "fid_HeaderFlagBitRetry" / Int8ul,
        "fid_HeaderFlagBitTimeStamp" / Int8ul,
        "fid_HeaderSubType" / Int8ul,
        "fid_HeaderType" / Int8ul,
        "fid_HeaderLength" / Int16ul,
        "fid_HeaderDeviceHandle" / Int16ul,
        "fid_HeaderDeviceAddress" / Int8ul,
        "fid_HeaderSSID" / Int8ul,
        "fid_HeaderStatusCode" / Int8ul,
        "fid_HeaderDialogToken" / Int16ul,
        "fid_NumberOfEpHandlesWithError" / Int8ul,
        "fid_EndpointHandle" / Int16ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=215, version=0)
class Microsoft_Windows_USB_MAUSBHOST_215_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_HeaderVersion" / Int8ul,
        "fid_HeaderFlagBitHost" / Int8ul,
        "fid_HeaderFlagBitRetry" / Int8ul,
        "fid_HeaderFlagBitTimeStamp" / Int8ul,
        "fid_HeaderSubType" / Int8ul,
        "fid_HeaderType" / Int8ul,
        "fid_HeaderLength" / Int16ul,
        "fid_HeaderDeviceHandle" / Int16ul,
        "fid_HeaderDeviceAddress" / Int8ul,
        "fid_HeaderSSID" / Int8ul,
        "fid_HeaderStatusCode" / Int8ul,
        "fid_HeaderDialogToken" / Int16ul,
        "fid_NumberOfEpHandlesToDelete" / Int8ul,
        "fid_EndpointHandle" / Int16ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=216, version=0)
class Microsoft_Windows_USB_MAUSBHOST_216_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_HeaderVersion" / Int8ul,
        "fid_HeaderFlagBitHost" / Int8ul,
        "fid_HeaderFlagBitRetry" / Int8ul,
        "fid_HeaderFlagBitTimeStamp" / Int8ul,
        "fid_HeaderSubType" / Int8ul,
        "fid_HeaderType" / Int8ul,
        "fid_HeaderLength" / Int16ul,
        "fid_HeaderDeviceHandle" / Int16ul,
        "fid_HeaderDeviceAddress" / Int8ul,
        "fid_HeaderSSID" / Int8ul,
        "fid_HeaderStatusCode" / Int8ul,
        "fid_HeaderDialogToken" / Int16ul,
        "fid_NumberOfEpHandlesWithError" / Int8ul,
        "fid_EndpointHandle" / Int16ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=217, version=0)
class Microsoft_Windows_USB_MAUSBHOST_217_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_HeaderVersion" / Int8ul,
        "fid_HeaderFlagBitHost" / Int8ul,
        "fid_HeaderFlagBitRetry" / Int8ul,
        "fid_HeaderFlagBitTimeStamp" / Int8ul,
        "fid_HeaderSubType" / Int8ul,
        "fid_HeaderType" / Int8ul,
        "fid_HeaderLength" / Int16ul,
        "fid_HeaderDeviceHandle" / Int16ul,
        "fid_HeaderDeviceAddress" / Int8ul,
        "fid_HeaderSSID" / Int8ul,
        "fid_HeaderStatusCode" / Int8ul,
        "fid_HeaderDialogToken" / Int16ul,
        "fid_NumberOfEPHandlesWithError" / Int8ul,
        "fid_EPHandle" / Int16ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=218, version=0)
class Microsoft_Windows_USB_MAUSBHOST_218_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_HeaderVersion" / Int8ul,
        "fid_HeaderFlagBitHost" / Int8ul,
        "fid_HeaderFlagBitRetry" / Int8ul,
        "fid_HeaderFlagBitTimeStamp" / Int8ul,
        "fid_HeaderSubType" / Int8ul,
        "fid_HeaderType" / Int8ul,
        "fid_HeaderLength" / Int16ul,
        "fid_HeaderDeviceHandle" / Int16ul,
        "fid_HeaderDeviceAddress" / Int8ul,
        "fid_HeaderSSID" / Int8ul,
        "fid_HeaderStatusCode" / Int8ul,
        "fid_HeaderDialogToken" / Int16ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=219, version=0)
class Microsoft_Windows_USB_MAUSBHOST_219_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_HeaderVersion" / Int8ul,
        "fid_HeaderFlagBitHost" / Int8ul,
        "fid_HeaderFlagBitRetry" / Int8ul,
        "fid_HeaderFlagBitTimeStamp" / Int8ul,
        "fid_HeaderSubType" / Int8ul,
        "fid_HeaderType" / Int8ul,
        "fid_HeaderLength" / Int16ul,
        "fid_HeaderDeviceHandle" / Int16ul,
        "fid_HeaderDeviceAddress" / Int8ul,
        "fid_HeaderSSID" / Int8ul,
        "fid_HeaderStatusCode" / Int8ul,
        "fid_HeaderDialogToken" / Int16ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=220, version=0)
class Microsoft_Windows_USB_MAUSBHOST_220_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_HeaderVersion" / Int8ul,
        "fid_HeaderFlagBitHost" / Int8ul,
        "fid_HeaderFlagBitRetry" / Int8ul,
        "fid_HeaderFlagBitTimeStamp" / Int8ul,
        "fid_HeaderSubType" / Int8ul,
        "fid_HeaderType" / Int8ul,
        "fid_HeaderLength" / Int16ul,
        "fid_HeaderDeviceHandle" / Int16ul,
        "fid_HeaderDeviceAddress" / Int8ul,
        "fid_HeaderSSID" / Int8ul,
        "fid_HeaderStatusCode" / Int8ul,
        "fid_HeaderDialogToken" / Int16ul,
        "fid_NumberOfEPResetInformationBlocks" / Int8ul,
        "fid_EPHandle" / Int16ul,
        "fid_TransferStatePreserve" / Int8ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=221, version=0)
class Microsoft_Windows_USB_MAUSBHOST_221_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_HeaderVersion" / Int8ul,
        "fid_HeaderFlagBitHost" / Int8ul,
        "fid_HeaderFlagBitRetry" / Int8ul,
        "fid_HeaderFlagBitTimeStamp" / Int8ul,
        "fid_HeaderSubType" / Int8ul,
        "fid_HeaderType" / Int8ul,
        "fid_HeaderLength" / Int16ul,
        "fid_HeaderDeviceHandle" / Int16ul,
        "fid_HeaderDeviceAddress" / Int8ul,
        "fid_HeaderSSID" / Int8ul,
        "fid_HeaderStatusCode" / Int8ul,
        "fid_HeaderDialogToken" / Int16ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=222, version=0)
class Microsoft_Windows_USB_MAUSBHOST_222_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_HeaderVersion" / Int8ul,
        "fid_HeaderFlagBitHost" / Int8ul,
        "fid_HeaderFlagBitRetry" / Int8ul,
        "fid_HeaderFlagBitTimeStamp" / Int8ul,
        "fid_HeaderSubType" / Int8ul,
        "fid_HeaderType" / Int8ul,
        "fid_HeaderLength" / Int16ul,
        "fid_HeaderDeviceHandle" / Int16ul,
        "fid_HeaderDeviceAddress" / Int8ul,
        "fid_HeaderSSID" / Int8ul,
        "fid_HeaderStatusCode" / Int8ul,
        "fid_HeaderDialogToken" / Int16ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=223, version=0)
class Microsoft_Windows_USB_MAUSBHOST_223_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_HeaderVersion" / Int8ul,
        "fid_HeaderFlagBitHost" / Int8ul,
        "fid_HeaderFlagBitRetry" / Int8ul,
        "fid_HeaderFlagBitTimeStamp" / Int8ul,
        "fid_HeaderSubType" / Int8ul,
        "fid_HeaderType" / Int8ul,
        "fid_HeaderLength" / Int16ul,
        "fid_HeaderDeviceHandle" / Int16ul,
        "fid_HeaderDeviceAddress" / Int8ul,
        "fid_HeaderSSID" / Int8ul,
        "fid_HeaderStatusCode" / Int8ul,
        "fid_HeaderDialogToken" / Int16ul,
        "fid_UsbDeviceAddress" / Int8ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=224, version=0)
class Microsoft_Windows_USB_MAUSBHOST_224_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_HeaderVersion" / Int8ul,
        "fid_HeaderFlagBitHost" / Int8ul,
        "fid_HeaderFlagBitRetry" / Int8ul,
        "fid_HeaderFlagBitTimeStamp" / Int8ul,
        "fid_HeaderSubType" / Int8ul,
        "fid_HeaderType" / Int8ul,
        "fid_HeaderLength" / Int16ul,
        "fid_HeaderDeviceHandle" / Int16ul,
        "fid_HeaderDeviceAddress" / Int8ul,
        "fid_HeaderSSID" / Int8ul,
        "fid_HeaderStatusCode" / Int8ul,
        "fid_HeaderDialogToken" / Int16ul,
        "fid_NumberOfEpDescriptors" / Int8ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=225, version=0)
class Microsoft_Windows_USB_MAUSBHOST_225_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_HeaderVersion" / Int8ul,
        "fid_HeaderFlagBitHost" / Int8ul,
        "fid_HeaderFlagBitRetry" / Int8ul,
        "fid_HeaderFlagBitTimeStamp" / Int8ul,
        "fid_HeaderSubType" / Int8ul,
        "fid_HeaderType" / Int8ul,
        "fid_HeaderLength" / Int16ul,
        "fid_HeaderDeviceHandle" / Int16ul,
        "fid_HeaderDeviceAddress" / Int8ul,
        "fid_HeaderSSID" / Int8ul,
        "fid_HeaderStatusCode" / Int8ul,
        "fid_HeaderDialogToken" / Int16ul,
        "fid_NumberOfEndpoints" / Int16ul,
        "fid_NumberOfDevices" / Int8ul,
        "fid_NumberOfStreams" / Int8ul,
        "fid_DeviceType" / Int8ul,
        "fid_DescriptorCount" / Int8ul,
        "fid_DescriptorLength" / Int32ul,
        "fid_MaxOutstandingTransferRequests" / Int16ul,
        "fid_MaxOutstandingManagementRequests" / Int16ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=226, version=0)
class Microsoft_Windows_USB_MAUSBHOST_226_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_HeaderVersion" / Int8ul,
        "fid_HeaderFlagBitHost" / Int8ul,
        "fid_HeaderFlagBitRetry" / Int8ul,
        "fid_HeaderFlagBitTimeStamp" / Int8ul,
        "fid_HeaderSubType" / Int8ul,
        "fid_HeaderType" / Int8ul,
        "fid_HeaderLength" / Int16ul,
        "fid_HeaderDeviceHandle" / Int16ul,
        "fid_HeaderDeviceAddress" / Int8ul,
        "fid_HeaderSSID" / Int8ul,
        "fid_HeaderStatusCode" / Int8ul,
        "fid_HeaderDialogToken" / Int16ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=227, version=0)
class Microsoft_Windows_USB_MAUSBHOST_227_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_HeaderVersion" / Int8ul,
        "fid_HeaderFlagBitHost" / Int8ul,
        "fid_HeaderFlagBitRetry" / Int8ul,
        "fid_HeaderFlagBitTimeStamp" / Int8ul,
        "fid_HeaderSubType" / Int8ul,
        "fid_HeaderType" / Int8ul,
        "fid_HeaderLength" / Int16ul,
        "fid_HeaderDeviceHandle" / Int16ul,
        "fid_HeaderDeviceAddress" / Int8ul,
        "fid_HeaderSSID" / Int8ul,
        "fid_HeaderStatusCode" / Int8ul,
        "fid_HeaderDialogToken" / Int16ul,
        "fid_NumberOfEpHandlesWithError" / Int8ul,
        "fid_EndpointHandle" / Int16ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=228, version=0)
class Microsoft_Windows_USB_MAUSBHOST_228_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_HeaderVersion" / Int8ul,
        "fid_HeaderFlagBitHost" / Int8ul,
        "fid_HeaderFlagBitRetry" / Int8ul,
        "fid_HeaderFlagBitTimeStamp" / Int8ul,
        "fid_HeaderSubType" / Int8ul,
        "fid_HeaderType" / Int8ul,
        "fid_HeaderLength" / Int16ul,
        "fid_HeaderDeviceHandle" / Int16ul,
        "fid_HeaderDeviceAddress" / Int8ul,
        "fid_HeaderSSID" / Int8ul,
        "fid_HeaderStatusCode" / Int8ul,
        "fid_HeaderDialogToken" / Int16ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=229, version=0)
class Microsoft_Windows_USB_MAUSBHOST_229_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_HeaderVersion" / Int8ul,
        "fid_HeaderFlagBitHost" / Int8ul,
        "fid_HeaderFlagBitRetry" / Int8ul,
        "fid_HeaderFlagBitTimeStamp" / Int8ul,
        "fid_HeaderSubType" / Int8ul,
        "fid_HeaderType" / Int8ul,
        "fid_HeaderLength" / Int16ul,
        "fid_HeaderDeviceHandle" / Int16ul,
        "fid_HeaderDeviceAddress" / Int8ul,
        "fid_HeaderSSID" / Int8ul,
        "fid_HeaderStatusCode" / Int8ul,
        "fid_HeaderDialogToken" / Int16ul,
        "fid_EP0Handle" / Int16ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=230, version=0)
class Microsoft_Windows_USB_MAUSBHOST_230_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_HeaderVersion" / Int8ul,
        "fid_HeaderFlagBitHost" / Int8ul,
        "fid_HeaderFlagBitRetry" / Int8ul,
        "fid_HeaderFlagBitTimeStamp" / Int8ul,
        "fid_HeaderSubType" / Int8ul,
        "fid_HeaderType" / Int8ul,
        "fid_HeaderLength" / Int16ul,
        "fid_HeaderDeviceHandle" / Int16ul,
        "fid_HeaderDeviceAddress" / Int8ul,
        "fid_HeaderSSID" / Int8ul,
        "fid_HeaderStatusCode" / Int8ul,
        "fid_HeaderDialogToken" / Int16ul,
        "fid_NumberOfEpDescriptors" / Int8ul,
        "fid_SizeOfEPDescriptor" / Int8ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=231, version=0)
class Microsoft_Windows_USB_MAUSBHOST_231_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_HeaderVersion" / Int8ul,
        "fid_HeaderFlagBitHost" / Int8ul,
        "fid_HeaderFlagBitRetry" / Int8ul,
        "fid_HeaderFlagBitTimeStamp" / Int8ul,
        "fid_HeaderSubType" / Int8ul,
        "fid_HeaderType" / Int8ul,
        "fid_HeaderLength" / Int16ul,
        "fid_HeaderDeviceHandle" / Int16ul,
        "fid_HeaderDeviceAddress" / Int8ul,
        "fid_HeaderSSID" / Int8ul,
        "fid_HeaderStatusCode" / Int8ul,
        "fid_HeaderDialogToken" / Int16ul,
        "fid_NumberOfEpHandlesToActivate" / Int8ul,
        "fid_EndpointHandle" / Int16ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=232, version=0)
class Microsoft_Windows_USB_MAUSBHOST_232_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_HeaderVersion" / Int8ul,
        "fid_HeaderFlagBitHost" / Int8ul,
        "fid_HeaderFlagBitRetry" / Int8ul,
        "fid_HeaderFlagBitTimeStamp" / Int8ul,
        "fid_HeaderSubType" / Int8ul,
        "fid_HeaderType" / Int8ul,
        "fid_HeaderLength" / Int16ul,
        "fid_HeaderDeviceHandle" / Int16ul,
        "fid_HeaderDeviceAddress" / Int8ul,
        "fid_HeaderSSID" / Int8ul,
        "fid_HeaderStatusCode" / Int8ul,
        "fid_HeaderDialogToken" / Int16ul
    )


@declare(guid=guid("7725b5f9-1f2e-4e21-baeb-b2af4690bc87"), event_id=233, version=0)
class Microsoft_Windows_USB_MAUSBHOST_233_0(Etw):
    pattern = Struct(
        "fid_Controller" / Int64ul,
        "fid_HeaderVersion" / Int8ul,
        "fid_HeaderFlagBitHost" / Int8ul,
        "fid_HeaderFlagBitRetry" / Int8ul,
        "fid_HeaderFlagBitTimeStamp" / Int8ul,
        "fid_HeaderSubType" / Int8ul,
        "fid_HeaderType" / Int8ul,
        "fid_HeaderLength" / Int16ul,
        "fid_HeaderDeviceHandle" / Int16ul,
        "fid_HeaderDeviceAddress" / Int8ul,
        "fid_HeaderSSID" / Int8ul,
        "fid_HeaderStatusCode" / Int8ul,
        "fid_HeaderDialogToken" / Int16ul
    )

