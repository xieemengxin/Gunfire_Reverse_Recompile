# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/bulletchange/p11125.pyc
# RelativePath: clientlogic/cl_perform/bulletchange/p11125.pyc
# Source Generated with Decompyle++
# File: p11125.pyc (Python 3.6)

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


def DoCallBackAction0(oWarrior, pfBulletChange, oSkill, dClientInfo):
    if condition.CheckFromPointPerform(oWarrior, pfBulletChange, dClientInfo, 9312):
        if condition.CheckOwnServerState(oWarrior, pfBulletChange, oSkill, dClientInfo, 1763) and condition.CheckRandom(oWarrior, pfBulletChange, oSkill, dClientInfo, 10000, 2000):
            action.BulletChangeCBRevertDualPFBulletByFightType(oWarrior, pfBulletChange, oSkill, dClientInfo, 2)
        else:
            action.BulletChangeCBRevertDualPFBulletByFightType(oWarrior, pfBulletChange, oSkill, dClientInfo, 1)
    else:
        action.BulletChangeCBCostDualPFBullet(oWarrior, pfBulletChange, oSkill, dClientInfo, 300)


def DoCallBackAction1(oWarrior, pfBulletChange, oSkill, dClientInfo):
    if condition.CheckOwnServerState(oWarrior, pfBulletChange, oSkill, dClientInfo, 1763) and condition.CheckRandom(oWarrior, pfBulletChange, oSkill, dClientInfo, 10000, 2000):
        action.BulletChangeCBRevertDualPFBulletByFightType(oWarrior, pfBulletChange, oSkill, dClientInfo, 2)
    else:
        action.BulletChangeCBRevertDualPFBulletByFightType(oWarrior, pfBulletChange, oSkill, dClientInfo, 1)


class CPerform(CCustomPerform):
    m_SID = 11125
    m_Name = '望潮双持射击回复能量效果'
    m_MaxLevel = 1
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }

