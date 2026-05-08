# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4123.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4123.pyc
# Source Generated with Decompyle++
# File: p4123.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_PERFORM, DAM_TYPE_TRUE, DAM_USE_ALL, WARRIOR_HERO
from cl_newformula import Func304, Func350

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 4, 25, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetRangeTargetByFightType(oWarrior, oEventCB, (lambda *a: Func350(*a)), WARRIOR_HERO, None, 1, 0, None, None, { }, None, None, None, None, None)
    cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'Att' }) * 100 / 100 + 0), DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 1, 1, None, None, None, None, None, None, None, None)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 7968, 25, { }, 0, 0, None)


class CPerform(CCustomPerform):
    m_SID = 4123
    m_Name = '风神龙卷风被动'
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

