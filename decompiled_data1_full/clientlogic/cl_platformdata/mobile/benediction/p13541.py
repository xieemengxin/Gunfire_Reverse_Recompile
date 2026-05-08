# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/benediction/p13541.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/benediction/p13541.pyc
# Source Generated with Decompyle++
# File: p13541.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJECT_SERVANT, OBJ_VICTIM, PF_TYPE_THROW
from cl_newformula import Func303

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33922, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenServantMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 2)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_THROW, 0) and cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'p13568', 0) == 0:
        cl_evact.EventCBSetCollectInfo(oWarrior, oEventCB, 'p13568', 1, 0)
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'ThrowHitNum', 1)
        if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'ThrowHitNum') >= 15:
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'ThrowHitNum', 0)
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
            cl_evact.PassiveCBUsePerform2EvtTarget(oWarrior, oEventCB, 8023, 1, {
                'Radius': (lambda *a: Func303(*a, **{
'sAttr': 'Radius' }) * 2) }, OBJECT_SERVANT)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 7151, 1, 0):
        cl_evact.EventCBClearCollectInfo(oWarrior, oEventCB, 'p13568', 0)


class CPerform(CCustomPerform):
    m_SID = 13541
    m_Name = '火力覆盖'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Career = 114

