# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_sceneevent.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_sceneevent.pyc
# Source Generated with Decompyle++
# File: crt_sceneevent.pyc (Python 3.6)

from cl_only import Time2Frame, Functor
from cl_commondefines import SCENE_EVT_SHAPE_SPHERE, SCENE_EVT_SHAPE_RECTANGLE, WARRIOR_HERO
from .mobject import CBaseCartoon

class SceneEventCartoon(CBaseCartoon):
    
    def Trace(cls, oSkill, dCartoon):
        cls.AddSceneEvt(oSkill, dCartoon)

    Trace = classmethod(Trace)
    
    def IsOver(cls, oSkill, dCartoon):
        iOver = 0
        if dCartoon['StartFrame'] + dCartoon['iLiveFrame'] <= oSkill.m_Game.GetFrameNum():
            cls.Trigger(oSkill)
            oSkill.Send(dCartoon['ID'], {
                'Trigger': 1 })
            iOver = 1
        if 'Over' in dCartoon:
            iOver = 1
        if iOver:
            ClearSceneEvt(dCartoon, oSkill)
            oSkill.Send(dCartoon['ID'], {
                'Over': 1 })
            return 1
        return 0

    IsOver = classmethod(IsOver)
    
    def InitTraceServer(cls, oSkill, dCartoon, StartPos, iLivetime, iShape, lstArgs, iFightType, iHitOver, funcCheckTar = None, *args, **kwargs):
        dCartoon['StartPos'] = StartPos
        dCartoon['iLiveFrame'] = Time2Frame(iLivetime)
        dCartoon['iShape'] = iShape
        dCartoon['dEffArgs'] = lstArgs
        dCartoon['iFightType'] = iFightType
        dCartoon['lstInScene'] = []
        dCartoon['iSceneEvtID'] = None
        dCartoon['HitOver'] = iHitOver
        dCartoon['Final'] = dCartoon['StartPos']
        dCartoon['CheckTar'] = funcCheckTar
        dNet = {
            'Start': StartPos,
            'Time': iLivetime }
        oSkill.Send(dCartoon['ID'], dNet)

    InitTraceServer = classmethod(InitTraceServer)
    
    def HitTargetServer(cls, oSkill, dCartoon):
        lstHit = dCartoon.pop('curEnter', [])
        if lstHit:
            iHit = 1
            if dCartoon['HitOver']:
                dCartoon['Over'] = 1
            oSkill.m_Update['LastVLST'] = lstHit
            dNet = {
                'LastVLST': lstHit }
            oSkill.Send(dCartoon['ID'], dNet)
        else:
            iHit = 0
        return iHit

    HitTargetServer = classmethod(HitTargetServer)
    
    def AddSceneEvt(cls, oSkill, dCartoon):
        oAttack = oSkill.GetAttack()
        oGame = oSkill.m_Game
        lstArgs = []
        if not oAttack:
            return None
        if dCartoon['iShape'] == SCENE_EVT_SHAPE_SPHERE:
            lstArgs = [
                dCartoon['StartPos'],
                dCartoon['dEffArgs']['Radius']]
        elif dCartoon['iShape'] == SCENE_EVT_SHAPE_RECTANGLE:
            lstArgs = [
                dCartoon['StartPos'],
                (dCartoon['dEffArgs']['HalfX'], dCartoon['dEffArgs']['HalfY'], dCartoon['dEffArgs']['HalfZ'])]
        oScene = oGame.m_SceneMgr.GetScene(oSkill.m_Base['Scene'])
        enterfunc = Functor(SceneEnterFunc, oSkill, dCartoon)
        leavefunc = Functor(SceneLeaveFunc, oSkill, dCartoon)
        dCartoon['iSceneEvtID'] = oScene.AddSceneEvent(oAttack, enterfunc, leavefunc, dCartoon['iShape'], lstArgs, { })
        oSkill.Call_Out(dCartoon['iLiveFrame'], dCartoon['ID'])
        oSkill.AddEndFunc(Functor(ClearSceneEvt, dCartoon))

    AddSceneEvt = classmethod(AddSceneEvt)


def ClearSceneEvt(dCartoon, oSkill):
    if 'Clear' in dCartoon:
        return None
    oScene = oSkill.m_Game.m_SceneMgr.GetScene(oSkill.m_Base['Scene'])
    if not oScene:
        return None
    oScene.RemoveSceneEvent(dCartoon['iSceneEvtID'])
    dCartoon['Clear'] = 1


def SceneEnterFunc(oSkill, dCartoon, oListener, dMsgInfo):
    iTriggerObj = dMsgInfo['VID']
    obj = oSkill.m_Game.GetObject(iTriggerObj)
    if obj.m_FightType & dCartoon['iFightType'] != dCartoon['iFightType']:
        return None
    if dCartoon['CheckTar']:
        func = dCartoon['CheckTar']
        if not func(oSkill, dCartoon, {
            'VID': iTriggerObj }):
            return None
    dCartoon['lstInScene'].append(iTriggerObj)
    dCartoon['curEnter'] = [
        iTriggerObj]
    oSkill.Update([
        dCartoon['ID']])


def SceneLeaveFunc(oSkill, dCartoon, oListener, dMsgInfo):
    iTriggerObj = dMsgInfo['VID']
    obj = oSkill.m_Game.GetObject(iTriggerObj)
    if not obj:
        return None
    if iTriggerObj in dCartoon['lstInScene']:
        dCartoon['lstInScene'].remove(iTriggerObj)

