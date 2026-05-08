# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p5334.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p5334.pyc
# Source Generated with Decompyle++
# File: p5334.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_newformula import Func686

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEDEBUFF, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonAddSourceWeaponPFBullet(oWarrior, oEventCB.GetCBLifeCycle(), 9799, (lambda *a: Func686(*a, **{
'iPerform': 9799,
'sAttr': 'PFBulletRecover' })))


class CPerform(CCustomPerform):
    m_SID = 5334
    m_Name = '#NT#元素法杖能量回复'
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

