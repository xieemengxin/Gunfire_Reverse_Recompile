# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p5001.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p5001.pyc
# Source Generated with Decompyle++
# File: p5001.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, EQUIP_ROCKET_LAUNCHER, OBJ_VICTIM
from cl_newformula import Func343, Func360

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckWeaponType(oWarrior, oEventCB, EQUIP_ROCKET_LAUNCHER) and cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 60):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.EventCBUsePerformEvtTarget(oWarrior, oEventCB, 8008, {
            'DamTimes': (lambda *a: Func343(*a, **{
'sid': 4508 })),
            'DamAtt': (lambda *a: Func360(*a, **{
'sid': 1409,
'sAttr': 'Att' })) }, None)


class CPerform(CCustomPerform):
    m_SID = 5001
    m_Name = '爆炸余波'
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
    m_TalentType = 3
    m_IsRareTalent = 1
    m_Career = 101

