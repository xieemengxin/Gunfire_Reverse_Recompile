# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4340.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4340.pyc
# Source Generated with Decompyle++
# File: p4340.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'Att', 10000, 0, 0)
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'AttSpeed', 2000, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'Att', 20000, 0, 0)
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'AttSpeed', 4000, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'Att', 35000, 0, 0)
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'AttSpeed', 6000, 0, 0)
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 7148)


def DisableAction3(oWarrior, oLifeCycle):
    cl_action.CommonRemovePerform(oWarrior, oLifeCycle, 7148)


class CPerform(CCustomPerform):
    m_SID = 4340
    m_Name = '御灵师仆从E2'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = {
        3: DisableAction3 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = { }
    m_BaseArgData = { }
    m_DieDisable = 0

