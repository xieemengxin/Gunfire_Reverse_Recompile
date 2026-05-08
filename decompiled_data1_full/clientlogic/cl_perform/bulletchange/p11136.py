# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/bulletchange/p11136.pyc
# RelativePath: clientlogic/cl_perform/bulletchange/p11136.pyc
# Source Generated with Decompyle++
# File: p11136.pyc (Python 3.6)

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
    action.BulletChangeListenMsgCallBack(oWarrior, pfBulletChange, cl_msgcenter.MSG_WAR_COSTBULLET, -1, 1, 0, 0)


def DoCallBackAction0(oWarrior, pfBulletChange, oSkill, dClientInfo):
    if condition.CheckSkillMainPF(oWarrior, pfBulletChange) and condition.CheckRandom(oWarrior, pfBulletChange, oSkill, dClientInfo, 100, 50):
        action.BulletChangeExtBulletUse(oWarrior, pfBulletChange, oSkill, dClientInfo, 1)


def DoCallBackAction1(oWarrior, pfBulletChange, oSkill, dClientInfo):
    if condition.CheckSkillMainPF(oWarrior, pfBulletChange):
        action.BulletChangeExtBulletUse(oWarrior, pfBulletChange, oSkill, dClientInfo, 1)


def DoCallBackAction2(oWarrior, pfBulletChange, oSkill, dClientInfo):
    if condition.CheckRandom(oWarrior, pfBulletChange, oSkill, dClientInfo, 100, 50):
        action.BulletChangeExtBulletUse(oWarrior, pfBulletChange, oSkill, dClientInfo, 1)


def DoCallBackAction3(oWarrior, pfBulletChange, oSkill, dClientInfo):
    action.BulletChangeExtBulletUse(oWarrior, pfBulletChange, oSkill, dClientInfo, 1)


class CPerform(CCustomPerform):
    m_SID = 11136
    m_Name = '等级增幅效果'
    m_MaxLevel = 2
    m_EnableActionInfo = {
        1: Action1,
        2: Action2 }
    m_DisableActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3 }

