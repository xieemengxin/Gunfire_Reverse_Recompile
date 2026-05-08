# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_achievement/pc/s1092.pyc
# RelativePath: clientlogic/cl_achievement/pc/s1092.pyc
# Source Generated with Decompyle++
# File: s1092.pyc (Python 3.6)

from cl_object.logging import CheekLog
from cl_commondefines import ATTACKERSUBMSG_NORMAL, EQUIP_SNIPER, EQUIP_TYPE_FUNDAMENTALWEAPON, OBJ_VICTIM, PLAYMODE_ROGUELIKE, PLAY_TYPE_SINGLE
from cl_newformula import Func205
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from ..mobject import CAchieveStat as CCustom

def EnableAction(oListener, oLifeCycle):
    if cl_condition.CheckHero(oListener, oLifeCycle, 207) and cl_condition.CheckWarPlayMode(oListener, oLifeCycle, PLAYMODE_ROGUELIKE) and cl_condition.CheckWarPlayType(oListener, oLifeCycle, PLAY_TYPE_SINGLE) and cl_condition.CalFormula(oListener, oLifeCycle, (lambda *a: Func205(*a))) >= 3:
        cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
        cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 2, 0, 0)
        cl_action.CommonDirectEventCBFunc(oListener, oLifeCycle, 0, None, None)


def DoCallBackAction0(oEventCB, oListener):
    if not cl_evcon.AchieveCBCheckWarStat(oListener, oEventCB, 1):
        cl_evact.AchieveCBAddState(oListener, oEventCB, 1477, 0, { }, None)


def DoCallBackAction1(oEventCB, oListener):
    if cl_evcon.CheckFromWeapon(oListener, oEventCB, 0):
        if not cl_evcon.CheckEventWeaponType(oListener, oEventCB, EQUIP_SNIPER) or cl_evcon.CheckEventWeaponType(oListener, oEventCB, EQUIP_TYPE_FUNDAMENTALWEAPON):
            cl_action.CommonRemoveOwnerState(oListener, oEventCB.GetCBLifeCycle(), 1477, 0)
            cl_evact.AchieveCBAddWarStat(oListener, oEventCB, 1)
            cl_action.CommonDoneEvent(oListener, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL)
            cl_action.CommonDoneEvent(oListener, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL)
            CustomCBAction(oListener, oEventCB, { })


def DoCallBackAction2(oEventCB, oListener):
    cl_evact.EventGetTargetByType(oListener, oEventCB, OBJ_VICTIM)
    if (cl_evcon.CheckTargetPointBaseMonster(oListener, oEventCB, 3924) or cl_evcon.CheckTargetPointBaseMonster(oListener, oEventCB, 3925) or cl_evcon.CheckTargetPointBaseMonster(oListener, oEventCB, 3902) or cl_evcon.CheckTargetPointBaseMonster(oListener, oEventCB, 3904)) and not cl_evcon.AchieveCBCheckWarStat(oListener, oEventCB, 1):
        cl_evact.AchieveCBAddStat(oListener, oEventCB, 1)
        cl_evact.AchieveRewardCheek(oListener, oEventCB, 1007)


def DoCallBackAction3(oEventCB, oListener):
    if not cl_evcon.CheckEventWeaponType(oListener, oEventCB, EQUIP_SNIPER) or cl_evcon.CheckEventWeaponType(oListener, oEventCB, EQUIP_TYPE_FUNDAMENTALWEAPON):
        cl_action.CommonRemoveOwnerState(oListener, oEventCB.GetCBLifeCycle(), 1477, 0)
        cl_evact.AchieveCBAddWarStat(oListener, oEventCB, 1)
        cl_action.CommonDoneEvent(oListener, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL)
        cl_action.CommonDoneEvent(oListener, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL)
        CustomCBAction(oListener, oEventCB, { })


class CAchieveStat(CCustom):
    m_SID = 1092
    m_Name = '虎啸雷吟'
    m_TargetValue = 1
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3 }


def CustomCBAction(oListener, oEventCB, dInfo):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iWeapon = 0
    iWeaponSID = 0
    if 'Skill' in dMsgInfo:
        oSkill = dMsgInfo['Skill']
        iWeapon = oSkill.m_Cache['ItemID'] if 'ItemID' in oSkill.m_Cache else 0
    elif 'ItemID' in dMsgInfo:
        iWeapon = dMsgInfo['ItemID']
    oWeapon = oListener.m_WieldCon.GetItemByID(iWeapon)
    if oWeapon:
        iWeaponSID = oWeapon.m_SID
    CheekLog.Info(f'''achievement1092 fail weaponSID:{iWeaponSID}''')

