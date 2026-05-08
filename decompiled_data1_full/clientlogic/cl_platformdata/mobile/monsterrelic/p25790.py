# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterrelic/p25790.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterrelic/p25790.pyc
# Source Generated with Decompyle++
# File: p25790.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, CURE_TYPE_PERFORM, DAM_TYPE_PERFORM, DAM_TYPE_TRUE, DAM_TYPE_WEAPON, DAM_USE_ALL, OBJ_ATTACK, OBJ_SELF, QUALITY_TYPE_NORMAL, WARRIOR_ELITE
from cl_newformula import Func304, Func374

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if not cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
        if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_ELITE):
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
            if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1662, 0, 0) == 0 and cl_condition.RandomTrigger(oWarrior, oEventCB.GetCBLifeCycle(), 10, 5):
                cl_evact.EventTargetCure(oWarrior, oEventCB, (lambda *a: (Func304(*a, **{
'sAttr': 'HPMax' }) + Func304(*a, **{
'sAttr': 'ArmorMax' }) + Func304(*a, **{
'sAttr': 'ShieldMax' })) * 2 / 100), CURE_TYPE_PERFORM | DAM_USE_ALL, 0, -1, None)
                cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1717, 100, { }, -1, -1, None)
            else:
                cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: Func374(*a) * 2 / 100), DAM_TYPE_WEAPON | DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 0, 0, 0, 0, 0, -1, 0, 0, None, None, None)
                if cl_evcon.CheckDeadlyPredictDam(oWarrior, oEventCB, None):
                    cl_evact.EventChangeHP(oWarrior, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'HPMax' }) * 0 / 100 + 1))
                else:
                    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
                    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1662, 0, 0) == 0 and cl_condition.RandomTrigger(oWarrior, oEventCB.GetCBLifeCycle(), 10, 5):
                        cl_evact.EventTargetCure(oWarrior, oEventCB, (lambda *a: (Func304(*a, **{
'sAttr': 'HPMax' }) + Func304(*a, **{
'sAttr': 'ArmorMax' }) + Func304(*a, **{
'sAttr': 'ShieldMax' })) * 10 / 100), CURE_TYPE_PERFORM | DAM_USE_ALL, 0, -1, None)
                        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1717, 100, { }, -1, -1, None)
                    else:
                        cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: Func374(*a) * 10 / 100), DAM_TYPE_WEAPON | DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 0, 0, 0, 0, 0, -1, 0, 0, None, None, None)
                        if cl_evcon.CheckDeadlyPredictDam(oWarrior, oEventCB, None):
                            cl_evact.EventChangeHP(oWarrior, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'HPMax' }) * 0 / 100 + 1))
        None.PassiveCBSetLiteCD(oWarrior, oEventCB, 100)


class CPerform(CCustomPerform):
    m_SID = 25790
    m_Name = '事功各半'
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
    m_HeroRelic = 5790
    m_Quality = QUALITY_TYPE_NORMAL
    m_ExcludeRelic = ()

