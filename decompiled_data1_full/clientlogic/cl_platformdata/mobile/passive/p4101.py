# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4101.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4101.pyc
# Source Generated with Decompyle++
# File: p4101.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import MG_BULLET, MG_CASH, MG_GSCASH, MG_SOURCE_KILLMONSTER, OBJ_ATTACK, WARRIOR_NORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GETMINIGAMETIME, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
    if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_NORMAL) and cl_evcon.CheckMiniGameSource(oWarrior, oEventCB, MG_SOURCE_KILLMONSTER):
        if cl_evcon.CheckMiniGameType(oWarrior, oEventCB, MG_CASH):
            cl_evact.PassiveChangeMiniGameInfo(oWarrior, oEventCB, -10000, 0, -10000, 0, None, None)
        if cl_evcon.CheckMiniGameType(oWarrior, oEventCB, MG_BULLET):
            cl_evact.PassiveChangeMiniGameInfo(oWarrior, oEventCB, 0, 10000, 0, 1, None, None)
        if cl_evcon.CheckMiniGameType(oWarrior, oEventCB, MG_GSCASH):
            cl_evact.PassiveChangeMiniGameInfo(oWarrior, oEventCB, -10000, 0, -10000, 0, None, None)


class CPerform(CCustomPerform):
    m_SID = 4101
    m_Name = '二幕boss关修改掉落'
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

