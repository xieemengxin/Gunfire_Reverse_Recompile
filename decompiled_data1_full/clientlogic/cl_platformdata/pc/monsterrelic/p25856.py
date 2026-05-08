# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterrelic/p25856.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterrelic/p25856.pyc
# Source Generated with Decompyle++
# File: p25856.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import DAM_TYPE_PERFORM, DAM_TYPE_TRUE, DAM_USE_ALL, OBJ_SELF, QUALITY_TYPE_NORMAL, WARRIOR_HERO
from cl_newformula import Func374

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DIE, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 25):
        cl_evact.EventGetRangeTargetByFightType(oWarrior, oEventCB, 5, WARRIOR_HERO, 1, 0, 0, 0, 0, { }, -1, None, None, None, None)
        cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: Func374(*a) * 2 // 10), DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 0, 0, 0, 0, 0, 0, 0, None, None, None)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventClientBehavior(oWarrior, oEventCB, 25856, 0)


class CPerform(CCustomPerform):
    m_SID = 25856
    m_Name = '涅槃之力'
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
    m_HeroRelic = 5856
    m_Quality = QUALITY_TYPE_NORMAL
    m_ExcludeRelic = ()

