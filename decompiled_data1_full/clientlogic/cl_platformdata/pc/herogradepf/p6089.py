# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/herogradepf/p6089.pyc
# RelativePath: clientlogic/cl_platformdata/pc/herogradepf/p6089.pyc
# Source Generated with Decompyle++
# File: p6089.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CHeroGradePassive as CCustomPerform
from cl_commondefines import OBJ_ATTACK, OBJ_ENEMY
from cl_newformula import Func305

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 0)
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'ShieldMax', 0, 2000, None)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
    if cl_evcon.CheckTargetSideType(oWarrior, oEventCB, OBJ_ENEMY) and cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func305(*a, **{
'sAttr': 'HP' }))) != 0:
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 20026, 500, { }, 0, 0, None)


class CPerform(CCustomPerform):
    m_SID = 6089
    m_Name = '虞火lv.4'
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

