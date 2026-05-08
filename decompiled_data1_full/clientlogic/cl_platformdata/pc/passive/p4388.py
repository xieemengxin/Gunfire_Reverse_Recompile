# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4388.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4388.pyc
# Source Generated with Decompyle++
# File: p4388.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_newformula import Func686

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 24, 24, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonAddSourceWeaponPFBullet(oWarrior, oEventCB.GetCBLifeCycle(), 9093, (lambda *a: Func686(*a, **{
'iPerform': 9093,
'sAttr': 'PFBulletRecover' })))


class CPerform(CCustomPerform):
    m_SID = 4388
    m_Name = '追踪步枪-能量恢复定时'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0

