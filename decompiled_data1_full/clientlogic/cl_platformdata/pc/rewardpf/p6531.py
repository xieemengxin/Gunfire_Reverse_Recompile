# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p6531.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p6531.pyc
# Source Generated with Decompyle++
# File: p6531.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_newformula import Func308

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4502, 0, (lambda *a: Func308(*a) * 45 + 0))
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4503, 0, (lambda *a: Func308(*a) * 8 + 0))
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4504, 0, (lambda *a: Func308(*a) * 3 + 0))


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4502, 0, (lambda *a: Func308(*a) * 45 + 0))
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4503, 0, (lambda *a: Func308(*a) * 8 + 0))
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4504, 0, (lambda *a: Func308(*a) * 3 + 0))


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4502, 0, (lambda *a: Func308(*a) * 45 + 0))
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4503, 0, (lambda *a: Func308(*a) * 8 + 0))
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4504, 0, (lambda *a: Func308(*a) * 3 + 0))


def Action4(oWarrior, oLifeCycle):
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4502, 0, (lambda *a: Func308(*a) * 45 + 0))
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4503, 0, (lambda *a: Func308(*a) * 8 + 0))
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4504, 0, (lambda *a: Func308(*a) * 3 + 0))


def Action5(oWarrior, oLifeCycle):
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4502, 0, (lambda *a: Func308(*a) * 45 + 0))
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4503, 0, (lambda *a: Func308(*a) * 8 + 0))
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4504, 0, (lambda *a: Func308(*a) * 3 + 0))


class CPerform(CCustomPerform):
    m_SID = 6531
    m_Name = '军用背包'
    m_MaxLevel = 5
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3,
        4: Action4,
        5: Action5 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = { }
    m_BaseArgData = { }
    m_DieDisable = 0

