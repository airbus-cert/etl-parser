# -*- coding: utf-8 -*-
"""
Microsoft-Windows-RTWorkQueue-Threading
GUID : e18d0fc9-9515-4232-98e4-89e456d8551b
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("e18d0fc9-9515-4232-98e4-89e456d8551b"), event_id=4435, version=0)
class Microsoft_Windows_RTWorkQueue_Threading_4435_0(Etw):
    pattern = Struct(
        "WorkQueuePointer" / Int64ul,
        "WorkQueueID" / Int32ul,
        "AsyncResult" / Int64ul,
        "LongRunning" / Int8ul
    )


@declare(guid=guid("e18d0fc9-9515-4232-98e4-89e456d8551b"), event_id=4436, version=0)
class Microsoft_Windows_RTWorkQueue_Threading_4436_0(Etw):
    pattern = Struct(
        "WorkQueuePointer" / Int64ul,
        "WorkQueueID" / Int32ul,
        "AsyncResult" / Int64ul,
        "LongRunning" / Int8ul
    )


@declare(guid=guid("e18d0fc9-9515-4232-98e4-89e456d8551b"), event_id=4437, version=0)
class Microsoft_Windows_RTWorkQueue_Threading_4437_0(Etw):
    pattern = Struct(
        "WorkQueuePointer" / Int64ul,
        "QueueDepth" / Int32sl,
        "AsyncResult" / Int64ul
    )


@declare(guid=guid("e18d0fc9-9515-4232-98e4-89e456d8551b"), event_id=4438, version=0)
class Microsoft_Windows_RTWorkQueue_Threading_4438_0(Etw):
    pattern = Struct(
        "WorkQueuePointer" / Int64ul,
        "QueueDepth" / Int32sl,
        "AsyncResult" / Int64ul
    )


@declare(guid=guid("e18d0fc9-9515-4232-98e4-89e456d8551b"), event_id=4439, version=0)
class Microsoft_Windows_RTWorkQueue_Threading_4439_0(Etw):
    pattern = Struct(
        "WorkQueuePointer" / Int64ul,
        "WordQueueID" / Int32ul,
        "ThreadCount" / Int32ul,
        "ThreadID" / Int32ul
    )


@declare(guid=guid("e18d0fc9-9515-4232-98e4-89e456d8551b"), event_id=4440, version=0)
class Microsoft_Windows_RTWorkQueue_Threading_4440_0(Etw):
    pattern = Struct(
        "WorkQueuePointer" / Int64ul,
        "WordQueueID" / Int32ul,
        "ThreadCount" / Int32ul,
        "ThreadID" / Int32ul
    )


@declare(guid=guid("e18d0fc9-9515-4232-98e4-89e456d8551b"), event_id=4454, version=0)
class Microsoft_Windows_RTWorkQueue_Threading_4454_0(Etw):
    pattern = Struct(
        "Queue" / Int64ul,
        "ThreadID" / Int32ul,
        "Handle" / Int64ul,
        "Error" / Int32ul,
        "Class" / WString,
        "Priority" / Int32sl,
        "TaskID" / Int32ul
    )


@declare(guid=guid("e18d0fc9-9515-4232-98e4-89e456d8551b"), event_id=4455, version=0)
class Microsoft_Windows_RTWorkQueue_Threading_4455_0(Etw):
    pattern = Struct(
        "Queue" / Int64ul,
        "ThreadID" / Int32ul,
        "Handle" / Int64ul,
        "Error" / Int32ul,
        "Class" / WString,
        "Priority" / Int32sl,
        "TaskID" / Int32ul
    )


@declare(guid=guid("e18d0fc9-9515-4232-98e4-89e456d8551b"), event_id=4472, version=0)
class Microsoft_Windows_RTWorkQueue_Threading_4472_0(Etw):
    pattern = Struct(
        "WorkQueuePointer" / Int64ul,
        "WorkQueueID" / Int32sl,
        "Flags" / Int32ul
    )


@declare(guid=guid("e18d0fc9-9515-4232-98e4-89e456d8551b"), event_id=4473, version=0)
class Microsoft_Windows_RTWorkQueue_Threading_4473_0(Etw):
    pattern = Struct(
        "WorkQueuePointer" / Int64ul,
        "WorkQueueID" / Int32sl,
        "Flags" / Int32ul
    )


@declare(guid=guid("e18d0fc9-9515-4232-98e4-89e456d8551b"), event_id=4474, version=0)
class Microsoft_Windows_RTWorkQueue_Threading_4474_0(Etw):
    pattern = Struct(
        "WorkQueuePointer" / Int64ul,
        "WorkQueueID" / Int32ul,
        "BaseWorkQueueID" / Int32ul,
        "ThreadID" / Int32ul,
        "AsyncResult" / Int64ul,
        "AsyncResultVTable" / Int64ul,
        "LongRunning" / Int8ul
    )


@declare(guid=guid("e18d0fc9-9515-4232-98e4-89e456d8551b"), event_id=4475, version=0)
class Microsoft_Windows_RTWorkQueue_Threading_4475_0(Etw):
    pattern = Struct(
        "WorkQueuePointer" / Int64ul,
        "WorkQueueID" / Int32ul,
        "BaseWorkQueueID" / Int32ul,
        "ThreadID" / Int32ul,
        "AsyncResult" / Int64ul,
        "AsyncResultVTable" / Int64ul,
        "LongRunning" / Int8ul
    )


@declare(guid=guid("e18d0fc9-9515-4232-98e4-89e456d8551b"), event_id=4476, version=0)
class Microsoft_Windows_RTWorkQueue_Threading_4476_0(Etw):
    pattern = Struct(
        "WorkQueuePointer" / Int64ul,
        "WorkQueueID" / Int32ul,
        "Class" / WString,
        "Priority" / Int32sl,
        "TaskID" / Int32ul
    )


@declare(guid=guid("e18d0fc9-9515-4232-98e4-89e456d8551b"), event_id=4477, version=0)
class Microsoft_Windows_RTWorkQueue_Threading_4477_0(Etw):
    pattern = Struct(
        "WorkQueuePointer" / Int64ul,
        "WorkQueueID" / Int32ul,
        "Class" / WString,
        "Priority" / Int32sl,
        "TaskID" / Int32ul
    )


@declare(guid=guid("e18d0fc9-9515-4232-98e4-89e456d8551b"), event_id=4478, version=0)
class Microsoft_Windows_RTWorkQueue_Threading_4478_0(Etw):
    pattern = Struct(
        "WorkQueuePointer" / Int64ul,
        "WorkQueueID" / Int32ul,
        "TaskID" / Int32ul,
        "PreviousDeadline" / Int64sl,
        "NextDeadline" / Int64sl,
        "lDelay_ms" / Int32sl,
        "lPreDelay_ms" / Int32sl
    )


@declare(guid=guid("e18d0fc9-9515-4232-98e4-89e456d8551b"), event_id=4479, version=0)
class Microsoft_Windows_RTWorkQueue_Threading_4479_0(Etw):
    pattern = Struct(
        "WorkQueuePointer" / Int64ul,
        "WorkQueueID" / Int32ul,
        "TaskID" / Int32ul,
        "PreviousDeadline" / Int64sl,
        "NextDeadline" / Int64sl,
        "lDelay_ms" / Int32sl,
        "lPreDelay_ms" / Int32sl
    )


@declare(guid=guid("e18d0fc9-9515-4232-98e4-89e456d8551b"), event_id=4480, version=0)
class Microsoft_Windows_RTWorkQueue_Threading_4480_0(Etw):
    pattern = Struct(
        "WorkQueuePointer" / Int64ul,
        "WorkQueueID" / Int32ul,
        "ItemPointer" / Int64ul,
        "GlobalDeadline" / Int64sl,
        "DeltaAhead_usec" / Int64sl
    )


@declare(guid=guid("e18d0fc9-9515-4232-98e4-89e456d8551b"), event_id=4481, version=0)
class Microsoft_Windows_RTWorkQueue_Threading_4481_0(Etw):
    pattern = Struct(
        "WorkQueuePointer" / Int64ul,
        "WorkQueueID" / Int32ul,
        "ItemPointer" / Int64ul,
        "GlobalDeadline" / Int64sl,
        "DeltaAhead_usec" / Int64sl
    )


@declare(guid=guid("e18d0fc9-9515-4232-98e4-89e456d8551b"), event_id=4482, version=0)
class Microsoft_Windows_RTWorkQueue_Threading_4482_0(Etw):
    pattern = Struct(
        "WorkQueuePointer" / Int64ul,
        "WorkQueueID" / Int32ul,
        "ItemPointer" / Int64ul,
        "GlobalDeadline" / Int64sl,
        "DeltaAhead_usec" / Int64sl
    )


@declare(guid=guid("e18d0fc9-9515-4232-98e4-89e456d8551b"), event_id=4483, version=0)
class Microsoft_Windows_RTWorkQueue_Threading_4483_0(Etw):
    pattern = Struct(
        "WorkQueuePointer" / Int64ul,
        "WorkQueueID" / Int32ul,
        "ItemPointer" / Int64ul,
        "GlobalDeadline" / Int64sl,
        "DeltaAhead_usec" / Int64sl
    )


@declare(guid=guid("e18d0fc9-9515-4232-98e4-89e456d8551b"), event_id=4484, version=0)
class Microsoft_Windows_RTWorkQueue_Threading_4484_0(Etw):
    pattern = Struct(
        "WorkQueueID" / Int32ul,
        "Yield" / Int32ul
    )


@declare(guid=guid("e18d0fc9-9515-4232-98e4-89e456d8551b"), event_id=4485, version=0)
class Microsoft_Windows_RTWorkQueue_Threading_4485_0(Etw):
    pattern = Struct(
        "WorkQueueID" / Int32ul,
        "Yield" / Int32ul
    )


@declare(guid=guid("e18d0fc9-9515-4232-98e4-89e456d8551b"), event_id=4486, version=0)
class Microsoft_Windows_RTWorkQueue_Threading_4486_0(Etw):
    pattern = Struct(
        "WorkQueuePointer" / Int64ul,
        "WorkQueueID" / Int32ul,
        "TotalCount" / Int32ul,
        "ImmediateCount" / Int32ul,
        "NextDeadline" / Int64sl,
        "ItemPointer" / Int64ul
    )


@declare(guid=guid("e18d0fc9-9515-4232-98e4-89e456d8551b"), event_id=4487, version=0)
class Microsoft_Windows_RTWorkQueue_Threading_4487_0(Etw):
    pattern = Struct(
        "WorkQueueID" / Int32ul,
        "TaskGroupID" / Int32ul
    )


@declare(guid=guid("e18d0fc9-9515-4232-98e4-89e456d8551b"), event_id=4488, version=0)
class Microsoft_Windows_RTWorkQueue_Threading_4488_0(Etw):
    pattern = Struct(
        "WorkQueueID" / Int32ul,
        "TaskGroupID" / Int32ul
    )


@declare(guid=guid("e18d0fc9-9515-4232-98e4-89e456d8551b"), event_id=4489, version=0)
class Microsoft_Windows_RTWorkQueue_Threading_4489_0(Etw):
    pattern = Struct(
        "WorkQueuePointer" / Int64ul,
        "WorkQueueID" / Int32ul,
        "TimerPointer" / Int64ul,
        "Timeout" / Int64sl,
        "IsPeriodic" / Int8ul
    )


@declare(guid=guid("e18d0fc9-9515-4232-98e4-89e456d8551b"), event_id=4490, version=0)
class Microsoft_Windows_RTWorkQueue_Threading_4490_0(Etw):
    pattern = Struct(
        "WorkQueuePointer" / Int64ul,
        "WorkQueueID" / Int32ul,
        "TimerPointer" / Int64ul,
        "IsPeriodic" / Int8ul
    )


@declare(guid=guid("e18d0fc9-9515-4232-98e4-89e456d8551b"), event_id=4493, version=0)
class Microsoft_Windows_RTWorkQueue_Threading_4493_0(Etw):
    pattern = Struct(
        "ProcessorGroup" / Int64ul,
        "ProcessorMask" / Int64ul
    )


@declare(guid=guid("e18d0fc9-9515-4232-98e4-89e456d8551b"), event_id=4494, version=0)
class Microsoft_Windows_RTWorkQueue_Threading_4494_0(Etw):
    pattern = Struct(
        "ProcessorGroup" / Int64ul,
        "ProcessorMask" / Int64ul,
        "hResult" / Int32ul
    )


@declare(guid=guid("e18d0fc9-9515-4232-98e4-89e456d8551b"), event_id=4495, version=0)
class Microsoft_Windows_RTWorkQueue_Threading_4495_0(Etw):
    pattern = Struct(
        "queryStatus" / Int32ul,
        "subscribeStatus" / Int32ul,
        "changeStamp" / Int32ul
    )


@declare(guid=guid("e18d0fc9-9515-4232-98e4-89e456d8551b"), event_id=4496, version=0)
class Microsoft_Windows_RTWorkQueue_Threading_4496_0(Etw):
    pattern = Struct(
        "dwWorkQueue" / Int32ul,
        "Class" / WString,
        "ProcessorGroup" / Int64ul,
        "ProcessorMask" / Int64ul
    )


@declare(guid=guid("e18d0fc9-9515-4232-98e4-89e456d8551b"), event_id=4497, version=0)
class Microsoft_Windows_RTWorkQueue_Threading_4497_0(Etw):
    pattern = Struct(
        "ChangeStamp" / Int32ul,
        "CurChangeStamp" / Int32ul,
        "ProcessorGroup" / Int64ul,
        "ProcessorMask" / Int64ul,
        "Length" / Int32ul
    )


@declare(guid=guid("e18d0fc9-9515-4232-98e4-89e456d8551b"), event_id=4498, version=0)
class Microsoft_Windows_RTWorkQueue_Threading_4498_0(Etw):
    pattern = Struct(
        "pWorkQueue" / Int64ul,
        "Class" / WString,
        "Priority" / Int32sl,
        "ThreadId" / Int32sl,
        "CurProcessorGroup" / Int64ul,
        "CurProcessorMask" / Int64ul,
        "NewProcessorGroup" / Int64ul,
        "NewProcessorMask" / Int64ul,
        "Status" / Int32sl
    )


@declare(guid=guid("e18d0fc9-9515-4232-98e4-89e456d8551b"), event_id=4499, version=0)
class Microsoft_Windows_RTWorkQueue_Threading_4499_0(Etw):
    pattern = Struct(
        "WorkQueuePointer" / Int64ul,
        "WorkQueueID" / Int32sl
    )


@declare(guid=guid("e18d0fc9-9515-4232-98e4-89e456d8551b"), event_id=4500, version=0)
class Microsoft_Windows_RTWorkQueue_Threading_4500_0(Etw):
    pattern = Struct(
        "WorkQueuePointer" / Int64ul,
        "WorkQueueID" / Int32sl
    )


@declare(guid=guid("e18d0fc9-9515-4232-98e4-89e456d8551b"), event_id=4501, version=0)
class Microsoft_Windows_RTWorkQueue_Threading_4501_0(Etw):
    pattern = Struct(
        "WorkQueuePointer" / Int64ul,
        "WorkQueueID" / Int32ul,
        "TaskGroup" / Int32ul
    )


@declare(guid=guid("e18d0fc9-9515-4232-98e4-89e456d8551b"), event_id=4502, version=0)
class Microsoft_Windows_RTWorkQueue_Threading_4502_0(Etw):
    pattern = Struct(
        "WorkQueuePointer" / Int64ul,
        "WorkQueueID" / Int32ul,
        "TaskGroup" / Int32ul
    )


@declare(guid=guid("e18d0fc9-9515-4232-98e4-89e456d8551b"), event_id=4503, version=0)
class Microsoft_Windows_RTWorkQueue_Threading_4503_0(Etw):
    pattern = Struct(
        "WorkQueuePointer" / Int64ul,
        "WorkQueueID" / Int32ul,
        "TaskGroup" / Int32ul
    )


@declare(guid=guid("e18d0fc9-9515-4232-98e4-89e456d8551b"), event_id=4504, version=0)
class Microsoft_Windows_RTWorkQueue_Threading_4504_0(Etw):
    pattern = Struct(
        "WorkQueuePointer" / Int64ul,
        "WorkQueueID" / Int32ul,
        "TaskGroup" / Int32ul
    )


@declare(guid=guid("e18d0fc9-9515-4232-98e4-89e456d8551b"), event_id=4505, version=0)
class Microsoft_Windows_RTWorkQueue_Threading_4505_0(Etw):
    pattern = Struct(
        "Platform" / Int64ul,
        "WorkQueueID" / Int32sl,
        "Index" / Int32sl
    )


@declare(guid=guid("e18d0fc9-9515-4232-98e4-89e456d8551b"), event_id=4506, version=0)
class Microsoft_Windows_RTWorkQueue_Threading_4506_0(Etw):
    pattern = Struct(
        "Platform" / Int64ul,
        "WorkQueueID" / Int32sl,
        "Index" / Int32sl
    )


@declare(guid=guid("e18d0fc9-9515-4232-98e4-89e456d8551b"), event_id=4507, version=0)
class Microsoft_Windows_RTWorkQueue_Threading_4507_0(Etw):
    pattern = Struct(
        "Platform" / Int64ul
    )


@declare(guid=guid("e18d0fc9-9515-4232-98e4-89e456d8551b"), event_id=4508, version=0)
class Microsoft_Windows_RTWorkQueue_Threading_4508_0(Etw):
    pattern = Struct(
        "Platform" / Int64ul
    )


@declare(guid=guid("e18d0fc9-9515-4232-98e4-89e456d8551b"), event_id=4509, version=0)
class Microsoft_Windows_RTWorkQueue_Threading_4509_0(Etw):
    pattern = Struct(
        "Platform" / Int64ul
    )


@declare(guid=guid("e18d0fc9-9515-4232-98e4-89e456d8551b"), event_id=4510, version=0)
class Microsoft_Windows_RTWorkQueue_Threading_4510_0(Etw):
    pattern = Struct(
        "Platform" / Int64ul
    )


@declare(guid=guid("e18d0fc9-9515-4232-98e4-89e456d8551b"), event_id=4511, version=0)
class Microsoft_Windows_RTWorkQueue_Threading_4511_0(Etw):
    pattern = Struct(
        "Platform" / Int64ul
    )


@declare(guid=guid("e18d0fc9-9515-4232-98e4-89e456d8551b"), event_id=4512, version=0)
class Microsoft_Windows_RTWorkQueue_Threading_4512_0(Etw):
    pattern = Struct(
        "Platform" / Int64ul,
        "WorkQueue" / Int32sl,
        "Index" / Int32sl
    )


@declare(guid=guid("e18d0fc9-9515-4232-98e4-89e456d8551b"), event_id=4513, version=0)
class Microsoft_Windows_RTWorkQueue_Threading_4513_0(Etw):
    pattern = Struct(
        "Platform" / Int64ul,
        "WorkQueue" / Int32sl,
        "Index" / Int32sl
    )


@declare(guid=guid("e18d0fc9-9515-4232-98e4-89e456d8551b"), event_id=4514, version=0)
class Microsoft_Windows_RTWorkQueue_Threading_4514_0(Etw):
    pattern = Struct(
        "WorkQueuePointer" / Int64ul,
        "WorkQueueID" / Int32ul,
        "TaskGroup" / Int32ul
    )


@declare(guid=guid("e18d0fc9-9515-4232-98e4-89e456d8551b"), event_id=4515, version=0)
class Microsoft_Windows_RTWorkQueue_Threading_4515_0(Etw):
    pattern = Struct(
        "WorkQueuePointer" / Int64ul,
        "WorkQueueID" / Int32ul,
        "TaskGroup" / Int32ul
    )


@declare(guid=guid("e18d0fc9-9515-4232-98e4-89e456d8551b"), event_id=4516, version=0)
class Microsoft_Windows_RTWorkQueue_Threading_4516_0(Etw):
    pattern = Struct(
        "WorkQueuePointer" / Int64ul,
        "WorkQueueID" / Int32ul,
        "TaskGroup" / Int32ul
    )


@declare(guid=guid("e18d0fc9-9515-4232-98e4-89e456d8551b"), event_id=4517, version=0)
class Microsoft_Windows_RTWorkQueue_Threading_4517_0(Etw):
    pattern = Struct(
        "TaskGroup" / Int64ul
    )


@declare(guid=guid("e18d0fc9-9515-4232-98e4-89e456d8551b"), event_id=4518, version=0)
class Microsoft_Windows_RTWorkQueue_Threading_4518_0(Etw):
    pattern = Struct(
        "TaskGroup" / Int64ul
    )


@declare(guid=guid("e18d0fc9-9515-4232-98e4-89e456d8551b"), event_id=4519, version=0)
class Microsoft_Windows_RTWorkQueue_Threading_4519_0(Etw):
    pattern = Struct(
        "TaskGroup" / Int64ul,
        "RefCount" / Int32ul
    )


@declare(guid=guid("e18d0fc9-9515-4232-98e4-89e456d8551b"), event_id=4520, version=0)
class Microsoft_Windows_RTWorkQueue_Threading_4520_0(Etw):
    pattern = Struct(
        "ObjectCount" / Int32ul
    )

