# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/bulletchange/p11132.pyc
# RelativePath: clientlogic/cl_perform/bulletchange/p11132.pyc
# Source Generated with Decompyle++
# File: p11132.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.bulletchange import CBulletChange as CCustomPerform
from . import action
from . import condition
from cl_commondefines import PFBULLET_SUBMSG_ADD_BEFORE

def Action1(oWarrior, pfBulletChange):
    action.BulletChangeListenMsgCallBack(oWarrior, pfBulletChange, cl_msgcenter.MSG_WAR_WEAPONPFBULLETCHANGE, PFBULLET_SUBMSG_ADD_BEFORE, 0, 0, 0)


def DoCallBackAction0(oWarrior, pfBulletChange, oSkill, dClientInfo):
    if condition.CheckFromPointPerform(oWarrior, pfBulletChange, dClientInfo, 9312) and condition.CheckWeaponResourceLessPercent(oWarrior, pfBulletChange, 50):
        action.BulletChangeCBRevertPFBullet(oWarrior, pfBulletChange, oSkill, dClientInfo, 2000, 1)


def DoCallBackAction1(oWarrior, pfBulletChange, oSkill, dClientInfo):
    if condition.CheckWeaponResourceLessPercent(oWarrior, pfBulletChange, 50):
        action.BulletChangeCBRevertPFBullet(oWarrior, pfBulletChange, oSkill, dClientInfo, 2000, 1)


class CPerform(CCustomPerform):
    m_SID = 11132
    m_Name = '枯荣往复望潮特殊处理'
    m_MaxLevel = 1
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }

