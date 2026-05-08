# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/bulletchange/p11130.pyc
# RelativePath: clientlogic/cl_perform/bulletchange/p11130.pyc
# Source Generated with Decompyle++
# File: p11130.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.bulletchange import CBulletChange as CCustomPerform
from . import action
from . import condition
from cl_newformula import Func309

def Action1(oWarrior, pfBulletChange):
    action.BulletChangeListenMsgCallBack(oWarrior, pfBulletChange, cl_msgcenter.MSG_WAR_COSTBULLET, -1, 0, 0, 0)


def DoCallBackAction0(oWarrior, pfBulletChange, oSkill, dClientInfo):
    if (condition.CheckOwnServerState(oWarrior, pfBulletChange, oSkill, dClientInfo, 1446) or condition.CheckFromPointPerform(oWarrior, pfBulletChange, dClientInfo, 9418)) and condition.CheckRandom(oWarrior, pfBulletChange, oSkill, dClientInfo, 10000, 3000):
        action.BulletChangeRevertBulletBag(oWarrior, pfBulletChange, oSkill, dClientInfo)
    elif condition.CheckFromPointPerform(oWarrior, pfBulletChange, dClientInfo, 9418) and condition.CheckRandom(oWarrior, pfBulletChange, oSkill, dClientInfo, 10000, 3000) and condition.CheckBulletConsume(oWarrior, pfBulletChange, oSkill, dClientInfo):
        action.BulletChangeRevertBullet(oWarrior, pfBulletChange, oSkill, dClientInfo, (lambda *a: Func309(*a) * 1 + 0), 0)


def DoCallBackAction1(oWarrior, pfBulletChange, oSkill, dClientInfo):
    if condition.CheckFromPointPerform(oWarrior, pfBulletChange, dClientInfo, 9418) and condition.CheckRandom(oWarrior, pfBulletChange, oSkill, dClientInfo, 10000, 3000) and condition.CheckBulletConsume(oWarrior, pfBulletChange, oSkill, dClientInfo):
        action.BulletChangeRevertBullet(oWarrior, pfBulletChange, oSkill, dClientInfo, (lambda *a: Func309(*a) * 1 + 0), 0)


def DoCallBackAction2(oWarrior, pfBulletChange, oSkill, dClientInfo):
    if condition.CheckFromPointPerform(oWarrior, pfBulletChange, dClientInfo, 9418) and condition.CheckRandom(oWarrior, pfBulletChange, oSkill, dClientInfo, 10000, 3000):
        action.BulletChangeRevertBulletBag(oWarrior, pfBulletChange, oSkill, dClientInfo)


class CPerform(CCustomPerform):
    m_SID = 11130
    m_Name = '#NT#水枪第三幕概率不消耗子弹彩蛋'
    m_MaxLevel = 1
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2 }

