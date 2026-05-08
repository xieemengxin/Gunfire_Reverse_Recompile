# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p2314.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p2314.pyc
# Source Generated with Decompyle++
# File: p2314.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_VICTIM

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32266, 0, { }, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32266, 0, { }, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 2, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32266, 0, { }, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1412, 1, None) or cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1413, 1, None):
        CustomAction(oWarrior, oEventCB, { })
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32264, 0, { }, 0, 0, None)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1412, 1, None) or cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1413, 1, None):
        CustomAction(oWarrior, oEventCB, { })
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32264, 0, { }, 0, 0, None)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1412, 1, None) or cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1413, 1, None):
        CustomAction(oWarrior, oEventCB, { })
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32264, 0, { }, 0, 0, None)


class CPerform(CCustomPerform):
    m_SID = 2314
    m_Name = '电索连环'
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
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 3
    m_IsRareTalent = 0
    m_Career = 104


def CustomAction(oWarrior, oEventCB, dInfo):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    dMonster = oWarrior.Query('dMonster', { })
    oGame = oWarrior.m_Game
    iPFLV = dEventInfo['PFLV']
    oSkill = dMsgInfo['Skill']
    iActNum = oSkill.m_Base['ActNum']
    if iActNum not in dMonster.keys():
        if iPFLV < 3:
            for lstMonster in dMonster.values():
                for iTarget in lstMonster:
                    oTarget = oGame.GetObject(iTarget)
                    if not oTarget:
                        continue
                    lstState = oTarget.m_State.GetItems(32264)
                    for oTarState in lstState:
                        oTarget.m_State.RemoveItem(oTarState.m_ID)
                    
                
            
            dMonster = { }
        lstMonster = []
        dMonster[iActNum] = lstMonster
        dMonster[iActNum].append(dMsgInfo['CurVID'])
    else:
        dMonster[iActNum].append(dMsgInfo['CurVID'])
    oWarrior.Set('dMonster', dMonster)

