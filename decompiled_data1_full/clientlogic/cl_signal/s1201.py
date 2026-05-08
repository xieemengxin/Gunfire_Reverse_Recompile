# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_signal/s1201.pyc
# RelativePath: clientlogic/cl_signal/s1201.pyc
# Source Generated with Decompyle++
# File: s1201.pyc (Python 3.6)

from __future__ import absolute_import
from cl_commondefines import SIGNAL_TYPE_NPC
from cl_signal.mobject import CNpcObjSignal as CCustom

class CSignal(CCustom):
    m_SID = 1201
    m_Name = '通关传送门'
    m_Type = SIGNAL_TYPE_NPC
    m_Notify = {
        'Weight': {
            1: 10,
            2: 10,
            3: 10 },
        'Info': {
            1: {
                131: 2238,
                132: 9131,
                133: 9156,
                134: 9181 },
            2: {
                131: 2281,
                132: 9147,
                133: 9172,
                134: 9197 },
            3: {
                131: 2282,
                132: 9148,
                133: 9173,
                134: 9198 } } }

