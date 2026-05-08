# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/relic/p5796.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/relic/p5796.pyc
# Source Generated with Decompyle++
# File: p5796.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import DAM_MASK_CLASS, DAM_MASK_ELEMENT, OBJ_SELF, QUALITY_TYPE_LOW, RELIC_TYPE_NORMAL, WARRIOR_BUILD
from cl_newformula import Func213

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEDEBUFF, -1, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, None, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADDSTATE, -1, 3, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEDEBUFF, -1, 4, 0, 0)
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'MoveSpeed', 4000, 0, -1)
    cl_action.CommonModifyDamResistance(oWarrior, oLifeCycle, 1000, DAM_MASK_CLASS, DAM_MASK_ELEMENT, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    if not cl_evcon.CheckTargetAddState(oWarrior, oEventCB, 20027) and cl_evcon.CheckVictimFightType(oWarrior, oEventCB, WARRIOR_BUILD):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 20027, (lambda *a: Func213(*a) * 100 / 100 + 0), { }, 1, None, None)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 20027, 1, None, None):
        cl_evact.PassiveAddFollowState(oWarrior, oEventCB, 1200, 20027, { }, 1, None, None)
        cl_evact.PassiveAddFollowState(oWarrior, oEventCB, 1237, 20027, { }, 1, 0, 0)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckTargetAddState(oWarrior, oEventCB, 20027):
        cl_evact.PassiveAddFollowState(oWarrior, oEventCB, 1200, 20027, { }, 1, None, None)
        cl_evact.PassiveAddFollowState(oWarrior, oEventCB, 1237, 20027, { }, 1, 0, 0)


def DoCallBackAction4(oEventCB, oWarrior):
    if not cl_evcon.CheckTargetAddState(oWarrior, oEventCB, 20027) and cl_evcon.CheckVictimFightType(oWarrior, oEventCB, WARRIOR_BUILD):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 20027, (lambda *a: Func213(*a) * 100 / 100 + 0), { }, 1, None, None)


def DoCallBackAction5(oEventCB, oWarrior):
    cl_action.CommonModifyDamResistance(oWarrior, oEventCB.GetCBLifeCycle(), 1000, DAM_MASK_CLASS, DAM_MASK_ELEMENT, 1)


class CPerform(CCustomPerform):
    m_SID = 5796
    m_Name = '腐蚀狂热'
    m_MaxLevel = 2
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4,
        5: DoCallBackAction5 }
    m_BaseArgData = { }
    m_DieDisable = 1
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5523
    m_ValidRemove = 1
    m_BasePrice = 40
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_LOW

