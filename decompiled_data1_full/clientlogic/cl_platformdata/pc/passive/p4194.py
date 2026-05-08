# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4194.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4194.pyc
# Source Generated with Decompyle++
# File: p4194.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import MAIN_HOLD

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveEnableBulletChangeRule(oWarrior, oLifeCycle, 11103, 1)
    cl_action.CommonChangeWeaponAttr(oWarrior, oLifeCycle, 'BulletSpeed', 400, 0, MAIN_HOLD)
    cl_action.CommonChangeWeaponAttr(oWarrior, oLifeCycle, 'Radius', 0, -10000, MAIN_HOLD)


class CPerform(CCustomPerform):
    m_SID = 4194
    m_Name = '瞄准关子弹变更被动'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = { }
    m_BaseArgData = { }
    m_DieDisable = 0

