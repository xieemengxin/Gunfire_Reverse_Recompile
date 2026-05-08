# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_achievement/pc/s1094.pyc
# RelativePath: clientlogic/cl_achievement/pc/s1094.pyc
# Source Generated with Decompyle++
# File: s1094.pyc (Python 3.6)

from cl_commondefines import PF_SUBMSG_THROW, PF_TYPE_THROW, PLAYMODE_ROGUELIKE
from cl_newformula import Func410
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from ..mobject import CAchieveStat as CCustom

def EnableAction(oListener, oLifeCycle):
    if cl_condition.CheckHero(oListener, oLifeCycle, 213) and cl_condition.CheckWarPlayMode(oListener, oLifeCycle, PLAYMODE_ROGUELIKE):
        cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_THROW, 0, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    if cl_evcon.CheckPerformType(oListener, oEventCB, PF_TYPE_THROW, None) and cl_evcon.GetFormula(oListener, oEventCB, (lambda *a: Func410(*a, **{
'sid': 32775 }))) >= 80:
        cl_evact.AchieveCBAddStat(oListener, oEventCB, 1)
        cl_evact.AchieveRewardCheek(oListener, oEventCB, 1009)


class CAchieveStat(CCustom):
    m_SID = 1094
    m_Name = '碧波万顷'
    m_TargetValue = 1
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0 }

