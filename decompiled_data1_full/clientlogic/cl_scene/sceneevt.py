# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_scene/sceneevt.pyc
# RelativePath: clientlogic/cl_scene/sceneevt.pyc
# Source Generated with Decompyle++
# File: sceneevt.pyc (Python 3.6)

from cl_commondefines import WARRIOR_HERO, SCENE_EVT_LEAVE
SCENEEVT_DYNAMIC_START = 65537
SCENEEVT_TYPE_STATIC = 1
SCENEEVT_TYPE_AREA = 2
SCENEEVT_TYPE_DYNAMIC = 4

def OnStatic(oScene, obj, iEventID, iLeave):
    oScene.m_SceneEvtMgr.OnTriggerStatic(iEventID, obj, iLeave)


def OnArea(oScene, obj, iEventID, iLeave):
    if not obj.m_FightType & WARRIOR_HERO:
        return None
    if iLeave or iEventID in obj.m_Area:
        obj.m_Area.pop(iEventID)
    else:
        obj.m_Area[iEventID] = 1

SCENEEVT_TYPE_CALLBACK = {
    SCENEEVT_TYPE_AREA: OnArea,
    SCENEEVT_TYPE_STATIC: OnStatic }

def OnSceneEvt2(iScene, iEventID, iEvtType, iTriType, obj):
    oScene = obj.m_Game.m_SceneMgr.GetScene(iScene)
    if not oScene:
        return None
    func = SCENEEVT_TYPE_CALLBACK.get(iEvtType)
    if not func:
        return None
    iLeave = 1 if iTriType == SCENE_EVT_LEAVE else 0
    func(oScene, obj, iEventID, iLeave)

