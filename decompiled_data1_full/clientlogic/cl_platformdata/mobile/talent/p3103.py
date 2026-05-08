# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p3103.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p3103.pyc
# Source Generated with Decompyle++
# File: p3103.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_VICTIM, PF_TYPE_THROW, WARRIOR_MONSTER
from cl_newformula import Func336

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'pf3103', None) == 0:
        cl_evact.EventCBAddCollectInfo(oWarrior, oEventCB, 'pf3103', 1, None)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_THROW, None) and cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 20026, 0, 0, None) and cl_evcon.CheckRandom(oWarrior, oEventCB, (lambda *a: 2 ** Func336(*a, **{
'sKey': 'StartTimes' }) * 150), 90) and cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func336(*a, **{
'sKey': 'StartTimes' }))) <= 5:
            cl_evact.EventTargetGetRangeTargetByFightType(oWarrior, oEventCB, 7, WARRIOR_MONSTER, 0, 0, 1, 0, 0, None, None)
            if cl_evcon.GetThisTargetNum(oWarrior, oEventCB) != 0:
                cl_evact.EventCBUsePerformEvtTarget(oWarrior, oEventCB, 8007, {
                    'StartTimes': (lambda *a: Func336(*a, **{
'sKey': 'StartTimes' })),
                    'TransDamFactor': cl_evact.EventCBGetPFTransDamFactor(oWarrior, oEventCB) }, None)


class CPerform(CCustomPerform):
    m_SID = 3103
    m_Name = '火雨流星'
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
    m_MaxUpgradeTimes = 0
    m_TalentType = 2
    m_IsRareTalent = 0
    m_Career = 112

