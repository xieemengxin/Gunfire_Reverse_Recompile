# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/daytrialpf/p4673.pyc
# RelativePath: clientlogic/cl_platformdata/pc/daytrialpf/p4673.pyc
# Source Generated with Decompyle++
# File: p4673.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.daytrial import CPerform as CCustomPerform
from cl_commondefines import NWARRIOR_DROP_TREASURE_DEAD, WARRIOR_MONSTER

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DROPDISAPPEAR, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckPickType(oWarrior, oEventCB, NWARRIOR_DROP_TREASURE_DEAD):
        cl_evact.PassiveSetPosToBead(oWarrior, oEventCB)
        cl_evact.EventGetRangeTargetByFightType(oWarrior, oEventCB, 6, WARRIOR_MONSTER, 1, 0, 0, 1, 0, { }, None, None, None, None, None)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1328, 0, { }, 1, 0, None)


class CPerform(CCustomPerform):
    m_SID = 4673
    m_Name = '治愈宝珠'
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

