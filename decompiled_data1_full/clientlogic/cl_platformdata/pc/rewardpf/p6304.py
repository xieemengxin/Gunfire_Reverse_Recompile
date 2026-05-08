# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p6304.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p6304.pyc
# Source Generated with Decompyle++
# File: p6304.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4504, 0, (0, None, ((308,), (lambda a0: a0 * 3 + 0))))


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4504, 0, (0, None, ((308,), (lambda a0: a0 * 3 + 0))))


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4504, 0, (0, None, ((308,), (lambda a0: a0 * 3 + 0))))


def Action4(oWarrior, oLifeCycle):
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4504, 0, (0, None, ((308,), (lambda a0: a0 * 3 + 0))))


class CPerform(CCustomPerform):
    m_SID = 6304
    m_Name = '图纸1018-1021特种弹载弹量增加'
    m_MaxLevel = 4
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3,
        4: Action4 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = { }
    m_BaseArgData = { }
    m_DieDisable = 0

