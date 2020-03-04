# -*- coding: utf-8 -*-
"""
This is wmi trace header declaration

WMI Headers are a subset of system trace header
"""

from construct import Enum, Int32ul, Struct, Int16ul, Int64ul, Int8ul, Bytes, \
    Const, FlagsEnum, Int32sl, BitStruct, BitsInteger

from etl.utils import check_enum


"""
Hook id is the id of underlying message
It refer to a GUID but more compacted
:see: https://www.geoffchappell.com/studies/windows/km/ntoskrnl/api/etw/callouts/hookid.htm?tx=40
"""
EventTraceGroup = Enum(
    Int8ul,
    EVENT_TRACE_GROUP_HEADER=0x00,
    EVENT_TRACE_GROUP_IO=0x01,
    EVENT_TRACE_GROUP_MEMORY=0x02,
    EVENT_TRACE_GROUP_PROCESS=0x03,
    EVENT_TRACE_GROUP_FILE=0x04,
    EVENT_TRACE_GROUP_THREAD=0x05,
    EVENT_TRACE_GROUP_TCPIP=0x06,
    EVENT_TRACE_GROUP_JOB=0x07,
    EVENT_TRACE_GROUP_UDPIP=0x08,
    EVENT_TRACE_GROUP_REGISTRY=0x09,
    EVENT_TRACE_GROUP_DBGPRINT=0x0a,
    EVENT_TRACE_GROUP_CONFIG=0x0b,
    EVENT_TRACE_GROUP_SPARE1=0x0c,
    EVENT_TRACE_GROUP_WNF=0x0d,
    EVENT_TRACE_GROUP_POOL=0x0e,
    EVENT_TRACE_GROUP_PERFINFO=0x0f,
    EVENT_TRACE_GROUP_HEAP=0x10,
    EVENT_TRACE_GROUP_OBJECT=0x11,
    EVENT_TRACE_GROUP_POWER=0x12,
    EVENT_TRACE_GROUP_MODBOUND=0x13,
    EVENT_TRACE_GROUP_IMAGE=0x14,
    EVENT_TRACE_GROUP_DPC=0x15,
    EVENT_TRACE_GROUP_GDI=0x16,
    EVENT_TRACE_GROUP_CRITSEC=0x17,
    EVENT_TRACE_GROUP_STACKWALK=0x18,
    EVENT_TRACE_GROUP_UMS=0x19,
    EVENT_TRACE_GROUP_ALPC=0x1a,
    EVENT_TRACE_GROUP_SPLITIO=0x1b,
    EVENT_TRACE_GROUP_THREAD_POOL=0x1c,
    EVENT_TRACE_GROUP_HYPERVISOR=0x1d,
    EVENT_TRACE_GROUP_HYPERVISORX=0x1e,
)


"""
Different flags use in the trace header to determine the nature of the event
:see: https://www.geoffchappell.com/studies/windows/km/ntoskrnl/api/etw/tracelog/wmi_buffer_header.htm
"""
EtwBufferFlag = FlagsEnum(
    Int16ul,
    ETW_BUFFER_FLAG_NORMAL=0x0,
    ETW_BUFFER_FLAG_FLUSH_MARKER=0x1,
    ETW_BUFFER_FLAG_EVENTS_LOST=0x2,
    ETW_BUFFER_FLAG_BUFFER_LOST=0x4,
    ETW_BUFFER_FLAG_RTBACKUP_CORRUPT=0x8,
    ETW_BUFFER_FLAG_RTBACKUP=0x10,
    ETW_BUFFER_FLAG_PROC_INDEX=0x20,
    ETW_BUFFER_FLAG_COMPRESSED=0x40
)

"""
The nature of the buffer use to generate the event (ETW)
:see: https://www.geoffchappell.com/studies/windows/km/ntoskrnl/api/etw/tracelog/wmi_buffer_header.htm
"""
EtwBufferType = Enum(
    Int16ul,
    ETW_BUFFER_TYPE_GENERIC=0x0,
    ETW_BUFFER_TYPE_RUNDOWN=0x1,
    ETW_BUFFER_TYPE_CTX_SWAP=0x2,
    ETW_BUFFER_TYPE_REFTIME=0x3,
    ETW_BUFFER_TYPE_HEADER=0x4,
    ETW_BUFFER_TYPE_BATCHED=0x5,
    ETW_BUFFER_TYPE_EMPTY_MARKER=0x6,
    ETW_BUFFER_TYPE_DBG_INFO=0x7,
    ETW_BUFFER_TYPE_MAXIMUM=0x8
)

"""
identify the sender
:see: https://www.geoffchappell.com/studies/windows/km/ntoskrnl/api/etw/tracelog/wmi_buffer_header.htm
"""
EtwBufferContext = Struct(
    "processor_index" / Int16ul,
    "logger_id" / Int16ul
)


"""
Common header for system and perf message
:see: https://www.geoffchappell.com/studies/windows/km/ntoskrnl/api/etw/tracelog/wmi_buffer_header.htm
"""
WnodeHeader = Struct(
    "buffer_size" / Int32ul,
    "saved_offset" / Int32ul,
    "current_offset" / Int32ul,
    "reference_count" / Int32sl,
    "timestamp" / Int64ul,
    "sequence_number" / Int64ul,
    "clock" / BitStruct(
        "type" / BitsInteger(3),
        "frequency" / BitsInteger(61)
    ),
    "client_context" / EtwBufferContext,
    "state" / Int32ul,
)

WmiBufferHeader = Struct(
    "wnode" / WnodeHeader,
    "offset" / Int32ul,
    "buffer_flag" / EtwBufferFlag,
    "buffer_type" / EtwBufferType,
    "padding" / Bytes(16)
)

WmiTracePacket = Struct(
    "size" / Int16ul,
    "type" / Int8ul,    # Do not check because most of them are not documented
    "group" / EventTraceGroup
)


def wmi_trace_marker(marker: Enum) -> Struct:
    """
    Generate a WMI base a specific marker
    Trace marker is used to identify the underlying object
    :param marker Enum: Check the value of the enum during reading
    :return: The struct object of the wmi trace marker
    """
    return Struct(
        "version" / Int16ul,
        "type" / check_enum(marker),
        "flags" / Const(0xc0, Int8ul)
    )


