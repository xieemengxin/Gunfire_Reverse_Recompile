# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/benediction/p13716.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/benediction/p13716.pyc
# Source Generated with Decompyle++
# File: p13716.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK
from cl_newformula import Func216, Func226, Func227

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1377, 0, { }, -1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADDRELIC, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REMOVERELIC, -1, 1, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, None, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SWITCH_CAREER_PERFORM, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, (lambda *a: max(int(30000 - (Func216(*a) * 3 + Func226(*a) * 2 + Func227(*a)) * 300), 0)), 0, 0, '')


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveChangeAttr(oWarrior, oEventCB, 'HPMax', (lambda *a: max(int(50 - Func216(*a) * 1.5 - Func226(*a) * 1 - Func227(*a) * 0.5), 0) * 100), 0)
    cl_evact.PassiveChangeAttr(oWarrior, oEventCB, 'MoveSpeed', 0, (lambda *a: max(int(5000 - (Func216(*a) * 3 + Func226(*a) * 2 + Func227(*a)) * 100), 0)))
    cl_action.CommonChangeCareerPerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'ColdTime', (lambda *a: -max(int(5000 - (Func216(*a) * 3 + Func226(*a) * 2 + Func227(*a)) * 100), 0)), 0, None)
    cl_action.CommonChangePerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 1310, 'ColdTime', (lambda *a: -max(int(5000 - (Func216(*a) * 3 + Func226(*a) * 2 + Func227(*a)) * 100), 0)), 0)
    if oWarrior.QueryAttr('ShieldMax') > 0:
        cl_evact.PassiveChangeAttr(oWarrior, oEventCB, 'ShieldMax', (lambda *a: max(int(50 - Func216(*a) * 1.5 - Func226(*a) * 1 - Func227(*a) * 0.5), 0) * 100), 0)
    else:
        cl_evact.PassiveChangeAttr(oWarrior, oEventCB, 'ArmorMax', (lambda *a: max(int(50 - Func216(*a) * 1.5 - Func226(*a) * 1 - Func227(*a) * 0.5), 0) * 100), 0)


class CPerform(CCustomPerform):
    m_SID = 13716
    m_Name = '超前消费'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Career = None

