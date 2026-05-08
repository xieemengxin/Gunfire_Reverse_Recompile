# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/benediction/p13544.pyc
# RelativePath: clientlogic/cl_platformdata/pc/benediction/p13544.pyc
# Source Generated with Decompyle++
# File: p13544.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform
from cl_newformula import Func560, Func561, Func563

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 1, 0, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func563(*a) - Func561(*a))) == 0 and cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        1424: 1,
        12008: 1 }, 1, 0) and cl_evcon.GetComb(oWarrior, oEventCB) >= 2:
        if cl_evcon.GetComb(oWarrior, oEventCB) == 2:
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32858, 700, { }, 1, -1, None)
            cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 32858, 8)
        elif cl_evcon.GetComb(oWarrior, oEventCB) == 3:
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32858, 700, { }, 1, -1, None)
            cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 32858, 16)
        elif cl_evcon.GetComb(oWarrior, oEventCB) >= 4:
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32858, 700, { }, 1, -1, None)
            cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 32858, 32)
        if cl_evcon.CheckRandom(oWarrior, oEventCB, 100, (lambda *a: Func560(*a))) == 0:
            cl_action.CommonClearAllGroove(oWarrior, oEventCB.GetCBLifeCycle(), 2)
            cl_evact.EventCBAddCollectInfo(oWarrior, oEventCB, 'ForbidAppendQuality', 1, None)


class CPerform(CCustomPerform):
    m_SID = 13544
    m_Name = '爆裂手牌'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Career = 113

