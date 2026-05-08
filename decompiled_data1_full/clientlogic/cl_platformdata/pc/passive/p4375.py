# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4375.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4375.pyc
# Source Generated with Decompyle++
# File: p4375.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, None, None)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.GetLiveMonsterPer(oWarrior, oEventCB) >= 7500:
        cl_evact.PassiveChangeAttr(oWarrior, oEventCB, 'HPMax', 0, 0)
        cl_action.CommonChangeBaseDamRatio(oWarrior, oEventCB.GetCBLifeCycle(), 0, 0, 0, 1)
        cl_evact.PassiveChangeAttr(oWarrior, oEventCB, 'MoveSpeed', 0, 1000)
    elif cl_evcon.GetLiveMonsterPer(oWarrior, oEventCB) >= 5500:
        cl_evact.PassiveChangeAttr(oWarrior, oEventCB, 'HPMax', 0, 2000)
        cl_action.CommonChangeBaseDamRatio(oWarrior, oEventCB.GetCBLifeCycle(), 0, 2000, 0, 1)
        cl_evact.PassiveChangeAttr(oWarrior, oEventCB, 'MoveSpeed', 0, 1000)
    elif cl_evcon.GetLiveMonsterPer(oWarrior, oEventCB) >= 3000:
        cl_evact.PassiveChangeAttr(oWarrior, oEventCB, 'HPMax', 0, 5000)
        cl_action.CommonChangeBaseDamRatio(oWarrior, oEventCB.GetCBLifeCycle(), 0, 4000, 0, 1)
        cl_evact.PassiveChangeAttr(oWarrior, oEventCB, 'MoveSpeed', 0, 2000)
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1213, 0, { }, 0, None, None)
    else:
        cl_evact.PassiveChangeAttr(oWarrior, oEventCB, 'HPMax', 0, 7000)
        cl_action.CommonChangeBaseDamRatio(oWarrior, oEventCB.GetCBLifeCycle(), 0, 6000, 0, 1)
        cl_evact.PassiveChangeAttr(oWarrior, oEventCB, 'MoveSpeed', 0, 3000)
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1233, 0, { }, 0, None, None)


class CPerform(CCustomPerform):
    m_SID = 4375
    m_Name = '少数精锐（轮回九）'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0

