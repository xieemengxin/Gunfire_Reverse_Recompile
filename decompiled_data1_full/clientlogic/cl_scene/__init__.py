# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_scene/__init__.pyc
# RelativePath: clientlogic/cl_scene/__init__.pyc
# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.6)

from cl_commondefines import WARRIOR_HERO
from cl_object.logging import SceneLog
import cl_msgcenter
import cl_duonet.dn_cl_scene as scenenet

def GS2CMapSceneEnter(oTarget, iScene, tPos, tFace):
    if not oTarget.m_FightType & WARRIOR_HERO:
        return None
    oGame = oTarget.m_Game
    oWarMgr = oGame.m_WarMgr
    oScene = oGame.m_SceneMgr.GetScene(iScene)
    dPreLoadData = oScene.m_ScenePreLoad.GetPreLoadData()
    iLevel = oScene.m_Level
    oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
    oLevelConfData = oLevelCtrl.m_LevelConfData
    oLevelNode = oLevelCtrl.GetLevelNode(iLevel)
    dLineStore = oLevelConfData.GetLevelConfig(iLevel, 'arealine')
    dLineInfo = oLevelNode.GetLevelLineInfo()
    lstCategory = oLevelNode.GetLevelMonsterCategory()
    (dx, dy, dz) = tFace
    dData = {
        'pid': oTarget.m_PlayerID,
        'oGame': oGame,
        'iScene': iScene,
        'iLevel': iLevel,
        'iMap': oScene.Map(),
        'iWarNo': oWarMgr.m_SID,
        'pos': tPos,
        'dx': dx,
        'dy': dy,
        'dz': dz,
        'LevelType': oLevelNode.m_LevelType,
        'GameType': oLevelNode.m_GameType,
        'MaxLevel': oLevelCtrl.GetMaxLevel(),
        'CurLevel': oLevelCtrl.m_LevelNum,
        'CurLayer': oLevelCtrl.m_LayerNum,
        'CurBaseLayer': oWarMgr.GetBaseLayer(oLevelCtrl.m_LayerNum),
        'lstArea': list(dLineStore.keys()),
        'lstLine': list(dLineInfo.values()),
        'MaxRoom': len(oLevelNode.m_RoomList),
        'CurRoomPos': oLevelNode.m_CurRoomPos,
        'lstWeaponPreLoad': dPreLoadData['Weapon'],
        'lstRelicPreLoad': dPreLoadData['Relic'],
        'lstMonsterCategory': lstCategory,
        'NewScene': oTarget.ValidEnterNewScene(iScene) }
    scenenet.DN_GS2CMapSceneEnter(dData)


def GS2CMapGoto(oTarget, tPos):
    netdata = {
        'iTarget': oTarget.m_ID,
        'oGame': oTarget.m_Game,
        'iScene': oTarget.m_Scene,
        'pos': tPos }
    scenenet.DN_GS2CMapGoto(netdata)


def GS2CMapDel(oTarget, dPlayer = None):
    if not dPlayer:
        oScene = oTarget.m_Game.m_SceneMgr.GetScene(oTarget.m_Scene)
        if not oScene:
            return None
        dPlayer = oScene.GetPlayers()
        if not dPlayer:
            return None
    dData = {
        'oGame': oTarget.m_Game,
        'iTarget': oTarget.m_ID,
        'iType': oTarget.m_FightType,
        'dPlayer': dPlayer }
    scenenet.DN_GS2CMapDel(dData)


def GS2CMapDelByDate(dData):
    scenenet.DN_GS2CMapDel(dData)


def GS2CMapTriggerGate(oTarget, iAction, iMask = 0):
    dData = {
        'iTarget': oTarget.m_ID,
        'oGame': oTarget.m_Game,
        'iScene': oTarget.m_Scene,
        'iAction': iAction,
        'iMask': iMask }
    scenenet.DN_GS2CMapTriggerGate(dData)


def GS2CMapTriggerUpStone(oTarget, tPos, fSpeed):
    dData = {
        'iTarget': oTarget.m_ID,
        'oGame': oTarget.m_Game,
        'iScene': oTarget.m_Scene,
        'tPos': tPos,
        'fSpeed': fSpeed }
    scenenet.DN_GS2CMapTriggerUpStone(dData)


def C2GSLoadMapOK(oHero, iScene):
    oGame = oHero.m_Game
    pid = oHero.m_PlayerID
    SceneLog.Debug('%s loadmapok pid:%s curscene:%s tarscene:%s' % (oGame.m_ID, pid, oHero.m_Scene, iScene))
    if oHero.m_Scene != iScene:
        return None
    oScene = oGame.m_SceneMgr.GetScene(oHero.m_Scene)
    if not oScene:
        return None
    oGame.S2CFrameStep(oGame.GetFrameNum(), {
        pid: 1 })
    oGame.m_LinkMgr.OnReady(pid)
    oScene.AddPlayer(pid, oHero.m_ID)
    oHero.SendScenePacket()
    oHero.m_State.RefreshAllShowTime()
    cl_msgcenter.SendCoreMsg(cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, oHero, {
        'pid': pid,
        'Hero': oHero.m_ID,
        'LevelID': oScene.m_Level,
        'Scene': iScene })
    oGame.m_SkillMgr.OnPlayerMapLoadOK(pid, iScene)

