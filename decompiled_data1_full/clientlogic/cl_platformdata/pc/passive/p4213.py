# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4213.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4213.pyc
# Source Generated with Decompyle++
# File: p4213.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_TRUE, DAM_TYPE_WEAPON, DAM_USE_ALL, OBJ_VICTIM, WARRIOR_BOSS, WARRIOR_ELITE, WARRIOR_NORMAL
from cl_newformula import Func302

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 1, 0, 0)
    cl_action.PassiveEnableBulletChangeRule(oWarrior, oLifeCycle, 11107, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 2, 0, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_condition.GetWeaponBulletCnt(oWarrior, oEventCB.GetCBLifeCycle()) > 0 and cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 9694, 0, None):
        cl_evact.EventChangeSkillCache(oWarrior, oEventCB, 'Att', 0, 6000)
        cl_evact.EventChangeSkillCache(oWarrior, oEventCB, 'DebuffProb', 7000, 0)
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 9697, 1, None):
        cl_evact.EventChangeSkillCache(oWarrior, oEventCB, 'DebuffProb', 7000, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 9697, 1, None) and cl_evcon.CheckVictimFightType(oWarrior, oEventCB, WARRIOR_NORMAL):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: (Func302(*a, **{
'sAttr': 'HP' }) + Func302(*a, **{
'sAttr': 'Armor' }) + Func302(*a, **{
'sAttr': 'Shield' })) * 25 / 100), DAM_TYPE_WEAPON | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 0, 0, 0, None, None, None, None, None, None, None)
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 9697, 1, None) and cl_evcon.CheckVictimFightType(oWarrior, oEventCB, WARRIOR_ELITE):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: (Func302(*a, **{
'sAttr': 'HP' }) + Func302(*a, **{
'sAttr': 'Armor' }) + Func302(*a, **{
'sAttr': 'Shield' })) * 12 / 100), DAM_TYPE_WEAPON | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 0, 0, 0, None, None, None, None, None, None, None)
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 9697, 1, None) and cl_evcon.CheckVictimFightType(oWarrior, oEventCB, WARRIOR_BOSS):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: (Func302(*a, **{
'sAttr': 'HP' }) + Func302(*a, **{
'sAttr': 'Armor' }) + Func302(*a, **{
'sAttr': 'Shield' })) * 5 / 100), DAM_TYPE_WEAPON | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 0, 0, 0, None, None, None, None, None, None, None)


class CPerform(CCustomPerform):
    m_SID = 4213
    m_Name = '鸩鬼右键技能'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0

