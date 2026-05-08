# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p5007.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p5007.pyc
# Source Generated with Decompyle++
# File: p5007.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import EQUIP_HANDGUN, EQUIP_LASER, EQUIP_RIFLE, EQUIP_ROCKET_LAUNCHER, EQUIP_SHOTGUN, EQUIP_SMG, EQUIP_SNIPER, EQUIP_TYPE_CLOSEWEAPON, EQUIP_TYPE_FUNDAMENTALWEAPON, MAIN_HOLD, PF_SUBMSG_CAREERPF

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 0, 0, 0)
    cl_action.CommonChangeCareerPerformAttr(oWarrior, oLifeCycle, 'ColdTime', -3000, 0, None)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1304, 1, 0):
        if cl_evcon.CheckWeaponTypeByHoldType(oWarrior, oEventCB, MAIN_HOLD, EQUIP_HANDGUN) or cl_evcon.CheckWeaponTypeByHoldType(oWarrior, oEventCB, MAIN_HOLD, EQUIP_LASER) or cl_evcon.CheckWeaponTypeByHoldType(oWarrior, oEventCB, MAIN_HOLD, EQUIP_SMG) or cl_evcon.CheckWeaponTypeByHoldType(oWarrior, oEventCB, MAIN_HOLD, EQUIP_RIFLE) or cl_evcon.CheckWeaponTypeByHoldType(oWarrior, oEventCB, MAIN_HOLD, EQUIP_TYPE_FUNDAMENTALWEAPON):
            cl_evact.EventChangeSkillCache(oWarrior, oEventCB, 'Att', 0, 20000)
        elif cl_evcon.CheckWeaponTypeByHoldType(oWarrior, oEventCB, MAIN_HOLD, EQUIP_ROCKET_LAUNCHER) or cl_evcon.CheckWeaponTypeByHoldType(oWarrior, oEventCB, MAIN_HOLD, EQUIP_SHOTGUN) or cl_evcon.CheckWeaponTypeByHoldType(oWarrior, oEventCB, MAIN_HOLD, EQUIP_SNIPER) or cl_evcon.CheckWeaponTypeByHoldType(oWarrior, oEventCB, MAIN_HOLD, EQUIP_TYPE_CLOSEWEAPON):
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32933, 0, { }, -1, -1, None)


class CPerform(CCustomPerform):
    m_SID = 5007
    m_Name = '张弛有度'
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
    m_TalentType = 1
    m_IsRareTalent = 1
    m_Career = 103

