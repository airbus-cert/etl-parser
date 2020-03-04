# -*- coding: utf-8 -*-
"""
Microsoft-Windows-EnergyEfficiencyWizard
GUID : 1a772f65-be1e-4fc6-96bb-248e03fa60f5
"""
from construct import Int8sl, Int8ul, Int16ul, Int16sl, Int32sl, Int32ul, Int64sl, Int64ul, Bytes, Double, Float32l, Struct
from etl.utils import WString, CString, SystemTime, Guid
from etl.dtyp import Sid
from etl.parsers.etw.core import Etw, declare, guid


@declare(guid=guid("1a772f65-be1e-4fc6-96bb-248e03fa60f5"), event_id=1, version=0)
class Microsoft_Windows_EnergyEfficiencyWizard_1_0(Etw):
    pattern = Struct(
        "KernelFlags" / Int32ul
    )


@declare(guid=guid("1a772f65-be1e-4fc6-96bb-248e03fa60f5"), event_id=2, version=0)
class Microsoft_Windows_EnergyEfficiencyWizard_2_0(Etw):
    pattern = Struct(
        "ProviderGUID" / Guid,
        "Rundown" / Int32ul
    )

