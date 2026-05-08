# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4291.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4291.pyc
# Source Generated with Decompyle++
# File: p4291.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_WEAKNESS, DAM_TYPE_WEAPON, EQUIP_HANDGUN, EQUIP_SNIPER, EQUIP_TYPE_AMULET, EQUIP_TYPE_FUNDAMENTALWEAPON, OBJ_ATTACK, OBJ_VICTIM, PF_SUBMSG_CAREERPF, PF_TYPE_CAREERPF, SKILLCACHE_LSTINT
from cl_newformula import Func336, Func360

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32666, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 2, 0, 12)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_CAREERPF, 4, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33639, 0, { }, 1)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1520, 0, { }, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_CAREERPF, None) and cl_evcon.EventCBCheckWeaponTypeInCache(oWarrior, oEventCB, EQUIP_SNIPER, SKILLCACHE_LSTINT):
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 32666, 40, None)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_CAREERPF, None):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if cl_evcon.CheckHasState(oWarrior, oEventCB, 32655):
            cl_evact.EventCBChangeLuckyHit(oWarrior, oEventCB, 80)
        if cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'Smash_IsCrazy', None):
            cl_evact.EventCBSetDamageType(oWarrior, oEventCB, DAM_TYPE_WEAKNESS)
        if cl_evcon.EventCBGetCurCrtData(oWarrior, oEventCB, 'launcher_mark'):
            cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_VICTIM, 0, 3000, DAM_TYPE_WEAPON, '')
        if (cl_evcon.EventCBCheckWeaponTypeInCache(oWarrior, oEventCB, EQUIP_HANDGUN, SKILLCACHE_LSTINT) or cl_evcon.EventCBCheckWeaponTypeInCache(oWarrior, oEventCB, EQUIP_TYPE_FUNDAMENTALWEAPON, SKILLCACHE_LSTINT) or cl_evcon.EventCBCheckWeaponTypeInCache(oWarrior, oEventCB, EQUIP_TYPE_AMULET, SKILLCACHE_LSTINT)) and cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'mengji_hitidx', None) != cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'p4291_handgun', None):
            cl_evact.EventCBClearCollectInfo(oWarrior, oEventCB, 'p4291_handgun', None)
            cl_evact.EventCBAddCollectInfo(oWarrior, oEventCB, 'p4291_handgun', (lambda *a: Func336(*a, **{
'sKey': 'mengji_hitidx' })), 0)
            cl_evact.EventCBUsePerformEvtTarget(oWarrior, oEventCB, 1709, {
                'PerformAtt': (lambda *a: Func360(*a, **{
'sid': 1422,
'sAttr': 'Att' }) * 2),
                'pfid': 1315,
                'TransDamFactor': cl_evact.EventCBGetPFTransDamFactor(oWarrior, oEventCB) }, None)
        if cl_evcon.EventCBCheckWeaponTypeInCache(oWarrior, oEventCB, EQUIP_SNIPER, SKILLCACHE_LSTINT) and cl_evcon.CheckHitWeakness(oWarrior, oEventCB, 0):
            cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, 6000, DAM_TYPE_WEAPON, '')


def DoCallBackAction4(oEventCB, oWarrior):
    cl_action.CommonSetStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 32666, 0, None)


class CPerform(CCustomPerform):
    m_SID = 4291
    m_Name = '噬魂剑客被动'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        2: DoCallBackAction2,
        4: DoCallBackAction4 }
    m_BaseArgData = { }
    m_DieDisable = 0

