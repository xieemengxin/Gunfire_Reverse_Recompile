# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p16036.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p16036.pyc
# Source Generated with Decompyle++
# File: p16036.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import CURE_TYPE_PERFORM, DAM_USE_HP, OBJ_SELF
from cl_newformula import Func304, Func324, Func410

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REVTOTALDAM, -1, 0, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32729, 0, { }, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 32729, (lambda *a: Func324(*a)), -1)
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func410(*a, **{
'sid': 32729 }))) >= 20 and oWarrior.HP() > 1:
        cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 32729, -20, -1)
        cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 20026, -1, None, None)
        cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 20027, -1, None, None)
        cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 20028, -1, None, None)
        cl_evact.EventTargetCure(oWarrior, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'HPMax' }) * 10 / 100 + 0), CURE_TYPE_PERFORM | DAM_USE_HP, 1, -1, None)


class CPerform(CCustomPerform):
    m_SID = 16036
    m_Name = '藤甲披肩'
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

