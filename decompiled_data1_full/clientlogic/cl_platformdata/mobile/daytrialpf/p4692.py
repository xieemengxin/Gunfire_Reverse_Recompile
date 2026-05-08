# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/daytrialpf/p4692.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/daytrialpf/p4692.pyc
# Source Generated with Decompyle++
# File: p4692.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.daytrial import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1317, 0, { }, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK_END, -1, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 1317, cl_evact.PassiveCBGetSceneData(oWarrior, oEventCB, 'PF-4692Intensify'))


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveCBSetCollectInfo(oWarrior, oEventCB, 'p4692', 1, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'p4692', None) >= 1:
        cl_evact.PassiveCBSetCollectInfo(oWarrior, oEventCB, 'p4692', -1, 0)
    elif cl_condition.GetSceneData(oWarrior, oEventCB.GetCBLifeCycle(), 'PF-4692Intensify') <= 29:
        cl_evact.PassiveCBChangeSceneData(oWarrior, oEventCB, 'PF-4692Intensify', 1, 0)
        cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 1317, cl_evact.PassiveCBGetSceneData(oWarrior, oEventCB, 'PF-4692Intensify'))
        cl_evact.EventGetAllMonsterByTargetScene(oWarrior, oEventCB, 1, None, None)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1318, 0, { }, 0, 0, None)


class CPerform(CCustomPerform):
    m_SID = 4692
    m_Name = '玩家射击未命中会强化该区域怪物'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0

