# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p16056.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p16056.pyc
# Source Generated with Decompyle++
# File: p16056.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL, DAM_TYPE_PERFORM, DAM_TYPE_WEAPON, DAM_USE_ALL, OBJ_VICTIM
from cl_newformula import Func438

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEDEBUFF, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 1605, 1, 1, None) == 0:
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1605, 300, { }, 1, 0, None)
        cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: Func438(*a) * 100 / 100), DAM_TYPE_WEAPON | DAM_TYPE_PERFORM | DAM_TYPE_NORMAL | DAM_USE_ALL, 1, 0, 0, 0, -1, -1, -1, None, None, None, None)


class CPerform(CCustomPerform):
    m_SID = 16056
    m_Name = '元素回响'
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

