# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/bulletchange/p11003.pyc
# RelativePath: clientlogic/cl_perform/bulletchange/p11003.pyc
# Source Generated with Decompyle++
# File: p11003.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.bulletchange import CBulletChange as CCustomPerform
from . import action
from . import condition
from cl_commondefines import PF_SUBMSG_FILLBULLET

def Action1(oWarrior, pfBulletChange):
    action.BulletChangeListenMsgCallBack(oWarrior, pfBulletChange, cl_msgcenter.MSG_WAR_COSTBULLET, -1, 0, 0, 0)
    action.BulletChangeListenMsgCallBack(oWarrior, pfBulletChange, cl_msgcenter.MSG_WAR_DP, -1, 1, 0, 0)
    action.BulletChangeListenMsgCallBack(oWarrior, pfBulletChange, cl_msgcenter.MSG_WAR_ATTACK, -1, 2, 0, 0)
    action.BulletChangeListenMsgCallBack(oWarrior, pfBulletChange, cl_msgcenter.MSG_WAR_SWITCH_ATT_PERFORM, -1, 3, 0, 0)
    action.BulletChangeListenMsgCallBack(oWarrior, pfBulletChange, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_FILLBULLET, 3, 0, 0)
    action.BulletChangeListenMsgCallBack(oWarrior, pfBulletChange, cl_msgcenter.MSG_WAR_ATTACK_END, -1, 4, 0, 0)


def DoCallBackAction0(oWarrior, pfBulletChange, oSkill, dClientInfo):
    if condition.CheckOwnClientState(oWarrior, pfBulletChange, oSkill, dClientInfo, 1005):
        action.BulletChangeReduceBulletUse(oWarrior, pfBulletChange, oSkill, dClientInfo, 0)


def DoCallBackAction1(oWarrior, pfBulletChange, oSkill, dClientInfo):
    if condition.CheckFireStatus(oWarrior, pfBulletChange, 5, 1):
        action.BulletChangeCBSummaryFireInfo(oWarrior, pfBulletChange, oSkill, dClientInfo)


def DoCallBackAction2(oWarrior, pfBulletChange, oSkill, dClientInfo):
    if condition.CheckSkillFireHit(oWarrior, pfBulletChange, 5, 1) and condition.CheckOwnClientState(oWarrior, pfBulletChange, oSkill, dClientInfo, 1005) == 0:
        action.BulletChangeCBAddStateCount(oWarrior, pfBulletChange, oSkill, dClientInfo, 1004, 1)
    if condition.CheckTargetStateCount(oWarrior, pfBulletChange, oSkill, dClientInfo, 1004, 5):
        action.BulletChangeCBDelClientState(oWarrior, pfBulletChange, oSkill, dClientInfo, 1004)


def DoCallBackAction3(oWarrior, pfBulletChange, oSkill, dClientInfo):
    action.BulletChangeCBDelClientState(oWarrior, pfBulletChange, oSkill, dClientInfo, 1004)
    action.BulletChangeCBDelClientState(oWarrior, pfBulletChange, oSkill, dClientInfo, 1005)


def DoCallBackAction4(oWarrior, pfBulletChange, oSkill, dClientInfo):
    if condition.CheckSkillFireUnAllHit(oWarrior, pfBulletChange, 5, 1):
        action.BulletChangeCBDelClientState(oWarrior, pfBulletChange, oSkill, dClientInfo, 1004)


class CPerform(CCustomPerform):
    m_SID = 11003
    m_Name = '铭刻4906子弹效果'
    m_MaxLevel = 1
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4 }

