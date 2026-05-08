# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_evact/ev_scene.pyc
# RelativePath: clientlogic/cl_evact/ev_scene.pyc
# Source Generated with Decompyle++
# File: ev_scene.pyc (Python 3.6)

import cl_snetwar

def PlayerCameraBehavior(oListener, dInfo, iBehavior):
    oWarrior = oListener.m_Game.GetObject(dInfo['VID'])
    if not oWarrior:
        return None
    lstPlayer = [
        oWarrior.m_PlayerID]
    cl_snetwar.GS2CTriggerBehavior(oListener.m_Game, dInfo['VID'], iBehavior, lstPlayer)


def UnBindSelf(oListener, dInfo):
    oScene = oListener.m_Game.m_SceneMgr.GetScene(dInfo['Scene'])
    if oScene:
        oScene.UnBindSceneEvent(dInfo['Event'])


def CheckMonsterGroupAlive(oLevelCtrl, dInfo, iGroup):
    return True


def CheckTriggerType(oLevelCtrl, dInfo, iType):
    oTarget = oLevelCtrl.m_Game.GetObject(dInfo['VID'])
    if oTarget.m_FightType & iType == iType:
        return True
    return False

