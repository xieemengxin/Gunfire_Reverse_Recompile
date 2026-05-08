# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_signal/s1208.pyc
# RelativePath: clientlogic/cl_signal/s1208.pyc
# Source Generated with Decompyle++
# File: s1208.pyc (Python 3.6)

from __future__ import absolute_import
from cl_commondefines import SIGNAL_TYPE_NPC
from cl_signal.mobject import CNpcObjSignal as CCustom

class CSignal(CCustom):
    m_SID = 1208
    m_Name = '三选一宝箱'
    m_Type = SIGNAL_TYPE_NPC
    m_Notify = {
        'Weight': {
            1: 10,
            2: 10 },
        'Info': {
            1: {
                131: 2285,
                132: 9151,
                133: 9176,
                134: 9201 },
            2: {
                131: 2286,
                132: 9152,
                133: 9177,
                134: 9202 } } }

