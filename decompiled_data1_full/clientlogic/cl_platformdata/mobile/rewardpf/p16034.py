# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p16034.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p16034.pyc
# Source Generated with Decompyle++
# File: p16034.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_newformula import Func441
from cl_commondefines import OBJ_SELF

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenGlobalMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WARMSG_PHASESTART, -1, 0)
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'HPMax', 0, (lambda *a: max(int(Func441(*a) * -100 + 10000), 0)), 0)
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'ShieldMax', 0, (lambda *a: max(int(Func441(*a) * -100 + 10000), 0)), 0)
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'ArmorMax', 0, (lambda *a: max(int(Func441(*a) * -100 + 10000), 0)), 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.PassiveChangeAttr(oWarrior, oEventCB, 'HPMax', (lambda *a: max(int(Func441(*a) * -100 + 10000), 0)), 0)
    cl_evact.PassiveChangeAttr(oWarrior, oEventCB, 'ShieldMax', (lambda *a: max(int(Func441(*a) * -100 + 10000), 0)), 0)
    cl_evact.PassiveChangeAttr(oWarrior, oEventCB, 'ArmorMax', (lambda *a: max(int(Func441(*a) * -100 + 10000), 0)), 0)


class CPerform(CCustomPerform):
    m_SID = 16034
    m_Name = '防御透支'
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

