# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_signal/s1225.pyc
# RelativePath: clientlogic/cl_signal/s1225.pyc
# Source Generated with Decompyle++
# File: s1225.pyc (Python 3.6)

from __future__ import absolute_import
from cl_commondefines import SIGNAL_TYPE_NPC
from cl_signal.mobject import CNpcObjSignal as CCustom

class CSignal(CCustom):
    m_SID = 1225
    m_Name = '抽奖商人'
    m_Type = SIGNAL_TYPE_NPC
    m_Notify = {
        'Weight': {
            1: 10,
            2: 10,
            3: 10 },
        'Info': {
            1: {
                131: 9630,
                132: 9631,
                133: 9632,
                134: 9633 },
            2: {
                131: 9634,
                132: 9636,
                133: 9638,
                134: 9640 },
            3: {
                131: 9635,
                132: 9637,
                133: 9639,
                134: 9641 } } }

