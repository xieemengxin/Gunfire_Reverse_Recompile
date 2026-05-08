# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterrelic/p25803.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterrelic/p25803.pyc
# Source Generated with Decompyle++
# File: p25803.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_MASK_ELEMENT, OBJ_ATTACK, QUALITY_TYPE_LOW, WARRIOR_HERO
from cl_newformula import Func322

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1822, 0, { }, -1)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckVictimFightType(oWarrior, oEventCB, WARRIOR_HERO):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, (lambda *a: min(10000, int(7.4 * Func322(*a) ** 2 + 26 * Func322(*a) + 0))), 0, DAM_MASK_ELEMENT, '')


class CPerform(CCustomPerform):
    m_SID = 25803
    m_Name = '穿云神箭'
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
    m_HeroRelic = 5803
    m_Quality = QUALITY_TYPE_LOW
    m_ExcludeRelic = ()

