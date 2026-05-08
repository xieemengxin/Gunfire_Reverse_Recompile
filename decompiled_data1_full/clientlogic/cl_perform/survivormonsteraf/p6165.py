# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/survivormonsteraf/p6165.pyc
# RelativePath: clientlogic/cl_perform/survivormonsteraf/p6165.pyc
# Source Generated with Decompyle++
# File: p6165.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.survivormonsteraf import CPerform as CCustomPerform
from cl_commondefines import MAF_TYPE_FIRE, WARRIOR_NORBOX, WARRIOR_NORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DIE_BEFORE, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetRangeTargetByFightType(oWarrior, oEventCB, 15, WARRIOR_NORMAL, 1, 0, 1, 0, 0, { }, 1, None)
    cl_evact.EventCBRemoveMonsterfromTargetList(oWarrior, oEventCB, WARRIOR_NORBOX)
    cl_evact.PassiveCBUsePerform2EvtTarget(oWarrior, oEventCB, 1708, None, { })


class CPerform(CCustomPerform):
    m_SID = 6165
    m_Name = '传承的'
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
    m_MonsterAfType = MAF_TYPE_FIRE

