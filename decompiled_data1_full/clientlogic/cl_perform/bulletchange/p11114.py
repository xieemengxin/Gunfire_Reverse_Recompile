# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/bulletchange/p11114.pyc
# RelativePath: clientlogic/cl_perform/bulletchange/p11114.pyc
# Source Generated with Decompyle++
# File: p11114.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.bulletchange import CBulletChange as CCustomPerform
from . import action
from . import condition
from cl_commondefines import CURE_TYPE_PERFORM, DAM_USE_ARMOR, DAM_USE_HP, DAM_USE_SHIELD
from cl_newformula import Func304

def Action1(oWarrior, pfBulletChange):
    action.BulletChangeListenMsgCallBack(oWarrior, pfBulletChange, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 0, 0, 0)
    action.BulletChangeListenMsgCallBack(oWarrior, pfBulletChange, cl_msgcenter.MSG_WAR_COSTBULLET, -1, 1, 0, 0)
    action.BulletChangeDirectEventCBFunc(oWarrior, pfBulletChange, 0)


def DoCallBackAction0(oWarrior, pfBulletChange, oSkill, dClientInfo):
    action.BulletChangeWeaponInfiniteFire(oWarrior, pfBulletChange, oSkill, dClientInfo)


def DoCallBackAction1(oWarrior, pfBulletChange, oSkill, dClientInfo):
    if condition.CheckWeaponBulletCnt(oWarrior, pfBulletChange, oSkill, dClientInfo, 0):
        if condition.CheckBulletConsume(oWarrior, pfBulletChange, oSkill, dClientInfo) and condition.CheckPerformTriggerType(oWarrior, pfBulletChange, oSkill, dClientInfo):
            action.BulletChangeReduceBulletUse(oWarrior, pfBulletChange, oSkill, dClientInfo, 0)
        action.BulletChangeCBOwnerCure(oWarrior, pfBulletChange, oSkill, dClientInfo, (lambda *a: Func304(*a, **{
'sAttr': 'HPMax' }) * 1 / 100 + 0), CURE_TYPE_PERFORM | DAM_USE_HP, 0)
        action.BulletChangeCBOwnerCure(oWarrior, pfBulletChange, oSkill, dClientInfo, (lambda *a: (Func304(*a, **{
'sAttr': 'ArmorMax' }) + Func304(*a, **{
'sAttr': 'ShieldMax' })) * 1 / 100 + 0), CURE_TYPE_PERFORM | DAM_USE_SHIELD | DAM_USE_ARMOR, 0)


def DoCallBackAction2(oWarrior, pfBulletChange, oSkill, dClientInfo):
    if condition.CheckPerformTriggerType(oWarrior, pfBulletChange, oSkill, dClientInfo):
        action.BulletChangeReduceBulletUse(oWarrior, pfBulletChange, oSkill, dClientInfo, 0)


def DoCallBackAction3(oWarrior, pfBulletChange, oSkill, dClientInfo):
    if condition.CheckBulletConsume(oWarrior, pfBulletChange, oSkill, dClientInfo) and condition.CheckPerformTriggerType(oWarrior, pfBulletChange, oSkill, dClientInfo):
        action.BulletChangeReduceBulletUse(oWarrior, pfBulletChange, oSkill, dClientInfo, 0)


class CPerform(CCustomPerform):
    m_SID = 11114
    m_Name = '套装15010子弹效果'
    m_MaxLevel = 1
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3 }

