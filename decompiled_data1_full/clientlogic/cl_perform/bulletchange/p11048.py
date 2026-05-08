# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/bulletchange/p11048.pyc
# RelativePath: clientlogic/cl_perform/bulletchange/p11048.pyc
# Source Generated with Decompyle++
# File: p11048.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.bulletchange import CBulletChange as CCustomPerform
from . import action
from . import condition
from cl_commondefines import PF_SUBMSG_SWITCHWEAPON

def Action1(oWarrior, pfBulletChange):
    action.BulletChangeListenMsgCallBack(oWarrior, pfBulletChange, cl_msgcenter.MSG_WAR_COSTBULLET, -1, 0, 0, 0)
    action.BulletChangeListenMsgCallBack(oWarrior, pfBulletChange, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_SWITCHWEAPON, 2, 0, 0)


def DoCallBackAction0(oWarrior, pfBulletChange, oSkill, dClientInfo):
    if not condition.CheckOwnClientState(oWarrior, pfBulletChange, oSkill, dClientInfo, 1007) and condition.CheckFromPointPerforms(oWarrior, pfBulletChange, dClientInfo, {
        0: 9495,
        1: 9097,
        2: 9098,
        3: 9498,
        4: 9295 }):
        action.BulletChangeReduceBulletUse(oWarrior, pfBulletChange, oSkill, dClientInfo, 0)
        action.BulletChangeCBAddStateCount(oWarrior, pfBulletChange, oSkill, dClientInfo, 1007, -1)
        if condition.CheckTargetStateCount(oWarrior, pfBulletChange, oSkill, dClientInfo, 1007, 0):
            action.BulletChangeCBDelClientState(oWarrior, pfBulletChange, oSkill, dClientInfo, 1007)


def DoCallBackAction1(oWarrior, pfBulletChange, oSkill, dClientInfo):
    if condition.CheckTargetStateCount(oWarrior, pfBulletChange, oSkill, dClientInfo, 1007, 0):
        action.BulletChangeCBDelClientState(oWarrior, pfBulletChange, oSkill, dClientInfo, 1007)


def DoCallBackAction2(oWarrior, pfBulletChange, oSkill, dClientInfo):
    action.BulletChangeCBDelClientState(oWarrior, pfBulletChange, oSkill, dClientInfo, 1007)


def DoCallBackAction3(oWarrior, pfBulletChange, oSkill, dClientInfo):
    if not condition.CheckFromPointPerforms(oWarrior, pfBulletChange, dClientInfo, {
        0: 9495,
        1: 9097,
        2: 9098,
        3: 9498,
        4: 9295 }):
        action.BulletChangeReduceBulletUse(oWarrior, pfBulletChange, oSkill, dClientInfo, 0)
        action.BulletChangeCBAddStateCount(oWarrior, pfBulletChange, oSkill, dClientInfo, 1007, -1)
        if condition.CheckTargetStateCount(oWarrior, pfBulletChange, oSkill, dClientInfo, 1007, 0):
            action.BulletChangeCBDelClientState(oWarrior, pfBulletChange, oSkill, dClientInfo, 1007)


class CPerform(CCustomPerform):
    m_SID = 11048
    m_Name = '遗物5792子弹效果'
    m_MaxLevel = 1
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3 }

