# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/bulletchange/p11105.pyc
# RelativePath: clientlogic/cl_perform/bulletchange/p11105.pyc
# Source Generated with Decompyle++
# File: p11105.pyc (Python 3.6)

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


def Action3(oWarrior, pfBulletChange):
    action.BulletChangeListenSnapshotMsg(oWarrior, pfBulletChange, cl_msgcenter.MSG_WAR_COSTBULLET, -1, 2, 0, 0)


def DoCallBackAction0(oWarrior, pfBulletChange, oSkill, dClientInfo):
    if condition.CheckOwnServerState(oWarrior, pfBulletChange, oSkill, dClientInfo, 32358):
        action.BulletChangeExtBulletUse(oWarrior, pfBulletChange, oSkill, dClientInfo, (lambda *a: Func309(*a) * 1 + 0))


def DoCallBackAction1(oWarrior, pfBulletChange, oSkill, dClientInfo):
    if condition.CheckOwnServerState(oWarrior, pfBulletChange, oSkill, dClientInfo, 32359):
        action.BulletChangeExtBulletUse(oWarrior, pfBulletChange, oSkill, dClientInfo, (lambda *a: Func309(*a) * 2 + 0))


def DoCallBackAction2(oWarrior, pfBulletChange, oSkill, dClientInfo):
    if condition.CheckOwnServerState(oWarrior, pfBulletChange, oSkill, dClientInfo, 32360):
        action.BulletChangeExtBulletUse(oWarrior, pfBulletChange, oSkill, dClientInfo, (lambda *a: Func309(*a) * 3 + 0))


class CPerform(CCustomPerform):
    m_SID = 11105
    m_Name = '雨环子弹消耗翻倍'
    m_MaxLevel = 3
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2 }

