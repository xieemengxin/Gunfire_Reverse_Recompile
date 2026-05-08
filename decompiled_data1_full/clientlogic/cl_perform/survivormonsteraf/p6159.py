# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/survivormonsteraf/p6159.pyc
# RelativePath: clientlogic/cl_perform/survivormonsteraf/p6159.pyc
# Source Generated with Decompyle++
# File: p6159.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.survivormonsteraf import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, MAF_TYPE_FIRE, OBJ_VICTIM

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 8051, 500, { }, 1, 1, None)


class CPerform(CCustomPerform):
    m_SID = 6159
    m_Name = '流血的'
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
    m_DieDisable = 1
    m_MonsterAfType = MAF_TYPE_FIRE

