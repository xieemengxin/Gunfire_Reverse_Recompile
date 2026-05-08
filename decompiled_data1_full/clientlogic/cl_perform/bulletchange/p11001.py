# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/bulletchange/p11001.pyc
# RelativePath: clientlogic/cl_perform/bulletchange/p11001.pyc
# Source Generated with Decompyle++
# File: p11001.pyc (Python 3.6)

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
    action.BulletChangeListenSnapshotMsg(oWarrior, pfBulletChange, cl_msgcenter.MSG_WAR_COSTBULLET, -1, 0, 0, 0)


def Action2(oWarrior, pfBulletChange):
    action.BulletChangeListenSnapshotMsg(oWarrior, pfBulletChange, cl_msgcenter.MSG_WAR_COSTBULLET, -1, 1, 0, 0)


def DoCallBackAction0(oWarrior, pfBulletChange, oSkill, dClientInfo):
    if condition.CheckFromSameItem(oWarrior, pfBulletChange, oSkill, dClientInfo) and condition.CheckSkillMainPF(oWarrior, pfBulletChange):
        action.BulletChangeExtBulletUse(oWarrior, pfBulletChange, oSkill, dClientInfo, (lambda *a: Func309(*a) * 1 + 0))


def DoCallBackAction1(oWarrior, pfBulletChange, oSkill, dClientInfo):
    if condition.CheckFromSameItem(oWarrior, pfBulletChange, oSkill, dClientInfo) and condition.CheckSkillMainPF(oWarrior, pfBulletChange):
        action.BulletChangeExtBulletUse(oWarrior, pfBulletChange, oSkill, dClientInfo, (lambda *a: Func309(*a) * 2 + 0))


class CPerform(CCustomPerform):
    m_SID = 11001
    m_Name = '铭刻4849子弹效果'
    m_MaxLevel = 2
    m_EnableActionInfo = {
        1: Action1,
        2: Action2 }
    m_DisableActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }

