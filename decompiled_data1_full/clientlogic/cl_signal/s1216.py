# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_signal/s1216.pyc
# RelativePath: clientlogic/cl_signal/s1216.pyc
# Source Generated with Decompyle++
# File: s1216.pyc (Python 3.6)

from __future__ import absolute_import
from cl_commondefines import SIGNAL_TYPE_DEFENDNPC
from cl_signal.mobject import CDefendNpcObjSignal as CCustom

class CSignal(CCustom):
    m_SID = 1216
    m_Name = '开启守护NPC'
    m_Type = SIGNAL_TYPE_DEFENDNPC
    m_Notify = {
        'Weight': {
            1: 10 },
        'Info': {
            1: {
                131: 9280,
                132: 9281,
                133: 9282,
                134: 9283 } } }

