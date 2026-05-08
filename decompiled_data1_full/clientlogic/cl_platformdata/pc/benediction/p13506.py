# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/benediction/p13506.pyc
# RelativePath: clientlogic/cl_platformdata/pc/benediction/p13506.pyc
# Source Generated with Decompyle++
# File: p13506.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK, OBJ_VICTIM

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonSetImmuneElementRestraint(oWarrior, oLifeCycle)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.EventCBGetTargetAbnormalStateNum(oWarrior, oEventCB) == 2:
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, 6000, 0, '')
    if cl_evcon.EventCBGetTargetAbnormalStateNum(oWarrior, oEventCB) == 3:
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, 9000, 0, '')


class CPerform(CCustomPerform):
    m_SID = 13506
    m_Name = '元素大师'
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
    m_Career = 102

