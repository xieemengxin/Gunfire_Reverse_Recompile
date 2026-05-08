# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_achievement/pc/s1224.pyc
# RelativePath: clientlogic/cl_achievement/pc/s1224.pyc
# Source Generated with Decompyle++
# File: s1224.pyc (Python 3.6)

from cl_newformula import Func651
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from ..mobject import CAchieveStat as CCustom

def EnableAction(oListener, oLifeCycle):
    if cl_condition.CheckHero(oListener, oLifeCycle, 220):
        cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    if cl_evcon.CheckTargetAddState(oListener, oEventCB, 8153):
        cl_evact.AchieveCBAddStat(oListener, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'Time' }) // 100))


class CAchieveStat(CCustom):
    m_SID = 1224
    m_Name = '凌云驻影'
    m_TargetValue = 500
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0 }

