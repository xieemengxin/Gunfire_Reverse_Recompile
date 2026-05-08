# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_achievement/pc/s1221.pyc
# RelativePath: clientlogic/cl_achievement/pc/s1221.pyc
# Source Generated with Decompyle++
# File: s1221.pyc (Python 3.6)

from cl_commondefines import INKVALUE_ADD
from cl_newformula import Func638
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from ..mobject import CAchieveStat as CCustom

def EnableAction(oListener, oLifeCycle):
    if cl_condition.CheckHero(oListener, oLifeCycle, 219):
        cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_INKVALUE, INKVALUE_ADD, 0, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    if cl_condition.CalFormula(oListener, oEventCB.GetCBLifeCycle(), (lambda *a: Func638(*a))) >= 180:
        cl_evact.AchieveRewardCheek(oListener, oEventCB, 1019)
        cl_evact.AchieveCBAddStat(oListener, oEventCB, 1)


class CAchieveStat(CCustom):
    m_SID = 1221
    m_Name = '含蓄藏锋'
    m_TargetValue = 1
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0 }

