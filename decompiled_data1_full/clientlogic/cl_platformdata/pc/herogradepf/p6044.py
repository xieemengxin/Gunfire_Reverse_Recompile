# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/herogradepf/p6044.pyc
# RelativePath: clientlogic/cl_platformdata/pc/herogradepf/p6044.pyc
# Source Generated with Decompyle++
# File: p6044.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CHeroGradePassive as CCustomPerform
from cl_commondefines import PF_SUBMSG_THROW

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_THROW, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1412, 1, None) or cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1413, 1, None):
        cl_evact.EventGetTargetBySkillVlst(oWarrior, oEventCB)
        if cl_evcon.GetTargetNum(oWarrior, oEventCB) == 1:
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32606, 0, { }, 1, 1, None)


class CPerform(CCustomPerform):
    m_SID = 6044
    m_Name = '游侠【技能】4'
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

