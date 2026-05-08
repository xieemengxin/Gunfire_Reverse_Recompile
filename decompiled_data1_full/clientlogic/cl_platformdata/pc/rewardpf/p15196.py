# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p15196.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p15196.pyc
# Source Generated with Decompyle++
# File: p15196.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import OBJ_VICTIM, PF_SUBMSG_CAREERPF, WARRIOR_MONSTER
from cl_newformula import Func744

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSE_ADDIMMOBILIZE, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.EventCBCheckAddImmobilize(oWarrior, oEventCB):
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33505, 300, { }, 0, 1, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1310, 1, 0) and cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1) == 0:
        cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, (lambda *a: 800 / (10000 + Func744(*a, **{
'iType': 2 })) / 10000))
        cl_evact.EventGetRangeTargetByFightType(oWarrior, oEventCB, 20, WARRIOR_MONSTER, 1, 0, 5, 0, 0, { }, 0, None, None, None, None)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33504, 200, { }, 0, 1, 0)


class CPerform(CCustomPerform):
    m_SID = 15196
    m_Name = '平波缓近'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0

