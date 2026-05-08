# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/bulletchange/p11121.pyc
# RelativePath: clientlogic/cl_perform/bulletchange/p11121.pyc
# Source Generated with Decompyle++
# File: p11121.pyc (Python 3.6)

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
    action.BulletChangeCBTriggerGroup(oWarrior, pfBulletChange, oSkill, dClientInfo, {
        1: 3000 })


def DoCallBackAction1(oWarrior, pfBulletChange, oSkill, dClientInfo):
    action.BulletChangeAddServerState(oWarrior, pfBulletChange, oSkill, dClientInfo, 1760, 0, -1, 0)
    action.BulletChangeReduceBulletUse(oWarrior, pfBulletChange, oSkill, dClientInfo, 0)


class CPerform(CCustomPerform):
    m_SID = 11121
    m_Name = '铭刻4952子弹效果'
    m_MaxLevel = 1
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }

