# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/bulletchange/p11042.pyc
# RelativePath: clientlogic/cl_perform/bulletchange/p11042.pyc
# Source Generated with Decompyle++
# File: p11042.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.bulletchange import CBulletChange as CCustomPerform
from . import action
from . import condition
from cl_commondefines import DAM_TYPE_PERFORM, DAM_TYPE_TRUE, DAM_USE_ALL
from cl_newformula import Func305

def Action1(oWarrior, pfBulletChange):
    action.BulletChangeListenMsgCallBack(oWarrior, pfBulletChange, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 0, 0, 0)
    action.BulletChangeListenMsgCallBack(oWarrior, pfBulletChange, cl_msgcenter.MSG_WAR_COSTBULLET, -1, 1, 0, 0)
    action.BulletChangeDirectEventCBFunc(oWarrior, pfBulletChange, 0)


def Action2(oWarrior, pfBulletChange):
    action.BulletChangeListenMsgCallBack(oWarrior, pfBulletChange, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 0, 0, 0)
    action.BulletChangeListenMsgCallBack(oWarrior, pfBulletChange, cl_msgcenter.MSG_WAR_COSTBULLET, -1, 4, 0, 0)
    action.BulletChangeDirectEventCBFunc(oWarrior, pfBulletChange, 0)


def DoCallBackAction0(oWarrior, pfBulletChange, oSkill, dClientInfo):
    action.BulletChangeWeaponInfiniteFire(oWarrior, pfBulletChange, oSkill, dClientInfo)


def DoCallBackAction1(oWarrior, pfBulletChange, oSkill, dClientInfo):
    if condition.CheckWeaponBulletCnt(oWarrior, pfBulletChange, oSkill, dClientInfo, 0) and condition.CheckBulletConsume(oWarrior, pfBulletChange, oSkill, dClientInfo) and condition.CheckPerformTriggerType(oWarrior, pfBulletChange, oSkill, dClientInfo):
        action.BulletChangeReduceBulletUse(oWarrior, pfBulletChange, oSkill, dClientInfo, 0)
        if not condition.CheckOwnServerState(oWarrior, pfBulletChange, oSkill, dClientInfo, 32703):
            action.BulletChangeAddServerState(oWarrior, pfBulletChange, oSkill, dClientInfo, 32703, 300, 0, 0)
            action.BulletChangeCBOwnerClientBehavior(oWarrior, pfBulletChange, oSkill, dClientInfo, 1080, 0)
        action.BulletChangeCBOwnerDamage(oWarrior, pfBulletChange, oSkill, dClientInfo, (lambda *a: (Func305(*a, **{
'sAttr': 'HP' }) + Func305(*a, **{
'sAttr': 'Armor' }) + Func305(*a, **{
'sAttr': 'Shield' })) * 1 / 100 + 0), DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 0, 1, 0)


def DoCallBackAction2(oWarrior, pfBulletChange, oSkill, dClientInfo):
    if condition.CheckPerformTriggerType(oWarrior, pfBulletChange, oSkill, dClientInfo):
        action.BulletChangeReduceBulletUse(oWarrior, pfBulletChange, oSkill, dClientInfo, 0)
        if not condition.CheckOwnServerState(oWarrior, pfBulletChange, oSkill, dClientInfo, 32703):
            action.BulletChangeAddServerState(oWarrior, pfBulletChange, oSkill, dClientInfo, 32703, 300, 0, 0)
            action.BulletChangeCBOwnerClientBehavior(oWarrior, pfBulletChange, oSkill, dClientInfo, 1080, 0)
        action.BulletChangeCBOwnerDamage(oWarrior, pfBulletChange, oSkill, dClientInfo, (lambda *a: (Func305(*a, **{
'sAttr': 'HP' }) + Func305(*a, **{
'sAttr': 'Armor' }) + Func305(*a, **{
'sAttr': 'Shield' })) * 1 / 100 + 0), DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 0, 1, 0)


def DoCallBackAction3(oWarrior, pfBulletChange, oSkill, dClientInfo):
    if condition.CheckBulletConsume(oWarrior, pfBulletChange, oSkill, dClientInfo) and condition.CheckPerformTriggerType(oWarrior, pfBulletChange, oSkill, dClientInfo):
        action.BulletChangeReduceBulletUse(oWarrior, pfBulletChange, oSkill, dClientInfo, 0)
        if not condition.CheckOwnServerState(oWarrior, pfBulletChange, oSkill, dClientInfo, 32703):
            action.BulletChangeAddServerState(oWarrior, pfBulletChange, oSkill, dClientInfo, 32703, 300, 0, 0)
            action.BulletChangeCBOwnerClientBehavior(oWarrior, pfBulletChange, oSkill, dClientInfo, 1080, 0)
        action.BulletChangeCBOwnerDamage(oWarrior, pfBulletChange, oSkill, dClientInfo, (lambda *a: (Func305(*a, **{
'sAttr': 'HP' }) + Func305(*a, **{
'sAttr': 'Armor' }) + Func305(*a, **{
'sAttr': 'Shield' })) * 1 / 100 + 0), DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 0, 1, 0)


