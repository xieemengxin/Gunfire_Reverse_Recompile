# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/bulletchange/p11113.pyc
# RelativePath: clientlogic/cl_perform/bulletchange/p11113.pyc
# Source Generated with Decompyle++
# File: p11113.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.bulletchange import CBulletChange as CCustomPerform
from . import action
from . import condition
from cl_newformula import Func310, Func335

def Action1(oWarrior, pfBulletChange):
    action.BulletChangeListenMsgCallBack(oWarrior, pfBulletChange, cl_msgcenter.MSG_WAR_COSTBULLET, -1, 0, 0, 0)


def DoCallBackAction0(oWarrior, pfBulletChange, oSkill, dClientInfo):
    if condition.CheckFromPointPerform(oWarrior, pfBulletChange, dClientInfo, 9499) and condition.CheckWeaponBulletCnt(oWarrior, pfBulletChange, oSkill, dClientInfo, 0) == 0:
        action.BulletChangeExtBulletUse(oWarrior, pfBulletChange, oSkill, dClientInfo, (lambda *a: Func335(*a) - Func310(*a)))


class CPerform(CCustomPerform):
    m_SID = 11113
    m_Name = '震山镈铭刻子弹消耗'
    m_MaxLevel = 1
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }

