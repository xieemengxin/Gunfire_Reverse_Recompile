# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4273.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4273.pyc
# Source Generated with Decompyle++
# File: p4273.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import NWARRIOR_DROP_KEYITEM

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenWarMgrMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DROPDISAPPEAR, -1, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckPickType(oWarrior, oEventCB, NWARRIOR_DROP_KEYITEM):
        cl_evact.EventGetTargetByLevelBoss(oWarrior, oEventCB)
        cl_evact.PassiveCBUsePerform(oWarrior, oEventCB, 39067, 0, { })
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 8020, 0, { }, -1)


class CPerform(CCustomPerform):
    m_SID = 4273
    m_Name = '夜姬丸炮弹自动爆炸'
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

