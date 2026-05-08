# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p2418.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p2418.pyc
# Source Generated with Decompyle++
# File: p2418.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import DAM_USE_HP, OBJ_VICTIM
from cl_newformula import Func331

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1, 0, 0, 5)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1, 0, 0, 5)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1, 0, 0, 5)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 32326) == 0:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if cl_evcon.CheckDeadlyPredictDam(oWarrior, oEventCB, None):
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
            cl_evact.EventChangeDefValue(oWarrior, oEventCB, 100, DAM_USE_HP, None)
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32325, (lambda *a: Func331(*a, **{
'sid': 2418 }) * 100 + 200), { }, 0, None, None)


class CPerform(CCustomPerform):
    m_SID = 2418
    m_Name = '不死化身'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 2
    m_IsRareTalent = 0
    m_Career = 105

