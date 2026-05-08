# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/bulletchange/p11085.pyc
# RelativePath: clientlogic/cl_perform/bulletchange/p11085.pyc
# Source Generated with Decompyle++
# File: p11085.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.bulletchange import CBulletChange as CCustomPerform
from . import action
from . import condition

def Action1(oWarrior, pfBulletChange):
    action.BulletChangeListenMsgCallBack(oWarrior, pfBulletChange, cl_msgcenter.MSG_WAR_COSTBULLET, -1, 0, 0, 0)


def Action2(oWarrior, pfBulletChange):
    action.BulletChangeListenMsgCallBack(oWarrior, pfBulletChange, cl_msgcenter.MSG_WAR_COSTBULLET, -1, 2, 0, 0)


def DoCallBackAction0(oWarrior, pfBulletChange, oSkill, dClientInfo):
    if condition.CheckOwnServerState(oWarrior, pfBulletChange, oSkill, dClientInfo, 32317) and condition.CheckOwnServerState(oWarrior, pfBulletChange, oSkill, dClientInfo, 32335):
        action.BulletChangeCBTriggerGroup(oWarrior, pfBulletChange, oSkill, dClientInfo, {
            1: 2000 })


def DoCallBackAction1(oWarrior, pfBulletChange, oSkill, dClientInfo):
    action.BulletChangeReduceBulletUse(oWarrior, pfBulletChange, oSkill, dClientInfo, 0)


def DoCallBackAction2(oWarrior, pfBulletChange, oSkill, dClientInfo):
    if condition.CheckOwnServerState(oWarrior, pfBulletChange, oSkill, dClientInfo, 32317) and condition.CheckOwnServerState(oWarrior, pfBulletChange, oSkill, dClientInfo, 32336):
        action.BulletChangeCBTriggerGroup(oWarrior, pfBulletChange, oSkill, dClientInfo, {
            1: 3000 })


class CPerform(CCustomPerform):
    m_SID = 11085
    m_Name = '天赋2402子弹效果'
    m_MaxLevel = 2
    m_EnableActionInfo = {
        1: Action1,
        2: Action2 }
    m_DisableActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2 }

