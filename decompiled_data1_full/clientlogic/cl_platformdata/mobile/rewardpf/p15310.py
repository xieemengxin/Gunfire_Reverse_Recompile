# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p15310.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p15310.pyc
# Source Generated with Decompyle++
# File: p15310.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import CREATE_PLANT, OBJ_VICTIM
from cl_newformula import Func302

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GARDENER_OPERATION_PLANT, CREATE_PLANT, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func302(*a, **{
'sAttr': 'Phase' }))) == 3:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.EventCBSetTargetStateArgVal(oWarrior, oEventCB, 33710, 'ExtraAttParasiticCnt', 2, 0)


class CPerform(CCustomPerform):
    m_SID = 15310
    m_Name = '根深蒂固'
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

