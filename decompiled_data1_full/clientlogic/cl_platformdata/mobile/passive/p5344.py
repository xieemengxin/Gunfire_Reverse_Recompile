# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p5344.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p5344.pyc
# Source Generated with Decompyle++
# File: p5344.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_newformula import Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 100, 100, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 33886) == 0:
        cl_action.CommonAddSourceWeaponPFBullet(oWarrior, oEventCB.GetCBLifeCycle(), 9690, (lambda *a: Func717(*a, **{
'sArg': 'PFBulletRec' })))


class CPerform(CCustomPerform):
    m_SID = 5344
    m_Name = '#NT#双刀一、二段攻击'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = {
        'PFBulletRec': 1000 }
    m_DieDisable = 0

