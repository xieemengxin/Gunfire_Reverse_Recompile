# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/benediction/p13558.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/benediction/p13558.pyc
# Source Generated with Decompyle++
# File: p13558.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_PERFORM, DAM_TYPE_TRUE, DAM_USE_ALL, MONSTER_PART_FLAW, OBJ_VICTIM, WARRIOR_MONSTER
from cl_newformula import Func369, Func423, Func684

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PFNODEKILL, -1, 3, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if not cl_evcon.CheckHitPart(oWarrior, oEventCB, MONSTER_PART_FLAW):
        cl_evact.EventCBHitUnbalance(oWarrior, oEventCB, 1500)
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 1854, 0, 0, 0):
        cl_evact.EventCBAddTargetListenerCustomData(oWarrior, oEventCB, '13558Dam', (lambda *a: Func369(*a)))
        cl_evact.EventCBListenTargetMsgCallBack(oWarrior, oEventCB, cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, -1, 1, None)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckFromPointState(oWarrior, oEventCB, 1854):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.EventGetRangeTargetByFightType(oWarrior, oEventCB, 10, WARRIOR_MONSTER, 0, 0, 0, 0, 0, { }, 0, None, None, None, None)
        cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: Func684(*a, **{
'sAttr': '13558Dam' }) * 0.5), DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 1, 1, 0, 0, 0, 0, 0, 0, None, None)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.EventCBClearTargetListenerCustomData(oWarrior, oEventCB, '13558Dam')


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        1324: 1,
        1328: 1 }, 1, 0):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.EventCBAddTargetListenerCustomData(oWarrior, oEventCB, '13558Dam', (lambda *a: Func423(*a)))
        cl_evact.EventCBListenTargetMsgCallBack(oWarrior, oEventCB, cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, -1, 1, None)


class CPerform(CCustomPerform):
    m_SID = 13558
    m_Name = '#NT#处决第四条灵佑'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Career = 116

