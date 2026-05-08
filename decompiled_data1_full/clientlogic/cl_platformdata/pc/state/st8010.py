# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st8010.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st8010.pyc
# Source Generated with Decompyle++
# File: st8010.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_SPECIAL, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    CustomAction(oTarget, oLifeCycle, {
        'Type': 'Init' })
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DIE, -1, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    CustomAction(oTarget, oEventCB.GetCBLifeCycle(), {
        'Type': 'Die' })


class CState(cl_state.CState):
    m_SID = 8010
    m_Name = '#NT#巨型召唤怪解锁房间目标'
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
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        0: CallBack0 }


def CustomAction(oTarget, oLifeCycle, dInfo):
    oGame = oTarget.m_Game
    oScene = oGame.m_SceneMgr.GetScene(oTarget.m_Scene)
    oState = oLifeCycle.GetObject()
    if not oScene:
        return None
    sKey = 'SceneExtMonster%d' % oState.m_SID
    iMonster = oTarget.m_ID
    if dInfo['Type'] == 'Init':
        setMonster = oScene.m_CustomData.setdefault(sKey, set())
        setMonster.add(iMonster)
    elif dInfo['Type'] == 'Die':
        oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
        setMonster = oScene.m_CustomData.setdefault(sKey, set())
        if iMonster in setMonster:
            setMonster.remove(iMonster)
        if not setMonster:
            iLevel = oScene.m_Level
            oLevelNode = oLevelCtrl.GetLevelNode(iLevel)
            oLevelNode.UnlockRoom(oLevelNode.m_CurRoomPos, 'LargeSummonMonster')

