# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_achievement/pc/s1104.pyc
# RelativePath: clientlogic/cl_achievement/pc/s1104.pyc
# Source Generated with Decompyle++
# File: s1104.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from ..mobject import CAchieveStat as CCustom

def EnableAction(oListener, oLifeCycle):
    if cl_condition.CheckOpenElement(oListener, oLifeCycle, {
        'EndlessElement': 1 }):
        cl_action.CommonListenWarMgrMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WARMGR_STARTENDLESS, -1, 0)


def DoCallBackAction0(oEventCB, oListener):
    cl_evact.AchieveCBAddStat(oListener, oEventCB, 1)


class CAchieveStat(CCustom):
    m_SID = 1104
    m_Name = '无尽旅途'
    m_TargetValue = 1
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0 }

