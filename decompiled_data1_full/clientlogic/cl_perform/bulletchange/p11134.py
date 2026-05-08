# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/bulletchange/p11134.pyc
# RelativePath: clientlogic/cl_perform/bulletchange/p11134.pyc
# Source Generated with Decompyle++
# File: p11134.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.bulletchange import CBulletChange as CCustomPerform
from . import action
from . import condition
from cl_commondefines import PF_SUBMSG_THROW

def Action1(oWarrior, pfBulletChange):
    action.BulletChangeListenMsgCallBack(oWarrior, pfBulletChange, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 0, 0, 0)


def DoCallBackAction0(oWarrior, pfBulletChange, oSkill, dClientInfo):
    if condition.CheckFromPointPerforms(oWarrior, pfBulletChange, dClientInfo, {
        1: 1409,
        3: 1436,
        4: 1429,
        5: 1410,
        6: 1431 }):
        if condition.CheckThrowMaxUpperLimit(oWarrior, pfBulletChange, 20):
            action.BulletChangeCBTriggerGroup(oWarrior, pfBulletChange, oSkill, dClientInfo, {
                2: 5000 })
        else:
            action.BulletChangeCBTriggerGroup(oWarrior, pfBulletChange, oSkill, dClientInfo, {
                2: 2000 })


def DoCallBackAction1(oWarrior, pfBulletChange, oSkill, dClientInfo):
    if condition.CheckThrowMaxUpperLimit(oWarrior, pfBulletChange, 20):
        action.BulletChangeCBTriggerGroup(oWarrior, pfBulletChange, oSkill, dClientInfo, {
            2: 5000 })
    else:
        action.BulletChangeCBTriggerGroup(oWarrior, pfBulletChange, oSkill, dClientInfo, {
            2: 2000 })


def DoCallBackAction2(oWarrior, pfBulletChange, oSkill, dClientInfo):
    action.BulletChangeCBSetSkillCacheChange(oWarrior, pfBulletChange, oSkill, dClientInfo, 'TriggerTimes', 1, 0)


class CPerform(CCustomPerform):
    m_SID = 11134
    m_Name = '双生法术效果'
    m_MaxLevel = 1
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2 }

