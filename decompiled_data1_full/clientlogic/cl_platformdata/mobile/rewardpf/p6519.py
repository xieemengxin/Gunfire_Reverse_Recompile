# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p6519.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p6519.pyc
# Source Generated with Decompyle++
# File: p6519.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import MG_GSCASH, MG_SOURCE_KILLMONSTER, OBJ_ATTACK, WARRIOR_BOSS
from cl_newformula import Func308

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GETMINIGAMETIME, -1, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GETMINIGAMETIME, -1, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GETMINIGAMETIME, -1, 0, 0, 0)


def Action4(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GETMINIGAMETIME, -1, 0, 0, 0)


def Action5(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GETMINIGAMETIME, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
    if cl_evcon.CheckMiniGameSource(oWarrior, oEventCB, MG_SOURCE_KILLMONSTER) and cl_evcon.CheckMiniGameType(oWarrior, oEventCB, MG_GSCASH) and cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_BOSS):
        cl_evact.PassiveChangeMiniGameInfo(oWarrior, oEventCB, 0, 0, (lambda *a: Func308(*a) * 1000 + 0), 0, None, None)


class CPerform(CCustomPerform):
    m_SID = 6519
    m_Name = '土豪首领'
    m_MaxLevel = 5
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3,
        4: Action4,
        5: Action5 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0

