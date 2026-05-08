# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/daytrialpf/p4681.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/daytrialpf/p4681.pyc
# Source Generated with Decompyle++
# File: p4681.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.daytrial import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL, DAM_TYPE_PERFORM, DAM_TYPE_WEAPON, DAM_USE_ALL, OBJ_SELF
from cl_newformula import Func353, Func356

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_EXPLOSION, -1, 1, 0, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.PassiveCBUsePerformAtCenterPos(oWarrior, oEventCB, 1671)
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: min(int((1 - Func356(*a) / Func353(*a)) * 1500), 1500))) > 0:
        cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: min(int((1 - Func356(*a) / Func353(*a)) * 1500), 1500)), DAM_TYPE_WEAPON | DAM_TYPE_PERFORM | DAM_TYPE_NORMAL | DAM_USE_ALL, 0, 0, 1, None, None, None, None, None, None, None, None)


class CPerform(CCustomPerform):
    m_SID = 4681
    m_Name = '爆炸会对自己造成伤害与击退'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0

