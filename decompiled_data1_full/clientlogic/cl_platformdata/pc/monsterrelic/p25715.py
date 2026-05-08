# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterrelic/p25715.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterrelic/p25715.pyc
# Source Generated with Decompyle++
# File: p25715.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import DAM_MASK_ELEMENT, OBJ_ATTACK, QUALITY_TYPE_HIGH, WARRIOR_HERO
from cl_newformula import Func213

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GOTDEFINALDEBUFF, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckTargetAddState(oWarrior, oEventCB, 20026):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
        if cl_condition.RandomTrigger(oWarrior, oEventCB.GetCBLifeCycle(), 10, 5) and cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_HERO):
            cl_evact.PassiveAddTargetStateWithCache(oWarrior, oEventCB, 20026, (lambda *a: Func213(*a) * 100 / 100 + 0), {
                'AbnormalSourceDam': 2500 }, 1, DAM_MASK_ELEMENT, 0)
        else:
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
            if cl_condition.RandomTrigger(oWarrior, oEventCB.GetCBLifeCycle(), 10, 5) and cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_HERO):
                cl_evact.PassiveAddTargetStateWithCache(oWarrior, oEventCB, 0, 0, { }, 1, DAM_MASK_ELEMENT, 0)


class CPerform(CCustomPerform):
    m_SID = 25715
    m_Name = '元素奥能'
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
    m_RelicType = 0
    m_HeroRelic = 5715
    m_Quality = QUALITY_TYPE_HIGH
    m_ExcludeRelic = ()

