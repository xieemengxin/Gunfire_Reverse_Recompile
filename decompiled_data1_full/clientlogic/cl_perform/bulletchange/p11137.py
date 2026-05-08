# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/bulletchange/p11137.pyc
# RelativePath: clientlogic/cl_perform/bulletchange/p11137.pyc
# Source Generated with Decompyle++
# File: p11137.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.bulletchange import CBulletChange as CCustomPerform
from . import action
from . import condition

def Action1(oWarrior, pfBulletChange):
    action.BulletChangeThrowInfiniteFire(oWarrior, pfBulletChange, 1)


def DisableAction1(oWarrior, pfBulletChange):
    action.BulletChangeThrowInfiniteFire(oWarrior, pfBulletChange, 0)


class CPerform(CCustomPerform):
    m_SID = 11137
    m_Name = '能力透支子弹效果'
    m_MaxLevel = 1
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = {
        1: DisableAction1 }
    m_CBFuncAction = { }

