# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p15183.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p15183.pyc
# Source Generated with Decompyle++
# File: p15183.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_newformula import Func374, Func385, Func558, Func589
from cl_commondefines import DAM_TYPE_PERFORM, DAM_TYPE_TRUE, DAM_USE_ALL, OBJ_SELF

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COSTPFBULLET, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func558(*a))) > 50:
        if not cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func589(*a))) <= 100:
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
            cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: min(Func385(*a) * 10 / 100, Func374(*a) - 100)), DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, None)
        cl_evact.EventCBReturnSourceWeaponPFBullet(oWarrior, oEventCB, (lambda *a: Func385(*a) * 3 // 10))


class CPerform(CCustomPerform):
    m_SID = 15183
    m_Name = '舍身求法'
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

