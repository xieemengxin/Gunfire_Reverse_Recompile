# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_achievement/pc/s1032.pyc
# RelativePath: clientlogic/cl_achievement/pc/s1032.pyc
# Source Generated with Decompyle++
# File: s1032.pyc (Python 3.6)

from cl_commondefines import COST_BAGBULLET_WEAPON
from cl_newformula import Func208, Func215
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from ..mobject import CAchieveStat as CCustom

def EnableAction(oListener, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBULLET, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBAGBULLET, COST_BAGBULLET_WEAPON, 1, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    cl_evact.AchieveCBAddStat(oListener, oEventCB, (lambda *a: Func208(*a) * 100 / 100 + 0))


def DoCallBackAction1(oEventCB, oListener):
    cl_evact.AchieveCBAddStat(oListener, oEventCB, (lambda *a: Func215(*a) * 100 / 100))


class CAchieveStat(CCustom):
    m_SID = 1032
    m_Name = '战争之王'
    m_TargetValue = 100000
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }

