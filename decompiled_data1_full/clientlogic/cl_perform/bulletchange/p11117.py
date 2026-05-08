# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/bulletchange/p11117.pyc
# RelativePath: clientlogic/cl_perform/bulletchange/p11117.pyc
# Source Generated with Decompyle++
# File: p11117.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.bulletchange import CBulletChange as CCustomPerform
from . import action
from . import condition

def Action1(oWarrior, pfBulletChange):
    action.BulletChangeListenMsgCallBack(oWarrior, pfBulletChange, cl_msgcenter.MSG_WAR_COSTBULLET, -1, 0, 0, 1)


def DoCallBackAction0(oWarrior, pfBulletChange, oSkill, dClientInfo):
    if not condition.CheckTargetServerStateGreaterCount(oWarrior, pfBulletChange, oSkill, dClientInfo, 33639, 1) and condition.CheckFromPointPerforms(oWarrior, pfBulletChange, dClientInfo, {
        0: 9495,
        1: 9097,
        2: 9098,
        3: 9498,
        4: 9295 }):
        action.BulletChangeReduceBulletUse(oWarrior, pfBulletChange, oSkill, dClientInfo, 0)


def DoCallBackAction1(oWarrior, pfBulletChange, oSkill, dClientInfo):
    if not condition.CheckFromPointPerforms(oWarrior, pfBulletChange, dClientInfo, {
        0: 9495,
        1: 9097,
        2: 9098,
        3: 9498,
        4: 9295 }):
        action.BulletChangeReduceBulletUse(oWarrior, pfBulletChange, oSkill, dClientInfo, 0)


class CPerform(CCustomPerform):
    m_SID = 11117
    m_Name = '天赋3013不消耗子弹效果'
    m_MaxLevel = 1
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }

