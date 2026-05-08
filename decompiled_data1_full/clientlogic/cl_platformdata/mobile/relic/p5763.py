# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/relic/p5763.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/relic/p5763.pyc
# Source Generated with Decompyle++
# File: p5763.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import MG_BULLET, MG_CASH, MG_SOURCE_KILLMONSTER, MG_TRIGGER, OBJ_ATTACK, QUALITY_TYPE_NORMAL, RELIC_TYPE_NORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GETMINIGAMETIME, -1, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GETMINIGAMETIME, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
    if cl_evcon.CheckMiniGameSource(oWarrior, oEventCB, MG_SOURCE_KILLMONSTER) and cl_evcon.CheckTargetDist(oWarrior, oEventCB, 7, None, None):
        if cl_evcon.CheckMiniGameType(oWarrior, oEventCB, MG_TRIGGER) or cl_evcon.CheckMiniGameType(oWarrior, oEventCB, MG_BULLET) or cl_evcon.CheckMiniGameType(oWarrior, oEventCB, MG_CASH):
            cl_evact.PassiveChangeMiniGameInfo(oWarrior, oEventCB, 0, 0, 10000, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
    if cl_evcon.CheckMiniGameSource(oWarrior, oEventCB, MG_SOURCE_KILLMONSTER) and cl_evcon.CheckTargetDist(oWarrior, oEventCB, 7, None, None):
        if cl_evcon.CheckMiniGameType(oWarrior, oEventCB, MG_TRIGGER) or cl_evcon.CheckMiniGameType(oWarrior, oEventCB, MG_BULLET) or cl_evcon.CheckMiniGameType(oWarrior, oEventCB, MG_CASH):
            cl_evact.PassiveChangeMiniGameInfo(oWarrior, oEventCB, 0, 0, 20000, 0)
        else:
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
            if cl_evcon.CheckMiniGameSource(oWarrior, oEventCB, MG_SOURCE_KILLMONSTER) and cl_evcon.CheckTargetDist(oWarrior, oEventCB, 15, 0, None):
                if cl_evcon.CheckMiniGameType(oWarrior, oEventCB, MG_TRIGGER) or cl_evcon.CheckMiniGameType(oWarrior, oEventCB, MG_BULLET) or cl_evcon.CheckMiniGameType(oWarrior, oEventCB, MG_CASH):
                    cl_evact.PassiveChangeMiniGameInfo(oWarrior, oEventCB, 0, 0, 10000, 0)


class CPerform(CCustomPerform):
    m_SID = 5763
    m_Name = '淘金工人'
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
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5524
    m_ValidRemove = 1
    m_BasePrice = 60
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_NORMAL

