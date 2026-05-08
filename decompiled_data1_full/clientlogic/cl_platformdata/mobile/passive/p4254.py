# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4254.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4254.pyc
# Source Generated with Decompyle++
# File: p4254.pyc (Python 3.6)

from cl_only import PY_FLAG_DEAD
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_object.logging import WarobjLog
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import OBJ_SELF

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DIE_BEFORE, -1, 0, 0, 99)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonDoneEvent(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DIE_BEFORE, -1)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if not cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 8015, 0, 0, None):
        cl_evact.EventChangeHP(oWarrior, oEventCB, 100)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 8006, 0, { }, 1, -1, None)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 8015, 0, { }, 1, -1, None)
    CustomAction(oWarrior, oEventCB.GetCBLifeCycle(), { })


class CPerform(CCustomPerform):
    m_SID = 4254
    m_Name = '同生共死'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = {
        1: DisableAction1 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0


def CustomAction(oWarrior, oLifeCycle, dInfo):
    oGame = oWarrior.m_Game
    oScene = oGame.m_SceneMgr.GetScene(oWarrior.m_Scene)
    bDie = True
    lstMonster = []
    for iMonster in oScene.GetObjectsByType('Monster'):
        if iMonster == oWarrior.m_ID:
            continue
        oMonster = oGame.GetObject(iMonster, PY_FLAG_DEAD)
        if not oMonster:
            continue
        if oMonster.GetPerform(4254):
            oState = oMonster.m_State.GetItemBySID(8006)
            if not oState:
                bDie = False
                break
            lstMonster.append(oMonster)
    
    if bDie:
        lstMonster.append(oWarrior)
        for oMonster in lstMonster:
            oMonster.m_Perform.RemovePerform(oMonster, CPerform.m_SID)
        

