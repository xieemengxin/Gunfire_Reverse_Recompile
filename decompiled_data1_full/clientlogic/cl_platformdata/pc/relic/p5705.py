# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/relic/p5705.pyc
# RelativePath: clientlogic/cl_platformdata/pc/relic/p5705.pyc
# Source Generated with Decompyle++
# File: p5705.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import DAM_USE_HP, OBJ_VICTIM, QUALITY_TYPE_NORMAL, RELIC_TYPE_NORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1, 0, 0, 6)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, -1, 8, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1, 4, 0, 6)


def DoCallBackAction0(oEventCB, oWarrior):
    if not cl_evcon.CheckHasState(oWarrior, oEventCB, 32480) or cl_evcon.CheckHasState(oWarrior, oEventCB, 1079) or cl_evcon.CheckHasState(oWarrior, oEventCB, 33711):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if cl_evcon.CheckDeadlyPredictDam(oWarrior, oEventCB, None):
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
            cl_evact.EventChangeDefValue(oWarrior, oEventCB, 100, DAM_USE_HP, None)
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1079, 500, { }, 0, None, None)


def DoCallBackAction4(oEventCB, oWarrior):
    if not cl_evcon.CheckHasState(oWarrior, oEventCB, 1498) or cl_evcon.CheckHasState(oWarrior, oEventCB, 32480) or cl_evcon.CheckHasState(oWarrior, oEventCB, 33711):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if cl_evcon.CheckDeadlyPredictDam(oWarrior, oEventCB, None):
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
            cl_evact.EventChangeDefValue(oWarrior, oEventCB, 100, DAM_USE_HP, None)
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1081, 504, { }, 0, None, None)
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1498, 12000, { }, 0, 0, 0)


def DoCallBackAction8(oEventCB, oWarrior):
    if cl_evcon.CheckTargetAddState(oWarrior, oEventCB, 1079):
        cl_evact.EventCBRemoveRelic(oWarrior, oEventCB, 5705, 1)


class CPerform(CCustomPerform):
    m_SID = 5705
    m_Name = '救命稻草'
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
        4: DoCallBackAction4,
        8: DoCallBackAction8 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5524
    m_ValidRemove = 0
    m_BasePrice = 100
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_NORMAL

