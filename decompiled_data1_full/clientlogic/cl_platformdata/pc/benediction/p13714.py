# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/benediction/p13714.pyc
# RelativePath: clientlogic/cl_platformdata/pc/benediction/p13714.pyc
# Source Generated with Decompyle++
# File: p13714.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform
from cl_commondefines import DAM_TYPE_CORRISION, DAM_TYPE_FIRE, DAM_TYPE_THUNDER, OBJ_VICTIM

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32548, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEDEBUFF, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckTargetHasState(oWarrior, oEventCB, 1504, 1, 1, None, None) == 0:
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1504, 200, { }, 1, 0, None)
        if cl_evcon.CheckTargetAddState(oWarrior, oEventCB, 20026):
            cl_evact.PassiveAddTargetStateWithCache(oWarrior, oEventCB, 20027, 500, { }, 0, DAM_TYPE_CORRISION, None)
            cl_evact.PassiveAddTargetStateWithCache(oWarrior, oEventCB, 20028, 500, { }, 0, DAM_TYPE_THUNDER, None)
        elif cl_evcon.CheckTargetAddState(oWarrior, oEventCB, 20027):
            cl_evact.PassiveAddTargetStateWithCache(oWarrior, oEventCB, 20026, 500, { }, 0, DAM_TYPE_FIRE, None)
            cl_evact.PassiveAddTargetStateWithCache(oWarrior, oEventCB, 20028, 500, { }, 0, DAM_TYPE_THUNDER, None)
        else:
            cl_evact.PassiveAddTargetStateWithCache(oWarrior, oEventCB, 20026, 500, { }, 0, DAM_TYPE_FIRE, None)
            cl_evact.PassiveAddTargetStateWithCache(oWarrior, oEventCB, 20027, 500, { }, 0, DAM_TYPE_CORRISION, None)


class CPerform(CCustomPerform):
    m_SID = 13714
    m_Name = '苦痛逆转'
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
    m_Career = None

