# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st1435.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st1435.pyc
# Source Generated with Decompyle++
# File: st1435.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_notify
from cl_commondefines import CHASTATUS_FAILED
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_SPECIAL, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    CustomAction(oTarget, oLifeCycle, {
        'Action': 'Init' })
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, -1, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    CustomAction(oTarget, oEventCB.GetCBLifeCycle(), {
        'Action': 'ReEnter' })


class CState(cl_state.CState):
    m_SID = 1435
    m_Name = '#NT#守护NPC重提示'
    m_Type = STATE_CLS_SPECIAL
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 0
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 1
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        0: CallBack0 }


def CustomAction(oTarget, oLifeCycle, dInfo):
    oState = oLifeCycle.GetObject()
    oGame = oTarget.m_Game
    if not oState:
        return None
    if 'DefendNpc' not in oState.m_StateInfo:
        return None
    oScene = oGame.m_SceneMgr.GetScene(oTarget.m_Scene)
    if not oScene:
        return None
    dNpc = oState.m_StateInfo['DefendNpc']
    oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
    oLevelNode = oLevelCtrl.GetLevelNode(oScene.m_Level)
    iNodeId = id(oLevelNode)
    if dInfo['Action'] == 'Init' and iNodeId != dNpc['LevelNodeId']:
        SendNotify(oTarget)
    elif dInfo['Action'] == 'ReEnter' and iNodeId == dNpc['LevelNodeId']:
        SendNotify(oTarget)


def SendNotify(oTarget):
    cl_notify.SendCommonNotify(oTarget.m_Game, {
        oTarget.m_PlayerID: 1 }, 9286, None)

