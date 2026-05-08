# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterrelic/p25733.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterrelic/p25733.pyc
# Source Generated with Decompyle++
# File: p25733.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK, QUALITY_TYPE_HIGH, WARRIOR_ELITE, WARRIOR_HERO
from cl_newformula import Func304, Func305

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if not cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1):
        cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 100)
        if (cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func304(*a, **{
'sAttr': 'ShieldMax' }))) > 0 or cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func304(*a, **{
'sAttr': 'ArmorMax' }))) > 0) and cl_evcon.CheckVictimFightType(oWarrior, oEventCB, WARRIOR_HERO):
            if cl_condition.CheckTargetFightType(oWarrior, oEventCB.GetCBLifeCycle(), WARRIOR_ELITE):
                cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
                cl_evact.EventChangeArmor(oWarrior, oEventCB, (lambda *a: Func305(*a, **{
'sAttr': 'ArmorMax' }) * 0.6 / 100 + 0))
                cl_evact.EventChangeShield(oWarrior, oEventCB, (lambda *a: Func305(*a, **{
'sAttr': 'ShieldMax' }) * 0.6 / 100 + 0))
                cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1717, 100, { }, -1, -1, None)
            else:
                cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
                cl_evact.EventChangeArmor(oWarrior, oEventCB, (lambda *a: Func305(*a, **{
'sAttr': 'ArmorMax' }) * 3 / 100 + 0))
                cl_evact.EventChangeShield(oWarrior, oEventCB, (lambda *a: Func305(*a, **{
'sAttr': 'ShieldMax' }) * 3 / 100 + 0))
                cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1717, 100, { }, -1, -1, None)


class CPerform(CCustomPerform):
    m_SID = 25733
    m_Name = '金质徽章'
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
    m_HeroRelic = 5733
    m_Quality = QUALITY_TYPE_HIGH
    m_ExcludeRelic = ()