def DoCallBackAction4(oWarrior, pfBulletChange, oSkill, dClientInfo):
    if condition.CheckWeaponBulletCnt(oWarrior, pfBulletChange, oSkill, dClientInfo, 0) and condition.CheckBulletConsume(oWarrior, pfBulletChange, oSkill, dClientInfo) and condition.CheckPerformTriggerType(oWarrior, pfBulletChange, oSkill, dClientInfo):
        action.BulletChangeReduceBulletUse(oWarrior, pfBulletChange, oSkill, dClientInfo, 0)
        action.BulletChangeCBOwnerDamage(oWarrior, pfBulletChange, oSkill, dClientInfo, (lambda *a: (Func305(*a, **{
'sAttr': 'HP' }) + Func305(*a, **{
'sAttr': 'Armor' }) + Func305(*a, **{
'sAttr': 'Shield' })) * 1 / 100 + 0), DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 0, 1, 0)
        action.BulletChangeAddServerState(oWarrior, pfBulletChange, oSkill, dClientInfo, 1460, 500, 1, 0)
        action.BulletChangeAddServerStateCnt(oWarrior, pfBulletChange, oSkill, dClientInfo, 1460, 1, 0)
        action.BulletChangeCBOwnerClientBehavior(oWarrior, pfBulletChange, oSkill, dClientInfo, 1080, 1)


def DoCallBackAction5(oWarrior, pfBulletChange, oSkill, dClientInfo):
    if condition.CheckBulletConsume(oWarrior, pfBulletChange, oSkill, dClientInfo) and condition.CheckPerformTriggerType(oWarrior, pfBulletChange, oSkill, dClientInfo):
        action.BulletChangeReduceBulletUse(oWarrior, pfBulletChange, oSkill, dClientInfo, 0)
        action.BulletChangeCBOwnerDamage(oWarrior, pfBulletChange, oSkill, dClientInfo, (lambda *a: (Func305(*a, **{
'sAttr': 'HP' }) + Func305(*a, **{
'sAttr': 'Armor' }) + Func305(*a, **{
'sAttr': 'Shield' })) * 1 / 100 + 0), DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 0, 1, 0)
        action.BulletChangeAddServerState(oWarrior, pfBulletChange, oSkill, dClientInfo, 1460, 500, 1, 0)
        action.BulletChangeAddServerStateCnt(oWarrior, pfBulletChange, oSkill, dClientInfo, 1460, 1, 0)
        action.BulletChangeCBOwnerClientBehavior(oWarrior, pfBulletChange, oSkill, dClientInfo, 1080, 1)


def DoCallBackAction6(oWarrior, pfBulletChange, oSkill, dClientInfo):
    if condition.CheckPerformTriggerType(oWarrior, pfBulletChange, oSkill, dClientInfo):
        action.BulletChangeReduceBulletUse(oWarrior, pfBulletChange, oSkill, dClientInfo, 0)
        action.BulletChangeCBOwnerDamage(oWarrior, pfBulletChange, oSkill, dClientInfo, (lambda *a: (Func305(*a, **{
'sAttr': 'HP' }) + Func305(*a, **{
'sAttr': 'Armor' }) + Func305(*a, **{
'sAttr': 'Shield' })) * 1 / 100 + 0), DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 0, 1, 0)
        action.BulletChangeAddServerState(oWarrior, pfBulletChange, oSkill, dClientInfo, 1460, 500, 1, 0)
        action.BulletChangeAddServerStateCnt(oWarrior, pfBulletChange, oSkill, dClientInfo, 1460, 1, 0)
        action.BulletChangeCBOwnerClientBehavior(oWarrior, pfBulletChange, oSkill, dClientInfo, 1080, 1)


def DoCallBackAction7(oWarrior, pfBulletChange, oSkill, dClientInfo):
    if not condition.CheckOwnServerState(oWarrior, pfBulletChange, oSkill, dClientInfo, 32703):
        action.BulletChangeAddServerState(oWarrior, pfBulletChange, oSkill, dClientInfo, 32703, 300, 0, 0)
        action.BulletChangeCBOwnerClientBehavior(oWarrior, pfBulletChange, oSkill, dClientInfo, 1080, 0)


class CPerform(CCustomPerform):
    m_SID = 11042
    m_Name = '遗物5707子弹效果'
    m_MaxLevel = 2
    m_EnableActionInfo = {
        1: Action1,
        2: Action2 }
    m_DisableActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4,
        5: DoCallBackAction5,
        6: DoCallBackAction6,
        7: DoCallBackAction7 }

