# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4351.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4351.pyc
# Source Generated with Decompyle++
# File: p4351.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import OBJ_ATTACK

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1972)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REVTOTALDAM, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
    if cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1) == 0 and cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 60) and cl_evcon.CheckTargetDist(oWarrior, oEventCB, 10, 0, 0) == 0:
        if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'Reincarnation9') == 1:
            cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 300)
            cl_evact.EventCBSelfStop(oWarrior, oEventCB)
            cl_action.CommonHaltPointPerform(oWarrior, oEventCB.GetCBLifeCycle(), 22852)
            cl_evact.EventCBUsePerformEvtTarget(oWarrior, oEventCB, 22853, { }, None)
        else:
            cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 300)
            cl_evact.EventCBSelfStop(oWarrior, oEventCB)
            cl_action.CommonHaltPointPerform(oWarrior, oEventCB.GetCBLifeCycle(), 22852)
            cl_evact.EventCBUsePerformEvtTarget(oWarrior, oEventCB, 1972, { }, None)


class CPerform(CCustomPerform):
    m_SID = 4351
    m_Name = '虚空僧被动'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = {
        'Reincarnation9': 0 }
    m_DieDisable = 0

