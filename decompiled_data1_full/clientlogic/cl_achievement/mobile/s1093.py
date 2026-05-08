# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_achievement/mobile/s1093.pyc
# RelativePath: clientlogic/cl_achievement/mobile/s1093.pyc
# Source Generated with Decompyle++
# File: s1093.pyc (Python 3.6)

from cl_commondefines import PF_SUBMSG_CAREERPF, PLAYMODE_ROGUELIKE
from cl_newformula import Func336
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from ..mobject import CAchieveStat as CCustom

def EnableAction(oListener, oLifeCycle):
    if cl_condition.CheckHero(oListener, oLifeCycle, 212) and cl_condition.CheckWarPlayMode(oListener, oLifeCycle, PLAYMODE_ROGUELIKE):
        cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_CAREERPF, 0, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    if cl_evcon.CheckFromPointPerform(oListener, oEventCB, 1312, 0, 0) and cl_evcon.GetFormula(oListener, oEventCB, (lambda *a: Func336(*a, **{
'sKey': 'TotalSwordNum' }))) >= 45:
        cl_evact.AchieveCBAddStat(oListener, oEventCB, 1)
        cl_evact.AchieveRewardCheek(oListener, oEventCB, 1008)


class CAchieveStat(CCustom):
    m_SID = 1093
    m_Name = '剑舞芳华'
    m_TargetValue = 1
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0 }

