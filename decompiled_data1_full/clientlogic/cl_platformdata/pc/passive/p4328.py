# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4328.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4328.pyc
# Source Generated with Decompyle++
# File: p4328.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_platformdata.custom.passive.customaction import CustomActionUsePerform1714 as CustomAction
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_NORMAL, DAM_TYPE_WEAPON, DAM_USE_ALL, MONSTER_PART_SHIELD, OBJ_VICTIM
from cl_newformula import Func509

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckDamageIsSourceWeapon(oWarrior, oEventCB) and cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 9195, 1, 0) and not cl_evcon.CheckHitPart(oWarrior, oEventCB, MONSTER_PART_SHIELD):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 1624, 0, 1, None):
            cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 1624, 1, 1, 0, None)
            if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), cl_evcon.GetTargetStateCount(oWarrior, oEventCB, 1624, 1, 0) // 3) > 0:
                cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: 5 * Func509(*a, **{
'sAttr': 'Att' })), DAM_TYPE_WEAPON | DAM_TYPE_NORMAL | DAM_USE_ALL, 1, 0, 0, 0, 0, 0, 0, 0, None, None, None)
                CustomAction(oWarrior, oEventCB, {
                    'perform': 12011,
                    'state': 1624,
                    'count': 3 })
                cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 1624, -((cl_evact.EventCBGetTargetStateCount(oWarrior, oEventCB, 1624, 1) // 3) * 3), 1)
            else:
                cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1624, 0, { }, 0, 0, None)
                cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 1624, 1, 1)
                if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), cl_evcon.GetTargetStateCount(oWarrior, oEventCB, 1624, 1, 0) // 3) > 0:
                    cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: 5 * Func509(*a, **{
'sAttr': 'Att' })), DAM_TYPE_WEAPON | DAM_TYPE_NORMAL | DAM_USE_ALL, 1, 0, 0, 0, 0, 0, 0, 0, None, None, None)
                    CustomAction(oWarrior, oEventCB, {
                        'perform': 12011,
                        'state': 1624,
                        'count': 3 })
                    cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 1624, -((cl_evact.EventCBGetTargetStateCount(oWarrior, oEventCB, 1624, 1) // 3) * 3), 1)


class CPerform(CCustomPerform):
    m_SID = 4328
    m_Name = '无悔武器技能管理状态计数'
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

