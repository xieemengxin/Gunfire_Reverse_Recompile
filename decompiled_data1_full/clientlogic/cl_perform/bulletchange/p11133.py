# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/bulletchange/p11133.pyc
# RelativePath: clientlogic/cl_perform/bulletchange/p11133.pyc
# Source Generated with Decompyle++
# File: p11133.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.bulletchange import CBulletChange as CCustomPerform
from . import action
from . import condition
from cl_commondefines import PF_SUBMSG_THROW
from cl_newformula import Func420

def Action1(oWarrior, pfBulletChange):
    action.BulletChangeListenMsgCallBack(oWarrior, pfBulletChange, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 0, 0, 0)


def DoCallBackAction0(oWarrior, pfBulletChange, oSkill, dClientInfo):
    if condition.CheckFromPointPerform(oWarrior, pfBulletChange, dClientInfo, 1409):
        action.BulletChangeCBTriggerGroup(oWarrior, pfBulletChange, oSkill, dClientInfo, {
            1: 4000 })


def DoCallBackAction1(oWarrior, pfBulletChange, oSkill, dClientInfo):
    action.BulletChangeCBOwnerClientBehavior(oWarrior, pfBulletChange, oSkill, dClientInfo, 1011, 0)
    action.BulletChangeReduceBulletUse(oWarrior, pfBulletChange, oSkill, dClientInfo, 0)
    if condition.CheckThrowBulletCntUpperLimit(oWarrior, pfBulletChange, 1):
        action.BulletChangeCBSetSkillCacheChange(oWarrior, pfBulletChange, oSkill, dClientInfo, 'TriggerTimes', 0, (lambda *a: (Func420(*a) - 1) * 10000))


def DoCallBackAction2(oWarrior, pfBulletChange, oSkill, dClientInfo):
    if condition.CheckThrowBulletCntUpperLimit(oWarrior, pfBulletChange, 1):
        action.BulletChangeCBSetSkillCacheChange(oWarrior, pfBulletChange, oSkill, dClientInfo, 'TriggerTimes', 0, (lambda *a: (Func420(*a) - 1) * 10000))


class CPerform(CCustomPerform):
    m_SID = 11133
    m_Name = '嗷呜乾坤一掷骰效果'
    m_MaxLevel = 1
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2 }

