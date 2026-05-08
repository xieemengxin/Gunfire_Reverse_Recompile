# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p5345.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p5345.pyc
# Source Generated with Decompyle++
# File: p5345.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import STATUS_MOVE, STATUS_STOP
from cl_newformula import Func686

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Enable', 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_MOVESTATUSCHANGE, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckMoveStatus(oWarrior, oEventCB, STATUS_STOP):
        cl_action.PassiveCloseCycleExecCBFuncAction(oWarrior, oEventCB.GetCBLifeCycle())
        cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'Enable', 0)
    elif cl_evcon.CheckMoveStatus(oWarrior, oEventCB, STATUS_MOVE) and oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('Enable') == 0:
        cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'Enable', 1)
        cl_action.PassiveCycleExecCBFuncAction(oWarrior, oEventCB.GetCBLifeCycle(), 100, 100, 2)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventCBAddSourceWeaponPFBullet(oWarrior, oEventCB, 9690, (lambda *a: Func686(*a, **{
'iPerform': 9690,
'sAttr': 'PFBulletRecover' })), 0, 0)


class CPerform(CCustomPerform):
    m_SID = 5345
    m_Name = '#NT#双刀自动回复武器资源'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0

